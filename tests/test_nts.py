# -*- coding: utf-8 -*-
"""sources/official/nts.py 연도 필터 단위 테스트 (2026-09-09 신설).

배경: 국세청 "개정세법 해설" 게시판은 연 1회 자료집인데 과거 발간분(2017~2026년치,
10건)이 전부 목록에 남아있어 매번 그대로 수집된다. 이 소스가 며칠 실패했다
복구될 때(캐시가 비어 신규 판정 기준선이 사라졌을 때) 10건 전부가 "신규 발표"로
오판되는 사고가 2026-09-04·09-09 재발(docs/NEXT.md 참고) — id/캐시 문제와는
별개로, 애초에 매번 10년치를 전부 수집 대상에 넣을 이유가 없다는 사용자 판단으로
연도 필터를 추가했다.
"""
from sources.official import nts


def _item(title: str) -> dict:
    return {"title": title}


class TestFilterRecentYears:
    def test_keeps_only_most_recent_two_years_by_default(self):
        # 실제 게시판 노출 순서(최신이 먼저)를 그대로 흉내낸다 — 필터는 입력
        # 순서를 보존하고 연도만 걸러낸다(재정렬하지 않음).
        items = [_item(f"{y}년 개정세법 해설") for y in range(2026, 2016, -1)]
        out = nts._filter_recent_years(items)
        assert [it["title"] for it in out] == ["2026년 개정세법 해설", "2025년 개정세법 해설"]

    def test_recency_based_on_years_present_not_todays_calendar_year(self):
        """오늘이 2027년이어도(올해치가 아직 안 올라왔으면) 목록에 있는 연도
        기준으로 최근 2개를 고른다 — 달력 연도로 자르면 그 사이엔 0건이 된다."""
        items = [_item(f"{y}년 개정세법 해설") for y in range(2025, 2016, -1)]  # 2025까지만
        out = nts._filter_recent_years(items)
        assert [it["title"] for it in out] == ["2025년 개정세법 해설", "2024년 개정세법 해설"]

    def test_keep_count_is_configurable(self):
        items = [_item(f"{y}년 개정세법 해설") for y in range(2026, 2016, -1)]
        out = nts._filter_recent_years(items, keep=3)
        assert [it["title"] for it in out] == [
            "2026년 개정세법 해설", "2025년 개정세법 해설", "2024년 개정세법 해설",
        ]

    def test_titles_without_leading_year_are_left_untouched(self):
        items = [_item(f"{y}년 개정세법 해설") for y in range(2026, 2016, -1)]
        items.append(_item("개정세법 해설 관련 공지"))  # 연도 없는 항목은 필터 대상 아님
        out = nts._filter_recent_years(items)
        titles = [it["title"] for it in out]
        assert "2026년 개정세법 해설" in titles
        assert "2017년 개정세법 해설" not in titles
        assert "개정세법 해설 관련 공지" in titles

    def test_empty_input(self):
        assert nts._filter_recent_years([]) == []

    def test_logs_dropped_count(self, capsys):
        items = [_item(f"{y}년 개정세법 해설") for y in range(2026, 2016, -1)]
        nts._filter_recent_years(items)
        out = capsys.readouterr().out
        assert "[nts] 연도 필터: 8건 제외" in out
