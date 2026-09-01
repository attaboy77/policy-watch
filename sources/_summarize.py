# -*- coding: utf-8 -*-
"""규칙 기반 2~3줄 요약 + 실무 영향 한 줄 생성 (SPEC.md §6) + AI 요약 캐시 우선
적용 (SPEC-ADDENDUM-8.md §4, 2026-08-31 재설계).

단일 인터페이스: summarize(item) -> {"summary": [...], "impact": str|None,
"ai_generated": bool}. `item["id"]`가 `data/summary_cache.json`에 있으면 그
캐시 내용을 그대로 쓰고(ai_generated=True), 없으면 아래 규칙 기반 로직으로
폴백한다(ai_generated=False) — §4-5 "키가 없으면 요약 없이 정상 동작" 원칙을
그대로 따른다. 캐시를 채우는 방법은 `_summary_cache.py`/`summary_candidates.py`
참고 — Anthropic API가 아니라 Claude Code가 직접 요약을 써서 캐시에 저장한다.

**본문 텍스트 한계(규칙 기반 폴백에만 해당)**: SPEC §6이 가정한 "본문 첫 문장 +
키워드 포함 문장 추출"은 본문이 있어야 가능하다. 지금까지 만든 어댑터 중 상세
본문을 실제로 긁어와 `item["_body"]`에 채워두는 건 일부(예: kasb.py의 A1
공개초안/검토의견 본문)뿐이고 나머지 대부분은 제목만 있다. `_body`가 없으면
억지로 문장을 지어내는 대신 **제목 + 우리가 실제로 아는 사실(문서종류·출처·
첨부파일 수)**로 대체한다 — 없는 내용을 요약이라고 우기는 것보다 낫다.
"""
from __future__ import annotations

import re

from ._config import CATEGORIES
from . import _esg_roadmap, _summary_cache

MAX_LINE_LEN = 60
MAX_SUMMARY_LINES = 3

# main.py 한 번 실행(프로세스 수명) 동안 재사용 — 항목마다 파일을 다시 읽지 않는다.
_CACHE = _summary_cache.load()
# 2026-09-02 사용자 지시: KSSB 자발적용 항목(doc_type="자발적용")은 기준서
# 자체에 시행일이 없어 규칙 기반 impact가 늘 None이었다 — data/esg_roadmap.yml
# (수동 관리, _esg_roadmap.py docstring 참고)을 규칙 기반 summary/impact의
# 재료로 쓴다. 캐시(AI 요약)가 있으면 여전히 그게 우선이다(summarize() 참고).
_ESG_ROADMAP = _esg_roadmap.load()

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?다요])\s+")


def _truncate(s: str, limit: int = MAX_LINE_LEN) -> str:
    """limit자 넘으면 어절 단위로 잘라 말줄임(SPEC §6)."""
    s = s.strip()
    if len(s) <= limit:
        return s
    words = s.split(" ")
    out = ""
    for w in words:
        candidate = (out + " " + w).strip()
        if len(candidate) > limit - 1:  # "…" 한 글자 자리 확보
            break
        out = candidate
    return (out or s[:limit - 1]).rstrip() + "…"


def _split_sentences(body: str) -> list[str]:
    parts = [p.strip() for p in _SENTENCE_SPLIT_RE.split(body) if p.strip()]
    return parts


def _summary_from_body(item: dict) -> list[str]:
    body = item.get("_body") or ""
    sentences = _split_sentences(body)
    if not sentences:
        return []

    category = item.get("category")
    c = CATEGORIES.get(category, {})
    keywords = c.get("required", []) + c.get("combine", [])

    lines = [sentences[0]]
    for s in sentences[1:]:
        if len(lines) >= MAX_SUMMARY_LINES:
            break
        if any(k in s for k in keywords):
            lines.append(s)
    return [_truncate(s) for s in lines[:MAX_SUMMARY_LINES]]


def _fact_lines(item: dict) -> list[str]:
    """본문이 없을 때 쓰는 대체 라인. **카드에 이미 표시되는 정보(제목·문서종류·
    출처)는 반복하지 않는다** — 프론트 카드 상단에 카테고리/문서종류 뱃지와
    출처가 이미 나오므로, 여기서는 카드에 없는 사실(첨부파일 수·시행일)만 보탠다.
    둘 다 없으면 빈 리스트를 반환하고, 호출부(`_build_summary`)가 그대로 빈
    요약으로 남긴다 — 반복하느니 없는 게 낫다는 원칙(2026-08-28 사용자 피드백).
    """
    lines = []
    attachments = item.get("attachments")
    if attachments:
        lines.append(_truncate(f"첨부파일 {len(attachments)}건"))
    effective_date = item.get("effective_date")
    if effective_date:
        # 2026-08-31 사용자 지시: KASB 주요일정(fetch_schedule()) 항목은
        # effective_date가 "시행일"이 아니라 위원회 "회의 진행일자"다 — 같은
        # 문구를 쓰면 실제로 시행되는 것처럼 오해된다.
        if item.get("is_meeting_schedule"):
            lines.append(_truncate(f"위원회 회의 {effective_date.replace('-', '.')}"))
        else:
            lines.append(_truncate(f"시행일 {effective_date.replace('-', '.')}"))
    return lines


