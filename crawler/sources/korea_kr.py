"""대한민국 정책브리핑(korea.kr) 표준 RSS 기반 수집.

여러 부처의 RSS를 한 번에 읽어 키워드로 카테고리를 자동 분류한다.
korea.kr RSS는 표준 RSS 2.0 포맷이라 구조가 안정적이다.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape

import requests

# 부처별 RSS 피드 (korea.kr 표준)
FEEDS = [
    ("기획재정부", "https://www.korea.kr/rss/dept_moef.xml"),
    ("국세청", "https://www.korea.kr/rss/dept_nts.xml"),
    ("금융위원회", "https://www.korea.kr/rss/dept_fsc.xml"),
]

# 카테고리 분류 키워드 (제목 기준, 위에서부터 우선 매칭)
# 세법 관련이면 시행령·개정이라도 '세법' 섹션에 들어가도록 세법을 법령보다 먼저 둔다.
CATEGORY_RULES = [
    ("회계기준", ["회계기준", "K-IFRS", "IFRS", "회계처리", "외부감사", "감사기준", "재무제표", "회계감독"]),
    ("세법", ["세법", "법인세", "소득세", "부가가치세", "종합부동산세", "상속세", "증여세",
             "조세", "관세", "세제", "세액", "과세", "비과세", "납세", "세율", "세금", "세무"]),
    ("법령", ["시행령", "시행규칙", "일부개정", "전부개정", "제정령", "입법예고", "고시", "법률안", "법 개정"]),
]

# 이 중 하나라도 제목에 없으면 수집하지 않음 (회계·세무 관련만 필터)
INCLUDE_ANY = (
    [kw for _, kws in CATEGORY_RULES for kw in kws]
)


def _classify(title: str) -> str | None:
    for cat, keywords in CATEGORY_RULES:
        if any(k in title for k in keywords):
            return cat
    return None


def _clean(text: str) -> str:
    return unescape(re.sub(r"\s+", " ", text or "")).strip()


def _parse_date(pub: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
        try:
            return datetime.strptime(pub, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", pub)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else datetime.today().strftime("%Y-%m-%d")


def fetch(session: requests.Session) -> list[dict]:
    items = []
    for source_name, url in FEEDS:
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
        except Exception as e:
            print(f"  [{source_name}] RSS 읽기 실패: {e}")
            continue

        for node in root.iter("item"):
            title = _clean(node.findtext("title"))
            link = _clean(node.findtext("link"))
            pub = node.findtext("pubDate") or ""
            if not title or not link:
                continue

            category = _classify(title)
            if category is None:  # 회계·세무·법령과 무관한 일반 보도자료는 제외
                continue

            items.append({
                "source": source_name,
                "category": category,
                "title": title,
                "url": link,
                "date": _parse_date(pub),
            })
    return items
