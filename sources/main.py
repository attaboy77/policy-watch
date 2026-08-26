# -*- coding: utf-8 -*-
"""오케스트레이터 (entry point).

각 소스 수집기를 독립적으로 실행하고(한 소스 실패가 전체를 죽이지 않도록),
정제 파이프라인(중복 제거 → 계층별 상한/정렬 → 요약 → 스키마 확정)을 거쳐
site/data.json을 생성한다.

실행: python -m sources.main
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone, timedelta

from . import _gap_log
from ._config import CATEGORIES, COLLECT_WINDOW_DAYS
from ._schema import validate as validate_schema
from ._summarize import summarize
from ._utils import apply_category_caps, dedupe, finalize_item, normalize_news_item
from .schedules import build_schedules

from . import google_news, naver_news
from .official import kasb, fss, moef, nts, fsc
from . import policy_briefing, law_api

_KST = timezone(timedelta(hours=9))
DATA_JSON_PATH = "site/data.json"
SCHEMA_VERSION = "1.0"

# (소스명, fetch 함수) — 이미 최종 스키마에 가까운 모양을 반환하는 어댑터들.
OFFICIAL_SOURCES = [
    ("kasb", kasb.fetch),
    ("fss", fss.fetch),
    ("moef", moef.fetch),
    ("nts", nts.fetch),
    ("fsc", fsc.fetch),
    ("policy_briefing", policy_briefing.fetch),
    ("law_api", law_api.fetch),
]
# (소스명, fetch_all 함수) — 카테고리별 raw item을 돌려주는 뉴스 어댑터. normalize 필요.
NEWS_SOURCES = [
    ("google_news", google_news.fetch_all, "news"),
    ("naver_news", naver_news.fetch_all, "news"),
]


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def collect_all() -> tuple[list[dict], list[str], list[dict]]:
    """모든 소스를 독립적으로 수집한다. 하나가 죽어도 나머지는 계속 진행(SPEC §9-4)."""
    items: list[dict] = []
    sources_ok: list[str] = []
    sources_failed: list[dict] = []

    for name, fetch_fn in OFFICIAL_SOURCES:
        try:
            got = fetch_fn()
            items.extend(got)
            sources_ok.append(name)
        except Exception as exc:  # noqa: BLE001 - 소스 단위 격리
            print(f"[main] {name} 수집 실패: {exc}")
            sources_failed.append({"name": name, "reason": str(exc)})

    for name, fetch_all_fn, source_type in NEWS_SOURCES:
        try:
            by_category = fetch_all_fn()
            got_any = False
            for _cat, raw_items in by_category.items():
                for raw in raw_items:
                    items.append(normalize_news_item(raw, source_type=source_type))
                    got_any = True
            if got_any:
                sources_ok.append(name)
            else:
                # 전부 빈 결과 — naver_news는 자격증명 없으면 조용히 빈 dict를 준다(graceful degradation).
                sources_failed.append({"name": name, "reason": "결과 0건(자격증명 미설정 또는 응답 없음)"})
        except Exception as exc:  # noqa: BLE001
            print(f"[main] {name} 수집 실패: {exc}")
            sources_failed.append({"name": name, "reason": str(exc)})

    return items, sources_ok, sources_failed


def build_data_json(items: list[dict]) -> dict:
    """수집된 raw item 리스트 → site/data.json 전체 구조(메타 제외 조립은 main()에서)."""
    deduped = dedupe(items)
    capped = apply_category_caps(deduped)

    finalized = []
    for it in capped:
        s = summarize(it)  # `_body`가 있으면 여기서 활용(finalize_item이 지우기 전에 먼저 호출)
        it["summary"], it["impact"] = s["summary"], s["impact"]
        finalized.append(finalize_item(it))

    schedules = build_schedules(finalized)

    counts_by_category = {c: 0 for c in CATEGORIES}
    for it in finalized:
        counts_by_category[it["category"]] = counts_by_category.get(it["category"], 0) + 1

    categories = [
        {"key": key, "label": c["label"], "color": c["color"], "team": c["team"]}
        for key, c in CATEGORIES.items()
    ]

    return {
        "categories": categories,
        "items": finalized,
        "schedules": schedules,
        "_counts_by_category": counts_by_category,  # main()에서 meta 조립용, 최종 출력엔 안 들어감
    }


def main() -> None:
    print("=== Policy Watch 수집 시작 ===")
    _gap_log.clear()  # 이 프로세스 실행 동안 모인 gap만 반영(재실행 시 누적 방지)
    raw_items, sources_ok, sources_failed = collect_all()
    print(f"  원본 수집: {len(raw_items)}건 (성공 소스 {len(sources_ok)}개, 실패 {len(sources_failed)}개)")

    built = build_data_json(raw_items)
    counts_by_category = built.pop("_counts_by_category")

    data = {
        "meta": {
            "schema_version": SCHEMA_VERSION,
            "generated_at": _now_kst_iso(),
            "window_days": COLLECT_WINDOW_DAYS,
            "total_items": len(built["items"]),
            "counts_by_category": counts_by_category,
            "sources_ok": sources_ok,
            "sources_failed": sources_failed,
        },
        **built,
    }

    errors = validate_schema(data)
    if errors:
        print(f"  ⚠ 스키마 검증 실패 {len(errors)}건:")
        for e in errors[:20]:
            print(f"    - {e}")
    else:
        print("  ✓ 스키마 검증 통과")

    os.makedirs(os.path.dirname(DATA_JSON_PATH) or ".", exist_ok=True)
    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"  총 {len(built['items'])}건 → {DATA_JSON_PATH} 저장 완료")
    print(f"  카테고리별: {counts_by_category}")
    print(f"  일정: {len(built['schedules'])}건")

    _gap_log.flush()
    gap_count = len(_gap_log.gaps())
    if gap_count:
        print(f"  ⚠ 시행일 수동 검토 필요: {gap_count}건 → docs/EFFECTIVE_DATE_GAPS.md")

    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