def _esg_roadmap_summary_lines() -> list[str]:
    """KSSB 자발적용 항목용 로드맵 요약 2줄. 로드맵 파일이 없거나 마일스톤이
    비어 있으면 빈 리스트(호출부가 기존 _fact_lines()로 폴백)."""
    r = _ESG_ROADMAP
    milestones = r.get("milestones") or []
    if not milestones:
        return []
    status = r.get("status", "예정")
    m0 = milestones[0]
    # 핵심 사실(시기·대상·의무화 내용)을 앞에 두고 출처/상태는 뒤로 뺀다 —
    # _truncate()가 잘라도 알맹이는 남게(2026-09-02 실측: 출처를 앞에 두면
    # 정작 "10조원"이 잘려나가는 문제가 있었다).
    # date(명시적 시행일, 2026-09-02 사용자 지시로 추가)가 있으면 그걸 우선
    # 쓰고, 없으면 기존처럼 연도만 표기한다(마일스톤별로 정밀도가 다를 수 있음).
    if m0.get("date"):
        year_tag = m0["date"].replace("-", ".") + (f"(FY{m0.get('fiscal_year')})" if m0.get("fiscal_year") else "")
    else:
        year_tag = f"{m0.get('year')}년" + (f"(FY{m0.get('fiscal_year')})" if m0.get("fiscal_year") else "")
    line1 = f"{year_tag} {m0.get('detail', m0.get('label', ''))} — 금융위 로드맵({status})"
    lines = [_truncate(line1)]
    if len(milestones) > 1:
        m1 = milestones[1]
        line2 = f"{m1.get('year')}년 {m1.get('detail', m1.get('label', ''))}"
        notes = r.get("notes") or []
        if notes:
            line2 += ", " + notes[0]
        lines.append(_truncate(line2))
    return lines


def _build_summary(item: dict) -> list[str]:
    if item.get("doc_type") == "자발적용":
        roadmap_lines = _esg_roadmap_summary_lines()
        if roadmap_lines:
            return roadmap_lines[:MAX_SUMMARY_LINES]
    lines = _summary_from_body(item)
    # 본문 기반 요약이 없거나(0줄) 3줄 미만이면 사실 라인으로 보충한다(있는 것만).
    # 본문도 사실도 전혀 없으면 빈 리스트를 그대로 반환 — 프론트가 요약 영역을 숨긴다.
    for fact in _fact_lines(item):
        if len(lines) >= MAX_SUMMARY_LINES:
            break
        if fact not in lines:
            lines.append(fact)
    return lines[:MAX_SUMMARY_LINES]


# ADDENDUM-2 §2-1이 "예규·유권해석"을 "질의회신"으로 통합했다 — SPEC.md §6 원문
# 규칙("기존 세무처리 관행 재확인 필요")은 세법 전용 문구라 다른 카테고리 질의회신에
# 그대로 쓰면 카테고리와 안 맞는다(2026-08-28 사용자 피드백) — 카테고리별로 나눈다.
_QNA_IMPACT_BY_CATEGORY = {
    "tax": "기존 세무처리 관행 재확인 필요.",
    "kifrs": "기존 회계처리 관행 재확인 필요.",
    "icfr": "기존 내부통제 운영 방식 재확인 필요.",
    "esg": "기존 공시 실무 재확인 필요.",
}


def _build_impact(item: dict) -> str | None:
    """SPEC §6 규칙. 해당 없으면 억지로 만들지 않고 None."""
    effective_date = item.get("effective_date")
    category = item.get("category")
    # 2026-09-02 사용자 지시: KSSB 자발적용 항목은 자체 시행일이 없어 이 함수가
    # 늘 None을 냈다 — data/esg_roadmap.yml의 company_note(팜한농 관점 문구)를
    # 그대로 쓴다. 로드맵 status가 "예정"이면 그 사실을 괄호로 명시(§6 "확정
    # 여부를 분명히 한다" 원칙과 동일).
    if item.get("doc_type") == "자발적용":
        note = _ESG_ROADMAP.get("company_note")
        if note:
            status = _ESG_ROADMAP.get("status", "예정")
            return f"{note}(금융위 로드맵 {status} 기준)"
    if effective_date:
        formatted = effective_date.replace("-", ".")
        # 2026-08-31 사용자 지시: KASB 주요일정(fetch_schedule()) 항목은
        # effective_date가 위원회 "회의 진행일자"이지 실제 "시행일"이 아니다 —
        # "~부터 적용"이라고 쓰면 그 날 규정이 시행되는 것처럼 오해된다. 안건이
        # 회의에서 의결되더라도 실제 시행일은 보통 그 이후라 별도 확인이 필요.
        if item.get("is_meeting_schedule"):
            return f"{formatted} 위원회 회의 예정 · 안건 의결 시 시행일 별도 확인"
        team = CATEGORIES.get(category, {}).get("team", "담당팀")
        return f"{formatted}부터 적용. {team} 사전 검토 필요."
    if item.get("doc_type") == "질의회신":
        # 매핑에 없는(알 수 없는) 카테고리면 억지로 만들지 않고 None.
        return _QNA_IMPACT_BY_CATEGORY.get(category)
    return None


def summarize(item: dict, cache: dict | None = None) -> dict:
    """item(최종 스키마에 가까운 dict, `_body` 있으면 활용)을 받아
    {"summary": [...], "impact": str|None, "ai_generated": bool}을 반환한다.

    `item["id"]`가 캐시(`cache` 인자로 주입 가능 — 테스트용. 기본은 모듈 로드 시
    읽은 `_CACHE`)에 있으면 그 내용을 그대로 쓴다(ADDENDUM-8 §4 재설계). 없으면
    기존 규칙 기반 로직으로 폴백한다.
    """
    c = _CACHE if cache is None else cache
    cached = c.get(item.get("id"))
    if cached:
        return {
            "summary": cached.get("summary") or [],
            "impact": cached.get("impact"),
            "ai_generated": True,
        }
    return {"summary": _build_summary(item), "impact": _build_impact(item), "ai_generated": False}
