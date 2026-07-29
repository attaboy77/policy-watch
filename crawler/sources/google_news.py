"""구글 뉴스 RSS — 정밀 검색 쿼리로 카테고리별 실무 뉴스만 수집.

노이즈(시황·재테크) 차단 + 필수/조합 키워드 재검증 + 출처 가중치 부여.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape
from urllib.parse import quote

import requests

from . import _common, _config

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
    if " - " in title:
        parts = title.rsplit(" - ", 1)
        return parts[0].strip(), parts[1].strip()
    return title, "구글뉴스"


def fetch(session: requests.Session) -> list[dict]:
    items = []
    for category in _config.CATEGORY_KEYWORDS:
        query = _common.build_query(category)          # 정밀 쿼리 생성
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

            # 1) 노이즈·광고 차단
            if _common.should_exclude(title, press):
                continue
            # 2) 정밀 키워드 재검증 (필수 AND 조합) — 쿼리가 느슨해도 여기서 거름
            if not _common.match_category(title, category):
                continue

            press_name = _common.trust_name(link) or press
            items.append({
                "source": press_name,
                "source_type": "뉴스",
                "category": category,
                "title": title,
                "url": link,
                "date": _parse_date(pub),
                "trust": _common.trust_score(link),
                "official": _common.official_links(category),
            })
            cnt += 1
            if cnt >= 10:
                break
        print(f"  [google/{category}] {cnt}건")
    return items
