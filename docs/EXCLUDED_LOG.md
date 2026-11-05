# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-05 10:56:55 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1668건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 17 |
| excluded:company_event | 2 |
| excluded:company_self_activity | 3 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 29 |
| excluded:financial | 1 |
| excluded:industry_specific | 7 |
| excluded:local_gov_petition | 1 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 48 |
| excluded:no_regulatory_signal | 39 |
| excluded:opinion_piece | 1 |
| excluded:similar_news_merged | 16 |
| excluded:smb_only | 1 |
| collect:event_announcement | 7 |
| collect:incident | 1 |
| collect:law_name_mismatch | 5 |
| collect:no_category | 25 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 205 |
| collect:out_of_window | 30 |
| collect:tax_subject | 40 |

## excluded:category_cap (17건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | [단독] 지속가능성 공시 로드맵 내년 1월 발표 계획 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5wNV9rc2dQMTJKQTVLcnpSbmY2R21OYjRuUzBCSjU4YnNVbGdJMUtsRm53NGlKYVZ5bXg0a05wbmlfYnJzT29UR3R3N2JHaHMxQ1ktdmVxTk5rLXBIWUdDeHJ0bW9oU0haUkliQw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성 공시 제도 로드맵 초안 및 확정 공시기준 주요 내용 - PwC | https://news.google.com/rss/articles/CBMif0FVX3lxTE1Gd29wMWxoczQwX09wRThxRzhCam43V3VTRHp6LWFzQWgyZUdjeTF5dzJBZUJoYnlLZFdYWEZlbWVmRDNEcHM5eGVpTGhPSThiUEtkNlpBTlVVb2laR1FlSnlCa2ZBeG5uWFFvaHNfdG9LeExxeFRLc1ltdXgzcmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 의무화 시대, '데이터'가 수익률 가른다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ETFBnRTJ0eEttX3pfeU9UeE9CSHl0UnQzX3lhenlxVWllRGVQUnV4RDZLZ3BZTzg2WlNTLXNUSHJoWTl1eUl1NjBYd2pPVnc3SzhuTXlNaGZUdw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 2028년 대기업부터 시작…스코프3는 3년 유예 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB0NEtXNnFZdGJLd01zRG5XaGUtZ1RyX1hFMTB2REQ5VlVJRkZzdVFJODBNVHdqTlhBZzZtQnZtM1N2dXhtc2tma3pMaEMzX3N1cjFjOVl3RE91Sjl6Rm9zV251UDBQYUo5NWtXMNIBcEFVX3lxTE1jYVpBZ1NRcDNjb0ZpaGh3Q09TZFpINmN2b3BxbTJMaGpJeVVqQ1loMHhkRjJYZkp2ZjVkTEN4R0FWM0lrcWtsSUphSW4wUHZ0MWw3ekgwb3JZeE5hcmNfUXE0VkxUcXhWOFdsYXlZVmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | yna.co.kr | 국내 대형 상장사 "ESG 공시 의무화 대비하고 있지만 일부 부담" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yZUdEcHdYT2V3Tk1jbEs1aTVwdmc1TUZhbzA3MmpJVXlHQXRCeEFVclI3YW95am5UNTU2d29fZTA3ZGZ1NElDU2o3dWhHYTVzcTd4LUs4bi00cnPSAWBBVV95cUxNWlJkdmlVWkFDR0czQlVSYlZ2c2VFdjZxOXcxQ0ZoeW5tNFllTEhzX0pVTG94UXJwemFHRnVWODBRZXZWTUlGOVZUNHNkODdKOTdxZ0NlZWlKdnFvOVpib3Q?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | womaneconomy.co.kr | ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 | https://www.womaneconomy.co.kr/news/articleView.html?idxno=259937 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | kr.investing.com | 드리븐 브랜즈, 실적 발표 연기·재무제표 재작성 발표 - Investing.com 한국어 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBhX2VwTUpSX2pIVHRXSnlocUtWSEZJVkIwODRPcEkyRjBRcno3a2lWOWZxaVFNYkN2VnRFVG5zTFBvWjd4Z01rRElmcW5feE1CeG1MUjh6V0pKSjVuWGJhYTAwZXl0SlhBdlFHdjZyb24?oc=5 |  |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 |  |

## excluded:company_self_activity (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | 泰, ISSB 지속가능성 공시 의무화 확정…28년 SET50부터 단계적 시행 | https://www.esgeconomy.com/news/articleView.html?idxno=17232 |  |
| esg | thepowernews.co.kr | KCC글라스, 생물다양성·해외사업장 ESG 공시 강화…여섯 번째 보고서 발... | https://www.thepowernews.co.kr/view.php?ud=20261104103704860de3f0aa1be_7 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |

## excluded:corporate_pr (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | asiae.co.kr | 중대 보안 취약점 방치 땐 CEO 책임…금융당국, 금융사 내부통제 강화 추진 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wVHBFeHhiNjhDb1pVRzYwbXFYTmRrZmhpOFNWS0laVUNkeGZ4NUdGQVY2eGJBWmdlRHJ6SFFsaEM5bW5RQ0FyazRqY0tUWmhnRHJYVjdLSUZwUjJRd2Y3TQ?oc=5 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (29건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |
| tax | 재정경제부 | 소득세법 시행령 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88010 |  |
| kifrs | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| esg | thepowernews.co.kr | ESG 공시 291곳→1년 뒤 3171곳…대기업 넘어 협력사까지 ‘데이터 전쟁... | https://www.thepowernews.co.kr/view.php?ud=202610221509381568de3f0aa1be_7 |  |
| esg | ESG경제 | "ESG 공시 강화에 중견기업·협력사 부담 가중…대응 격차 우려" | https://www.esgeconomy.com/news/articleView.html?idxno=17072 |  |
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
| esg | tfmedia.co.kr | [KAI 세미나] 주성호 KSSB실장 “KSSB 파일럿 테스트 연말까지…일관적 ... | https://www.tfmedia.co.kr/news/article.html?no=206990 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 권오규 전 부총리 ‘AI‧녹색 전환엔 금융지원 필요…KSSB는... | https://www.tfmedia.co.kr/news/article.html?no=206988 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |
| esg | 임팩트온 | ESG 공시 규제 후퇴 vs. 월가는 기후데이터기업 인수 경쟁 | https://www.impacton.net/news/articleView.html?idxno=30224 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |

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

