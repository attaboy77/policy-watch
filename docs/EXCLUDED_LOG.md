# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-08 10:01:57 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1668건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 15 |
| excluded:company_event | 1 |
| excluded:company_self_activity | 3 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 25 |
| excluded:financial | 1 |
| excluded:industry_specific | 7 |
| excluded:local_gov_petition | 1 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 44 |
| excluded:no_regulatory_signal | 39 |
| excluded:opinion_piece | 1 |
| excluded:reader_content | 1 |
| excluded:similar_news_merged | 11 |
| excluded:smb_only | 1 |
| collect:event_announcement | 6 |
| collect:incident | 1 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 22 |
| collect:noise_keyword | 1 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 208 |
| collect:out_of_window | 32 |
| collect:tax_subject | 36 |

## excluded:category_cap (15건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 의무화 시대, '데이터'가 수익률 가른다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ETFBnRTJ0eEttX3pfeU9UeE9CSHl0UnQzX3lhenlxVWllRGVQUnV4RDZLZ3BZTzg2WlNTLXNUSHJoWTl1eUl1NjBYd2pPVnc3SzhuTXlNaGZUdw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 로드맵 확정…10조 이상 코스피 상장사부터 의무화 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5XUnhUekpXVlVFZEFuR0ZtdldTYlhvX1A4Yk84UVZqc0xCLTVYQVlTT2wwLWZRUkNGb0FpWTZaeEJzUFNXWVpwYlFJQUhvTmR3aEtOS0FKeFVvQzBiVGJObkF4X3phc1VScmJMQdIBcEFVX3lxTE5HcHpjSzJTMnQyakNLT190LUVLX3ZGNXM0LWJKVzA1cXlHcjhVc1dWY1V4OGFrcG42REdfMWJRVmlXVUcwZ2JYTXE5ZE1BamduRllrbGZReTBqbjRUeWVQZUl2cEdfZ09CRVFRemlvS3Q?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 2028년 대기업부터 시작…스코프3는 3년 유예 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB0NEtXNnFZdGJLd01zRG5XaGUtZ1RyX1hFMTB2REQ5VlVJRkZzdVFJODBNVHdqTlhBZzZtQnZtM1N2dXhtc2tma3pMaEMzX3N1cjFjOVl3RE91Sjl6Rm9zV251UDBQYUo5NWtXMNIBcEFVX3lxTE1jYVpBZ1NRcDNjb0ZpaGh3Q09TZFpINmN2b3BxbTJMaGpJeVVqQ1loMHhkRjJYZkp2ZjVkTEN4R0FWM0lrcWtsSUphSW4wUHZ0MWw3ekgwb3JZeE5hcmNfUXE0VkxUcXhWOFdsYXlZVmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | yna.co.kr | 국내 대형 상장사 "ESG 공시 의무화 대비하고 있지만 일부 부담" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yZUdEcHdYT2V3Tk1jbEs1aTVwdmc1TUZhbzA3MmpJVXlHQXRCeEFVclI3YW95am5UNTU2d29fZTA3ZGZ1NElDU2o3dWhHYTVzcTd4LUs4bi00cnPSAWBBVV95cUxNWlJkdmlVWkFDR0czQlVSYlZ2c2VFdjZxOXcxQ0ZoeW5tNFllTEhzX0pVTG94UXJwemFHRnVWODBRZXZWTUlGOVZUNHNkODdKOTdxZ0NlZWlKdnFvOVpib3Q?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 |  |

## excluded:company_self_activity (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | 泰, ISSB 지속가능성 공시 의무화 확정…28년 SET50부터 단계적 시행 | https://www.esgeconomy.com/news/articleView.html?idxno=17232 |  |
| kifrs | 파이낸셜뉴스 | 삼성전자 부사장, '글로벌 회계기준 제정'에 참여…韓 기업 목소리 커진... | https://www.fnnews.com/news/202611061034591232 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |

## excluded:corporate_pr (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | asiae.co.kr | 중대 보안 취약점 방치 땐 CEO 책임…금융당국, 금융사 내부통제 강화 추진 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wVHBFeHhiNjhDb1pVRzYwbXFYTmRrZmhpOFNWS0laVUNkeGZ4NUdGQVY2eGJBWmdlRHJ6SFFsaEM5bW5RQ0FyazRqY0tUWmhnRHJYVjdLSUZwUjJRd2Y3TQ?oc=5 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (25건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |
| tax | 행정안전부 | 지방세법 시행령 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88292 |  |
| kifrs | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
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

## excluded:news_too_old (44건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | investchosun.com | 삼성생명 몰아붙인 회계기준원…2분기 결산 고민 깊어졌다 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPZWdwcnZLaWNBaTl1c3BFRlZyaG9NR0M5eFZRQzBYb0JBeVRIeWQzODI4VUJQbWlKNWdtX2hlWW56WUd0TEwxWjM2ZnlNWHZIYTFSUHNrUmFidUhOVUhDWU5OTVN6c2tCZ09IZVBZYXdzSEZBaTByVGFRTG9tQ1k3MmxtSQ?oc=5 |  |
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| kifrs | 일간NTN | “회계기준 질의회신 결과로 재무제표 재작성하면 처벌 예외규정 고려해야” - www.intn.co.kr | https://news.google.com/rss/articles/CBMiakFVX3lxTE8yV2NfWjFmYjY2OXVvS09YeVVycWo0QlZXQ1VWTW9zbGlMbXBGRmJCNXp2MnJzdTQ4bXFKblVoblhVaHhkTnR2bXQwdy10M3RzcDBQUWNZdmJMOFpBSzVXeDVRUEF2Q3d3RXc?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1001호 ‘재무제표 표시’ 개정 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5CTE82SldnUm1UUEtiTVpXeGxFdHdqbEFHQVk3dGF0WFh5YkdzRW9xLWJFOU5RamNEdXhFWGRmNVQzb0txb3JDcXFzdktmWGRzRXoxOFB1YXU?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | 조세일보 | 김현정 "尹 정부, 3년간 신외감법 무력화" - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JdDQ0dDRwdlpDdGhzcnpHZ3hhZ3V3OXFqbXplRXJ5SlFFeU5VWXhlZHg1clRpNHVfQ3B6YXB2RDZBR21GSWlzVnJ4RnY3NDRpaURGVVBBTW5UWWtzQnd3?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
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
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | fntimes.com | 금감원, 신외감법·K-IFRS 제·개정 내용 설명회 개최 - 금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE51eTFBa0dYOXQ5UEt2bmF4SFUtZ0cwS0l0NjZRSUZTYlQ5d01iOGNPNHBQTTBvQTA5N2lycVJYc0s3NW16T091M2xmRjVydmRJekFheUU1TXhvZU94MXNaZVBvQUVMLWtMUXdvWkcwalR4NTZIbUpnV1JSZnA?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | lawtimes.co.kr | 구 외감법 상 ‘회계처리기준’이 구성요건이 될 수 있는지 여부 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9mQkQ0MVloUTljd2UzOXI3QnZfVFA2ZUJaYTlEa3NfLWNHa0ZYVUxHZ0hUMHkyeDFIWmdZV2VtaFM3TDVpYUZwR1A1R1JweFJQUWJFOTU4VFF5WnUtdmtmU0JuWnNUQ3dYc0ctbGdR0gFyQVVfeXFMTWtxblhPLWdZc3p5VU1QdmZhczA5aHVlRHZPOS1fZXBsYUFvWGNRNG9naXhhRXlOdjY5c0RPbmNLWHpQMFJWcmlab2piTXJ1VVZRNDJ3SlpYLTlydjNXX195WmNkTnYwZUNzYm15aWFOYU5B?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |

