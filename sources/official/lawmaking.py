# -*- coding: utf-8 -*-
"""국민참여입법센터(opinion.lawmaking.go.kr) (부처)입법예고 수집기 — 2026-10-01 신설.

법제처 현행법령 API(law_api.py)는 **공포된 뒤에야** 잡힌다(실측: 9/30 공포·10/1 시행
법인세법 시행령이 시행일 당일 수집됨). 이 사이트 목적은 시행 전에 미리 파악하는 것이라,
공포 1~2개월 전 단계인 입법예고를 따로 받는다.

- 법제처 입법예고 Open API(`lawmaking.go.kr/rest/ogLmPp`)는 국민참여입법센터 정보공개
  서비스로 별도 발급받은 OC가 필요하다(`OC=test`는 401, `LAW_API_OC`와 신청 체계가 다름).
  그래서 OC 없이 공개 웹 목록(`/gcom/ogLmPp`, 서버 렌더링 HTML)을 쓴다. 공식 OC를
  받으면 이 모듈만 API로 바꾸면 된다.
- 검색: 활성 세목 법령(data/tax_subjects.yml `laws:`)의 본법 이름마다 한 번씩
  `lsNm=` 부분일치 검색(종료된 예고 포함, `finishIncludeYn=Y`) → 요청 7회. 제목에서
  법령명("법인세법 시행령 일부개정령안 입법예고" → "법인세법 시행령")을 뽑아 활성
  세목 법령명과 **정확히** 일치하는 것만 남긴다(관세법·개별소비세법 등 배제).
- 예고 시작일이 최근 `COLLECT_WINDOW_DAYS`일 이내인 것만.
- law_api와 별도 소스라 main.py의 소스별 60초 상한이 따로 적용된다.
- 관련 예고가 없는 날 0건은 정상(main.ALLOW_EMPTY_SOURCES). 검색이 전부 실패하거나
  목록 표 자체를 못 읽으면 예외로 올려 실패 처리한다.
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime, timezone, timedelta

from bs4 import BeautifulSoup

from .. import _http
from .._config import COLLECT_WINDOW_DAYS
from .._utils import (configured_tax_laws, doc_type_of, final_score, keyword_score, make_id_exact,
                      match_tax_law, matched_keywords, recency_score)

BASE = "https://opinion.lawmaking.go.kr"
LIST_URL = f"{BASE}/gcom/ogLmPp"
SOURCE_DOMAIN = "lawmaking.go.kr"
SLEEP_BETWEEN_REQUESTS = 0.5
_KST = timezone(timedelta(hours=9))
_MINISTRY_NAME_FIX = {"기획재정부": "재정경제부"}  # 2026.1.2 개편 전 명칭 → 현행 명칭(law_api.py와 동일)

_SEQ_RE = re.compile(r"/gcom/ogLmPp/(\d+)")
# "법인세법 시행령 일부개정령안 입법예고", "지방세법 일부개정법률안 재입법예고" → 앞부분이 법령명.
_LAW_NAME_RE = re.compile(r"^(.*?)\s*(?:일부개정|전부개정|제정|폐지)")
_DATE_RE = re.compile(r"(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.")


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _search_roots() -> list[str]:
    """활성 세목 법령명의 본법 이름(검색어) 목록. "OO법 시행령"도 "OO법" 검색에 걸린다."""
    roots: dict[str, None] = {}
    for name in configured_tax_laws():
        for suffix in (" 시행규칙", " 시행령"):
            if name.endswith(suffix):
                name = name[: -len(suffix)]
                break
        roots.setdefault(name, None)
    return list(roots)


def _dates(text: str) -> list[str]:
    out = []
    for y, m, d in _DATE_RE.findall(text):
        try:
            out.append(date(int(y), int(m), int(d)).isoformat())
        except ValueError:
            pass
    return out


def law_name_of(title: str) -> str | None:
    m = _LAW_NAME_RE.match(title.strip())
    return m.group(1).strip() if m else None


def parse_list(html: str) -> tuple[list[dict], bool]:
    """목록 HTML → (행 dict 리스트, 목록 표를 찾았는지). 행: seq/title/ministry/law_kind/start/end."""
    soup = BeautifulSoup(html, "html.parser")
    # 결과가 없을 때도 같은 표가 "해당 목록이 없습니다" 한 행으로 온다 — 표(캡션)가
    # 있으면 정상 응답으로 본다.
    table = next((t for t in soup.select("table")
                  if t.caption and "입법예고 목록" in t.caption.get_text()), None)
    if table is None:
        return [], False
    rows = []
    for tr in table.select("tbody tr"):
        subject = tr.select_one("td[data-th='법령 제명'] a[href]")
        if subject is None:
            continue
        m = _SEQ_RE.search(subject["href"])
        if not m:
            continue
        dept_ps = [p.get_text(strip=True) for p in tr.select("td[data-th^='소관부처'] p")]
        period = tr.select_one("td[data-th='입법의견 접수기간']")
        dates = _dates(period.get_text(" ", strip=True)) if period else []
        rows.append({
            "seq": m.group(1),
            "title": subject.get_text(strip=True),
            "ministry": dept_ps[0] if dept_ps else "",
            "law_kind": dept_ps[1].strip("()") if len(dept_ps) > 1 else "",
            "start": dates[0] if dates else None,
            "end": dates[1] if len(dates) > 1 else None,
        })
    return rows, True


def _build_item(row: dict) -> dict:
    title = row["title"]
    url = f"{LIST_URL}/{row['seq']}"
    raw_ministry = row["ministry"] or "국민참여입법센터"
    ministry = ",".join(_MINISTRY_NAME_FIX.get(p, p) for p in raw_ministry.split(","))
    kw = keyword_score(title, "tax")
    published_at = row["start"]
    rec = recency_score(date.fromisoformat(published_at)) if published_at else 0
    period = f"{(row['start'] or '?').replace('-', '.')}~{(row['end'] or '?').replace('-', '.')}"
    return {
        "id": make_id_exact(url),
        "category": "tax",
        "doc_type": doc_type_of(title, source_tier=1),  # "입법예고" → 공개초안(stage 의견수렴)
        "title": title,
        "summary": [],
        "impact": None,
        "published_at": published_at,
        "collected_at": _now_kst_iso(),
        "effective_date": None,  # 입법예고 단계엔 시행일 미확정 — 공포 후 law_api가 채운다
        "source": {"name": ministry, "domain": SOURCE_DOMAIN, "tier": 1, "type": "official"},
        "trust_score": 100,
        "keyword_score": kw,
        "final_score": final_score(100, kw, rec),
        "matched_keywords": matched_keywords(title, "tax"),
        "urls": {"news": None, "official": url},
        # law_meta는 비운다 — current_standards.build_tax_laws()가 "law_meta 있는 tax
        # 항목 = 현행 법령"으로 모으므로, 입법예고안이 "현행 기준" 탭에 섞이면 안 된다.
        "law_meta": None,
        "attachments": None,
        # 카드에 없는 사실(의견 접수기간)을 규칙 기반 요약 1줄로 — _summarize._summary_from_body()
        "_body": f"입법의견 접수기간 {period}",
        "layer": "L1",
        "is_noise": False,
    }


def fetch() -> list[dict]:
    today = datetime.now(_KST).date()
    cutoff = (today - timedelta(days=COLLECT_WINDOW_DAYS)).isoformat()
    roots = _search_roots()
    found: dict[str, dict] = {}
    ok_queries = 0
    t0 = time.monotonic()
    for i, root in enumerate(roots):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            resp = _http.get_govt(LIST_URL, params={"lsNm": root, "finishIncludeYn": "Y"})
            rows, table_found = parse_list(resp.text)
        except Exception as exc:  # noqa: BLE001
            print(f"[lawmaking] '{root}' 검색 실패: {exc}")
            continue
        if not table_found:
            print(f"[lawmaking] '{root}' 목록 표를 찾지 못함(구조 변경·차단 의심)")
            continue
        ok_queries += 1
        for row in rows:
            law_name = law_name_of(row["title"])
            if not law_name or not match_tax_law([law_name]):
                continue
            if not row["start"] or row["start"] < cutoff:
                continue
            item = _build_item(row)
            found.setdefault(item["id"], item)
    if roots and ok_queries == 0:
        raise RuntimeError("입법예고 검색 전부 실패 — 응답 없음 또는 목록 구조 변경·차단 의심")
    print(f"[lawmaking] fetch() 완료 - 검색 {len(roots)}회(성공 {ok_queries}), "
          f"총 {time.monotonic() - t0:.2f}초, {len(found)}건")
    return list(found.values())


if __name__ == "__main__":
    for it in fetch():
        print(f"  [{it['source']['name']}] {it['published_at']} {it['title']} | {it['_body']}")