## excluded:news_too_old (48건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | investchosun.com | 삼성생명 몰아붙인 회계기준원…2분기 결산 고민 깊어졌다 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPZWdwcnZLaWNBaTl1c3BFRlZyaG9NR0M5eFZRQzBYb0JBeVRIeWQzODI4VUJQbWlKNWdtX2hlWW56WUd0TEwxWjM2ZnlNWHZIYTFSUHNrUmFidUhOVUhDWU5OTVN6c2tCZ09IZVBZYXdzSEZBaTByVGFRTG9tQ1k3MmxtSQ?oc=5 |  |
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| kifrs | dbr.donga.com | 종속-관계기업 구분하는 지배력 기준 논란 - 동아비즈니스리뷰 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9ZeE1sREktWEhLSjVXQ1VzWTFPNFZad0lxdjVHYWF1aEtrT0YxZ1ltZFhES0EyZWlCcTllNHZBZDJXY3JEVXB5NFlCSlVUWnFMNlFtQVVHdnlSRlVCT0lzS1dIVGl2LWs?oc=5 |  |
| kifrs | 일간NTN | “회계기준 질의회신 결과로 재무제표 재작성하면 처벌 예외규정 고려해야” - www.intn.co.kr | https://news.google.com/rss/articles/CBMiakFVX3lxTE8yV2NfWjFmYjY2OXVvS09YeVVycWo0QlZXQ1VWTW9zbGlMbXBGRmJCNXp2MnJzdTQ4bXFKblVoblhVaHhkTnR2bXQwdy10M3RzcDBQUWNZdmJMOFpBSzVXeDVRUEF2Q3d3RXc?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1001호 ‘재무제표 표시’ 개정 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5CTE82SldnUm1UUEtiTVpXeGxFdHdqbEFHQVk3dGF0WFh5YkdzRW9xLWJFOU5RamNEdXhFWGRmNVQzb0txb3JDcXFzdktmWGRzRXoxOFB1YXU?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | 조세일보 | 김현정 "尹 정부, 3년간 신외감법 무력화" - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JdDQ0dDRwdlpDdGhzcnpHZ3hhZ3V3OXFqbXplRXJ5SlFFeU5VWXhlZHg1clRpNHVfQ3B6YXB2RDZBR21GSWlzVnJ4RnY3NDRpaURGVVBBTW5UWWtzQnd3?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | newspim.com | '신외감법 도입' 회계사 인력난 가속도...시간제 고용도 나와 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9jN0V1bGFpbDFpcGJOcTRFR0JOR0lCT0ZKUy0yS21MQ1NQYVUwbHY0RWFKRUs4M0cwUVJsZEhuR2tGUjlLUlBDeU4zRjlWRFhpUjg5Ukc0VGY5UzNX?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | 일간NTN | 우리회계법인 공인회계사 외감법 위반 감사업무제한 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1KdDNUR3BQVVl1dGtYZ2prUllIQVhuOHVKYXdKcW4xbmUxQk5LaExyeXFyMnp5ZTZSTG5TN0RENEp5NEJWeHRNSlVjRjEyMDNsc0x3Q0NRNEZrSDBuejVxNXczOHd3RHA4VWc?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | lawtimes.co.kr | 구 외감법 상 ‘회계처리기준’이 구성요건이 될 수 있는지 여부 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9mQkQ0MVloUTljd2UzOXI3QnZfVFA2ZUJaYTlEa3NfLWNHa0ZYVUxHZ0hUMHkyeDFIWmdZV2VtaFM3TDVpYUZwR1A1R1JweFJQUWJFOTU4VFF5WnUtdmtmU0JuWnNUQ3dYc0ctbGdR0gFyQVVfeXFMTWtxblhPLWdZc3p5VU1QdmZhczA5aHVlRHZPOS1fZXBsYUFvWGNRNG9naXhhRXlOdjY5c0RPbmNLWHpQMFJWcmlab2piTXJ1VVZRNDJ3SlpYLTlydjNXX195WmNkTnYwZUNzYm15aWFOYU5B?oc=5 |  |
| icfr | view.asiae.co.kr | 금감원, PB업무 내부통제 모범규준 시행 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFByWmtmZUtmVmM4XzBSZGp1d0ZlRHhSSmk1U3JZSVVvQ0pPaU9Ca2FFeUI3aUxEdXpjREozMTJNVUVFVFdZUTRvVjBBNzExbUJYWmVYZnM1Z05NVHl4ZmZfcnpB?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |

## excluded:no_regulatory_signal (39건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1MWmtQakwyaG5XUW92Vk9OUGdQaWpYbFI4N2ZGNG9DNko2V01IRVo0RTM1bUkwcUIwc1MtNGMzZFFlTG96Zmpoc2hDc1VKYlFETHQ3b1Q3cWJ6ZjVZdXh1Tl9kVUE5blRvOUE?oc=5 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | newstomato.com | 보험사 ESG 공시 늘었지만…비교는 '깜깜' | http://www.newstomato.com/ReadNews.aspx?no=1318745&inflow=N |  |
| esg | dt.co.kr | KCC글라스, ESG 공시 범위 해외로 넓혔다…생물다양성 영향도 공개 | https://www.dt.co.kr/article/12093213?ref=naver |  |
| esg | finomy.com | KCC글라스, ESG 공시 확대···인니 법인 성과 첫 공개 | http://www.finomy.com/news/articleView.html?idxno=265631 |  |
| esg | news1.kr | KCC글라스, ESG 공시 범위 확대…자연자본·해외 사업장 담아 | https://www.news1.kr/industry/general-industry/6342251 |  |
| esg | worklaw.co.kr | ESG 공시, 직원 성장 이끄는 장치가 돼야 | http://www.worklaw.co.kr/view/view.asp?accessSite=Naver&accessMethod=Search&accessMenu=News&in_cate=101&in_cate2=0&gopage=1&bi_pidx=39682 |  |
| esg | asiatime.co.kr | [윤영민 칼럼] ESG 공시 시대, 보여주기식 경영의 종말 | https://www.asiatime.co.kr/article/20261023500342 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | CPA뉴스 | [강의 소개] 전·당기 감사인 간 의견불일치 조정 협의회 사례 해설 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9LUEVCLXJEYk01eDM5b0FFV043WXFLOVJtekIyb3ZIdHI1c2VsZGtWV29tNXBtNFZGM3Rha2pETDl1TGhpX2RJOGZodmlIMjUtRzFRNVZabUdCdXZVSnE1MmZHSXZweElw?oc=5 |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 매일경제 | “잘 나가던 ‘K뷰티 공룡’ 에이피알, 환율에 발목”…목표가↓ - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE1HM2t2VVRDRHVjTHZGYXVlY256bjFMb0RMcE9GX3VvSWlXQTFkSkk2TGFxbWVuaFRfcEpzMEx2U2VSLVlRZzZ3T3VvbFFLWDFIYlE?oc=5 |  |
| kifrs | 한국경제 | 상장사 ‘숨은 땅값’ 공개된다…자산주 재평가 기대 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9JLTM3blBCSXYxQ2VjXy03dGZpbDR1RG1HbkF1YVQ4ZEtqSG1BSVJiMExSSEM0OGpvSjEwVUFaSWdqa3p6a3c5WS1KU0tHYlAtQXFzTl9lUS0zdw?oc=5 |  |
| kifrs | datatooza.com | 웨스트레이크 케미컬 파트너스, 모회사 특수관계자 원가 공시 누락분 정정…재무제표 영향은 없어 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE93WUdEeThtRzMwMF9obHhuQnlwMW1OQmNpOTAydndNNTR0eGdkSWs0OHZkWUpXRGtET0RhVlE2WGliWTIwMklLeTduWmt5d1cyV2JTdkxYWGdUYVhIalQ3UXZ1UFM0QVVsbDBNb1QyRkpQTnc?oc=5 |  |
| kifrs | datatooza.com | CVR 에너지, 인수 예정 마라톤 정유 사업부 감사 재무제표 공시 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE40U3BmZ2lvbE9ZMHV6Y201eEd3XzJXUlBXVkwxZjNpM3R3VjhEc1J5ZlhVQmluQ2ZubkRsNmgxQUVEQTR0LS1DejJrdUd6SUZuQlQ0dTNubXlUa3FFTmJpRzJWMFlxSGl3NF95YXNEcEwzLUU?oc=5 |  |
| kifrs | datatooza.com | UDR, 3분기 영업이익 2억 7019만 달러로 254% 증가…아폴로 합작사 회계 처리·수익 배분 구조 공개 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE50TXlRZzc0MjFROUt4eUE5QVN3eFZVWVllOWVCYndWRWJucW5zaUxzcFJhOVF3Sm5yVm5iV0RoSVdRRFVxNTRocTVrYTFFMzJFWXBqNGYwdDdQN0RLeDFRd1YwTThuQWJ1MGprcWxNX2lDZw?oc=5 |  |
| kifrs | livebiz.today | [K-자동차 밸류업 체크] 현대차 125조 원 비전...무시할 수 없는 재무제표의 경고 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBZOHpTbGpYNTNZeHZ1YUtiX3RkYm5oSFJHOW9tRlI3MXlRYXZQa0ZhTnNmLXR5RVVkbG9hX0Fjc3NwU1hhYl83WmxwUU85cENEMzFUNGNGVEF1blRHNS1qV3BWaWRKOEhFMmFJcA?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| kifrs | livesnews.com | 김원국 하이브미디어코프, 83억 회계오류에 특수관계자 대여 17.7억…2027년 IPO '빨간불' - livesnews.com | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBqYjJKM0hxQUZPS3owQ0lSelc0SnhSb2dQZGhXNWxoNUNxSHhGVmtLLVdXb1lVQmxwSmtBLTFxcU1rdVItZ0V1WE9CQ1NmMkZzUVBYaTdva3FidzUt?oc=5 |  |
| kifrs | hdnews.co.kr | 고려아연, 3분기 영업이익 2243억…전 분기보다 61.9% 급감 - 현대경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5CY2NOeE5UTGhuMklvLVY0RnVCNUhxMmpVY3FKUy1POGItYUs2RnJra3J5ZWNFdzZielBLODktOG5qQ3hJMzByQW5oekJ3NXJvZmJpckRVUDhuQWRfRmh1UDJPUGQxMEg0amxV?oc=5 |  |
| kifrs | digitaltoday.co.kr | 에스엠, 2026년 3분기 순이익 110억7000만원…전년 동기 대비 65.7% 감소 - 디지털투데이 | https://news.google.com/rss/articles/CBMie0FVX3lxTFBNSmJCU19QT2F4eTNsMHA3c1dBVVZINGNoNUk3T3QzRWZ2T0x6WG5vYUhtamd3NW9UUFRRV3JfeXNTN3g2UDZLNmY5aE5EbjI5V0FEV0ltbnpfWmgtYVRzdTBDT0dMVzBBSTdaSGwzdm4zc1pPdXY5NG51UQ?oc=5 |  |
| tax | 한국경제 | 경기도 재정난, 국회서 지방세제 개편 요구 | https://www.hankyung.com/article/202611044774h |  |
| tax | weeklytoday.com | [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... | http://www.weeklytoday.com/news/articleView.html?idxno=800450 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| icfr | datatooza.com | 인터내셔널 페이퍼, 내부통제 '중대한 취약점' 공개…미 법무부 골판지 가격 조사 소환장도 받아 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTFBfdzBCVmNOaUNUdG1xVEtINDhURGVWYUhoZGttNk14c3V3dXNmS3FYZTlyUWZyUFo3Nmp5UXNsdUJlTFJTTEhBdVgzLTZYaS1uY042ekNBV3U5T1NkX0N2dERPYlV6Wkt0UWZ0SGYzZkJucG8?oc=5 |  |
| icfr | insjournal.co.kr | GA 검사 대응, 정도영업이 답이다③ "서류만 갖춰선 부족하다"… '상시 내부통제'로 취약점부터 잡아야 - 보험저널 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1wNE1tMXlPTk1hQXNhbzcxdm1CbkFKbHBnNzk3VGRKc3FwX1c0cU1seVVWNmlKMVA0Uzl2dGR0cllJSHZpa2w4a3hpT0Z0TzhKby0yUm9OaUtieC03aGlnU2M1WXp1NmdVdGJzNnNfTQ?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:similar_news_merged (16건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 | https://www.impacton.net/news/articleView.html?idxno=30527 | → 대표: 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 - 임팩트온 |
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| esg | joongangenews.com | KCC글라스, 생물다양성 영향까지 공개…해외 법인 ESG 공시 확대 | https://www.joongangenews.com/news/articleView.html?idxno=561023 | → 대표: KCC글라스, ESG 공시 범위 해외로 넓혔다…생물다양성 영향도 공개 |
| esg | biz.heraldcorp.com | KCC글라스, ESG 공시 해외로 확대…인도네시아 법인 성과 첫 공개 | https://biz.heraldcorp.com/article/10924977?ref=naver | → 대표: KCC글라스, ESG 공시 범위 해외로 넓혔다…생물다양성 영향도 공개 |
| esg | paxetv.com | 상장협, ESG 공시 실무교육 실시…2028년 의무화 대비 지원 | http://www.paxetv.com/news/articleView.html?idxno=284514 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | enewstoday.co.kr | 상장협, 'ESG 공시담당자 실무 쟁점' 과정 개설 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2481878 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | dailian.co.kr | "차질 없는 대응 지원"…상장협, ESG 공시 핵심실무 쟁점 대비 | https://www.dailian.co.kr/news/view/1703168/?sc=Naver | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| kifrs | datatooza.com | 드리븐 브랜즈, 유형자산 회계 오류로 재무제표 또 재작성…3분기 보고서 제출 지연 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9kMHZnMUViSlVyZXk1N2RPTFI4SFJqY3l6SXJTcW10dWFfR2oxelAyVTFScno4Z1J1NDM2WlRCVXJkXzVudk5XZU90VFl6a1NfSHdsQWh2bWFCcWdoZEdzM2hfV0lYaG8xTTR5MXJ1Z0VTM28?oc=5 | → 대표: 드리븐 브랜즈, 실적 발표 연기·재무제표 재작성 발표 - Investing.com 한국어 |
| kifrs | carmgz.kr | 폴스타, 3분기 실적 발표 돌연 연기…회계 내부통제 문제 재조명 - 카매거진 CAR MAGAZINE | https://news.google.com/rss/articles/CBMiZkFVX3lxTE9yd29LbTc4QUFaMnBWZWdVNFpzNng4OUcwUmdKRGdVOFRPNm5PN0hVdjgwMVdqYV9XMGZULWN0NXdxOGQ4VWtHRlZ6OUx1QUtMdi1LX1VoMGdNWnlLSGZjSzhmR1NKdw?oc=5 | → 대표: 드리븐 브랜즈, 실적 발표 연기·재무제표 재작성 발표 - Investing.com 한국어 |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 |
| tax | segye.com | “지방세제 개편·민생정책 총력 홍보”…경기도, 국회 입법박람회 출격 | https://www.segye.com/newsView/20261105506954?OutUrl=naver | → 대표: 경기도 재정난, 국회서 지방세제 개편 요구 |
| tax | kgnews.co.kr | 경기도 지방세제 개편 6개 법안 발의…‘14조 확충’ 기대 현실화될까 | https://www.kgnews.co.kr/news/article.html?no=918123 | → 대표: 경기도 재정난, 국회서 지방세제 개편 요구 |
| tax | asiatoday.co.kr | “지방세제 개편·체감형 민생정책 입법화”…경기도, 국회 입법박람회... | https://www.asiatoday.co.kr/kn/view.php?key=20261104010001432 | → 대표: 경기도 재정난, 국회서 지방세제 개편 요구 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## collect:event_announcement (7건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | 2026년 글로벌 ESG 교육 워크숍 안내 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2199 |  |
|  | 금융위원회 | 생산적 금융의 온기를 지방과 중소기업까지 이어갑니다.   - 이억원 금융위원장, 제6차 생산적 금융 대전환 회의 개최 | https://www.fsc.go.kr/no010101/88052?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| esg | betanews.net | 네이버, ‘2026 지속가능경영유공 정부포상’ 대통령 표창 수상 | https://www.betanews.net/article/view/beta202610300070 |  |
| esg | ESG경제 | [알림] KSSB·ESRS 이중중대성 평가 웨비나 초청 | https://www.esgeconomy.com/news/articleView.html?idxno=17019 |  |
| esg | news.tf.co.kr | 동아ST 지속가능경영보고서, '2025 LACP 비전 어워즈' 수상 | https://news.tf.co.kr/read/economy/2361168.htm |  |

## collect:incident (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 한국경제 | 외감법은 경찰, 자본법은 중수청…분식회계 수사 차질 불가피 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wOF91b3FKNTlVV3FUM3J2amdHek9VS29CTHZ1N3d3NFJiOWtOakNkRVRPSzhFd3ZKMHM3RkRmcW9QeE9hRFV4NHNhbmQ5Q0RSNUpIbEYyOG9zUQ?oc=5 |  |

## collect:law_name_mismatch (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 법제처 | 지방교부세법 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방교부세법 시행령 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방교부세법 시행규칙 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방세특례제한법 시행령 (검색어 '지방세특례제한법') |  |  |
| tax | 법제처 | 지방세특례제한법 시행규칙 (검색어 '지방세특례제한법') |  |  |

## collect:no_category (25건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 허장 차관, 방글라데시 차우두리 재무장관 면담 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079853&menuNo=4010100 |  |
|  | 재정경제부 | 국제 신용평가사 Fitch, 한국 연례협의 실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079837&menuNo=4010100 |  |
|  | 재정경제부 | '26.10월 소비자물가 동향 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079839&menuNo=4010100 |  |
|  | 재정경제부 | 물가관계차관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079838&menuNo=4010100 |  |
|  | 재정경제부 | 「의료데이터의 안전한 학습·검증·활용을 위한 국가 AI 인프라 구축」 포럼 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079836&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 미셸 박 스틸 주한미국대사 접견 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079826&menuNo=4010100 |  |
|  | 재정경제부 | 전기차 산업 경쟁력 강화를 위한 현장방문 및 업계 간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079830&menuNo=4010100 |  |
|  | 재정경제부 | [보도자료] 국제통화기금(IMF) 2026년 한국 연례협의 실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079829&menuNo=4010100 |  |
|  | 재정경제부 | 경제현안간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079820&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「주요 국책과제 이행점검」 TF 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079811&menuNo=4010100 |  |
|  | 금융위원회 | AI시대, 거세지는 침해위협에 맞서 全 금융권이 튼튼한 보안체계로 무장하도록 혁신적인 정책과제를 적극 추진하겠습니다.. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88086?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ｢“취재정보로 매매해 ○○억 부당이득”···○○신문 조사 마무리｣ 보도 관련. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88085?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 한국, 아시아지배구조협회(ACGA)    기업지배구조 순위 역대급 ‘5위’ 달성 | https://www.fsc.go.kr/no010101/88084?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 홍콩 H지수 ELS 관련 은행·증권사 검사 결과 조치 - 제19차 금융위원회(11.4.) 의결 | https://www.fsc.go.kr/no010101/88082?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 계리가정보고서 도입 등  ｢보험업감독규정｣ 개정안 금융위원회 의결 | https://www.fsc.go.kr/no010101/88081?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 2027년 금융위원회 예산안에 대해  자세히 설명드립니다. | https://www.fsc.go.kr/no010101/88074?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 코너스톤투자자 제도 등 도입 관련  자본시장법 시행령 개정안 국무회의 의결 | https://www.fsc.go.kr/no010101/88071?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 글로벌 해킹 위협에 대비한 국내 가상자산사업자의 사고대응력 제고를 위해 긴밀하고 신속하게  대응해 나가겠습니다. | https://www.fsc.go.kr/no010101/88054?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융정보분석원, 국제자금세탁방지기구(FATF) 총회 참석 | https://www.fsc.go.kr/no010101/88048?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | AI시대, 거세지는 침해위협에 맞서 全 금융권이 튼튼한 보안체계로 무장하도록 혁신적인 정책과제를 적극 추진하겠습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788025&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | ｢"취재정보로 매매해 ○○억 부당이득"···○○신문 조사 마무리｣ 보도 관련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788022&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 홍콩 H지수 ELS 관련 은행·증권사 검사 결과 조치 - 제19차 금융위원회(11.4.) 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787946&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 한국, 아시아지배구조협회(ACGA)    기업지배구조 순위 역대급 '5위' 달성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787970&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 계리가정보고서 도입 등  ｢보험업감독규정｣ 개정안 금융위원회 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787941&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국세청) | 주식 양도소득 기본공제 누락분, 국세청이 먼저 찾아 돌려드립니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787734&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |

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

## collect:out_of_scope (205건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | [공지사항] ISSB 자연 관련 공시 실무서 공개초안 요약자료(Snapshot) 국문본, ISSB 아웃리치 세션 및 국내 의견수렴 일정 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(5차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 본인 인증 서비스 일시 점검 안내(2026. 10. 17.(토) 21:00 ~ 2026. 10. 18.(일) 05:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [한국회계기준원] 2026년 하반기 추가채용(연구직-회계기준 연구원) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [KARI REPORT] IFRS 16 도입 이후 리스 기반 영업구조 하방위험 가시화와 정보적 함의 : 사용권자산 손상차손을 중심으로 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [세미나] IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/calViewA.do?seq=1129 |  |
|  | 한국회계기준원 | [세미나] 회계기준원-환경산업기술원, 지속가능성 공시기준 이행지원 세미나 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1127 |  |
|  | 한국회계기준원 | [세미나] 한국회계기준원 개원 27주년 세미나: 지속가능성 공시, 새로운 기준의 시대 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1125 |  |
|  | 정책브리핑(고용노동부) | 명장의 손끝에서 도제학생의 꿈이 자란다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788046&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 사회적기업의 성과와 새로운 도전, '밸류업 데이'에서 만나다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788045&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 오송역에서 국회세종의사당까지, 버스 한 번에… 간선급행버스(BRT)로 달린다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788043&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산으로 키운 지역 새싹기업, 투자유치로 잇는다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788044&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 국가 지식재산 정책 이끌 제8기 전문위원회 공식 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788042&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | K-미용의 세계 1위 도약, 지식재산이 뒷받침한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788041&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 경주 소나무재선충병  방제전략 마련 현장협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788039&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 2025년 호스피스 신규 이용 환자 26,020명으로 전년 대비 1,662명 증가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788040&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 11월 '이달의 임업인'에 강원 정선에서 마가목을 재배하는 이정수 임업인 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788037&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 현장의 아이디어와 AI로 임업직불 행정 혁신 속도 낸다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788035&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동화를 정원으로 펼친 청년들!  2026 정원드림프로젝트 우수정원 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788032&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 기술환경 변화 등을 알기 쉽게 반영한 안전조치 안내서 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788033&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 6.25참전유공자들 미8군사령부 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788024&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | '통신분쟁 급증' 이용자 피해구제 강화 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788027&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 산불 통합지휘본부 훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788030&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | '전국 병원체 감시기관 한자리에 모인다' 감염병 대응 성과와 개선 방안 논의(11.5.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788021&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 방산기업과 원가제도 발전방향 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788018&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 국내복귀 포럼,  기업과 지역을 잇는 투자유치 플랫폼으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788017&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산불 대응! 과학과 현장의 연결로 강화한다 - 국립산림과학원, 가을철 산불조심기간 맞아 제4회 미래산림포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788020&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(조달청) | AI로 구매실례 검색부터 견적 요청까지 예정가격 작성 더 쉽고 빨라진다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788016&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 유진이엔티㈜에 대한 ㈜와이티엔 최다액 출자자 변경승인 청문일시 통지는 청문 주재자의 독립적인 결정입니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788014&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 고위험군 소아·영유아 코로나19 국가예방접종 시작 안내(11.5.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788013&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "영구임대주택 임차인의 권익 보호는 현재 진행 중"… 이번에는 여수로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788012&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "종이헌혈증 대신 모바일헌혈증으로"…  대국민 설문조사 통해 '국민제안'으로 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788011&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 산·학·관 협력으로 임상시험 통계 전문성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788010&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 신임 국립장애인도서관 관장에 전영환 씨 임명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788009&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 민관이 함께 '케이-콘텐츠' 해외 침해 대응 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788008&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한-아세안, '문화 지식재산'으로 지속 가능한 문화협력 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788007&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 양산국유림관리소, 대학RCY 및 교촌과 함께하는 '촌스러버 프로젝트' 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788006&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 「한지 제작의 전통 지식과 기술 및 문화적 실천」 유네스코 무형유산위원회 평가에서 '등재 권고' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788003&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 2026년 소방공무원 승진시험 11월 7일 전국 동시 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788002&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "소방의 날도, 현장 안전도 일구와 함께!" 소방청, 카카오톡 그림말(이모티콘) 6일 배포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788001&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 고속철도 통합 60일, 하루 32.2만 명 이용 … 예매·객실 서비스 개선 이어간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787999&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한중일 환경과학원장 한자리에, 동북아 환경협력 강화한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788000&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 내년도 공직적격성평가·국가공무원 시험 일정 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787998&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 2026년 메콩 지역 공관장회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787997&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 경기 연천군 고병원성 조류인플루엔자 발생 관련 긴급지시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787995&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | OECD 가입 30주년, 한국경제의  새로운 도약을 위한 성장전략 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787996&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청, '해양안전'과 '민생보호'를 위한 특별단속으로 1,489명 단속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787969&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 경기 연천 산란계 농장에서 고병원성 조류인플루엔자(AI) 첫 발생에 따라 전국 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787972&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, QR코드를 활용한 안전보건교육 진행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787968&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '27년 농어촌 기본소득 시범사업 신규 공모에 34개 군 신청 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787966&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(병무청) | "극장에서 만난 청춘들의 병역이야기" 병무청, '2026 청춘예찬 영화제' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787965&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국민통합위원회) | 통합위, 제22차 전체회의 개최…국민통합 국민제안 도출 및 제도적 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787963&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 남재헌 해수부 차관, 부산국제수산엑스포에서 수산식품 수출 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787964&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 모두의 일상에 더 가까이, 모두의 삶이 더 든든히! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787962&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부, 티메프 피해 중소기업 특별만기연장 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787961&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 가을철 산불재난대응 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787960&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동부지방산림청, '2026년 산림조사 현장교육' 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787958&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 한우농가 찾아 정보통신기술 활용 현장 살펴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787955&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 젖소 메탄 배출량, 품종별 생산 특성 함께 살펴야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787953&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | [관계부처 합동] 이 땅에 집 지을 수 있나요? 복잡한 토지개발 인허가, 인공지능(AI)으로 쉽게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787945&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 이 땅에 집 지을 수 있나요? "복잡한 인허가, 인공지능(AI)으로 쉽게" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787948&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 시장 출하 앞둔 감 '봉황' 현장 평가회, 새로운 모양·식감 주목 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787951&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 대마 기능성 성분 '칸플라빈' 생산 적합한 숙주-효소 조합 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787949&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 「제1회 로컬창업 페스타 in 제주」 개막! 지역에서 시작한 혁신, 투자·상권·수출로  이어지는 성장의 길 열어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787944&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 대테러 전담조직 저격수 역량강화 훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787943&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 우주항공청-합동참모본부 민·군 우주상황 대응 훈련(FTX) 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787939&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 국제거대전파망원경(SKA) 국제협력 확대 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787938&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | AI 시대, '대체불가 대한민국' 실현을 위한 AI 전략과 글로벌 협력 방안 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787940&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 가장 가까운 위협으로부터 국민이 안심할 수 있도록... 경찰청, 관계성 범죄 전수점검 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787937&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 「코리아 커스텀즈 위크 2026」 성공적 마무리… 수출기업 통관 장벽 낮췄다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787936&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 첫 통합돌봄 지역계획 수립 위한 중앙-지방 협력방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787928&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 디지털크리에이터, 아시아 최대 규모 라이선싱 엑스포 첫 참가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787934&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부·산업통상부, 군수 빅데이터 기반 「RAM-C AI 에이전트」 기술개발 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787932&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 호라이즌 유럽 참여 확대 넘어 전략적 공동연구 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787926&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 허장 차관, 방글라데시 차우두리 재무장관 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787933&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 「제11회 해양법 국제학술회의」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787930&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 기후부, 소속·산하기관과 인공지능 활용으로 업무혁신 함께 이룬다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787931&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 가을철 산불 예방...한라산 영실서 캠페인 실시 -국립산림과학원, 산불조심기간 맞아 한라산 탐방객 대상 산불예방 독려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787923&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제7차 한-아프리카연합(AU) 정책협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787924&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | "맛으로 잇는 세계, K-푸드로 통하다"… 「푸드위크 코리아 2026」 화려한 막 올려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787920&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 미국 스위프트(SWIFT) 우주망원경 4일 저녁 대기권 재진입 예상 한반도 영향 없어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787921&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | 국민권익위, 베트남과의  반부패 협력 관계 재확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787919&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "공사 차량으로 안전 위협받는 초등학생들"… 우회도로 개설, 교통안전 시설물 설치하기로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787918&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림, 가을철 산불예방 및 산지정화 캠페인 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787917&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 제23회 대한민국 평생학습대상 시상식 및 2026년 평생학습도시 동판 수여식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787909&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 경제협력개발기구(OECD) 가입 30주년, 한국 교육의 성과와 미래 방향 조명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787908&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 대한민국 과학기술인상 11월 수상자 이종원 단장 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787901&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 소프트웨어마이스터고등학교 세계적 인재 양성으로 4년연속 실리콘밸리 취업 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787900&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 지구촌 학생 765명, 조선왕조실록 읽고 '미래의 나'에게 기록 남긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787915&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부, 'K-주소' 첫 해외 수익형 수주... 유럽 강국 제치고 우즈베키스탄  국가주소등록부 구축 기술지원 사업 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787913&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 사회적 고립, 국민과 함께 고민하고 답을 찾는다... 제4회 '모두의 토론회' 참가자 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787911&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 8월 경제활동인구조사 비임금근로 및 비경제활동인구 부가조사 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787907&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 기후에너지환경부, 경제협력개발기구 화학·생명공학위원회 의장단으로 활동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787906&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 중소·중견기업 녹색금융 현장과 소통하고, 우수기업 성과 알린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787905&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | '녹조 예측력 향상' 위한 담수 조류 탄소량 산정기법 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787904&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.5.목.조간] 치매 연구, 새로운 단서 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787903&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K팝 추고 태권도 품새까지…킨텍스 달군 K-로봇 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787899&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 분양가의 25%로 입주하는 LH 공공분양주택, 금년 12월 고양창릉서 첫 분양 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787896&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 인공지능(AI)·드론 활용해 토지행정 혁신 … 제49회 지적세미나 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787895&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 연체 걱정 없이 세 놓으세요, 월세 부담 없는 집에서 사세요. 전월세 안심신탁 첫 임대인 모집 공고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787894&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 내항여객선의 안전 제고를 위해 선사 경영층의 인식을 개선하고 역량을 강화한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787893&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 세계 해양의 혁신 기술, '오션테크코리아'에서 국내 기업과 연결된다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787892&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 남극해 관련 국제사회에서 해양외교 노력 결실! 국제규범 제안 채택에 이어 새 어장 개척도 성공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787891&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부-경제협력개발기구-한국해양수산개발원, 세계해양포럼에서 해양경제를 논한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787890&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 안전한 항해를 위해서는 필수, 부유물 감김 사고 현황도를 확인하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787889&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 수소는 탈탄소를 이끄는 핵심수단… 제5회 수소의 날 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787898&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | AI로 진화하는 국방... 군수 AI 에이전트 개발 본격 시동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787897&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 의대 신설 지역/대학 선정 및 정원 배정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787886&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 복잡한 외자구매 간소화해 수요기관 부담 낮춰 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787888&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 의대 신설 지역/대학 선정 및 정원 배정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787884&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 계약현장과 소통하며 공공조달 개선방안 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787887&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 순국선열의 날 기념식， 한 편의 뮤지컬 서사극인 '공연형 정부기념식'으로 새롭게 선보인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787879&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기상청) | [2026년 10월 기후특성] 변동 컸던 10월, 상순 건조 → 중순 이상고온 → 하순 잦은 강수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787885&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 중국 산동행정 연수단, 조정원 방문…선진 분쟁조정 노하우 배운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787878&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 우수 임업경영체 찾아 현장중심 산림지원 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787883&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 충청북도 산불 대응 역량 강화 교육실tl | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787881&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 네이버와 중소 IT 기업, 공동으로 재취업지원서비스 시행! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787877&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 'AI(인공지능) 기반 디지털 감사 및 적극행정, 사전컨설팅 활성화'를 위한 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787876&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | '통합적 진로교육을 위한 생태계 구축' 추계학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787875&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 안전 필수템 '위험성평가'를 통해 모든 일터를 안전하게! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787874&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 희귀·중증난치질환자 건강보험 본인부담률 10% → 7% 인하 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787872&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 실물 인공지능 융합 기업의 현장 목소리 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787873&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 「지식재산과 혁신」 지식재산처 제1호 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787871&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 제33회 ｢외국인 인권보호 및 권익증진협의회｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787870&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) '바다의 경주' 태안 마도해역에서 고려 난파선 두 척(5·6호선) 발굴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787865&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 한국전통문화대학교, 전통회화전공 기획전시 「Memory: 전통과 오늘이 만나는 자리」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787862&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 5극 3특, M.AX로 여는 새로운 투자기회 ｢인베스트 코리아 서밋(IKS) 2026｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787869&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 제33회 ｢외국인 인권보호 및 권익증진협의회｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787861&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부, APEC 외교통상합동각료회의서실용적 협력과 기업친화적 통상환경 조성 강조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787868&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한-프, 통상현안 및 첨단산업·기술 협력 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787867&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | AI와 탄소소재, 첨단산업의 미래를 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787866&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부-AMD, 인공지능 반도체 협력 본격 가동... AMD 대표 인공지능 행사도 한국서 첫 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787858&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(감사원) | '지방자치단체 적극행정 권역별 간담회' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787902&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 중견기업을 세계적 기업으로 날아오르게 할 10대 초격차 기술 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787859&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '한글 점자' 탄생 100년, 「점자법」 제정 10년 만에  첫 점자 교원 20명 나와 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787856&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한글 점자 '훈맹정음' 반포 100주년 의미 되새긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787855&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식품안전나라 'AI 기반 검색'·'자주 찾는 민원'으로 쉽고 빠르게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787852&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 생성형 인공지능 시대, 저작권 기술의 미래를 논하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787854&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 덜 짜고 덜 단 식품 선택의 폭 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787851&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-폴란드, 방산·배터리·인프라 분야 실질협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787853&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "소방차량 오염관리, 현장에서 해법 찾는다" 국립소방연구원, 산업안전보건연구원과 소방차량 오염환경 공동 평가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787850&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청, 제79회 '불조심 강조의 달' 운영 국민과 함께 겨울철 화재예방 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787849&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 2026 아시아태평양경제협력체(APEC) 외교통상합동각료회의 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787847&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 전국 동물원 질병관리 실무자 한자리에 모여 선진 관리 체계 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787848&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부 장관, 배추 등 가격 하락 김장채소류 실질적 소비촉진 대책 추진 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787857&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국민인공지능서비스혁신추진단, 전문임기제공무원 2차 공개 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787846&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 청년들의 창의적 아이디어로  합성생물학의 미래를 열다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787845&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 최휘영 장관, 전북도지사 만나 '2036 하계올림픽' 유치 현안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787813&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 응급실 등 필수의료분야 수사 가이드라인 마련 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787811&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제7차 한-스위스 정책협의회 개최(11.3.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787812&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 상습체불사업주 777명,  1년간 신용제재 받는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787810&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 정부, 여수·순천 10·19사건 희생자 고(故)박찬길 검사 유족 제기 국가배상소송 항소 포기 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787809&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 새로운 IgA 신병증 희귀 치료제 허가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787808&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 위기채무자 지원 강화를 위한 업무협약 체결식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787806&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 김진아 2차관, 국제해양법재판소(ITLOS) 소장 접견(11.3.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787805&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "중복지적으로 인한 5,159세대 대지권 미등기 문제, 16년 만에 조정으로 해결" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787803&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 인제 자작나무 유아숲체험원 안전관리실태 특별점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787802&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 고 안성호 이등중사 호국의 영웅 귀환 행사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787800&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 한파 오기 전 한랭질환 예방 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787799&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | "새만금에서 일하고, 전북에서 함께 살아요" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787792&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 모듈러주택 산업 현장소통을 위한 규제합리화 현장캠프 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787791&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인간형 로봇이 '일하는 법' 배우는  데이터 생산기지 문 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787790&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세평가분류원, 2026년 '관세평가·품목분류 연구논문 및 판례평석 공모전' 우수작 선정·발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787788&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 대한민국 제조업 판 바꾼다... 산업부, 제조AI 4단계 확산전략 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787789&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 생활공간에서 의료서비스 받는다, 전국 최초 의료집중형 장애인거주시설 대전 '로뎀' 개소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787787&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 소비자생활협동조합 지원과 육성을 위한 ｢소비자생활협동조합법 시행령 개정안｣ 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787785&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 원안위원장, 한빛 원전 현장 안전점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787786&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "예술 활동이 멈춘 때에도,  고용보험이 힘이 됩니다" 근로복지공단, 방송 연기자 축제 찾아 예술인 고용·산재보험 안내 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787784&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 민관이 함께 자살예방·생명존중 위해 협력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787780&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 말하기 어려웠던 연구 현장의 목소리, 익명의 문자 한 통(1551-1441)으로 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787779&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과학 탐구의 결실 한자리에, 제72회 전국과학전람회 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787778&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 공무원미술전·공직문학상 수상자 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787781&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 지역 교육의 새로운 도약, 43개 교육혁신선도지역 시동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787782&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | "배고파 훔친 즉석밥, 경찰은 처벌보다 생필품을 건넸다" 경찰청, 경미범죄 심사위원회 우수사례 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787783&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 안전한 대불산단, 실천으로 이뤄낸다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787775&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 산업안전보건본부장, 대불산단 불시점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787761&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 외국인투자기업,  한국 산업의 든든한 동반자 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787764&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 「고용상 연령차별금지 및 고령자고용촉진에 관한 법률 시행령」 및 「남녀고용평등과 일·가정 양립 지원에 관한 법률 시행령」 개정안 국무회의 심의·의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787760&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 소비자생활협동조합법 시행령 개정안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787758&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 생산자·소비자 함께 '감탄' 벼 수확·유기농업 가치 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787769&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 2026년 농촌 체험학습 프로그램 우수 사례 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787767&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 폴리텍대학, 정규수업으로  '한국인정기구 합격증'까지 챙긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787759&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 행정규제기본법 시행령 개정안 국무회의 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787762&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 11월 12일부터 다세대·다가구주택  면적 제한 1,000㎡로 완화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787763&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 국산 열풍건초 이용 확대 현장 목소리 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787765&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 가을철 시설 딸기 잿빛곰팡이병, 습도 관리 중요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787755&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 보행 불편한 장애아동·어르신 주차 편의 높인다, 「장애인 등 편의증진법 시행령」 개정안 국무회의 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787757&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 특허심판 분쟁, 현장에서 답을 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787754&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 해외 생산제품과 달라도 기술·기능 유사하면 국내복귀 인정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787751&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 건축내화재 KS, 현장 제품 특성 반영과 안전성 강화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787750&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K-수출스타 참여기업 수출액 34% 증가 '모두의 수출'  성과 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787748&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 적극행정 공무원 보호 강화...'보호지원단' 신설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787753&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 디지털 미디어 문해교육, 학교 현장에서 새롭게 만들어 가다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787739&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | '국가 긴급현안' 해결 속도 높인다, 국민 안전을 위한 긴급과제 기술개발 즉시 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787732&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 정부 인사업무 특화된 인공지능 업무시스템 첫 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787735&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 동아시아 기록관리 전문가, 한 자리에 모여 기록관리의 미래를 논하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787745&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 폭염 피해자 지원 사각지대 최소화, 관계기관·전문가 TF 첫 회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787743&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 디지털네이션스 · OECD 무대에서  인공지능(AI) 정부의 미래 논의 선도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787741&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제3차 고준위 방사성폐기물 관리 기본계획 수립을 위한 국민 의견수렴 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787738&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 숨은 물그릇 확보, 홍수예측 고도화로 올여름 홍수 대응 역량 높였다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787737&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 11월 멸종위기 야생생물로 고니 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787736&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 가축전염병의 선제적 차단과 확산방지를 위한 K-가축방역 개선대책 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787733&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-05&endDate=2026-11-05&srchWord=&period= |  |

## collect:out_of_window (30건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 국민참여입법센터 | 법인세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87940 |  |
| tax | 국민참여입법센터 | 부가가치세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87934 |  |
| tax | 국민참여입법센터 | 소득세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87942 |  |
| tax | 국민참여입법센터 | 국제조세조정에 관한 법률 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87944 |  |
| tax | 국민참여입법센터 | 조세특례제한법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87946 |  |
| kifrs | 임팩트온 | 기후위험, 재무제표 주석까지 들어온다…회계기준원, 공시 사례 공개 | http://www.impacton.net/news/articleView.html?idxno=19406 |  |
| kifrs | ESG경제 | 재무공시와 기후공시 연계 강화...회계기준원, 기후위험 공시 사례 제시 | https://www.esgeconomy.com/news/articleView.html?idxno=15878 |  |
| kifrs | tfmedia.co.kr | 회계기준원 IFRS 20 간담회에 에너지 기업 ‘쫑긋’…IASB 부위원장도 참... | https://www.tfmedia.co.kr/news/article.html?no=204787 |  |
| kifrs | 일간NTN | 회계기준원 지속가능성기준위원회, 지속가능성 공시기준 첫번째 세트 의... | http://www.intn.co.kr/news/articleView.html?idxno=2049269 |  |
| kifrs | tfmedia.co.kr | 회계기준원 KSSB, 지속가능성 공시기준 첫 번째 세트 의결 | https://www.tfmedia.co.kr/news/article.html?no=201983 |  |
| kifrs | 매일경제 | 국제회계기준 해석委, 일탈회계 관련 기준개정 필요없다 의견 | https://www.mk.co.kr/article/11489251 |  |
| kifrs | 이데일리 | 한국회계기준원 "국제회계기준 해석위, 일탈회계 극히 예외적…기준개... | http://www.edaily.co.kr/news/newspath.asp?newsid=04060646642397208 |  |
| tax | sejungilbo.com | 법원, 18억대 농특세 가산세 "취소하라"…"세법해석 어려움, 원고 탓 아... | https://www.sejungilbo.com/news/articleView.html?idxno=59290 |  |
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

## collect:tax_subject (40건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | karnews.or.kr | [세법톡톡] 2026년 세제개편안 (양도소득세) - 한국부동산뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Ub0liX2hObkdsdUhZc3lES3AycE9NV2xfVHBvMDJNYXpkbkVZNi1FdlZKcklqUndyX0xoZXB1OUFDdHNkZWNHa1BQN1FWMHBMUlZhV2V1ckpvRWUwZVpzZFctNllmUFd3bHZB?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | news.kbs.co.kr | 부부 공동명의는 진짜 불리할까? 세제개편안 오해와 진실 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5yTUo1c2FfUGVDcERxc2lJM0JHSUItNks1N083NkViV1Z2VHFnSWFUdjdHYnRyUE9fSUoydEg0ekNnY0xVRlBiTEkzYWlBYkplV3p4UjctSkVGVlU?oc=5 |  |
| tax | lawtimes.co.kr | 가업상속공제 제도 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE0tZHB3U0FDMU95aVE4TFFlMFh1ZW1zRkJyQ0ptMXowNTdiOXF6dFhXczE1ZVdDNTRxZ0kxUEhlVVNHZDhKdkl5TWFUR3lmQk5WNGNEYVpzRl9lMDlySGVSak01S3psQ1RCNTdxZXN30gFyQVVfeXFMUEpkOVBWUEI2ODBteGUyTHZMOWxkSVJGS0twRmk4V3ZmZ2g3RkliS3VyTzBJR3VEQVYxSWlaZmo5bDluYVpZTThqdGYwMXlESnpraENELU9vcVViTkp2dEVoaWxfU3NnUmVIaU1oREpQbTlB?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzDSAWBBVV95cUxOeDlrTWJMLVFFUHdRdGFKSnZYenV2UWl2UnZxTUtyamE4YUNfSjVfSzNHY2U4eEQ1X096RGc2aE9BN3dMUGlnaE56N1I2c2c0bkZkVTR0a1lJR1pUQWxUSGk?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | newspim.com | [뉴스분석] 부동산 세제개편안 정부안 의결…與 내부서 불거지는 수정·보완 목소리 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBaMU94ZFRIbWRacklQenVyOHN0dUxYc3AzM0ZveTR5a3Fvd0NsaW9jcVNNRGN3emRCcUFCQWJsa0J5TEFNWnd3bEc1cExsRlNSVDJCMWNNWEkxOWQz?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | yna.co.kr | 거주주택 매도 5년내 비과세 혜택도 못받나…임대사업자 반발 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBpYzcxU3VvMk11SGgteHA0djBIUURacE4zTDBZUkxodHVJRWFwWTJ2SGd1Z3dOVXBndUJWVEtNeE55MmRRREhkWGlqZkRQSWxFXzlJaVN3bUM2UDDSAWBBVV95cUxNYy14RnVzSFZybThNX0ptUE1yOHQzcVFDR05VaDVUSHczWWlydEJGUkZoTV9WcjZxRUEyUGdsdmxiemgxZzNIUFJCaDZpOXF0emJnQTVOS3FiMTJOaEplV2c?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | lawtimes.co.kr | (29) 법률가와 세법 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9UYnRhb200WmtsSXk2QUxnQ1NPQkVVS00ySENCS2Q1TlNZV3BIU3JPUEhsUURCU2JYTU1kY1c1UFVOVDdkRVBlXzhHbVlZVnBhclZreEI1OWYtWUhUQXhrV2NGUnNULV9JZlNtZlZn0gFyQVVfeXFMT0cycGlqMEhfNDJEX1ZqNWxycnlIX0pUMEN1bDB5ejlTUi1wdEt5RkM3UTdMT0Q0X2Yxajdzc0JqTllEdkpBdXo1UGlGMWZhUlJSMkNlS3oxRHZoMHhHQWNIR3g1TzlGaGEtX3YtLU5jQ2lR?oc=5 |  |
| tax | 한국세정신문 | 대통령 업무보고까지 했으나…국세청 '세무플랫폼 감독규정 명문화' 불발 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1WUmhWcEZCbHdGN2h1RTR4aHdsaFV0bTVjWDVfWHdGVVdKREpvTnAyVUM1djVfYTdLbFhRWE1tV2Rwd25tRzZYQWNpZF8xU2lyYmtJVHFaRUNscWJobHBTQ3VRdWw?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | mbnmoney.mbn.co.kr | 국세청 세법 개정건의 10건 중 8건 반영 못 해…'실적 쌓기' 지적 - 매일경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wYjVGQjdSbkZCY2RpRjFvUjNyX0tpSFFDazNZVnFkcHdXY2hCd1Z5MUJKbmdNVG56NGdRc2trbnQzYXVoSUhGM25DRy05anRvNnhPYnlOYWdDSjdKOV9wSFgtbjgyaFBo?oc=5 |  |
| tax | m.kbsm.net | 세제개편안 29일 만에 유턴…비거주1주택 종부세 공제 12억 유지 - 경북신문 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE5ub09KcURLZ3Mwd0tCOWxmMEg3R2tNSlFHV2c3NDhFOVdjWW05bTdRWG8wVk1OaktGY0VJMTdQdG9oS0xCS3NFXzlMd1NIQVE?oc=5 |  |
| tax | jinju.news | 김태호 의원, 지역균형발전 강화를 위한 지방교부세법 개정안 대표발의 - 진주인터넷뉴스 | https://news.google.com/rss/articles/CBMid0FVX3lxTE44X0w1UUNpbTMtSnZFa2ZpdUF0dHhxeU5GWFlWNF9NZTY0aWRNWGJlS0lLMEJFc1lERHd0MFBubjhHUVBERlVKT204VjQ2TlIxb3drSUJfV3FyMWcxX1RONzUxWE9LMzkxY2VGZVBCVjl5WVlnTUp3?oc=5 |  |
| tax | newsk.net | 세법 개정안의 주요 변경 사항 : 한인동포신문(몽골) - 뉴스케이 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXdlRVQnREMG5BcGNrUjNUdF9MSEVtbGJzdHBuWjNBM29ZTDBtYXY5TWw4Q1F4OG1QMlVSZnQ1YTNYMEpBcmJKX1hhTDJOczE0UTQ5VnlRY1FmZw?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | newsis.com | 이형일 부총리, 세법 개정안 관련 제안설명 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE14d2tkM2pvUlBhZ1lJRlFtdVVoWnU0RVd6X3Q5UWhQWC1VcHJiSUJJWTAtRFpCSjY2Z3ZCV25id2cwSGtYX3pDemxTVEk0YThibk90a3MyeVdhUE83QWYwdw?oc=5 |  |
| tax | imaeil.com | "살면 보유세, 팔면 양도세 폭탄" vs "서울시장 책임" - 매일신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wQTFnTkQ1OWM0OU9vQmh4ck9wdk5Sb0pzdkZZX0tKNzNXbDdNWWlNVGJGTnlyVjliRThaZG9mZUhCVGZjWU9CeUZDSEZMZUV4N3o1cFBZcjVFQ0J4Yi14QXNn?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | paxmedicalnews.com | 2026 세법개정안에 병원계 ‘발끈’… “가업상속공제 제외는 필수의료 사형선고” - 팍스메디컬뉴스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1Dd3lHSEFoSWkzMDJXZVAwcnpDVjkyLXJYa0gwVURLSWJjeGhfTVZnV2pnVTZfdWdqTU1sZU9wM093UDhoT2dmUDdtVThCc3o3VlZEY3lVbzFuQTZCX3N6bHlvSDhrekpTdFFKcWpId3A?oc=5 |  |
| tax | thevaluenews.co.kr | 국회예산정책처 “2026년 세법개정안, 5년간 세수 14.5조 증가” | http://www.thevaluenews.co.kr/news/view.php?idx=202849 |  |
| tax | ftoday.co.kr | 국회예산정책처, "세법개정안 따라 5년간 세수 14.5조원 증가" | http://www.ftoday.co.kr/news/articleView.html?idxno=368597 |  |
| tax | betanews.net | 경기도, 국회 입법박람회서 지방소비세율 인상 등 세제개편 과제 알린다 | https://www.betanews.net/article/view/beta202611040071 |  |
| tax | sentv.co.kr | 경기도, 재정위기 돌파구 찾나…국회에 세제개편안 제시 | https://www.sentv.co.kr/article/view/sentv202611040070 |  |
| tax | joongdo.co.kr | 지방 곳간 넓힐 세제개편안…경기도, 국회 입법 무대서 분권 승부수 | https://www.joongdo.co.kr/web/view.php?key=20261104010001227 |  |
| tax | gokorea.kr | 국회 부동산 세제 개편안 논란, 비거주자 세금 폭탄의 진실은? | https://www.gokorea.kr/news/articleView.html?idxno=884004 |  |
| tax | womennews.co.kr | 서울 아파트 매물 8만건 넘어...8.3 세제 개편 이후 33%↑ | https://www.womennews.co.kr/news/articleView.html?idxno=284089 |  |
| tax | tfmedia.co.kr | [전문가 칼럼] 2026년 가업승계 세제개편안…승계 가능한 업종과 제외되... | https://www.tfmedia.co.kr/news/article.html?no=208392 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

