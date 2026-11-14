# -*- coding: utf-8 -*-
"""fss.fetch() 하위 수집 실패 처리 (2026-10-14 B2/B3, 2026-11-14 press/notes). 네트워크 호출 없음."""
from types import SimpleNamespace

import pytest

from sources import _source_health as sh
from sources.official import fss


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch):
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)


@pytest.fixture(autouse=True)
def _quiet_new_parts(monkeypatch):
    """B2/B3 테스트가 press·notes 때문에 실사이트에 나가지 않게 기본은 '행은 읽었고 관련 0건'."""
    monkeypatch.setattr(fss, "fetch_press", lambda: ([], []))
    monkeypatch.setattr(fss, "fetch_disclosure_notes", lambda: ([], []))


B2 = {"id": "b2", "urls": {"official": "https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=1"}}
B3 = {"id": "b3", "urls": {"official": "https://www.k-icfr.org/sub/menu/guideline.asp?rNo=1"}}
PRESS = {"id": "p", "urls": {"official": "https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=9"}}
NOTE = {"id": "n", "urls": {"official": "https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=7"}}


def _boom():
    raise RuntimeError("timeout")


def test_both_ok(monkeypatch):
    monkeypatch.setattr(fss, "fetch_data_board", lambda: [B2])
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [B3])
    assert fss.fetch() == [B2, B3]


@pytest.mark.parametrize("b2", [_boom, lambda: []])
def test_b2_failure_or_empty_is_partial(monkeypatch, b2):
    monkeypatch.setattr(fss, "fetch_data_board", b2)
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [B3])
    with pytest.raises(sh.PartialFetch) as ei:
        fss.fetch()
    assert ei.value.items == [B3]
    assert set(ei.value.failed) == {"b2"}
    assert ei.value.part_of is fss.part_of


def test_b3_failure_is_partial(monkeypatch):
    monkeypatch.setattr(fss, "fetch_data_board", lambda: [B2])
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", _boom)
    with pytest.raises(sh.PartialFetch) as ei:
        fss.fetch()
    assert set(ei.value.failed) == {"b3"}


def test_b2_b3_failed_but_new_parts_ok_is_partial(monkeypatch):
    # 2026-11-14: 하위 수집이 넷이 되면서 B2·B3만 실패한 건 부분 실패다(전엔 소스 전체 실패).
    monkeypatch.setattr(fss, "fetch_data_board", _boom)
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [])
    monkeypatch.setattr(fss, "fetch_press", lambda: ([PRESS], []))
    with pytest.raises(sh.PartialFetch) as ei:
        fss.fetch()
    assert set(ei.value.failed) == {"b2", "b3"} and ei.value.items == [PRESS]


def test_all_parts_failed_raises_plain_error(monkeypatch):
    monkeypatch.setattr(fss, "fetch_data_board", _boom)
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [])
    monkeypatch.setattr(fss, "fetch_press", _boom)
    monkeypatch.setattr(fss, "fetch_disclosure_notes", _boom)
    with pytest.raises(RuntimeError, match="모두 실패"):
        fss.fetch()


def test_part_of():
    assert fss.part_of(B2) == "b2"
    assert fss.part_of(B3) == "b3"
    assert fss.part_of(PRESS) == "press"
    assert fss.part_of(NOTE) == "notes"


def test_tracked_parts_match_main_sub_sources():
    from sources import main
    assert tuple(main.SUB_SOURCES["fss"]) == fss.TRACKED_PARTS


# ── 2026-11-14: press(B0000188)·notes(B0000128) 게시판 파싱 ─────────────────────────
def _row(title, day, n, *, board="B0000188", attach=None):
    files = ""
    if attach:
        files = (f'<td><ul><li><a href="/fss/cmmn/file/fileDown.do?atchFileId=x&fileSn=1">'
                 f'<span class="name">{attach}</span></a></li></ul></td>')
    else:
        files = "<td></td>"
    return (f'<tr><td class="num">{n}</td><td class="title"><a href="/fss/bbs/{board}/view.do?nttId={n}'
            f'&menuNo=1">{title}</a></td><td>회계감독국</td><td>{day}</td>{files}<td>10</td></tr>')


