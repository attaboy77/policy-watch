"""국세청 보도자료 게시판 크롤링.

주의: HTML 구조 변경 시 셀렉터 수정 필요. 목록 URL은 nts.go.kr 에서 확인하세요.
"""
import re
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://www.nts.go.kr"
# ── 사이트 확인 후 실제 보도자료 목록 URL로 교체 ──
LIST_URL = BASE + "/nts/na/ntt/selectNttList.do?mi=2201&bbsId=1030"


def fetch(session: requests.Session) -> list[dict]:
    items = []
    resp = session.get(LIST_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    rows = soup.select("table tbody tr")  # ── 구조 변경 시 수정 ──
    for row in rows:
        a = row.select_one("a")
        if not a:
            continue
        title = a.get_text(strip=True)
        href = a.get("href", "")
        m = re.search(r"nttSn=(\d+)|['\"](\d+)['\"]", href)
        if href.startswith("javascript") and m:
            seq = m.group(1) or m.group(2)
            url = f"{BASE}/nts/na/ntt/selectNttInfo.do?mi=2201&bbsId=1030&nttSn={seq}"
        else:
            url = urljoin(BASE, href)

        items.append({
            "source": "국세청",
            "category": "세법",
            "title": title,
            "url": url,
            "date": _find_date(row),
        })
    return items


def _find_date(row) -> str:
    text = row.get_text(" ", strip=True)
    m = re.search(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", text)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.today().strftime("%Y-%m-%d")
