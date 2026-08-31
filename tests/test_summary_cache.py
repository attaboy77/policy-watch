# -*- coding: utf-8 -*-
"""sources/_summary_cache.py + sources/summary_candidates.py 단위 테스트
(SPEC-ADDENDUM-8.md §4, 2026-08-31 재설계 — Claude Code가 직접 요약을 생성해
캐시에 저장하는 방식)."""
import json

from sources import _summary_cache
from sources.summary_candidates import find_candidates


class TestLoad:
    def test_missing_file_returns_empty_dict(self, tmp_path):
        assert _summary_cache.load(str(tmp_path / "nope.json")) == {}

    def test_malformed_json_returns_empty_dict_not_raise(self, tmp_path):
        p = tmp_path / "broken.json"
        p.write_text("{not valid json", encoding="utf-8")
        assert _summary_cache.load(str(p)) == {}

    def test_reads_existing_cache(self, tmp_path):
        p = tmp_path / "cache.json"
        p.write_text(json.dumps({"x1": {"summary": ["a"], "impact": None}}), encoding="utf-8")
        assert _summary_cache.load(str(p)) == {"x1": {"summary": ["a"], "impact": None}}


class TestSaveAndWriteEntry:
    def test_save_creates_parent_dir(self, tmp_path):
        p = tmp_path / "sub" / "cache.json"
        _summary_cache.save({"x1": {"summary": []}}, str(p))
        assert p.exists()
        assert json.loads(p.read_text(encoding="utf-8")) == {"x1": {"summary": []}}

    def test_write_entry_adds_required_fields(self, tmp_path):
        p = tmp_path / "cache.json"
        _summary_cache.write_entry("x1", summary=["줄1", "줄2"], impact="준비사항", path=str(p))
        cache = json.loads(p.read_text(encoding="utf-8"))
        entry = cache["x1"]
        assert entry["summary"] == ["줄1", "줄2"]
        assert entry["impact"] == "준비사항"
        assert entry["model"] == "claude-code-manual"
        assert "generated_at" in entry

    def test_write_entry_preserves_other_existing_entries(self, tmp_path):
        p = tmp_path / "cache.json"
        _summary_cache.write_entry("x1", summary=["a"], impact=None, path=str(p))
        _summary_cache.write_entry("x2", summary=["b"], impact=None, path=str(p))
        cache = json.loads(p.read_text(encoding="utf-8"))
        assert set(cache.keys()) == {"x1", "x2"}

    def test_write_entry_overwrites_same_id(self, tmp_path):
        p = tmp_path / "cache.json"
        _summary_cache.write_entry("x1", summary=["old"], impact=None, path=str(p))
        _summary_cache.write_entry("x1", summary=["new"], impact=None, path=str(p))
        cache = json.loads(p.read_text(encoding="utf-8"))
        assert cache["x1"]["summary"] == ["new"]


class TestFindCandidates:
    def _data(self, items):
        return {"items": items}

    def _item(self, **overrides):
        base = {
            "id": "x1", "category": "kifrs", "doc_type": "제·개정",
            "title": "K-IFRS 제1118호 제정", "is_static": False,
            "source": {"tier": 1}, "urls": {"official": "https://x", "news": None},
        }
        base.update(overrides)
        return base

    def test_excludes_items_already_cached(self, tmp_path):
        data_path = tmp_path / "data.json"
        data_path.write_text(json.dumps(self._data([self._item(id="x1")])), encoding="utf-8")
        out = find_candidates(data_path=str(data_path), cache={"x1": {}})
        assert out == []

    def test_excludes_static_items(self, tmp_path):
        data_path = tmp_path / "data.json"
        data_path.write_text(json.dumps(self._data([self._item(is_static=True)])), encoding="utf-8")
        out = find_candidates(data_path=str(data_path), cache={})
        assert out == []

    def test_excludes_skip_doc_types(self, tmp_path):
        data_path = tmp_path / "data.json"
        data_path.write_text(json.dumps(self._data([self._item(doc_type="논의자료")])), encoding="utf-8")
        out = find_candidates(data_path=str(data_path), cache={})
        assert out == []

    def test_excludes_low_tier_news(self, tmp_path):
        # SUMMARIZE_CONFIG.min_tier=2 — tier 3(대형 회계법인 등)·4(종합경제지)는 제외.
        data_path = tmp_path / "data.json"
        data_path.write_text(json.dumps(self._data([self._item(source={"tier": 4})])), encoding="utf-8")
        out = find_candidates(data_path=str(data_path), cache={})
        assert out == []

    def test_includes_eligible_official_item(self, tmp_path):
        data_path = tmp_path / "data.json"
        data_path.write_text(json.dumps(self._data([self._item()])), encoding="utf-8")
        out = find_candidates(data_path=str(data_path), cache={})
        assert len(out) == 1
        assert out[0]["id"] == "x1"

    def test_respects_max_batch(self, tmp_path, monkeypatch):
        import sources._config as cfg
        monkeypatch.setitem(cfg.SUMMARIZE_CONFIG, "max_batch", 2)
        data_path = tmp_path / "data.json"
        items = [self._item(id=f"x{i}") for i in range(5)]
        data_path.write_text(json.dumps(self._data(items)), encoding="utf-8")
        out = find_candidates(data_path=str(data_path), cache={})
        assert len(out) == 2
