# 다음에 이어서 할 일 (NEXT)

마지막 갱신: 2026-08-31, SPEC-ADDENDUM-8.md §1(검색)+§2(캘린더 정렬) 구현·§4(AI 요약) 재설계 커밋(`d846cda`) 직후 기준.
현재 `site/data.json`: 163건(K-IFRS 81 / 세법 33 / 내부회계 32 / ESG 17), 일정 73건. 테스트 313개 통과.

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

## 다음 순서

### 사용자 확인 대기 (최우선)
- **브라우저 렌더링 확인이 계속 누적되고 있다.** 이 환경엔 여러 세션째 브라우저 구동 도구(chromium-cli/Node/Claude in Chrome)가 없어서 프론트엔드는 전부 코드 리뷰로만 검증했다. 특히 이번 세션(ADDENDUM-8)에서 새로 생긴 검색창 2개(오늘의 정책동향/전체 동향), "시행일 캘린더" 탭의 미래/과거 구분+"과거 일정 더 보기", "(AI 생성)" 라벨은 아직 한 번도 실제 화면에서 못 봤다. `python -m http.server`(사용법은 아래 "브라우저 확인" 참고)로 직접 열어서 확인 필요.
- **AI 요약**: `data/summary_cache.json`이 비어있어 전부 규칙 기반 문구다. "요약 생성해줘"라고 시키면 `python -m sources.summary_candidates`로 대상(현재 30건)을 뽑아 직접 읽고 채운다 — §5-3("생성된 요약 10건을 사용자가 직접 검토")은 실제로 몇 건 생성한 뒤에 적용할 것.
- SPEC-ADDENDUM-5.md §6(관련성 점수)·§8(`data/filters.yml` 설정파일화)은 여전히 미착수 — §1~§5·§7 위주 addendum들이 뒤이어 나오면서 우선순위가 밀렸다. 필요하면 사용자가 순서 지시.

### 브라우저 확인 (사용자가 직접)
```
cd C:\policy-watch\site
python -m http.server 8791
# 이후 브라우저에서 http://localhost:8791 열기
```

### Phase 6 — GitHub Actions + Pages
- `.github/workflows/crawl.yml`도 확인 결과 아직 Phase 0 placeholder 그대로다(`workflow_dispatch`만 있고 `echo` 한 줄이 전부). SPEC.md §1 설계대로 cron(`0 22 * * *` = 07:00 KST) + `python -m sources.main` 실행 → `site/data.json` 커밋·푸시 + 시크릿(`LAW_API_OC`/`PROXY_BASE`/`NAVER_CLIENT_ID`/`NAVER_CLIENT_SECRET`) 연결까지 전부 새로 작성해야 한다.
- **PROXY_BASE 실전 미검증**: `sources/_http.py`의 `get_govt()`가 프록시 경유 로직은 갖고 있지만, 로컬(한국 IP)에서는 프록시 없이도 다 되기 때문에 실제 프록시 경유 자체는 한 번도 검증 못 했다. GitHub Actions에서 처음 돌릴 때 `law.go.kr` 등이 차단되는지, 차단된다면 `PROXY_BASE`가 실제로 우회해주는지 확인 필요.
- **fss.or.kr 전용 UA도 Actions IP에서 미검증**. 로컬에선 브라우저형 UA로 차단을 피했는데(SOURCE_PROBE.md 참고), 이게 UA 문자열만 보는 필터인지 IP 평판까지 보는 필터인지는 Actions에서 실행해봐야 안다.

## 운영 준비물 (시크릿/설정)

| 항목 | 현재 상태 | 필요 조치 |
|---|---|---|
| `LAW_API_OC` | 미설정 — 법제처 공개 테스트용 "test"로 대체 동작 중(실제 데이터는 나오지만 사용량 제한 가능성) | 실 서비스 전환 전에 정식 OC 코드 발급 |
| `NAVER_CLIENT_ID`/`NAVER_CLIENT_SECRET` | 미설정 — `naver_news.py` 전체가 매 실행 스킵됨(graceful degradation 정상 동작) | 발급 후 GitHub Secrets에 등록 |
| `PROXY_BASE` | 미설정, 로직만 구현 | Cloudflare Worker 배포 후 URL 등록 + Actions에서 실동작 확인 |
| `data/schedules_manual.yml` | 비어있음(`[]`) | `docs/EFFECTIVE_DATE_GAPS.md` 검토해서 필요한 항목 수동 추가(아래 참고) |
| `data/summary_cache.json` | 비어있음(`{}`) — ADDENDUM-8 §4 재설계로 **API 키 불필요**(Claude Code가 직접 생성) | 사용자가 "요약 생성해줘"라고 시키면 `python -m sources.summary_candidates`로 대상 뽑아서 채움 |
| ~~`ANTHROPIC_API_KEY`~~ | **불필요** — §4 원안(유료 API)을 사용자 지시로 재설계해 폐기 | 없음 |

