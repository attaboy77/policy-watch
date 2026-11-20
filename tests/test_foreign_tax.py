# -*- coding: utf-8 -*-
"""외국 세제 기사 제외 테스트 (2026-11-20).

분류 보강(tax 세목 이름)으로 "베트남 진출기업 부가세 환급", "UAE 법인세 도입" 같은
외국 세제 기사가 화면까지 올라왔다. 현지 세무는 현지 법인 업무라 "국내 진출기업"
맥락이 있어도 뺀다. 해외 뉴스 필터(美·미국·EU·FASB·SEC)와는 별도 목록이다.
"""
import pytest

from sources import _utils as U
from sources._config import FOREIGN_NEWS_SIGNALS, FOREIGN_TAX_COUNTRIES


class TestIsForeignTaxNews:
    @pytest.mark.parametrize("title", [
        "베트남 진출기업 '부가세 환급' 숙원 풀려…법 개정 전 거래도 소급",   # 실측
        "베트남 진출 한국기업 부가세 환급길 열렸다…최소 400억원 규모",      # 진출기업 맥락도 제외
        "UAE 법인세 도입 후 첫 시행 1년, 기업 주요 문의사항과 연방국세청 답변",  # 실측
        "인도네시아 부가가치세율 인상 시행",
        "사우디 법인세 신고 기한 변경",
        "싱가포르 글로벌최저한세 국내 도입",
    ])
    def test_foreign_tax_excluded(self, title):
        assert U.is_foreign_tax_news("tax", title)

    @pytest.mark.parametrize("title", [
        "한-베트남 조세조약 개정의정서 서명",       # 우리 국제조세 규정
        "한·사우디 이중과세방지협정 발효",
        "글로벌최저한세, 세무전문가들과 함께 두 번째 신고를 준비하다!",
        "[국세 예규] 거래 단계별 총액 세금계산서 각각 발급·수취?",
        "'중국산 공세'에 전기차 세액공제 법 개정 추진",
    ])
    def test_domestic_tax_kept(self, title):
        assert not U.is_foreign_tax_news("tax", title)

    def test_only_tax_category(self):
        assert not U.is_foreign_tax_news("esg", "베트남 공급망 실사 법제화")
        assert not U.is_foreign_tax_news("kifrs", "말레이시아 회계기준 개정")

    def test_left_out_ambiguous_names(self):
        # "오만"(오만하다)·"이란"(조사)·"인도"(물품 인도)는 부분일치 위험이라 목록에 없다.
        for name in ("오만", "이란", "인도"):
            assert name not in FOREIGN_TAX_COUNTRIES
        assert not U.is_foreign_tax_news("tax", "부가가치세법상 재화의 인도 시기란 무엇인가")

    def test_separate_from_foreign_news_signals(self):
        assert not set(FOREIGN_TAX_COUNTRIES) & set(FOREIGN_NEWS_SIGNALS)


class TestApplyForeignTaxFilter:
    def test_filter_excludes_with_reason(self):
        items = [
            {"title": "베트남 진출기업 부가세 환급길 열려", "category": "tax"},
            {"title": "법인세법 시행령 개정안 입법예고", "category": "tax"},
            {"title": "베트남 공급망 실사 법제화", "category": "esg"},
        ]
        kept, excluded = U.apply_foreign_tax_filter(items)
        assert [it["title"] for it in kept] == ["법인세법 시행령 개정안 입법예고", "베트남 공급망 실사 법제화"]
        assert excluded[0]["excluded_reason"] == "excluded:foreign_tax"

    def test_applies_to_official_layer_too(self):
        items = [{"title": "베트남 진출기업 세무 안내", "category": "tax", "layer": "L1",
                  "source": {"type": "official", "tier": 1}}]
        kept, excluded = U.apply_foreign_tax_filter(items)
        assert not kept and len(excluded) == 1


def test_pipeline_runs_foreign_tax_filter():
    import inspect
    from sources import main
    src = inspect.getsource(main.build_data_json)
    assert src.index("apply_non_target_tax_subject_filter") < src.index("apply_foreign_tax_filter")
