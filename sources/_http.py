# -*- coding: utf-8 -*-
"""공용 HTTP 요청 헬퍼: User-Agent / 타임아웃 / 지수 백오프 재시도 공통 처리.

SPEC.md §9-4: 각 수집기는 독립적으로 try/except, 타임아웃 15초, 재시도 3회(지수 백오프).
SPEC.md §9-7: 크롤링 시 User-Agent 명시, 요청 간 0.5초 sleep, robots.txt 존중.
"""
import time

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
