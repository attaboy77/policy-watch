# -*- coding: utf-8 -*-
"""금융위원회(fsc.go.kr) 보도자료 수집기 — A4/C2 직접 소스.

Phase 3C에서 정책브리핑(policy_briefing.py, D3)이 금융위원회를 사실상 거의
못 잡는다는 게 실측으로 확인돼(15페이지/약 300건 중 0건 반영) 추가했다
(사용자 지시 2026-08-26). docs/SOURCE_PROBE.md "fsc.go.kr 직접 소스 추가"
참고.

- robots.txt는 `Allow: /`만 있어 제약 없음. 우리 UA로 302(정상) 확인, FSS 같은
  차단 없음.
- 목록: `/no010101` (fsc010101 홈 위젯의 "보도자료 더보기" 링크). eGov류 게시판과
  달리 상세 링크(`/no010101/{id}`)와 첨부파일 다운로드 링크(`/comm/getFile?...`)가
  전부 평문 href다 — KASB/NTS와 달리 attachments를 바로 채울 수 있는 소스.
- 날짜는 `<div class="day">YYYY-MM-DD</div>`로 이미 ISO 포맷.
- 이 게시판은 금융위 전체 보도자료(보험업법, 은행 감독, 가계부채 등)를 다 담고
  있어 회계·ESG·내부회계와 무관한 게 대부분이다. `_utils.classify()`로 우리
  4개 카테고리에 걸리는 것만 남긴다.
- 2026-11-14: 하위 수집 notice(입법예고/규정변경예고 `/po040301`) 추가 — 외감규정 등이
  확정 고시 전 예고 단계로 올라온다. 필터는 보도자료와 같다(행사 공지 → classify → 세목).
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _excluded_log, _http
from .._config import COLLECT_WINDOW_DAYS, DISABLED_SOURCES
from .._source_health import PartialFetch
from .._utils import (classify, doc_type_of, extract_effective_date, is_event_announcement,
                      pass_tax_filter, keyword_score, matched_keywords, make_id_exact,
                      final_score, recency_score)

BASE = "https://www.fsc.go.kr"
LIST_URL = f"{BASE}/no010101"

SOURCE_NAME = "금융위원회"
SLEEP_BETWEEN_REQUESTS = 1.0
_KST = timezone(timedelta(hours=9))


def _classify_own_press(title: str) -> str | None:
    """금융위원회 자체 보도자료다 보니 제목 대부분에 '금융위원회'가 들어있다
    ("금융위원회, OO 개최" 같은 관용구). "금융위원회"는 kifrs 카테고리의 필수
    키워드라 이걸 그대로 두면 감독·제재·외교 등 회계와 무관한 보도자료가 전부
    kifrs로 오분류된다(실측 확인: "롯데카드 정보유출 과징금", "베트남 금융외교"
    등이 전부 kifrs로 걸림). 제목에서 그 토큰을 지우고 나머지로 분류한다 —
    출처 자체가 이미 금융위원회이므로 그 이름이 있다는 사실은 카테고리 신호가
    아니다.
    """
    return classify(title.replace("금융위원회", ""))


def probe() -> dict:
    try:
        resp = _http.get_govt(LIST_URL)
        ok = resp.status_code == 200 and 'class="day"' in resp.text
        return {"ok": ok, "method": "html", "note": f"no010101 HTTP {resp.status_code}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _extract_attachments(li) -> list[dict] | None:
    out = []
    for a in li.select('.file-list > a[href*="getFile"]'):
        name_span = a.select_one("span.name")
        name = name_span.get_text(strip=True) if name_span else a.get("title", "")
        href = a.get("href", "")
        if not name or not href:
            continue
        out.append({"name": name, "url": href if href.startswith("http") else f"{BASE}{href}"})
    return out or None


# 2026-10-01: fetch()가 "목록 행을 하나라도 읽었는지"를 알기 위한 카운터 — 관련 항목이
# 없어서 0건인 것(정상, main.ALLOW_EMPTY_SOURCES)과 구조 변경·차단으로 행 자체를
# 못 읽은 것(실패)을 구분한다.
_rows_seen = 0
_row_errors = 0  # 2026-11-13: 날짜 등 해석 실패로 건너뛴 행 수

# 2026-10-01 실측: 목록 페이지(no010101)는 한 페이지에 24~26초가 걸린다(메인 페이지는
# 1초 — 서버 쪽 목록 조회가 느림). 기본 timeout 15초·재시도 3회로는 매번 read timeout,
# 5페이지면 소스 상한 60초를 크게 넘는다(로컬 218초). 1페이지(10건, 2~3일치)만
# 넉넉한 timeout으로 한 번만(재시도 없이 — _http.get의 retries는 총 시도 횟수) 받는다.
PAGE_TIMEOUT = 40
PAGE_RETRIES = 1


def fetch_page(page: int = 1) -> list[dict]:
    global _rows_seen, _row_errors
    resp = _http.get_govt(LIST_URL, params={"curPage": page}, timeout=PAGE_TIMEOUT, retries=PAGE_RETRIES)
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []

    for li in soup.select("li"):
        subject_a = li.select_one(".subject a")
        day_div = li.select_one(".day")
        if subject_a is None or day_div is None:
            continue
        title, url = "", None
        try:  # 2026-11-13: 행 하나의 해석 실패가 페이지 전체를 죽이지 않게 행 단위로 격리
            title = subject_a.get_text(strip=True)
            href = subject_a.get("href", "")
            if not title or not href:
                continue
            url = href if href.startswith("http") else f"{BASE}{href}"
            published_at = day_div.get_text(strip=True) or None
            # 2026-11-13: 날짜 해석을 카테고리 필터보다 먼저, 행 수는 해석 성공 뒤에 센다 — 전엔
            # 행 수를 먼저 세서 날짜 예외로 행이 전부 빠져도 "행은 읽었다 → 0건 정상"이 됐다.
            pub_date = _parse_iso_date(published_at) if published_at else None
            _rows_seen += 1
            if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:event_announcement", title=title, url=url)
                continue
            category = _classify_own_press(title)
            if category is None:
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:no_category", title=title, url=url)
                continue  # 보험업 감독·가계부채 등 우리 4개 카테고리와 무관한 보도자료는 버림
            if not pass_tax_filter(category=category, layer="L1", text=title):
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:tax_subject", title=title, url=url,
                                   category=category)
                continue  # 드물지만 tax로 분류될 경우 세목 화이트리스트 적용(ADDENDUM-3 §3)

            doc_type = doc_type_of(title, source_tier=1)
            effective_date = extract_effective_date(title) if category != "tax" else None
            kw = keyword_score(title, category)
            rec = recency_score(pub_date) if pub_date else 0
            items.append({
                "id": make_id_exact(url),
                "category": category,
                "doc_type": doc_type,
                "title": title,
                "summary": [],
                "impact": None,
                "published_at": published_at,
                "collected_at": _now_kst_iso(),
                "effective_date": effective_date,
                "source": {"name": SOURCE_NAME, "domain": "fsc.go.kr", "tier": 1, "type": "official"},
                "trust_score": 100,
                "keyword_score": kw,
                "final_score": final_score(100, kw, rec),
                "matched_keywords": matched_keywords(title, category),
                "urls": {"news": None, "official": url},
                "law_meta": None,
                "attachments": _extract_attachments(li),
                "layer": "L1",
                "is_noise": False,
            })
        except Exception as exc:  # noqa: BLE001
            _row_errors += 1
            shown = title or "(제목 없음)"
            print(f"[fsc] 행 건너뜀: {shown} — {exc}")
            _excluded_log.skip(source=SOURCE_NAME, reason="collect:row_parse_error",
                               title=f"{shown} — {exc}", url=url)
    return items


def _fetch_list(max_pages: int) -> tuple[list[dict], list[str]]:
    """보도자료 목록(list). (항목, 부분 실패 사유) — 목록 행을 하나도 못 읽으면 예외."""
    global _rows_seen, _row_errors
    _rows_seen = 0
    _row_errors = 0
    items: list[dict] = []
    page_errors: list[str] = []
    for page in range(1, max_pages + 1):
        if page > 1:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            items.extend(fetch_page(page))
        except Exception as exc:  # noqa: BLE001
            print(f"[fsc] page={page} 수집 실패: {exc}")
            page_errors.append(f"page={page}: {exc}")
    if _rows_seen == 0:
        detail = "; ".join(page_errors) or (f"행 {_row_errors}개 전부 해석 실패" if _row_errors else "")
        raise RuntimeError("보도자료 목록 행 0개 — 전 페이지 실패 또는 페이지 구조 변경·차단 의심"
                           + (f" ({detail})" if detail else ""))
    reasons = list(page_errors)
    if _row_errors:
        reasons.append(f"행 {_row_errors}개 해석 실패(건너뜀, EXCLUDED_LOG collect:row_parse_error)")
    return items, reasons


# ── notice: 입법예고/규정변경예고(/po040301) — 2026-11-14 사용자 지시로 추가 ──────────
# 외감규정·증권공시규정·외감법 시행령 등이 확정 고시 전 예고 단계로 올라오는 게시판.
# 한 페이지 10행, 서버 응답이 빠르다(실측 0.6초). 최근 COLLECT_WINDOW_DAYS일 안의 예고만
# 받는다 — 페이지의 가장 오래된 게시일이 기간 밖이면 다음 페이지는 읽지 않는다.
# 보도자료 목록(list)이 Actions에서 최대 PAGE_TIMEOUT(40초)까지 걸리므로 이쪽 요청은
# 짧게 끊는다(소스 전체 상한 60초, main.SOURCE_TIMEOUT_SECONDS).
NOTICE_URL = f"{BASE}/po040301"
NOTICE_MAX_PAGES = 4
NOTICE_TIMEOUT = 10
_NOTICE_ID_RE = re.compile(r"noticeId=(\d+)")
_PERIOD_RE = re.compile(r"예고기간\s*:\s*(\d{4}-\d{2}-\d{2})\s*~\s*(\d{4}-\d{2}-\d{2})")


def _notice_attachments(li) -> list[dict] | None:
    out = []
    for fl in li.select(".file-list"):
        name_span = fl.select_one("span.name")
        a = fl.select_one('a[href*="getFile"]')
        if name_span is None or a is None:
            continue
        name = name_span.get_text(strip=True)
        href = a.get("href", "")
        if name and href:
            out.append({"name": name, "url": href if href.startswith("http") else f"{BASE}{href}"})
    return out or None


def fetch_notice_page(page: int, *, cutoff: date) -> tuple[list[dict], int, int, date | None]:
    """입법예고 목록 한 페이지 → (항목, 읽은 행 수, 해석 실패 행 수, 페이지의 가장 오래된 게시일)."""
    resp = _http.get_govt(NOTICE_URL, params={"curPage": page}, timeout=NOTICE_TIMEOUT, retries=1)
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []
    rows_seen = row_errors = 0
    oldest: date | None = None
    for a in soup.select('a[href*="po040301/view"]'):
        li = a.find_parent("li")
        if li is None:
            continue
        title, url = "", None
        try:  # 행 단위 격리(11/13 kasb·fsc와 같은 방식)
            title = a.get_text(strip=True)
            m = _NOTICE_ID_RE.search(a.get("href", ""))
            day_div = li.select_one(".day")
            if not title or not m or day_div is None:
                raise ValueError("제목·noticeId·게시일 중 하나가 없음")
            url = f"{NOTICE_URL}/view?noticeId={m.group(1)}"  # 목록 검색 파라미터는 떼서 id를 고정
            published_at = day_div.get_text(strip=True)
            pub_date = _parse_iso_date(published_at)
            rows_seen += 1  # 날짜 해석 성공 뒤에 센다(11/13 fsc 방식)
            oldest = pub_date if oldest is None or pub_date < oldest else oldest
            if pub_date < cutoff:
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:out_of_window",
                                   title=f"{title} (게시 {published_at})", url=url)
                continue
            if is_event_announcement(title):
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:event_announcement", title=title, url=url)
                continue
            category = _classify_own_press(title)
            if category is None:
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:no_category", title=title, url=url)
                continue
            if not pass_tax_filter(category=category, layer="L1", text=title):
                _excluded_log.skip(source=SOURCE_NAME, reason="collect:tax_subject", title=title, url=url,
                                   category=category)
                continue
            pm = _PERIOD_RE.search(li.get_text(" ", strip=True))
            period = f"{pm.group(1).replace('-', '.')}~{pm.group(2).replace('-', '.')}" if pm else None
            kw = keyword_score(title, category)
            items.append({
                "id": make_id_exact(url),
                "category": category,
                "doc_type": doc_type_of(title, source_tier=1),
                "title": title,
                "summary": [],
                "impact": None,
                "published_at": published_at,
                "collected_at": _now_kst_iso(),
                "effective_date": None,  # 예고 단계엔 시행일 미확정(lawmaking과 같음)
                "source": {"name": SOURCE_NAME, "domain": "fsc.go.kr", "tier": 1, "type": "official"},
                "trust_score": 100,
                "keyword_score": kw,
                "final_score": final_score(100, kw, recency_score(pub_date)),
                "matched_keywords": matched_keywords(title, category),
                "urls": {"news": None, "official": url},
                "law_meta": None,
                "attachments": _notice_attachments(li),
                # 카드에 없는 사실(의견 접수기간)을 규칙 기반 요약 1줄로(lawmaking과 같은 방식)
                "_body": f"의견 접수기간 {period}" if period else None,
                "layer": "L1",
                "is_noise": False,
            })
        except Exception as exc:  # noqa: BLE001
            row_errors += 1
            shown = title or "(제목 없음)"
            print(f"[fsc] 입법예고 행 건너뜀: {shown} — {exc}")
            _excluded_log.skip(source=SOURCE_NAME, reason="collect:row_parse_error",
                               title=f"{shown} — {exc}", url=url)
    return items, rows_seen, row_errors, oldest


def _fetch_notices(max_pages: int) -> tuple[list[dict], list[str]]:
    """입법예고/규정변경예고(notice). (항목, 부분 실패 사유) — 목록 행을 하나도 못 읽으면 예외."""
    cutoff = datetime.now(_KST).date() - timedelta(days=COLLECT_WINDOW_DAYS)
    items: list[dict] = []
    page_errors: list[str] = []
    rows_seen = row_errors = 0
    for page in range(1, max_pages + 1):
        if page > 1:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            got, seen, errs, oldest = fetch_notice_page(page, cutoff=cutoff)
        except Exception as exc:  # noqa: BLE001
            print(f"[fsc] 입법예고 page={page} 수집 실패: {exc}")
            page_errors.append(f"page={page}: {exc}")
            break  # 다음 페이지가 기간 안인지 알 수 없다 — 읽은 데까지만
        items.extend(got)
        rows_seen += seen
        row_errors += errs
        if oldest is None or oldest < cutoff:
            break
    if rows_seen == 0:
        detail = "; ".join(page_errors) or (f"행 {row_errors}개 전부 해석 실패" if row_errors else "")
        raise RuntimeError("입법예고 목록 행 0개 — 전 페이지 실패 또는 페이지 구조 변경·차단 의심"
                           + (f" ({detail})" if detail else ""))
    reasons = list(page_errors)
    if row_errors:
        reasons.append(f"행 {row_errors}개 해석 실패(건너뜀, EXCLUDED_LOG collect:row_parse_error)")
    return items, reasons


# 부분 실패를 따로 세는 하위 수집(main.SUB_SOURCES["fsc"]와 같아야 한다).
TRACKED_PARTS = ("list", "notice")


def part_enabled(part: str) -> bool:
    """data/source_toggles.yml에서 `fsc_{part}`를 enabled: false로 두면 그 하위 수집만 끈다
    (2026-11-14, notice용 — 코드 수정 없이 한 줄로 끄기)."""
    return f"fsc_{part}" not in DISABLED_SOURCES


def part_of(item: dict) -> str:
    """부분 폴백용(main.SUB_SOURCES["fsc"]) — 보도자료 목록(list) / 입법예고(notice)."""
    url = (item.get("urls") or {}).get("official") or ""
    return "notice" if "/po040301/" in url else "list"


def fetch(*, max_pages: int = 1, notice_max_pages: int = NOTICE_MAX_PAGES) -> list[dict]:
    """A4/C2: 금융위원회 보도자료(list) + 입법예고/규정변경예고(notice, 2026-11-14 추가).

    2026-10-01: 관련 항목이 없어 0건인 건 정상(main.ALLOW_EMPTY_SOURCES). 대신
    모든 페이지가 실패했거나 목록 행을 하나도 못 읽었으면 그 하위 수집은 실패다.

    2026-11-13: 행 수는 날짜 해석이 성공한 행만 센다(위 fetch_page). 페이지 실패나 행 해석
    실패가 있으면 `PartialFetch(failed={부분: …})`로 올려 source_health·메일에 남기고,
    main이 전일 캐시에서 이번에 없는 항목만 채운다(fss B2/B3 10/14 방식).
    2026-11-14: 하위 수집이 둘이 됐다. 둘 다 실패하면 일반 예외(소스 단위 폴백).
    """
    out: list[dict] = []
    failed: dict[str, str] = {}
    for part, fn in (("list", lambda: _fetch_list(max_pages)),
                     ("notice", lambda: _fetch_notices(notice_max_pages))):
        if not part_enabled(part):
            print(f"[fsc] {part}: data/source_toggles.yml에서 꺼짐(fsc_{part}) — 건너뜀")
            continue
        if part == "notice":
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            got, reasons = fn()
        except Exception as exc:  # noqa: BLE001
            print(f"[fsc] {part} 수집 실패: {exc}")
            failed[part] = str(exc)
            continue
        out.extend(got)
        if reasons:
            failed[part] = " / ".join(reasons)
            print(f"[fsc] {part} 부분 실패: {failed[part]}")
    if len(failed) == sum(map(part_enabled, TRACKED_PARTS)) and not out:
        raise RuntimeError(" / ".join(f"{p}: {r}" for p, r in failed.items()))
    if failed:
        raise PartialFetch(out, failed, part_of)
    return out

if __name__ == "__main__":
    print("=== FSC probe ===")
    print(probe())

    print("\n=== A4/C2: 금융위원회 보도자료(카테고리 매칭분만, 5페이지) ===")
    items = fetch()
    for it in items[:15]:
        att = f" | 첨부 {len(it['attachments'])}개" if it["attachments"] else ""
        print(f"  [{it['category']:5s}] [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:45]}{att}")
    print(f"  총 {len(items)}건")
