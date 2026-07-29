"""네이버 뉴스 검색 API — 정밀 쿼리로 카테고리별 실무 뉴스만 수집.

노이즈 차단 + 필수/조합 키워드 재검증 + 출처 가중치. 키 없으면 건너뜀.
네이버는 괄호 AND/OR 미지원이라 단순 쿼리를 쓰고, 받은 뒤 정밀 필터로 거른다.
"""
import os
import re
from datetime import datetime
from html import unescape

import requests

from . import _common, _config

API = "https://openapi.naver.com/v1/search/news.json"


def _strip_tags(t: str) -> str:
    t = re.sub(r"<[^>]+>", "", t or "")
    return unescape(re.sub(r"\s+", " ", t)).strip()


def _parse_date(pub: str) -> str:
    try:
        return datetime.strptime(pub.strip(), "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
    except ValueError:
        return datetime.today().strftime("%Y-%m-%d")


def fetch(session: requests.Session) -> list[dict]:
    cid = os.environ.get("NAVER_CLIENT_ID")
    csec = os.environ.get("NAVER_CLIENT_SECRET")
    if not cid or not csec:
        print("  [naver] API 키 없음 — 건너뜀")
        return []

    headers = {"X-Naver-Client-Id": cid, "X-Naver-Client-Secret": csec}
    items = []
    for category in _config.CATEGORY_KEYWORDS:
        query = _common.build_naver_query(category)   # 네이버용 단순 쿼리
        try:
            resp = session.get(API, headers=headers, params={
                "query": query, "display": 20, "sort": "date",
            }, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(f"  [naver/{category}] 실패: {str(e)[:50]}")
            continue

        cnt = 0
        for art in data.get("items", []):
            title = _strip_tags(art.get("title", ""))
            link = art.get("originallink") or art.get("link", "")
            if not title or not link:
                continue
            if _common.should_exclude(title):
                continue
            if not _common.match_category(title, category):
                continue

            press = _common.trust_name(link) or "네이버뉴스"
            items.append({
                "source": press,
                "source_type": "뉴스",
                "category": category,
                "title": title,
                "url": link,
                "date": _parse_date(art.get("pubDate", "")),
                "trust": _common.trust_score(link),
                "official": _common.official_links(category),
            })
            cnt += 1
            if cnt >= 8:
                break
        print(f"  [naver/{category}] {cnt}건")
    return items
