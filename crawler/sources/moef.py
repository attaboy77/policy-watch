"""기획재정부 보도자료 RSS 수집 (세법개정안 등)."""
import re
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

RSS_URL = "https://www.moef.go.kr/com/detailRssTagService.do?bbsId=MOSFBBS_000000000028"
KEYWORDS = ["세법", "개정", "법인세", "소득세", "부가가치세", "조세", "시행령", "시행규칙"]


def fetch(session: requests.Session) -> list[dict]:
    items = []
    resp = session.get(RSS_URL, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)

    for node in root.iter("item"):
        title = (node.findtext("title") or "").strip()
        link = (node.findtext("link") or "").strip()
        pub = (node.findtext("pubDate") or "").strip()

        # 세법 관련 키워드가 포함된 건만 수집 (전체 수집을 원하면 이 필터 제거)
        if not any(k in title for k in KEYWORDS):
            continue

        items.append({
            "source": "기획재정부",
            "category": "세법",
            "title": title,
            "url": link,
            "date": _parse_date(pub),
        })
    return items


def _parse_date(pub: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(pub, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", pub)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")
