# Policy Watch — 팜한농 재경 규제 모니터링 대시보드
## Claude Code 작업 지시서 (SPEC)

> **사용법**
> 1. 빈 폴더를 만들고 이 파일을 `SPEC.md`로 저장한 뒤 그 폴더에서 `claude` 실행
> 2. 첫 프롬프트: `SPEC.md를 읽고 Phase 0부터 순서대로 진행해줘. 각 Phase가 끝나면 결과를 보고하고 내 확인을 받은 뒤 다음으로 넘어가.`
> 3. 이후에는 `Phase 2 진행해줘` 처럼 단계별로 지시

---

# 0. 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 서비스명 | Policy Watch |
| 목적 | 회계기준·세법·ESG·내부회계관리제도 관련 정책/법령 변경사항을 자동 수집하여 단일 대시보드로 제공 |
| 사용자 | 팜한농 회계팀 / 세무팀 / ESG팀 / 내부회계관리팀 (재경 실무자) |
| 성공 기준 | 손이 가지 않는(유지보수 최소) 자동 수집 + 실무자가 5분 안에 "이번 주 챙길 것"을 파악 |
| 비기능 요건 | 무료 인프라, 매일 1회 자동 갱신, 모바일 대응 |

**중요 원칙**
- 이 대시보드는 **투자정보 서비스가 아니라 실무 규제 트래킹 도구**다. 주가·테마주성 기사는 신뢰도를 직접 훼손하므로 강하게 배제한다.
- 정보의 최종 목적지는 "원문"이다. 모든 항목은 **기사 링크와 기관 원문 링크를 분리해서** 제공한다.

---

# 1. 기술 스택 및 아키텍처

```
[GitHub Actions: 매일 07:00 KST]
        │  python -m sources.main
        ▼
[Python 크롤러]
   ├── 법제처 국가법령정보 Open API   (공식 법령/시행일 — 1차 소스)
   ├── 금융위/국세청/기재부/회계기준원 보도자료
   ├── 네이버 뉴스 API
   └── 구글 뉴스 RSS
        │  (한국 정부 사이트가 해외 IP를 차단하므로 Cloudflare Workers 프록시 경유)
        ▼
[정제 파이프라인]  키워드 매칭 → 노이즈 제거 → 중복 제거 → 신뢰도 점수 → 요약
        ▼
[site/data.json]  (+ site/data.js 폴백)
        ▼
[GitHub Pages: 정적 대시보드]
```

**스택 확정**
- 수집: Python 3.11 (`requests`, `feedparser`, `beautifulsoup4`, `python-dateutil`)
- 자동화: GitHub Actions (cron `0 22 * * *` UTC = 07:00 KST)
- 호스팅: GitHub Pages (`/site` 디렉토리)
- 프록시: Cloudflare Workers (정부 사이트 IP 차단 우회용)
- 프론트: **빌드 없는 정적 페이지** — HTML + Tailwind CSS(CDN) + 바닐라 JS
  - 프레임워크/번들러 쓰지 말 것. GitHub Pages에 그대로 올라가야 하고, 팀원이 직접 수정 가능해야 함.

**시크릿 (GitHub Secrets)**
`NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET`, `LAW_API_OC`(법제처 OC 코드), `PROXY_BASE`(Cloudflare Worker URL)
→ 시크릿이 없으면 해당 소스만 건너뛰고 나머지는 정상 수집되도록 **graceful degradation** 처리할 것.

---

# 2. 디렉토리 구조

```
policy-watch/
├── SPEC.md                     ← 이 문서
├── README.md
├── requirements.txt
├── .github/workflows/crawl.yml
├── sources/
│   ├── __init__.py
│   ├── _config.py              ★ 단일 진실 공급원(Single Source of Truth)
│   ├── _utils.py               쿼리 생성 / 노이즈 필터 / 신뢰도 / 중복제거 / 날짜파싱
│   ├── _summarize.py           2~3줄 요약 + 실무 영향 한 줄 생성
│   ├── law_api.py              법제처 Open API
│   ├── gov_press.py            금융위·국세청·기재부·회계기준원 보도자료
│   ├── naver_news.py           네이버 뉴스 API
│   ├── google_news.py          구글 뉴스 RSS
│   ├── schedules.py            시행일정 추출 → calendar 데이터 생성
│   └── main.py                 오케스트레이터 (entry point)
├── data/
│   └── schedules_manual.yml    수동 관리 시행일정 (자동수집 보완용)
└── site/
    ├── index.html
    ├── app.js
    ├── styles.css
    ├── data.json               ← 크롤러 산출물
    └── data.js                 ← data.json fetch 실패 시 폴백
```

