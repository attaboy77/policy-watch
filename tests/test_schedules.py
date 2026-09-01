# -*- coding: utf-8 -*-
"""sources/schedules.py 단위 테스트 (SPEC.md §4 schedules 스키마)."""
from datetime import date, timedelta

import pytest

from sources.schedules import build_schedules, schedule_from_item, _status_of, _importance_of


def _item(**overrides):
    base = {
        "id": "abc123",
        "category": "icfr",
        "title": "연결 내부회계관리제도 감사 의무 적용",
        "effective_date": "2027-01-01",
        "final_score": 90.0,
        "impact": "2027.01.01부터 적용. 내부회계관리팀 사전 검토 필요.",
        "summary": ["요약 한 줄"],
        "source": {"name": "금융위원회", "domain": "fsc.go.kr", "tier": 1, "type": "official"},
        "urls": {"news": None, "official": "https://law.go.kr/x"},
    }
    base.update(overrides)
    return base


class TestScheduleFromItem:
    def test_id_prefixed_with_sch(self):
        assert schedule_from_item(_item())["id"] == "sch_abc123"

    def test_uses_impact_as_description_when_present(self):
        sch = schedule_from_item(_item())
        assert sch["description"] == "2027.01.01부터 적용. 내부회계관리팀 사전 검토 필요."

    def test_falls_back_to_summary_when_no_impact(self):
        sch = schedule_from_item(_item(impact=None))
        assert sch["description"] == "요약 한 줄"

    def test_falls_back_to_title_when_no_impact_or_summary(self):
        sch = schedule_from_item(_item(impact=None, summary=[]))
        assert sch["description"] == "연결 내부회계관리제도 감사 의무 적용"

    # 2026-09-02 사용자 지시: AI가 검토했지만 둘 다 비운 항목(예: 지방세법
    # 시행령)이 title로 폴백하면 캘린더 카드에 제목이 두 번 나온다 —
    # ai_generated=True면 title 대신 전체 동향 탭과 같은 문구를 쓴다.
    def test_ai_generated_empty_falls_back_to_notice_not_title(self):
        sch = schedule_from_item(_item(impact=None, summary=[], ai_generated=True))
        assert sch["description"] == "AI 검토 결과 팜한농 해당사항 없음"
        assert sch["description"] != "연결 내부회계관리제도 감사 의무 적용"

    def test_non_ai_generated_empty_still_falls_back_to_title(self):
        # ai_generated가 아니면(예: 규칙 기반 폴백) 기존 동작 그대로 유지.
        sch = schedule_from_item(_item(impact=None, summary=[], ai_generated=False))
        assert sch["description"] == "연결 내부회계관리제도 감사 의무 적용"

    def test_carries_source_and_urls_through(self):
        sch = schedule_from_item(_item())
        assert sch["source"]["name"] == "금융위원회"
        assert sch["urls"]["official"] == "https://law.go.kr/x"

    # ── is_meeting (2026-08-31 사용자 지시: 회의 일정/시행일정 캘린더 구분) ──
    def test_defaults_to_not_meeting(self):
        assert schedule_from_item(_item())["is_meeting"] is False

    def test_carries_is_meeting_schedule_flag_through(self):
        sch = schedule_from_item(_item(is_meeting_schedule=True))
        assert sch["is_meeting"] is True

    # ── is_roadmap_estimate (2026-09-02 사용자 지시: KSSB 자발적용 로드맵 예정) ──
    def test_defaults_to_not_roadmap_estimate(self):
        assert schedule_from_item(_item())["is_roadmap_estimate"] is False

    def test_carries_is_roadmap_estimate_flag_through(self):
        sch = schedule_from_item(_item(is_roadmap_estimate=True))
        assert sch["is_roadmap_estimate"] is True


class TestImportanceOf:
    @pytest.mark.parametrize("score,expected", [(85, "high"), (60, "medium"), (10, "low")])
    def test_thresholds(self, score, expected):
        assert _importance_of(_item(final_score=score)) == expected


class TestStatusOf:
    def test_future_date_is_upcoming(self):
        future = (date.today() + timedelta(days=30)).isoformat()
        assert _status_of(future) == "upcoming"

    def test_past_date_is_passed(self):
        past = (date.today() - timedelta(days=30)).isoformat()
        assert _status_of(past) == "passed"

    def test_today_is_upcoming(self):
        assert _status_of(date.today().isoformat()) == "upcoming"


class TestBuildSchedules:
    def test_only_items_with_effective_date_become_schedules(self):
        items = [_item(id="a", effective_date="2027-01-01"), _item(id="b", effective_date=None)]
        out = build_schedules(items, manual_path="__no_such_file__.yml")
        assert len(out) == 1
        assert out[0]["id"] == "sch_a"

    def test_sorted_by_effective_date_ascending(self):
        items = [
            _item(id="later", effective_date="2027-06-01"),
            _item(id="earlier", effective_date="2026-01-01"),
        ]
        out = build_schedules(items, manual_path="__no_such_file__.yml")
        assert [s["id"] for s in out] == ["sch_earlier", "sch_later"]

    def test_missing_manual_file_does_not_raise(self):
        out = build_schedules([_item()], manual_path="__no_such_file__.yml")
        assert len(out) == 1

    def test_dedupes_by_schedule_id(self):
        items = [_item(id="dup"), _item(id="dup")]
        out = build_schedules(items, manual_path="__no_such_file__.yml")
        assert len(out) == 1
