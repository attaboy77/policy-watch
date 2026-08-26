# -*- coding: utf-8 -*-
"""구글 뉴스 RSS 수집기.

`_utils.build_google_query()` / `_utils.google_news_rss_url()`을 사용해
(필수 OR ...) AND (조합 OR ...) NOT(노이즈...) 완전 불리언 쿼리로 수집한다.
"""
from __future__ import annotations

import time
from datetime import date

import feedparser

from . import _http
from ._config import CATEGORIES, COLLECT_WINDOW_DAYS
from ._utils import (
    google_news_rss_url,
    keyword_score,
    matched_keywords,
    is_noise_l3,
    make_id,
    trust_of,
)

SLEEP_BETWEEN_REQUESTS = 0.5


def _parse_published(entry) -> date | None:
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None)
        if t:
            return date(t.tm_year, t.tm_mon, t.tm_mday)
    return None


def _entry_source_hint(entry) -> str:
    """실제 언론사 도메인 판별용 힌트.

    구글 뉴스 RSS의 `link`는 news.google.com 리다이렉트 URL이라 신뢰도 판정에 못 쓴다.
    `<source url="...">` 필드(있으면)가 실제 퍼블리셔 도메인이라 이를 우선한다.
    """
    src = getattr(entry, "source", None)
    href = getattr(src, "href", None) if src is not None else None
    return href or getattr(entry, "link", "") or ""


def fetch_category(cat_key: str, days: int = COLLECT_WINDOW_DAYS, *,
                    filter_noise: bool = True) -> list[dict]:
    """구글 뉴스 RSS에서 카테고리 1개 분량을 수집해 표준 raw item 리스트로 반환한다.

    실패 시 예외를 삼키지 않고 그대로 올린다 — 소스 단위 격리는 호출부(fetch_all/main)가 담당.
    `filter_noise=False`면 노이즈 항목도 `is_noise=True`로 표시된 채 포함해 반환한다
    (수집 검증/리포팅용).
    """
    url = google_news_rss_url(cat_key, days=days)
    resp = _http.get(url)
    feed = feedparser.parse(resp.content)

    items: list[dict] = []
    for entry in feed.entries:
        title = getattr(entry, "title", "").strip()
        link = getattr(entry, "link", "") or ""
        if not title or not link:
            continue
        source_hint = _entry_source_hint(entry)
        tier, trust_score, source_name = trust_of(source_hint)
        noise = is_noise_l3(title, tier=tier, category=cat_key)
        items.append({
            "id": make_id(link),
            "category": cat_key,
            "title": title,
            "url": link,
            "published": _parse_published(entry),
            "source_name": source_name,
            "source_domain": source_hint,
            "trust_tier": tier,
            "trust_score": trust_score,
            "keyword_score": keyword_score(title, cat_key),
            "matched_keywords": matched_keywords(title, cat_key),
            "is_noise": noise,
        })

    if filter_noise:
        return [it for it in items if not it["is_noise"]]
    return items


def fetch_all(days: int = COLLECT_WINDOW_DAYS) -> dict[str, list[dict]]:
    """카테고리 전체 수집. 카테고리 하나가 실패해도 나머지는 계속 진행한다."""
    results: dict[str, list[dict]] = {}
    for i, cat_key in enumerate(CATEGORIES):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            results[cat_key] = fetch_category(cat_key, days=days)
        except Exception as exc:  # noqa: BLE001 - 소스 단위 격리(SPEC §9-4)
            print(f"[google_news] {cat_key} 수집 실패: {exc}")
            results[cat_key] = []
    return results


if __name__ == "__main__":
    print("=== Google News RSS 수집 결과 (카테고리별) ===")
    total_kept = total_noise = 0
    for i, cat_key in enumerate(CATEGORIES):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        label = CATEGORIES[cat_key]["label"]
        try:
            raw = fetch_category(cat_key, filter_noise=False)
        except Exception as exc:  # noqa: BLE001
            print(f"  {label:8s} ({cat_key:6s}): 수집 실패 - {exc}")
            continue
        noisy = sum(1 for it in raw if it["is_noise"])
        kept = [it for it in raw if not it["is_noise"]]
        total_kept += len(kept)
        total_noise += noisy
        print(f"  {label:8s} ({cat_key:6s}): 원본 {len(raw):3d}건 → 노이즈 {noisy}건 제거 → 유지 {len(kept):3d}건")
        for it in kept[:3]:
            print(f"      · [{it['trust_tier']}] {it['source_name']:12s} | {it['title'][:50]}")
    print(f"  합계 유지: {total_kept}건 (노이즈 {total_noise}건 제거됨)")
