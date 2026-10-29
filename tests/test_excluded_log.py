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


def test_skip_records_collect_reason_listed_after_pipeline_reasons(tmp_path):
    _excluded_log.clear()
    _excluded_log.skip(source="재정경제부", reason="collect:no_category", title="국고채 발행 계획", url="https://m")
    _excluded_log.record(category="kifrs", title="x", url=None, source="s", reason="excluded:opinion_piece")
    path = tmp_path / "EXCLUDED_LOG.md"
    _excluded_log.flush(str(path))
    _excluded_log.clear()
    text = path.read_text(encoding="utf-8")
    assert "|  | 재정경제부 | 국고채 발행 계획 | https://m |  |" in text
    assert text.index("## excluded:opinion_piece") < text.index("## collect:no_category")


def test_tally_writes_count_line_without_titles(tmp_path):
    _excluded_log.clear()
    for _ in range(3):
        _excluded_log.tally("네이버 검색 결과 중 카테고리 미분류")
    path = tmp_path / "EXCLUDED_LOG.md"
    _excluded_log.flush(str(path))
    text = path.read_text(encoding="utf-8")
    assert "- 네이버 검색 결과 중 카테고리 미분류: 3건 (제목은 남기지 않음)" in text
    assert "collect:no_category" not in text
    _excluded_log.clear()
    assert _excluded_log.tallies() == {}
