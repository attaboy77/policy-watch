# -*- coding: utf-8 -*-
""""현행 기준" 탭 데이터 조립 (2026-09-02 사용자 요청).

4개 분야의 "지금 유효한 기준·법령" 목록을 새로 크롤링하지 않고 이미 수집된
`finalized` 아이템(sources/main.py의 build_data_json()이 넘겨주는, 최종
확정 단계 리스트)에서 뽑는다. 분야별 접근이 다르다:

- K-IFRS: `kasb.py` D(List2006.do 제·개정 이력)에서 제목의 "제NNNN호"를 정규식
  추출해 기준서 번호별로 최신 개정 1건만 남기고, 그중 최근 5건만 노출한다.
  전체 기준서(100여 종) 목록이 아니라 "개정 이력이 있는 것"만 있다는 한계가
  있어 KASB 공식 열람서비스(db.kasb.or.kr/standard) 링크를 함께 준다
  (2026-09-02 사용자 지시 — 목록 자체보다 "전체 목록 보기" 링크 우선).
- 지속가능성 공시(KSSB): `kasb.py` E(자발적용가능)에서 나온 제1호/제2호
  그대로(정확히 2건이라 캡 불필요). 같은 이유로 db.kasb.or.kr/esg 링크 병행.
- 세법: `law_api.py`(법제처 API)가 매 실행마다 항상 최신 스냅샷으로 주는
  law_meta 그대로 — 이미 "현재 유효한 법령" 그 자체라 가공이 거의 없다.
- 내부회계: k-icfr.org에 3분류(모범규준/평가·보고 기준/적용지침)별 안정 URL이
  없어(2026-09-02 조사 확인 — 전체 진입점 하나와 신/구 버전 인덱스 2개뿐,
  3분류 구분은 없음) 제목 키워드로 문서를 직접 분류한다.
"""
from __future__ import annotations

import re
from typing import Callable

KIFRS_CATALOG_URL = "https://db.kasb.or.kr/standard"
ESG_CATALOG_URL = "https://db.kasb.or.kr/esg"
ICFR_CATALOG_URL = "https://www.k-icfr.org/sub/menu/guideline.asp"

_KIFRS_RECENT_CAP = 5
_STANDARD_NO_RE = re.compile(r"제(\d{4})호")


def _item_link(item: dict) -> str | None:
    urls = item.get("urls") or {}
    return urls.get("official") or urls.get("news")


def build_kifrs_standards(items: list[dict]) -> dict:
    """기준서 번호별 최신 개정 1건 → 최근 5건만."""
    by_std: dict[str, dict] = {}
    for it in items:
        if it.get("category") != "kifrs" or it.get("doc_type") != "제·개정":
            continue
        for std_no in set(_STANDARD_NO_RE.findall(it.get("title", ""))):
            prev = by_std.get(std_no)
            if not prev or (it.get("published_at") or "") > (prev.get("published_at") or ""):
                by_std[std_no] = it

    recent = sorted(
        (
            {
                "standard_no": f"제{no}호",
                "title": it["title"],
                "latest_revision_date": it.get("published_at"),
                "effective_date": it.get("effective_date"),
                "url": _item_link(it),
            }
            for no, it in by_std.items()
        ),
        key=lambda r: r["latest_revision_date"] or "",
        reverse=True,
    )[:_KIFRS_RECENT_CAP]

    return {"catalog_url": KIFRS_CATALOG_URL, "recent": recent}


def build_esg_standards(items: list[dict]) -> dict:
    """KSSB 자발적용 기준서(제1호/제2호) — 있는 만큼 전부."""
    recent = sorted(
        (
            {
                "title": it["title"],
                "issued_date": it.get("published_at"),
                "effective_date": it.get("effective_date"),
                "is_roadmap_estimate": bool(it.get("is_roadmap_estimate")),
                "url": _item_link(it),
            }
            for it in items
            if it.get("category") == "esg" and it.get("doc_type") == "자발적용"
        ),
        key=lambda r: r["title"],
    )
    return {"catalog_url": ESG_CATALOG_URL, "recent": recent}


# 세법: 법령명 표시 순서(요청하신 5개 법 우선 + 보너스 2개, 2026-09-02 사용자
# 확정) → 그 안에서 본법 → 시행령 → 시행규칙 순.
_TAX_LAW_ORDER = [
    "법인세법", "부가가치세법", "소득세법", "지방세법", "지방세특례제한법",
    "조세특례제한법", "국제조세조정에 관한 법률",
]
_TAX_LAW_SUFFIX_RANK = {"": 0, " 시행령": 1, " 시행규칙": 2}


def _tax_law_sort_key(law_name: str) -> tuple[int, int, str]:
    for root in _TAX_LAW_ORDER:
        for suffix, rank in _TAX_LAW_SUFFIX_RANK.items():
            if law_name == root + suffix:
                return (_TAX_LAW_ORDER.index(root), rank, law_name)
    return (len(_TAX_LAW_ORDER), 0, law_name)  # 목록에 없는 법령(폴백) — 맨 뒤


