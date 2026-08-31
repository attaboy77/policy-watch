# -*- coding: utf-8 -*-
"""쿼리 생성 / 노이즈 필터 / 신뢰도 / 중복제거 / 날짜파싱 유틸리티.
"""
import hashlib, re
from datetime import date, datetime, timezone, timedelta
from urllib.parse import urlparse, quote_plus
from ._config import (CATEGORIES, NOISE_KEYWORDS, TRUST_TIERS,
                      DEFAULT_TIER, DEFAULT_TRUST, DOC_TYPE_RULES,
                      INCIDENT_KEYWORDS, PROCEDURAL_KEYWORDS, TAX_INVESTIGATION_COMBO,
                      TAX_SUBJECTS, MAX_NEWS_PER_CATEGORY, MAX_TIER4_PER_CATEGORY,
                      ADMIN_NOISE_KEYWORDS, SIMILARITY_THRESHOLD, SUBJECT_SIMILARITY_THRESHOLD,
                      SIMILARITY_DAY_WINDOW,
                      RELATED_NEWS_MAX, RELATED_NEWS_DAY_WINDOW, RELATED_NEWS_MIN_SIMILARITY,
                      DISCUSSION_MATERIAL_KEYWORDS, DISCUSSION_OVERRIDE_KEYWORDS,
                      REGULATORY_SIGNALS, CORPORATE_PR_KEYWORDS, CORPORATE_PR_STRONG_SIGNALS,
                      APPLICABILITY, COMPANY_EVENTS, COMPANY_EVENT_STRONG_SIGNALS,
                      MANUFACTURING_ACCOUNTING_CONTEXT, EVENT_ANNOUNCEMENT_STRONG_SIGNALS,
                      FOREIGN_STANDARD_BODIES)


# ── 0-1) required_strong/required_weak 카테고리 지원 (SPEC-ADDENDUM-5.md §4) ─
# icfr/kifrs는 "내부통제"/"금융위원회"처럼 일반 명사 성격의 약한 키워드가
# required_strong 없이도 카테고리를 확정시켜버리는 문제(예: 이란 군부 기사가
# "내부 통제"로 icfr에 걸림)가 있어, required를 강/약으로 나눴다. 약한 키워드는
# weak_context(회계 문맥)와 함께 있을 때만 인정한다. tax/esg처럼 나누지 않은
# 카테고리는 기존 "required" 리스트를 그대로 쓴다(하위 호환).
def _required_list(cat_key: str) -> list[str]:
    """점수 계산 등 '히트 개수 세기' 용도의 평평한 필수 키워드 리스트."""
    c = CATEGORIES[cat_key]
    if "required_strong" in c:
        return c["required_strong"] + c.get("required_weak", [])
    return c["required"]


def _has_required_match(text: str, cat_key: str) -> bool:
    """카테고리 확정 여부(통과/탈락) 판정. required_strong/required_weak로 나뉜
    카테고리는 약한 키워드가 weak_context와 함께 있을 때만 통과시킨다.
    """
    c = CATEGORIES[cat_key]
    t = _norm(text)
    if "required_strong" in c:
        if any(_norm(k) in t for k in c["required_strong"]):
            return True
        weak = c.get("required_weak", [])
        if any(_norm(k) in t for k in weak):
            return any(_norm(k) in t for k in c.get("weak_context", []))
        return False
    return any(_norm(k) in t for k in c["required"])


# ── 1) 구글 뉴스 RSS: (A OR B) AND (C OR D) NOT(...) 완전 지원 ──────────────
def build_google_query(cat_key: str, days: int = 30) -> str:
    """(필수 OR ...) AND (조합 OR ...) -노이즈 -노이즈 ... when:30d

    required_strong/required_weak로 나뉜 카테고리는 두 리스트를 합쳐 넓게 검색어를
    구성한다 — weak_context 문맥 판정은 검색 단계가 아니라 결과를 받은 뒤
    `match_loose()`(사후 필터)에서 적용한다.
    """
    c = CATEGORIES[cat_key]
    q = lambda k: f'"{k}"' if " " in k else k
    required = " OR ".join(q(k) for k in _required_list(cat_key))
    combine  = " OR ".join(q(k) for k in c["combine"])
    negative = " ".join(f"-{q(n)}" for n in NOISE_KEYWORDS)
    return f"({required}) AND ({combine}) {negative} when:{days}d"


def google_news_rss_url(cat_key: str, days: int = 30) -> str:
    q = quote_plus(build_google_query(cat_key, days))
    return f"https://news.google.com/rss/search?q={q}&hl=ko&gl=KR&ceid=KR%3Ako"


# ── 2) 네이버 뉴스 API: 복합 불리언 미지원 → 단순 질의 × N + 사후 필터 ──────
def build_naver_queries(cat_key: str) -> list[str]:
    return CATEGORIES[cat_key]["naver_queries"]


def naver_news_api_url(query: str, display: int = 100, start: int = 1) -> str:
    return ("https://openapi.naver.com/v1/search/news.json"
            f"?query={quote_plus(query)}&display={display}&start={start}&sort=date")


# ── 3) 사후 매칭: 느슨한 매칭(필수 1개면 통과) + 점수화 ────────────────────
def match_loose(text: str, cat_key: str) -> bool:
    """필수 키워드가 하나라도 있으면 통과(약한 키워드는 문맥 필요). 조합 키워드는 점수에만 반영."""
    return _has_required_match(text, cat_key)


def keyword_score(text: str, cat_key: str) -> int:
    t = _norm(text)
    c = CATEGORIES[cat_key]
    hit_req = sum(1 for k in _required_list(cat_key) if _norm(k) in t)
    hit_com = sum(1 for k in c["combine"]  if _norm(k) in t)
    # "세무조사"는 combine 목록에 없다(단독 매칭 금지, ADDENDUM-3 §5-2) — 조합 조건을
    # 만족할 때만 combine 히트 하나로 친다.
    if cat_key == "tax" and matches_tax_investigation_combo(text):
        hit_com += 1
    return min(100, hit_req * 20 + hit_com * 10)


