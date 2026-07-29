"""공용 유틸 — 공식원문 링크 매칭, 노이즈/광고/중복 필터, 정밀 분류, 쿼리 생성."""
import re

from . import _config

# 카테고리별 공식 원문 링크 (프론트 '공식 원문 보기' 버튼용)
OFFICIAL_SOURCES = {
    "K-IFRS": [("한국회계기준원", "https://www.kasb.or.kr/"), ("금융위원회", "https://www.fsc.go.kr/index")],
    "세법": [("국가법령정보센터", "https://www.law.go.kr/"), ("국세청", "https://www.nts.go.kr/")],
    "내부회계": [("한국회계기준원", "https://www.kasb.or.kr/"), ("금융위원회", "https://www.fsc.go.kr/index")],
    "ESG": [("한국회계기준원", "https://www.kasb.or.kr/"), ("금융위원회", "https://www.fsc.go.kr/index")],
}


def official_links(category: str):
    return [{"label": n, "url": u} for n, u in OFFICIAL_SOURCES.get(category, [])]


# ── 노이즈/광고 필터 ──
def is_noise(title: str) -> bool:
    """주식 시황·재테크 등 실무 무관 찌라시 기사 판별."""
    return any(k in title for k in _config.NOISE_KEYWORDS)


def is_ad(title: str, source: str = "") -> bool:
    if any(k in title for k in _config.AD_KEYWORDS):
        return True
    if any(s in source for s in ["뉴스와이어", "보도자료", "블로그", "카페"]):
        return True
    return False


def should_exclude(title: str, source: str = "") -> bool:
    """수집 제외 여부 통합 판정 (노이즈 OR 광고)."""
    return is_noise(title) or is_ad(title, source)


# ── 정밀 카테고리 매칭 (필수 AND 조합) ──
def match_category(title: str, category: str) -> bool:
    """제목이 해당 카테고리의 [필수 키워드] AND [조합 키워드]를 만족하는지.

    뉴스는 정밀도가 중요하므로 must 하나 + combine 하나를 모두 요구한다.
    """
    kw = _config.CATEGORY_KEYWORDS.get(category)
    if not kw:
        return False
    has_must = any(m in title for m in kw["must"])
    has_combine = any(c in title for c in kw["combine"])
    return has_must and has_combine


def classify_strict(title: str):
    """어느 카테고리에 정밀 매칭되는지 반환 (없으면 None)."""
    for cat in _config.CATEGORY_KEYWORDS:
        if match_category(title, cat):
            return cat
    return None


# ── 검색 쿼리 생성 ──
def build_query(category: str) -> str:
    """카테고리별 뉴스 검색 쿼리 문자열 반환 (구글용, OR/AND 조합)."""
    kw = _config.CATEGORY_KEYWORDS.get(category, {})
    return kw.get("query", category)


def build_naver_query(category: str) -> str:
    """네이버용 단순 쿼리 반환 (네이버는 괄호 AND/OR 미지원)."""
    kw = _config.CATEGORY_KEYWORDS.get(category, {})
    return kw.get("naver_query", category)


# ── 중복 제거 (제목 유사도) ──
def _normalize(title: str) -> str:
    t = re.sub(r"\[[^\]]*\]", "", title)
    t = re.sub(r"[^가-힣a-zA-Z0-9]", "", t)
    return t.lower()


def dedup_key(title: str) -> str:
    return _normalize(title)[:24]


def dedup(items: list[dict]) -> list[dict]:
    seen, out = set(), []
    for it in items:
        k = dedup_key(it.get("title", ""))
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(it)
    return out


# ── 출처 가중치 ──
def trust_score(url: str) -> int:
    return _config.trust_score(url)


def trust_name(url: str):
    return _config.trust_name(url)