def build_tax_laws(items: list[dict]) -> dict:
    """law_api.py가 매 실행마다 채워주는 law_meta 그대로 — 이미 "현재 유효한
    법령"이라 별도 최신판 판정이 필요 없다. 날짜가 없으면(law_detail 조회
    실패 등) 빈 문자열로 둔다(사용자 지시 — "없으면 빈칸으로")."""
    laws = [
        {
            "law_name": (it.get("law_meta") or {}).get("law_name") or it.get("title", ""),
            "promulgation_date": (it.get("law_meta") or {}).get("promulgation_date") or "",
            "enforcement_date": (it.get("law_meta") or {}).get("enforcement_date") or "",
            "url": _item_link(it),
        }
        for it in items
        if it.get("category") == "tax" and it.get("law_meta")
    ]
    laws.sort(key=lambda r: _tax_law_sort_key(r["law_name"]))
    return {"laws": laws}


# 내부회계 3분류(2026-09-02 사용자 확정): 제목 키워드로 판정한다 — k-icfr.org에
# 3분류별 안정 URL이 없어(조사 완료, 위 모듈 docstring 참고) 유일한 방법.
#
# 판정 "우선순위"(이 순서로 매치 검사)와 화면 "표시 순서"는 다르다 — "적용기법"
# 문서 중에도 "평가"+"보고"가 같이 들어간 제목이 많아서(예: "…평가 및 보고
# 적용기법 전문") 평가·보고 기준의 느슨한 규칙을 먼저 보면 잘못 걸린다. 반드시
# "개념체계"(모범규준) → "적용기법"/"가이드라인"(적용지침) → 나머지 평가+보고
# 조합(평가·보고 기준) 순으로 검사해야 한다.
_ICFR_BUCKET_RULES: list[tuple[str, Callable[[str], bool]]] = [
    ("모범규준", lambda t: "개념체계" in t),
    ("적용지침", lambda t: "적용기법" in t or "가이드라인" in t),
    ("평가·보고 기준", lambda t: "평가" in t and "보고" in t and ("모범규준" in t or "지침" in t)),
]

# 화면 표시 순서(사용자 확정 화면 구성안 그대로) — 위 판정 우선순위와 별개.
_ICFR_BUCKET_DISPLAY_ORDER = ["모범규준", "평가·보고 기준", "적용지침"]


def _icfr_bucket_of(title: str) -> str | None:
    for label, rule in _ICFR_BUCKET_RULES:
        if rule(title):
            return label
    return None


_TRAILING_PAREN_RE = re.compile(r"\s*\([^)]*\)\s*$")
_TRAILING_CLEAN_VER_RE = re.compile(r"\s*Clean\s*ver\.?\s*$", re.IGNORECASE)


def _icfr_doc_base_title(title: str) -> str:
    """날짜·버전 표시(괄호, "Clean ver.")를 뗀 "같은 문서" 판정용 키.
    예: "…평가·보고 지침 Clean ver. ('24.12.23 개정)"과 "…평가·보고 지침
    ('23.12.29 배포)"가 같은 문서의 서로 다른 재게시본임을 알아본다."""
    base = _TRAILING_PAREN_RE.sub("", title)
    base = _TRAILING_CLEAN_VER_RE.sub("", base)
    return base.strip()


def build_icfr_documents(items: list[dict]) -> dict:
    """모범규준/적용지침 doc_type 항목 중 3분류 키워드에 걸리는 것만 채택하고,
    같은 문서의 재게시본(날짜만 다른 동일 base title)은 최신 published_at
    하나만 남긴다."""
    latest_by_base: dict[str, dict] = {}
    bucket_of_base: dict[str, str] = {}
    for it in items:
        if it.get("category") != "icfr" or it.get("doc_type") not in ("모범규준", "적용지침"):
            continue
        title = it.get("title", "")
        bucket = _icfr_bucket_of(title)
        if not bucket:
            continue
        base = _icfr_doc_base_title(title)
        prev = latest_by_base.get(base)
        if not prev or (it.get("published_at") or "") > (prev.get("published_at") or ""):
            latest_by_base[base] = it
            bucket_of_base[base] = bucket

    by_bucket: dict[str, list[dict]] = {}
    for base, it in latest_by_base.items():
        by_bucket.setdefault(bucket_of_base[base], []).append({
            "title": it["title"],
            "revision_date": it.get("published_at"),
            "url": _item_link(it),
        })

    buckets = []
    for label in _ICFR_BUCKET_DISPLAY_ORDER:
        docs = sorted(by_bucket.get(label, []), key=lambda d: d["revision_date"] or "", reverse=True)
        buckets.append({"label": label, "documents": docs})

    return {"catalog_url": ICFR_CATALOG_URL, "buckets": buckets}


def build_current_standards(items: list[dict]) -> dict:
    return {
        "kifrs": build_kifrs_standards(items),
        "esg": build_esg_standards(items),
        "tax": build_tax_laws(items),
        "icfr": build_icfr_documents(items),
    }