def matched_keywords(text: str, cat_key: str) -> list[str]:
    t = _norm(text)
    c = CATEGORIES[cat_key]
    hits = [k for k in (_required_list(cat_key) + c["combine"]) if _norm(k) in t]
    if cat_key == "tax" and matches_tax_investigation_combo(text):
        hits.append("세무조사")
    return hits


def classify(text: str) -> str | None:
    """가장 점수가 높은 카테고리 1개로 확정. 어디에도 안 걸리면 None(=버림)."""
    scored = [(k, keyword_score(text, k)) for k in CATEGORIES if match_loose(text, k)]
    if not scored:
        return None
    return max(scored, key=lambda x: x[1])[0]


def _norm(s: str) -> str:
    return re.sub(r"\s+", "", (s or "")).lower()


# ── 4) 노이즈 필터 (tier 1 공식기관은 면제) ───────────────────────────────
def is_noise(text: str, tier: int = 5) -> bool:
    if tier == 1:
        return False
    t = _norm(text)
    return any(_norm(n) in t for n in NOISE_KEYWORDS)


# ── 4-1) 조직 운영성 공지 제외 (SPEC-ADDENDUM-4.md §1) ──────────────────────
def is_admin_noise(title: str) -> bool:
    """기관의 인사·조직·운영 공지 판정. **계층(tier)과 무관하게 적용**한다 —
    L1(공식기관)도 NOISE_KEYWORDS는 면제받지만 이 판정은 면제받지 않는다.
    각 어댑터가 `classify()`/카테고리 확정 이전에 이 함수로 먼저 걸러야 한다.
    """
    t = _norm(title)
    return any(_norm(k) in t for k in ADMIN_NOISE_KEYWORDS)


# ── 4-1b) 행사·포럼 안내 제외 보강 (SPEC-ADDENDUM-7.md §4) ──────────────────
# "제N회"/"제N차" 패턴. 영문 행사 표현(Forum 등)은 ADMIN_NOISE_KEYWORDS에 이미
# 포함돼 있어 is_admin_noise() 쪽에서 잡힌다 — 이 정규식은 그걸로 못 잡는
# "제149회 OO" 처럼 숫자 회차로만 식별되는 경우를 추가로 잡기 위한 것이다.
_SERIAL_EVENT_RE = re.compile(r"제\s*\d+\s*[회차]")


def is_event_announcement(title: str) -> bool:
    """행사·운영 공지 판정(§4-2). `is_admin_noise()`의 상위 호환 —
    ADMIN_NOISE_KEYWORDS 매칭에 더해 "제N회/제N차" 패턴을 규제 신호 유무로
    한 번 더 본다. §5 처리순서 2번(수집 단계) — google_news.py/naver_news.py의
    is_noise_l3()와 각 공식 어댑터가 기존 is_admin_noise() 대신 이 함수를 쓴다.

    "회계기준위원회 제12차 회의 결과"처럼 강한 신호 없이 회차 번호만 있는
    제목도 걸릴 것 같지만, `_norm()`이 공백을 지우면서 "회의 결과"가
    "회의결과"가 되고 그 안에 강한 신호 "의결"이 부분 문자열로 우연히 포함돼
    실제로는 안 걸린다(§4 "주의" 사례와 동일한 부분일치 특성 — is_discussion_
    material()의 `_norm_keep_spaces()` 도입 배경이 된 바로 그 현상). 이 함수가
    특별 취급을 하는 게 아니라 `_norm()`을 다른 함수들과 똑같이 쓴 결과다.
    """
    t = _norm(title)
    if any(_norm(k) in t for k in ADMIN_NOISE_KEYWORDS):
        return True
    if _SERIAL_EVENT_RE.search(title):
        return not any(_norm(k) in t for k in EVENT_ANNOUNCEMENT_STRONG_SIGNALS)
    return False


# ── 4-2) 적용 대상 판정 게이트 (SPEC-ADDENDUM-6.md §1) ──────────────────────
def is_applicable(title: str, body: str = "") -> tuple[bool, str | None]:
    """이 규제가 우리 조직(비금융 일반 제조법인)에 적용되는지 판정.

    "이게 회계·세무 주제인가"가 아니라 "적용 대상에 우리가 포함되는가"를 묻는다
    (§0-2). **L1/L2/L3 전 계층에 적용** — 호출부(main.py)가 tier/layer로 면제
    처리하지 않는다(§1-2, 기존 필터들과의 핵심 차이).

    Returns:
        (적용여부, 제외사유). 적용되면 (True, None).
    """
    t = _norm(title + " " + body)

    for scope, kws in APPLICABILITY["excluded_entities"].items():
        if any(_norm(k) in t for k in kws):
            return False, f"excluded:{scope}"

    if any(_norm(k) in t for k in APPLICABILITY["foreign_jurisdiction"]):
        if not any(_norm(k) in t for k in APPLICABILITY["foreign_exception_context"]):
            return False, "excluded:foreign"

    return True, None


def apply_applicability_gate(items: list[dict]) -> tuple[list[dict], list[dict]]:
    """items 전체(L1/L2/L3 구분 없이)에 `is_applicable()`을 적용해 (통과분, 제외분)을
    반환한다. 제외분에는 `excluded_reason`을 채워 넣어 `main.py`가 로그로 남길 수
    있게 한다(§1-3). 반드시 다른 필터들보다 먼저, `main.build_data_json()`에서
    `dedupe()` 이전에 호출한다.
    """
    kept, excluded = [], []
    for it in items:
        ok, reason = is_applicable(it.get("title", ""))
        if ok:
            kept.append(it)
        else:
            it = dict(it, excluded_reason=reason)
            excluded.append(it)
    return kept, excluded


