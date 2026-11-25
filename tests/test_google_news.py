# -*- coding: utf-8 -*-
"""sources/google_news.py 단위 테스트 (네트워크 모킹, 실제 요청 없음)."""
import time
from datetime import date, timedelta
from types import SimpleNamespace

import pytest

from sources import google_news as gn


class _FakeResp:
    def __init__(self, content: bytes):
        self.content = content


def _ts(d: date):
    return time.struct_time((d.year, d.month, d.day, 0, 0, 0, 0, 0, 0))


# 기본 발행일은 오늘 — 2026-11-25부터 fetch_category()가 90일 창을 적용해서, 고정 날짜를 쓰면
# 시간이 지나며 테스트가 저절로 깨진다.
def _entry(title, link, source_href=None, published="today"):
    ns = SimpleNamespace(title=title, link=link)
    if published == "today":
        published = _ts(date.today())
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


class TestCollectWindow:
    """2026-11-25: 구글 뉴스도 네이버처럼 수집 기간(기본 90일) 밖 기사를 수집 단계에서 뺀다.
    검색어의 when:90d를 구글이 지키지 않아 옛 기사가 ESG 상한 자리를 날마다 다르게 채웠다."""

    def _run(self, monkeypatch, entries, **kw):
        from sources import _excluded_log
        monkeypatch.setattr(gn, "_http", SimpleNamespace(get=lambda url, **k: _FakeResp(b"")))
        monkeypatch.setattr(gn.feedparser, "parse", lambda content: SimpleNamespace(entries=entries))
        _excluded_log.clear()
        kept = gn.fetch_category("esg", **kw)
        logged = list(_excluded_log.excluded())
        _excluded_log.clear()
        return kept, logged

    def test_old_article_excluded_and_logged(self, monkeypatch):
        old = date.today() - timedelta(days=239)
        entries = [
            _entry("국회 정무위서 지속가능성 공시 로드맵 후퇴 지적 나와", "https://news.google.com/rss/articles/a",
                   "https://www.esgeconomy.com", published=_ts(old)),
            _entry("ESG 공시 의무화 법안 국회 통과", "https://news.google.com/rss/articles/b",
                   "https://www.esgeconomy.com"),
        ]
        kept, logged = self._run(monkeypatch, entries)
        assert [it["url"] for it in kept] == ["https://news.google.com/rss/articles/b"]
        assert [(e["reason"], e["category"], e["source"]) for e in logged] == [
            ("collect:out_of_window", "esg", "ESG경제")]

    def test_boundary_90_days_kept_91_excluded(self, monkeypatch):
        today = date.today()
        entries = [
            _entry("ESG 공시 로드맵 발표 90일", "https://x.example.com/90", published=_ts(today - timedelta(days=90))),
            _entry("ESG 공시 로드맵 발표 91일", "https://x.example.com/91", published=_ts(today - timedelta(days=91))),
        ]
        kept, logged = self._run(monkeypatch, entries)
        assert [it["url"] for it in kept] == ["https://x.example.com/90"]
        assert [e["reason"] for e in logged] == ["collect:out_of_window"]

    def test_missing_published_date_is_kept(self, monkeypatch):
        # 네이버와 같다 — 발행일이 없으면 남긴다(언론 1년 상한 #4도 날짜 없으면 남김).
        entries = [_entry("ESG 공시 로드맵 발표", "https://x.example.com/n", published=None)]
        kept, logged = self._run(monkeypatch, entries)
        assert len(kept) == 1 and kept[0]["published"] is None
        assert logged == []

    def test_days_argument_sets_window(self, monkeypatch):
        entries = [_entry("ESG 공시 로드맵 발표", "https://x.example.com/d",
                          published=_ts(date.today() - timedelta(days=40)))]
        assert len(self._run(monkeypatch, entries, days=30)[0]) == 0
        assert len(self._run(monkeypatch, entries, days=90)[0]) == 1

    def test_window_applies_even_with_filter_noise_false(self, monkeypatch):
        # 노이즈 표시 모드(filter_noise=False)는 노이즈만 남겨 표시한다 — 기간 밖은 네이버처럼 뺀다.
        entries = [_entry("ESG 공시 로드맵 발표", "https://x.example.com/o",
                          published=_ts(date.today() - timedelta(days=200)))]
        assert self._run(monkeypatch, entries, filter_noise=False)[0] == []

    def test_query_still_has_when_clause(self):
        from urllib.parse import unquote_plus
        assert "when:90d" in unquote_plus(gn.google_news_rss_url("esg", days=90))


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


