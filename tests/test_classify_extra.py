# -*- coding: utf-8 -*-
"""분류 단계 보강 테스트 (2026-11-20).

배경: 필터·검색 쪽에서 이미 쓰는 목록이 분류(classify/match_loose)에는 안 쓰여
앞뒤가 안 맞았다 — tax 필수 키워드는 세법·세제개편·유권해석 3개뿐이라
data/tax_subjects.yml 세목 이름만 있는 제목("글로벌최저한세 신고 준비")은 세목
필터에 닿기도 전에 미분류로 버려졌고, esg는 네이버 검색어 "지속가능성 공시"로
가져온 기사를 그 자리에서 버렸다. 키워드를 넓히는 게 아니라 같은 목록을 분류에도
쓰게 맞춘다. 구글 검색어(수집 범위)는 그대로다.
"""
import pytest

from sources import _utils as U


class TestTaxSubjectNames:
    @pytest.mark.parametrize("title", [
        "글로벌최저한세, 세무전문가들과 함께 두 번째 신고를 준비하다!",
        "지방세특례제한법 일부개정법률안 입법예고",
        "조세특례제한법 시행령 개정",
        "국제조세조정에 관한 법률 일부개정법률안 입법예고",
        "부가가치세법 시행규칙 개정",
        "전기차 국내생산세액공제 도입 추진",           # 앞에 다른 말이 붙은 합성어
        "[국세 예규] 거래 단계별 총액 세금계산서 각각 발급·수취?",
    ])
    def test_subject_name_classifies_as_tax(self, title):
        assert U.classify(title) == "tax"
        assert U.match_loose(title, "tax")

    @pytest.mark.parametrize("title", [
        "인천지방세무사회, '2026년 회직자 워크숍' 성료…추진 과제 점검",  # 실측 오탐
        "중부지방세무사회, '자사주 소각부터 배당까지' 세금 문제 논의",
        "면세점 매출 회복세",            # 두 글자 이름은 앞뒤 경계
        "감면세액 계산 방법",
    ])
    def test_word_boundary_blocks_false_hits(self, title):
        assert U.tax_subject_name_hits(title) == []
        assert U.classify(title) is None

    @pytest.mark.parametrize("title", [
        "국제조세조정에 관한 법률 시행령",   # "…세" 뒤 정상 합성어는 통과
        "법인세회계기준 개정 안내",
        "경기도, 지방세제 확충 토론회",
    ])
    def test_legit_compounds_after_se_still_match(self, title):
        assert U.tax_subject_name_hits(title)

    def test_non_target_subject_still_excluded_after_classify(self):
        title = "한교총, 상증법 및 법인세법 시행령 재개정 공청회 개최"
        assert U.classify(title) == "tax"
        assert U.is_non_target_tax_subject("tax", title)  # 파이프라인에서 지금처럼 제외

    def test_subject_hit_counts_in_score_and_keywords(self):
        title = "글로벌최저한세 두 번째 신고 안내"
        assert U.keyword_score(title, "tax") > 0
        assert "글로벌최저한세" in U.matched_keywords(title, "tax")

    def test_existing_scores_unchanged(self):
        # 기존 필수 키워드가 있는 제목은 점수 그대로(순위 변화 없음): "세법" 20 + 조합 "법인세법" 10.
        assert U.keyword_score("법인세법", "tax") == 30
        # 조합 키워드와 같은 분류 전용 단어는 한 번만: "공급망 실사" 조합 10 + 필수로는 안 셈.
        assert U.keyword_score("EU 공급망 실사 법제화", "esg") == 10

    def test_kifrs_signal_still_wins(self):
        assert U.classify("기준서 제1012호 법인세 개정 공개초안") == "kifrs"


class TestEsgQueryPhrases:
    @pytest.mark.parametrize("title", [
        "금융위, 지속가능성 공시 로드맵 이달 발표 목표",
        "EU 공급망 실사 법제화 시행 앞두고",
    ])
    def test_query_phrases_classify_as_esg(self, title):
        # 다른 카테고리 필수 키워드가 같이 있으면 기존 규칙대로 점수로 정한다
        # (예: "한국회계기준원 '지속가능성 공시…'"는 회계기준원 때문에 kifrs와 동점 → kifrs).
        assert U.classify(title) == "esg"
        assert U.match_loose(title, "esg")

    @pytest.mark.parametrize("title", [
        "기후공시, 숫자만으론 부족",
        "탄소회계 기준 후퇴 논란",
        "온실가스 배출권 거래제 개편",
    ])
    def test_climate_words_not_added(self, title):
        assert U.classify(title) is None


class TestCollectionScopeUnchanged:
    def test_google_query_required_part_unchanged(self):
        tax_required = U.build_google_query("tax").split(" AND ")[0]
        esg_required = U.build_google_query("esg").split(" AND ")[0]
        assert "법인세" not in tax_required and "글로벌최저한세" not in tax_required
        assert "지속가능성 공시" not in esg_required and "공급망 실사" not in esg_required


class TestFinancialSectorRulesStayExcluded:
    """미분류 조사 5번 유형 — 2026-11-20 사용자 결정으로 계속 제외."""

    @pytest.mark.parametrize("title", [
        "｢은행업감독규정｣ 일부개정고시안 규정변경예고",
        "｢증권의 발행 및 공시 등에 관한 규정｣ 일부개정고시안 규정변경예고",
        "「자본시장과 금융투자업에 관한 법률 시행령」 일부개정령안 입법예고",
        "「보험업감독규정」 일부개정고시안 규정변경예고",
    ])
    def test_still_no_category(self, title):
        assert U.classify(title) is None
