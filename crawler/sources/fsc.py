"""금융위원회(FSC) 공식 RSS — 회계·감사·공시·세제 관련 보도자료만 선별.

공식 RSS라 실제 보도자료 item만 들어온다(사이트 메뉴가 섞이지 않음).
XML이므로 원본보존 프록시(_http)를 경유한다.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape

from . import _http

FSC_RSS = "http://www.fsc.go.kr/about/fsc_bbs_rss/?fid=0111"

# 회계·감사·공시 관련 → 회계기준
ACCT_KEYWORDS = ["회계기준", "회계처리", "외부감사", "감사인", "내부회계",
                 "재무제표", "IFRS", "K-IFRS", "지속가능성 공시", "ESG 공시",
                 "회계감독", "공시서식", "사업보고서"]
# 세제 관련 → 세법
TAX_KEYWORDS = ["세제", "세법", "과세", "비과세", "세액공제", "증권거래세", "금융세제"]
# 제도·규정 개정 관련 → 법령
LAW_KEYWORDS = ["감독규정", "시행세칙", "규정변경예고", "규정 개정", "입법예고",
                "시행령 개정", "고시 개정", "감독규정 개정"]

# 회계·세법·법령과 무관하면 아예 제외 (아래 중 하나도 없으면 버림)
EXCLUDE_HINTS = ["채용", "인사", "포상", "공모", "세미나", "간담회", "행사",
                 "정부포상", "후보자", "부고", "일정", "안내"]


def _clean(t: str) -> str:
    return unescape(re.sub(r"\s+", " ", t or "")).strip()


def _classify(title: str):
    if any(k in title for k in ACCT_KEYWORDS):
        return "회계기준"
    if any(k in title for k in TAX_KEYWORDS):
        return "세법"
    if any(k in title for k in LAW_KEYWORDS):
        return "법령"
    return None


def _parse_date(pub: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
        try:
            return datetime.strptime(pub.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r"(\d{4})[-.](\d{1,2})[-.](\d{1,2})", pub)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")


def fetch(session):
    content = _http.fetch_bytes(session, FSC_RSS, tag="fsc")
    if not content:
        return []
    try:
        root = ET.fromstring(content)
    except Exception as e:
        print(f"  [fsc] XML 파싱 실패: {str(e)[:40]}")
        return []

    items, matched = [], 0
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
            "source": "금융위원회", "category": category,
            "title": title, "url": link, "date": _parse_date(pub),
        })
        matched += 1
    print(f"  [fsc] {matched}건 분류됨")
    return items
