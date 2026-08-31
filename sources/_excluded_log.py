# -*- coding: utf-8 -*-
"""적용 대상 판정 게이트(SPEC-ADDENDUM-6.md §1)에서 제외된 항목을
`docs/EXCLUDED_LOG.md`에 기록한다.

§1-3: "제외된 항목은 data.json에 넣지 않되, 제외 로그를 파일로 남긴다 — 과다
필터링 여부를 사후에 검증하기 위함." §9-2가 특히 점검하라고 지목한 것:
"감독규정" 키워드로 제외된 것 중 회계 관련 규정이 섞이지 않았는지,
"공익법인" 등으로 제외된 세법 개정 중 일반법인에도 적용되는 게 없는지.
이 로그가 그 사후 검토의 근거 자료다. `_gap_log.py`와 동일한
record/gaps/clear/flush 패턴을 따른다(누적이 아니라 매 실행 최신 상태로 덮어씀).
"""
from __future__ import annotations

import os
from datetime import datetime, timezone, timedelta

_KST = timezone(timedelta(hours=9))
_excluded: list[dict] = []


def record(*, category: str, title: str, url: str | None, source: str | None,
           reason: str) -> None:
    """제외 항목 하나를 메모리 목록에 추가한다. flush()를 호출해야 파일에 쓰인다."""
    _excluded.append({
        "category": category,
        "title": title,
        "url": url,
        "source": source,
        "reason": reason,
    })


def excluded() -> list[dict]:
    """지금까지 record()된 항목 전체(읽기 전용 스냅샷)."""
    return list(_excluded)


def clear() -> None:
    """다음 수집 실행을 위해 메모리 목록을 비운다."""
    _excluded.clear()


def flush(path: str = "docs/EXCLUDED_LOG.md") -> None:
    """현재까지 모인 제외 항목을 마크다운 표로 `path`에 덮어쓴다(누적 아님).

    사유(reason)별로 묶어서 보여준다 — §9-2 점검("감독규정으로 제외된 것 중
    회계 관련이 섞이지 않았는가" 등)을 사유 단위로 훑기 쉽게 하기 위함.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    now = datetime.now(_KST).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 적용 대상 판정 제외 목록 (EXCLUDED_LOG)",
        "",
        f"생성 시각: {now}",
        "",
        "SPEC-ADDENDUM-6.md §1(적용 대상 판정 게이트)에서 제외된 항목이다.",
        "L1/L2/L3 전 계층 대상 — 공식 소스도 면제되지 않는다(§1-2).",
        "**과다 필터링 점검용**: 아래 목록 중 실제로는 우리에게 적용되는 항목이",
        "있으면(오제외) 해당 키워드를 `sources/_config.py`의 `APPLICABILITY`에서",
        "빼거나 예외 조건을 추가할 것(§9-2).",
        "",
    ]
    if not _excluded:
        lines.append("_현재 수집 결과에는 제외된 항목이 없다._")
    else:
        by_reason: dict[str, list[dict]] = {}
        for e in _excluded:
            by_reason.setdefault(e["reason"], []).append(e)
        for reason in sorted(by_reason):
            group = by_reason[reason]
            lines.append(f"## {reason} ({len(group)}건)")
            lines.append("")
            lines.append("| 카테고리 | 출처 | 제목 | 링크 |")
            lines.append("|---|---|---|---|")
            for e in group:
                title = (e["title"] or "").replace("|", "\\|")
                lines.append(f"| {e['category']} | {e['source'] or ''} | {title} | {e['url'] or ''} |")
            lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
