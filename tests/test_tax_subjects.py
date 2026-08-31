# -*- coding: utf-8 -*-
"""세목 화이트리스트 / INCIDENT_KEYWORDS / 세무조사 조합 / 계층 정렬·상한 테스트.

세목 테스트 케이스는 SPEC-ADDENDUM-3.md §7을 그대로 따른다.
"""
import pytest

from sources._utils import (
    match_tax_subject,
    pass_tax_filter,
    is_incident_noise,
    matches_tax_investigation_combo,
    keyword_score,
    matched_keywords,
    layer_of,
    sort_by_layer_then_score,
    apply_category_caps,
)
from sources._config import TAX_SUBJECTS


# ── 세목 화이트리스트 (ADDENDUM-3 §7) ───────────────────────────────────────
class TestMatchTaxSubject:
    def test_jongbuse_excluded_outside_whitelist(self):
        assert match_tax_subject("초고가 주택 종부세 인상, 장특공제 10억원 한도") == []

    def test_corp_included_when_corp_tax_mentioned(self):
        assert "corp" in match_tax_subject("소득·법인세 줄고 종부세 증가…5년간 세수효과")

    def test_vat_matches(self):
        assert "vat" in match_tax_subject("부가가치세법 시행령 일부개정령안 입법예고")

    def test_inheritance_tax_excluded_outside_whitelist(self):
        assert match_tax_subject("상속세 및 증여세법 개정안") == []

    def test_stt_matches_tax_credit(self):
        assert "stt" in match_tax_subject("통합투자세액공제 확대 (조특법)")

    def test_intl_matches_global_minimum_tax(self):
        assert "intl" in match_tax_subject("글로벌최저한세 신고 안내")

    def test_disabled_subject_excluded(self, monkeypatch):
        # local(지방세)을 비활성화한 상태를 흉내낸다.
        import sources._utils as u
        disabled = [s for s in TAX_SUBJECTS if s["key"] != "local"]
        monkeypatch.setattr(u, "TAX_SUBJECTS", disabled)
        assert match_tax_subject("취득세 개편") == []

    def test_empty_subjects_config_passes_everything(self, monkeypatch):
        import sources._utils as u
        monkeypatch.setattr(u, "TAX_SUBJECTS", [])
        assert match_tax_subject("아무 텍스트나") == ["_all"]


class TestPassTaxFilter:
    def test_non_tax_category_always_passes(self):
        assert pass_tax_filter(category="kifrs", layer="L3", text="종부세 인상") is True

    def test_l1_comprehensive_exempt(self):
        assert pass_tax_filter(category="tax", layer="L1_comprehensive",
                                text="2026년 세제개편안 발표") is True

    def test_l3_tax_requires_whitelist_match(self):
        assert pass_tax_filter(category="tax", layer="L3",
                                text="초고가 주택 종부세 인상") is False
        assert pass_tax_filter(category="tax", layer="L3",
                                text="법인세법 개정안 발표") is True

    def test_l2_tax_requires_whitelist_match(self):
        assert pass_tax_filter(category="tax", layer="L2", text="상속세 개편안") is False


# ── 세무조사 조합 매칭 (ADDENDUM-3 §5-2) ────────────────────────────────────
class TestTaxInvestigationCombo:
    def test_bare_semujosa_does_not_match(self):
        assert matches_tax_investigation_combo("세무조사 로비 의혹 계열사 수사") is False

    @pytest.mark.parametrize("qualifier", [
        "사전통지", "대상 선정", "운영규정", "절차", "기간 연장", "납세자권리",
    ])
    def test_semujosa_with_each_qualifier_matches(self, qualifier):
        assert matches_tax_investigation_combo(f"세무조사 {qualifier} 안내") is True

    def test_qualifier_alone_without_trigger_does_not_match(self):
        assert matches_tax_investigation_combo("절차 안내") is False

    def test_keyword_score_counts_combo_once(self):
        # 필수 1개(세법) + 세무조사 조합 1개 = 20 + 10 = 30
        # ADDENDUM-6 §2-3: tax의 required에서 "국세청"(기관명)을 뺐으므로
        # 필수 키워드 예시를 "세법"로 교체(§2-3, 2026-08-31).
        assert keyword_score("세법 세무조사 사전통지 개선", "tax") == 30

    def test_matched_keywords_includes_semujosa_when_combo_present(self):
        hits = matched_keywords("국세청 세무조사 절차 개선", "tax")
        assert "세무조사" in hits

    def test_matched_keywords_excludes_semujosa_when_bare(self):
        hits = matched_keywords("국세청 세무조사 로비 의혹", "tax")
        assert "세무조사" not in hits


