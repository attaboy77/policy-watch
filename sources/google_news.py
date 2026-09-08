# -*- coding: utf-8 -*-
"""구글 뉴스 RSS 수집기.

`_utils.build_google_query()` / `_utils.google_news_rss_url()`을 사용해
(필수 OR ...) AND (조합 OR ...) NOT(노이즈...) 완전 불리언 쿼리로 수집한다.
"""
from __future__ import annotations

import time
from datetime import date

import feedparser

from . import _google_decode, _http
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

# 2026-09-08: news.google.com 리다이렉트 링크를 실제 원문 URL로 디코딩할 때
# 요청 사이에 두는 간격(초) — 요청 2회/건이라 짧은 간격으로 몰아치면 구글이
# 차단(속도 제한)할 위험이 있다. `_google_decode.py` 모듈 docstring 참고.
DECODE_SLEEP_SECONDS = 1.0

# 이번 프로세스 실행 동안의 디코딩 성공/시도 건수 — fetch_all() 시작 시
# reset_decode_stats()로 초기화, main.py가 크롤링 로그/메일 경고에 활용한다.
_DECODE_STATS = {"attempted": 0, "success": 0}


def reset_decode_stats() -> None:
    _DECODE_STATS["attempted"] = 0
    _DECODE_STATS["success"] = 0


def get_decode_stats() -> dict:
    return dict(_DECODE_STATS)


def resolve_news_url(link: str) -> str:
    """구글 뉴스 리다이렉트 링크는 실제 원문 URL로 디코딩을 시도하고,
    실패하거나 애초에 구글 뉴스 링크가 아니면 원래 link를 그대로 반환한다
    (2026-09-08 사용자 지시 — 절대 항목을 버리지 않는다).

    id는 이 함수와 무관하게 원래 link(구글 리다이렉트 URL)로 계산한다(id는
    `fetch_category()`에서 이미 확정됨) — 디코딩 성공 여부에 따라 같은 기사의
    id가 실행마다 바뀌면 dedupe/요약 캐시/신규 항목 판정이 전부 깨지므로,
    id 기준은 그대로 두고 화면에 보여줄 url 필드만 더 나은 값으로 교체한다.
    """
    if "news.google.com" not in link:
        return link
    _DECODE_STATS["attempted"] += 1
    real_url = _google_decode.decode_google_news_url(link)
    time.sleep(DECODE_SLEEP_SECONDS)
    if real_url:
        _DECODE_STATS["success"] += 1
        return real_url
    return link


def resolve_finalized_urls(items: list[dict]) -> None:
    """main.py의 필터 파이프라인(중복제거/규제성 게이트/개별기업소식 제외/
    홍보성 제외/카테고리 상한 등)을 전부 통과해 실제로 site/data.json에
    남는 항목만 대상으로, 아직 news.google.com 리다이렉트 링크인 `urls.news`를
    실제 원문 URL로 디코딩해 제자리에서 교체한다(각 item dict를 직접 수정).

    2026-09-08: 원래는 `fetch_category()` 수집 시점에 바로 디코딩했으나, 그
    시점엔 아직 노이즈 필터만 거친 상태라 이후 파이프라인에서 어차피 걸러질
    항목(중복/규제성 없음/개별기업 소식 등)까지 구글에 요청을 보내게 돼
    불필요하게 느리고 차단 위험만 키웠다 — 파이프라인 맨 끝(finalize 직후)
    으로 옮겨 실제 생존 항목만 디코딩하도록 변경.
    """
    reset_decode_stats()
    for it in items:
        urls = it.get("urls") or {}
        news = urls.get("news")
        if news and "news.google.com" in news:
            urls["news"] = resolve_news_url(news)

    stats = get_decode_stats()
    if stats["attempted"]:
        failed = stats["attempted"] - stats["success"]
        print(f"[google_news] URL 복원 {stats['success']}/{stats['attempted']}건, 실패 {failed}건")


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
        # 구글 뉴스 리다이렉트 링크 디코딩은 여기서 하지 않는다 — 이 시점엔
        # 아직 노이즈 필터만 거친 상태라 이후 파이프라인에서 걸러질 항목까지
        # 구글에 요청을 보내게 된다. main.py 파이프라인 맨 끝에서
        # resolve_finalized_urls()가 실제 생존 항목만 디코딩한다.
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
