# -*- coding: utf-8 -*-
"""공용 HTTP 요청 헬퍼: User-Agent / 타임아웃 / 지수 백오프 재시도 공통 처리.

SPEC.md §9-4: 각 수집기는 독립적으로 try/except, 타임아웃 15초, 재시도 3회(지수 백오프).
SPEC.md §9-7: 크롤링 시 User-Agent 명시, 요청 간 0.5초 sleep, robots.txt 존중.
SPEC.md §9-3 / §4-5: GitHub Actions(미국 IP)에서 한국 정부 사이트가 차단될 수 있다.
`PROXY_BASE`(Cloudflare Workers) 시크릿이 있으면 그 경유로 요청한다.
"""
import os
import time
from urllib.parse import quote_plus

import requests

USER_AGENT = "PolicyWatchBot/1.0 (+https://github.com/; contact: alchem1024@gmail.com)"
DEFAULT_TIMEOUT = 15
DEFAULT_RETRIES = 3
DEFAULT_HEADERS = {"User-Agent": USER_AGENT}


def get(url: str, *, params: dict | None = None, headers: dict | None = None,
        timeout: int = DEFAULT_TIMEOUT, retries: int = DEFAULT_RETRIES) -> requests.Response:
    """GET 요청. 실패 시 0.5s, 1s, 2s ... 지수 백오프로 재시도한다.

    모든 재시도가 실패하면 마지막 예외를 그대로 올린다 — 호출부(각 수집기)가
    소스 단위로 try/except 하여 나머지 소스 수집을 막지 않도록 한다.
    """
    hdrs = {**DEFAULT_HEADERS, **(headers or {})}
    last_exc: Exception | None = None
    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, headers=hdrs, timeout=timeout)
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < retries - 1:
                time.sleep(0.5 * (2 ** attempt))
    assert last_exc is not None
    raise last_exc


def proxy_base() -> str | None:
    """`PROXY_BASE` 시크릿/환경변수. 없으면 None(직접 호출)."""
    return os.environ.get("PROXY_BASE") or None


def get_govt(url: str, *, params: dict | None = None, headers: dict | None = None,
             timeout: int = DEFAULT_TIMEOUT, retries: int = DEFAULT_RETRIES) -> requests.Response:
    """정부 사이트(law.go.kr 등) 전용 GET. `PROXY_BASE`가 설정돼 있으면 그 경유로,
    없으면 직접 호출한다.

    프록시 규약(Cloudflare Workers 관례): `{PROXY_BASE}?url={인코딩된 원본 URL(쿼리스트링 포함)}`.
    실제 배포된 Worker가 이 규약과 다르면 이 함수만 고치면 된다(호출부는 그대로).
    로컬(한국 IP) 개발 환경에서는 `PROXY_BASE`를 안 쓰는 게 정상이며, 이 경로는
    GitHub Actions(미국 IP)에서만 검증 가능하다 — 로컬 성공이 Actions 성공을
    보장하지 않는다(SPEC.md §9-3).
    """
    base = proxy_base()
    if base is None:
        return get(url, params=params, headers=headers, timeout=timeout, retries=retries)
    # 프록시 경유 시 쿼리스트링을 원본 URL에 먼저 합쳐 넣는다(프록시는 target url 하나만 받음).
    target = url
    if params:
        req = requests.Request("GET", url, params=params).prepare()
        target = req.url
    proxied_url = f"{base.rstrip('/')}?url={quote_plus(target)}"
    return get(proxied_url, headers=headers, timeout=timeout, retries=retries)