**절대 규칙:** 키워드·노이즈·신뢰도·카테고리 색상 등 **모든 정책값은 `sources/_config.py`에만** 둔다. 다른 파일에 키워드를 하드코딩하지 말 것.

---

# 3. 수집 정책 (`sources/_config.py`에 그대로 반영)

## 3-1. 카테고리별 키워드 셋

### ① K-IFRS / 회계기준 — 회계팀
- 필수: `K-IFRS`, `한국채택국제회계기준`, `회계기준원`, `금융위원회`, `회계감리`
- 조합: `개정`, `제정`, `공표`, `MPM`, `경영진성과측정치`, `기준서`, `주석 공시`, `회계처리 지침`, `감리 지적사례`
- 우선 쿼리: `(K-IFRS OR 회계기준) AND (개정 OR 공표 OR 지침 OR 감리)`

### ② 국내 세법 / 세무 — 세무팀
- 필수: `세법`, `세제개편`, `국세청`, `유권해석`, `기획재정부`
- 조합: `개정안`, `시행령 개정`, `조세특례제한법`, `부가가치세법`, `법인세법`, `예규`, `판례`, `조세심판원`, `세무조사`
- 우선 쿼리: `(세법 OR 시행령 OR 유권해석) AND (법인세 OR 부가가치세 OR 개정)`

### ③ ESG 공시기준 — ESG팀
- 필수: `ESG 공시`, `지속가능경영`, `ISSB`, `KSSB`, `GRI`
- 조합: `의무화`, `공시기준`, `로드맵`, `스코프3`, `Scope 3`, `공급망 실사`, `글로벌 스탠다드`, `가이드라인`
- 우선 쿼리: `(ESG 공시 OR ISSB OR KSSB) AND (의무화 OR 기준 OR 가이드라인)`

### ④ 내부회계관리제도 — 내부회계팀
- 필수: `내부회계관리제도`, `내부통제`, `외감법`
- 조합: `감사 전환`, `모범규준`, `취약점`, `외감법 개정`, `연결 내부회계`, `평가 가이드라인`, `내부통제 미비점`
- 우선 쿼리: `(내부회계관리제도 OR 내부통제) AND (모범규준 OR 감사 OR 가이드라인)`

## 3-2. 노이즈 차단 (NOT 조건, 제목+본문 모두 검사)

```
테마주, 수혜주, 주가, 급등, 상한가, 매수 리포트, 특징주, 개미,
재테크, 비트코인, 투자 유망, 증시 일정, 목표주가, 코스닥 급등, 상승률
```
- 구글 뉴스 RSS: 쿼리에 `-테마주 -수혜주 ...` 로 직접 배제
- 네이버 API / RSS 결과: 수집 후 파이썬 레벨에서 `is_noise()`로 2차 필터
- **단, `source.tier == 1`(공식기관 도메인)은 노이즈 필터를 적용하지 않는다.** 금융위 보도자료에 "주가"가 들어갔다고 버리면 안 됨.

## 3-3. 출처 신뢰도 (Source Trust Score)

| Tier | 구분 | 도메인 | 기본점수 |
|---|---|---|---|
| 1 | 공식 기관 | kasb.or.kr, fsc.go.kr, law.go.kr, nts.go.kr, moef.go.kr, fss.or.kr, kicpa.or.kr | 100 |
| 2 | 전문 미디어 | intn.co.kr(일간NTN), taxtimes.co.kr(한국세정신문), joseilbo.com(조세일보), impacton.net(임팩트온), esgeconomy.com(ESG경제), cpanews.co.kr(CPA뉴스) | 80 |
| 3 | 4대 회계법인 | samil.com, pwc.com, kr.kpmg.com, samjong.co.kr, ey.com, deloitte.com, deloitte.kr, anjin.co.kr | 70 |
| 4 | 메이저 경제지 | mk.co.kr, hankyung.com, sedaily.com, edaily.co.kr, fnnews.com, mt.co.kr | 50 |
| 5 | 기타 | (그 외 전부) | 20 |

