# -*- coding: utf-8 -*-
"""기획재정부(moef.go.kr → 실접속 도메인 mofe.go.kr) 보도·참고자료 수집기 — D1.

docs/SOURCE_PROBE.md §D1 "재조사 결과" 기반.

- `moef.go.kr`/`www.moef.go.kr`은 전부 `mofe.go.kr`로 301 리다이렉트된다.
- 목록: `nesdta.do?bbsId=MOSFBBS_000000000028&menuNo=4010100`. 행은
  `<a href="javascript:fn_egov_select('MOSF_...');">` onclick 패턴이며, 별도 세션/POST
  없이 최초 GET 응답에 전부 들어있다(제목/날짜/담당부서).
- **명칭 함정**: 페이지 메타데이터(`<title>`, `og:title`, 바닥글)가 전부 "재정경제부"
  (2008년 이전 명칭)로 남아있다. `source.name`은 절대 스크래핑하지 않고 "기획재정부"로
  고정한다.
- 이 게시판은 세제 전용이 아니라 기재부 전체 보도자료(부동산 PF, 국고채, 관세 등도
  섞여 있음)다. `_utils.classify()`로 우리 4개 카테고리(주로 tax) 중 하나에 걸리는
  항목만 남기고, 아무 데도 안 걸리면 버린다.
- **세법 시행일 = 법제처(D4) 단일 소스** 원칙(SOURCE_PROBE.md, 사용자 지시 2026-08-26)에
  따라 이 소스는 `effective_date` 추출을 아예 시도하지 않고 항상 None으로 둔다.
  `_gap_log`에도 기록하지 않는다(세법은 그 로그 대상이 아님 — `_gap_log.py` docstring 참고).
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _http
from .._utils import (classify, doc_type_of, is_admin_noise, pass_tax_filter, keyword_score,
                      matched_keywords, make_id_exact, final_score, recency_score)

BASE = "https://mofe.go.kr"
PRESS_LIST_URL = f"{BASE}/nw/nes/nesdta.do"
PRESS_DETAIL_URL = f"{BASE}/nw/nes/detailNesDtaView.do"
BBS_ID = "MOSFBBS_000000000028"
MENU_NO = "4010100"

SOURCE_NAME = "기획재정부"  # 스크래핑 금지 — 페이지 메타데이터는 "재정경제부"로 오염돼 있음
SLEEP_BETWEEN_REQUESTS = 1.0
_KST = timezone(timedelta(hours=9))
_SELECT_RE = re.compile(r"fn_egov_select\('([^']+)'\)")


def probe() -> dict:
    try:
        resp = _http.get(PRESS_LIST_URL, params={"bbsId": BBS_ID, "menuNo": MENU_NO})
        ok = resp.status_code == 200 and "fn_egov_select" in resp.text
        return {"ok": ok, "method": "html", "note": f"nesdta.do HTTP {resp.status_code}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _parse_dotted_date(s: str) -> str | None:
    """'2026.08.24.' → '2026-08-24'."""
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


def _build_item(*, category: str, title: str, url: str, published_at: str | None, doc_type: str) -> dict:
    kw = keyword_score(title, category)
    rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
    return {
        "id": make_id_exact(url),  # detailNesDtaView.do?searchNttId1=처럼 쿼리가 식별자
        "category": category,
        "doc_type": doc_type,
        "title": title,
        "summary": [],
        "impact": None,
        "published_at": published_at,
        "collected_at": _now_kst_iso(),
        "effective_date": None,  # 세법 시행일은 법제처(D4) 단일 소스 — 이 소스는 시도하지 않음
        "source": {"name": SOURCE_NAME, "domain": "moef.go.kr", "tier": 1, "type": "official"},
        "trust_score": 100,
        "keyword_score": kw,
        "final_score": final_score(100, kw, rec),
        "matched_keywords": matched_keywords(title, category),
        "urls": {"news": None, "official": url},
        "law_meta": None,
        "attachments": None,
        "layer": "L1",
        "is_noise": False,
    }


def fetch(*, max_items: int | None = None) -> list[dict]:
    """D1: 보도·참고자료 게시판. 우리 카테고리(주로 tax)에 안 걸리는 항목은 버린다."""
    resp = _http.get(PRESS_LIST_URL, params={"bbsId": BBS_ID, "menuNo": MENU_NO})
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []

    for li in soup.select("li"):
        a = li.find("h3")
        a = a.find("a") if a else None
        if a is None:
            continue
        m = _SELECT_RE.search(a.get("href", ""))
        if not m:
            continue
        title = a.get_text(strip=True)
        if is_admin_noise(title):  # ADDENDUM-4 §1
            continue
        category = classify(title)
        if category is None:
            continue  # 부동산 PF·국고채 등 우리 4개 카테고리와 무관한 보도자료는 버림
        # 이 게시판은 기재부 보도자료 전체라 "세제개편안" 종합문서(L1_comprehensive)가
        # 아니다 — tax로 분류된 항목은 세목 화이트리스트를 통과해야 한다
        # (종부세·상속세 등이 "세법"류 required 키워드에 우연히 걸려 새는 것 방지).
        if not pass_tax_filter(category=category, layer="L1", text=title):
            continue

        ntt_id = m.group(1)
        date_span = li.select_one(".boardInfo .infoLeft .date")
        published_at = _parse_dotted_date(date_span.get_text(strip=True)) if date_span else None
        url = f"{PRESS_DETAIL_URL}?searchBbsId1={BBS_ID}&searchNttId1={ntt_id}&menuNo={MENU_NO}"
        doc_type = doc_type_of(title, source_tier=1)
        items.append(_build_item(category=category, title=title, url=url,
                                  published_at=published_at, doc_type=doc_type))
        if max_items and len(items) >= max_items:
            break
    return items


if __name__ == "__main__":
    print("=== MOEF probe ===")
    print(probe())

    print("\n=== D1: 보도·참고자료(카테고리 매칭분만) ===")
    items = fetch()
    for it in items[:15]:
        print(f"  [{it['category']:5s}] [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:55]}")
    print(f"  총 {len(items)}건 (effective_date는 전부 None — 법제처(D4)가 세법 시행일 단일 소스)")
