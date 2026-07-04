"""한국회계기준원(KASB) 기준서 제·개정 공고 게시판 크롤링.

주의: 게시판 HTML 구조가 바뀌면 아래 CSS 셀렉터를 수정해야 합니다.
실제 URL/파라미터는 www.kasb.or.kr 에서 '제·개정 공고' 게시판 주소를 확인해 넣으세요.
"""
import re
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://www.kasb.or.kr"
# ── 사이트 확인 후 실제 게시판 목록 URL로 교체 ──
LIST_URL = BASE + "/fe/bbs/NR_list.do?bbsCd=1023"


def fetch(session: requests.Session) -> list[dict]:
    items = []
    resp = session.get(LIST_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # ── 구조 변경 시 이 셀렉터 수정 ──
    rows = soup.select("table tbody tr")
    for row in rows:
        a = row.select_one("a")
        if not a:
            continue
        title = a.get_text(strip=True)
        href = a.get("href", "")
        # 자바스크립트 링크(예: goView('1234'))인 경우 게시글 번호 추출
        m = re.search(r"['\"](\d+)['\"]", href)
        if href.startswith("javascript") and m:
            url = f"{BASE}/fe/bbs/NR_view.do?bbsCd=1023&bbsSeq={m.group(1)}"
        else:
            url = urljoin(BASE, href)

        date = _find_date(row)
        items.append({
            "source": "회계기준원",
            "category": "회계기준",
            "title": title,
            "url": url,
            "date": date,
        })
    return items


def _find_date(row) -> str:
    text = row.get_text(" ", strip=True)
    m = re.search(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", text)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")
