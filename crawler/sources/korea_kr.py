"""대한민국 정책브리핑(korea.kr) RSS 기반 수집.

통합 보도자료 RSS + 법제처 RSS를 읽어 키워드로 카테고리를 자동 분류한다.
개별 부처 RSS가 해외 IP(GitHub Actions)에서 간헐적으로 차단될 수 있어,
전체 보도자료가 흐르는 통합 피드(pressrelease.xml)를 기본으로 사용한다.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape

import requests

# 통합 보도자료 피드(가장 안정적) + 법제처(시행법령) 피드
FEEDS = [
    ("정책브리핑", "https://www.korea.kr/rss/pressrelease.xml"),
    ("법제처", "https://www.korea.kr/rss/dept_moleg.xml"),
]

# 카테고리 분류 키워드 (제목 기준, 위에서부터 우선 매칭)
# 세법 관련이면 시행령이라도 '세법' 섹션에 들어가도록 세법을 법령보다 먼저 둔다.
CATEGORY_RULES = [
    ("회계기준", ["회계기준", "K-IFRS", "IFRS", "회계처리", "외부감사", "감사기준",
              "재무제표", "회계감독", "지속가능성 공시", "ESG 공시"]),
    ("세법", ["세법", "법인세", "소득세", "부가가치세", "종합부동산세", "종부세",
            "상속세", "증여세", "조세", "관세", "세제", "세액", "과세", "비과세",
            "납세", "세율", "세금", "세무", "연말정산", "원천징수"]),
    ("법령", ["시행령", "시행규칙", "일부개정", "전부개정", "제정령", "입법예고",
            "법률안", "주요 시행법령", "공포"]),
]

# 회계·세무·법령과 무관한 일반 보도자료는 이 접두어 등으로도 한 번 더 거른다.
EXCLUDE_HINTS = ["채용", "인사발령", "정례브리핑", "일일 정례"]


def _classify(title: str) -> str | None:
    for cat, keywords in CATEGORY_RULES:
        if any(k in title for k in keywords):
            return cat
    return None


def _clean(text: str) -> str:
    return unescape(re.sub(r"\s+", " ", text or "")).strip()


def _parse_date(pub: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S"):
        try:
            return datetime.strptime(pub.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r"(\d{4})[-.](\d{1,2})[-.](\d{1,2})", pub)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")


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

        matched = 0
        for node in root.iter("item"):
            title = _clean(node.findtext("title"))
            link = _clean(node.findtext("link"))
            pub = node.findtext("pubDate") or ""
            if not title or not link:
                continue
            if any(h in title for h in EXCLUDE_HINTS):
                continue

            category = _classify(title)
            if category is None:
                continue

            items.append({
                "source": source_name,
                "category": category,
                "title": title,
                "url": link,
                "date": _parse_date(pub),
            })
            matched += 1
        print(f"  [{source_name}] {matched}건 분류됨")
    return items
