# -*- coding: utf-8 -*-
"""쿼리 생성 / 노이즈 필터 / 신뢰도 / 중복제거 / 날짜파싱 유틸리티.
"""
import hashlib, re
from datetime import date, datetime
from urllib.parse import urlparse, quote_plus
from ._config import (CATEGORIES, NOISE_KEYWORDS, TRUST_TIERS,
                      DEFAULT_TIER, DEFAULT_TRUST)


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
    return min(100, hit_req * 20 + hit_com * 10)


def matched_keywords(text: str, cat_key: str) -> list[str]:
    t = _norm(text)
    c = CATEGORIES[cat_key]
    return [k for k in (c["required"] + c["combine"]) if _norm(k) in t]


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