## excluded:no_regulatory_signal (39건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 | https://www.impacton.net/news/articleView.html?idxno=30527 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | lcnews.co.kr | SK증권, 기후금융·ESG 공시 성과 인정…UNGC LEAD 기업 선정 | https://www.lcnews.co.kr/news/articleView.html?idxno=210942 |  |
| esg | newstomato.com | 보험사 ESG 공시 늘었지만…비교는 '깜깜' | http://www.newstomato.com/ReadNews.aspx?no=1318745&inflow=N |  |
| esg | dt.co.kr | KCC글라스, ESG 공시 범위 해외로 넓혔다…생물다양성 영향도 공개 | https://www.dt.co.kr/article/12093213?ref=naver |  |
| esg | finomy.com | KCC글라스, ESG 공시 확대···인니 법인 성과 첫 공개 | http://www.finomy.com/news/articleView.html?idxno=265631 |  |
| esg | worklaw.co.kr | ESG 공시, 직원 성장 이끄는 장치가 돼야 | http://www.worklaw.co.kr/view/view.asp?accessSite=Naver&accessMethod=Search&accessMenu=News&in_cate=101&in_cate2=0&gopage=1&bi_pidx=39682 |  |
| esg | asiatime.co.kr | [윤영민 칼럼] ESG 공시 시대, 보여주기식 경영의 종말 | https://www.asiatime.co.kr/article/20261023500342 |  |
| esg | thepowernews.co.kr | ESG 공시 291곳→1년 뒤 3171곳…대기업 넘어 협력사까지 ‘데이터 전쟁... | https://www.thepowernews.co.kr/view.php?ud=202610221509381568de3f0aa1be_7 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | peopleview.co.kr | [신간] “차트는 거짓말해도 숫자는 배신 안 해”… 이대훈 회계사, '좋은 회사 재무제표' 출간 - 사람의 풍경 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE54SThtOERpcHVOQ3R2aDd6dmZCM05hM2RnUllBTlIwdXpFaTNxcl82dERVT0xlc2lQZUJhZlByaGpnenRtdEQyN1pTeHcxeU05WTRUQ2QtdnFGUFBNWHdJaHVnWmRYQQ?oc=5 |  |
| kifrs | kr.investing.com | DTE Energy, DTE Gas의 2026년 3분기 재무제표 공개 - Investing.com 한국어 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBCYmhReUNrazdwMW9MOEQ4UE1QTER2NHFseTFnaVZjYzh4MzM3WTI5dnJZTElRWDNpcEQxTk45OXJtS2pOb3dUV1M2bFc2TS1LQm5USDE4TVU2Z0FWM0NpQ25NMWVPb19jNkRQM29YYw?oc=5 |  |
| kifrs | coinreaders.com | 클라우드플레어, 3분기 매출 39% 증가…회계기준 영업손실도 확대 - 코인리더스 | https://news.google.com/rss/articles/CBMiSkFVX3lxTFB6c2ZJc2dwaWxaZVA1Yml2WXA3X28ybVZodEx0VENFNkF5ajF5SkRiQ3VOWnktek5VXzdyQVV6b0RlM0c4dmlYMElB?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] K-방산의 롱사이클(Long-Cycle)을 바라볼 때 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBjQXJweWE2aHlLODdIa1BBUXFBT2xqYlBPSmZSWEIwVERTdXAyU25VREcyNU9GSDNBWm54TW9ybm1HQ1lKcUUxUW1iZjJCT3VqdkY5Y0RWZHl1WHJyQmZKLWVBZnN6SjlFY0Qycg?oc=5 |  |
| kifrs | livebiz.today | [K-자동차 밸류업 체크] 현대차 125조 원 비전...무시할 수 없는 재무제표의 경고 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBZOHpTbGpYNTNZeHZ1YUtiX3RkYm5oSFJHOW9tRlI3MXlRYXZQa0ZhTnNmLXR5RVVkbG9hX0Fjc3NwU1hhYl83WmxwUU85cENEMzFUNGNGVEF1blRHNS1qV3BWaWRKOEhFMmFJcA?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| kifrs | kihoilbo.co.kr | 의왕시의회, 백운PFV 회계 논란 집중 추궁…출연금·민간위탁 제동 - 기호일보 | https://news.google.com/rss/articles/CBMib0FVX3lxTE81eDhFelVrVTBrRmJ3WWY5aFA5SGNXalc1Y3lKUGFaZW1CQ2RuX29iX3h3RlNmQ0k0b0VXSkRqbFlzeEJ5VDA4alNoMHkwM1RlNm1PVjVmOU1WLTdacHBFQ3hlRkRBS0M3QkU2UGw5Yw?oc=5 |  |
| kifrs | dailyculture.kr | 김태흥 의왕시의원 “의왕백운PFV, 시민 감시의 성역인가”…자료제출 거부 정면 비판 - 문화매일신문 | https://news.google.com/rss/articles/CBMiSkFVX3lxTE50MGRBOGlkanYwR1gwUnFhY0xqMTF3MVpXNDMyMmJ3aTdaZ29aQjl2MDZnUnBKclVydF9qTnlTVGdDZkhCRXM1TlhB?oc=5 |  |
| kifrs | dailypop.kr | [줌인] 고려아연 최윤범에 해명 요구한 영풍·MBK…석포제련소·홈플러스 책임론은 현재진행형 - 데일리팝 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBZX2oxcWxGbHJ3YUxhZjRBQmYyWkt1S01ZdDBrR2V4XzI2Nl85Q0xvQTkyNTQtVjBPWXhFMUNCZURVS3FaeUpjNl9obTB3bThreEItWFlZUi1KUmNxUkw5R0FDT1BNaGw2?oc=5 |  |
| kifrs | leadeconomy.co.kr | 카카오 3분기 영업이익 1178억원…전년 대비 17.2% 증가 - 리드경제 | https://news.google.com/rss/articles/CBMicEFVX3lxTE9NNTNBUjFiRjVKOV8tZmpDVndUQjZZX19qY1Jqdy1MWU1lWkNHZm5TOEZ2cUNfaGtGSmticjBnbHBmWGM0MDVFdkdEOE1JS0ItTTlUVDdqRVpkY25KczdaX1Y0dlVvbU5aOG9XRG5XODA?oc=5 |  |
| kifrs | biztribune.co.kr | 카카오게임즈, 3분기 매출 691억원·적자 지속… 4분기 '도깨비의세계' 구글 1위·M&A 드라이브로 턴어라운드 승부수 - 비즈트리뷴 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBuQWRWNldza2NCdi1fY1NEb25Zdzh0MHVZRXlLQXA3Mk5MQ1dyb291YkxhTEc2aGIwbWdWYnZoamcxQmdrZjRkUnNnSlZISDc2RmtOYzJiU3FrNjFDbkFESG5WLVZISS0ydXFGYmNROUc?oc=5 |  |
| icfr | datatooza.com | 아스트라나 헬스, 내부통제 취약점 미시정으로 공시통제 비효과적 결론…사이버사고 집단소송도 피소 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9kc0RkNDVQemVNajdUdDJxVkFjcTBZUmNQU3ZTcS1jaHFhWGw1Y0dUVVh5Nlp1V2kwSHpvUGRBN1J0MjRuakgzZXZFQWlpX0Uzb2RSamJndGZ3dDBtQURWUTBMQTVJMmN2U3lTVFZLNVNjMjg?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| tax | kgnews.co.kr | 경기도 지방세제 개편 6개 법안 발의…‘14조 확충’ 기대 현실화될까 | https://www.kgnews.co.kr/news/article.html?no=918123 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:reader_content (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | 'KSSB 공시 의무화 시대, 무엇을 준비해야 하나' 세미나 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE81V1p4YkEyeGp6aWFCY2lCYmcxVXNZYm5ZWEJrV21QR0NOSjZfMFN0RWgza3otTFR4ZjZzTnBoQU9sWkw5SDFkSS05bkRQUXBxY0l2LTVQaW5QbWFOR2FWcUZWVE1oSlpNR193ZQ?oc=5 | event |