# ── 5) 신뢰도 ────────────────────────────────────────────────────────────
def trust_of(url: str) -> tuple[int, int, str]:
    """returns (tier, score, source_name)"""
    u = url or ""
    if "://" not in u:
        u = "//" + u  # 스킴 없는 순수 도메인(예: RSS <source> 힌트)도 netloc으로 파싱되게
    host = (urlparse(u).hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    for tier, score, domains in TRUST_TIERS:
        for dom, name in domains.items():
            if host == dom or host.endswith("." + dom):
                return tier, score, name
    return DEFAULT_TIER, DEFAULT_TRUST, host or "기타"


def recency_score(published: date, today: date | None = None) -> int:
    base = today or date.today()
    d = (base - published).days
    return max(0, 100 - d * 6)


def final_score(trust: int, kw: int, rec: int) -> float:
    return round(trust * 0.55 + kw * 0.30 + rec * 0.15, 2)


# ── 6) 중복 제거 ─────────────────────────────────────────────────────────
def make_id(url: str) -> str:
    canon = re.sub(r"[?#].*$", "", (url or "").strip().lower())
    return hashlib.sha1(canon.encode()).hexdigest()[:16]


def make_id_exact(url: str) -> str:
    """`make_id()`와 달리 쿼리스트링/프래그먼트를 지우지 않는다.

    `make_id()`는 뉴스 URL의 추적 파라미터(?utm_source=...)를 무시하려고 일부러
    쿼리스트링을 지운다 — 뉴스 중복 제거엔 맞는 설계다. 하지만 정부 사이트
    상세 페이지처럼 **쿼리 파라미터 자체가 유일 식별자**인 URL(예:
    `lsInfoP.do?lsiSeq=123`, `view.do?nttId=456`, 목록+프래그먼트 앵커)에
    `make_id()`를 쓰면 경로가 같은 모든 항목이 같은 id로 뭉개져버린다
    (실측: law_api.py 18건이 dedupe에서 1건으로 뭉개지는 버그로 발견됨).
    공식 어댑터(kasb/fss/moef/nts/policy_briefing/law_api)는 전부 이 함수를 쓴다.
    """
    canon = (url or "").strip().lower()
    return hashlib.sha1(canon.encode()).hexdigest()[:16]


def dedupe(items: list[dict]) -> list[dict]:
    """URL 해시 + 제목 정규화(전체 일치) 이중 제거. 신뢰도 높은 쪽을 남긴다.

    id 또는 정규화된 제목이 겹치는 항목들을 같은 그룹으로 묶은 뒤(Union-Find),
    그룹마다 final_score가 가장 높은 항목 하나만 남긴다.
    """
    n = len(items)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    key_owner: dict[str, int] = {}
    for i, it in enumerate(items):
        for key in (it["id"], "T:" + _norm(it["title"])):
            if key in key_owner:
                union(i, key_owner[key])
            else:
                key_owner[key] = i

    groups: dict[int, list[int]] = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)

    out = [items[max(idxs, key=lambda i: items[i]["final_score"])] for idxs in groups.values()]
    out.sort(key=lambda x: -x["final_score"])
    return out


# ── 7) 문서 종류 판정 (SPEC-ADDENDUM-2.md §4) ───────────────────────────────
def doc_type_of(title: str, source_tier: int = 1) -> str:
    """제목 기준 doc_type 판정. 어디에도 안 걸리고 tier>=4면 '기사', 아니면 '보도자료'.

    DOC_TYPE_RULES는 앞쪽 규칙이 우선이다("개정"보다 "공개초안"이 먼저 걸려야
    "K-IFRS 제1116호 개정안 공개초안"이 공개초안으로 판정된다).
    """
    t = _norm(title)
    for dtype, kws in DOC_TYPE_RULES:
        if any(_norm(k) in t for k in kws):
            return dtype
    return "기사" if source_tier >= 4 else "보도자료"


def _norm_keep_spaces(s: str) -> str:
    """`_norm()`과 달리 공백을 지우지 않고 한 칸으로만 정리한다.

    "회의 결과"처럼 두 어절짜리 키워드는 `_norm()`으로 공백을 전부 지우면
    "회의결과"가 되어 그 안에 override 키워드 "의결"이 우연히 부분 문자열로
    끼어버린다(2026-08-28 실측으로 발견). `is_discussion_material()`처럼 다어절
    구문을 다루는 곳에서만 이 정규화를 쓴다.
    """
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def is_discussion_material(title: str) -> bool:
    """TF·실무그룹 중간 산출물 판정(2026-08-28 사용자 피드백). 제목에 확정을
    뜻하는 표현(의결·공표·제정·개정·확정)이 함께 있으면 재분류하지 않는다
    (사용자 지시 — 이미 결론이 난 문서를 논의자료로 숨기면 안 되므로).
    `finalize_item()`에서 doc_type을 최종 확정하기 직전에 호출해, 어댑터가
    doc_type을 `doc_type_of()`로 판정했든 하드코딩했든 상관없이 일관되게 적용한다.
    """
    t = _norm_keep_spaces(title)
    if any(_norm_keep_spaces(k) in t for k in DISCUSSION_OVERRIDE_KEYWORDS):
        return False
    return any(_norm_keep_spaces(k) in t for k in DISCUSSION_MATERIAL_KEYWORDS)


# ── 해외 기준 처리 — 안 A: 별도 분류 (SPEC-ADDENDUM-7.md §3) ────────────────
def is_foreign_standard(title: str) -> bool:
    """IASB/ISSB 발신 항목인지 판정(§3-2 안 A). True면 `finalize_item()`이
    doc_type을 "해외기준"으로 재분류해 기본 조회/오늘의 정책동향에서 뺀다
    (완전 제외가 아니다 — EFRAG/FASB/SEC 등과 달리 K-IFRS/KSSB의 원천이라
    수집은 유지). §3-4: 국내 도입 맥락(APPLICABILITY.foreign_exception_context)이
    함께 있으면 정상 항목으로 취급한다(False 반환).

    안 B(전면 제외)로 전환하려면 이 함수를 안 쓰고 FOREIGN_STANDARD_BODIES를
    `APPLICABILITY.foreign_jurisdiction`으로 옮기면 된다(§3-3, _config.py 참고).
    """
    t = _norm(title)
    if not any(_norm(k) in t for k in FOREIGN_STANDARD_BODIES):
        return False
    if any(_norm(k) in t for k in APPLICABILITY["foreign_exception_context"]):
        return False
    return True