def _mock_board(monkeypatch, pages):
    """pages: pageIndex → tbody 행 HTML 리스트. 요청 파라미터를 기록해 돌려준다."""
    calls = []

    def get(url, params=None, headers=None, **kw):
        calls.append(dict(params))
        rows = pages.get(params["pageIndex"], [])
        return SimpleNamespace(text=f"<table><tbody>{''.join(rows)}</tbody></table>")
    monkeypatch.setattr(fss._http, "get", get)
    skipped = []
    monkeypatch.setattr(fss._excluded_log, "skip", lambda **kw: skipped.append(kw))
    return calls, skipped


def test_press_keeps_matching_rows_with_category_and_row_attachments(monkeypatch):
    monkeypatch.undo()  # autouse 스텁을 풀고 진짜 fetch_press를 쓴다
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    calls, skipped = _mock_board(monkeypatch, {1: [
        _row("2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요", "2026-10-13", 1, attach="보도자료.hwpx"),
        _row("증권사 발행어음, IMA 부문 C-level 임원 간담회 개최", "2026-11-12", 2),
    ]})
    items, reasons = fss.fetch_press()
    assert reasons == []
    assert [i["title"] for i in items] == ["2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요"]
    it = items[0]
    assert it["category"] == "kifrs" and it["source"]["name"] == "금융감독원"
    assert it["attachments"][0]["name"] == "보도자료.hwpx"
    assert it["attachments"][0]["url"].startswith("https://www.fss.or.kr/fss/cmmn/file/fileDown.do")
    assert fss.part_of(it) == "press"
    # 서버 쪽 날짜 필터·pageUnit을 건다(최근 COLLECT_WINDOW_DAYS일)
    assert calls[0]["pageUnit"] == fss.PRESS_PAGE_UNIT and calls[0]["sdate"] and calls[0]["edate"]
    assert any(s["reason"] == "collect:no_category" for s in skipped)


