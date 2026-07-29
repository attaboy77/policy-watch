"""공용 유틸 — 카테고리별 공식 원문 링크 매칭, 광고·중복 필터."""
import re

# 카테고리별 공식 원문 링크 (요구사항 매칭 기준)
OFFICIAL_SOURCES = {
    "K-IFRS": [
        ("한국회계기준원", "https://www.kasb.or.kr/"),
        ("금융위원회", "https://www.fsc.go.kr/index"),
    ],
    "세법": [
        ("국가법령정보센터", "https://www.law.go.kr/"),
    ],
    "내부회계": [
        ("한국회계기준원", "https://www.kasb.or.kr/"),
        ("금융위원회", "https://www.fsc.go.kr/index"),
    ],
    "ESG": [
        ("한국회계기준원", "https://www.kasb.or.kr/"),
        ("금융위원회", "https://www.fsc.go.kr/index"),
    ],
}


def official_links(category: str):
    """카테고리에 맞는 공식 원문 링크 목록 반환."""
    return [{"label": name, "url": url} for name, url in OFFICIAL_SOURCES.get(category, [])]


# ── 광고성/저품질 기사 필터 ──
AD_KEYWORDS = [
    "제휴", "광고", "분양", "이벤트", "할인", "쿠폰", "특가", "무료체험",
    "카드혜택", "적립", "사은품", "프로모션", "협찬", "[AD]", "(광고)",
    "바로가기", "무료상담", "가입혜택", "최저가", "핫딜",
]
# 언론사가 아닌 저품질 출처(보도자료 배포처 등)
LOW_QUALITY_SOURCES = ["뉴스와이어", "보도자료", "블로그", "카페"]


def is_ad(title: str, source: str = "") -> bool:
    if any(k in title for k in AD_KEYWORDS):
        return True
    if any(s in source for s in LOW_QUALITY_SOURCES):
        return True
    return False


# ── 중복 기사 제거 (제목 유사도) ──
def _normalize(title: str) -> str:
    # 대괄호 태그, 특수문자, 공백 제거 후 비교용 키 생성
    t = re.sub(r"\[[^\]]*\]", "", title)      # [속보] 등 제거
    t = re.sub(r"[^가-힣a-zA-Z0-9]", "", t)    # 특수문자·공백 제거
    return t.lower()


def dedup_key(title: str) -> str:
    """중복 판정용 키. 앞부분 위주로 잘라 유사 제목을 같은 키로."""
    norm = _normalize(title)
    return norm[:24]  # 앞 24자 같으면 같은 기사로 간주


def dedup(items: list[dict]) -> list[dict]:
    """제목 유사도 기반 중복 제거. 먼저 온 것을 유지."""
    seen, out = set(), []
    for it in items:
        k = dedup_key(it.get("title", ""))
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(it)
    return out