# ── 8) 시행일 추출 (SPEC-ADDENDUM.md §4-4) ──────────────────────────────────
_EFFECTIVE_DATE_PATTERNS = [
    # "2027년 1월 1일 이후 개시하는 사업연도부터" / "2026년 1월 1일부터 적용"
    re.compile(r"(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일\s*(?:이후\s*개시(?:하는)?\s*사업연도부터|부터\s*적용|부터\s*시행)"),
    # "2026. 7. 1. 시행"
    re.compile(r"(\d{4})\s*[.년]\s*(\d{1,2})\s*[.월]\s*(\d{1,2})\s*[.일]?\s*(?:부터\s*)?시행"),
]
_PROMULGATION_DELAY_RE = re.compile(r"공포\s*후\s*(\d+)\s*개월\s*(?:이\s*)?경과한?\s*날부터\s*시행")


def extract_effective_date(text: str, promulgation_date: date | None = None) -> str | None:
    """본문 텍스트에서 시행일을 뽑아 'YYYY-MM-DD' 문자열로 반환. 실패하면 None.

    "공포 후 N개월이 경과한 날부터 시행" 패턴은 promulgation_date가 있어야 계산할 수
    있다 — 없으면 이 패턴은 건너뛴다(호출부가 로그를 남기고 수동 보완하도록).
    """
    t = text or ""
    for pat in _EFFECTIVE_DATE_PATTERNS:
        m = pat.search(t)
        if m:
            y, mo, d = (int(x) for x in m.groups())
            try:
                return date(y, mo, d).isoformat()
            except ValueError:
                continue
    m = _PROMULGATION_DELAY_RE.search(t)
    if m and promulgation_date is not None:
        months = int(m.group(1))
        return _add_months(promulgation_date, months).isoformat()
    return None


# ── 8-1) 제목에서 개정·제정일 추출 (SPEC-ADDENDUM-4.md §2-1) ────────────────
# "상시 비치 자료" 게시판(예: fss.py의 k-icfr.org 모범규준)은 published_at이
# 없어 수집일로 대체되면 "오늘 나온 자료"처럼 보인다. 제목에 박힌 개정일을
# 뽑아 published_at으로 쓰고, 실패하면 호출부가 date_estimated=True를 세운다.
_TITLE_DATE_4DIGIT_RE = re.compile(r"(\d{4})\s*[.]\s*(\d{1,2})\s*[.]\s*(\d{1,2})\s*[.]?")
_TITLE_DATE_2DIGIT_RE = re.compile(r"['‘](\d{2})\s*[.]\s*(\d{1,2})\s*[.]\s*(\d{1,2})")
# "모범규준(2012.12)"/"新모범규준(2018.6)"처럼 일(day) 없이 연.월만 있는 경우
# (2026-08-28 실사용 확인: 이 패턴을 못 잡아 오늘 날짜로 새서 필터를 통과했었다).
# 위 두 패턴이 먼저 시도되고 실패했을 때만 쓰이므로 뒤에 일자가 더 있는 경우와는
# 겹치지 않는다. 일(day)은 1일로 고정.
_TITLE_DATE_YEAR_MONTH_RE = re.compile(r"(\d{4})\s*[.]\s*(\d{1,2})(?!\s*[.]?\s*\d)")


def extract_title_revision_date(title: str) -> str | None:
    """"(2021.10.1. 개정)", "('24.12.23 개정)", "Clean ver.('24.12.23)",
    "(2012.12)"(일자 없음) 등에서 날짜를 뽑아 'YYYY-MM-DD'로 반환한다. 못 찾으면 None.
    """
    t = title or ""
    m = _TITLE_DATE_4DIGIT_RE.search(t)
    if m:
        y, mo, d = (int(x) for x in m.groups())
        try:
            return date(y, mo, d).isoformat()
        except ValueError:
            pass
    m = _TITLE_DATE_2DIGIT_RE.search(t)
    if m:
        yy, mo, d = (int(x) for x in m.groups())
        try:
            return date(2000 + yy, mo, d).isoformat()
        except ValueError:
            pass
    m = _TITLE_DATE_YEAR_MONTH_RE.search(t)
    if m:
        y, mo = (int(x) for x in m.groups())
        try:
            return date(y, mo, 1).isoformat()
        except ValueError:
            pass
    return None


def matches_tax_investigation_combo(text: str) -> bool:
    """SPEC-ADDENDUM-3.md §5-2: "세무조사"는 단독 매칭하지 않고
    세무조사 + (사전통지 | 대상 선정 | 운영규정 | 절차 | 기간 연장 | 납세자권리)
    조합으로만 매칭한다. keyword_score()/matched_keywords()가 tax 카테고리에서
    이 함수 결과를 추가로 반영한다.
    """
    t = _norm(text)
    trigger = _norm(TAX_INVESTIGATION_COMBO["trigger"])
    if trigger not in t:
        return False
    return any(_norm(q) in t for q in TAX_INVESTIGATION_COMBO["qualifiers"])


# ── 9) 세법 카테고리 노이즈 보강 (SPEC-ADDENDUM.md §5) ──────────────────────
def is_incident_noise(text: str, tier: int = 5) -> bool:
    """사건·사고 기사 제외. L3(뉴스)에만 적용 — tier==1(L1 공식기관)은 면제.

    제목에 INCIDENT_KEYWORDS가 있고 **동시에** PROCEDURAL_KEYWORDS(개정·시행령·
    예규·지침)가 **없으면** 노이즈로 본다. AND 조건인 이유: "탈세 혐의 판결에
    따른 예규 변경" 같은 실무 관련 기사를 잃지 않기 위함(ADDENDUM.md §5-1).
    """
    if tier == 1:
        return False
    t = _norm(text)
    has_incident = any(_norm(k) in t for k in INCIDENT_KEYWORDS)
    if not has_incident:
        return False
    has_procedural = any(_norm(k) in t for k in PROCEDURAL_KEYWORDS)
    return not has_procedural


# ── 규제성 판정 게이트 (SPEC-ADDENDUM-5.md §1) ──────────────────────────────
def has_regulatory_signal(title: str) -> bool:
    """제목에 "제도가 바뀌었다"는 신호가 있는지. L3 통과의 필요조건(§1)."""
    t = _norm(title)
    return any(_norm(k) in t for k in REGULATORY_SIGNALS)