## 알려진 이슈 / 기술 부채 (심각도순은 아님)

1. **`google_news.py`에 title 레벨 재검증 게이트가 없다.** `naver_news.py`는 `match_loose(title, cat_key)`로 제목에 카테고리 키워드가 실제로 있는지 한 번 더 거르는데, `google_news.py`는 구글이 매칭시킨 결과를 그대로 믿는다. 실행 중 실제로 노이즈 사례 발견됨: 내부회계(icfr) 카테고리에 "클린코어(ZONE), 도지코인 금고 비웠다..." 기사가 `matched_keywords=[]`인 채로 섞여 들어왔다. `naver_news.py`와 같은 게이트를 추가할지 사용자 확인 후 진행.
2. **KASB/NTS 첨부파일 다운로드 URL 미해결.** 전부 `javascript:fileDownload(...)`/`javascript:htmlDocTransView(...)` 형태라 목록 HTML만으로 실제 파일 URL을 못 만든다(FSC/FSS는 평문 href라 이미 해결됨). `attachments=None`(A1/A3/C) 또는 파일명만 있고 `url=None`(D: List2006.do, 2026-08-31 추가분)으로 남아있다.
3. **C3(KSSB 기준서 목록) 전용 게시판 미특정.** 지금은 A1(KASB 소식) 게시판에서 "제N호"/KSSB 키워드로 대체 필터링 중. kasb.or.kr을 더 뒤져서 정확한 게시판을 찾으면 개선 가능.
4. **예규·유권해석/판례/조세심판원 심판례 미구현.** SPEC-ADDENDUM-3.md §5에서 MVP 제외로 확정한 항목. `data/tax_subjects.yml`의 `features.collect_rulings`/`collect_precedents`/`collect_tribunal`이 전부 `false`로 준비는 돼 있으나, 실제 `sources/official/nts_rulings.py` 등 어댑터 파일 자체가 아직 없다(ADDENDUM-3 §5-1: "파일은 만들되 flag가 false면 빈 리스트 반환"까지가 원래 지침 — 파일 생성 자체를 안 함).
5. **정책브리핑(policy_briefing.py, L2)이 실측 기준 기여도가 거의 0에 가깝다.** 국세청·금융위원회가 정책브리핑 전체 게시물 중 비중이 작아(300건 중 2건 수준, SOURCE_PROBE.md 참고) 실행할 때마다 0건이 나오는 경우가 흔하다. 국세청은 D2(nts.py)가 있어 상관없지만, 금융위원회는 fsc.py가 이미 있어 실질적으로 중복 안전망 역할만 한다 — 문제는 아니지만 참고.
6. **`data/schedules_manual.yml`이 비어있다.** `docs/EFFECTIVE_DATE_GAPS.md`(매 실행 갱신됨, 최근 6건)를 보고 관리자가 판단해서 채워 넣는 운영 프로세스가 아직 한 번도 실행 안 됨.
7. **"부분일치 오탐" 클래스 버그가 이 저장소에서 세 번 나왔다**(`is_discussion_material`의 "회의 결과"/"의결", `doc_type_of`의 "회의결과"/"의결", `is_company_event`의 "공포"·"상장"/"비상"). 전부 `_norm()`이 공백을 지우거나 두 단어가 우연히 이어 붙어 생겼다. **새 키워드를 `_config.py`에 추가할 때는 기존 키워드 목록과 부분일치 충돌이 없는지 먼저 확인하는 습관이 필요** — 특히 2글자짜리 흔한 단어(의결/공포/상장/비상 등)는 위험도가 높다.

## 참고 문서

- `docs/SOURCE_PROBE.md`: Phase 3A~3E 전체 조사·구현 기록(가장 상세함).
- `docs/EFFECTIVE_DATE_GAPS.md`: 매 `python -m sources.main` 실행마다 최신 상태로 갱신되는 "시행일 수동 검토 목록".
