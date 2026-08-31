# -*- coding: utf-8 -*-
"""내부회계관리제도(icfr) 카테고리 수집기 — B1(FSS 기준 개요) / B2(FSS 자료 게시판) /
B3(내부회계관리제도운영위원회, k-icfr.org).

docs/SOURCE_PROBE.md §B 조사 결과에 기반한다.

- fss.or.kr은 "Bot"이 들어간 User-Agent를 통째로 차단한다(WAF 추정). robots.txt를
  확인한 결과 우리 대상 경로는 비허용 목록에 없어, 신원(연락처)을 숨기지 않는
  브라우저형 UA로 이 도메인에서만 우회한다(사용자 결정 2026-08-26). 요청 간격은
  2초 이상.
- B2 게시판은 실측 결과 상세 페이지 본문에 시행일 텍스트가 전혀 없고 첨부
  HWP/PDF 안에만 있다. SPEC §4-3(첨부파일 다운로드·파싱 금지)을 지키는 한 이
  소스의 effective_date는 항상 None이며, 이를 `_gap_log`에 모아 관리자가
  `data/schedules_manual.yml`에 옮길지 판단하게 한다.
- B1(정적 개요 페이지)은 날짜가 있는 "항목"이 아니라 참고 링크 성격이라
  items로 만들지 않는다(probe만 제공).
- B3(k-icfr.org)는 EUC-KR 인코딩 레거시 ASP 사이트다.
"""
from __future__ import annotations

import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _http, _gap_log
from .._utils import (doc_type_of, extract_title_revision_date, is_event_announcement,
                      keyword_score, matched_keywords, make_id_exact, final_score, recency_score)

FSS_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/124.0.0.0 Safari/537.36 (contact: alchem1024@gmail.com, project: policy-watch)")
FSS_BASE = "https://www.fss.or.kr"
B1_URL = f"{FSS_BASE}/fss/main/contents.do?menuNo=201174"
B2_LIST_URL = f"{FSS_BASE}/fss/bbs/B0000155/list.do?menuNo=201177"

KICFR_BASE = "https://www.k-icfr.org"
B3_GUIDELINE_URL = f"{KICFR_BASE}/sub/menu/guideline.asp"
B3_DATA_URL = f"{KICFR_BASE}/sub/menu/data.asp"

SLEEP_BETWEEN_REQUESTS = 2.0  # 사용자 지시: fss.or.kr은 2초 이상 간격
_KST = timezone(timedelta(hours=9))


def probe() -> dict:
    """B1/B2(fss.or.kr, 전용 UA)와 B3(k-icfr.org)에 실제로 접근해 상태를 확인한다."""
    results = {}
    try:
        resp = _http.get(B2_LIST_URL, headers={"User-Agent": FSS_UA})
        results["fss"] = {"ok": resp.status_code == 200 and 'class="title"' in resp.text,
                           "method": "html", "note": f"B0000155/list.do HTTP {resp.status_code} (전용 UA)"}
    except Exception as exc:  # noqa: BLE001
        results["fss"] = {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}
    time.sleep(SLEEP_BETWEEN_REQUESTS)
    try:
        resp = _http.get(B3_GUIDELINE_URL)
        results["k_icfr"] = {"ok": resp.status_code == 200, "method": "html",
                              "note": f"guideline.asp HTTP {resp.status_code} (EUC-KR)"}
    except Exception as exc:  # noqa: BLE001
        results["k_icfr"] = {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}
    return results


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _build_item(*, title: str, url: str, published_at: str | None, doc_type: str,
                 domain: str, source_name: str, effective_date: str | None = None,
                 is_static: bool = False, date_estimated: bool = False) -> dict:
    kw = keyword_score(title, "icfr")
    rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
    return {
        "id": make_id_exact(url),  # view.do?nttId=처럼 쿼리가 식별자(B2/B3 공용 헬퍼)
        "category": "icfr",
        "doc_type": doc_type,
        "title": title,
        "summary": [],
        "impact": None,
        "published_at": published_at,
        "collected_at": _now_kst_iso(),
        "effective_date": effective_date,
        "source": {"name": source_name, "domain": domain, "tier": 1, "type": "official"},
        "trust_score": 100,
        "keyword_score": kw,
        "final_score": final_score(100, kw, rec),
        "matched_keywords": matched_keywords(title, "icfr"),
        "urls": {"news": None, "official": url},
        "law_meta": None,
        "attachments": None,  # TODO: fileDown.do 링크는 있으나 파일명 파싱은 후속 작업
        "layer": "L1",
        "is_noise": False,
        "is_static": is_static,
        "date_estimated": date_estimated,
    }


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def fetch_static_overview_note() -> dict:
    """B1: 정적 개요 페이지. 날짜 있는 '항목'이 아니라 참고 자료라 items로 만들지 않고
    접근 가능 여부/제목만 확인해 반환한다(로그·probe 용도).
    """
    resp = _http.get(B1_URL, headers={"User-Agent": FSS_UA})
    soup = BeautifulSoup(resp.text, "html.parser")
    h1 = soup.select_one("h1")
    return {"url": B1_URL, "title": h1.get_text(strip=True) if h1 else None,
            "status": resp.status_code}


