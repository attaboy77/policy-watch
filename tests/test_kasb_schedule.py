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
OTHER = {"id": "n", "urls": {"official": "https://www.kasb.or.kr/front/board/comm010View.do?seq=1"}}
SCHED = {"id": "s", "urls": {"official": "https://www.kasb.or.kr/front/board/calViewA.do?seq=1132"}}


def _patch_parts(monkeypatch, schedule):
    monkeypatch.setattr(kasb, "fetch_notices", lambda **kw: [OTHER])
    monkeypatch.setattr(kasb, "fetch_qna", lambda: [])
    monkeypatch.setattr(kasb, "fetch_schedule", schedule)
    monkeypatch.setattr(kasb, "fetch_revisions", lambda: [])
    monkeypatch.setattr(kasb, "fetch_kssb_voluntary_standards", lambda: [])


def test_all_ok(monkeypatch):
    _patch_parts(monkeypatch, lambda **kw: [SCHED])
    assert kasb.fetch() == [OTHER, SCHED]


def _boom(**kw):
    raise ValueError("unconverted data remains: ~ 2026-11-06")


@pytest.mark.parametrize("schedule", [_boom, lambda **kw: []])
def test_schedule_failure_or_empty_is_partial(monkeypatch, schedule):
    _patch_parts(monkeypatch, schedule)
    with pytest.raises(sh.PartialFetch) as ei:
        kasb.fetch()
    assert ei.value.items == [OTHER]
    assert set(ei.value.failed) == {"schedule"}
    assert ei.value.part_of is kasb.part_of


def test_part_of():
    assert kasb.part_of(SCHED) == "schedule"
    assert kasb.part_of(OTHER) == "other"
