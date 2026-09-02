# -*- coding: utf-8 -*-
"""sources/current_standards.py 단위 테스트 (2026-09-02 신설 — "현행 기준" 탭).

전부 합성(synthetic) 데이터로 테스트한다 — 실제 site/data.json에 의존하면
크롤링 결과가 바뀔 때마다 테스트가 흔들린다.
"""
from sources import current_standards as cs


def _item(**overrides):
    base = {
        "category": "kifrs", "doc_type": "제·개정", "title": "제목",
        "published_at": "2024-01-01", "effective_date": "2025-01-01",
        "urls": {"official": "https://official.example/x", "news": None},
    }
    base.update(overrides)
    return base


class TestBuildKifrsStandards:
    def test_extracts_standard_no_and_keeps_latest_per_number(self):
        items = [
            _item(title="2020년 개정 (제1001호 재무제표 표시)", published_at="2020-01-01", effective_date="2021-01-01"),
            _item(title="2023년 개정 (제1001호 재무제표 표시)", published_at="2023-01-01", effective_date="2024-01-01"),
        ]
        out = cs.build_kifrs_standards(items)
        assert len(out["recent"]) == 1
        r = out["recent"][0]
        assert r["standard_no"] == "제1001호"
        assert r["latest_revision_date"] == "2023-01-01"
        assert r["effective_date"] == "2024-01-01"

    def test_one_title_with_multiple_standard_numbers_produces_multiple_rows(self):
        items = [_item(title="2024년 연차개선 (제1007호 현금흐름표, 제1101호 최초채택)")]
        out = cs.build_kifrs_standards(items)
        nos = {r["standard_no"] for r in out["recent"]}
        assert nos == {"제1007호", "제1101호"}

    def test_caps_at_five_most_recent(self):
        items = [
            _item(title=f"제{1000 + i}호 기준 (제{1000 + i}호)", published_at=f"2020-01-{i + 1:02d}")
            for i in range(8)
        ]
        out = cs.build_kifrs_standards(items)
        assert len(out["recent"]) == 5
        dates = [r["latest_revision_date"] for r in out["recent"]]
        assert dates == sorted(dates, reverse=True)

    def test_ignores_non_kifrs_and_non_revision_doctype(self):
        items = [
            _item(category="tax", title="제1001호 무관 세법"),
            _item(doc_type="보도자료", title="제1001호 보도"),
        ]
        assert cs.build_kifrs_standards(items)["recent"] == []

    def test_catalog_url_present(self):
        assert cs.build_kifrs_standards([])["catalog_url"] == cs.KIFRS_CATALOG_URL


class TestBuildEsgStandards:
    def test_only_voluntary_doctype_esg_items(self):
        items = [
            _item(category="esg", doc_type="자발적용", title="KSSB 공시기준서 제1호 일반 요구사항",
                  published_at="2026-02-26", effective_date="2028-01-01"),
            _item(category="esg", doc_type="자발적용", title="KSSB 공시기준서 제2호 기후 관련 공시",
                  published_at="2026-02-26", effective_date="2028-01-01"),
            _item(category="esg", doc_type="보도자료", title="무관 보도"),
            _item(category="kifrs", doc_type="자발적용", title="다른 카테고리"),
        ]
        out = cs.build_esg_standards(items)
        assert len(out["recent"]) == 2
        titles = {r["title"] for r in out["recent"]}
        assert titles == {"KSSB 공시기준서 제1호 일반 요구사항", "KSSB 공시기준서 제2호 기후 관련 공시"}

    def test_is_roadmap_estimate_passed_through(self):
        items = [_item(category="esg", doc_type="자발적용", title="제1호",
                        is_roadmap_estimate=True)]
        assert cs.build_esg_standards(items)["recent"][0]["is_roadmap_estimate"] is True

    def test_scope_note_attached_when_roadmap_estimate(self, monkeypatch):
        # 2026-09-02 사용자 지시: 시행 예정일만 보면 팜한농 자체 적용일로
        # 오독할 수 있어 대상 범위(data/esg_roadmap.yml의 scope_note)를
        # 병기한다 — 실제 yml 파일 문구에 테스트가 흔들리지 않도록 monkeypatch.
        monkeypatch.setattr(cs._esg_roadmap, "load", lambda: {"milestones": [{"scope_note": "테스트 대상 범위"}]})
        items = [_item(category="esg", doc_type="자발적용", title="제1호", is_roadmap_estimate=True)]
        assert cs.build_esg_standards(items)["recent"][0]["effective_date_scope_note"] == "테스트 대상 범위"

    def test_scope_note_absent_when_not_roadmap_estimate(self, monkeypatch):
        # 확정 시행일(로드맵 추정이 아닌 경우)에는 "대상 범위" 개념 자체가
        # 없다 — 붙이면 안 된다.
        monkeypatch.setattr(cs._esg_roadmap, "load", lambda: {"milestones": [{"scope_note": "테스트 대상 범위"}]})
        items = [_item(category="esg", doc_type="자발적용", title="제1호", is_roadmap_estimate=False)]
        assert cs.build_esg_standards(items)["recent"][0]["effective_date_scope_note"] is None

    def test_scope_note_none_when_roadmap_yml_missing_field(self, monkeypatch):
        monkeypatch.setattr(cs._esg_roadmap, "load", lambda: {})
        items = [_item(category="esg", doc_type="자발적용", title="제1호", is_roadmap_estimate=True)]
        assert cs.build_esg_standards(items)["recent"][0]["effective_date_scope_note"] is None

    def test_catalog_url_present(self):
        assert cs.build_esg_standards([])["catalog_url"] == cs.ESG_CATALOG_URL


