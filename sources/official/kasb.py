# -*- coding: utf-8 -*-
"""한국회계기준원(kasb.or.kr) 수집기 — A1(소식) / A3(질의회신요약). (A2는 아래 참고, fetch()에서 제외)

docs/SOURCE_PROBE.md §A 조사 결과에 기반한다.

- A1(comm010List.do)의 카테고리는 "공지사항"/"회계기준소식"/"지속가능성기준소식" 3종이
  섞여 있다. "공지사항"은 본인 인증 서비스 점검 안내처럼 규제·기준과 무관한 운영성
  공지라 **수집 단계에서 제외한다**(사용자 지시 2026-08-26).
- 상세 페이지(comm010View.do?seq=)는 본문이 HTML에 그대로 노출되므로 시행일/기한
  텍스트를 `_utils.extract_effective_date()`로 시도한다(A3는 성격상 시도하지 않음).
- 첨부파일 다운로드 링크는 `javascript:fileDownload(...)` 형태라 목록 HTML만으로는
  실제 URL을 구성할 수 없다. attachments는 채우지 않는다(사용자 지시 2026-08-26 —
  추적하지 않기로 함. FSS와 달리 평문 href가 아니라서 추적하려면 별도 JS 분석이 필요).
- A2(기준서 목록)는 실측 결과 (1) 날짜 없는 정적 카탈로그이고 (2) 애초에 K-IFRS가
  아니라 "일반기업회계기준"이라 fetch()에서 뺐다 — `fetch_standards()` 함수 docstring 참고.
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _http
from .._utils import (
    classify,
    doc_type_of,
    extract_effective_date,
    is_admin_noise,
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

SLEEP_BETWEEN_REQUESTS = 1.0  # SPEC §4-6: 공식 사이트는 뉴스보다 여유 있게
_KST = timezone(timedelta(hours=9))

# comm010 게시판의 카테고리 텍스트 → 우리 category key. 여기 없는 값은 classify(title)로 대체 판정.
_NOTICE_CATEGORY_MAP = {
    "회계기준소식": "kifrs",
    "지속가능성기준소식": "esg",
}
_EXCLUDED_NOTICE_CATEGORIES = {"공지사항"}  # 운영성 공지 — 사용자 지시로 제외


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


def _build_item(*, category: str, title: str, url: str, published_at: str | None,
                 doc_type: str, effective_date: str | None, tier: int, trust_score: int,
                 source_name: str) -> dict:
    kw = keyword_score(title, category) if category in ("kifrs", "esg") else 0
    rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
    return {
        "id": make_id_exact(url),  # comm010View.do?seq=/앵커(#seq)처럼 쿼리·프래그먼트가 식별자라 make_id()는 못 씀
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
        "attachments": None,  # TODO: fileDownload() JS 엔드포인트 특정 필요(위 모듈 docstring 참고)
        "layer": "L1",        # SPEC-ADDENDUM.md §1: L1은 노이즈 필터 면제, 상한 미적용
        "is_noise": False,
    }


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _fetch_detail_body_text(seq: str) -> str:
    resp = _http.get(NOTICE_VIEW_URL, params={"seq": seq})
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
        if is_admin_noise(title):  # ADDENDUM-4 §1: 인사·조직·운영 공지 제외(tier 무관)
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
        if is_admin_noise(title):  # ADDENDUM-4 §1
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
    """A1+A3. A2(fetch_standards)는 제외 — 위 fetch_standards() docstring 참고.
    소스 한 종류가 실패해도 나머지는 계속 진행한다(SPEC §9-4).
    """
    out: list[dict] = []
    for name, fn in (("notices", lambda: fetch_notices(fetch_detail=fetch_detail)),
                      ("qna", fetch_qna)):
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
