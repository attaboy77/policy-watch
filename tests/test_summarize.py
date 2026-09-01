# -*- coding: utf-8 -*-
"""sources/_summarize.py 단위 테스트 (SPEC.md §6 + SPEC-ADDENDUM-8.md §4)."""
from sources._summarize import summarize


def _item(**overrides):
    base = {
        # id는 일부러 안 넣는다 — summarize()가 캐시 조회에 item["id"]를 쓰는데,
        # None은 실제 캐시 파일에 절대 있을 수 없는 키라 테스트가 실제
        # data/summary_cache.json 내용과 무관하게 항상 격리된다.
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

    # ── is_meeting_schedule (2026-08-31 사용자 지시: KASB 주요일정 문구 구분) ──
    def test_meeting_schedule_uses_meeting_wording_not_takes_effect(self):
        result = summarize(_item(effective_date="2026-09-04", category="kifrs",
                                  is_meeting_schedule=True))
        assert result["impact"] == "2026.09.04 위원회 회의 예정 · 안건 의결 시 시행일 별도 확인"
        assert "부터 적용" not in result["impact"]

    def test_non_meeting_schedule_keeps_existing_wording(self):
        result = summarize(_item(effective_date="2026-09-04", category="kifrs",
                                  is_meeting_schedule=False))
        assert result["impact"] == "2026.09.04부터 적용. 회계팀 사전 검토 필요."

    def test_meeting_schedule_summary_line_says_committee_meeting(self):
        result = summarize(_item(effective_date="2026-09-04", is_meeting_schedule=True))
        assert any("위원회 회의 2026.09.04" in line for line in result["summary"])
        assert not any("시행일 2026.09.04" in line for line in result["summary"])


# ── AI 요약 캐시 우선 적용 (SPEC-ADDENDUM-8.md §4, 2026-08-31 재설계) ────────
class TestSummaryCache:
    def test_no_id_or_cache_miss_falls_back_to_rule_based(self):
        result = summarize(_item(), cache={})
        assert result["ai_generated"] is False

    def test_rule_based_path_reports_ai_generated_false(self):
        result = summarize(_item(effective_date="2026-01-01"), cache={})
        assert result["ai_generated"] is False

    def test_cache_hit_uses_cached_summary_and_impact_verbatim(self):
        cache = {
            "kifrs-1118": {
                "summary": ["K-IFRS 제1118호가 제정되어 손익계산서 표시가 개편된다.",
                            "경영진성과측정치(MPM) 공시가 새로 요구된다."],
                "impact": "2027년 재무제표부터 적용되므로 2026년 중 대응 필요.",
                "generated_at": "2026-08-31T10:00:00+09:00",
                "model": "claude-code-manual",
            }
        }
        result = summarize(_item(id="kifrs-1118", title="K-IFRS 제1118호 제정"), cache=cache)
        assert result["summary"] == cache["kifrs-1118"]["summary"]
        assert result["impact"] == cache["kifrs-1118"]["impact"]
        assert result["ai_generated"] is True

    def test_cache_hit_takes_priority_over_rule_based_effective_date_wording(self):
        # 캐시가 있으면 effective_date 기반 "~부터 적용" 규칙 문구를 덮어써야 한다.
        cache = {"x1": {"summary": ["요약"], "impact": "AI가 쓴 준비사항", "model": "m"}}
        result = summarize(_item(id="x1", effective_date="2026-01-01"), cache=cache)
        assert result["impact"] == "AI가 쓴 준비사항"
        assert "부터 적용" not in result["impact"]

    def test_cache_entry_with_null_impact_preserved(self):
        cache = {"x1": {"summary": ["요약 1", "요약 2"], "impact": None, "model": "m"}}
        result = summarize(_item(id="x1"), cache=cache)
        assert result["impact"] is None
        assert result["ai_generated"] is True


# ── KSSB 자발적용 → ESG 로드맵 규칙 기반 요약 (2026-09-02 사용자 지시) ─────────
# doc_type="자발적용"(KSSB 공시기준서)은 effective_date가 늘 None이라 기존
# 규칙으로는 summary/impact가 둘 다 비었다 — data/esg_roadmap.yml(수동 관리)을
# 대신 재료로 쓴다. 실제 파일 내용에 결합하지 않도록(파일이 나중에 갱신돼도
# 안 깨지게) 구조적 특성만 검증한다.
class TestKssbVoluntaryRoadmap:
    def test_voluntary_doc_type_gets_non_empty_summary(self):
        result = summarize(_item(category="esg", doc_type="자발적용", effective_date=None))
        assert result["summary"]  # 로드맵이 등록돼 있으면 빈 요약이면 안 된다
        assert result["ai_generated"] is False

    def test_voluntary_doc_type_impact_mentions_parent_company_context(self):
        # SPEC: "우리는 1차 대상은 아니나 모회사 연결 공시 대응 필요" 맥락.
        result = summarize(_item(category="esg", doc_type="자발적용", effective_date=None))
        assert result["impact"] is not None
        assert "모회사" in result["impact"]

    def test_voluntary_doc_type_cache_hit_still_takes_priority(self):
        # AI 요약 캐시가 있으면 로드맵 규칙보다 우선한다(기존 캐시 우선 원칙 유지).
        cache = {"x1": {"summary": ["AI가 직접 쓴 요약"], "impact": None, "model": "m"}}
        result = summarize(_item(id="x1", category="esg", doc_type="자발적용"), cache=cache)
        assert result["summary"] == ["AI가 직접 쓴 요약"]
        assert result["impact"] is None
        assert result["ai_generated"] is True

    def test_non_voluntary_doc_type_unaffected_by_roadmap(self):
        # doc_type이 "자발적용"이 아니면 기존 동작(빈 요약) 그대로여야 한다 —
        # 로드맵 분기가 다른 doc_type까지 잘못 건드리지 않는지 확인.
        result = summarize(_item(category="esg", doc_type="제·개정", effective_date=None))
        assert result["summary"] == []
        assert result["impact"] is None