# ── 타사 홍보성 보도 제외 (SPEC-ADDENDUM-5.md §3) ───────────────────────────
def is_corporate_pr(title: str) -> bool:
    """타사 홍보성 보도 판정. 홍보 동사가 있으면서 강한 규제 신호(제도 변경
    절차)가 없으면 홍보성으로 본다(§3)."""
    t = _norm(title)
    if not any(_norm(k) in t for k in CORPORATE_PR_KEYWORDS):
        return False
    return not any(_norm(k) in t for k in CORPORATE_PR_STRONG_SIGNALS)


# ── 개별 기업 소식 제외 (SPEC-ADDENDUM-7.md §1) ─────────────────────────────
# "상장"/"비상"은 COMPANY_EVENTS 평문 키워드 목록에 없다(부분일치 오탐 실측—
# _config.COMPANY_EVENTS 주석 참고). 부정 전방탐색으로 "상장사"/"상장기업"/
# "상장법인"/"상장회사"(회사 상태를 가리키는 일반 명사), "비상장"(그 부정형)은
# 걸러내고 "상장 확정"/"상장 추진"처럼 실제 이벤트만 잡는다.
_LISTING_EVENT_RE = re.compile(r"상장(?!사|기업|법인|회사)")
_EMERGENCY_RE = re.compile(r"비상(?!장)")


def is_company_event(title: str) -> bool:
    """개별 기업 소식·시황 기사 판정(§1-1). `is_corporate_pr()`이 홍보 동사(가동·
    맞손)를 잡는다면, 이건 특정 기업의 자본시장 이벤트·실적·재무위기·시황을 잡는다
    — "규제가 바뀐 게 아니라 한 회사의 개별 사정"인 기사(§0 공통 원인).

    §1-2 제조업 회계 예외: 개별 기업 사례라도 제조업 회계기준과 직결되면
    (재고자산·감가상각 등) 통과시킨다 — 실무 참고 가치가 크다는 사용자 요청.
    """
    t = _norm(title)
    has_event_kw = (any(_norm(k) in t for k in COMPANY_EVENTS)
                    or bool(_LISTING_EVENT_RE.search(title))
                    or bool(_EMERGENCY_RE.search(title)))
    if not has_event_kw:
        return False
    if any(_norm(k) in t for k in MANUFACTURING_ACCOUNTING_CONTEXT):
        return False  # §1-2 예외
    return not any(_norm(k) in t for k in COMPANY_EVENT_STRONG_SIGNALS)


def is_noise_l3(text: str, tier: int, category: str) -> bool:
    """L3(뉴스) 전용 종합 노이즈 판정(수집 단계에서 적용). 기존 `is_noise()`
    (NOISE_KEYWORDS)에 사건·사고 필터(`is_incident_noise`)와 세목 화이트리스트
    (`pass_tax_filter`, tax 카테고리만)를 OR로 더한다. tier==1(L1 공식기관)은
    전부 면제(기존 is_noise와 동일 원칙) — 단 `is_event_announcement`(조직 운영
    공지 + 행사·포럼 안내, ADDENDUM-4 §1 + ADDENDUM-7 §4)만은 tier 무관하게
    적용한다.

    §1(규제성 게이트)·§3(홍보성 제외)는 여기 없다 — 2026-08-31 사용자 지시로
    "§5(중복제거) → §1 → §3" 순서를 적용하기 위해 `main.build_data_json()`의
    `dedupe_similar_news()` 다음 단계(`apply_regulatory_gate`/
    `apply_corporate_pr_filter`)로 옮겼다. 그래야 §1/§3에 걸려 사라졌을 기사도
    §5 중복 병합의 후보(및 duplicate_count 집계 대상)에 먼저 포함된다.
    """
    if is_event_announcement(text):
        return True
    if tier == 1:
        return False
    if is_noise(text, tier=tier):
        return True
    if is_incident_noise(text, tier=tier):
        return True
    if category == "tax" and not pass_tax_filter(category=category, layer="L3", text=text):
        return True
    return False


# ── 10) 세목 화이트리스트 (SPEC-ADDENDUM-3.md §3) ───────────────────────────
def match_tax_subject(text: str) -> list[str]:
    """활성 세목 중 매칭되는 것들의 key 리스트를 반환.

    `TAX_SUBJECTS`가 비어있으면(설정 파일 없음/파싱 실패) **전체 통과**로 보고
    빈 리스트 대신 `["_all"]`을 반환한다 — `_config._load_tax_subjects()`의
    "조용히 0건이 되는 것보다 낫다" 원칙을 여기서도 지킨다.
    """
    if not TAX_SUBJECTS:
        return ["_all"]
    t = _norm(text)
    return [s["key"] for s in TAX_SUBJECTS if any(_norm(k) in t for k in s["keywords"])]


def pass_tax_filter(*, category: str, layer: str, text: str) -> bool:
    """계층에 따라 세목 필터 적용 여부를 결정한다(ADDENDUM-3 §3 표).

    - category != "tax": 세목 필터 대상이 아니므로 항상 통과.
    - layer == "L1_comprehensive"(세제개편안·개정세법 해설 등 전 세목 포괄 문서): 면제, 항상 통과.
    - 그 외(L1 법령은 화이트리스트 방식이 이미 law_api.py의 법령명 정확일치로
      처리되고 있어 이 함수 대상이 아님. L2/L3): 세목 매칭 필요.
    """
    if category != "tax":
        return True
    if layer == "L1_comprehensive":
        return True
    return bool(match_tax_subject(text))


# ── 11) 계층별 정렬·상한 (SPEC-ADDENDUM.md §1) ──────────────────────────────
def layer_of(item: dict) -> str:
    """items[]의 계층. 어댑터가 'layer'를 명시 안 했으면(뉴스 수집기 등) L3로 간주한다."""
    return item.get("layer") or "L3"


def _tier_of(item: dict) -> int:
    """공식 어댑터(중첩 source.tier)와 뉴스 어댑터(평면 trust_tier) 두 raw item
    모양을 다 지원한다 — Phase 4에서 완전히 합쳐지기 전까지의 과도기 대응."""
    src = item.get("source")
    if isinstance(src, dict) and "tier" in src:
        return src["tier"]
    return item.get("trust_tier", DEFAULT_TIER)


