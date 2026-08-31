# -*- coding: utf-8 -*-
"""sources/_schema.py 단위 테스트 — site/data.json이 SPEC.md §4 스키마와
100% 일치하는지 검증하는 스크립트 자체를 검증한다."""
import copy

from sources._schema import validate

_VALID_ITEM = {
    "id": "abc123",
    "category": "tax",
    "doc_type": "제·개정",
    "stage": "확정",
    "title": "법인세법 시행령 일부개정",
    "summary": ["요약 한 줄"],
    "impact": "2026.01.01부터 적용. 세무팀 사전 검토 필요.",
    "published_at": "2025-12-23",
    "collected_at": "2026-08-26T18:00:00+09:00",
    "effective_date": "2026-01-01",
    "source": {"name": "기획재정부", "domain": "law.go.kr", "tier": 1, "type": "official"},
    "trust_score": 100,
    "keyword_score": 30,
    "final_score": 64.0,
    "matched_keywords": ["법인세법"],
    "urls": {"news": None, "official": "https://law.go.kr/x"},
    "law_meta": None,
    "attachments": None,
    "is_static": False,
    "date_estimated": False,
    "duplicate_count": 0,
    "duplicate_sources": [],
    "related_news": [],
    "is_meeting_schedule": False,
}

_VALID_SCHEDULE = {
    "id": "sch_abc123",
    "category": "tax",
    "title": "법인세법 시행령 일부개정",
    "effective_date": "2026-01-01",
    "status": "upcoming",
    "importance": "high",
    "description": "2026.01.01부터 적용.",
    "source": {"name": "기획재정부", "domain": "law.go.kr", "tier": 1, "type": "official"},
    "urls": {"news": None, "official": "https://law.go.kr/x"},
    "is_meeting": False,
}

_VALID_DATA = {
    "meta": {
        "schema_version": "1.0",
        "generated_at": "2026-08-26T18:00:00+09:00",
        "window_days": 90,
        "total_items": 1,
        "counts_by_category": {"tax": 1},
        "sources_ok": ["law_api"],
        "sources_failed": [],
    },
    "categories": [
        {"key": "kifrs", "label": "K-IFRS", "color": "#1e3a8a", "team": "회계팀"},
        {"key": "tax", "label": "세법", "color": "#047857", "team": "세무팀"},
        {"key": "icfr", "label": "내부회계", "color": "#b45309", "team": "내부회계관리팀"},
        {"key": "esg", "label": "ESG", "color": "#0e7490", "team": "ESG팀"},
    ],
    "items": [_VALID_ITEM],
    "schedules": [_VALID_SCHEDULE],
}


class TestValidate:
    def test_valid_data_has_no_errors(self):
        assert validate(copy.deepcopy(_VALID_DATA)) == []

    def test_missing_top_level_key_fails(self):
        data = copy.deepcopy(_VALID_DATA)
        del data["schedules"]
        assert validate(data) != []

    def test_invalid_category_enum_fails(self):
        data = copy.deepcopy(_VALID_DATA)
        data["items"][0]["category"] = "not_a_real_category"
        assert validate(data) != []

    def test_invalid_doc_type_enum_fails(self):
        data = copy.deepcopy(_VALID_DATA)
        data["items"][0]["doc_type"] = "예규·유권해석"  # ADDENDUM-2가 "질의회신"으로 대체한 옛 값
        assert validate(data) != []

    def test_stage_must_be_stored_value_not_computed_ones(self):
        # ADDENDUM-2 §2-2: data.json에는 "시행예정"/"시행중"을 저장하면 안 된다
        data = copy.deepcopy(_VALID_DATA)
        data["items"][0]["stage"] = "시행예정"
        assert validate(data) != []

    def test_summary_more_than_3_items_fails(self):
        data = copy.deepcopy(_VALID_DATA)
        data["items"][0]["summary"] = ["a", "b", "c", "d"]
        assert validate(data) != []

    def test_bad_date_format_fails(self):
        data = copy.deepcopy(_VALID_DATA)
        data["items"][0]["published_at"] = "2026/08/26"
        assert validate(data) != []

    def test_null_effective_date_and_null_impact_are_allowed(self):
        data = copy.deepcopy(_VALID_DATA)
        data["items"][0]["effective_date"] = None
        data["items"][0]["impact"] = None
        assert validate(data) == []
