"""대한민국 정책브리핑(korea.kr) RSS — 프록시 경유 보조 수집.

korea.kr이 해외 IP(GitHub Actions)를 차단하므로, 공개 리더 프록시를 경유한다.
여러 프록시를 순서대로 시도하고, 모두 실패하면 조용히 건너뛴다(주력은 법제처 API).
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape
from urllib.parse import quote

import requests

RSS_TARGET = "https://www.korea.kr/rss/pressrelease.xml"

# 공개 프록시들 (앞에서부터 시도). {url}에 대상 주소가 채워진다.
PROXIES = [
    "https://api.allorigins.win/raw?url={url}",
    "https://corsproxy.io/?url={url}",
    "https://thingproxy.freeboard.io/fetch/{url}",
]

CATEGORY_RULES = [
    ("회계기준", ["회계기준", "K-IFRS", "IFRS", "회계처리", "외부감사", "감사기준",
              "재무제표", "회계감독", "지속가능성 공시", "ESG 공시"]),
    ("세법", ["세법", "법인세", "소득세", "부가가치세", "종합부동산세", "종부세",
            "상속세", "증여세", "조세", "관세", "세제", "세액", "과세", "비과세",
            "납세", "세율", "세금", "세무", "연말정산", "원천징수"]),
    ("법령", ["시행령", "시행규칙", "일부개정", "전부개정", "제정령", "입법예고",
            "법률안", "주요 시행법령", "공포"]),
]
EXCLUDE_HINTS = ["채용", "인사발령", "정례브리핑", "일일 정례"]


def _classify(title: str):
    for cat, keywords in CATEGORY_RULES:
        if any(k in title for k in keywords):
            return cat
    return None


def _clean(text: str) -> str:
    return unescape(re.sub(r"\s+", " ", text or "")).strip()


def _parse_date(pub: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
        try:
            return datetime.strptime(pub.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r"(\d{4})[-.](\d{1,2})[-.](\d{1,2})", pub)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")


def _fetch_via_proxy(session: requests.Session) -> bytes | None:
    for tpl in PROXIES:
        url = tpl.format(url=quote(RSS_TARGET, safe=""))
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            if b"<item" in resp.content or b"<rss" in resp.content:
                print(f"  [korea_kr] 프록시 성공: {tpl.split('/')[2]}")
                return resp.content
        except Exception as e:
            print(f"  [korea_kr] 프록시 실패({tpl.split('/')[2]}): {e}")
    return None


def fetch(session: requests.Session) -> list[dict]:
    content = _fetch_via_proxy(session)
    if not content:
        print("  [korea_kr] 모든 프록시 실패 — 건너뜀 (법제처 API가 주력)")
        return []

    try:
        root = ET.fromstring(content)
    except Exception as e:
        print(f"  [korea_kr] XML 파싱 실패: {e}")
        return []

    items, matched = [], 0
    for node in root.iter("item"):
        title = _clean(node.findtext("title"))
        link = _clean(node.findtext("link"))
        pub = node.findtext("pubDate") or ""
        if not title or not link or any(h in title for h in EXCLUDE_HINTS):
            continue
        category = _classify(title)
        if category is None:
            continue
        items.append({
            "source": "정책브리핑",
            "category": category,
            "title": title,
            "url": link,
            "date": _parse_date(pub),
        })
        matched += 1

    print(f"  [korea_kr] {matched}건 분류됨")
    return items