def _fetch_attachments(detail_url: str) -> list[dict] | None:
    """상세 페이지의 dl.file-list에서 첨부파일명+다운로드 링크를 뽑는다.

    FSS는 (KASB와 달리) 첨부 다운로드 링크가 `javascript:` 아니라 실제 href
    (`/fss/cmmn/file/fileDown.do?...`)라 추출 가능하다(SPEC-ADDENDUM.md §4-3 스키마 예시와
    정확히 일치하는 소스).
    """
    resp = _http.get(detail_url, headers={"User-Agent": FSS_UA})
    soup = BeautifulSoup(resp.text, "html.parser")
    out = []
    for a in soup.select('a[href*="fileDown.do"]'):
        name_span = a.find_next("span", class_="name")
        if name_span is None:
            continue
        # .name 안에 "(파일크기: ...)" 같은 중첩 span이 더 있어 첫 텍스트 노드만 취한다.
        name = next((c for c in name_span.contents if isinstance(c, str)), "").strip()
        href = a.get("href", "")
        if not name or not href:
            continue
        url = href if href.startswith("http") else f"{FSS_BASE}{href}"
        out.append({"name": name, "url": url})
    return out or None


def fetch_data_board(*, fetch_attachments: bool = True) -> list[dict]:
    """B2: 내부회계관리제도자료 게시판(B0000155). 시행일은 항상 첨부파일 안에 있어
    본문에서 추출을 시도하지 않고 곧바로 _gap_log에 기록한다(실측 확인, SOURCE_PROBE.md 참고).
    """
    resp = _http.get(B2_LIST_URL, headers={"User-Agent": FSS_UA})
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []

    for row in soup.select("table tbody tr"):
        cells = row.find_all("td")
        title_cell = row.select_one("td.title a")
        if title_cell is None or len(cells) < 4:
            continue
        title = title_cell.get_text(strip=True)
        href = title_cell.get("href", "")
        if not title or not href:
            continue
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            continue
        url = href if href.startswith("http") else f"{FSS_BASE}{href}"
        published_at = cells[3].get_text(strip=True) or None
        doc_type = doc_type_of(title, source_tier=1)
        item = _build_item(title=title, url=url, published_at=published_at,
                            doc_type=doc_type, domain="fss.or.kr", source_name="금융감독원")
        if fetch_attachments:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
            try:
                item["attachments"] = _fetch_attachments(url)
            except Exception as exc:  # noqa: BLE001 - 첨부파일 조회 실패해도 항목 자체는 살린다
                print(f"[fss] 첨부파일 조회 실패({url}): {exc}")
        items.append(item)
        _gap_log.record(source="금융감독원(fss.or.kr)", category="icfr", title=title, url=url)
    return items


def fetch_kicfr_guidelines() -> list[dict]:
    """B3: 내부회계관리제도운영위원회(k-icfr.org) 모범규준 페이지. EUC-KR 인코딩 주의.

    이 게시판은 **상시 비치 자료**다(ADDENDUM-4 §2) — 신규 게시 소식이 아니라
    현재 유효한 모범규준을 상설 비치해둔 것이라 `is_static=True`로 고정한다.
    제목에 개정일이 박혀 있으면(예: "(2021.10.1. 개정)") 그걸 published_at으로
    쓰고, 없으면 collected_at으로 대체하되 date_estimated=True를 세운다
    (§2-1/§2-2 — 그렇게 안 하면 2021년 자료가 "오늘 나온 자료"로 보인다).
    """
    resp = _http.get(B3_GUIDELINE_URL)
    resp.encoding = "euc-kr"
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []
    for a in soup.select("a"):
        title = a.get_text(strip=True)
        href = a.get("href", "")
        if not title or not href or href.startswith("javascript"):
            continue
        if "모범규준" not in title and "설계" not in title and "평가" not in title:
            continue
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            continue
        url = href if href.startswith("http") else f"{KICFR_BASE}/sub/menu/{href.lstrip('./')}"
        doc_type = doc_type_of(title, source_tier=1)
        revision_date = extract_title_revision_date(title)
        items.append(_build_item(
            title=title, url=url, published_at=revision_date, doc_type=doc_type,
            domain="k-icfr.org", source_name="내부회계관리제도운영위원회",
            is_static=True, date_estimated=revision_date is None,
        ))
    return items


def fetch() -> list[dict]:
    """B2+B3 전체(B1은 참고 자료라 제외). 소스 한 종류가 실패해도 나머지는 계속 진행."""
    out: list[dict] = []
    try:
        out.extend(fetch_data_board())
    except Exception as exc:  # noqa: BLE001
        print(f"[fss] B2 수집 실패: {exc}")
    time.sleep(SLEEP_BETWEEN_REQUESTS)
    try:
        out.extend(fetch_kicfr_guidelines())
    except Exception as exc:  # noqa: BLE001
        print(f"[fss] B3(k-icfr.org) 수집 실패: {exc}")
    return out


if __name__ == "__main__":
    print("=== FSS/k-icfr.org probe ===")
    print(probe())

    print("\n=== B1: 내부회계관리제도 기준 개요(참고자료, items 아님) ===")
    print(fetch_static_overview_note())

    time.sleep(SLEEP_BETWEEN_REQUESTS)
    print("\n=== B2: 내부회계관리제도자료 게시판 ===")
    b2 = fetch_data_board()
    for it in b2[:10]:
        att = f" | 첨부 {len(it['attachments'])}개" if it["attachments"] else ""
        print(f"  [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:55]}{att}")
    print(f"  총 {len(b2)}건 (전부 _gap_log에 기록됨 — effective_date는 첨부파일 안에만 있음)")

    time.sleep(SLEEP_BETWEEN_REQUESTS)
    print("\n=== B3: 내부회계관리제도운영위원회(k-icfr.org) ===")
    b3 = fetch_kicfr_guidelines()
    for it in b3[:10]:
        print(f"  [{it['doc_type']:6s}] {it['title'][:55]}")
    print(f"  총 {len(b3)}건")

    _gap_log.flush()
    print(f"\n=== _gap_log: {len(_gap_log.gaps())}건 → docs/EFFECTIVE_DATE_GAPS.md 기록 ===")
