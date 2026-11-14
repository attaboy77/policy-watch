# -*- coding: utf-8 -*-
"""재정경제부(moef)·금융위(fsc)·정책브리핑(policy_briefing) 어댑터 — 2026-10-01 재활성화.

- 관련 항목이 없어 0건인 건 정상(main.ALLOW_EMPTY_SOURCES), 목록 행 자체를 못 읽으면 예외.
- moef: "「소득세법 시행령」 등 4개 시행령 국무회의 의결" 같은 묶음 보도자료는 첨부
  hwpx의 법령 목록으로 세목 필터를 다시 판단한다.
네트워크 모킹, 실제 요청 없음.
"""
import io
import zipfile
from types import SimpleNamespace

import pytest

from sources import _utils, policy_briefing
from sources.official import fsc, moef


# ── 공용: match_tax_law ──────────────────────────────────────────────────────
def test_match_tax_law_exact_names_only():
    assert _utils.match_tax_law(["법인세법 시행령", "종합부동산세법 시행령", "관세법"]) == ["법인세법 시행령"]
    assert _utils.match_tax_law(["법인세법 시행령 일부개정령안"]) == []  # 부분일치 아님


def test_match_tax_law_passes_everything_without_config(monkeypatch):
    monkeypatch.setattr(_utils, "TAX_SUBJECTS", [])
    assert _utils.match_tax_law(["관세법"]) == ["관세법"]


# ── moef ─────────────────────────────────────────────────────────────────────
def _moef_li(ntt, title, day="2026.09.29."):
    return (f'<li><h3><a href="javascript:fn_egov_select(\'{ntt}\');">{title}</a></h3>'
            f'<div class="boardInfo"><div class="infoLeft"><span class="date">{day}</span></div></div></li>')


def _moef_list(*lis):
    return f"<html><body><ul>{''.join(lis)}</ul></body></html>"


BUNDLE = "「소득세법 시행령」 등 4개 시행령 국무회의 의결"
# 실측(2026-10-01) 상세 페이지의 첨부 미리보기 링크 모양.
DETAIL = ('<html><body><a class="view" href="/com/synap/synapView.do;jsessionid=x?atchFileId=ATCH_000000000032807'
          '&amp;fileSn=1" title="260929 소득세법 시행령 등 국무회의 의결.hwpx 파일 새 창 열림">보기</a></body></html>')


def _hwpx(text):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("Contents/section0.xml", f"<hs:sec><hp:t>{text}</hp:t></hs:sec>")
        z.writestr("mimetype", "application/hwp+zip")
    return buf.getvalue()


def _mock_moef(monkeypatch, list_html, *, detail=DETAIL, hwpx=None, calls=None):
    def fake_get_govt(url, *, params=None, **kw):
        if calls is not None:
            calls.append(url.rsplit("/", 1)[-1])
        if url == moef.PRESS_LIST_URL:
            return SimpleNamespace(text=list_html)
        if url == moef.PRESS_DETAIL_URL:
            return SimpleNamespace(text=detail)
        if url == moef.FILE_DOWN_URL:
            assert params == {"atchFileId": "ATCH_000000000032807", "fileSn": "1"}
            return SimpleNamespace(content=hwpx)
        raise AssertionError(url)
    monkeypatch.setattr(moef._http, "get_govt", fake_get_govt)
    monkeypatch.setattr(moef.time, "sleep", lambda s: None)


def test_moef_bundle_passes_when_attachment_lists_target_law(monkeypatch):
    hwpx = _hwpx("「소득세법 시행령」, 「법인세법 시행령」, 「종합부동산세법 시행령」 및 "
                 "「상속세 및 증여세법 시행령」 일부개정령안을 심의·의결")
    _mock_moef(monkeypatch, _moef_list(_moef_li("MOSF_1", BUNDLE)), hwpx=hwpx)
    items = moef.fetch()
    assert [it["title"] for it in items] == [BUNDLE]
    assert items[0]["source"]["name"] == "재정경제부"


def test_moef_bundle_dropped_when_no_target_law_inside(monkeypatch):
    title = "「종합부동산세법 시행령」 등 2개 시행령 국무회의 의결"
    hwpx = _hwpx("「종합부동산세법 시행령」 및 「상속세 및 증여세법 시행령」")
    _mock_moef(monkeypatch, _moef_list(_moef_li("MOSF_1", title)), hwpx=hwpx)
    assert moef.fetch() == []


def test_moef_bundle_attachment_failure_falls_back_to_title(monkeypatch):
    """첨부 확인이 실패해도 제목의 「…」가 활성 세목 법령이면 통과(소득세법 시행령은
    원천세 세목의 laws에 들어 있다)."""
    _mock_moef(monkeypatch, _moef_list(_moef_li("MOSF_1", BUNDLE)), detail="<html></html>")
    assert [it["title"] for it in moef.fetch()] == [BUNDLE]


