# 다음에 이어서 할 일 (NEXT)

마지막 갱신: 2026-08-26, "Phase 3 완료 — 공식 소스 전환" 커밋 시점 기준.

## 지금까지 된 것

- Phase 3A~3E(SPEC-ADDENDUM.md 기준): 소스 접근성 조사, 공식 소스 어댑터(KASB/FSS/MOEF/NTS/FSC/정책브리핑/법제처) 전부 구현·실측 검증.
- Phase 4(SPEC.md 기준): `_summarize.py`/`schedules.py`/`main.py` 오케스트레이터 구현. `python -m sources.main` 실행하면 실데이터로 `site/data.json`이 생성되고 스키마 검증까지 통과한다(최근 실행: 313건 원본 → 116건, 세법 41 / 내부회계 33 / K-IFRS 26 / ESG 16, 일정 18건).
- 테스트 166개 통과(`pytest tests/`).

## 다음 순서 (SPEC.md §8 기준)

### Phase 5 — 프론트엔드 (`site/index.html`, `app.js`, `styles.css`)
확인 결과 아직 Phase 0 스캐폴딩 그대로다(`index.html` 15줄, `app.js`/`styles.css` 각 1줄) — SPEC.md §7 요구사항은 전혀 반영 안 된 상태. SPEC.md §7-5 원칙대로:
1. 더미 데이터로 UI 먼저 완성(레이아웃/필터/카드/캘린더).
2. 완성 후 `site/data.json`(이번에 실제로 생성됨)에 연결.
3. `python -m http.server`로 로컬 렌더 확인, 데스크톱/모바일 스크린샷.

**주의**: `site/data.json`의 `stage` 필드는 `"확정"`까지만 저장돼 있고 `"시행예정"`/`"시행중"` 구분은 프론트엔드가 `effective_date`로 직접 계산해야 한다(ADDENDUM-2 §2-2, `d_day`와 같은 이유 — 날짜가 지나면 틀려지므로).

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

## 알려진 이슈 / 기술 부채 (심각도순은 아님)

1. **`google_news.py`에 title 레벨 재검증 게이트가 없다.** `naver_news.py`는 `match_loose(title, cat_key)`로 제목에 카테고리 키워드가 실제로 있는지 한 번 더 거르는데, `google_news.py`는 구글이 매칭시킨 결과를 그대로 믿는다. 실행 중 실제로 노이즈 사례 발견됨: 내부회계(icfr) 카테고리에 "클린코어(ZONE), 도지코인 금고 비웠다..." 기사가 `matched_keywords=[]`인 채로 섞여 들어왔다. `naver_news.py`와 같은 게이트를 추가할지 사용자 확인 후 진행.
2. **KASB/NTS 첨부파일 다운로드 URL 미해결.** 둘 다 `javascript:fileDownload(...)`/`javascript:htmlDocTransView(...)` 형태라 목록 HTML만으로 실제 파일 URL을 못 만든다(FSC/FSS는 평문 href라 이미 해결됨). `attachments=None`으로 남아있다.
3. **C3(KSSB 기준서 목록) 전용 게시판 미특정.** 지금은 A1(KASB 소식) 게시판에서 "제N호"/KSSB 키워드로 대체 필터링 중. kasb.or.kr을 더 뒤져서 정확한 게시판을 찾으면 개선 가능.
4. **예규·유권해석/판례/조세심판원 심판례 미구현.** SPEC-ADDENDUM-3.md §5에서 MVP 제외로 확정한 항목. `data/tax_subjects.yml`의 `features.collect_rulings`/`collect_precedents`/`collect_tribunal`이 전부 `false`로 준비는 돼 있으나, 실제 `sources/official/nts_rulings.py` 등 어댑터 파일 자체가 아직 없다(ADDENDUM-3 §5-1: "파일은 만들되 flag가 false면 빈 리스트 반환"까지가 원래 지침 — 파일 생성 자체를 안 함).
5. **정책브리핑(policy_briefing.py, L2)이 실측 기준 기여도가 거의 0에 가깝다.** 국세청·금융위원회가 정책브리핑 전체 게시물 중 비중이 작아(300건 중 2건 수준, SOURCE_PROBE.md 참고) 실행할 때마다 0건이 나오는 경우가 흔하다. 국세청은 D2(nts.py)가 있어 상관없지만, 금융위원회는 fsc.py가 이미 있어 실질적으로 중복 안전망 역할만 한다 — 문제는 아니지만 참고.
6. **`data/schedules_manual.yml`이 비어있다.** `docs/EFFECTIVE_DATE_GAPS.md`(매 실행 갱신됨, 최근 6건)를 보고 관리자가 판단해서 채워 넣는 운영 프로세스가 아직 한 번도 실행 안 됨.

## 참고 문서

- `docs/SOURCE_PROBE.md`: Phase 3A~3E 전체 조사·구현 기록(가장 상세함).
- `docs/EFFECTIVE_DATE_GAPS.md`: 매 `python -m sources.main` 실행마다 최신 상태로 갱신되는 "시행일 수동 검토 목록".
