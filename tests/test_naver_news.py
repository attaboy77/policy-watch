# -*- coding: utf-8 -*-
"""sources/naver_news.py 단위 테스트 (네트워크 모킹, 실제 요청 없음)."""
import time
from datetime import date, timedelta
from types import SimpleNamespace

import pytest

from sources import naver_news as nn


class _FakeResp:
    def __init__(self, payload: dict):
        self._payload = payload

    def json(self):
        return self._payload


def _pubdate(d: date) -> str:
    return d.strftime("%a, %d %b %Y 00:00:00 +0900")


@pytest.fixture(autouse=True)
def naver_creds(monkeypatch):
    monkeypatch.setenv("NAVER_CLIENT_ID", "test-id")
    monkeypatch.setenv("NAVER_CLIENT_SECRET", "test-secret")


def test_auth_headers_raises_when_env_missing(monkeypatch):
    monkeypatch.delenv("NAVER_CLIENT_ID", raising=False)
    monkeypatch.delenv("NAVER_CLIENT_SECRET", raising=False)
    with pytest.raises(nn.NaverCredentialsMissing):
        nn._auth_headers()


def test_auth_headers_returns_expected_shape():
    headers = nn._auth_headers()
    assert headers == {"X-Naver-Client-Id": "test-id", "X-Naver-Client-Secret": "test-secret"}


def test_strip_html_removes_tags_and_entities():
    raw = "<b>법인세법</b> &quot;시행령&quot; 개정 &amp; 공표"
    assert nn._strip_html(raw) == '법인세법 "시행령" 개정 & 공표'


def test_parse_pubdate_valid_rfc822():
    assert nn._parse_pubdate("Wed, 05 Aug 2026 09:00:00 +0900") == date(2026, 8, 5)


def test_parse_pubdate_invalid_returns_none():
    assert nn._parse_pubdate("not-a-date") is None
    assert nn._parse_pubdate("") is None


def test_fetch_category_filters_noise_and_off_topic_and_stale(monkeypatch):
    today = date.today()
    payload = {
        "items": [
            {  # on-topic, tier1(official) → 노이즈 필터 면제(제목엔 노이즈 단어 없음, 통과)
                "title": "<b>법인세법</b> 시행령 개정안 입법예고",
                "originallink": "https://moef.go.kr/press/1",
                "link": "https://n.news.naver.com/x/1",
                "pubDate": _pubdate(today),
            },
            {  # 노이즈 키워드 포함 + tier5 → 제거 대상
                "title": "이 종목 테마주 급등, 국세청 세법 검토",
                "originallink": "https://random-blog.example.com/2",
                "link": "https://random-blog.example.com/2",
                "pubDate": _pubdate(today),
            },
            {  # 카테고리 무관(필수 키워드 없음) → 제거
                "title": "오늘의 날씨는 맑음입니다",
                "originallink": "https://random-blog.example.com/3",
                "link": "https://random-blog.example.com/3",
                "pubDate": _pubdate(today),
            },
            {  # 수집 기간(90일) 밖 → 제거
                "title": "국세청 세법 개정안 오래된 기사",
                "originallink": "https://random-blog.example.com/4",
                "link": "https://random-blog.example.com/4",
                "pubDate": _pubdate(today - timedelta(days=200)),
            },
        ]
    }
    monkeypatch.setattr(nn, "_http", SimpleNamespace(get=lambda url, **kw: _FakeResp(payload)))
    monkeypatch.setattr(time, "sleep", lambda s: None)

    kept = nn.fetch_category("tax")
    assert len(kept) == 1
    assert kept[0]["url"] == "https://moef.go.kr/press/1"
    assert kept[0]["trust_tier"] == 1


def test_fetch_category_dedupes_across_queries_by_url(monkeypatch):
    payload = {
        "items": [
            {
                "title": "법인세법 시행령 개정안",
                "originallink": "https://moef.go.kr/press/dup",
                "pubDate": _pubdate(date.today()),
            },
        ]
    }
    monkeypatch.setattr(nn, "_http", SimpleNamespace(get=lambda url, **kw: _FakeResp(payload)))
    monkeypatch.setattr(time, "sleep", lambda s: None)

    # tax 카테고리는 naver_queries가 여러 개라 같은 결과가 반복 수집될 수 있음 → 중복 제거 확인
    kept = nn.fetch_category("tax")
    assert len(kept) == 1


def test_fetch_category_raises_without_credentials(monkeypatch):
    monkeypatch.delenv("NAVER_CLIENT_ID", raising=False)
    monkeypatch.delenv("NAVER_CLIENT_SECRET", raising=False)
    with pytest.raises(nn.NaverCredentialsMissing):
        nn.fetch_category("tax")


def test_fetch_all_gracefully_skips_when_credentials_missing(monkeypatch):
    monkeypatch.delenv("NAVER_CLIENT_ID", raising=False)
    monkeypatch.delenv("NAVER_CLIENT_SECRET", raising=False)
    monkeypatch.setattr(time, "sleep", lambda s: None)

    results = nn.fetch_all()
    assert all(results[cat] == [] for cat in results)