## excluded:similar_news_merged (11건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| kifrs | newsis.com | 유한종 삼성전자 부사장, GPF 위원 선임…국제회계기준 제·개정 자문 | https://www.newsis.com/view/NISX20261106_0003857682 | → 대표: 삼성전자 부사장, '글로벌 회계기준 제정'에 참여…韓 기업 목소리 커진... |
| kifrs | datatooza.com | 사이더스 스페이스, 2024~2026년 재무제표 신뢰 불가…회계 오류로 재작성 예정 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTFBnRnV1OUQwUWVDUDJ5MVhCZU5GaFF6Y09mSzZQemlfSjdGUGVWc3otTGVqTUJTdzRLOUpIVVRLeE9Ud0xqQzZKZFhqX1dPSGVBQ19SREh0cy15RUNEWXA2dW9IVXhWWjVuRHVtTTBodzhsUkk?oc=5 | → 대표: DTE Energy, DTE Gas의 2026년 3분기 재무제표 공개 - Investing.com 한국어 |
| kifrs | digitaltoday.co.kr | 에스엠, 2026년 3분기 순이익 110억7000만원…전년 동기 대비 65.7% 감소 - 디지털투데이 | https://news.google.com/rss/articles/CBMie0FVX3lxTFBNSmJCU19QT2F4eTNsMHA3c1dBVVZINGNoNUk3T3QzRWZ2T0x6WG5vYUhtamd3NW9UUFRRV3JfeXNTN3g2UDZLNmY5aE5EbjI5V0FEV0ltbnpfWmgtYVRzdTBDT0dMVzBBSTdaSGwzdm4zc1pPdXY5NG51UQ?oc=5 | → 대표: DTE Energy, DTE Gas의 2026년 3분기 재무제표 공개 - Investing.com 한국어 |
| kifrs | biztribune.co.kr | 넥써쓰, 3분기 매출 328억원으로 전년 대비 257% 폭증… 원스토어 품고 글로벌 AI·Web3 플랫폼 외연 확장 - 비즈트리뷴 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1RTFMwZllHQkNXelBFb1RIaTE4LXVaWm9mUElSaXpLNzBSdVEyX1ZGT2lod1BBYmtxeExTRXB3Unh2d3ZENWI3RDBfUGhockgtUVhKSkRDRVFqUzg3bExBLVNNLTRLeU9BYnJsbzY4ZjQ?oc=5 | → 대표: 카카오 3분기 영업이익 1178억원…전년 대비 17.2% 증가 - 리드경제 |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 |
| icfr | news1.kr | "내부통제 경험 나누고 취약점 보완"…기보, 5개 공공기관과 맞손 - 뉴스1 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1Wc3pJS2E4NzV3cC1zV3NGTlZ5dFBxcmlJNi1id0RSRVdORXVTWDJJZHJCMy1tcldVYjlZTlR5SUJMYzdjcE91RGFweWxrNVhZX0dDS1dIWk90M0N5?oc=5 | → 대표: 아스트라나 헬스, 내부통제 취약점 미시정으로 공시통제 비효과적 결론…사이버사고 집단소송도 피소 - 데이터투자 |
| icfr | datatooza.com | 린트리스, 재무보고 내부통제 '중대한 취약점' 4건…공시통제 효과적이지 않다고 결론 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE0xMk9tbDh2QTYwcWEzNTZibFpGbXlhRmJkV0tMMThlUTBWOVNucHpsZnAwVW9MZHUwNWdJbXE1Nzh3d2dyRkkxVUJ3TW9pWWNCeW1sX2MtcHM5X1BNT0dYRWQ3d1VoZ0tnMjdoQXlqbWNUQQ?oc=5 | → 대표: 아스트라나 헬스, 내부통제 취약점 미시정으로 공시통제 비효과적 결론…사이버사고 집단소송도 피소 - 데이터투자 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## collect:event_announcement (6건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | 2026년 글로벌 ESG 교육 워크숍 안내 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2199 |  |
|  | 재정경제부 | 제276차 대외경제장관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079883&menuNo=4010100 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
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

