# 필터 규칙 한 장 정리 (FILTER_RULES)

2026-10-29 기준 **코드에 실제로 들어 있는 규칙**만 적었다(NEXT.md·SPEC 원안이 아니라 동작 기준).
키워드 목록 원본은 전부 `sources/_config.py`, 판정 함수는 대부분 `sources/_utils.py`에 있다.

**적용 표기**
- **둘 다**: `site/data.json`에 들어가기 전에 빠진다 → 메일·화면 어디에도 안 나온다.
- **메일**: `sources/notify_mail.py`에서만 빠진다(화면엔 나온다).
- **화면**: `site/app.js`에서만 빠진다(data.json엔 있다).
- **로그 코드**: `docs/EXCLUDED_LOG.md`의 사유. `collect:…` = 수집 단계(§1), `excluded:…` = 정제 파이프라인(§2).
  2026-10-29부터 §1·§2의 제외는 **전부** 로그에 남는다.

---

## 0. 빨리 찾기

**"이거 왜 안 나와?"**
1. `docs/EXCLUDED_LOG.md`에서 제목 검색 → 있으면 사유 코드로 아래 §1·§2 표를 본다.
2. 로그에 없으면 필터에 걸린 게 아니다. 다음 중 하나다.
   - data.json에 있는데 화면에 없음 → `hidden_reason`(§3)과 화면 조건(§5).
   - 화면엔 있는데 메일에 없음 → §4.
   - 그 소스가 오늘 실패해 전일 캐시를 썼음(Actions 로그 `수집 실패 … 전일 캐시`, 메일 하단 ⚠) — 그 소스의 오늘 제외 기록은 없다.
   - 애초에 수집 대상이 아님: 검색어에 안 걸린 뉴스, KASB 주요일정 −90~+90일 밖, 수집 페이지 수 밖.

**"이거 왜 나와?"** (걸러질 줄 알았는데 나오는 경우)
- 공식(L1/L2) 항목은 §2의 L3 전용 필터를 **전부 면제**받는다. 면제 안 되는 건 적용 대상·비대상 세목·기준 제정 절차 3개뿐이다.
- 키워드 필터마다 **예외(오버라이드) 단어**가 있다 — 표의 "예외" 칸을 본다.
- 소스 수집이 실패하면 **전일 캐시**(`data/source_cache.json`)가 그대로 들어간다(`main._use_fallback`). 오늘 없어진 글이 하루 더 보일 수 있다.
- 논의자료(`doc_type="논의자료"`)는 숨김 사유가 **아니다** — 메일·화면 모두 나온다(§3).

---

## 1. 수집 단계 (어댑터) — 둘 다

어댑터가 항목을 만들기 전에 버린다. 로그의 출처 칸은 기관명(정책브리핑은 `정책브리핑(부서)`), 카테고리 칸은 정해지기 전이면 비어 있다.

### 1-1. 뉴스(구글·네이버) 공통

| 규칙 · 로그 코드 | 거르는 것 | 도입 · 이유 |
|---|---|---|
| 검색어 / 카테고리 확정 `collect:no_category` (네이버만) | 카테고리 필수 키워드가 없는 기사. icfr·kifrs는 `required_weak` 단어가 `weak_context`와 함께 있어야 인정. 구글은 검색어(필수 AND 조합, `-NOISE_KEYWORDS`, `when:90d`) 단계에서 걸러져 결과에 안 옴 → 로그 없음. 네이버는 수집 후 `match_loose` | SPEC 원안 · ADDENDUM-5 §4(8/31): "내부 통제"로 이란 군부 기사가 icfr에 잡힘. ADDENDUM-6 §2(8/31): "금융위원회" 키워드가 금융업 규제를 끌어와서 제거 |
| 수집 기간 `collect:out_of_window` (네이버만) | 발행일이 90일(`COLLECT_WINDOW_DAYS`) 넘은 기사 | SPEC 원안 |
| 투자·시황 노이즈 `collect:noise_keyword` | 제목에 `NOISE_KEYWORDS`(테마주·주가·급등·특징주·비트코인 …). tier 1 매체는 면제 | SPEC 원안 · 주식 기사 제거 |
| 행사·운영 공지 `collect:event_announcement` | `ADMIN_NOISE_KEYWORDS`(인사·위촉·조직개편·점검·수상·MOU·Forum·세미나·개최 안내 …), 또는 "제N회/제N차"인데 개정·제정·공표·의결·확정이 없는 제목. **tier 무관** | ADDENDUM-4 §1(8/31) 인사·운영 공지 · ADDENDUM-6 §3 기관 홍보 · ADDENDUM-7 §4 "제149회 KAI Forum" 미탐 · "위촉" 9/1 |
| 사건·사고 `collect:incident` | `INCIDENT_KEYWORDS`(검찰·수사·구속·기소·혐의·고발 …)가 있고 개정·시행령·예규·지침이 **없는** 기사. tier 1 면제 | ADDENDUM §5(8/26) · 탈세 사건 기사 제거, 예규 변경 기사는 살림 |
| 세목 화이트리스트 `collect:tax_subject` | tax 카테고리 기사 중 `data/tax_subjects.yml` 활성 세목(법인세·부가세·원천세·국조·조특·지방세) 키워드가 없는 것. 세무조사는 사전통지·대상 선정 등과 조합일 때만 인정 | ADDENDUM-3 §3·§5-2(8/26) · 종부세·상속세 등 비대상 세목 차단 |