**최종 정렬 점수**
```
final_score = trust_score * 0.55
            + keyword_score * 0.30      # 필수 1개당 20점, 조합 1개당 10점, 최대 100
            + recency_score * 0.15      # 오늘 100, 1일 -6점, 0점 하한
```

---

# 4. JSON 데이터 스키마 (`site/data.json`)

프론트엔드는 **오직 이 스키마만** 신뢰한다. 필드를 임의로 추가/변경하지 말 것.

```json
{
  "meta": {
    "schema_version": "1.0",
    "generated_at": "2026-08-07T07:00:12+09:00",
    "window_days": 90,
    "total_items": 137,
    "counts_by_category": { "kifrs": 31, "tax": 58, "icfr": 19, "esg": 29 },
    "sources_ok": ["law_api", "naver", "google_news", "fsc"],
    "sources_failed": [
      { "name": "nts", "reason": "timeout after 3 retries" }
    ]
  },

  "categories": [
    { "key": "kifrs", "label": "K-IFRS",   "color": "#1e3a8a", "team": "회계팀" },
    { "key": "tax",   "label": "세법",      "color": "#047857", "team": "세무팀" },
    { "key": "icfr",  "label": "내부회계",  "color": "#b45309", "team": "내부회계관리팀" },
    { "key": "esg",   "label": "ESG",      "color": "#0e7490", "team": "ESG팀" }
  ],

  "items": [
    {
      "id": "a3f9c1d2e8b04a17",
      "category": "tax",
      "doc_type": "법령",
      "title": "법인세법 시행령 일부개정령안 입법예고",
      "summary": [
        "접대비 손금산입 한도 산정 방식이 매출액 구간별로 세분화된다.",
        "적용 시점은 2027 사업연도 개시일 이후 최초 개시하는 과세연도부터다."
      ],
      "impact": "2026년 4분기 예산 편성 시 판관비 한도 재산정 필요.",
      "published_at": "2026-08-05",
      "collected_at": "2026-08-07T07:00:12+09:00",
      "effective_date": "2027-01-01",
      "source": {
        "name": "기획재정부",
        "domain": "moef.go.kr",
        "tier": 1,
        "type": "official"
      },
      "trust_score": 100,
      "keyword_score": 60,
      "final_score": 89.5,
      "matched_keywords": ["세법", "시행령 개정", "법인세법"],
      "urls": {
        "news": "https://www.moef.go.kr/nw/nes/detailNesDtaView.do?menuNo=...",
        "official": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=..."
      },
      "law_meta": {
        "law_name": "법인세법 시행령",
        "law_id": "011357",
        "revision_type": "일부개정",
        "promulgation_date": "2026-08-04",
        "enforcement_date": "2027-01-01"
      }
    }
  ],

  "schedules": [
    {
      "id": "sch_2027_icfr_consol",
      "category": "icfr",
      "title": "연결 내부회계관리제도 감사 의무 적용 (자산 5천억~2조)",
      "effective_date": "2027-01-01",
      "status": "upcoming",
      "importance": "high",
      "description": "해당 규모 상장사는 연결 기준 내부회계관리제도에 대한 외부감사를 받아야 한다.",
      "source": { "name": "금융위원회", "domain": "fsc.go.kr", "tier": 1 },
      "urls": {
        "news": "https://...",
        "official": "https://www.law.go.kr/..."
      }
    }
  ]
}
```

