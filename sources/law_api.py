# -*- coding: utf-8 -*-
"""법제처 국가법령정보 Open API 수집기 (1차 소스 — 공식 법령/시행일) — D4.

docs/SOURCE_PROBE.md §D4 "완전 검증" 기반. 세법 카테고리의 시행일 단일 소스
원칙(사용자 지시 2026-08-26)에 따라, 이 어댑터가 반환하는 `effective_date`가
tax 카테고리 전체의 사실상 유일한 신뢰 가능 시행일 정보다.

- `lawSearch.do`(검색): `query=`가 부분일치라 "지방세법"으로 검색하면 무관한
  "지방교부세법"까지 딸려온다(실측 확인). **법령명이 정확히 일치하는 것만**
  (본법/시행령/시행규칙) 채택한다.
- `lawService.do`(본문 상세): `<시행일자>`/`<공포일자>` 필드가 구조화돼 그대로
  나온다 — 정규식 파싱 불필요. 이 소스만 유일하게 이렇다.
- **명칭 함정**: API 응답의 `소관부처명`도 "재정경제부"(구 명칭)로 나올 수 있다
  (실측: 법인세법 사례). `_MINISTRY_NAME_FIX`로 정규화한다.
- 프록시: `PROXY_BASE`가 있으면 `_http.get_govt()`가 알아서 경유한다(SPEC §9-3).
- `LAW_API_OC` 환경변수가 없으면 법제처가 공개 제공하는 테스트용 OC "test"로
  대체한다(실측 확인 — 실제 데이터가 온다). 다만 사용량 제한이 있을 수 있어
  운영 배포 시엔 실제 OC 발급을 권장한다는 경고를 남긴다.
"""
from __future__ import annotations

import os
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone, timedelta

from . import _http
from ._config import TAX_SUBJECTS
from ._utils import keyword_score, matched_keywords, make_id_exact, final_score, recency_score

SEARCH_URL = "https://www.law.go.kr/DRF/lawSearch.do"
SERVICE_URL = "https://www.law.go.kr/DRF/lawService.do"
VIEW_URL = "https://www.law.go.kr/LSW/lsInfoP.do"  # SPEC.md §4 urls.official 예시와 동일 패턴
# 2026-09-02: "관련 기관 공식 원문 보기"를 lsRvsDocInfoR.do(제정·개정이유
# 단독 페이지, 조문·신구조문대비표로 못 넘어감)로 잠깐 바꿨다가 사용자 지시로
# 되돌렸다 — 오히려 불편하다는 판단. 개정이유는 대신 카드 안의 접이식
# "개정이유 전문 보기" 토글로 보여준다(revision_reason 필드 그대로, app.js
# 참고) — urls.official은 다시 전체 법령 페이지(lsInfoP.do) 하나로 고정.

# TAX_SUBJECTS(data/tax_subjects.yml)가 비어있을 때(설정 파일 없음/파싱 실패)의 폴백.
# ADDENDUM-3 §4-1: "조회 대상 법령은 tax_subjects.yml의 laws: 필드를 모두 합친 목록".
_FALLBACK_LAW_NAMES = [
    "법인세법", "부가가치세법", "소득세법",
    "국제조세조정에 관한 법률", "조세특례제한법", "지방세법",
]


def _configured_law_names() -> list[str]:
    """TAX_SUBJECTS의 laws: 필드를 전부 합쳐 중복 제거한다. 비어있으면 폴백을 쓴다."""
    if not TAX_SUBJECTS:
        return _FALLBACK_LAW_NAMES
    seen: dict[str, None] = {}
    for subject in TAX_SUBJECTS:
        for law_name in subject.get("laws", []):
            seen.setdefault(law_name, None)
    return list(seen) or _FALLBACK_LAW_NAMES

_MINISTRY_NAME_FIX = {"재정경제부": "기획재정부"}  # 레거시 명칭 정규화(SOURCE_PROBE.md D1/D4 참고)
_KST = timezone(timedelta(hours=9))
SLEEP_BETWEEN_REQUESTS = 1.0

