# -*- coding: utf-8 -*-
"""sources/_sent_log.py 단위 테스트 (2026-09-10 신설 — 메일 발송 이력 누적,
구글 뉴스 RSS 재등장 기사의 중복 발송 방지)."""
from datetime import date

from sources import _sent_log as sl


class TestLoadSave:
    def test_load_missing_file_returns_empty_dict(self, tmp_path):
        assert sl.load(str(tmp_path / "nope.json")) == {}

    def test_malformed_json_returns_empty_not_raise(self, tmp_path):
        p = tmp_path / "broken.json"
        p.write_text("{not valid", encoding="utf-8")
        assert sl.load(str(p)) == {}

    def test_non_dict_json_returns_empty(self, tmp_path):
        p = tmp_path / "list.json"
        p.write_text("[1, 2, 3]", encoding="utf-8")
        assert sl.load(str(p)) == {}

    def test_save_then_load_roundtrip(self, tmp_path):
        p = tmp_path / "sub" / "sent_log.json"
        sl.save({"a1": "2026-09-09"}, str(p))
        assert sl.load(str(p)) == {"a1": "2026-09-09"}


class TestRecord:
    def test_adds_new_ids_with_given_date(self):
        sent = {}
        sl.record(sent, ["a", "b"], "2026-09-10")
        assert sent == {"a": "2026-09-10", "b": "2026-09-10"}

    def test_overwrites_existing_id_with_latest_date(self):
        sent = {"a": "2026-09-01"}
        sl.record(sent, ["a"], "2026-09-10")
        assert sent == {"a": "2026-09-10"}

    def test_ignores_empty_or_none_ids(self):
        sent = {}
        sl.record(sent, ["", None, "a"], "2026-09-10")
        assert sent == {"a": "2026-09-10"}


class TestPrune:
    def test_keeps_ids_within_retention_window(self):
        sent = {"a": "2026-09-01"}
        today = date(2026, 9, 10)
        assert sl.prune(sent, today=today, retention_days=90) == {"a": "2026-09-01"}

    def test_removes_ids_older_than_retention_window(self):
        today = date(2026, 9, 10)
        sent = {"old": "2025-01-01", "recent": "2026-09-01"}
        out = sl.prune(sent, today=today, retention_days=90)
        assert out == {"recent": "2026-09-01"}

    def test_boundary_exactly_at_cutoff_kept(self):
        today = date(2026, 9, 10)
        cutoff_date = "2026-06-12"  # 정확히 90일 전(경계값 — >=이므로 유지)
        sent = {"boundary": cutoff_date}
        assert sl.prune(sent, today=today, retention_days=90) == {"boundary": cutoff_date}

    def test_malformed_date_is_preserved_not_dropped(self):
        sent = {"weird": "not-a-date"}
        assert sl.prune(sent, today=date(2026, 9, 10)) == {"weird": "not-a-date"}

    def test_returns_new_dict_does_not_mutate_input(self):
        sent = {"old": "2025-01-01"}
        out = sl.prune(sent, today=date(2026, 9, 10), retention_days=90)
        assert out is not sent
        assert sent == {"old": "2025-01-01"}  # 입력은 그대로