def sort_by_layer_then_score(items: list[dict]) -> list[dict]:
    """SPEC-ADDENDUM.md §1: 정렬 시 L1/L2를 항상 L3보다 위에 놓는다.
    final_score 비교 이전에 계층으로 먼저 가른다.
    """
    def key(it):
        rank = 0 if layer_of(it) in ("L1", "L2", "L1_comprehensive") else 1
        return (rank, -it.get("final_score", 0))
    return sorted(items, key=key)


def apply_category_caps(items: list[dict]) -> list[dict]:
    """카테고리별 상한 적용(ADDENDUM.md §1). L1/L2(공식)는 무제한(`MAX_OFFICIAL_PER_CATEGORY`),
    L3(뉴스)는 `MAX_NEWS_PER_CATEGORY` — 그중 tier4(종합 경제지)는 먼저
    `MAX_TIER4_PER_CATEGORY`로 서브캡한 뒤 나머지 뉴스와 합쳐 최종 상한을 적용한다.
    카테고리별로 계층 정렬(L1/L2 먼저)까지 마친 리스트를 반환한다.
    """
    by_cat: dict[str, list[dict]] = {}
    for it in items:
        by_cat.setdefault(it["category"], []).append(it)
    # CATEGORIES 순서(kifrs/tax/icfr/esg)로 고정 — 입력 순서에 좌우되지 않게.
    cat_order = [c for c in CATEGORIES if c in by_cat] + [c for c in by_cat if c not in CATEGORIES]

    out: list[dict] = []
    for cat in cat_order:
        cat_items = by_cat[cat]
        official = [it for it in cat_items if layer_of(it) in ("L1", "L2", "L1_comprehensive")]
        news = [it for it in cat_items if layer_of(it) == "L3"]

        tier4 = sorted((it for it in news if _tier_of(it) == 4), key=lambda x: -x.get("final_score", 0))
        other_news = [it for it in news if _tier_of(it) != 4]
        news_pool = sorted(other_news + tier4[:MAX_TIER4_PER_CATEGORY], key=lambda x: -x.get("final_score", 0))
        capped_news = news_pool[:MAX_NEWS_PER_CATEGORY]

        out.extend(official + capped_news)
    # SPEC-ADDENDUM.md §1: 최종 배열 정렬도 계층 우선(L1/L2 먼저) + final_score DESC.
    return sort_by_layer_then_score(out)


def _add_months(d: date, months: int) -> date:
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    # 말일 보정(예: 1/31 + 1개월 → 2/28)
    day = d.day
    while True:
        try:
            return date(year, month, day)
        except ValueError:
            day -= 1


# ── 12) stage 판정 (SPEC-ADDENDUM-2.md §2-2) ────────────────────────────────
_KST = timezone(timedelta(hours=9))


def compute_stage(doc_type: str) -> str:
    """doc_type만으로 stage를 정한다. "시행예정"/"시행중" 구분은 날짜에 따라
    바뀌므로 여기서 계산하지 않고 프론트엔드가 effective_date로 매번 계산한다
    (ADDENDUM-2 §2-2) — 그래서 이 함수는 "확정"까지만 반환한다.
    """
    if doc_type in ("공개초안", "검토의견"):
        return "의견수렴"
    if doc_type in ("제·개정", "적용지침", "모범규준", "감사·검토기준"):
        return "확정"
    return "참고"


# ── 13) 뉴스(L3) raw item → 최종 스키마 정규화 ──────────────────────────────
def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def normalize_news_item(raw: dict, *, source_type: str = "news") -> dict:
    """google_news.py/naver_news.py의 평면(raw) item 모양을
    공식 어댑터들과 같은 최종 스키마 모양으로 맞춘다(Phase 4 main.py에서 사용).

    raw item 필수 키: id, category, title, url, published(date|None), source_name,
    source_domain, trust_tier, trust_score, keyword_score, matched_keywords, is_noise.
    """
    published = raw.get("published")
    published_at = published.isoformat() if published else None
    rec = recency_score(published) if published else 0
    trust = raw.get("trust_score", DEFAULT_TRUST)
    kw = raw.get("keyword_score", 0)
    category = raw["category"]
    title = raw["title"]
    tier = raw.get("trust_tier", DEFAULT_TIER)
    return {
        "id": raw["id"],
        "category": category,
        "doc_type": doc_type_of(title, source_tier=tier),
        "title": title,
        "summary": [],
        "impact": None,
        "published_at": published_at,  # None이면 main.py에서 collected_at 날짜로 대체(SPEC §4 필드 규칙)
        "collected_at": _now_kst_iso(),
        "effective_date": None,  # L3 뉴스는 시행일 추출 대상이 아님(공식 소스가 담당)
        "source": {"name": raw.get("source_name"), "domain": raw.get("source_domain"), "tier": tier, "type": source_type},
        "trust_score": trust,
        "keyword_score": kw,
        "final_score": final_score(trust, kw, rec),
        "matched_keywords": raw.get("matched_keywords", []),
        "urls": {"news": raw.get("url"), "official": None},
        "law_meta": None,
        "attachments": None,
        "layer": "L3",
        "is_noise": raw.get("is_noise", False),
    }


# ── 14-1) 유사 기사 중복 제거 (SPEC-ADDENDUM-4.md §3, SPEC-ADDENDUM-5.md §5로 개선) ─
# "- 스트레이트뉴스" 같은 매체명 접미사, "[로컬 게시판/...]" 같은 대괄호 접두사가
# 어절 집합에 섞이면 유사도가 희석된다(ADDENDUM-5 §5-1 실측 확인) — 비교 전용으로
# 제목을 정제한다. 표시용 title은 절대 건드리지 않는다.
_MEDIA_SUFFIX_RE = re.compile(r"\s*[-–—|]\s*[^-–—|\s]{2,15}$")
# ↑ 매체명은 보통 공백 없는 한 단어 브랜드명(스트레이트뉴스·조세일보·CPA뉴스 등)이라
#   트레일링 세그먼트에 공백이 없을 때만 매체명 접미사로 본다. ADDENDUM-5 원안은
#   공백까지 허용해서 "법인세법 시행령 개정안 — 접대비 한도" 같은 제목의 "접대비
#   한도"(공백 포함, 2어절)까지 매체명으로 오인해 지워버리는 문제가 있었다(§5-4가
#   명시적으로 "묶이면 안 된다"고 한 바로 그 케이스) — 그래서 `\s`를 제외해 고쳤다.
_BRACKET_PREFIX_RE = re.compile(r"^\s*[\[\(【][^\]\)】]{1,30}[\]\)】]\s*")
_QUOTE_RE = re.compile(r"[\"'‘’“”`]")


