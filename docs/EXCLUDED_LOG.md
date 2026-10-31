# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-10-31 10:19:02 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1679건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:blog_community | 1 |
| excluded:category_cap | 18 |
| excluded:company_event | 1 |
| excluded:company_self_activity | 2 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 28 |
| excluded:financial | 2 |
| excluded:industry_specific | 7 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 98 |
| excluded:no_regulatory_signal | 48 |
| excluded:opinion_piece | 1 |
| excluded:similar_news_merged | 18 |
| excluded:smb_only | 1 |
| collect:event_announcement | 12 |
| collect:incident | 4 |
| collect:law_name_mismatch | 5 |
| collect:no_category | 21 |
| collect:noise_keyword | 1 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 206 |
| collect:out_of_window | 34 |
| collect:tax_subject | 40 |

## excluded:blog_community (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | brunch.co.kr | 외감법인이면 만사형통? - 브런치 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE8zcGFYUXpjSUZPcF9lNUxuY25hT19oMDJqTDFxSXk3MVNVOS1hUldwb19pNC1lRlcxb2taR0pYQ183QnJTdi0xMm5kc2ZoVl81ZE9J?oc=5 |  |

## excluded:category_cap (18건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | "지속가능성 공시기준 이달 확정"...로드맵도 “조속히 마련” - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1ZTFNyYnk5b29fZndlSVBFUzZaWkJkQnNvUFQxU1hiNVJqNVNULWMtelNJRl81R2VjYkdtZm1OMjR1a0s5OHNvRnBoUGZyS1hjRlRoSklnaEpfX2RNSWNCUTZobmRGY3FrQTltNg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ESG경제 | 회계기준원, KSSB 기준 확정 발표..."기후공시만 의무" - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB2cWxadWxVWDJhT1hOUkczdU1WWGtZWlNKdVlPbmIzTVc4c0hMVlVzV3lzd0RnZjR6eEtNY1VaU05XQzBiMmUxbnBSRFE4SjdfMHNpYWdEN1hvWmRuVHY5b1g2ekZPZzdFbENVYQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ESG경제 | [단독] 지속가능성 공시 로드맵 내년 1월 발표 계획 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5wNV9rc2dQMTJKQTVLcnpSbmY2R21OYjRuUzBCSjU4YnNVbGdJMUtsRm53NGlKYVZ5bXg0a05wbmlfYnJzT29UR3R3N2JHaHMxQ1ktdmVxTk5rLXBIWUdDeHJ0bW9oU0haUkliQw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성 공시 제도 로드맵 초안 및 확정 공시기준 주요 내용 - PwC | https://news.google.com/rss/articles/CBMif0FVX3lxTE1Gd29wMWxoczQwX09wRThxRzhCam43V3VTRHp6LWFzQWgyZUdjeTF5dzJBZUJoYnlLZFdYWEZlbWVmRDNEcHM5eGVpTGhPSThiUEtkNlpBTlVVb2laR1FlSnlCa2ZBeG5uWFFvaHNfdG9LeExxeFRLc1ltdXgzcmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | womaneconomy.co.kr | ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 | https://www.womaneconomy.co.kr/news/articleView.html?idxno=259937 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 로드맵 공개…주요 내용과 업계 반응은 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5QTEtfY0U0dmlsWDJRenJ2WVYzYkR3MHk2cHdJS1R4T2VXQUs3X1QxZFhtclN2T1lydjhPZ2pUaVdyVGhIM2gzQWs2cUMtOVVvWF9DdUh1b0NTY1FWaWpVM3pNTTRUaWx2bDdKSdIBcEFVX3lxTFBrczh4Q2VrTEdUWXdpeTJYUE9rMDYyaHc1VnF4NndNeGplTUFtQnhlSnB2ck1JdHR2aFpEZ3hPMlhpNnRwX2FNcl96UFZLbFlGVTZhMG1zalkwQ182UjVPemxESWlfdW9vd2hsUk1oSlk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 |  |

## excluded:company_self_activity (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |
| esg | ESG경제 | 아시아 각국, ESG 공시 의무화 '질주'...한국은 계속 '헛바퀴'만 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9iT1p3aDQ1bGItZFl4NDZ4Z3QxVGtEUS0wYnpjZ1BkTmF6MF9aakdtRVpBaGdIN3dUSms2bkxKUlBjU1VkT2NUaDRpNVdEaEExdDZjWkZEQlI0RjFQS0gwZ3IwRTVpTmNHNWJTMw?oc=5 |  |

## excluded:corporate_pr (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | asiae.co.kr | 중대 보안 취약점 방치 땐 CEO 책임…금융당국, 금융사 내부통제 강화 추진 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wVHBFeHhiNjhDb1pVRzYwbXFYTmRrZmhpOFNWS0laVUNkeGZ4NUdGQVY2eGJBWmdlRHJ6SFFsaEM5bW5RQ0FyazRqY0tUWmhnRHJYVjdLSUZwUjJRd2Y3TQ?oc=5 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (28건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBycHhoWWZqWWRDeFVnV3k5UHZWYktkOFRyaUdodjBSV21ZRmhPSzZNaXk0b3JrVW5UbmFzaklYNmtTWFlza0ticG9fS2JRNnl0VFNYQndsLTVxZXY2VDZyRWtzeVdtWXdyTGc?oc=5 |  |
| kifrs | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| esg | 임팩트온 | EU 은행 ESG 공시항목 37% 축소…EBA, XBRL 전산규격 확정 | https://www.impacton.net/news/articleView.html?idxno=30289 |  |
| esg | 임팩트온 | ESG 공시 규제 후퇴 vs. 월가는 기후데이터기업 인수 경쟁 | https://www.impacton.net/news/articleView.html?idxno=30224 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| esg | ESG경제 | "ESG 공시 대응, 기존 지표와 의무공시 항목 통합해야" | https://www.esgeconomy.com/news/articleView.html?idxno=17084 |  |
| esg | seoulfn.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.seoulfn.com/news/articleView.html?idxno=640152 |  |
| esg | econovill.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.econovill.com/news/articleView.html?idxno=753696 |  |
| esg | 임팩트온 | ISSB, 22일 자연공시 초안 공개…사업장 위치·가치사슬까지 평가 | https://www.impacton.net/news/articleView.html?idxno=30168 |  |
| esg | ESG경제 | EU 역외 지속가능성 공시대상 국내기업 "20~30곳"...KSSB 공시 정보 활용... | https://www.esgeconomy.com/news/articleView.html?idxno=16805 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 권미엽 삼일회계 전무 “ESG공시의 복병 ‘보고서 일정‧... | https://www.tfmedia.co.kr/news/article.html?no=207256 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 백태영 전 ISSB 위원 “ISSB 전면 도입은 기준 통제권 포기... | https://www.tfmedia.co.kr/news/article.html?no=207254 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 주성호 KSSB실장 “KSSB 파일럿 테스트 연말까지…일관적 ... | https://www.tfmedia.co.kr/news/article.html?no=206990 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 권오규 전 부총리 ‘AI‧녹색 전환엔 금융지원 필요…KSSB는... | https://www.tfmedia.co.kr/news/article.html?no=206988 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 최중경 IFRS재단 이사 “재무와 연계성 확보된 KSSB, 기업엔... | https://www.tfmedia.co.kr/news/article.html?no=206984 |  |
| esg | 임팩트온 | 삼성전자·LG전자 등 KSSB 실무진 한자리…연결공시·내부통제 집중 논의 | http://www.impacton.net/news/articleView.html?idxno=20212 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |

## excluded:financial (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |
| icfr | 서울경제 | 카드·캐피탈사 순환근무 강화…금감원 내부통제 모범규준 정비 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5yMmlfZHJmeGF0N3BFaW0tS1NmZUZXM2dEQXBCUmM5NHV5aEJwcXNCN0Z4bG5ZWlhsaGpuU3FGUDgwQlZ3NTRWM3R4QVRVUUcyVHfSAVNBVV95cUxPZ2JSaTVKelZ2S2NNQTQtNzRyaHQzODQ2THVqOWFOVHhVaEltN3NpdmRfR3VIaG9WZzRXanRaOWdndkJHYUFMWDRXUWh4NS1HWVFoTQ?oc=5 |  |

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

## excluded:manual_id (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |

## excluded:news_too_old (98건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | investchosun.com | 삼성생명 몰아붙인 회계기준원…2분기 결산 고민 깊어졌다 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPZWdwcnZLaWNBaTl1c3BFRlZyaG9NR0M5eFZRQzBYb0JBeVRIeWQzODI4VUJQbWlKNWdtX2hlWW56WUd0TEwxWjM2ZnlNWHZIYTFSUHNrUmFidUhOVUhDWU5OTVN6c2tCZ09IZVBZYXdzSEZBaTByVGFRTG9tQ1k3MmxtSQ?oc=5 |  |
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| kifrs | dbr.donga.com | 종속-관계기업 구분하는 지배력 기준 논란 - 동아비즈니스리뷰 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9ZeE1sREktWEhLSjVXQ1VzWTFPNFZad0lxdjVHYWF1aEtrT0YxZ1ltZFhES0EyZWlCcTllNHZBZDJXY3JEVXB5NFlCSlVUWnFMNlFtQVVHdnlSRlVCT0lzS1dIVGl2LWs?oc=5 |  |
| kifrs | yna.co.kr | 회계기준원, 회계기준위원회 비상임위원에 이경호씨 선임 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5FWVlpcHAzaUlmSWt5ejZaMnVUYjFwaVM1YWZ2MFVITVVfNG5ZVTNrYUFPMUdQcDRUYURMZ3lzNTRNMWRsYl9OOFBVVVJXRDhxMHZnaEpubjZjWU3SAWBBVV95cUxQdHpFUU04MjFtTzR2VFRHRmpFZ2xGRUptc1RvSWxCbmNsVk1iOFpoV1EtUUNUQ0UwSDVFMk5kUmpZYXp6NUtJYk01WUlSa2xZMnV6emVmbnB0VDhMRmx0Z2g?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | fortunekorea.co.kr | 글로벌 기업 깜깜이 실적 드러날까… 금융위 외감법 개선 검토 - 포춘코리아 | https://news.google.com/rss/articles/CBMickFVX3lxTE9GQnJfSm5OMk5pOWVUUC14aFBrQUJUZEJuMnVzLS01MU0tM3M5UzA5RzNPTnVfS21iUzI1QzZxNmU0a09iUG1RU0ZEY1hPdUtzNEFDME9pS1JqdmlFZkhULXUyWXh6ejZ5WU8xWTRmMFhYUdIBdkFVX3lxTE1Md0FkSEpRTmxlZENOUXBSRmtDMzBoZjl6dE1xTi1QcmtsN0d0OTR0NXhyVjdGUGpGSlc3dXpoRnNBQldzcWlzU2NzRlhsdlJieGhUS3o0ZUtFcnFTLWdCdmtDbmdaOVVIR0RRMU10LURKRXBIUlE?oc=5 |  |
| icfr | kbanker.co.kr | 회계부정조사단에 ‘10년↑ 전문가’ 포함…외감법 손질 - DFT 대한금융신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBtdGx4aHdKQzluYXROcmN0dUxiRHoxWUd5ck0wYTFPNEhUdXFiUjZYWFhhTjBCS09HNG1FYzNCRi1ySnZDcm1raFpidVh3N0tYaXRqRjZNMEo5bmw2SVV5S1FHWnJfRk9CYUk5Y9IBcEFVX3lxTE9ZN1h2NEU3Y3BCd0VES2QwMzhveXo2SDZPeGdpckdLVUxXcEwxdWJfTTk4WE9ydjBHblNNaTdVWnI0em9IVXloYy1SMlpnc3dUcHdCaC03d3UxQ3dhMkVlUE1KeHY1MXNJQXhqNVNlbTI?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9zaTlJci1iWW1GZ2c3TFFYUUxvS3JWTnZJNXZmQm1rdUhGSzMzUTJvM2hwNlBDdGhKdmJ5WU5ZRnR1MDJIYkl6bTlfZFEtMXE3Q1E?oc=5 |  |
| icfr | tfmedia.co.kr | [감사인세미나] 최운열 회계사회장 “외감법‧공인회계사법상 형벌규정 합리적 정비 필요” - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE5wQ0ltZmZmdENDTnZ1eF9kZmIxRUg4RVJrOFlhN2dQVVgtM0dBcExGRUdjVDRzY3R0SnAzRllzZ3FaaTdaMEh6Q0JvdnFpY2t5eTRNT2x3RVE1c1VmWHNqVmJZTQ?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | ESG경제 | 공인회계사회 새 회장에 최운열 전 의원 당선..."신외감법 유지해야" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5wczU3VWVubFMtUTdpOUI4Sm5XQUozYW9mVjRwQVY5TlEtRE5heC1nSnZrWV8waWZjNktsX2MxZk14TC1sRTdCdUxhbDdtZldlQkhsRElIVFBya25mLW5PLUFMd2xpR3c0X3VV?oc=5 |  |
| icfr | 일간NTN | 외감법인 주주 500명 이상이면 정기공시 의무발생…"IPO 예정기업 유의해야" - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmR1RBZURFNTBjZXVRakRjaWVfRHN6QnJucVdVLWVqaExkcjlReTZYazY3ZExxbGJLX1E3dkhvZ1Q5ei1vRVlZR2stUl92Q1BKV1QwUFpuMExaQnIxNmVrR3dTU1M?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년④)"유례 없는 감사인지정제 폐지해야" - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SYVZyanVjZE9LQzY5OTdsWEtDNWhDMmxFZmh4eGNyYnN5RWZkZmNhdjd4M3Rra1FrRVh5dVFwem9CUjM1WkpOUlBaSUZ2ZzBzalJnaFN2M0tFSlQzaTJFeQ?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | biz.chosun.com | 신외감법 효과 끝났나… 회계법인, 성장세 주춤 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUm1NS2l2eUNoQmVvMGxQTmIzdDRMRmhWcnBDRkhSMDl3MFdkVGZTNUI2cXRUVENWVkdtRGw0anhYWU1rZk5BRE9vYXhkMG8ycklqbmY1WlBRVk4wcVpPRUw2cVJWeXotSGVvZTltUHk0RFdMcHhVRzNhY3hXNF9zQ1VqZkprMVpF0gGcAUFVX3lxTFBvOXhIVjJnMVdEd2F2bVNnZnRZdkY5ZFJRZU5ESVN0cnlvMk9aYmd5cjlKbTZWTDV2TEF6dG1nTGk5a1daQi0xOE91bno4RUltazMtZUFocEk2d0NkM1h2XzBxYTZ6eHgyMTFQOFNBYW42VUpVZUF4Vlo3cUcyVTZHbWEwLUVLb0J6MDk5OW5uc0tjTVhhZzc0RmlRZg?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | m.ekn.kr | 코스닥협회 ``신외감법 시행으로 상장사 규제비용 15년간 124% 증가`` - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1IR3cyN2t5c0NGQWRqM0k5dnRWSWxyd1VJZDgxQUp0X1FmMjlTb0tiXy0tajI1MWZTNjFabk53Mnl6Z2lJeHdRazRCOXQ5T1ROMVc1RUdGNXNVclU?oc=5 |  |
| icfr | m.ekn.kr | 금융당국, 여전사 내부통제 모범규준 시행...동일부서 5년 초과근무 금지 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzUkZ2RFlzUjE5OUZ4b3ZxOURwN3ZORVo1UWFXTDBrckdQREVSMmVpbUFkU0VqQzlHNkVVVjBvLWRPUURzenpUNkVjZXBrTlpMblpmMDdmWXFjcnc?oc=5 |  |
| icfr | ceoscoredaily.com | 금감원, ‘여전업권 내부통제 모범규준’ 마련 - CEO스코어데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uT1g3UWpVTlBNRkRaZ0lXdFpDT1RuekF3QmIwVlE2NFJaTTJYRmZSaU5fRERFUWdoaldUc3BYZ05pU3h6RldDSFA3cUxpME1nMzRtMG1QWmdrNU1jcUgzRDM2WmdnZw?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년①)회계법인 배만 불린 감사 강화…품질 향상도 '낮다' - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBTdWt1T1hzUXZla043LUxoallBVWtGRHpDOHA0Nnh2c1pXRk16dVR4MUM2UHdBcUx0SXhvZFVDWFQ3QktDd2gtcUxzbWExTnFvQWxLam1KMkVXQnRiQ05XSg?oc=5 |  |
| icfr | paxetv.com | [1분 영상] 최운열 신임 공인회계사회장 "회계투명성 높이려면 신외감법 유지해야...감사 비용은 투자" - 팍스경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9tWWdmYkxZY2dXTDVBV2xJeFUtLXU0S213RklleTJDZUlCd0ZSQTFyc0FPdjVhYXBGZjBQTXNaUHNsYXpGMzZlMWNMNGMyVlZSNWc2WEd6c0NtX0VibnVjVXphVmdpbldj?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | investchosun.com | 두산에너빌리티, 회계 논란…신 외감법 이후 강화한 제재에 치열한 공방전 예고 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPd3hmMGM1TkJ4dFQwVkt5a3hmYmdZbmctQy1GYnpoR2JyUGN1MURsVWFyUWhtVENCaF9wUk1wZW5sYWhXSmp2OTBLeHFQN0pPRk5ESnZHTndNXzJzbmFjc1E4aTlzcXJOLUNKV3I0UVhhNXdFVS1wbUMtYmR3TElGVTRCMA?oc=5 |  |
| icfr | tfmedia.co.kr | 기업 재무담당자 70% 이상, 신외감법 ‘긍정적’…회계투명성 대폭 개선 - 조세금융신문 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5BeFRkTl9qUGNmOTNkX1R6UlcwYXZzYTFIc3NHdklsRGZ1N2NUd00yRjVmYUI5TDdNSVRwZlhxY0gxMHhqWjlnbk9NUWJqeG1UZU1uYThRSlM5R014YlJBRjB6N0lXUQ?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | biz.chosun.com | 대우조선해양 회계 조작으로 도입된 ‘신외감법’, 기업 부담에 소폭 후퇴 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNQmQ5eVo0TEJUNlRkN19FSjNSZUtkM3dRVnNJZ1Fyd2o4cFBJUlVFU0xMRTNhSFpSRjhkWlVvV1VUMjJXYjhuSnFzc1gwdW1WWlhUd1RfTHRuNExyc2tka29wOXN2RHBEMDNnNmxqUV9lZ0JJbGRzMkgwczJuLXJ2NGdWeEJoMU9E0gGcAUFVX3lxTE9sZVczell6ZTBVdnVVLVdkam9ZZFJXd2UzNm5oTG4xMlVhMWkwWjFUT21SZHJOVHZuV2ZrU2hhdkpBR0NwZGlzV0ZqNEl0bm5sZkJKXzA5Szc4X2h3WGppQi02YXhVNy05Um9EUzFCbUpsVGdFOXRlZ2JXdElVeGJZTnhkdnQ1cTdhMUdsWXZUMEJDaC13RTJoLVN5cQ?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | 머니투데이 | 신외감법 주도했던 회계전문가…'회계기본법' 제정까지 힘 싣는다 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9zZ2tGSkR1eU54TFk4RnYyTUlzcFhjbWNDdlpuTHkxNUppQnVQdHhQcjRtY1RsT2JkT0xudVpxdlVHSG9MSW9nWDhNa3FvRS1pUl9qTFlRcUtQMkRUY3hqSHphMTNRN0Yz0gFuQVVfeXFMTTlSZmpjcWZ5eDdQZTVwRjZPQzBmSXFScEN0bFlyanVlLUlTdGN2Mi10alpTZTd5ckVxei0zTGxWLUNPQTVISTNhb05PeUpXaFFwcXRHTzdUYm1xRG5zSDRLcUxsUXlVcy14LUhqQUE?oc=5 |  |
| icfr | 일간NTN | 우리회계법인 공인회계사 외감법 위반 감사업무제한 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1KdDNUR3BQVVl1dGtYZ2prUllIQVhuOHVKYXdKcW4xbmUxQk5LaExyeXFyMnp5ZTZSTG5TN0RENEp5NEJWeHRNSlVjRjEyMDNsc0x3Q0NRNEZrSDBuejVxNXczOHd3RHA4VWc?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | byline.network | ‘신외감법’ 적용받는 유한회사 – 글로벌 빅테크 기업들 - 바이라인네트워크 | https://news.google.com/rss/articles/CBMiTEFVX3lxTFA5WXBCTzF6LXIyb3R6MDNzazViYWVBNzVjOHVCMlJncXdyUTdxQmdmMTFPNVpNckVFYXBlTVp5TkFZY0MxcWROUy1NdDk?oc=5 |  |
| icfr | newsis.com | 초유의 오스템임플란트 횡령, '신 외감법 무용론' 번지나 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SR1lOd2VmanJnVW9FQXRwSVJYUlIzSkNnRndGNEcyRmlxUGxiUUE4VHkyZUwxbFZOMk1wMWZ0dXh3QUlkOXlUWHNvYlh2Qm80QlhOMGlydTJvTXNyQVF3N9IBeEFVX3lxTE1CUVJtSHR0MHpJa2JOZ1dtODNsZUp4ZlEtZ0g0ZEFpNDVzNHM5RlZndGdpS2xoc3hDcUVuOUsybGxVQUotSzJmdlRadEdPX1lhMlVMTzN2RzJaakNuWmJrZko3ajBfbmVNVXZ6eWpOemh4ZVNrOWEzcQ?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | 일간NTN | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - www.intn.co.kr | https://news.google.com/rss/articles/CBMiakFVX3lxTE5BbndhQ0dRSk5hQzluRU90Y29uci1RdFJ3SHlBTTZGY2U3c05mRlZOVW42bFlDYVBYMmdhSTgyQlJidjQzd2FZZHQ4eDFvMFlzLUdneHNkLWYtMjlsdHJTdXZjSkxNQUtuVnc?oc=5 |  |
| icfr | 매일경제 | “외부감사 대상인지도 모르는데”…감사인 선임부터 하라는 외감법 - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBfb3RIa3ZJZXVfMGlqNXVPSzh1bXhyMDdxRXY5Zm9tM2xselczNFhncmwwWGk3VE1McW5RZ1cwY0tydHBEdW5oRWpfUm9JMEVINFdhUg?oc=5 |  |
| icfr | zdnet.co.kr | "중견·중소기업도 '신외부감사법' 곧 적용...미리 준비해야" - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE94ODR2UVJKYTdMMjEwVWZRRW9vUlFQdkc0enB5RFBiVTgxRjBKUENtLTFUeXpneU5nZ1k5THlfa05PZWdZZTAyZFFVZFBmaEt6MFlJY2h3?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | ibtomato.com | 신외감법 시대…발등에 불 떨어진 코스닥 - IB토마토 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1wTnhJTjNyNlBDcXBLejBQRm16NmxYYjlGa2htY1poZkVTTVVMcGFkNW15M2xwMUFYRDZlLUN1SEE2M3JpT1oxZ3MtYlFIai1nWHdKTTlkVDB5VFlUTVR6MnAxVFJWendn?oc=5 |  |
| icfr | 일간NTN | 여전업권 금융사고 예방을 위한 '여전업권 내부통제 모범규준' 시행 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5YVW5sNE1GN19VOTFHTVd6OGxFWE04LTA1d09Id25RTVd4VVhiU2pQdlAwRGlaUklEZjRzOU5oRDZJWmdDTGJ3ckU4U3Y5Z2t5OXVEUF8tdnY1WVFHQjFaeFYzYzVxa2RjbFE?oc=5 |  |
| icfr | fntimes.com | [프로필] 최운열 한국공인회계사회 회장…신외감법 주도한 전문가 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE4wWUZmaWJVbHVCRHNmQng0VFYxZG9kTGVuQmhqSmtlekt4MEZtODRIWTU0ZjhYczd1dzZIaWlCTzJBNURnWVJqRmp3ejA3end6ZUZMTzZtbkxYMmV6b2dCQWJKVGRjc2QxV2dUVUdSSWNydy1YdndvbzBZTWg?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | tfmedia.co.kr | 新외감법 국무회의 통과…자산 또는 매출액 500억원 이상 법인, 외부감사 대상 - 조세금융신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE9vTG94WUNKczB1eWVZX0tpbmFISWhGU2NOS0VCOE9oMG9FMjBpTFVyWHFsNjdXbVAyNkJPUVBwcC1OdlR0NTBIaEl0WGtXWUhlZUtiNVFuWkd1RW9OQ3hhSzZB?oc=5 |  |
| icfr | zdnet.co.kr | 더존비즈온, 내부회계관리제도 시스템 'DICS' 출시 - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ZWDVfQU95b2dIdy1LZE1MZWxXRUNPY3gzTUxjLUNMdDVjU0draEpfMWZJOEJzN1gtb05BVUZiNE1xODV3LW5TTmR0VnA1YnJYV1ZhbEZB?oc=5 |  |
| icfr | fntimes.com | 신외감법 시행 4년차…감사인 선임제도 위반 기업 전년비 177%↑ - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE1scHBINWVyT3R0NmVEdzNYeVAyLW9qaEJic2JFSjlJc1ZHTHdydzlYOHJQRXh3X3Rqa1RqcVlVM0tYREQ5UjBhMUNVbFAzQ3JyTU1obGlkeVRSM0tzV0NSMkcySy1vZlM4TWwyQUplTWNOcWo2aWg0NC1DcVE?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| icfr | etnews.com | 씨에이에스, 新외감법 대응 위한 내부회계관리시스템 'ControlWare' 재출시 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE03bTFIY0VhM3FDbE83bncta3kwdFFMNHFpY1NVb0lZV3drZWpOWUViNzZSekhXM0VxVmJCZ0VPSmdHQTlocUdkY3IzNlNTQQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | news2day.co.kr | “新 외감법, 부담 가중” 경제인 앓는 소리 진짜였다… 감사 보수액, 4년새 2배 '훌쩍' - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Jd2hPSnlTb2h1bmhZbXFvSmI4d1JrZEQwTzV3eFZfX0V5c201YWF6Nlk3YmdhQjlnejN1UjB5TDQ4V1Nfc0R0aUdUTjludGN0QzF5MW9OTl96ZUhtWGc?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | fntimes.com | 삼성 등 금융그룹, 내부통제 구축·통합 공시 도입…감독 모범규준 5월 시행 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE5GRTk0ekFOakRta0tINzdwNTFSQU1yb3hzNkRKbHN4dkxVSkwwWXRHa3l6UVBSdFdBV2JxT2JGV2tlbzQ2RU1nUGRIdDVYVTNPWmh6eFJZT2ZaUEJVWGduZXdOOXhiOFFCaWJhQmktelFFcjJ0U3FJS2lpQ2Q?oc=5 |  |
| icfr | itdaily.kr | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 아이티데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE1CODVGNXBKQjRGMjhVY1pUU3JiQXIwU25Ga2NkeU9IR0xaVzlwYXVxdkZSeFVWWG00WXprcHlIRlM4R0ljbFhvWmFMeGRPTlRnbm1uT19JWHdrS1FzdFhTbTJjZEU2QQ?oc=5 |  |
| icfr | ajunews.com | [경계불문 DX] 신외감법 시행에 ERP 회사 더존비즈온 바빠졌다 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DUVhuQ0cyWmN2YmtERDB3aWRYTmVGMGlfek8yQ3lQTVpkTFdMLTZKVkpqZDN6RnhpQUhLcTVUa19CdlROS25TdUdkcU9rc0IyNkRYMUhKM2tIQdIBWEFVX3lxTE5NT1pQdWFtT0RrNS1SbG1Fdmx1SmhJYlVMcjQzSmpMenpNbFhtUWVNZldfc3FyekduZTkyakl0YTlHZ0R4MkZxN002Zy02cWV4cTlGMGlfR1Y?oc=5 |  |
| icfr | sejungilbo.com | [재계리포트] 新외감법 ‘그룹 연결회계관리’ 비상…더존비즈온 ‘EFIS 10’ 주목 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTFAwMkJtZHdlX3lNSUxIMWRMMkNZb0tRbjJkNHF2Sm0zbm5GeFdjeGE0R2RRRFhyX3FSbXJRTXpPVmpBSHlKR0R2NzVPTGtES1pTZjhhd1hkbjNzQ0dXZGFxWVZ4dnZaelltNnZ1Zg?oc=5 |  |
| icfr | thevaluenews.co.kr | 은행권, 비예금상품 내부통제 높인다..."DLF 재발 방지" - 더밸류뉴스 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE1ud2JVUmZLcHFXdHRUcmZfNU5RS0pHZ20xV3BPUU1tOUNiSTBVOG13SEpHcklMMlVNelZuNkY1N19QSVpXTWpTX0xyS3M1TWdyUVFv?oc=5 |  |
| icfr | m.bikorea.net | 더존비즈온, ‘딕스’ 출시 - BI KOREA | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1oSE9NUDlTaGlDenVfdHhWYVZMcVFJSUxGUU95ZHAtNVh6Q1hQSlZSNmVFM3RZWUdDb2ZfZmFnNmpyWm96RUVGOFBWM0RBdXlISlBuSkt2QU9weEYybFZMUkF0TUE?oc=5 |  |
| icfr | etoday.co.kr | 28개사 ‘내부회계관리’ 비적정…“내년엔 더 문제” - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBMOW1idWYtTDJmTzJCazdzXzF6dVRNbzRsYklQaHFSRkc1Zm1MVFRiX0hwZ1ltNHVJTFM4Y0JZYTh1OHc4Zmp5MnkwR2tSYUdYMmo2SA?oc=5 |  |
| icfr | newsis.com | 외부감사인 선임 45일내로 단축…'新외감법'시행 본격화 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9oc0dCbXI4OXR0SU9FSVdXM0ZQOXgxSHZNRGplVFhZX1pUZms0ZFpWWWZnX2RFbEVnWGlIWnBNc0JNUU9KOUxBS1EtczhhTGlOZnFQcEIyUTJkMWM5eTRtNNIBeEFVX3lxTFA3ZXU1SVRsUU4tMDd6ZzcxZnRYU0tIaEJWeUFZclVKVlpUT19HM0Q2QTBxbnRicjJQRHo3ajlxYWx3V3FLMnlrTWRUZS15T0dfTmtqc3NRazdnSGVrMUNPUm9LSWVBQ004TGNpRTZpY05abGpuWExWeA?oc=5 |  |
| icfr | 매일경제 | ‘新외감법’으로 상장사 회계법인 교체 쓰나미-삼성전자 감사인 누가?…빅4 판도(삼일·삼정·한영·안진) ‘흔들’ - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFA5cno2VzNKMGd0UlJ4UjI1Q3hSamxObEItQWNqYThZcElJYm4tR25UZGVOYkhVNUhYcXBMNlpGV1hLQ0hOQUZnck1jdFBHWXlLcXk4Vw?oc=5 |  |
| icfr | biz.sbs.co.kr | 씨에이에스, 외감법 개정따라 내부회계관리운영 소프트웨어 재출시 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE9CdDhZWEJKNm1ZdWRTcDM0RndZMkY5dGo0cjZCU3RucHBFM1BVeUk3cVFzMEF6WGdMWC0yNEsycTNJRWtTYlltcXNIa0pjaTZDaHhn0gFYQVVfeXFMT3lNY1Y5VUxSOHVnU0ZiWEZyb1M1V1ZMVElxZnIyU0U4TlEtTHE5aHVwekdxU2p5amVVcDYtaWpzcHBqUl9JT3RyM0RELVpKTmJ1RzJYSGszUg?oc=5 |  |
| icfr | daily.hankooki.com | 新외감법, 내부회계관리제도 시스템 도입 필요성 커져 - 데일리한국 | https://news.google.com/rss/articles/CBMibkFVX3lxTFA5QzR2eGtpWW1lcWszaUhtc3lvTHp3TDZNc3QxRmJXTjd3RGZYMDM3RXBGZDhic2U4STFJMUYyenBmNHg5YXlBdnV5cm1idHBRR1hBbjAtamhsVDN3Y0Vxb2s2OWNuM05JTWtXS2h30gFyQVVfeXFMT19XcWVUYzd4V3FiRzlBSGJLZXZoeVYzeW1yU1k1ck1yVHh5MlpucFlwMktrSkJkeUhJVjdXRlJ1ekJsRjNBY0gxUU5nczBnRVdvbDUtNktTMVZSNnpXUzk2UXpSQjMxSmc5QXY5YVRrRmdn?oc=5 |  |
| icfr | etoday.co.kr | 新외감법 피해 ‘유한책임회사’로…실적 공개 피하는 외국계 자본“[밸류업 결핍과 과잉](하)③ - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE56V0JDSGxxRXBKTlliQWl4VXl3bWtoWHVJcDZkY0xOVWk2d3R4X25iemVFTVNxbzdjSjBqYktYazlZWkwxbk9hOXRaXzBTS1hOTzFBSg?oc=5 |  |
| icfr | indifocus.kr | 채이배 국회의원 주최 신외감법 중간평가·제도개선 간담회 열려 - 인디포커스 | https://news.google.com/rss/articles/CBMiQ0FVX3lxTE5NNzJ5OUh1RGlfb3NTX3RxcDZlalhqb050ZlRPZ2F2eHYzVWEtSXRRYklDRW85M0k0NmxuSHZnUndUdkE?oc=5 |  |
| icfr | sejungilbo.com | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE8wbVA1bV91THUxeGRfdFo3SzItRkQ5M2RmNDNFeG1QUzZQS0ZQR1RFemphaWRHcVlnbWZHN0FlVy0waWFuMlIta2EwQWJOdy1qWWZIV0drcmJWTEFSLXVpZDZrQVRsQW1YeDBJUg?oc=5 |  |
| icfr | ajunews.com | [기업쇄신]최종만 부회장 “신외감법으로 회계부정 어려울 것 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE04aDRvZjFQWkc5Tl94eFpxYmRaWFczbG5VdHBGREhIN0JaSy1MRnBqZ3hTdlpodmItZHhrR2lsRmpWRTdWdTZkQ0FYUFZkcndwNDF3QnRPbUY3d9IBWEFVX3lxTE8zdlk3LWJBOFZWZzVRbmtsWjhUNU1Sci0wazNJRVZtNDA4VXEySXBzWXhPcWVibmhGb1FDc2hBQjFpSm5PTU5BR2o2VlAzU1F4c1Y5YWtZYUQ?oc=5 |  |
| icfr | 이데일리 | [新외감법, 감사비 논란]①회계 개혁 눈앞인데…보수 놓고 갈등 - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxObWFhT29aS3RIZkJKODZUWEN4WjlGUmIzU3ozU1l1WmZUbXZ5OGxaWjl0eWY0aDg3UEZZRzNfSWtabEkxemMzNUM0dEtpazdjS2ZrM2FGanFhNFowY1JySVFtMXBWbzU4djB4MzNOa285S3prR3pqemZLSmhvcnN1OA?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]뒤바뀐 갑을 관계…회계법인이 '기업 결산능력' 따져 고른다 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxNVEd6emg0SDFlcWI4LWhaZFhwS2tBdVB1TjFQeTkwb3JxRGEtQ3kydmFGSlNIQV9DbXNHdFdCQjVwLW83cnlwZVpOS3Q0ZVFST2U4NnUydGxZUE5OLWRCLWF2RzBnNXM4VjluOFpvd1l3SllFWnpndGhHMGtWc3NWMg?oc=5 |  |
| icfr | 파이낸셜뉴스 | [인터뷰] 채이배 의원 "외감법 개정의 주역이 회계개혁 완수해야" - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9wdUF6OXdLMktRWk9RTlBNaEIybnUzb1NaYmgzTkZ6Q3VLcndXNmRCQlhzeFhyTWFBZnU5WXVIVl9aQWplZFdnT3ZReGkzaDJDMTNVUkJhTXhndw?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]전용석 딜로이트안진 본부장 “회계투명성, 기업과 함께 높여야” - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxPZFh3QnZzRU13RFpUbzRacTJkbi01RVJuU1BuWDJIajBWcnd3UmttSGtfZnZGcFI0QmxEMGtfZmdNc3ItVms4Z3ZvaDlqZ0pFb3NUSTNVSkxVVVIxNE9HdjRlaGx2YkxwOE5HSEdoNFVCV2ZEMkxiWVlvZVRlUGM4QQ?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]윤훈수 삼일PwC 대표 “사람이 경쟁력…최고 지원체계 갖춰” - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxNc2FJOG9IU1IwTnl6cXlQLXJqdm9tVl9sVTVmXzNlNFZLd3dVbUttN1VJSDdDWThEc2FUei1QWnhzSG9hRjY4eG1TRnZiNnBvUVNIM0t1aXk2YlFIUlFiS1UyUzRpaTEtVjV0ZWZMN3QtbVZDSjFUVGNTZGpvYWhGSg?oc=5 |  |
| icfr | 이데일리 | “작년 사업보고서, 新회계기준·외감법 내용 꼼꼼히 기재해야” - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxOdkxseHYwRzUyel9SRDUwcEQ4aW5lNU9lMVBTbVdOTnQya240SUZJVHJKbk1wdHlLWThCTTF5TWJCbm5rSXI5OGFJclFickw4NTh5RzRQTHhKUU1DaGpXa191aDhGSHg2NDZHUDZNYkI5LWRFYm5kREQ1Slc5UjNIMw?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]박용근 EY한영 본부장 "글로벌 협업으로 감사 품질 제고" - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxPX2ZFeGk2NVQxN24tZHRoaThvZlRPdmpiYkFvUklGZXFLUmEtU1VfM0t4QXlkTm5CVHhoY19IQkZHdTZtVU1lSl9QR1dfY09ycmRzM2Z0TWwwdS1WUnVfdkh4NFV6UzV4dUpONjRwRFk5UVRfYmQzQVo5OW41NjdGbg?oc=5 |  |
| icfr | view.asiae.co.kr | 금감원, PB업무 내부통제 모범규준 시행 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFByWmtmZUtmVmM4XzBSZGp1d0ZlRHhSSmk1U3JZSVVvQ0pPaU9Ca2FFeUI3aUxEdXpjREozMTJNVUVFVFdZUTRvVjBBNzExbUJYWmVYZnM1Z05NVHl4ZmZfcnpB?oc=5 |  |
| icfr | biz.chosun.com | '新외감법' 발효되니 '유한책임회사'로 전환한 구찌…'깜깜이' 영업 여전 - Chosunbiz | https://news.google.com/rss/articles/CBMie0FVX3lxTE1tdURoaS1ORzMycmhsNW84VEFZT0d1LWFsdWtVUHhidlFPUUx3RDFLRGFzOVZrLUNnSEtibVVFLTNhMEJJdFdJM2F0SkhqUjFZbUE3TUxjY2ZqTWJ6cHNUM1d1MEZFbGJXLWpqTjAzcjhEemJBUnV0ckNnVdIBjwFBVV95cUxPcWJmNE1aVHNIMWhYc2JEbmtWR2xqN3JMZGVpN0V6SlNYdVgtRlZ5Um0wbWhyU1hMM3EzWTk2Nnc5bXYwN0E1VmVTNVhLNWlTV2VrNm1CVDF2OE1keXZwT2xWb0RBWktrTy1RQVliVHFodkN0VVd3aUlCOVZhM3hKRE1vaUJiUWJueUxOVm55aw?oc=5 |  |
| icfr | biz.heraldcorp.com | “신외감법 시대인데…” 여전히 60위 밖인 한국 회계 투명성 순위 - 헤럴드경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE9FSG1PaDBKX0YyUGxNMU5ZSzhEbWg3SDB1V2JzUzV0dEJ5Rkc4U0xMaThpMkVRako4bm44NGY3UVRMUjZBNWdIRDlYSWNMREhqeElEeA?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | ESG경제 | KSSB 지속가능성 공시기준 초안...'유감'과 '기대' - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5IbzRUeVpVLUVnVUk4MGRxWHBfRmN2ZW0yU3VDYkxLbUdteXFPWGdVb05ueXNwTzBSS0ExSUU2V1BTd0xLYUo4eDlLVjc3LTFJS1QtQVVJNVdtZzNvcHF4UjdsVjFFUHdKZnJJ?oc=5 |  |

