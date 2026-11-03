# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-03 12:17:09 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1663건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:blog_community | 1 |
| excluded:category_cap | 18 |
| excluded:company_event | 2 |
| excluded:company_self_activity | 3 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 29 |
| excluded:financial | 3 |
| excluded:foreign_news | 1 |
| excluded:industry_specific | 9 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 93 |
| excluded:no_regulatory_signal | 77 |
| excluded:opinion_piece | 1 |
| excluded:similar_news_merged | 44 |
| collect:event_announcement | 11 |
| collect:law_name_mismatch | 5 |
| collect:no_category | 21 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 206 |
| collect:out_of_window | 31 |
| collect:tax_subject | 9 |

## excluded:blog_community (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | brunch.co.kr | 외감법인이면 만사형통? - 브런치 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE8zcGFYUXpjSUZPcF9lNUxuY25hT19oMDJqTDFxSXk3MVNVOS1hUldwb19pNC1lRlcxb2taR0pYQ183QnJTdi0xMm5kc2ZoVl81ZE9J?oc=5 |  |

## excluded:category_cap (18건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | 회계기준원, KSSB 기준 확정 발표..."기후공시만 의무" - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB2cWxadWxVWDJhT1hOUkczdU1WWGtZWlNKdVlPbmIzTVc4c0hMVlVzV3lzd0RnZjR6eEtNY1VaU05XQzBiMmUxbnBSRFE4SjdfMHNpYWdEN1hvWmRuVHY5b1g2ekZPZzdFbENVYQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ESG경제 | [단독] 지속가능성 공시 로드맵 내년 1월 발표 계획 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5wNV9rc2dQMTJKQTVLcnpSbmY2R21OYjRuUzBCSjU4YnNVbGdJMUtsRm53NGlKYVZ5bXg0a05wbmlfYnJzT29UR3R3N2JHaHMxQ1ktdmVxTk5rLXBIWUdDeHJ0bW9oU0haUkliQw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성 공시 제도 로드맵 초안 및 확정 공시기준 주요 내용 - PwC | https://news.google.com/rss/articles/CBMif0FVX3lxTE1Gd29wMWxoczQwX09wRThxRzhCam43V3VTRHp6LWFzQWgyZUdjeTF5dzJBZUJoYnlLZFdYWEZlbWVmRDNEcHM5eGVpTGhPSThiUEtkNlpBTlVVb2laR1FlSnlCa2ZBeG5uWFFvaHNfdG9LeExxeFRLc1ltdXgzcmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | womaneconomy.co.kr | ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 | https://www.womaneconomy.co.kr/news/articleView.html?idxno=259937 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 2028년 대기업부터 시작…스코프3는 3년 유예 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB0NEtXNnFZdGJLd01zRG5XaGUtZ1RyX1hFMTB2REQ5VlVJRkZzdVFJODBNVHdqTlhBZzZtQnZtM1N2dXhtc2tma3pMaEMzX3N1cjFjOVl3RE91Sjl6Rm9zV251UDBQYUo5NWtXMNIBcEFVX3lxTE1jYVpBZ1NRcDNjb0ZpaGh3Q09TZFpINmN2b3BxbTJMaGpJeVVqQ1loMHhkRjJYZkp2ZjVkTEN4R0FWM0lrcWtsSUphSW4wUHZ0MWw3ekgwb3JZeE5hcmNfUXE0VkxUcXhWOFdsYXlZVmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | yna.co.kr | 국내 대형 상장사 "ESG 공시 의무화 대비하고 있지만 일부 부담" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yZUdEcHdYT2V3Tk1jbEs1aTVwdmc1TUZhbzA3MmpJVXlHQXRCeEFVclI3YW95am5UNTU2d29fZTA3ZGZ1NElDU2o3dWhHYTVzcTd4LUs4bi00cnPSAWBBVV95cUxNWlJkdmlVWkFDR0czQlVSYlZ2c2VFdjZxOXcxQ0ZoeW5tNFllTEhzX0pVTG94UXJwemFHRnVWODBRZXZWTUlGOVZUNHNkODdKOTdxZ0NlZWlKdnFvOVpib3Q?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 증선위, 만호제강 회계기준 위반 적발…감사인지정 3년 의결 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1sVHAtUXQ3WjNRbkIwZ0piSjUtRks5R1FQeXRrYXkzUTMtdXZ1YWN5b21yUkwwVnFJYk5YVUd4V3g5WkVkeGtzUFQ3NXlmQll1MEZEdWdfdndQTE5INC1RMVFiMUJ2OUt4dkE?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ZXAtQlFZQjUwUV9rbDZDZ0dodTF2MGw1MG9NS09xRUFJekhCQlcxVk4wWkJmZVRoYlkwR2xNdGJEbmVrdU5LRV9qZXpzbkNXVVVNeXlDc3BRZ0XSAWBBVV95cUxQVjBoZ29XNWttV2hfYkFPTG1KWjRuTXRadFBtQnhON29lekYyck5PelV1b3hnbHZVa291TmpZQmdRak1FNmhKLTFTWkZsOGJSZnBUQV91eG9kNXNiV0sxcHE?oc=5 |  |

## excluded:company_self_activity (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBhZ3dNVjNHQldlUXYzVlltVzgwTGtmb1ZMWlh1SHZwNDBhemYtTkF6c1dPVmxyNHE1dlVuSTg1ck1yUHB4MzVqdlRjQ3R5R296RXc?oc=5 |  |
| kifrs | idnfinancials.com | 아고스 프로조사스미토, 재무제표 발표 앞두고 BRMS 주식 550만 주 매입 - IDNFinancials | https://news.google.com/rss/articles/CBMimANBVV95cUxNQVc5WlBJeEJ0Zzd4b3RxVnZmWGxiMXlkbFNqb3JNX1QxQ0NFcXlRUVR4OWgyZlMxMEM3Z194M0lBYlhDRG95alJMdjdHV1R3N3BhTE5KN1BlSjBadFE0b3V6UWZxMGhRcGw3ZnBFUEFNUEhINl84MXU1cm93cGxVOG9OQkhiVFFCSUxXSlZ6aHBZSUN3dVVHTFZoTEJzRnhwNzBRVFo3ekJtTXAxSTVSYnoxVllERG1ncm00dkVuZkVzU1V0cEtHSlhmeEhnMWY3OXZiNVVNYS0tUXpnaUljc0JYd0RSTXR5dEhMOURoN0EwN2s3STlCa3BidTRNWVZSNUp0dDRVSTZ2THA5eWUxWTNDUW1DRFVUNjdHYmFqd3FwSGY0Z2d6WGNGSkxwbHd6YTRDYmE5UmJHUEcyS3Excy12OTVtSUhEQklPSjFqMlhTcFh3d214bnhNYjFzNVhjekU3Qno4TW9zeWhud1hfM1B6aU94WFEtbDNKc0NyaThYcWh1a252R1BxRWRyWVpqelFyb01QNW8?oc=5 |  |
| kifrs | hani.co.kr | 수출입은행, 회계처리 위반 기업에 여신 54조…“심사·관리 강화해야” - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8xX2I3MlBacWZXSVAtZUxfb3Z3amdGYm1OOVVEVGZtMG92V0VkdnEtTDJ1WVMwSVU3UWVCa0J6bVluTkh0U0luY05Bbm1Vb2tKT0VVbTc1S1R5Mk0wUmFWSUNmcF9CdGs?oc=5 |  |

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
| kifrs | core.asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFBCZkpUZzR6MDU1TFpsb3YzajlvTUt0eW01Mk1WX1FZamlEb0w3UEY3dFdOWjBJQVJkbE12cThnT3pXbWc2WVl3UU1lM2IySEQ1U192b1NnWlNBX2d6UVdJY0d3?oc=5 |  |
| kifrs | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| esg | ESG경제 | "ESG 공시 강화에 중견기업·협력사 부담 가중…대응 격차 우려" | https://www.esgeconomy.com/news/articleView.html?idxno=17072 |  |
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
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |

## excluded:financial (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |
| icfr | news2day.co.kr | 한국캐피탈, 내부회계관리제도 고도화 나서…투명성·신뢰성 제고 - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE1fVjl2UnRnek5jelpoRk9reU55VW5IR2ZuSGpGbkVzNkVuYllnbExVWUZlMTU0N2JLalhEdmhwSmtPcDdYQ01ua3RJTkU0dFBxUVBQdEtmdHBaOWl5Z1E?oc=5 |  |
| icfr | 서울경제 | 카드·캐피탈사 순환근무 강화…금감원 내부통제 모범규준 정비 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5yMmlfZHJmeGF0N3BFaW0tS1NmZUZXM2dEQXBCUmM5NHV5aEJwcXNCN0Z4bG5ZWlhsaGpuU3FGUDgwQlZ3NTRWM3R4QVRVUUcyVHfSAVNBVV95cUxPZ2JSaTVKelZ2S2NNQTQtNzRyaHQzODQ2THVqOWFOVHhVaEltN3NpdmRfR3VIaG9WZzRXanRaOWdndkJHYUFMWDRXUWh4NS1HWVFoTQ?oc=5 |  |

## excluded:foreign_news (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | idnfinancials.com | 다난타라 신호 및 재무제표 발표가 IDX 종합 지수를 지지합니다. - IDNFinancials | https://news.google.com/rss/articles/CBMihgNBVV95cUxOOUdlRXhTX0RtdThUZG1kNnhzS0pjRVQyc3FKV2NwRHRqMjRsdE1Selp1aGFOYjVZY3BnM1dvMVRNZzRLX25MeGxmc2hMOGlZcHZlUWdONHhnUUYwVjQtMnViVDhWdkdpNU5UWDc3Wm5pcDF4bGYxS3hWQ2doVzdFbGM5cktVNXFSNDVQdTJWVWhKOWRTeU1uQ3FkTDlNZ3JqejlJR2xaQ01NVlg3U1FqVUhOeHN2UEVUOWNISDZ0NTJZN2o0M0JIOVpXR181ZHoxTE5jZUJyeWZpSWNydWZSNGNFeFNPTktEZ0dLVWVhY2J6ZFZIS2hPSnF0RHV6eGRHRFg4dWI4R1ZzOEduYXlXNUw0WFJtNE1felZvNmlKYUVWYkpuMmZKOVRka0p2R3FzWHUxeDNqY0hrci1Sem56UE5HWlNDbHNIR3dtQVdsWE0zOGM3VFJDbVBBSmxQVHBMZTdYNjFFM0VOdk1BN3B2anI5My05TUlXa3lJZEJrR3pTVE56R0E?oc=5 |  |

## excluded:industry_specific (9건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 2025년 제1117호 보험계약 | https://kasb.or.kr/front/board/comm020View.do?boardMngNo=&boardNo=&cmtreadSeq=&seq=494&siteCd=002000000000000 |  |
| kifrs | 한국회계기준원 | 2022년 제1117호 '보험계약'과 제1109호 '금융상품'의 최초 적용 - 비교정보 (제1117호 보험계약) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=316&searchfield=ALL&searchword=%EA%B3%B5%ED%91%9C&s_date_start=2022-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2021년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=300&searchfield=ALL&searchword=1117&s_date_start=&s_date_end= |  |
| kifrs | 한국회계기준원 | 2018년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=231&searchfield=ALL&searchword=1117&s_date_start=2018-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2017년 제1104호 ‘보험계약’과 제1109호 '금융상품'의 동시 적용 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=220&searchfield=ALL&searchword=&s_date_start=2017-12-01&s_date_end=2017-12-31 |  |
| kifrs | 한국회계기준원 | 2015년 건설계약 공시 (제1011호 건설계약, 제1037호 충당부채, 우발부채, 우발자산, 제1115호 고객과의 계약에서 생기는 수익, 제2115호 부동산건설약정) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=166&searchfield=ALL&searchword=1115&s_date_start=2015-01-01&s_date_end= |  |
| kifrs | hapt.co.kr | ‘공동주택 회계 감리’ 법안에 “옥상옥(屋上屋) 규제” 지적 - 한국아파트신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1zVlZtb2JHeEpyV204Q3FUVTRVU1JiRWswRmZuR3RDUEk0TFVhRlI3OVgzek00MlZwOGlQUmp4elFQRkFjMDh2YThBV05WZlhzeV9SZmhWMEl4WF9DcUZDc0ZwOWh3aEcy?oc=5 |  |
| kifrs | mediwelfare.com | 요양병원협회, 29일 의료기관 회계기준 교육 - 의료&복지뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1pZmFjQjF4dmlPZHRrdjBWSTUzYmdMM2RZSGNvLUQzR1Z6SnQ1NkFEQnd1anVLN0VSb1QyOVg1bXllUDBGNERxUWozY0ZtdE0xNmVEa0VlanFkbENySTZCdm1CY2pnSEh3aE0w?oc=5 |  |
| kifrs | hapt.co.kr | '공동주택 회계 감리' 법안에 "옥상옥(屋上屋) 규제" 지적 | https://www.hapt.co.kr/news/articleView.html?idxno=169530 |  |

## excluded:manual_id (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |

## excluded:news_too_old (93건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9zaTlJci1iWW1GZ2c3TFFYUUxvS3JWTnZJNXZmQm1rdUhGSzMzUTJvM2hwNlBDdGhKdmJ5WU5ZRnR1MDJIYkl6bTlfZFEtMXE3Q1E?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 조세일보 | 김현정 "尹 정부, 3년간 신외감법 무력화" - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JdDQ0dDRwdlpDdGhzcnpHZ3hhZ3V3OXFqbXplRXJ5SlFFeU5VWXhlZHg1clRpNHVfQ3B6YXB2RDZBR21GSWlzVnJ4RnY3NDRpaURGVVBBTW5UWWtzQnd3?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | ESG경제 | 공인회계사회 새 회장에 최운열 전 의원 당선..."신외감법 유지해야" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5wczU3VWVubFMtUTdpOUI4Sm5XQUozYW9mVjRwQVY5TlEtRE5heC1nSnZrWV8waWZjNktsX2MxZk14TC1sRTdCdUxhbDdtZldlQkhsRElIVFBya25mLW5PLUFMd2xpR3c0X3VV?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | kbanker.co.kr | 회계부정조사단에 ‘10년↑ 전문가’ 포함…외감법 손질 - DFT 대한금융신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBtdGx4aHdKQzluYXROcmN0dUxiRHoxWUd5ck0wYTFPNEhUdXFiUjZYWFhhTjBCS09HNG1FYzNCRi1ySnZDcm1raFpidVh3N0tYaXRqRjZNMEo5bmw2SVV5S1FHWnJfRk9CYUk5Y9IBcEFVX3lxTE9ZN1h2NEU3Y3BCd0VES2QwMzhveXo2SDZPeGdpckdLVUxXcEwxdWJfTTk4WE9ydjBHblNNaTdVWnI0em9IVXloYy1SMlpnc3dUcHdCaC03d3UxQ3dhMkVlUE1KeHY1MXNJQXhqNVNlbTI?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | 일간NTN | 외감법인 주주 500명 이상이면 정기공시 의무발생…"IPO 예정기업 유의해야" - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmR1RBZURFNTBjZXVRakRjaWVfRHN6QnJucVdVLWVqaExkcjlReTZYazY3ZExxbGJLX1E3dkhvZ1Q5ei1vRVlZR2stUl92Q1BKV1QwUFpuMExaQnIxNmVrR3dTU1M?oc=5 |  |
| icfr | tfmedia.co.kr | [감사인세미나] 최운열 회계사회장 “외감법‧공인회계사법상 형벌규정 합리적 정비 필요” - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE5wQ0ltZmZmdENDTnZ1eF9kZmIxRUg4RVJrOFlhN2dQVVgtM0dBcExGRUdjVDRzY3R0SnAzRllzZ3FaaTdaMEh6Q0JvdnFpY2t5eTRNT2x3RVE1c1VmWHNqVmJZTQ?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년④)"유례 없는 감사인지정제 폐지해야" - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SYVZyanVjZE9LQzY5OTdsWEtDNWhDMmxFZmh4eGNyYnN5RWZkZmNhdjd4M3Rra1FrRVh5dVFwem9CUjM1WkpOUlBaSUZ2ZzBzalJnaFN2M0tFSlQzaTJFeQ?oc=5 |  |
| icfr | m.ekn.kr | 금융당국, 여전사 내부통제 모범규준 시행...동일부서 5년 초과근무 금지 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzUkZ2RFlzUjE5OUZ4b3ZxOURwN3ZORVo1UWFXTDBrckdQREVSMmVpbUFkU0VqQzlHNkVVVjBvLWRPUURzenpUNkVjZXBrTlpMblpmMDdmWXFjcnc?oc=5 |  |
| icfr | biz.chosun.com | 대우조선해양 회계 조작으로 도입된 ‘신외감법’, 기업 부담에 소폭 후퇴 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNQmQ5eVo0TEJUNlRkN19FSjNSZUtkM3dRVnNJZ1Fyd2o4cFBJUlVFU0xMRTNhSFpSRjhkWlVvV1VUMjJXYjhuSnFzc1gwdW1WWlhUd1RfTHRuNExyc2tka29wOXN2RHBEMDNnNmxqUV9lZ0JJbGRzMkgwczJuLXJ2NGdWeEJoMU9E0gGcAUFVX3lxTE9sZVczell6ZTBVdnVVLVdkam9ZZFJXd2UzNm5oTG4xMlVhMWkwWjFUT21SZHJOVHZuV2ZrU2hhdkpBR0NwZGlzV0ZqNEl0bm5sZkJKXzA5Szc4X2h3WGppQi02YXhVNy05Um9EUzFCbUpsVGdFOXRlZ2JXdElVeGJZTnhkdnQ1cTdhMUdsWXZUMEJDaC13RTJoLVN5cQ?oc=5 |  |
| icfr | 매일경제 | “외부감사 대상인지도 모르는데”…감사인 선임부터 하라는 외감법 - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBfb3RIa3ZJZXVfMGlqNXVPSzh1bXhyMDdxRXY5Zm9tM2xselczNFhncmwwWGk3VE1McW5RZ1cwY0tydHBEdW5oRWpfUm9JMEVINFdhUg?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년①)회계법인 배만 불린 감사 강화…품질 향상도 '낮다' - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBTdWt1T1hzUXZla043LUxoallBVWtGRHpDOHA0Nnh2c1pXRk16dVR4MUM2UHdBcUx0SXhvZFVDWFQ3QktDd2gtcUxzbWExTnFvQWxLam1KMkVXQnRiQ05XSg?oc=5 |  |
| icfr | newspim.com | '신외감법 도입' 회계사 인력난 가속도...시간제 고용도 나와 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9jN0V1bGFpbDFpcGJOcTRFR0JOR0lCT0ZKUy0yS21MQ1NQYVUwbHY0RWFKRUs4M0cwUVJsZEhuR2tGUjlLUlBDeU4zRjlWRFhpUjg5Ukc0VGY5UzNX?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | 일간NTN | 우리회계법인 공인회계사 외감법 위반 감사업무제한 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1KdDNUR3BQVVl1dGtYZ2prUllIQVhuOHVKYXdKcW4xbmUxQk5LaExyeXFyMnp5ZTZSTG5TN0RENEp5NEJWeHRNSlVjRjEyMDNsc0x3Q0NRNEZrSDBuejVxNXczOHd3RHA4VWc?oc=5 |  |
| icfr | investchosun.com | 두산에너빌리티, 회계 논란…신 외감법 이후 강화한 제재에 치열한 공방전 예고 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPd3hmMGM1TkJ4dFQwVkt5a3hmYmdZbmctQy1GYnpoR2JyUGN1MURsVWFyUWhtVENCaF9wUk1wZW5sYWhXSmp2OTBLeHFQN0pPRk5ESnZHTndNXzJzbmFjc1E4aTlzcXJOLUNKV3I0UVhhNXdFVS1wbUMtYmR3TElGVTRCMA?oc=5 |  |
| icfr | fortunekorea.co.kr | 글로벌 기업 깜깜이 실적 드러날까… 금융위 외감법 개선 검토 - 포춘코리아 | https://news.google.com/rss/articles/CBMickFVX3lxTE9GQnJfSm5OMk5pOWVUUC14aFBrQUJUZEJuMnVzLS01MU0tM3M5UzA5RzNPTnVfS21iUzI1QzZxNmU0a09iUG1RU0ZEY1hPdUtzNEFDME9pS1JqdmlFZkhULXUyWXh6ejZ5WU8xWTRmMFhYUdIBdkFVX3lxTE1Md0FkSEpRTmxlZENOUXBSRmtDMzBoZjl6dE1xTi1QcmtsN0d0OTR0NXhyVjdGUGpGSlc3dXpoRnNBQldzcWlzU2NzRlhsdlJieGhUS3o0ZUtFcnFTLWdCdmtDbmdaOVVIR0RRMU10LURKRXBIUlE?oc=5 |  |
| icfr | ceoscoredaily.com | 금감원, ‘여전업권 내부통제 모범규준’ 마련 - CEO스코어데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uT1g3UWpVTlBNRkRaZ0lXdFpDT1RuekF3QmIwVlE2NFJaTTJYRmZSaU5fRERFUWdoaldUc3BYZ05pU3h6RldDSFA3cUxpME1nMzRtMG1QWmdrNU1jcUgzRDM2WmdnZw?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | tfmedia.co.kr | 기업 재무담당자 70% 이상, 신외감법 ‘긍정적’…회계투명성 대폭 개선 - 조세금융신문 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5BeFRkTl9qUGNmOTNkX1R6UlcwYXZzYTFIc3NHdklsRGZ1N2NUd00yRjVmYUI5TDdNSVRwZlhxY0gxMHhqWjlnbk9NUWJqeG1UZU1uYThRSlM5R014YlJBRjB6N0lXUQ?oc=5 |  |
| icfr | ibtomato.com | 신외감법 시대…발등에 불 떨어진 코스닥 - IB토마토 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1wTnhJTjNyNlBDcXBLejBQRm16NmxYYjlGa2htY1poZkVTTVVMcGFkNW15M2xwMUFYRDZlLUN1SEE2M3JpT1oxZ3MtYlFIai1nWHdKTTlkVDB5VFlUTVR6MnAxVFJWendn?oc=5 |  |
| icfr | 머니투데이 | 신외감법 주도했던 회계전문가…'회계기본법' 제정까지 힘 싣는다 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9zZ2tGSkR1eU54TFk4RnYyTUlzcFhjbWNDdlpuTHkxNUppQnVQdHhQcjRtY1RsT2JkT0xudVpxdlVHSG9MSW9nWDhNa3FvRS1pUl9qTFlRcUtQMkRUY3hqSHphMTNRN0Yz0gFuQVVfeXFMTTlSZmpjcWZ5eDdQZTVwRjZPQzBmSXFScEN0bFlyanVlLUlTdGN2Mi10alpTZTd5ckVxei0zTGxWLUNPQTVISTNhb05PeUpXaFFwcXRHTzdUYm1xRG5zSDRLcUxsUXlVcy14LUhqQUE?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | paxetv.com | [1분 영상] 최운열 신임 공인회계사회장 "회계투명성 높이려면 신외감법 유지해야...감사 비용은 투자" - 팍스경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9tWWdmYkxZY2dXTDVBV2xJeFUtLXU0S213RklleTJDZUlCd0ZSQTFyc0FPdjVhYXBGZjBQTXNaUHNsYXpGMzZlMWNMNGMyVlZSNWc2WEd6c0NtX0VibnVjVXphVmdpbldj?oc=5 |  |
| icfr | 일간NTN | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - www.intn.co.kr | https://news.google.com/rss/articles/CBMiakFVX3lxTE5BbndhQ0dRSk5hQzluRU90Y29uci1RdFJ3SHlBTTZGY2U3c05mRlZOVW42bFlDYVBYMmdhSTgyQlJidjQzd2FZZHQ4eDFvMFlzLUdneHNkLWYtMjlsdHJTdXZjSkxNQUtuVnc?oc=5 |  |
| icfr | zdnet.co.kr | "중견·중소기업도 '신외부감사법' 곧 적용...미리 준비해야" - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE94ODR2UVJKYTdMMjEwVWZRRW9vUlFQdkc0enB5RFBiVTgxRjBKUENtLTFUeXpneU5nZ1k5THlfa05PZWdZZTAyZFFVZFBmaEt6MFlJY2h3?oc=5 |  |
| icfr | newspim.com | '비외감법인' 데이터도 공개..."비상장기업 투자에 적극 활용" - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9RN0FQbk5JNG55OWZCTXN1bi1XLXNPUHR4WWJiUnZNSHl5eFk0M04yRGlYaTQ2Njd3bE5MbnRRenBIUm1RUGxGaVljRXNUWVZQVThxQVNhdk9FOUdP?oc=5 |  |
| icfr | newsis.com | 초유의 오스템임플란트 횡령, '신 외감법 무용론' 번지나 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SR1lOd2VmanJnVW9FQXRwSVJYUlIzSkNnRndGNEcyRmlxUGxiUUE4VHkyZUwxbFZOMk1wMWZ0dXh3QUlkOXlUWHNvYlh2Qm80QlhOMGlydTJvTXNyQVF3N9IBeEFVX3lxTE1CUVJtSHR0MHpJa2JOZ1dtODNsZUp4ZlEtZ0g0ZEFpNDVzNHM5RlZndGdpS2xoc3hDcUVuOUsybGxVQUotSzJmdlRadEdPX1lhMlVMTzN2RzJaakNuWmJrZko3ajBfbmVNVXZ6eWpOemh4ZVNrOWEzcQ?oc=5 |  |
| icfr | byline.network | ‘신외감법’ 적용받는 유한회사 – 글로벌 빅테크 기업들 - 바이라인네트워크 | https://news.google.com/rss/articles/CBMiTEFVX3lxTFA5WXBCTzF6LXIyb3R6MDNzazViYWVBNzVjOHVCMlJncXdyUTdxQmdmMTFPNVpNckVFYXBlTVp5TkFZY0MxcWROUy1NdDk?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | 일간NTN | 여전업권 금융사고 예방을 위한 '여전업권 내부통제 모범규준' 시행 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5YVW5sNE1GN19VOTFHTVd6OGxFWE04LTA1d09Id25RTVd4VVhiU2pQdlAwRGlaUklEZjRzOU5oRDZJWmdDTGJ3ckU4U3Y5Z2t5OXVEUF8tdnY1WVFHQjFaeFYzYzVxa2RjbFE?oc=5 |  |
| icfr | sentv.co.kr | 한국거래소 코스닥 상장법인 회계지원으로 新외감법 대응 돕는다 - 서울경제TV | https://news.google.com/rss/articles/CBMia0FVX3lxTE8yYVhXZ1F0cTN4OWY4ckhBUWFuZHBoT2E1c29Zdmo4WWtYUDE5OWhONUc0TVlNT3lvbzgzcjNLWGNMd1k3ZVl3VVJDOXkxRU1qRFJXQ0tpYU1VRUR6LVVZZG9YMFJ6LVl1Tzlj?oc=5 |  |
| icfr | zdnet.co.kr | 더존비즈온, 내부회계관리제도 시스템 'DICS' 출시 - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ZWDVfQU95b2dIdy1LZE1MZWxXRUNPY3gzTUxjLUNMdDVjU0draEpfMWZJOEJzN1gtb05BVUZiNE1xODV3LW5TTmR0VnA1YnJYV1ZhbEZB?oc=5 |  |
| icfr | fntimes.com | [프로필] 최운열 한국공인회계사회 회장…신외감법 주도한 전문가 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE4wWUZmaWJVbHVCRHNmQng0VFYxZG9kTGVuQmhqSmtlekt4MEZtODRIWTU0ZjhYczd1dzZIaWlCTzJBNURnWVJqRmp3ejA3end6ZUZMTzZtbkxYMmV6b2dCQWJKVGRjc2QxV2dUVUdSSWNydy1YdndvbzBZTWg?oc=5 |  |
| icfr | tfmedia.co.kr | 新외감법 국무회의 통과…자산 또는 매출액 500억원 이상 법인, 외부감사 대상 - 조세금융신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE9vTG94WUNKczB1eWVZX0tpbmFISWhGU2NOS0VCOE9oMG9FMjBpTFVyWHFsNjdXbVAyNkJPUVBwcC1OdlR0NTBIaEl0WGtXWUhlZUtiNVFuWkd1RW9OQ3hhSzZB?oc=5 |  |
| icfr | ajunews.com | [경계불문 DX] 신외감법 시행에 ERP 회사 더존비즈온 바빠졌다 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DUVhuQ0cyWmN2YmtERDB3aWRYTmVGMGlfek8yQ3lQTVpkTFdMLTZKVkpqZDN6RnhpQUhLcTVUa19CdlROS25TdUdkcU9rc0IyNkRYMUhKM2tIQdIBWEFVX3lxTE5NT1pQdWFtT0RrNS1SbG1Fdmx1SmhJYlVMcjQzSmpMenpNbFhtUWVNZldfc3FyekduZTkyakl0YTlHZ0R4MkZxN002Zy02cWV4cTlGMGlfR1Y?oc=5 |  |
| icfr | etnews.com | 씨에이에스, 新외감법 대응 위한 내부회계관리시스템 'ControlWare' 재출시 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE03bTFIY0VhM3FDbE83bncta3kwdFFMNHFpY1NVb0lZV3drZWpOWUViNzZSekhXM0VxVmJCZ0VPSmdHQTlocUdkY3IzNlNTQQ?oc=5 |  |
| icfr | infostockdaily.co.kr | [人터뷰] 정우용 상장사協 전무 "표준감사시간 등…新외감법, 기업특성 반영 돼야" - 인포스탁데일리 | https://news.google.com/rss/articles/CBMidEFVX3lxTE1MQ2U1WnhmMFZ6eFZFQVl1ZWhzVWVQZWxKYklwX3VkRUtMWWN3OUt0Zko1QkhCY0xzSUxSWXhGU28tamowM1QwazdKQjZRd2RyN09uMTNCcGowMjFFWEY2eXVBblg2Yk1McFBPaVl3TlZ3OExJ?oc=5 |  |
| icfr | g-enews.com | 여전업권 ‘내부통제 모범규준’ 발표…금융사고 예방 - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPdnN1VDh3OWtkWUZQSlUwaGZqdFVtYWpZcC14YXhnMlBKTDlkczNkRl9DQ1drMGRrdE04dzJvaktvYmR0V2JDakp2YkpqUVhZbVdwdC1nY1lNS3NGLVBDU0o0TmxEaV9ocWJxWjhmTzh5S0M3bXRIb1kyaGtTamlKZWtsWQ?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | 매일경제 | ‘新외감법’으로 상장사 회계법인 교체 쓰나미-삼성전자 감사인 누가?…빅4 판도(삼일·삼정·한영·안진) ‘흔들’ - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFA5cno2VzNKMGd0UlJ4UjI1Q3hSamxObEItQWNqYThZcElJYm4tR25UZGVOYkhVNUhYcXBMNlpGV1hLQ0hOQUZnck1jdFBHWXlLcXk4Vw?oc=5 |  |
| icfr | fntimes.com | 금감원, 신외감법·K-IFRS 제·개정 내용 설명회 개최 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE51eTFBa0dYOXQ5UEt2bmF4SFUtZ0cwS0l0NjZRSUZTYlQ5d01iOGNPNHBQTTBvQTA5N2lycVJYc0s3NW16T091M2xmRjVydmRJekFheUU1TXhvZU94MXNaZVBvQUVMLWtMUXdvWkcwalR4NTZIbUpnV1JSZnA?oc=5 |  |
| icfr | sejungilbo.com | [재계리포트] 新외감법 ‘그룹 연결회계관리’ 비상…더존비즈온 ‘EFIS 10’ 주목 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTFAwMkJtZHdlX3lNSUxIMWRMMkNZb0tRbjJkNHF2Sm0zbm5GeFdjeGE0R2RRRFhyX3FSbXJRTXpPVmpBSHlKR0R2NzVPTGtES1pTZjhhd1hkbjNzQ0dXZGFxWVZ4dnZaelltNnZ1Zg?oc=5 |  |
| icfr | news2day.co.kr | “新 외감법, 부담 가중” 경제인 앓는 소리 진짜였다… 감사 보수액, 4년새 2배 '훌쩍' - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Jd2hPSnlTb2h1bmhZbXFvSmI4d1JrZEQwTzV3eFZfX0V5c201YWF6Nlk3YmdhQjlnejN1UjB5TDQ4V1Nfc0R0aUdUTjludGN0QzF5MW9OTl96ZUhtWGc?oc=5 |  |
| icfr | etoday.co.kr | 28개사 ‘내부회계관리’ 비적정…“내년엔 더 문제” - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBMOW1idWYtTDJmTzJCazdzXzF6dVRNbzRsYklQaHFSRkc1Zm1MVFRiX0hwZ1ltNHVJTFM4Y0JZYTh1OHc4Zmp5MnkwR2tSYUdYMmo2SA?oc=5 |  |
| icfr | biz.sbs.co.kr | 씨에이에스, 외감법 개정따라 내부회계관리운영 소프트웨어 재출시 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE9CdDhZWEJKNm1ZdWRTcDM0RndZMkY5dGo0cjZCU3RucHBFM1BVeUk3cVFzMEF6WGdMWC0yNEsycTNJRWtTYlltcXNIa0pjaTZDaHhn0gFYQVVfeXFMT3lNY1Y5VUxSOHVnU0ZiWEZyb1M1V1ZMVElxZnIyU0U4TlEtTHE5aHVwekdxU2p5amVVcDYtaWpzcHBqUl9JT3RyM0RELVpKTmJ1RzJYSGszUg?oc=5 |  |
| icfr | itdaily.kr | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 아이티데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE1CODVGNXBKQjRGMjhVY1pUU3JiQXIwU25Ga2NkeU9IR0xaVzlwYXVxdkZSeFVWWG00WXprcHlIRlM4R0ljbFhvWmFMeGRPTlRnbm1uT19JWHdrS1FzdFhTbTJjZEU2QQ?oc=5 |  |
| icfr | fntimes.com | 삼성 등 금융그룹, 내부통제 구축·통합 공시 도입…감독 모범규준 5월 시행 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE5GRTk0ekFOakRta0tINzdwNTFSQU1yb3hzNkRKbHN4dkxVSkwwWXRHa3l6UVBSdFdBV2JxT2JGV2tlbzQ2RU1nUGRIdDVYVTNPWmh6eFJZT2ZaUEJVWGduZXdOOXhiOFFCaWJhQmktelFFcjJ0U3FJS2lpQ2Q?oc=5 |  |
| icfr | 이데일리 | 서울변회 "외감법 개정안 환영"…국회 조속한 통과 촉구 - edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxOVm1uellJdWhSME9jdzExNTVjZ3FpZWVobVlqVmtTZURBdnZieW5NRFd5QjNzSW41cVlqTnJmdl9Zcm1NQjFpdDIwU2lwT0hKdlkwNC1uak9xcUswQnZ1TnB6dl9YNVV0dXlrdTB5ZXlaX3JvZ2ZyMzlaRGg2YnNFMw?oc=5 |  |
| icfr | newsis.com | 외부감사인 선임 45일내로 단축…'新외감법'시행 본격화 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9oc0dCbXI4OXR0SU9FSVdXM0ZQOXgxSHZNRGplVFhZX1pUZms0ZFpWWWZnX2RFbEVnWGlIWnBNc0JNUU9KOUxBS1EtczhhTGlOZnFQcEIyUTJkMWM5eTRtNNIBeEFVX3lxTFA3ZXU1SVRsUU4tMDd6ZzcxZnRYU0tIaEJWeUFZclVKVlpUT19HM0Q2QTBxbnRicjJQRHo3ajlxYWx3V3FLMnlrTWRUZS15T0dfTmtqc3NRazdnSGVrMUNPUm9LSWVBQ004TGNpRTZpY05abGpuWExWeA?oc=5 |  |
| icfr | m.bikorea.net | 더존비즈온, ‘딕스’ 출시 - BI KOREA | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1oSE9NUDlTaGlDenVfdHhWYVZMcVFJSUxGUU95ZHAtNVh6Q1hQSlZSNmVFM3RZWUdDb2ZfZmFnNmpyWm96RUVGOFBWM0RBdXlISlBuSkt2QU9weEYybFZMUkF0TUE?oc=5 |  |
| icfr | thevaluenews.co.kr | 은행권, 비예금상품 내부통제 높인다..."DLF 재발 방지" - 더밸류뉴스 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE1ud2JVUmZLcHFXdHRUcmZfNU5RS0pHZ20xV3BPUU1tOUNiSTBVOG13SEpHcklMMlVNelZuNkY1N19QSVpXTWpTX0xyS3M1TWdyUVFv?oc=5 |  |
| icfr | 이데일리 | 헌재 "법 위반 이익·손실 벌금 상한액 안둔 외감법, 헌법불합치" - edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxPOFE2aWxObU1Fd0pRQ3FCOGV6RkRQTFlVRWc4bzExNldzZ01vWEIyUUJ2T3ZIaGNZOVdGejEya1pqTmYxZmNBWF9Fa19Tb0xUOTBxTGhrdkhVWERlY3lKbkxBaGs5Y2lLYWRaQjRUb3dHX2JMV29QN3lSeWptNExKRw?oc=5 |  |
| icfr | ajunews.com | [기업쇄신]최종만 부회장 “신외감법으로 회계부정 어려울 것 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE04aDRvZjFQWkc5Tl94eFpxYmRaWFczbG5VdHBGREhIN0JaSy1MRnBqZ3hTdlpodmItZHhrR2lsRmpWRTdWdTZkQ0FYUFZkcndwNDF3QnRPbUY3d9IBWEFVX3lxTE8zdlk3LWJBOFZWZzVRbmtsWjhUNU1Sci0wazNJRVZtNDA4VXEySXBzWXhPcWVibmhGb1FDc2hBQjFpSm5PTU5BR2o2VlAzU1F4c1Y5YWtZYUQ?oc=5 |  |
| icfr | daily.hankooki.com | 新외감법, 내부회계관리제도 시스템 도입 필요성 커져 - 데일리한국 | https://news.google.com/rss/articles/CBMibkFVX3lxTFA5QzR2eGtpWW1lcWszaUhtc3lvTHp3TDZNc3QxRmJXTjd3RGZYMDM3RXBGZDhic2U4STFJMUYyenBmNHg5YXlBdnV5cm1idHBRR1hBbjAtamhsVDN3Y0Vxb2s2OWNuM05JTWtXS2h30gFyQVVfeXFMT19XcWVUYzd4V3FiRzlBSGJLZXZoeVYzeW1yU1k1ck1yVHh5MlpucFlwMktrSkJkeUhJVjdXRlJ1ekJsRjNBY0gxUU5nczBnRVdvbDUtNktTMVZSNnpXUzk2UXpSQjMxSmc5QXY5YVRrRmdn?oc=5 |  |
| icfr | indifocus.kr | 채이배 국회의원 주최 신외감법 중간평가·제도개선 간담회 열려 - 인디포커스 | https://news.google.com/rss/articles/CBMiQ0FVX3lxTE5NNzJ5OUh1RGlfb3NTX3RxcDZlalhqb050ZlRPZ2F2eHYzVWEtSXRRYklDRW85M0k0NmxuSHZnUndUdkE?oc=5 |  |
| icfr | sejungilbo.com | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE8wbVA1bV91THUxeGRfdFo3SzItRkQ5M2RmNDNFeG1QUzZQS0ZQR1RFemphaWRHcVlnbWZHN0FlVy0waWFuMlIta2EwQWJOdy1qWWZIV0drcmJWTEFSLXVpZDZrQVRsQW1YeDBJUg?oc=5 |  |
| icfr | 이데일리 | [新외감법, 감사비 논란]①회계 개혁 눈앞인데…보수 놓고 갈등 - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxObWFhT29aS3RIZkJKODZUWEN4WjlGUmIzU3ozU1l1WmZUbXZ5OGxaWjl0eWY0aDg3UEZZRzNfSWtabEkxemMzNUM0dEtpazdjS2ZrM2FGanFhNFowY1JySVFtMXBWbzU4djB4MzNOa285S3prR3pqemZLSmhvcnN1OA?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]뒤바뀐 갑을 관계…회계법인이 '기업 결산능력' 따져 고른다 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxNVEd6emg0SDFlcWI4LWhaZFhwS2tBdVB1TjFQeTkwb3JxRGEtQ3kydmFGSlNIQV9DbXNHdFdCQjVwLW83cnlwZVpOS3Q0ZVFST2U4NnUydGxZUE5OLWRCLWF2RzBnNXM4VjluOFpvd1l3SllFWnpndGhHMGtWc3NWMg?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]전용석 딜로이트안진 본부장 “회계투명성, 기업과 함께 높여야” - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxPZFh3QnZzRU13RFpUbzRacTJkbi01RVJuU1BuWDJIajBWcnd3UmttSGtfZnZGcFI0QmxEMGtfZmdNc3ItVms4Z3ZvaDlqZ0pFb3NUSTNVSkxVVVIxNE9HdjRlaGx2YkxwOE5HSEdoNFVCV2ZEMkxiWVlvZVRlUGM4QQ?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]윤훈수 삼일PwC 대표 “사람이 경쟁력…최고 지원체계 갖춰” - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxNc2FJOG9IU1IwTnl6cXlQLXJqdm9tVl9sVTVmXzNlNFZLd3dVbUttN1VJSDdDWThEc2FUei1QWnhzSG9hRjY4eG1TRnZiNnBvUVNIM0t1aXk2YlFIUlFiS1UyUzRpaTEtVjV0ZWZMN3QtbVZDSjFUVGNTZGpvYWhGSg?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |

## excluded:no_regulatory_signal (77건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE43SzV1ZWNkVHBRQzZUUkJ4OW5zQWoyekgtQ2pvZ0FJTXQ4NHVLNjYwa0lPa1RqVHpMemJzRUNxLUJyeXpuT29LWGVJbFNLMWZtelJseHBfNWNoVTBuVVJtb2xoWlpEQ1oyY3c?oc=5 |  |
| kifrs | CPA뉴스 | [재무제표 수다떨기] 기업 인수 뒤의 숨은 이야기, 외부평가 의견서와 M&A 공시 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFA4UVFYV2FvWGtPaTZjbVIxQjBESjVJenlJallEaERzQXhUczVGMm1KVmdYb1BwMzRlXzE0dXlhUXA5eS1ya0VwNVFRSnVWM08ybWJlalFfLUUzOUI0OTdVNUlaelFMTEFL?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, 회계기준위원회 비상임위원 1인 선임 - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5acXJMcUxsamFWTzZRRU1MVU5nazdpUTVUUDhMLU1NVFdjYlItenhWQXJPcENrZW54a3RXZG9XeFljdnZNVXVjbUxmemdtUWNEbGpKRnJ4RGxHRDhLY1Q5RTlQamE?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QQkdfaGlxSmJXLWJ6ZWxsbmxpZVhYZHJHRWl4V0VIalhpZEJEYXJIUy1CSFQ1MzF3TEM5Y1JWdkxvVmkzZDNQSUpyVTNFSExWS2t6Q01Qem9VTkM1TzVheWpUS3Y?oc=5 |  |
| kifrs | 한국세정신문 | 빗썸, VIP '블랙카드' 운영비 편법 회계처리로 탈세 의혹 일어 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1kdDl3OTdXT1NxX1V2SHhwbkQzeTh5eWg4R2RYcVROVFlKV3NtRlJ5SHhIRzhWa0tvcG16MDF3YWtZRFpLbGh6UE00YWgyTVZEcHhtX3lnSHBsaGx3NklFRmpMeks?oc=5 |  |
| kifrs | 일간NTN | 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1OV0h5TUE1U1VyU0R1eG5FWTkzbmJyM1RrQkpwVkxVQUhfNzFJcmcxTGpGT3U3SUlSWjNsZU1YVVBxQVFyc0Y4MTZRSXhfVDJyaEtoMndWWlhXOWVQMmJpWnRMalQxWjNudWc?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원-한국환경산업기술원, 지속가능성 공시기준 이행지원 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1Dbm80OFRBdTd1QjFhRDA5dTFRMjNzR3QwaXpkQnBzdllCaVk2SXNVekZ3WVNIaXJhTXhScTF5QTYzS2dTWHlDcW9KcU9ITjJkWmtrTnhSNmN2UWJfS1ExOWhlLUJtZnhUeVE?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, ‘지속가능성 공시, 새로운 기준의 시대’ 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBPT3dBRVdDZDVhdEFkU1ZZWmx0Z2daaHZkbGtpY3ppa1FWUVpmOGdldEdwcHRHUDM4RmhPOGVuZXNGeE1RVXpid1dnblpnYm1LV216TUlFMkhjazhmeEtwVG5kY0JRcHlwc3c?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑧] 현금흐름표도 함께 바뀐다 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5OWVd5Z0VCYWFKcFRxZ2MydDVicTBORGU5YzhnTFpXQ1NLRFJ0ZHNLVzRKd3N2SEZuQlJqTFZWb1ZidWN2MGJfQmM5ZzdWZmVvVXBTcGNlNFRhT2ZTT2pqYnZ6bEc3aXJv?oc=5 |  |
| kifrs | 일간NTN | 증선위, 영풍·고려아연 회계기준 위반 적발…감사인지정·과징금 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBVYjhpbjhCWGZMXy11SUxRNkVneDZyek1hclFyTzB1WU1KRkdQRFN6NElBczZpWHN4U3BhRXhwMlYzSUZrSmFiZGhubjRGMll0ZGx3TUlwak9qakpONUZpRjk1OG1fRFk0SlE?oc=5 |  |
| kifrs | 일간NTN | “공동기업 재무제표 오류 반드시 검토해야”…지분법 평가 오류 사례 공개 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE56cTAyejRleHo1aGMyUWRaTkxPa0NnTFJoODJJTkk1M2hjRkNpV1dWNlMya2tzLVZjVGpzaEJGV1hEdk9JQ19FX2NCQ0N4UlVQOFExSEt5YW9OVTUwNmQzQUNaYk5fRjdpTlE?oc=5 |  |
| kifrs | 일간NTN | 금융위, 만호제강·의왕백운PF 회계기준 위반 제재…과징금 9억9640만원 부과 - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9MTW43ZkRaY0EwNkh5N3FrSFAtU2tkVmZmTmQxMWg5N3lVYllzZl9qX2lCSkhXSGNIVXVHVW1Mbnpib2dweXUydUNkc2JRaHRtWnQzVE56b2xYeVFWU08zYmd3QUI?oc=5 |  |
| kifrs | 조세일보 | [진단] 제각각 회계기준, '회계기본법'으로 통일되나 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iZExnWDViSmtJa1VsVmpUS3MtTHpYcDNDQU1iWkFWMlBkYi1QMjljcW9za0MwUjE5Vmg4V2dkdDg5blhYZjFrNkhDRmRkbnZ2bjVla0pOR2xMenlvUEc4?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑥] 두 개의 영업이익 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5FRUxaZW9oYmNpYTBhR3h5d0VOQ0NtQmxKU0NHTTFsc3ltYkhTQURmNmV6TGMwNnBtOE85QjFvT1l5Sk9zRHpUX1lwZUYycTVsY1NYRW9seGpuN0QxaDZqdVZLeGczMk1i?oc=5 |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 매일경제 | ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE51S0dscjIzU0MxMnhMZXB0elJqR3lfNnFHTzh5QzA2UzNhbUtVX0hhVnVHTzNIU01QZzV4YVZodnJSLW1vZmktQmcxOGRkWWhPeUE?oc=5 |  |
| kifrs | 한국경제 | ‘몸값 6000억원?’…중앙일보 진짜 가격표는 [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1MbUtmTVBIS3ptTXgzUzNIRHZ2eXc3NnUzSXVlSEhxU0ZOcVI1VTZ1MENuVUFCNTFmMlJaMXE0SHlaSGU1WVVhZnk4S3dFWWwtRWx1aGY3cml2VDlyQVowVXdORnhJWlZwTERtRA?oc=5 |  |
| kifrs | 서울경제 | 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE41YkVzeThWTUVTaGpkSnBmRDVfWVprSTY2UncyajZDOUpiZFVYTDN5eENqM3ZQcENzZm80RjZwTVNxalhNaWQ3bDRkYTV3S1JnNFHSAVNBVV95cUxOSy1rVnBqeks0alRJRUZOaGVubDNZSmpBYU9TaTY0ME5RT1NnLUtUZjdfZGp5QkVvSTNQMmRvS2pUTlpJR2RXYlcxTklYNW5wNlVxRQ?oc=5 |  |
| kifrs | joseplus.com | 회계기준원, KSSB 공시기준 파일럿 테스트…전문가 TF 논의 착수 - 조세플러스 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVeU1lZTlHX0JVazgxRndLeWdMSEZEbGZOVkJxdzAzUjZGSnAxaEM3bHROQ2ROWHJoZ0pnQWhmZTVPUHFESWFnU3czT1lpMmpMMDNj0gFTQVVfeXFMUFV5TWVlOUdfQlVrODFGd0t5Z0xIRkRsZk5WQnF3MDNSNkZKcDFoQzdsdE5DZE5YcmhnSmdBaGZlNU9QcURJYWdTdzNPWWkyakwwM2M?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| kifrs | vietnam.vn | 주지사: "세금 납부용 재무제표와 은행 대출용 재무제표를 따로 둘 수는 없습니다." - Vietnam.vn | https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMlVmMUd5WHVuNnFqNDhjdjZtVnlrZFhNYXhJZHh0MGFxVS1rYTJPSExDclIxcWFsY1h1UUZTWnl5XzRRNmhlUTk2NkRDVkZRVEh5SVdJdzIyWVk1UG5QRmpqOW9EWUdRZm92bDBPU3JNZnllejZWME9hRkdLQ2lETFlRbHNJRUtzeThLaVVaTlVvUXBBdm5TSzRDNmtSRU9LQk9abkMyX0k4a3B3djdmN1MzUURiYl9OZ2RR?oc=5 |  |
| kifrs | snmnews.com | [현대제철 IR] 3분기 요약 별도·별도재무제표 - 철강금속신문 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBOWWEyWll4OHFHeG9MWHUyNUdYbksxcnRhZ09jQlFBdE9RUkJnRDk3d0RoWWtQSWhQcGpXU0gyNmJqZF9sUEpORjNDWVhKNkRQZnltamhiVXQzeUFjVDRXZzVvLUlCeEVkZnc?oc=5 |  |
| kifrs | cstimes.com | 보험사 실적 '고무줄' 논란…회계 기준 바꿔야 - 컨슈머타임스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBKQ1I3ZDI2MzJUVVp5NnBOVTRJNk9PdU5Nb215Nzcya3IxcTRXZ3ZaVV9sMHdiWTg4aE15SmJNWFhBQXhLWm1iWmNJdTlnQWVZdU4wc2Z4UEl6elEtTUsxdDRNSTJ4TjZxVmc?oc=5 |  |
| kifrs | sentv.co.kr | 금융위, 해태제과식품 회계처리기준 위반에 과징금 약 13억원 부과 - 서울경제TV | https://news.google.com/rss/articles/CBMiZEFVX3lxTFAtX2dCMTRIT3lLOU1qUWtVd2l3RVBWbjBHaURXMHowbnhsSmdGSS1qd24tOVZkV09BSkVMTzdFTm1pdTVweFl6ZzBNVG9KdkVIQ2xuWW85TWRPanlGbFlSSlVldUg?oc=5 |  |
| kifrs | m.ekn.kr | [기후경영 포럼] 윤나영 한국회계기준원 팀장 “온실가스 배출량 측정, 조직경계·산정기준부터 따져야” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBwSENJcGZ1alVPdzFhZEREMjZSamRuYTFyLUJYS2xhX25zd1RIXzd2SjZzQlVyZVBqQXp2VnQyUkNTSXNEamFuZU9UaGQzZ1lDQVJXbXpRWXp5TEE?oc=5 |  |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 해태제과식품에 9억 과징금·감사인지정 3년 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBobFhCYWR4N0lQcGVqalJueHV6TzVVUVdxZmVWVFQtaGlOcGM4akhva1hsYkdkMXhURkRNcnNvb0Vka2RMOHFpZE5YQTRtRElLYzBJcktKWHVLV1JXSzZSZg?oc=5 |  |
| kifrs | newscj.com | 안양시의회 예결특위, 결산 심사서 세입 편성·회계처리 문제 지적 - 천지일보 | https://news.google.com/rss/articles/CBMiakFVX3lxTE56bHVRcjE2MnFTZVhzdmFiaU1pU3IxZG9ScHc0LVZyZzg3YlRuOUNaMUd1aDJCcDlUSXM0UHlMNlhHT1NxUHpJMzE3ZEJNLUNCSWRBbTJCZjBiUDdGVHRRS2Q1bThUbEdaY2c?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1118호 영향 관련 사전 주석공시 모범사례 마련 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE13d18yem9ReWp0R1hMQXhJaVctcGpyTzgxRm9XSXBNOXZxcnNZaDhfZVgzajBhR0gwNm9EQnBmZElrWWhsQ01mbE05dzc5NmVWbksxVVE5STk?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 눈에 띄는 LG이노텍의 수익성 악화...사업 포트폴리오 고도화에 미래 달렸다 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1ORVdUdkZBZVRyajNHa3pVeTJjR1JGTDVuNmlibWtycmN3TnVpVUtXRGhaQlBpRWRkMmZwcE1objBEV3hUV3A5blVoNVBpbmNWNmMyN1EyRzZWN0lldkNYZ25QbGdFT1dFbUM0cQ?oc=5 |  |
| kifrs | tradingkey.com | ETRA\|Electra Therapeutics Ord Shs\|가격:8.100\|Chg%:-0.540 - TradingKey | https://news.google.com/rss/articles/CBMibEFVX3lxTE1LSDNVV0pDZVFvU3FJeDBhZ0JoQnUzMWw4U3dmSVFtSUFXdWtPVUVzaFVqcE43bTVVSjFwOU9lcG9ucDZ5d244eWtVX2tsSHoxNDY4OEdwVGE0UzgtQ21fV2hub0p6WFdIWl81cQ?oc=5 |  |
| kifrs | news.kbs.co.kr | 금융위, 금양에 과징금 76억 부과…“회계처리기준 위반” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBWaTRGZl9ncHJaNnNyVVJYa2tNLVZ1WU5uTG1iMjNfZzVOTFZPM19BamE2RHIyalNKMFdrcnZRbWh1amNza0JGUmxVdDg5NjdMTWdsSlpnQ3BwbE0?oc=5 |  |
| kifrs | khan.co.kr | 영풍, 회계처리 기준 위반으로 204억 ‘과징금 폭탄’ - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1YYzUyQ1hlWFFkZWl5ZU9meEtjaDBLWktSYXFqWFU0Nl9oeTFmQnQ2N201S3RoRkJ3dzdMSFU3enVBYVZMdVhCV3lNVHg5X3BXWl9ZS2NyOGZYQdIBX0FVX3lxTE91cDQzanVYOTM3MFFPeUhrS0ZjaDdlN0QzTWZPSDlzZ0IxS3FMc2U1Uk5WX01pQ0N3V1Nrc3dXMWhQWXhnWnBOMElaVUVzOHVWbzVHQmNMQ2toNHNaQVBN?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBJYkpxaXBTcjhUQkZPcHVfay1mQnptQXRhMklhUVNBQ3VSZy1WYWpzeVp4eGdkMmF2bHhDclR6ZHMtMnNJQlNWYVFmb2tsWWxYYndaTEFrcVVHZUnSAWBBVV95cUxPelVLaldNY3hnelFDQzFqaVY0UDBDX3EwY2xkU0QzS3JBc0JBUm5STlFaVlhxRnlpN0FmbXNSQjdEd28zTXFCQWctb2JYN3JLWGZQcUZFdEM3MzJtOFhTTlk?oc=5 |  |
| kifrs | etnews.com | [기고] 회계감리 대응, 숫자만 고쳐선 끝나지 않는다...거래실질·자료제출·내부통제까지 본다 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE9HZ09Dc3F4WjdxRnByRmlYU3FjN1dGVzEyVXF5N08waVNablpCWWF6SFhXbHJjWGRkUGVGalhOY3VxQzllNTFDdjZUb0ZGdw?oc=5 |  |
| kifrs | joongang.co.kr | 기준 바꾸니 27조 흑자가 적자로…새 회계기준에 지주사 ‘비상’ - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE4ybk5IZk1jY3dMRTE3a21sWnlBZ0RYcVpPYnduMW56UzJhek1fellTTEdkMmJSelc1LVBIME55clJXYko5Z0lnbkpEakVFbmVkdmdzbHB3?oc=5 |  |
| kifrs | m-i.kr | 안산시, 복식부기 회계처리 정확성 높인다…11월까지 컨설팅 추진 - 매일일보 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5kMXpHWEhyOUpvVzVwbmM0RFQ1ZGgtNjFTY1VETHU3RDlQd1d5MmExWDMzS0NYUGlEZlYtQzhEQW16Y015UnQ5X2IwbjBRWU1rLWg4R0xnUUZZTk9WR1N4RUs4OGE?oc=5 |  |
| kifrs | lawtimes.co.kr | 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE05MDRqekxIcGRMRFZhMmdwVnM0OWZ3R2lMRGhka0NDWU1EblRBMFplYXc2bldHUDJvMnJtaG0tSnFaX2U3ckt1WXY1U2FxNk1zVm1yb0lUb09Mb2o5elV4S3ZNWVRfSUJPdmxvRHhR0gFyQVVfeXFMUFhvWmtXbVVXc2lzOTFnYnp6bGFkWnc3T2kzcC03bFVzam5Sb25NNWZsSmt6Q29WVmUyZ0EtYVY4SC1IVlB5QmtXTVIxR005WDVzdDYwcDhramd6dXRGOGh5eHdZRnVrTTBoYV9FNzBFbnVn?oc=5 |  |
| kifrs | news.bizwatch.co.kr | 회계감리 중징계 영풍…내부통제 시스템 허점 논란 - 비즈워치 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5aNFQ0V2JXaVMtOVBoRVNNV2RZNE1GYS1mcE1Gd0J2NDA2YnhGaUV3cFJmZldxRDh3eUdNdkxvRktUNEFkQ1NkMVFCaVpBZG9TenNBYVR0Y09KUkZnS0poeUxQNjhEaXhKVVVSVg?oc=5 |  |
| kifrs | yna.co.kr | 2025년 재무제표 '비적정' 상장사 53개…전년대비 소폭 감소 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMOWoySmx2N1Voc05Ba04zNC1ZYzBBZ1A5aUdXNzEzVms5N2hyTHA1ald3Zjc5dnRNRHh3LU9XLWtmTWJfR2Q5eV9aSzBnQVBCX3VHTzNsUnNKT2PSAWBBVV95cUxPTmZ3M2J3VVctVkFTTmRhU01tZkRBTkROS3Rmb195V1R6OTJrYjRUNG1uUXh3Z29sTkJXRDhpaS1ZTUQ1ZkdrRHZJdnV5SDhCRktQQ1JYaWtEWlBTTm1od1I?oc=5 |  |
| kifrs | yna.co.kr | 감사 전 재무제표 제출 위반 76건…전년보다 24건↑ - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lODhfd3R3TUpXOFZneW5tMjJ0OEVEeXBMWExHS1F1MzNOdExVUlNsdTFwYVpFZTRxLXNTZzZoZzRmQnhhYW5ZZlhtUjJJM1M4YXA0ZWNCbU5ubzjSAWBBVV95cUxNUWMwYlBCMlpvS2R1a2dOaVdCYkRqcE04YXNwb0JCSC0xb3NSc05OM194Z2dCcVhiSFU1elMzQklVZHNCc2dtRG1wMk5kSTJmMW1rVWZWdDFQcjZrZFVRTno?oc=5 |  |
| kifrs | news.kbs.co.kr | 금양, 회계처리 위반…“행정소송 맞대응” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE8yTHV4QVF4ODRCdkZraVFaV0ljWkV1Wk5QOFVQRUF3SEZRaXhrNll0bU9ONkxuZTBzaHhNOUtLTDRXVFR5bFZMWWlTM21YSHRrOVJaTHlabWphRzg?oc=5 |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5tQWI5RHBpTVRkQWY4TEhWVXdJek5VRG50QTBTLW5ZTU4yNDVoUW9wRWtXZldMdXBjMldnSkxzVDV2blFoU1RpMndUX0pWdTNDVDlPYXB5T05RY2s?oc=5 |  |
| kifrs | news.bizwatch.co.kr | [SFS 2.0]재무제표 밖 거래망까지 읽는다…AI가 넓힌 신용평가 - 비즈워치 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBBOFR0QWktVXlHMWpfSjFlTVEzTk1kTm9QQzhjN2VTYWpOVFcwVnlMUnNxNXZ5MzRqOWJBNnY0aWlPY2JWZ2NGNWdkV3hlMXpRdmxjQmtucVc3aHVDRVgxMHlVNGJhRGtQVldr?oc=5 |  |
| kifrs | news.einfomax.co.kr | 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBzREN4d0RmcDJBMXFhZ3BfZVVTRXJOalhqNmNYYVRoUFNzQmJoNHdqb3pmaXVqX3RGTlpMbGVYUGh1dGNHbEpBbXBmQkE3cEI0dVFMS05DaHdjUkswWTk3Vy1qam5vYXhpckdud2xoX1k?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 영풍에 과징금 204억…고려아연은 84억 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sVlBmQzJPbXZuSTFOai1kaDhGb1hLVkpCdktFWnZaU1YweGRJWllmVk9zbUdZQTdpUTVRaFpHM1RlQXllWkhpdVpJUFlqLVV1SEJESnZkVUcyZEnSAWBBVV95cUxQZTlEXzktdDljVUR2UENmbHJnUzFKNE04U3BxTzNETFZBTlA3alY4VGJtREYwdmVvSldHM1JlM1kyNWlsVXJFbUxCaHhaQlBlU3VHTVY2UUh0Uk1aS1U4MzM?oc=5 |  |
| esg | ESG경제 | ISSB 자연 관련 공시 실무서 들여다 보니...S1ㆍS2 보완 | https://www.esgeconomy.com/news/articleView.html?idxno=17209 |  |
| esg | 임팩트온 | 클래리티 AI, 1만2500개 기업 평가...ESG 공시 잘해도 최고등급 못 받는... | https://www.impacton.net/news/articleView.html?idxno=30480 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
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
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | newscj.com | 충남북부상의, 지역기업 ESG 공시·규제 대응 지원 | https://www.newscj.com/news/articleView.html?idxno=3441094 |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| tax | 서울경제 | 경기도, 지방세제 개편 입법 논의 본격화 | https://www.sedaily.com/article/20107006?ref=naver |  |
| tax | weeklytoday.com | [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... | http://www.weeklytoday.com/news/articleView.html?idxno=800450 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| tax | busan.com | 어업용 면세유는 3년 연장…어업법인 세금혜택은 ‘계속’ - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTE5PVHpqNVBDeVdjRklPM1N3TFNZOWh6SkJfSkNRSXU2dVJQVlFZWmJ2TkFWWkl4eDI5TWRvNWo5NVZyY1hlbHgyRjNqNUZ5d0lTN09FY2JCY0dCdmVaOUxkSzd5alBKOV91T0lWM1Q4LXJFdkJU?oc=5 |  |
| tax | etaxnews.com | 지방소비세 40.3%·법인세 5% 지방 이양 추진…경기도 “4년간 14.1조 확충” - 이택스뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBKQ19CZjZfWHZIWmh0MGRPZGZ3aFpuZWFDQnBrcFRPeEl2UTNocVBKaWRXTXk1dTZkeHNRVzJJQlNMZ3FkcEl5SDJTdkZDNV9vdDBlWEx2Vl91VzQ0THFGQy1MUGxzX2ZfOWc?oc=5 |  |
| icfr | datatooza.com | 하모니 골드, 연간 순이익 두 배…과거 2개년 재무제표 재작성·내부통제 중대 취약점 4건 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE14WWR2eUNqYUluVzhxek9IYXdLSEM5bnBUalFuQnhCYkpzZUdQU3QycjZVTXFzdGs5Nk15LW1IWWZDLUVtREpXTWVpcUQ5elJMblpNa05ESVphVVlDYUYyTFhWaHNiNlJIQU94dkVCNTNQMDg?oc=5 |  |
| icfr | datatooza.com | OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE85anpGNUU3UzhJX2JBTDA1dFRqRHhkQ2dhdXZGZ0ZVcHRkVU9Gc29Ca1hXWnNSMUYwOEJEWlR3NmFlblRvSmtIVHhwemFzVFpockFoWFFla0VfUmVVekFaRXAwZEUxSGc4RGt2Y1M4WmFHRmM?oc=5 |  |
| icfr | newsroad.co.kr | "내부통제 효과적" 자평한 빗썸 경영진…감사·회계법인은 "취약점 발견" - 뉴스로드 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5Cdzl4cjBaTmg1YmMwNTFrUm16YmVUcW9lTlBfcU1YWFBXR3kzeGkzWEtibERzajFnMG92Wk9oYWh6Y3FHRTdDNEJJVkNVZWxXLVdLYWpTUm5CWThiTGV0cURIcldhZDRMYU04?oc=5 |  |
| icfr | datatooza.com | 리소시스 커넥션, 내부통제 중대한 취약점 미해소… 1분기 구조조정 비용 41만 7000달러 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE4xYy1JWnFhRGhwbDJwMzRiVkgxUjdfMlYyWl9yMzVQd1NMS3kwanZRR2p2LU9oU0Fob19kbzN0M2NSaE9iSUhBX2hWb1JGTFUyUF81LXp6S0lHa0hLaThtaWhnSTl5MlZVYXJQR255RUVYa1k?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| icfr | mediapen.com | 신외감법 후 외부감사 기업 증가…지난해 4만 2891사 - 미디어펜 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE1scWRLWExwNnFZVlItbzk2QnhHMGo4VkdGc0Y5Y2dseDMtOGFxNDB0LWhTalFDV3J2ODNudEFnTllWZS1odGEweG52dU0zVGlLRFpNVdIBWEFVX3lxTE9KMnZUVy1CTWIybHRmSFFvZ1lqWkJibTIyNzN5eWg2V3lVeVRlLWhYaXJ2VnRKSmVOMXR4b1FxQVpnTnFya3kzV2tLbEh3OUJ4X2hSUVhiTEI?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:similar_news_merged (44건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | joseplus.com | 회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 세미나 개최 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBOTGZHQncyWkZkNWphSDRhUGV1S3ZSNDYxWmxtRVpVUkV4SzVxaGV0eWZ1allzUnJ1REVBTXBsY1BLcGpoVU9JblZRWjZQcy1MSFh4Ym5RWEnSAVNBVV95cUxORWdjXzk0bGwzdHhMMzJMQjNCWm5Rb0xxTWctc2lOaFZmQ215Tl9iZS1ZTGlwckpUTjBmUnVmQ2h1V0ZEdHQtUHJrOUhBZEtCUnJ5QQ?oc=5 | → 대표: 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중심으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFBQcFZGSDROYXJzRmRvdFlZOHJfbDNQME56R1plWDNLM3c3YUU5bmJWUDhpYXVHdU05YzdGOUxLbl9ma3hUeTJCSnpTUUt3LVk5dl9IY1Y3TFJvV082d1Nz?oc=5 | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | joseplus.com | 회계기준원, 김정일 대한상의 상근부회장 지속가능성기준위 비상임위원에 선임 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBWQUt1dDZwX0VzYmZtTTBLcDhpQ1pJZWFrdzhwSW5oTF9sRUV6SDVKSVNqenNEV2o4S2VrdVV5b0d2dmE1RGw3c2hrQzZsRmY3OXZTaXNUcHXSAVNBVV95cUxQTWZfbl9xdnBpZ0I3aWgwSm9HN2t5SVRQaWluVjYycU0xMmZ4WDhHcEJFcktlV25Lc3Voa25iU3BNVkUtaGhENkxfbG1XUEdYUG1Gdw?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | seoulfn.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE51SEdGb0VqY2lPZEJIbFZVNHp4QmR5X18tb1NBMlpxOThhU2pTWFgtS3FtaFhZdzk2eGJ5cU5kcjVnMFM2d19laXNxTG5jYm9HUElEMXdwbml1VWFxTGlfMXRuejlocFVNT2c?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | 일간NTN | 금감원, 감사前 재무제표 제출 위반 76건 적발…9개사 감사인 지정 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9FelZSMGExRC1CYVJ4OUFrTHhCdjMwUy1tSjBoQmZFNER3WWo0Ry04dGZSSmttZlBFM2l3VnpZVnRtdV9ZcGdlcTEteW53WURpR1BMZTdmVm1GYWJ6amNQTmhZZXpXUjdianc?oc=5 | → 대표: 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN |
| kifrs | 조세일보 | 영업이익 새 판 짠다…K-IFRS 1118호 시행 석 달 앞으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFB0MnpUYjZVSVNaY2VaT21MQUJDY0Z1N21nWEtCbVNZVWxZNmE3ZTlrcEI3VFdEb2dlZWpVZ0k1bXVzNlBYUENtcnJSUVlLTWFhNjNzZTZyQmphNy13dmtz?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | junggi.co.kr | 2027년 K-IFRS 제1118호 시행…기업, 도입 점검 필요 - 중기이코노미 | https://news.google.com/rss/articles/CBMiakFVX3lxTE41S2l3VmRscy1LUlowVVNJaW5BdExCQ3FIQ0Y1N3Zlb0FhSW1qSXpBVzZSVXRpRFJzdHNKN2RqTlhxSEk0Rm9SSkpRaks0d0JHNV9VVDFBUGZYeE9keW5WNVVtM3hMdGhVVHc?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPOGFldExqZEFIdGQycE1SbC05ZHV2Z1JaajVGU2YwOWtuSkJ2bmc5aFFSQmJEdGlSVG91anA4RXIyanNELXJDOEd3bkVFclVVRGlSa3E5V01Tb3lyOFZOVVpzQjZYSHo0MUlzSjlEd3dBeTdKeHh5dHlGNUc0VEcxZzFIdW5HRHhB?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | thevaluenews.co.kr | 손해보험사 영업이익 산출·공시 기준 바뀐다...K-IFRS 제1118호 내년 시행 - 더밸류뉴스 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE14eS1FSzVMV0x5TmlpOUpXUHBwSFpuazk0alpNQWhKdXhNLV9mY0piRXlRVVRFVk5DZmNEMm5HZXJqWEpISG5FVks3X1luTGVOSUNMTw?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | ebn.co.kr | '회계처리기준 위반' 해태제과식품, 이사회·내부통제 '대수술' - ebn.co.kr | https://news.google.com/rss/articles/CBMiaEFVX3lxTE91X0F4NDVZYXhKQUZNcWYyNThodFUwdEJ2MEdweXZOMU5nLUEtc2ZQLW84ZS1FQ3hVcXJZcTlONEtHa09vNFQ2Q1d3QXNzSWN6elJGbXNOSXZEMWpoRHMzLTlqbkdGcXJm?oc=5 | → 대표: ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 마켓 |
| kifrs | yna.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VYm1UdW9mM2l1SG84VFJPSnBhSHNGa1dpUzJobWpjNnJ1aXliX2RGMkhNR3FPM09rYjQtREI1d0hBTHU3V2V5aGcwRzJfUEpvaFdvc1V3WENNeVHSAWBBVV95cUxQT2JUYXQzVE5hTGZwR0dROTBxLU93YWYyUDdjMkVxbjBtaEFMYzltaWNJRzRKLVh1OG1ZLWx1ZEJTOWktcHZFRmNOR1lfZzdjZG5wdnB5YzM0M3dra0hXaDU?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | news.kbs.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE83QWNpcGNnbWJVTGVnclJaTDdkblBWbmRVNl9uLU5TRl91NHdlN0h1WEhiQzNNNGhFd2dkbjNKWmVYaGMwQ19sbEh4TU9zZjRlMVBWNkRPb3RBTkk?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | 매일경제 | 내년부터 바뀌는 기업 영업이익 기준에 투자자 혼란 커질라…금감원, 사전검증 주문 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE1XbEZYTE0xMXk5NmdzaTRnR0h3MkFfNU9IQXVoMkozdFdQVUgteGQxeW1jQTZNQWdQZlRvSG5QdFR1d3ItSi1yU2tlOGJrQ1I1SkE?oc=5 | → 대표: 내년부터 새 손익 회계기준 도입…시장서는 "당분간 혼란 불가피" - 한국경제 |
| kifrs | etoday.co.kr | 내년부터 기업 손익계산서 바뀐다⋯금감원 "새 회계기준 대비해야" - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5vbWtNd2xlMWZDeGdsX1BKWU5PSVAycU5qX2tqYXRGRV9hWXMzMTM2RUViZW1JYTh1TktzSXlQaVY3NDZWYy00aTRadmR1QlFwZnZJNQ?oc=5 | → 대표: 내년부터 새 손익 회계기준 도입…시장서는 "당분간 혼란 불가피" - 한국경제 |
| kifrs | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBycHhoWWZqWWRDeFVnV3k5UHZWYktkOFRyaUdodjBSV21ZRmhPSzZNaXk0b3JrVW5UbmFzaklYNmtTWFlza0ticG9fS2JRNnl0VFNYQndsLTVxZXY2VDZyRWtzeVdtWXdyTGc?oc=5 | → 대표: 회계기준원, KSSB 공시기준 파일럿 테스트…전문가 TF 논의 착수 - 조세플러스 |
| kifrs | tfmedia.co.kr | 금융위, '회계처리 위반' 해태제과에 9억 과징금·감사인지정 3년 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE1nVW9jUjhaYTVIc1p6ZjFubzYwSEFsUDl4Zkw3dkpKN2hoeHJoUHFBVDFVa3kwZm5XSEpwM0lXcUd3ZjRiZkhVcThYYlNRa0dfOFZCdUFENUpLVGFWclp2UTNvcw?oc=5 | → 대표: 금융위, '회계처리기준 위반' 해태제과식품에 9억 과징금·감사인지정 3년 - 아시아경제 |
| kifrs | newsis.com | 내년부터 'K-IFRS 1118' 시행…"실제 재무제표 산출·검증해야" - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFB5M3puck1JNk05dVZDajFVRjhtR0s0MDc5bm8tWGVSSXQ4QlppWGV2UXlwVHc5U1JQaEZhTjVqZWkwU09jM3U4RFlXTkYyN1dfQWhNaTF3Uzl4OGtzUkFuc9IBeEFVX3lxTE5CNHE0czVVcE1TUXBYcGg2WTRLdTR5X0c1Uks4SkYxOHF3cE0yXy1KUGhIY1lIeXBvMmR3UXBkUkVNblUyNDF4blJ4eTBNcXYyY1h5U1MwVWNnQThXU3RBYmtCZnZtWkJJbWNpUjNWVUdJUmExYjFGUA?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | seoulfn.com | 금감원 "내년 MPM 공시의무 신설···기업별 재무제표 사전 점검 필요" - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBQc3RBaFduX21VU2pXNEhrSlBLV3Nia0MwN0VDVy12Y19ZZjRITGVBVUFQMHl4eHBWV3pSM2txQXZocXhMd1FTSlNweGhsMFFqV0VncS1DVjlNa2xjVWRaOVlkbGFNc2YydHc?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | insnews.co.kr | 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5PTnlLYzlLQklteE1MaW50MjZwRV9RQkRtZDAyal9rdVpCc1pvNXk0M2tCS2hLOVpFa18tVDFmd0VQTDh6bmVBZGR3dkdIU1VFR0ZrWWFrOFpRRkZ1a0Z1eUxsNG9UOG5ncjZF0gFvQVVfeXFMT3dydTBxd2xRSzI3ekVzdF9GVEdtakV1TURuT0VTOEFSbkloTURQV0UzX0F2NWk2MVFqYVBFaDdZN0M2V2xTOGhwR3N1RTB6QnNWUlhNLU9RNkVEbUpmZk12cXlUb3NXUmJJc2dWcFFn?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | alphabiz.co.kr | 내년 새 회계기준 시행…금감원, 기업에 사전 준비 당부 - 알파경제 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1DVjBKVS1Bai03amhmX0k4Zlg1X29uN1RWQjFRNElnYzBDX3JsZHIxVldxTUYzY21EZElaRlJ4eTlYYUdrb3BIWnlTbjZ0T095ZzNMMWlRTEtfeG1QcG9NYnctNXV4SXJodVBZNjJR?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE8teDVTVFFGcExHbG5QekVJcDJNbkxQNVVOamZvdmpheXlIQ2E2WndnOHR2RVA1YnQxZ1JXek5RcW1DZXJrWW9vWE9oblVUZjFxQUFKeWJEeVEwSlc0ZS1MSw?oc=5 | → 대표: 금융위, 금양에 과징금 76억 부과…“회계처리기준 위반” - KBS 뉴스 |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 | → 대표: 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 |
| kifrs | joongang.co.kr | 법무법인 지평, ‘AI회계감리대응센터’ 확대 개편 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE9vMHpYaEZibllYVUpNMThST2MxRi1ZelNUd3BBWG5qbVM4M2lSNEttSDRzRG5Vd3NrWGxyTFp0VHpBajV3Qll6ZmJIU3dtT2x3OGlpdU5n?oc=5 | → 대표: 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 |
| kifrs | safetimes.co.kr | 금융위 '회계처리 위반' 금양에 과징금 76억 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE85NENZdTJ1VVl2Zl85aFlqUnVCa2tuZ19BWk1BRWpOUkhrQXZVVzNIR1djeEh1YkVBY0hld1FkOGtiTEtlS3lUd29DcVNDdF9XSGVKMUxLeUc5RlQwUXpwbkRkWjFDNWNqb3Q4RzJKa9IBc0FVX3lxTE1MdWw3dTRUX2o2eEtKNFg1Wlgyb2tSY193eml3cUJ6M2ZoZDNRNFVoLXgxRWZZblBJN2xqZklteFExdDEtaEppU0RvZ1I1ZFFUYTExaGVteUxxSkxhOVJQMzhqTlluMGs0MFpGLVdNQ2lpQjQ?oc=5 | → 대표: 수출입은행, 회계처리 위반 기업에 여신 54조…“심사·관리 강화해야” - 한겨레 |
| kifrs | newspim.com | 상장사 재무제표·내부회계 비적정 동반 감소…내부회계 6년 이래 최저 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE81TWRyNUpHREE3djFpQTJQc2tsUjBjTXQ2TmlZdEJjSmhubkMxelFzUTN5M3dlX0VtZWtMY3l1ZjE0Y0MtM0xKVEFycTN5TUJpeTFJZzBCbEZlenZh?oc=5 | → 대표: 2025년 재무제표 '비적정' 상장사 53개…전년대비 소폭 감소 - 연합뉴스 |
| kifrs | crowe.com | 2026년 재무제표에 대한 중점심사 회계이슈 사전예고 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5lYjFWby1TbVI5SWdPLTdTQXdhX3lfdi1GektuUG5LQ0FLMDlDbWVsYm11S3o0ZDlXeEIwTlVxZzlmYVdDajVSUWJDY3FVSGZxSG1Ublg2M2E?oc=5 | → 대표: 「2026년 재무제표에 대한 중점심사 회계이슈 사전예고」 발표 - 법률신문 |
| kifrs | kbthink.com | 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - KB Think | https://news.google.com/rss/articles/CBMickFVX3lxTE8xVl9jR0xORmROcTJxTWtwUFZwbTZ5VEcwNUJnWTdhQmFOamoyYi1yMjFtWUdJMDVMV0JLQk9nRXpmZl90dzhJMHRxYjljS1NHQWJlUHNCZXQ4SklDc1Z3Q1NYbDBpcHF1VDJxOEZia3JZdw?oc=5 | → 대표: 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - 연합인포맥스 |
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| esg | paxetv.com | 상장협, ESG 공시 실무교육 실시…2028년 의무화 대비 지원 | http://www.paxetv.com/news/articleView.html?idxno=284514 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | enewstoday.co.kr | 상장협, 'ESG 공시담당자 실무 쟁점' 과정 개설 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2481878 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | dailian.co.kr | "차질 없는 대응 지원"…상장협, ESG 공시 핵심실무 쟁점 대비 | https://www.dailian.co.kr/news/view/1703168/?sc=Naver | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | newsis.com | 상장협, ESG 공시담당자 대상 실무 과정 진행 | https://www.newsis.com/view/NISX20261019_0003831375 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | hankookilbo.com | 추미애표 지방세제 개편 3개 과제 입법 절차 돌입 - 한국일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTFA1M05NLUNhTTY2ekVWVUZIUG82WHltbkJ2OUNvQnpHZEY2M1IyUlZCdjRyRGMyYzM4NGZMdzVnT3NDSE1hYVlUSUNWaUh2Z29idG5WQjdBMjlYTVBtcHJSZ0JkVWlnZkV5VENjLUFn0gFzQVVfeXFMUHVhOTRjZkJMMUxoSG0takFvaFA0THJfc2xEQmZoMi1yaEtrek1wbUFOR1Q5Q1Z3dzJNdmlVYXFOVDhBLW9QREtNR3I4RDlaZUxlaHo4MU9kWjlkRmdJSUFEWW1mLWZ3dFUtUXcyQlhpOTJiQQ?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | discoverynews.kr | 추미애표 지방세제 개편안 국회로…재정분권 입법 본격화 - 디스커버리뉴스(DISCOVERYNEWS) | https://news.google.com/rss/articles/CBMickFVX3lxTE1NYnhfZDhHV2taQUtZRmRsQ0lrS0YzX1BYZllnSVVaSVJQNHo3eGJyTFE1d3NTUERyUDJXdXNpN3VLQVc0MEREMllTUjNhRTY0MnJOV0JDSUc0d3FxeGNQTnFseTZNdVRUOHVDTkJvTnZ5dw?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | suwon.com | 추미애 지사 제안한 지방세제 구조 개편안 국회 입법 절차 돌입 - 수원신문 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE0wNzAwdTRPSEJuYmlseURxMU1ZcTdCNHBWNURCTmF6NHJwVlhHNnBaT0RTMlREZkNRZ0V1VHh0XzFDa1BrMDRtanRnbU42TmI5QWpqRnBDNzFyNXR1dUtEUjRfSFNCdw?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| icfr | datatooza.com | 유니퍼스트, 10-K서 재무보고 내부통제 중대한 취약점 미해소 공개 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE4zc00yaE5xclJ5OFA1OTBhSkJCNWVsU2tRb19DSmlWQnpxU1FPX0xMblVVVWVrNURlVUk0TUdMQ3ExM0ZPRlFWQWxzbXVDdExXeFhkTkVzbzFKVW90TDBFRGlHbTlTLVFYMXkwTU5jenBwdw?oc=5 | → 대표: 하모니 골드, 연간 순이익 두 배…과거 2개년 재무제표 재작성·내부통제 중대 취약점 4건 - 데이터투자 |
| icfr | datatooza.com | 크레수드, 2026 회계연도 지배주주 순이익 1772억 페소로 증가…내부통제 취약점 해소 - 데이터투자 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBnNFQycEFSeEhqZTRqekp4cnFJc3dQQVVyRWZRNEpaamtHcFFfV2VQUDI3OTZGMXFRdUVmSHpoQUM5VHVjVzdVZ2NIVUdIU0RpU0xiSmFQcmNYdjdrTGVBZFJFdGlCcWl5UTNsa1lUeHo?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |
| icfr | datatooza.com | 팩트셋, 연간보고서서 내부통제 중대한 취약점 해소 밝혀…미주 영업이익 15.2% 감소 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE51N3FTQkt2U2tmcmgzSGdRZkM2azVxMjZsZWNTd2dOanVQN2Rxei1RNC02QkpmMHRfcFFLaFBCZXNvY1c5bTY4eHNoMTZ5OGtaaExYS1FuN2E3LWtuUUI3aThLeFFtVlFrVGxUZVluTnNvYWM?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |

## collect:event_announcement (11건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | 2026년 글로벌 ESG 교육 워크숍 안내 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2199 |  |
|  | 금융위원회 | 생산적 금융의 온기를 지방과 중소기업까지 이어갑니다.   - 이억원 금융위원장, 제6차 생산적 금융 대전환 회의 개최 | https://www.fsc.go.kr/no010101/88052?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 제9회 ‘회계의 날’ 기념식 및 회계업계 간담회 개최 | https://www.fsc.go.kr/no010101/88031?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 제2차 국민참여성장펀드의 운용사들의 국민투자금 운용전략을 청취하고 향후 관리방안을 논의하였습니다. | https://www.fsc.go.kr/no010101/88025?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | 생산적 금융의 온기를 지방과 중소기업까지 이어갑니다.   - 이억원 금융위원장, 제6차 생산적 금융 대전환 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787584&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| esg | betanews.net | 네이버, ‘2026 지속가능경영유공 정부포상’ 대통령 표창 수상 | https://www.betanews.net/article/view/beta202610300070 |  |
| esg | ESG경제 | [알림] KSSB·ESRS 이중중대성 평가 웨비나 초청 | https://www.esgeconomy.com/news/articleView.html?idxno=17019 |  |
| esg | news.tf.co.kr | 동아ST 지속가능경영보고서, '2025 LACP 비전 어워즈' 수상 | https://news.tf.co.kr/read/economy/2361168.htm |  |
| esg | ttlnews.com | 동아에스티, 지속가능경영 유공 종합 ESG 분야 산업통상부 장관 표창 | http://www.ttlnews.com/news/articleView.html?idxno=3157355 |  |

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
|  | 재정경제부 | 국제 신용평가사 Fitch, 한국 연례협의 실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079837&menuNo=4010100 |  |
|  | 재정경제부 | '26.10월 소비자물가 동향 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079839&menuNo=4010100 |  |
|  | 재정경제부 | 물가관계차관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079838&menuNo=4010100 |  |
|  | 재정경제부 | 「의료데이터의 안전한 학습·검증·활용을 위한 국가 AI 인프라 구축」 포럼 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079836&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 미셸 박 스틸 주한미국대사 접견 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079826&menuNo=4010100 |  |
|  | 재정경제부 | 전기차 산업 경쟁력 강화를 위한 현장방문 및 업계 간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079830&menuNo=4010100 |  |
|  | 재정경제부 | [보도자료] 국제통화기금(IMF) 2026년 한국 연례협의 실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079829&menuNo=4010100 |  |
|  | 재정경제부 | 경제현안간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079820&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「주요 국책과제 이행점검」 TF 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079811&menuNo=4010100 |  |
|  | 재정경제부 | 한-독일 이중과세방지협정 개정의정서 서명 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079805&menuNo=4010100 |  |
|  | 금융위원회 | 글로벌 해킹 위협에 대비한 국내 가상자산사업자의 사고대응력 제고를 위해 긴밀하고 신속하게  대응해 나가겠습니다. | https://www.fsc.go.kr/no010101/88054?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융정보분석원, 국제자금세탁방지기구(FATF) 총회 참석 | https://www.fsc.go.kr/no010101/88048?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 불법 가상자산 취급업자(특금법상 미신고 가상자산사업자)에 대한 수사의뢰(DAXA, 3건) 및 접속차단(2건) 요청 | https://www.fsc.go.kr/no010101/88039?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 한국의 풀뿌리 금융,  미소금융이 다시 한번 도약합니다. - 미소금융 재원 기부 협약식 개최 | https://www.fsc.go.kr/no010101/88029?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 국민성장펀드가 국내 최대 태양광 발전소 건설과 반도체 밸류체인 경쟁력 강화를 지원합니다. | https://www.fsc.go.kr/no010101/88028?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 퇴직연금 기능강화를 위한 노사정 합의로 노동자의 든든한 노후소득 보장체계 구축 | https://www.fsc.go.kr/no010101/88027?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융위원장, ‘금융분야 재난대응 안전한국훈련’ 주관 | https://www.fsc.go.kr/no010101/88023?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(국세청) | 주식 양도소득 기본공제 누락분, 국세청이 먼저 찾아 돌려드립니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787734&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국세청) | 5월에 놓친 근로·자녀장려금, 12.1.까지 '꼭' 신청 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787551&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 글로벌 해킹 위협에 대비한 국내 가상자산사업자의 사고대응력 제고를 위해 긴밀하고 신속하게  대응해 나가겠습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787597&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 금융정보분석원, 국제자금세탁방지기구(FATF) 총회 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787494&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |

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
|  | 정책브리핑(교육부) | 디지털 미디어 문해교육, 학교 현장에서 새롭게 만들어 가다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787739&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | '국가 긴급현안' 해결 속도 높인다, 국민 안전을 위한 긴급과제 기술개발 즉시 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787732&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 정부 인사업무 특화된 인공지능 업무시스템 첫 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787735&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 동아시아 기록관리 전문가, 한 자리에 모여 기록관리의 미래를 논하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787745&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 폭염 피해자 지원 사각지대 최소화, 관계기관·전문가 TF 첫 회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787743&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 디지털네이션스 · OECD 무대에서  인공지능(AI) 정부의 미래 논의 선도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787741&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제3차 고준위 방사성폐기물 관리 기본계획 수립을 위한 국민 의견수렴 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787738&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 숨은 물그릇 확보, 홍수예측 고도화로 올여름 홍수 대응 역량 높였다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787737&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 11월 멸종위기 야생생물로 고니 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787736&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 가축전염병의 선제적 차단과 확산방지를 위한 K-가축방역 개선대책 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787733&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 산불방지대책본부 운영, 예방활동강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787722&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 군부대 "맞춤형 산불 안전교육" 성료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787720&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국장애인고용공단,  노사 함께 중증장애인 문화 체험활동 펼쳐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787726&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 서울-양평 고속도로 신규 타당성조사 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787718&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | GTX 삼성역 안전 확보 방안, 안전 최우선으로 검증 거쳐 연내 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787717&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 인공지능(AI)과 공간정보가 바꿀 미래 11월 4일 킨텍스에서 만나세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787716&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해양수산 공적개발원조의 새로운 길을 찾는다, '2026 해양수산 국제협력 콘퍼런스' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787715&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | Blue connect : 미래의 바다로, 이어진 기술로! '2026 해양수산과학기술주간' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787714&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 수산 현장의 아이디어를 성과로 이끈 '2026년 수산신지식인' 3명 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787713&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 한 컷으로 만나는 미래의 씨앗  '제2회 종자사진 공모전' 수상작 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787712&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 검역본부 서울지역본부, 광견병 항체가 시험 분야에서 국제공인시험기관(KOLAS) 인정 획득 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787711&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 해외 바이어부터 필리핀 정부까지…  K-농기계 수출 확대 협력의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787710&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | AI·디지털·로봇 식품 제조부터 고령친화식품까지…K-푸드의 미래 성장 해법을 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787709&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 청소년의 시선으로 전하는 따뜻한 위로, '너의 곁엔 항상 우리가 함께해' 특별전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787724&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 간병인력 전문성 제고 위한표준교육과정 시범운영 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787723&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제47차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787706&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 교제폭력이 시작되는 '지배·통제' 단계부터 피해자를 선제적으로 보호하는 「스토킹처벌법」 개정 적극 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787705&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 민간·공공 협력으로 결핵 발생 66.2% 감소, 지속 가능한 결핵 퇴치 전략 모색(11.3.화) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787704&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 해외취업 지원사업 우수사례 공유의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787702&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 한빛(영광) 원자력안전정보공유센터 본격 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787700&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 안데스 산맥 빙하호 범람 가능성 대비 본부-공관 합동 상황점검회의(11.3.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787699&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 사전예방 중심 보호체계 혁신, 인공지능 보안 대응 방향에 대해 각계가 함께 모색한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787701&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | "연결을 넘어, AI가 만드는 새로운 가치"  「2026 AIoT Week Korea」 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787697&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 국제 신용평가사 Fitch, 한국 연례협의 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787703&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공시의무 위반에 대한 과태료 부과 고시 개정·시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787695&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 청년 노동자의 장시간·공짜 노동 근절을 위한  장시간 노동 기획감독 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787696&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 2026년 제14차 아세안+3 HRD 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787694&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 2026년 공공백신 연구개발 성과교류회 개최(11.3.화) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787689&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금 개발 대전환  - 개발목표 2050년에서 15년 앞당겨 2035년으로 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787690&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 국민 10명 중 7명 "노동교육 필요"… 의무교육 제외 경험률은 8.8% | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787685&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 11월은 고용차별예방 강조의 달..전국 6개 차별개선센터 합동 캠페인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787684&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, '제4회 특별성과 포상금제' 수상자 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787688&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(조달청) | '혁신조달 탑티어' 레메디 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787730&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 군수품 '무분별 입찰' 막고 장병 안전 지킨다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787729&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 국립문화유산연구원, 한국고고학회와 「제50회 한국고고학전국대회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787681&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 공장인허가 사전진단 서비스, 더 쉽고 편리해 진다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787683&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 글로벌 의약품 규제의 미래, 서울에서 논의한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787674&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 국제 전문가들과 무형유산 정기조사 발전 방향 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787679&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청-대한암협회, 암 투병 중인 전승자에 치료비·간병비 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787672&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 2차 중앙행정기관 이전, 국민 의견 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787678&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | "모두의 꿈이 꿈틀대고 연결되는 곳" 2026 청소년비즈쿨 페스티벌 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787675&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 적극행정 우수 공무원 선정... 20년간 쌓은 행정 자료 인공지능(AI)로 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787671&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 세계 최고 수준의 3,600톤급 디젤잠수함 '서희함' 진수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787670&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "11월에도 달리는 국민신문고는 전국 순회 중"… 이번에는 거제·하동·진안으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787668&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 세계 무대에 나갈 우리 글과 그림, '2026 대한민국 그림책상' 수상작 9편 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787667&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '2026 월드 웹툰 어워즈' 본상 수상작 10편 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787666&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 5·18 민주화운동의 진실을 세계에 알린 '고(故) 위르겐 힌츠페터 10주기 특별전' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787665&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 가을배추·무 풍작, 올해 김장은 부담 없이 '한 포기 더' 담그세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787658&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 10월 소비자물가동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787662&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 10월 소비자물가는 2.8% 기록, 김장재료 수급안정 위해 역대 최대규모 김장대책(640억원) 시행, 동절기 농축수산물 수급 안정 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787669&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 가을배추·무 풍작, 올해 김장은 부담 없이 '한 포기 더' 담그세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787657&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 축·수산물 안심, PLS 확대로 한층 PLuS! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787659&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-불가리아 경제공동위 7년 만에 재개…교역·투자 확대 및 방산·원전 협력 강화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787661&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 국립소방연구원, 공주 신청사 시대 열다... 새로운 도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787664&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 공장 지을 곳 더 찾기 쉬워진다,  스마트폰으로 입지·규제 미리 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787656&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | '26.10월 소비자물가 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787687&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 물가관계차관회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787686&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(인구전략위원회) | 김진오 인구전략위 부위원장, 국립재활원 현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787731&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제17차 한일 차관 전략대화(11.2.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787655&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 가습기살균제 배상 심의위원회 위촉식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787654&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 가을철 산불방지대책본부 본격 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787622&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 더 강한 해경, 더 안전한 바다 구현...2027년도 예산안 2조 2,291억원 국회 심사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787620&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청, 현장 중심 특별성과 발굴해 포상금 1억 360만 원 지급 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787619&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 변화하는 수사 환경에 맞춰 전문성 높인다... 해경청, 전국 수사경찰관 역량 강화 연수 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787618&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 송미령 농림축산식품부 장관, 충남 서산 벼 수확 및 쌀 수매현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787617&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 규제합리화 라이브클럽 현장 간담회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787616&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 「의료데이터의 안전한 학습·검증·활용을 위한 국가 AI 인프라 구축」 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787615&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 제69주년 '112의 날' 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787614&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부 장관, 쇼핑축제 현장 찾아 세계인의 장바구니에 K-소비재를 채우다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787613&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년도 대규모 통계조사 업무 유공 포상 전수식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787612&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 콩 생산자·가공업계 손잡고,  국산 콩 소비 확대 나선다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787608&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 문체부와 국토부, 관광교통 칸막이 허물고 '지방관광 시대' 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787609&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 무주국유림관리소, 가을철 산불조심기간 대비 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787611&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 제7회 임업인의 날 기념행사에서 정부포상 전수 등 임업인 격려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787605&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 문체부-국토부, 관광교통 칸막이 허물고 '지방관광 시대' 연다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787603&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 기업이 만드는 지속가능한 노인일자리, 기업 상생 협력 성과 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787606&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함양산림항공관리소, 가을철 산불 대비 총력 대응 체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787602&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 유엔생물다양성협약(CBD) 당사국총회 공식 문서에 이름 올려, 글로벌 산림 리더십 입증 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787600&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국가 드론·대드론 전략 추진단 출범식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787596&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 충남 서산 야생포유류 삵에서 고병원성 조류인플루엔자(AI) 검출… 예찰·방역 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787595&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 넷제로 챌린지X 민간 투자기관 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787594&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국무조정실장 개발협력주간 홍보존 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787593&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처장 화장품 점자QR코드 자율표시 지원 행보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787592&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 박홍근 장관, 호국 보훈단체 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787591&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 미셸 박 스틸 주한미국대사 접견 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787589&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가기후위기대응위원회) | 넷제로 챌린지X, 민간투자 5개 기관 신규 합류 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787588&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 시민과학으로 함께 지키는 산림유전자원보호구역 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787587&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 공공공사 페이퍼컴퍼니 차단부터 AI 업무혁신까지…조달청, 직원 11명 특별성과 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787728&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 우리의(지구를 위한) 기후행동, 전기차 전환 서명에 동참해 주세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787692&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 국내외 석학·현장 과학수사관 한자리... AI시대 과학수사관의 가치와 역할 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787583&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한국과 베트남, 문화산업 분야 협력 강화 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787582&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(소방청) | '가을철 산불 예방 위해 전국 화재위험경보 경계 발령"… 소방청, 화재위험경보 대응체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787663&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "기술 배우고 싶은 국민 누구나" 폴리텍, 직업교육과정 교육생 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787581&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 표준과 지식재산으로 여는 피지컬 AI 시대, 글로벌 주도권 확보 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787578&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 기획예산처, 2045 국가발전전략 수립을 위해 미래전략 전문가와 심층 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787576&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함양국유림관리소 "가을철 산불방지대책본부 가동" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787571&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함양국유림관리소, 소나무재선충병 차단 '공동방제' 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787569&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한-싱가포르 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787567&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한·베트남 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787566&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 2026년 전국 학교예술교육 축제 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787559&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | "성희롱·성폭력, 본인·제3자 익명신고 가능해요" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787554&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 행안부 국립과학수사연구원장 등 15개 개방형 직위 채용 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787553&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 대통령의 외교, 세계를 품다 : 선물에 담긴 기록의 가치를 선보이다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787565&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 겨울철 대설·한파 대비, 중앙과 지방정부가 함께 대응 역량 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787563&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부·제주도, '2026 자전거의 날' 기념행사 개최… 탄소중립 실천 가치 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787561&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 국민을 위한 특별한 성과로 데이터·통계 혁신을 이끈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787558&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 9월 온라인쇼핑동향 및 3/4분기 온라인 해외 직접 판매 및 구매 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787557&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 지방정부 10곳 2026년도 환경교육도시로 선정… 지역 중심 탄소중립 사회 실현에 기여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787556&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제21회 생물다양성 세밀화·인공지능 이미지 공모전 수상작 41점 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787555&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 국제 행성탐사 전문가와 미래 우주과학탐사 전략 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787552&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방드론본부 창설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787548&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 정부, 전후납북자 추가 인정 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787547&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 표준과 지식재산(특허)으로 여는 피지컬 AI 시대, 글로벌 주도권 확보 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787540&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 「2026 해외건설 플랜트의 날」 기념식 "세계를 넘어 미래를 짓는 K-건설 시대 열릴 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787545&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해양 분야의 미래를 하나로 연결한다... 제20회 세계해양포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787544&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 미래 농업을 한눈에! 「2026 대한민국 국제농기계자재박람회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787543&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농관원, 김장철 앞두고 배추김치·양념류  원산지 표시 집중 단속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787542&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 아세안+3 역내 농업 협력 강화와 K-스마트팜 및 K-푸드 진출 확대 도모 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787541&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '제61회 잡지의 날' 기념, 잡지문화 발전 유공자 14명 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787537&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 제49대 이광호 동부지방산림청장 취임 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787536&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 국외산림탄소축적증진(REDD+) 심화과정 교육생 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787534&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 이차전지 산업 성장을 위한 규제합리화 방안 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787530&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(조달청) | '무분별입찰 집중 신고기간' 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787727&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 노사발전재단, 남아시아 3개국과 청년고용 지원을 위한 공공고용서비스 협력 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787529&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | [인사] 산림청 인사발령(2026년 11월 1일자) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787527&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 거동불편 어르신의 일상생활 자립을 돕는 '장기요양 재택자립훈련 시범사업' 공모 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787528&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국가 슈퍼컴퓨터 6호기 '한강' 본격 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787521&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 제97주년 학생독립운동 기념식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787520&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 인천항만공사 제8대 사장에 박인서 씨 임명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787524&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.2.행사시작(10시)이후] 손상 걱정 없는 건강한 사회! 2026년 국가손상예방의 날 기념행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787522&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공정위, GCR 평가 13년 연속 매우 우수 이상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787463&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립자연휴양림관리소 다자녀 기준 완화 후 이용객 1.7배 증가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787517&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 개정 형사소송법 시행 한 달,새로운 수사체계 안정적 정착을 기대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787518&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립자연휴양림, 가을철 산불방지대책본부 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787515&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고)「(약칭)초광역특구법 관련 원포인트 사회적 대화」제1차 운영협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787513&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 「청소년 중독성범죄(사이버도박·마약) 자진신고 기간」 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787512&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 청년창업자라면 누구나, 특허심사 결과 한 달만에 받는다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787509&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 재외공관을 통한 제1종 보통 운전면허증 갱신, 국제 운전면허증 신청서비스 11. 2.(월)부터 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787511&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청,  「특별자수·신고기간」 및 「불법사금융 전국 특별단속」 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787510&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부 보호기관 고위공무원 인사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787508&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 대한제국 황실 만찬의 요리사가 되다… 덕수궁에서 즐기는 인공지능(AI) 체험 전시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787502&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 안동산림항공관리소, 대구광역시 산불진화 교육·훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787507&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 새 단장 마친 '남양주 사릉 역사문화관' 11월 3일부터 문 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787500&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 「창녕 교동 고분군의 구조와 축조기법 검토」 학술발표회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787498&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 울진국유림관리소, 세계중요농업유산 체험행사 중 산불예방 캠페인 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787492&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 같이 발굴한 신라의 역사, 전시로 함께 나누다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787496&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부, 체코 원전사업 비상관리체제 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787505&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 정상 경제외교 성과, 수출·수주 본계약까지 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787504&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 광군제·블랙프라이데이 맞아 '해외직구 악용사범 특별단속' 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787493&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 국립문화유산연구원, 몽골과 건축문화유산 보존관리 학술 토론회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787489&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(법제처) | Crackdown on Unreported Online Accommodation Brokerage… | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787477&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 한국의 디지털 기록관리 경험,  페루의 기록관리 발전으로 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787487&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 안전하게 뛰놀고, 스스로 상상하는 놀이터! 2026년 우수 어린이놀이시설 9개소 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787485&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 중앙마을기업육성·지원위원회 출범으로 마을기업 정책 새 출발한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787483&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 최초라 더 특별하게! 최고라 더 자랑스럽게! 정부혁신 최초･최고 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787481&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 「온AI」 기능 확대… 업무망서 AI로 웹 검색하고 보고서 작성한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787479&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 온라인 미신고 숙박 중개 엄단... 저공해자동차 충전소 실시간 정보 제공 등 생활 속 안전·편의 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787476&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 2026년 10월 수출입 현황 [잠정치] | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787472&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 아름다운 가을 단풍, 산불로부터 지킨다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787470&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 한-일 관세청장 회담 개최...'마약 밀수정보 교환, K-브랜드 등 한일 브랜드의 짝퉁 단속협력, 역직구 확대 위한 해상특송 특례 운영' 등  3대 협력체계 구축 협의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787471&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 사이버작전사령부, 국제 사이버대회 사이버넷(CyberNet) 5년 연속 우승 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787474&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국장애인고용공단 고용개발원, 제18회 장애인고용패널 학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787466&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 광릉숲 정원벨트에서 생활 속 산림규제 개선 성과 알려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787468&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "청렴윤리경영 실무 정보 한곳에 모아 기업 활용도 높인다!" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787465&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "한국의 반부패 정책성과, 세계에 알린다" …국제반부패아카데미 당사국 총회 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787464&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부, 「2026 국방AI 활용 아이디어 챔피언십」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787473&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 위생용품 신설 영업 시행 대비 민원인 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787460&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '11월 저작권 주간' 운영, 저작권 가치와 존중 문화 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787459&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 도서관에서 피어난 문화예술, 주민들의 무대와 작품으로 만난다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787458&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] '나의 부작용 정보, 나눌수록 안전해져요', 2026 약물안전캠페인 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787456&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 정부혁신 국내 최고 사례 선정 발판 삼아, '꿈의 예술단 2.0'으로 아동·청소년의 예술적 성장을 한 단계 더 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787457&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 첨단 신기술 기반 바이오의약품 가이드라인 현장 활용 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787455&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(소방청) | '가을 산불, 번지기 전에 잡는다"… 소방청 선제 대응체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787461&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 30살 국제해양법재판소, 해양법의 미래를 항해하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787454&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 이소영 중기부 장관, 울산 대학창업부터  영주 지역상권까지 1박 2일 경상권 현장 행보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787453&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 안동에서 시작하는 소비축제,  「제2회 코리아 그랜드 페스티벌」 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787452&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | [보도설명자료] 재외동포교육문화센터 건립 MOU 관련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787546&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 재외공관을 통한 제1종 보통 운전면허증 갱신, 국제 운전면허증 신청서비스 11.2.(월)부터 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787488&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 청소년이 직접 찾고 실천하는 성평등, 학교 현장에서 배운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787574&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | [보도자료] 국제통화기금(IMF) 2026년 한국 연례협의 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787590&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 경제현안간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787519&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 전기차 산업 경쟁력 강화를 위한 현장방문 및 업계 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787607&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 원전 공론화위원회, 시민참여단 선정 위한 국민기초조사 시작 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787676&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 충남 서산 야생포유류 삵에서 고병원성 조류인플루엔자(AI) 검출… 예찰·방역 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787693&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | [연구행정 혁신+-⑨] "협력의 문은 넓게, 기술주권 수호는 확실하게" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787418&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-03&endDate=2026-11-03&srchWord=&period= |  |

## collect:out_of_window (31건)

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

## collect:tax_subject (9건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | thevaluenews.co.kr | 국회예산정책처 “2026년 세법개정안, 5년간 세수 14.5조 증가” | http://www.thevaluenews.co.kr/news/view.php?idx=202849 |  |
| tax | ftoday.co.kr | 국회예산정책처, "세법개정안 따라 5년간 세수 14.5조원 증가" | http://www.ftoday.co.kr/news/articleView.html?idxno=368597 |  |
| tax | chosun.com | 수십조원 ‘세수 펑크’ 원인은…세법 개정, 우크라 전쟁 등 변수 반영... | https://www.chosun.com/politics/politics_general/2026/10/27/ICBT5YQXINCPDMGFZSEEMNWJJA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | ajunews.com | [8·3 세제개편 3개월] 강남·서초 거래 절반이 가격 낮췄다…세금 시계... | https://www.ajunews.com/view/20261102154956931 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

