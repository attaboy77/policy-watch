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
- 2026-11-14: 하위 수집 press(금감원 보도자료 B0000188)·notes(주석공시 모범사례 B0000128)
  추가. B2와 달리 카테고리를 icfr로 고정하지 않고 fsc 보도자료와 같은 기존 필터(행사 공지 →
  classify → 세목)를 탄다. 첨부는 목록 행에 있어 상세 페이지를 열지 않는다.
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _excluded_log, _http, _gap_log
from .._config import COLLECT_WINDOW_DAYS, DISABLED_SOURCES
from .._source_health import PartialFetch
from .._utils import (classify, doc_type_of, extract_effective_date, extract_title_revision_date,
                      is_event_announcement, keyword_score, matched_keywords, make_id_exact,
                      final_score, pass_tax_filter, recency_score, has_fiscal_year_override)

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
                 is_static: bool = False, date_estimated: bool = False,
                 category: str = "icfr") -> dict:
    # 2026-11-14: press·notes는 classify()로 카테고리를 정하므로 인자로 받는다(B2·B3는 icfr 고정).
    kw = keyword_score(title, category)
    rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
    return {
        "id": make_id_exact(url),  # view.do?nttId=처럼 쿼리가 식별자(B2/B3 공용 헬퍼)
        "category": category,
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
        "matched_keywords": matched_keywords(title, category),
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
        url = href if href.startswith("http") else f"{FSS_BASE}{href}"
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            _excluded_log.skip(source="금융감독원", reason="collect:event_announcement", title=title,
                               url=url, category="icfr")
            continue
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
        # 2026-09-02 사용자 지시로 원문을 직접 확인해 effective_date를 수동
        # 등록한 항목(_utils._FISCAL_YEAR_EFFECTIVE_DATES)은 이미 해결됐으니
        # "검토 필요" 목록에 또 안 남게 건너뛴다(실측 버그: 이 필터 없이는
        # finalize_item()이 나중에 채운 값과 무관하게 여기서 무조건 기록됨).
        if not has_fiscal_year_override(item["id"]):
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
        url = href if href.startswith("http") else f"{KICFR_BASE}/sub/menu/{href.lstrip('./')}"
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            _excluded_log.skip(source="내부회계관리제도운영위원회", reason="collect:event_announcement",
                               title=title, url=url, category="icfr")
            continue
        doc_type = doc_type_of(title, source_tier=1)
        revision_date = extract_title_revision_date(title)
        items.append(_build_item(
            title=title, url=url, published_at=revision_date, doc_type=doc_type,
            domain="k-icfr.org", source_name="내부회계관리제도운영위원회",
            is_static=True, date_estimated=revision_date is None,
        ))
    return items


def _row_attachments(row) -> list[dict] | None:
    """목록 행 안의 첨부(`a[href*=fileDown.do]` + `span.name`) — 상세 페이지를 따로 열지 않는다."""
    out = []
    for a in row.select('a[href*="fileDown.do"]'):
        name_span = a.select_one("span.name")
        name = name_span.get_text(strip=True) if name_span else ""
        href = a.get("href", "")
        if name and href:
            out.append({"name": name, "url": href if href.startswith("http") else f"{FSS_BASE}{href}"})
    return out or None


_NTT_ID_RE = re.compile(r"nttId=(\d+)")


def _fetch_board(part: str, list_url: str, params: dict, *, page_unit: int,
                 max_pages: int) -> tuple[list[dict], list[str]]:
    """FSS 일반 게시판(table tbody tr / td.title a / 4번째 칸 등록일) 한 곳을 읽어 우리 카테고리에
    걸리는 행만 항목으로 만든다(2026-11-14, press·notes 공용). (항목, 부분 실패 사유)를 돌려주고,
    목록 행을 하나도 못 읽으면 예외 — 관련 행이 없어 0건인 건 정상이다.

    필터는 fsc 보도자료와 같은 기존 파이프라인 그대로: 행사 공지 → classify() → 세목 필터.
    """
    items: list[dict] = []
    page_errors: list[str] = []
    rows_seen = row_errors = 0
    for page in range(1, max_pages + 1):
        if page > 1:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            resp = _http.get(list_url, params={**params, "pageUnit": page_unit, "pageIndex": page},
                             headers={"User-Agent": FSS_UA})
            rows = BeautifulSoup(resp.text, "html.parser").select("table tbody tr")
        except Exception as exc:  # noqa: BLE001
            print(f"[fss] {part} page={page} 수집 실패: {exc}")
            page_errors.append(f"page={page}: {exc}")
            break
        for row in rows:
            title, url = "", None
            try:  # 행 단위 격리(11/13 kasb·fsc와 같은 방식)
                link = row.select_one("td.title a")
                cells = row.find_all("td")
                if link is None or len(cells) < 4:
                    continue  # "등록된 게시물이 없습니다" 같은 안내 행
                title = link.get_text(strip=True)
                m = _NTT_ID_RE.search(link.get("href", ""))
                if not title or not m:
                    raise ValueError("제목 또는 nttId 없음")
                # 목록 href엔 sdate·edate·pageIndex가 붙어 매일 바뀐다 — 그대로 id를 만들면 같은 글이
                # 날마다 새 id(=메일 "신규" 재발송)가 된다. nttId·menuNo만 남긴 URL로 고정한다.
                url = f"{list_url.rsplit('/', 1)[0]}/view.do?nttId={m.group(1)}&menuNo={params['menuNo']}"
                published_at = cells[3].get_text(strip=True)
                pub_date = _parse_iso_date(published_at)
                rows_seen += 1  # 날짜 해석 성공 뒤에 센다(11/13 fsc 방식)
                if is_event_announcement(title):
                    _excluded_log.skip(source="금융감독원", reason="collect:event_announcement",
                                       title=title, url=url)
                    continue
                category = classify(title)
                if category is None:
                    _excluded_log.skip(source="금융감독원", reason="collect:no_category", title=title, url=url)
                    continue
                if not pass_tax_filter(category=category, layer="L1", text=title):
                    _excluded_log.skip(source="금융감독원", reason="collect:tax_subject", title=title,
                                       url=url, category=category)
                    continue
                item = _build_item(title=title, url=url, published_at=pub_date.isoformat(),
                                   doc_type=doc_type_of(title, source_tier=1), domain="fss.or.kr",
                                   source_name="금융감독원", category=category,
                                   effective_date=extract_effective_date(title) if category != "tax" else None)
                item["attachments"] = _row_attachments(row)
                items.append(item)
            except Exception as exc:  # noqa: BLE001
                row_errors += 1
                shown = title or "(제목 없음)"
                print(f"[fss] {part} 행 건너뜀: {shown} — {exc}")
                _excluded_log.skip(source="금융감독원", reason="collect:row_parse_error",
                                   title=f"{shown} — {exc}", url=url)
        if len(rows) < page_unit:
            break  # 마지막 페이지
    if rows_seen == 0:
        detail = "; ".join(page_errors) or (f"행 {row_errors}개 전부 해석 실패" if row_errors else "")
        raise RuntimeError(f"{part} 목록 행 0개 — 전 페이지 실패 또는 페이지 구조 변경·차단 의심"
                           + (f" ({detail})" if detail else ""))
    reasons = list(page_errors)
    if row_errors:
        reasons.append(f"행 {row_errors}개 해석 실패(건너뜀, EXCLUDED_LOG collect:row_parse_error)")
    return items, reasons


# ── press: 금감원 보도자료(B0000188) — 2026-11-14 사용자 지시로 추가 ──────────────────
# 전 분야 보도자료(하루 3~8건)라 우리 카테고리에 걸리는 것만 남는다. 서버 쪽 날짜 필터
# (sdate/edate)와 pageUnit이 실제로 먹는다(실측: 90일 220행을 한 번에 3.6초) — 최근
# COLLECT_WINDOW_DAYS일만 받는다.
PRESS_LIST_URL = f"{FSS_BASE}/fss/bbs/B0000188/list.do"
PRESS_PAGE_UNIT = 300
PRESS_MAX_PAGES = 2


def fetch_press() -> tuple[list[dict], list[str]]:
    today = datetime.now(_KST).date()
    start = today - timedelta(days=COLLECT_WINDOW_DAYS)
    return _fetch_board("press", PRESS_LIST_URL,
                        {"menuNo": "200218", "sdate": start.isoformat(), "edate": today.isoformat()},
                        page_unit=PRESS_PAGE_UNIT, max_pages=PRESS_MAX_PAGES)


# ── notes: 주석공시 모범사례(B0000128) — 2026-11-14 사용자 지시로 추가 ─────────────────
# 연 1~2건, 전체 13건(2014~)인 상설 성격 게시판이라 B2처럼 기간 제한 없이 전부 읽는다.
NOTES_LIST_URL = f"{FSS_BASE}/fss/bbs/B0000128/list.do"


def fetch_disclosure_notes() -> tuple[list[dict], list[str]]:
    return _fetch_board("notes", NOTES_LIST_URL, {"menuNo": "200435"}, page_unit=100, max_pages=1)


def part_of(item: dict) -> str:
    """캐시 항목이 어느 하위 수집에서 왔는지 — 부분 폴백용(main.SUB_SOURCES)."""
    url = (item.get("urls") or {}).get("official") or ""
    if "k-icfr.org" in url:
        return "b3"
    if "/B0000188/" in url:
        return "press"
    if "/B0000128/" in url:
        return "notes"
    return "b2"


def fetch() -> list[dict]:
    """B2+B3+press+notes(B1은 참고 자료라 제외). 소스 한 종류가 실패해도 나머지는 계속 진행.

    2026-10-14: 하위 수집이 예외를 내거나 0건이면 실패로 본다. 일부만 실패하면
    `PartialFetch`로 올려 main이 그 부분만 전일 캐시로 채우게 하고, 전부 실패하면
    일반 예외로 올려 소스 단위 폴백을 탄다. 전에는 실패를 print만 하고 삼켜서
    10/9~10/10 B2 6건이 조용히 빠졌다가 10/11 신규 메일로 다시 나갔다.

    2026-11-14: press(보도자료)·notes(주석공시 모범사례) 추가. 이 둘은 행 단위 격리 +
    "목록 행을 읽었는데 관련 항목이 없으면 정상 0건" 기준(fsc 11/13 방식) — 예외·행 0개·
    행 해석 실패만 부분 실패다. B2·B3의 "0건 = 실패" 기준은 그대로 둔다."""
    out: list[dict] = []
    failed: dict[str, str] = {}
    try:
        got = fetch_data_board()
        if got:
            out.extend(got)
        else:
            failed["b2"] = "결과 0건(목록 행 없음 또는 파싱 실패)"
    except Exception as exc:  # noqa: BLE001
        failed["b2"] = str(exc)
    if "b2" in failed:
        print(f"[fss] B2 수집 실패: {failed['b2']}")
    time.sleep(SLEEP_BETWEEN_REQUESTS)
    try:
        got = fetch_kicfr_guidelines()
        if got:
            out.extend(got)
        else:
            failed["b3"] = "결과 0건(목록 행 없음 또는 파싱 실패)"
    except Exception as exc:  # noqa: BLE001
        failed["b3"] = str(exc)
    if "b3" in failed:
        print(f"[fss] B3(k-icfr.org) 수집 실패: {failed['b3']}")
    for part, fn in (("press", fetch_press), ("notes", fetch_disclosure_notes)):
        if not part_enabled(part):
            print(f"[fss] {part}: data/source_toggles.yml에서 꺼짐(fss_{part}) — 건너뜀")
            continue
        time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            got, reasons = fn()
        except Exception as exc:  # noqa: BLE001
            failed[part] = str(exc)
            print(f"[fss] {part} 수집 실패: {failed[part]}")
            continue
        out.extend(got)
        if reasons:
            failed[part] = " / ".join(reasons)
            print(f"[fss] {part} 부분 실패: {failed[part]}")
    if len(failed) == sum(map(part_enabled, TRACKED_PARTS)) and not out:
        raise RuntimeError("fss 하위 수집 모두 실패 — " + " / ".join(f"{p}: {r}" for p, r in failed.items()))
    if failed:
        raise PartialFetch(out, failed, part_of)
    return out


# 부분 실패를 따로 세는 하위 수집(main.SUB_SOURCES["fss"]와 같아야 한다).
TRACKED_PARTS = ("b2", "b3", "press", "notes")


def part_enabled(part: str) -> bool:
    """data/source_toggles.yml에서 `fss_{part}`를 enabled: false로 두면 그 하위 수집만 끈다
    (2026-11-14, press·notes용 — 코드 수정 없이 한 줄로 끄기)."""
    return f"fss_{part}" not in DISABLED_SOURCES


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
