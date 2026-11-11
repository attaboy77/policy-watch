# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-11 10:39:27 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1660건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 13 |
| excluded:company_event | 2 |
| excluded:company_self_activity | 7 |
| excluded:corporate_pr | 2 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 24 |
| excluded:financial | 1 |
| excluded:industry_specific | 7 |
| excluded:local_gov_petition | 1 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 42 |
| excluded:no_regulatory_signal | 44 |
| excluded:opinion_piece | 1 |
| excluded:reader_content | 2 |
| excluded:similar_news_merged | 28 |
| excluded:smb_only | 1 |
| collect:event_announcement | 6 |
| collect:incident | 1 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 17 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 212 |
| collect:out_of_window | 34 |
| collect:tax_subject | 41 |

## excluded:category_cap (13건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 의무화 초읽기…최초 시기·스코프 3 두고 이견 여전 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFA3NTR1NFY1M3RnQ1hWT1g4bzJvNjhUSTdfcTY5ZnQ4eUZISkFoY3pQbVIzWkk4ODQ4SEFIQTJQUjh3Z21lUWhKdUFaMFctaUFmYlFiYjl5RUgzRnNwaW5weDZNYU1sT205U25rZtIBcEFVX3lxTFBpREZVZVFLSnJuUXdfZDloVkxZVHhzNGpXMS1qRU51SkNCbVpRV1dJWmdQclVzemlGQ01YSU1QOV83VGtjam5wTU94MmxzNzVjNWx6ZlNMYzJBQmNtWjFVZ0ZLOGgxRk5SOUx2T1dZMEo?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 2028년 대기업부터 시작…스코프3는 3년 유예 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB0NEtXNnFZdGJLd01zRG5XaGUtZ1RyX1hFMTB2REQ5VlVJRkZzdVFJODBNVHdqTlhBZzZtQnZtM1N2dXhtc2tma3pMaEMzX3N1cjFjOVl3RE91Sjl6Rm9zV251UDBQYUo5NWtXMNIBcEFVX3lxTE1jYVpBZ1NRcDNjb0ZpaGh3Q09TZFpINmN2b3BxbTJMaGpJeVVqQ1loMHhkRjJYZkp2ZjVkTEN4R0FWM0lrcWtsSUphSW4wUHZ0MWw3ekgwb3JZeE5hcmNfUXE0VkxUcXhWOFdsYXlZVmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | kr.investing.com | Goosehead Insurance, 실적 발표 연기·과거 재무제표 재작성 - Investing.com 한국어 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBobmJvQXg1Ukd1dGlXdjNwTGw5M3lIX1pDTlVFT2JERTVnLUU1UExJTWdQMEtmcmlyUXpRTUpoN001dlZpcjBnYTJjUkROX1VINVdUaVNJOEF1ZV9oNXV5R2psN3lwYk9VYk00c0phOVE?oc=5 |  |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 |  |

## excluded:company_self_activity (7건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tradersunion.com | 삼성전자, 국제회계기준 자문기구 합류로 IFRS 개정 대응력 확대 - Traders Union | https://news.google.com/rss/articles/CBMimwFBVV95cUxQSjl6OWFIODkxTDBkWEV3RUo2YVpwSTY5VVRCamFSekU3alRVMWtab3RwalFTWHRmdWlOclR2bWV1RnRxNzZac3c1X2p0dzdOaUFfUENudGE0c1NHU0tLd1dRNW9VVFUtbWIwY1pqeEpjR0x0ODlCVVhnbm9RSTRQbWRldU54WHd5S09UNjhLRG1GLUdBWjBoWjRaWQ?oc=5 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |
| esg | ESG경제 | 泰, ISSB 지속가능성 공시 의무화 확정…28년 SET50부터 단계적 시행 | https://www.esgeconomy.com/news/articleView.html?idxno=17232 |  |
| esg | ESG경제 | 아시아 각국, ESG 공시 의무화 '질주'...한국은 계속 '헛바퀴'만 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9iT1p3aDQ1bGItZFl4NDZ4Z3QxVGtEUS0wYnpjZ1BkTmF6MF9aakdtRVpBaGdIN3dUSms2bkxKUlBjU1VkT2NUaDRpNVdEaEExdDZjWkZEQlI0RjFQS0gwZ3IwRTVpTmNHNWJTMw?oc=5 |  |
| esg | news1.kr | 셀트리온, MSCI ESG 평가 최고등급 획득…"지속가능경영 강화" | https://www.news1.kr/bio/pharmaceutical-bio/6350171 |  |
| esg | news.einfomax.co.kr | "ESG 공시, 홍보가 아니라 책임"…2028년 의무화에 재계 '긴장' - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE5SSmtLcFNmdDRLOGhCZTJUX1JpektFVjRFcGN4dWlHVk1BMGVBQmQ4N1RfN2lrOHJrd2RRdXBjLTh3SXduMmRoRnptMkJFNFlPdF85aVFYSFRnNnc3MEFXWXZaQU1CX0dmQXFJUV81Ymk?oc=5 |  |
| icfr | datatooza.com | 퓨마 바이오테크놀로지, 새 ERP 도입 뒤 내부통제 중대한 취약점 공개…재무제표 재작성은 불필요 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE93eVFHZkV5OEtUeGRSQldLc2JJQ1FkRG01MkF5OGVOT1FaRzlDMUl6anBKcnNBNXZDOHNRSHJZOTBwS19SX3Z5MGRzcU5HblNXd08xR19OdGFpZTNmSExPYTE4NXVTay1sNHpnNWFRUnBreWc?oc=5 |  |

