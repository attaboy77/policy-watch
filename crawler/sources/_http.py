"""공용 HTTP 유틸 — 한국 공공기관이 해외 IP(GitHub Actions)를 차단하는 경우가 많아,
직접 접속 → 실패 시 공개 프록시를 순차 경유한다.

중요: XML을 받을 때는 원본을 그대로 주는 프록시(allorigins raw, codetabs)를 우선 쓴다.
r.jina.ai는 내용을 마크다운으로 변환해버려 XML 파싱이 깨지므로 XML엔 쓰지 않는다.
"""
from urllib.parse import quote

import requests

# XML/RSS용: 원본 바이트를 그대로 반환하는 프록시만 사용
XML_PROXIES = [
    "https://api.allorigins.win/raw?url={enc}",
    "https://api.codetabs.com/v1/proxy/?quest={raw}",
    "https://corsproxy.io/?url={enc}",
]


def fetch_bytes(session: requests.Session, url: str, *, timeout: int = 40,
                tag: str = "") -> bytes | None:
    """직접 접속 → 실패 시 원본보존 프록시 순차 시도. 성공 시 bytes, 전부 실패 시 None."""
    label = f"[{tag}] " if tag else ""

    # 1) 직접 접속
    try:
        resp = session.get(url, timeout=timeout)
        resp.raise_for_status()
        if resp.content:
            return resp.content
    except Exception as e:
        print(f"  {label}직접 접속 실패: {str(e)[:60]} → 프록시 시도")

    # 2) 원본보존 프록시
    for tpl in XML_PROXIES:
        proxy_url = tpl.format(raw=url, enc=quote(url, safe=""))
        host = tpl.split("/")[2]
        try:
            resp = session.get(proxy_url, timeout=timeout)
            resp.raise_for_status()
            content = resp.content
            # RSS/XML이 실제로 들어왔는지 확인 (마크다운 변환분 걸러냄)
            if content and (b"<item" in content or b"<rss" in content
                            or b"<?xml" in content or b"<law" in content
                            or b"<LawSearch" in content):
                print(f"  {label}프록시 성공: {host}")
                return content
            print(f"  {label}프록시 응답이 XML 아님: {host}")
        except Exception as e:
            print(f"  {label}프록시 실패({host}): {str(e)[:50]}")

    print(f"  {label}모든 경로 실패")
    return None
