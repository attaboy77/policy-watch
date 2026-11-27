# -*- coding: utf-8 -*-
"""타 산업 전용 세제 기사 제외 테스트 (2026-11-27).

"전기차 생산세액공제" 기사가 11/23~11/27 닷새 동안 화면에 4건 올라왔다. 전기차 산업을 위한
세제라 당사(작물보호제·비료·종자) 재경 업무가 아니다. 업종을 안 가리는 세제와 당사 업종
세제는 산업명이 같이 있어도 통과해야 한다.
"""
import pytest

from sources import _utils as U
from sources._config import OTHER_INDUSTRY_TAX_INDUSTRIES


class TestIsOtherIndustryTax:
    @pytest.mark.parametrize("title", [
        # 실측 — 11/23~11/27 화면 노출 4건
        "전기차 생산세액공제 도입 공감대…'공제액·수출차·통상 마찰' 변수",
        "중국산 전기차 비중 43%… 생산세액공제 도입에 촉각",
        "전기차 생산세액공제 국회 논의 지연…지원대책 발표 또 연기",
        "전기차 세액공제 논의 난항···정부, 경쟁력 강화방안 발표 연기",
        # 다른 세제 단어
        "국산 전기차 법인세 감면 놓고…당정 막판 조율",
        "친환경차 구매 세제 혜택 줄이는데 전기차 생산공제",
        "전기차 개별소비세 감면 연장",
    ])
    def test_excluded(self, title):
        assert U.is_other_industry_tax(title)

    @pytest.mark.parametrize("title", [
        # 업종 무관 세제 — 산업명이 없으면 당연히 통과
        "통합투자세액공제 일몰 3년 연장 추진",
        "연구인력개발비 세액공제 신성장 범위 확대",
        "고용증대세액공제 개편…통합고용세액공제로 일원화",
        "데이터센터 경쟁력 막는 세액공제 제도",
        # 업종 무관 세제 + 산업명이 같이 있어도 통과
        "통합투자세액공제 확대…전기차·반도체 포함",
        "전기차 R&D 세액공제 확대",
        "전기차 추가 검토, 비거주 종부세 차등은 고수…정부 세제개편 '촉각'",
        "2027년 세법개정안 발표…전기차 생산세액공제 포함",
        # 당사 업종이 제목에 있으면 통과
        "작물보호제·전기차 세액공제 대상 추가",
        "비료·전기차 생산세액공제 적용",
        # 전기차지만 세제가 아님
        "전기차 산업 경쟁력 강화를 위한 현장방문 및 업계 간담회 개최",
        "중국 전기차 韓 시장 급속 잠식.. 전방위 대책 시급",
        # 세제지만 다른 문맥
        "법인세법 시행령 개정안 입법예고",
    ])
    def test_kept(self, title):
        assert not U.is_other_industry_tax(title)

    def test_industry_list_only_ev_for_now(self):
        # 다른 산업명은 발견되는 대로 추가 — 미리 채우지 않는다(사용자 지시).
        assert OTHER_INDUSTRY_TAX_INDUSTRIES == ["전기차"]

    def test_list_is_extensible(self, monkeypatch):
        monkeypatch.setattr(U, "OTHER_INDUSTRY_TAX_INDUSTRIES", ["전기차", "항공유"])
        assert U.is_other_industry_tax("항공유 국내생산세액공제 도입")
        assert not U.is_other_industry_tax("항공유 가격 상승")


class TestApplyOtherIndustryTaxFilter:
    def test_filter_excludes_with_reason(self):
        items = [
            {"title": "전기차 생산세액공제 국회 논의 지연", "category": "tax"},
            {"title": "통합투자세액공제 일몰 연장", "category": "tax"},
        ]
        kept, excluded = U.apply_other_industry_tax_filter(items)
        assert [it["title"] for it in kept] == ["통합투자세액공제 일몰 연장"]
        assert excluded[0]["excluded_reason"] == "excluded:other_industry_tax"

    def test_applies_to_all_layers_and_categories(self):
        items = [
            {"title": "전기차 국내생산세액공제 도입", "category": "tax", "layer": "L1",
             "source": {"type": "official", "tier": 1}},
            {"title": "전기차 세액공제 확대", "category": "esg", "source": {"type": "news", "tier": 1}},
        ]
        kept, excluded = U.apply_other_industry_tax_filter(items)
        assert not kept and len(excluded) == 2


def test_pipeline_runs_before_similar_news_merge():
    # #8 유사 뉴스 병합보다 먼저 빼야 전기차 기사가 다른 기사의 대표가 되지 않는다.
    import inspect
    from sources import main
    src = inspect.getsource(main.build_data_json)
    assert (src.index("apply_foreign_tax_filter")
            < src.index("apply_other_industry_tax_filter")
            < src.index("dedupe_similar_news_with_excluded"))