### 필드 규칙
| 필드 | 규칙 |
|---|---|
| `id` | `sha1(정규화된 URL)[:16]`. 중복 제거 키로 사용 |
| `category` | `kifrs` / `tax` / `icfr` / `esg` 중 하나 (복수 매칭 시 keyword_score 최고 카테고리 1개) |
| `doc_type` | `법령` / `보도자료` / `예규·유권해석` / `기준·가이드라인` / `기사` / `리포트` |
| `summary` | 문자열 배열, **2~3개 원소**, 각 원소 60자 이내 |
| `impact` | 실무 영향 한 줄(80자 이내). 생성 불가 시 `null` |
| `published_at` | `YYYY-MM-DD` (파싱 실패 시 `collected_at`의 날짜로 대체) |
| `effective_date` | 시행일. 없으면 `null` |
| `urls.official` | 원문 없으면 `null` → 프론트에서 버튼 비활성 처리 |
| `law_meta` | 법제처 API 출처일 때만 존재, 아니면 `null` |
| `d_day` | **JSON에 넣지 말 것.** 날짜가 지나면 틀려지므로 프론트에서 실시간 계산 |

정렬: `items`는 `final_score DESC`, 동점 시 `published_at DESC`. `schedules`는 `effective_date ASC`.

---

# 5. 쿼리 생성 함수 (예시 코드 — 이대로 구현)

## 5-1. `sources/_config.py`

```python
# -*- coding: utf-8 -*-
"""단일 진실 공급원. 수집 정책 변경은 반드시 이 파일에서만."""

CATEGORIES = {
    "kifrs": {
        "label": "K-IFRS", "team": "회계팀", "color": "#1e3a8a",
        "required": ["K-IFRS", "한국채택국제회계기준", "회계기준원", "금융위원회", "회계감리"],
        "combine":  ["개정", "제정", "공표", "MPM", "경영진성과측정치",
                     "기준서", "주석 공시", "회계처리 지침", "감리 지적사례"],
        # 네이버 API는 (A OR B) AND (C OR D) 구문을 지원하지 않음 → 단순 질의를 나열
        "naver_queries": ["K-IFRS 개정", "회계기준 개정", "회계기준원 공표",
                          "회계감리 지적사례", "회계처리 지침"],
    },
    "tax": {
        "label": "세법", "team": "세무팀", "color": "#047857",
        "required": ["세법", "세제개편", "국세청", "유권해석", "기획재정부"],
        "combine":  ["개정안", "시행령 개정", "조세특례제한법", "부가가치세법",
                     "법인세법", "예규", "판례", "조세심판원", "세무조사"],
        "naver_queries": ["법인세법 개정", "부가가치세법 개정", "세제개편안",
                          "국세청 유권해석", "조세심판원 결정"],
    },
    "icfr": {
        "label": "내부회계", "team": "내부회계관리팀", "color": "#b45309",
        "required": ["내부회계관리제도", "내부통제", "외감법"],
        "combine":  ["감사 전환", "모범규준", "취약점", "외감법 개정",
                     "연결 내부회계", "평가 가이드라인", "내부통제 미비점"],
        "naver_queries": ["내부회계관리제도", "연결 내부회계", "외감법 개정",
                          "내부회계 모범규준"],
    },
    "esg": {
        "label": "ESG", "team": "ESG팀", "color": "#0e7490",
        "required": ["ESG 공시", "지속가능경영", "ISSB", "KSSB", "GRI"],
        "combine":  ["의무화", "공시기준", "로드맵", "스코프3", "Scope 3",
                     "공급망 실사", "글로벌 스탠다드", "가이드라인"],
        "naver_queries": ["ESG 공시 의무화", "KSSB 공시기준", "ISSB 기준",
                          "지속가능성 공시", "공급망 실사"],
    },
}

NOISE_KEYWORDS = [
    "테마주", "수혜주", "주가", "급등", "상한가", "매수 리포트", "특징주",
    "개미", "재테크", "비트코인", "투자 유망", "증시 일정", "목표주가", "상승률",
]

TRUST_TIERS = [
    (1, 100, {
        "kasb.or.kr": "한국회계기준원", "fsc.go.kr": "금융위원회",
        "law.go.kr": "국가법령정보센터", "nts.go.kr": "국세청",
        "moef.go.kr": "기획재정부", "fss.or.kr": "금융감독원",
        "kicpa.or.kr": "한국공인회계사회",
    }),
    (2, 80, {
        "intn.co.kr": "일간NTN", "taxtimes.co.kr": "한국세정신문",
        "joseilbo.com": "조세일보", "impacton.net": "임팩트온",
        "esgeconomy.com": "ESG경제", "cpanews.co.kr": "CPA뉴스",
    }),
    (3, 70, {
        "samil.com": "삼일회계법인", "pwc.com": "PwC",
        "kr.kpmg.com": "삼정KPMG", "kpmg.com": "KPMG",
        "samjong.co.kr": "삼정KPMG", "ey.com": "EY한영",
        "deloitte.com": "딜로이트", "deloitte.kr": "딜로이트 안진",
        "anjin.co.kr": "딜로이트 안진",
    }),
    (4, 50, {
        "mk.co.kr": "매일경제", "hankyung.com": "한국경제",
        "sedaily.com": "서울경제", "edaily.co.kr": "이데일리",
        "fnnews.com": "파이낸셜뉴스", "mt.co.kr": "머니투데이",
    }),
]
DEFAULT_TIER, DEFAULT_TRUST = 5, 20

COLLECT_WINDOW_DAYS = 90     # 수집 기간
MAX_ITEMS_PER_CATEGORY = 60  # 카테고리당 상한
```

