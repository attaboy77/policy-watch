"""한국회계기준원(KASB/KAI) 게시판 크롤링.

보도자료·기준서 제개정 공고 게시판을 파싱한다. korea.kr과 달리 게시판 HTML이라
구조 변경 시 셀렉터 조정이 필요할 수 있다. 해외 IP 차단 대비로 프록시를 경유한다.
"""
import re
from datetime import datetime

from bs4 import BeautifulSoup

from . import _http

BASE = "https://www.kasb.or.kr"

# (게시판 이름, bbsCd) — 회계기준원 게시판 코드
BOARDS = [
    ("보도자료", "1005"),
    ("기준서 제·개정", "1023"),
]


def _parse_date(text: str) -> str:
    m = re.search(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", text)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")


def fetch(session):
    items = []
    for board_name, bbs_cd in BOARDS:
        list_url = f"{BASE}/fe/bbs/NR_list.do?bbsCd={bbs_cd}"
        content = _http.fetch_url(session, list_url, tag=f"kasb/{board_name}")
        if not content:
            continue

        soup = BeautifulSoup(content, "html.parser")
        rows = soup.select("table tbody tr")
        matched = 0
        for row in rows:
            a = row.select_one("a")
            if not a:
                continue
            title = a.get_text(strip=True)
            if not title or len(title) < 4:
                continue

            href = a.get("href", "")
            m = re.search(r"['\"(](\d{4,})['\")]", href)
            if href.startswith("javascript") and m:
                url = f"{BASE}/fe/bbs/NR_view.do?bbsCd={bbs_cd}&bbsSeq={m.group(1)}"
            elif href.startswith("/"):
                url = BASE + href
            elif href.startswith("http"):
                url = href
            else:
                url = list_url

            items.append({
                "source": "회계기준원",
                "category": "회계기준",
                "title": title,
                "url": url,
                "date": _parse_date(row.get_text(" ", strip=True)),
            })
            matched += 1
        print(f"  [kasb/{board_name}] {matched}건")
    return items
