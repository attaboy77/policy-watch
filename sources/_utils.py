# -*- coding: utf-8 -*-
"""쿼리 생성 / 노이즈 필터 / 신뢰도 / 중복제거 / 날짜파싱 유틸리티.
"""
import hashlib, re
from datetime import date, datetime, timezone, timedelta
from urllib.parse import urlparse, quote_plus
from ._config import (CATEGORIES, NOISE_KEYWORDS, TRUST_TIERS,
                      DEFAULT_TIER, DEFAULT_TRUST, DOC_TYPE_RULES,
                      INCIDENT_KEYWORDS, PROCEDURAL_KEYWORDS, TAX_INVESTIGATION_COMBO,
                      TAX_SUBJECTS, MAX_NEWS_PER_CATEGORY, MAX_TIER4_PER_CATEGORY)


# ── 1) 구글 뉴스 RSS: (A OR B) AND (C OR D) NOT(...) 완전 지원 ──────────────
def build_google_query(cat_key: str, days: int = 30) -> str:
    """(필수 OR ...) AND (조합 OR ...) -노이즈 -노이즈 ... when:30d"""
    c = CATEGORIES[cat_key]
    q = lambda k: f'"{k}"' if " " in k else k
    required = " OR ".join(q(k) for k in c["required"])
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
    """필수 키워드가 하나라도 있으면 통과. 조합 키워드는 점수에만 반영."""
    t = _norm(text)
    return any(_norm(k) in t for k in CATEGORIES[cat_key]["required"])


def keyword_score(text: str, cat_key: str) -> int:
    t = _norm(text)
    c = CATEGORIES[cat_key]
    hit_req = sum(1 for k in c["required"] if _norm(k) in t)
    hit_com = sum(1 for k in c["combine"]  if _norm(k) in t)
    # "세무조사"는 combine 목록에 없다(단독 매칭 금지, ADDENDUM-3 §5-2) — 조합 조건을
    # 만족할 때만 combine 히트 하나로 친다.
    if cat_key == "tax" and matches_tax_investigation_combo(text):
        hit_com += 1
    return min(100, hit_req * 20 + hit_com * 10)


def matched_keywords(text: str, cat_key: str) -> list[str]:
    t = _norm(text)
    c = CATEGORIES[cat_key]
    hits = [k for k in (c["required"] + c["combine"]) if _norm(k) in t]
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


def is_noise_l3(text: str, tier: int, category: str) -> bool:
    """L3(뉴스) 전용 종합 노이즈 판정. 기존 `is_noise()`(NOISE_KEYWORDS)에
    사건·사고 필터(`is_incident_noise`)와 세목 화이트리스트(`pass_tax_filter`,
    tax 카테고리만)를 OR로 더한다 — ADDENDUM.md §5-1의 L3 처리 순서(분류→세목
    필터→노이즈 키워드→사건사고 필터) 중 노이즈/사건사고/세목 세 단계를 한 번에
    반영한 것. tier==1(L1 공식기관)은 전부 면제(기존 is_noise와 동일 원칙).
    """
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


# ── 14) 최종 스키마 필드 화이트리스트 (SPEC.md §4 + ADDENDUM-2 stage + ADDENDUM §4-3 attachments) ─
# layer/is_noise/_body 등은 파이프라인 내부용이라 최종 JSON에는 안 나간다.
ITEM_FIELDS = [
    "id", "category", "doc_type", "stage", "title", "summary", "impact",
    "published_at", "collected_at", "effective_date", "source",
    "trust_score", "keyword_score", "final_score", "matched_keywords",
    "urls", "law_meta", "attachments",
]


def finalize_item(item: dict) -> dict:
    """stage를 계산해 채우고, published_at 결측 시 collected_at 날짜로 대체하고
    (SPEC §4 필드 규칙), 허용된 필드만 남겨 최종 스키마 모양으로 만든다.
    """
    out = {k: item.get(k) for k in ITEM_FIELDS}
    out["stage"] = compute_stage(item["doc_type"])
    if not out["published_at"]:
        out["published_at"] = item["collected_at"][:10]
    return out