def test_fetch_category_does_not_decode_google_links(monkeypatch):
    """2026-09-08: 디코딩은 fetch_category()가 아니라 main.py 파이프라인 맨
    끝(resolve_finalized_urls)에서 한다 — 여기서는 원래 구글 링크가 그대로
    url/id 양쪽에 쓰여야 한다(나중에 걸러질 항목까지 구글에 요청을 보내지
    않기 위함)."""
    google_link = "https://news.google.com/rss/articles/xyz"
    entries = [_entry("법인세법 개정안 발표", google_link, "intn.co.kr")]
    monkeypatch.setattr(gn, "_http", SimpleNamespace(get=lambda url, **kw: _FakeResp(b"")))
    monkeypatch.setattr(gn.feedparser, "parse", lambda content: SimpleNamespace(entries=entries))
    called = {"decode": False}

    def fake_decode(url):
        called["decode"] = True
        return "https://example.com/real"

    monkeypatch.setattr(gn._google_decode, "decode_google_news_url", fake_decode)

    kept = gn.fetch_category("tax")
    assert len(kept) == 1
    assert kept[0]["url"] == google_link
    assert called["decode"] is False


def test_resolve_news_url_tracks_stats_and_sleeps(monkeypatch):
    gn.reset_decode_stats()
    sleeps = []
    monkeypatch.setattr(gn.time, "sleep", lambda s: sleeps.append(s))
    monkeypatch.setattr(gn._google_decode, "decode_google_news_url", lambda url: "https://real.example.com/a")

    result = gn.resolve_news_url("https://news.google.com/rss/articles/xyz")

    assert result == "https://real.example.com/a"
    assert gn.get_decode_stats() == {"attempted": 1, "success": 1, "reused": 0, "unresolved": 0}
    assert sleeps == [gn.DECODE_SLEEP_SECONDS]


def test_resolve_news_url_stats_count_failure(monkeypatch):
    gn.reset_decode_stats()
    monkeypatch.setattr(gn.time, "sleep", lambda s: None)
    monkeypatch.setattr(gn._google_decode, "decode_google_news_url", lambda url: None)

    result = gn.resolve_news_url("https://news.google.com/rss/articles/xyz")

    assert result == "https://news.google.com/rss/articles/xyz"
    assert gn.get_decode_stats() == {"attempted": 1, "success": 0, "reused": 0, "unresolved": 0}


def test_resolve_news_url_ignores_non_google_links(monkeypatch):
    called = {"decode": False}
    monkeypatch.setattr(gn._google_decode, "decode_google_news_url",
                         lambda url: called.__setitem__("decode", True) or "x")
    result = gn.resolve_news_url("https://moef.go.kr/a")
    assert result == "https://moef.go.kr/a"
    assert called["decode"] is False


