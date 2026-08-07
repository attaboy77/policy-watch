# -*- coding: utf-8 -*-
"""sources/_utils.py 단위 테스트 (SPEC.md §8 Phase 1 완료 조건)."""
from datetime import date

import pytest

from sources._utils import (
    build_google_query,
    google_news_rss_url,
    build_naver_queries,
    naver_news_api_url,
    match_loose,
    keyword_score,
    matched_keywords,
    classify,
    is_noise,
    trust_of,
    recency_score,
    final_score,
    make_id,
    dedupe,
)
from sources._config import CATEGORIES, NOISE_KEYWORDS


# ── 쿼리 생성 ────────────────────────────────────────────────────────────
class TestBuildGoogleQuery:
    def test_contains_required_and_combine_groups(self):
        q = build_google_query("tax", days=30)
        assert q.startswith("(")
        assert " AND (" in q
        assert "세법" in q
        assert "개정안" in q

    def test_multiword_keywords_are_quoted(self):
        q = build_google_query("tax", days=30)
        assert '"시행령 개정"' in q

    def test_noise_keywords_excluded_with_minus(self):
        q = build_google_query("kifrs")
        for n in NOISE_KEYWORDS:
            token = f'"{n}"' if " " in n else n
            assert f"-{token}" in q

    def test_when_window_present(self):
        assert "when:7d" in build_google_query("esg", days=7)
        assert "when:30d" in build_google_query("esg", days=30)

    def test_all_categories_buildable(self):
        for cat in CATEGORIES:
            q = build_google_query(cat)
            assert q  # 빈 문자열 아님

    def test_google_news_rss_url_is_encoded(self):
        url = google_news_rss_url("tax", days=30)
        assert url.startswith("https://news.google.com/rss/search?q=")
        assert " " not in url  # quote_plus로 인코딩됨
        assert "hl=ko&gl=KR" in url


class TestBuildNaverQueries:
    def test_returns_simple_query_list_no_boolean_syntax(self):
        for cat in CATEGORIES:
            queries = build_naver_queries(cat)
            assert queries == CATEGORIES[cat]["naver_queries"]
            for q in queries:
                # 네이버 API는 AND/OR/괄호 불리언을 지원하지 않으므로 포함 금지
                assert "AND" not in q
                assert "OR" not in q
                assert "(" not in q

    def test_naver_news_api_url_shape(self):
        url = naver_news_api_url("법인세법 개정")
        assert url.startswith("https://openapi.naver.com/v1/search/news.json?")
        assert "query=" in url
        assert "sort=date" in url


# ── 분류 / 키워드 매칭 ──────────────────────────────────────────────────
class TestClassifyAndMatching:
    def test_match_loose_true_on_required_keyword(self):
        assert match_loose("법인세법 시행령 개정안 입법예고", "tax") is True

    def test_match_loose_false_without_required_keyword(self):
        assert match_loose("삼성전자 신제품 출시", "tax") is False

    def test_keyword_score_counts_required_and_combine(self):
        # required 1개(세법) + combine 1개(개정안) = 20 + 10 = 30
        score = keyword_score("세법 개정안 발표", "tax")
        assert score == 30

    def test_keyword_score_capped_at_100(self):
        text = " ".join(CATEGORIES["tax"]["required"] + CATEGORIES["tax"]["combine"])
        assert keyword_score(text, "tax") == 100

    def test_matched_keywords_lists_hits(self):
        hits = matched_keywords("세법 개정안 국세청 발표", "tax")
        assert "세법" in hits
        assert "국세청" in hits
        assert "개정안" in hits

    def test_classify_picks_highest_scoring_category(self):
        # ESG 관련 텍스트는 esg 카테고리로 분류돼야 함
        assert classify("ISSB 지속가능경영 공시기준 로드맵 발표") == "esg"

    def test_classify_returns_none_when_no_match(self):
        assert classify("오늘의 날씨는 맑음입니다") is None

    def test_classify_disambiguates_by_score(self):
        # tax 필수 키워드 2개 + combine 1개(score=50) vs kifrs 필수 1개(score=20)
        text = "세법 국세청 개정안 발표, 회계기준원 참고자료"
        assert classify(text) == "tax"


# ── 노이즈 필터 ──────────────────────────────────────────────────────────
class TestIsNoise:
    def test_noise_keyword_detected_for_default_tier(self):
        assert is_noise("이 종목 테마주 급등", tier=5) is True

    def test_clean_text_not_noise(self):
        assert is_noise("법인세법 시행령 개정안 입법예고", tier=5) is False

    def test_tier1_official_source_exempted_from_noise_filter(self):
        # tier 1(공식기관)은 "주가" 등이 들어가도 걸러지지 않아야 함
        assert is_noise("금융위원회 보도자료: 주가 관련 공시 의무화", tier=1) is False

    def test_all_noise_keywords_individually_detected(self):
        for kw in NOISE_KEYWORDS:
            assert is_noise(f"오늘 {kw} 소식", tier=5) is True


