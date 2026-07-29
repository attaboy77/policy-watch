"""공용 HTTP 유틸 — Cloudflare Worker 프록시를 경유해 한국 사이트 차단을 우회한다.

Worker 주소는 환경변수 PROXY_BASE로 주입한다(없으면 공개 프록시로 폴백).
GitHub Secrets에 PROXY_BASE = https://policy-proxy.epsillon.workers.dev 형태로 등록.
"""
import os
from urllib.parse import quote

import requests

# 우리 전용 Cloudflare Worker (한국 사이트 접속용)
PROXY_BASE = os.environ.get("PROXY_BASE", "").rstrip("/")

# Worker가 없을 때를 대비한 공개 프록시 폴백 (원본 XML 보존형)
FALLBACK_PROXIES = [
    "https://api.allorigins.win/raw?url={enc}",
    "https://api.codetabs.com/v1/proxy/?quest={raw}",
]

_XML_MARKERS = (b"<item", b"<rss", b"<?xml", b"<law", b"<LawSearch", b"<channel")


def _looks_ok(content: bytes, require_xml: bool) -> bool:
    if not content or len(content) < 100:
        return False
    if not require_xml:
        return True
    return any(m in content for m in _XML_MARKERS)


def fetch_bytes(session: requests.Session, url: str, *, timeout: int = 40,
                tag: str = "", require_xml: bool = True) -> bytes | None:
    """Worker 프록시 우선 → 실패 시 공개 프록시. 성공 시 bytes, 전부 실패 시 None."""
    label = f"[{tag}] " if tag else ""

    # 1) 우리 Worker 프록시 (가장 안정적)
    if PROXY_BASE:
        proxy_url = f"{PROXY_BASE}/?url={quote(url, safe='')}"
        try:
            resp = session.get(proxy_url, timeout=timeout)
            resp.raise_for_status()
            if _looks_ok(resp.content, require_xml):
                print(f"  {label}Worker 프록시 성공")
                return resp.content
            print(f"  {label}Worker 응답 형식 확인 필요 (그대로 사용)")
            return resp.content  # XML 마커 없어도 일단 반환 (JSON 등)
        except Exception as e:
            print(f"  {label}Worker 프록시 실패: {str(e)[:60]} → 폴백")

    # 2) 공개 프록시 폴백
    for tpl in FALLBACK_PROXIES:
        purl = tpl.format(raw=url, enc=quote(url, safe=""))
        host = tpl.split("/")[2]
        try:
            resp = session.get(purl, timeout=timeout)
            resp.raise_for_status()
            if _looks_ok(resp.content, require_xml):
                print(f"  {label}폴백 프록시 성공: {host}")
                return resp.content
        except Exception as e:
            print(f"  {label}폴백 실패({host}): {str(e)[:40]}")

    print(f"  {label}모든 경로 실패")
    return None