### 1-2. 공식 소스별

모든 공식 어댑터가 위 **행사·운영 공지**(`collect:event_announcement`)를 먼저 건다.

| 소스 | 거르는 것 · 로그 코드 | 도입 · 이유 |
|---|---|---|
| 공통 | `data/source_toggles.yml`에서 꺼진 소스는 수집 시도 자체를 안 함(항목 단위 로그 없음) | 9/9 · 실패 경고 반복 방지 (현재 전부 켜짐, 10/1) |
| KASB 소식(A1) | 게시판 분류 "공지사항" 전부 `collect:out_of_scope`(제목 앞에 `[공지사항]`). 분류가 회계기준소식·지속가능성기준소식이 아니면 `classify`로 kifrs/esg일 때만 `collect:no_category` | 8/26 · 본인인증 점검 같은 운영 공지 |
| KASB 주요일정(C) | 중분류가 회계기준위원회·지속가능성기준위원회가 아닌 행사 `collect:out_of_scope`(제목 앞에 `[중분류]`), 제목에 "일반기업회계기준" `collect:non_kifrs`. 진행일 −90~+90일 밖은 서버에 요청 자체를 안 함. 남은 건 `is_meeting_schedule=True`(§3) | 8/31 · 위원회 회의만, 당사는 K-IFRS 대상 |
| KASB 제개정현황(D) | "적용기준" 열이 정확히 "한국채택국제회계기준"이 아닌 행 `collect:non_kifrs`(제목 앞에 `[적용기준]`) | 8/31 · 일반기업회계기준 제외 |
| KASB 질의회신 | 날짜 없는 상단 고정 행 `collect:non_kifrs` | 8/26 · 고정 행 = 일반기업회계기준 비교표 |
| FSS B3(k-icfr.org) | 제목에 모범규준·설계·평가가 없는 링크 — **로그 안 남김**(페이지 메뉴·바로가기 링크를 거르는 선택자라 문서가 아님). 남은 건 전부 `is_static=True`(§3) | ADDENDUM-4 §2(8/31) · 상시 비치 자료 |
| 재정경제부·금융위·정책브리핑 | `classify`가 None인 보도자료(부동산 PF·보험 감독 등) `collect:no_category`. tax로 분류되면 세목 화이트리스트 `collect:tax_subject`. 금융위는 제목에서 "금융위원회"를 지우고 분류. 정책브리핑은 부서가 국세청·금융위원회가 아니면 `collect:out_of_scope`(하루 200건 중 대부분) | 8/26~ · 기관 보도자료 대부분이 무관. 금융위 이름 자체가 kifrs 신호로 오분류되던 문제 |
| 재정경제부 묶음 예외 | "「소득세법 시행령」 등 4개 시행령"처럼 묶은 보도자료는 세목 키워드가 없어도 첨부 본문 법령명이 활성 세목 법령과 **정확히** 맞으면 통과. 안 맞으면 `collect:tax_subject` | 10/1 · 묶음 보도자료 누락 |
| 국세청 개정세법 해설 | "YYYY년 …" 제목은 목록에 있는 연도 중 최근 2개 연도치만 `collect:old_year` | 9/9 · 캐시 비었을 때 2017년치까지 "신규" 메일 |
| 법제처(law_api) | 법령명이 `tax_subjects.yml`의 `laws:`와 정확히 일치하는 것만 `collect:law_name_mismatch`(제목 뒤에 검색어) | 8/26 · "지방세법" 검색에 "지방교부세법"이 딸려옴 |
| 입법예고(lawmaking) | 법령명 정확 일치 `collect:law_name_mismatch` + 예고 시작일 90일 이내 `collect:out_of_window`(제목 뒤에 시작일) | 10/1 · 관세법·개소세법 배제 |

