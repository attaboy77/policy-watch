# -*- coding: utf-8 -*-
"""fss.fetch() 하위 수집(B2/B3) 실패 처리 (2026-10-14). 네트워크 호출 없음."""
import pytest

from sources import _source_health as sh
from sources.official import fss


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch):
    monkeypatch.setattr(fss.time, "sleep", lambda s: None)


B2 = {"id": "b2", "urls": {"official": "https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=1"}}
B3 = {"id": "b3", "urls": {"official": "https://www.k-icfr.org/sub/menu/guideline.asp?rNo=1"}}


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


def test_both_failed_raises_plain_error(monkeypatch):
    monkeypatch.setattr(fss, "fetch_data_board", _boom)
    monkeypatch.setattr(fss, "fetch_kicfr_guidelines", lambda: [])
    with pytest.raises(RuntimeError):
        fss.fetch()


def test_part_of():
    assert fss.part_of(B2) == "b2"
    assert fss.part_of(B3) == "b3"
