# -*- coding: utf-8 -*-
"""sources/official/lawmaking.py — 국민참여입법센터 입법예고 수집기 (2026-10-01 신설).
네트워크 모킹, 실제 요청 없음."""
from types import SimpleNamespace

import pytest

from sources.official import lawmaking


def _row(seq, title, ministry, kind, start, end):
    return f"""
<tr>
  <td data-th="번호" class="reHide">3</td>
  <td data-th="법령 제명" class="subject">
    <a href="/gcom/ogLmPp/{seq}?finishIncludeYn=Y&amp;lsNm=x" title="{title}">{title}</a>
    <span class="ogmark_2">일부</span>
  </td>
  <td data-th="소관부처 (법령종류)"><p>{ministry}</p><p>({kind})</p></td>
  <td data-th="법령분야 (주요적용대상)"><p>내국세</p></td>
  <td data-th="입법의견 접수기간"><p>{start}</p><p>~{end}</p></td>
  <td data-th="입법의견 남은 기간">-</td>
  <td data-th="의견수"><a href="#">66</a></td>
  <td data-th="조회수" class="reHide">11,808</td>
</tr>"""


def _page(*rows):
    body = "".join(rows) or '<tr><td colspan="8">해당 목록이 없습니다.</td></tr>'
    return f"""<html><body><table><caption><p>(부처)입법예고 목록</p></caption>
<thead><tr><th>번호</th></tr></thead><tbody>{body}</tbody></table></body></html>"""


# 실측 2026-10-01 목록에 있던 행들(일부 변형).
CORP_DECREE = _row("88012", "법인세법 시행령 일부개정령안 입법예고", "재정경제부", "대통령령",
                   "2026. 8. 7.", "2026. 9. 10.")
CORP_LAW = _row("87990", "법인세법 일부개정법률안 입법예고", "기획재정부", "법률",
                "2026. 8. 4.", "2026. 8. 20.")
OLD_RULE = _row("85001", "법인세법 시행규칙 일부개정령안 입법예고", "재정경제부", "부령",
                "2026. 4. 24.", "2026. 6. 4.")  # 90일 밖
CUSTOMS = _row("87000", "관세법 일부개정법률안 입법예고", "재정경제부", "법률",
               "2026. 8. 4.", "2026. 8. 11.")    # 활성 세목 아님


def _fix_today(monkeypatch):
    class _DT(lawmaking.datetime):
        @classmethod
        def now(cls, tz=None):
            return lawmaking.datetime(2026, 10, 1, 7, 0, tzinfo=tz)
    monkeypatch.setattr(lawmaking, "datetime", _DT)


def _mock_http(monkeypatch, pages_by_query, calls=None):
    def fake_get_govt(url, *, params=None, **kw):
        if calls is not None:
            calls.append(params["lsNm"])
        page = pages_by_query.get(params["lsNm"], _page())
        if isinstance(page, Exception):
            raise page
        return SimpleNamespace(text=page)
    monkeypatch.setattr(lawmaking._http, "get_govt", fake_get_govt)
    monkeypatch.setattr(lawmaking.time, "sleep", lambda s: None)


def test_law_name_of():
    assert lawmaking.law_name_of("법인세법 시행령 일부개정령안 입법예고") == "법인세법 시행령"
    assert lawmaking.law_name_of("지방세법 일부개정법률안 재입법예고") == "지방세법"
    assert lawmaking.law_name_of("국제조세조정에 관한 법률 일부개정법률안 입법예고") == "국제조세조정에 관한 법률"
    assert lawmaking.law_name_of("공지사항") is None


def test_parse_list_reads_rows_and_dates():
    rows, found = lawmaking.parse_list(_page(CORP_DECREE))
    assert found is True
    assert rows == [{"seq": "88012", "title": "법인세법 시행령 일부개정령안 입법예고",
                     "ministry": "재정경제부", "law_kind": "대통령령",
                     "start": "2026-08-07", "end": "2026-09-10"}]


def test_parse_list_empty_result_is_still_a_valid_table():
    rows, found = lawmaking.parse_list(_page())
    assert rows == [] and found is True


def test_parse_list_without_table_is_not_found():
    assert lawmaking.parse_list("<html><body>차단</body></html>") == ([], False)


def test_search_roots_one_per_base_law():
    roots = lawmaking._search_roots()
    assert "법인세법" in roots and "지방세특례제한법" in roots
    assert not any(r.endswith(("시행령", "시행규칙")) for r in roots)


def test_fetch_keeps_only_target_laws_within_window(monkeypatch):
    _fix_today(monkeypatch)
    calls = []
    _mock_http(monkeypatch, {"법인세법": _page(CORP_DECREE, CORP_LAW, OLD_RULE, CUSTOMS)}, calls)

    items = lawmaking.fetch()

    assert calls == lawmaking._search_roots()  # 본법 이름마다 1회
    by_title = {it["title"]: it for it in items}
    assert set(by_title) == {"법인세법 시행령 일부개정령안 입법예고", "법인세법 일부개정법률안 입법예고"}
    decree = by_title["법인세법 시행령 일부개정령안 입법예고"]
    assert decree["published_at"] == "2026-08-07"
    assert decree["doc_type"] == "공개초안"
    assert decree["urls"]["official"] == "https://opinion.lawmaking.go.kr/gcom/ogLmPp/88012"
    assert decree["source"]["domain"] == "lawmaking.go.kr"
    assert decree["law_meta"] is None  # "현행 기준" 탭에 섞이지 않게
    assert decree["_body"] == "입법의견 접수기간 2026.08.07~2026.09.10"
    # 개편 전 명칭은 현행 명칭으로.
    assert by_title["법인세법 일부개정법률안 입법예고"]["source"]["name"] == "재정경제부"


def test_fetch_dedupes_same_notice_from_two_queries(monkeypatch):
    _fix_today(monkeypatch)
    _mock_http(monkeypatch, {"법인세법": _page(CORP_DECREE), "소득세법": _page(CORP_DECREE)})
    assert len(lawmaking.fetch()) == 1


def test_fetch_zero_results_is_normal(monkeypatch):
    _fix_today(monkeypatch)
    _mock_http(monkeypatch, {})
    assert lawmaking.fetch() == []


def test_fetch_raises_when_every_query_fails(monkeypatch):
    _fix_today(monkeypatch)
    roots = lawmaking._search_roots()
    _mock_http(monkeypatch, {r: RuntimeError("timeout") for r in roots})
    with pytest.raises(RuntimeError):
        lawmaking.fetch()


def test_fetch_raises_when_no_table_anywhere(monkeypatch):
    _fix_today(monkeypatch)
    roots = lawmaking._search_roots()
    _mock_http(monkeypatch, {r: "<html>차단</html>" for r in roots})
    with pytest.raises(RuntimeError):
        lawmaking.fetch()