def test_moef_non_bundle_titles_do_not_fetch_attachments(monkeypatch):
    calls = []
    _mock_moef(monkeypatch, _moef_list(_moef_li("MOSF_2", "개인투자용 국채 10월 2,300억원 발행 예정")),
               calls=calls)
    assert moef.fetch() == []  # 관련 없음 → 정상 0건
    assert calls == ["nesdta.do"]  # 목록 1회만, 상세/첨부 요청 없음


def test_moef_raises_when_no_rows(monkeypatch):
    _mock_moef(monkeypatch, "<html><body>차단</body></html>")
    with pytest.raises(RuntimeError):
        moef.fetch()


# ── fsc / policy_briefing: 행 0개면 실패, 행은 있는데 관련 없으면 정상 0건 ──────
# 2026-11-14: fsc 하위 수집이 list(보도자료)·notice(입법예고) 둘이 돼서 URL로 응답을 나눈다.
def _notice_li(title, day, n, period=("2026-11-02", "2026-12-14")):
    return (f'<li><div class="inner"><div class="count">{n}</div><div class="cont">'
            f'<div class="subject"><a href="./po040301/view?noticeId={n}&curPage=&srchKey=">{title}</a></div>'
            f'<div class="info"><span>구분 : 규정변경예고</span>'
            f'<span>예고기간 : {period[0]} ~ {period[1]}</span></div>'
            f'<div class="file"><div class="file-list"><span class="name">1. 공고문.hwpx (36 KB)</span>'
            f'<span class="ico download"><a href="/comm/getFile?srvcId=RULENOTICE&upperNo={n}&fileNo=1">'
            f'다운로드</a></span></div></div></div><div class="day">{day}</div></div></li>')


def _recent(days_ago=1):
    from datetime import date, timedelta
    return (date.today() - timedelta(days=days_ago)).isoformat()


UNRELATED_NOTICE = "<ul>" + _notice_li("「예금자보호법」 일부개정법률안 입법예고", _recent(), 9001) + "</ul>"


def _route(list_html, notice_html=UNRELATED_NOTICE):
    """list는 모든 페이지에 같은 HTML, notice는 1페이지에만 행이 있다(2페이지부터 빈 목록)."""
    def get(url, params=None, **kw):
        if "po040301" in url:
            return SimpleNamespace(text=notice_html if (params or {}).get("curPage", 1) == 1 else "<ul></ul>")
        return SimpleNamespace(text=list_html)
    return get


def test_fsc_raises_when_every_page_fails(monkeypatch):
    def boom(*a, **kw):
        raise RuntimeError("timeout")
    monkeypatch.setattr(fsc._http, "get_govt", boom)
    monkeypatch.setattr("time.sleep", lambda s: None)
    with pytest.raises(RuntimeError):
        fsc.fetch(max_pages=2)


def test_fsc_unrelated_rows_return_empty_without_error(monkeypatch):
    html = ('<ul><li><div class="subject"><a href="/no/1">보험업 감독규정 개정</a></div>'
            '<div class="day">2026-09-30</div></li></ul>')
    monkeypatch.setattr(fsc._http, "get_govt", _route(html))
    monkeypatch.setattr("time.sleep", lambda s: None)
    assert fsc.fetch(max_pages=1) == []


# 2026-11-13: 날짜가 깨진 행이 섞여도 나머지는 수집되고 부분 실패로 기록 / 전부 깨지면 실패
def _fsc_li(title, day, n):
    return (f'<li><div class="subject"><a href="/no010101/{n}">{title}</a></div>'
            f'<div class="day">{day}</div></li>')


def _mock_fsc(monkeypatch, lis, notice_html=UNRELATED_NOTICE):
    html = "<ul>" + "".join(lis) + "</ul>"
    monkeypatch.setattr(fsc._http, "get_govt", _route(html, notice_html))
    monkeypatch.setattr("time.sleep", lambda s: None)
    skipped = []
    monkeypatch.setattr(fsc._excluded_log, "skip", lambda **kw: skipped.append(kw))
    return skipped


