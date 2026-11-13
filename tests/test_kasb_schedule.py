# -*- coding: utf-8 -*-
"""KASB 주요일정(C) — 기간형 진행일·행 단위 격리·부분 실패 (2026-11-13). 네트워크 호출 없음."""
from datetime import date

import pytest

from sources import _source_health as sh
from sources.official import kasb


@pytest.fixture(autouse=True)
def _no_side_effects(monkeypatch):
    monkeypatch.setattr(kasb.time, "sleep", lambda s: None)
    monkeypatch.setattr(kasb._excluded_log, "skip", lambda **kw: _SKIPPED.append(kw))
    _SKIPPED.clear()


_SKIPPED: list[dict] = []


# ── [1] 기간형 날짜 ──
@pytest.mark.parametrize("text", [
    "2026-10-30", "2026-10-30 ~ 2026-11-06", "2026-10-30~2026-11-06",
    "2026-10-30 ～ 2026-11-06", "2026-10-30∼2026-11-06", "2026-10-30 − 2026-11-06",
    "2026-10-30 - 2026-11-06", " 2026-10-30 ~2026-11-06 ",
])
def test_range_uses_start_date(text):
    assert kasb._parse_iso_date(text) == date(2026, 10, 30)
    assert kasb._start_date_text(text) == "2026-10-30"


@pytest.mark.parametrize("text", ["", "2026.10.30", "미정", "2026-10-30 ~ 미정"])
def test_bad_date_raises(text):
    with pytest.raises(ValueError):
        kasb._parse_iso_date(text)


# ── [2] 행 단위 격리 ──
def _row(date_text, title, seq, minor="회계기준위원회"):
    return (f"<tr><td>{date_text}</td><td>회계기준</td><td><p>{minor}</p></td>"
            f"<td><a onclick=\"fn_Detail('{seq}')\">{title}</a></td><td>BM Room</td></tr>")


class _Resp:
    def __init__(self, rows):
        self.text = ("<div class='cal_board'><table><tbody>" + "".join(rows)
                     + "</tbody></table></div>")


def _serve(monkeypatch, rows):
    monkeypatch.setattr(kasb._http, "get", lambda *a, **kw: _Resp(rows))


def test_range_row_collected_with_start_date(monkeypatch):
    _serve(monkeypatch, [
        _row("2026-11-06", "2026년 제11회 회계기준위원회(K-IFRS 제1119호 제정안 등)", "1132"),
        _row("2026-10-30 ~ 2026-11-06", "2026년 제9회 지속가능성기준위원회(IFRS 재단 정관 개정 공개초안에 대한 검토 등)",
             "1133", minor="지속가능성기준위원회"),
    ])
    items = kasb.fetch_schedule(fetch_detail=False)
    assert [i["published_at"] for i in items] == ["2026-11-06", "2026-10-30"]
    assert all(i["is_meeting_schedule"] for i in items)


def test_bad_row_skipped_and_logged_rest_kept(monkeypatch):
    _serve(monkeypatch, [
        _row("일정 미정", "2026년 제12회 회계기준위원회", "1140"),
        _row("2026-11-06", "2026년 제11회 회계기준위원회(K-IFRS 제1119호 제정안 등)", "1132"),
    ])
    items = kasb.fetch_schedule(fetch_detail=False)
    assert [i["urls"]["official"].rsplit("=", 1)[1] for i in items] == ["1132"]
    bad = [s for s in _SKIPPED if s["reason"] == "collect:row_parse_error"]
    assert len(bad) == 1
    assert "제12회 회계기준위원회" in bad[0]["title"] and "일정 미정" in bad[0]["title"]
    assert bad[0]["url"].endswith("seq=1140")


# ── [3] 부분 실패 ──
NOTICE = {"id": "n", "urls": {"official": "https://www.kasb.or.kr/front/board/comm010View.do?seq=1"}}
QNA = {"id": "q", "urls": {"official": "https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=2&ctgCd=016002&replySummary=Y"}}
SCHED = {"id": "s", "urls": {"official": "https://www.kasb.or.kr/front/board/calViewA.do?seq=1132"}}
REV = {"id": "r", "urls": {"official": "https://www.kasb.or.kr/front/board/List2006.do"}}


def _patch_parts(monkeypatch, *, notices=None, qna=None, schedule=None):
    monkeypatch.setattr(kasb, "fetch_notices", notices or (lambda **kw: [NOTICE]))
    monkeypatch.setattr(kasb, "fetch_qna", qna or (lambda: [QNA]))
    monkeypatch.setattr(kasb, "fetch_schedule", schedule or (lambda **kw: [SCHED]))
    monkeypatch.setattr(kasb, "fetch_revisions", lambda: [REV])
    monkeypatch.setattr(kasb, "fetch_kssb_voluntary_standards", lambda: [])
    kasb._ROW_ERRORS.clear()


