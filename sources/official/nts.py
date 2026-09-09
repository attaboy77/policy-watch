# -*- coding: utf-8 -*-
"""국세청(nts.go.kr) 개정세법 해설 수집기 — D2.

docs/SOURCE_PROBE.md §D2 "완전 검증" 기반.

- 목록: `selectNttList.do?mi=7133&bbsId=1083`. 행은 `data-table="number"/"date"/"subject"/
  "write"` 4열로 매우 깔끔하다. 날짜는 `YYYY.MM.DD.` 점 구분 포맷.
- 상세: `selectNttInfo.do?mi=7133&nttSn={data-id}`.
- 연 1회(매년 4월경) 발간되는 자료집이라 이 게시판 자체가 이미 "개정세법 해설"
  전용이므로 category="tax" 고정, doc_type="해설·교육자료" 고정(ADDENDUM-3 §4).
- **세법 시행일 = 법제처(D4) 단일 소스** 원칙(사용자 지시 2026-08-26)에 따라
  effective_date는 항상 None — 연간 자료집 PDF 안에 세목별로 제각각 있어 항목
  단위로 뽑을 수 없고(SOURCE_PROBE.md D2 참고), 애초에 시도하지 않는다.
- 첨부 PDF 링크는 `javascript:htmlDocTransView(...)` 형태라 KASB와 마찬가지로
  평문 URL을 구성할 수 없다. attachments는 채우지 않는다(KASB와 동일 정책).
- **연도 필터(2026-09-09)**: 이 게시판은 연 1회 자료집이지만 과거 발간분이
  전부 목록에 남아있어(2017~2026년치, 10건) 매번 그대로 수집된다. 평소엔
  전일 캐시와 id가 같아 "신규"로 안 잡히지만, 이 소스가 며칠 실패했다 복구될
  때(캐시가 비었을 때) 10건 전부가 "신규 발표"로 오판돼 메일에 섞이는 사고가
  2026-09-04·09-09 두 차례 재발(원인은 `sources/main.py`의 소스 실패 폴백
  경로 문제 — `docs/NEXT.md` 참고, 이 필터는 그것과 별개로 애초에 오래된
  연도까지 매번 수집 대상에 넣을 이유가 없다는 사용자 판단). 제목이
  "YYYY년 ..."로 시작하는 항목은 최근 `_KEEP_YEARS`개 연도치만 남긴다.
"""
from __future__ import annotations

import re
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _http
from .._utils import is_event_announcement, keyword_score, matched_keywords, make_id_exact, final_score, recency_score

BASE = "https://www.nts.go.kr"
LIST_URL = f"{BASE}/nts/na/ntt/selectNttList.do"
DETAIL_URL = f"{BASE}/nts/na/ntt/selectNttInfo.do"
MI = "7133"
BBS_ID = "1083"

SOURCE_NAME = "국세청"
_KST = timezone(timedelta(hours=9))

_TITLE_YEAR_RE = re.compile(r"^(\d{4})년")  # "2026년 개정세법 해설" 형태만 매칭(연도 필터용)
_KEEP_YEARS = 2  # 제목에 연도가 있는 연간 자료는 최근 몇 개 연도치만 남길지


def probe() -> dict:
    try:
        resp = _http.get_govt(LIST_URL, params={"mi": MI, "bbsId": BBS_ID})
        ok = resp.status_code == 200 and 'data-table="subject"' in resp.text
        return {"ok": ok, "method": "html", "note": f"selectNttList.do HTTP {resp.status_code}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _parse_dotted_date(s: str) -> str | None:
    m = re.match(r"(\d{4})\.(\d{1,2})\.(\d{1,2})\.?", s.strip())
    if not m:
        return None
    y, mo, d = (int(x) for x in m.groups())
    try:
        return date(y, mo, d).isoformat()
    except ValueError:
        return None


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _filter_recent_years(items: list[dict], *, keep: int = _KEEP_YEARS) -> list[dict]:
    """제목이 "YYYY년 ..."로 시작하는 연간 자료는 최근 `keep`개 연도치만 남긴다.

    "최근"의 기준은 오늘 날짜가 아니라 **이 목록에 실제로 있는 연도 중 큰 값**
    이다 — 예를 들어 올해치가 아직 안 올라온 시점(4월 이전)엔 작년이 최신이
    되므로, 오늘 연도를 기준으로 자르면 그 사이엔 0건이 되는 문제를 피한다.
    제목에 연도가 없는 항목(형식이 다른 공지 등)은 건드리지 않고 그대로 둔다.
    """
    years_present = sorted(
        {int(m.group(1)) for it in items if (m := _TITLE_YEAR_RE.match(it["title"]))},
        reverse=True,
    )
    keep_years = set(years_present[:keep])
    kept, dropped = [], []
    for it in items:
        m = _TITLE_YEAR_RE.match(it["title"])
        if m and int(m.group(1)) not in keep_years:
            dropped.append(it)
        else:
            kept.append(it)
    if dropped:
        print(f"[nts] 연도 필터: {len(dropped)}건 제외(최근 {sorted(keep_years, reverse=True)}년치만 유지) - "
              + ", ".join(it["title"][:20] for it in dropped))
    return kept


def fetch() -> list[dict]:
    """D2: 개정세법 해설 게시판 전체. 게시판 자체가 세법 전용이라 classify() 불필요."""
    resp = _http.get_govt(LIST_URL, params={"mi": MI, "bbsId": BBS_ID})
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []

    for row in soup.select("table tbody tr"):
        subject_cell = row.select_one('td[data-table="subject"]')
        date_cell = row.select_one('td[data-table="date"]')
        if subject_cell is None:
            continue
        a = subject_cell.find("a")
        if a is None:
            continue
        title = a.get_text(strip=True)
        ntt_id = a.get("data-id", "")
        if not title or not ntt_id:
            continue
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            continue
        published_at = _parse_dotted_date(date_cell.get_text(strip=True)) if date_cell else None
        url = f"{DETAIL_URL}?mi={MI}&nttSn={ntt_id}"
        kw = keyword_score(title, "tax")
        rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
        items.append({
            "id": make_id_exact(url),  # selectNttInfo.do?nttSn=처럼 쿼리가 식별자
            "category": "tax",
            "doc_type": "해설·교육자료",
            "title": title,
            "summary": [],
            "impact": None,
            "published_at": published_at,
            "collected_at": _now_kst_iso(),
            "effective_date": None,  # 법제처(D4)가 세법 시행일 단일 소스 — 이 소스는 시도하지 않음
            "source": {"name": SOURCE_NAME, "domain": "nts.go.kr", "tier": 1, "type": "official"},
            "trust_score": 100,
            "keyword_score": kw,
            "final_score": final_score(100, kw, rec),
            "matched_keywords": matched_keywords(title, "tax"),
            "urls": {"news": None, "official": url},
            "law_meta": None,
            "attachments": None,
            "layer": "L1_comprehensive",  # ADDENDUM-3 §4 D2: 전 세목 포괄 연간 자료집, 세목 필터 면제
            "is_noise": False,
        })
    return _filter_recent_years(items)


if __name__ == "__main__":
    print("=== NTS probe ===")
    print(probe())

    print("\n=== D2: 개정세법 해설 ===")
    items = fetch()
    for it in items[:10]:
        print(f"  [{it['doc_type']}] {it['published_at']} | {it['title'][:50]}")
    print(f"  총 {len(items)}건 (effective_date는 전부 None — 법제처(D4)가 세법 시행일 단일 소스)")