# ── 신뢰도 ───────────────────────────────────────────────────────────────
class TestTrustOf:
    def test_tier1_official_domain(self):
        tier, score, name = trust_of("https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=1")
        assert (tier, score, name) == (1, 100, "국가법령정보센터")

    def test_tier1_without_www(self):
        tier, score, name = trust_of("https://fsc.go.kr/no010101/12345")
        assert (tier, score, name) == (1, 100, "금융위원회")

    def test_tier2_media_domain(self):
        tier, score, name = trust_of("https://www.taxtimes.co.kr/news/article/1")
        assert (tier, score, name) == (2, 80, "한국세정신문")

    def test_tier3_big4_domain(self):
        tier, score, name = trust_of("https://home.kpmg.com/kr/ko/home.html")
        assert tier == 3 and score == 70

    def test_subdomain_matches_registered_domain(self):
        tier, score, name = trust_of("https://news.hankyung.com/article/2026")
        assert (tier, score, name) == (4, 50, "한국경제")

    def test_unknown_domain_falls_back_to_default_tier(self):
        tier, score, name = trust_of("https://random-blog.example.com/post/1")
        assert tier == 5 and score == 20

    def test_empty_url_returns_default(self):
        tier, score, name = trust_of("")
        assert tier == 5 and score == 20

    def test_scheme_less_bare_domain_is_parsed(self):
        # 구글 뉴스 RSS의 <source url="..."> 힌트가 스킴 없이 올 수 있음
        tier, score, name = trust_of("moef.go.kr")
        assert (tier, score, name) == (1, 100, "기획재정부")


# ── 최신성 / 최종 점수 ──────────────────────────────────────────────────
class TestScoring:
    def test_recency_score_today_is_100(self):
        today = date(2026, 8, 7)
        assert recency_score(today, today=today) == 100

    def test_recency_score_decays_6_per_day(self):
        today = date(2026, 8, 7)
        published = date(2026, 8, 6)
        assert recency_score(published, today=today) == 94

    def test_recency_score_floored_at_0(self):
        today = date(2026, 8, 7)
        published = date(2025, 1, 1)
        assert recency_score(published, today=today) == 0

    def test_final_score_formula(self):
        # trust*0.55 + kw*0.30 + rec*0.15
        assert final_score(100, 60, 100) == round(100 * 0.55 + 60 * 0.30 + 100 * 0.15, 2)
        assert final_score(100, 60, 100) == 88.0


# ── 중복 제거 ────────────────────────────────────────────────────────────
class TestDedupe:
    def test_make_id_strips_query_and_fragment(self):
        a = make_id("https://law.go.kr/path?x=1#frag")
        b = make_id("https://law.go.kr/path")
        assert a == b

    def test_make_id_is_case_insensitive_and_trims(self):
        a = make_id("  HTTPS://LAW.GO.KR/PATH  ")
        b = make_id("https://law.go.kr/path")
        assert a == b

    def test_dedupe_removes_exact_id_duplicates_keeps_higher_score(self):
        items = [
            {"id": "dup1", "title": "법인세법 개정", "final_score": 50.0},
            {"id": "dup1", "title": "법인세법 개정(중복)", "final_score": 90.0},
        ]
        out = dedupe(items)
        assert len(out) == 1
        assert out[0]["final_score"] == 90.0

    def test_dedupe_removes_same_title_duplicates_across_sources(self):
        # 공백만 다르고 정규화하면 완전히 동일한 제목 → 중복 제거 대상
        items = [
            {"id": "a1", "title": "법인세법 시행령 일부개정령안 입법예고", "final_score": 70.0},
            {"id": "b2", "title": "법인세법  시행령 일부개정령안  입법예고", "final_score": 85.0},
        ]
        out = dedupe(items)
        assert len(out) == 1
        assert out[0]["id"] == "b2"

    def test_dedupe_keeps_titles_that_differ_even_slightly(self):
        # 제목 전체 비교이므로 뒷부분만 달라도 서로 다른 항목으로 유지
        items = [
            {"id": "a1", "title": "법인세법 시행령 일부개정령안 입법예고 상세내용", "final_score": 70.0},
            {"id": "b2", "title": "법인세법 시행령 일부개정령안 입법예고 다른출처", "final_score": 85.0},
        ]
        out = dedupe(items)
        assert len(out) == 2

    def test_dedupe_keeps_distinct_items_sorted_by_score_desc(self):
        items = [
            {"id": "low", "title": "ESG 공시기준 발표", "final_score": 40.0},
            {"id": "high", "title": "내부회계관리제도 개편", "final_score": 90.0},
        ]
        out = dedupe(items)
        assert [it["id"] for it in out] == ["high", "low"]

    def test_dedupe_empty_input(self):
        assert dedupe([]) == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
