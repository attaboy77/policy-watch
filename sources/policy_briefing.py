# -*- coding: utf-8 -*-
"""정책브리핑(korea.kr) 통합 보도자료 수집기 — D3.

docs/SOURCE_PROBE.md §D3 "통합 수집기 특이사항" 기반. SPEC-ADDENDUM.md §3이 그린
"기재부·국세청·금융위 3개 부처 단일 파서" 구상과 달리, 실측 결과 이 소스가
실제로 커버하는 건 **국세청 + 금융위원회 전용**으로 확정됐다(사용자 결정 2026-08-26):

- 금융감독원은 정부 부처가 아니라 정책브리핑의 부처 taxonomy 자체에 없다
  (fss.py의 B1/B2로 직접 수집).
- 기획재정부도 이 사이트의 deptCode 체크박스 목록에 없다(구 명칭 "재정경제부"만
  존재) — 실제 기사에 "기획재정부"로 정확히 태깅되는지 표본 내 실증 못 함
  (moef.py로 직접 수집).

**부처 필터는 서버측 파라미터(`deptCode`)가 GET/POST 모두 작동하지 않는다**
(JS/AJAX 기반으로 추정, SOURCE_PROBE.md 확인). 그래서 필터 없이 목록 전체를
가져온 뒤, 각 항목의 `span.source` 두 번째 `<span>` 텍스트(부처명)가 우리 대상
부처와 정확히 일치하는 것만 남기는 사후 필터링 방식을 쓴다.

`urls.official`은 정책브리핑 자체 링크를 쓴다(원 부처 원문 링크를 이 목록만으로는
확정할 수 없음 — SPEC-ADDENDUM.md §3의 "있으면 원 부처, 없으면 정책브리핑" 원칙 중
후자에 해당. 원 부처 링크 매핑은 후속 과제).

세법(tax)으로 분류된 항목(주로 국세청발)의 effective_date는 법제처(D4) 단일
소스 원칙에 따라 시도하지 않는다. 그 외 카테고리(국세청/금융위가 kifrs·icfr·esg
관련 보도자료를 낼 수도 있음 — 예: 금융위 ESG 로드맵)는 본문 요약(`lead`)에서
시도해 본다.
"""
from __future__ import annotations

from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from . import _http
from ._utils import (classify, doc_type_of, extract_effective_date, is_admin_noise,
                     pass_tax_filter, keyword_score, matched_keywords, make_id_exact,
                     final_score, recency_score)

BASE = "https://www.korea.kr"
LIST_URL = f"{BASE}/briefing/pressReleaseList.do"

TARGET_DEPTS = {"국세청", "금융위원회"}  # 확정 범위 — 위 모듈 docstring 참고
_KST = timezone(timedelta(hours=9))


def probe() -> dict:
    try:
        resp = _http.get(LIST_URL)
        ok = resp.status_code == 200 and 'class="source"' in resp.text
        return {"ok": ok, "method": "html", "note": f"pressReleaseList.do HTTP {resp.status_code}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "method": "html", "note": f"요청 실패: {exc}"}


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _parse_dotted_date(s: str) -> str | None:
    parts = s.strip().split(".")
    if len(parts) != 3:
        return None
    try:
        y, mo, d = (int(p) for p in parts)
        return date(y, mo, d).isoformat()
    except ValueError:
        return None


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _build_item(*, category: str, dept: str, title: str, lead: str, url: str,
                 published_at: str | None, doc_type: str) -> dict:
    kw = keyword_score(title, category)
    rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
    effective_date = None
    if category != "tax":  # 세법은 법제처(D4) 단일 소스 — 그 외 카테고리는 본문에서 시도
        effective_date = extract_effective_date(lead)
    return {
        "id": make_id_exact(url),  # pressReleaseView.do?newsId=처럼 쿼리가 식별자
        "category": category,
        "doc_type": doc_type,
        "title": title,
        "summary": [],
        "impact": None,
        "published_at": published_at,
        "collected_at": _now_kst_iso(),
        "effective_date": effective_date,
        "source": {"name": dept, "domain": "korea.kr", "tier": 1, "type": "official"},
        "trust_score": 100,
        "keyword_score": kw,
        "final_score": final_score(100, kw, rec),
        "matched_keywords": matched_keywords(title, category),
        "urls": {"news": None, "official": url},
        "law_meta": None,
        "attachments": None,
        "layer": "L2",  # SPEC-ADDENDUM.md §1: 정책브리핑 경유는 L2(공식 보도자료), L1 아님
        "is_noise": False,
    }


def fetch_page(page_index: int) -> list[dict]:
    resp = _http.get(LIST_URL, params={"pageIndex": page_index})
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []

    for li in soup.select("li"):
        a = li.find("a", href=True)
        source_span = li.select_one("span.source")
        strong = li.find("strong")
        if a is None or source_span is None or strong is None:
            continue
        spans = source_span.find_all("span")
        if len(spans) < 2:
            continue
        published_raw, dept = spans[0].get_text(strip=True), spans[1].get_text(strip=True)
        if dept not in TARGET_DEPTS:
            continue

        title = strong.get_text(strip=True)
        if not title or title in ("선택한 항목", "보도자료"):
            continue
        if is_admin_noise(title):  # ADDENDUM-4 §1: "금융위원회 인사보도(과장급 전보)" 등 제외
            continue
        category = classify(title)
        if category is None:
            continue  # 우리 4개 카테고리와 무관한 보도자료는 버림
        if not pass_tax_filter(category=category, layer="L2", text=title):
            continue  # ADDENDUM-3 §3: L2 정책브리핑은 세목 화이트리스트 적용 대상

        lead_span = li.select_one("span.lead")
        lead = lead_span.get_text(" ", strip=True) if lead_span else ""
        href = a.get("href", "")
        url = href if href.startswith("http") else f"{BASE}{href}"
        published_at = _parse_dotted_date(published_raw)
        doc_type = doc_type_of(title, source_tier=1)  # ADDENDUM-3 §4: D3=보도자료 기본, 제목에 따라 세분화 가능
        items.append(_build_item(category=category, dept=dept, title=title, lead=lead,
                                  url=url, published_at=published_at, doc_type=doc_type))
    return items


def fetch(*, max_pages: int = 10) -> list[dict]:
    """국세청·금융위원회 보도자료만 골라 반환한다. 페이지 하나가 실패해도 계속 진행.

    기본값 10페이지(~200건): 실측 결과 이 두 부처는 정책브리핑 전체 게시물 중
    비중이 작아(300건 중 2건, 아래 __main__ 실행 결과 참고) 하루치를 안정적으로
    잡으려면 1~2페이지로는 부족했다. 값은 운영하면서 조정할 것.
    """
    items: list[dict] = []
    for page in range(1, max_pages + 1):
        try:
            items.extend(fetch_page(page))
        except Exception as exc:  # noqa: BLE001
            print(f"[policy_briefing] page={page} 수집 실패: {exc}")
    return items


if __name__ == "__main__":
    print("=== 정책브리핑 probe ===")
    print(probe())

    print("\n=== D3: 국세청·금융위원회 보도자료(카테고리 매칭분만, 10페이지) ===")
    items = fetch(max_pages=10)
    for it in items[:15]:
        eff = f" | 시행일: {it['effective_date']}" if it["effective_date"] else ""
        print(f"  [{it['source']['name']:6s}] [{it['category']:5s}] {it['published_at']} | {it['title'][:45]}{eff}")
    print(f"  총 {len(items)}건")