class TestBuildTaxLaws:
    def _tax_item(self, law_name, promulgation="2025-01-01", enforcement="2025-02-01", **overrides):
        d = _item(category="tax", law_meta={
            "law_name": law_name, "promulgation_date": promulgation, "enforcement_date": enforcement,
        })
        d.update(overrides)
        return d

    def test_only_tax_items_with_law_meta(self):
        items = [
            self._tax_item("법인세법"),
            _item(category="tax", law_meta=None, title="법령메타 없는 세법 뉴스"),
            _item(category="kifrs", law_meta={"law_name": "무관", "promulgation_date": "", "enforcement_date": ""}),
        ]
        out = cs.build_tax_laws(items)
        assert len(out["laws"]) == 1
        assert out["laws"][0]["law_name"] == "법인세법"

    def test_missing_dates_become_empty_string_not_null(self):
        items = [self._tax_item("법인세법", promulgation=None, enforcement=None)]
        law = cs.build_tax_laws(items)["laws"][0]
        assert law["promulgation_date"] == ""
        assert law["enforcement_date"] == ""

    def test_sort_order_root_then_suffix(self):
        items = [
            self._tax_item("법인세법 시행규칙"),
            self._tax_item("부가가치세법"),
            self._tax_item("법인세법"),
            self._tax_item("법인세법 시행령"),
        ]
        names = [r["law_name"] for r in cs.build_tax_laws(items)["laws"]]
        assert names == ["법인세법", "법인세법 시행령", "법인세법 시행규칙", "부가가치세법"]

    def test_unlisted_law_name_sorts_last(self):
        items = [self._tax_item("법인세법"), self._tax_item("어떤 이상한 법")]
        names = [r["law_name"] for r in cs.build_tax_laws(items)["laws"]]
        assert names == ["법인세법", "어떤 이상한 법"]


