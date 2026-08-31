# -*- coding: utf-8 -*-
"""수집된 항목 + data/schedules_manual.yml에서 시행일정을 추출해
data.json의 `schedules` 배열을 생성한다 (SPEC.md §4 schedules 스키마).

`effective_date`가 있는 모든(최종 스키마) item을 자동으로 일정 하나씩으로
변환하고, `data/schedules_manual.yml`의 수동 항목과 합친다. `d_day`는 절대
여기서 계산하지 않는다 — 날짜가 지나면 틀려지므로 프론트엔드가 매번 계산한다
(SPEC §4 필드 규칙).
"""
from __future__ import annotations

import os
from datetime import date, datetime, timezone, timedelta

import yaml

_KST = timezone(timedelta(hours=9))
MANUAL_PATH = "data/schedules_manual.yml"


def _today_kst() -> date:
    return datetime.now(_KST).date()


def _status_of(effective_date: str) -> str:
    try:
        d = date.fromisoformat(effective_date)
    except ValueError:
        return "upcoming"
    return "upcoming" if d >= _today_kst() else "passed"


def _importance_of(item: dict) -> str:
    """final_score 기반 단순 휴리스틱(SPEC/ADDENDUM 어디에도 명시 규칙이 없어
    이미 계산해둔 신뢰도·키워드·최신성 종합 점수를 그대로 재사용한다)."""
    score = item.get("final_score", 0)
    if score >= 80:
        return "high"
    if score >= 50:
        return "medium"
    return "low"


def _description_of(item: dict) -> str:
    if item.get("impact"):
        return item["impact"]
    summary = item.get("summary") or []
    if summary:
        return summary[0]
    return item["title"]


def schedule_from_item(item: dict) -> dict:
    return {
        "id": f"sch_{item['id']}",
        "category": item["category"],
        "title": item["title"],
        "effective_date": item["effective_date"],
        "status": _status_of(item["effective_date"]),
        "importance": _importance_of(item),
        "description": _description_of(item),
        "source": item["source"],
        "urls": item["urls"],
        # 2026-08-31 사용자 지시: 법제처 시행일과 위원회 회의 일정이 캘린더에
        # 섞이면 헷갈린다 — is_meeting=true면 프론트가 "회의 예정"으로 구분
        # 표시한다(kasb.py fetch_schedule() 참고).
        "is_meeting": bool(item.get("is_meeting_schedule", False)),
    }


def _load_manual(path: str = MANUAL_PATH) -> list[dict]:
    """data/schedules_manual.yml을 읽는다. 없거나 비었으면(`[]`) 빈 리스트,
    파싱 실패해도 나머지 파이프라인을 막지 않도록 빈 리스트 + 경고 로그.
    """
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not data:
            return []
        out = []
        for entry in data:
            entry = dict(entry)
            entry.setdefault("id", f"sch_manual_{entry['category']}_{entry['effective_date']}")
            entry.setdefault("status", _status_of(entry["effective_date"]))
            entry.setdefault("urls", {"news": None, "official": None})
            entry.setdefault("is_meeting", False)  # 수동 입력은 전부 실제 시행일정
            out.append(entry)
        return out
    except Exception as exc:  # noqa: BLE001 - 수동 파일 하나 깨져도 자동 수집분은 살린다
        print(f"[schedules] {path} 파싱 실패({exc}) — 수동 일정 없이 진행합니다.")
        return []


def build_schedules(items: list[dict], *, manual_path: str = MANUAL_PATH) -> list[dict]:
    """`items`(최종 스키마) 중 effective_date가 있는 것 전부 + 수동 일정을 합쳐
    effective_date ASC로 정렬해 반환한다(SPEC §4). id가 겹치면 하나만 남긴다.
    """
    auto = [schedule_from_item(it) for it in items if it.get("effective_date")]
    manual = _load_manual(manual_path)

    seen: set[str] = set()
    out: list[dict] = []
    for sch in auto + manual:
        if sch["id"] in seen:
            continue
        seen.add(sch["id"])
        out.append(sch)
    out.sort(key=lambda s: s["effective_date"])
    return out
