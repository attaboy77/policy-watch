# -*- coding: utf-8 -*-
"""네이버 뉴스 검색 API 수집기.

주의: 네이버 API는 (A OR B) AND (C OR D) 복합 불리언 쿼리를 지원하지 않는다.
`_config.CATEGORIES[*].naver_queries` 단순 질의를 순회 + `_utils.match_loose()` 사후 필터로 구현한다.

시크릿(`NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET`)이 없으면 이 소스만 건너뛰고
나머지 소스는 정상 수집되도록 graceful degradation 한다(SPEC §1).
"""
from __future__ import annotations

import os
import re
import time
from datetime import date, timedelta
from email.utils import parsedate_to_datetime

from . import _http
from ._config import CATEGORIES, COLLECT_WINDOW_DAYS
from ._utils import (
    build_naver_queries,
    naver_news_api_url,
    match_loose,
    keyword_score,
    matched_keywords,
    is_noise,
    make_id,
    trust_of,
)

SLEEP_BETWEEN_REQUESTS = 0.5
_TAG_RE = re.compile(r"<[^>]+>")
_ENTITY_MAP = {"&quot;": '"', "&amp;": "&", "&lt;": "<", "&gt;": ">", "&#39;": "'"}


class NaverCredentialsMissing(RuntimeError):
    """NAVER_CLIENT_ID / NAVER_CLIENT_SECRET 환경변수가 없을 때 발생시킨다."""


def _strip_html(s: str) -> str:
    """네이버 API가 제목/설명에 심는 <b> 하이라이트 태그와 HTML 엔티티를 제거한다."""
    out = _TAG_RE.sub("", s or "")
    for entity, ch in _ENTITY_MAP.items():
        out = out.replace(entity, ch)
    return out


def _parse_pubdate(s: str) -> date | None:
    try:
        return parsedate_to_datetime(s).date()
    except (TypeError, ValueError):
        return None


def _auth_headers() -> dict:
    client_id = os.environ.get("NAVER_CLIENT_ID")
    client_secret = os.environ.get("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise NaverCredentialsMissing(
            "NAVER_CLIENT_ID/NAVER_CLIENT_SECRET 환경변수가 설정되지 않았습니다."
        )
    return {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}


def fetch_category(cat_key: str, days: int = COLLECT_WINDOW_DAYS, *,
                    filter_noise: bool = True) -> list[dict]:
    """네이버 뉴스 API에서 카테고리 1개 분량을 수집해 표준 raw item 리스트로 반환한다.

    자격 증명이 없으면 `NaverCredentialsMissing`을 올린다 — 호출부가 잡아서 건너뛴다.
    """
    headers = _auth_headers()
    cutoff = date.today() - timedelta(days=days)
    seen_urls: set[str] = set()
    items: list[dict] = []

    queries = build_naver_queries(cat_key)
    for i, query in enumerate(queries):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        url = naver_news_api_url(query, display=100)
        resp = _http.get(url, headers=headers)
        payload = resp.json()

        for raw in payload.get("items", []):
            link = raw.get("originallink") or raw.get("link") or ""
            if not link or link in seen_urls:
                continue
            title = _strip_html(raw.get("title", "")).strip()
            if not title or not match_loose(title, cat_key):
                continue
            published = _parse_pubdate(raw.get("pubDate", ""))
            if published and published < cutoff:
                continue
            seen_urls.add(link)
            tier, trust_score, source_name = trust_of(link)
            noise = is_noise(title, tier=tier)
            items.append({
                "id": make_id(link),
                "category": cat_key,
                "title": title,
                "url": link,
                "published": published,
                "source_name": source_name,
                "source_domain": link,
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
    """카테고리 전체 수집. 자격 증명이 없거나 카테고리 하나가 실패해도 나머지는 계속 진행한다."""
    results: dict[str, list[dict]] = {}
    for i, cat_key in enumerate(CATEGORIES):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            results[cat_key] = fetch_category(cat_key, days=days)
        except NaverCredentialsMissing as exc:
            print(f"[naver_news] 건너뜀: {exc}")
            results[cat_key] = []
        except Exception as exc:  # noqa: BLE001 - 소스 단위 격리(SPEC §9-4)
            print(f"[naver_news] {cat_key} 수집 실패: {exc}")
            results[cat_key] = []
    return results


if __name__ == "__main__":
    print("=== 네이버 뉴스 API 수집 결과 (카테고리별) ===")
    try:
        _auth_headers()
    except NaverCredentialsMissing as exc:
        print(f"  건너뜀: {exc}")
        print("  NAVER_CLIENT_ID / NAVER_CLIENT_SECRET 환경변수를 설정한 뒤 다시 실행하세요.")
    else:
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
