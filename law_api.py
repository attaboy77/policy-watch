"""구글 뉴스 RSS — 카테고리별 키워드로 언론 기사 수집.

구글 뉴스 RSS는 인증 불필요, 해외 IP에서도 열림. Worker 없이 직접 접속.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape
from urllib.parse import quote

import requests

from . import _common

# 카테고리별 검색 키워드 (구글 뉴스 검색 쿼리)
QUERIES = {
    "세법": '세법개정 OR 법인세 OR 소득세 OR 부가가치세',
    "K-IFRS": 'K-IFRS OR 회계기준 OR 외부감사',
    "내부회계": '내부회계관리제도',
    "ESG": 'ESG공시 OR 지속가능성공시',
}

BASE = "https://news.google.com/rss/search?q={q}&hl=ko&gl=KR&ceid=KR:ko"


def _clean(t: str) -> str:
    return unescape(re.sub(r"\s+", " ", t or "")).strip()


def _parse_date(pub: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
        try:
            return datetime.strptime(pub.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return datetime.today().strftime("%Y-%m-%d")


def _extract_source(title: str):
    # 구글 뉴스 제목은 "기사제목 - 언론사" 형태
    if " - " in title:
        parts = title.rsplit(" - ", 1)
        return parts[0].strip(), parts[1].strip()
    return title, "구글뉴스"


def fetch(session: requests.Session) -> list[dict]:
    items = []
    for category, query in QUERIES.items():
        url = BASE.format(q=quote(query))
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
        except Exception as e:
            print(f"  [google/{category}] 실패: {str(e)[:50]}")
            continue

        cnt = 0
        for node in root.iter("item"):
            raw_title = _clean(node.findtext("title"))
            link = _clean(node.findtext("link"))
            pub = node.findtext("pubDate") or ""
            if not raw_title or not link:
                continue

            title, press = _extract_source(raw_title)
            if _common.is_ad(title, press):
                continue

            items.append({
                "source": press,
                "source_type": "구글뉴스",
                "category": category,
                "title": title,
                "url": link,
                "date": _parse_date(pub),
                "official": _common.official_links(category),
            })
            cnt += 1
            if cnt >= 8:  # 카테고리당 최대 8건
                break
        print(f"  [google/{category}] {cnt}건")
    return items
