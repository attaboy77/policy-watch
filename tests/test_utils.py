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
    is_admin_noise,
    is_noise_l3,
    trust_of,
    recency_score,
    final_score,
    make_id,
    make_id_exact,
    dedupe,
    compute_stage,
    normalize_news_item,
    finalize_item,
    ITEM_FIELDS,
    extract_title_revision_date,
    is_discussion_material,
    title_similarity,
    clean_title_for_compare,
    extract_subject,
    dedupe_similar_news,
    extract_core_phrase,
    attach_related_news,
    has_regulatory_signal,
    is_corporate_pr,
    is_applicable,
    apply_applicability_gate,
    is_company_event,
    apply_company_event_filter,
    is_event_announcement,
    is_foreign_standard,
    is_local_gov_petition,
    apply_local_gov_petition_filter,
    is_foreign_news_only,
    apply_foreign_news_filter,
    apply_corporate_pr_filter,
)
from sources._config import (CATEGORIES, NOISE_KEYWORDS, ADMIN_NOISE_KEYWORDS,
                             REGULATORY_SIGNALS, APPLICABILITY, COMPANY_EVENTS,
                             FOREIGN_STANDARD_BODIES, LOCAL_GOV_PETITION_KEYWORDS,
                             FOREIGN_NEWS_SIGNALS)


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
        # ADDENDUM-6 §2-3: tax의 required에서 "국세청"(기관명)을 뺐으므로
        # "유권해석"으로 교체(2026-08-31).
        hits = matched_keywords("세법 개정안 유권해석 발표", "tax")
        assert "세법" in hits
        assert "유권해석" in hits
        assert "개정안" in hits

    def test_classify_picks_highest_scoring_category(self):
        # ESG 관련 텍스트는 esg 카테고리로 분류돼야 함
        assert classify("ISSB 지속가능경영 공시기준 로드맵 발표") == "esg"

    def test_classify_returns_none_when_no_match(self):
        assert classify("오늘의 날씨는 맑음입니다") is None

    def test_classify_disambiguates_by_score(self):
        # tax 필수 2개("세법"·"세제개편")+combine 1개("법인세법")=50
        # vs kifrs 필수 1개("K-IFRS")=20. ADDENDUM-6 §2-3: tax의 required에서
        # "국세청"(기관명)을 뺐으므로 "세제개편"으로 교체(2026-08-31). "회계기준원"은
        # §2에서 kifrs required_weak에 추가된 "회계"/"회계기준"과 부분일치가 겹쳐
        # 점수가 예상보다 높아져("개정안"도 kifrs combine "개정"과 겹침) 겹치지 않는
        # "K-IFRS"·"법인세법"으로 교체했다.
        text = "세법 세제개편 법인세법 발표, K-IFRS 참고자료"
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

    def test_exact_subdomain_override_beats_parent_suffix(self):
        # 2026-09-01 실측 버그: "news.kicpa.or.kr"(CPA뉴스 칼럼이 실리는 포털)이
        # tier1 "kicpa.or.kr"(한국공인회계사회 공식 사이트)의 suffix 규칙에 걸려
        # 공식 자료로 오분류됐다. TRUST_TIERS에 등록된 정확 일치(exact match)가
        # 상위 tier의 suffix 규칙보다 우선해야 한다.
        tier, score, name = trust_of("https://news.kicpa.or.kr/news/article/1")
        assert (tier, score, name) == (2, 80, "CPA뉴스")

    def test_parent_domain_still_tier1(self):
        # 위 오버라이드가 kicpa.or.kr 본 도메인 자체(공식 사이트)의 tier1
        # 분류에는 영향을 주지 않아야 한다.
        tier, score, name = trust_of("https://kicpa.or.kr/notice/1")
        assert (tier, score, name) == (1, 100, "한국공인회계사회")


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

    def test_make_id_exact_keeps_query_string(self):
        # law.go.kr?lsiSeq=처럼 쿼리 자체가 식별자인 URL은 make_id()로 뭉개진다 —
        # make_id_exact()는 그러지 않아야 한다(실측 버그: law_api.py 18건 → 1건으로 뭉개짐).
        a = make_id_exact("https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=1")
        b = make_id_exact("https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=2")
        assert a != b

    def test_make_id_exact_is_case_insensitive_and_trims(self):
        a = make_id_exact("  HTTPS://LAW.GO.KR/PATH?X=1  ")
        b = make_id_exact("https://law.go.kr/path?x=1")
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


# ── stage 판정 (ADDENDUM-2 §2-2) ────────────────────────────────────────────
class TestComputeStage:
    @pytest.mark.parametrize("doc_type,expected", [
        ("공개초안", "의견수렴"),
        ("검토의견", "의견수렴"),
        ("제·개정", "확정"),
        ("적용지침", "확정"),
        ("모범규준", "확정"),
        ("감사·검토기준", "확정"),
        ("FAQ", "참고"),
        ("해설·교육자료", "참고"),
        ("기사", "참고"),
    ])
    def test_doc_type_maps_to_expected_stage(self, doc_type, expected):
        assert compute_stage(doc_type) == expected

    def test_never_returns_시행예정_or_시행중(self):
        # ADDENDUM-2 §2-2: data.json에는 "확정"까지만 저장, 나머지는 프론트가 계산
        for doc_type in ("제·개정", "적용지침", "공개초안", "FAQ", "기사"):
            assert compute_stage(doc_type) not in ("시행예정", "시행중")


# ── 뉴스(L3) raw item 정규화 ─────────────────────────────────────────────────
class TestNormalizeNewsItem:
    def _raw(self, **overrides):
        base = {
            "id": "newsid1",
            "category": "tax",
            "title": "법인세법 개정안 국회 통과",
            "url": "https://example.com/a",
            "published": date(2026, 8, 20),
            "source_name": "한국경제",
            "source_domain": "hankyung.com",
            "trust_tier": 4,
            "trust_score": 50,
            "keyword_score": 30,
            "matched_keywords": ["법인세법"],
            "is_noise": False,
        }
        base.update(overrides)
        return base

    def test_produces_nested_source_dict(self):
        out = normalize_news_item(self._raw())
        assert out["source"] == {"name": "한국경제", "domain": "hankyung.com", "tier": 4, "type": "news"}

    def test_urls_news_populated_official_null(self):
        out = normalize_news_item(self._raw())
        assert out["urls"] == {"news": "https://example.com/a", "official": None}

    def test_published_at_is_iso_string(self):
        out = normalize_news_item(self._raw())
        assert out["published_at"] == "2026-08-20"

    def test_published_none_when_missing(self):
        out = normalize_news_item(self._raw(published=None))
        assert out["published_at"] is None

    def test_effective_date_always_none(self):
        assert normalize_news_item(self._raw())["effective_date"] is None

    def test_layer_is_l3(self):
        assert normalize_news_item(self._raw())["layer"] == "L3"

    def test_final_score_is_computed(self):
        out = normalize_news_item(self._raw())
        assert isinstance(out["final_score"], float)
        assert out["final_score"] > 0

    def test_law_meta_and_attachments_null(self):
        out = normalize_news_item(self._raw())
        assert out["law_meta"] is None
        assert out["attachments"] is None


