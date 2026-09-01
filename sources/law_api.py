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
VIEW_URL = "https://www.law.go.kr/LSW/lsInfoP.do"  # SPEC.md §4 urls.official 예시와 동일 패턴 — lsiSeq 없을 때만 폴백으로 씀
# 2026-09-02 사용자 지시("관련 기관 공식 원문 보기"를 누르면 제정·개정이유가
# 바로 보이면 좋겠다) — 실측 확인: lsInfoP.do는 탭 전환이 순수 클릭 JS
# (sideInfo())라 URL 쿼리로 초기 탭을 지정할 방법이 없다(location.hash도,
# urlMode류 파라미터도 안 읽는다 — 페이지 로드 시 항상 lsBdy(본문)로 고정).
# 대신 그 탭이 AJAX로 불러오는 실제 엔드포인트(lsRvsDocInfoR.do)가 lsiSeq만
# 넘기면 단독 페이지로도 정상 렌더링된다는 걸 확인했다(법인세법/법인세법
# 시행규칙 2건 실측 — "【제정·개정이유】"+"【제정·개정문】" 내용이 그대로 나옴).
# 사이트 전체 메뉴·헤더는 없는 더 좁은 페이지(원래 팝업창용으로 설계된 것으로
# 보임)라 조문 본문·신구조문대비표 등 다른 탭으로는 그 페이지 안에서 못
# 넘어간다 — "개정이유를 바로 보여주는 것"과 "전체 법령 페이지 그대로"를
# 동시에 만족할 방법은 없었다(사용자 지시: 안 되는 걸 억지로 만들지 말 것).
REASON_VIEW_URL = "https://www.law.go.kr/LSW/lsRvsDocInfoR.do"

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


def _oc() -> str:
    oc = os.environ.get("LAW_API_OC")
    if not oc:
        print("[law_api] LAW_API_OC 환경변수 없음 — 법제처 공개 테스트용 OC('test')로 대체합니다. "
              "운영 배포 시 실제 OC 발급을 권장합니다.")
        return "test"
    return oc


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
    """
    resp = _http.get_govt(SEARCH_URL, params={
        "OC": oc or _oc(), "target": "law", "type": "XML", "query": law_name,
    })
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
    resp = _http.get_govt(SERVICE_URL, params={
        "OC": oc or _oc(), "target": "law", "type": "XML", "LM": law_name,
    })
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
    """
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
            time.sleep(SLEEP_BETWEEN_REQUESTS)
            try:
                detail = law_detail(m["법령명한글"], oc=oc) or {}
            except Exception as exc:  # noqa: BLE001
                print(f"[law_api] '{m['법령명한글']}' 상세 조회 실패: {exc}")
                detail = {}

            promulgation = _yyyymmdd_to_iso(m.get("공포일자") or detail.get("공포일자"))
            effective = _yyyymmdd_to_iso(detail.get("시행일자"))
            title = m["법령명한글"]
            raw_ministry = m.get("소관부처명") or "국가법령정보센터"
            # 공동소관 법령은 "재정경제부,행정안전부"처럼 콤마로 여러 부처가 온다 — 토큰별로 정규화.
            ministry = ",".join(_MINISTRY_NAME_FIX.get(p, p) for p in raw_ministry.split(","))
            url = f"{VIEW_URL}?lsiSeq={m['법령일련번호']}" if m.get("법령일련번호") else f"{VIEW_URL}?efYd=&lsNm={title}"
            # 2026-09-02: "관련 기관 공식 원문 보기"는 제정·개정이유가 바로 보이는
            # REASON_VIEW_URL로 바꾸되, id는 반드시 기존 url(lsInfoP.do?lsiSeq=)
            # 그대로 써서 만든다 — id가 바뀌면 data/summary_cache.json에 이미
            # 채워둔 AI 요약들(법인세법 등 18건)이 전부 고아가 된다(id 불변 원칙).
            lsi_seq = m.get("법령일련번호")
            official_url = f"{REASON_VIEW_URL}?lsiSeq={lsi_seq}" if lsi_seq else url

            kw = keyword_score(title, "tax")
            rec = recency_score(_parse_iso_date(promulgation)) if promulgation else 0
            items.append({
                "id": make_id_exact(url),  # lsInfoP.do?lsiSeq=가 유일 식별자(이 버그로 dedupe에서 18건이 1건으로 뭉개졌었음) — official_url이 바뀌어도 이 값은 고정
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
                "urls": {"news": None, "official": official_url},
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
