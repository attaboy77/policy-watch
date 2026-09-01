# -*- coding: utf-8 -*-
"""한국회계기준원(kasb.or.kr) 수집기 — A1(소식) / A3(질의회신요약) / C(주요일정) /
D(제개정현황). (A2는 아래 참고, fetch()에서 제외)

docs/SOURCE_PROBE.md §A 조사 결과에 기반한다.

- A1(comm010List.do)의 카테고리는 "공지사항"/"회계기준소식"/"지속가능성기준소식" 3종이
  섞여 있다. "공지사항"은 본인 인증 서비스 점검 안내처럼 규제·기준과 무관한 운영성
  공지라 **수집 단계에서 제외한다**(사용자 지시 2026-08-26).
- 상세 페이지(comm010View.do?seq=)는 본문이 HTML에 그대로 노출되므로 시행일/기한
  텍스트를 `_utils.extract_effective_date()`로 시도한다(A3는 성격상 시도하지 않음).
- 첨부파일 다운로드 링크는 `javascript:fileDownload(...)` 형태라 목록 HTML만으로는
  실제 URL을 구성할 수 없다. A1/A3/C는 attachments를 채우지 않는다(사용자 지시
  2026-08-26 — 추적하지 않기로 함. FSS와 달리 평문 href가 아니라서 추적하려면
  별도 JS 분석이 필요). D(제개정현황)는 파일명만이라도 넘긴다 — `fetch_revisions()` 참고.
- A2(기준서 목록)는 실측 결과 (1) 날짜 없는 정적 카탈로그이고 (2) 애초에 K-IFRS가
  아니라 "일반기업회계기준"이라 fetch()에서 뺐다 — `fetch_standards()` 함수 docstring 참고.
- C(calListA.do, "회계기준 주요일정")는 위원회 회의·세미나 등을 진행일자 기준으로
  나열하는 캘린더 게시판(2026-08-31 사용자 지시로 추가). 2019년부터 누적된
  ~1,100건짜리 아카이브라 서버 사이드 날짜필터(`s_date_start`/`s_date_end`) 없이
  훑으면 안 된다 — `fetch_schedule()` 참고.
- D(List2006.do, "회계기준연혁 > 제개정현황")는 K-IFRS/일반기업회계기준 등 기준서
  제·개정 이력과 **시행일이 직접 실려 있는** 표(2026-08-31 사용자 지시로 추가).
  연도/적용기준 드롭다운은 전부 클라이언트 사이드 JS(`applyFilters()`)로 행을
  숨기는 방식이라 서버는 항상 전체 73건(2026-08-31 기준)을 한 번에 내려준다 —
  페이지네이션도 없다(실측 확인). `fetch_revisions()` 참고.
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _gap_log, _http
from .._config import COLLECT_WINDOW_DAYS
from .._utils import (
    classify,
    doc_type_of,
    extract_effective_date,
    is_event_announcement,
    keyword_score,
    matched_keywords,
    make_id_exact,
    final_score,
    recency_score,
    trust_of,
)

BASE = "https://www.kasb.or.kr"
NOTICE_LIST_URL = f"{BASE}/front/board/comm010List.do"
NOTICE_VIEW_URL = f"{BASE}/front/board/comm010View.do"
QNA_LIST_URL = f"{BASE}/front/board/allReplySummaryList.do"
STANDARD_LIST_URLS = [f"{BASE}/front/board/List300{n}.do" for n in range(3, 9)]  # List3003~List3008
# calListA.do(=bu=A, "회계기준" 메뉴 하위)를 쓴다(2026-08-31 사용자 지시).
# 실측 확인: calList.do(접미사 없음)·calListB.do와 행 데이터가 완전히 동일한
# 게시판이다 — bu 파라미터는 메뉴 하이라이트에만 쓰이고 실제 목록 필터링에는
# 영향이 없다. 상세 페이지 액션도 calViewA.do로 페어를 맞춘다.
CALENDAR_LIST_URL = f"{BASE}/front/board/calListA.do"
CALENDAR_VIEW_URL = f"{BASE}/front/board/calViewA.do"
# D: 회계기준연혁 > 제개정현황(2026-08-31 사용자 지시로 추가). 실측 확인: 연도/
# 적용기준 드롭다운은 전부 클라이언트 JS(`applyFilters()`, 서버 요청 없이
# `<tr>`을 style="display:none"으로 숨기는 방식)이므로 쿼리 파라미터 없이 그냥
# GET 한 번이면 전체 행(73건, 2026-08-31 기준)이 다 온다 — 페이지네이션 없음.
REVISION_LIST_URL = f"{BASE}/front/board/List2006.do"
# E: KSSB(지속가능성기준) 공시기준서 "자발적용가능" 목록(2026-09-02 사용자
# 지시로 추가). sstnb_stndrList.do는 "시행중"(A)/"자발적용가능"(B) 탭 2개짜리
# 게시판 — <form id="frm" method="GET">의 hidden input #tab 기본값이 "A"라
# 쿼리 없이 GET하면 A(시행중) 결과(현재는 빈 목록)만 온다. 실측 확인: B탭은
# `?tab=B&siteCd=002000000000000&bu=B`를 붙여야 자발적용가능 목록(현재 KSSB
# 제1호/제2호 2건)이 온다. 상세 페이지(View3012.do)는 `fn_Detail(gubun,
# accstdSeq)`가 넘기는 두 파라미터로 접근하며, "최종제(개)정일" 필드가
# 곧 의결일(제정 의결·공표가 같은 날)이다 — 시행일 필드 자체가 없다(사용자가
# 미리 알려준 대로: "의결일자는 있는데 시행일자가 없음").
KSSB_STANDARD_LIST_URL = f"{BASE}/front/board/sstnb_stndrList.do"
KSSB_STANDARD_VIEW_URL = f"{BASE}/front/board/View3012.do"

SLEEP_BETWEEN_REQUESTS = 1.0  # SPEC §4-6: 공식 사이트는 뉴스보다 여유 있게
_KST = timezone(timedelta(hours=9))

# comm010 게시판의 카테고리 텍스트 → 우리 category key. 여기 없는 값은 classify(title)로 대체 판정.
_NOTICE_CATEGORY_MAP = {
    "회계기준소식": "kifrs",
    "지속가능성기준소식": "esg",
}
_EXCLUDED_NOTICE_CATEGORIES = {"공지사항"}  # 운영성 공지 — 사용자 지시로 제외

# calListA.do 중분류(<p class="cata03_..">) → 우리 category key. 실측 결과 KASB는
# 회계기준·지속가능성기준 두 위원회만 운영하고(icfr/tax는 각각 FSS/NTS 소관이라
# 이 게시판에 안 나옴), 나머지 중분류("세미나"/"포럼" 등 공통 행사)는 매핑에
# 없으면 스킵한다 — A1과 달리 classify(title)로 대체 판정하지 않는다. 위원회
# 회의가 아닌 행사 안내를 "혹시나" 우리 카테고리로 잘못 편입시키는 게 더 위험하다
# 판단(§9-2류 과다 추정 방지 원칙의 반대 방향 — 여기선 과다 포함이 위험).
_CALENDAR_CATEGORY_MAP = {
    "회계기준위원회": "kifrs",
    "지속가능성기준위원회": "esg",
}
CALENDAR_FORWARD_DAYS = 90  # 과거뿐 아니라 예정된 회의도 보여준다(조기 경보 가치, ADDENDUM-6 §3 근거와 동일한 논리)

# List2006.do "적용기준" 열 텍스트. 이 값과 정확히 일치하는 행만 수집한다
# (일반기업회계기준·특수분야회계기준 등은 제외 — 사용자 지시: "우리는 K-IFRS 적용 대상").
_REVISION_APPLICABLE_STANDARD = "한국채택국제회계기준"
# "2025년  11월  21일"(공백 불규칙)·"2027년 01월 01일" 둘 다 처리.
_KOREAN_DATE_RE = re.compile(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일")


def probe() -> dict:
    """A1/A3 목록 페이지에 실제로 접근해 상태를 확인한다(개발용 진단 함수)."""
    try:
        resp = _http.get(NOTICE_LIST_URL)
        ok = resp.status_code == 200 and "board_date" in resp.text
        return {"ok": ok, "method": "html", "note": f"comm010List.do HTTP {resp.status_code}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _build_item(*, category: str, title: str, url: str | None, published_at: str | None,
                 doc_type: str, effective_date: str | None, tier: int, trust_score: int,
                 source_name: str, is_meeting_schedule: bool = False,
                 id_source: str | None = None, attachments: list[dict] | None = None) -> dict:
    kw = keyword_score(title, category) if category in ("kifrs", "esg") else 0
    rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
    return {
        # comm010View.do?seq=/앵커(#seq)처럼 쿼리·프래그먼트가 식별자라 make_id()는 못 씀.
        # id_source가 오면 그걸로 id를 만든다 — List2006.do(제개정현황)는 서로 다른
        # 여러 행이 같은 보도자료 URL(seq)을 공유하는 걸 실측 확인해서, url만으로
        # id를 만들면 dedupe()에서 서로 다른 기준서 개정 항목이 하나로 뭉개진다
        # (fetch_revisions() 참고).
        "id": make_id_exact(id_source if id_source is not None else (url or "")),
        "category": category,
        "doc_type": doc_type,
        "title": title,
        "summary": [],       # Phase 4(_summarize.py)에서 채움
        "impact": None,      # Phase 4에서 채움
        "published_at": published_at,
        "collected_at": _now_kst_iso(),
        "effective_date": effective_date,
        "source": {"name": source_name, "domain": "kasb.or.kr", "tier": tier, "type": "official"},
        "trust_score": trust_score,
        "keyword_score": kw,
        "final_score": final_score(trust_score, kw, rec),
        "matched_keywords": matched_keywords(title, category) if category in ("kifrs", "esg") else [],
        "urls": {"news": None, "official": url},
        "law_meta": None,
        # TODO: A1/A3/C는 fileDownload() JS 엔드포인트 특정 필요해 늘 None이었으나
        # List2006.do(제개정현황)는 파일명만이라도 넘겨준다(실제 다운로드 URL은
        # 여전히 못 만듦 — url=None으로 채움, fetch_revisions() 참고).
        "attachments": attachments,
        "layer": "L1",        # SPEC-ADDENDUM.md §1: L1은 노이즈 필터 면제, 상한 미적용
        "is_noise": False,
        # 2026-08-31 사용자 지시: effective_date가 "시행일"이 아니라 위원회
        # "회의 진행일자"인 항목(fetch_schedule() 전용) 표시 — _summarize.py가
        # "~부터 적용" 대신 "~ 위원회 회의 예정" 문구를 쓰게 하고, 캘린더가
        # 회의 일정과 실제 시행일을 구분해 보여주는 데 쓴다.
        "is_meeting_schedule": is_meeting_schedule,
    }


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _fetch_detail_body_text(seq: str, *, base_url: str = NOTICE_VIEW_URL) -> str:
    """상세 페이지 본문 텍스트. calViewA.do도 comm010View.do와 같은 클래스
    (.board_view_cont)를 쓰므로 `base_url`만 바꿔 재사용한다(fetch_schedule() 참고)."""
    resp = _http.get(base_url, params={"seq": seq})
    soup = BeautifulSoup(resp.text, "html.parser")
    cont = soup.select_one(".board_view_cont")
    return cont.get_text(" ", strip=True) if cont else ""


def fetch_notices(*, fetch_detail: bool = True, max_detail_fetches: int = 30) -> list[dict]:
    """A1: 공지사항/소식 게시판. "공지사항" 카테고리는 제외하고 반환한다."""
    resp = _http.get(NOTICE_LIST_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []
    detail_fetches = 0

    for row in soup.select("table tbody tr"):
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        cat_text = cells[1].get_text(strip=True)
        if cat_text in _EXCLUDED_NOTICE_CATEGORIES:
            continue
        link = cells[2].find("a")
        if link is None:
            continue
        title = link.get_text(strip=True)
        m = re.search(r"fn_Detail\('(\d+)'\)", link.get("onclick", ""))
        if not title or not m:
            continue
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4: 인사·조직·운영 공지 + 행사/포럼 안내 제외(tier 무관)
            continue
        seq = m.group(1)
        date_p = row.select_one(".board_date")
        published_at = date_p.get_text(strip=True) if date_p else None

        category = _NOTICE_CATEGORY_MAP.get(cat_text) or classify(title)
        if category not in ("kifrs", "esg"):
            continue  # 매핑도 안 되고 키워드로도 못 걸리면 스킵(잘못된 카테고리 태깅 방지)

        url = f"{NOTICE_VIEW_URL}?seq={seq}"
        effective_date = None
        if fetch_detail and detail_fetches < max_detail_fetches:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
            try:
                body_text = _fetch_detail_body_text(seq)
                effective_date = extract_effective_date(body_text)
            except Exception as exc:  # noqa: BLE001 - 상세 조회 실패해도 목록 항목은 살린다
                print(f"[kasb] seq={seq} 상세 조회 실패: {exc}")
            detail_fetches += 1

        tier, trust_score, source_name = trust_of(url)
        doc_type = doc_type_of(title, tier)
        items.append(_build_item(
            category=category, title=title, url=url, published_at=published_at,
            doc_type=doc_type, effective_date=effective_date,
            tier=tier, trust_score=trust_score, source_name=source_name,
        ))
    return items


def fetch_schedule(*, fetch_detail: bool = True, max_detail_fetches: int = 20,
                    max_pages: int = 5) -> list[dict]:
    """C: 회계기준 주요일정(calListA.do) — 위원회 회의·세미나 등 진행일자 기준
    캘린더(2026-08-31 사용자 지시로 추가).

    `s_date_start`/`s_date_end`(YYYY-MM-DD)로 서버 사이드 날짜필터를 건다 —
    COLLECT_WINDOW_DAYS(과거) ~ CALENDAR_FORWARD_DAYS(미래) 범위. 이 게시판은
    2019년부터 누적된 ~1,100건짜리 아카이브라 필터 없이 훑으면 안 된다(실측
    확인, 총 110페이지). `page` 쿼리 파라미터로 페이지네이션(실측 확인).

    _CALENDAR_CATEGORY_MAP에 없는 중분류(세미나·포럼 등 공통 행사)는 스킵한다
    (A1과 달리 classify(title)로 대체 판정하지 않음 — 위원회 회의가 아닌 행사를
    우리 카테고리로 잘못 편입시키는 게 더 위험하다고 판단). "일반기업회계기준"이
    일정명에 들어간 건 명시적으로 제외한다(2026-08-31 사용자 지시 — "우리는
    K-IFRS 적용 대상") — ADDENDUM-6 §1 APPLICABILITY.smb_only가 이미 걸러주지만,
    이 소스에서 바로 눈에 보이게 한 번 더 막는다.

    effective_date: 상세 페이지 본문에서 `extract_effective_date()`를 먼저
    시도한다(안건 목록 텍스트라 대개 실패해도 정상 — A1과 같은 패턴). 못 찾았고
    진행일자가 미래면 진행일자 자체를 effective_date로 채운다(2026-08-31
    사용자 지시 — "우측 캘린더가 비어 있는데 이걸로 채울 수 있다"). 회의
    진행일자가 엄밀히는 "시행일"이 아니라 "논의일"이지만, 예정된 위원회 안건을
    미리 보여주는 조기 경보 용도로 schedules[]에 태운다. 과거 진행일자는 채우지
    않는다 — 지난 회의를 "일정"으로 보여줄 이유가 없다.
    """
    today = date.today()
    start = today - timedelta(days=COLLECT_WINDOW_DAYS)
    end = today + timedelta(days=CALENDAR_FORWARD_DAYS)

    items: list[dict] = []
    detail_fetches = 0
    for page in range(1, max_pages + 1):
        if page > 1:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        resp = _http.get(CALENDAR_LIST_URL, params={
            "s_date_start": start.isoformat(), "s_date_end": end.isoformat(), "page": page,
        })
        soup = BeautifulSoup(resp.text, "html.parser")
        rows = soup.select(".cal_board table tbody tr")
        if not rows:
            break

        for row in rows:
            cells = row.find_all("td")
            if len(cells) < 5:
                continue
            published_at = cells[0].get_text(strip=True) or None
            minor_p = cells[2].select_one("p")
            minor = minor_p.get_text(strip=True) if minor_p else ""
            category = _CALENDAR_CATEGORY_MAP.get(minor)
            if category is None:
                continue  # 세미나/포럼 등 위원회 회의가 아닌 공통 행사는 스킵
            link = cells[3].find("a")
            title = link.get_text(strip=True) if link else ""
            m = re.search(r"fn_Detail\('(\d+)'\)", link.get("onclick", "") if link else "")
            if not title or not m or not published_at:
                continue
            if "일반기업회계기준" in title:  # 2026-08-31 사용자 지시: K-IFRS 대상 아님
                continue
            if is_event_announcement(title):  # 세미나·포럼 등 제목 기반 보강 필터
                continue

            seq = m.group(1)
            url = f"{CALENDAR_VIEW_URL}?seq={seq}"
            effective_date = None
            if fetch_detail and detail_fetches < max_detail_fetches:
                time.sleep(SLEEP_BETWEEN_REQUESTS)
                try:
                    body_text = _fetch_detail_body_text(seq, base_url=CALENDAR_VIEW_URL)
                except Exception as exc:  # noqa: BLE001
                    print(f"[kasb] calendar seq={seq} 상세 조회 실패: {exc}")
                else:
                    effective_date = extract_effective_date(body_text)
                detail_fetches += 1
            if effective_date is None:
                try:
                    if _parse_iso_date(published_at) > today:
                        effective_date = published_at  # 2026-08-31: 미래 일정→schedules 노출
                except ValueError:
                    pass

            tier, trust_score, source_name = trust_of(url)
            doc_type = doc_type_of(title, tier)
            items.append(_build_item(
                category=category, title=title, url=url, published_at=published_at,
                doc_type=doc_type, effective_date=effective_date,
                tier=tier, trust_score=trust_score, source_name=source_name,
                is_meeting_schedule=True,
            ))

        if len(rows) < 10:  # 페이지당 10건 — 덜 찼으면 마지막 페이지
            break
    return items


def _parse_korean_date(text: str) -> str | None:
    """"2025년  11월  21일" 같은 표기를 "2025-11-21"로. 못 찾으면 None."""
    m = _KOREAN_DATE_RE.search(text or "")
    if not m:
        return None
    y, mo, d = (int(g) for g in m.groups())
    return f"{y:04d}-{mo:02d}-{d:02d}"


def fetch_revisions() -> list[dict]:
    """D: 회계기준연혁 > 제개정현황(List2006.do, 2026-08-31 사용자 지시로 추가).

    "적용기준" 열이 정확히 "한국채택국제회계기준"인 행만 수집한다(일반기업회계기준
    등은 제외 — 사용자 지시). 제목은 "{의결연도}년 {제개정명} (관련기준서)" 형태로
    합친다(관련기준서가 제개정명과 완전히 같으면 괄호는 생략).

    **의결연도를 반드시 앞에 붙인다** — 처음엔 "제개정명 (관련기준서)"만
    썼다가 실측에서 심각한 문제를 발견했다: K-IFRS 제1117호 보험계약은
    2018/2021/2025년에 각각 별개로 제·개정됐는데(시행일 2021-01-01·
    2023-01-01·2025-12-31, 전부 다름) 세 행 모두 "제1117호 보험계약"이라는
    **똑같은 제목**이 나온다(관련기준서 열도 제개정명과 동일해서 괄호를 안
    붙이면 구분이 안 됨). `_utils.dedupe()`는 제목 완전일치도 그룹 키로 쓰므로
    의결연도 없이는 세 건 중 두 건이 조용히 사라진다 — 실측으로 확인 후 수정.

    effective_date(시행일)가 이 소스의 핵심 값이다 — 못 뽑으면(실측상 거의
    안 그렇지만) `_gap_log`에 기록해 수동 검토 대상으로 남긴다. 과거/미래 구분
    없이 채운다 — `build_schedules()`가 effective_date 있는 항목을 전부
    schedules[]로 만들고 상태(status)로 지난 일정과 예정 일정을 이미 구분하므로,
    여기서 미래 항목만 따로 골라낼 필요가 없다(calListA.do의 회의 일정과 달리
    이 소스의 effective_date는 처음부터 "진짜 시행일"이라 `is_meeting_schedule`을
    세우지 않는다 — 캘린더에서 꽉 찬 점=시행일로 표시됨).

    id는 "보도자료" 링크(seq)만으로 만들지 않는다 — 실측 확인 결과 서로 다른
    여러 제·개정 항목이 같은 seq(같은 보도자료 게시물)를 공유해서, url 기반
    id를 쓰면 dedupe()에서 서로 다른 기준서 개정이 하나로 뭉개진다. 대신
    제개정명+의결일+시행일 원문 텍스트로 id를 만든다.

    첨부파일은 `javascript:fileDownload(...)`라 실제 다운로드 URL은 여전히 못
    만들지만(다른 kasb.py 게시판과 같은 한계), 파일명만은 목록 HTML의 <span>
    에서 바로 뽑을 수 있어 attachments에 name만 채우고 url=None으로 둔다.
    """
    resp = _http.get(REVISION_LIST_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    tier, trust_score, source_name = trust_of(REVISION_LIST_URL)

    items: list[dict] = []
    for row in soup.select("tr[name='rowItem']"):
        cells = row.find_all("td")
        if len(cells) < 9:
            continue
        standard = cells[2].get_text(strip=True)
        if standard != _REVISION_APPLICABLE_STANDARD:
            continue  # 일반기업회계기준 등 K-IFRS가 아니면 제외(사용자 지시)

        name = cells[3].get_text(strip=True)
        if not name:
            continue
        dec_year = cells[0].get_text(strip=True)  # 의결연도 — 제목 유일성 확보용(위 docstring 참고)
        related = ", ".join(cells[6].stripped_strings)
        base = f"{name} ({related})" if related and related != name else name
        title = f"{dec_year}년 {base}" if dec_year else base

        decided_raw = cells[4].get_text(strip=True)
        effective_raw = cells[5].get_text(strip=True)
        published_at = _parse_korean_date(decided_raw)
        effective_date = _parse_korean_date(effective_raw)
        if not effective_date:
            _gap_log.record(source="한국회계기준원(제개정현황)", category="kifrs",
                             title=title, url=REVISION_LIST_URL,
                             note=f"시행일 텍스트 파싱 실패(원문: {effective_raw!r}) — 수동 확인 필요")

        link = cells[7].find("a")
        url = link.get("href") if link and link.get("href") else None

        attachments = [
            {"name": span.get_text(strip=True), "url": None}
            for span in cells[8].select("li.down_hwp a span")
            if span.get_text(strip=True)
        ] or None

        id_source = f"list2006:{name}:{decided_raw}:{effective_raw}"
        items.append(_build_item(
            category="kifrs", title=title, url=url, published_at=published_at,
            doc_type="제·개정",  # 분류(제정/개정) 둘 다 이 프로젝트의 doc_type enum에서는 "제·개정" 하나
            effective_date=effective_date,
            tier=tier, trust_score=trust_score, source_name=source_name,
            id_source=id_source, attachments=attachments,
        ))
    return items


_KSSB_DETAIL_LINK_RE = re.compile(r"fn_Detail\('(\d+)'\s*,\s*'(\d+)'\)")


def fetch_kssb_voluntary_standards() -> list[dict]:
    """E: KSSB 공시기준서 "자발적용가능" 목록(sstnb_stndrList.do, 2026-09-02
    사용자 지시로 추가). B탭(자발적용가능)만 수집한다 — A탭(시행중)은 실측
    결과 아직 빈 목록이다(어떤 KSSB 기준서도 시행일이 확정되지 않았다는 뜻).

    목록 행의 `fn_Detail(gubun, accstdSeq)`에서 상세 페이지(View3012.do) 접근에
    필요한 두 파라미터를 뽑고, 상세 페이지의 "최종제(개)정일"을 published_at으로
    쓴다(제정 의결과 공표가 같은 날 — "최종 공표일"과 항상 동일해 published_at
    하나로 충분). **시행일자는 없다** — 상세 페이지 자체에 그 필드가 없어
    effective_date는 항상 None으로 둔다(_gap_log에도 안 남긴다 — 다른 소스의
    "파싱 실패"와 달리 애초에 없는 값이라 수동 확인 대상이 아니다).
    """
    resp = _http.get(KSSB_STANDARD_LIST_URL, params={
        "tab": "B", "siteCd": "002000000000000", "bu": "B",
    })
    soup = BeautifulSoup(resp.text, "html.parser")
    tier, trust_score, source_name = trust_of(KSSB_STANDARD_LIST_URL)

    items: list[dict] = []
    rows = soup.select("table tbody tr")
    for i, row in enumerate(rows):
        link = row.select_one("td.left a")
        if link is None:
            continue
        title = link.get_text(strip=True)
        m = _KSSB_DETAIL_LINK_RE.search(link.get("onclick", ""))
        if not title or not m:
            continue
        gubun, accstd_seq = m.group(1), m.group(2)
        url = f"{KSSB_STANDARD_VIEW_URL}?siteCd=002000000000000&gubun={gubun}&accstdSeq={accstd_seq}"

        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            detail_resp = _http.get(url)
        except Exception as exc:  # noqa: BLE001 - 상세 하나 실패해도 나머지는 계속(SPEC §9-4)
            print(f"[kasb] KSSB 자발적용 상세 조회 실패({title}): {exc}")
            continue
        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")

        published_at = None
        for th in detail_soup.select("table th"):
            if th.get_text(strip=True) == "최종제(개)정일":
                td = th.find_next_sibling("td")
                date_el = td.select_one(".board_date") if td else None
                text = (date_el or td).get_text(strip=True) if td else None
                if text and re.match(r"^\d{4}-\d{2}-\d{2}$", text):
                    published_at = text
                break

        attachments = [
            {"name": a.get_text(strip=True), "url": None}
            for a in detail_soup.select(".board_view_file_wrap a[onclick*='fileDownload']")
            if a.get_text(strip=True)
        ] or None

        items.append(_build_item(
            category="esg", title=title, url=url, published_at=published_at,
            doc_type="자발적용", effective_date=None,
            tier=tier, trust_score=trust_score, source_name=source_name,
            attachments=attachments,
        ))
    return items


def fetch_standards() -> list[dict]:
    """A2: List3003~List3008 게시판. **fetch()에서 제외됨 — 아래 참고.**

    2026-08-26 실측 재확인 결과 두 가지 문제로 대시보드에 부적합하다고 판단해 뺐다.
    1) 76건이 매 실행마다 항상 같다 — 날짜 컬럼 자체가 없는 정적 목록(카탈로그)이라
       "최근 90일 내 변경"을 가려낼 수단이 없다. 대시보드 취지("새로 바뀐 것 파악")와
       안 맞고, 오히려 A1(소식)의 실제 변경 항목을 76건 속에 묻어버린다.
    2) **애초에 K-IFRS가 아니다.** 실제 제목("제01장 목적, 구성 및 적용", "제19호 리스",
       "제5001호 결합재무제표" 등)은 "일반기업회계기준"(비상장 중소기업용 K-GAAP)의
       장·호 번호 체계다. K-IFRS 기준서는 "K-IFRS 제1116호"처럼 1000번대로 불리는데
       이 목록에는 한 건도 없다. SPEC-ADDENDUM.md §2-A2가 기대한 "K-IFRS 기준서 목록"이
       아니라 다른 회계기준 세트를 잘못 짚은 것으로 보인다.

    K-IFRS 제·개정 소식은 A1(comm010, category="회계기준소식")이 이미 커버한다
    (실측: "IASB 공개초안 '위험경감회계'" 등 K-IFRS/IASB 관련 항목 확인됨) — 그쪽이
    날짜도 있고 본문도 있어 훨씬 쓸모있는 소스다. 이 함수는 향후(진짜 K-IFRS 기준서
    목록 게시판을 찾으면) 재사용할 수 있도록 코드만 남겨둔다. `python -m
    sources.official.kasb --standards`로 직접 호출은 가능하다.
    """
    items: list[dict] = []
    for i, url in enumerate(STANDARD_LIST_URLS):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            resp = _http.get(url)
        except Exception as exc:  # noqa: BLE001 - 게시판 하나 실패해도 나머지는 계속
            print(f"[kasb] {url} 수집 실패: {exc}")
            continue
        soup = BeautifulSoup(resp.text, "html.parser")
        for row in soup.select("table tbody tr"):
            link = row.select_one("td.left a")
            if link is None:
                continue
            title = link.get_text(strip=True)
            m = re.search(r"fn_Detail\('(\d+)'", link.get("onclick", ""))
            if not title or not m:
                continue
            seq = m.group(1)
            item_url = f"{url}#{seq}"  # A2는 상세 URL 패턴 미확정(SOURCE_PROBE.md A2 참고) — 목록 페이지+앵커로 대체
            tier, trust_score, source_name = trust_of(item_url)
            items.append(_build_item(
                category="kifrs", title=title, url=item_url, published_at=None,
                doc_type="제·개정", effective_date=None,
                tier=tier, trust_score=trust_score, source_name=source_name,
            ))
    return items


def fetch_qna() -> list[dict]:
    """A3: 질의회신요약. doc_type을 게시판 단위로 '질의회신' 고정한다.

    상단에 날짜 없이 고정된 항목들은 실측 결과 "일반기업회계기준 질의회신 비교표"
    계열(A2와 같은 이유로 K-IFRS 대상 밖 — 우리 대상은 K-IFRS)이라 제외한다.
    날짜 있는 항목은 실제로 K-IFRS 관련("K-IFRS 제1118호 정착지원 TF" 등, 1000번대
    확인됨)이라 그대로 둔다. 날짜 유무가 곧 "일반기업회계기준 고정자료 여부"와 일치해
    별도 제목 키워드 필터 없이 published_at 유무만으로 걸러도 된다(사용자 지시 2026-08-26).
    """
    resp = _http.get(QNA_LIST_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []
    for row in soup.select("table tbody tr"):
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        link = row.find("a")
        if link is None:
            continue
        title = link.get_text(strip=True)
        m = re.search(r"fn_Detail\('(\d+)'", link.get("onclick", ""))
        if not title or not m:
            continue
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            continue
        seq = m.group(1)
        date_p = row.select_one(".board_date")
        published_at = date_p.get_text(strip=True) if date_p else None
        if not published_at:
            continue  # 날짜 없는 상단 고정 항목 = 일반기업회계기준 계열, 제외
        url = f"{QNA_LIST_URL}#{seq}"  # A3도 상세 URL 패턴 미확정 — 동일하게 앵커로 대체
        tier, trust_score, source_name = trust_of(url)
        items.append(_build_item(
            category="kifrs", title=title, url=url, published_at=published_at,
            doc_type="질의회신", effective_date=None,
            tier=tier, trust_score=trust_score, source_name=source_name,
        ))
    return items


def fetch(*, fetch_detail: bool = True) -> list[dict]:
    """A1+A3+C(주요일정)+D(제개정현황)+E(KSSB 자발적용가능). A2(fetch_standards)는
    제외 — 위 fetch_standards() docstring 참고. 소스 한 종류가 실패해도 나머지는
    계속 진행한다(SPEC §9-4).
    """
    out: list[dict] = []
    for name, fn in (("notices", lambda: fetch_notices(fetch_detail=fetch_detail)),
                      ("qna", fetch_qna),
                      ("schedule", lambda: fetch_schedule(fetch_detail=fetch_detail)),
                      ("revisions", fetch_revisions),
                      ("kssb_voluntary", fetch_kssb_voluntary_standards)):
        try:
            out.extend(fn())
        except Exception as exc:  # noqa: BLE001
            print(f"[kasb] {name} 수집 실패: {exc}")
    return out


if __name__ == "__main__":
    print("=== KASB probe ===")
    print(probe())

    print("\n=== A1: 소식(공지사항 제외) ===")
    notices = fetch_notices(fetch_detail=True, max_detail_fetches=10)
    for it in notices[:10]:
        eff = f" | 시행/기한: {it['effective_date']}" if it["effective_date"] else ""
        print(f"  [{it['category']:5s}] [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:50]}{eff}")
    print(f"  총 {len(notices)}건")

    print("\n=== A2: fetch()에서 제외됨 (정적 카탈로그 + K-IFRS 아님, fetch_standards() docstring 참고) ===")

    print("\n=== A3: 질의회신요약 ===")
    qna = fetch_qna()
    for it in qna[:5]:
        print(f"  [{it['doc_type']}] {it['published_at']} | {it['title'][:50]}")
    print(f"  총 {len(qna)}건")

    print("\n=== C: 회계기준 주요일정(calListA.do) ===")
    schedule = fetch_schedule(fetch_detail=True, max_detail_fetches=10)
    for it in schedule[:10]:
        eff = f" | 시행/기한: {it['effective_date']}" if it["effective_date"] else ""
        print(f"  [{it['category']:5s}] [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:50]}{eff}")
    print(f"  총 {len(schedule)}건")

    print("\n=== D: 제개정현황(List2006.do, K-IFRS만) ===")
    revisions = fetch_revisions()
    for it in revisions[:10]:
        eff = f" | 시행일: {it['effective_date']}" if it["effective_date"] else " | 시행일 파싱 실패"
        print(f"  [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:60]}{eff}")
    print(f"  총 {len(revisions)}건")

    print("\n=== E: KSSB 자발적용가능(sstnb_stndrList.do) ===")
    kssb = fetch_kssb_voluntary_standards()
    for it in kssb:
        print(f"  [{it['doc_type']}] 의결/공표: {it['published_at']} | 시행일: {it['effective_date']} | {it['title']}")
        print(f"    첨부: {it['attachments']}")
    print(f"  총 {len(kssb)}건")