## 5-2. `sources/_utils.py` — 쿼리 생성 & 필터

```python
# -*- coding: utf-8 -*-
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
    host = (urlparse(url).hostname or "").lower().lstrip("www.")
    for tier, score, domains in TRUST_TIERS:
        for dom, name in domains.items():
            if host == dom or host.endswith("." + dom):
                return tier, score, name
    return DEFAULT_TIER, DEFAULT_TRUST, host or "기타"


def recency_score(published: date, today: date | None = None) -> int:
    d = (today or date.today() - published).days if today else (date.today() - published).days
    return max(0, 100 - d * 6)


def final_score(trust: int, kw: int, rec: int) -> float:
    return round(trust * 0.55 + kw * 0.30 + rec * 0.15, 2)


# ── 6) 중복 제거 ─────────────────────────────────────────────────────────
def make_id(url: str) -> str:
    canon = re.sub(r"[?#].*$", "", (url or "").strip().lower())
    return hashlib.sha1(canon.encode()).hexdigest()[:16]


def dedupe(items: list[dict]) -> list[dict]:
    """URL 해시 + 제목 정규화 이중 제거. 신뢰도 높은 쪽을 남긴다."""
    best: dict[str, dict] = {}
    for it in items:
        for key in (it["id"], "T:" + _norm(it["title"])[:40]):
            prev = best.get(key)
            if prev is None or it["final_score"] > prev["final_score"]:
                best[key] = it
    seen, out = set(), []
    for it in sorted(best.values(), key=lambda x: -x["final_score"]):
        if it["id"] in seen:
            continue
        seen.add(it["id"]); out.append(it)
    return out
```

## 5-3. JS 버전 (프론트에서 클라이언트 재검색이 필요할 때)

```javascript
// site/app.js 내부 유틸 — data.json을 클라이언트에서 재필터링할 때 사용
const norm = s => (s || "").replace(/\s+/g, "").toLowerCase();

function filterItems(items, { categories, from, to, query }) {
  const f = from ? new Date(from) : null;
  const t = to   ? new Date(to)   : null;
  const q = norm(query);
  return items.filter(it => {
    if (categories?.length && !categories.includes(it.category)) return false;
    const d = new Date(it.published_at);
    if (f && d < f) return false;
    if (t && d > t) return false;
    if (q) {
      const hay = norm(it.title + (it.summary || []).join("") + it.source.name);
      if (!hay.includes(q)) return false;
    }
    return true;
  });
}

const dday = iso => Math.ceil((new Date(iso) - new Date().setHours(0,0,0,0)) / 864e5);
const ddayLabel = n => n === 0 ? "D-DAY" : n > 0 ? `D-${n}` : `D+${-n}`;
```

---

# 6. 요약 생성 (`sources/_summarize.py`)

- 외부 LLM API 호출 없이 **규칙 기반**으로 먼저 구현한다(비용·키 관리 이슈 회피).
  - 본문 첫 문장 + 키워드 포함 문장 중 최상위 1~2문장을 추출
  - 문장 60자 초과 시 어절 단위로 자르고 말줄임
