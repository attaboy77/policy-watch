# -*- coding: utf-8 -*-
"""첨부파일(HWP/PDF) 안에만 시행일 정보가 있어 자동 추출이 안 되는 항목을 모아
`docs/EFFECTIVE_DATE_GAPS.md`에 기록한다.

SPEC.md §4-3은 첨부파일을 내려받아 파싱하지 않는다고 못박고 있다. 그 결과
일부 공식 소스(대표적으로 금융감독원 내부회계관리제도자료 게시판)는
`effective_date`가 구조적으로 거의 항상 `null`이 된다. 이건 버그가 아니라
소스 특성이므로, "조용히 null로 두는 것"보다 "사람이 검토할 목록으로
모아두는 것"이 낫다 — 관리자가 이 목록을 보고 `data/schedules_manual.yml`에
무엇을 수동으로 채울지 판단한다(사용자 지시 2026-08-26).

세법(tax) 카테고리는 대상이 아니다. 법제처(law_api, D4)가 시행일의 단일
소스이므로 기획재정부·국세청 항목은 애초에 시행일 추출을 시도하지 않는다
(SOURCE_PROBE.md "SPEC-ADDENDUM-2.md/-3.md 반영 상태" §2 참고). 이 로그는
kifrs/icfr/esg처럼 법제처가 커버하지 않는 카테고리를 위한 것이다.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone, timedelta

_KST = timezone(timedelta(hours=9))
_gaps: list[dict] = []


def record(*, source: str, category: str, title: str, url: str,
           note: str = "첨부파일(HWP/PDF) 안에 시행일 정보가 있을 수 있음 — 본문 HTML에는 없음") -> None:
    """gap 하나를 메모리 목록에 추가한다. flush()를 호출해야 파일에 실제로 쓰인다."""
    _gaps.append({
        "source": source,
        "category": category,
        "title": title,
        "url": url,
        "note": note,
    })


def gaps() -> list[dict]:
    """지금까지 record()된 항목 전체(읽기 전용 스냅샷)."""
    return list(_gaps)


def clear() -> None:
    """다음 수집 실행을 위해 메모리 목록을 비운다."""
    _gaps.clear()


def flush(path: str = "docs/EFFECTIVE_DATE_GAPS.md") -> None:
    """현재까지 모인 gap을 마크다운 표로 `path`에 덮어쓴다(누적 아님 — 매 실행 최신 상태 반영).

    관리자가 이 표를 보고 `data/schedules_manual.yml`에 옮길 항목을 고른 뒤 지운다는
    전제이므로, 이전 실행에서 이미 처리된 항목이 다음 실행에서 안 잡히면 자연히
    표에서 빠진다(append가 아니라 overwrite인 이유).
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    now = datetime.now(_KST).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 시행일 수동 검토 목록 (EFFECTIVE_DATE_GAPS)",
        "",
        f"생성 시각: {now}",
        "",
        "첨부파일(HWP/PDF) 안에만 시행일 정보가 있어 자동 추출에 실패한 항목이다.",
        "검토 후 필요한 항목을 `data/schedules_manual.yml`에 수동으로 옮길 것.",
        "세법(tax) 카테고리는 법제처(law_api)가 시행일 단일 소스라 이 목록 대상이 아니다.",
        "",
    ]
    if not _gaps:
        lines.append("_현재 수집 결과에는 검토 대상이 없다._")
    else:
        lines.append("| 카테고리 | 출처 | 제목 | 링크 | 비고 |")
        lines.append("|---|---|---|---|---|")
        for g in _gaps:
            title = g["title"].replace("|", "\\|")
            lines.append(f"| {g['category']} | {g['source']} | {title} | {g['url']} | {g['note']} |")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