---

## 2. 정제 파이프라인 — 둘 다

`main.build_data_json()`이 **이 순서대로** 적용한다. 이 함수에 들어온 항목은 최종 data.json 아니면 로그, 둘 중 하나에 반드시 있다.
"대상"이 L3이면 공식(L1/L2)과 tier 1 뉴스는 면제(`_l3_gate_exempt`).

| # | 규칙 · 로그 코드 | 대상 | 거르는 것 (예외) | 도입 · 이유 |
|---|---|---|---|---|
| 1 | 적용 대상 게이트 `excluded:financial` · `public` · `nonprofit` · `smb_only` · `industry_specific` · `religious` · `foreign` | **전 계층** | 제목에 `APPLICABILITY.excluded_entities` 단어: 금융업(은행법·대부업·저축은행·**감독규정** …), 공공기관(공기업·경영평가), 비영리, 중소기업(일반기업회계기준·간이과세), 업종 특화(공동주택·농협·학교회계·**제1117호·제1104호·제2115호**), 종교(교회·한교총·종교인 과세). 해외 관할(EFRAG·CSRD·FASB·US GAAP …)은 국내 도입·KSSB·금융위·K-IFRS 반영 등 맥락이 없을 때. (제1104호는 제목에 "이자율지표"가 있으면 통과.) **제목만 본다** | ADDENDUM-6 §1(8/31) "주제가 맞아도 우리가 적용 대상이 아니면 제외" · 업종 특화 ADDENDUM-7 §2(8/31) · 보험·건설 기준서 9/1 · 종교 9/10 · "지방재정"은 8/31 오제외로 뺌 |
| 2 | 비대상 세목 `excluded:non_target_tax_subject` | 전 계층, tax만 | 상증법·상속세·증여세 등이 제목에 있으면 활성 세목 단어가 같이 있어도 제외 | 9/10 · "한교총, 상증법 및 법인세법 시행령…" 이 화이트리스트를 통과 |
| 3 | 기준 제정 절차·조직 `excluded:standard_setter_governance` | 전 계층 | Due Process Handbook·Agenda Consultation·IFRS 재단 정관, 또는 (IFRS 재단/IASB/ISSB) + (정관·Trustee·의제 협의·Monitoring Board …) | 10/1 · "IFRS 재단 정관 개정 공개초안 검토의견 조회"는 회계팀이 볼 내용이 아님 |
| 4 | 언론 1년 상한 `excluded:news_too_old` | L3 (tier 1 포함) | 발행일이 365일 넘은 기사. 날짜 없으면 남김 | 10/14 · 2011·2019년 기사가 상한 빈자리를 채움 |
| 5 | 블로그·커뮤니티 `excluded:blog_community` | L3 (tier 1 포함) | 출처 도메인이 `BLOG_COMMUNITY_DOMAINS`(brunch.co.kr·blog.naver.com·cafe.naver.com·tistory.com·velog.io·medium.com·커뮤니티 …, 서브도메인 포함) | 10/29 · "강냉이콘의 산업별 재무제표 해석법 - 브런치" — 언론이 아니라 개인 글 |
| 6 | 정확 일치 중복 `excluded:duplicate_exact` | 전 계층 | id(URL) 또는 공백 제거한 제목이 같은 묶음에서 `final_score` 최고 1건만 남김 | SPEC 원안 · 로그는 10/8부터 |
| 7 | 같은 문서 변형본 `excluded:doc_variant_merged` | 공식만 | Clean ver.·전문·요약본 수식어와 날짜 괄호를 뗀 문서명 + 개정일이 같으면 1건(수식어 없는 원본 우선). 비고에 남긴 쪽 제목 | 10/14 · 같은 지침이 2~3번 나옴 |
| 8 | 유사 기사 병합 `excluded:similar_news_merged` | L3 (같은 카테고리) | (a) 어절 유사도 ≥0.55, (b) 같은 "주체, …" + 3일 이내 + ≥0.35(기초지자체 주체는 0.20), (c) 주체 없는 제목끼리 3일 이내 + 핵심어 2개 이상 겹침. 대표는 신뢰도 우선, 단 #9를 통과하는 기사가 있으면 그걸 대표로. 남은 대표에 "외 N건 보도", 비고에 대표 제목 | ADDENDUM-4 §3 · ADDENDUM-5 §5(8/31) · 지자체 9/2 · (c) 9/14 대법원 판결 3건 · 대표 선정 10/8: 대표가 #9에서 떨어져 묶음째 54건 사라짐 |
| 9 | 규제성 게이트 `excluded:no_regulatory_signal` | L3 | 제목에 `REGULATORY_SIGNALS`(개정·시행·입법예고·의결·도입·강화·완화·발표·안내·집행기준 …)가 하나도 없는 기사 | ADDENDUM-5 §1(8/31) · "제도가 바뀌었다"는 기사만 |
| 10 | 개별 기업 소식 `excluded:company_event` | L3 | `COMPANY_EVENTS`(IPO·유상증자·합병·영업이익·워크아웃·징계·적발·과징금 …), "상장 ~"(상장사 제외), "비상", 통계 기사(퍼센트 + 실태조사 등, 또는 "감사의견 적정 97%"). 예외: 제조업 회계 문맥(재고자산·감가상각·수익인식 …), `COMPANY_EVENT_STRONG_SIGNALS`(개정·제정·K-IFRS·시행령 …). 단 감사의견 통계는 예외 없이 제외 | ADDENDUM-7 §1(8/31) · 통계·제재 결과 9/1 · 로그는 10/29부터 |
| 11 | 기업 주체 자사 활동 `excluded:company_self_activity` | L3 | "주체, …" 제목(**쉼표 필수**)의 주체가 공적 주체(…위원회·…청·의원·장관·~위 약칭·정당·지자체), 업계 전체(업계·금융권 …), 국민연금·지배구조 단체, 법령·기준명이 **아니면** 기업으로 보고 제외. 예외는 제조업 회계 문맥뿐(강한 제도 신호 예외 없음) | 10/14 · "한난, 경영진 내부회계 교육 시행"(7개 매체), 벤더 홍보가 "개정"으로 통과 |
| 12 | 자기 조직 내부 활동 `excluded:internal_activity` | L3 | 제목에 내부 인원(`INTERNAL_AUDIENCE_KEYWORDS`: 직원·임직원·공무원·임원진·경영진·실무자·담당자)과 교육·연수(`INTERNAL_TRAINING_KEYWORDS`: 교육·연수·워크숍·특강·역량강화·아카데미)가 **같이** 있으면 주체(공적 기관·기업)와 무관하게 제외. 예외: 의무화·개정안·입법예고·시행령·발의·법안 | 10/29 · "장수군 회계교육에 직원 100여 명 참여…예산 집행 기준·감사 사례 학습" — 쉼표가 없어 #11이 안 걸렸고 "집행 기준"으로 #9를 통과 |
| 13 | 논평성 기사 `excluded:opinion_piece` | L3 | 제목 맨 앞 대괄호가 [시선]·[칼럼]·[기고]·[사설] | 9/15 · "[시선] …빗썸, K-IFRS 전환"이 #10을 통과 |
| 14 | 지자체 건의 `excluded:local_gov_petition` | L3 | 주체가 OO구/시/군이고 건의·촉구·요구·요청·요망 | 9/2 · 건의 단계는 확정 규제가 아님 |
| 15 | 해외 전용 뉴스 `excluded:foreign_news` | L3 | (가) 도메인이 `FOREIGN_NEWS_DOMAINS`(tradingview.com·idnfinancials.com·tradingkey.com·vietnam.vn·unite.ai·coindesk.com, 서브도메인·경로 포함), (나) 국가 도메인(.vn·.id·.jp·.cn …, `.kr`과 일반 용도로 쓰이는 .ai·.io·.co·.me·.tv 등 `GENERIC_USE_CCTLDS` 제외), (다) 제목에 美·미국·EU·FASB·SEC가 있고 국내 도입 맥락이 없음(IASB/ISSB는 대상 아님 → §3 해외기준) | 9/2 · "서클 CEO 美 디지털자산 회계기준 개정" · 10/29 "https://…/경로" 꼴 도메인도 잡히게 수정 · 10/29 "…IDX 종합 지수를 지지합니다 - IDNFinancials"(인도네시아 증시) — 해외 매체 한국어 번역판, 8/26~ 뉴스 1,381건 중 같은 유형 10건 |
| 16 | 홍보성 보도 `excluded:corporate_pr` | L3 | `CORPORATE_PR_KEYWORDS`(출범·맞손·협약·수상·선정·구축·추진·지속가능경영보고서 발간·창사 첫 …). 예외: 개정·제정·공포·입법예고·기준서·모범규준·예규·의무화 등 | ADDENDUM-5 §3(8/31) · ESG 보고서 발간 문구 9/2 |
| 17 | 카테고리 상한 `excluded:category_cap_tier4` · `excluded:category_cap` | L3 | 카테고리당 종합 경제지(tier 4)는 `final_score` 상위 5건(`_tier4`), 그다음 전체 뉴스 15건(`category_cap`). 공식은 무제한 | ADDENDUM §1(8/26) · 뉴스가 공식을 덮음 · 로그는 10/29부터 |
| 18 | 관련 보도 흡수 `excluded:related_news_attached` | L3 | 같은 카테고리 공식 항목과 7일 이내 + 유사도 ≥0.30 또는 핵심 명사구 포함이면 공식 카드의 "관련 보도"(최대 3건)로 들어가고 피드에서는 빠짐. 비고에 붙은 공식 항목 제목 — **화면에서 그 공식 카드를 펼치면 보인다** | ADDENDUM-4 §4(8/31) · 같은 소식 중복 노출 · 로그는 10/29부터 |

