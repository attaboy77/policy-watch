# Policy Watch

팜한농 재경(회계·세무·ESG·내부회계관리) 규제 모니터링 대시보드.
회계기준·세법·ESG 공시기준·내부회계관리제도 관련 정책/법령 변경사항을 매일 자동 수집해
단일 대시보드(GitHub Pages)로 제공합니다.

> 전체 요구사항과 작업 지시는 [`SPEC.md`](./SPEC.md)가 단일 진실 공급원(SSOT)입니다.
> 이 문서와 SPEC.md가 어긋나면 SPEC.md를 따릅니다.

## 아키텍처 개요

```
GitHub Actions(매일 07:00 KST)
  → Python 크롤러 (법제처 API / 정부 보도자료 / 네이버뉴스 / 구글뉴스 RSS)
  → 정제 파이프라인 (키워드 매칭 → 노이즈 제거 → 중복 제거 → 신뢰도 점수 → 요약)
  → site/data.json
  → GitHub Pages 정적 대시보드 (site/)
```

## 디렉토리 구조

```
policy-watch/
├── SPEC.md
├── README.md
├── requirements.txt
├── .github/workflows/crawl.yml   수집 자동화 (GitHub Actions)
├── sources/                      Python 크롤러 · 정제 파이프라인
│   ├── _config.py                ★ 키워드/신뢰도/카테고리 등 모든 정책값의 SSOT
│   ├── _utils.py                 쿼리 생성 / 노이즈 필터 / 신뢰도 / 중복제거
│   ├── _summarize.py             규칙 기반 요약 생성
│   ├── law_api.py                법제처 국가법령정보 Open API
│   ├── gov_press.py              금융위·국세청·기재부·회계기준원 보도자료
│   ├── naver_news.py             네이버 뉴스 API
│   ├── google_news.py            구글 뉴스 RSS
│   ├── schedules.py              시행일정 추출
│   └── main.py                   오케스트레이터 (entry point)
├── tests/                        단위 테스트
├── data/
│   └── schedules_manual.yml      수동 관리 시행일정 (자동수집 보완용)
└── site/                         빌드 없는 정적 프론트엔드 (GitHub Pages)
    ├── index.html
    ├── app.js
    ├── styles.css
    ├── data.json                 크롤러 산출물 (스키마: SPEC.md §4)
    └── data.js                   data.json fetch 실패 시 폴백
```

## 로컬 개발

### 1. Python 환경

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
```

### 2. 환경변수 (시크릿)

크롤러는 아래 환경변수가 없어도 동작합니다(해당 소스만 건너뛰고 나머지는 정상 수집 — graceful degradation).

| 변수 | 용도 |
|---|---|
| `NAVER_CLIENT_ID` / `NAVER_CLIENT_SECRET` | 네이버 뉴스 검색 API |
| `LAW_API_OC` | 법제처 국가법령정보 Open API OC 코드 |
| `PROXY_BASE` | 정부 사이트 IP 차단 우회용 Cloudflare Workers 프록시 URL |

로컬 실행 시 `.env` 파일 등으로 주입하거나 쉘 환경변수로 export 하세요(`.env`는 `.gitignore`에 포함되어 커밋되지 않습니다).

### 3. 크롤러 실행

```bash
python -m sources.main
```

성공 시 `site/data.json`이 생성/갱신됩니다.

### 4. 대시보드 로컬 확인

```bash
cd site
python -m http.server 8000
# http://localhost:8000 접속
```

### 5. 테스트

```bash
pytest
```

## 배포

GitHub Actions가 매일 07:00 KST(cron `0 22 * * *` UTC)에 크롤러를 실행하고
`site/data.json`을 커밋 → GitHub Pages(`/site`)가 정적으로 서빙합니다.
수동 실행은 Actions 탭에서 `workflow_dispatch`로 트리거할 수 있습니다.

## 정책값 변경

카테고리 키워드, 노이즈 키워드, 출처 신뢰도 등 **모든 정책값은 `sources/_config.py` 한 곳에서만** 관리합니다.
다른 파일에 키워드를 하드코딩하지 마세요.
