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
from ._utils import (apply_category_caps, apply_corporate_pr_filter,
                     apply_regulatory_gate, attach_related_news, dedupe,
                     dedupe_similar_news, finalize_item, normalize_news_item)
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


def _log_stage(stage: str, items: list[dict]) -> None:
    """ADDENDUM-5 §7: 단계별 카테고리별 건수 로그(과다 필터링 확인용)."""
    counts: dict[str, int] = {}
    for it in items:
        counts[it["category"]] = counts.get(it["category"], 0) + 1
    parts = ", ".join(f"{k} {v}" for k, v in counts.items())
    print(f"  [필터] {stage}: 합계 {len(items)}건 ({parts})")


def build_data_json(items: list[dict]) -> dict:
    """수집된 raw item 리스트 → site/data.json 전체 구조(메타 제외 조립은 main()에서).

    필터 순서: dedupe(정확일치) → §5(유사기사 병합) → §1(규제성 게이트) →
    §3(홍보성 제외) → 상한 적용. §1/§3을 §5 뒤로 옮긴 것은 2026-08-31
    사용자 지시(SPEC-ADDENDUM-5.md §7 원안은 §1→§3→...→§5 순서였음) — 그래야
    §1/§3에 걸려 사라질 기사도 §5 중복 병합의 후보에 먼저 포함된다.
    """
    deduped = dedupe(items)
    deduped = dedupe_similar_news(deduped)  # ADDENDUM-5 §5: L3 유사 기사 병합
    _log_stage("§5 중복 제거 후", deduped)
    deduped = apply_regulatory_gate(deduped)  # ADDENDUM-5 §1
    _log_stage("§1 규제성 게이트 후", deduped)
    deduped = apply_corporate_pr_filter(deduped)  # ADDENDUM-5 §3
    _log_stage("§3 홍보성 제외 후", deduped)
    capped = apply_category_caps(deduped)
    # ADDENDUM-4 §4: 공식(L1/L2) 항목에 관련 L3 기사를 연결하고, 그렇게 붙은 L3는
    # 피드 중복 노출을 막기 위해 여기서 제외한다(layer 필드가 남아있는 동안 처리 —
    # finalize_item()이 layer를 지우므로 그 전에 해야 함).
    capped = attach_related_news(capped)

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
