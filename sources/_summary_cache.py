# -*- coding: utf-8 -*-
"""AI 요약 캐시 파일(data/summary_cache.json) 읽기/쓰기 (SPEC-ADDENDUM-8.md §4-3).

캐시 구조는 §4-3 원안 그대로 쓴다(사용자 지시):
{
  "<item_id>": {
    "summary": ["...", "..."],
    "impact": "..." | null,
    "generated_at": "2026-08-31T10:00:00+09:00",
    "model": "..."
  }
}

**원안과 다른 점은 누가/어떻게 채우느냐뿐이다.** §4 원안은 Anthropic API 호출
결과로 이 캐시를 채우는 걸 전제했지만, 유료 API 대신 **Claude Code가 직접
요약을 생성해 이 캐시에 저장**하는 방식으로 재설계했다(2026-08-31 사용자 지시
— "내가 필요할 때마다 시킬게", 즉 자동/정기 실행이 아니라 사용자가 명시적으로
요청할 때만 작동).

표준 사용 흐름:
1. `python -m sources.summary_candidates` 로 아직 캐시에 없는 대상을 뽑는다
   (SUMMARIZE_CONFIG 필터 적용 — 공식 소스 위주, 논의자료/해외기준/상설자료 제외).
2. Claude Code가 각 후보의 원문(urls.official 또는 urls.news)을 읽는다.
3. `_config.SUMMARY_SYSTEM_PROMPT`(§4-2 원안 그대로) 기준으로 summary 2줄 +
   impact 1줄을 직접 판단해 작성한다.
4. `write_entry()`로 이 파일에 기록한다.
5. `python -m sources.main`을 다시 돌리면 `_summarize.summarize()`가 캐시를
   자동으로 읽어 반영한다(캐시에 없는 항목은 그대로 규칙 기반 폴백 — §4-5).

캐시 파일은 git에 커밋해 재사용한다(§4-3) — 매번 새로 만들 필요가 없다.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone, timedelta

from ._config import SUMMARY_CACHE_PATH

_KST = timezone(timedelta(hours=9))


def load(path: str = SUMMARY_CACHE_PATH) -> dict:
    """캐시 파일을 읽는다. 없거나 파싱 실패하면 빈 dict를 반환한다 — §4-5
    "키가 없으면 요약 없이 정상 동작한다" 원칙을 캐시 부재/손상에도 그대로 적용.
    """
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:  # noqa: BLE001 - 캐시 파일 하나 깨져도 전체를 막지 않는다
        print(f"[summary_cache] {path} 파싱 실패({exc}) — 캐시 없이 규칙 기반으로 폴백합니다.")
        return {}


def save(cache: dict, path: str = SUMMARY_CACHE_PATH) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2, sort_keys=True)


def write_entry(item_id: str, *, summary: list[str], impact: str | None,
                 model: str = "claude-code-manual", path: str = SUMMARY_CACHE_PATH) -> None:
    """캐시 항목 하나를 기록한다. Claude Code가 원문을 읽고 SUMMARY_SYSTEM_PROMPT
    기준으로 직접 판단해 요약을 작성한 뒤 이 함수를 호출하는 게 표준 사용법이다
    (모듈 docstring의 "표준 사용 흐름" 참고). 기존 캐시를 지우지 않고 이 id만
    갱신·추가한다.
    """
    cache = load(path)
    cache[item_id] = {
        "summary": summary,
        "impact": impact,
        "generated_at": datetime.now(_KST).isoformat(timespec="seconds"),
        "model": model,
    }
    save(cache, path)