def test_press_unrelated_rows_only_is_normal_zero(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    _mock_board(monkeypatch, {1: [_row("가상자산사업자 보안 강화 조치", "2026-11-12", 1)]})
    assert fss.fetch_press() == ([], [])


def test_press_no_rows_raises(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    _mock_board(monkeypatch, {})
    with pytest.raises(RuntimeError, match="행 0개"):
        fss.fetch_press()


def test_press_bad_date_row_isolated_and_reported(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    _, skipped = _mock_board(monkeypatch, {1: [
        _row("K-IFRS 제1118호 주석공시 모범사례", "2026.10.13", 1),
        _row("2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요", "2026-10-13", 2),
    ]})
    items, reasons = fss.fetch_press()
    assert len(items) == 1 and "행 1개 해석 실패" in reasons[0]
    assert [s for s in skipped if s["reason"] == "collect:row_parse_error"]


def test_press_all_rows_bad_date_is_failure_not_empty_success(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    _mock_board(monkeypatch, {1: [_row("가상자산사업자 보안 강화", "2026.11.12", 1)]})
    with pytest.raises(RuntimeError, match="전부 해석 실패"):
        fss.fetch_press()


def test_press_reads_next_page_only_when_page_is_full(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    monkeypatch.setattr(fss, "PRESS_PAGE_UNIT", 2)
    full = [_row("가상자산 보안", "2026-11-12", 1), _row("IMA 간담회", "2026-11-11", 2)]
    calls, _ = _mock_board(monkeypatch, {1: full, 2: [_row("ESG 공시 로드맵", "2026-11-10", 3)]})
    fss.fetch_press()
    assert [c["pageIndex"] for c in calls] == [1, 2]


def test_press_page_failure_after_first_page_is_reported(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    monkeypatch.setattr(fss, "PRESS_PAGE_UNIT", 1)

    def get(url, params=None, headers=None, **kw):
        if params["pageIndex"] == 2:
            raise RuntimeError("read timeout")
        return SimpleNamespace(text="<table><tbody>"
                               + _row("가상자산 보안", "2026-11-12", 1) + "</tbody></table>")
    monkeypatch.setattr(fss._http, "get", get)
    monkeypatch.setattr(fss._excluded_log, "skip", lambda **kw: None)
    items, reasons = fss.fetch_press()
    assert items == [] and "page=2" in reasons[0]


def test_new_part_partial_reasons_reach_partialfetch(monkeypatch):
    monkeypatch.setattr(fss, "fetch_data_board", lambda: [B2])
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [B3])
    monkeypatch.setattr(fss, "fetch_press", lambda: ([PRESS], ["행 1개 해석 실패(건너뜀)"]))
    with pytest.raises(sh.PartialFetch) as ei:
        fss.fetch()
    assert set(ei.value.failed) == {"press"} and PRESS in ei.value.items


def test_notes_board_reads_without_date_window(monkeypatch):
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    calls, _ = _mock_board(monkeypatch, {1: [
        _row("K-IFRS 제1118호 영향 관련 사전 주석공시 모범사례", "2026-04-15", 13, board="B0000128"),
    ]})
    items, reasons = fss.fetch_disclosure_notes()
    assert reasons == [] and len(items) == 1
    assert fss.part_of(items[0]) == "notes"
    assert "sdate" not in calls[0]


# ── 2026-11-14: data/source_toggles.yml로 하위 수집만 끄기 ─────────────────────────
def test_disabled_press_is_skipped_not_failed(monkeypatch):
    monkeypatch.setattr(fss, "DISABLED_SOURCES", {"fss_press": ""})
    monkeypatch.setattr(fss, "fetch_data_board", lambda: [B2])
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [B3])
    monkeypatch.setattr(fss, "fetch_press", lambda: pytest.fail("꺼진 press를 호출함"))
    assert fss.fetch() == [B2, B3]


def test_disabled_parts_not_counted_for_all_failed(monkeypatch):
    monkeypatch.setattr(fss, "DISABLED_SOURCES", {"fss_press": "", "fss_notes": ""})
    monkeypatch.setattr(fss, "fetch_data_board", _boom)
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", _boom)
    with pytest.raises(RuntimeError, match="모두 실패"):
        fss.fetch()


def test_toggle_yml_disables_single_part(tmp_path):
    from sources import _config
    p = tmp_path / "toggles.yml"
    p.write_text("sources:\n  - name: fss_notes\n    enabled: false\n  - name: fss_press\n    enabled: true\n",
                 encoding="utf-8")
    assert set(_config._load_disabled_sources(str(p))) == {"fss_notes"}


def test_press_id_does_not_change_with_list_query_params(monkeypatch):
    # 실측(11/14): 목록 href에 sdate·edate·pageIndex가 붙는다 — 날짜가 바뀌어도 id는 같아야 한다.
    monkeypatch.undo()
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)
    monkeypatch.setattr(fss._excluded_log, "skip", lambda **kw: None)
    title = "2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요"
    ids = []
    for sdate, page in (("2026-08-16", 1), ("2026-08-17", 2)):
        row = (f'<tr><td>1</td><td class="title"><a href="/fss/bbs/B0000188/view.do?nttId=240494&menuNo=200218'
               f'&sdate={sdate}&edate=2026-11-14&pageIndex={page}">{title}</a></td><td>회계감독국</td>'
               f'<td>2026-10-13</td><td></td></tr>')
        monkeypatch.setattr(fss._http, "get", lambda *a, _r=row, **kw: SimpleNamespace(
            text=f"<table><tbody>{_r}</tbody></table>"))
        items, _ = fss.fetch_press()
        ids.append((items[0]["id"], items[0]["urls"]["official"]))
    assert ids[0] == ids[1]
    assert ids[0][1] == "https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=240494&menuNo=200218"