def test_fsc_bad_date_row_skipped_rest_kept_and_partial(monkeypatch):
    from sources import _source_health as sh
    skipped = _mock_fsc(monkeypatch, [
        _fsc_li("금융위원회, 내부회계관리제도 평가·보고 기준 개정", "2026.11.12", 1),
        _fsc_li("ESG 공시기준 로드맵 발표", "2026-11-12", 2),
    ])
    with pytest.raises(sh.PartialFetch) as ei:
        fsc.fetch(max_pages=1)
    assert [i["title"] for i in ei.value.items] == ["ESG 공시기준 로드맵 발표"]
    assert set(ei.value.failed) == {"list"} and "행 1개 해석 실패" in ei.value.failed["list"]
    assert ei.value.part_of is fsc.part_of
    bad = [x for x in skipped if x["reason"] == "collect:row_parse_error"]
    assert len(bad) == 1 and "내부회계관리제도" in bad[0]["title"]


def test_fsc_all_rows_bad_date_is_failure_not_empty_success(monkeypatch):
    # 전엔 행 수를 날짜 해석 전에 세서 이 경우 "0건 정상"이 됐다.
    # 2026-11-14: notice는 정상이라 소스 전체가 아니라 list 부분 실패로 올라온다.
    from sources import _source_health as sh
    _mock_fsc(monkeypatch, [_fsc_li("보험업 감독규정 개정", "2026.11.12", 1)])
    with pytest.raises(sh.PartialFetch) as ei:
        fsc.fetch(max_pages=1)
    assert set(ei.value.failed) == {"list"} and "행 0개" in ei.value.failed["list"]


def test_fsc_page_failure_is_partial(monkeypatch):
    from sources import _source_health as sh
    good = "<ul>" + _fsc_li("ESG 공시기준 로드맵 발표", "2026-11-12", 2) + "</ul>"

    def get(url, params, **kw):
        if "po040301" in url:
            return SimpleNamespace(text=UNRELATED_NOTICE)
        if params["curPage"] == 2:
            raise RuntimeError("read timeout")
        return SimpleNamespace(text=good)
    monkeypatch.setattr(fsc._http, "get_govt", get)
    monkeypatch.setattr("time.sleep", lambda s: None)
    with pytest.raises(sh.PartialFetch) as ei:
        fsc.fetch(max_pages=2)
    assert "page=2" in ei.value.failed["list"] and len(ei.value.items) == 1


# ── 2026-11-14: fsc notice(입법예고/규정변경예고, /po040301) ─────────────────────────
def test_fsc_notice_matching_row_becomes_item(monkeypatch):
    day = _recent()
    notice = "<ul>" + _notice_li("「외부감사 및 회계 등에 관한 규정」일부개정고시안 규정변경예고", day, 4170,
                                 period=("2026-09-18", "2026-09-28")) + "</ul>"
    _mock_fsc(monkeypatch, [_fsc_li("보험업 감독규정 개정", "2026-11-12", 1)], notice_html=notice)
    items = fsc.fetch(max_pages=1)
    assert len(items) == 1
    it = items[0]
    assert it["urls"]["official"] == "https://www.fsc.go.kr/po040301/view?noticeId=4170"
    assert it["published_at"] == day and it["effective_date"] is None
    assert it["_body"] == "의견 접수기간 2026.09.18~2026.09.28"
    assert it["attachments"][0]["name"].startswith("1. 공고문")
    assert fsc.part_of(it) == "notice"


def test_fsc_notice_unrelated_rows_is_normal_zero(monkeypatch):
    skipped = _mock_fsc(monkeypatch, [_fsc_li("보험업 감독규정 개정", "2026-11-12", 1)])
    assert fsc.fetch(max_pages=1) == []
    assert any(s["reason"] == "collect:no_category" and "예금자보호법" in s["title"] for s in skipped)


def test_fsc_notice_no_rows_is_partial_and_list_kept(monkeypatch):
    from sources import _source_health as sh
    _mock_fsc(monkeypatch, [_fsc_li("ESG 공시기준 로드맵 발표", "2026-11-12", 2)],
              notice_html="<html>차단</html>")
    with pytest.raises(sh.PartialFetch) as ei:
        fsc.fetch(max_pages=1)
    assert set(ei.value.failed) == {"notice"} and "행 0개" in ei.value.failed["notice"]
    assert [i["title"] for i in ei.value.items] == ["ESG 공시기준 로드맵 발표"]


def test_fsc_notice_bad_row_isolated(monkeypatch):
    from sources import _source_health as sh
    notice = ("<ul>" + _notice_li("「외부감사 및 회계 등에 관한 규정」 개정고시안 규정변경예고", "2026.11.02", 1)
              + _notice_li("「예금자보호법」 일부개정법률안 입법예고", _recent(), 2) + "</ul>")
    skipped = _mock_fsc(monkeypatch, [_fsc_li("보험업 감독규정 개정", "2026-11-12", 1)], notice_html=notice)
    with pytest.raises(sh.PartialFetch) as ei:
        fsc.fetch(max_pages=1)
    assert set(ei.value.failed) == {"notice"} and "행 1개 해석 실패" in ei.value.failed["notice"]
    assert [s for s in skipped if s["reason"] == "collect:row_parse_error"]


