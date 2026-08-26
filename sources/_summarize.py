# -*- coding: utf-8 -*-
"""규칙 기반 2~3줄 요약 + 실무 영향 한 줄 생성 (SPEC.md §6).

단일 인터페이스: summarize(item) -> {"summary": [...], "impact": str|None}
(추후 외부 LLM 요약으로 교체 가능하도록 인터페이스만 고정)

**본문 텍스트 한계**: SPEC §6이 가정한 "본문 첫 문장 + 키워드 포함 문장 추출"은
본문이 있어야 가능하다. 지금까지 만든 어댑터 중 상세 본문을 실제로 긁어와
`item["_body"]`에 채워두는 건 일부(예: kasb.py의 A1 공개초안/검토의견 본문)뿐이고
나머지 대부분은 제목만 있다. `_body`가 없으면 억지로 문장을 지어내는 대신
**제목 + 우리가 실제로 아는 사실(문서종류·출처·첨부파일 수)**로 대체한다 — 없는
내용을 요약이라고 우기는 것보다 낫다.
"""
from __future__ import annotations

import re

from ._config import CATEGORIES

MAX_LINE_LEN = 60
MAX_SUMMARY_LINES = 3

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
    """본문이 없을 때 쓰는 대체 라인. 있는 사실만 짧게 나열한다."""
    lines = []
    source_name = (item.get("source") or {}).get("name")
    doc_type = item.get("doc_type")
    if source_name and doc_type:
        lines.append(_truncate(f"{doc_type} · 출처: {source_name}"))
    attachments = item.get("attachments")
    if attachments:
        lines.append(_truncate(f"첨부파일 {len(attachments)}건"))
    effective_date = item.get("effective_date")
    if effective_date:
        lines.append(_truncate(f"시행일 {effective_date.replace('-', '.')}"))
    return lines


def _build_summary(item: dict) -> list[str]:
    lines = _summary_from_body(item)
    if not lines:
        lines = [_truncate(item["title"])]
    # 3줄 채우기: 본문 기반 요약이 1~2줄뿐이면 사실 라인으로 보충한다(있는 것만).
    for fact in _fact_lines(item):
        if len(lines) >= MAX_SUMMARY_LINES:
            break
        if fact not in lines:
            lines.append(fact)
    return lines[:MAX_SUMMARY_LINES]


def _build_impact(item: dict) -> str | None:
    """SPEC §6 규칙. 해당 없으면 억지로 만들지 않고 None."""
    effective_date = item.get("effective_date")
    category = item.get("category")
    if effective_date:
        team = CATEGORIES.get(category, {}).get("team", "담당팀")
        formatted = effective_date.replace("-", ".")
        return f"{formatted}부터 적용. {team} 사전 검토 필요."
    # ADDENDUM-2 §2-1이 "예규·유권해석"을 "질의회신"으로 통합했다 — SPEC.md §6 원문 규칙을 그에 맞게 적용.
    if item.get("doc_type") == "질의회신":
        return "기존 세무처리 관행 재확인 필요."
    return None


def summarize(item: dict) -> dict:
    """item(최종 스키마에 가까운 dict, `_body` 있으면 활용)을 받아
    {"summary": [...], "impact": str|None}을 반환한다.
    """
    return {"summary": _build_summary(item), "impact": _build_impact(item)}