## collect:no_category (22건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 반도체 전문가 간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079895&menuNo=4010100 |  |
|  | 재정경제부 | 긴급 시장상황점검회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079890&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 코리아그랜드페스티벌x행복한 백화점 현장행보 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079882&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] 세계은행그룹 부총재에 두 번째 한국인 진출 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079886&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「기업활력 제고 TF」 첫 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079863&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, Fitch 연례협의단과 면담 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079878&menuNo=4010100 |  |
|  | 재정경제부 | 범부처 민생안정지원단, 소상공인 재기 지원 현장 방문 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079866&menuNo=4010100 |  |
|  | 재정경제부 | 가상자산 과세 관련 부총리 브리핑 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079862&menuNo=4010100 |  |
|  | 재정경제부 | 시장상황점검회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079867&menuNo=4010100 |  |
|  | 금융위원회 | 국내외 주식시장 변동성 확대로 단계별 대응조치 가동 | https://www.fsc.go.kr/no010101/88100?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 현재 유포되고 있는 부동산 대책 관련 게시글의 보도에 유의하여 주시기 바랍니다. | https://www.fsc.go.kr/no010101/88099?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융권은 개인정보 유출 사고에 따른 보이스피싱 예방에 총력 대응하고 있습니다. | https://www.fsc.go.kr/no010101/88098?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 기업지배구조보고서 공시를 통해 상장회사의 주주보호와 주주환원 노력을 확대해 나가겠습니다. | https://www.fsc.go.kr/no010101/88091?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | AI시대, 거세지는 침해위협에 맞서 全 금융권이 튼튼한 보안체계로 무장하도록 혁신적인 정책과제를 적극 추진하겠습니다. | https://www.fsc.go.kr/no010101/88086?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ｢“취재정보로 매매해 ○○억 부당이득”···○○신문 조사 마무리｣ 보도 관련 | https://www.fsc.go.kr/no010101/88085?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 한국, 아시아지배구조협회(ACGA)    기업지배구조 순위 역대급 ‘5위’ 달성 | https://www.fsc.go.kr/no010101/88084?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 홍콩 H지수 ELS 관련 은행·증권사 검사 결과 조치 - 제19차 금융위원회(11.4.) 의결 | https://www.fsc.go.kr/no010101/88082?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 계리가정보고서 도입 등  ｢보험업감독규정｣ 개정안 금융위원회 의결 | https://www.fsc.go.kr/no010101/88081?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 2027년 금융위원회 예산안에 대해  자세히 설명드립니다. | https://www.fsc.go.kr/no010101/88074?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | 금융권은 개인정보 유출 사고에 따른 보이스피싱 예방에 총력 대응하고 있습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788216&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 현재 유포되고 있는 부동산 대책 관련 게시글의 보도에 유의하여 주시기 바랍니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788220&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 국내외 주식시장 변동성 확대로 단계별 대응조치 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788244&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |

## collect:noise_keyword (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | kookje.co.kr | [차호중의 재테크 칼럼] 급락장에서 살펴볼 재무제표 - 국제신문 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPNU4wQzNxTlk0ajJlRk5MOXlzRi1NRVAyZW9ranV1TkNWQmlsT01OWWZKVHkzLXZvZ0ZqVEQ0THBLSlE0by1XMWtaRUxuVXlxVllKMUl5aHBoaU0xbVBvSFd2YlZPUW93Sm4xcmVQN29uWFhTb0RjM2xTcHJ4NUdNcGVJN3QyTzNIM0l4UU5B?oc=5 |  |

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