# 2026-09-09: 로컬 실측(13.5초, 요청 14회)과 실제 GitHub Actions("60초 초과",
# 연속 3일째)의 격차가 너무 커서 원인 후보(프록시 왕복 지연 / law_api만 유독
# 느림 / 재시도+백오프 중첩으로 실제 요청이 14회보다 많음)를 Actions 로그로
# 가려야 한다는 사용자 요청 — 요청 번호·소요시간을 요청 단위로 남긴다.
# 소요시간엔 `_http.get()`의 재시도(최대 3회, 0.5s/1s/2s 백오프)까지 전부
# 포함된다 — 한 줄이 유난히 길면(예: 수 초 이상) 그 요청에서 재시도가
# 걸렸다는 뜻으로 읽으면 된다.
_request_count = 0


def _oc() -> str:
    oc = os.environ.get("LAW_API_OC")
    if not oc:
        print("[law_api] LAW_API_OC 환경변수 없음 — 법제처 공개 테스트용 OC('test')로 대체합니다. "
              "운영 배포 시 실제 OC 발급을 권장합니다.")
        return "test"
    return oc


def _timed_get_govt(url: str, *, params: dict, label: str):
    """`_http.get_govt()`를 요청 번호·소요시간 로그와 함께 호출한다(law_api 전용)."""
    global _request_count
    _request_count += 1
    n = _request_count
    t0 = time.monotonic()
    try:
        resp = _http.get_govt(url, params=params)
    except Exception as exc:  # noqa: BLE001 - 로그만 남기고 그대로 올린다
        elapsed = time.monotonic() - t0
        print(f"[law_api] 요청 #{n} {label} - {elapsed:.2f}초 후 실패: {exc}")
        raise
    elapsed = time.monotonic() - t0
    status = getattr(resp, "status_code", "?")  # 테스트용 fake response는 status_code가 없을 수 있음
    print(f"[law_api] 요청 #{n} {label} - {elapsed:.2f}초 (HTTP {status})")
    return resp


def probe() -> dict:
    try:
        resp = _http.get_govt(SEARCH_URL, params={"OC": _oc(), "target": "law", "type": "XML", "query": "법인세법"})
        ok = resp.status_code == 200 and "<totalCnt>" in resp.text
        return {"ok": ok, "method": "api", "note": f"lawSearch.do HTTP {resp.status_code}, proxy={_http.proxy_base() is not None}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "method": "api", "note": f"요청 실패: {exc}"}


def _tag_text(root: ET.Element, name: str) -> str | None:
    el = root.find(name)
    if el is None or el.text is None:
        return None
    text = el.text.strip()
    return text or None


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _yyyymmdd_to_iso(s: str | None) -> str | None:
    if not s or len(s) != 8 or not s.isdigit():
        return None
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:8])).isoformat()
    except ValueError:
        return None


