# -*- coding: utf-8 -*-
"""sources/_google_decode.py 단위 테스트 (네트워크 모킹, 실제 요청 없음).

실측(2026-09-08)으로 확인한 실제 응답 모양을 그대로 재현해서 파싱 로직을
검증한다 — 응답 파싱 관련 리그레션을 잡는 게 목적이라 진짜 배관(HTTP)은
전부 monkeypatch로 대체한다."""
import json

import pytest

from sources import _google_decode as gd

_GOOGLE_URL = "https://news.google.com/rss/articles/CBMitest?oc=5"

_HTML_WITH_TOKENS = (
    '<div data-n-a-id="CBMitest" data-n-a-ts="1788848114" '
    'data-n-a-sg="Ae5Wzi--zDRSE9nqK7VaSDNJKvNn"></div>'
)


def _batchexecute_body(real_url: str) -> str:
    """실측한 실제 응답 모양(안티하이재킹 접두사 + JSON-in-JSON 이스케이프)을 그대로 재현."""
    inner = json.dumps(["garturlres", real_url, 1])
    outer = [["wrb.fr", "Fbv4je", inner, None, None, None, ""]]
    return ")]}'\n\n" + json.dumps(outer)


class _FakeResp:
    def __init__(self, text: str, status: int = 200):
        self.text = text
        self.status_code = status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


def test_decode_success_returns_real_url(monkeypatch):
    real_url = "https://www.intn.co.kr/news/articleView.html?idxno=2035283"
    monkeypatch.setattr(gd.requests, "get", lambda url, **kw: _FakeResp(_HTML_WITH_TOKENS))
    monkeypatch.setattr(gd.requests, "post", lambda url, **kw: _FakeResp(_batchexecute_body(real_url)))

    assert gd.decode_google_news_url(_GOOGLE_URL) == real_url


def test_decode_returns_none_for_non_google_url():
    assert gd.decode_google_news_url("https://moef.go.kr/a") is None


def test_decode_returns_none_when_tokens_missing(monkeypatch):
    """구글이 페이지 구조를 바꿔 data-n-a-* 속성이 사라진 경우(차단 페이지 포함)."""
    monkeypatch.setattr(gd.requests, "get", lambda url, **kw: _FakeResp("<html>sorry</html>"))
    called = {"post": False}

    def fake_post(url, **kw):
        called["post"] = True
        return _FakeResp("")

    monkeypatch.setattr(gd.requests, "post", fake_post)

    assert gd.decode_google_news_url(_GOOGLE_URL) is None
    assert called["post"] is False  # 토큰이 없으면 POST 자체를 시도하지 않는다


def test_decode_returns_none_when_batchexecute_response_unparseable(monkeypatch):
    monkeypatch.setattr(gd.requests, "get", lambda url, **kw: _FakeResp(_HTML_WITH_TOKENS))
    monkeypatch.setattr(gd.requests, "post", lambda url, **kw: _FakeResp("not json at all"))

    assert gd.decode_google_news_url(_GOOGLE_URL) is None


def test_decode_returns_none_on_get_exception(monkeypatch):
    def boom(url, **kw):
        raise RuntimeError("connection refused")

    monkeypatch.setattr(gd.requests, "get", boom)
    assert gd.decode_google_news_url(_GOOGLE_URL) is None


def test_decode_returns_none_on_http_error_status(monkeypatch):
    monkeypatch.setattr(gd.requests, "get", lambda url, **kw: _FakeResp("blocked", status=429))
    assert gd.decode_google_news_url(_GOOGLE_URL) is None


def test_decode_returns_none_when_garturlres_missing(monkeypatch):
    """batchexecute가 다른 종류의 응답(예: 에러 wrb.fr)을 줄 때."""
    monkeypatch.setattr(gd.requests, "get", lambda url, **kw: _FakeResp(_HTML_WITH_TOKENS))
    inner = json.dumps(["someothertype", None])
    outer = [["wrb.fr", "Fbv4je", inner, None, None, None, ""]]
    body = ")]}'\n\n" + json.dumps(outer)
    monkeypatch.setattr(gd.requests, "post", lambda url, **kw: _FakeResp(body))

    assert gd.decode_google_news_url(_GOOGLE_URL) is None