# ── 최종 스키마 필드 화이트리스트 ────────────────────────────────────────────
class TestFinalizeItem:
    def _item(self, **overrides):
        base = {
            "id": "x1", "category": "tax", "doc_type": "제·개정", "title": "제목",
            "summary": [], "impact": None, "published_at": "2026-08-20",
            "collected_at": "2026-08-26T10:00:00+09:00", "effective_date": None,
            "source": {"name": "국세청", "domain": "nts.go.kr", "tier": 1, "type": "official"},
            "trust_score": 100, "keyword_score": 0, "final_score": 55.0,
            "matched_keywords": [], "urls": {"news": None, "official": None},
            "law_meta": None, "attachments": None,
            "layer": "L1", "is_noise": False, "_body": "내부용 스크래치 필드",
        }
        base.update(overrides)
        return base

    def test_strips_internal_fields(self):
        out = finalize_item(self._item())
        assert "layer" not in out
        assert "is_noise" not in out
        assert "_body" not in out

    def test_keeps_only_whitelisted_fields(self):
        out = finalize_item(self._item())
        assert set(out.keys()) == set(ITEM_FIELDS)

    def test_computes_stage_field(self):
        out = finalize_item(self._item(doc_type="공개초안"))
        assert out["stage"] == "의견수렴"

    def test_published_at_falls_back_to_collected_at_date(self):
        out = finalize_item(self._item(published_at=None))
        assert out["published_at"] == "2026-08-26"

    def test_published_at_kept_when_present(self):
        out = finalize_item(self._item(published_at="2025-01-01"))
        assert out["published_at"] == "2025-01-01"

    # ── KSSB 자발적용 → esg_roadmap.yml 시행일 채움 (2026-09-02 사용자 지시) ──
    # 실제 파일 내용에 값을 결합하지 않도록 로드맵을 직접 읽어 기대값을 만든다
    # (나중에 esg_roadmap.yml의 날짜가 바뀌어도 이 테스트는 안 깨진다).
    def test_kssb_voluntary_gets_roadmap_effective_date(self):
        from sources._esg_roadmap import load as load_roadmap
        expected_date = load_roadmap()["milestones"][0]["date"]
        out = finalize_item(self._item(doc_type="자발적용", effective_date=None))
        assert out["effective_date"] == expected_date
        assert out["is_roadmap_estimate"] is True

    def test_kssb_voluntary_does_not_override_existing_effective_date(self):
        # 이미 진짜 시행일이 있으면(향후 다른 소스가 채울 수도 있음) 로드맵으로
        # 덮어쓰지 않고, is_roadmap_estimate도 false로 둔다(그건 확정 시행일이므로).
        out = finalize_item(self._item(doc_type="자발적용", effective_date="2027-06-01"))
        assert out["effective_date"] == "2027-06-01"
        assert out["is_roadmap_estimate"] is False

    def test_non_voluntary_doc_type_unaffected_by_roadmap(self):
        out = finalize_item(self._item(doc_type="제·개정", effective_date=None))
        assert out["effective_date"] is None
        assert out["is_roadmap_estimate"] is False

    # ── 사업연도 기준 근사 시행일 (2026-09-02 사용자 지시) ────────────────────
    # _FISCAL_YEAR_EFFECTIVE_DATES는 특정 id를 직접 키로 쓰는 수동 매핑이라
    # 그 id 중 하나를 그대로 써서 검증한다.
    def test_fiscal_year_mapped_id_gets_effective_date_and_note(self):
        out = finalize_item(self._item(id="9204a2cb8d4f8a52", effective_date=None))
        assert out["effective_date"] == "2024-01-01"
        assert out["effective_date_note"] == "적용: 2024.1.1 이후 개시 사업연도부터"

    def test_fiscal_year_mapping_does_not_override_existing_effective_date(self):
        out = finalize_item(self._item(id="9204a2cb8d4f8a52", effective_date="2025-03-01"))
        assert out["effective_date"] == "2025-03-01"
        assert out["effective_date_note"] is None

    def test_unmapped_id_gets_no_note(self):
        out = finalize_item(self._item(id="some-other-id", effective_date=None))
        assert out["effective_date_note"] is None


# ── 조직 운영성 공지 제외 (ADDENDUM-4 §1) ────────────────────────────────────
class TestIsAdminNoise:
    def test_hr_notice_excluded(self):
        assert is_admin_noise("금융위원회 인사보도(과장급 전보)") is True

    def test_maintenance_notice_excluded(self):
        assert is_admin_noise("본인 인증 서비스 일시 점검 안내") is True

    def test_real_meeting_result_passes(self):
        assert is_admin_noise("회계기준위원회 제12차 회의 결과") is False

    def test_industry_forum_passes(self):
        assert is_admin_noise("ESG 공시 관련 업계 간담회 결과 발표") is False

    def test_all_keywords_individually_detected(self):
        for kw in ADMIN_NOISE_KEYWORDS:
            assert is_admin_noise(f"{kw} 관련 공지") is True

    def test_committee_appointment_excluded(self):
        # 2026-09-01 사용자 지시: 위촉 소식은 제도 변경이 아닌 인사 소식.
        assert is_admin_noise("회계기준원, 지속가능성기준 자문위원 10명 위촉") is True

    def test_noise_l3_applies_admin_noise_even_for_tier1(self):
        # tier==1(L1 공식기관)은 NOISE_KEYWORDS는 면제지만 admin noise는 아니다.
        assert is_noise_l3("금융위원회 인사보도(과장급 전보)", tier=1, category="kifrs") is True


# ── 제목에서 개정·제정일 추출 (ADDENDUM-4 §2-1) ──────────────────────────────
class TestExtractTitleRevisionDate:
    def test_4digit_year_with_periods(self):
        assert extract_title_revision_date("내부회계관리제도 모범규준 전문(2021.10.1. 개정)") == "2021-10-01"

    def test_2digit_year_with_quote(self):
        assert extract_title_revision_date("평가·보고 가이드라인('24.12.23 개정)") == "2024-12-23"

    def test_4digit_year_with_spaces(self):
        assert extract_title_revision_date("설계·운영 모범규준(2023. 6. 30. 제정)") == "2023-06-30"

    def test_clean_ver_without_keyword(self):
        assert extract_title_revision_date("Clean ver.('24.12.23)") == "2024-12-23"

    def test_year_month_without_day_defaults_to_1st(self):
        # 2026-08-28 실사용 확인: 일자 없는 "(2012.12)" 형태를 놓쳐 오늘 날짜로 새면서
        # 최근 90일 필터를 통과하는 버그가 있었다.
        assert extract_title_revision_date("내부회계관리제도 모범규준(2012.12)") == "2012-12-01"

    def test_year_month_single_digit_month(self):
        assert extract_title_revision_date("新내부회계관리제도 모범규준(2018.6)") == "2018-06-01"

    def test_no_date_returns_none(self):
        assert extract_title_revision_date("내부회계관리제도 평가 가이드라인") is None


# ── 유사 기사 중복 제거 (ADDENDUM-4 §3) ──────────────────────────────────────
class TestTitleSimilarity:
    def test_near_duplicate_headlines_are_similar(self):
        a = "남부발전, 내부통제 고도화 '앞장'…6대 중점관리 분야 분과위 가동"
        b = "남부발전, 내부통제 고도화 위한 '6대 중점관리 분야' 분과위 가동"
        assert title_similarity(a, b) >= 0.65

    def test_different_topics_not_similar(self):
        a = "법인세법 시행령 개정안 입법예고 — 접대비 한도"
        b = "법인세법 시행령 개정안 입법예고 — 감가상각 특례"
        assert title_similarity(a, b) < 0.65

    def test_empty_strings_zero_similarity(self):
        assert title_similarity("", "아무거나") == 0.0


