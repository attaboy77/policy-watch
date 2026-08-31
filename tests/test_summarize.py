# -*- coding: utf-8 -*-
"""sources/_summarize.py 단위 테스트 (SPEC.md §6)."""
from sources._summarize import summarize


def _item(**overrides):
    base = {
        "category": "tax",
        "doc_type": "제·개정",
        "title": "법인세법 시행령 일부개정령안 입법예고",
        "effective_date": None,
        "source": {"name": "기획재정부", "domain": "law.go.kr", "tier": 1, "type": "official"},
        "attachments": None,
    }
    base.update(overrides)
    return base


class TestBuildSummary:
    def test_empty_when_no_body_and_no_extra_facts(self):
        # 본문도, 카드에 없는 추가 사실(첨부파일·시행일)도 없으면 제목/출처를
        # 반복하는 대신 빈 요약을 반환한다(반복하느니 없는 게 낫다는 원칙).
        result = summarize(_item())
        assert result["summary"] == []

    def test_does_not_duplicate_doctype_and_source_as_summary(self):
        # doc_type·출처는 카드 상단에 이미 뱃지로 표시되므로 요약에 다시 넣지 않는다.
        result = summarize(_item(attachments=[{"name": "a.pdf", "url": "https://x/a.pdf"}]))
        assert not any("기획재정부" in line for line in result["summary"])
        assert not any("제·개정" in line for line in result["summary"])

    def test_adds_attachment_count_line(self):
        result = summarize(_item(attachments=[{"name": "a.pdf", "url": "https://x/a.pdf"}]))
        assert any("첨부파일 1건" in line for line in result["summary"])

    def test_summary_has_at_most_3_lines(self):
        result = summarize(_item(effective_date="2026-01-01",
                                  attachments=[{"name": "a.pdf", "url": "https://x"}]))
        assert len(result["summary"]) <= 3

    def test_uses_body_sentences_when_available(self):
        body = ("첫 문장입니다. 법인세법 개정과 관련된 두번째 문장입니다. "
                "관련 없는 세번째 문장입니다.")
        result = summarize(_item(_body=body))
        assert result["summary"][0] == "첫 문장입니다."
        assert any("법인세법" in line for line in result["summary"])

    def test_long_line_truncated_at_word_boundary_with_ellipsis(self):
        long_body = ("가나다라마바사아자차카 " * 10).strip() + "이다."
        result = summarize(_item(_body=long_body))
        assert len(result["summary"][0]) <= 60
        assert result["summary"][0].endswith("…")


class TestBuildImpact:
    def test_effective_date_present_generates_team_review_message(self):
        result = summarize(_item(effective_date="2026-01-01", category="tax"))
        assert result["impact"] == "2026.01.01부터 적용. 세무팀 사전 검토 필요."

    def test_doc_type_qna_generates_review_message(self):
        result = summarize(_item(doc_type="질의회신", effective_date=None))
        assert result["impact"] == "기존 세무처리 관행 재확인 필요."

    def test_doc_type_qna_message_matches_category_not_always_tax(self):
        # 카테고리가 tax가 아닌데 세무 문구가 나오면 안 된다(2026-08-28 사용자 피드백:
        # K-IFRS 질의회신에 "기존 세무처리 관행 재확인 필요"가 나온 버그).
        result = summarize(_item(category="kifrs", doc_type="질의회신", effective_date=None))
        assert result["impact"] == "기존 회계처리 관행 재확인 필요."
        assert "세무" not in result["impact"]

    def test_no_rule_matches_returns_none(self):
        result = summarize(_item(doc_type="기사", effective_date=None))
        assert result["impact"] is None

    def test_effective_date_takes_priority_over_doc_type_rule(self):
        result = summarize(_item(doc_type="질의회신", effective_date="2026-06-01", category="icfr"))
        assert "2026.06.01" in result["impact"]
