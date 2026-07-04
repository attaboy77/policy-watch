"""공용 HTTP 유틸 — 한국 공공기관 사이트가 해외 IP(GitHub Actions)를 차단하는
경우가 많아, 직접 접속을 먼저 시도하고 실패하면 공개 프록시를 순차 경유한다.

각 소스 모듈은 fetch_url()만 호출하면 된다.
"""
from urllib.parse import quote

import requests

# 앞에서부터 시도. {raw}=원본 URL, {enc}=URL 인코딩된 URL
PROXIES = [
    "https://r.jina.ai/{raw}",
    "https://api.allorigins.win/raw?url={enc}",
    "https://api.codetabs.com/v1/proxy/?quest={raw}",
    "https://corsproxy.io/?url={enc}",
]


def fetch_url(session: requests.Session, url: str, *, timeout: int = 40,
              tag: str = "") -> bytes | None:
    """직접 접속 → 실패 시 프록시 순차 시도. 성공하면 bytes, 전부 실패하면 None."""
    label = f"[{tag}] " if tag else ""

    # 1) 직접 접속 시도 (국내에서 실행하거나 차단이 없으면 가장 빠름)
    try:
        resp = session.get(url, timeout=timeout)
        resp.raise_for_status()
        if resp.content:
            return resp.content
    except Exception as e:
        print(f"  {label}직접 접속 실패: {str(e)[:70]} → 프록시 시도")

    # 2) 프록시 경유
    for tpl in PROXIES:
        proxy_url = tpl.format(raw=url, enc=quote(url, safe=""))
        host = tpl.split("/")[2]
        try:
            resp = session.get(proxy_url, timeout=timeout)
            resp.raise_for_status()
            if resp.content and len(resp.content) > 200:
                print(f"  {label}프록시 성공: {host}")
                return resp.content
        except Exception as e:
            print(f"  {label}프록시 실패({host}): {str(e)[:60]}")

    print(f"  {label}모든 경로 실패")
    return None