class TestResolveFinalizedUrls:
    """2026-09-08: 파이프라인 마지막 단계 — 실제 생존 항목만 디코딩."""

    def test_decodes_google_news_url_in_place(self, monkeypatch):
        monkeypatch.setattr(gn.time, "sleep", lambda s: None)
        monkeypatch.setattr(gn._google_decode, "decode_google_news_url",
                             lambda url: "https://real.example.com/a")
        items = [{"id": "x", "urls": {"news": "https://news.google.com/rss/articles/xyz", "official": None}}]

        gn.resolve_finalized_urls(items)

        assert items[0]["urls"]["news"] == "https://real.example.com/a"

    def test_failure_without_prior_url_is_returned_as_unresolved(self, monkeypatch):
        """2026-11-05: 전날 URL도 없으면 구글 링크 그대로 돌려준다 — 빼는 건 main.py."""
        monkeypatch.setattr(gn.time, "sleep", lambda s: None)
        monkeypatch.setattr(gn._google_decode, "decode_google_news_url", lambda url: None)
        google_link = "https://news.google.com/rss/articles/xyz"
        items = [{"id": "x", "urls": {"news": google_link, "official": None}}]

        unresolved = gn.resolve_finalized_urls(items)

        assert unresolved == items
        assert items[0]["urls"]["news"] == google_link
        assert gn.get_decode_stats()["unresolved"] == 1

    def test_failure_reuses_prior_url_for_same_id(self, monkeypatch):
        """2026-11-05: 11/3처럼 구글이 막힌 날 — 전날 복원해 둔 원문 URL을 쓴다."""
        monkeypatch.setattr(gn.time, "sleep", lambda s: None)
        monkeypatch.setattr(gn._google_decode, "decode_google_news_url", lambda url: None)
        items = [{"id": "x", "urls": {"news": "https://news.google.com/rss/articles/xyz", "official": None}}]

        unresolved = gn.resolve_finalized_urls(items, {"x": "https://www.impacton.net/a"})

        assert unresolved == []
        assert items[0]["urls"]["news"] == "https://www.impacton.net/a"
        assert gn.get_decode_stats() == {"attempted": 1, "success": 0, "reused": 1, "unresolved": 0}

    def test_success_does_not_use_prior_url(self, monkeypatch):
        monkeypatch.setattr(gn.time, "sleep", lambda s: None)
        monkeypatch.setattr(gn._google_decode, "decode_google_news_url", lambda url: "https://new.example.com/a")
        items = [{"id": "x", "urls": {"news": "https://news.google.com/rss/articles/xyz", "official": None}}]

        gn.resolve_finalized_urls(items, {"x": "https://old.example.com/a"})

        assert items[0]["urls"]["news"] == "https://new.example.com/a"
        assert gn.get_decode_stats()["reused"] == 0

    def test_ignores_non_google_and_missing_urls(self, monkeypatch):
        called = {"decode": False}
        monkeypatch.setattr(gn._google_decode, "decode_google_news_url",
                             lambda url: called.__setitem__("decode", True) or "x")
        items = [
            {"id": "official1", "urls": {"news": None, "official": "https://law.go.kr/a"}},
            {"id": "naver1", "urls": {"news": "https://n.news.naver.com/mnews/article/1", "official": None}},
        ]

        gn.resolve_finalized_urls(items)

        assert called["decode"] is False
        assert items[1]["urls"]["news"] == "https://n.news.naver.com/mnews/article/1"

    def test_resets_stats_and_logs_summary(self, monkeypatch, capsys):
        monkeypatch.setattr(gn.time, "sleep", lambda s: None)
        monkeypatch.setattr(gn._google_decode, "decode_google_news_url",
                             lambda url: None if "fail" in url else "https://real.example.com/ok")
        gn._DECODE_STATS["attempted"] = 99  # 이전 실행 잔재 시뮬레이션
        items = [
            {"id": "a", "urls": {"news": "https://news.google.com/rss/articles/ok1", "official": None}},
            {"id": "b", "urls": {"news": "https://news.google.com/rss/articles/fail1", "official": None}},
            {"id": "c", "urls": {"news": "https://news.google.com/rss/articles/ok2", "official": None}},
        ]

        gn.resolve_finalized_urls(items)

        assert gn.get_decode_stats() == {"attempted": 3, "success": 2, "reused": 0, "unresolved": 1}
        out = capsys.readouterr().out
        assert "URL 복원 2/3건, 실패 1건 (전날 URL 재사용 0건, 복원 못 해 제외 1건)" in out

    def test_no_google_links_prints_nothing(self, monkeypatch, capsys):
        items = [{"id": "a", "urls": {"news": None, "official": "https://law.go.kr/a"}}]
        gn.resolve_finalized_urls(items)
        assert capsys.readouterr().out == ""


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


def test_prior_news_urls_skips_google_links_and_missing():
    data = {"items": [
        {"id": "a", "urls": {"news": "https://www.esgeconomy.com/1", "official": None}},
        {"id": "b", "urls": {"news": "https://news.google.com/rss/articles/b", "official": None}},
        {"id": "c", "urls": {"news": None, "official": "https://law.go.kr/c"}},
    ]}
    assert gn.prior_news_urls(data) == {"a": "https://www.esgeconomy.com/1"}
    assert gn.prior_news_urls(None) == {}
