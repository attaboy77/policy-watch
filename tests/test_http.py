# -*- coding: utf-8 -*-
"""sources/_http.py 단위 테스트 (네트워크 모킹, 실제 요청 없음).

2026-09-08: moef/nts/fsc/policy_briefing 4개 소스를 `_http.get()`에서
`_http.get_govt()`로 전환하면서(정부 사이트 IP 차단 우회용 PROXY_BASE 경유)
`get_govt()`의 라우팅 로직과 "PROXY_BASE 미설정" 경고 로그를 검증한다."""
import pytest

from sources import _http


class _FakeResp:
    def __init__(self, url):
        self.url = url
        self.status_code = 200


@pytest.fixture(autouse=True)
def _reset_proxy_warning_flag(monkeypatch):
    """`_warned_no_proxy`는 프로세스 전역 상태(로그 도배 방지용 "한 번만" 플래그)라
    테스트 간에 새어나가지 않도록 매 테스트 전에 초기화한다."""
    monkeypatch.setattr(_http, "_warned_no_proxy", False)


def test_get_govt_without_proxy_base_calls_get_directly(monkeypatch):
    monkeypatch.delenv("PROXY_BASE", raising=False)
    calls = []

    def fake_get(url, **kw):
        calls.append((url, kw.get("params")))
        return _FakeResp(url)

    monkeypatch.setattr(_http, "get", fake_get)

    resp = _http.get_govt("https://law.go.kr/DRF/lawSearch.do", params={"query": "법인세법"})

    assert resp.url == "https://law.go.kr/DRF/lawSearch.do"
    assert calls == [("https://law.go.kr/DRF/lawSearch.do", {"query": "법인세법"})]


def test_get_govt_with_proxy_base_routes_through_proxy(monkeypatch):
    monkeypatch.setenv("PROXY_BASE", "https://policy-proxy.epsillon.workers.dev")
    calls = []

    def fake_get(url, **kw):
        calls.append(url)
        return _FakeResp(url)

    monkeypatch.setattr(_http, "get", fake_get)

    _http.get_govt("https://law.go.kr/DRF/lawSearch.do", params={"query": "법인세법"})

    assert len(calls) == 1
    proxied = calls[0]
    assert proxied.startswith("https://policy-proxy.epsillon.workers.dev?url=")
    assert "law.go.kr" in proxied  # 인코딩된 원본 URL이 그대로 들어있어야 함


def test_get_govt_strips_trailing_slash_on_proxy_base(monkeypatch):
    monkeypatch.setenv("PROXY_BASE", "https://policy-proxy.epsillon.workers.dev/")
    calls = []
    monkeypatch.setattr(_http, "get", lambda url, **kw: calls.append(url) or _FakeResp(url))

    _http.get_govt("https://moef.go.kr/a")

    assert calls[0].startswith("https://policy-proxy.epsillon.workers.dev?url=")
    assert "//?url=" not in calls[0]


def test_get_govt_warns_once_when_proxy_base_missing(monkeypatch, capsys):
    monkeypatch.delenv("PROXY_BASE", raising=False)
    monkeypatch.setattr(_http, "get", lambda url, **kw: _FakeResp(url))

    _http.get_govt("https://moef.go.kr/a")
    _http.get_govt("https://nts.go.kr/b")
    _http.get_govt("https://fsc.go.kr/c")

    out = capsys.readouterr().out
    assert out.count("PROXY_BASE 미설정 - 직접 접속으로 진행") == 1  # 3번 호출해도 경고는 한 번만


def test_get_govt_does_not_warn_when_proxy_base_set(monkeypatch, capsys):
    monkeypatch.setenv("PROXY_BASE", "https://policy-proxy.epsillon.workers.dev")
    monkeypatch.setattr(_http, "get", lambda url, **kw: _FakeResp(url))

    _http.get_govt("https://moef.go.kr/a")

    out = capsys.readouterr().out
    assert "PROXY_BASE 미설정" not in out


def test_proxy_base_treats_empty_string_as_none(monkeypatch):
    monkeypatch.setenv("PROXY_BASE", "")
    assert _http.proxy_base() is None


def test_proxy_base_returns_value_when_set(monkeypatch):
    monkeypatch.setenv("PROXY_BASE", "https://policy-proxy.epsillon.workers.dev")
    assert _http.proxy_base() == "https://policy-proxy.epsillon.workers.dev"
