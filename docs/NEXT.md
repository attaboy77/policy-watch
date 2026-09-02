# 다음에 이어서 할 일 (NEXT)

마지막 갱신: 2026-09-01, K-IFRS 업종 특화 기준서 제외 커밋(`5d2c780`) 직후 기준. **Phase 6(GitHub Pages 자동 배포) 완료·운영 중.**
현재 `site/data.json`: 152건(K-IFRS 68 / 세법 33 / 내부회계 32 / ESG 19), 일정 73건. 테스트 345개 통과. AI 요약 캐시 43건.

## 2026-09-01 세션 요약 (커밋 `685a55f`~`5d2c780`, 21개 커밋 — 실제 배포 후 첫 세션)

사용자가 배포된 사이트(github.com/attaboy77/policy-watch, GitHub Pages)를 직접 브라우저로 보면서
발견한 버그들을 순서대로 고쳤고, 그 과정에서 **Phase 6 배포 자체도 이번 세션에 처음 완료**했다.
KSSB 자발적용 기준서 수집, 법제처 개정이유 수집, AI 요약 43건 누적도 이 세션에서 진행했다.
아래는 주제별로 묶어서 요약(각 항목의 실제 커밋 해시는 괄호 안 참고).

- **K-IFRS 오분류·정렬 버그 3건 + 캘린더 3건 + 탭 전환 CSS 버그 + 최근 정책동향 개선** (`685a55f`)
  - K-IFRS 탭 상위 3건이 잘못 분류된 걸 사용자가 직접 발견: (1) CPA뉴스 연재 칼럼이 "공식" 배지로 뜬 건 — `trust_of()`가 `.endswith()` 접미사 매칭이라 `news.kicpa.or.kr`가 `kicpa.or.kr`(tier1)을 그대로 상속받은 버그. 정확 일치를 우선 검사하는 2단계 루프로 수정. (2) "회계기준원, ...자문위원 10명 위촉" 같은 인사 소식이 안 걸러진 건 — `ADMIN_NOISE_KEYWORDS`에 "위촉" 추가. (3) 정렬을 "중요도순"으로 바꿔도 화면은 날짜 그룹으로만 내려가던 건 — `renderFeed()`가 정렬 기준과 무관하게 항상 날짜 그룹핑을 하던 버그. 중요도순일 때는 그룹 헤더 없이 플랫 리스트로 렌더링하도록 분기 추가.
  - 캘린더: 시행 완료 71건이 전부 노출되던 걸 12개월 컷오프 + "이전 일정 더보기" 토글로 정리, 일정 제목의 "N년" 의결연도 접두사를 표시 전용으로 제거(원본 데이터는 dedup 때문에 그대로 둠), 미니 달력에 과거 시행 항목도 회색 점으로 표시.
  - CSS 버그: `.layout{display:grid}`(단일 클래스)와 `.view{display:none}`가 명시도(specificity)가 같아서 소스 순서상 `.layout`이 항상 이겨 탭을 바꿔도 이전 탭 내용이 스크롤 시 드러나던 문제 — `main.view:not(.is-active){display:none}`(요소+클래스+가상클래스, 더 높은 명시도) 추가로 해결.
  - "오늘의 정책동향"을 "최근 정책동향" 개념으로 개선 — 1/3/7/14/30일 순으로 최소 5건 채워질 때까지 창을 넓히고, 실제 사용한 기간을 안내 문구에 명시. 개별 기업 제재·감리 뉴스("영풍 회계처리 위반 중징계" 등)와 집계형 통계 기사("상장사 감사의견 '적정' 97%" 등)를 `is_company_event()`에 `_AUDIT_OPINION_STATS_RE`/`STATISTICAL_REPORT_SIGNALS` 추가해 제외(통계 기사는 다른 강한 신호보다 우선하는 무조건 제외로 처리 — 사용자가 재확인).
  - 디버그용 `console.log` 4줄(캘린더 "더보기" 버튼 원인 조사용)은 추가 후 문제 우선순위가 낮아져 전부 제거 확인(`grep -c "console.log"` → 0).

