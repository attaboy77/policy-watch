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
    monkeypatch.setattr(fsc._http, "get_govt", lambda *a, **kw: SimpleNamespace(text=html))
    monkeypatch.setattr("time.sleep", lambda s: None)
    assert fsc.fetch(max_pages=1) == []


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