## excluded:no_regulatory_signal (48건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | CPA뉴스 | [재무제표 수다떨기] 기업 인수 뒤의 숨은 이야기, 외부평가 의견서와 M&A 공시 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFA4UVFYV2FvWGtPaTZjbVIxQjBESjVJenlJallEaERzQXhUczVGMm1KVmdYb1BwMzRlXzE0dXlhUXA5eS1ya0VwNVFRSnVWM08ybWJlalFfLUUzOUI0OTdVNUlaelFMTEFL?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 매일경제 | ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE4yMzAySUdLM2MzcEFZbEFDMjYzbktLaE1uTUtfS2tGQzRoVWEwcm51OXJ1elZMWWZrd1VaTFNYd2hYb3NsYzdFRVl6SjdMbFZkTFE?oc=5 |  |
| kifrs | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBycHhoWWZqWWRDeFVnV3k5UHZWYktkOFRyaUdodjBSV21ZRmhPSzZNaXk0b3JrVW5UbmFzaklYNmtTWFlza0ticG9fS2JRNnl0VFNYQndsLTVxZXY2VDZyRWtzeVdtWXdyTGc?oc=5 |  |
| kifrs | snmnews.com | [현대제철 IR] 3분기 요약 별도·별도재무제표 - 철강금속신문 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBOWWEyWll4OHFHeG9MWHUyNUdYbksxcnRhZ09jQlFBdE9RUkJnRDk3d0RoWWtQSWhQcGpXU0gyNmJqZF9sUEpORjNDWVhKNkRQZnltamhiVXQzeUFjVDRXZzVvLUlCeEVkZnc?oc=5 |  |
| kifrs | datatooza.com | 하모니 골드, 연간 순이익 두 배…과거 2개년 재무제표 재작성·내부통제 중대 취약점 4건 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE14WWR2eUNqYUluVzhxek9IYXdLSEM5bnBUalFuQnhCYkpzZUdQU3QycjZVTXFzdGs5Nk15LW1IWWZDLUVtREpXTWVpcUQ5elJMblpNa05ESVphVVlDYUYyTFhWaHNiNlJIQU94dkVCNTNQMDg?oc=5 |  |
| kifrs | datatooza.com | 포커스 유니버설, 인수한 오피스 빌딩 작년 매출 296만 달러 감사 재무제표 공개 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE83dTF1SjdwZ2hjSzNrclAxWWxqNGF1cnB4bWRENmV4bDFyRGhiTjI4SVVxclFhUV8zSGFEejFoZlVYV3hzNWc1TzdGNU5tbUxqN3RoRV96cjdoSEdUU2pYVjYyTUtEcWl2Ykp0b3lfWnl6Znc?oc=5 |  |
| kifrs | cstimes.com | 보험사 실적 '고무줄' 논란…회계 기준 바꿔야 - 컨슈머타임스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBKQ1I3ZDI2MzJUVVp5NnBOVTRJNk9PdU5Nb215Nzcya3IxcTRXZ3ZaVV9sMHdiWTg4aE15SmJNWFhBQXhLWm1iWmNJdTlnQWVZdU4wc2Z4UEl6elEtTUsxdDRNSTJ4TjZxVmc?oc=5 |  |
| kifrs | datatooza.com | 오시코시, 3분기 누적 순이익 3억 6470만 달러…2028년 적용 회계기준 검토 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE4yWVB4dWxWNkRZNW9nVmUwLUpfS0NJLTZBbjFXNmF4WElVUmp4c1JpMmdsekwwTVloSzFocnNCbWs1VjBWQkNEekdZN0RJdjIwb1JRWlRaVmwybS1YQ3VTQVJXTnFlVER5dVZlMGpzOVIybU0?oc=5 |  |
| kifrs | newscj.com | 안양시의회 예결특위, 결산 심사서 세입 편성·회계처리 문제 지적 - 천지일보 | https://news.google.com/rss/articles/CBMiakFVX3lxTE56bHVRcjE2MnFTZVhzdmFiaU1pU3IxZG9ScHc0LVZyZzg3YlRuOUNaMUd1aDJCcDlUSXM0UHlMNlhHT1NxUHpJMzE3ZEJNLUNCSWRBbTJCZjBiUDdGVHRRS2Q1bThUbEdaY2c?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 눈에 띄는 LG이노텍의 수익성 악화...사업 포트폴리오 고도화에 미래 달렸다 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1ORVdUdkZBZVRyajNHa3pVeTJjR1JGTDVuNmlibWtycmN3TnVpVUtXRGhaQlBpRWRkMmZwcE1objBEV3hUV3A5blVoNVBpbmNWNmMyN1EyRzZWN0lldkNYZ25QbGdFT1dFbUM0cQ?oc=5 |  |
| kifrs | newsmp.com | HK이노엔 케이캡, 처방 성장 앞세워 실적 개선 전망 - 의약뉴스 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBTWmZzbWt4T09URWlNZmt5SzRfR2xyTUU1UTdMNTE4cWxxUFBta29oR3pfUm95dUlOUm81dHJKY2h1eERUdWx3bFpZd3FUcTVPMEJuU2hna25SVWhrcEgwMDQ5NmhEeEU?oc=5 |  |
| kifrs | tradingkey.com | OIG\|Orion180 Insurance Group Ord Shs Class A\|가격:9.840\|Chg%:+0.310 - TradingKey | https://news.google.com/rss/articles/CBMia0FVX3lxTE14Ty14aHAyZUtCMXR0R3Rlby1Ta05QWGs4Y1RfWWowbnZ3UDctYmFoZndseWpOX1NXbzJCNkkxbzVxN0hJNF81S3gxZS0xZzNSRWpXY0Vtdy1BeGE3a3dsaXEzamNhUE5BdXdn?oc=5 |  |
| kifrs | lawtimes.co.kr | (3) 회계기준이 바뀌면 투자 판도가 달라진다 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFA1MDNTVV9xNmxfOENuZUdmZkVpaG9oMzFrRkxuRFlIeHFERFVITndSUXhYRGs3eERLODZLeWJueDlVQUs4RFVXeEFxazhHcUhzNmYzNUZwVXRkeDQ4U2VXY0h6cld5N094MVJMdzBR0gFyQVVfeXFMTV9WdTlfY3pUTVRUVndPYmRhVTlYa3hOOFB4OVFoSnFWUDFhb0dYMWZudzhtSGxpSkh1ZTVMSW1YckpVUEdGU3FIOUxXMEJBSU50bVpXaS0yQmZSMW82T0RncUxGMzFPQ1pHMzZFTjNGSVZ3?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 영풍에 과징금 204억…고려아연은 84억 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sVlBmQzJPbXZuSTFOai1kaDhGb1hLVkpCdktFWnZaU1YweGRJWllmVk9zbUdZQTdpUTVRaFpHM1RlQXllWkhpdVpJUFlqLVV1SEJESnZkVUcyZEnSAWBBVV95cUxQZTlEXzktdDljVUR2UENmbHJnUzFKNE04U3BxTzNETFZBTlA3alY4VGJtREYwdmVvSldHM1JlM1kyNWlsVXJFbUxCaHhaQlBlU3VHTVY2UUh0Uk1aS1U4MzM?oc=5 |  |
| esg | 임팩트온 | 클래리티 AI, 1만2500개 기업 평가...ESG 공시 잘해도 최고등급 못 받는... | https://www.impacton.net/news/articleView.html?idxno=30480 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 머니투데이 | 상장협, ESG 공시 대비해 실무자 쟁점 미리 챙긴다 | https://www.mt.co.kr/stock/2026/10/19/2026101913585170575 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | worklaw.co.kr | ESG 공시, 직원 성장 이끄는 장치가 돼야 | http://www.worklaw.co.kr/view/view.asp?accessSite=Naver&accessMethod=Search&accessMenu=News&in_cate=101&in_cate2=0&gopage=1&bi_pidx=39682 |  |
| esg | asiatime.co.kr | [윤영민 칼럼] ESG 공시 시대, 보여주기식 경영의 종말 | https://www.asiatime.co.kr/article/20261023500342 |  |
| esg | thepowernews.co.kr | ESG 공시 291곳→1년 뒤 3171곳…대기업 넘어 협력사까지 ‘데이터 전쟁... | https://www.thepowernews.co.kr/view.php?ud=202610221509381568de3f0aa1be_7 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | newscj.com | 충남북부상의, 지역기업 ESG 공시·규제 대응 지원 | https://www.newscj.com/news/articleView.html?idxno=3441094 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| esg | hansbiz.co.kr | [ESG 칼럼]ESG공시, 기후 넘어 자연과 사람으로 | http://www.hansbiz.co.kr/news/articleView.html?idxno=860684 |  |
| tax | 서울경제 | 경기도, 지방세제 개편 입법 논의 본격화 | https://www.sedaily.com/article/20107006?ref=naver |  |
| tax | sentv.co.kr | 경기도, 취득세 의존에 재정 흔들…지방세제 개편 추진 | https://www.sentv.co.kr/article/view/sentv202610300206 |  |
| tax | weeklytoday.com | [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... | http://www.weeklytoday.com/news/articleView.html?idxno=800450 |  |
| tax | lawissue.co.kr | 경기도, 지방세제 개편안 국회 논의… 소비세율 40.3%·법인세 지방 이양... | https://www.lawissue.co.kr/view.php?ud=202610281438496967d94aa4ada6_12 |  |
| tax | gukjenews.com | 경기도 '추미애표 지방세제개편안' 30일 국회서 토론한다 | https://www.gukjenews.com/news/articleView.html?idxno=3734897 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| tax | dailypharm.com | 카드 세액공제 연 500만원 축소…매약 매출 높은 약국 부담 - 데일리팜 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1ZakNScUpnQ09qa0VVX2RlSVlwRFltUmwxczAxOGdNb3h1Nlh1Yl9OalRvakt2dTJQdERPMU1wOWFaYWtaR0xBby00MEdVODdQNVdEU1Bn?oc=5 |  |
| icfr | datatooza.com | 유니퍼스트, 10-K서 재무보고 내부통제 중대한 취약점 미해소 공개 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE4zc00yaE5xclJ5OFA1OTBhSkJCNWVsU2tRb19DSmlWQnpxU1FPX0xMblVVVWVrNURlVUk0TUdMQ3ExM0ZPRlFWQWxzbXVDdExXeFhkTkVzbzFKVW90TDBFRGlHbTlTLVFYMXkwTU5jenBwdw?oc=5 |  |
| icfr | datatooza.com | OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE85anpGNUU3UzhJX2JBTDA1dFRqRHhkQ2dhdXZGZ0ZVcHRkVU9Gc29Ca1hXWnNSMUYwOEJEWlR3NmFlblRvSmtIVHhwemFzVFpockFoWFFla0VfUmVVekFaRXAwZEUxSGc4RGt2Y1M4WmFHRmM?oc=5 |  |
| icfr | newsroad.co.kr | "내부통제 효과적" 자평한 빗썸 경영진…감사·회계법인은 "취약점 발견" - 뉴스로드 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5Cdzl4cjBaTmg1YmMwNTFrUm16YmVUcW9lTlBfcU1YWFBXR3kzeGkzWEtibERzajFnMG92Wk9oYWh6Y3FHRTdDNEJJVkNVZWxXLVdLYWpTUm5CWThiTGV0cURIcldhZDRMYU04?oc=5 |  |
| icfr | datatooza.com | 리소시스 커넥션, 내부통제 중대한 취약점 미해소… 1분기 구조조정 비용 41만 7000달러 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE4xYy1JWnFhRGhwbDJwMzRiVkgxUjdfMlYyWl9yMzVQd1NMS3kwanZRR2p2LU9oU0Fob19kbzN0M2NSaE9iSUhBX2hWb1JGTFUyUF81LXp6S0lHa0hLaThtaWhnSTl5MlZVYXJQR255RUVYa1k?oc=5 |  |
| icfr | mediapen.com | 신외감법 후 외부감사 기업 증가…지난해 4만 2891사 - 미디어펜 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE1scWRLWExwNnFZVlItbzk2QnhHMGo4VkdGc0Y5Y2dseDMtOGFxNDB0LWhTalFDV3J2ODNudEFnTllWZS1odGEweG52dU0zVGlLRFpNVdIBWEFVX3lxTE9KMnZUVy1CTWIybHRmSFFvZ1lqWkJibTIyNzN5eWg2V3lVeVRlLWhYaXJ2VnRKSmVOMXR4b1FxQVpnTnFya3kzV2tLbEh3OUJ4X2hSUVhiTEI?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:similar_news_merged (18건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 |
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| esg | paxetv.com | 상장협, ESG 공시 실무교육 실시…2028년 의무화 대비 지원 | http://www.paxetv.com/news/articleView.html?idxno=284514 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | enewstoday.co.kr | 상장협, 'ESG 공시담당자 실무 쟁점' 과정 개설 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2481878 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | dailian.co.kr | "차질 없는 대응 지원"…상장협, ESG 공시 핵심실무 쟁점 대비 | https://www.dailian.co.kr/news/view/1703168/?sc=Naver | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | newsis.com | 상장협, ESG 공시담당자 대상 실무 과정 진행 | https://www.newsis.com/view/NISX20261019_0003831375 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| tax | obsnews.co.kr | 추미애 "정면돌파"…국회 찾아 지방세제 개편 제시 | https://www.obsnews.co.kr/news/articleView.html?idxno=1542212 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | metroseoul.co.kr | 추미애 경기도지사 "지방세제 개편 시급"…3대 구조개편안 국회에 촉구 | http://www.metroseoul.co.kr/article/20261030500206 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | newspim.com | 추미애 경기지사 "지방세제 개편 시급...벼랑 끝 지방재정 구해야" | https://www.newspim.com/news/view/20261030001263 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | news2day.co.kr | 추미애 경기지사, "지방자치 이대로는 불가능"...지방세제 개편으로 재... | https://www.news2day.co.kr/article/20261030500294 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | getnews.co.kr | '지방세제 개편' 견인할 정책토론회'...추미애 "이대로는 대한민국 지방... | https://www.getnews.co.kr/news/articleView.html?idxno=885477 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | fieldnews.kr | 추미애 경기도지사, 지방재정 위기 정면 돌파…3대 지방세제 개편 입법... | http://www.fieldnews.kr/news/articleView.html?idxno=32701 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | asiatime.co.kr | 경기도, 지방소비세율 인상 등 지방세제 개편 추진… 30일 국회 토론회 | https://www.asiatime.co.kr/article/20261028500244 | → 대표: [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| icfr | datatooza.com | 크레수드, 2026 회계연도 지배주주 순이익 1772억 페소로 증가…내부통제 취약점 해소 - 데이터투자 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBnNFQycEFSeEhqZTRqekp4cnFJc3dQQVVyRWZRNEpaamtHcFFfV2VQUDI3OTZGMXFRdUVmSHpoQUM5VHVjVzdVZ2NIVUdIU0RpU0xiSmFQcmNYdjdrTGVBZFJFdGlCcWl5UTNsa1lUeHo?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |
| icfr | datatooza.com | 팩트셋, 연간보고서서 내부통제 중대한 취약점 해소 밝혀…미주 영업이익 15.2% 감소 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE51N3FTQkt2U2tmcmgzSGdRZkM2azVxMjZsZWNTd2dOanVQN2Rxei1RNC02QkpmMHRfcFFLaFBCZXNvY1c5bTY4eHNoMTZ5OGtaaExYS1FuN2E3LWtuUUI3aThLeFFtVlFrVGxUZVluTnNvYWM?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## collect:event_announcement (12건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | 2026년 글로벌 ESG 교육 워크숍 안내 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2199 |  |
|  | 재정경제부 | 이형일 부총리, 글로벌녹색성장서밋에서 기후대응·성장의 선순환을 위한 국제협력 강조 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079788&menuNo=4010100 |  |
|  | 금융위원회 | 제9회 ‘회계의 날’ 기념식 및 회계업계 간담회 개최 | https://www.fsc.go.kr/no010101/88031?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 제2차 국민참여성장펀드의 운용사들의 국민투자금 운용전략을 청취하고 향후 관리방안을 논의하였습니다. | https://www.fsc.go.kr/no010101/88025?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | 제9회 '회계의 날' 기념식 및 회계업계 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787286&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
| icfr | core.asiae.co.kr | [Why&Next]‘회계사의 꽃’ 파트너 승진, 신외감법 도입 후 최저수준 전락 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1GQ0paYVh4cms0bTZZVFotNGI5OUI2cnpILU9TVi1qZmZ1MHFlbnRrZnhRNUJ6Y280OGl4TFV0QkpTOGtOV0UtM2Y2Q1JvdmVJTmxLLUxobk9jLV9CM3locm1B?oc=5 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| esg | betanews.net | 네이버, ‘2026 지속가능경영유공 정부포상’ 대통령 표창 수상 | https://www.betanews.net/article/view/beta202610300070 |  |
| esg | ESG경제 | [알림] KSSB·ESRS 이중중대성 평가 웨비나 초청 | https://www.esgeconomy.com/news/articleView.html?idxno=17019 |  |
| esg | news.tf.co.kr | 동아ST 지속가능경영보고서, '2025 LACP 비전 어워즈' 수상 | https://news.tf.co.kr/read/economy/2361168.htm |  |
| esg | ttlnews.com | 동아에스티, 지속가능경영 유공 종합 ESG 분야 산업통상부 장관 표창 | http://www.ttlnews.com/news/articleView.html?idxno=3157355 |  |

## collect:incident (4건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 머니투데이 | 증선위, 코스닥 상장사 피델릭스 '회계기준 위반' 고발 조치 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMidkFVX3lxTE5weWxIak43RVJfVlZydWYzWlZSWEk5eTFFT2xvN0hseklrb0YzNWFSWEpkNWtfOGJvV055d0xzRktETEx3VEhIRlBkR0JheTFqeHlXOFNNNDVrdlk3ZTFncmlhRV9EMVhZTEMtM0NwYTJXZmdTNmfSAXtBVV95cUxNOURUXzlucko3V0NMU1MyYVlHQ2N6UG9PMkVwMGdYQnAxakxyalNHMDJveFoyS1ZJM1Q0aE1iNGZrNGkwUFZCZVVmN2tFZ3ZOMWstYVhtd3BjaUdpd2Rocnh4cWpOblI5N2RQSE9kclN1MjdVbnVVbmhXQUU?oc=5 |  |
| kifrs | datatooza.com | 한국거래소, 피델릭스에 회계처리기준 위반 고발 풍문 조회공시 요구 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE5ybGdLZXFWdHc1SHlVb0cxNThfajVTYnlnTDlHT2JrYkhlSnFJbmI4cTRPVlJzRmphVENmWjFvQ19ZMXo2dEVaUDlvUEdtWnpmS2F1QkNQbGZRODJ2VERiTzlyRmVLM0dZNnM2eDFZWlk0UQ?oc=5 |  |
| icfr | 한국경제 | 외감법은 경찰, 자본법은 중수청…분식회계 수사 차질 불가피 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wOF91b3FKNTlVV3FUM3J2amdHek9VS29CTHZ1N3d3NFJiOWtOakNkRVRPSzhFd3ZKMHM3RkRmcW9QeE9hRFV4NHNhbmQ5Q0RSNUpIbEYyOG9zUQ?oc=5 |  |
| icfr | etoday.co.kr | 기업인 50% “신외감법 시행으로 비용부담 급증” - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE9ndVlHYUhDc21PU0RJcC1SUjZDUzRpSmtGUjAtZjA4dzZUb2w5V1c1ellfM2EyUjhVSVpnUnFRYjZsYU1lMG9EQzdieGdWVFUwdkJiZg?oc=5 |  |

## collect:law_name_mismatch (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 법제처 | 지방교부세법 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방교부세법 시행령 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방교부세법 시행규칙 (검색어 '지방세법') |  |  |
| tax | 법제처 | 지방세특례제한법 시행령 (검색어 '지방세특례제한법') |  |  |
| tax | 법제처 | 지방세특례제한법 시행규칙 (검색어 '지방세특례제한법') |  |  |

## collect:no_category (21건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 권대영 1차관, 「주요 국책과제 이행점검」 TF 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079811&menuNo=4010100 |  |
|  | 재정경제부 | 한-독일 이중과세방지협정 개정의정서 서명 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079805&menuNo=4010100 |  |
|  | 재정경제부 | '26.9월 국세수입 동향 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079808&menuNo=4010100 |  |
|  | 재정경제부 | '26.9월 및 3분기 산업활동동향 및 평가 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079806&menuNo=4010100 |  |
|  | 재정경제부 | 26.11월 국고채, 재정증권, 원화표시 외평채 발행 계획 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079801&menuNo=4010100 |  |
|  | 재정경제부 | 퇴직연금 기능강화 방안 발표 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079784&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 광진 서민금융통합지원센터 방문, 서민금융 지원 강화 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079800&menuNo=4010100 |  |
|  | 재정경제부 | 개인투자용 국채 11월 2,000억원 발행 예정 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079786&menuNo=4010100 |  |
|  | 재정경제부 | 확대 거시경제금융회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079792&menuNo=4010100 |  |
|  | 금융위원회 | 불법 가상자산 취급업자(특금법상 미신고 가상자산사업자)에 대한 수사의뢰(DAXA, 3건) 및 접속차단(2건) 요청 | https://www.fsc.go.kr/no010101/88039?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 한국의 풀뿌리 금융,  미소금융이 다시 한번 도약합니다. - 미소금융 재원 기부 협약식 개최 | https://www.fsc.go.kr/no010101/88029?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 국민성장펀드가 국내 최대 태양광 발전소 건설과 반도체 밸류체인 경쟁력 강화를 지원합니다. | https://www.fsc.go.kr/no010101/88028?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 퇴직연금 기능강화를 위한 노사정 합의로 노동자의 든든한 노후소득 보장체계 구축 | https://www.fsc.go.kr/no010101/88027?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융위원장, ‘금융분야 재난대응 안전한국훈련’ 주관 | https://www.fsc.go.kr/no010101/88023?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 보험사기 연루 보험업종사자에 대한 등록취소·업무정지 등 제재 | https://www.fsc.go.kr/no010101/88021?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | “금융회사의 부실 확산에 신속·선제적으로 대응하여 금융시장의 안정 및 소비자 보호를 위한  ｢금융회사 신속정리제도｣ 도입을 추진합니다.” | https://www.fsc.go.kr/no010101/88020?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ☎1375(일상치료)로,  빚의 고통은 덜고 희망의 빛은 더하겠습니다. - 금융위원회·신용회복위원회, 채무상담 대표번호 ☎1375 개통식 개최 - | https://www.fsc.go.kr/no010101/88019?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | 한국의 풀뿌리 금융,  미소금융이 다시 한번 도약합니다. - 미소금융 재원 기부 협약식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787267&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 국민성장펀드가 국내 최대 태양광 발전소 건설과 반도체 밸류체인 경쟁력 강화를 지원합니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787212&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 퇴직연금 기능강화를 위한 노사정 합의로 노동자의 든든한 노후소득 보장체계 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787204&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 불법 가상자산 취급업자(특금법상 미신고 가상자산사업자)에 대한 수사의뢰(DAXA, 3건) 및 접속차단(2건) 요청 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787377&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |

## collect:noise_keyword (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | g-enews.com | [특징주] 해태제과식품, 회계기준 거래 정지 후 재개 첫날.. '급락' - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPbkZaRjEwOU9SRDR0UFAzcFRJVjNDZlBIYVRja29fcXRlcXY5T05ORVo4cTdtZHV2amlSR3hOOFlzUGFSUXJzNjlBMVNSX2V6RG16bXdUckxxd0hsSUw3b0xZTFNTR2tYX1VMa1RMRURYX1c2LXA0d3BHM0Q2QkJEOGY3VHJ4aUZX?oc=5 |  |

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

## collect:out_of_scope (206건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(5차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 본인 인증 서비스 일시 점검 안내(2026. 10. 17.(토) 21:00 ~ 2026. 10. 18.(일) 05:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [한국회계기준원] 2026년 하반기 추가채용(연구직-회계기준 연구원) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [KARI REPORT] IFRS 16 도입 이후 리스 기반 영업구조 하방위험 가시화와 정보적 함의 : 사용권자산 손상차손을 중심으로 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 회계기준위원회 상임위원 초빙 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 10월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [세미나] IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/calViewA.do?seq=1129 |  |
|  | 한국회계기준원 | [세미나] 회계기준원-환경산업기술원, 지속가능성 공시기준 이행지원 세미나 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1127 |  |
|  | 한국회계기준원 | [세미나] 한국회계기준원 개원 27주년 세미나: 지속가능성 공시, 새로운 기준의 시대 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1125 |  |
|  | 정책브리핑(외교부) | 한미일 외교장관회의(10.30.) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787391&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교전략정보본부장, 스위스 외교장관 만찬 협의(10.30.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787390&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 2026년 수소발전 입찰시장 개설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787389&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 박윤주 외교부 제1차관,  미국 외교정책위원회 대표단 면담(10.30.) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787388&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 제8차 주택공급 현장점검(은평구 불광동) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787387&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)EU, 수입 하이브리드 자동차에 대한 글로벌 세이프가드 조사 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787386&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 카드뮴 기준 초과 검출된 '기타 수산물가공품' 회수 조치 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787382&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 윤호중 행안부 장관, 핼러윈 대비 인파밀집 예상지역 현장점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787385&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 제1회 '공학인의 날' 개최… 공학인의 도전과 미래를 응원한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787381&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 고(故) 최불암 배우 금관문화훈장 추서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787380&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 소비기한 이중 표시 '과·채가공품' 회수 조치 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787379&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-해양동남아 협력기금, 역내 지속 가능한 발전과 포용적 상생을 위한 실질적 기여 지속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787376&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청 농업 전문가, 남수단 한빛농장 찾아 기술 전수 구슬땀 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787372&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 밥맛으로 승부한다. '황금예찬' 소비자 곁으로 더 가까이 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787370&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '적외선 소고기 숙성장치' 싱가포르 현지 진출 가능성 타진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787368&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌관광에 맛을 더한다! 농촌 미식 명소 88곳으로 늘어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787366&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 중증 어르신 재가 돌봄 월 이용 한도액 최대 37만 원 인상… "살던 집에서 더 충분하게" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787374&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-몽골 황금시대에 걸맞는 전략적･호혜적 실질협력 강화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787364&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국토대전환 두 번째 현장랩(나주) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787365&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 한-일 관세청장 회담 개최...'마약 밀수정보 교환, K-브랜드 등 한일 브랜드의 짝퉁 단속협력, 역직구 확대 위한 해상특송 특례 운영' 등  3대 협력체계 구축 협의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787363&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 고속도로·철도 주변  소나무재선충병 위험목 제거 본격 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787361&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정은경 장관, 대한소아응급의학회와 만나 의견 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787362&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "우리 배 품질 경쟁력 빛났다" 최고 품질 한국 배 시상식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787356&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 가루쌀 맥주 기술 확산 산업체 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787354&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | '방송 송출 중단' 훈련으로 미리 대비 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787340&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 잎들깨 '새봄' 양액재배 현장 평가회 열어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787352&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 중남미와 농업 바이오 혁신기술 협력 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787350&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '유전자 가위(편집) 갖춘 돼지 폐 면역세포주' 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787348&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 막걸리 품질개선 연구 성과 '눈에 띄네' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787346&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 양산산림항공관리소, 가을철 산불대비 총력 대응태세 확립! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787359&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 기후 위기 대응 '시설 딸기 보광 기술' 현장 확산 박차 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787344&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 팽이버섯 고깔 세척·건조 기계화로 '위생 관리' 효율 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787342&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 해외 산림당국에 산불진화 기술력 알려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787337&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 케이(K)-농산물, '농약 안전관리' 강화로 비관세장벽 넘었다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787334&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 범죄피해자의 권리 보장부터 일상회복까지  국가가 함께합니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787338&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 고준위위원회, 고준위 방사성폐기물 관리시설 부적합지역 배제기준 확정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787339&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 사료 원료 수급 안정·사료비 절감 '전문가 머리 맞대' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787332&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 단백질 고함유 신품종 콩 '대단', 농가 수익 증대·콩 산업 활력화 기대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787330&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '꿀벌전용사료 3종', 벌무리 발달과 꿀벌 건강 증진 효과 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787328&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 시각 예술 전문가와 2027년 정부 예산안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787327&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 개발협력주간 사전행사 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787325&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리 주재 민생침해범죄 유공 격려 오찬간담회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787324&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "황금빛 농촌 만끽, 풍성한 가을 맛 기행 떠나요!" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787321&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 겨울철 과수 보호 위한 전용 흰색 수성페인트, 현장 활용 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787319&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 디지털융합의약품.. '원스톱 통합심사 체계' 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787323&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동부지방산림청, 가을철 산불방지대책본부 본격 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787317&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(경제사회노동위원회) | [보도자료] 국제노사정기구연합 이사회 및 총회 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787318&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 'HRDK 국민성장추진위원회' 성과 도약의 기반 다지는 마무리 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787315&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "청년 사회복지사의 든든한 울타리 되겠다", 정은경 장관, 청년 사회복지사 소통의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787313&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 통신재난 대응 강화로 국민 일상 보호 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787312&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 권대영 1차관, 「주요 국책과제 이행점검」 TF 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787314&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 서부지방산림청, 가을철 산불방지대책본부 운영 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787310&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 가을철 산불조심기간 시작… 산불 예방 총력 대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787308&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 서울출입국·외국인청 문정동 신청사에서 36년 만에 새출발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787311&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '농생명 특화 거대언어모델' 개발 방법 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787303&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농자재 절감 기술 ·스마트 농업 확산 신기술 보급 박차 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787301&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 돼지 도축로봇, 현장 실증으로 정밀 제어 기술 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787299&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "도로점용허가 문제로 첫 삽도 못 뜬 공장"… 행정기관 간 합의로 기업고충 '해소' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787306&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 우리 풀꽃 산업화 이끌 유망 품목 선정 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787297&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "5분이면 뚝딱" 현장에서 신속하게 퇴비 수분 상태 확인한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787295&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청장 직무대행, 핼러윈 데이  이태원 인파 안전관리 현장점검에 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787294&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 생애말 의료·돌봄 공론화 위한 두 번째 의료혁신 시민패널 토론회 준비 최종 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787293&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | AI 발전 속도에 발맞춰 보건의료데이터 안전 활용법 교육한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787292&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 대한민국-몽골 보건의료협력, 디지털 전환과 K-의료 인재양성 새 지평 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787290&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한-독, 전기화 시대 산업경쟁력 확보 위한 에너지 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787291&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부·국토교통부·고용노동부·경찰청·해양경찰청, 외국인 불법행위 방지를 위한 범정부 공동 대응 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787289&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "산업변화를 진단하고 현장의 혁신을 이끈다" 산업별 인적자원개발위원회, 제5기 도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787285&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '27년 문학 분야 정부 예산안 논의, 한국문학의 지속 가능한 성장 기반 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787288&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 조현 외교부 장관, 미국 조지아주 인근 진출 우리 기업 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787283&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 미래 우주항공 인재양성방안 모색을 위한 '제12차 우주항공 SOS간담회' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787282&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 인공지능시대사이버보안영재교육지원을위한 교육부.LG유플러스.티오리한국 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787281&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 재배면적조사 결과_가을배추, 가을무 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787280&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 따스한 가정의 품으로, 국가봉사동물의 견(犬)생 2막을 지원합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787276&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 미래항공 핵심부품 성능 및 신뢰성 검증 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787279&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | "2032년 달 착륙선 어디에 내릴까" 착륙 후보 지역 분석 결과 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787278&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관,  "8·13 대책 신속 추진, 서울 연내 3.1만호 착공 지원" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787277&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 제5차 한-캐나다 과학기술혁신공동위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787275&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 강릉산림항공관리소, 가을철 산불기간 대비 산불방지 총력대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787274&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 통상교섭본부장, K-콘텐츠 기업과 함께중국 시장 진출 전략 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787272&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 민관 원팀으로 중동發 공급망 위기 넘어, 구조개편 가속화로 화학산업 재도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787271&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한·독, 경제안보·첨단산업 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787270&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 대국민 재정교육 아이디어 공모전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787269&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국장애인고용공단, 자폐성 장애 인식 개선 위한 '2026 오티즘 레이스' 참여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787264&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "공정하고 투명한 업무 수행" 근로복지공단 박승흡 이사장,  추혜선 상임감사 직무청렴계약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787263&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 지역산업의 변화, 일자리 정책과 함께 대응해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787262&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 음악가 공모부터 선곡까지, 시민의 댓글이 콘서트가 됐다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787266&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 현대차그룹 새만금 현지 사무소 30일 개소,  새만금 9조원 투자 실행 본격화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787259&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 주민 삶 바꾼 복지정책 어느 지역 빛났나 2025년 지역사회보장계획 시행 우수 지방정부 44곳 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787258&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 자가면역세포 배양 치료, 앞으로 2~3년 소요 선행 임상연구 없이 치료계획 신청·심의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787257&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 소아·응급의료 필수의약품 삼진로라제팜주, 퇴장방지의약품 신규 지정 및 약가 개선 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787256&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 불법사금융 피해자 지원 위한 금융관계기관-지방정부 간 긴급의뢰 시스템 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787255&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 보건복지 분야 사회적 가치 실현 앞장선다, 2026년 예비사회적기업 17개 신규 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787254&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "술은 관계와 관계없다", 연말연시 절주·금주 공익광고 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787253&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-인도네시아 외교장관 회담(10.29.) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787252&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 상주 청년농·포도 수출 현장 찾아 현장 목소리 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787247&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 카페에서 즐기는 양봉산물, 올해 최고 요리는 "뀰페스티복과 뀰퍼레이드" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787245&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림항공본부, 가을철 산불방지대책본부 본격 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787250&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 인공지능(AI) 시대! 농업 대전환 이끌 현장강사 역량 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787243&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 이달의 신간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787241&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 울산화력발전소 보일러타워 붕괴사고 조사결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787238&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 민관합동 농업생명공학 연구 안전관리 현장 점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787239&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 문화·관광·산업 등 분야 어려운 법령,  한눈에 이해되는 시각 콘텐츠로 본다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787237&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 수목원 조성부터 운영까지, 국가·지자체 자금지원 근거 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787236&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 스타링크를 활용한 산불 드론 진화 합동훈련 참여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787231&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 의약품 허가심사에 '환자경험자료' 반영한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787232&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국방·미래산업의 핵심 화합물반도체,  국내 기술이 양산까지 닿도록...산학연과 밑그림 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787226&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 권오을 장관， 교육부 및 소방청과 보훈역사 현장체험교육 확대 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787225&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 2026년 11월의 독립운동가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787224&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 2026년 11월 이달의 6.25전쟁영웅 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787223&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 휴게소 직계약 시범사업 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787227&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 추워지는 날씨, 보일러 가동 전 점검 철저로 화재와 일산화탄소 중독 예방! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787234&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 질병관리청 기관생명윤리위원회(IRB) 국가기관 최초 평가·인증 획득(10.30.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787326&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 도급사업 안전보건협의체 및 안전실천결의대회 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787229&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청, 국민 체감 '신라왕경 핵심유적' 정비방향 모색한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787220&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 무형유산 디지털 음성자료, 「무형유산지식새김」에서도 본다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787219&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청, 제1대 국가무형유산 청년정책자문단 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787217&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 고려 후기 금동불감 「구례 천은사 금동불감」 국보 지정 예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787215&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산, 사랑하면 보이나니! '2026 국가유산지킴이 전국대회' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787207&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 11월 대형사업 총 342건, 2조 9,938억 원 상당 입찰 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787203&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 한-독일 이중과세방지협정 개정의정서 서명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787211&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청 시설공사 주간('26.11.2.~'26.11.6.)입찰 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787202&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)산업부, 기술보호 현장 집행에 속도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787208&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 행복청, 인공지능 추진성과 공유...전문가들과 발전방향 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787201&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 2026년도 하반기 해상풍력 경쟁입찰 공고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787209&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 의료기관 방사선관계종사자 피폭선량 30년 분석, 1인당 연평균 피폭선량 84.9% 감소(10.30.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787200&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "청년이 주도하는 청렴 문화" 국민권익위-한국전력 교류회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787198&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 한약(생약)제제 GMP 질의응답집 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787197&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 의료기기 사이버보안 허가심사 가이드라인 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787196&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, '인공무릎관절' 컴퓨터 모델링 및 시뮬레이션(CM&SS) 신뢰성평가 사례 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787195&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, '의약품 사전 GMP 평가 지침' 전면 개정… 절차·제출자료 명확화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787194&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 손끝으로 확인하는 의약품 정보, 더 정확하고 안전하게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787193&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, '과일 찹쌀떡·샌드위치' 등 배달 음식점 및 무인 식품 판매점 집중 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787192&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '케이-콘텐츠' 지식재산, 유럽·중국에서 해외 진출 기반 넓혀 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787191&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '케이-컬처' 전진기지 확대, 말레이시아에 한국문화원 개원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787189&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 9월 산업활동동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787190&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(소방청) | '독도 순직 소방항공대원 7주기 기억하는 날' 가져... 중앙119구조본부, 순직 소방항공대원 7주기 추모날(데이) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787188&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 로컬창업 소상공인 투자유치 1,227억원 달성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787187&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 2025년 장애인학대 신고 6,608건 1년 새 9.6%↑, 학대의심사례의 23.9%는 본인 신고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787185&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | '26년 9월 주택통계 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787184&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 대구경북통합신공항 민간공항 기본계획 변경 고시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787183&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부, 제3회 특별성과 우수사례 시상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787186&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 더 정교한 촉매 설계의 실마리 찾았다... 화학 결합의 장거리 영향 규명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787182&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 파독 광부·간호사 한자리에...지난 헌신에 감사하고 오늘의 어려움 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787251&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | '26.9월 국세수입 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787265&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | '26.9월 및 3분기 산업활동동향 및 평가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787199&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-독일 이중과세방지협정 개정의정서 서명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787181&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 2026년 제6회 민간투자사업심의위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787156&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 국가공무원 5급·외교관후보자 최종합격자 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787154&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 「2026 안보지킴이 공모전」 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787152&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 한국에서 함께 그린 원자력의 내일, 국제원자력기구 원자력 장관회의 폐막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787151&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | '산림휴양디렉터', 자연휴양림 조성의 길잡이 역할 톡톡 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787149&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 26.11월 국고채, 재정증권, 원화표시 외평채 발행 계획 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787147&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 장관, 코리아 그랜드 페스티벌 수산물 할인행사 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787146&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한국과 아랍에미리트 두바이, 문화협력 확대 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787145&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 부패는 멈추고 청렴은 키우고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787143&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 항공엔진 구조물용 고강도 소재부품 기술개발 심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787144&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 임산물 수출 유망업체 4개사 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787141&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-인도네시아 G20 셰르파 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787139&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, '다누리호' 출항 축하.. 원양산업의 새로운 도약 기대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787134&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 제15차 아시아산림협력기구 총회 개최… 국제산림협력 확대 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787136&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 박홍근 장관, AI 영상 제작 현장방문 및 전문가 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787130&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부 국제질병퇴치기금 출국 납부금 환급 서비스 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787138&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "산림 사업 현장 안전 사각지대 없앤다." - 영주국유림관리소, 안전보건공단 경북지역본부 합동 중대재해 예방 교육 실시 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787129&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 강신철 국방부장관  제13차 아세안 확대 국방장관회의(ADMM-Plus) 참가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787126&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 조용범 차관, 제24회 협동조합정책심의위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787122&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동부지방산림청, 태백에서 임업인들과 산림규제 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787125&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [차관동정] 정의경 제2차관, "이동로봇, 실증 넘어 상용화 기반 마련할 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787123&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 구혁채 과기정통부 제1차관, 원자력학회 참석 및 경주지역 연구현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787116&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 기술에서 시장까지,  K-GX 선도하는 기후테크 혁신기업 본격 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787121&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부, AI 스타트업의 유니콘 도약, 현장 의견으로 정책 완성도 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787120&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중소 제조현장을 피지컬 AI 혁신의 무대로, 「중소제조 피지컬 AI 확산 전략」 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787119&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부·복지부, 글로벌 제약바이오 시장을 선도할 「K-제약바이오 프론티어기업」 200개 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787118&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "멈춰 있던 일상에서 꿈을 향한 첫걸음까지" 청년들의 작은 도전과 성장의 기록 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787113&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 글로벌녹색성장서밋에서 기후대응·성장의 선순환을 위한 국제협력 강조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787114&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한국형 녹색대전환 이끌 기후테크 혁신기업, 기술부터 시장까지 전방위 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787112&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 동포와 함께 여는 대한민국의 미래...동포정책 전문가 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787111&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 편지와 함께 먹거리, 집배원이 그냥드림 전하며 어려움 살핍니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787109&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 법제처, 아동·청소년 대상 성범죄 예방을 위한 현장 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787108&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)국내 수급에 차질 없는 범위 내에서 경유 수출제한 조건부 완화 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787107&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 특송물품 악용한 마약밀수 차단을 위한 검사 강화 현장점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787106&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 2027년 장애인일자리 사업 참여 가능 인원 2,600명 늘어 3만 8천 명으로 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787100&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "AI로 누구도 소외되지 않는 보건체계 구축", 한국-아세안 보건 협력 연결망 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787099&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 국내 물리적 인공지능 산업 육성 가속화를 위한 전문가 소통 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787096&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 공직 전문성 높이고, 일하는 방식 바꾼 공무원 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787103&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [정부합동] 백해무익(百害無益)한 '담배'...유해성분 검사 확대, 정보 제출 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787098&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [정부합동] 정부, 국내 판매 담배 465개 제품 유해성분 검사결과 최초 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787097&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 기부채납 수목원, 국·공립 전환 때 조성면적 기준 10ha에서 2ha로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787093&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림, '기운담길 소원 걷기행사' 연계 산불예방 캠페인 펼쳐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787091&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 장애인 건강 수준과 격차, 건강지표로 본다 「2026년 장애인 건강보건통계 콘퍼런스」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787085&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정부, 국내 판매 담배 465개 제품 유해성분 검사결과 최초 공개… | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787084&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 백해무익(百害無益)한 '담배'... 유해성분 검사 확대, 정보 제출 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787083&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제16회 국가정책조정회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787087&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 국토교통부는 타워크레인 안전 강화를 위해 노력중입니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787079&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년 공정거래 학술연구 지원사업 최종발표회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787074&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 부패를 막는 청렴, 갑질을 넘어선 공존... 푸른 숲을 닮은 공직문화를 위하여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787082&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-31&endDate=2026-10-31&srchWord=&period= |  |

## collect:out_of_window (34건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 국민참여입법센터 | 법인세법 시행규칙 일부개정령안 입법예고 (예고 시작 2026-04-24) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86522 |  |
| tax | 국민참여입법센터 | 소득세법 시행령 일부개정령안 입법예고 (예고 시작 2026-04-24) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86534 |  |
| tax | 국민참여입법센터 | 소득세법 시행규칙 일부개정령안 입법예고 (예고 시작 2026-04-24) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86526 |  |
| tax | 국민참여입법센터 | 소득세법 시행령 일부개정령안 입법예고 (예고 시작 2026-04-10) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86300 |  |
| tax | 국민참여입법센터 | 조세특례제한법 시행규칙 일부개정령안 입법예고 (예고 시작 2026-04-24) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86532 |  |
| tax | 국민참여입법센터 | 조세특례제한법 시행령 일부개정령안 입법예고 (예고 시작 2026-04-24) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86530 |  |
| tax | 국민참여입법센터 | 지방세법 시행령 일부개정령안 입법예고 (예고 시작 2026-04-22) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86446 |  |
| tax | 국민참여입법센터 | 지방세법 시행규칙 일부개정령안 입법예고 (예고 시작 2026-04-22) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/86498 |  |
| kifrs | 임팩트온 | 기후위험, 재무제표 주석까지 들어온다…회계기준원, 공시 사례 공개 | http://www.impacton.net/news/articleView.html?idxno=19406 |  |
| kifrs | ESG경제 | 재무공시와 기후공시 연계 강화...회계기준원, 기후위험 공시 사례 제시 | https://www.esgeconomy.com/news/articleView.html?idxno=15878 |  |
| kifrs | tfmedia.co.kr | 회계기준원 IFRS 20 간담회에 에너지 기업 ‘쫑긋’…IASB 부위원장도 참... | https://www.tfmedia.co.kr/news/article.html?no=204787 |  |
| kifrs | 일간NTN | 회계기준원 지속가능성기준위원회, 지속가능성 공시기준 첫번째 세트 의... | http://www.intn.co.kr/news/articleView.html?idxno=2049269 |  |
| kifrs | tfmedia.co.kr | 회계기준원 KSSB, 지속가능성 공시기준 첫 번째 세트 의결 | https://www.tfmedia.co.kr/news/article.html?no=201983 |  |
| kifrs | 매일경제 | 국제회계기준 해석委, 일탈회계 관련 기준개정 필요없다 의견 | https://www.mk.co.kr/article/11489251 |  |
| kifrs | 이데일리 | 한국회계기준원 "국제회계기준 해석위, 일탈회계 극히 예외적…기준개... | http://www.edaily.co.kr/news/newspath.asp?newsid=04060646642397208 |  |
| kifrs | ajunews.com | 중앙그룹 채권투자자들, 금감원에 중앙그룹 5개사 회계 감리 요청 | https://www.ajunews.com/view/20260726212534288 |  |
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
| tax | yna.co.kr | [2026세법] 가업상속공제, 병원·주차장 배제…제3자가 물려받아도 지원 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1DbEhoVWxxZ05yVThvSmRaS2RHWHZsbFFMVTdvUVFRRUk2VnJrNTdrTXo2dnctY2UxNzFXTXF0eGpnd2pFU1dxWmJBN1JqNktEWURJQ0lDZ0lpZVHSAWBBVV95cUxNc2dtUlA1VzIzYzFFMVctaVhEQmF1Z2xmYmtuZE0yWk1JUmkwaGZzaWlwTFEtUWkxUzNkakI0akxxeWd3U2c1eVV1RkVqeU5JTW9lSjh5dWlnbk05UlpPZ1c?oc=5 |  |
| tax | lawtimes.co.kr | 미국 세법 및 판례상 국내원천소득의 증명책임과 상호주의 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB4bmthMkluOF84Uk9raFgzaFlqM2ptOW1oNnJWemdCRHRSMGxKZElNU1VkNG55SUdOUjZtTWp1R3loeFZHMkcxblNiRDJBNlY3NmRMZXZZa1pWTXdVdUhfT3V6SUZSajRxdzduclFB0gFyQVVfeXFMTU84R0QxVWZuQTdqTGJjM2M5UXA4R1JPQThYY1ZPV3RQRWdhcjhmaW0zUXAzRUtEVUlIcDBKYXdCSWltUHozb3liYlA1TnlyUWI4TmRlZkdrV2h3UXBzWmNjWEtLQi14bTJvSF9ldE1oVDJn?oc=5 |  |
| tax | shinailbo.co.kr | 안철수 "정부 세제개편안은 '고려장 세법 개정안'…파기가 답" - 신아일보 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1xSmFfcWRZc09JRzl6dFJRQVlodkhpWWM4aEU4TE1XVUNfXzQ2VFczQnlTVWJ1QUtCMmV1WWRGT19CODd6NXI3NGhsWldHXzlBcUxJRk52MXdkUnplb0NtSWJOUExvV1JQeEtUX3FFMmc?oc=5 |  |
| tax | hani.co.kr | 민주 “세제개편안, 정교하게 다듬겠다”…서울 의원들은 여론 주시 - 한겨레 | https://news.google.com/rss/articles/CBMidEFVX3lxTE9ZTzhoZFVjaW01QjdfMGNrUkhSdXJKaUVZSGEtSkJ4M21RbG03cUxDUVZSbHJTZk5tYWtXQ3RQaHVuSWthcHA5cGM2TlZEWFRCVXFBRVItN2JCQjhWcDQ4TlpDQmpmUy0xNUE3Q0pZaURubXZh?oc=5 |  |
| tax | ftoday.co.kr | 국회예산정책처, “세법개정안 따라 5년간 세수 14.5조원 증가” - 파이낸셜투데이 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9PNGhxandZMnhIemQtQkdNUXBLMlFLUU01MVlIamVsX2g2YWZtdHNCZnJNLVo4eThFcF80Ym0zdGZwcWl3VUJNVnRYdl94bGpxX3laaTlLVUNhNkhTRHgwZzNRdXpBMkozM2fSAW5BVV95cUxPeERNTGhHN2tBOTdjV0NoWFZzeWo2MUQxRmlLdTNBRnpTNFA3WlMwaktyd3R0NnFzMEcyN2RNWWI5MXltNE1SeGtVZWU2RGZXOVo0WEdFVTI3b2phVXNDUFpmM2tlel8xT1B2cGlQUQ?oc=5 |  |
| tax | newstomato.com | (8·3 세제개편 한 달)종부세 후퇴…정책 신뢰 ‘실종’ - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFAzbGtwN19uMk0xRExHYUtyLTVMalFQeVp5U2FtSno4N2IyOUlVbXRXRE92TnBqUjl2TS0tYW4zdWNoSmRsMjhwZVhPZ04xZUVHVVlEajBMSzF1Y25hdXdfWA?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | joongang.co.kr | 안철수 “李 정부 부동산 세제 개편안 ‘고려장 세법’” 비판 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1rbU5oUml0aWw5SjRrN3p2b2JuZGpzZE55azhFOVZzMTBaWGZSbDk0WjQtLUNJMzhobm00dk14YmhaZ19TRTZpalBfWjJ5N2ZmZTJ3bk9n?oc=5 |  |
| tax | 한국세정신문 | 2026년 부동산 세제개편안 주요 내용 총괄표 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9VV05RWWFtWkNqZmNWQktodVFiLS1GckNYcXZ6SGUxcFc5dXhEQi0tN0FmM2tucEROdHF6OU4xUnpmd1NXd29fQUpnMkdRbnVac2pqOEsxUTBaN1JWdjcyVjBHOUE?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzDSAWBBVV95cUxOeDlrTWJMLVFFUHdRdGFKSnZYenV2UWl2UnZxTUtyamE4YUNfSjVfSzNHY2U4eEQ1X096RGc2aE9BN3dMUGlnaE56N1I2c2c0bkZkVTR0a1lJR1pUQWxUSGk?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | jinju.news | 김태호 의원, 지역균형발전 강화를 위한 지방교부세법 개정안 대표발의 - 진주인터넷뉴스 | https://news.google.com/rss/articles/CBMid0FVX3lxTE44X0w1UUNpbTMtSnZFa2ZpdUF0dHhxeU5GWFlWNF9NZTY0aWRNWGJlS0lLMEJFc1lERHd0MFBubjhHUVBERlVKT204VjQ2TlIxb3drSUJfV3FyMWcxX1RONzUxWE9LMzkxY2VGZVBCVjl5WVlnTUp3?oc=5 |  |
| tax | news.mtn.co.kr | 부동산 세법에 정치권 '시끌'...나경원 "강제 이주 명령" - MTN 머니투데이방송 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5PMFlBZTFJdUYtRUpCdlNGXzQ3SkR5WE10SlBvcGFkWExqX0llN19WZjBCbjZhT0RDNTczTkcwajh2RXM5bmh5UFNJNDl4YzdaQ2o3alNLOVdRM0JULWVhbVFieXI?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | newspim.com | [2026 세제개편] 가업상속공제 최대 1000억으로 확대…경영요건 10년→30년 강화 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1LMUhHbGx0N1NBekZQc1VSbHhZbllJR3VobXJFREtXLXpFejNmUVdua2U3eE81TEU3c0JRUGRwMURmS0FRTlZsOHRjck9mVTA0NXJURUlzNDhERzlH?oc=5 |  |
| tax | newsk.net | 세법 개정안의 주요 변경 사항 : 한인동포신문(몽골) - 뉴스케이 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXdlRVQnREMG5BcGNrUjNUdF9MSEVtbGJzdHBuWjNBM29ZTDBtYXY5TWw4Q1F4OG1QMlVSZnQ1YTNYMEpBcmJKX1hhTDJOczE0UTQ5VnlRY1FmZw?oc=5 |  |
| tax | news33.net | 2026년 세법개정안 5년간 세수 14조5000억 원 증가…종합부동산세 10조5000억 원이 견인 - 창업일보 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5STnRheEtYWS1XdjNKMUIyR2VmRUNZVFNRU29pZi1xdWE2VlhqLTVJSkw5R2dFODhLcUhKUlRzVmhraVR1WC01dFBSTm1Vamx4aWd0TTdOYU10TnhvSV92ZWlKX1VSQXJw?oc=5 |  |
| tax | nbnbiz.co.kr | 정부 세법개정안 속 ISA 대수술에 투자자들 거센 반발 - nbn 시사경제 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE15SE5vWnlDRVAwMGxJRDZfdVlLX2l1SXdjaC1PbHRKd1NVN3VuTG9jdkNFSFFmdGY2MW0xeDFfSmljS1prNlJndHhOdUt5Q05SWGg0a0Z1MXJTWGllOGRfS05ySFk?oc=5 |  |
| tax | chungnamilbo.co.kr | 이재관 의원, 농업인 세제 특례 일몰 연장 등 세법개정안 2건 대표발의 - 충남일보 | https://news.google.com/rss/articles/CBMickFVX3lxTE53NERMV05sWGVwSks0QlVHLU5ZZllyMmRvMVQ0MGE4RHN0TUkwTUZUUW1WV0lTcmN5VTJpX0NKdHNIRFJnVVhQOGtiUHJqcHZoUWU2TGF4WkNDTzJDSGNuUDE3T2lKczFPZldnN0RIdzlsdw?oc=5 |  |
| tax | imaeil.com | "살면 보유세, 팔면 양도세 폭탄" vs "서울시장 책임" - 매일신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wQTFnTkQ1OWM0OU9vQmh4ck9wdk5Sb0pzdkZZX0tKNzNXbDdNWWlNVGJGTnlyVjliRThaZG9mZUhCVGZjWU9CeUZDSEZMZUV4N3o1cFBZcjVFQ0J4Yi14QXNn?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | hankooki.com | 국민의힘 재경위원들, 정부 세법 개정안 비판 기자회견 - 한국아이닷컴 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9Kbm1OSGFfem03UlVTMUtQVjJ4TGtGU3IycWV3YWRodmE2UVlKSV9Jd01NWXl4VWRfd0Q1enR4Y2RWVko2WHhTY21UVjVHU1FoOHROUnVuTktDM192R0JoWnh1Rmt2cVJRcFJn0gFvQVVfeXFMTjFUZHBkS3BIcGdabXFsMWpSODNMWVVsQW4zM3dUVEdiOXcwcnNkOGVURHdoNmlSSGwxWWMxYl9fWWpYQ0dlLWkwdHNwN0hRQ1JsNzc2cngxUk5hckNyR21Dajh2R1lpLUhjZmVDdnFr?oc=5 |  |
| tax | ftoday.co.kr | 국회예산정책처, "세법개정안 따라 5년간 세수 14.5조원 증가" | http://www.ftoday.co.kr/news/articleView.html?idxno=368597 |  |
| tax | chosun.com | 수십조원 ‘세수 펑크’ 원인은…세법 개정, 우크라 전쟁 등 변수 반영... | https://www.chosun.com/politics/politics_general/2026/10/27/ICBT5YQXINCPDMGFZSEEMNWJJA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | biz.heraldcorp.com | ‘책 출판’은 되고 ‘잡지 출판’은 안 된다?…가업승계 세제 개편의 ... | https://biz.heraldcorp.com/article/10913027?ref=naver |  |
| tax | dream.kotra.or.kr | 헝가리, 부유세 신설·개인사업자 정액세 확대 추진...세제 개편 주요 내... | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=80&CONTENTS_NO=2&bbsGbn=242&bbsSn=242&pNttSn=244760 |  |
| tax | 조세일보 | 한국조세법학회·국회입법조사처, 30일 세법개정 쟁점 논의 | http://www.joseilbo.com/news/news_read.php?uid=578449&class=7&grp= |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

