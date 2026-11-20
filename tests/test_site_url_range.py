# -*- coding: utf-8 -*-
"""홈페이지 기간 필터의 주소(URL) 표현 테스트 (2026-11-20 신설).

배경: 기간 버튼을 누르면 주소에 ?from=...&to=... 절대 날짜가 남아, 그 주소를
즐겨찾기하면 다음에 열어도 과거 기간에 고정됐다.
- 기간 버튼(최근 N일)은 ?days=N(상대 기간)으로 적는다.
- 날짜를 직접 입력한 경우에만 ?from=&to=를 쓴다(기존 공유 링크도 그대로 동작).
- 주소의 절대 기간 종료일이 14일 이상 지났으면 화면 위쪽에 안내 + [최근으로 보기].

site/index.html을 file://로 열면 data.json fetch가 막혀 data.js 폴백으로 뜬다.
Playwright(+Chromium)가 없는 환경(CI 수집 워크플로 등)에서는 건너뛴다.
"""
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

sync_api = pytest.importorskip("playwright.sync_api")

INDEX = (Path(__file__).resolve().parent.parent / "site" / "index.html").as_uri()
TODAY = datetime(2026, 11, 20, 10, 0, 0)  # 테스트 기준 "오늘"


@pytest.fixture(scope="module")
def browser():
    with sync_api.sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception as e:  # 브라우저 바이너리 미설치
            pytest.skip(f"Chromium 실행 불가: {e}")
        yield b
        b.close()


@pytest.fixture
def open_page(browser):
    pages = []

    def _open(query=""):
        page = browser.new_page()
        page.clock.set_fixed_time(TODAY)
        page.goto(INDEX + query)
        page.wait_for_function("document.getElementById('dateTo').value !== ''")
        pages.append(page)
        return page

    yield _open
    for pg in pages:
        pg.close()


def _query(page):
    return parse_qs(urlparse(page.url).query)


class TestRelativeRangeInURL:
    def test_default_load_uses_relative_days(self, open_page):
        page = open_page()
        q = _query(page)
        assert q.get("days") == ["30"]
        assert "from" not in q and "to" not in q

    @pytest.mark.parametrize("days", ["7", "30", "90"])
    def test_quick_range_button_writes_days_not_dates(self, open_page, days):
        page = open_page("?view=all&from=2026-01-01&to=2026-01-31")
        page.click(f'.quick-range[data-days="{days}"]')
        q = _query(page)
        assert q.get("days") == [days]
        assert "from" not in q and "to" not in q
        assert page.input_value("#dateTo") == "2026-11-20"

    def test_days_param_is_relative_to_today(self, open_page):
        page = open_page("?days=7")
        assert page.input_value("#dateFrom") == "2026-11-13"
        assert page.input_value("#dateTo") == "2026-11-20"
        assert page.is_hidden("#staleRangeBanner")

    def test_manual_dates_write_from_to(self, open_page):
        page = open_page("?view=all")
        page.fill("#dateFrom", "2026-11-01")
        page.fill("#dateTo", "2026-11-15")
        page.click("#applyDateBtn")
        q = _query(page)
        assert q.get("from") == ["2026-11-01"]
        assert q.get("to") == ["2026-11-15"]
        assert "days" not in q

    def test_invalid_days_falls_back_to_default(self, open_page):
        page = open_page("?days=abc")
        assert page.input_value("#dateFrom") == "2026-10-21"
        assert _query(page).get("days") == ["30"]


class TestLegacyAbsoluteLinks:
    def test_old_from_to_link_still_works(self, open_page):
        page = open_page("?from=2026-09-28&to=2026-10-29")
        assert page.input_value("#dateFrom") == "2026-09-28"
        assert page.input_value("#dateTo") == "2026-10-29"
        q = _query(page)
        assert q.get("from") == ["2026-09-28"] and q.get("to") == ["2026-10-29"]


class TestStaleRangeBanner:
    def test_banner_shown_when_end_14_days_old(self, open_page):
        page = open_page("?from=2026-09-28&to=2026-10-29")
        assert page.is_visible("#staleRangeBanner")
        assert page.inner_text("#staleRangeText") == "과거 기간(2026.09.28~2026.10.29)을 보고 있습니다."

    def test_banner_boundary(self, open_page):
        # 오늘 2026-11-20 기준: 11-06은 정확히 14일 전 → 안내, 11-07은 13일 전 → 안내 없음.
        assert open_page("?from=2026-10-01&to=2026-11-06").is_visible("#staleRangeBanner")
        assert open_page("?from=2026-10-01&to=2026-11-07").is_hidden("#staleRangeBanner")

    def test_recent_button_clears_dates_and_restores_default(self, open_page):
        page = open_page("?view=all&cat=tax&from=2026-09-28&to=2026-10-29")
        page.click("#staleRangeBtn")
        q = _query(page)
        assert "from" not in q and "to" not in q
        assert q.get("days") == ["30"]
        assert q.get("cat") == ["tax"]  # 다른 필터는 유지
        assert page.input_value("#dateFrom") == "2026-10-21"
        assert page.input_value("#dateTo") == "2026-11-20"
        assert page.is_hidden("#staleRangeBanner")


class TestAllRange:
    """2026-11-20 추가: "전체 기간으로 조회"도 상대 표기(?days=all)로 적는다."""

    def test_widen_all_button_writes_days_all(self, open_page):
        # 검색 결과가 없을 때만 "전체 기간으로 조회" 버튼이 나온다.
        page = open_page("?view=all&q=절대없는검색어zzqx")
        page.click("#widenAllBtn")
        q = _query(page)
        assert q.get("days") == ["all"]
        assert "from" not in q and "to" not in q
        assert page.input_value("#dateFrom") == "2000-01-01"
        assert page.input_value("#dateTo") == "2026-11-20"

    def test_days_all_bookmark_tracks_today_without_banner(self, open_page):
        page = open_page("?days=all")
        assert page.input_value("#dateFrom") == "2000-01-01"
        assert page.input_value("#dateTo") == "2026-11-20"
        assert page.is_hidden("#staleRangeBanner")
        assert _query(page).get("days") == ["all"]

    def test_legacy_absolute_all_range_link_unchanged(self, open_page):
        # 예전 방식으로 저장된 전체 기간 링크는 절대 기간 그대로 동작한다.
        page = open_page("?from=2000-01-01&to=2026-10-01")
        assert page.input_value("#dateTo") == "2026-10-01"
        q = _query(page)
        assert q.get("from") == ["2000-01-01"] and q.get("to") == ["2026-10-01"]
        assert page.is_visible("#staleRangeBanner")