## collect:out_of_scope (208건)

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
|  | 정책브리핑(교육부) | 폐교의 새로운 시작, 지역의 가능성을 열다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788317&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 수상의 영광을 시장의 기회로, K-Sool의 도약이 시작된다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788310&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 노동부 장관, 산업안전 대응 강화를 위한 긴급 기관장 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788306&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | '학대의 신호도, 마음의 신호도 놓치지 마세요',  2026 발달장애인 가족치유행사 홍보부스 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788305&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 박윤주 제1차관, 벨기에 외교부 사무차관 면담(11.6.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788304&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 전남광주 장흥 육용오리 농장 고병원성 조류인플루엔자 확진에 따라 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788303&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국무조정실장, 국토대전환 전략자문단 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788302&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 제4차 농식품규제 합리화 전략회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788301&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 식품 스마트팩토리 기술 혁신과  표준화의 미래를 그리다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788300&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 김종구 농식품부 차관, 전남광주통합특별시 및 강진군 고병원성 AI 등 방역실태 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788299&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한·미·일 해외재난대응협력 협의체 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788298&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 배추·무 수확기, 비·저온 대비 철저한 생육 관리 필요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788296&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 올해 2,064건 홍보…직원 1인당 1건꼴  "전 직원이 홍보대사" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788294&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국산 우유로 만든 명품 치즈를 찾습니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788292&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 생명지킴본부-개신교 자살예방협력회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788289&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국내 재래종 콩 230점 분석, 검정콩 '유용 성분'·'항산화 활성' 높아 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788290&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한일 초임 외교관 교류사업 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788288&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관, 국가철도공단·한국공항공사 신임 기관장에 임명장 전수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788287&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 겨울철 대비 풀사료 생산단지 조성 시범 농장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788285&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 알디에이(RDA)승용마, 어린이 승마체험 인기몰이 톡톡 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788283&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 순환식 양액 재활용 시범 현장서 농가 의견 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788281&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 다자간 '업무합의'로 '노지 스마트 농업' 현장 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788279&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 스마트 농기계 국제 협력 강화··· 세계 시장 진출 기반 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788277&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 한중 정상외교 성과 1년 만에 결실…한국산 단감, 첫 중국 수출길 열렸다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788273&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 외래 품종 의존 높은 팽이버섯 시장, '설단'·'아람'으로 국산화 속도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788274&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 지방정부와 함께 공정하고 균형잡힌 출입국·이민정책 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788271&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농업과 에너지의 새로운 동행,  '영농형태양광 상생한마당' 열려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788268&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(기상청) | '감기'는 노래로, '한파'는 대비로! 기상청, 이기찬과 한파 피해 예방 캠페인 전개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788272&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 유관기관과 함께 가을철 산불예방 캠페인 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788270&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 전기차 넘어 인공지능(AI)·로봇까지, 지식재산처가 학계와 이차전지 산업의 해법 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788267&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 주요 5개국 지식재산 심판제도 변화 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788266&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 현장의 목소리로 디스플레이 특허심사 품질 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788265&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국민통합위원회) | 통합위, 「청년통통 함께 토론회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788263&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 코리아 그랜드 페스티벌의 온기를  골목과 중소기업으로 !  이형일 부총리, '코그페x행복한백화점' 현장행보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788264&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 이종욱 관세청장, '코리아 듀티프리 페스타' 현장방문 및 면세업계 격려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788262&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 반도체 전문가 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788260&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 제8차 여성과 함께하는 평화 국제회의 개최 예정(11.11.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788261&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰대학, 경찰학 교육·연구 협력 강화를 위한 연합학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788258&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 「(약칭) 초광역특구법 관련 원포인트 사회적 대화」 제7차 실무협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788256&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, ?제19회 사이버치안대상 시상식? 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788257&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 주요 전자상거래 플랫폼 4개사와  업무협약 체결... 역직구 활성화 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788253&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 청양산림항공관리소, 부소산성 찾아 규제혁신 현장지원센터 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788252&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 정부와 퇴직연금사업자가 함께 안정성과 수익성을 갖춘 퇴직연금 생태계를 만들어 나가겠습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788255&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국기술교육대학교, '2026 STEP 학습 우수사례 공모전' 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788254&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | "방송미디어통신위원회를 사칭한 사기메일에 주의하세요" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788246&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업현장을 이끄는 힘, 여성공학인의 도전과 성장을 지원한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788250&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 지역 맞춤형 외국인정책, 중앙･지방정부가 함께 모색한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788242&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 제6기 사업재편계획심의위원회 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788249&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 톡톡 튀는 인공지능(AI) 아이디어, 산업현장의 미래를 바꾸다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788243&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부 장관, 中 산둥 찾아 우리 소비재 수출 판로 직접 뚫는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788248&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "단풍철 산행과 함께하는 산불조심"... 영주국유림관리소, 가을철 산불예방 총력대응 - 11월 1일부터 12월 15일까지 '가을철 산불대책기간 운영 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788241&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 한-네덜란드, 첫 과학기술공동위 개최  첨단 과학기술 협력 본격화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788239&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국고용노동교육원, 2026 한국산업노동학회 가을학술대회 공동 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788237&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관, "주택건설업계와 적극 소통하며, 현장의 어려움을 신속히 해소할 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788259&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 김영훈 장관, "성장의 성과를 국민이 체감하는 일자리로" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788236&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 국립보건연구원, 한국장기이식연구단 공동 기자간담회·심포지엄 개최(11.6.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788235&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 환자 자기결정권 및 존엄성 보장 위한 생애 말 의료·돌봄 공론화 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788230&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 부산 불꽃축제, 관람객 안전 최우선으로 빈틈없이 관리한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788232&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 현재 유포되고 있는 부동산 대책 관련 게시글의 보도에 유의하여 주시기 바랍니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788229&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 대학생의 참신한 아이디어,   미래 도심항공교통(UAM) 이끈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788228&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 자생식물 '기린초' 수면 유도 효과 밝혀, 지역·기업과 산업화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788226&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 제주 나물콩 '해찬' 기계수확 연시회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788224&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 더 다채로워진 가을의 색, 경쟁력 갖춘 '국산 국화' 선보여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788222&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동부지방산림청, 봄에 심은 나무 가을에 가꾼다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788219&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 실내를 넘어 유적 현장으로… 국내 최초 야외 확장현실로 되살린 백제 미륵사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788214&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "통학 안전 확보와 주거환경 개선에 방점!" '조정'을 통해 GTX-B 공사 정상 추진 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788212&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 미래 세대가 함께 지키는 국가유산 '2026 청소년 국가유산지킴이 한마당' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788209&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 자율형 인공지능 이용 환경에서 철통 인증을 적용할 수 있는 안내서 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788207&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "국민연금 궁금증 풀고 혜택 챙긴다" 보건복지부, 청년 소통 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788211&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-보스니아·헤르체고비나  경제협력협정 발효 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788206&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 한-브라질 정부 간 협력 결실··· 국산 라이신(사료첨가제) 브라질 첫 수출 성사! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788199&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한국언론진흥재단 신임 이사장에 권태선 씨 임명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788200&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 숲에서 시작하는 여행, '대한민국 구석구석'에서 만나보세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788202&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 덜 짜고 덜 단 식품, 이제 더 다양하게 선택하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788203&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 희귀질환 치료 위한 신속 등재 대상 약제 5종 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788196&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 연구실 기술이 실제 현장의 제품과 서비스로 국립재활원, 자체개발 재활기술 5건 민간 이전 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788195&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 재선충병 방제약제 공급방식 등 개선 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788194&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "불편을 호소하는 '국민의 목소리'에 '제도개선'으로 답하다." | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788192&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 2026년 제6회 동부지방산림청장배 트리클라이밍 챔피언십 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788191&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 6개국 유엔참전용사와 유가족 등 36명 대한민국 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788189&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 국가보훈부， 독립기념관과 자회사 통합 추진으로 체계적인 서비스 제공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788188&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공정거래법 시행령 개정안 입법예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788187&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 의약품 허가·심사 수수료 현실화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788186&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 한센병, 질병의 역사 넘어 인간을 보다 한센병박물관 개관 10주년 기념 학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788183&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청 시설공사 주간('26.11.9.~'26.11.13.)입찰 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788184&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 한-중 실버경제 협력 국장급 회의·기업교류회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788178&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과학관으로 온 첨단기술 원정대 아이들의 손끝에서 미래기술 만난다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788208&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 역대 가장 강한 엘니뇨 발생, 올겨울 동안 지속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788185&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 인플루엔자 발생 다시 증가! 어린이·어르신 예방접종 서두르고, 의심증상 시 신속한 진료 당부(11.6.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788182&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 털진드기 활동 증가 시기에 따른 쯔쯔가무시증 예방수칙 준수 당부(11.6.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788181&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 나이지리아 에볼라 해외유입 확인, 국내 유입 대비 검역망 넓힌다(11.6.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788180&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 제276차 대외경제장관회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788176&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 인지청구소송 중인 한국인의 외국적 혼외자녀 및 양육자의 체류 어려움을 살핀다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788175&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, '연조직고정용장치 허가심사 가이드라인(민원인안내서)' 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788173&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] '대국민 단짠 탈출 공모전' 최우수 작품은 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788172&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '2026 코리아시즌', 태국·베트남에서 '케이-컬처' 빛나다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788167&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '2026 인문문화축제', 인공지능 시대에 '인문지능'을 묻다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788166&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 신생아·소아환자의 치료를 위한 긴급도입 의료기기 신규 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788171&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부 공관장 인사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788174&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 독감(인플루엔자 A, B형) 진단키트 품질검사 결과 모두 적합 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788170&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립산림과학원, 제21회 전국 산림생태복원 기술대전 최우수상 수상  - 멸종위기 고산 침엽수종의 현장 복원 성공 사례 인정 받아... | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788169&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 전국 의용소방대 산불예방 총력, 전국 동시 홍보(캠페인) 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788165&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 강의실을 넘어 세계로, 반도체·인공지능(AI) 인재 한자리에 모이다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788164&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 철도안전법 위반 철도운영기관 및 철도차량 정비조직 등에 과징금 부과 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788163&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | '26년 공간정보 품질관리 수준 15.9% 향상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788162&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 코리아그랜드페스티벌x행복한 백화점 현장행보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788233&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 긴급 시장상황점검회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788234&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | [보도참고] 세계은행그룹 부총재에 두 번째 한국인 진출 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788198&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (인천북부지청) 간이대지급금 약 1억 3천만원을 부정수급 및 추가 편취 시도한 사업주 구속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788161&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 전남광주 장흥 육용오리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788177&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 유네스코 세계기록유산 아시아태평양 지역목록 2건 등재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788160&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 전국 유망 소공인, 성수동에 모인다 중기부, 무신사·오아시스와 판로개척 성과보고대회 개최 - 2026년 소공인 디깅위크(DIGGING WEEK), 11월 4일 개막 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788158&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (설명) 전주MBC, "'사망사고 은폐 시도' 노무사..자료 넘긴 노동청 직원도 송치" 기사 관련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788157&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 차관보, 영국 의회 대표단 면담(11.5.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788155&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중소벤처기업부, 신임 소상공인정책실장에  조경원 창업정책관 발탁 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788156&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)「첨단 디스플레이 국가연구플랫폼 구축사업」 예비타당성 조사 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788125&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 「제3자 부당개입 문제해결 TF」 7차 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788124&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 핵융합, 해양용 용융염원자로 등 예타 통과로 7대 미래 전략기술 사업(7대 시드(SEED) 프로젝트) 뒷받침 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788120&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 강원특별자치도 양구군 소나무재선충병 신규발생에 따른 긴급 중앙방제대책회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788122&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부 중남미국장 베네수엘라 방문 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788123&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 고혈압·당뇨병 등 만성질환 관리, 만성질환 통합관리센터로 전국 단계적 확대(11.5.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788117&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 김용석 대광위원장,"하남교산 주요 교통시설 적기 구축에 총력" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788116&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(기본사회위원회) | 사회연대경제연계전문위원회 현장간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788113&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(기본사회위원회) | 기본사회위원회, 한국법제연구원과 기본사회 실현 위한 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788112&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 'AI·데이터 행정' 산하기관 협력 체계 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788115&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 「모두의 토론회」 로 모은 국민의 목소리 "AI 시대 개인정보, 유연한 처리·명확한 고지·확실한 거부권 필요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788109&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 숲에서 찾는 지역상생의 길 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788106&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "산림 R&D로 개발한 다목적 산불진화차량, 육군 전력으로 거듭난다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788104&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 에이전트·피지컬 인공지능(AI) 시대의 개인정보 보호, 기술에서 해법 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788108&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 유망 심층 기술 창업 초기 기업, 정부와 민간이 함께 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788119&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농업혁신을 이끄는  2026년 '신지식농업인' 5명 선정 및 章 수여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788102&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 26-27절기 가금류 고병원성 조류인플루엔자 첫 발생에 따른 인체감염 예방조치 및 감시 강화(11.5.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788101&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 국제기구와 함께 식품 안전사고 위기대응 역량 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788107&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 현장경험은 나누고, 산림생태복원 기술 더한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788100&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 산·학·관 협력으로 임상시험 통계 전문성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788098&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 「2026 대한민국 드론 공방전」 본선 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788097&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 국제 공동연구 추진 및 연구자 교류 확대 등 한·중 전통의학 글로벌 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788093&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 반세기 봉사부터 2조 원 기부까지… 나눔 실천한 132명 '대한민국 나눔국민대상' 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788094&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(경제사회노동위원회) | [보도자료] 소규모 사업장 안전보건관리자의 활용을 위한 방안 합의문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788096&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 감기약 속 마약류에 노출되는 청소년… 관세청, 국경부터 철저히 단속한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788091&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 제5회 동행프로젝트 「우리 같이 숲길을 걸어요」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788090&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림정책 발전 위한 민관소통 이어간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788088&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 원주교도소, 47년 만에 새 보금자리로...새로운 도약 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788085&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | '동덕여대, KT 등' 다중이용시설 테러 협박 불법행위에 대한 손해배상 청구 소송 제기 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788082&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 대구-경북, 미래모빌리티 산업과 일자리를 하나로 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788084&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청·한국피해자지원협회(KOVA) 공동 학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788081&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 건설근로자공제회, 취약계층 주거환경 개선 사회공헌, 「희망 뚝딱!」 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788083&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 국립나주병원, '청소년 행위중독'  과학적 해법 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788078&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | '국민이 어디서나 안심하고 치료받는 공공보건의료체계 확립' 위한 정책 의견 수렴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788077&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 2027년도 기초연구사업 2.91조 원 투자 총 과제 수 18,516개로 역대 최대 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788076&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 정보통신기술 고급인재양성 연구센터 신규 개소 및 공동 현판증정식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788075&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 라이즈 아시아 이니셔티브, 민관 손잡고 아시아 에너지 안보 새 판 짠다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788080&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 재활용 가능한 차세대 항공기 소재·부품 기술 산학연과 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788079&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부·국방과학연구소, K-MOSA 성과공유회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788070&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.5.행사시작(13시)이후] '안전한 방사선, 건강한 국민' 「제1회 의료방사선 안전의 날」 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788067&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 로봇 기업 인사 담당자가 직접 부트캠프 학생의 취업 상담에 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788063&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 2026년 직업계고 졸업자 취업통계조사 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788062&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 대한민국 미래 성장동력을 뒷받침할  7대 미래 전략기솔(7대 SEED) 등 심층기술 창업·사업화 축제 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788059&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 국민의 알 권리 보장은 두텁게  정보공개 문화는 건전하게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788065&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2025년 다문화 인구동태 통계 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788061&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 결혼분야 모니터링 최종결과 및 위반 사업자에 대한 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788058&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(감사원) | 재외공관 재외국민 보호 등 운영실태 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788060&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 스트리밍의 미래는? '국제 OTT포럼' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788056&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 평화가이드 꾸꾸와 시간여행, 「경주에 평화온담」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788066&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 다세대·오피스텔 층간소음 차단 기준 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788052&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | '26년도 제2회 건축사 자격시험 합격예정자 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788051&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 권대영 1차관, 「기업활력 제고 TF」 첫 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788055&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부, 포괄적·점진적 환태평양경제동반자협정(CPTPP) 관련 어업인 현장 목소리 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788050&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 전 세계 곳곳으로 K-씨푸드가 찾아간다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788049&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농업기상재해 정보, 이제 '농업e지' 앱으로 매일 아침 자동 알림 받으세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788048&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 첨단 농기계 시대는 더 빠르게, 농작업 사고 위험은 더 낮게 '농업기계 검정기준' 고시 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788047&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한국, 싱가포르 및 뉴질랜드 3국, 복수국간 그린경제협정 주요진전 평가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788053&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 명장의 손끝에서 도제학생의 꿈이 자란다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788046&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 사회적기업의 성과와 새로운 도전, '밸류업 데이'에서 만나다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788045&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 오송역에서 국회세종의사당까지, 버스 한 번에… 간선급행버스(BRT)로 달린다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788043&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산으로 키운 지역 새싹기업, 투자유치로 잇는다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788044&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 국가 지식재산 정책 이끌 제8기 전문위원회 공식 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788042&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | K-미용의 세계 1위 도약, 지식재산이 뒷받침한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788041&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 경주 소나무재선충병  방제전략 마련 현장협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788039&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 2025년 호스피스 신규 이용 환자 26,020명으로 전년 대비 1,702명 증가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788040&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 11월 '이달의 임업인'에 강원 정선에서 마가목을 재배하는 이정수 임업인 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788037&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 현장의 아이디어와 AI로 임업직불 행정 혁신 속도 낸다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788035&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동화를 정원으로 펼친 청년들!  2026 정원드림프로젝트 우수정원 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788032&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 기술환경 변화 등을 알기 쉽게 반영한 안전조치 안내서 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788033&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 6.25참전유공자들 미8군사령부 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788024&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | '통신분쟁 급증' 이용자 피해구제 강화 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788027&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 산불 통합지휘본부 훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788030&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | '전국 병원체 감시기관 한자리에 모인다' 감염병 대응 성과와 개선 방안 논의(11.5.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788021&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 방산기업과 원가제도 발전방향 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788018&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방홍보원 KFN TV 위문열차 해병대 연평부대 공연 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788054&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 국내복귀 포럼,  기업과 지역을 잇는 투자유치 플랫폼으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788017&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산불 대응! 과학과 현장의 연결로 강화한다 - 국립산림과학원, 가을철 산불조심기간 맞아 제4회 미래산림포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788020&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(조달청) | AI로 구매실례 검색부터 견적 요청까지 예정가격 작성 더 쉽고 빨라진다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788016&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 유진이엔티㈜에 대한 ㈜와이티엔 최다액 출자자 변경승인 청문일시 통지는 청문 주재자의 독립적인 결정입니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788014&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 고위험군 소아·영유아 코로나19 국가예방접종 시작 안내(11.5.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788013&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "영구임대주택 임차인의 권익 보호는 현재 진행 중"… 이번에는 여수로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788012&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "종이헌혈증 대신 모바일헌혈증으로"…  대국민 설문조사 통해 '국민제안'으로 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788011&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-08&endDate=2026-11-08&srchWord=&period= |  |

## collect:out_of_window (32건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 국민참여입법센터 | 법인세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-07) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88012 |  |
| tax | 국민참여입법센터 | 법인세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87940 |  |
| tax | 국민참여입법센터 | 부가가치세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87934 |  |
| tax | 국민참여입법센터 | 소득세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-07) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88010 |  |
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

## collect:tax_subject (36건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | 2026년 부동산 세제개편안 주요 내용 총괄표 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9VV05RWWFtWkNqZmNWQktodVFiLS1GckNYcXZ6SGUxcFc5dXhEQi0tN0FmM2tucEROdHF6OU4xUnpmd1NXd29fQUpnMkdRbnVac2pqOEsxUTBaN1JWdjcyVjBHOUE?oc=5 |  |
| tax | karnews.or.kr | [세법톡톡] 2026년 세제개편안 (양도소득세) - 한국부동산뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Ub0liX2hObkdsdUhZc3lES3AycE9NV2xfVHBvMDJNYXpkbkVZNi1FdlZKcklqUndyX0xoZXB1OUFDdHNkZWNHa1BQN1FWMHBMUlZhV2V1ckpvRWUwZVpzZFctNllmUFd3bHZB?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | daenews.co.kr | 정부 세법개정안, 세수 얼마나 바뀌나…국회서 여야·전문가 토론:동아경제신문 & daenews.co.kr - 동아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1zamFET0V6bVlRR1NOd3A5OWk2UFc0anBVbUxMSEN4WGJHWGk1ZUVTemRXMVpQSHZRM1ItUnFKOFd0cEdNc0ZEYXhORlNWdVJzakZJUFJ4b1l4RGc2d3lCUFJR0gFiQVVfeXFMTXNqYURPRXptWVFHU053cDk5aTZQVzRqcFVtTExIQ3hYYkdYaTVlRVN6ZFcxWlBIdlEzUi1ScUo4V3RwR01zRkRheE5GU1Z1UnNqRklQUnhvWXhEZzZ3eUJQUlE?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | m.kbsm.net | 세제개편안 29일 만에 유턴…비거주1주택 종부세 공제 12억 유지 - 경북신문 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE5ub09KcURLZ3Mwd0tCOWxmMEg3R2tNSlFHV2c3NDhFOVdjWW05bTdRWG8wVk1OaktGY0VJMTdQdG9oS0xCS3NFXzlMd1NIQVE?oc=5 |  |
| tax | newsk.net | 세법 개정안의 주요 변경 사항 : 한인동포신문(몽골) - 뉴스케이 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXdlRVQnREMG5BcGNrUjNUdF9MSEVtbGJzdHBuWjNBM29ZTDBtYXY5TWw4Q1F4OG1QMlVSZnQ1YTNYMEpBcmJKX1hhTDJOczE0UTQ5VnlRY1FmZw?oc=5 |  |
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | womannews.net | 국회예산정책처, 2026년 세법개정안 토론회 개최 - 여성종합뉴스 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9OcGR3NHp2Xy0wMVE4RGt6ekE0RGoxM1IzOXRnTmZnUWZ4UzhrQ25uaDFSdWRJcnFDd2NwOTBDdEMwc2xySy03aTNXMGlaUDVTakplV3I5T1U0Yk1BVnd2RFlpdTE4QjB1UzZ3R050Yw?oc=5 |  |
| tax | newsis.com | 이형일 부총리, 세법 개정안 관련 제안설명 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE14d2tkM2pvUlBhZ1lJRlFtdVVoWnU0RVd6X3Q5UWhQWC1VcHJiSUJJWTAtRFpCSjY2Z3ZCV25id2cwSGtYX3pDemxTVEk0YThibk90a3MyeVdhUE83QWYwdw?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | paxmedicalnews.com | 2026 세법개정안에 병원계 ‘발끈’… “가업상속공제 제외는 필수의료 사형선고” - 팍스메디컬뉴스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1Dd3lHSEFoSWkzMDJXZVAwcnpDVjkyLXJYa0gwVURLSWJjeGhfTVZnV2pnVTZfdWdqTU1sZU9wM093UDhoT2dmUDdtVThCc3o3VlZEY3lVbzFuQTZCX3N6bHlvSDhrekpTdFFKcWpId3A?oc=5 |  |
| tax | 일간NTN | [판례평석] 구 상증세법 시행규칙 제17조의3 제1항 각 호의 사유가 있으... | http://www.intn.co.kr/news/articleView.html?idxno=2054518 |  |
| tax | thevaluenews.co.kr | 국회예산정책처 “2026년 세법개정안, 5년간 세수 14.5조 증가” | http://www.thevaluenews.co.kr/news/view.php?idx=202849 |  |
| tax | ftoday.co.kr | 국회예산정책처, "세법개정안 따라 5년간 세수 14.5조원 증가" | http://www.ftoday.co.kr/news/articleView.html?idxno=368597 |  |
| tax | shindonga.donga.com | 반드시 챙겨야 할 은퇴자 연말 절세법 ‘1000만 원 룰’ | https://shindonga.donga.com/3/all/13/6444739/1 |  |
| tax | 일간NTN | "세제개편안, 조세지출 재정사업 전환....지원공백 방지·성과평가 강화... | https://www.intn.co.kr/news/articleView.html?idxno=2054550 |  |
| tax | realty.chosun.com | "부동산 세제 개편이 민주당 서울 의석 반토막 낼 것" 서울 민주당 의원... | https://realty.chosun.com/site/data/html_dir/2026/11/06/2026110601634.html |  |
| tax | betanews.net | 병원·호텔 가업승계 길 다시 연다…김상훈, 상증세법 개정안 발의 | https://www.betanews.net/article/view/beta202611060055 |  |
| tax | mdtoday.co.kr | 서울 의원들, 1주택자·실수요자 보호 부동산 세제 개편안 중점 추진 | https://www.mdtoday.co.kr/news/articleView.html?idxno=623424 |  |
| tax | gokorea.kr | 서울 지역 의원들, 1주택자 위한 부동산 세제 개편 본격 추진 | https://www.gokorea.kr/news/articleView.html?idxno=884304 |  |
| tax | 서울경제 | 서울 민심 심상찮자…與 서울 의원들, 정부 부동산 세제개편에 제동 | https://www.sedaily.com/article/20110926?ref=naver |  |
| tax | newsis.com | 與 서울 의원들 "1주택자·서민 보호"…부동산 세제개편 당정 추진 | https://www.newsis.com/view/NISX20261105_0003857035 |  |
| tax | news1.kr | 與서울시당, 부동산 세제개편안 당정협 추진…"3주 안에 결론내야" | https://www.news1.kr/politics/assembly/6344781 |  |
| tax | sejungilbo.com | 세종, 18일 기업승계 세미나…세제개편·오너가 세무조사 대응 짚는다 | https://www.sejungilbo.com/news/articleView.html?idxno=60976 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

