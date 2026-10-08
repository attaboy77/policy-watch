# -*- coding: utf-8 -*-
from sources import _excluded_log


def test_flush_writes_reason_summary_and_note(tmp_path):
    _excluded_log.clear()
    _excluded_log.record(category="kifrs", title="금양 과징금", url="https://a", source="중앙신문",
                         reason="excluded:similar_news_merged", note="→ 대표: 금양 과징금 의결")
    _excluded_log.record(category="kifrs", title="비적정 53곳", url=None, source="서울경제",
                         reason="excluded:no_regulatory_signal")
    path = tmp_path / "EXCLUDED_LOG.md"
    _excluded_log.flush(str(path))
    _excluded_log.clear()
    text = path.read_text(encoding="utf-8")
    assert "| excluded:no_regulatory_signal | 1 |" in text
    assert "| excluded:similar_news_merged | 1 |" in text
    assert "| kifrs | 중앙신문 | 금양 과징금 | https://a | → 대표: 금양 과징금 의결 |" in text
    assert "| kifrs | 서울경제 | 비적정 53곳 |  |  |" in text
