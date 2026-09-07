# -*- coding: utf-8 -*-
"""sources/_source_health.py 단위 테스트 (2026-09-07 신설 — 소스 실패 시
전일 데이터 폴백 + 연속 실패 횟수 추적).
"""
from sources import _source_health as sh


class TestCacheLoadSave:
    def test_load_missing_file_returns_empty_dict(self, tmp_path, monkeypatch):
        monkeypatch.setattr(sh, "CACHE_PATH", str(tmp_path / "nope.json"))
        assert sh.load_cache() == {}

    def test_malformed_json_returns_empty_not_raise(self, tmp_path, monkeypatch):
        p = tmp_path / "cache.json"
        p.write_text("{not valid", encoding="utf-8")
        monkeypatch.setattr(sh, "CACHE_PATH", str(p))
        assert sh.load_cache() == {}

    def test_save_then_load_roundtrip(self, tmp_path, monkeypatch):
        p = tmp_path / "sub" / "cache.json"
        monkeypatch.setattr(sh, "CACHE_PATH", str(p))
        sh.save_cache({"nts": [{"id": "x1", "title": "2026년 개정세법 해설"}]})
        assert sh.load_cache() == {"nts": [{"id": "x1", "title": "2026년 개정세법 해설"}]}


class TestHealthLoadSave:
    def test_load_missing_file_returns_empty_dict(self, tmp_path, monkeypatch):
        monkeypatch.setattr(sh, "HEALTH_PATH", str(tmp_path / "nope.json"))
        assert sh.load_health() == {}

    def test_save_then_load_roundtrip(self, tmp_path, monkeypatch):
        p = tmp_path / "health.json"
        monkeypatch.setattr(sh, "HEALTH_PATH", str(p))
        sh.save_health({"nts": {"consecutive_failures": 1}})
        assert sh.load_health() == {"nts": {"consecutive_failures": 1}}


class TestRecordSuccess:
    def test_first_success_sets_zero_and_timestamp(self):
        health = {}
        sh.record_success(health, "nts", "2026-09-04T08:49:53+09:00")
        assert health["nts"]["consecutive_failures"] == 0
        assert health["nts"]["last_success_at"] == "2026-09-04T08:49:53+09:00"
        assert health["nts"]["last_failure_reason"] is None

    def test_success_after_failures_resets_counter_but_keeps_last_failure_at(self):
        health = {"nts": {"consecutive_failures": 3, "last_failure_at": "2026-09-03T...",
                           "last_failure_reason": "timeout", "last_success_at": None}}
        sh.record_success(health, "nts", "2026-09-06T08:33:48+09:00")
        assert health["nts"]["consecutive_failures"] == 0
        assert health["nts"]["last_success_at"] == "2026-09-06T08:33:48+09:00"
        assert health["nts"]["last_failure_reason"] is None
        # 마지막 실패 시각 자체는 기록으로 남겨둔다(언제 마지막으로 문제였는지 참고용)
        assert health["nts"]["last_failure_at"] == "2026-09-03T..."


class TestRecordFailure:
    def test_first_failure_returns_one(self):
        health = {}
        n = sh.record_failure(health, "nts", "timeout", "2026-09-03T08:58:47+09:00")
        assert n == 1
        assert health["nts"]["consecutive_failures"] == 1
        assert health["nts"]["last_failure_reason"] == "timeout"

    def test_consecutive_failures_increment(self):
        health = {}
        sh.record_failure(health, "nts", "timeout", "day1")
        sh.record_failure(health, "nts", "timeout", "day2")
        n = sh.record_failure(health, "nts", "timeout", "day3")
        assert n == 3
        assert health["nts"]["consecutive_failures"] == 3

    def test_failure_after_success_starts_from_one(self):
        health = {}
        sh.record_success(health, "nts", "day0")
        n = sh.record_failure(health, "nts", "timeout", "day1")
        assert n == 1

    def test_independent_sources_tracked_separately(self):
        health = {}
        sh.record_failure(health, "nts", "timeout", "day1")
        sh.record_failure(health, "google_news", "empty", "day1")
        assert health["nts"]["consecutive_failures"] == 1
        assert health["google_news"]["consecutive_failures"] == 1