---

## 3. 표시 분류 — 지우지 않고 표시만 한다

data.json에는 남는다(그래서 EXCLUDED_LOG에 없다). 메일·화면이 이 값을 보고 따로 거른다(§4, §5).

| 값 | 붙는 조건 | 메일 | 화면 | 도입 · 이유 |
|---|---|---|---|---|
| `is_static` → `hidden_reason="static"` | (가) FSS B3 수집분은 항상. (나) 공식 + icfr + doc_type이 모범규준·적용지침·FAQ이거나 제목에 "가이드라인": 게시일이 30일 이내가 아니면(날짜 추정 포함) static, 이내면 static 해제 (`mark_standing_documents`) | 제외 | 최근 정책동향 제외. 전체 동향은 기간을 90일 넘게 잡을 때만 나오고 맨 아래 정렬 | ADDENDUM-4 §2(8/31) · 10/14: 옛 기준 문서 6건이 수집 복귀하며 재발송 |
| `doc_type="해외기준"` → `hidden_reason="foreign"` | 제목에 IASB/ISSB가 있고 국내 도입 맥락(회계기준위원회·지속가능성기준위원회·KSSB·국내 도입 …)이 없음 | 제외 | 최근 정책동향 제외. 전체 동향은 문서 종류에서 "해외기준"을 직접 고를 때만 | ADDENDUM-7 §3 안 A(8/31) · K-IFRS 원천이라 수집은 유지 · 메일 제외 10/20 |
| `is_meeting_schedule` → `hidden_reason="meeting"` | KASB 주요일정(C)에서 온 위원회 회의 항목 | 제외 | 제외(최근 정책동향·전체 동향·캘린더 모두, 다시 보는 방법 없음) | 메일 10/20 · 화면 10/29 · 의결 자료가 나오면 그게 소식 |
| `doc_type="논의자료"` | 제목에 TF·태스크포스·논의 내용·회의 결과·진행 경과·워킹그룹 등이 있고 의결·공표·제정·개정·확정이 없음 | **나옴** | **나옴** | 8/28 분류 도입 · 10/20 숨김 해제("메일·화면 둘 다 보인다") |

