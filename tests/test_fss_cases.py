# -*- coding: utf-8 -*-
"""금감원 심사·감리지적사례(B0000135) 하위 수집 테스트 (2026-11-27).

등록일 칸이 없어 공개번호 FSS/YYMM의 연월을 발행일로 쓰고, FSS/24xx 이후만 받는다.
공개번호 없는 옛 행·그 이전 묶음은 건수만, 일반기업회계기준 사례는 collect:non_kifrs.
"""
import pytest
from bs4 import BeautifulSoup

from sources import _excluded_log
from sources import main
from sources._config import DISABLED_SOURCES, SOURCE_LABELS
from sources._source_health import PartialFetch
from sources.official import fss


def _row(no, case_no, title, standard="기업회계기준서 제1115호", ntt="218902"):
    return (f'<tr><td class="num">{no}</td><td>{case_no}</td>'
            f'<td class="title2"><a href="/fss/bbs/B0000135/view.do?nttId={ntt}&menuNo=200448&pageIndex=1">'
            f'{title}</a></td><td>수익인식</td><td>{standard}</td><td>2025</td>'
            f'<td><a href="/fss/cmmn/file/fileDown.do?atchFileId=x&fileSn=1"><span class="name">{case_no}.pdf</span></a></td>'
            f'<td>100</td></tr>')


def _rows(*rows):
    html = "<table><thead><tr><th>번호</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>"
    return BeautifulSoup(html, "html.parser").select("table tbody tr")


@pytest.fixture(autouse=True)
def _clear_log():
    _excluded_log.clear()
    yield
    _excluded_log.clear()


class TestCasePublishedAt:
    def test_yymm_to_first_day(self):
        assert fss.case_published_at("FSS/2606-10") == "2026-06-01"
        assert fss.case_published_at("FSS/2409-01") == "2024-09-01"

    @pytest.mark.parametrize("no", ["", "FSS", "C-4", "FSS/2606"])
    def test_not_case_number(self, no):
        assert fss.case_published_at(no) is None

    def test_bad_month_raises(self):
        with pytest.raises(ValueError):
            fss.case_published_at("FSS/2613-01")


class TestParseCasesRows:
    def test_keeps_24xx_and_later_only(self):
        rows = _rows(_row(239, "FSS/2606-10", "특수관계자로부터 제공받은 담보 미공시", ntt="218922"),
                     _row(186, "FSS/2405-09", "파생상품 등 허위계상", ntt="2"),
                     _row(174, "FSS/2311-15", "매출채권에 대한 손실충당금 과소·과대계상", ntt="3"),
                     _row(20, "", "C-4[매출채권 할인 및 양도 주석]", ntt="4"))
        items, seen, errors = fss.parse_cases_rows(rows)
        assert (seen, errors) == (4, 0)
        assert [it["published_at"] for it in items] == ["2026-06-01", "2024-05-01"]
        assert _excluded_log.tallies() == {fss.CASES_TALLY_LABEL: 2}

    def test_item_shape(self):
        items, _, _ = fss.parse_cases_rows(_rows(_row(239, "FSS/2606-10", "특수관계자로부터 제공받은 담보 미공시",
                                                       ntt="218922")))
        it = items[0]
        assert it["title"] == "특수관계자로부터 제공받은 담보 미공시 (FSS/2606-10)"
        assert it["category"] == "kifrs" and it["doc_type"] == "결정례·판례" and it["layer"] == "L1"
        assert it["urls"]["official"] == ("https://www.fss.or.kr/fss/bbs/B0000135/view.do"
                                          "?nttId=218922&menuNo=200448")  # pageIndex 없음 — id 고정
        assert it["date_estimated"] is True and it["is_static"] is False
        assert it["attachments"][0]["name"] == "FSS/2606-10.pdf"
        assert fss.part_of(it) == "cases"

    def test_same_title_in_batch_stays_distinct(self):
        items, _, _ = fss.parse_cases_rows(_rows(_row(181, "FSS/2405-04", "매출 및 매출원가 허위계상", ntt="1"),
                                                 _row(179, "FSS/2405-01", "매출 및 매출원가 허위계상", ntt="2")))
        assert len({it["title"] for it in items}) == 2 and len({it["id"] for it in items}) == 2

    def test_k_gaap_case_excluded(self):
        items, _, _ = fss.parse_cases_rows(_rows(_row(206, "FSS/2505-01", "매출 및 매출원가 허위계상",
                                                      standard="일반기업회계기준 제2장, 제16장")))
        assert items == []
        assert _excluded_log.excluded()[0]["reason"] == "collect:non_kifrs"

    def test_row_isolation(self):
        rows = _rows(_row(1, "FSS/2613-01", "월이 이상한 행", ntt="1"),
                     _row(2, "FSS/2606-01", "영업수익 및 영업비용 과대계상", ntt="2"))
        items, seen, errors = fss.parse_cases_rows(rows)
        assert len(items) == 1 and errors == 1
        assert _excluded_log.excluded()[0]["reason"] == "collect:row_parse_error"


class TestFetchReviewCases:
    def _fake(self, monkeypatch, html):
        class R:
            text = html
            status_code = 200
        monkeypatch.setattr(fss._http, "get", lambda *a, **k: R())

    def test_zero_rows_raises(self, monkeypatch):
        self._fake(monkeypatch, "<table><tbody></tbody></table>")
        with pytest.raises(RuntimeError):
            fss.fetch_review_cases()

    def test_rows_but_no_target_is_normal(self, monkeypatch):
        self._fake(monkeypatch, "<table><tbody>" + _row(1, "FSS/2311-01", "옛 사례") + "</tbody></table>")
        assert fss.fetch_review_cases() == ([], [])

    def test_row_error_is_partial_reason(self, monkeypatch):
        self._fake(monkeypatch, "<table><tbody>" + _row(1, "FSS/2613-01", "이상") +
                   _row(2, "FSS/2606-01", "정상", ntt="9") + "</tbody></table>")
        items, reasons = fss.fetch_review_cases()
        assert len(items) == 1 and reasons and "해석 실패" in reasons[0]


class TestWiring:
    def test_tracked_and_sub_sources(self):
        assert "cases" in fss.TRACKED_PARTS
        assert "cases" in main.SUB_SOURCES["fss"]
        assert "fss_cases" in SOURCE_LABELS

    def test_toggle_listed_and_enabled(self):
        text = open("data/source_toggles.yml", encoding="utf-8").read()
        assert "name: fss_cases" in text
        assert "fss_cases" not in DISABLED_SOURCES

    def test_toggle_off_skips(self, monkeypatch):
        monkeypatch.setattr(fss, "DISABLED_SOURCES", {"fss_cases": "test"})
        assert not fss.part_enabled("cases")

    def test_cases_failure_is_partial(self, monkeypatch):
        monkeypatch.setattr(fss, "SLEEP_BETWEEN_REQUESTS", 0)
        monkeypatch.setattr(fss, "fetch_data_board", lambda **k: [{"id": "b2", "urls": {"official": "x"}}])
        monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [{"id": "b3", "urls": {"official": "https://www.k-icfr.org/a"}}])
        monkeypatch.setattr(fss, "fetch_press", lambda: ([], []))
        monkeypatch.setattr(fss, "fetch_disclosure_notes", lambda: ([], []))

        def boom():
            raise RuntimeError("cases 목록 행 0개")
        monkeypatch.setattr(fss, "fetch_review_cases", boom)
        with pytest.raises(PartialFetch) as ei:
            fss.fetch()
        assert set(ei.value.failed) == {"cases"}

