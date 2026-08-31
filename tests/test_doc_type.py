# -*- coding: utf-8 -*-
"""sources._utils.doc_type_of() / extract_effective_date() 단위 테스트.

테스트 케이스는 SPEC-ADDENDUM-2.md §4-1을 그대로 따른다.
"""
from datetime import date

import pytest

from sources._utils import doc_type_of, extract_effective_date


class TestDocTypeOf:
    @pytest.mark.parametrize("title,expected", [
        ("K-IFRS 제1116호 개정안 공개초안", "공개초안"),          # 개정보다 공개초안 우선
        ("내부회계관리제도 평가·보고 지침 개정", "적용지침"),      # 개정보다 적용지침 우선
        ("법인세법 시행령 일부개정령안 입법예고", "공개초안"),      # 입법예고 판정
        ("지속가능성 공시기준 제2호 제정 공표", "제·개정"),        # 확정본 판정
        ("내부회계관리제도 FAQ", "FAQ"),
        ("2026년 개정세법 해설", "해설·교육자료"),
        ("국내 ESG 공시 도입 로드맵", "로드맵·일정"),
    ])
    def test_addendum2_cases(self, title, expected):
        assert doc_type_of(title, source_tier=1) == expected

    def test_unmatched_title_high_tier_falls_back_to_article(self):
        assert doc_type_of("삼성전자 신제품 출시", source_tier=4) == "기사"

    def test_unmatched_title_official_tier_falls_back_to_press_release(self):
        assert doc_type_of("금융위원회 정기 간담회 개최", source_tier=1) == "보도자료"

    # ── _norm_keep_spaces() 전환 회귀 테스트 (2026-08-31 사용자 지시) ─────────
    # `_norm()`(공백 전부 제거)을 쓰면 "…ISSB 6월 논의내용 및 회의결과 보고…"의
    # "회의 결과"가 "회의결과"로 붙어 "제·개정" 규칙의 "의결"과 부분일치해버려
    # 회의결과 보고를 "제·개정"(확정)으로 오분류했다(is_discussion_material()이
    # "회의 결과"/"의결" 충돌로 이미 겪었던 것과 같은 종류의 버그).
    def test_committee_meeting_result_report_not_misread_as_final_decision(self):
        title = "2026년 제6회 지속가능성기준위원회(ISSB 6월 주요 논의내용 및 회의결과 보고 등)"
        assert doc_type_of(title, source_tier=1) != "제·개정"

    def test_meeting_result_alone_does_not_trigger_final_decision_rule(self):
        assert doc_type_of("OO위원회 회의 결과 보고", source_tier=1) != "제·개정"

    @pytest.mark.parametrize("kw", [
        "평가·보고지침", "평가및보고", "적용가이드", "설계및운영", "자주묻는",
        "도입일정", "적용일정", "단계별적용", "시행일정",
    ])
    def test_multiword_keyword_no_space_variants_still_match(self, kw):
        # _norm_keep_spaces()는 제목에 실제로 그 공백이 있어야 매칭되므로, 공백
        # 없이 붙여 쓴 실제 사례를 놓치지 않도록 DOC_TYPE_RULES에 공백 없는
        # 형태도 나란히 올려뒀다 — 그 커버리지를 잠근다.
        assert doc_type_of(f"{kw} 관련 공지", source_tier=1) != "보도자료"


class TestExtractEffectiveDate:
    def test_gaesi_saeophyeondo_pattern(self):
        text = "2027년 1월 1일 이후 개시하는 사업연도부터 적용한다."
        assert extract_effective_date(text) == "2027-01-01"

    def test_dot_separated_sihaeng_pattern(self):
        assert extract_effective_date("2026. 7. 1. 시행") == "2026-07-01"

    def test_buteo_jeogyong_pattern(self):
        assert extract_effective_date("2026년 1월 1일부터 적용") == "2026-01-01"

    def test_promulgation_plus_months_pattern(self):
        text = "공포 후 6개월이 경과한 날부터 시행한다."
        promulgation = date(2026, 1, 15)
        assert extract_effective_date(text, promulgation_date=promulgation) == "2026-07-15"

    def test_promulgation_pattern_without_promulgation_date_returns_none(self):
        text = "공포 후 6개월이 경과한 날부터 시행한다."
        assert extract_effective_date(text) is None

    def test_no_pattern_returns_none(self):
        assert extract_effective_date("이 문서는 참고용입니다.") is None

    def test_empty_text_returns_none(self):
        assert extract_effective_date("") is None
        assert extract_effective_date(None) is None