우선순위는 static → foreign → meeting(`_utils.feed_hidden_reason`). 메일과 화면이 같은 함수 결과(`hidden_reason`)를 쓴다(10/20 통일).

---

## 4. 메일 전용 (`sources/notify_mail.py`)

| 규칙 | 거르는 것 | 도입 · 이유 |
|---|---|---|
| 신규 판정 | 직전 data.json(`PREV_DATA_JSON`)에 같은 id가 있던 항목 | 9/2 · 신규만 알림 |
| 발송 이력 | `data/sent_log.json`에 있는 id(90일 보관) | 9/10 · 구글 RSS에서 빠졌다 돌아온 기사 재발송 |
| 숨김 사유 | `hidden_reason`이 static·foreign·meeting인 항목 | static 10/14 · foreign·meeting 10/20 |
| 언론 발행일 | L3 중 발행일이 오늘·어제(KST)가 아닌 기사. 공식은 면제, 날짜 파싱 실패는 포함 | 9/10 · 구글이 옛 기사를 뒤늦게 줌 |
| 발송 조건 | 위를 거친 뒤 0건이면 메일을 안 보냄(`FORCE_MAIL=true` 제외) | 9/2 |

EXCLUDED_LOG가 아니라 Actions 출력에만 남는다(`[notify_mail] … N건 메일에서 제외`).