- `impact`는 카테고리별 템플릿 규칙으로 생성:
  - `effective_date`가 있으면 → `"{시행일}부터 적용. {카테고리 담당팀} 사전 검토 필요."`
  - `doc_type == "예규·유권해석"` → `"기존 세무처리 관행 재확인 필요."`
  - 규칙에 해당 없으면 `null` (억지로 만들지 말 것)
- 향후 LLM 요약으로 교체 가능하도록 `summarize(item) -> dict` 단일 인터페이스로 분리해둘 것.

---

# 7. 프론트엔드 요구사항 (`site/index.html`, `app.js`, `styles.css`)

## 7-1. 전체 레이아웃

```
┌─────────────────────────────────────────────────────────────┐
│ [PW] Policy Watch      K-IFRS · 세법 · 내부회계 · ESG    ⟳ 갱신 07:00 │  ← sticky top
├──────────────────────────────────────┬──────────────────────┤
│ FILTER                               │  ┌────────────────┐  │
│  [전체][K-IFRS][세법][내부회계][ESG] │  │  2026년 8월  ‹ ›│  │
│  시작일 [____] ~ 종료일 [____] [조회]│  │  일 월 화 수 목 금 토│ │
│                                      │  │   ...  ●  ●    │  │  ← sticky
│  총 137건 · 정렬: 중요도순 ▾         │  └────────────────┘  │
├──────────────────────────────────────┤                      │
│ 2026.08.05  ─────────────────────    │  시행 예정 일정      │
│  ┌────────────────────────────────┐  │  ┌────────────────┐  │
│  │ [세법]        출처: 기획재정부 │  │  │ D-147          │  │
│  │ 법인세법 시행령 일부개정령안   │  │  │ 연결 내부회계  │  │
│  │ · 요약 1줄                     │  │  │ 2027.01.01     │  │
│  │ · 요약 2줄                     │  │  │ [기사][원문 🔗]│  │
│  │ ▸ 실무 영향: ...               │  │  └────────────────┘  │
│  │ [뉴스 기사 보기] [공식 원문 🔗]│  │  ┌────────────────┐  │
│  └────────────────────────────────┘  │  │ D-203 ...      │  │
│           70%                        │        30%           │
└──────────────────────────────────────┴──────────────────────┘
```

## 7-2. 상단 네비게이션 (고정)
- 좌측: 워드마크 `Policy Watch` + 아래 작은 캡션 `팜한농 재경 규제 모니터링`
- 중앙/우측: 4개 카테고리 메뉴 (클릭 시 좌측 필터와 연동, 현재 선택 항목은 하단 2px 언더라인)
- 우측 끝: `마지막 갱신 2026.08.07 07:00` (data.json의 `meta.generated_at`)
- `position: sticky; top: 0;` + 스크롤 시 하단 1px 보더 + 미세 그림자

## 7-3. 좌측 (70%) — 필터 + 피드

**필터 바**
- 카테고리 칩: `전체 / K-IFRS / 세법 / 내부회계 / ESG` — **다중 선택 가능**, 선택 시 해당 카테고리 색상으로 채움
- 날짜: `<input type="date">` 2개 (시작일 ~ 종료일) + `조회` 버튼
- 기본값: 종료일 = 오늘, 시작일 = 30일 전
- 빠른 선택 버튼: `최근 7일` `최근 30일` `최근 90일`
- 우측에 결과 건수 + 정렬 셀렉트(`중요도순` / `최신순`)
- 필터 상태는 URL 쿼리스트링에 동기화(`?cat=tax,esg&from=2026-07-01`) → 팀원 간 링크 공유 가능

**피드**
- 날짜별 그룹핑. 각 그룹 헤더는 `2026.08.05 (수)` + 우측으로 뻗는 1px 구분선
- 카드 구성(위→아래):
  1. 상단 행: 카테고리 뱃지(고유 색상, 배경은 12% 투명도, 텍스트는 원색) / 우측에 `출처: 기획재정부` + tier 1이면 작은 `공식` 라벨
  2. 제목 (17px, 600, 딥네이비, 2줄 말줄임)
  3. 요약 (14px, `#475569`, 최대 3줄, `·` 불릿)
  4. `실무 영향` 한 줄 — 좌측 3px 세로선 + 연한 배경 박스 (`impact`가 null이면 렌더 생략)
  5. 버튼 행: `[뉴스 기사 보기]` (아웃라인 버튼) `[관련 기관 공식 원문 보기 🔗]` (솔리드 네이비)
     - `urls.official`이 null이면 해당 버튼은 `disabled` + 툴팁 `원문 링크 없음`
     - 모두 `target="_blank" rel="noopener"`