class TestDedupeSimilarNews:
    def _news(self, id_, title, score, published_at="2026-08-20", category="icfr", trust_score=0):
        return {
            "id": id_, "category": category, "title": title, "final_score": score,
            "trust_score": trust_score,
            "published_at": published_at, "source": {"name": id_}, "layer": "L3",
        }

    def test_merges_near_duplicate_l3_within_category_and_window(self):
        items = [
            self._news("a", "남부발전, 내부통제 고도화 '앞장'…6대 중점관리 분야 분과위 가동", 80.0),
            self._news("b", "남부발전, 내부통제 고도화 위한 '6대 중점관리 분야' 분과위 가동", 60.0),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 1
        assert out[0]["id"] == "a"  # final_score가 높은 쪽이 남는다
        assert out[0]["duplicate_count"] == 1
        assert "b" in out[0]["duplicate_sources"]

    def test_does_not_merge_across_categories(self):
        items = [
            self._news("a", "동일한 제목의 기사입니다", 80.0, category="icfr"),
            self._news("b", "동일한 제목의 기사입니다", 60.0, category="esg"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 2

    def test_condition_a_merges_regardless_of_day_gap(self):
        # ADDENDUM-5 §5-3 조건(a)는 유사도만 보고 날짜는 안 본다 — 20일 떨어져
        # 있어도 유사도(0.55 이상)만 넘으면 병합된다(조건 (b)와 다른 점).
        items = [
            self._news("a", "남부발전, 내부통제 고도화 '앞장'…6대 중점관리 분야 분과위 가동", 80.0, published_at="2026-08-01"),
            self._news("b", "남부발전, 내부통제 고도화 위한 '6대 중점관리 분야' 분과위 가동", 60.0, published_at="2026-08-20"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 1

    def test_condition_b_requires_day_window_for_moderate_similarity(self):
        # 같은 주체 + 유사도 0.375(0.35~0.55 사이, 조건 a는 미달) → 조건(b) 적용,
        # 3일보다 멀면 안 묶인다.
        items = [
            self._news("a", "남부발전, 알파베타 감마델타 입실론", 80.0, published_at="2026-08-01"),
            self._news("b", "남부발전, 알파베타 감마델타 제타에타 세타요타 카파람다 뮤뉴크시", 60.0, published_at="2026-08-20"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 2

    def test_condition_b_merges_within_day_window_for_moderate_similarity(self):
        items = [
            self._news("a", "남부발전, 알파베타 감마델타 입실론", 80.0, published_at="2026-08-18"),
            self._news("b", "남부발전, 알파베타 감마델타 제타에타 세타요타 카파람다 뮤뉴크시", 60.0, published_at="2026-08-20"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 1

    def test_no_subject_and_moderate_similarity_does_not_merge(self):
        # 주체가 없으면 조건(b) 자체가 적용 안 됨 — ESG 로드맵 예시(ADDENDUM-5 §5-4).
        items = [
            self._news("a", "ESG 공시 로드맵 연기", 80.0, category="esg"),
            self._news("b", "ESG 공시 의무화 로드맵 핵심쟁점 6가지", 60.0, category="esg"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 2

    def test_media_suffix_stripped_before_comparison(self):
        items = [
            self._news("a", "남부발전, 내부통제 고도화 위한 분과위 가동 - 스트레이트뉴스", 80.0),
            self._news("b", "남부발전, 내부통제 고도화 위한 분과위 가동 - 에너지플랫폼뉴스", 60.0),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 1

    def test_over_merge_guard_different_content_with_dash_suffix_shape(self):
        # ADDENDUM-5 §5-4: "법인세법 시행령 개정안 — 접대비 한도" 류는 매체명이 아닌
        # 실제 내용 차이인데, 원안 정규식(공백 허용)대로면 "접대비 한도"/"감가상각
        # 특례"가 매체명처럼 잘려나가 오탐 병합된다 — 그러면 안 된다.
        items = [
            self._news("a", "법인세법 시행령 개정안 — 접대비 한도", 80.0, category="tax"),
            self._news("b", "법인세법 시행령 개정안 — 감가상각 특례", 60.0, category="tax"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 2

    def test_l1_l2_items_untouched(self):
        items = [
            {"id": "l1a", "category": "tax", "title": "법인세법 개정", "final_score": 90.0,
             "published_at": "2026-08-20", "source": {"name": "국세청"}, "layer": "L1"},
        ]
        out = dedupe_similar_news(items)
        assert out == items

    def test_local_gov_subject_merges_below_normal_subject_threshold(self):
        # 2026-09-02 사용자 지시 — 실측: 두 기사 모두 주체는 "송파구"로 정확히
        # 일치하지만 어절 유사도가 0.25로 일반 SUBJECT_SIMILARITY_THRESHOLD(0.35)
        # 에 못 미친다. 기초자치단체 주체는 LOCAL_GOV_SUBJECT_SIMILARITY_
        # THRESHOLD(0.20)를 적용해 병합돼야 한다.
        items = [
            self._news("gukjenews", "송파구, 신축주택 재산세 급증 막는다…지방세법 시행령 개정 건의",
                       80.0, category="tax", published_at="2026-08-24"),
            self._news("jeonmae", "송파구, 신축주택 과세표준 상한 적용 건의",
                       60.0, category="tax", published_at="2026-08-24"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 1
        assert out[0]["duplicate_count"] == 1

    def test_non_local_gov_subject_still_uses_normal_threshold(self):
        # 위 완화가 "주체 일치 + 낮은 유사도"를 전부 다 묶어버리는 건 아니어야
        # 한다 — 위 송파구 예시와 같은 구조(같은 어절 집합, 주체만 교체)를
        # 기업 주체(남부발전)로 바꿔 유사도 0.25를 유지한 채로 확인: 기업
        # 주체는 기존 임계값(0.35) 그대로라 병합되면 안 된다.
        items = [
            self._news("a", "남부발전, 신축주택 재산세 급증 막는다…지방세법 시행령 개정 건의",
                       80.0, category="tax", published_at="2026-08-24"),
            self._news("b", "남부발전, 신축주택 과세표준 상한 적용 건의",
                       60.0, category="tax", published_at="2026-08-24"),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 2  # 유사도 0.25 < 0.35 + 기업 주체라 병합 안 됨(기존 동작 유지)

    def test_higher_trust_source_survives_even_with_lower_final_score(self):
        # 2026-09-02 사용자 지시 — "신뢰도 높은 매체를 우선". trust_score가 높으면
        # final_score가 더 낮아도 대표로 남아야 한다(기존엔 final_score만 봄).
        items = [
            self._news("low_trust_high_score", "동일한 제목의 기사입니다", 90.0, trust_score=20),
            self._news("high_trust_low_score", "동일한 제목의 기사입니다", 50.0, trust_score=80),
        ]
        out = dedupe_similar_news(items)
        assert len(out) == 1
        assert out[0]["id"] == "high_trust_low_score"


# ── 공식-뉴스 연결 (ADDENDUM-4 §4) ───────────────────────────────────────────
class TestAttachRelatedNews:
    def _official(self, title="지속가능성 공시기준 제2호 공개초안 발표", published_at="2026-08-20", category="esg"):
        return {
            "id": "off1", "category": category, "title": title, "final_score": 90.0,
            "published_at": published_at, "source": {"name": "금융위원회"},
            "urls": {"news": None, "official": "https://fsc.go.kr/x"}, "layer": "L1",
        }

    def _news(self, id_, title, published_at="2026-08-20", category="esg", score=60.0):
        return {
            "id": id_, "category": category, "title": title, "final_score": score,
            "published_at": published_at, "source": {"name": "임팩트온"},
            "urls": {"news": f"https://impacton.net/{id_}", "official": None}, "layer": "L3",
        }

    def test_links_matching_news_and_removes_it_from_feed(self):
        off = self._official()
        news = self._news("n1", "지속가능성 공시기준 제2호 공개초안 관련 해설")
        out = attach_related_news([off, news])
        assert [it["id"] for it in out] == ["off1"]  # n1은 피드에서 빠짐
        assert len(off["related_news"]) == 1
        assert off["related_news"][0]["title"] == news["title"]
        assert off["related_news"][0]["source"] == "임팩트온"

    def test_unrelated_news_not_linked_and_stays_in_feed(self):
        off = self._official()
        news = self._news("n2", "전혀 관련 없는 다른 주제의 기사")
        out = attach_related_news([off, news])
        assert off["related_news"] == []
        assert "n2" in [it["id"] for it in out]

    def test_max_3_related_news_sorted_by_final_score(self):
        off = self._official()
        candidates = [self._news(f"n{i}", "지속가능성 공시기준 제2호 공개초안 후속보도", score=float(i))
                      for i in range(1, 6)]
        attach_related_news([off] + candidates)
        assert len(off["related_news"]) == 3
        assert off["related_news"][0]["title"] == candidates[-1]["title"]  # score 5.0이 최상위

    def test_different_category_not_linked(self):
        off = self._official(category="esg")
        news = self._news("n3", "지속가능성 공시기준 제2호 공개초안 후속", category="tax")
        attach_related_news([off, news])
        assert off["related_news"] == []

    def test_outside_day_window_not_linked(self):
        off = self._official(published_at="2026-08-20")
        news = self._news("n4", "지속가능성 공시기준 제2호 공개초안 관련", published_at="2026-07-01")
        attach_related_news([off, news])
        assert off["related_news"] == []


class TestExtractCorePhrase:
    def test_strips_org_name_and_keeps_leading_words(self):
        phrase = extract_core_phrase("금융위원회 지속가능성 공시기준 제2호 공개초안 발표")
        assert phrase == "지속가능성 공시기준 제2호 공개초안"

    def test_too_short_returns_none(self):
        assert extract_core_phrase("금융위원회 발표") is None


# ── required_strong/required_weak 문맥 게이팅 (SPEC-ADDENDUM-5.md §4) ───────
class TestRequiredStrongWeakGating:
    # icfr: "내부통제"는 회계 문맥(weak_context) 없이는 통과 못 함(§4-3)
    def test_icfr_weak_keyword_without_context_fails(self):
        assert match_loose("타에브의 바시즈 사령관 복귀, 모즈타바의 내부 통제 강화 포석", "icfr") is False

    def test_icfr_weak_keyword_without_context_fails_corporate_pr_case(self):
        assert match_loose("남부발전, 내부통제 고도화 위한 분과위 가동", "icfr") is False

    def test_icfr_weak_keyword_with_context_passes(self):
        assert match_loose("금융지주 내부통제 강화…감사위원회 역할 확대", "icfr") is True

    def test_icfr_strong_keyword_passes_without_context(self):
        assert match_loose("내부회계관리제도 평가·보고 지침 개정", "icfr") is True

    def test_icfr_classify_drops_military_article_entirely(self):
        # §4 효과: 이 카테고리뿐 아니라 classify() 전체에서 걸리는 카테고리가 없어야 한다.
        assert classify("타에브의 바시즈 사령관 복귀, 모즈타바의 내부 통제 강화 포석") is None

    # kifrs: "금융위원회"/"금융감독원"도 동일 원칙(§4-4)
    def test_kifrs_weak_keyword_without_context_fails(self):
        assert match_loose("금융위원회, 부동산 PF 대책 발표", "kifrs") is False

    def test_kifrs_weak_keyword_with_context_passes(self):
        assert match_loose("금융위원회 재무제표 공시 관련 지침 개정", "kifrs") is True

    def test_kifrs_strong_keyword_passes_without_context(self):
        assert match_loose("K-IFRS 제1116호 리스 기준 개정", "kifrs") is True

    def test_keyword_score_uses_combined_strong_and_weak_list(self):
        # required_strong 1개("회계기준원") 히트 → hit_req=1 → 최소 20점 이상.
        score = keyword_score("회계기준원 참고자료", "kifrs")
        assert score >= 20

    def test_matched_keywords_includes_strong_hits(self):
        hits = matched_keywords("내부회계관리제도 평가 지침", "icfr")
        assert "내부회계관리제도" in hits

    def test_google_query_still_buildable_for_split_categories(self):
        for cat in ("kifrs", "icfr"):
            q = build_google_query(cat)
            assert q.startswith("(") and " AND (" in q


# ── 기관명 키워드 제거 (SPEC-ADDENDUM-6.md §2) ────────────────────────────────
# §0-1 실측 오탐 3건 + §8 테스트 필수 케이스. "금융위원회"/"금융감독원"을 kifrs
# 매칭 키워드에서 완전히 제거하고 내용 키워드(§2-2)로 대체한 효과를 검증한다.
class TestInstitutionNameRemoved:
    def test_financial_regulation_by_fsc_not_classified_as_kifrs(self):
        # §0-1 실측 오탐 1: 대부업법은 금융업 규제이지 회계기준이 아니다.
        assert classify("금융위, 대부업법 개정해 신협도 부실채권 전담기관 허용") != "kifrs"

    def test_supervisory_regulation_not_classified_as_kifrs(self):
        # §0-1 실측 오탐 2: "감독규정"은 weak_context 시절 "회계"류와 우연히
        # 안 겹쳤을 뿐 회계기준 개정이 아니다.
        assert classify("신협자산관리회사, 대부채권 양도…금융위 감독규정 개정 예고") != "kifrs"

    def test_capital_market_policy_not_classified_as_kifrs(self):
        # §0-1 실측 오탐 3: 저PBR 공표제도는 자본시장 정책이지 회계기준이 아니다.
        assert classify('금융위 "저PBR기업 공표제도 세부기준(안)" 의견수렴') != "kifrs"

    def test_fsc_accounting_regulation_still_classified_as_kifrs(self):
        # §8 통과 예시: 기관명 없이도 "외부감사"·"회계" 내용 키워드로 잡혀야 한다.
        assert classify("금융위, 외부감사 및 회계 등에 관한 규정 개정") == "kifrs"

    def test_law_reform_still_classified_as_tax(self):
        # §8 통과 예시: tax에서 "국세청"을 빼도 세법 자체 키워드로는 정상 분류돼야 한다.
        assert classify("법인세법 시행령 개정안 입법예고") == "tax"


# ── 기관 홍보·외교 활동 제외 (SPEC-ADDENDUM-6.md §3) ─────────────────────────
class TestPromotionalActivityAdminNoise:
    def test_tax_administration_export_pr_is_admin_noise(self):
        # §0-1/§8 실측 오탐: 규제 변경이 아니라 기관의 대외 활동 홍보.
        assert is_admin_noise("글로벌최저한세, 한국 국세청의 선진 세정경험 수출") is True

    def test_core_tax_terms_not_removed(self):
        # §3-2 주의사항: "국제조세"·"조세조약"·"글로벌최저한세" 자체는 실무
        # 관련성이 높으므로 제거하지 않는다 — 홍보 표현이 없으면 admin_noise가
        # 아니어야 한다.
        for term in ("국제조세", "조세조약", "글로벌최저한세"):
            assert is_admin_noise(f"{term} 관련 개정안 발표") is False

    def test_all_new_keywords_individually_detected(self):
        new_keywords = ["세정경험", "경험 수출", "우수사례 공유", "국제협력",
                        "기술협력", "초청 연수", "방한", "방문단", "업무협약 체결",
                        "양해각서", "공동선언", "국제기구 진출", "수상", "표창"]
        for kw in new_keywords:
            assert is_admin_noise(f"{kw} 관련 소식") is True


# ── 적용 대상 판정 게이트 (SPEC-ADDENDUM-6.md §1) ────────────────────────────
class TestIsApplicable:
    def test_financial_regulation_excluded(self):
        ok, reason = is_applicable("금융위, 대부업법 개정해 신협도 부실채권 전담기관 허용")
        assert ok is False
        assert reason == "excluded:financial"

    def test_supervisory_regulation_excluded(self):
        ok, reason = is_applicable("신협자산관리회사, 대부채권 양도…금융위 감독규정 개정 예고")
        assert ok is False
        assert reason == "excluded:financial"

    def test_nonprofit_excluded(self):
        ok, reason = is_applicable("사회복지법인 전문인력 확보 절실…법인세법 시행령 개정 선행돼야")
        assert ok is False
        assert reason == "excluded:nonprofit"

    def test_foreign_jurisdiction_excluded(self):
        ok, reason = is_applicable("EFRAG, 비EU 기업 대상 ESRS-40a 공개초안")
        assert ok is False
        assert reason == "excluded:foreign"

    def test_foreign_jurisdiction_with_domestic_context_passes(self):
        # §8 통과 예시: 해외 관할이라도 국내 도입 맥락이 함께 있으면 예외.
        ok, reason = is_applicable("EU CSRD 국내 도입 영향…금융위 검토 착수")
        assert ok is True
        assert reason is None

    def test_tax_law_reform_passes(self):
        ok, reason = is_applicable("법인세법 시행령 개정안 입법예고")
        assert ok is True
        assert reason is None

    def test_kssb_disclosure_standard_passes(self):
        ok, reason = is_applicable("KSSB, 지속가능성 공시기준 제2호 공개초안")
        assert ok is True
        assert reason is None

    def test_all_excluded_entity_keywords_individually_detected(self):
        for scope, kws in APPLICABILITY["excluded_entities"].items():
            for kw in kws:
                ok, reason = is_applicable(f"{kw} 관련 개정 소식")
                assert ok is False, f"{kw}가 통과됨(scope={scope})"
                assert reason == f"excluded:{scope}"

    def test_all_foreign_jurisdiction_keywords_individually_detected(self):
        for kw in APPLICABILITY["foreign_jurisdiction"]:
            ok, reason = is_applicable(f"{kw} 관련 공개초안 발표")
            assert ok is False, f"{kw}가 통과됨"
            assert reason == "excluded:foreign"

    def test_apply_applicability_gate_splits_kept_and_excluded(self):
        items = [
            {"category": "kifrs", "title": "K-IFRS 제1118호 기준서 개정"},
            {"category": "kifrs", "title": "신협, 대부채권 양도 감독규정 개정"},
        ]
        kept, excluded = apply_applicability_gate(items)
        assert [it["title"] for it in kept] == ["K-IFRS 제1118호 기준서 개정"]
        assert len(excluded) == 1
        assert excluded[0]["excluded_reason"] == "excluded:financial"

    # ── 업종 특화 감리·회계 제외 (SPEC-ADDENDUM-7.md §2) ────────────────────
    def test_public_apartment_audit_excluded(self):
        ok, reason = is_applicable("한국공인회계사회, 2025년 공동주택 감리 지적사례 공개")
        assert ok is False
        assert reason == "excluded:industry_specific"

    def test_all_industry_specific_keywords_individually_detected(self):
        for kw in APPLICABILITY["excluded_entities"]["industry_specific"]:
            ok, reason = is_applicable(f"{kw} 관련 개정 소식")
            assert ok is False, f"{kw}가 통과됨"
            assert reason == "excluded:industry_specific"

    def test_labor_union_not_excluded_by_industry_specific(self):
        # §2-2 주의: "조합" 단독은 목록에 없어 "노동조합"/"조합원"은 안 걸려야 한다.
        ok, reason = is_applicable("노동조합 임금교섭 타결, 조합원 총회 개최")
        assert ok is True
        assert reason is None

    # ── K-IFRS 업종 특화 기준서 제외 (2026-09-02 사용자 지시) ──────────────────
    def test_insurance_standard_1117_excluded(self):
        ok, reason = is_applicable("2025년 제1117호 보험계약")
        assert ok is False
        assert reason == "excluded:industry_specific"

    def test_insurance_standard_1104_excluded(self):
        ok, reason = is_applicable("2017년 제1104호 '보험계약'과 제1109호 '금융상품'의 동시 적용")
        assert ok is False
        assert reason == "excluded:industry_specific"

    def test_construction_arrangement_2115_excluded(self):
        ok, reason = is_applicable(
            "2015년 건설계약 공시 (제1011호 건설계약, 제2115호 부동산건설약정)"
        )
        assert ok is False
        assert reason == "excluded:industry_specific"

    def test_interest_rate_benchmark_reform_not_excluded_despite_mentioning_1104(self):
        # 실측 오탐 방지: "이자율지표 개혁" 항목은 제1104호(보험계약)를 여러
        # 개정 대상 기준서 중 하나로만 나열할 뿐, 내용은 금리지표 개혁(모든
        # 업종의 변동금리 금융상품·헤지회계에 영향)이라 제외하면 안 된다.
        ok, reason = is_applicable(
            "2020년 이자율지표 개혁 - 2단계 (제1039호 금융상품: 인식과측정, "
            "제1104호 보험계약, 제1107호 금융상품: 공시, 제1109호 금융상품, 제1116호 리스)"
        )
        assert ok is True
        assert reason is None

    def test_agriculture_annual_improvements_not_excluded(self):
        # 농림어업(제1041호)은 애매해서(종자 사업 관련 가능성) 목록에 안 넣었다
        # — 이 회귀 테스트가 그 결정을 고정한다.
        ok, reason = is_applicable(
            "2020년 한국채택국제회계기준 2018-2020 연차개선 (제1041호 농림어업, "
            "제1101호 한국채택국제회계기준의 최초채택, 제1109호 금융상품, 제1116호 리스)"
        )
        assert ok is True
        assert reason is None


# ── 개별 기업 소식 제외 (SPEC-ADDENDUM-7.md §1) ──────────────────────────────
class TestIsCompanyEvent:
    def test_ipo_denial_excluded(self):
        assert is_company_event('두나무 "美 상장 확정 아냐…회계기준 전환도 사실무근"') is True

    def test_market_panic_headline_excluded(self):
        assert is_company_event("삼전닉스에 몰려 '재무제표' 발표가 두려운 기업들…흑자도산 공포") is True

    def test_manufacturing_accounting_context_passes_despite_company_event_keyword(self):
        # §1-2 제조업 회계 예외: "인수"가 있어도 재고자산 문맥이면 통과.
        assert is_company_event("A사, 재고자산 저가법 적용 오류로 감리 지적") is False

    def test_strong_regulatory_signal_passes_despite_company_event_keyword(self):
        assert is_company_event("상장기업 재고자산 평가 관련 K-IFRS 질의회신 공개") is False

    def test_no_company_event_keyword_passes(self):
        assert is_company_event("법인세법 시행령 개정안 입법예고") is False

    def test_all_company_event_keywords_individually_detected(self):
        for kw in COMPANY_EVENTS:
            assert is_company_event(f"{kw} 관련 소식") is True, f"{kw}가 통과됨"

    # ── "상장"/"비상" 부분일치 오탐 회귀 테스트 (2026-08-31 실측으로 발견) ────
    def test_listed_company_noun_not_excluded(self):
        # "상장사"는 "상장 이벤트"가 아니라 그냥 "상장된 회사"를 가리키는 일반
        # 명사 — 퍼센트·통계 문구가 없는 제목으로 "상장" 부정 전방탐색만 검증한다
        # (원래 이 테스트가 쓰던 "…감사의견 '적정' 97%…" 제목은 2026-09-01
        # 사용자가 실제 화면에서 재확인해 통계 기사로 재분류했다 — 아래
        # test_audit_opinion_statistics_with_kifrs_context_now_excluded 참고).
        assert is_company_event("상장사 재고자산 평가 관련 새로운 K-IFRS 도입 검토") is False

    def test_non_listed_company_noun_not_excluded(self):
        # "비상장회사"도 "비상"(긴급) 오탐 + "상장"(공모) 오탐 둘 다 없어야 한다.
        assert is_company_event("신외감법 시행으로 비상장회사 규제비용 증가") is False

    def test_listing_confirmation_still_excluded(self):
        # "상장" 뒤에 회사 관련 명사가 안 붙으면(공백·"확정" 등) 실제 이벤트로 본다.
        assert is_company_event("OO기업, 코스닥 상장 확정") is True

    def test_kifrs_series_explainer_not_excluded_by_operating_profit(self):
        # "영업이익"은 실적 발표 신호이자 K-IFRS 제1118호 손익계산서 개편의 핵심
        # 용어이기도 하다 — K-IFRS 시리즈 해설 기사가 오탐 제외되던 걸 실측 확인.
        assert is_company_event("[K-IFRS 제1118호 시리즈] 두 개의 영업이익") is False

    def test_apply_company_event_filter_l3_only(self):
        items = [
            {"category": "kifrs", "title": "두나무 상장 준비", "layer": "L3",
             "source": {"tier": 5}},
            {"category": "kifrs", "title": "K-IFRS 제1118호 개정 공표", "layer": "L1",
             "source": {"tier": 1}},
        ]
        kept = apply_company_event_filter(items)
        assert [it["title"] for it in kept] == ["K-IFRS 제1118호 개정 공표"]

    # ── 제재·감리 결과 + 집계·통계성 보도 제외 (2026-09-01 사용자 지시) ────────
    def test_named_company_sanction_excluded(self):
        assert is_company_event("영풍 회계처리 위반 중징계") is True

    def test_named_company_audit_finding_excluded(self):
        assert is_company_event("증선위, 만호제강 회계기준 위반 적발") is True

    def test_sanction_policy_change_passes_via_override(self):
        # "제재" 자체는 목록에 없지만, 그 결과인 "과징금"이 있어도 "개정"/"의결"
        # 같은 제도 변경 신호가 있으면 정책 기사로 보고 제외하지 않는다.
        assert is_company_event("회계처리기준 위반 시 제재 양정기준 개정안 의결") is False

    def test_audit_opinion_statistics_excluded(self):
        # 실측: 사용자가 보고한 바로 그 헤드라인 — 정책 연결 없는 순수 통계 보도.
        assert is_company_event("상장사 감사의견 '적정' 97%") is True

    def test_audit_opinion_statistics_with_kifrs_context_now_excluded(self):
        # 2026-08-31 세션은 이 제목을 "K-IFRS 오버라이드로 통과시켜야 할 정상
        # 기사"로 판단했었는데, 2026-09-01 사용자가 실제 화면에서 이 기사를
        # 다시 보고 "감사의견 통계 기사일 뿐"이라고 재확인해 결정을 뒤집었다 —
        # 감사의견 통계 리드(_AUDIT_OPINION_STATS_RE)는 뒤에 K-IFRS가 언급돼도
        # STRONG_SIGNALS 오버라이드 없이 항상 제외한다.
        assert is_company_event(
            "상장사 감사의견 '적정' 97%…내년 새로운 K-IFRS 도입에 손익계산서 변경"
        ) is True

    def test_generic_stat_signal_still_respects_override(self):
        # _AUDIT_OPINION_STATS_RE(감사의견+의견유형+퍼센트)와 달리, 좀 더 느슨한
        # "퍼센트 + STATISTICAL_REPORT_SIGNALS" 조합은 여전히 STRONG_SIGNALS
        # 오버라이드를 존중한다 — 진짜 정책 기사(개정안)까지 지우면 안 되니까.
        assert is_company_event(
            "실태조사 결과 회계기준 위반 30%…양정기준 개정안 마련"
        ) is False

    def test_bare_percent_without_stat_signal_not_excluded(self):
        # 퍼센트 수치만으로는 통계 보도로 안 본다(세율 인상 등 진짜 정책 기사가
        # 훨씬 흔하다) — STATISTICAL_REPORT_SIGNALS과 함께 있을 때만 잡는다.
        assert is_company_event("법인세율 25%로 인상하는 개정안 국회 통과") is False


# ── 행사·포럼 안내 제외 보강 (SPEC-ADDENDUM-7.md §4) ─────────────────────────
class TestIsEventAnnouncement:
    def test_forum_name_excluded(self):
        assert is_event_announcement("한국회계기준원, 제149회 KAI Forum: IASB 공개초안 '위험경감회계' 개최") is True

    def test_serial_number_with_strong_signal_passes(self):
        assert is_event_announcement("회계기준위원회 제12차 회의, 제1116호 개정 의결") is False

    def test_admin_noise_still_excluded(self):
        # is_admin_noise()의 상위 호환이므로 기존 케이스도 그대로 걸려야 한다.
        assert is_event_announcement("금융위원회 인사보도(과장급 전보)") is True

    def test_no_serial_no_keyword_passes(self):
        assert is_event_announcement("재무제표 중점심사 회계이슈 사전예고") is False


# ── 해외 기준 처리 — 안 A (SPEC-ADDENDUM-7.md §3) ────────────────────────────
class TestIsForeignStandard:
    def test_iasb_exposure_draft_is_foreign_standard(self):
        assert is_foreign_standard("IASB 공개초안 '위험경감회계(Risk Mitigation Accounting)' 검토의견 조회 기한 연장") is True

    def test_domestic_adoption_context_passes(self):
        # §3-4: 국내 도입 논의는 항상 통과.
        assert is_foreign_standard("IASB 리스 기준 개정, K-IFRS 반영 시기는") is False

    def test_no_foreign_body_passes(self):
        assert is_foreign_standard("KSSB, 지속가능성 공시기준 제2호 공개초안") is False

    def test_domestic_committee_reporting_on_issb_passes(self):
        # KASB "주요일정" 게시판 연동(2026-08-31) 이후 실측: 지속가능성기준위원회
        # 자체 회의 안건에 ISSB가 언급돼도 국내 절차이지 해외기준이 아니다.
        assert is_foreign_standard("2026년 제6회 지속가능성기준위원회(ISSB 6월 주요 논의내용 및 회의결과 보고 등)") is False

    def test_all_foreign_standard_bodies_individually_detected(self):
        for kw in FOREIGN_STANDARD_BODIES:
            assert is_foreign_standard(f"{kw} 공개초안 발표") is True, f"{kw}가 통과됨"

    def test_finalize_item_overrides_doc_type_to_foreign_standard(self):
        item = {
            "id": "x1", "category": "kifrs", "doc_type": "검토의견",
            "title": "IASB 공개초안 '위험경감회계' 검토의견 조회 기한 연장",
            "summary": [], "impact": None, "published_at": "2026-08-20",
            "collected_at": "2026-08-26T10:00:00+09:00", "effective_date": None,
            "source": {"name": "한국회계기준원", "domain": "kasb.or.kr", "tier": 1, "type": "official"},
            "trust_score": 100, "keyword_score": 0, "final_score": 55.0,
            "matched_keywords": [], "urls": {"news": None, "official": None},
            "law_meta": None, "attachments": None, "layer": "L1", "is_noise": False,
        }
        out = finalize_item(item)
        assert out["doc_type"] == "해외기준"


# ── 논의자료(TF·실무그룹 중간 산출물) 판정 (2026-08-28 사용자 피드백) ────────
class TestIsDiscussionMaterial:
    def test_tf_discussion_note_detected(self):
        assert is_discussion_material("제1118호 정착지원 TF 논의 내용(4차)") is True

    def test_kickoff_meeting_variant_detected(self):
        assert is_discussion_material("K-IFRS 제1118호 정착지원 TF 논의 내용(킥오프 미팅)") is True

    def test_all_keywords_individually_detected(self):
        for kw in ["TF", "태스크포스", "논의 내용", "회의 결과", "진행 경과",
                   "중간 보고", "검토 경과", "워킹그룹", "실무그룹"]:
            assert is_discussion_material(f"{kw} 관련 자료") is True

    def test_no_keyword_not_discussion_material(self):
        assert is_discussion_material("내부회계관리제도 평가·보고 지침") is False

    # 사용자 지시: 의결/공표/제정/개정/확정이 함께 있으면 그대로 통과(재분류 안 함)
    @pytest.mark.parametrize("override", ["의결", "공표", "제정", "개정", "확정"])
    def test_override_keywords_prevent_reclassification(self, override):
        title = f"TF 논의 내용 최종 {override}"
        assert is_discussion_material(title) is False

    def test_finalize_item_reclassifies_regardless_of_original_doc_type(self):
        # kasb.py fetch_qna()처럼 doc_type을 "질의회신"으로 하드코딩한 경로도 잡아야 한다.
        item = {
            "id": "x1", "category": "kifrs", "doc_type": "질의회신",
            "title": "제1118호 정착지원 TF 논의 내용(4차)",
            "summary": [], "impact": None, "published_at": "2026-08-20",
            "collected_at": "2026-08-26T10:00:00+09:00", "effective_date": None,
            "source": {"name": "한국회계기준원", "domain": "kasb.or.kr", "tier": 1, "type": "official"},
            "trust_score": 100, "keyword_score": 0, "final_score": 55.0,
            "matched_keywords": [], "urls": {"news": None, "official": None},
            "law_meta": None, "attachments": None, "layer": "L1", "is_noise": False,
        }
        out = finalize_item(item)
        assert out["doc_type"] == "논의자료"
        assert out["stage"] == "참고"

    def test_finalize_item_keeps_original_when_override_present(self):
        item = {
            "id": "x2", "category": "kifrs", "doc_type": "질의회신",
            "title": "제1118호 TF 논의 결과 최종 의결", "summary": [], "impact": None,
            "published_at": "2026-08-20", "collected_at": "2026-08-26T10:00:00+09:00",
            "effective_date": None,
            "source": {"name": "한국회계기준원", "domain": "kasb.or.kr", "tier": 1, "type": "official"},
            "trust_score": 100, "keyword_score": 0, "final_score": 55.0,
            "matched_keywords": [], "urls": {"news": None, "official": None},
            "law_meta": None, "attachments": None, "layer": "L1", "is_noise": False,
        }
        out = finalize_item(item)
        assert out["doc_type"] == "질의회신"


# ── 제목 정제 (SPEC-ADDENDUM-5.md §5-2) ──────────────────────────────────────
class TestCleanTitleForCompare:
    def test_strips_media_suffix(self):
        assert clean_title_for_compare("남부발전, 분과위 가동 - 스트레이트뉴스") == "남부발전, 분과위 가동"

    def test_keeps_multiword_dash_content(self):
        # §5-4 과다병합 방지: 공백 있는 트레일링 세그먼트는 매체명이 아니므로 안 지운다.
        assert "접대비 한도" in clean_title_for_compare("법인세법 시행령 개정안 — 접대비 한도")

    def test_strips_bracket_prefix(self):
        assert clean_title_for_compare("[로컬 게시판] 남부발전 소식") == "남부발전 소식"

    def test_strips_quotes(self):
        assert '"' not in clean_title_for_compare('남부발전 "내부통제" 고도화')

    def test_display_title_untouched(self):
        # clean_title_for_compare는 비교 전용 — title_similarity가 원본을 바꾸지 않는지 확인.
        original = "남부발전, 분과위 가동 - 스트레이트뉴스"
        title_similarity(original, "다른 제목")
        assert original == "남부발전, 분과위 가동 - 스트레이트뉴스"


class TestExtractSubject:
    def test_extracts_leading_subject_before_comma(self):
        assert extract_subject("남부발전, 내부통제 고도화") == "남부발전"

    def test_no_comma_returns_none(self):
        assert extract_subject("ESG 공시 로드맵 연기") is None


# ── 규제성 판정 게이트 (SPEC-ADDENDUM-5.md §1) ────────────────────────────────
class TestHasRegulatorySignal:
    def test_military_article_has_false_positive_signal(self):
        # ADDENDUM-5 §1-3 스스로 인정하는 한계: "강화"가 REGULATORY_SIGNALS에
        # 있어서 §1 단독으로는 못 거른다("§3에서 재차단" — 그런데 §3도 이 예시엔
        # 홍보 동사가 없어서 못 거른다. §2(무관 업종·군사 키워드)가 있어야 완전히
        # 걸러진다 — 이번 라운드는 §2를 안 하기로 했으니 이 한계는 남아있다).
        assert has_regulatory_signal("타에브의 바시즈 사령관 복귀…내부 통제 강화 포석") is True

    def test_corporate_activity_no_signal(self):
        assert has_regulatory_signal("남부발전, 내부통제 고도화 위한 분과위 가동") is False

    def test_kssb_resolution_delay_has_signal(self):
        assert has_regulatory_signal("KSSB, ESG공시 기준서 권고안 의결 연기") is True

    def test_tax_reform_bill_has_signal(self):
        assert has_regulatory_signal("2026년 정부 세제개편(안) - 국제조세 관련 주요 개정사항") is True

    def test_all_signals_individually_detected(self):
        for kw in REGULATORY_SIGNALS:
            assert has_regulatory_signal(f"{kw} 관련 소식") is True


# ── 타사 홍보성 보도 제외 (SPEC-ADDENDUM-5.md §3) ─────────────────────────────
class TestIsCorporatePr:
    def test_pr_without_strong_signal_is_pr(self):
        assert is_corporate_pr("남부발전, 내부통제 고도화 위한 분과위 가동") is True

    def test_pr_verb_with_strong_signal_is_not_pr(self):
        assert is_corporate_pr("금감원, 내부회계관리제도 평가 지침 개정") is False

    def test_no_pr_verb_is_not_pr(self):
        assert is_corporate_pr("KSSB, ESG공시 기준서 권고안 의결 연기") is False

    def test_explanation_session_without_signal_is_pr(self):
        assert is_corporate_pr("회계기준원, ESG 공시기준 설명회 개최") is True

    # 2026-09-02 사용자 지시 — 개별 기업 ESG 홍보(실측 예시들).
    def test_individual_company_sustainability_report_is_pr(self):
        assert is_corporate_pr("지오영, 창사 첫 지속가능경영보고서 발간") is True

    def test_esg_roadmap_presentation_is_pr(self):
        assert is_corporate_pr("OO그룹, 2030 ESG 로드맵 제시") is True


class TestApplyCorporatePrFilter:
    """2026-09-02 사용자 지시로 (통과분, 제외분) 튜플 반환으로 변경."""

    def _item(self, title, layer="L3", tier=5):
        return {"category": "esg", "title": title, "layer": layer,
                "source": {"tier": tier}, "urls": {"news": "https://x", "official": None}}

    def test_splits_kept_and_excluded(self):
        items = [
            self._item("지오영, 창사 첫 지속가능경영보고서 발간"),
            self._item("금감원, 내부회계관리제도 평가 지침 개정"),
        ]
        kept, excluded = apply_corporate_pr_filter(items)
        assert [it["title"] for it in kept] == ["금감원, 내부회계관리제도 평가 지침 개정"]
        assert len(excluded) == 1
        assert excluded[0]["excluded_reason"] == "excluded:corporate_pr"

    def test_l1_exempt(self):
        items = [self._item("지오영, 창사 첫 지속가능경영보고서 발간", layer="L1", tier=1)]
        kept, excluded = apply_corporate_pr_filter(items)
        assert len(kept) == 1
        assert excluded == []


# ── 지자체 건의·민원 제외 (2026-09-02 사용자 지시) ──────────────────────────
class TestIsLocalGovPetition:
    def test_real_example_excluded(self):
        assert is_local_gov_petition("송파구, 신축주택 재산세 급증 막는다…지방세법 시행령 개정 건의") is True

    def test_all_petition_keywords_individually_detected(self):
        for kw in LOCAL_GOV_PETITION_KEYWORDS:
            assert is_local_gov_petition(f"강남구, 지방세법 개정 {kw}") is True, f"{kw}가 통과됨"

    def test_local_gov_subject_without_petition_keyword_passes(self):
        # 지자체가 주체여도 "건의" 류 표현이 없으면(예: 실제 시행 소식) 통과.
        assert is_local_gov_petition("강남구, 지방세법 개정 시행 안내") is False

    def test_petition_keyword_without_local_gov_subject_passes(self):
        # 주체가 지자체가 아니면(기업·중앙부처 등) 이 필터 대상이 아니다.
        assert is_local_gov_petition("대한상공회의소, 지방세법 개정 건의") is False

    def test_no_subject_passes(self):
        assert is_local_gov_petition("지방세법 개정 건의 잇따라") is False

    def test_metropolitan_gov_not_matched(self):
        # 사용자 지시 범위: 기초자치단체(구/시/군)만. 광역단체는 포함 안 함.
        assert is_local_gov_petition("경기도, 지방세법 개정 건의") is False


class TestApplyLocalGovPetitionFilter:
    def _item(self, title, layer="L3", tier=5):
        return {"category": "tax", "title": title, "layer": layer,
                "source": {"tier": tier}, "urls": {"news": "https://x", "official": None}}

    def test_splits_kept_and_excluded(self):
        items = [
            self._item("송파구, 신축주택 재산세 급증 막는다…지방세법 시행령 개정 건의"),
            self._item("기획재정부, 법인세법 시행령 개정"),
        ]
        kept, excluded = apply_local_gov_petition_filter(items)
        assert [it["title"] for it in kept] == ["기획재정부, 법인세법 시행령 개정"]
        assert len(excluded) == 1
        assert excluded[0]["excluded_reason"] == "excluded:local_gov_petition"

    def test_l1_exempt(self):
        items = [self._item("송파구, 신축주택 재산세 급증 막는다…지방세법 시행령 개정 건의",
                             layer="L1", tier=1)]
        kept, excluded = apply_local_gov_petition_filter(items)
        assert len(kept) == 1
        assert excluded == []


# ── 해외 전용 뉴스 제외 (2026-09-02 사용자 지시) ────────────────────────────
class TestIsForeignNewsOnly:
    def test_real_example_excluded(self):
        assert is_foreign_news_only("서클 CEO 美 디지털자산 회계기준 개정") is True

    def test_all_signals_individually_detected(self):
        for kw in FOREIGN_NEWS_SIGNALS:
            assert is_foreign_news_only(f"{kw} 회계기준 개정 소식") is True, f"{kw}가 통과됨"

    def test_domestic_adoption_context_passes(self):
        assert is_foreign_news_only("EU 회계기준 국내 도입 영향 검토") is False

    def test_no_foreign_signal_passes(self):
        assert is_foreign_news_only("K-IFRS 제1118호 재무제표 표시 개정") is False

    def test_iasb_not_excluded_by_this_filter(self):
        # ADDENDUM-7 §3(안 A) — IASB/ISSB는 doc_type="해외기준"으로 유지·분류
        # 하기로 이미 결정했다. 여기서 완전 제외하면 그 결정과 충돌한다.
        assert is_foreign_news_only("IASB, 새 공개초안 발표") is False

    def test_foreign_domain_excluded_regardless_of_title(self):
        assert is_foreign_news_only("K-IFRS 관련 국내 기사", domain="fr.tradingview.com") is True

    def test_korean_domain_not_excluded(self):
        assert is_foreign_news_only("서클 CEO 美 디지털자산 회계기준 개정", domain=None) is True
        assert is_foreign_news_only("K-IFRS 국내 소식", domain="hankyung.com") is False


class TestApplyForeignNewsFilter:
    def _item(self, title, layer="L3", tier=5, domain=None):
        return {"category": "kifrs", "title": title, "layer": layer,
                "source": {"tier": tier, "domain": domain},
                "urls": {"news": "https://x", "official": None}}

    def test_splits_kept_and_excluded(self):
        items = [
            self._item("서클 CEO 美 디지털자산 회계기준 개정"),
            self._item("회계기준원, K-IFRS 제1118호 제정"),
        ]
        kept, excluded = apply_foreign_news_filter(items)
        assert [it["title"] for it in kept] == ["회계기준원, K-IFRS 제1118호 제정"]
        assert len(excluded) == 1
        assert excluded[0]["excluded_reason"] == "excluded:foreign_news"

    def test_l1_exempt(self):
        items = [self._item("서클 CEO 美 디지털자산 회계기준 개정", layer="L1", tier=1)]
        kept, excluded = apply_foreign_news_filter(items)
        assert len(kept) == 1
        assert excluded == []

    def test_foreign_domain_excluded_even_without_keyword(self):
        items = [self._item("국내 회계 소식 헤드라인", domain="fr.tradingview.com")]
        kept, excluded = apply_foreign_news_filter(items)
        assert kept == []
        assert excluded[0]["excluded_reason"] == "excluded:foreign_news"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