## excluded:corporate_pr (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | munhwa.com | 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5rS2E2d0xlNFhmLTRnWk5BWUNMTTE3V2dFdDlPYlZ5NHg5N3BRWHYyc05NTzZOM2FCRGdSbExyS0JRQ2FEWjhnay0zbHVxNVMw?oc=5 |  |
| icfr | asiae.co.kr | 중대 보안 취약점 방치 땐 CEO 책임…금융당국, 금융사 내부통제 강화 추진 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wVHBFeHhiNjhDb1pVRzYwbXFYTmRrZmhpOFNWS0laVUNkeGZ4NUdGQVY2eGJBWmdlRHJ6SFFsaEM5bW5RQ0FyazRqY0tUWmhnRHJYVjdLSUZwUjJRd2Y3TQ?oc=5 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (24건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |
| tax | 행정안전부 | 지방세법 시행령 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88292 |  |
| kifrs | datatooza.com | 퓨마 바이오테크놀로지, 새 ERP 도입 뒤 내부통제 중대한 취약점 공개…재무제표 재작성은 불필요 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE93eVFHZkV5OEtUeGRSQldLc2JJQ1FkRG01MkF5OGVOT1FaRzlDMUl6anBKcnNBNXZDOHNRSHJZOTBwS19SX3Z5MGRzcU5HblNXd08xR19OdGFpZTNmSExPYTE4NXVTay1sNHpnNWFRUnBreWc?oc=5 |  |
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| esg | ESG경제 | ISSB 자연 관련 공시 실무서 들여다 보니...S1ㆍS2 보완 | https://www.esgeconomy.com/news/articleView.html?idxno=17209 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| esg | ESG경제 | "ESG 공시 대응, 기존 지표와 의무공시 항목 통합해야" | https://www.esgeconomy.com/news/articleView.html?idxno=17084 |  |
| esg | 임팩트온 | EU 은행 ESG 공시항목 37% 축소…EBA, XBRL 전산규격 확정 | https://www.impacton.net/news/articleView.html?idxno=30289 |  |
| esg | seoulfn.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.seoulfn.com/news/articleView.html?idxno=640152 |  |
| esg | econovill.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.econovill.com/news/articleView.html?idxno=753696 |  |
| esg | 임팩트온 | ISSB, 22일 자연공시 초안 공개…사업장 위치·가치사슬까지 평가 | https://www.impacton.net/news/articleView.html?idxno=30168 |  |
| esg | ESG경제 | EU 역외 지속가능성 공시대상 국내기업 "20~30곳"...KSSB 공시 정보 활용... | https://www.esgeconomy.com/news/articleView.html?idxno=16805 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 권미엽 삼일회계 전무 “ESG공시의 복병 ‘보고서 일정‧... | https://www.tfmedia.co.kr/news/article.html?no=207256 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 백태영 전 ISSB 위원 “ISSB 전면 도입은 기준 통제권 포기... | https://www.tfmedia.co.kr/news/article.html?no=207254 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |
| esg | 임팩트온 | ESG 공시 규제 후퇴 vs. 월가는 기후데이터기업 인수 경쟁 | https://www.impacton.net/news/articleView.html?idxno=30224 |  |

## excluded:financial (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |

## excluded:industry_specific (7건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 2025년 제1117호 보험계약 | https://kasb.or.kr/front/board/comm020View.do?boardMngNo=&boardNo=&cmtreadSeq=&seq=494&siteCd=002000000000000 |  |
| kifrs | 한국회계기준원 | 2022년 제1117호 '보험계약'과 제1109호 '금융상품'의 최초 적용 - 비교정보 (제1117호 보험계약) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=316&searchfield=ALL&searchword=%EA%B3%B5%ED%91%9C&s_date_start=2022-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2021년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=300&searchfield=ALL&searchword=1117&s_date_start=&s_date_end= |  |
| kifrs | 한국회계기준원 | 2018년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=231&searchfield=ALL&searchword=1117&s_date_start=2018-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2017년 제1104호 ‘보험계약’과 제1109호 '금융상품'의 동시 적용 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=220&searchfield=ALL&searchword=&s_date_start=2017-12-01&s_date_end=2017-12-31 |  |
| kifrs | 한국회계기준원 | 2015년 건설계약 공시 (제1011호 건설계약, 제1037호 충당부채, 우발부채, 우발자산, 제1115호 고객과의 계약에서 생기는 수익, 제2115호 부동산건설약정) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=166&searchfield=ALL&searchword=1115&s_date_start=2015-01-01&s_date_end= |  |
| kifrs | hapt.co.kr | '공동주택 회계 감리' 법안에 "옥상옥(屋上屋) 규제" 지적 | https://www.hapt.co.kr/news/articleView.html?idxno=169530 |  |

## excluded:local_gov_petition (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | gukjenews.com | 송파구, 신축주택 재산세 급증 막는다…지방세법 시행령 개정 건의 - 국제뉴스 | https://news.google.com/rss/articles/CBMibkFVX3lxTE4ybVZqakNwakU3WmxHRkxTdW02Q2Y3RnVmalItcFpLY19pQUw4bzBpU3FMVTRRSUtRNVdjTkxXMk1sSnN4VmhaRkNlQmhOeUxBc2JnSVNBeEdpci05TWZYbFhETUZoMWFjRkk0YWln?oc=5 |  |

## excluded:manual_id (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |

## excluded:news_too_old (42건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | investchosun.com | 삼성생명 몰아붙인 회계기준원…2분기 결산 고민 깊어졌다 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPZWdwcnZLaWNBaTl1c3BFRlZyaG9NR0M5eFZRQzBYb0JBeVRIeWQzODI4VUJQbWlKNWdtX2hlWW56WUd0TEwxWjM2ZnlNWHZIYTFSUHNrUmFidUhOVUhDWU5OTVN6c2tCZ09IZVBZYXdzSEZBaTByVGFRTG9tQ1k3MmxtSQ?oc=5 |  |
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | 조세일보 | 김현정 "尹 정부, 3년간 신외감법 무력화" - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JdDQ0dDRwdlpDdGhzcnpHZ3hhZ3V3OXFqbXplRXJ5SlFFeU5VWXhlZHg1clRpNHVfQ3B6YXB2RDZBR21GSWlzVnJ4RnY3NDRpaURGVVBBTW5UWWtzQnd3?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9zaTlJci1iWW1GZ2c3TFFYUUxvS3JWTnZJNXZmQm1rdUhGSzMzUTJvM2hwNlBDdGhKdmJ5WU5ZRnR1MDJIYkl6bTlfZFEtMXE3Q1E?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | fntimes.com | 금감원, 신외감법·K-IFRS 제·개정 내용 설명회 개최 - 금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE51eTFBa0dYOXQ5UEt2bmF4SFUtZ0cwS0l0NjZRSUZTYlQ5d01iOGNPNHBQTTBvQTA5N2lycVJYc0s3NW16T091M2xmRjVydmRJekFheUU1TXhvZU94MXNaZVBvQUVMLWtMUXdvWkcwalR4NTZIbUpnV1JSZnA?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | 한국경제 | [한경 CFO Insight] 신외감법 2년...감사비용 70% 폭등 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCc1VNZVE2U181NVZDQzlZYnpVM2E1MEtxdXRDS00tUGVlN0ZSTFVzNTRhWFQxc1NKUFFtYjVKWEFDUmZkZVItN21jdkJvSFphVUVVY19QNVVlUQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | lawtimes.co.kr | 구 외감법 상 ‘회계처리기준’이 구성요건이 될 수 있는지 여부 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9mQkQ0MVloUTljd2UzOXI3QnZfVFA2ZUJaYTlEa3NfLWNHa0ZYVUxHZ0hUMHkyeDFIWmdZV2VtaFM3TDVpYUZwR1A1R1JweFJQUWJFOTU4VFF5WnUtdmtmU0JuWnNUQ3dYc0ctbGdR0gFyQVVfeXFMTWtxblhPLWdZc3p5VU1QdmZhczA5aHVlRHZPOS1fZXBsYUFvWGNRNG9naXhhRXlOdjY5c0RPbmNLWHpQMFJWcmlab2piTXJ1VVZRNDJ3SlpYLTlydjNXX195WmNkTnYwZUNzYm15aWFOYU5B?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |

## excluded:no_regulatory_signal (44건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE43SzV1ZWNkVHBRQzZUUkJ4OW5zQWoyekgtQ2pvZ0FJTXQ4NHVLNjYwa0lPa1RqVHpMemJzRUNxLUJyeXpuT29LWGVJbFNLMWZtelJseHBfNWNoVTBuVVJtb2xoWlpEQ1oyY3c?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 서울경제 | [단독] 금감원, 제이알글로벌리츠 회계감리 착수…자산평가 논란 재점화하나 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9ncUJvZWtlNmZ2VnZHNUhpZnFoN2RrcTUwR2RBQUV0QkVpejJ5ZW5tQUVjMWRBalQ0Snp6Slpob28zeDNBazdIQ19XQmVEcDZUcFHSAVNBVV95cUxOcGpaa1J0eGxlaXl5TXB3aS1hMFlqVllzM3F5ZkhKem1JbE1WX2JyU3ZZRi10UUFnV3hzTXJmLWVWajVJODB5WlBxYThTS3BCSDlLOA?oc=5 |  |
| kifrs | 파이낸셜뉴스 | IFRS18부터 PRS까지… 재무제표 바꿀 변수 쏟아진다 - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1qMmQyTGZyUUpzOFBMOVF0Z1I4WHNUcUFZLUo5ODRlMkdOMGNqZ2pvSXJGODl1eUFYT1lDanRka29kdkRuWEJPNGRYdWNxWHBXZlA1ZGFqMGJJZw?oc=5 |  |
| kifrs | 한국경제 | 스벅·메가 사이서 버틸 수 있나…“사라질 커피 브랜드, 숫자는 알고 있다” [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9qRldRTGs4OGVtMnRWRnNrdWE2TGxBQmh3eXZGQ2I0SDAtMzFoM1Z0dHMwb0wtb1lnRi1TRlU0aFd5alYzeUZIanpBdEkyS0Z1ellKcmZma3ZfZXdZc2dpU2dua0paZ0NLRHNRVQ?oc=5 |  |
| kifrs | ittimes.com | "돈에는 회계기준, 사람에는?"…플렉스, 조직·인사 연구 조직 '한국인사기준원' 출범 - IT타임스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5TclZ0QndtNmZuUzFwUkdQOHhRbDNsbzBJRHcwRGphWTNkYVRISVpzNTdCTmEyVVVUMGxuQl9YWFhBYV82SFZGNUhyRWRsaEpDNVN4WlJudVQwUExYZjZmSEtKSlhiclV3?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 흑자 전환 컬리...그래도 여전히 '미생(未生)' - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1CZHpNRmxVcHB3N3hSazFQYkNJelpma2U0UzVNSjBkcThaNmUxcWlfZGVRWS1STGZzcF9vVVZRb1hfdWdhMEJWRWw4M1RwWjdQM1FGa2tEOXhZdDlaMnZCU0hrV3M0LWd0a0xNcw?oc=5 |  |
| kifrs | datatooza.com | 혼벡 오프쇼어, 헬릭스 합병 역취득 회계처리…예비 취득대가 15억 7559만 달러 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE84OEhsdTFaX0JUdEwtQmxsSWJaVHdZQ1UtSGpHMUlZVEcwSlAyLTMzNGNDVlFySFBiSmpkTlcwS2wtcVdKVGFtMXljSndXaUxkV0hQSTU0VU5mTHdhQ09Xc1ZYd1VQcGJtcWlWU2JnSXExaHc?oc=5 |  |
| kifrs | coinreaders.com | 클라우드플레어, 3분기 매출 39% 증가…회계기준 영업손실도 확대 - 코인리더스 | https://news.google.com/rss/articles/CBMiSkFVX3lxTFB6c2ZJc2dwaWxaZVA1Yml2WXA3X28ybVZodEx0VENFNkF5ajF5SkRiQ3VOWnktek5VXzdyQVV6b0RlM0c4dmlYMElB?oc=5 |  |
| kifrs | kr.investing.com | 넥스테라, Dominion Energy 합병 관련 재무제표 제출 - Investing.com 한국어 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9RYXh5YjI0WE1aLVJGVEtYMlNmdkpoOTNhU3A4aE5GTzNHaE5qMG1KNzZ6Q0VadHhfWXZPaHBmU2s1RU9QaGpkMFlwc1Via0xGVHFTVlJaRzJxQmZ6ckdEYW5HVE1qaTZHQ0ZHTmtLNA?oc=5 |  |
| kifrs | datatooza.com | 폭스, 로쿠 인수에 따른 프로포마 재무정보 및 통합 위험 요인 공시 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE13UnFPUjdiMGVMaUVhYS1KQ2twTHZUaWVOSmhKLTdpNXVKYnZ4bndqOWJDVHN5RXc0em4wX19vcWxFRTdYaENqdFRDeDZVOVFHZ0tfRlFNRXNiRXM3c2Y4WHQ4NndwWGlfVUd2TlY3XzFZVU0?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 영풍에 과징금 204억…고려아연은 84억 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sVlBmQzJPbXZuSTFOai1kaDhGb1hLVkpCdktFWnZaU1YweGRJWllmVk9zbUdZQTdpUTVRaFpHM1RlQXllWkhpdVpJUFlqLVV1SEJESnZkVUcyZEnSAWBBVV95cUxQZTlEXzktdDljVUR2UENmbHJnUzFKNE04U3BxTzNETFZBTlA3alY4VGJtREYwdmVvSldHM1JlM1kyNWlsVXJFbUxCaHhaQlBlU3VHTVY2UUh0Uk1aS1U4MzM?oc=5 |  |
| kifrs | yna.co.kr | 증선위, 영풍·고려아연 감사인지정 등 조치…"회계기준 위반" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE02dVZmLXlJRkNzWEFLT0pjTFFEQzFhWFh0bERfQXlVbDM0dEpxVWMyY3p3S3ZaTV9zSFlHQzhaclVuREtOQVkxX3g2bE5JN052U1ptVlRNVnVfaTTSAWBBVV95cUxOMk5wMlV2TldLRFRLWWo2SlBnRFBqTVFxVk1nYnkzdF96d01sM3hLUVlTU3Itckp2bTQ2MVFreHA1cnBsN28yMFplTXdkS2lFYlZQb1hYSzZnVDRxNVgzQ2U?oc=5 |  |
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 | https://www.impacton.net/news/articleView.html?idxno=30527 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | sateconomy.co.kr | ESG 공시, '작성'보다 '증명'으로…기업가치 가르는 이행능력 | https://sateconomy.co.kr/news/view/1065574204012569 |  |
| esg | cc.newdaily.co.kr | 대전상공회의소, 국내 ESG 공시제도·공급망 규제 설명회 열어 | https://cc.newdaily.co.kr/site/data/html/2026/11/10/2026111000377.html |  |
| esg | etoday.co.kr | AI로 들춰낸 친환경 기업의 민낯⋯ESG 공시 44%는 ‘그린워싱 고위험’ | https://www.etoday.co.kr/news/view/2646387 |  |
| esg | hellot.net | [ESG 칼럼] ESG 공시 대상 3천 개사 시대 협력 중견·중소기업이 받게 될... | https://www.hellot.net/news/article.html?no=116128 |  |
| esg | vtimes.kr | BSI 영국표준협회, 지속가능성 공시 대응 과제 조명 세미나 개최 - 벤처타임즈 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE82eGVua2NvUTUzRnk2MjdUc3J1RTBlaGkwcEwxRWQ0d0lPRWoxX3M1UzduRlE5UWFjUkNGZVNPbGMyZmRmcjE3bTNhUVhnT0hQcjlhd0Z3N0JHdk9nakJnaFpnU1VkQQ?oc=5 |  |
| esg | newstomato.com | 보험사 ESG 공시 늘었지만…비교는 '깜깜' | http://www.newstomato.com/ReadNews.aspx?no=1318745&inflow=N |  |
| esg | worklaw.co.kr | ESG 공시, 직원 성장 이끄는 장치가 돼야 | http://www.worklaw.co.kr/view/view.asp?accessSite=Naver&accessMethod=Search&accessMenu=News&in_cate=101&in_cate2=0&gopage=1&bi_pidx=39682 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | asiatime.co.kr | [윤영민 칼럼] ESG 공시 시대, 보여주기식 경영의 종말 | https://www.asiatime.co.kr/article/20261023500342 |  |
| esg | thepowernews.co.kr | ESG 공시 291곳→1년 뒤 3171곳…대기업 넘어 협력사까지 ‘데이터 전쟁... | https://www.thepowernews.co.kr/view.php?ud=202610221509381568de3f0aa1be_7 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| icfr | seoul.co.kr | 손정화 서울시의원, 서울연구원 회계관리 부실 지적...내부통제 체계 점... | https://www.seoul.co.kr/news/publicnews/local_govern/smc_movement/2026/11/11/20261111500024?wlog_tag3=naver |  |
| icfr | news1.kr | "내부통제 경험 나누고 취약점 보완"…기보, 5개 공공기관과 맞손 - 뉴스1 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1Wc3pJS2E4NzV3cC1zV3NGTlZ5dFBxcmlJNi1id0RSRVdORXVTWDJJZHJCMy1tcldVYjlZTlR5SUJMYzdjcE91RGFweWxrNVhZX0dDS1dIWk90M0N5?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| tax | kgnews.co.kr | 경기도 지방세제 개편 6개 법안 발의…‘14조 확충’ 기대 현실화될까 | https://www.kgnews.co.kr/news/article.html?no=918123 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:reader_content (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | veritas-a.com | 안산대 세무회계학과 '재무제표 분석' 전공역량강화 직무특강 진행 - 베리타스알파 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9JaEFSeVlicDVPdFlzTl9ud2ZDSWtscUlOTXQtZDRFZWpqZW1QWjlKbDFDWHItQnUyMXNaNVZhVXNlUzFUdnljeGpGYWthMXluN3ZOSzdlRlZTdWVGd0tjc2FXbnhWTFdLUW5oZA?oc=5 | event |
| esg | ESG경제 | 'KSSB 공시 의무화 시대, 무엇을 준비해야 하나' 세미나 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE81V1p4YkEyeGp6aWFCY2lCYmcxVXNZYm5ZWEJrV21QR0NOSjZfMFN0RWgza3otTFR4ZjZzTnBoQU9sWkw5SDFkSS05bkRQUXBxY0l2LTVQaW5QbWFOR2FWcUZWVE1oSlpNR193ZQ?oc=5 | event |

## excluded:similar_news_merged (28건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 서울경제 | 국제 회계기준 개정에 韓 목소리↑…자문기구에 삼성 부사장 합류 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9XcmlVc1ZOLUNEZjhVaGFqcmkwOWVTZE94T2J2Q3VWS09QUGQxUDNxQm5qQy1rVzhlMlg1cEtHSFh0SGJPcDFqd3ZlaEVrY1dLb1HSAVNBVV95cUxPQlZLNlZfTXdsSnRvdEZGcnVfY3A5UEVaaVctdV9BMmtSV1dBMVduUnpxTWJWdV9nX1U3S1lPOU8zN05TZHZiZk5LWXJYN1pnbkp6aw?oc=5 | → 대표: 국제 회계기준 개정에 韓 목소리↑…자문기구에 삼성 부사장 합류 |
| kifrs | 파이낸셜뉴스 | 삼성전자 부사장, '글로벌 회계기준 제정'에 참여…韓 기업 목소리 커진... | https://www.fnnews.com/news/202611061034591232 | → 대표: 국제 회계기준 개정에 韓 목소리↑…자문기구에 삼성 부사장 합류 |
| kifrs | 이데일리 | 이찬진 금감원장 “20년 회계 감리주기, 3~5년으로 단축할 것” - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxOX3NLU0l0OVZ4ODJfMU5SSnBUM1NCa3VoVFNnUGw1SUNLQjJJcTJnR2pyb1pjQXpjRDVDSkdRM3BPS2ZwUjY5WnYyQWp0UFlOMk80aWVoRHBzZ1BkNzV5QVNCWTJram5JRHMzVER6OHBSX1hzbUdPdFhUclFUNnZTWA?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | news.bizwatch.co.kr | 상장사 회계감리 20년에 한 번꼴...이찬진 금감원장 "획기적으로 줄일 것" - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE05dWV0Ul9JcGNYOFN2b1drODJqNzNLNnRfMGNXYngzODk3d0I0eS10dTJJWHZ1VEZzZDRqRDRVOXFOM3M4RGFaRnlURGV0c3NwZDFsMnIxZUQ4U0RKMVVTZ2tlUjBBbHZPeFE?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | newspim.com | 이찬진 금감원장 "회계 감리주기 단축 추진…고의 분식회계 무관용 제재" - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE5idmFUaEJWUEF0bEdzNWl3dDVETFREdHFUdTVkNHBYeGFiSm0xSVhQYWh6MGlzd1JtUmNsTWJfNWRnYVdMUm04aTNuZ3dHNjNWNkF4OC1MVVZ2eVBa?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | dnews.co.kr | 이찬진 금감원장 "상장사 회계감리 주기, 20년→ 美3년·英5년 수준으로 단축" - 대한경제 | https://news.google.com/rss/articles/CBMidEFVX3lxTE1fbUk5RzFyejJNVjBxbGxhVHB3Z01UczUzTFZ1YlUxZXlwVEc3VzVaVHNuQ2FfT1BwaVRRNVVOV2hGeGF0ZWwydDNXWVNtRk5SeEFWc3hZd29QY1VxTHdZQno2cXpQZDRZZmtZVVZvSFIybWdf?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | newsfc.co.kr | 이찬진 "회계 감리주기 단축 추진…고의 분식회계 무관용 제재" - 금융소비자뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBFeTBXbnppVWZjMjFvakZqTVo5QU9XTC1mU2lxaFN4RjBGX18waGhEN2swclR4SG1uenltVXBTMUt2cXZrMk4xLUxoMEVVVkpFTGs4ckhGY2lka3ZkdlhUZW94TlpCUVdpSEE?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | hdnews.co.kr | 금감원장 “고의적 회계 부정 무관용”…상장사 회계감리 대폭 강화 - 현대경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE05WFQwV1hKd1QtV2NBSXFranVhWU1qeWxpb2E0dGpmWlk3SWpwUm1qN012S0tEdDQwNjZwWEVFWUxyS2tuNXpZSzR4bEpfS1VERUxMN1BrLWZrZmg4N2o0b2FqeXZqd29NdGpF?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | 한국경제 | 유한종 삼성전자 재경팀 부사장, 국제회계기준委 GPF위원 선임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5SYy05eHZBcVRBaTcxbXlRNG5USFFUMjJ0ajNuZktXbF9NZEJlRWFVcC1WbXF1WjJNTXFvR2VtVDRWVk9DeG01R2oxaUV4V2ZBRnVHbElSVEhtZw?oc=5 | → 대표: 삼성전자, 국제회계기준 자문기구 합류로 IFRS 개정 대응력 확대 - Traders Union |
| kifrs | newsis.com | 유한종 삼성전자 부사장, GPF 위원 선임…국제회계기준 제·개정 자문 | https://www.newsis.com/view/NISX20261106_0003857682 | → 대표: 삼성전자, 국제회계기준 자문기구 합류로 IFRS 개정 대응력 확대 - Traders Union |
| kifrs | safetimes.co.kr | 금감원 20년 걸리는 상장사 회계감리 주기 단축 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBha2RUM2lwVUQ5SnFaQTFFXzdRR3o4YmpPUDlmVVI4SmE1X1g5bHY3RFBFLVFtaUloX2hZak9BWlFmVEdaYXFpNlByLVl6cWNkRm1qQW1FYzJaNGw1Tm5nUUVQNmp0TXQxSWttQ0MtVdIBc0FVX3lxTFBQbDRmNi1JeE9xeGoxSEtpZEN6b1lHUTV2QXlLUldNSDQxYmh2Njc0eXZzb1IzNWZwNzVUdjdpZXFZS3Q1NndQYi1aOVl3d0pFQkhEX1ptQTkyNmpFS1I1VllGTGZaZUdNTHZpSHNPVDRkdjQ?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | metroseoul.co.kr | 상장사 회계감리 ‘20년 주기’ 줄인다…부실감사 징후 땐 집중 점검 - 메트로신문 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1NQlE3LWNaVDUtWXBLWHhKSHRHc0tvaUJHX25lV1hlNG1HZUtQaGdxeEVabTBYQ0N4VnZxS3JvUmZjOFJMdnE4WXN2cm9UanA0QWNaWTFQN0pSdE5tbnYzUg?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | woorieconomy.com | 금감원, 상장사 회계감리 주기 20년서 3~5년으로 단축 추진 - 우리경제신문 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE44T3ZSTzVIYzB4c2NmRkpaX05acHk0S2hMa1B3dGhLWXNfYU8teW9ZdUZGY0FsVkpDbGlXVlBvRFBTVXZvLUxpVmxlMEVyb2Y3SmRaczlHcS0?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | seoulfn.com | 금감원, 상장사 회계감리 주기 단축 추진···부실감사 감독 강화 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5MNW1fZE5GWFc3X2Fzc1NIUE1zVkZ1RXh6U05KeTd3WFVGd25tZkJEcWxEYkVqUGY5SHkzZmhYNWllX1NUTThuaHRjZHVHWGhvWDV0em9VdTZwVnhHbEhOUGh5WG9DbmNrd0E?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | ezyeconomy.com | 상장사 회계감리 20년에 한 번꼴...금감원, 감독 주기 대폭 줄인다 - 이지경제 | https://news.google.com/rss/articles/CBMibkFVX3lxTE0yWnJ2N1NRZm5EVjhnSTFYTVN3eXdxdlZaM1BwSmZETjluOXFYbnN2ZzlBRkZsa1pjRDRfM2Z5NTBDQWlsY3FFMEI4QzQ2aTA2cHVoenhfYnhDYW1qYzA3MTZteGtGcGFhYm9FdjB3?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | sidae.com | 금감원, 회계감리 주기 단축 추진 - 동행미디어 시대 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE9KemduSlRJeFU5V21ObXNvR1preTBsdE02OTYydHJSZ3lIR0dVUXZxTTkyV3RUemxFSkstRkpLdFREOGxlN3BhQlI2bGxoNFVYaEZWM2RnTVU0MHptVUE?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | ajunews.com | 금감원, 상장사 회계감리 20년 주기 대폭 단축…부실감사 무관용 제재 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFByTU5hM0NwZFdlNzNQem5RV1lFT1Bfel9CTG9OODQyUjQ3WWpFSFBtdmdwNVhLZ2wzVmtIbmNGakFObWZNdVEycF9MN2RKY0ViUzVhZENGT3hEUdIBWEFVX3lxTE00UnhZRmFfNlpCcE9fVnAxNmRXc3ZLNnBVNTZfYjVHN1RRUW8xdlFzVFltc3hjOE51LUtaMWlJNGZzZjFLeG1FbURWOV9uLTBOamNKVm5XM1I?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | datatooza.com | 구스헤드 인슈어런스, 3년치 재무제표 재작성…3분기 보고서 제출 지연 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5KdHRPM0V6OG5mNnpMTU82LVFxbmZDd01ZSWVvMnVzMnJ2cnBVX0VjSXZiV0d0Z25kYThTSWpCejV0cWhVNHBJV2p6LVZlcmRfdEdMTkVJdVUwd0VLOHNrTWhad3pWem9HRWJ6OURDV19CUGs?oc=5 | → 대표: Goosehead Insurance, 실적 발표 연기·과거 재무제표 재작성 - Investing.com 한국어 |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 |
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 머니투데이 | 코스피 상장사 5곳중 1곳, ESG 공시 준비 안 됐다 | https://www.mt.co.kr/stock/2026/11/11/2026111019562387265 | → 대표: ESG 공시 의무화 코앞인데…대형 상장사 5곳 중 1곳 '보고서 無' |
| esg | electimes.com | ESG 공시 로드맵 확정…10조 이상 코스피 상장사부터 의무화 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5XUnhUekpXVlVFZEFuR0ZtdldTYlhvX1A4Yk84UVZqc0xCLTVYQVlTT2wwLWZRUkNGb0FpWTZaeEJzUFNXWVpwYlFJQUhvTmR3aEtOS0FKeFVvQzBiVGJObkF4X3phc1VScmJMQdIBcEFVX3lxTE5HcHpjSzJTMnQyakNLT190LUVLX3ZGNXM0LWJKVzA1cXlHcjhVc1dWY1V4OGFrcG42REdfMWJRVmlXVUcwZ2JYTXE5ZE1BamduRllrbGZReTBqbjRUeWVQZUl2cEdfZ09CRVFRemlvS3Q?oc=5 | → 대표: ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| icfr | datatooza.com | 퍼블릭 폴리시 홀딩스, 내부통제 중대한 취약점 여전히 미해소…3분기 분기보고서 제출 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE5OLWNZM2l1SkVIdWs1djAtY2Jubkx6aTlvbDE3V0tTamd3ZlZfY0VMMzM2d29iWGEwVVMxN256dXdNOHRac0NncUlhdEJkbXNSb21LVnRkSlF4Y3FpWWFzekRneW1PLUlZclZxa0xDX0dQQQ?oc=5 | → 대표: 퓨마 바이오테크놀로지, 새 ERP 도입 뒤 내부통제 중대한 취약점 공개…재무제표 재작성은 불필요 - 데이터투자 |
| icfr | datatooza.com | 고어스 홀딩스 10, 2025년 3분기 주당순손익 오류 정정…내부통제 중대한 취약점 발견 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE1TZ0ZZUE5aSnZjbVhWT1JyNktDQVlXT0duUlpkbzF1ajFabzFMUnJRREQtVEFTdnlKejBvMHVIR2JKVm1EU2ttMW9qN1Byd0N3SHliMjlIUWlkQTZZZTJycWxtVHhDUER1TENfc3c2Wm9qaHc?oc=5 | → 대표: 퓨마 바이오테크놀로지, 새 ERP 도입 뒤 내부통제 중대한 취약점 공개…재무제표 재작성은 불필요 - 데이터투자 |
| icfr | biz.chosun.com | 이찬진 “회계법인 내부통제 부실, 경영진 책임까지 묻겠다” | https://biz.chosun.com/stock/stock_general/2026/11/10/3FVIQISXFZHHLBLXGAPGYUMYQA/?utm_source=naver&utm_medium=original&utm_campaign=biz | → 대표: 손정화 서울시의원, 서울연구원 회계관리 부실 지적...내부통제 체계 점... |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## collect:event_announcement (6건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 제13차 관계부처 합동 일자리전담반(TF) 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079914&menuNo=4010100 |  |
|  | 재정경제부 | 제19회 아시아 고위공무원 초청연수 실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079901&menuNo=4010100 |  |
|  | 재정경제부 | 제276차 대외경제장관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079883&menuNo=4010100 |  |
| esg | globalhumantimes.kr | BSI 영국표준협회, ‘지속가능성 세미나 2026’ 개최… 의무 공시 및 검증 시대 대응 전략 제시(BSI Korea to Host 'Sustainability Seminar 2026' on Strategies for Mandatory Disclosure and Verification Era) - 글로벌휴먼타임즈 | https://news.google.com/rss/articles/CBMickFVX3lxTE9XdmpZUGo5SVRFOGVzOVB4aWozVzlWLUdib1V1ekdRZDVES25XUTJTQ1c2WnAtWnVKZWI4cUUwaEhQMjNpQ3dKbFlDNXdDM3dodUVUSGJTdUQxMkJvZEFiOUFSdGYzSkFIYTcyLXB4dllFdw?oc=5 |  |
| esg | betanews.net | 네이버, ‘2026 지속가능경영유공 정부포상’ 대통령 표창 수상 | https://www.betanews.net/article/view/beta202610300070 |  |
| esg | ESG경제 | [알림] KSSB·ESRS 이중중대성 평가 웨비나 초청 | https://www.esgeconomy.com/news/articleView.html?idxno=17019 |  |

## collect:incident (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 한국경제 | 외감법은 경찰, 자본법은 중수청…분식회계 수사 차질 불가피 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wOF91b3FKNTlVV3FUM3J2amdHek9VS29CTHZ1N3d3NFJiOWtOakNkRVRPSzhFd3ZKMHM3RkRmcW9QeE9hRFV4NHNhbmQ5Q0RSNUpIbEYyOG9zUQ?oc=5 |  |

## collect:law_name_mismatch (7건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 법제처 | 지방교부세법 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방교부세법 시행령 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방교부세법 시행규칙 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방세특례제한법 시행령 (검색어 '지방세특례제한법') |  |  |
| tax | 법제처 | 지방세특례제한법 시행규칙 (검색어 '지방세특례제한법') |  |  |
| tax | 국민참여입법센터 | 지방세특례제한법 시행령 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/89360 |  |
| tax | 국민참여입법센터 | 지방세특례제한법 시행규칙 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/89358 |  |

## collect:no_category (17건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 비상경제장관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079917&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] '26.10월 고용동향 및 평가 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079916&menuNo=4010100 |  |
|  | 재정경제부 | 아세안+3 역내 위기 대응 역량을 강화하는 신속금융 프로그램(RFF) 시행 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079919&menuNo=4010100 |  |
|  | 재정경제부 | 반도체 전문가 간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079895&menuNo=4010100 |  |
|  | 재정경제부 | 긴급 시장상황점검회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079890&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 코리아그랜드페스티벌x행복한 백화점 현장행보 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079882&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] 세계은행그룹 부총재에 두 번째 한국인 진출 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079886&menuNo=4010100 |  |
|  | 금융위원회 | 다음 금융은 이미 시작됐다 「코리아 핀테크 위크 2026」, 11월 25일 개막 | https://www.fsc.go.kr/no010101/88104?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 국내외 주식시장 변동성 확대로 단계별 대응조치 가동 | https://www.fsc.go.kr/no010101/88100?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 현재 유포되고 있는 부동산 대책 관련 게시글의 보도에 유의하여 주시기 바랍니다. | https://www.fsc.go.kr/no010101/88099?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융권은 개인정보 유출 사고에 따른 보이스피싱 예방에 총력 대응하고 있습니다. | https://www.fsc.go.kr/no010101/88098?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 기업지배구조보고서 공시를 통해 상장회사의 주주보호와 주주환원 노력을 확대해 나가겠습니다. | https://www.fsc.go.kr/no010101/88091?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | AI시대, 거세지는 침해위협에 맞서 全 금융권이 튼튼한 보안체계로 무장하도록 혁신적인 정책과제를 적극 추진하겠습니다. | https://www.fsc.go.kr/no010101/88086?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ｢“취재정보로 매매해 ○○억 부당이득”···○○신문 조사 마무리｣ 보도 관련 | https://www.fsc.go.kr/no010101/88085?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 한국, 아시아지배구조협회(ACGA)    기업지배구조 순위 역대급 ‘5위’ 달성 | https://www.fsc.go.kr/no010101/88084?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 홍콩 H지수 ELS 관련 은행·증권사 검사 결과 조치 - 제19차 금융위원회(11.4.) 의결 | https://www.fsc.go.kr/no010101/88082?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 계리가정보고서 도입 등  ｢보험업감독규정｣ 개정안 금융위원회 의결 | https://www.fsc.go.kr/no010101/88081?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |

## collect:non_kifrs (26건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 종전기업회계기준과 일반기업회계기준 질의회신 비교표 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40533&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 24-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40531&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 21-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40530&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 20-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40529&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 19-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40528&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 17-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40527&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 2026년 제10회 회계기준위원회(일반기업회계기준 개정안 – 제4장 연결재무제표 등) | https://www.kasb.or.kr/front/board/calViewA.do?seq=1130 |  |
|  | 한국회계기준원 | [일반기업회계기준] 2023년 부채의 유동·비유동 분류 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2023년 국제조세개혁 – 필라2 모범규칙 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2023년 국제조세개혁 – 필라2 모범규칙 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2022년 소규모비상장 지배기업의 비외감기업 연결제외 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2022년 수익관련보조금 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2022년 고객 예수금의 현금흐름표 분류 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2020년 종속기업의 범위: 적용유예 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2020년 일반기업회계기준 연차개선(2020년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2019년 일반기업회계기준 연차개선(2019년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2018년 일반기업회계기준 연차개선(2018년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2018년 일반기업회계기준 연차개선(2018년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2018년 일반기업회계기준 연차개선(2018년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2017년 일반기업회계기준 연차개선(2017년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2017년 일반기업회계기준 연차개선(2017년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2016년 일반기업회계기준 연차개선(2016년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2016년 일반기업회계기준 연차개선(2016년) | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2015년 건설계약 공시 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2015년 물적분할(불비례적 인적분할 포함) 회계처리 변경 | https://www.kasb.or.kr/front/board/List2006.do |  |
|  | 한국회계기준원 | [일반기업회계기준] 2015년 일반기업회계기준 연차개선(2015년) | https://www.kasb.or.kr/front/board/List2006.do |  |

## collect:old_year (8건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 국세청 | 2024년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=1333184 |  |
| tax | 국세청 | 2023년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=1322892 |  |
| tax | 국세청 | 2022년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=1303856 |  |
| tax | 국세청 | 2021년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=1294867 |  |
| tax | 국세청 | 2020년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=54244 |  |
| tax | 국세청 | 2019년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=54245 |  |
| tax | 국세청 | 2018년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=54246 |  |
| tax | 국세청 | 2017년 개정세법 해설 | https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=7133&nttSn=54247 |  |

## collect:out_of_scope (212건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | [공지사항] 홈페이지 게시_본인 인증 서비스 일시 점검 안내(2026. 11. 14.(토) 22:00 ~ 2026. 11. 15.(일) 04:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI 실무 세미나 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] IASB 정보요청서, IFRS 9 '금융상품', IFRS 7 '금융상품: 공시' 위험회피회계 사후이행검토(PIR) 국내 의견조회 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] ISSB 자연 관련 공시 실무서 공개초안 요약자료(Snapshot) 국문본, ISSB 아웃리치 세션 및 국내 의견수렴 일정 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(5차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 본인 인증 서비스 일시 점검 안내(2026. 10. 17.(토) 21:00 ~ 2026. 10. 18.(일) 05:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [세미나] IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/calViewA.do?seq=1129 |  |
|  | 한국회계기준원 | [세미나] 회계기준원-환경산업기술원, 지속가능성 공시기준 이행지원 세미나 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1127 |  |
|  | 한국회계기준원 | [세미나] 한국회계기준원 개원 27주년 세미나: 지속가능성 공시, 새로운 기준의 시대 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1125 |  |
|  | 정책브리핑(질병관리청) | [11.11.행사시작(10시30분)이후] '국민 건강을 지킨 현장의 노력, 더 나은 만성질환 예방관리로' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788704&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 고교 일학습병행 학습근로자 대상 '도메인 인공지능(AI) 특강' 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788702&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 영월의료원, 의료 AI로 진료 부담 덜고 '분만·소아' 등 필수의료 공백 해소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788705&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 세계적 인공지능바이오 강국 도약을 위한 소버린 바이오 전략 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788703&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 민원현장 목소리 듣고 국민 신뢰 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788700&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 계약부터 분쟁까지, 법무부가 해외진출 기업의 법률 리스크 대응을 지원합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788693&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 아동·청소년부터 사망자까지, 개인정보 보호체계 개선 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788695&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 민간 노하우·장비 더해'공공나노팹' 반도체 연구지원 거점으로 도약 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788688&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능·정보통신기술, 성장의 공식을 바꾸다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788687&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부， 6개 참전국 참전용사 및 유가족 감사오찬 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788686&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 6.25전쟁 에티오피아 전사자 추모의 벽 건립， 11일 현지서 제막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788685&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | '26~'27년 겨울철 대설·한파 대응 본격 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788699&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 안전은 더 높게, K-승강기는 세계로! 2026 승강기 안전주간·엑스포 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788697&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 인공지능 기술로 방송미디어 산업의 미래혁신을 일군다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788689&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 매개충 우화 시기부터 병 발생 위험까지… 소나무재선충병, 산림과학으로 예측한다! - 국립산림과학원, 매개충 우화 전망·발생위험도 분석으로 방제전략 수립 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788692&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 비상경제장관회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788684&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 민원현장 목소리 듣고 국민 신뢰 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788679&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 김성환 기후부 장관, 호남권 반도체 산단 전력·용수 공급 현장점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788683&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 2026년 11월 1일 ~ 11월 10일 수출입 현황 [잠정치] | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788682&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 민·관·학 협력으로 건설정보모델링(BIM) 실효성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788678&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 공주 공산성, 백제 왕궁의 실체를 드러내다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788680&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) '26.10월 취업자수는 13.9만명 증가하여 4개월 연속 두 자릿수 증가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788677&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 미래의 역사가 될 한국 현대사 기록 6건, '예비문화유산' 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788672&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 「영덕 장육사 대웅전」 국가지정문화유산 보물 지정 예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788670&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 행복청, 동절기 대비 건설현장 안전점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788674&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | [보도참고] '26.10월 고용동향 및 평가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788668&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | 농구 관람부터 고충상담, 고용정보까지 한 번에! 달리는 국민신문고, 창원시 '청년 명소' 찾아간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788665&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, GLP-1 계열 의약품 안전조치 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788664&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 동물병원 수의사 '케타민' 셀프 투약 적발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788663&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '제10회 서점의 날', 책과 사람을 잇는 서점의 가치 되새겨 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788660&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 디지털·AI 경쟁력, 전년대비 8단계 상승한 10위 기록 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788662&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 10월 고용동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788661&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | G7 외교장관회의 계기 한-우크라이나 외교장관회담(11.10) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788659&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "사용이 끝난 배터리, 남아 있는 에너지에 주의해야" 국립소방연구원, 폐리튬이온배터리 열폭주 실험으로 화재위험 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788658&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 「제11회 부동산산업의 날」  "국민 신뢰와 산업 혁신 다짐" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788656&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 전국 겨울철새 서식지 100곳, 27년간의 생태기록으로 과학적 관리체계 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788657&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 제13차 관계부처 합동 일자리전담반(TF) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788667&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 제13차 관계부처 합동 일자리전담반 회의 개최 취약계층 체감 일자리 여건 개선을 위해 총력 대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788666&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | G7 외교장관회의 계기 한-캐나다 외교장관회담(11.10) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788655&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한미 외교장관 환담(11.10.) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788654&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한국 정부대표단, 프랑스 주최 「G7+ 마약밀매 대응 항만 네트워크」 출범회의 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788652&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 한국 정부대표단, 프랑스가 개최한 'G7+ 마약 밀매 대응 항만 네트워크' 출범 회의 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788653&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한일 에너지 파트너십의 미래 - 탄소중립과 에너지 공급망 회복력 강화를 위한 한일 민관 협력 강화 방안 논의 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788651&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 진주국제농식품박람회서 산림바이오 소재 연구성과 선보여... - 국립산림과학원, 가시나무류 및 보리밥나무 등 다양한 산림소재 활용 기술이전 성과 전시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788650&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부, 국군사관학교 민간자문특별위원회 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788625&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 2026년 하반기 선교단체와의 안전간담회(11.10.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788624&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 행복청·충북도, 오송역~인천공항 버스 운행으로 접근성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788673&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부장관, 육·해·공군사관학교  생도 및 사관학교장 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788623&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | ODA에 대한 청년의 생각, 직접 듣고 싶습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788622&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가교육위원회) | [보도자료] 국가교육위원회 2026년 제12차 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788621&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 제4회 한·ASEAN·CIS 경쟁당국 협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788620&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | LG디스플레이, 2026년 특허기술상 1등 영예 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788619&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [차관동정] 정의경 제2차관, "수도권 서부지역 교통난 해소, 철도·도로사업 조기 완공에 속도 내야" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788616&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 범국가 「지식재산 거래 통합 플랫폼」 2027년에 구축된다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788618&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "잘 심은 나무, 알차게 키운다"... 영주국유림관리소, 숲가꾸기 1일 체험행사 개최 - 11월 숲가꾸기 기간 맞아, 영주국유림·영림단·약용자원연구소 총출동 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788613&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 폭설에도 제설제 공급 차질 없도록,민관 협력체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788615&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제2차 G7 외교장관회의 계기 한-이집트 외교장관회담(11.9.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788611&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 행복주택 공실 해소를 위해 적극 노력해 나가겠습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788610&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 울진 금강소나무림의 효과적 보호를 위한 방제전략 마련 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788605&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 피지컬 AI 경쟁 속  한국의 경제안보 대응 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788606&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림, 2026년 가을철 소나무류 이동 특별단속 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788603&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제16차 한-카리브 고위급 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788597&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청 편백숲! 국민과 함께 가꾸어요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788601&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 'K-문샷 정책 세미나' 개최, 국가 과학 난제 해결을 위한 과학 인공지능 혁신을 논의하다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788593&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 우체국과 함께 따뜻하고 안전한 겨울나기 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788599&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 충주국유림관리소, 숲가꾸기 1일 체험행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788595&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청이 개발 지원한 '건축유산 복원설계' 기술, CES 2027 최고혁신상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788591&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰, 연말 고속도로 사망자 감소를 위해, 전국 단위 '화물차 등 계도·단속' 나선다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788590&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰, 멈춤 없는 단속, 예외 없는 엄단 「부동산범죄 3차 특별단속」 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788588&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 겨울철 도로안전 빈틈없이  … 15일부터 24시간 제설대응체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788583&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 소나무재선충병 '생활권 위험목' 긴급 예찰·방제 총력 대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788585&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 전국 재난의료 인력 150명 모여 대형 재난 대비 현장 대응 역랑 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788581&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | G7 외교장관회의 계기 한-사우디 외교장관회담(11.9.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788576&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 「유아교육법 시행령」 일부개정령안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788579&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 「영유아보육법 시행령」 일부개정령안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788578&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 「교육공무원 임용령」 일부개정령안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788577&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 지역방송 콘텐츠, 해외 진출 지원 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788573&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 2026년 3분기 기업특성별 무역통계(잠정) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788572&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "소음피해, 사고 위험에서 주민 보호해야"… 서대전역 광장 교통혼잡 문제 해결한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788571&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 너랑 나랑 다 같이, 한국어로 하나 되는 세계 청소년 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788567&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 위험직무 순직공무원 예우 확대·재활 통계 신설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788562&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | '2026년 시·도교육청 등 230개 공공기관 기록관리 기관평가 결과' 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788570&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 3분기 기업특성별 무역통계(잠정) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788566&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 올겨울, 먼저 찾아가는 에너지바우처로 따뜻한 겨울나기를 지원합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788565&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | '유출지하수, 하·폐수, 공업용수'까지 수열에너지 범위 대폭 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788582&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 자생 생물자원으로 한국형 화장품 소재 개발 지원 앞장선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788564&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 겉모습 구별 어려운 습지플라나리아, 유전정보·형태 분석으로 신종 3종 규명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788563&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 네이버파이낸셜-두나무 기업결합 건  심의 절차 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788559&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 매운맛 라면 12종 품질 비교정보 제공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788558&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(조달청) | [보도참고] 평가위원 사진 유출 신속 대응 피해 최소화 및 재발 방지 총력 "사진만 유출… 다른 개인 정보 유출 없어" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788555&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 알바니아 여행경보 상향 조정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788557&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 「한반도 평화체제 및 평화경제 미래비전 국제세미나」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788580&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국장애인고용공단-충청남도교육청 장애인 고용증진 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788609&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 「2026 울산 공공기관 합동 혁신 경진대회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788589&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 「철도차량 형식승인제도 개선방안」 추진 "철도차량 안전은 꼼꼼하게, 검사는 효율적으로" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788554&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 신도시 교통대책 속도 높인다 … 도로사업 16곳 집중 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788553&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 항만 내 드론 비행 금지 정보, 이제는 지도에서 바로 확인하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788552&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '26년도 염소고기에 대한  FTA피해보전직불금 지급 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788551&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '26년 4분기 축산물이력제 합동단속 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788550&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농업과 기업의 상생,  '모두의 상생 프로젝트' 본격 시동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788549&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 제21차 논 농업·물·생태계 운영위원회(INWEPF), 대한민국에서 열린다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788548&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농관원 시험연구소, '안전관리 우수연구실'과 'KOLAS' 동시 석권, 철통 안전망 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788547&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, '특정농지등의 정리에 관한 특별조치법안' 지역별 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788546&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 사회적기업의 새로운 지평,  국내외 경험에서 해법을 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788543&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국폴리텍대학, 산업이 원하는 학과를 먼저 만든다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788542&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 안전의 가치를 더하고,  감사혁신의 기반을 넓히다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788541&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) "공공부문이 선도하여 '모두를 위한 더 나은 일터'를 만들겠습니다." 정부, 공무직委 6개 분야별협의회 발족 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788540&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제1차 규제합리화 정례브리핑 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788545&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제22차 부동산 불법행위 대응협의회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788544&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 겨울철 위기가구, 정부가 먼저 찾아 온기 건넨다 「2026~2027년 겨울철 취약계층 보호대책」 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788539&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 그릇과 기와에 새겨진 '조선 왕실의 기록' 시민강좌 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788537&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | '탄생 100주년' 안비취 명인의 세 제자, 한 무대에서 스승을 추억하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788535&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 「한국 미술문화유산 정보의 국제적 활용과 확산」 국제학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788533&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 양자 플래그십 프로젝트, 양자컴퓨팅·통신·센싱 핵심기술 개발 성과 가시화  - 「양자과학기술 플래그십 프로젝트 연례회의(애뉴얼 미팅, Annual Meeting)」 개최 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788531&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | '내 개인정보를 지키는 꿀팁'.. 개인정보위, 숏폼 콘텐츠 공모전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788526&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 빚 때문에 생명 포기하는 일 없도록 자살예방상담(109)에서 채무상담(1375)으로 바로 연결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788530&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 킬레이션 주사 투약 의혹 의료기관 행정조사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788529&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 유엔참전용사 국제추모의 날 기념식 부산서 거행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788520&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 부정청약 관계부처 합동점검 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788524&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 2026년도 도선수습생 13명 선발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788523&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 연구실부터 임상 현장까지, 차세대 결핵 진단·치료 실용화 연구 성과 공유(11.10.화) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788521&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 한·일 국립감염병연구소, 감염병 공동연구 협력 강화(11.10.화) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788522&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 전자상거래 등에서의 소비자보호 지침 개정안 행정예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788519&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 대·중소기업 간 대금지급 관행 개선을 위한 현장 의견 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788518&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 서비스 수출실적 증명, 더 쉽고 편리하게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788517&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | K-사이언스의 기틀을 만든 과학기술 이야기, 국가중요과학기술자료 23건 신규 등록 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788532&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(감사원) | 감사원, 최초 실시한 '국민제안 감사 아이디어 공모'에 국민 855명 참여, 1,109건의 제안 접수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788568&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 화장품 인체적용시험기관 대상 정책설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788516&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 겨울철 다소비 수산물 집중 수거.검사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788515&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | G7 외교장관회의 계기 한-프랑스 외교장관회담(11.9.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788512&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 창립 20주년 한국도핑방지위원회, 새로운 도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788514&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 청와대 사랑채, 강원 지역문화 상징하는 전시와 특별공연 선사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788513&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | K-소상공인 수출성과, '로컬'을 넘어 '글로컬'로 도약 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788511&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "소방 현장 위험, 미리 보고 대비한다!" 국립소방연구원, 「소방 현장 안전보건 정책연구 소통 발표회(세미나)」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788510&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교전략정보본부장, 국제원자력기구(IAEA) 사무총장 면담(11.9.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788509&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.10.화.석간] 만성콩팥병 환자, 단백질 무조건 줄이면 오히려 '독', 투석·사망 위험 급증 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788508&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | AI로 아동·청소년 성착취물 삭제 지원 9.7배 늘었다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788607&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제48차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788505&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 2차관, 국제수로기구(IHO) 사무총장 접견 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788476&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 헝가리 진출 배터리 기업,  친환경 파트너쉽 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788475&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 순직 소방공무원 추모 이름표(명패) 헌정식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788478&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청 제64주년 소방의 날 기념식 개최… 소방의 헌신과 사명 되새겨 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788477&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해양경찰청, 제5회 해양 국제범죄 대응 학술의회(I-MARC) 성공적 개최 ! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788471&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 아시아·태평양 해양오염 방제 협력 주도...제2회 한-아세안 방제 공개 토론회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788470&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 배경훈 부총리, 국제전기통신연합 전권회의에서 국제 디지털 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788469&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 제주에 '탄소저감·새활용' 모델정원 2곳 조성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788467&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 강금실 글로벌기후환경대사, 제31차 유엔기후변화협약 당사국총회(COP31) 정상회의에 대통령 특사로 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788468&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(경제사회노동위원회) | [보도자료]「인구구조 변화와 일자리 공론화 특별위원회」 4차 전체회의- 일자리 녹서 초안 및 100인 시민회의 결과 보고 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788465&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 산불 취약 가구 찾아 화목보일러 안전관리 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788464&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 전남광주 어르신, 카드 한 장으로 도시철도 무료·교통비 환급 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788462&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 민간과 함께 인공지능 침해 위협에 대응하는 보호체계 정착방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788460&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 고용노동부 서산지청,  부당노동행위 혐의  압수·수색 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788456&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 환자 안전과 인권 보호 위해 연말까지 정신의료기관 운영실태 릴레이 합동점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788452&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국산 NPU, 엔비디아 시스템과 연계해 글로벌 AI 인프라 시장 진출 길 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788455&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 전직급 인공지능 대화형 코딩으로 행정혁신 앞당긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788451&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 소나무재선충병 전국 확산 차단 위해 소나무류 이동 특별단속 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788449&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 스마트 안경 관련 내신평가 부정행위 전수조사 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788440&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 수능 수험생 여러분, 전자기기 가져오지 마세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788439&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부-일본 문부과학성, 교육행정 교류로 상호이해와 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788438&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부, 맞춤형 현장 자문으로 학생 마음건강 안전망 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788437&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "중독 예방·치료·회복, 함께 만드는 변화" '2026 중독예방·치료·회복 주간' 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788434&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | '26년 11월 '대한민국 엔지니어 상' 수상자 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788461&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부, '2027년 생활권 보행환경 종합정비사업' 대상지 5곳 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788444&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | '차세대 지방행정공통시스템 구축 통합사업 설명회' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788442&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 국립공원 자원봉사자 구슬땀 결실… 경북 안동서 참여자 교류 행사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788435&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 고농도 초미세먼지 발생… 실전처럼 훈련하고 빈틈없이 대응한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788436&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(기상청) | "극한호우-이상기후, 똑똑한 인공지능(AI)으로 잡는다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788561&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.10.화.조간] 남성 30~40대 2명 중 1명 비만 성인 비만율 10년 새 26.9% 증가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788433&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 배달앱 불공정행위 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788431&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(감사원) | 육군본부 기관정기감사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788432&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 제19회 아시아 고위공무원 초청연수 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788428&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "현장학습과 소풍을 보장해 주세요" 아동총회 대표, 국회에 정책 결의문 전달 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788426&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 「한반도 평화관광협력 국제세미나」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788454&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 도심항공교통(UAM) 실증,  기술검증 넘어 지역 상용화로 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788425&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 전세사기피해자 최소보장제 시행,  10일부터 최소지원금 신청하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788424&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 어촌뉴딜 3.0 신규 대상지 40개소 선정...  사업 구조도 개편한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788423&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해양수산부, 중소선사와 함께 친환경·저탄소 전환에 대응한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788422&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 글로벌 해양정보 디지털 전환의 중심인 '국제수로기구(IHO) 인프라센터' 대한민국에 문 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788421&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부, 국내 해양플랜트 서비스기업의 베트남 시장 진출을 본격 지원한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788420&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 국내 곤충산업 591억 원 규모로 지속 성장··· 사료용 곤충산업 '65.3% 증가' 견인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788419&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 산불 대비 태세 강화에 재난특교세 150억 원 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788418&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 디지털윤리 골든벨 왕중왕은 나야 나! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788413&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 국립재활원 사용적합성평가지원센터 ISO 13485 국제 인증 획득 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788411&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | AI가 흔드는 지식재산의 경계, 새로운 질서를 논의한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788410&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 스마트 글래스 이용 시 유의사항 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788408&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 충남 예산 대흥초 출신 독립유공자 5명 후손 확인  10일 훈장 전수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788407&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | AI 로봇 등 첨단기술로 보훈복지시설 국가유공자 정신건강과 안전 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788406&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 기업결합 시정조치 부과기준 고시 개정안 행정예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788402&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 한·중·일 협력으로 생성형 인공지능(AI) 시대의 지식재산 인재 양성 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788409&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | K-지식재산, 동티모르 산업 발전 이끈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788401&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 한국에서 배우고 세계와 연결하는 국제적 지식재산(IP) 인재들 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788400&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 카페 점장에서 로봇 개발자로 국민내일배움카드로 여는 인생 2막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788405&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국장애인고용공단,  '대한민국 일자리 어워드' 3년 연속 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788404&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | ㈜아워홈 산업안전·근로기준  합동 감독·점검 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788403&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 인공지능(AI) 분야 선도연구기관 3곳 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788399&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 죽변항 수산물축제와 함께하는 산불예방·산림보호 홍보 캠페인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788395&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 2026년 10월 고용행정 통계로 본 노동시장 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788397&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 일하는 사람의 든든한 사회안전매트, 국민이 이름 짓는다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788396&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 가덕도신공항 부지조성공사 실시설계 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788398&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부·해수부, 어업분야 외국인 계절노동자 고용 어가 인권실태 합동점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788393&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-11&endDate=2026-11-11&srchWord=&period= |  |

## collect:out_of_window (34건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 국민참여입법센터 | 법인세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-07) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88012 |  |
| tax | 국민참여입법센터 | 법인세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87940 |  |
| tax | 국민참여입법센터 | 부가가치세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87934 |  |
| tax | 국민참여입법센터 | 소득세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-07) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88010 |  |
| tax | 국민참여입법센터 | 소득세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87942 |  |
| tax | 국민참여입법센터 | 국제조세조정에 관한 법률 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87944 |  |
| tax | 국민참여입법센터 | 조세특례제한법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87946 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| kifrs | 임팩트온 | 기후위험, 재무제표 주석까지 들어온다…회계기준원, 공시 사례 공개 | http://www.impacton.net/news/articleView.html?idxno=19406 |  |
| kifrs | ESG경제 | 재무공시와 기후공시 연계 강화...회계기준원, 기후위험 공시 사례 제시 | https://www.esgeconomy.com/news/articleView.html?idxno=15878 |  |
| kifrs | tfmedia.co.kr | 회계기준원 IFRS 20 간담회에 에너지 기업 ‘쫑긋’…IASB 부위원장도 참... | https://www.tfmedia.co.kr/news/article.html?no=204787 |  |
| kifrs | 일간NTN | 회계기준원 지속가능성기준위원회, 지속가능성 공시기준 첫번째 세트 의... | http://www.intn.co.kr/news/articleView.html?idxno=2049269 |  |
| kifrs | tfmedia.co.kr | 회계기준원 KSSB, 지속가능성 공시기준 첫 번째 세트 의결 | https://www.tfmedia.co.kr/news/article.html?no=201983 |  |
| kifrs | 매일경제 | 국제회계기준 해석委, 일탈회계 관련 기준개정 필요없다 의견 | https://www.mk.co.kr/article/11489251 |  |
| kifrs | 이데일리 | 한국회계기준원 "국제회계기준 해석위, 일탈회계 극히 예외적…기준개... | http://www.edaily.co.kr/news/newspath.asp?newsid=04060646642397208 |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| icfr | 한국세정신문 | '회계부정 포상금 상한 폐지' 외감법 시행령 공포 | https://www.taxtimes.co.kr/news/article.html?no=275268 |  |
| icfr | news2day.co.kr | 김현정 의원, 고의 분식 회사관계자의 과징금 상향하는 외감법 개정안 ... | https://www.news2day.co.kr/article/20260114500002 |  |
| icfr | 조세일보 | 與, 고의 분식 회사관계자 과징금 상향 외감법 개정안 발의 | http://www.joseilbo.com/news/news_read.php?uid=560684&class=18&grp= |  |
| icfr | kgnews.co.kr | 김현정, 고의 분식 회사관계자 과징금 올리는 ‘외감법 개정안’ 제출 | https://www.kgnews.co.kr/news/article.html?no=881132 |  |
| icfr | incheonilbo.com | 고의 분식 회사관계자 과징금 '두 배'…김현정 의원, 외감법 개정안 발... | https://www.incheonilbo.com/news/articleView.html?idxno=1314393 |  |
| icfr | dailyt.co.kr | 김현정 의원, 고의 분식 회사관계자의 과징금 상향하는 외감법 개정안 ... | https://www.dailyt.co.kr/newsView/dlt202601130009 |  |
| icfr | news.koreanbar.or.kr | '통과 목전' 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔... | https://news.koreanbar.or.kr/news/articleView.html?idxno=34797 |  |
| icfr | shinailbo.co.kr | 금융위, 회계부정 제재 강화 후속조치…외감법 시행령·감사규정 개정 ... | http://www.shinailbo.co.kr/news/articleView.html?idxno=2152790 |  |
| icfr | tfmedia.co.kr | [감사인세미나] 최운열 회계사회장 “외감법‧공인회계사법상 형벌규정... | https://www.tfmedia.co.kr/news/article.html?no=194910 |  |
| icfr | news.koreanbar.or.kr | "기업 외부 감사인에 변호사 반드시 포함"… 이정문 의원, 외감법 발의 | https://news.koreanbar.or.kr/news/articleView.html?idxno=33201 |  |
| icfr | kbanker.co.kr | 회계부정조사단에 '10년↑ 전문가' 포함…외감법 손질 | https://www.kbanker.co.kr/news/articleView.html?idxno=219315 |  |
| icfr | 한국세정신문 | 외감법 시행령 입법예고…지정 유예요건 미유지시 감사인 지정 | https://www.taxtimes.co.kr/news/article.html?no=268901 |  |
| icfr | etoday.co.kr | 분식회계로 돈 못 벌어도 최대 10억 벌금…외감법 개정안 본회의 통과 | https://www.etoday.co.kr/news/view/2452467 |  |
| icfr | 한국세정신문 | 상법‧외감법 개정안 등 국회 본회의 통과 | https://www.taxtimes.co.kr/news/article.html?no=268817 |  |
| icfr | 한국세정신문 | '지배구조 우수기업 주기적 지정 유예' 외감법 시행령 이달 입법예고 | https://www.taxtimes.co.kr/news/article.html?no=268815 |  |
| icfr | 한국세정신문 | 이상휘 의원, 외감법 개정안 발의…배수벌금형·벌금상한액 함께 규정 | https://www.taxtimes.co.kr/news/article.html?no=268780 |  |
| icfr | 이데일리 | 금감원 "2024회계연도서 내부회계관리제도 위반 14건…과태료 부과" | http://www.edaily.co.kr/news/newspath.asp?newsid=01725286642401800 |  |

## collect:tax_subject (41건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | 2026년 부동산 세제개편안 주요 내용 총괄표 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9VV05RWWFtWkNqZmNWQktodVFiLS1GckNYcXZ6SGUxcFc5dXhEQi0tN0FmM2tucEROdHF6OU4xUnpmd1NXd29fQUpnMkdRbnVac2pqOEsxUTBaN1JWdjcyVjBHOUE?oc=5 |  |
| tax | karnews.or.kr | [세법톡톡] 2026년 세제개편안 (양도소득세) - 한국부동산뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Ub0liX2hObkdsdUhZc3lES3AycE9NV2xfVHBvMDJNYXpkbkVZNi1FdlZKcklqUndyX0xoZXB1OUFDdHNkZWNHa1BQN1FWMHBMUlZhV2V1ckpvRWUwZVpzZFctNllmUFd3bHZB?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | news.kbs.co.kr | 부부 공동명의는 진짜 불리할까? 세제개편안 오해와 진실 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5yTUo1c2FfUGVDcERxc2lJM0JHSUItNks1N083NkViV1Z2VHFnSWFUdjdHYnRyUE9fSUoydEg0ekNnY0xVRlBiTEkzYWlBYkplV3p4UjctSkVGVlU?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | sejungilbo.com | [토론회] “체감 경기 회복 vs 과세 예측가능성”…`26 세제개편 쟁점은? - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE14eTJsdUFhend0enBURENHX2dBT0pFdS1mcU9pcGo3UllMbXZsU2x3OG1jb183aFBKZFJQb3ZGWlgxQUVqM1YwZDNRV1JlX0F6SWdiVHdyTzRQRXNnY0FqczZNZ1Ixam80UGFMZw?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | daenews.co.kr | 정부 세법개정안, 세수 얼마나 바뀌나…국회서 여야·전문가 토론:동아경제신문 & daenews.co.kr - 동아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1zamFET0V6bVlRR1NOd3A5OWk2UFc0anBVbUxMSEN4WGJHWGk1ZUVTemRXMVpQSHZRM1ItUnFKOFd0cEdNc0ZEYXhORlNWdVJzakZJUFJ4b1l4RGc2d3lCUFJR0gFiQVVfeXFMTXNqYURPRXptWVFHU053cDk5aTZQVzRqcFVtTExIQ3hYYkdYaTVlRVN6ZFcxWlBIdlEzUi1ScUo4V3RwR01zRkRheE5GU1Z1UnNqRklQUnhvWXhEZzZ3eUJQUlE?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | mobile.newsis.com | 이형일 부총리, 세법 개정안 관련 제안설명 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTFA0RjZKVUZXUjJIaHFhMkxQTnVla0hFM3JYeHFhaVJKa0JZR3BNVXZ4Q1l1cE14SkFndjlNMmdHQzFDRnhxRVU5R19sMzFiS0ltRkJtQTJJNTVkdmhhaVRoTjNENUdPTWNzaW5GRGU1cnRvREd1dGhyU9IBeEFVX3lxTFA0RjZKVUZXUjJIaHFhMkxQTnVla0hFM3JYeHFhaVJKa0JZR3BNVXZ4Q1l1cE14SkFndjlNMmdHQzFDRnhxRVU5R19sMzFiS0ltRkJtQTJJNTVkdmhhaVRoTjNENUdPTWNzaW5GRGU1cnRvREd1dGhyUw?oc=5 |  |
| tax | newsk.net | 세법 개정안의 주요 변경 사항 : 한인동포신문(몽골) - 뉴스케이 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXdlRVQnREMG5BcGNrUjNUdF9MSEVtbGJzdHBuWjNBM29ZTDBtYXY5TWw4Q1F4OG1QMlVSZnQ1YTNYMEpBcmJKX1hhTDJOczE0UTQ5VnlRY1FmZw?oc=5 |  |
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | jinju.news | 김태호 의원, 지역균형발전 강화를 위한 지방교부세법 개정안 대표발의 - 진주인터넷뉴스 | https://news.google.com/rss/articles/CBMid0FVX3lxTE44X0w1UUNpbTMtSnZFa2ZpdUF0dHhxeU5GWFlWNF9NZTY0aWRNWGJlS0lLMEJFc1lERHd0MFBubjhHUVBERlVKT204VjQ2TlIxb3drSUJfV3FyMWcxX1RONzUxWE9LMzkxY2VGZVBCVjl5WVlnTUp3?oc=5 |  |
| tax | womannews.net | 국회예산정책처, 2026년 세법개정안 토론회 개최 - 여성종합뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9oZG1XLVJaV3F3bEhYNlZNWnluMDJQZmRKRjJjby1fM1ZDdW5DUFZpWHFKeXIzX0wtdGpKSzAzbDZzTlRfUldJeV9FcHdJQzlHRGl1ak15R3l0QQ?oc=5 |  |
| tax | womannews.net | 국회예산정책처, 2026년 세법개정안 토론회 개최 - 여성종합뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBWNEhGdVdNam1MdkRRbzVmaE0zZ2F6eWRhYjBwOG1jYzdhQUJyNnFNUWZSRE9kOXBhQ1NzZ0tQNkF1bk1sLVVBWFlSTElIX3p2NzBZRHRITWNZQQ?oc=5 |  |
| tax | press24.co.kr | 국회예산정책처, 2026년 세법개정안 토론회 개최 - press24.co.kr | https://news.google.com/rss/articles/CBMiZkFVX3lxTE52S3FvcTZXUHh0OWRSamVwa3dncEREakFMNVY0dkxmUW1DT0ZDVWFIRDB3RzAtRHV4elVFM0cyc3hqT09KbjExZGRibXRma3JtdHJPYzNqYXZpeFZMOE5nR0VpVVRiUQ?oc=5 |  |
| tax | christiandaily.co.kr | 샬롬나비, 세법 시행령 개정에 “해외 선교비 과세 우려” - 기독일보 | https://news.google.com/rss/articles/CBMiV0FVX3lxTE5rYk12WWY2QzY2SktqY0s4UDYwTnc4azhpcXBpRDhienBKS1E3Zkprc2VwUklIal9pRGRKcW1CdmRSLU5BTUE2UmdFUjYwYjlHbVo0VWhBWdIBXEFVX3lxTE1QNE5tWFA0cWJLaEdOa19PbzVFNDQ0ejhuTzdXLUdWVTlaSm9YejZtV0hJb0E5ZkdBeEY5TC1QN2ozOE1YRFhWdjJUMUxGMll2WVpLV0cwcWNFSWZi?oc=5 |  |
| tax | paxmedicalnews.com | 2026 세법개정안에 병원계 ‘발끈’… “가업상속공제 제외는 필수의료 사형선고” - 팍스메디컬뉴스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1Dd3lHSEFoSWkzMDJXZVAwcnpDVjkyLXJYa0gwVURLSWJjeGhfTVZnV2pnVTZfdWdqTU1sZU9wM093UDhoT2dmUDdtVThCc3o3VlZEY3lVbzFuQTZCX3N6bHlvSDhrekpTdFFKcWpId3A?oc=5 |  |
| tax | sportsseoul.com | 국회예산정책처, ‘2026년 세법개정안 토론회’ 성료 - 스포츠서울 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAxY2luMmRVY3NUUEZNdkVZQzVPUURuSXZYRW1uU3EtLTFRcXRDUGp6WTgxX0o2NzNaamducGdHbENLYlY4bU1iOUZHNThXUnNaMGMtNHU1S2U?oc=5 |  |
| tax | 매일경제 | 2026년 세법개정안 토론회 - 매일경제 | https://news.google.com/rss/articles/CBMiRkFVX3lxTE1OZjRDYkM3MUdVUExlMzRxZkZxM1VzTG41TDR6MXQ0ZDNBZHYtaGRBRGdOMFdQeV9MenRxWHFkSUxTMWpVMEE?oc=5 |  |
| tax | sejungilbo.com | [판세] 구 소득세법 17조의 '잉여금', 기업회계와 세무조정 중 어느쪽 잉... | https://www.sejungilbo.com/news/articleView.html?idxno=60676 |  |
| tax | 조세일보 | 세법개정, 소득재분배 효과…부동산은 복잡 [토론회] | http://www.joseilbo.com/news/news_read.php?uid=579256&class=7&grp= |  |
| tax | 일간NTN | [판례평석] 구 상증세법 시행규칙 제17조의3 제1항 각 호의 사유가 있으... | http://www.intn.co.kr/news/articleView.html?idxno=2054518 |  |
| tax | newsis.com | 국힘 "정부 부동산 세제개편안 전면 철회해야…정부·여당 엇박자로 시... | https://www.newsis.com/view/NISX20261111_0003863289 |  |
| tax | 서울경제 | 종부세 당정 엇박자에…野 “표 계산 따른 땜질, 세제개편안 전면 재검... | https://www.sedaily.com/article/20112807?ref=naver |  |
| tax | newsis.com | 與, 당 싱크탱크 산하 '부동산 대책 TF' 구성…세제 개편안 등 논의 | https://www.newsis.com/view/NISX20261111_0003863163 |  |
| tax | 서울경제 | 與 마음 급해졌다... 종부세 이어 줄줄이 감세 법안 발의 | https://www.sedaily.com/article/20112523?ref=naver |  |
| tax | 머니투데이 | 눈높이 못 맞추는 정부…자본시장 세제 개편안 연이은 '헛발' | https://www.mt.co.kr/economy/2026/11/11/2026111011285966844 |  |
| tax | news1.kr | 총선 앞 '종부세 완화' 꺼낸 與…靑과 부동산 세제 개편 갈등 2R(종합) | https://www.news1.kr/politics/assembly/6349655 |  |
| tax | viva100.com | 이형일 부총리, 부동산세제 개편 “거주 주택 우대 원칙 반드시 유지돼... | https://www.viva100.com/article/20261110501347 |  |
| tax | news1.kr | 이형일 "부동산세제 개편 핵심은 거주 중심 주택시장 정착" | https://www.news1.kr/economy/trend/6349653 |  |
| tax | dkilbo.com | 與 부동산 세제 개편 내부 반발에…국힘 "집값 못 잡고 세금만 올리더니... | https://www.dkilbo.com/news/articleView.html?idxno=560282 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