- 카드: 배경 흰색, `border: 1px solid #e2e8f0`, `border-radius: 8px`, `padding: 20px 24px`, hover 시 보더가 네이비로 바뀌고 `translateY(-1px)`
- 결과 0건: `조건에 맞는 항목이 없습니다. 기간을 넓히거나 카테고리를 추가해 보세요.` + `최근 90일로 보기` 버튼

## 7-4. 우측 (30%) — 시행일 캘린더 (Sticky)

- `position: sticky; top: 76px;` (네비 높이만큼)
- **미니 캘린더**
  - 헤더: `‹  2026년 8월  ›` — 화살표로 이전/다음 달 자유 이동(과거·미래 모두)
  - 요일 헤더 + 날짜 그리드, 오늘 날짜는 네이비 원형 배경
  - 시행일이 있는 날짜 하단에 **카테고리 색상 점(dot)** 표시, 최대 3개까지 표시 후 `+n`
  - 날짜 클릭 → 아래 일정 리스트가 해당 날짜로 스크롤/하이라이트
- **시행 예정 주요 일정 리스트**
  - 캘린더 바로 아래, 제목 `시행 예정 일정` + 부제 `당월 ~ 향후 3개월`
  - 각 항목: `D-147` 뱃지(중요도 high면 네이비 솔리드, 그 외 아웃라인) / 카테고리 뱃지 / 제목 / `2027.01.01` / 설명 1줄
  - 각 항목 하단에 `[뉴스 기사 보기]` `[공식 원문 🔗]` 버튼 나란히 (좌측 카드와 동일 규칙)
  - D-Day는 **클라이언트에서 매번 계산** (JSON에 저장 금지)
  - 지난 일정은 회색 처리하되 당월 것은 목록에 남긴다

## 7-5. 디자인 토큰

```css
:root{
  --navy:#1e3a8a;        /* 메인 */
  --navy-deep:#172554;   /* 제목/강조 */
  --ink:#0f172a;
  --muted:#475569;
  --line:#e2e8f0;
  --bg:#f8fafc;
  --card:#ffffff;

  --c-kifrs:#1e3a8a;
  --c-tax:#047857;
  --c-icfr:#b45309;
  --c-esg:#0e7490;

  --r:8px;
  --gap:24px;
}
```
- 폰트: `Pretendard`(CDN) → 폴백 `-apple-system, "Malgun Gothic", sans-serif`. 숫자·날짜·D-Day에는 `font-variant-numeric: tabular-nums` 적용.
- **이미지·아이콘 이미지 사용 금지.** 필요한 기호는 텍스트/유니코드(`‹ › 🔗 ●`)와 CSS 도형으로만.
- 그림자 최소화(hover 시에만 `0 2px 8px rgba(15,23,42,.06)`), 그라데이션 금지.
- 여백: 섹션 간 32px, 카드 간 12px, 카드 내부 20~24px.

## 7-6. 반응형
- `≥1280px`: 70:30 2단
- `1024~1279px`: 66:34, 사이드바 폰트 1단계 축소
- `<1024px`: **1단 세로 정렬**. 순서는 `필터 → 시행 예정 일정(접힘 상태 요약) → 피드`
  - 사이드바 sticky 해제
  - 캘린더는 `<details>` 로 접어두고 기본은 일정 리스트 3건만 노출 + `전체 일정 보기`
- `<640px`: 카드 padding 16px, 버튼 2개는 세로 100% 폭으로 쌓기, 날짜 입력은 1행 2열 유지

## 7-7. 품질 기준 (반드시 충족)
- 키보드 포커스 링 항상 보이게(`:focus-visible` 2px 네이비 아웃라인)
- `prefers-reduced-motion` 존중
- `data.json` fetch 실패 → `data.js`(전역 `window.POLICY_DATA`) 폴백 → 그것도 실패 시 명확한 오류 안내 표시
- 로딩 중에는 스켈레톤 3장 표시
- 색상만으로 카테고리를 구분하지 않는다(뱃지에 항상 텍스트 라벨 병기)

