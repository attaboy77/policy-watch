# -*- coding: utf-8 -*-
"""sources/google_news.py 단위 테스트 (네트워크 모킹, 실제 요청 없음)."""
import time
from datetime import date
from types import SimpleNamespace

import pytest

from sources import google_news as gn


class _FakeResp:
    def __init__(self, content: bytes):
        self.content = content


def _entry(title, link, source_href=None, published=(2026, 8, 5, 0, 0, 0, 0, 0, 0)):
    ns = SimpleNamespace(title=title, link=link)
    if published:
        ns.published_parsed = time.struct_time(published)
    if source_href:
        ns.source = SimpleNamespace(href=source_href)
    return ns


def test_fetch_category_filters_noise_by_default(monkeypatch):
    entries = [
        _entry("법인세법 시행령 개정안 입법예고", "https://moef.go.kr/a", "moef.go.kr"),
        _entry("이 종목 테마주 급등 국세청 세법", "https://random.example.com/b"),
    ]
    monkeypatch.setattr(gn, "_http", SimpleNamespace(get=lambda url, **kw: _FakeResp(b"")))
    monkeypatch.setattr(gn.feedparser, "parse", lambda content: SimpleNamespace(entries=entries))

    kept = gn.fetch_category("tax")
    assert len(kept) == 1
    assert kept[0]["title"].startswith("법인세법")
    assert kept[0]["trust_tier"] == 1


def test_fetch_category_filter_noise_false_keeps_and_flags(monkeypatch):
    entries = [
        _entry("이 종목 테마주 급등 국세청 세법", "https://random.example.com/b"),
    ]
    monkeypatch.setattr(gn, "_http", SimpleNamespace(get=lambda url, **kw: _FakeResp(b"")))
    monkeypatch.setattr(gn.feedparser, "parse", lambda content: SimpleNamespace(entries=entries))

    raw = gn.fetch_category("tax", filter_noise=False)
    assert len(raw) == 1
    assert raw[0]["is_noise"] is True


def test_fetch_category_skips_entries_without_title_or_link(monkeypatch):
    entries = [
        _entry("", "https://moef.go.kr/a"),
        _entry("세법 개정안 발표", ""),
        _entry("세법 개정안 발표", "https://moef.go.kr/c"),
    ]
    monkeypatch.setattr(gn, "_http", SimpleNamespace(get=lambda url, **kw: _FakeResp(b"")))
    monkeypatch.setattr(gn.feedparser, "parse", lambda content: SimpleNamespace(entries=entries))

    kept = gn.fetch_category("tax")
    assert len(kept) == 1
    assert kept[0]["url"] == "https://moef.go.kr/c"


def test_entry_source_hint_prefers_source_href_over_link():
    e = _entry("세법 개정안 발표", "https://news.google.com/rss/articles/xyz", "moef.go.kr")
    assert gn._entry_source_hint(e) == "moef.go.kr"


def test_entry_source_hint_falls_back_to_link():
    e = _entry("세법 개정안 발표", "https://moef.go.kr/direct")
    assert gn._entry_source_hint(e) == "https://moef.go.kr/direct"


def test_parse_published_reads_published_parsed():
    e = _entry("t", "https://moef.go.kr/x", published=(2026, 8, 5, 0, 0, 0, 0, 0, 0))
    assert gn._parse_published(e) == date(2026, 8, 5)


def test_parse_published_none_when_missing():
    e = _entry("t", "https://moef.go.kr/x", published=None)
    assert gn._parse_published(e) is None


def test_fetch_all_isolates_category_failure(monkeypatch):
    def fake_fetch_category(cat_key, days=90, *, filter_noise=True):
        if cat_key == "tax":
            raise RuntimeError("network down")
        return [{"id": "x", "title": "ok"}]

    monkeypatch.setattr(gn, "fetch_category", fake_fetch_category)
    monkeypatch.setattr(time, "sleep", lambda s: None)

    results = gn.fetch_all()
    assert results["tax"] == []
    assert all(cat in results for cat in ("kifrs", "tax", "icfr", "esg"))
    assert results["kifrs"] == [{"id": "x", "title": "ok"}]