class TestBuildIcfrDocuments:
    def _icfr_item(self, title, doc_type="모범규준", published_at="2021-01-01", **overrides):
        d = _item(category="icfr", doc_type=doc_type, title=title, published_at=published_at)
        d.update(overrides)
        return d

    def test_gaenyeomcheje_goes_to_standard_bucket(self):
        items = [self._icfr_item("내부회계관리제도 설계 및 운영 개념체계 전문(2021.10.1. 개정)")]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert len(buckets["모범규준"]) == 1
        assert buckets["평가·보고 기준"] == []
        assert buckets["적용지침"] == []

    def test_jeogyongginbeop_goes_to_guideline_bucket_even_with_pyeongga_bogo(self):
        # "적용기법"이 있으면 "평가"+"보고"가 같이 있어도 적용지침으로 분류돼야
        # 한다(우선순위 규칙 검증) — 실제 데이터에 이런 제목이 다수 있음.
        items = [self._icfr_item("내부회계관리제도 평가 및 보고 적용기법 전문(2022.2.7. 개정)", doc_type="적용지침")]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert len(buckets["적용지침"]) == 1
        assert buckets["평가·보고 기준"] == []

    def test_pyeongga_bogo_mobeomgyujun_goes_to_pyeongga_bogo_bucket(self):
        items = [self._icfr_item("내부회계관리제도 평가 및 보고 모범규준 전문(2021.10.1. 개정)", doc_type="적용지침")]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert len(buckets["평가·보고 기준"]) == 1

    def test_unclassifiable_title_excluded(self):
        items = [self._icfr_item("여전업권 내부통제 모범규준 시행")]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert all(docs == [] for docs in buckets.values())

    def test_generic_index_titles_excluded(self):
        items = [
            self._icfr_item("모범규준"),
            self._icfr_item("新모범규준(2018.6)"),
            self._icfr_item("모범규준(2012.12)"),
        ]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert all(docs == [] for docs in buckets.values())

    def test_ignores_wrong_category_and_wrong_doctype(self):
        items = [
            self._icfr_item("설계 및 운영 개념체계", **{"category": "kifrs"}),
            self._icfr_item("설계 및 운영 개념체계", doc_type="FAQ"),
        ]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert all(docs == [] for docs in buckets.values())

    def test_dedupes_reposted_versions_keeping_latest(self):
        items = [
            self._icfr_item("내부회계관리제도 평가·보고 지침 ('23.12.29 배포)", doc_type="적용지침", published_at="2024-06-05"),
            self._icfr_item("내부회계관리제도 평가·보고 지침 ('24.12.23 개정)", doc_type="적용지침", published_at="2025-01-02"),
            self._icfr_item("내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정)", doc_type="적용지침", published_at="2025-01-08"),
        ]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        docs = buckets["평가·보고 기준"]
        assert len(docs) == 1
        assert docs[0]["revision_date"] == "2025-01-08"

    def test_distinct_documents_with_same_date_not_merged(self):
        # 접두어 유무로 실제 서로 다른 문서 — 날짜가 같아도 따로 남아야 한다.
        # ("중소기업" 접두어는 아래 SME 제외 테스트가 따로 검증하므로 여기서는
        # 일부러 다른 접두어를 쓴다.)
        items = [
            self._icfr_item("내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정)", doc_type="적용지침"),
            self._icfr_item("지주회사 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정)", doc_type="적용지침"),
        ]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert len(buckets["적용지침"]) == 2

    def test_excludes_sme_titled_documents(self):
        # 2026-09-02 사용자 지시: 팜한농은 중소기업이 아니므로 "중소기업"
        # 문서는 다른 조건과 무관하게 제외한다.
        items = [
            self._icfr_item("중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정)", doc_type="적용지침"),
            self._icfr_item("중소기업 내부회계관리제도 평가 및 보고 적용기법 전문(2022.2.7. 개정)", doc_type="적용지침"),
        ]
        buckets = {b["label"]: b["documents"] for b in cs.build_icfr_documents(items)["buckets"]}
        assert all(docs == [] for docs in buckets.values())

    def test_display_order_is_fixed_regardless_of_input_order(self):
        items = [
            self._icfr_item("내부회계관리제도 평가 및 보고 적용기법 전문(2022.2.7. 개정)", doc_type="적용지침"),
            self._icfr_item("내부회계관리제도 평가 및 보고 모범규준 전문(2021.10.1. 개정)", doc_type="적용지침"),
            self._icfr_item("내부회계관리제도 설계 및 운영 개념체계 전문(2021.10.1. 개정)"),
        ]
        labels = [b["label"] for b in cs.build_icfr_documents(items)["buckets"]]
        assert labels == ["모범규준", "평가·보고 기준", "적용지침"]

    def test_catalog_url_present(self):
        assert cs.build_icfr_documents([])["catalog_url"] == cs.ICFR_CATALOG_URL


class TestBuildCurrentStandards:
    def test_assembles_all_four_keys(self):
        out = cs.build_current_standards([])
        assert set(out.keys()) == {"kifrs", "esg", "tax", "icfr"}
