"""금융위원회(FSC) 공식 RSS + 금융감독원(FSS) 보도자료 게시판.

금융위는 공식 RSS를 제공하고, 금감원은 게시판을 파싱한다.
회계·감사·공시 관련 키워드만 '회계기준', 나머지 제도·법령성은 '법령'으로 분류한다.
"""
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape

from bs4 import BeautifulSoup

from . import _http

# 금융위 공식 RSS (보도자료)
FSC_RSS = "http://www.fsc.go.kr/about/fsc_bbs_rss/?fid=0111"
# 금감원 보도자료 게시판
FSS_LIST = "https://www.fss.or.kr/fss/bbs/B0000188/list.do?menuNo=200218"

# 회계·감사·공시 관련 → 회계기준 / 그 외 제도·규정성 → 법령
ACCT_KEYWORDS = ["회계", "감사", "외부감사", "공시", "재무제표", "IFRS", "회계기준",
                 "내부회계", "지속가능성", "ESG"]
LAW_KEYWORDS = ["개정", "제정", "규정", "고시", "입법예고", "규정변경예고",
                "시행", "감독규정", "제도"]

# 회계·법령과 무관한 일반 보도자료는 제외
INCLUDE_ANY = ACCT_KEYWORDS + LAW_KEYWORDS + ["자본시장", "상장", "감독", "공인회계사"]
EXCLUDE_HINTS = ["채용", "인사", "포상", "공모", "세미나", "간담회 참가",
                 "행사 개최", "정부포상", "후보자", "일정", "부고"]


def _clean(t: str) -> str:
    return unescape(re.sub(r"\s+", " ", t or "")).strip()


def _classify(title: str):
    if any(k in title for k in ACCT_KEYWORDS):
        return "회계기준"
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


def _fetch_fsc(session):
    content = _http.fetch_url(session, FSC_RSS, tag="fsc")
    if not content:
        return []
    try:
        root = ET.fromstring(content)
    except Exception as e:
        print(f"  [fsc] XML 파싱 실패: {e}")
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
            "source": "금융위원회", "category": category,
            "title": title, "url": link, "date": _parse_date(pub),
        })
        matched += 1
    print(f"  [fsc] {matched}건 분류됨")
    return items


def _fetch_fss(session):
    content = _http.fetch_url(session, FSS_LIST, tag="fss")
    if not content:
        return []
    soup = BeautifulSoup(content, "html.parser")

    items, matched = [], 0
    for a in soup.select("a"):
        title = a.get_text(strip=True)
        if not title or len(title) < 6:
            continue
        if any(h in title for h in EXCLUDE_HINTS):
            continue
        category = _classify(title)
        if category is None:
            continue
        href = a.get("href", "")
        if href.startswith("/"):
            url = "https://www.fss.or.kr" + href
        elif href.startswith("http"):
            url = href
        else:
            url = FSS_LIST
        items.append({
            "source": "금융감독원", "category": category,
            "title": title, "url": url,
            "date": datetime.today().strftime("%Y-%m-%d"),
        })
        matched += 1
        if matched >= 20:
            break
    print(f"  [fss] {matched}건 분류됨")
    return items


def fetch(session):
    return _fetch_fsc(session) + _fetch_fss(session)
