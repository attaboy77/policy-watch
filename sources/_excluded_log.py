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
           reason: str, note: str | None = None) -> None:
    """제외 항목 하나를 메모리 목록에 추가한다. flush()를 호출해야 파일에 쓰인다.
    `note`는 비고 칸(2026-10-08 — §5 병합이면 살아남은 대표 제목)."""
    _excluded.append({
        "category": category,
        "title": title,
        "url": url,
        "source": source,
        "reason": reason,
        "note": note,
    })


def skip(*, source: str, reason: str, title: str, url: str | None = None,
         category: str = "") -> None:
    """수집 단계(어댑터)에서 버린 항목 기록용(2026-10-29). `reason`은 "collect:…".
    어댑터는 파이프라인 item 모양을 만들기 전에 버리므로 `record()`보다 인자를 줄였다.
    소스가 실패해 전일 캐시로 대체되면 그 소스의 이번 기록은 없다(캐시분은 이미 걸러진 것)."""
    record(category=category, title=title, url=url, source=source, reason=reason)


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
        "# 필터 제외 목록 (EXCLUDED_LOG)",
        "",
        f"생성 시각: {now}",
        "",
        "이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는",
        "`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),",
        "`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가",
        "아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.",
        "**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)",
        "`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.",
        "",
    ]
    if not _excluded:
        lines.append("_현재 수집 결과에는 제외된 항목이 없다._")
    else:
        by_reason: dict[str, list[dict]] = {}
        for e in _excluded:
            by_reason.setdefault(e["reason"], []).append(e)
        # 정제 단계(excluded:)를 먼저 — 수집 단계(collect:)는 기관 보도자료 중 무관한 것이 많아 길다.
        order = sorted(by_reason, key=lambda r: (r.startswith("collect:"), r))
        lines.append("| 사유 | 건수 |")
        lines.append("|---|---|")
        for reason in order:
            lines.append(f"| {reason} | {len(by_reason[reason])} |")
        lines.append("")
        for reason in order:
            group = by_reason[reason]
            lines.append(f"## {reason} ({len(group)}건)")
            lines.append("")
            lines.append("| 카테고리 | 출처 | 제목 | 링크 | 비고 |")
            lines.append("|---|---|---|---|---|")
            for e in group:
                title = (e["title"] or "").replace("|", "\\|")
                note = (e.get("note") or "").replace("|", "\\|")
                lines.append(f"| {e['category']} | {e['source'] or ''} | {title} | {e['url'] or ''} | {note} |")
            lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
