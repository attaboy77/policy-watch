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
"""
from __future__ import annotations

from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _http
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
        resp = _http.get(LIST_URL)
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


def fetch_page(page: int = 1) -> list[dict]:
    resp = _http.get(LIST_URL, params={"curPage": page})
    soup = BeautifulSoup(resp.text, "html.parser")
    items: list[dict] = []

    for li in soup.select("li"):
        subject_a = li.select_one(".subject a")
        day_div = li.select_one(".day")
        if subject_a is None or day_div is None:
            continue
        title = subject_a.get_text(strip=True)
        href = subject_a.get("href", "")
        if not title or not href:
            continue
        if is_event_announcement(title):  # ADDENDUM-4 §1 + ADDENDUM-7 §4
            continue
        category = _classify_own_press(title)
        if category is None:
            continue  # 보험업 감독·가계부채 등 우리 4개 카테고리와 무관한 보도자료는 버림
        if not pass_tax_filter(category=category, layer="L1", text=title):
            continue  # 드물지만 tax로 분류될 경우 세목 화이트리스트 적용(ADDENDUM-3 §3)

        published_at = day_div.get_text(strip=True) or None
        url = href if href.startswith("http") else f"{BASE}{href}"
        doc_type = doc_type_of(title, source_tier=1)
        effective_date = extract_effective_date(title) if category != "tax" else None
        kw = keyword_score(title, category)
        rec = recency_score(_parse_iso_date(published_at)) if published_at else 0
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
    return items


def fetch(*, max_pages: int = 5) -> list[dict]:
    """A4/C2: 금융위원회 보도자료. 페이지 하나가 실패해도 계속 진행."""
    items: list[dict] = []
    for page in range(1, max_pages + 1):
        if page > 1:
            import time
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            items.extend(fetch_page(page))
        except Exception as exc:  # noqa: BLE001
            print(f"[fsc] page={page} 수집 실패: {exc}")
    return items


if __name__ == "__main__":
    print("=== FSC probe ===")
    print(probe())

    print("\n=== A4/C2: 금융위원회 보도자료(카테고리 매칭분만, 5페이지) ===")
    items = fetch(max_pages=5)
    for it in items[:15]:
        att = f" | 첨부 {len(it['attachments'])}개" if it["attachments"] else ""
        print(f"  [{it['category']:5s}] [{it['doc_type']:6s}] {it['published_at']} | {it['title'][:45]}{att}")
    print(f"  총 {len(items)}건")
