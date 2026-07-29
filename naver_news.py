"""네이버 뉴스 검색 API — 카테고리별 키워드로 언론 기사 수집.

네이버 개발자센터 Client ID/Secret 필요 (GitHub Secrets):
  NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
키가 없으면 조용히 건너뛴다. 하루 25,000회 무료.
"""
import os
import re
from datetime import datetime
from html import unescape

import requests

from . import _common

API = "https://openapi.naver.com/v1/search/news.json"

QUERIES = {
    "세법": "세법개정",
    "K-IFRS": "회계기준 K-IFRS",
    "내부회계": "내부회계관리제도",
    "ESG": "ESG 공시",
}


def _strip_tags(t: str) -> str:
    t = re.sub(r"<[^>]+>", "", t or "")       # <b> 등 제거
    return unescape(re.sub(r"\s+", " ", t)).strip()


def _parse_date(pub: str) -> str:
    try:
        return datetime.strptime(pub.strip(), "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
    except ValueError:
        return datetime.today().strftime("%Y-%m-%d")


def _press_from_url(url: str) -> str:
    # 네이버 뉴스는 원문 링크 도메인으로 언론사 추정이 어려워 일반 표기
    if "naver.com" in url:
        return "네이버뉴스"
    m = re.search(r"https?://(?:www\.)?([^./]+)", url)
    return m.group(1) if m else "네이버뉴스"


def fetch(session: requests.Session) -> list[dict]:
    cid = os.environ.get("NAVER_CLIENT_ID")
    csec = os.environ.get("NAVER_CLIENT_SECRET")
    if not cid or not csec:
        print("  [naver] API 키 없음 — 건너뜀")
        return []

    headers = {"X-Naver-Client-Id": cid, "X-Naver-Client-Secret": csec}
    items = []
    for category, query in QUERIES.items():
        try:
            resp = session.get(API, headers=headers, params={
                "query": query, "display": 10, "sort": "date",
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
            press = _press_from_url(link)
            if _common.is_ad(title, press):
                continue
            items.append({
                "source": press,
                "source_type": "네이버뉴스",
                "category": category,
                "title": title,
                "url": link,
                "date": _parse_date(art.get("pubDate", "")),
                "official": _common.official_links(category),
            })
            cnt += 1
            if cnt >= 6:
                break
        print(f"  [naver/{category}] {cnt}건")
    return items