---

## 5. 화면 전용 (`site/app.js`)

| 화면 | 거르는 것 | 도입 · 이유 |
|---|---|---|
| 최근 정책동향 (`renderTodayView`) | `hidden_reason`이 있는 항목 전부(static·foreign·meeting). 날짜는 **공식은 max(발행일, 처음 수집일)**, 언론은 발행일(`recentDateOf`). 기간은 1→3→7→14→30일로 늘리며 **5건 이상 + 공식 1건 이상**이 되면 멈춤(30일에서 무조건 멈춤). 공식·보도 각 12건까지 보이고 나머지는 "전체 동향에서 더 보기". 공식은 그 날짜 내림차순 → tier → 점수, 보도는 그 날짜 내림차순 → 점수 순. 검색어는 기간을 정한 뒤 그 안에서만 적용 | 9/1 이름·점진 확대 · 10/20 공식 1건 조건(보도만 5건으로 공식을 놓침) · 10/29 meeting 제외 · 10/29 처음 수집일: 메일로 간 공식 36건 중 28건이 그날 화면에 없었음 |
| 전체 동향 (`filterItems`) | 카테고리·문서 종류·기간(기본 최근 30일)·검색어. meeting은 항상 제외, foreign은 "해외기준"을 직접 골라야, static은 기간 90일 초과일 때만. static은 정렬에서 항상 아래 | ADDENDUM-4 §2-4 · 8/28 · 10/20 hidden_reason 통일 · 10/29 meeting 제외 |
| 캘린더 (`schedules.build_schedules`) | `effective_date` 있는 항목 + `data/schedules_manual.yml`. **위원회 회의 예정(`is_meeting_schedule`)은 제외** | 9/14 · 회의 일정이 실제 시행일과 섞임 |

**처음 수집일**(`first_seen_at`, `data/first_seen.json`, `sources/_first_seen.py`): 최종 data.json에 처음 들어간 날. 공식 카드는 발행일보다 늦게 처음 수집됐으면 날짜 옆에 "· 수집 M/D"를 붙인다(최근 정책동향·전체 동향 둘 다). 전체 동향의 기간 필터는 발행일 그대로다. 메일 신규 판정은 이 값을 쓰지 않는다(직전 data.json + `sent_log`).

**메일과 일부러 다르게 둔 것**(10/29 검토): 언론은 메일이 어제·오늘 발행분만 보내고 화면은 기간 안 발행분을 보여준다(화면에만 있는 방향뿐, 7주간 44건). 화면의 12건 상한은 숨김이 아니라 "더 보기"로 넘긴다.

`hidden_reason` 필드가 없는 옛 data.json이면 화면은 `is_static`·`doc_type="해외기준"`·`is_meeting_schedule`로 대신 판정한다.

---

## 6. 손볼 곳

- 키워드 추가·삭제: `sources/_config.py` (상수 이름은 표에 적은 그대로).
- 세목 범위: `data/tax_subjects.yml` — 세목을 추가하면 `NON_TARGET_TAX_SUBJECTS`에서도 빼야 한다.
  입법예고·법제처는 `laws:` 정확 일치라, 목록에 없는 시행규칙(예: 지방세법 시행규칙)은 `collect:law_name_mismatch`로 빠진다.
- 소스 켜기·끄기: `data/source_toggles.yml`.
- 오제외 점검: `docs/EXCLUDED_LOG.md`(매 실행 덮어씀). 정제 단계(`excluded:`)가 위, 수집 단계(`collect:`)가 아래다.