def _parse_iso_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _search_root(name: str) -> str:
    """"OO법 시행령"/"OO법 시행규칙"의 본법 이름(검색 쿼리로 쓸 root)을 뽑는다.
    쿼리 한 번(본법 이름)이면 본법+시행령+시행규칙이 한꺼번에 딸려오므로, 여러
    파생 법령이 있어도 root마다 한 번씩만 호출하면 된다.
    """
    for suffix in (" 시행규칙", " 시행령"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def search_law(law_name: str, *, oc: str | None = None, wanted: set[str] | None = None) -> list[dict]:
    """`law_name`을 루트로 검색해, `wanted`(기본값: 본법+시행령+시행규칙 자동유도)에
    **정확히** 속하는 것만 골라 반환한다.

    lawSearch.do의 query는 부분일치라 "지방세법"이 "지방교부세법"도 끌고 오는
    것까지 실측 확인했다(SOURCE_PROBE.md D4) — 여기서 정확일치로 한 번 더 거른다.

    2026-09-08: `<시행일자>`도 이 응답에 이미 들어있다(실측 확인) — 예전엔 이걸
    안 뽑고 매 법령마다 `law_detail()`(lawService.do, 별도 요청)을 또 불러서
    시행일자를 얻었는데, `fetch()`의 요청량(25회)이 소스 타임아웃(60초) 예산을
    거의 다 써버리는 원인이었다. 여기서 바로 뽑아두면 `law_detail()` 호출
    자체가 필요 없어진다(그건 검색 응답에 없는 `제개정이유내용`용으로만 남음).
    """
    resp = _timed_get_govt(SEARCH_URL, params={
        "OC": oc or _oc(), "target": "law", "type": "XML", "query": law_name,
    }, label=f"검색 '{law_name}'")
    root = ET.fromstring(resp.content)
    wanted = wanted or {law_name, f"{law_name} 시행령", f"{law_name} 시행규칙"}
    out = []
    for law in root.findall("law"):
        name = _tag_text(law, "법령명한글") or ""
        if name not in wanted:
            continue
        out.append({
            "법령명한글": name,
            "법령ID": _tag_text(law, "법령ID"),
            "법령일련번호": _tag_text(law, "법령일련번호"),
            "공포일자": _tag_text(law, "공포일자"),
            "공포번호": _tag_text(law, "공포번호"),
            "제개정구분명": _tag_text(law, "제개정구분명"),
            "소관부처명": _tag_text(law, "소관부처명"),
            "시행일자": _tag_text(law, "시행일자"),
        })
    return out


def law_detail(law_name: str, *, oc: str | None = None) -> dict | None:
    """lawService.do 본문 상세. `<시행일자>`가 구조화된 필드로 바로 나온다.

    2026-09-02: `<제개정이유><제개정이유내용>`도 함께 뽑는다 — 법제처 사람용
    페이지(`lsInfoP.do`)의 "제·개정이유" 탭과 동일한 텍스트인데, 그 페이지는
    JS로 렌더링되는 SPA라 스크래핑이 안 되는 반면 이 API 응답엔 처음부터
    구조화된 필드로 들어있다(실측 확인: 법인세법/법인세법 시행령/법인세법
    시행규칙/부가가치세법 4건 전부 정상 추출). `_tag_text()`가 첫 매치만
    반환하므로 이 필드는 항상 하나만 온다(실측상 여러 건인 사례 없음).
    """
    resp = _timed_get_govt(SERVICE_URL, params={
        "OC": oc or _oc(), "target": "law", "type": "XML", "LM": law_name,
    }, label=f"상세조회 '{law_name}'")
    root = ET.fromstring(resp.content)
    result_code = _tag_text(root, "resultCode")
    if result_code is not None and result_code != "00":
        return None
    # lawService.do는 <법령><기본정보><시행일자>...처럼 한 단계 더 들어가 있다(lawSearch.do와 다름).
    reason = _tag_text(root, ".//제개정이유내용")
    return {
        "시행일자": _tag_text(root, ".//시행일자"),
        "공포일자": _tag_text(root, ".//공포일자"),
        "제개정이유": reason,
    }


def fetch(law_names: list[str] | None = None) -> list[dict]:
    """D4: `law_names`(기본값: TAX_SUBJECTS의 laws: 전체, data/tax_subjects.yml)를
    수집한다. 검색은 법령 루트(본법) 단위로 한 번씩만 호출하고(같은 API 호출로
    시행령·시행규칙까지 딸려오므로), `law_names`에 정확히 속하는 것만 채택한다.
    법령 하나 조회가 실패해도 나머지는 계속 진행한다(SPEC §9-4).

    2026-09-08: 상세 조회(`law_detail()`, lawService.do)는 **본법(검색 루트와
    이름이 같은 항목)에만** 한다 — 시행일자는 이제 `search_law()` 응답에서
    바로 나오므로(위 docstring 참고) 시행령/시행규칙까지 상세 조회할 필요가
    없고, 상세 조회의 유일한 존재 이유는 검색 응답에 없는 `제개정이유내용`
    뿐이다. 사용자 지시로 시행령/시행규칙의 개정이유는 포기(대체로 본법
    개정이유에 함께 언급되는 경우가 많다는 게 사용자 판단) — 요청 25회→14회,
    강제 sleep 24초→13초로 줄어 소스 타임아웃(60초) 안에 여유 있게 끝난다.
    """
    global _request_count
    _request_count = 0  # 이번 fetch() 실행 동안의 요청 번호를 1부터 다시 매긴다
    fetch_t0 = time.monotonic()
    oc = _oc()
    items: list[dict] = []
    wanted = set(law_names or _configured_law_names())
    roots = sorted({_search_root(name) for name in wanted})

    for i, root_name in enumerate(roots):
        if i > 0:
            time.sleep(SLEEP_BETWEEN_REQUESTS)
        try:
            matches = search_law(root_name, oc=oc, wanted=wanted)
        except Exception as exc:  # noqa: BLE001
            print(f"[law_api] '{root_name}' 검색 실패: {exc}")
            continue
        for m in matches:
            detail = {}
            if m["법령명한글"] == root_name:  # 본법만 상세 조회(개정이유 목적)
                time.sleep(SLEEP_BETWEEN_REQUESTS)
                try:
                    detail = law_detail(m["법령명한글"], oc=oc) or {}
                except Exception as exc:  # noqa: BLE001
                    print(f"[law_api] '{m['법령명한글']}' 상세 조회 실패: {exc}")
                    detail = {}

            promulgation = _yyyymmdd_to_iso(m.get("공포일자") or detail.get("공포일자"))
            effective = _yyyymmdd_to_iso(m.get("시행일자") or detail.get("시행일자"))
            title = m["법령명한글"]
            raw_ministry = m.get("소관부처명") or "국가법령정보센터"
            # 공동소관 법령은 "재정경제부,행정안전부"처럼 콤마로 여러 부처가 온다 — 토큰별로 정규화.
            ministry = ",".join(_MINISTRY_NAME_FIX.get(p, p) for p in raw_ministry.split(","))
            url = f"{VIEW_URL}?lsiSeq={m['법령일련번호']}" if m.get("법령일련번호") else f"{VIEW_URL}?efYd=&lsNm={title}"

            kw = keyword_score(title, "tax")
            rec = recency_score(_parse_iso_date(promulgation)) if promulgation else 0
            items.append({
                "id": make_id_exact(url),  # lsInfoP.do?lsiSeq=가 유일 식별자(이 버그로 dedupe에서 18건이 1건으로 뭉개졌었음)
                "category": "tax",
                "doc_type": "제·개정",
                "title": title,
                "summary": [],
                "impact": None,
                "published_at": promulgation,
                "collected_at": _now_kst_iso(),
                "effective_date": effective,
                "source": {"name": ministry, "domain": "law.go.kr", "tier": 1, "type": "official"},
                "trust_score": 100,
                "keyword_score": kw,
                "final_score": final_score(100, kw, rec),
                "matched_keywords": matched_keywords(title, "tax"),
                "urls": {"news": None, "official": url},
                "revision_reason": detail.get("제개정이유"),
                "law_meta": {
                    "law_name": title,
                    "law_id": m.get("법령ID"),
                    "revision_type": m.get("제개정구분명"),
                    "promulgation_date": promulgation,
                    "enforcement_date": effective,
                },
                "attachments": None,
                "layer": "L1",
                "is_noise": False,
            })
    total_elapsed = time.monotonic() - fetch_t0
    print(f"[law_api] fetch() 완료 - 요청 {_request_count}회, 총 {total_elapsed:.2f}초, {len(items)}건")
    return items


if __name__ == "__main__":
    print("=== 법제처 probe ===")
    print(probe())

    print("\n=== D4: 세목 화이트리스트 법령 수집 ===")
    items = fetch()
    for it in items:
        lm = it["law_meta"]
        print(f"  [{it['source']['name']:6s}] {lm['law_name']:12s} | 공포:{lm['promulgation_date']} "
              f"시행:{lm['enforcement_date']} | {lm['revision_type']}")
    print(f"  총 {len(items)}건")
