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