- **Phase 6 — GitHub Pages 자동 배포 완료** (`d302ed0`, `f0078fc`, `57d5b11`)
  - 원격(github.com/attaboy77/policy-watch)이 2개월 전 `crawler/` 구조인 걸 발견 → 사용자 확인 후 `legacy-crawler-archive` 브랜치로 백업하고 로컬 `sources/` 구조로 교체(데이터 손실 없이 되돌릴 수 있게).
  - `.github/workflows/crawl.yml`을 Phase 0 placeholder에서 실제 3-job(crawl/build/deploy) 워크플로로 재작성 — cron(07:00 KST) + `workflow_dispatch` + `push`(site/**, data/** 경로) 트리거, 시크릿(`LAW_API_OC`/`PROXY_BASE`/`NAVER_CLIENT_ID`/`NAVER_CLIENT_SECRET`) 연결.
  - **버그**: push 트리거로 실행하면 `crawl`은 의도대로 skip되는데 `deploy`도 같이 skip됨. 원인은 `deploy`가 `needs: build`만 쓰고 `if:`를 안 써서 기본값 `success()`가 적용됐고, 이건 직접 needs뿐 아니라 **전체 의존 그래프**(build→crawl)를 다 확인하는데 `crawl`이 skipped라 false가 된 것. `if: always() && needs.build.result == 'success'`로 명시해 해결 — push #89 재실행에서 deploy까지 초록으로 확인.
  - `data/summary_cache.json`(요약 10건 등 미커밋 파일들)도 함께 push해 배포 사이트에 요약이 반영되도록 함.

- **법제처 개정이유(revision_reason) 수집 + 카드 토글 UI** (`cc8a587`, `7c91bf7`→`aa1f7d3`)
  - `law_api.py`가 `lawService.do` XML API에서 `<제개정이유내용>`도 함께 파싱해 `revision_reason` 필드로 저장(id 생성은 계속 `lsInfoP.do` URL 기준으로 안정적으로 유지 — 캐시 연결 안 깨지게).
  - 세법 탭 "관련 기관 공식 원문 보기"를 법제처 URL의 `#tab` 파라미터로 "제·개정이유" 탭 우선 노출을 시도 → 실측 결과 `lsRvsDocInfoR.do`로 바꾸면 가능했으나, **바로 다음 요청에서 사용자가 되돌림**: 이 페이지는 조문/신구조문대비표로 못 넘어가서 오히려 불편 → `lsInfoP.do`(법령 본문)로 원복하고, 대신 카드에 "개정이유 전문 보기" `<details>` 토글 추가(기본 접힘, `revision_reason` 있는 항목에만 노출).

- **KSSB 자발적용 기준서 수집 + ESG 로드맵 연결** (`cf477ef`, `6193a1e`, `127c2fe`)
  - `kasb.py`에 `fetch_kssb_voluntary_standards()` 신설 — KASB "자발적용가능" 탭(제1호/제2호)을 esg 카테고리, `doc_type="자발적용"`, `effective_date=None`으로 수집.
  - 시행일은 크롤링 대상이 아니라(FSC 보도자료가 KSSB 기준서 번호를 직접 언급하지 않음 — 별도 조사 결론) `data/esg_roadmap.yml`로 수동 관리(1차 2028.01.01/FY2027, 2차 2030년, 금융위 로드맵 출처·상태 "예정" 명시). 이후 사용자 요청으로 1차 시행일을 2028-01-01로 명시 갱신.
  - `finalize_item()`에서 `doc_type=="자발적용"`이고 `effective_date`가 비어있으면 로드맵 1차 시행일로 채우되 `is_roadmap_estimate=True`를 함께 표시 — 캘린더에 "로드맵 예정"(점선 테두리 점 + 배지)으로 확정 시행일과 시각적으로 구분. `_summarize.py`도 로드맵 정보를 요약/impact에 자동 반영("팜한농은 1차 대상은 아니나 모회사 연결 공시 대응 필요" 문구 포함).
  - **버그**: 지방세법 시행령 캘린더 카드에 제목이 두 번 나오던 문제 — 요약이 없을 때 설명란이 제목으로 폴백되는데 이미 카드 제목도 표시되고 있어 중복. 전체 동향 탭과 통일해 `ai_generated`인데 요약/impact가 없으면 "AI 검토 결과 팜한농 해당사항 없음"으로 채우도록 `_description_of()` 수정.

- **AI 요약 43건 누적 + 빈 카드 안내 문구** (`6b0571e`, `cc8a587`, `36fc766`, `acfdde5`, 다수)
  - 요약 대상(kifrs/icfr/esg/tax 후보)을 원문 직접 읽고 summary 2줄 + impact 1줄(팜한농 제조업·연결 실체 관점, 무관하면 impact는 null로 두고 억지로 안 만듦) 방식으로 여러 배치에 걸쳐 채움: 10건 → +25(kifrs4/tax18/icfr3) → +17(kifrs15/icfr2) 등, 누적 43건.
  - **뉴스(L3) 기사는 요약 대상에서 명시적으로 제외하기로 결정** — 공식/L1/L2 문서만 AI 요약.
  - "AI 요약" 뱃지는 있는데 summary/impact가 둘 다 비어있어 헷갈리던 카드에 "AI 검토 결과 팜한농 해당사항 없음" 한 줄을 표시 전용으로 추가(원본 데이터는 그대로 빈 상태 유지 — 표시 레이어에서만 처리).

- **첨부파일 전용 시행일(사업연도 기준) 4건 캘린더 반영** (`a6e6806`)
  - "N년 이후 개시 사업연도부터 적용"처럼 특정 시행일 없이 사업연도 기준으로만 적혀 있는 항목 4건을, 팜한농이 12월 결산이므로 해당 연도 1/1로 근사 시행일을 부여 — `_FISCAL_YEAR_EFFECTIVE_DATES` 수동 매핑(id→(date, 원문 표현 그대로 병기한 note)). 카드에는 "적용: 2024.1.1 이후 개시 사업연도부터" 형태로 날짜의 성격이 드러나게 병기.
  - **버그**: `_gap_log.record()`가 `fss.py`의 수집 루프에서 `finalize_item()`보다 먼저·독립적으로 호출돼서, 위 매핑을 추가해도 `EFFECTIVE_DATE_GAPS.md`가 그대로였음(6건 불변) — `fss.py`에 `has_fiscal_year_override(id)` 가드를 추가해 매핑된 항목은 애초에 gap-log에 안 남도록 수정. 재검증: 6건→2건.

- **K-IFRS 업종 특화 기준서 3종 제외** (`5d2c780`)
  - 사용자가 캘린더에서 "제1117호 보험계약"이 팜한농(보험업 아님)과 무관하다고 지적 → 현재 수집분 전수 조사 후 목록·의견 제시, 사용자가 "제외" 방식(별도 표시 아님) 확정.
  - `APPLICABILITY.excluded_entities.industry_specific`에 `"제1117호"`(보험계약)·`"제1104호"`(보험계약, 구기준)·`"제2115호"`(부동산건설약정) 3개 키워드 추가. 애매해서 넣지 않은 것(제1106호/제2120호/제2112호/제1041호/이자율지표 개혁)은 사용자가 "농림어업은 종자 사업 때문에 실제로 걸릴 수 있다"며 그대로 두기로 확정.
  - **주의**: 제1104호는 "2020년 이자율지표 개혁 - 2단계"(업종 무관, 유지해야 함) 제목과 겹칠 위험이 있어 `is_applicable()`에 `if k == "제1104호" and "이자율지표" in title: continue` 가드를 넣어 충돌 방지(실측 8건 전수 확인).
  - 제외 결과는 `docs/EXCLUDED_LOG.md`의 `excluded:industry_specific` 버킷에 기록(과다 필터링 검토용). **참고**: 이번에 추가한 키워드는 3개(제1117호/제1104호/제2115호)이고, "제1011호"는 키워드로 넣지 않았다 — 2015년 건설계약 공시 항목 제목에 제1011호/제1037호/제1115호/제2115호가 함께 나열돼 있어 제2115호 매칭으로 그 항목 전체가 제외됐을 뿐, 제1011호 자체가 독립 제외 키워드로 등록된 건 아니다.

- **디자인 개선 — 계획 제시까지, 미구현**: 배지 위계(카테고리만 항상 강조, 나머지는 톤다운)·여백 재구성(관련 항목은 붙이고 섹션은 떼기)·타이포 대비 강화·색상 축소 4가지 방향의 구체안을 `styles.css` 범위로 제시했으나, 사용자 승인 전에 이번 커밋 시점(NEXT.md 갱신 요청)이 와서 **아직 파일에 반영 안 함**. `/mnt/skills/public/frontend-design/SKILL.md`는 이 환경에 존재하지 않아 직접 디자인 판단으로 대체한다고 사용자에게 알린 상태.

## 2026-08-31 세션 요약 (커밋 `00ef998`~`d846cda`, 8개 커밋)

이 세션에서 SPEC-ADDENDUM-5~8을 순서대로 처리했고, KASB 소스 2개를 추가했고,
`doc_type_of()`의 오래된 부분일치 버그를 잡았다. 아래는 최신 것부터 역순 요약 —
자세한 내용은 각 커밋 메시지 참고(전부 실측·재수집·테스트로 검증하고 커밋했다).

- **SPEC-ADDENDUM-8.md §1(검색)+§2(캘린더 정렬) 구현, §4(AI 요약) 재설계** (`d846cda`)
  - §1: 오늘의 정책동향/전체 동향 양쪽에 검색창(`state.q`, URL `?q=` 동기화, 200ms 디바운스, 공백 토큰 AND 매칭). addendum 원문 pseudo-code가 공백을 먼저 지운 뒤 공백으로 split해서 토큰화가 무력화되는 버그가 있어 순서를 고쳐 구현.
  - §2: "시행일 캘린더" 탭에 미래(가까운 순)/과거(최근 순) 구분 + "시행 예정"/"시행 완료" 라벨 + 과거 10건 기본 노출("과거 일정 더 보기"). **사이드바 위젯은 §2-4가 "변경 없음"이라 명시** — 재검토 중 실수로 거기까지 건드릴 뻔한 걸 발견해서 `scheduleItemHtml(s, hideDdayIfPast)`로 매개변수를 분리해 방지. `Array#map`에 함수를 직접 넘기면 index가 두 번째 인자에 섞여드는 문제도 전 호출부에서 래퍼로 방지.
  - §4: **유료 Anthropic API 대신 Claude Code가 직접 요약을 생성해 캐시에 저장하는 방식으로 재설계**(사용자 지시 — "내가 필요할 때마다 시킬게"). `data/summary_cache.json`(§4-3 구조 그대로) + `sources/_summary_cache.py`(load/save/write_entry) + `sources/summary_candidates.py`(대상 후보만 나열, 생성은 안 함 — 실측: 현재 30건) 신규. `_summarize.summarize()`가 캐시 우선 조회 후 없으면 기존 규칙 기반 폴백, `ai_generated` 플래그로 카드에 "(AI 생성)" 라벨+보라색 강조(§5-1). §4-4 원안의 "상설자료"는 doc_type이 아니라 `is_static` 플래그라 바로잡음. §3(본문 수집 인프라)은 안 만듦 — Claude Code가 후보 처리 시 원문 URL을 그때그때 직접 읽으면 되므로 불필요하다고 판단.
  - 캐시가 비어있어 이번 커밋은 기존 규칙 기반 동작과 100% 동일(163건 전부 `ai_generated=false` 확인).
  - **미검증**: 이 환경에 브라우저 구동 도구(chromium-cli/Node)가 없어 실제 화면 렌더링을 확인 못 함. JS 문법(괄호 균형)과 로직은 재검토했고 그 과정에서 위 2개 버그를 직접 찾아 고쳤지만, 시각적 확인은 사용자 몫으로 남음.

- **`doc_type_of()` 부분일치 오분류 수정** (`e3a1c06`) — 같은 클래스 버그가 `is_discussion_material()`(2026-08-28) 이후 두 번째로 나와서 사용자가 근본 수정을 지시.
  - `_norm()`(공백 전부 제거) 대신 `_norm_keep_spaces()`로 전환 + 다어절 키워드 9개에 공백 없는 형태를 나란히 추가(기존 "공개초안"/"공개 초안" 방식과 동일).
  - **1차 진단이 틀렸음을 재검증 중 발견**: "…ISSB 6월 논의내용 및 회의결과 보고…"의 "회의결과"는 원문 자체가 공백 없는 복합명사라 `_norm_keep_spaces()`만으로는 "의결"과의 부분일치를 못 막음 — `_MEETING_RESULT_RE`(회의결과/논의결과 복합어 가드)를 추가로 도입해 해결.
  - 전체 시스템 영향 확인(사용자 지시): 재수집 전/후 109건 전수 대조 → 분류 변경은 원래 문제였던 KASB ESG 위원회 항목 2건뿐(제·개정→보도자료로 정상화), 나머지 107건 불변. 테스트 279→295개.

- **KASB 소스 2개 추가** (`e61bac5`→`64bbbf3`→`4c46900`)
  - **C: 주요일정**(`calListA.do`) — 위원회 회의·세미나 등 진행일자 기준 캘린더. 연도/적용기준 드롭다운이 전부 클라이언트 JS라 쿼리 없이 GET 한 번으로 전체(73건, K-IFRS/ESG committee만 채택)가 온다는 걸 실측 확인. `is_meeting_schedule` 플래그 신설(캘린더에서 "회의 예정"과 "시행일"을 시각적으로 구분 — 속 빈 고리 vs 꽉 찬 점, `_summarize.py` 문구도 "~부터 적용" 대신 "~ 위원회 회의 예정 · 안건 의결 시 시행일 별도 확인"으로 분리).
    - 버그: 지속가능성기준위원회 자체 회의 안건에 ISSB가 언급되면 §3(해외기준 안A)이 "해외기준"으로 오분류 — 위원회명을 `foreign_exception_context`에 추가해 해결.
  - **D: 제개정현황**(`List2006.do`) — "적용기준=한국채택국제회계기준"인 행만 수집, **K-IFRS 시행일이 직접 담겨 있는** 유일한 소스(그동안 K-IFRS 시행일을 못 뽑았던 문제 해결). 미래 시행일이면 `schedules[]`에도 자동 반영(effective_date를 쓰는 기존 파이프라인 그대로 재사용).
    - 버그: 같은 기준서(예: K-IFRS 1117)가 여러 해에 걸쳐 별도로 제·개정되면 "제개정명(관련기준서)"만으로는 제목이 완전히 같아져서 `dedupe()`의 제목 완전일치 로직에 3건 중 2건이 사라짐 — 의결연도를 제목 앞에 붙여 해결(재검증: 54건 전부 고유 id/생존 확인).
  - kifrs 27→81건, 일정 19→73건.

- **SPEC-ADDENDUM-7.md §1~§4 완료** (`501993a`) — 개별 기업 소식/업종 특화/해외 기준/행사 안내.
  - §1: `is_company_event()`(자본시장 이벤트·실적·재무위기·시황 키워드) + §1-2 제조업 회계 예외(재고자산 등 문맥 있으면 통과). **버그 2건 실측 발견**: (1) "공포"가 COMPANY_EVENTS(시장 공포)와 그 STRONG_SIGNALS(법령 공포)에 동시에 있어 패닉 헤드라인이 자기 자신을 강한 신호로 오인 → STRONG_SIGNALS에서 제거. (2) "상장"/"비상" 부분일치가 "상장사"/"비상장회사" 같은 일반 명사를 오탐 제외(정상 K-IFRS 기사 4건 확인) → 부정 전방탐색 정규식으로 교체.
  - §2: 업종 특화 감리·회계(공동주택/협동조합/학교·병원회계 등)를 `APPLICABILITY.excluded_entities.industry_specific`에 추가.
  - §3(안 A): IASB/ISSB는 doc_type="해외기준"으로 분류해 수집은 유지하되 기본 조회/오늘의 정책동향에서만 제외. 프론트 뱃지·필터 버튼 추가.
  - §4: `is_admin_noise()`를 `is_event_announcement()`로 승격(전 어댑터 교체) — 영문 행사 키워드 + "제N회/제N차" 패턴.
  - 279개 테스트 통과, 재수집 105건(K-IFRS 25/세법 33/내부회계 32/ESG 15).

- **SPEC-ADDENDUM-6.md §1~§3 완료** (`948045d`) — 적용 대상 판정 게이트(신규·최상위) + 기관명 키워드 제거 + 홍보 키워드 보강.
  - §2: kifrs/tax에서 금융위원회/금융감독원/국세청/기획재정부 등 기관명 키워드 제거, 내용 기반 키워드로 대체.
  - §1: `is_applicable()` 신설 — **L1/L2/L3 전 계층 적용**(기존 필터와 달리 공식 소스도 면제 안 함). 제외 항목은 `docs/EXCLUDED_LOG.md`에 사유별로 기록. 사용자 검토 후 `excluded_entities.public`에서 "지방재정" 제거(지방세법 개정 관련 기사 오제외 확인).
  - §3: `ADMIN_NOISE_KEYWORDS`에 기관 홍보·외교 활동 표현 추가.
  - 107건(328건에서).

- **SPEC-ADDENDUM-5.md §5→§1→§3 반영·커밋** (`00ef998`) — 지난 세션에서 진단만 하고 미반영이었던 걸 실제로 `main.py` 파이프라인 순서 변경(§5 중복제거를 §1/§3보다 먼저) + 재수집 + 커밋까지 완료. 102건(328건에서).

## 지금까지 된 것 (2026-08-28 이전, 과거 세션 기록)

- **SPEC-ADDENDUM-5.md §5(중복제거)→§1(규제성 게이트)→§3(홍보성 제외) 완료**(사용자 지정 순서, 단계마다 카테고리별 건수 확인하며 진행 — 전부 3건 미만 없이 통과):
  - **§5**: `title_similarity()`가 `clean_title_for_compare()`로 정제한 제목을 비교하도록 변경(매체명 접미사 "- OO뉴스", 대괄호 접두사, 따옴표 제거). `extract_subject()`(주체 추출, "남부발전, ..." → "남부발전") 신설. 병합 조건을 (a) 유사도≥0.55(날짜 무관) 또는 (b) 주체 일치+3일 이내+유사도≥0.35로 확장(기존 0.65 고정 임계값보다 관대해짐). `SIMILARITY_THRESHOLD` 0.65→0.55, `SUBJECT_SIMILARITY_THRESHOLD`=0.35 신설.
    - **addendum 원안 버그 2건 직접 발견·수정**: (1) `clean_title_for_compare()`가 쉼표까지 공백으로 바꿔버려서 정작 addendum 자신의 §5-3 예시("남부발전, ...")의 주체 추출이 깨지는 문제 — 쉼표·가운뎃점은 안 지우도록 수정(`title_similarity`의 어절 추출엔 어차피 영향 없음). (2) `MEDIA_SUFFIX_RE`가 공백을 허용해서 "법인세법 시행령 개정안 — 접대비 한도"의 "접대비 한도"(2어절, 실제 내용 차이)까지 매체명으로 오인해 지워버려 §5-4가 명시적으로 "묶이면 안 된다"고 한 케이스가 오탐 병합될 뻔함 — 트레일링 세그먼트에 공백 있으면 매체명으로 안 보도록 정규식 수정.
    - 실측(단독 적용): kifrs 26 / tax 41 / icfr 32 / esg 16. `duplicate_count>0` 병합 6건(이전 §3-only 기준 2건보다 증가 — 개선 확인).
  - **§1**: `has_regulatory_signal()`(REGULATORY_SIGNALS 키워드) 신설, L3만 적용(L1/L2는 `is_noise_l3()`의 `tier==1` 분기에서 이미 게이트 면제). addendum 자신이 명시한 한계(§1-3: "강화"가 목록에 있어 "…내부 통제 강화 포석" 같은 군사 기사를 §1 단독으로는 못 거름, §2가 있어야 완전 해결)를 테스트로 그대로 문서화해둠.
    - 실측: kifrs 26(변화없음, 대부분 L1/L2) / **tax 41→37**(4건 감소) / icfr 32(변화없음) / esg 16(변화없음).
  - **§3**: `is_corporate_pr()`(CORPORATE_PR_KEYWORDS + CORPORATE_PR_STRONG_SIGNALS 오버라이드) 신설.
    - 실측: kifrs 26 / tax 37(§1과 동일, 이번 크롤링엔 추가로 걸린 홍보성 L3 없음) / icfr 32 / esg 16.
  - `is_noise_l3()`에 §1→§3 순서로 통합(§7 처리순서 그대로, §2·§6 스킵). 스키마 검증 통과. 테스트 205→237개 통과(신규: `TestCleanTitleForCompare`/`TestExtractSubject`/`TestHasRegulatorySignal`/`TestIsCorporatePr`/dedup 신규 케이스 6개).
  - **미검증**: §7이 요구하는 "단계별 제외 건수 로그"(`[L3 필터] tax: 원본 71 → 규제성 42 → ...` 형식)는 아직 안 만들었다 — `is_noise_l3()`가 단일 bool 함수라 세부 카운터가 없어서, 이번엔 각 단계 재실행 시점의 카테고리별 최종 합계로만 보고했다. 필요하면 별도 계측 추가 가능. 브라우저 렌더링도 여전히 미확인.

- **"논의자료" doc_type 신설**

- **"논의자료" doc_type 신설**(2026-08-28 사용자 피드백, addendum 문서 없이 직접 지시): "제1118호 정착지원 TF 논의 내용(4차)" 같은 TF·실무그룹 중간 산출물은 실무에 쓸 게 없다는 지적. `_config.DISCUSSION_MATERIAL_KEYWORDS`(TF/태스크포스/논의 내용/회의 결과/진행 경과/중간 보고/검토 경과/워킹그룹/실무그룹) + `DISCUSSION_OVERRIDE_KEYWORDS`(의결/공표/제정/개정/확정 — 함께 있으면 재분류 안 함, 사용자 지시) 신설.
  - `_utils.is_discussion_material()`을 **`finalize_item()`에서** 적용 — `doc_type_of()`를 거치든 어댑터가 하드코딩했든(실제 원인: `kasb.py`의 `fetch_qna()`가 A3 게시판 전체를 `doc_type="질의회신"`으로 고정하고 있었음) 전부 한 곳에서 잡히도록 단일 지점으로 설계.
  - **버그 하나 잡음**: 최초 구현은 공백을 전부 지우는 기존 `_norm()`을 그대로 썼는데, "회의 결과"가 공백 제거 후 "회의결과"가 되면서 override 키워드 "의결"이 그 안에 우연히 부분 문자열로 끼어(회+**의결**+과) "회의 결과"가 있는 제목은 절대 논의자료로 안 잡히는 버그가 됨. 공백을 한 칸으로만 정리하는 `_norm_keep_spaces()`를 별도로 만들어 이 함수에서만 사용하도록 수정(단위테스트로 재현·고정).
  - 프론트: 상설자료와 같은 원칙으로 "오늘의 정책동향"과 기본 조회에서 제외하되, 상설자료(날짜 기반)와 달리 논의자료는 최신 날짜일 수 있어 **문서종류 필터에서 "논의자료"를 직접 선택했을 때만** 노출(날짜 범위와 무관). 기존 "제·개정만"/"질의회신만"/"공개초안만"과 같은 방식의 "논의자료만" 빠른 버튼 추가(`data-doctype="논의자료"` — 기존 공용 핸들러 재사용, 새 JS 불필요).
  - 스키마(`_schema.py`)의 `DOC_TYPES`에 "논의자료" 추가(stage는 기존 `compute_stage()`의 기본값 "참고"로 자동 처리).
  - 재수집 결과: kifrs의 "TF 논의 내용" 5건 전부 `doc_type="논의자료"`로 재분류 확인, 나머지 정상 질의회신 5건은 그대로 유지 확인. 스키마 검증 통과, 테스트 205→216개 통과.
  - **미검증**: 브라우저 렌더링(동일 사유). "논의자료만" 버튼 클릭 시 실제로 카드가 나오는지, 기본 조회에서 실제로 안 보이는지 확인 필요.

- **SPEC-ADDENDUM-5.md §4 완료**(§1/§2/§3/§5/§6/§8/§9는 사용자가 결과 확인 후 진행하기로 보류): `icfr`/`kifrs` 카테고리의 `required`를 `required_strong`/`required_weak`/`weak_context`로 분리. "내부통제"(icfr)·"금융위원회"/"금융감독원"(kifrs) 같은 일반 명사 성격 키워드는 `weak_context`(회계 문맥 단어)와 함께 있을 때만 인정 — `_utils._has_required_match()`/`_required_list()` 신설, `match_loose`/`keyword_score`/`matched_keywords`/`build_google_query`가 전부 이걸 통해 동작하도록 리팩터링(tax/esg는 기존 `required` 그대로 하위호환).
  - 재수집 결과: icfr 26→32건(제목 전수 확인 — 전부 회계·감사 문맥, 군사/일반홍보성 0건), kifrs 26건 유지(전부 K-IFRS/회계기준원/금융위+회계문맥 관련). addendum §0 진단표의 icfr 관련 사례(타에브 군부 기사, 남부발전/캠코-한수원 홍보성)는 원본 재현은 못 했지만(그날그날 뉴스가 달라짐) 신규 유닛테스트 11개로 정확히 그 판정 로직을 검증함(`tests/test_utils.py::TestRequiredStrongWeakGating`).
  - 발견한 부수 이슈(§4 범위 밖, 별도 기록): kifrs에 제목이 "보도자료 - 금융위원회"로 뭉뚱그려진 항목 1건 발견 — `classify()` 게이트를 안 거치는 경로(KASB A1 게시판이 스스로 "회계기준소식"으로 태깅한 항목은 `_NOTICE_CATEGORY_MAP`에서 바로 카테고리를 확정하고 `classify()`를 안 거침)라 §4와 무관한 기존 동작. 제목 추출 자체가 부실한 원본 소스 문제로 보이며 시급하지 않음.
  - 스키마 검증 통과, 테스트 194→205개 통과.
- **사용자 확인 대기 중**: 위 §4 결과를 보고 나머지(§1 규제성 게이트, §2 무관 업종 제외, §3 홍보성 제외, §5 중복제거 개선, §6 관련성 점수, §8 `data/filters.yml` 설정파일화, §9 `tests/test_relevance.py`) 진행 여부/순서를 사용자가 정할 것.

- Phase 3A~3E(SPEC-ADDENDUM.md 기준): 소스 접근성 조사, 공식 소스 어댑터(KASB/FSS/MOEF/NTS/FSC/정책브리핑/법제처) 전부 구현·실측 검증.
- Phase 4(SPEC.md 기준): `_summarize.py`/`schedules.py`/`main.py` 오케스트레이터 구현. `python -m sources.main` 실행하면 실데이터로 `site/data.json`이 생성되고 스키마 검증까지 통과한다(최근 실행: 313건 원본 → 116건, 세법 41 / 내부회계 33 / K-IFRS 26 / ESG 16, 일정 18건).
- Phase 5(SPEC.md §7 + ADDENDUM-2 §2-3 기준) — `site/index.html`/`app.js`/`styles.css`를 전면 새로 작성함. 실데이터(`site/data.json`, 116건)에 바로 연결(더미 단계는 건너뜀 — 실데이터가 이미 스키마를 통과한 상태였기 때문).
  - 구현: 상단 sticky 네비 + 카테고리 4종 연동, 필터 바(카테고리 칩 다중선택·문서종류 드롭다운·날짜 범위+빠른선택·정렬), 날짜별 그룹 피드 카드(카테고리/문서종류/단계 뱃지, 공식 라벨, 실무영향 박스, 뉴스/원문 버튼), `stage`("확정"만 저장됨)를 `effective_date`로 클라이언트에서 "시행예정"/"시행중"으로 재계산(ADDENDUM-2 §2-2), 우측 sticky 미니 캘린더(월 이동·일정 dot·클릭 시 하이라이트)+시행 예정 일정 리스트(D-Day 클라이언트 계산), URL 쿼리스트링 동기화(`?cat=&doctype=&from=&to=&sort=`), `data.json` fetch 실패 시 `data.js` 폴백(스키마 맞춰 갱신함) → 그것도 실패 시 오류 문구, 로딩 스켈레톤 3장, 반응형 3단계(1280/1024/640px, `<1024px`는 필터→일정→피드 순서로 재배치 + 캘린더 `<details>` 접힘).
  - 검증: `python -m http.server`로 5개 정적 파일 전부 200 확인, `python -m sources._schema site/data.json` 재검증 통과, `pytest tests/` 166개 그대로 통과(프론트는 파이썬 테스트 대상 아님).
  - **미검증**: 실제 브라우저 렌더링/반응형 스크린샷은 못 했다 — 이 세션에서 Claude in Chrome 확장 설치를 사용자가 거절함. 코드 리뷰(HTML id 교차검증, CSS 로직 재검토)로만 확인한 상태. **사용자가 직접 브라우저로 열어서(`python -m http.server` 후 `localhost:PORT`) 데스크톱/모바일 확인 필요** — SPEC.md §8 Phase 5 완료조건("데스크톱/모바일 스크린샷")이 아직 미충족.
- Phase 5 화면 검수 반영 1차(2026-08-28, 사용자가 실제 화면 보고 지적한 4건): 요약이 제목/출처를 반복하던 문제, 실무영향 문구가 카테고리와 안 맞던 문제, 캘린더가 안 보이던 문제(`<details>` 강제-노출 CSS가 브라우저에서 불안정 → 버튼+클래스 토글로 교체) 수정. "시행 예정 일정 0건"은 코드 버그가 아니라 법제처 테스트 OC가 그 시점엔 미래 시행일 항목을 안 돌려준 실제 데이터 특성으로 확인됨(items[]→schedules[] 변환 18=18 일치 확인).
- **SPEC-ADDENDUM-4.md §1~§4 완료**(§5 "오늘의 정책동향" 탭, §6 푸터는 사용자 지시대로 아직 안 함):
  - §1 조직 운영성 공지 제외: `_config.ADMIN_NOISE_KEYWORDS` + `_utils.is_admin_noise()` 신설. tier 무관(L1 공식소스도) 적용 — `is_noise_l3()`에 통합해 google_news/naver_news는 자동 반영, kasb/fss/moef/nts/fsc/policy_briefing은 각 어댑터의 파싱 루프에 직접 삽입. law_api.py는 법령명만 다뤄서 제외(관련 문구가 나올 수 없는 소스). 실측: "금융위원회 인사보도(과장급 전보)" 등 admin-noise 0건으로 확인.
  - §2 상시 비치 자료: `_utils.extract_title_revision_date()`(제목 속 "(2021.10.1. 개정)" 등 4종 패턴) + `is_static`/`date_estimated` 필드 신설. 현재 실제로 해당하는 소스는 `fss.py`의 B3(k-icfr.org 운영위원회 모범규준)뿐이라 거기만 `is_static=True` 고정 적용(kasb.py A2는 이미 Phase 3에서 fetch()에서 제외돼 있어 손 안 댐). 프론트: 카드에 회색 "상설자료" 뱃지, 정렬 시 신규 항목보다 아래로 데모션, 필터 바에 "상설자료만" 빠른 버튼 추가. 실측: 11건이 is_static=true로 잡히고 전부 제목에서 날짜 추출 성공(date_estimated=false).
  - §3 유사 기사 중복 제거: `_utils.title_similarity()`(자카드) + `dedupe_similar_news()`(L3만, 카테고리+3일 이내), `duplicate_count`/`duplicate_sources` 필드. 실측: "남부발전 내부통제" 기사(3개 매체 → 1건 + `duplicate_count=2`)로 addendum 예시 그대로 재현·병합 확인.
  - §4 공식-뉴스 연결: `_utils.attach_related_news()` + `extract_core_phrase()`("핵심 명사구"는 형태소 분석 없는 어절 기반 근사치). `related_news` 필드, 흡수된 L3는 피드에서 제외(`main.py`가 `layer` 필드 삭제 전에 처리). 실측: 이번 데이터셋에서는 조건(같은 카테고리+7일 이내+유사도)을 만족하는 짝이 없어 0건 연결됨 — 로직 자체는 신규 유닛테스트 6개로 검증됨(진짜 화면에서 보려면 실데이터에 조건 맞는 공식+뉴스 쌍이 나올 때까지 기다리거나, 다음 실행에서 재확인 필요).
  - 스키마(`_schema.py`)에 5개 필드 추가(`is_static`/`date_estimated`/`duplicate_count`/`duplicate_sources`/`related_news`), `summary`는 `minItems: 0`으로 완화(위 요약 수정 건과 연결).
  - 재수집 실행 결과: 230건 원본 → 106건(세법 31 / 내부회계 33 / K-IFRS 26 / ESG 16), 일정 18건, 스키마 검증 통과. 테스트 192개 통과.
  - **미검증**: 브라우저 렌더링(위 미검증 항목과 동일 사유 — Claude in Chrome 미설치). §4는 특히 실데이터에서 관련 뉴스가 붙은 카드를 아직 육안으로 못 봤다.
- 테스트 192개 통과(`pytest tests/`).
- **화면 검수 반영 2차**(2026-08-28, 같은 세션 후속 피드백 2건):
  1. 상설자료가 날짜 필터를 통과하던 버그 — 실제 원인은 `extract_title_revision_date()`가 "(2021.10.1. 개정)"처럼 일(day)까지 있는 형식만 잡고 "(2012.12)"/"新모범규준(2018.6)"처럼 **연.월만 있고 일이 없는** 형식을 못 잡아 오늘 날짜로 샌 것. 연.월만 있으면 1일로 간주하는 세 번째 정규식(`_TITLE_DATE_YEAR_MONTH_RE`)을 추가해 해결(재수집 확인: 2012-12-01/2018-06-01로 정확히 나옴). 날짜 필터·그룹핑은 원래도 둘 다 `published_at` 기준으로 이미 일치했었다 — 데이터 자체가 틀려서 어긋나 보인 것.
  2. 상설자료를 기본 조회에서 제외 — "기본"을 앱의 최장 빠른선택 기준인 **90일**로 정의: 조회 기간이 90일 이하면 상설자료 하드 제외, 90일보다 넓게 잡으면 실제 `published_at`으로 정상 필터링(과거로 충분히 넓히면 다시 보임), "상설자료만" 버튼은 날짜 필터와 무관하게 항상 상설자료만 보여줌. `site/app.js`의 `filterItems()`/`isWideDateRange()` 참고. **이 세 갈래 동작은 사용자 문장을 최대한 문자 그대로 해석한 설계라 실제 의도와 다를 수 있음 — 확인 필요.**
- **SPEC-ADDENDUM-4.md §5 "오늘의 정책동향" + §6 푸터 완료**:
  - §5: 네비게이션을 카테고리 바로가기 4개 → 탭 3개(오늘의 정책동향/전체 동향/시행일 캘린더)로 교체(기본 진입 = 오늘의 정책동향). "오늘"은 `meta.generated_at` 날짜 기준, 5건 미만이면 최근 3일로 확대(안내문구 표시), `is_static` 전부 제외. 공식/보도 그룹 분리(`source.type` 필드로 판별 — `layer`는 `finalize_item()`에서 지워지므로 못 씀), 공식은 tier→final_score, 보도는 final_score로 정렬, 그룹당 12건 cap + "더 보기"(전체 동향 탭으로 전환). 카드: 좌측 카테고리 컬러바(공식 solid/보도 40% 투명도 — `hexToRgba()`), 요약 최대 2줄, impact 박스, 관련보도 접이식(공식만). "시행일 캘린더" 탭은 사이드바 캘린더/일정리스트 렌더 로직을 `renderCalendarInto()`/`scheduleItemHtml()`로 공유 리팩터링해 재사용 — 전체 화면 버전은 기간 제한 없이 전체 18건을 다 보여줌. `localStorage` 사용 없음(애초에 안 썼음, 확인 완료) — "내가 찜한 문서" 탭은 네비게이션에서 제외.
  - §6: `<footer>`를 body 최하단에 항상 노출(스크롤 무관 — "고정"을 position:fixed가 아니라 "언제나 존재"로 해석; 대시보드 특성상 겹침 방지 목적). 8개 기관 링크 전부 `target="_blank" rel="noopener"`, 고지 문구는 addendum 원문 그대로 포함.
  - 초기화 시 `<section id="viewToday">`를 카테고리 nav 버튼(`#navCats`) 제거에 맞춰 관련 JS도 정리함 — 지우다가 실제로 `document.getElementById("navCats")`가 null이라 `init()` 전체가 죽는 버그를 만들 뻔했고 커밋 전에 직접 잡아 고침(교차검증 습관화 필요).
  - **미검증**: 이번에도 브라우저 렌더링 확인은 못 했다. 특히 §5는 신규 화면이라 실제로 봐야 할 것 많음(3열/2열/1열 그리드 줄바꿈, 탭 전환, 카드 색상바).

## 2026-09-02 세션 진행 중

- **신규 항목 메일 알림 신설** — GitHub Actions 수집 완료 후 신규 항목이 있으면 메일 발송.
  - `sources/notify_mail.py` 신규: `find_new_items()`(id 기준, 수집 실행 "전" 백업한 이전 data.json과 비교) → `is_official()`로 공식(L1/L2, `source.type=="official"`) vs 언론(L3) 분리 → 카테고리별 그룹핑(`group_by_category()`, `_config.CATEGORIES` 선언 순서) → 제목/본문 조립 → `send_via_gmail()`(표준 `smtplib`, 의존성 추가 없음).
  - **발송 조건**(2026-09-02 사용자 지시로 최초안에서 변경): 공식만이 아니라 **공식 또는 언론 둘 중 하나라도 신규가 있으면 발송**(뉴스는 매일 들어오는 게 아니라 도배 걱정 없다고 판단). 본문은 "공식 기관 발표"(제목+요약+실무영향+링크) 섹션이 위, "언론 보도"(제목+링크만, 요약 없음) 섹션이 아래 — 한쪽이 0건이면 그 섹션 자체를 뺀다. 제목 `"[Policy Watch] 신규 N건 - YYYY.MM.DD"`의 N은 공식+언론 합계.
  - `MAIL_TO`는 쉼표로 분리해 수신자 목록으로 처리(`parse_recipients()`, 향후 여러 명 대비 — 사용자 지시).
  - 시크릿(`GMAIL_USER`/`GMAIL_APP_PASSWORD`/`MAIL_TO`) 중 하나라도 없으면 조용히 스킵, 발송 자체가 실패해도(SMTP 오류 등) `main()`이 전체를 try/except로 감싸 **exit 0 유지** — 메일 기능이 수집·배포 파이프라인을 절대 막지 않는다.
  - `.github/workflows/crawl.yml`: `workflow_dispatch.inputs.force_mail`(boolean, 기본 false) 추가 — 신규 없어도 강제 발송(테스트용, 신규 생길 때까지 기다릴 필요 없게). `crawl` 잡에 "이전 data.json 백업"(수집 실행 전, `/tmp/pw_prev_data.json`) → "수집 실행" → "신규 항목 메일 알림"(`python -m sources.notify_mail`) 3단계로 재배치.
  - `tests/test_notify_mail.py` 신규 33개(diff/그룹핑/제목·본문/수신자 파싱/발송 게이팅 — SMTP는 전부 monkeypatch로 대체, 실제 메일 발송 없음). 테스트 345→378개 통과.
  - **미검증**: 실제 GitHub Actions에서 Gmail 발송이 정말 되는지(시크릿은 사용자가 이미 등록함) — `workflow_dispatch`에서 `force_mail: true`로 한 번 수동 실행해 확인 필요.
  - **2026-09-02 후속 수정 3건**(발송 조건은 그대로 유지, 형식만 개선):
    1. 구글 뉴스 RSS 링크가 200자 넘어 plain text 메일이 안 읽히던 문제 — **HTML 메일**(제목 자체에 `<a href>` 링크, URL 문자열은 화면에 안 보임) + **plain text 대체본**(alternative, HTML 못 읽는 클라이언트용, 여기는 원래대로 "링크: URL" 노출) 이중 발송으로 전환. 아웃룩 호환을 위해 `<div>/<p>/<a>/<b>/<hr>` 기본 태그 + 인라인 style만 사용(flexbox/grid/이미지 없음). `build_body_text()`/`build_body_html()`로 분리, 공통 구조(`_sections()`)를 공유해 두 렌더러가 어긋나지 않게 함.
    2. 발신자 표시 이름 `"Policy Watch <GMAIL_USER>"` — `email.utils.formataddr()` 사용.
    3. 메일 하단에 "이 메일은 신규 항목이 있을 때만 발송됩니다" 고정 문구(`_FOOTER_NOTE`) 추가.
    - 테스트 44개(11개 추가: HTML 이스케이프·앵커·섹션순서 등), 전체 389개 통과.

- **"현행 기준" 탭 신설** — 4개 분야(K-IFRS/지속가능성 공시/세법/내부회계)의 "지금 유효한 기준·법령"을 새로 크롤링 없이 기존 수집 데이터에서 조립해 보여주는 4번째 탭(최근 정책동향/전체 동향/시행일 캘린더 다음).
  - `sources/current_standards.py` 신규 — 분야별 접근이 전부 다르다:
    - **K-IFRS**: `kasb.py` D(List2006.do 제·개정 이력)에서 제목의 "제NNNN호"를 정규식 추출해 기준서 번호별 최신 개정 1건만 남기고 **최근 5건만** 노출(`build_kifrs_standards()`). 전체 기준서(100여 종) 목록이 아니라 "개정 이력이 있는 것"만이라는 한계가 있어, 목록보다 **"전체 목록 보기" 링크**(`https://db.kasb.or.kr/standard`, 사용자 지정)를 우선하고 최근 개정은 참고용으로 아래 붙임.
    - **지속가능성 공시(KSSB)**: 제1호/제2호 그대로(`build_esg_standards()`) + `https://db.kasb.or.kr/esg` 전체 목록 링크.
    - **세법**: `law_api.py`(법제처)가 매 실행마다 이미 채워주는 현재 스냅샷(법인세법/부가가치세법/소득세법/지방세법/지방세특례제한법/조세특례제한법/국제조세조정에 관한 법률 각 본법+시행령+시행규칙, 18건)을 법령명 순서(요청 5개 법 우선 + 보너스 2개, 본법→시행령→시행규칙)로 정리(`build_tax_laws()`). 날짜 없으면 사용자 지시대로 빈 문자열.
    - **내부회계**: k-icfr.org에 모범규준/평가·보고 기준/적용지침 3분류별 안정 URL이 없다는 걸 확인(전체 진입점 1개 + 신/구버전 인덱스 2개뿐, 3분류 구분 없음) → 제목 키워드로 직접 분류(`build_icfr_documents()`, "개념체계"→모범규준, "적용기법"/"가이드라인"→적용지침, "평가"+"보고"+("모범규준"/"지침")→평가·보고 기준, 판정 우선순위는 이 순서로 검사해야 함 — 적용기법 문서에도 "평가"+"보고"가 섞여있는 경우가 많아서). 같은 문서의 재게시본(날짜만 다른 "Clean ver." 등)은 정규화 후 최신 published_at 하나만 남김.
  - `main.py`의 `build_data_json()`에서 `finalized` 리스트로 호출해 `data.json`에 최상위 `current_standards` 필드로 저장. `_schema.py`에 스키마 추가(4개 분야 구조가 서로 달라 분야별로 따로 정의).
  - 프론트: `index.html`에 4번째 nav 탭(`data-view="standards"`) + `<section id="viewStandards">`(4개 `<section class="std-section">`), `app.js`에 `renderKifrsStandards()`/`renderEsgStandards()`/`renderTaxStandards()`/`renderIcfrStandards()` + `renderCurrentStandards()`(init()에서 한 번만 렌더 — 필터/검색과 무관한 정적 참고 화면), `styles.css`에 `.std-table` 등 표 스타일 신규.
  - **버그 발견·수정**: `stateFromURL()`의 `?view=` 파서가 `today`/`all`/`calendar` 하드코딩 허용목록이라 `standards`가 빠져있었음 — `?view=standards` URL을 직접 열면 조용히 `today`로 리셋되는 문제. 배열 기반 `indexOf` 체크로 수정.
  - `tests/test_current_standards.py` 신규 23개(합성 데이터 — 실제 크롤링 결과에 테스트가 흔들리지 않도록), `tests/test_schema.py`에 `current_standards` 최소 픽스처 추가. 테스트 389→412개 통과. 실제 `site/data.json`(153건)에 대입해 스키마 0 errors 확인.
  - **미검증**: 브라우저 렌더링(Claude in Chrome 확장 설치를 사용자가 재차 거절 — 이번 세션엔 다시 권하지 않기로 함). 코드 리뷰(HTML id 교차검증, JS 문법 재확인)로만 확인한 상태 — 사용자가 직접 열어서 4개 섹션 표가 제대로 나오는지 확인 필요.

- **헤더 "오늘 챙길 것" 한 줄 추가** — 사용자가 형식 지정("D-3 회계기준위원회 회의 · 이번 주 신규 5건", 가장 임박한 일정 + 최근 신규 건수만). `.nav` 바로 아래 `.nav-highlight` 줄 신설. 가장 임박한 일정은 `sortSchedules().future[0]`(회의 예정/로드맵 예정 포함, D-day는 기존 `dday()`/`ddayLabel()` 재사용), 신규 건수는 "이번 주"(월요일 시작)를 `DATA.meta.generated_at` 기준일로 계산(클라이언트 로컬 날짜가 아니라 실제 수집일 기준 — "오늘의 정책동향"과 동일 원칙). 실측(2026-09-02 데이터 기준): "D-2 제9회 회계기준위원회(...) · 이번 주 신규 1건". 테스트 345개 통과, 정적 파일 200 확인. **미검증**: 브라우저 렌더링(줄바꿈 없이 ellipsis로 잘리는지 등) — 사용자 확인 필요.

- **디자인 개선 4종 반영 완료**(`0d3cfef`) — 지난 세션엔 계획만 있고 파일엔 없었던 걸, 현재 `styles.css`/`app.js`를 다시 보고 구체안(아래 4가지) 재정리 후 사용자 승인받아 반영:
  - 배지 위계: `badge-stage`(시행단계)·`badge-official`(공식) 꽉 채운 배경 → outline 톤다운(카테고리 배지만 색 채움 유지).
  - 여백 재구성: 카드 내부(요약/실무영향/토글) 간격 14px→8px, 날짜 그룹 간(`.feed`) 32px→44px.
  - 타이포 대비: `card-title`/`today-card-title` 600→700, `card-summary`/`today-card-summary` `--muted`→`--ink`.
  - 색상 축소: `badge-meeting`/`badge-roadmap`을 주황/호박색(우연히 `--c-icfr`와 동일)에서 중립 `--muted`로 통일(캘린더 점은 모양으로 이미 구분돼 있어 배지는 색 불필요 확인).
  - 테스트 345개 통과, `python -m http.server`로 정적 파일 200 확인. **미검증**: 실제 브라우저 렌더링 — 사용자 확인 필요, 확인 후 괜찮으면 push해서 배포 반영.

## 다음 순서

사용자가 2026-09-01 세션 마지막에 정리한 "남은 일" 중 남은 것:
- **요약은 주 1~2회 몰아서 처리** — 매일 크롤링에서 새 후보가 계속 쌓이므로, 그때그때가 아니라 주기적으로 배치 처리하는 운영 방식으로 확정.
- **시행완료 "더보기" 버튼 미표시** — 원인 조사(console.log 계측)까지 했으나 우선순위 낮음으로 확정, 보류 중.
- **뉴스(L3) 기사는 AI 요약 대상에서 제외하기로 확정** — 공식/L1/L2 문서만 요약.

그 외 이전부터 미착수:
- SPEC-ADDENDUM-5.md §6(관련성 점수)·§8(`data/filters.yml` 설정파일화) — 여전히 미착수, 우선순위 계속 밀림.
- **PROXY_BASE 실전 검증** — Secrets에는 등록됐으나(2026-09-01), GitHub Actions 크롤링 실행에서 `law.go.kr` 등 차단 시 실제로 우회하는지는 아직 로그로 확인 안 함.

### 브라우저 확인 (사용자가 직접)
```
cd C:\policy-watch\site
python -m http.server 8791
# 이후 브라우저에서 http://localhost:8791 열기
```
Phase 6 배포 완료 후로는 실제 배포 사이트(GitHub Pages)에서도 확인 가능 — 이번 세션 버그 대부분이 사용자가 배포 사이트를 직접 보다가 찾은 것.

## 운영 준비물 (시크릿/설정)

| 항목 | 현재 상태 | 필요 조치 |
|---|---|---|
| `LAW_API_OC` | 미설정 — 법제처 공개 테스트용 "test"로 대체 동작 중(실제 데이터는 나오지만 사용량 제한 가능성) | 실 서비스 전환 전에 정식 OC 코드 발급 |
| `NAVER_CLIENT_ID`/`NAVER_CLIENT_SECRET` | 미설정 — `naver_news.py` 전체가 매 실행 스킵됨(graceful degradation 정상 동작) | 발급 후 GitHub Secrets에 등록 |
| `PROXY_BASE` | **GitHub Secrets에 등록됨(2026-09-01)** — Actions에서 실제 우회 동작은 아직 로그로 미확인 | 다음 Actions 실행 로그에서 law.go.kr 등 정상 수집되는지 확인 |
| `data/schedules_manual.yml` | 비어있음(`[]`) — 사업연도 기준 근사 시행일은 `_FISCAL_YEAR_EFFECTIVE_DATES`(코드 내 수동 매핑)로 대신 처리해서 아직 이 파일을 쓸 일이 없었음 | `docs/EFFECTIVE_DATE_GAPS.md`(현재 2건) 검토해서 필요하면 수동 추가 |
| `data/esg_roadmap.yml` | **신규** — KSSB/ESG 공시 로드맵(금융위 발표 기준, 1차 2028-01-01/FY2027) 수동 관리 중 | 금융위 로드맵이 실제로 바뀌면(확정 등) 수동 갱신 |
| `data/summary_cache.json` | **43건 채워짐**(Claude Code가 원문 읽고 직접 작성 — API 키 불필요) | 새 후보 생길 때마다 사용자가 "요약해줘"로 배치 요청(주 1~2회 목표) |
| `GMAIL_USER`/`GMAIL_APP_PASSWORD`/`MAIL_TO` | **GitHub Secrets에 등록됨(2026-09-02)** — `sources/notify_mail.py` 실전 발송은 아직 미확인 | `workflow_dispatch`에서 `force_mail: true`로 수동 실행해 실제 메일 수신 확인 |
| ~~`ANTHROPIC_API_KEY`~~ | **불필요** — 유료 API 대신 Claude Code가 직접 요약 생성하는 방식으로 재설계 완료 | 없음 |

## 알려진 이슈 / 기술 부채 (심각도순은 아님)

1. **`google_news.py`에 title 레벨 재검증 게이트가 없다.** `naver_news.py`는 `match_loose(title, cat_key)`로 제목에 카테고리 키워드가 실제로 있는지 한 번 더 거르는데, `google_news.py`는 구글이 매칭시킨 결과를 그대로 믿는다. 실행 중 실제로 노이즈 사례 발견됨: 내부회계(icfr) 카테고리에 "클린코어(ZONE), 도지코인 금고 비웠다..." 기사가 `matched_keywords=[]`인 채로 섞여 들어왔다. `naver_news.py`와 같은 게이트를 추가할지 사용자 확인 후 진행.
2. **KASB/NTS 첨부파일 다운로드 URL 미해결.** 전부 `javascript:fileDownload(...)`/`javascript:htmlDocTransView(...)` 형태라 목록 HTML만으로 실제 파일 URL을 못 만든다(FSC/FSS는 평문 href라 이미 해결됨). `attachments=None`(A1/A3/C) 또는 파일명만 있고 `url=None`(D: List2006.do, 2026-08-31 추가분)으로 남아있다.
3. **C3(KSSB 기준서 목록) 전용 게시판 미특정.** 지금은 A1(KASB 소식) 게시판에서 "제N호"/KSSB 키워드로 대체 필터링 중. kasb.or.kr을 더 뒤져서 정확한 게시판을 찾으면 개선 가능.
4. **예규·유권해석/판례/조세심판원 심판례 미구현.** SPEC-ADDENDUM-3.md §5에서 MVP 제외로 확정한 항목. `data/tax_subjects.yml`의 `features.collect_rulings`/`collect_precedents`/`collect_tribunal`이 전부 `false`로 준비는 돼 있으나, 실제 `sources/official/nts_rulings.py` 등 어댑터 파일 자체가 아직 없다(ADDENDUM-3 §5-1: "파일은 만들되 flag가 false면 빈 리스트 반환"까지가 원래 지침 — 파일 생성 자체를 안 함).
5. **정책브리핑(policy_briefing.py, L2)이 실측 기준 기여도가 거의 0에 가깝다.** 국세청·금융위원회가 정책브리핑 전체 게시물 중 비중이 작아(300건 중 2건 수준, SOURCE_PROBE.md 참고) 실행할 때마다 0건이 나오는 경우가 흔하다. 국세청은 D2(nts.py)가 있어 상관없지만, 금융위원회는 fsc.py가 이미 있어 실질적으로 중복 안전망 역할만 한다 — 문제는 아니지만 참고.
6. **`data/schedules_manual.yml`이 비어있다.** `docs/EFFECTIVE_DATE_GAPS.md`(매 실행 갱신됨, 2026-09-01 기준 2건 — 사업연도 근사 시행일 4건은 `_FISCAL_YEAR_EFFECTIVE_DATES`로 별도 처리해 여기서 빠짐)를 보고 관리자가 판단해서 채워 넣는 운영 프로세스가 아직 한 번도 실행 안 됨.
7. **"부분일치 오탐" 클래스 버그가 이 저장소에서 계속 나온다**(`is_discussion_material`의 "회의 결과"/"의결", `doc_type_of`의 "회의결과"/"의결", `is_company_event`의 "공포"·"상장"/"비상", `trust_of`의 `news.kicpa.or.kr`↔`kicpa.or.kr` 접미사 오상속, `is_applicable`의 "제1104호"↔"이자율지표 개혁"). 전부 `_norm()`이 공백을 지우거나, 두 단어가 우연히 이어 붙거나, 문자열 접미사/부분 매칭이 의도보다 넓게 걸려서 생겼다. **새 키워드를 `_config.py`에 추가할 때는 기존 키워드 목록과 부분일치 충돌이 없는지 먼저 확인하는 습관이 필요** — 특히 짧은 흔한 단어·도메인 접미사·기준서 번호는 위험도가 높다.
8. **시행완료 목록 "더보기" 버튼이 조건에 따라 안 보이는 경우가 있다** — 원인 조사(console.log 계측)까지 했으나 사용자가 우선순위를 낮게 판단해 보류 중(2026-09-01).

## 참고 문서

- `docs/SOURCE_PROBE.md`: Phase 3A~3E 전체 조사·구현 기록(가장 상세함).
- `docs/EFFECTIVE_DATE_GAPS.md`: 매 `python -m sources.main` 실행마다 최신 상태로 갱신되는 "시행일 수동 검토 목록".