# ── 사건·사고 노이즈 필터 (ADDENDUM.md §5-1) ────────────────────────────────
class TestIsIncidentNoise:
    def test_incident_without_procedural_keyword_is_noise(self):
        assert is_incident_noise("세무조사 로비 의혹 계열사 수사", tier=5) is True

    def test_incident_with_procedural_keyword_is_not_noise(self):
        assert is_incident_noise("탈세 혐의 판결에 따른 예규 변경", tier=5) is False

    def test_no_incident_keyword_is_not_noise(self):
        assert is_incident_noise("법인세법 시행령 개정안 입법예고", tier=5) is False

    def test_tier1_official_exempted(self):
        assert is_incident_noise("검찰 수사 관련 국세청 보도자료", tier=1) is False


# ── 계층 정렬·상한 (ADDENDUM.md §1) ─────────────────────────────────────────
class TestLayerSortAndCaps:
    def test_layer_of_defaults_to_l3_when_missing(self):
        assert layer_of({"title": "뉴스"}) == "L3"

    def test_layer_of_reads_explicit_layer(self):
        assert layer_of({"layer": "L1"}) == "L1"

    def test_sort_puts_l1_l2_before_l3_regardless_of_score(self):
        items = [
            {"layer": "L3", "final_score": 99.0},
            {"layer": "L1", "final_score": 10.0},
        ]
        out = sort_by_layer_then_score(items)
        assert [it["layer"] for it in out] == ["L1", "L3"]

    def test_sort_orders_by_score_within_same_layer(self):
        items = [
            {"layer": "L3", "final_score": 10.0},
            {"layer": "L3", "final_score": 90.0},
        ]
        out = sort_by_layer_then_score(items)
        assert [it["final_score"] for it in out] == [90.0, 10.0]

    def test_apply_category_caps_keeps_all_official_items(self):
        official = [{"category": "tax", "layer": "L1", "final_score": float(i),
                     "source": {"tier": 1}} for i in range(30)]
        out = apply_category_caps(official)
        assert len(out) == 30

    def test_apply_category_caps_limits_news_to_max(self):
        news = [{"category": "tax", "layer": "L3", "final_score": float(i),
                 "source": {"tier": 2}} for i in range(30)]
        out = apply_category_caps(news)
        assert len(out) == 15  # MAX_NEWS_PER_CATEGORY

    def test_apply_category_caps_subcaps_tier4_before_overall_cap(self):
        # tier4 20건 중 상위 5건만 서브캡 통과 → other(8건, 전체 상한 15에 여유 있음)와
        # 합쳐도 그 5건이 최종 결과에 살아남는지 확인.
        tier4 = [{"category": "tax", "layer": "L3", "final_score": float(i),
                  "source": {"tier": 4}} for i in range(20)]
        other = [{"category": "tax", "layer": "L3", "final_score": 1000.0 + i,
                  "source": {"tier": 2}} for i in range(8)]
        out = apply_category_caps(tier4 + other)
        kept_tier4 = [it for it in out if it["source"]["tier"] == 4]
        assert len(kept_tier4) == 5  # MAX_TIER4_PER_CATEGORY
        assert {it["final_score"] for it in kept_tier4} == {15.0, 16.0, 17.0, 18.0, 19.0}
        assert len(out) == 13  # other 8건 + tier4 서브캡 생존 5건, 전체 상한(15) 밑

    def test_apply_category_caps_official_always_ranks_above_news(self):
        items = (
            [{"category": "tax", "layer": "L3", "final_score": 999.0, "source": {"tier": 1}}]
            + [{"category": "tax", "layer": "L1", "final_score": 1.0, "source": {"tier": 1}}]
        )
        out = apply_category_caps(items)
        assert out[0]["layer"] == "L1"

    def test_apply_category_caps_groups_by_category_independently(self):
        items = (
            [{"category": "tax", "layer": "L3", "final_score": float(i), "source": {"tier": 2}} for i in range(20)]
            + [{"category": "kifrs", "layer": "L3", "final_score": float(i), "source": {"tier": 2}} for i in range(3)]
        )
        out = apply_category_caps(items)
        assert sum(1 for it in out if it["category"] == "tax") == 15
        assert sum(1 for it in out if it["category"] == "kifrs") == 3


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