---

# 8. 작업 순서 (Phase — 반드시 이 순서로, 각 단계 끝에 보고)

| Phase | 산출물 | 완료 조건 |
|---|---|---|
| **0** | 레포 스캐폴딩, `requirements.txt`, `.gitignore`, README | 디렉토리 구조가 §2와 일치 |
| **1** | `_config.py`, `_utils.py` + `tests/test_utils.py` | 쿼리 생성·노이즈 필터·신뢰도·중복제거 단위 테스트 전부 통과 |
| **2** | `google_news.py`, `naver_news.py` | 카테고리별 실제 수집 결과 건수를 콘솔에 출력, 노이즈 0건 확인 |
| **3** | `law_api.py`, `gov_press.py`, 프록시 연동 | 법제처 API에서 시행일 포함 항목 수집 확인 |
| **4** | `_summarize.py`, `schedules.py`, `main.py` → `site/data.json` 생성 | 스키마 §4와 100% 일치 (JSON Schema 검증 스크립트 포함) |
| **5** | `site/index.html`, `app.js`, `styles.css` | 로컬 `python -m http.server`로 렌더 확인, 데스크톱/모바일 스크린샷 |
| **6** | `.github/workflows/crawl.yml`, GitHub Pages 설정 | 수동 실행(workflow_dispatch) 성공 → 커밋 자동 푸시 확인 |

**Phase 5는 먼저 더미 `data.json`(각 카테고리 3건 + 일정 5건)을 만들어 UI를 완성한 뒤** 실데이터를 붙일 것.

---

# 9. 반드시 지켜야 할 주의사항 (과거 실패 사례 기반)

1. **파일 완전성 검증**: 긴 파이썬 파일은 잘려서 저장되는 사고가 반복됐다. 각 파일 작성 직후 `tail -5`로 끝부분을 확인하고, `main.py`는 `if __name__ == "__main__": main()`이, `_config.py`는 마지막 상수까지 존재하는지 확인할 것.
2. **네이버 API 쿼리 구문**: `(A OR B) AND (C OR D)`를 지원하지 **않는다**. 반드시 `naver_queries` 단순 질의 + `match_loose()` 사후 필터 방식으로 구현.
3. **정부 사이트 IP 차단**: GitHub Actions(미국 IP)에서 `law.go.kr`, `nts.go.kr` 등은 차단될 수 있다. `PROXY_BASE`가 설정돼 있으면 프록시 경유, 없으면 직접 호출 후 실패 시 `meta.sources_failed`에 기록하고 계속 진행.
4. **한 소스 실패가 전체를 죽이지 않게**: 각 수집기는 독립적으로 try/except, 타임아웃 15초, 재시도 3회(지수 백오프).
5. **모든 정책값은 `_config.py`에만.** 다른 파일에서 키워드 문자열을 발견하면 리팩터링 대상이다.
6. **`data.json`은 반드시 UTF-8, `ensure_ascii=False`, 2-space indent**로 저장(diff 가독성).
7. 크롤링 시 `User-Agent` 명시, 요청 간 0.5초 sleep, `robots.txt` 존중.

---

# 10. Claude Code에 붙여넣을 첫 프롬프트

```
이 폴더의 SPEC.md를 정독해줘. 팜한농 재경 부서용 규제 모니터링 대시보드
"Policy Watch"를 만들 거야.

작업 방식:
- SPEC.md §8의 Phase 0부터 순서대로 진행한다.
- 각 Phase가 끝나면 (1) 생성/수정한 파일 목록, (2) 실행 결과,
  (3) 내가 확인해야 할 사항을 보고하고 멈춘다. 내 승인 후 다음 Phase로 간다.
- SPEC.md §9의 주의사항은 매 Phase마다 스스로 점검한다.
- 스키마(§4)와 다른 필드를 만들거나 이름을 바꾸지 않는다. 변경이 필요하면 먼저 제안한다.

Phase 0 시작해줘.
```