def clean_title_for_compare(title: str) -> str:
    """중복 비교 전용 제목 정제(ADDENDUM-5 §5-2). 표시용 title은 건드리지 않는다.

    ","와 "·"는 여기서 지우지 않는다 — `extract_subject()`가 "남부발전, ..."의
    쉼표를 주체 경계로 써야 하는데, 이 함수를 먼저 거치기 때문이다(원안 코드는
    쉼표까지 공백으로 바꿔버려서 정작 자기 자신이 쓰는 §5-3 예시("남부발전, ...")의
    주체 추출을 깨뜨리는 문제가 있었다 — 실제로 걸려서 고침). 어차피
    `title_similarity()`의 어절 추출 정규식(`[가-힣A-Za-z0-9]+`)은 쉼표·가운뎃점을
    이미 구분자로 취급하므로 지우지 않아도 유사도 계산에는 차이가 없다.
    """
    t = title or ""
    t = _BRACKET_PREFIX_RE.sub("", t)
    t = _MEDIA_SUFFIX_RE.sub("", t)
    t = _QUOTE_RE.sub("", t)
    t = re.sub(r"[…、]", " ", t)
    return t.strip()


def title_similarity(a: str, b: str) -> float:
    """정제된 제목을 어절 단위로 쪼개 자카드 유사도 계산(ADDENDUM-5 §5-2)."""
    ta = set(re.findall(r"[가-힣A-Za-z0-9]+", clean_title_for_compare(a)))
    tb = set(re.findall(r"[가-힣A-Za-z0-9]+", clean_title_for_compare(b)))
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def extract_subject(title: str) -> str | None:
    """제목 앞부분의 주체명 추출(ADDENDUM-5 §5-3). "남부발전, ..." → "남부발전"."""
    t = clean_title_for_compare(title)
    m = re.match(r"^([가-힣A-Za-z0-9]{2,12})\s*[,·]", t)
    return m.group(1) if m else None


def _within_days(a_iso: str | None, b_iso: str | None, window: int) -> bool:
    if not a_iso or not b_iso:
        return False
    try:
        da, db = date.fromisoformat(a_iso), date.fromisoformat(b_iso)
    except ValueError:
        return False
    return abs((da - db).days) <= window


def dedupe_similar_news(items: list[dict]) -> list[dict]:
    """L3(뉴스)끼리만 정제된 제목 유사도로 병합한다(ADDENDUM-4 §3, ADDENDUM-5 §5로
    개선). L1/L2는 완전 일치만 중복 처리하는 기존 `dedupe()`가 이미 처리했으므로
    건드리지 않는다.

    같은 카테고리 안에서 다음 중 하나라도 만족하면 동일 사안으로 보고 병합한다
    (ADDENDUM-5 §5-3):
      (a) title_similarity(정제본) >= SIMILARITY_THRESHOLD(0.55) — 날짜 무관
      (b) extract_subject()가 서로 같고 + published_at이 SIMILARITY_DAY_WINDOW일
          이내 + title_similarity(정제본) >= SUBJECT_SIMILARITY_THRESHOLD(0.35)

    final_score가 가장 높은 것만 남기고, 남은 항목에 `duplicate_count`/
    `duplicate_sources`를 기록한다("외 N건 보도" 표시용).
    """
    news = [it for it in items if layer_of(it) == "L3"]
    others = [it for it in items if layer_of(it) != "L3"]

    by_cat: dict[str, list[dict]] = {}
    for it in news:
        by_cat.setdefault(it["category"], []).append(it)

    kept: list[dict] = []
    for cat_items in by_cat.values():
        cat_items = sorted(cat_items, key=lambda x: -x.get("final_score", 0))
        absorbed: set[int] = set()
        for i, it in enumerate(cat_items):
            if i in absorbed:
                continue
            sources = [it["source"]["name"]]
            subject_i = extract_subject(it["title"])
            for j in range(i + 1, len(cat_items)):
                if j in absorbed:
                    continue
                other = cat_items[j]
                sim = title_similarity(it["title"], other["title"])
                is_dup = sim >= SIMILARITY_THRESHOLD  # 조건 (a)
                if not is_dup and subject_i and subject_i == extract_subject(other["title"]):
                    if (sim >= SUBJECT_SIMILARITY_THRESHOLD
                            and _within_days(it.get("published_at"), other.get("published_at"), SIMILARITY_DAY_WINDOW)):
                        is_dup = True  # 조건 (b)
                if is_dup:
                    absorbed.add(j)
                    sources.append(other["source"]["name"])
            if len(sources) > 1:
                it["duplicate_count"] = len(sources) - 1
                it["duplicate_sources"] = sources
            kept.append(it)
    return others + kept


# ── 14-1b) §5 이후 순서로 옮긴 §1/§3 게이트 (2026-08-31 사용자 지시) ─────────
# main.build_data_json()에서 dedupe_similar_news() 다음, apply_category_caps()
# 이전에 호출한다. L1/L2(공식 소스)와 tier==1 뉴스는 기존 is_noise_l3와 같은
# 원칙으로 게이트를 면제한다.
def _l3_gate_exempt(item: dict) -> bool:
    """§1/§3 게이트 면제 대상인지. L1/L2(공식 소스) 또는 tier==1 뉴스면 면제."""
    return layer_of(item) != "L3" or item.get("source", {}).get("tier") == 1


def apply_regulatory_gate(items: list[dict]) -> list[dict]:
    """ADDENDUM-5 §1. "제도가 바뀌었다"는 신호 없는 L3 뉴스를 제외한다."""
    return [it for it in items if _l3_gate_exempt(it) or has_regulatory_signal(it["title"])]


