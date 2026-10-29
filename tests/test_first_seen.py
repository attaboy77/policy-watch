# -*- coding: utf-8 -*-
from datetime import date

from sources import _first_seen
from sources.main import stamp_first_seen


def test_update_keeps_first_and_moves_last():
    store = {"a": {"first": "2026-10-01", "last": "2026-10-28"}}
    _first_seen.update(store, ["a", "b", ""], "2026-10-29")
    assert store == {"a": {"first": "2026-10-01", "last": "2026-10-29"},
                     "b": {"first": "2026-10-29", "last": "2026-10-29"}}


def test_prune_by_last_seen_not_first():
    store = {
        "daily": {"first": "2025-01-01", "last": "2026-10-29"},   # 매일 보이는 상설 자료 — 남김
        "gone": {"first": "2026-06-01", "last": "2026-06-30"},    # 120일 넘게 안 보임 — 정리
        "edge": {"first": "2026-07-01", "last": "2026-07-01"},    # 정확히 120일 — 남김
        "broken": {"first": "x", "last": None},                   # 깨진 항목은 보존
    }
    out = _first_seen.prune(store, date(2026, 10, 29))
    assert set(out) == {"daily", "edge", "broken"}


def test_load_missing_or_broken_returns_empty(tmp_path):
    assert _first_seen.load(str(tmp_path / "none.json")) == {}
    p = tmp_path / "bad.json"
    p.write_text("{not json", encoding="utf-8")
    assert _first_seen.load(str(p)) == {}


def test_stamp_first_seen_fills_items_and_saves(tmp_path):
    path = str(tmp_path / "first_seen.json")
    _first_seen.save({"old": {"first": "2026-10-01", "last": "2026-10-28"}}, path)
    items = [{"id": "old", "published_at": "2026-08-04"}, {"id": "new", "published_at": "2026-10-20"}]
    stamp_first_seen(items, "2026-10-29", path=path)
    assert [it["first_seen_at"] for it in items] == ["2026-10-01", "2026-10-29"]
    assert _first_seen.load(path)["old"] == {"first": "2026-10-01", "last": "2026-10-29"}


def test_stamp_first_seen_without_store_starts_from_published(tmp_path):
    # 파일이 사라져도 전부 "오늘 처음 본 것"이 되면 안 된다.
    path = str(tmp_path / "first_seen.json")
    items = [{"id": "a", "published_at": "2026-08-04"}, {"id": "b", "published_at": None}]
    stamp_first_seen(items, "2026-10-29", path=path)
    assert [it["first_seen_at"] for it in items] == ["2026-08-04", "2026-10-29"]