def test_all_ok(monkeypatch):
    _patch_parts(monkeypatch)
    assert kasb.fetch() == [NOTICE, QNA, SCHED, REV]


def _boom(**kw):
    raise ValueError("unconverted data remains: ~ 2026-11-06")


@pytest.mark.parametrize("part", ["notices", "qna", "schedule"])
@pytest.mark.parametrize("broken", ["boom", "empty"])
def test_tracked_part_failure_or_empty_is_partial(monkeypatch, part, broken):
    fn = _boom if broken == "boom" else (lambda **kw: [])
    _patch_parts(monkeypatch, **{part: fn})
    with pytest.raises(sh.PartialFetch) as ei:
        kasb.fetch()
    assert set(ei.value.failed) == {part}
    assert ei.value.part_of is kasb.part_of
    assert REV in ei.value.items


def test_part_of():
    assert kasb.part_of(SCHED) == "schedule"
    assert kasb.part_of(NOTICE) == "notices"
    assert kasb.part_of(QNA) == "qna"
    assert kasb.part_of(REV) == "other"


# ── 2026-11-13: A1·A3 — 날짜가 깨진 행이 섞여도 나머지는 수집되고 부분 실패로 기록 ──
def _notice_row(date_text, title, seq, cat="회계기준소식"):
    return (f"<tr><td>{seq}</td><td>{cat}</td><td><a onclick=\"fn_Detail('{seq}')\">{title}</a></td>"
            f"<td><p class='board_date'>{date_text}</p></td></tr>")


def _qna_row(date_text, title, seq):
    return (f"<tr><td>{seq}</td><td><a onclick=\"fn_Detail('{seq}','016002')\">{title}</a></td>"
            f"<td><p class='board_date'>{date_text}</p></td></tr>")


class _Table:
    def __init__(self, rows):
        self.text = "<table><tbody>" + "".join(rows) + "</tbody></table>"


def _table(rows):
    return _Table(rows)


def _real_parts(monkeypatch, notice_rows, qna_rows):
    def get(url, *a, **kw):
        if "comm010List" in url:
            return _table(notice_rows)
        if "allReplySummaryList" in url:
            return _table(qna_rows)
        raise AssertionError(url)
    monkeypatch.setattr(kasb._http, "get", get)
    monkeypatch.setattr(kasb, "fetch_schedule", lambda **kw: [SCHED])
    monkeypatch.setattr(kasb, "fetch_revisions", lambda: [REV])
    monkeypatch.setattr(kasb, "fetch_kssb_voluntary_standards", lambda: [])


GOOD_NOTICE = _notice_row("2026-11-10", "K-IFRS 제1119호 제정 공표", "501")
BAD_NOTICE = _notice_row("2026/11/11", "K-IFRS 제1021호 개정 공표", "502")
GOOD_QNA = _qna_row("2026-11-10", "K-IFRS 제1115호 수익 인식 질의회신", "601")
BAD_QNA = _qna_row("11월 11일", "K-IFRS 제1116호 리스 질의회신", "602")


@pytest.mark.parametrize("part", ["notices", "qna"])
def test_bad_date_row_skipped_rest_kept_and_partial(monkeypatch, part):
    notice_rows = [BAD_NOTICE, GOOD_NOTICE] if part == "notices" else [GOOD_NOTICE]
    qna_rows = [BAD_QNA, GOOD_QNA] if part == "qna" else [GOOD_QNA]
    _real_parts(monkeypatch, notice_rows, qna_rows)
    monkeypatch.setattr(kasb, "_qna_attachment_text", lambda row, seq: None)
    with pytest.raises(sh.PartialFetch) as ei:
        kasb.fetch(fetch_detail=False)
    assert set(ei.value.failed) == {part}
    assert "행 1개 해석 실패" in ei.value.failed[part]
    titles = [i.get("title") for i in ei.value.items]
    assert "K-IFRS 제1119호 제정 공표" in titles and "K-IFRS 제1115호 수익 인식 질의회신" in titles
    assert "K-IFRS 제1021호 개정 공표" not in titles and "K-IFRS 제1116호 리스 질의회신" not in titles
    bad = [x for x in _SKIPPED if x["reason"] == "collect:row_parse_error"]
    assert len(bad) == 1
    assert ("제1021호" if part == "notices" else "제1116호") in bad[0]["title"]