def apply_corporate_pr_filter(items: list[dict]) -> list[dict]:
    """ADDENDUM-5 §3. §1 통과분 중 타사 홍보성 보도를 제외한다."""
    return [it for it in items if _l3_gate_exempt(it) or not is_corporate_pr(it["title"])]


def apply_company_event_filter(items: list[dict]) -> list[dict]:
    """ADDENDUM-7 §1. §5 처리순서 7번 — 규제성 게이트(6) 다음, 홍보성 제외(8) 이전에
    호출한다(main.py). `_l3_gate_exempt()`로 L1/L2·tier==1 뉴스는 그대로 면제한다.
    """
    return [it for it in items if _l3_gate_exempt(it) or not is_company_event(it["title"])]


# ── 14-2) 공식 항목에 관련 뉴스 연결 (SPEC-ADDENDUM-4.md §4) ────────────────
_ORG_NAME_STOPWORDS = {
    "금융위원회", "국세청", "기획재정부", "한국회계기준원", "금융감독원",
    "국가법령정보센터", "한국공인회계사회", "내부회계관리제도운영위원회",
}


def extract_core_phrase(title: str) -> str | None:
    """공식 제목에서 기관명을 지우고 남는 어절 중 앞쪽 2~4어절을 "핵심 명사구"
    후보로 삼는다(§4 "핵심 명사구 추출"). 형태소 분석 없는 실용적 근사치다.
    """
    words = [w for w in re.split(r"\s+", (title or "").strip()) if w and w not in _ORG_NAME_STOPWORDS]
    if len(words) < 2:
        return None
    return " ".join(words[:4])


def attach_related_news(items: list[dict]) -> list[dict]:
    """L1/L2 공식 항목에 관련 L3 기사를 최대 `RELATED_NEWS_MAX`건 붙이고
    (`related_news` 필드), 그렇게 붙은 L3 항목은 피드에서 중복 노출하지 않도록
    반환 리스트에서 뺀다(§4 "부수 효과"). `finalize_item()` 이전(= `layer` 필드가
    아직 남아있는) item 리스트를 받아야 한다.

    매칭 조건: 같은 카테고리 + published_at 차이 `RELATED_NEWS_DAY_WINDOW`일 이내 +
    (title_similarity >= `RELATED_NEWS_MIN_SIMILARITY` 또는 핵심 명사구 포함).
    """
    official = [it for it in items if layer_of(it) in ("L1", "L2", "L1_comprehensive")]
    news = [it for it in items if layer_of(it) == "L3"]

    used_ids: set[str] = set()
    for off in official:
        core = extract_core_phrase(off["title"])
        candidates = []
        for n in news:
            if n["id"] in used_ids:
                continue
            if n["category"] != off["category"]:
                continue
            if not _within_days(off.get("published_at"), n.get("published_at"), RELATED_NEWS_DAY_WINDOW):
                continue
            sim = title_similarity(off["title"], n["title"])
            phrase_hit = bool(core) and _norm(core) in _norm(n["title"])
            if sim >= RELATED_NEWS_MIN_SIMILARITY or phrase_hit:
                candidates.append(n)
        candidates.sort(key=lambda n: -n.get("final_score", 0))
        top = candidates[:RELATED_NEWS_MAX]
        off["related_news"] = [
            {
                "title": n["title"],
                "source": n["source"]["name"],
                "url": n["urls"]["news"],
                "published_at": n["published_at"],
            }
            for n in top
        ]
        used_ids.update(n["id"] for n in top)

    return [it for it in items if not (layer_of(it) == "L3" and it["id"] in used_ids)]


# ── 15) 최종 스키마 필드 화이트리스트 (SPEC.md §4 + ADDENDUM-2 stage + ADDENDUM §4-3 attachments
#         + ADDENDUM-4 §2 is_static/date_estimated, §3 duplicate_*, §4 related_news) ──────
# layer/is_noise/_body 등은 파이프라인 내부용이라 최종 JSON에는 안 나간다.
ITEM_FIELDS = [
    "id", "category", "doc_type", "stage", "title", "summary", "impact",
    "published_at", "collected_at", "effective_date", "source",
    "trust_score", "keyword_score", "final_score", "matched_keywords",
    "urls", "law_meta", "attachments",
    "is_static", "date_estimated", "duplicate_count", "duplicate_sources", "related_news",
]


def finalize_item(item: dict) -> dict:
    """stage를 계산해 채우고, published_at 결측 시 collected_at 날짜로 대체하고
    (SPEC §4 필드 규칙), 신규 필드(is_static/date_estimated/duplicate_*/related_news)에
    기본값을 채운 뒤, 허용된 필드만 남겨 최종 스키마 모양으로 만든다.

    doc_type이 여기서 최종 확정된다 — `doc_type_of()`로 판정됐든 어댑터가
    하드코딩했든(예: kasb.py fetch_qna()의 "질의회신" 고정) 상관없이, 여기서
    한 번 더 `is_discussion_material()`을 걸어 "논의자료"로 재분류한다(2026-08-28
    사용자 피드백 — 모든 경로에 일관되게 적용하기 위한 단일 지점). ADDENDUM-7 §3
    (안 A)의 `is_foreign_standard()`도 같은 지점에서 "해외기준"으로 재분류한다 —
    두 조건이 동시에 걸리면(드묾) 해외기준 쪽을 최종값으로 둔다.
    """
    out = {k: item.get(k) for k in ITEM_FIELDS}
    doc_type = item.get("doc_type")
    if is_discussion_material(item.get("title", "")):
        doc_type = "논의자료"
    if is_foreign_standard(item.get("title", "")):
        doc_type = "해외기준"
    out["doc_type"] = doc_type
    out["stage"] = compute_stage(doc_type)
    if not out["published_at"]:
        out["published_at"] = item["collected_at"][:10]
    out["is_static"] = bool(item.get("is_static", False))
    out["date_estimated"] = bool(item.get("date_estimated", False))
    out["duplicate_count"] = int(item.get("duplicate_count") or 0)
    out["duplicate_sources"] = item.get("duplicate_sources") or []
    out["related_news"] = item.get("related_news") or []
    return out
