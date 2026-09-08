# -*- coding: utf-8 -*-
"""구글 뉴스 RSS 링크(news.google.com/rss/articles/...)를 실제 언론사 원문
URL로 디코딩한다 (2026-09-08, 사용자 실측 보고 대응).

## 배경
구글 뉴스 RSS의 `<link>`는 news.google.com 리다이렉트 URL이고, 실제 원문
페이지로의 이동은 브라우저에서 JS(구글 내부 `batchexecute` API 호출)로
처리된다. 이 링크를 그대로 메일/대시보드에 노출하면 자동화 요청으로 판단돼
"We're sorry... automated queries" 차단 페이지가 뜨는 경우가 있다.

## 조사 결과 (실측)
- RSS의 `<description>`/`<source url="...">`엔 원문 URL이 없다(각각 같은
  구글 리다이렉트 링크 재노출, 매체 홈페이지 도메인만).
- 단순 302 리다이렉트를 따라가도 news.google.com 자기 자신으로 돌아온다
  (`?hl=..&gl=..&ceid=..`만 붙음) — 실제 이동은 JS가 처리.
- `CBMi...` 부분은 base64가 맞지만 디코딩해도 원문 URL이 평문으로 나오지
  않는다(예전 포맷은 그랬으나 구글이 opaque 토큰 방식으로 바꿨다).
- 대신 그 리다이렉트 URL을 한 번 GET하면 응답 HTML 안에
  `data-n-a-id`/`data-n-a-sg`/`data-n-a-ts` 3개 값이 있고, 이 값들로
  구글 내부 `batchexecute` 엔드포인트에 POST하면 원문 URL을 돌려준다
  (`googlenewsdecoder` 등 서드파티 라이브러리가 쓰는 것과 같은 방식).
  로컬 IP에서 6/6 성공, 도메인·제목 전부 실제 매체와 일치 확인.

## 신뢰성 경고
구글 공식 API가 아닌 **비공식 내부 엔드포인트**라 예고 없이 바뀔 수 있다
(실제로 base64 직접 디코딩 방식에서 지금 방식으로 이미 한 번 바뀐 이력이
있다). 그래서 이 모듈은 어떤 이유로든 실패하면 예외를 삼키고 None만
반환한다 — 호출부(`google_news.py`)는 반드시 원래 구글 링크로 폴백해야
하고, 항목 자체를 버리면 안 된다.
"""
from __future__ import annotations

import json
import re

import requests

# 구글 뉴스는 봇으로 보이는 요청을 더 쉽게 차단한다 — sources/_http.py의
# 기본 UA("PolicyWatchBot/1.0...")는 일부러 안 쓰고, 실측에 성공한 일반
# 브라우저 UA를 그대로 쓴다.
_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
_TIMEOUT = 15
_BATCHEXECUTE_URL = "https://news.google.com/_/DotsSplashUi/data/batchexecute"

_ID_RE = re.compile(r'data-n-a-id="([^"]+)"')
_SG_RE = re.compile(r'data-n-a-sg="([^"]+)"')
_TS_RE = re.compile(r'data-n-a-ts="([^"]+)"')


def decode_google_news_url(google_url: str) -> str | None:
    """news.google.com/rss/articles/... 링크 → 실제 원문 URL.

    요청 2회(HTML GET + batchexecute POST) 필요. 실패하면(파싱 실패/네트워크
    오류/구글이 응답 형식을 바꿈 등) 절대 예외를 올리지 않고 None을 반환한다.
    """
    if "news.google.com" not in google_url:
        return None
    try:
        resp = requests.get(google_url, headers={"user-agent": _UA}, timeout=_TIMEOUT)
        resp.raise_for_status()
        html = resp.text
        m_id, m_sg, m_ts = _ID_RE.search(html), _SG_RE.search(html), _TS_RE.search(html)
        if not (m_id and m_sg and m_ts):
            return None
        article_id, sg, ts = m_id.group(1), m_sg.group(1), m_ts.group(1)

        inner = (
            '["garturlreq",[["en-US","US",["FINANCE_TOP_INDICES","WEB_TEST_1_0_0"],'
            'null,null,1,1,"US:en",null,180,null,null,null,null,null,0,null,null,'
            '[1608992183,723341000]],"en-US","US",1,[2,3,4,8],1,1,null,0,0,null,0],'
            '"{}",{},"{}"]'
        ).format(article_id, ts, sg)
        payload = ["Fbv4je", inner]

        resp2 = requests.post(
            _BATCHEXECUTE_URL,
            headers={
                "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "user-agent": _UA,
                "referer": "https://news.google.com/",
            },
            data={"f.req": json.dumps([[payload]])},
            timeout=_TIMEOUT,
        )
        resp2.raise_for_status()
        body = resp2.text
        if body.startswith(")]}'"):
            body = body.split("\n", 2)[-1]
        outer = json.loads(body)
        inner_result = json.loads(outer[0][2])
        if len(inner_result) < 2 or inner_result[0] != "garturlres":
            return None
        real_url = inner_result[1]
        return real_url if isinstance(real_url, str) and real_url.startswith("http") else None
    except Exception:  # noqa: BLE001 - 실패는 전부 폴백 대상, 크롤링을 절대 막지 않는다
        return None
