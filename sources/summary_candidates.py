# -*- coding: utf-8 -*-
"""AI 요약 대상 후보를 뽑는다 (SPEC-ADDENDUM-8.md §4, 2026-08-31 재설계).

**이 스크립트는 요약을 직접 만들지 않는다.** "어떤 항목에 아직 요약이 없는지"만
알려준다 — 실제 summary/impact 작성은 Claude Code가 각 후보의 원문을 읽고
`_config.SUMMARY_SYSTEM_PROMPT`(§4-2 원안 그대로) 기준으로 직접 판단해서 쓰고,
`_summary_cache.write_entry()`로 저장한다. 사용자가 "요약 생성해줘"라고 명시적
으로 시킬 때만 이 흐름을 실행한다(자동/정기 실행 아님 — 사용자 지시).

실행: `python -m sources.summary_candidates` (site/data.json이 먼저 있어야 함 —
`python -m sources.main`으로 생성)

필터(SUMMARIZE_CONFIG, §4-4 원안 기준 + 한 가지 정정):
- tier가 min_tier보다 크면(일반 뉴스) 제외 — 공식 자료·전문지 위주
- doc_type이 skip_doc_types(논의자료/해외기준)면 제외
- is_static(상설자료)이면 제외 — §4-4 원안은 이걸 "상설자료"라는 doc_type인
  것처럼 적었으나 실제로는 별도 불리언 플래그다(_config.py 주석 참고)
- data/summary_cache.json에 이미 있는 id는 제외(재호출 안 함, §4-3)
- max_batch개까지만
"""
from __future__ import annotations

import json

from ._config import SUMMARIZE_CONFIG
from . import _summary_cache

DATA_JSON_PATH = "site/data.json"


def find_candidates(*, data_path: str = DATA_JSON_PATH,
                     cache: dict | None = None) -> list[dict]:
    """조건에 맞는(아직 요약 없는) 항목 목록을 반환한다. 이미 캐시에 있는 id는
    제외한다(§4-3 "한 번 요약한 항목을 다시 호출하지 않는다").
    """
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    c = _summary_cache.load() if cache is None else cache

    out = []
    for it in data["items"]:
        if it["id"] in c:
            continue
        if it.get("is_static"):
            continue
        if it.get("doc_type") in SUMMARIZE_CONFIG["skip_doc_types"]:
            continue
        tier = (it.get("source") or {}).get("tier", 99)
        if tier > SUMMARIZE_CONFIG["min_tier"]:
            continue
        out.append(it)
        if len(out) >= SUMMARIZE_CONFIG["max_batch"]:
            break
    return out


if __name__ == "__main__":
    if not SUMMARIZE_CONFIG["enabled"]:
        print("[summary_candidates] SUMMARIZE_CONFIG.enabled=False — 그래도 후보는 보여줍니다")
        print("  (이 스크립트는 요약을 자동 생성하지 않으므로 enabled는 참고용입니다).")
    candidates = find_candidates()
    print(f"[summary_candidates] 대상 {len(candidates)}건 (min_tier={SUMMARIZE_CONFIG['min_tier']}, "
          f"max_batch={SUMMARIZE_CONFIG['max_batch']})")
    for it in candidates:
        url = (it.get("urls") or {}).get("official") or (it.get("urls") or {}).get("news")
        print(f"  [{it['category']:5s}][{it['doc_type']:8s}] id={it['id']} | {it['title']}")
        print(f"      원문: {url}")