def test_fsc_notice_stops_paging_past_window_and_skips_old_rows(monkeypatch):
    pages = {1: "<ul>" + _notice_li("「예금자보호법」 개정안 입법예고", _recent(), 2)
                + _notice_li("「외부감사 및 회계 등에 관한 규정」 개정고시안 규정변경예고", _recent(400), 1)
                + "</ul>"}
    calls = []

    def get(url, params=None, **kw):
        if "po040301" in url:
            calls.append(params["curPage"])
            return SimpleNamespace(text=pages.get(params["curPage"], "<ul></ul>"))
        return SimpleNamespace(text="<ul>" + _fsc_li("보험업 감독규정 개정", "2026-11-12", 1) + "</ul>")
    monkeypatch.setattr(fsc._http, "get_govt", get)
    monkeypatch.setattr("time.sleep", lambda s: None)
    skipped = []
    monkeypatch.setattr(fsc._excluded_log, "skip", lambda **kw: skipped.append(kw))
    assert fsc.fetch(max_pages=1) == []
    assert calls == [1]  # 페이지의 가장 오래된 행이 기간 밖 → 다음 페이지는 안 읽음
    assert any(s["reason"] == "collect:out_of_window" and "외부감사" in s["title"] for s in skipped)


def test_fsc_notice_reads_next_page_while_in_window(monkeypatch):
    pages = {1: "<ul>" + _notice_li("「예금자보호법」 개정안 입법예고", _recent(1), 2) + "</ul>",
             2: "<ul>" + _notice_li("「은행법」 개정안 입법예고", _recent(400), 1) + "</ul>"}
    calls = []

    def get(url, params=None, **kw):
        if "po040301" in url:
            calls.append(params["curPage"])
            return SimpleNamespace(text=pages.get(params["curPage"], "<ul></ul>"))
        return SimpleNamespace(text="<ul>" + _fsc_li("보험업 감독규정 개정", "2026-11-12", 1) + "</ul>")
    monkeypatch.setattr(fsc._http, "get_govt", get)
    monkeypatch.setattr("time.sleep", lambda s: None)
    monkeypatch.setattr(fsc._excluded_log, "skip", lambda **kw: None)
    fsc.fetch(max_pages=1)
    assert calls == [1, 2]


def test_fsc_both_parts_failed_raises(monkeypatch):
    monkeypatch.setattr(fsc._http, "get_govt", lambda *a, **kw: SimpleNamespace(text="<html>차단</html>"))
    monkeypatch.setattr("time.sleep", lambda s: None)
    with pytest.raises(RuntimeError, match="list: .*notice: "):
        fsc.fetch(max_pages=1)


def test_fsc_tracked_parts_match_main_sub_sources():
    from sources import main
    assert tuple(main.SUB_SOURCES["fsc"]) == fsc.TRACKED_PARTS


def test_policy_briefing_raises_when_no_rows(monkeypatch):
    monkeypatch.setattr(policy_briefing._http, "get_govt",
                        lambda *a, **kw: SimpleNamespace(text="<html>차단</html>"))
    with pytest.raises(RuntimeError):
        policy_briefing.fetch(max_pages=2)


def test_policy_briefing_other_ministries_only_is_normal_zero(monkeypatch):
    html = ('<ul><li><a href="/briefing/pressReleaseView.do?newsId=1"><strong>고용 동향</strong></a>'
            '<span class="source"><span>2026.09.30</span><span>고용노동부</span></span></li></ul>')
    monkeypatch.setattr(policy_briefing._http, "get_govt", lambda *a, **kw: SimpleNamespace(text=html))
    assert policy_briefing.fetch(max_pages=1) == []


# ── 2026-11-14: fsc notice만 끄기(data/source_toggles.yml fsc_notice) ────────────────
def test_fsc_disabled_notice_is_not_requested(monkeypatch):
    monkeypatch.setattr(fsc, "DISABLED_SOURCES", {"fsc_notice": ""})
    urls = []

    def get(url, *a, **kw):
        urls.append(url)
        return SimpleNamespace(text="<ul>" + _fsc_li("ESG 공시기준 로드맵 발표", "2026-11-12", 2) + "</ul>")
    monkeypatch.setattr(fsc._http, "get_govt", get)
    monkeypatch.setattr("time.sleep", lambda s: None)
    items = fsc.fetch(max_pages=1)
    assert [i["title"] for i in items] == ["ESG 공시기준 로드맵 발표"]
    assert not any("po040301" in u for u in urls)
