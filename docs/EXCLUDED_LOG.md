# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-10-29 18:10:01 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

| 사유 | 건수 |
|---|---|
| excluded:blog_community | 1 |
| excluded:category_cap | 19 |
| excluded:company_event | 3 |
| excluded:company_self_activity | 5 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 25 |
| excluded:financial | 2 |
| excluded:foreign_news | 1 |
| excluded:industry_specific | 9 |
| excluded:news_too_old | 94 |
| excluded:no_regulatory_signal | 76 |
| excluded:opinion_piece | 1 |
| excluded:similar_news_merged | 41 |
| collect:event_announcement | 11 |
| collect:incident | 5 |
| collect:law_name_mismatch | 5 |
| collect:no_category | 1720 |
| collect:noise_keyword | 5 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 204 |
| collect:out_of_window | 34 |
| collect:tax_subject | 38 |

## excluded:blog_community (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | brunch.co.kr | 외감법인이면 만사형통? - 브런치 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE8zcGFYUXpjSUZPcF9lNUxuY25hT19oMDJqTDFxSXk3MVNVOS1hUldwb19pNC1lRlcxb2taR0pYQ183QnJTdi0xMm5kc2ZoVl81ZE9J?oc=5 |  |

## excluded:category_cap (19건)

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
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 로드맵 공개…주요 내용과 업계 반응은 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5QTEtfY0U0dmlsWDJRenJ2WVYzYkR3MHk2cHdJS1R4T2VXQUs3X1QxZFhtclN2T1lydjhPZ2pUaVdyVGhIM2gzQWs2cUMtOVVvWF9DdUh1b0NTY1FWaWpVM3pNTTRUaWx2bDdKSdIBcEFVX3lxTFBrczh4Q2VrTEdUWXdpeTJYUE9rMDYyaHc1VnF4NndNeGplTUFtQnhlSnB2ck1JdHR2aFpEZ3hPMlhpNnRwX2FNcl96UFZLbFlGVTZhMG1zalkwQ182UjVPemxESWlfdW9vd2hsUk1oSlk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | yna.co.kr | 국내 대형 상장사 "ESG 공시 의무화 대비하고 있지만 일부 부담" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yZUdEcHdYT2V3Tk1jbEs1aTVwdmc1TUZhbzA3MmpJVXlHQXRCeEFVclI3YW95am5UNTU2d29fZTA3ZGZ1NElDU2o3dWhHYTVzcTd4LUs4bi00cnPSAWBBVV95cUxNWlJkdmlVWkFDR0czQlVSYlZ2c2VFdjZxOXcxQ0ZoeW5tNFllTEhzX0pVTG94UXJwemFHRnVWODBRZXZWTUlGOVZUNHNkODdKOTdxZ0NlZWlKdnFvOVpib3Q?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 증선위, 만호제강 회계기준 위반 적발…감사인지정 3년 의결 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1sVHAtUXQ3WjNRbkIwZ0piSjUtRks5R1FQeXRrYXkzUTMtdXZ1YWN5b21yUkwwVnFJYk5YVUd4V3g5WkVkeGtzUFQ3NXlmQll1MEZEdWdfdndQTE5INC1RMVFiMUJ2OUt4dkE?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ZXAtQlFZQjUwUV9rbDZDZ0dodTF2MGw1MG9NS09xRUFJekhCQlcxVk4wWkJmZVRoYlkwR2xNdGJEbmVrdU5LRV9qZXpzbkNXVVVNeXlDc3BRZ0XSAWBBVV95cUxQVjBoZ29XNWttV2hfYkFPTG1KWjRuTXRadFBtQnhON29lekYyck5PelV1b3hnbHZVa291TmpZQmdRak1FNmhKLTFTWkZsOGJSZnBUQV91eG9kNXNiV0sxcHE?oc=5 |  |
| kifrs | news.sbs.co.kr | 금융위, '회계 기준 위반' 금양에 76억 3천만 원 과징금 의결 - SBS 뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE10N0ZJa25pVm5uREdfNEdnTFVOQVFfbVhrZzBkZklBVGhscGNlNnpQeVBFczU2UXhnX3c5OUVSU1piVVF2bGNaNG53aWN3NVBPTXRMTmZEVU1MUThkeWYxWVhaUFg4OFVNcXc?oc=5 |  |

## excluded:company_self_activity (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBhZ3dNVjNHQldlUXYzVlltVzgwTGtmb1ZMWlh1SHZwNDBhemYtTkF6c1dPVmxyNHE1dlVuSTg1ck1yUHB4MzVqdlRjQ3R5R296RXc?oc=5 |  |
| kifrs | idnfinancials.com | 아고스 프로조사스미토, 재무제표 발표 앞두고 BRMS 주식 550만 주 매입 - IDNFinancials | https://news.google.com/rss/articles/CBMimANBVV95cUxNQVc5WlBJeEJ0Zzd4b3RxVnZmWGxiMXlkbFNqb3JNX1QxQ0NFcXlRUVR4OWgyZlMxMEM3Z194M0lBYlhDRG95alJMdjdHV1R3N3BhTE5KN1BlSjBadFE0b3V6UWZxMGhRcGw3ZnBFUEFNUEhINl84MXU1cm93cGxVOG9OQkhiVFFCSUxXSlZ6aHBZSUN3dVVHTFZoTEJzRnhwNzBRVFo3ekJtTXAxSTVSYnoxVllERG1ncm00dkVuZkVzU1V0cEtHSlhmeEhnMWY3OXZiNVVNYS0tUXpnaUljc0JYd0RSTXR5dEhMOURoN0EwN2s3STlCa3BidTRNWVZSNUp0dDRVSTZ2THA5eWUxWTNDUW1DRFVUNjdHYmFqd3FwSGY0Z2d6WGNGSkxwbHd6YTRDYmE5UmJHUEcyS3Excy12OTVtSUhEQklPSjFqMlhTcFh3d214bnhNYjFzNVhjekU3Qno4TW9zeWhud1hfM1B6aU94WFEtbDNKc0NyaThYcWh1a252R1BxRWRyWVpqelFyb01QNW8?oc=5 |  |
| kifrs | hani.co.kr | 수출입은행, 회계처리 위반 기업에 여신 54조…“심사·관리 강화해야” - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8xX2I3MlBacWZXSVAtZUxfb3Z3amdGYm1OOVVEVGZtMG92V0VkdnEtTDJ1WVMwSVU3UWVCa0J6bVluTkh0U0luY05Bbm1Vb2tKT0VVbTc1S1R5Mk0wUmFWSUNmcF9CdGs?oc=5 |  |
| esg | ESG경제 | 아시아 각국, ESG 공시 의무화 '질주'...한국은 계속 '헛바퀴'만 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9iT1p3aDQ1bGItZFl4NDZ4Z3QxVGtEUS0wYnpjZ1BkTmF6MF9aakdtRVpBaGdIN3dUSms2bkxKUlBjU1VkT2NUaDRpNVdEaEExdDZjWkZEQlI0RjFQS0gwZ3IwRTVpTmNHNWJTMw?oc=5 |  |
| icfr | popcornnews.net | 해태제과, 회계부정 후 이사회 감독기능 강화...내부통제 실효성 시험대 | http://www.popcornnews.net/news/articleView.html?idxno=137275 |  |

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
| kifrs | core.asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFBCZkpUZzR6MDU1TFpsb3YzajlvTUt0eW01Mk1WX1FZamlEb0w3UEY3dFdOWjBJQVJkbE12cThnT3pXbWc2WVl3UU1lM2IySEQ1U192b1NnWlNBX2d6UVdJY0d3?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| esg | 임팩트온 | EU 은행 ESG 공시항목 37% 축소…EBA, XBRL 전산규격 확정 | https://www.impacton.net/news/articleView.html?idxno=30289 |  |
| esg | 임팩트온 | ESG 공시 규제 후퇴 vs. 월가는 기후데이터기업 인수 경쟁 | https://www.impacton.net/news/articleView.html?idxno=30224 |  |
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
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |

## excluded:financial (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |
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

## excluded:news_too_old (94건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | fortunekorea.co.kr | 글로벌 기업 깜깜이 실적 드러날까… 금융위 외감법 개선 검토 - 포춘코리아 | https://news.google.com/rss/articles/CBMickFVX3lxTE9GQnJfSm5OMk5pOWVUUC14aFBrQUJUZEJuMnVzLS01MU0tM3M5UzA5RzNPTnVfS21iUzI1QzZxNmU0a09iUG1RU0ZEY1hPdUtzNEFDME9pS1JqdmlFZkhULXUyWXh6ejZ5WU8xWTRmMFhYUdIBdkFVX3lxTE1Md0FkSEpRTmxlZENOUXBSRmtDMzBoZjl6dE1xTi1QcmtsN0d0OTR0NXhyVjdGUGpGSlc3dXpoRnNBQldzcWlzU2NzRlhsdlJieGhUS3o0ZUtFcnFTLWdCdmtDbmdaOVVIR0RRMU10LURKRXBIUlE?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | kbanker.co.kr | 회계부정조사단에 ‘10년↑ 전문가’ 포함…외감법 손질 - DFT 대한금융신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBtdGx4aHdKQzluYXROcmN0dUxiRHoxWUd5ck0wYTFPNEhUdXFiUjZYWFhhTjBCS09HNG1FYzNCRi1ySnZDcm1raFpidVh3N0tYaXRqRjZNMEo5bmw2SVV5S1FHWnJfRk9CYUk5Y9IBcEFVX3lxTE9ZN1h2NEU3Y3BCd0VES2QwMzhveXo2SDZPeGdpckdLVUxXcEwxdWJfTTk4WE9ydjBHblNNaTdVWnI0em9IVXloYy1SMlpnc3dUcHdCaC03d3UxQ3dhMkVlUE1KeHY1MXNJQXhqNVNlbTI?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | tfmedia.co.kr | [감사인세미나] 최운열 회계사회장 “외감법‧공인회계사법상 형벌규정 합리적 정비 필요” - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE5wQ0ltZmZmdENDTnZ1eF9kZmIxRUg4RVJrOFlhN2dQVVgtM0dBcExGRUdjVDRzY3R0SnAzRllzZ3FaaTdaMEh6Q0JvdnFpY2t5eTRNT2x3RVE1c1VmWHNqVmJZTQ?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | ESG경제 | 공인회계사회 새 회장에 최운열 전 의원 당선..."신외감법 유지해야" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5wczU3VWVubFMtUTdpOUI4Sm5XQUozYW9mVjRwQVY5TlEtRE5heC1nSnZrWV8waWZjNktsX2MxZk14TC1sRTdCdUxhbDdtZldlQkhsRElIVFBya25mLW5PLUFMd2xpR3c0X3VV?oc=5 |  |
| icfr | 일간NTN | 외감법인 주주 500명 이상이면 정기공시 의무발생…"IPO 예정기업 유의해야" - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmR1RBZURFNTBjZXVRakRjaWVfRHN6QnJucVdVLWVqaExkcjlReTZYazY3ZExxbGJLX1E3dkhvZ1Q5ei1vRVlZR2stUl92Q1BKV1QwUFpuMExaQnIxNmVrR3dTU1M?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년④)"유례 없는 감사인지정제 폐지해야" - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SYVZyanVjZE9LQzY5OTdsWEtDNWhDMmxFZmh4eGNyYnN5RWZkZmNhdjd4M3Rra1FrRVh5dVFwem9CUjM1WkpOUlBaSUZ2ZzBzalJnaFN2M0tFSlQzaTJFeQ?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | biz.chosun.com | 신외감법 효과 끝났나… 회계법인, 성장세 주춤 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUm1NS2l2eUNoQmVvMGxQTmIzdDRMRmhWcnBDRkhSMDl3MFdkVGZTNUI2cXRUVENWVkdtRGw0anhYWU1rZk5BRE9vYXhkMG8ycklqbmY1WlBRVk4wcVpPRUw2cVJWeXotSGVvZTltUHk0RFdMcHhVRzNhY3hXNF9zQ1VqZkprMVpF0gGcAUFVX3lxTFBvOXhIVjJnMVdEd2F2bVNnZnRZdkY5ZFJRZU5ESVN0cnlvMk9aYmd5cjlKbTZWTDV2TEF6dG1nTGk5a1daQi0xOE91bno4RUltazMtZUFocEk2d0NkM1h2XzBxYTZ6eHgyMTFQOFNBYW42VUpVZUF4Vlo3cUcyVTZHbWEwLUVLb0J6MDk5OW5uc0tjTVhhZzc0RmlRZg?oc=5 |  |
| icfr | m.ekn.kr | 코스닥협회 ``신외감법 시행으로 상장사 규제비용 15년간 124% 증가`` - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1IR3cyN2t5c0NGQWRqM0k5dnRWSWxyd1VJZDgxQUp0X1FmMjlTb0tiXy0tajI1MWZTNjFabk53Mnl6Z2lJeHdRazRCOXQ5T1ROMVc1RUdGNXNVclU?oc=5 |  |
| icfr | m.ekn.kr | 금융당국, 여전사 내부통제 모범규준 시행...동일부서 5년 초과근무 금지 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzUkZ2RFlzUjE5OUZ4b3ZxOURwN3ZORVo1UWFXTDBrckdQREVSMmVpbUFkU0VqQzlHNkVVVjBvLWRPUURzenpUNkVjZXBrTlpMblpmMDdmWXFjcnc?oc=5 |  |
| icfr | ceoscoredaily.com | 금감원, ‘여전업권 내부통제 모범규준’ 마련 - CEO스코어데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uT1g3UWpVTlBNRkRaZ0lXdFpDT1RuekF3QmIwVlE2NFJaTTJYRmZSaU5fRERFUWdoaldUc3BYZ05pU3h6RldDSFA3cUxpME1nMzRtMG1QWmdrNU1jcUgzRDM2WmdnZw?oc=5 |  |
| icfr | paxetv.com | [1분 영상] 최운열 신임 공인회계사회장 "회계투명성 높이려면 신외감법 유지해야...감사 비용은 투자" - 팍스경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9tWWdmYkxZY2dXTDVBV2xJeFUtLXU0S213RklleTJDZUlCd0ZSQTFyc0FPdjVhYXBGZjBQTXNaUHNsYXpGMzZlMWNMNGMyVlZSNWc2WEd6c0NtX0VibnVjVXphVmdpbldj?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년①)회계법인 배만 불린 감사 강화…품질 향상도 '낮다' - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBTdWt1T1hzUXZla043LUxoallBVWtGRHpDOHA0Nnh2c1pXRk16dVR4MUM2UHdBcUx0SXhvZFVDWFQ3QktDd2gtcUxzbWExTnFvQWxLam1KMkVXQnRiQ05XSg?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | investchosun.com | 두산에너빌리티, 회계 논란…신 외감법 이후 강화한 제재에 치열한 공방전 예고 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPd3hmMGM1TkJ4dFQwVkt5a3hmYmdZbmctQy1GYnpoR2JyUGN1MURsVWFyUWhtVENCaF9wUk1wZW5sYWhXSmp2OTBLeHFQN0pPRk5ESnZHTndNXzJzbmFjc1E4aTlzcXJOLUNKV3I0UVhhNXdFVS1wbUMtYmR3TElGVTRCMA?oc=5 |  |
| icfr | tfmedia.co.kr | 기업 재무담당자 70% 이상, 신외감법 ‘긍정적’…회계투명성 대폭 개선 - 조세금융신문 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5BeFRkTl9qUGNmOTNkX1R6UlcwYXZzYTFIc3NHdklsRGZ1N2NUd00yRjVmYUI5TDdNSVRwZlhxY0gxMHhqWjlnbk9NUWJqeG1UZU1uYThRSlM5R014YlJBRjB6N0lXUQ?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | biz.chosun.com | 대우조선해양 회계 조작으로 도입된 ‘신외감법’, 기업 부담에 소폭 후퇴 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNQmQ5eVo0TEJUNlRkN19FSjNSZUtkM3dRVnNJZ1Fyd2o4cFBJUlVFU0xMRTNhSFpSRjhkWlVvV1VUMjJXYjhuSnFzc1gwdW1WWlhUd1RfTHRuNExyc2tka29wOXN2RHBEMDNnNmxqUV9lZ0JJbGRzMkgwczJuLXJ2NGdWeEJoMU9E0gGcAUFVX3lxTE9sZVczell6ZTBVdnVVLVdkam9ZZFJXd2UzNm5oTG4xMlVhMWkwWjFUT21SZHJOVHZuV2ZrU2hhdkpBR0NwZGlzV0ZqNEl0bm5sZkJKXzA5Szc4X2h3WGppQi02YXhVNy05Um9EUzFCbUpsVGdFOXRlZ2JXdElVeGJZTnhkdnQ1cTdhMUdsWXZUMEJDaC13RTJoLVN5cQ?oc=5 |  |
| icfr | 머니투데이 | 신외감법 주도했던 회계전문가…'회계기본법' 제정까지 힘 싣는다 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9zZ2tGSkR1eU54TFk4RnYyTUlzcFhjbWNDdlpuTHkxNUppQnVQdHhQcjRtY1RsT2JkT0xudVpxdlVHSG9MSW9nWDhNa3FvRS1pUl9qTFlRcUtQMkRUY3hqSHphMTNRN0Yz0gFuQVVfeXFMTTlSZmpjcWZ5eDdQZTVwRjZPQzBmSXFScEN0bFlyanVlLUlTdGN2Mi10alpTZTd5ckVxei0zTGxWLUNPQTVISTNhb05PeUpXaFFwcXRHTzdUYm1xRG5zSDRLcUxsUXlVcy14LUhqQUE?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | 일간NTN | 우리회계법인 공인회계사 외감법 위반 감사업무제한 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1KdDNUR3BQVVl1dGtYZ2prUllIQVhuOHVKYXdKcW4xbmUxQk5LaExyeXFyMnp5ZTZSTG5TN0RENEp5NEJWeHRNSlVjRjEyMDNsc0x3Q0NRNEZrSDBuejVxNXczOHd3RHA4VWc?oc=5 |  |
| icfr | 매일경제 | “외부감사 대상인지도 모르는데”…감사인 선임부터 하라는 외감법 - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBfb3RIa3ZJZXVfMGlqNXVPSzh1bXhyMDdxRXY5Zm9tM2xselczNFhncmwwWGk3VE1McW5RZ1cwY0tydHBEdW5oRWpfUm9JMEVINFdhUg?oc=5 |  |
| icfr | zdnet.co.kr | "중견·중소기업도 '신외부감사법' 곧 적용...미리 준비해야" - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE94ODR2UVJKYTdMMjEwVWZRRW9vUlFQdkc0enB5RFBiVTgxRjBKUENtLTFUeXpneU5nZ1k5THlfa05PZWdZZTAyZFFVZFBmaEt6MFlJY2h3?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | 일간NTN | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - www.intn.co.kr | https://news.google.com/rss/articles/CBMiakFVX3lxTE5BbndhQ0dRSk5hQzluRU90Y29uci1RdFJ3SHlBTTZGY2U3c05mRlZOVW42bFlDYVBYMmdhSTgyQlJidjQzd2FZZHQ4eDFvMFlzLUdneHNkLWYtMjlsdHJTdXZjSkxNQUtuVnc?oc=5 |  |
| icfr | etoday.co.kr | 新외감법 피해 ‘유한책임회사’로…실적 공개 피하는 외국계 자본“[밸류업 결핍과 과잉](하)③ - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE56V0JDSGxxRXBKTlliQWl4VXl3bWtoWHVJcDZkY0xOVWk2d3R4X25iemVFTVNxbzdjSjBqYktYazlZWkwxbk9hOXRaXzBTS1hOTzFBSg?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | ibtomato.com | 신외감법 시대…발등에 불 떨어진 코스닥 - IB토마토 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1wTnhJTjNyNlBDcXBLejBQRm16NmxYYjlGa2htY1poZkVTTVVMcGFkNW15M2xwMUFYRDZlLUN1SEE2M3JpT1oxZ3MtYlFIai1nWHdKTTlkVDB5VFlUTVR6MnAxVFJWendn?oc=5 |  |
| icfr | tfmedia.co.kr | 新외감법 국무회의 통과…자산 또는 매출액 500억원 이상 법인, 외부감사 대상 - 조세금융신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE9vTG94WUNKczB1eWVZX0tpbmFISWhGU2NOS0VCOE9oMG9FMjBpTFVyWHFsNjdXbVAyNkJPUVBwcC1OdlR0NTBIaEl0WGtXWUhlZUtiNVFuWkd1RW9OQ3hhSzZB?oc=5 |  |
| icfr | 일간NTN | 여전업권 금융사고 예방을 위한 '여전업권 내부통제 모범규준' 시행 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5YVW5sNE1GN19VOTFHTVd6OGxFWE04LTA1d09Id25RTVd4VVhiU2pQdlAwRGlaUklEZjRzOU5oRDZJWmdDTGJ3ckU4U3Y5Z2t5OXVEUF8tdnY1WVFHQjFaeFYzYzVxa2RjbFE?oc=5 |  |
| icfr | fntimes.com | [프로필] 최운열 한국공인회계사회 회장…신외감법 주도한 전문가 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE4wWUZmaWJVbHVCRHNmQng0VFYxZG9kTGVuQmhqSmtlekt4MEZtODRIWTU0ZjhYczd1dzZIaWlCTzJBNURnWVJqRmp3ejA3end6ZUZMTzZtbkxYMmV6b2dCQWJKVGRjc2QxV2dUVUdSSWNydy1YdndvbzBZTWg?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | biz.chosun.com | 신외부감사법 도입 4년, 감사 품질 개선 효과 두고 ‘갑론을박’ - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxOdTJSWUFuWmlEZERmV0gzZVdoS0hIOEdKVUJlWHBJOE4tNElJTHBjU3V3NHl4YmtGYzFsZlFWa0VyNGlvRWJMUUdrSVFoRWJRSXJKc3Zxd3ppUWNzNk9kcks0Wm5GVkJrYkt3RnptTlJxTUt0dlN0M1FLLTFzZk1aUEVsV3QzRXJf0gGcAUFVX3lxTE5mdmlMV05UOER1YklmMVFBRUFZZjBWaF9zLVhkU0tnX1NNeEpIT1pFcUM0SVpBUkFTc3RhY3NfMVUyRnZKLTA5eHp5VnVCX29TR0d2cEctbF82UWtMOGJzMXo0bUlYSVNhTE1CcTFLZ1NHdTFTSXZVMHZ6TGlxSFFTRXZjQlJrdzZ1M3BVZHM4RXhzMGg2SXNWdmFaZg?oc=5 |  |
| icfr | ddaily.co.kr | 외감법 개정 `특수`, 상장기업 IT거버넌스 고도화 사업 본격화 - 디지털데일리 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBVNmlvMV85bmo4a2otSjFkTTFFcFIxZVR6WDF2Vm91c1JiRjJ3OFF0RDBmMG92ZDVWcXFxRlBHcTRrem40NTF3QmZzMWEwRy1xYnUyUi1nMllVMDRLZndyY3BlSUk?oc=5 |  |
| icfr | zdnet.co.kr | 더존비즈온, 내부회계관리제도 시스템 'DICS' 출시 - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ZWDVfQU95b2dIdy1LZE1MZWxXRUNPY3gzTUxjLUNMdDVjU0draEpfMWZJOEJzN1gtb05BVUZiNE1xODV3LW5TTmR0VnA1YnJYV1ZhbEZB?oc=5 |  |
| icfr | fntimes.com | 금융당국 '회계개혁 평가·개선 추진단' 구성…"외감법 개선안 연내 도출" - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTFBGUXkzSDVpRXVnTXJFYk9nNmtHc0g5d2N1THZHNlJfYUpzTk1iLWlOR2ZQUWRjOW9GMFNnMXpZdVZuLTREd3htelFCd0JhZ0FOZjdwNE5fS1RBaktzcEJWZS0waUIzS0U0MUp0ZTk0VGg5OGRQaGQxbktwcTE?oc=5 |  |
| icfr | fntimes.com | 신외감법 시행 4년차…감사인 선임제도 위반 기업 전년비 177%↑ - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE1scHBINWVyT3R0NmVEdzNYeVAyLW9qaEJic2JFSjlJc1ZHTHdydzlYOHJQRXh3X3Rqa1RqcVlVM0tYREQ5UjBhMUNVbFAzQ3JyTU1obGlkeVRSM0tzV0NSMkcySy1vZlM4TWwyQUplTWNOcWo2aWg0NC1DcVE?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | etnews.com | 씨에이에스, 新외감법 대응 위한 내부회계관리시스템 'ControlWare' 재출시 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE03bTFIY0VhM3FDbE83bncta3kwdFFMNHFpY1NVb0lZV3drZWpOWUViNzZSekhXM0VxVmJCZ0VPSmdHQTlocUdkY3IzNlNTQQ?oc=5 |  |
| icfr | fntimes.com | 금감원, 신외감법·K-IFRS 제·개정 내용 설명회 개최 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE51eTFBa0dYOXQ5UEt2bmF4SFUtZ0cwS0l0NjZRSUZTYlQ5d01iOGNPNHBQTTBvQTA5N2lycVJYc0s3NW16T091M2xmRjVydmRJekFheUU1TXhvZU94MXNaZVBvQUVMLWtMUXdvWkcwalR4NTZIbUpnV1JSZnA?oc=5 |  |
| icfr | news2day.co.kr | “新 외감법, 부담 가중” 경제인 앓는 소리 진짜였다… 감사 보수액, 4년새 2배 '훌쩍' - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Jd2hPSnlTb2h1bmhZbXFvSmI4d1JrZEQwTzV3eFZfX0V5c201YWF6Nlk3YmdhQjlnejN1UjB5TDQ4V1Nfc0R0aUdUTjludGN0QzF5MW9OTl96ZUhtWGc?oc=5 |  |
| icfr | ajunews.com | [경계불문 DX] 신외감법 시행에 ERP 회사 더존비즈온 바빠졌다 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DUVhuQ0cyWmN2YmtERDB3aWRYTmVGMGlfek8yQ3lQTVpkTFdMLTZKVkpqZDN6RnhpQUhLcTVUa19CdlROS25TdUdkcU9rc0IyNkRYMUhKM2tIQdIBWEFVX3lxTE5NT1pQdWFtT0RrNS1SbG1Fdmx1SmhJYlVMcjQzSmpMenpNbFhtUWVNZldfc3FyekduZTkyakl0YTlHZ0R4MkZxN002Zy02cWV4cTlGMGlfR1Y?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | fntimes.com | 삼성 등 금융그룹, 내부통제 구축·통합 공시 도입…감독 모범규준 5월 시행 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE5GRTk0ekFOakRta0tINzdwNTFSQU1yb3hzNkRKbHN4dkxVSkwwWXRHa3l6UVBSdFdBV2JxT2JGV2tlbzQ2RU1nUGRIdDVYVTNPWmh6eFJZT2ZaUEJVWGduZXdOOXhiOFFCaWJhQmktelFFcjJ0U3FJS2lpQ2Q?oc=5 |  |
| icfr | itdaily.kr | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 아이티데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE1CODVGNXBKQjRGMjhVY1pUU3JiQXIwU25Ga2NkeU9IR0xaVzlwYXVxdkZSeFVWWG00WXprcHlIRlM4R0ljbFhvWmFMeGRPTlRnbm1uT19JWHdrS1FzdFhTbTJjZEU2QQ?oc=5 |  |
| icfr | thevaluenews.co.kr | 은행권, 비예금상품 내부통제 높인다..."DLF 재발 방지" - 더밸류뉴스 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE1ud2JVUmZLcHFXdHRUcmZfNU5RS0pHZ20xV3BPUU1tOUNiSTBVOG13SEpHcklMMlVNelZuNkY1N19QSVpXTWpTX0xyS3M1TWdyUVFv?oc=5 |  |
| icfr | sejungilbo.com | [재계리포트] 新외감법 ‘그룹 연결회계관리’ 비상…더존비즈온 ‘EFIS 10’ 주목 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTFAwMkJtZHdlX3lNSUxIMWRMMkNZb0tRbjJkNHF2Sm0zbm5GeFdjeGE0R2RRRFhyX3FSbXJRTXpPVmpBSHlKR0R2NzVPTGtES1pTZjhhd1hkbjNzQ0dXZGFxWVZ4dnZaelltNnZ1Zg?oc=5 |  |
| icfr | m.bikorea.net | 더존비즈온, ‘딕스’ 출시 - BI KOREA | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1oSE9NUDlTaGlDenVfdHhWYVZMcVFJSUxGUU95ZHAtNVh6Q1hQSlZSNmVFM3RZWUdDb2ZfZmFnNmpyWm96RUVGOFBWM0RBdXlISlBuSkt2QU9weEYybFZMUkF0TUE?oc=5 |  |
| icfr | newsis.com | 외부감사인 선임 45일내로 단축…'新외감법'시행 본격화 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9oc0dCbXI4OXR0SU9FSVdXM0ZQOXgxSHZNRGplVFhZX1pUZms0ZFpWWWZnX2RFbEVnWGlIWnBNc0JNUU9KOUxBS1EtczhhTGlOZnFQcEIyUTJkMWM5eTRtNNIBeEFVX3lxTFA3ZXU1SVRsUU4tMDd6ZzcxZnRYU0tIaEJWeUFZclVKVlpUT19HM0Q2QTBxbnRicjJQRHo3ajlxYWx3V3FLMnlrTWRUZS15T0dfTmtqc3NRazdnSGVrMUNPUm9LSWVBQ004TGNpRTZpY05abGpuWExWeA?oc=5 |  |
| icfr | etoday.co.kr | 28개사 ‘내부회계관리’ 비적정…“내년엔 더 문제” - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBMOW1idWYtTDJmTzJCazdzXzF6dVRNbzRsYklQaHFSRkc1Zm1MVFRiX0hwZ1ltNHVJTFM4Y0JZYTh1OHc4Zmp5MnkwR2tSYUdYMmo2SA?oc=5 |  |
| icfr | 매일경제 | ‘新외감법’으로 상장사 회계법인 교체 쓰나미-삼성전자 감사인 누가?…빅4 판도(삼일·삼정·한영·안진) ‘흔들’ - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFA5cno2VzNKMGd0UlJ4UjI1Q3hSamxObEItQWNqYThZcElJYm4tR25UZGVOYkhVNUhYcXBMNlpGV1hLQ0hOQUZnck1jdFBHWXlLcXk4Vw?oc=5 |  |
| icfr | biz.sbs.co.kr | 씨에이에스, 외감법 개정따라 내부회계관리운영 소프트웨어 재출시 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE9CdDhZWEJKNm1ZdWRTcDM0RndZMkY5dGo0cjZCU3RucHBFM1BVeUk3cVFzMEF6WGdMWC0yNEsycTNJRWtTYlltcXNIa0pjaTZDaHhn0gFYQVVfeXFMT3lNY1Y5VUxSOHVnU0ZiWEZyb1M1V1ZMVElxZnIyU0U4TlEtTHE5aHVwekdxU2p5amVVcDYtaWpzcHBqUl9JT3RyM0RELVpKTmJ1RzJYSGszUg?oc=5 |  |
| icfr | indifocus.kr | 채이배 국회의원 주최 신외감법 중간평가·제도개선 간담회 열려 - 인디포커스 | https://news.google.com/rss/articles/CBMiQ0FVX3lxTE5NNzJ5OUh1RGlfb3NTX3RxcDZlalhqb050ZlRPZ2F2eHYzVWEtSXRRYklDRW85M0k0NmxuSHZnUndUdkE?oc=5 |  |
| icfr | sejungilbo.com | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE8wbVA1bV91THUxeGRfdFo3SzItRkQ5M2RmNDNFeG1QUzZQS0ZQR1RFemphaWRHcVlnbWZHN0FlVy0waWFuMlIta2EwQWJOdy1qWWZIV0drcmJWTEFSLXVpZDZrQVRsQW1YeDBJUg?oc=5 |  |
| icfr | ajunews.com | [기업쇄신]최종만 부회장 “신외감법으로 회계부정 어려울 것 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE04aDRvZjFQWkc5Tl94eFpxYmRaWFczbG5VdHBGREhIN0JaSy1MRnBqZ3hTdlpodmItZHhrR2lsRmpWRTdWdTZkQ0FYUFZkcndwNDF3QnRPbUY3d9IBWEFVX3lxTE8zdlk3LWJBOFZWZzVRbmtsWjhUNU1Sci0wazNJRVZtNDA4VXEySXBzWXhPcWVibmhGb1FDc2hBQjFpSm5PTU5BR2o2VlAzU1F4c1Y5YWtZYUQ?oc=5 |  |
| icfr | 이데일리 | [新외감법, 감사비 논란]①회계 개혁 눈앞인데…보수 놓고 갈등 - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxObWFhT29aS3RIZkJKODZUWEN4WjlGUmIzU3ozU1l1WmZUbXZ5OGxaWjl0eWY0aDg3UEZZRzNfSWtabEkxemMzNUM0dEtpazdjS2ZrM2FGanFhNFowY1JySVFtMXBWbzU4djB4MzNOa285S3prR3pqemZLSmhvcnN1OA?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]뒤바뀐 갑을 관계…회계법인이 '기업 결산능력' 따져 고른다 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxNVEd6emg0SDFlcWI4LWhaZFhwS2tBdVB1TjFQeTkwb3JxRGEtQ3kydmFGSlNIQV9DbXNHdFdCQjVwLW83cnlwZVpOS3Q0ZVFST2U4NnUydGxZUE5OLWRCLWF2RzBnNXM4VjluOFpvd1l3SllFWnpndGhHMGtWc3NWMg?oc=5 |  |
| icfr | 파이낸셜뉴스 | [인터뷰] 채이배 의원 "외감법 개정의 주역이 회계개혁 완수해야" - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9wdUF6OXdLMktRWk9RTlBNaEIybnUzb1NaYmgzTkZ6Q3VLcndXNmRCQlhzeFhyTWFBZnU5WXVIVl9aQWplZFdnT3ZReGkzaDJDMTNVUkJhTXhndw?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]전용석 딜로이트안진 본부장 “회계투명성, 기업과 함께 높여야” - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxPZFh3QnZzRU13RFpUbzRacTJkbi01RVJuU1BuWDJIajBWcnd3UmttSGtfZnZGcFI0QmxEMGtfZmdNc3ItVms4Z3ZvaDlqZ0pFb3NUSTNVSkxVVVIxNE9HdjRlaGx2YkxwOE5HSEdoNFVCV2ZEMkxiWVlvZVRlUGM4QQ?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]윤훈수 삼일PwC 대표 “사람이 경쟁력…최고 지원체계 갖춰” - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxNc2FJOG9IU1IwTnl6cXlQLXJqdm9tVl9sVTVmXzNlNFZLd3dVbUttN1VJSDdDWThEc2FUei1QWnhzSG9hRjY4eG1TRnZiNnBvUVNIM0t1aXk2YlFIUlFiS1UyUzRpaTEtVjV0ZWZMN3QtbVZDSjFUVGNTZGpvYWhGSg?oc=5 |  |
| icfr | 이데일리 | “작년 사업보고서, 新회계기준·외감법 내용 꼼꼼히 기재해야” - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxOdkxseHYwRzUyel9SRDUwcEQ4aW5lNU9lMVBTbVdOTnQya240SUZJVHJKbk1wdHlLWThCTTF5TWJCbm5rSXI5OGFJclFickw4NTh5RzRQTHhKUU1DaGpXa191aDhGSHg2NDZHUDZNYkI5LWRFYm5kREQ1Slc5UjNIMw?oc=5 |  |
| icfr | view.asiae.co.kr | 금감원, PB업무 내부통제 모범규준 시행 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFByWmtmZUtmVmM4XzBSZGp1d0ZlRHhSSmk1U3JZSVVvQ0pPaU9Ca2FFeUI3aUxEdXpjREozMTJNVUVFVFdZUTRvVjBBNzExbUJYWmVYZnM1Z05NVHl4ZmZfcnpB?oc=5 |  |
| icfr | 이데일리 | [新외감법 시대]박용근 EY한영 본부장 "글로벌 협업으로 감사 품질 제고" - www.edaily.co.kr | https://news.google.com/rss/articles/CBMigAFBVV95cUxPX2ZFeGk2NVQxN24tZHRoaThvZlRPdmpiYkFvUklGZXFLUmEtU1VfM0t4QXlkTm5CVHhoY19IQkZHdTZtVU1lSl9QR1dfY09ycmRzM2Z0TWwwdS1WUnVfdkh4NFV6UzV4dUpONjRwRFk5UVRfYmQzQVo5OW41NjdGbg?oc=5 |  |
| icfr | biz.chosun.com | '新외감법' 발효되니 '유한책임회사'로 전환한 구찌…'깜깜이' 영업 여전 - Chosunbiz | https://news.google.com/rss/articles/CBMie0FVX3lxTE1tdURoaS1ORzMycmhsNW84VEFZT0d1LWFsdWtVUHhidlFPUUx3RDFLRGFzOVZrLUNnSEtibVVFLTNhMEJJdFdJM2F0SkhqUjFZbUE3TUxjY2ZqTWJ6cHNUM1d1MEZFbGJXLWpqTjAzcjhEemJBUnV0ckNnVdIBjwFBVV95cUxPcWJmNE1aVHNIMWhYc2JEbmtWR2xqN3JMZGVpN0V6SlNYdVgtRlZ5Um0wbWhyU1hMM3EzWTk2Nnc5bXYwN0E1VmVTNVhLNWlTV2VrNm1CVDF2OE1keXZwT2xWb0RBWktrTy1RQVliVHFodkN0VVd3aUlCOVZhM3hKRE1vaUJiUWJueUxOVm55aw?oc=5 |  |
| icfr | biz.heraldcorp.com | “신외감법 시대인데…” 여전히 60위 밖인 한국 회계 투명성 순위 - 헤럴드경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE9FSG1PaDBKX0YyUGxNMU5ZSzhEbWg3SDB1V2JzUzV0dEJ5Rkc4U0xMaThpMkVRako4bm44NGY3UVRMUjZBNWdIRDlYSWNMREhqeElEeA?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |
| esg | ESG경제 | KSSB 지속가능성 공시기준 초안...'유감'과 '기대' - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5IbzRUeVpVLUVnVUk4MGRxWHBfRmN2ZW0yU3VDYkxLbUdteXFPWGdVb05ueXNwTzBSS0ExSUU2V1BTd0xLYUo4eDlLVjc3LTFJS1QtQVVJNVdtZzNvcHF4UjdsVjFFUHdKZnJJ?oc=5 |  |

## excluded:no_regulatory_signal (76건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE43SzV1ZWNkVHBRQzZUUkJ4OW5zQWoyekgtQ2pvZ0FJTXQ4NHVLNjYwa0lPa1RqVHpMemJzRUNxLUJyeXpuT29LWGVJbFNLMWZtelJseHBfNWNoVTBuVVJtb2xoWlpEQ1oyY3c?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, 회계기준위원회 비상임위원 1인 선임 - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5acXJMcUxsamFWTzZRRU1MVU5nazdpUTVUUDhMLU1NVFdjYlItenhWQXJPcENrZW54a3RXZG9XeFljdnZNVXVjbUxmemdtUWNEbGpKRnJ4RGxHRDhLY1Q5RTlQamE?oc=5 |  |
| kifrs | 한국세정신문 | 빗썸, VIP '블랙카드' 운영비 편법 회계처리로 탈세 의혹 일어 - 한국세정신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFBPaXJpdTZZanVIUnNmbnlPX1ctNzM2THJTWl95TFdIVVJrcVpfUzVGOVVSOEdlM3lCMDhiS0N2Q0VvUjFsc2MtZmxrWk1KVUhIZWQxaUJrcnpaM3IxWTJteVBn?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑧] 현금흐름표도 함께 바뀐다 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5OWVd5Z0VCYWFKcFRxZ2MydDVicTBORGU5YzhnTFpXQ1NLRFJ0ZHNLVzRKd3N2SEZuQlJqTFZWb1ZidWN2MGJfQmM5ZzdWZmVvVXBTcGNlNFRhT2ZTT2pqYnZ6bEc3aXJv?oc=5 |  |
| kifrs | CPA뉴스 | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5nWU1iSkc0YXQ1V1ZsVWF6RVVlMmVRUkVHMEpWZVNlemtPVHpiR244S2JKc0c4UHE0TXRQWmd4OGhwTkdWczJ2elRCbkRGVEhnMkxmaV9EdUx5bnJacFA4NExtOXlQYzBP?oc=5 |  |
| kifrs | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QQkdfaGlxSmJXLWJ6ZWxsbmxpZVhYZHJHRWl4V0VIalhpZEJEYXJIUy1CSFQ1MzF3TEM5Y1JWdkxvVmkzZDNQSUpyVTNFSExWS2t6Q01Qem9VTkM1TzVheWpUS3Y?oc=5 |  |
| kifrs | 일간NTN | 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1OV0h5TUE1U1VyU0R1eG5FWTkzbmJyM1RrQkpwVkxVQUhfNzFJcmcxTGpGT3U3SUlSWjNsZU1YVVBxQVFyc0Y4MTZRSXhfVDJyaEtoMndWWlhXOWVQMmJpWnRMalQxWjNudWc?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원-한국환경산업기술원, 지속가능성 공시기준 이행지원 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1Dbm80OFRBdTd1QjFhRDA5dTFRMjNzR3QwaXpkQnBzdllCaVk2SXNVekZ3WVNIaXJhTXhScTF5QTYzS2dTWHlDcW9KcU9ITjJkWmtrTnhSNmN2UWJfS1ExOWhlLUJtZnhUeVE?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, ‘지속가능성 공시, 새로운 기준의 시대’ 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBPT3dBRVdDZDVhdEFkU1ZZWmx0Z2daaHZkbGtpY3ppa1FWUVpmOGdldEdwcHRHUDM4RmhPOGVuZXNGeE1RVXpid1dnblpnYm1LV216TUlFMkhjazhmeEtwVG5kY0JRcHlwc3c?oc=5 |  |
| kifrs | 일간NTN | 증선위, 영풍·고려아연 회계기준 위반 적발…감사인지정·과징금 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBVYjhpbjhCWGZMXy11SUxRNkVneDZyek1hclFyTzB1WU1KRkdQRFN6NElBczZpWHN4U3BhRXhwMlYzSUZrSmFiZGhubjRGMll0ZGx3TUlwak9qakpONUZpRjk1OG1fRFk0SlE?oc=5 |  |
| kifrs | 일간NTN | 금융위, 만호제강·의왕백운PF 회계기준 위반 제재…과징금 9억9640만원 부과 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBlQnVuWTBYYm5OdDc0Nm40UGVzZmU2TEpUNE1iRkJiZzNDMjRjNlZXbjR2UWpmQXkwRURFemN3U2pvRWo5ZXpIZnNxNE1sdHQxSlNxRG1aM0RmUHR6VjN0SlBrRVg3eTN3bGc?oc=5 |  |
| kifrs | 조세일보 | [진단] 제각각 회계기준, '회계기본법'으로 통일되나 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iZExnWDViSmtJa1VsVmpUS3MtTHpYcDNDQU1iWkFWMlBkYi1QMjljcW9za0MwUjE5Vmg4V2dkdDg5blhYZjFrNkhDRmRkbnZ2bjVla0pOR2xMenlvUEc4?oc=5 |  |
| kifrs | 일간NTN | “공동기업 재무제표 오류 반드시 검토해야”…지분법 평가 오류 사례 공개 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE56cTAyejRleHo1aGMyUWRaTkxPa0NnTFJoODJJTkk1M2hjRkNpV1dWNlMya2tzLVZjVGpzaEJGV1hEdk9JQ19FX2NCQ0N4UlVQOFExSEt5YW9OVTUwNmQzQUNaYk5fRjdpTlE?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑥] 두 개의 영업이익 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5FRUxaZW9oYmNpYTBhR3h5d0VOQ0NtQmxKU0NHTTFsc3ltYkhTQURmNmV6TGMwNnBtOE85QjFvT1l5Sk9zRHpUX1lwZUYycTVsY1NYRW9seGpuN0QxaDZqdVZLeGczMk1i?oc=5 |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 매일경제 | ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE4yMzAySUdLM2MzcEFZbEFDMjYzbktLaE1uTUtfS2tGQzRoVWEwcm51OXJ1elZMWWZrd1VaTFNYd2hYb3NsYzdFRVl6SjdMbFZkTFE?oc=5 |  |
| kifrs | 파이낸셜뉴스 | 게임사 영업손익 표시 바뀐다…삼일PwC, 지스타서 회계·IR 대응 전략 제시 - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBKX1hGaE5xeEgyRGVpbzBrMHBNSzF6UnBIRXVwUy1SdFMxUjJ2dWhTbmh2R2lsaUpnM0FId2Z4UjJuRWNZN0ZRTHpxMTE1M0UwYUdPRWtzOVJoUQ?oc=5 |  |
| kifrs | 한국경제 | ‘몸값 6000억원?’…중앙일보 진짜 가격표는 [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1MbUtmTVBIS3ptTXgzUzNIRHZ2eXc3NnUzSXVlSEhxU0ZOcVI1VTZ1MENuVUFCNTFmMlJaMXE0SHlaSGU1WVVhZnk4S3dFWWwtRWx1aGY3cml2VDlyQVowVXdORnhJWlZwTERtRA?oc=5 |  |
| kifrs | 서울경제 | 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE41YkVzeThWTUVTaGpkSnBmRDVfWVprSTY2UncyajZDOUpiZFVYTDN5eENqM3ZQcENzZm80RjZwTVNxalhNaWQ3bDRkYTV3S1JnNFHSAVNBVV95cUxOSy1rVnBqeks0alRJRUZOaGVubDNZSmpBYU9TaTY0ME5RT1NnLUtUZjdfZGp5QkVvSTNQMmRvS2pUTlpJR2RXYlcxTklYNW5wNlVxRQ?oc=5 |  |
| kifrs | sentv.co.kr | 금융위, 해태제과식품 회계처리기준 위반에 과징금 약 13억원 부과 - 서울경제TV | https://news.google.com/rss/articles/CBMiZEFVX3lxTFAtX2dCMTRIT3lLOU1qUWtVd2l3RVBWbjBHaURXMHowbnhsSmdGSS1qd24tOVZkV09BSkVMTzdFTm1pdTVweFl6ZzBNVG9KdkVIQ2xuWW85TWRPanlGbFlSSlVldUg?oc=5 |  |
| kifrs | kr.investing.com | Endava, 회계 처리 조사로 2026회계연도 실적 재작성 - Investing.com 한국어 | https://news.google.com/rss/articles/CBMicEFVX3lxTE8waEw3TUxGZDh6a3FWOHFidUNtcEdhMFh3RHpBRGFfY0JsWGh2ZzBGZDdnMEczenRtT0lPUVZoMTVUTEl1OVpxV3NrVWJtSlFlc0dVZ09ja3hOQ2ZpcFItOG5LNFNWd1k4a2hmM1Z4N2I?oc=5 |  |
| kifrs | m.ekn.kr | [기후경영 포럼] 윤나영 한국회계기준원 팀장 “온실가스 배출량 측정, 조직경계·산정기준부터 따져야” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBwSENJcGZ1alVPdzFhZEREMjZSamRuYTFyLUJYS2xhX25zd1RIXzd2SjZzQlVyZVBqQXp2VnQyUkNTSXNEamFuZU9UaGQzZ1lDQVJXbXpRWXp5TEE?oc=5 |  |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 해태제과식품에 9억 과징금·감사인지정 3년 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBobFhCYWR4N0lQcGVqalJueHV6TzVVUVdxZmVWVFQtaGlOcGM4akhva1hsYkdkMXhURkRNcnNvb0Vka2RMOHFpZE5YQTRtRElLYzBJcktKWHVLV1JXSzZSZg?oc=5 |  |
| kifrs | hellot.net | [이슈 포커스] 기업 반발에 탄소회계 기준 후퇴 논란…과학계·투자자는 “그린워싱 우려” - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFB4bmx2T2E5RnZBMmpMTGh2aVBrcHhsQWNoRHJlMy1SdjYyLUIxUU1JZ2cwSUtFYlFweUdSaHMyOE5yanVkSGVuOXhOeU1QVDVocXQ2bkhjcFR3cjVIRWQ4?oc=5 |  |
| kifrs | newscj.com | 안양시의회 예결특위, 결산 심사서 세입 편성·회계처리 문제 지적 - 천지일보 | https://news.google.com/rss/articles/CBMiakFVX3lxTE56bHVRcjE2MnFTZVhzdmFiaU1pU3IxZG9ScHc0LVZyZzg3YlRuOUNaMUd1aDJCcDlUSXM0UHlMNlhHT1NxUHpJMzE3ZEJNLUNCSWRBbTJCZjBiUDdGVHRRS2Q1bThUbEdaY2c?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 눈에 띄는 LG이노텍의 수익성 악화...사업 포트폴리오 고도화에 미래 달렸다 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1ORVdUdkZBZVRyajNHa3pVeTJjR1JGTDVuNmlibWtycmN3TnVpVUtXRGhaQlBpRWRkMmZwcE1objBEV3hUV3A5blVoNVBpbmNWNmMyN1EyRzZWN0lldkNYZ25QbGdFT1dFbUM0cQ?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1118호 영향 관련 사전 주석공시 모범사례 마련 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE13d18yem9ReWp0R1hMQXhJaVctcGpyTzgxRm9XSXBNOXZxcnNZaDhfZVgzajBhR0gwNm9EQnBmZElrWWhsQ01mbE05dzc5NmVWbksxVVE5STk?oc=5 |  |
| kifrs | tradingkey.com | LOVIU\|Live Oak Acquisition VI Units\|가격:10.000\| - TradingKey | https://news.google.com/rss/articles/CBMibkFVX3lxTE5GM3VpN0U5M3A0dlRLWFpDcExLMEktdFFtbGNrYmoyTmZJNm5WTlVzVkMzdi1SeE1tMG9tenYzSXpQdlNnS01xbDlrMHdodEJsZ0xDUGFJQkpDS2t1bU8tS3NCRnQxeTdESW9PNUV3?oc=5 |  |
| kifrs | etnews.com | [기고] 회계감리 대응, 숫자만 고쳐선 끝나지 않는다...거래실질·자료제출·내부통제까지 본다 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE9HZ09Dc3F4WjdxRnByRmlYU3FjN1dGVzEyVXF5N08waVNablpCWWF6SFhXbHJjWGRkUGVGalhOY3VxQzllNTFDdjZUb0ZGdw?oc=5 |  |
| kifrs | m-i.kr | 안산시, 복식부기 회계처리 정확성 높인다…11월까지 컨설팅 추진 - 매일일보 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5kMXpHWEhyOUpvVzVwbmM0RFQ1ZGgtNjFTY1VETHU3RDlQd1d5MmExWDMzS0NYUGlEZlYtQzhEQW16Y015UnQ5X2IwbjBRWU1rLWg4R0xnUUZZTk9WR1N4RUs4OGE?oc=5 |  |
| kifrs | joongang.co.kr | 기준 바꾸니 27조 흑자가 적자로…새 회계기준에 지주사 ‘비상’ - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE4ybk5IZk1jY3dMRTE3a21sWnlBZ0RYcVpPYnduMW56UzJhek1fellTTEdkMmJSelc1LVBIME55clJXYko5Z0lnbkpEakVFbmVkdmdzbHB3?oc=5 |  |
| kifrs | lawtimes.co.kr | 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE05MDRqekxIcGRMRFZhMmdwVnM0OWZ3R2lMRGhka0NDWU1EblRBMFplYXc2bldHUDJvMnJtaG0tSnFaX2U3ckt1WXY1U2FxNk1zVm1yb0lUb09Mb2o5elV4S3ZNWVRfSUJPdmxvRHhR0gFyQVVfeXFMUFhvWmtXbVVXc2lzOTFnYnp6bGFkWnc3T2kzcC03bFVzam5Sb25NNWZsSmt6Q29WVmUyZ0EtYVY4SC1IVlB5QmtXTVIxR005WDVzdDYwcDhramd6dXRGOGh5eHdZRnVrTTBoYV9FNzBFbnVn?oc=5 |  |
| kifrs | yna.co.kr | 2025년 재무제표 '비적정' 상장사 53개…전년대비 소폭 감소 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMOWoySmx2N1Voc05Ba04zNC1ZYzBBZ1A5aUdXNzEzVms5N2hyTHA1ald3Zjc5dnRNRHh3LU9XLWtmTWJfR2Q5eV9aSzBnQVBCX3VHTzNsUnNKT2PSAWBBVV95cUxPTmZ3M2J3VVctVkFTTmRhU01tZkRBTkROS3Rmb195V1R6OTJrYjRUNG1uUXh3Z29sTkJXRDhpaS1ZTUQ1ZkdrRHZJdnV5SDhCRktQQ1JYaWtEWlBTTm1od1I?oc=5 |  |
| kifrs | news.bizwatch.co.kr | 회계감리 중징계 영풍…내부통제 시스템 허점 논란 - 비즈워치 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5aNFQ0V2JXaVMtOVBoRVNNV2RZNE1GYS1mcE1Gd0J2NDA2YnhGaUV3cFJmZldxRDh3eUdNdkxvRktUNEFkQ1NkMVFCaVpBZG9TenNBYVR0Y09KUkZnS0poeUxQNjhEaXhKVVVSVg?oc=5 |  |
| kifrs | hapt.co.kr | 승강기 교체부터 고철 매각까지 세무･회계처리 - 한국아파트신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9mSmFsQnZBTmRvNzZha0dudUFIN2I4Q3lwWTJleVlqTERKaTdIUklzT1dobzA5dGViTWxmNlFGOW01dnJycmpYZUhudHNMdV9TbGhoUy1wSnF1MG0yTjZvTUFDS2U0bGY4?oc=5 |  |
| kifrs | yna.co.kr | 감사 전 재무제표 제출 위반 76건…전년보다 24건↑ - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lODhfd3R3TUpXOFZneW5tMjJ0OEVEeXBMWExHS1F1MzNOdExVUlNsdTFwYVpFZTRxLXNTZzZoZzRmQnhhYW5ZZlhtUjJJM1M4YXA0ZWNCbU5ubzjSAWBBVV95cUxNUWMwYlBCMlpvS2R1a2dOaVdCYkRqcE04YXNwb0JCSC0xb3NSc05OM194Z2dCcVhiSFU1elMzQklVZHNCc2dtRG1wMk5kSTJmMW1rVWZWdDFQcjZrZFVRTno?oc=5 |  |
| kifrs | news.bizwatch.co.kr | [SFS 2.0]재무제표 밖 거래망까지 읽는다…AI가 넓힌 신용평가 - 비즈워치 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBBOFR0QWktVXlHMWpfSjFlTVEzTk1kTm9QQzhjN2VTYWpOVFcwVnlMUnNxNXZ5MzRqOWJBNnY0aWlPY2JWZ2NGNWdkV3hlMXpRdmxjQmtucVc3aHVDRVgxMHlVNGJhRGtQVldr?oc=5 |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5tQWI5RHBpTVRkQWY4TEhWVXdJek5VRG50QTBTLW5ZTU4yNDVoUW9wRWtXZldMdXBjMldnSkxzVDV2blFoU1RpMndUX0pWdTNDVDlPYXB5T05RY2s?oc=5 |  |
| kifrs | news.einfomax.co.kr | 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBzREN4d0RmcDJBMXFhZ3BfZVVTRXJOalhqNmNYYVRoUFNzQmJoNHdqb3pmaXVqX3RGTlpMbGVYUGh1dGNHbEpBbXBmQkE3cEI0dVFMS05DaHdjUkswWTk3Vy1qam5vYXhpckdud2xoX1k?oc=5 |  |
| kifrs | news.kbs.co.kr | 금양, 회계처리 위반…“행정소송 맞대응” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE8yTHV4QVF4ODRCdkZraVFaV0ljWkV1Wk5QOFVQRUF3SEZRaXhrNll0bU9ONkxuZTBzaHhNOUtLTDRXVFR5bFZMWWlTM21YSHRrOVJaTHlabWphRzg?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 영풍에 과징금 204억…고려아연은 84억 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sVlBmQzJPbXZuSTFOai1kaDhGb1hLVkpCdktFWnZaU1YweGRJWllmVk9zbUdZQTdpUTVRaFpHM1RlQXllWkhpdVpJUFlqLVV1SEJESnZkVUcyZEnSAWBBVV95cUxQZTlEXzktdDljVUR2UENmbHJnUzFKNE04U3BxTzNETFZBTlA3alY4VGJtREYwdmVvSldHM1JlM1kyNWlsVXJFbUxCaHhaQlBlU3VHTVY2UUh0Uk1aS1U4MzM?oc=5 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 머니투데이 | 상장협, ESG 공시 대비해 실무자 쟁점 미리 챙긴다 | https://www.mt.co.kr/stock/2026/10/19/2026101913585170575 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | asiatime.co.kr | [윤영민 칼럼] ESG 공시 시대, 보여주기식 경영의 종말 | https://www.asiatime.co.kr/article/20261023500342 |  |
| esg | thepowernews.co.kr | ESG 공시 291곳→1년 뒤 3171곳…대기업 넘어 협력사까지 ‘데이터 전쟁... | https://www.thepowernews.co.kr/view.php?ud=202610221509381568de3f0aa1be_7 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | newscj.com | 충남북부상의, 지역기업 ESG 공시·규제 대응 지원 | https://www.newscj.com/news/articleView.html?idxno=3441094 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | straightnews.co.kr | ESG 공시 확대에 협력사도 대응…동아쏘시오그룹, 공급망 교육 | https://www.straightnews.co.kr/news/articleView.html?idxno=312824 |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| esg | hansbiz.co.kr | [ESG 칼럼]ESG공시, 기후 넘어 자연과 사람으로 | http://www.hansbiz.co.kr/news/articleView.html?idxno=860684 |  |
| tax | 서울경제 | 경기도, 지방세제 개편 입법 논의 본격화 | https://www.sedaily.com/article/20107006?ref=naver |  |
| tax | lawissue.co.kr | 경기도, 지방세제 개편안 국회 논의… 소비세율 40.3%·법인세 지방 이양... | https://www.lawissue.co.kr/view.php?ud=202610281438496967d94aa4ada6_12 |  |
| tax | asiatime.co.kr | 경기도, 지방소비세율 인상 등 지방세제 개편 추진… 30일 국회 토론회 | https://www.asiatime.co.kr/article/20261028500244 |  |
| tax | gukjenews.com | 경기도 '추미애표 지방세제개편안' 30일 국회서 토론한다 | https://www.gukjenews.com/news/articleView.html?idxno=3734897 |  |
| tax | sidae.com | 경기도 지방세제 개편안 국회 공론화…재정난 돌파구 연다 | https://www.sidae.com/article/2026102807154836058 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| tax | dailypharm.com | 카드 세액공제 연 500만원 축소…매약 매출 높은 약국 부담 - 데일리팜 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1ZakNScUpnQ09qa0VVX2RlSVlwRFltUmwxczAxOGdNb3h1Nlh1Yl9OalRvakt2dTJQdERPMU1wOWFaYWtaR0xBby00MEdVODdQNVdEU1Bn?oc=5 |  |
| icfr | datatooza.com | 유니퍼스트, 10-K서 재무보고 내부통제 중대한 취약점 미해소 공개 - 데이터투자 | https://news.google.com/rss/articles/CBMickFVX3lxTE4zc00yaE5xclJ5OFA1OTBhSkJCNWVsU2tRb19DSmlWQnpxU1FPX0xMblVVVWVrNURlVUk0TUdMQ3ExM0ZPRlFWQWxzbXVDdExXeFhkTkVzbzFKVW90TDBFRGlHbTlTLVFYMXkwTU5jenBwdw?oc=5 |  |
| icfr | datatooza.com | OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE85anpGNUU3UzhJX2JBTDA1dFRqRHhkQ2dhdXZGZ0ZVcHRkVU9Gc29Ca1hXWnNSMUYwOEJEWlR3NmFlblRvSmtIVHhwemFzVFpockFoWFFla0VfUmVVekFaRXAwZEUxSGc4RGt2Y1M4WmFHRmM?oc=5 |  |
| icfr | newsroad.co.kr | "내부통제 효과적" 자평한 빗썸 경영진…감사·회계법인은 "취약점 발견" - 뉴스로드 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5Cdzl4cjBaTmg1YmMwNTFrUm16YmVUcW9lTlBfcU1YWFBXR3kzeGkzWEtibERzajFnMG92Wk9oYWh6Y3FHRTdDNEJJVkNVZWxXLVdLYWpTUm5CWThiTGV0cURIcldhZDRMYU04?oc=5 |  |
| icfr | datatooza.com | 리소시스 커넥션, 내부통제 중대한 취약점 미해소… 1분기 구조조정 비용 41만 7000달러 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE4xYy1JWnFhRGhwbDJwMzRiVkgxUjdfMlYyWl9yMzVQd1NMS3kwanZRR2p2LU9oU0Fob19kbzN0M2NSaE9iSUhBX2hWb1JGTFUyUF81LXp6S0lHa0hLaThtaWhnSTl5MlZVYXJQR255RUVYa1k?oc=5 |  |
| icfr | datatooza.com | 니오볼타, 10-K서 내부통제 중대한 취약점 2건 기재…TPO 판매 플랫폼 2027 회계연도 1분기 가동 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTFA1OHJvcDk3Nng1TjJOUHByRUtMdVRfZnJfVlNkaUFOUkw3ZkUyRXVaOEhuWm5IRVUtbnM4SjBqWXE2MVl6d3hjcG5aZU4yWEZCcDhLSDFJb3pRMzVCRWs5SjdfVEU0NGcxOVBQTmlCMFdCVHc?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| icfr | mediapen.com | 신외감법 후 외부감사 기업 증가…지난해 4만 2891사 - 미디어펜 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE1scWRLWExwNnFZVlItbzk2QnhHMGo4VkdGc0Y5Y2dseDMtOGFxNDB0LWhTalFDV3J2ODNudEFnTllWZS1odGEweG52dU0zVGlLRFpNVdIBWEFVX3lxTE9KMnZUVy1CTWIybHRmSFFvZ1lqWkJibTIyNzN5eWg2V3lVeVRlLWhYaXJ2VnRKSmVOMXR4b1FxQVpnTnFya3kzV2tLbEh3OUJ4X2hSUVhiTEI?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:similar_news_merged (41건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중심으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFBQcFZGSDROYXJzRmRvdFlZOHJfbDNQME56R1plWDNLM3c3YUU5bmJWUDhpYXVHdU05YzdGOUxLbl9ma3hUeTJCSnpTUUt3LVk5dl9IY1Y3TFJvV082d1Nz?oc=5 | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBJYkpxaXBTcjhUQkZPcHVfay1mQnptQXRhMklhUVNBQ3VSZy1WYWpzeVp4eGdkMmF2bHhDclR6ZHMtMnNJQlNWYVFmb2tsWWxYYndaTEFrcVVHZUnSAWBBVV95cUxPelVLaldNY3hnelFDQzFqaVY0UDBDX3EwY2xkU0QzS3JBc0JBUm5STlFaVlhxRnlpN0FmbXNSQjdEd28zTXFCQWctb2JYN3JLWGZQcUZFdEM3MzJtOFhTTlk?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 |
| kifrs | ilemonde.com | 회계처리 위반 해태제과, 과징금 13억 부과 - 르몽드디플로마티크 | https://news.google.com/rss/articles/CBMiakFVX3lxTE80eXlxMXdTYzVJTlhVTEJEMThxdTh6RUpqX2NBNnp4SXlXaW9JX0Q3WWEwdFRabGRCRkN1d0hsMC01NzAxN05FNkY1c0RiVTRUc2k5VTkyOVNTbVVIdXJFVjJDMDBld2dTbXfSAW5BVV95cUxQa0F2WS1Zd0p6UEw1VXpCWnBDT3NOZW5KdVZuRm5tOHRUSllSb1kwakZSVnNoQktlY1Q0UjJQV040dGIxZjZwRER1MVZUcHlHWXo3ZUlvQVFaUnh1ejJpczV1QXVxTk9ZOGktcC1tdw?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 |
| kifrs | tfmedia.co.kr | 금융위, '회계처리 위반' 해태제과에 9억 과징금·감사인지정 3년 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE1nVW9jUjhaYTVIc1p6ZjFubzYwSEFsUDl4Zkw3dkpKN2hoeHJoUHFBVDFVa3kwZm5XSEpwM0lXcUd3ZjRiZkhVcThYYlNRa0dfOFZCdUFENUpLVGFWclp2UTNvcw?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 |
| kifrs | news.sbs.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - SBS 뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5TcnBZb2hTU0pIYUo2T2VfLTNqTlNwR25EZ0JrWjFMWFJzcjNZUXNZWE9QQnNnN3M1UjBReThYdXlyVHZzT2RGeHpIa1VtMWxyS3N0SlJ3MGctX1JKM01OZ09ZS1QwbDZPSEE?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 |
| kifrs | joseplus.com | 회계기준원, 김정일 대한상의 상근부회장 지속가능성기준위 비상임위원에 선임 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBWQUt1dDZwX0VzYmZtTTBLcDhpQ1pJZWFrdzhwSW5oTF9sRUV6SDVKSVNqenNEV2o4S2VrdVV5b0d2dmE1RGw3c2hrQzZsRmY3OXZTaXNUcHXSAVNBVV95cUxQTWZfbl9xdnBpZ0I3aWgwSm9HN2t5SVRQaWluVjYycU0xMmZ4WDhHcEJFcktlV25Lc3Voa25iU3BNVkUtaGhENkxfbG1XUEdYUG1Gdw?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | seoulfn.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE51SEdGb0VqY2lPZEJIbFZVNHp4QmR5X18tb1NBMlpxOThhU2pTWFgtS3FtaFhZdzk2eGJ5cU5kcjVnMFM2d19laXNxTG5jYm9HUElEMXdwbml1VWFxTGlfMXRuejlocFVNT2c?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | 일간NTN | 금감원, 감사前 재무제표 제출 위반 76건 적발…9개사 감사인 지정 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9FelZSMGExRC1CYVJ4OUFrTHhCdjMwUy1tSjBoQmZFNER3WWo0Ry04dGZSSmttZlBFM2l3VnpZVnRtdV9ZcGdlcTEteW53WURpR1BMZTdmVm1GYWJ6amNQTmhZZXpXUjdianc?oc=5 | → 대표: 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN |
| kifrs | 조세일보 | 영업이익 새 판 짠다…K-IFRS 1118호 시행 석 달 앞으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFB0MnpUYjZVSVNaY2VaT21MQUJDY0Z1N21nWEtCbVNZVWxZNmE3ZTlrcEI3VFdEb2dlZWpVZ0k1bXVzNlBYUENtcnJSUVlLTWFhNjNzZTZyQmphNy13dmtz?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | 이데일리 | 내년 K-IFRS 제1118호 의무 적용…금감원 "기업들, 도입 준비 철저히 해야" - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5ld2NBM0dGUjlxX25jVjFiQmV3cVdPQ0FLYzFUQU8yX2lqUEItQ0JJZ0hEdVBVai1rNmlrZXc5b2stUHhoYWdkdDZpQTAyTWdBM3ZnQUNYX3ZMMjI0cXNKUjBRcjN0UjJXYWNkYkdvSzNOT2c?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | junggi.co.kr | 2027년 K-IFRS 제1118호 시행…기업, 도입 점검 필요 - 중기이코노미 | https://news.google.com/rss/articles/CBMiakFVX3lxTE41S2l3VmRscy1LUlowVVNJaW5BdExCQ3FIQ0Y1N3Zlb0FhSW1qSXpBVzZSVXRpRFJzdHNKN2RqTlhxSEk0Rm9SSkpRaks0d0JHNV9VVDFBUGZYeE9keW5WNVVtM3hMdGhVVHc?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | thevaluenews.co.kr | 손해보험사 영업이익 산출·공시 기준 바뀐다...K-IFRS 제1118호 내년 시행 - 더밸류뉴스 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE14eS1FSzVMV0x5TmlpOUpXUHBwSFpuazk0alpNQWhKdXhNLV9mY0piRXlRVVRFVk5DZmNEMm5HZXJqWEpISG5FVks3X1luTGVOSUNMTw?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPOGFldExqZEFIdGQycE1SbC05ZHV2Z1JaajVGU2YwOWtuSkJ2bmc5aFFSQmJEdGlSVG91anA4RXIyanNELXJDOEd3bkVFclVVRGlSa3E5V01Tb3lyOFZOVVpzQjZYSHo0MUlzSjlEd3dBeTdKeHh5dHlGNUc0VEcxZzFIdW5HRHhB?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | kr.investing.com | ’회계처리기준 위반’ 해태제과식품, 이사회·내부통제 ’대수술’ By EBN - Investing.com 한국어 | https://news.google.com/rss/articles/CBMicEFVX3lxTE5RN0o2MmRJQnNjSTQ5bHBWUURNcG5MV2ZzQzJtR2ZocF9hZ1RKYUdDdEFJczk5ZUtOcElKVXBSd1JONWxteGRlUXN5VDB1UXVzc3JDRVBxUkVPNEVIQmktQUlSaEtGeDFRZVM1Z1JYbTA?oc=5 | → 대표: ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 |
| kifrs | newsis.com | 해태제과식품, 회계 위반 적발에 12%대 급락 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wR0lpRDI5cjZaRUxsaVA5Nzk0SGxINUk2SjMtdks4cGJCWXQ1aTM1b21nVjJjajYxTF9Ed1IxakVteFdxaDlWYllpVGhodHJlSUdZOU9sUy1iQlViczF3dNIBeEFVX3lxTFB2ZXkzLWdiRzBBZkdjTURMaDh1Y1hnVHpBbXRCLTFsdWZ1Y1U0eloyU2NXaUVOeHQ2a2FDZXQzR1lwYUFaNHdXd0c0TWFxRm96QnlMR2NGRy0wOEpjeFkzVVpYU1BpUl9vVlZfcEtHYnNSMlg5SGZydQ?oc=5 | → 대표: ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 |
| kifrs | yna.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VYm1UdW9mM2l1SG84VFJPSnBhSHNGa1dpUzJobWpjNnJ1aXliX2RGMkhNR3FPM09rYjQtREI1d0hBTHU3V2V5aGcwRzJfUEpvaFdvc1V3WENNeVHSAWBBVV95cUxQT2JUYXQzVE5hTGZwR0dROTBxLU93YWYyUDdjMkVxbjBtaEFMYzltaWNJRzRKLVh1OG1ZLWx1ZEJTOWktcHZFRmNOR1lfZzdjZG5wdnB5YzM0M3dra0hXaDU?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | etoday.co.kr | 내년부터 기업 손익계산서 바뀐다⋯금감원 "새 회계기준 대비해야" - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5vbWtNd2xlMWZDeGdsX1BKWU5PSVAycU5qX2tqYXRGRV9hWXMzMTM2RUViZW1JYTh1TktzSXlQaVY3NDZWYy00aTRadmR1QlFwZnZJNQ?oc=5 | → 대표: 내년부터 새 손익 회계기준 도입…시장서는 "당분간 혼란 불가피" - 한국경제 |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 | → 대표: 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 |
| kifrs | newsis.com | 내년부터 'K-IFRS 1118' 시행…"실제 재무제표 산출·검증해야" - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFB5M3puck1JNk05dVZDajFVRjhtR0s0MDc5bm8tWGVSSXQ4QlppWGV2UXlwVHc5U1JQaEZhTjVqZWkwU09jM3U4RFlXTkYyN1dfQWhNaTF3Uzl4OGtzUkFuc9IBeEFVX3lxTE5CNHE0czVVcE1TUXBYcGg2WTRLdTR5X0c1Uks4SkYxOHF3cE0yXy1KUGhIY1lIeXBvMmR3UXBkUkVNblUyNDF4blJ4eTBNcXYyY1h5U1MwVWNnQThXU3RBYmtCZnZtWkJJbWNpUjNWVUdJUmExYjFGUA?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | seoulfn.com | 금감원 "내년 MPM 공시의무 신설···기업별 재무제표 사전 점검 필요" - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBQc3RBaFduX21VU2pXNEhrSlBLV3Nia0MwN0VDVy12Y19ZZjRITGVBVUFQMHl4eHBWV3pSM2txQXZocXhMd1FTSlNweGhsMFFqV0VncS1DVjlNa2xjVWRaOVlkbGFNc2YydHc?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | insnews.co.kr | 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5PTnlLYzlLQklteE1MaW50MjZwRV9RQkRtZDAyal9rdVpCc1pvNXk0M2tCS2hLOVpFa18tVDFmd0VQTDh6bmVBZGR3dkdIU1VFR0ZrWWFrOFpRRkZ1a0Z1eUxsNG9UOG5ncjZF0gFvQVVfeXFMT3dydTBxd2xRSzI3ekVzdF9GVEdtakV1TURuT0VTOEFSbkloTURQV0UzX0F2NWk2MVFqYVBFaDdZN0M2V2xTOGhwR3N1RTB6QnNWUlhNLU9RNkVEbUpmZk12cXlUb3NXUmJJc2dWcFFn?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | alphabiz.co.kr | 내년 새 회계기준 시행…금감원, 기업에 사전 준비 당부 - 알파경제 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1DVjBKVS1Bai03amhmX0k4Zlg1X29uN1RWQjFRNElnYzBDX3JsZHIxVldxTUYzY21EZElaRlJ4eTlYYUdrb3BIWnlTbjZ0T095ZzNMMWlRTEtfeG1QcG9NYnctNXV4SXJodVBZNjJR?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE8teDVTVFFGcExHbG5QekVJcDJNbkxQNVVOamZvdmpheXlIQ2E2WndnOHR2RVA1YnQxZ1JXek5RcW1DZXJrWW9vWE9oblVUZjFxQUFKeWJEeVEwSlc0ZS1MSw?oc=5 | → 대표: 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 |
| kifrs | news.kbs.co.kr | 금융위, 금양에 과징금 76억 부과…“회계처리기준 위반” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBWaTRGZl9ncHJaNnNyVVJYa2tNLVZ1WU5uTG1iMjNfZzVOTFZPM19BamE2RHIyalNKMFdrcnZRbWh1amNza0JGUmxVdDg5NjdMTWdsSlpnQ3BwbE0?oc=5 | → 대표: 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 |
| kifrs | joongang.co.kr | 법무법인 지평, ‘AI회계감리대응센터’ 확대 개편 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE9vMHpYaEZibllYVUpNMThST2MxRi1ZelNUd3BBWG5qbVM4M2lSNEttSDRzRG5Vd3NrWGxyTFp0VHpBajV3Qll6ZmJIU3dtT2x3OGlpdU5n?oc=5 | → 대표: 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 |
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
| icfr | datatooza.com | 크레수드, 2026 회계연도 지배주주 순이익 1772억 페소로 증가…내부통제 취약점 해소 - 데이터투자 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBnNFQycEFSeEhqZTRqekp4cnFJc3dQQVVyRWZRNEpaamtHcFFfV2VQUDI3OTZGMXFRdUVmSHpoQUM5VHVjVzdVZ2NIVUdIU0RpU0xiSmFQcmNYdjdrTGVBZFJFdGlCcWl5UTNsa1lUeHo?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |
| icfr | datatooza.com | 팩트셋, 연간보고서서 내부통제 중대한 취약점 해소 밝혀…미주 영업이익 15.2% 감소 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE51N3FTQkt2U2tmcmgzSGdRZkM2azVxMjZsZWNTd2dOanVQN2Rxei1RNC02QkpmMHRfcFFLaFBCZXNvY1c5bTY4eHNoMTZ5OGtaaExYS1FuN2E3LWtuUUI3aThLeFFtVlFrVGxUZVluTnNvYWM?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |

## collect:event_announcement (11건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | 2026년 글로벌 ESG 교육 워크숍 안내 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2199 |  |
|  | 재정경제부 | 이형일 부총리, 글로벌녹색성장서밋에서 기후대응·성장의 선순환을 위한 국제협력 강조 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079788&menuNo=4010100 |  |
|  | 금융위원회 | 제2차 국민참여성장펀드의 운용사들의 국민투자금 운용전략을 청취하고 향후 관리방안을 논의하였습니다.. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88025?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 기후대응위, 민관 협력으로 철강산업 저탄소 전환 해법 모색 -「산업부문 저탄소 전환정책 포럼(제2차)」개최, 철강산업 현장의 전환과제와 이를 뒷받침할 투자·금융 연계방안 논의 | https://www.fsc.go.kr/no010101/88008?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 포용금융이 금융권에 뿌리내리도록 평가체계를 도입하고, 공공부문이 앞장서서 부실채권 관리체계를 개편하겠습니다.  - 이억원 금융위원장, 제7차 포용적 금융 대전환 회의 주재 | https://www.fsc.go.kr/no010101/88006?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | 제2차 국민참여성장펀드의 운용사들의 국민투자금 운용전략을 청취하고 향후 관리방안을 논의하였습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787132&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
| icfr | core.asiae.co.kr | [Why&Next]‘회계사의 꽃’ 파트너 승진, 신외감법 도입 후 최저수준 전락 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1GQ0paYVh4cms0bTZZVFotNGI5OUI2cnpILU9TVi1qZmZ1MHFlbnRrZnhRNUJ6Y280OGl4TFV0QkpTOGtOV0UtM2Y2Q1JvdmVJTmxLLUxobk9jLV9CM3locm1B?oc=5 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| esg | ESG경제 | [알림] KSSB·ESRS 이중중대성 평가 웨비나 초청 | https://www.esgeconomy.com/news/articleView.html?idxno=17019 |  |
| esg | news.tf.co.kr | 동아ST 지속가능경영보고서, '2025 LACP 비전 어워즈' 수상 | https://news.tf.co.kr/read/economy/2361168.htm |  |

## collect:incident (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 머니투데이 | 증선위, 코스닥 상장사 피델릭스 '회계기준 위반' 고발 조치 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBzNHNDbVFWaDFDNk1nWXdVWW9hZnBpWV9qMXNTSkxBTEthWHM1RFZFb3UtaFE3M1hvZXR5d2ROdC1WaDRMSVJuZ0d6TEJabTR5VmtJbVB6eVZNbWRfNW5Yc3ZBLVJ4UUJ00gFuQVVfeXFMT21rM0lwdWF2UFFfLU5PN0FQUHFtMzl3OW1aZ2UwRm1BTGwtTHY4WWhFb2d3bC0yczhJM3Vmemd1VjFoWk0xc3VKVUF2RzFyU21vT3ZBbnE4RHQxRjRlQnMwajhTSlVuQW85Yk55RVE?oc=5 |  |
| kifrs | news.einfomax.co.kr | 금융당국, '상폐 위기' 금양 검찰 고발…회계기준 위반 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE4tV2cwN0F0UnBSSEg1N2FxSnlKY2JBSk5URk1SelBmemVXOHRwdllqZXFObW1RV002dUczNjI2UHMxMFdZcl9fNFNtSk5QM090ck5MNnBRdjJTcVJyUXFXU2c5eWUtSllrdTZwbmdQNjU?oc=5 |  |
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

## collect:no_category (1720건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 26.11월 국고채, 재정증권, 원화표시 외평채 발행 계획 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079801&menuNo=4010100 |  |
|  | 재정경제부 | 퇴직연금 기능강화 방안 발표 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079784&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 광진 서민금융통합지원센터 방문, 서민금융 지원 강화 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079800&menuNo=4010100 |  |
|  | 재정경제부 | 개인투자용 국채 11월 2,000억원 발행 예정 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079786&menuNo=4010100 |  |
|  | 재정경제부 | 확대 거시경제금융회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079792&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 블룸버그 아태 대표 면담 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079785&menuNo=4010100 |  |
|  | 재정경제부 | 요소수·요소, 주사기·주사침 매점매석행위 금지 고시 종료 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079777&menuNo=4010100 |  |
|  | 재정경제부 | 공공기관 AI 대전환, 우리의 일상을 바꾸다(2026 공공기관 AI 혁신 성과 대회 개최) | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079793&menuNo=4010100 |  |
|  | 재정경제부 | 수출플러스 지원단, 전남광주 지역수출진흥 협력회의 및 수출금융 설명회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079781&menuNo=4010100 |  |
|  | 금융위원회 | 금융위원장, ‘금융분야 재난대응 안전한국훈련’ 주관. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88023?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 보험사기 연루 보험업종사자에 대한 등록취소·업무정지 등 제재. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88021?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | “금융회사의 부실 확산에 신속·선제적으로 대응하여 금융시장의 안정 및 소비자 보호를 위한  ｢금융회사 신속정리제도｣ 도입을 추진합니다.”. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88020?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ☎1375(일상치료)로,  빚의 고통은 덜고 희망의 빛은 더하겠습니다. - 금융위원회·신용회복위원회, 채무상담 대표번호 ☎1375 개통식 개최 -. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88019?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 사업보고서 등에 대한 조사·감리결과 조치 - 제19차 증권선물위원회(’26.10.28.) 조치 의결 | https://www.fsc.go.kr/no010101/88013?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 미공개중요정보를 이용한 내부자등에 대한 중대범죄수사청 고발·통보 등 조치(2건)  - 제19차 증권선물위원회(10.28.) 의결 | https://www.fsc.go.kr/no010101/88012?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 빗썸 등 주요 가상자산사업자들에 대한 해킹사고에 대해 긴밀하고 신속하게 대응하고 있습니다. -「가상자산업권 등 침해사고 관련 긴급점검 회의 개최」 | https://www.fsc.go.kr/no010101/88010?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(국세청) | 글로벌최저한세, 세무전문가들과 함께 두 번째 신고를 준비하다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787086&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 보험사기 연루 보험업종사자에 대한 등록취소·업무정지 등 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787088&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | "금융회사의 부실 확산에 신속·선제적으로 대응하여 금융시장의 안정 및 소비자 보호를 위한  ｢금융회사 신속정리제도｣ 도입을 추진합니다." | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787077&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | ☎1375(일상치료)로,  빚의 고통은 덜고 희망의 빛은 더하겠습니다. - 금융위원회·신용회복위원회, 채무상담 대표번호 ☎1375 개통식 개최 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787075&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 금융위원장, '금융분야 재난대응 안전한국훈련' 주관 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787104&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국세청) | 고용·투자 늘린 중소기업, 세무조사 부담 없앤다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786866&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
| kifrs | sisajournal-e.com | 예보료율 수정안 30일 공개···인상 폭보다 산정 기준이 관건 | https://www.sisajournal-e.com/news/articleView.html?idxno=424652 |  |
| kifrs | youthdaily.co.kr | 삼성전자 주가에 "명운"...삼성생명, 넉달 새 지분가치 '46조' 증발 | https://www.youthdaily.co.kr/news/article.html?no=228986 |  |
| kifrs | newsroad.co.kr | 경영승계 속도 현대해상, 정경선 부사장 리더십 시험대 | http://www.newsroad.co.kr/news/articleView.html?idxno=66627 |  |
| kifrs | news2day.co.kr | 보험업계 반발에 예보료율 인상 재논의…4차 TF 30일 개최 | https://www.news2day.co.kr/article/20261028500214 |  |
| kifrs | metroseoul.co.kr | 삼일PwC, 지스타서 게임기업 회계·세무·AI 전략 짚는다 | http://www.metroseoul.co.kr/article/20261027500160 |  |
| kifrs | 조세일보 | 삼일PwC, 지스타서 ‘게임 산업의 변화 속 기회와 인사이트’ 세미나 개... | http://www.joseilbo.com/news/news_read.php?uid=578210&class=10&grp= |  |
| kifrs | sisaon.co.kr | 생보사 듀레이션갭 '온도차'…내년 규제 앞두고 새판짜기 | https://www.sisaon.co.kr/news/articleView.html?idxno=205473 |  |
| kifrs | newspim.com | "보험사 예보료 1.5조 더 내야"…예보, 인상 폭 논란에 30일 수정안 제시 | https://www.newspim.com/news/view/20261026000877 |  |
| kifrs | fins.co.kr | 보험사 건전성 관리 전환점 맞은 2026년…업계 양극화 우려 | http://www.fins.co.kr/news/articleView.html?idxno=110297 |  |
| kifrs | hansbiz.co.kr | 박병희號 NH농협생명, 신계약 CSM 1조 목표…순익 반등 시험대 | http://www.hansbiz.co.kr/news/articleView.html?idxno=874051 |  |
| kifrs | news.dealsitetv.com | 책임경영 전면 나선 현대해상 3세 정경선 | https://news.dealsitetv.com/articles/177088 |  |
| kifrs | 머니투데이 | 투자자의 자리[MT시평/이병건] | https://www.mt.co.kr/opinion/2026/10/19/2026101517104479541 |  |
| kifrs | hansbiz.co.kr | 프라임에셋, 2027년 하반기 코스피 상장 추진 | http://www.hansbiz.co.kr/news/articleView.html?idxno=873629 |  |
| kifrs | moneystorm.kr | [특징주] 서부T&D, 개발사업 본격화·자산가치 재평가 기대에 8.26% 급등 | https://www.moneystorm.kr/news/articleView.html?idxno=7353 |  |
| kifrs | pointdaily.co.kr | '오픈 다트'서 주총 안건 한눈에 본다…금감원, 기관 의결권 행사 지원 | https://www.pointdaily.co.kr/news/articleView.html?idxno=322122 |  |
| kifrs | 한국경제 | 오픈 다트에서 주총 안건 한눈에…XBRL 주석 데이터도 개방 | https://www.hankyung.com/article/202610138647r |  |
| kifrs | newspim.com | 금감원, 오픈다트 개선·XBRL 분류체계 정비 | https://www.newspim.com/news/view/20261013000752 |  |
| kifrs | dailian.co.kr | 주총 '쏠림 개최'에 공시 개선…금감원, 기관투자자 의결권 행사 '측면... | https://www.dailian.co.kr/news/view/1700786/?sc=Naver |  |
| kifrs | 이데일리 | 내년부터 오픈 다트(Open DART)서 주총 안건도 확인 “신속한 의결권 행... | https://www.edaily.co.kr/News/Read?newsId=03001206645612592&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| kifrs | newspim.com | 금감원, 주총 안건 Open DART로 한 눈에…XBRL 재무정보 활용도 높인다 | https://www.newspim.com/news/view/20261013000348 |  |
| kifrs | news.einfomax.co.kr | [오늘의 채권ㆍ외환 메모] (10월13일) | https://news.einfomax.co.kr/news/articleView.html?idxno=4438882 |  |
| kifrs | view.asiae.co.kr | 비싼 땅 많이 가진 '알짜 땅부자' 자산株 뜰까 | https://view.asiae.co.kr/article/2026100717011194659 |  |
| kifrs | fins.co.kr | 새 회계기준 앞둔 보험사, 영업손익 재편·성과공시 부담 커진다 | http://www.fins.co.kr/news/articleView.html?idxno=110214 |  |
| kifrs | news.einfomax.co.kr | [오늘 재경부 등 경제부처 일정] | https://news.einfomax.co.kr/news/articleView.html?idxno=4438843 |  |
| kifrs | ppss.kr | 금융감독원, 내년 도입 '새 회계기준' 점검 촉구…"재무제표 전면 개편... | https://www.ppss.kr/news/articleView.html?idxno=315172 |  |
| kifrs | news2day.co.kr | [N2 모닝 경제 브리핑-10월 13일] 美 증시, 반도체주 급락에 3대 지수 혼... | https://www.news2day.co.kr/article/20261012500029 |  |
| kifrs | news.einfomax.co.kr | [이번주 한국은행 및 금융위·금감원 일정] | https://news.einfomax.co.kr/news/articleView.html?idxno=4438585 |  |
| kifrs | 조세일보 | 금주 한국은행 및 금융당국(금융위·금감원) 주요일정 | http://www.joseilbo.com/news/news_read.php?uid=577139&class=18&grp= |  |
| kifrs | newspim.com | 이번주 국내 주요 금융일정(10.12~10.16) | https://www.newspim.com/news/view/20261008001274 |  |
| kifrs | 이데일리 | 다음 주 금융당국 일정 | https://www.edaily.co.kr/News/Read?newsId=01521926645611608&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| kifrs | news.einfomax.co.kr | [다음주 한국은행 및 금융위·금감원 일정] | https://news.einfomax.co.kr/news/articleView.html?idxno=4438462 |  |
| kifrs | fins.co.kr | 자본부담 줄이려다 새 위험 떠안나…일본, 생보 재보험 감독 강화 | http://www.fins.co.kr/news/articleView.html?idxno=110179 |  |
| kifrs | businessplus.kr | [금융권 이모저모]미래에셋자산운용, TIGER 커버드콜 3종 개인 순매수 1... | https://www.businessplus.kr/news/articleView.html?idxno=117838 |  |
| kifrs | naeil.com | 저PBR 기업 자산재평가 통한 기업가치 제고 요구 활성화 | https://www.naeil.com/news/read/604408?ref=naver |  |
| kifrs | pointdaily.co.kr | 日 재보험 규제 강화…국내서도 위험 관리 필요 지적 | https://www.pointdaily.co.kr/news/articleView.html?idxno=321395 |  |
| kifrs | thepublic.kr | '숨은 땅부자' 상장사 뜬다…토지 가치 드러나자 주주행동도 활발 | https://www.thepublic.kr/news/articleView.html?idxno=321216 |  |
| kifrs | news2day.co.kr | 교육세 인상 청구서 받는 보험·카드사…국감 질의 과제로 | https://www.news2day.co.kr/article/20261002500291 |  |
| kifrs | kookje.co.kr | 기업 보유 토지 공시지가 공시 의무화…‘땅부자’ 상장사 수면 위로 | http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20261006.22010001099 |  |
| kifrs | econovill.com | 상장사 '숨은 땅값' 드러난다…저PBR 자산주 주목 | https://www.econovill.com/news/articleView.html?idxno=752722 |  |
| kifrs | chosun.com | 기업 보유한 토지, 이제 공시지가로도 공시…저(低) PBR ‘숨은 땅부자... | https://www.chosun.com/economy/money/2026/10/05/SOPVRUJQMFHE3GM5LFBITI23TA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| kifrs | lcnews.co.kr | 日 생보사 재보험 활용 확대…자본 부담 낮추자 감독도 강화 | https://www.lcnews.co.kr/news/articleView.html?idxno=209206 |  |
| kifrs | yna.co.kr | 보유 부동산 가치 한눈에…'알짜배기 부동산' 저PBR주 훈풍부나 | https://www.yna.co.kr/view/AKR20261002078000008?input=1195m |  |
| kifrs | joongang.co.kr | 영림원소프트랩, IFRS 18 맞춰 ERP 개편…천안·수원서 세미나 | https://www.joongang.co.kr/article/25466372 |  |
| kifrs | zdnet.co.kr | 영림원소프트랩, IFRS 18 대응 ERP 고도화…천안·수원서 고객 세미나 개... | https://zdnet.co.kr/view/?no=20261001143212 |  |
| kifrs | itdaily.kr | 영림원소프트랩, IFRS 18 선제 대응 나선다 | https://www.itdaily.kr/news/articleView.html?idxno=241953 |  |
| kifrs | cbci.co.kr | [금융家] 교보생명 ㅣ SBI 품고 금융그룹 재편 속도…저축은행·디지털... | https://www.cbci.co.kr/news/articleView.html?idxno=611455 |  |
| kifrs | it.chosun.com | 영림원소프트랩, IFRS 18 전환 지원…ERP 고도화·고객 세미나 확대 | https://it.chosun.com/news/articleView.html?idxno=2023092171175 |  |
| kifrs | hansbiz.co.kr | 영림원소프트랩 IFRS18 ERP 고도화 | http://www.hansbiz.co.kr/news/articleView.html?idxno=869235 |  |
| kifrs | etnews.com | 영림원소프트랩, IFRS18 대응 ERP 고도화…전국 고객 세미나 확대 | https://www.etnews.com/20261001000073 |  |
| kifrs | newsis.com | 영림원소프트랩, 새 국제회계기준 맞춰 ERP 고도화…전국 세미나 확대 | https://www.newsis.com/view/NISX20261001_0003810085 |  |
| kifrs | it-b.co.kr | 영림원소프트랩, IFRS 18 제도 변화에 ERP 시스템 선제 고도화 | https://www.it-b.co.kr/news/articleView.html?idxno=90079 |  |
| kifrs | mdtoday.co.kr | 기업 토지 '공시지가' 주석공시 의무화..."기업가치 변동 자료로" | https://www.mdtoday.co.kr/news/articleView.html?idxno=616422 |  |
| kifrs | m.skyedaily.com | 장부가 옆에 ‘공시지가’… 기업분석에 비교정보 하나 더 | https://m.skyedaily.com/news_view.html?ID=312079 |  |
| kifrs | vegannews.co.kr | 회계정책 변경은 소급, 추정 변경은 전진 적용 | https://www.vegannews.co.kr/news/article.html?no=388537 |  |
| kifrs | ddaily.co.kr | “기업 땅값, 장부가만 보지 마세요”…올해부터 공시지가도 재무제표... | https://www.ddaily.co.kr/page/view/2026092411113285473 |  |
| kifrs | metroseoul.co.kr | 기업 보유 토지 공시지가, 올해 결산부터 재무제표에 공개 | http://www.metroseoul.co.kr/article/20260923500282 |  |
| kifrs | view.asiae.co.kr | "기업가치 파악 쉽게"…금융위, 기업토지 '공시지가' 주석공시 의무화 | https://view.asiae.co.kr/article/2026092319580144801 |  |
| kifrs | newsway.co.kr | 기업 땅값 '장부가 착시' 줄인다…공시지가로 자산가치 비교 | https://www.newsway.co.kr/news/view?ud=2026092316484459330 |  |
| kifrs | news1.kr | 장부에 묵혀둔 기업보유 땅값, 재무제표에 공시지가로 공개 | https://www.news1.kr/finance/financial-policy/6300634 |  |
| kifrs | dnews.co.kr | 기업 보유 부동산 취득원가ㆍ공시지가 함께 공시 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202609231545293300322 |  |
| kifrs | 매일경제 | 기업 보유 토지 공시지가, 올해 결산부터 주석에 공개 | https://www.mk.co.kr/article/12160450 |  |
| kifrs | wowtv.co.kr | ‘알짜 땅’ 얼마나 들고 있나…'공시지가' 주석 공시 의무화 | http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202609230145&t=NN |  |
| kifrs | 한국경제 | 기업 토지 '공시지가' 재무제표 기재 의무화…올해 결산부터 적용 | https://www.hankyung.com/article/202609233912r |  |
| kifrs | 조세일보 | [Q&A] 기업 토지 ‘공시지가’ 주석공시 예시 및 FAQ | http://www.joseilbo.com/news/news_read.php?uid=576307&class=18&grp= |  |
| kifrs | etoday.co.kr | 기업 보유 토지 장부가 옆에 ‘공시지가’ 공개…올해부터 적용 | https://www.etoday.co.kr/news/view/2629181 |  |
| kifrs | 머니투데이 | 기업 보유 토지 '공시지가' 재무제표에 공개…올해 말부터 적용 | https://www.mt.co.kr/stock/2026/09/23/2026092315224870052 |  |
| kifrs | 조세일보 | 장부가에 묻힌 ‘땅값’ 드러난다…기업 토지 공시지가 공개 | http://www.joseilbo.com/news/news_read.php?uid=576306&class=18&grp= |  |
| kifrs | sentv.co.kr | 기업 보유 토지 ‘공시지가’ 주석에 담는다…올해 말부터 적용 | https://www.sentv.co.kr/article/view/sentv202609230159 |  |
| kifrs | biz.sbs.co.kr | 장부가만 보이던 기업 토지…올해 결산부터 '공시지가' 공개 | https://biz.sbs.co.kr/article_hub/20000336544?division=NAVER |  |
| kifrs | newsis.com | 기업 보유 토지 '공시지가' 재무제표에 뜬다…올해 결산부터 주석공시 | https://www.newsis.com/view/NISX20260923_0003802355 |  |
| kifrs | 한국세정신문 | 삼정KPMG, 내달 대구·부산서 '경북·경남지역 재무전략 세미나' 개최 | https://www.taxtimes.co.kr/news/article.html?no=276890 |  |
| kifrs | topdaily.kr | iM라이프, 단기납 종신보험 만기 도래에 자본관리 '적신호' | https://www.topdaily.kr/articles/111941 |  |
| kifrs | fins.co.kr | GA 판매품질, 보험사 K-ICS 변수 된다…제휴 기준 재편 예고 | http://www.fins.co.kr/news/articleView.html?idxno=109970 |  |
| kifrs | upkoreanews.kr | 한화손해보험, 車보험 6% 키우고 CSM 39.6%↑…캐롯·여성보험으로 이익... | https://www.upkoreanews.kr/news/articleView.html?idxno=100221 |  |
| kifrs | newsis.com | 삼정KPMG, 내달 1~2일 대구·부산서 '재무전략 세미나' 개최 | https://www.newsis.com/view/NISX20260914_0003788426 |  |
| kifrs | biz.heraldcorp.com | 삼정KPMG, 10월 ‘2026 경북·경남지역 재무전략 세미나’ 개최 | https://biz.heraldcorp.com/article/10872232?ref=naver |  |
| kifrs | cbci.co.kr | [금융家] 보험 ⑤ㅣ 산재보험 지원부터 GA 규제까지…보장은 넓히고 감... | https://www.cbci.co.kr/news/articleView.html?idxno=606480 |  |
| kifrs | view.asiae.co.kr | 경상권 기업 새 회계기준 대응은…삼정KPMG, 재무전략 세미나 | https://view.asiae.co.kr/article/2026091409184141922 |  |
| kifrs | 파이낸셜뉴스 | AI가 장부까지 쓴다…삼정KPMG "재무혁신, 내부통제가 관건" | https://www.fnnews.com/news/202609140841034867 |  |
| kifrs | 조세일보 | 삼정KPMG, 10월 대구·부산서 ‘경북·경남지역 재무전략 세미나’ 개최 | http://www.joseilbo.com/news/news_read.php?uid=575597&class=10&grp= |  |
| kifrs | etoday.co.kr | 삼정KPMG, 경북∙경남지역 재무전략 세미나 개최…"기업 재무전략 통합... | https://www.etoday.co.kr/news/view/2624962 |  |
| kifrs | sidae.com | 보험부채 부풀리기 막는다…계리가정 보고 의무화 | https://www.sidae.com/article/2026091117293612259 |  |
| kifrs | dealsite.co.kr | 보험사 ‘계리가정’ 매년 들여다본다…금융당국 감독 강화 | https://dealsite.co.kr/articles/168902 |  |
| kifrs | businesspost.co.kr | 보험사 내년부터 GA 불완전판매 발생하면 지급여력비율 불이익, 관리 책... | https://www.businesspost.co.kr/BP?command=article_view&num=447012 |  |
| kifrs | cstimes.com | 보험부채 평가 투명성 높인다…보험사 '계리가정 보고서' 의무화 | https://www.cstimes.com/news/articleView.html?idxno=720379 |  |
| kifrs | etoday.co.kr | GA 관리 부실 땐 보험사 ‘킥스’ 불이익…내년 운영위험 등급제 도입 | https://www.etoday.co.kr/news/view/2624627 |  |
| kifrs | econovill.com | 보험사 GA 운영위험 등급제 도입...불완전판매 비율 등 기준 | https://www.econovill.com/news/articleView.html?idxno=750590 |  |
| kifrs | kbanker.co.kr | 보험사, 계리가정 보고서 매년 금감원에 낸다 | https://www.kbanker.co.kr/news/articleView.html?idxno=225917 |  |
| kifrs | ebn.co.kr | 금융당국, '계리가정 보고서' 도입으로 보험부채평가 투명성 '대수술' | https://www.ebn.co.kr/news/articleView.html?idxno=1723968 |  |
| kifrs | globalepic.co.kr | GA 리스크, 보험사 '자본건전성'에 연동…계리가정 검증도 전면 강화 | http://www.globalepic.co.kr/view.php?ud=2026091115341114437cc35ccc5c_29 |  |
| kifrs | ppss.kr | 금융위, 보험사 관리 책임 강화...보험 GA 운영위험 5등급 평가 도입 | https://www.ppss.kr/news/articleView.html?idxno=310163 |  |
| kifrs | greened.kr | 보험사 계리가정 관리 깐깐해진다…금융위, 듀레이션 갭·GA 운영위험도... | https://www.greened.kr/news/articleView.html?idxno=349860 |  |
| kifrs | dailian.co.kr | 보험사 계리가정 함부로 못 바꾼다…매년 금감원에 보고한다 | https://www.dailian.co.kr/news/view/1689333/?sc=Naver |  |
| kifrs | ddaily.co.kr | “보험부채 평가 더 깐깐해진다”…보험사 ‘계리가정 보고서’ 의무화 | https://www.ddaily.co.kr/page/view/2026091115025834950 |  |
| kifrs | kpinews.kr | 금융위, 보험사 '계리가정 보고서' 신설…부채평가 이상징후 살핀다 | https://www.kpinews.kr/newsView/1065589771615035 |  |
| kifrs | 일간NTN | 보험업감독규정 개정…보험부채 평가 신뢰성 높여 IFRS17 안착 다진다 | http://www.intn.co.kr/news/articleView.html?idxno=2053279 |  |
| kifrs | ntoday.co.kr | 보험사 실적 만드는 '가정'까지 본다…IFRS17 감독 강화 | https://www.ntoday.co.kr/news/articleView.html?idxno=129313 |  |
| kifrs | pinpointnews.co.kr | 보험부채 좌우하는 계리가정, 매년 금감원에 보고 의무화 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=486176 |  |
| kifrs | nbntv.kr | 국세청, 글로벌최저한세 간담회 개최… 두 번째 신고 대비 행정·전산 지... | https://www.nbntv.kr/news/articleView.html?idxno=341051 |  |
| kifrs | newspenguin.com | 삼성생명 숨은 배출량 80% 더 나왔는데..."감축 목표와는 별개" | https://www.newspenguin.com/news/articleView.html?idxno=22362 |  |
| kifrs | goodkyung.com | [금융 이모저모] 신한은행, 창경궁 무료 오디오 가이드 서비스 운영 | https://www.goodkyung.com/news/articleView.html?idxno=292918 |  |
| kifrs | smarttoday.co.kr | [은행가] 우리은행, 보안 허점 찾는 청년 인재에 기회 열다 등 | https://www.smarttoday.co.kr/ko-kr/articles/113263 |  |
| kifrs | ESG경제 | 한국공인회계사회, '제27회 지속가능성인증포럼' 웨비나 | https://www.esgeconomy.com/news/articleView.html?idxno=17175 |  |
| kifrs | daily.hankooki.com | [태안군의회소식] 장영숙 부의장 "태안해상풍력, 군정 방향 명확히 밝혀... | https://daily.hankooki.com/news/articleView.html?idxno=1419822 |  |
| kifrs | thefirstmedia.net | NH농협은행, 기업 퇴직연금 실무 안내서 개정판 발간 | http://www.thefirstmedia.net/news/articleView.html?idxno=212145 |  |
| kifrs | biotimes.co.kr | 제약업계, CVC 투자 R&D 인정 촉구…정부 재무 잣대 변수 | https://www.biotimes.co.kr/news/articleView.html?idxno=35701 |  |
| kifrs | newsworks.co.kr | 은행권, 퇴직연금 서비스 확대…ETF 거래부터 실무 지원까지 | https://www.newsworks.co.kr/news/articleView.html?idxno=901293 |  |
| kifrs | news.bbsi.co.kr | NH농협은행, '알기쉬운 퇴직연금' 2026 개정판 발간 | https://news.bbsi.co.kr/news/articleView.html?idxno=4115526 |  |
| kifrs | insightkorea.co.kr | 이실 NH투자증권 본부장 "주식보상, 기업·임직원 모두에게 '윈-윈'" | https://www.insightkorea.co.kr/news/articleView.html?idxno=257605 |  |
| kifrs | news.dealsitetv.com | [은행 Talk Talk] KB금융, 3분기 사회적 가치 9037억원 창출 外 | https://news.dealsitetv.com/articles/177709 |  |
| kifrs | webeconomy.co.kr | [은행] 수은 전략물자 금융지원·농협 퇴직연금 안내서 및 모바일 개편... | https://www.webeconomy.co.kr/news/articleView.html?idxno=2353415 |  |
| kifrs | bloter.net | SK이노베이션이 설명한 'SKIET 합병' 속사정 | https://www.bloter.net/news/articleView.html?idxno=677080 |  |
| kifrs | sateconomy.co.kr | [금융소식] NH농협·신한·IBK기업·우리·BNK경남은행·새마을금고·농... | https://sateconomy.co.kr/news/view/1065585653445278 |  |
| kifrs | womentimes.co.kr | NH농협은행, '알기쉬운 퇴직연금' 개정판 발간…8월 기준 법령 반영 | https://www.womentimes.co.kr/news/articleView.html?idxno=107416 |  |
| kifrs | thevaluenews.co.kr | [더밸류 브리핑] 오늘의 은행 소식...NH농협은행·BNK부산은행·Sh수협은... | http://www.thevaluenews.co.kr/news/view.php?idx=202780 |  |
| kifrs | businessplus.kr | [금융권 이모저모]신한자산운용, 환헤지 미국배당 ETF 수익률 1위 外 | https://www.businessplus.kr/news/articleView.html?idxno=118927 |  |
| kifrs | slist.kr | [은행가] 하나금융그룹, 밀알학교 '디지털 진로탐색 교실' 조성 外 | https://www.slist.kr/news/articleView.html?idxno=777392 |  |
| kifrs | newsclaim.co.kr | NH농협은행 퇴직연금 실무 길라잡이 새단장 | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080589 |  |
| kifrs | delighti.co.kr | NH농협은행, 기업 실무자를 위한 '알기쉬운 퇴직연금' 2026 개정판 발간 | https://www.delighti.co.kr/news/articleView.html?idxno=124073 |  |
| kifrs | 4th.kr | [경제소식] 우리은행·금융보안원, '우리콘' 시상식…대학생 40개팀 모의... | http://www.4th.kr/news/articleView.html?idxno=2120673 |  |
| kifrs | 한국경제 | "세금 1원도 안 낸다"…억만장자들의 5조달러 절세 비법 [밤 사이 해외 ... | https://www.hankyung.com/article/202610292669i |  |
| kifrs | mhj21.com | NH농협은행, 기업 실무자용 '알기쉬운 퇴직연금' 2026 개정판 발간 | https://www.mhj21.com/news/articleView.html?idxno=254549 |  |
| kifrs | dailysmart.co.kr | "복잡한 퇴직연금 실무, 이 한 권으로 끝"… NH농협은행, '알기쉬운 퇴직... | http://www.dailysmart.co.kr/news/articleView.html?idxno=131689 |  |
| kifrs | weeklytoday.com | [금융권 소식] KB금융ㆍNH농협은행ㆍ새마을금고(10.29) | http://www.weeklytoday.com/news/articleView.html?idxno=800094 |  |
| kifrs | pressman.kr | 은행권, 기업·청년 맞춤 지원 확대 | https://www.pressman.kr/news/articleView.html?idxno=104220 |  |
| kifrs | newsquest.co.kr | NH농협은행, 기업 실무자용 '알기쉬운 퇴직연금' 개정판 발간 | https://www.newsquest.co.kr/news/articleView.html?idxno=303685 |  |
| kifrs | discoverynews.kr | NH농협은행, 퇴직연금 실무 안내서 개정판 발간 | https://www.discoverynews.kr/news/articleView.html?idxno=1105212 |  |
| kifrs | newsmap.co.kr | NH농협은행, '알기쉬운 퇴직연금' 2026 개정판 발간 | https://www.newsmap.co.kr/news/articleView.html?idxno=4573 |  |
| kifrs | ziksir.com | NH농협은행, 기업 실무자 위한 퇴직연금 안내서 개정판 발간 | https://www.ziksir.com/news/articleView.html?idxno=151184 |  |
| kifrs | popcornnews.net | NH농협은행, 기업 퇴직연금 실무 안내서 개정판 발간 | http://www.popcornnews.net/news/articleView.html?idxno=137831 |  |
| kifrs | kpenews.com | NH농협은행, 기업 퇴직연금 실무 지원 강화..'알기쉬운 퇴직연금' 개정... | https://kpenews.com/View.aspx?No=4287986 |  |
| kifrs | jasm.co.kr | NH농협은행, '알기쉬운 퇴직연금' 2026년 개정판 발간 | https://www.jasm.co.kr/news/view/323371/?sc=Naver |  |
| kifrs | newsian.co.kr | 박현주가 예고한 日M&A는 산코증권…닛케이 "50억엔 규모" | https://www.newsian.co.kr/news/articleView.html?idxno=100171 |  |
| kifrs | srtimes.kr | NH농협은행, 기업 실무자 위한 '알기쉬운 퇴직연금' 개정판 발간 | http://www.srtimes.kr/news/articleView.html?idxno=216148 |  |
| kifrs | globalepic.co.kr | NH농협은행, '알기쉬운 퇴직연금' 발간…기업 실무 지원 사격 | https://www.globalepic.co.kr/view.php?ud=2026102908540651697cc35ccc5c_29 |  |
| kifrs | 파이낸셜뉴스 | NH농협은행, 기업 실무자 위한 '알기쉬운 퇴직연금' 개정판 발간 | https://www.fnnews.com/news/202610290841271377 |  |
| kifrs | hansbiz.co.kr | [증권가H] 맥쿼리, 가비아·KINX 인수 추진...얼라인도 합의 등 | http://www.hansbiz.co.kr/news/articleView.html?idxno=877403 |  |
| kifrs | futurechosun.com | [더나은미래 경제브리핑] SK하이닉스, 분기 매출 첫 100조 돌파…이찬진... | https://futurechosun.com/?p=164825 |  |
| kifrs | businesspost.co.kr | '65세 정년' 논의 이어지는데 65세 이상 취업자 400만 명 넘어서, '실업... | https://www.businesspost.co.kr/BP?command=article_view&num=450554 |  |
| kifrs | 임팩트온 | 싱가포르, 해외 REC 인정 기준 강화…전력 공급 없으면 재생전력 실적 ... | https://www.impacton.net/news/articleView.html?idxno=30438 |  |
| kifrs | hellot.net | [이슈 포커스] 기업 반발에 탄소회계 기준 후퇴 논란…과학계·투자자는... | https://www.hellot.net/news/article.html?no=115827 |  |
| kifrs | sejungilbo.com | '역대급 세수 오차'…오차 80%는 재경부 모형 부실 탓이었다 | https://www.sejungilbo.com/news/articleView.html?idxno=60829 |  |
| kifrs | etoday.co.kr | [ESGX 이슈 5] GHG 프로토콜, 전력 배출량 산정기준 강화 유예 검토 | https://www.etoday.co.kr/news/view/2640503 |  |
| kifrs | view.asiae.co.kr | 정부가 떠안은 보증·융자 빚, 국가 장부에 안보여...통합 결산 방식 도... | https://view.asiae.co.kr/article/2026102710003162822 |  |
| kifrs | newsclaim.co.kr | [BNK금융 인사 전망] 빈대인 연임 첫 연말 인사… 7개 계열사 CEO 인선 | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080169 |  |
| kifrs | news.tf.co.kr | 전남광주시 첫 공식 금고에 농협은행·광주은행 선정…25조 원 재정 관리 | https://news.tf.co.kr/read/national/2381033.htm |  |
| kifrs | dailian.co.kr | 국감 끝난 보험업계…예보료 부담 조정·GA 관행 개선 과제 | https://www.dailian.co.kr/news/view/1706283/?sc=Naver |  |
| kifrs | 머니투데이 | 이준석, 美 '코리아코커스'에 "동맹의 책임, 한국의 권익 모두 중요" | https://www.mt.co.kr/politics/2026/10/26/2026102618583471824 |  |
| kifrs | busan.com | ‘서울시 민간위탁 사업 조례 개정안’ 입법예고…세무사회 “적극 환영... | https://www.busan.com/view/busan/view.php?code=2026102621342054024 |  |
| kifrs | ekn.kr | [패트롤] 고양시의회-남양주시의회-동두천시의회-의왕시의회 | https://www.ekn.kr/web/view.php?key=20261026021521414 |  |
| kifrs | namdonews.com | 25조 통합시 금고지기, 농협 일반·광주은행 특별회계 | https://www.namdonews.com/news/articleView.html?idxno=927322 |  |
| kifrs | 임팩트온 | 기후공시, 숫자만으론 부족…기업의 기후위험, 투자 판단으로 연결해야 | https://www.impacton.net/news/articleView.html?idxno=30403 |  |
| kifrs | news.tf.co.kr | 이준석, 美 코리아코커스 공동의장 측 면담…"韓 안보 무임승차, 동의 ... | https://news.tf.co.kr/read/ptoday/2380964.htm |  |
| kifrs | gndomin.com | 진주시의회, 예산심사 실무교육으로 준비 박차 | http://www.gndomin.com/news/articleView.html?idxno=494265 |  |
| kifrs | fieldnews.kr | 세무사회, 서울시 민간위탁 조례 개정안 환영…조속한 통과 촉구 | http://www.fieldnews.kr/news/articleView.html?idxno=32539 |  |
| kifrs | weekly.hankooki.com | [혁신형 제약 이원화 법률 점검 上] "30점 받아도 도약형"…사라지는 최... | https://weekly.hankooki.com/news/articleView.html?idxno=7190333 |  |
| kifrs | biz.chosun.com | 예보료 3.3배 인상안에 보험업계 반발… 요율 확정 해 넘기나 | https://biz.chosun.com/stock/finance/2026/10/26/XTEOJLN5QBCYVM2MNUNGC6W534/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| kifrs | aptn.co.kr | 경기도, 간접흡연 예방 등 공동주택 관리규약 준칙 개정 추진 | http://www.aptn.co.kr/news/articleView.html?idxno=113089 |  |
| kifrs | 조세일보 | 세무사회 "서울시 민간위탁 사업비 검사, 세무사 참여 허용해야" | http://www.joseilbo.com/news/news_read.php?uid=578113&class=10&grp= |  |
| kifrs | theviewers.co.kr | [한화금융 확장 셈법] ⑦진격의 김동원, 이해상충 장벽 넘을 해법은 | https://theviewers.co.kr/View.aspx?No=4275164 |  |
| kifrs | gj.newdaily.co.kr | 한병도 국회의원 “대학을 지역 성장 거점으로”…‘대학도시’ 정책 제... | https://gj.newdaily.co.kr/site/data/html/2026/10/25/2026102500066.html |  |
| kifrs | jeollailbo.com | 한병도 "대학을 지역의 심장으로"대학 자원, 지역 성장동력 전환 | http://www.jeollailbo.com/news/articleView.html?idxno=814620 |  |
| kifrs | 일간NTN | [한국세무사회 논평] "서울시의회는 민간위탁 '결산서 검사' 조례안 조... | http://www.intn.co.kr/news/articleView.html?idxno=2054294 |  |
| kifrs | 임팩트온 | 【박정훈의 ESG 리터러시】ESG ADHD | https://www.impacton.net/news/articleView.html?idxno=30383 |  |
| kifrs | ohmynews.com | 아파트 간접흡연 해결 나선 경기도... 관리규약 준칙 개정 | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003278115&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| kifrs | weeklytoday.com | [위클리오늘] 경기도, 공동주택 간접흡연 예방 등 관리규약 준칙 개정 ... | http://www.weeklytoday.com/news/articleView.html?idxno=799367 |  |
| kifrs | lawissue.co.kr | 경기도, 아파트 관리규약 18개 항목 손질… 층간 간접흡연 대응·종사자... | https://www.lawissue.co.kr/view.php?ud=202610231356146954d94aa4ada6_12 |  |
| kifrs | thelec.kr | 中 딥시크, 약 20조원 대형 투자 유치 마무리 단계 | https://www.thelec.kr/news/articleView.html?idxno=64199 |  |
| kifrs | etnews.com | AC협회, 창업기획자 준법감시인 양성 교육 개최 | https://www.etnews.com/20261023000308 |  |
| kifrs | ngetnews.com | 경기도, 공동주택 관리규약 준칙 개정 추진…간접흡연 예방 등 18건 | https://www.ngetnews.com/news/articleView.html?idxno=555021 |  |
| kifrs | newstnt.com | 경기도, 아파트 간접흡연·관리종사자 처우 개선 추진…관리규약 준칙 ... | https://www.newstnt.com/news/articleView.html?idxno=724574 |  |
| kifrs | wikileaks-kr.org | 초기투자액셀러레이터협회, 창업기획자 준법감시인 양성교육 연다 | https://www.wikileaks-kr.org/news/articleView.html?idxno=193644 |  |
| kifrs | hapt.co.kr | 경기도 '공동주택 간접흡연 민원 처리기준' 준칙 의견 받는다 | https://www.hapt.co.kr/news/articleView.html?idxno=169787 |  |
| kifrs | daily.hankooki.com | 경기도, 공동주택 간접흡연 예방 등 관리규약 준칙 개정 추진 | https://daily.hankooki.com/news/articleView.html?idxno=1417836 |  |
| kifrs | sportsseoul.com | 한병도, “대학을 지역의 심장으로”… 대학 자원 활용한 ‘대학도시’... | https://www.sportsseoul.com/news/read/1643554?ref=naver |  |
| kifrs | jeonmin.co.kr | 한병도 "대학을 지역 성장 거점으로"…유휴 부지·적립금 활용 제안 | http://www.jeonmin.co.kr/news/articleView.html?idxno=449119 |  |
| kifrs | venturesquare.net | 초기투자액셀러레이터협회, 창업기획자 준법감시인 양성 교육 개최…내... | https://www.venturesquare.net/1122306/ |  |
| kifrs | 머니투데이 | 한병도 의원, 대학 자원 활용한 '대학도시' 정책자료집 발간 | https://www.mt.co.kr/policy/2026/10/23/2026102310013691179 |  |
| kifrs | kmaeil.com | 경기도, 공동주택 관리규약 준칙 개정 추진 | https://www.kmaeil.com/news/articleView.html?idxno=655462 |  |
| kifrs | enewstoday.co.kr | 경기도, 공동주택 간접흡연·관리종사자 처우 개선 나서 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2483666 |  |
| kifrs | kyeonggi.com | 경기도, 공동주택 간접흡연 예방·관리종사자 처우 개선 나서 | https://www.kyeonggi.com/article/20261023580027 |  |
| kifrs | news1.kr | 경기도, 공동주택 관리규약 개정 추진…간접흡연 피해 방지 강화 | https://www.news1.kr/local/gyeonggi/6329549 |  |
| kifrs | econonews.co.kr | 경기도, 공동주택 간접흡연·관리종사자 처우 개선 등 관리규약 준칙 개... | http://www.econonews.co.kr/news/articleView.html?idxno=446119 |  |
| kifrs | view.asiae.co.kr | 경기도, 공동주택 간접흡연 예방 등 관리규약 준칙 개정 추진 | https://view.asiae.co.kr/article/2026102307340308894 |  |
| kifrs | ceoscoredaily.com | [중복상장 논란]③ SK, ‘최태원 리밸런싱’에도 3중상장 4곳 ‘최다’…... | https://www.ceoscoredaily.com/page/view/2026102211110810793 |  |
| kifrs | daily.hankooki.com | 남부발전, 경영진·이사진 대상 내부통제·회계관리 교육 진행 | https://daily.hankooki.com/news/articleView.html?idxno=1417630 |  |
| kifrs | pinpointnews.co.kr | 남부발전, 경영진 내부통제 교육…재무 투명성 제고 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=497742 |  |
| kifrs | 이데일리 | IFRS18에 코스닥 환기종목 변수…5년 연속 적자 판정 달라지나 | https://www.edaily.co.kr/News/Read?newsId=04821606645615544&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| kifrs | nocutnews.co.kr | 춘천시의회 행감에서, 이해충돌부터 안전·회계 부실까지 무더기 지적 | https://www.nocutnews.co.kr/news/6595103?utm_source=naver&utm_medium=article&utm_campaign=20261021060412 |  |
| kifrs | newstomato.com | 생보사, 종신보험 판매 주춤하자 상품개편 안간힘 | http://www.newstomato.com/ReadNews.aspx?no=1317482&inflow=N |  |
| kifrs | naeil.com | 금융당국 ‘회계부정 기업’ 중수청 고발…수사체계 개편 후 첫 적용 | https://www.naeil.com/news/read/605796?ref=naver |  |
| kifrs | bizhankook.com | '무늬만 친환경' 투자 넘어서려면…한국형 기후 벤치마크의 성공조건 | https://bizhankook.com/articles/korea-climate-finance-investment-strategy.html |  |
| kifrs | 일간NTN | 한국회계연구원(KARI) KARI Accounting and Sustainability Research Seminar... | http://www.intn.co.kr/news/articleView.html?idxno=2054166 |  |
| kifrs | hellot.net | [ESG 칼럼] 글로벌 기후 규제 장벽 도래와 생존을 위한 CBAM 검증 | https://www.hellot.net/news/article.html?no=115296 |  |
| kifrs | 한국경제 | KB증권, 온실가스 줄여야 자금 조달…지속가능채권 확대 | https://www.hankyung.com/article/2026100647061 |  |
| kifrs | ESG경제 | EU 역외 지속가능성 공시대상 국내기업 "20~30곳"...KSSB 공시 정보 활용... | https://www.esgeconomy.com/news/articleView.html?idxno=16805 |  |
| kifrs | tfmedia.co.kr | [KAI 세미나] 박상혁 의원 “한국 현실에 맞는 지속가능성 제도…국회서... | https://www.tfmedia.co.kr/news/article.html?no=206987 |  |
| kifrs | socialvalue.kr | [SV 리포트] 새 대표 맞은 사조오양, ESG 신뢰성 흔들…환경 공시·산업... | https://www.socialvalue.kr/news/view/1065575181336703 |  |
| kifrs | sateconomy.co.kr | ESG, 홍보에서 법정공시로 간다 | https://sateconomy.co.kr/news/view/1065591928361066 |  |
| kifrs | sidae.com | '신뢰 회복' 나선 코스닥…불성실 공시 제재 강화·컨설팅 확대 | https://www.sidae.com/article/2026070311190060233 |  |
| kifrs | niceeconomy.co.kr | [산업 브리핑] HD현대·한샘·NHN·한화비전 | http://www.niceeconomy.co.kr/news/articleView.html?idxno=90156 |  |
| kifrs | sateconomy.co.kr | 4대 금융지주, 지속가능경영보고서에 ‘생산적·포용금융’ 전면 배치 | https://sateconomy.co.kr/news/view/1065586856421098 |  |
| kifrs | tfmedia.co.kr | [이슈체크] ‘뚝 떨어진 영업권’…측정 단위 뭉쳐서 숨기기 수법 횡행 | https://www.tfmedia.co.kr/news/article.html?no=205405 |  |
| kifrs | theviewers.co.kr | [삼성생명 투자경보①] 시총 100조 터무니없다 | https://theviewers.co.kr/View.aspx?No=4120232 |  |
| kifrs | thevaluenews.co.kr | [더밸류 브리핑] 오늘의 증권 소식...NH투자·현대차·SK증권 | http://www.thevaluenews.co.kr/news/view.php?idx=199467 |  |
| kifrs | enewstoday.co.kr | SK증권, '2025 KSSB 제2호 파일럿 리포트' 발간 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2439947 |  |
| kifrs | goodkyung.com | [증권 이모저모] 미래에셋증권, 선물옵션 투자대회 연다 | https://www.goodkyung.com/news/articleView.html?idxno=288255 |  |
| kifrs | sateconomy.co.kr | SK증권, 기후공시 ‘파일럿 리포트’ 발간…금융배출량까지 선제 공개 | https://sateconomy.co.kr/news/view/1065600633318245 |  |
| kifrs | 이데일리 | SK증권, KSSB 제2호 준용 '기후공시 보고서' 발간 | https://www.edaily.co.kr/news/newspath.asp?newsid=05005286645482704 |  |
| kifrs | popcornnews.net | SK증권, KSSB 기준 맞춘 기후공시 보고서 발간 | http://www.popcornnews.net/news/articleView.html?idxno=124116 |  |
| kifrs | 파이낸셜뉴스 | SK증권, 기후공시 고도화...KSSB 제2호 기반 리포트 발간 | http://www.fnnews.com/news/202606171635479997 |  |
| kifrs | pointe.co.kr | SK증권, 국내 증권사 최초 KSSB 기후공시 파일럿 보고서 발간 | https://www.pointe.co.kr/news/articleView.html?idxno=80777 |  |
| kifrs | megaeconomy.co.kr | SK증권, KSSB 기후공시 보고서 발간…온실가스 배출 37% 감축 | https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065594274922849 |  |
| kifrs | cnbizm.com | SK증권, KSSB 제2호 기반 기후공시 보고서 발간 | https://www.cnbizm.com/news/articleView.html?idxno=305796 |  |
| kifrs | 일간NTN | 기후공시 적용사례 추가, 재무제표 불확실성 공시 사례 논의...시행은 언... | http://www.intn.co.kr/news/articleView.html?idxno=2051224 |  |
| kifrs | 임팩트온 | 【데일리 ESG정책 브리핑】기후리스크 회계공시 강화, AI 산사태 예측기... | http://www.impacton.net/news/articleView.html?idxno=19166 |  |
| kifrs | 조세일보 | 회계사회, ‘제23회 지속가능성인증포럼’ 성료 | http://www.joseilbo.com/news/news_read.php?uid=566229&class=10&grp= |  |
| kifrs | tfmedia.co.kr | 회계사회, 지속가능성 공시 로드맵 안 및 인증·감독 도입 논의 | https://www.tfmedia.co.kr/news/article.html?no=203545 |  |
| kifrs | biz.chosun.com | 한국공인회계사회, 제23회 지속가능성인증포럼 성료 | https://biz.chosun.com/stock/stock_general/2026/04/08/AOMNLETFCZB67P7GLENFAV22VM/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| kifrs | sejungilbo.com | 회계사회, '제23회 지속가능성인증포럼' 성료 | https://www.sejungilbo.com/news/articleView.html?idxno=57914 |  |
| kifrs | 일간NTN | 한국공인회계사회, '제23회 지속가능성인증포럼' 성료 | http://www.intn.co.kr/news/articleView.html?idxno=2050054 |  |
| kifrs | 한국세정신문 | 회계사회 지속가능성인증포럼 "재무정보 감독체계, 지속가능성정보 감... | https://www.taxtimes.co.kr/news/article.html?no=274640 |  |
| kifrs | inews24.com | [ESG NOW] 기후리스크, 이젠 법적 리스크 | http://www.inews24.com/view/1957134 |  |
| kifrs | ESG경제 | [정책브리핑] 산업부, '지속가능경영 종합시책' 발표…기업 ESG 지원 | https://www.esgeconomy.com/news/articleView.html?idxno=14934 |  |
| kifrs | businesspost.co.kr | [Who Is ?] 전필립 파라다이스그룹 회장 | https://www.businesspost.co.kr/BP?command=article_view&num=433782 |  |
| kifrs | dnews.co.kr | 엔츠, 탄소중립 솔루션 활용한 기후 공시 대응책 소개 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202603201431307190997 |  |
| kifrs | biz.heraldcorp.com | 엔츠, KSSB 시대 기업 대응 방향 모색 세미나 마련 | https://biz.heraldcorp.com/article/10699131?ref=naver |  |
| kifrs | biz.chosun.com | 엔츠, ‘KSSB 시대, 기후 공시 대응 전략 및 실행 인프라 구축’ 세미나... | https://biz.chosun.com/industry/business_info/2026/03/23/TRKL6S6Y35AG7MEQF46PHVMOYA/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| kifrs | datanet.co.kr | 엔츠, 오는 26일 'KSSB 최종안 대응 세미나' 개최 | https://www.datanet.co.kr/news/articleView.html?idxno=210280 |  |
| kifrs | epnc.co.kr | ﻿엔츠, 기후 공시 대비 실행 체계 및 데이터 관리 전략 제시 | https://www.epnc.co.kr/news/articleView.html?idxno=330199 |  |
| kifrs | itbiznews.com | ﻿엔츠, 탄소중립 솔루션 활용한 기후 공시 대응책 소개 | https://www.itbiznews.com/news/articleView.html?idxno=207351 |  |
| kifrs | ekn.kr | 엔츠, KSSB 기후 공시 대응 전략 세미나 26일 개최 | https://www.ekn.kr/web/view.php?key=20260320026359524 |  |
| kifrs | efnews.co.kr | 신한금융, SK하이닉스 등 5개 기업, 탄소경영 플래티넘 클럽 등극 | http://www.efnews.co.kr/news/articleView.html?idxno=128059 |  |
| kifrs | inews24.com | [ESG NOW] 새로운 경영의 '뉴노멀', ESG 공시 | http://www.inews24.com/view/1946717 |  |
| kifrs | hansbiz.co.kr | KSSB, 지속가능성 공시 기준 첫 번째 세트 의결·공표 | http://www.hansbiz.co.kr/news/articleView.html?idxno=821626 |  |
| kifrs | ESG경제 | 2026 CDP 코리아 컨퍼런스 개최...'기후변화와 기업·산업·금융의 전환... | https://www.esgeconomy.com/news/articleView.html?idxno=14561 |  |
| kifrs | electimes.com | "전환계획, 투자 가능하게"...'CDP 컨퍼런스' 3월 개최 | https://www.electimes.com/news/articleView.html?idxno=365363 |  |
| kifrs | energy-news.co.kr | 내달 10일 '2026 CDP Korea Conference' 열린다 | https://www.energy-news.co.kr/news/articleView.html?idxno=223029 |  |
| kifrs | efnews.co.kr | CDP 한국위원회, CDP 코리아 컨퍼런스 내달 10일 개최 | http://www.efnews.co.kr/news/articleView.html?idxno=127666 |  |
| kifrs | greened.kr | [증권사 ESG 구조진단] A+도 S도 없다…증권사 ESG, B·C등급 '우수수' - ... | https://www.greened.kr/news/articleView.html?idxno=335179 |  |
| kifrs | news2day.co.kr | [ESG경영 사례분석] 효성티앤씨, ‘주주가치 제고’로 종합등급 A로 상승... | https://www.news2day.co.kr/article/20251231500218 |  |
| kifrs | newspim.com | '삼성생명 일탈회계' 3년 논란 종결…국제 검증이 남긴 세 가지 의미 | https://www.newspim.com/news/view/20251212001056 |  |
| kifrs | 한국경제 | '자율' 스튜어드십코드, 10년만에 강제규범으로 바뀐다 | https://www.hankyung.com/article/2025121426201 |  |
| kifrs | tfmedia.co.kr | [이슈체크] 삼성생명 일탈회계, 용인 안 된다…국제회계기준 해석위, 사... | https://www.tfmedia.co.kr/news/article.html?no=198954 |  |
| kifrs | 조세일보 | IFRS IC “일탈회계, 극히 예외적…국제적으로 인정 받을 수 없어” | http://www.joseilbo.com/news/news_read.php?uid=558560&class=87&grp= |  |
| kifrs | opinionnews.co.kr | IFRS IC, 삼성생명 일탈회계 종지부…"일탈은 극히 예외적…회계, 개념 ... | http://www.opinionnews.co.kr/news/articleView.html?idxno=129238 |  |
| kifrs | 일간NTN | 국제회계기준 해석위원회 잠정결론, 일탈회계는 극히 예외적인 조항 | http://www.intn.co.kr/news/articleView.html?idxno=2047783 |  |
| kifrs | newstomato.com | IFRS 해석위원회, 삼성생명 일탈회계 논리 사실상 무력화 | http://www.newstomato.com/ReadNews.aspx?no=1284416&inflow=N |  |
| kifrs | upkoreanews.kr | 박지원 체제 두산에너빌리티, 실적 폭발 속 '지배구조 D등급'에 '지배구... | https://www.upkoreanews.kr/news/articleView.html?idxno=96307 |  |
| kifrs | siminilbo.co.kr | 풀무원, 한국ESG기준원(KCGS) 지배구조 최우수상 수상…ESG 통합 A+ 등급... | https://www.siminilbo.co.kr/news/newsview.php?ncode=1160274165238542 |  |
| kifrs | biztribune.co.kr | [브리프]SPC던킨 풀무원 정관장 대상 삼양식품 hy KT&G | http://www.biztribune.co.kr/news/articleView.html?idxno=344942 |  |
| kifrs | ngetnews.com | 풀무원, 한국ESG기준원 '지배구조 최우수상' 수상 | https://www.ngetnews.com/news/articleView.html?idxno=542710 |  |
| kifrs | 4th.kr | [브리핑] 이랜드월드  '스파오 크리에이터' 1기 모집 | http://www.4th.kr/news/articleView.html?idxno=2102206 |  |
| kifrs | newsmaker.or.kr | 풀무원, 한국ESG기준원 지배구조 최우수상 수상 | http://www.newsmaker.or.kr/news/articleView.html?idxno=171972 |  |
| kifrs | ibabynews.com | [ESG 트렌드] 풀무원, 한국ESG기준원(KCGS) 지배구조 최우수상 수상…ESG... | https://www.ibabynews.com/news/articleView.html?idxno=144228 |  |
| kifrs | sisacast.kr | 풀무원, '한국ESG기준원(KCGS) 지배구조 최우수상' 수상 | http://www.sisacast.kr/news/articleView.html?idxno=87579 |  |
| kifrs | fetv.co.kr | 풀무원, 한국ESG기준원 '지배구조 최우수상 수상' | https://www.fetv.co.kr/news/article.html?no=207146 |  |
| kifrs | industrynews.co.kr | 풀무원, 한국ESG기준원 지배구조 최우수상 수상…ESG 통합 A+ 등급 획득 | https://www.industrynews.co.kr/news/articleView.html?idxno=75237 |  |
| kifrs | updownnews.co.kr | 풀무원, 한국ESG기준원 지배구조 최우수상...ESG 통합 A+ 등급 | http://www.updownnews.co.kr/news/articleView.html?idxno=315309 |  |
| kifrs | thefirstmedia.net | 풀무원, '2025년 한국ESG기준원 우수기업 시상식'서 지배구조 부문 최우... | http://www.thefirstmedia.net/news/articleView.html?idxno=188072 |  |
| kifrs | newspost.kr | 풀무원, 한국ESG기준원 지배구조 최우수상 수상…ESG 통합 A+ 등급 | https://www.newspost.kr/news/articleView.html?idxno=219240 |  |
| kifrs | s-journal.co.kr | 풀무원, '2025 한국ESG기준원 우수기업 시상식'서 지배구조 부문 최우수... | https://www.s-journal.co.kr/news/articleView.html?idxno=36364 |  |
| kifrs | ezyeconomy.com | 풀무원, 한국ESG기준원 지배구조 최우수상 수상…805개 평가 대상 중 최... | https://www.ezyeconomy.com/news/articleView.html?idxno=227483 |  |
| kifrs | newsworks.co.kr | 풀무원, KCGS '지배구조 최우수상' 수상…ESG 통합 A+ 획득 | https://www.newsworks.co.kr/news/articleView.html?idxno=821857 |  |
| kifrs | daily.hankooki.com | 풀무원, 한국ESG기준원 지배구조 최우수상 수상 | https://daily.hankooki.com/news/articleView.html?idxno=1305939 |  |
| kifrs | queen.co.kr | 풀무원, 한국ESG기준원(KCGS) 지배구조 최우수상 수상… ESG 전 영역에서... | http://www.queen.co.kr/news/articleView.html?idxno=447181 |  |
| kifrs | greened.kr | [유통가 레이더] 슈뢰더 전 독일 총리 부부가 콜마를 찾은 이유는... 윤... | https://www.greened.kr/news/articleView.html?idxno=333890 |  |
| kifrs | globalepic.co.kr | 풀무원, 한국ESG기준원(KCGS) 지배구조 최우수상 수상…ESG 통합 A+ 등급... | http://www.globalepic.co.kr/view.php?ud=20251205103151968948439a4874_29 |  |
| kifrs | newsdream.kr | 풀무원, 한국ESG기준원 지배구조 최우수상 수상…ESG 통합 A+ 등급 획득 | http://www.newsdream.kr/news/articleView.html?idxno=102281 |  |
| kifrs | inews24.com | 풀무원, 한국ESG기준원 지배구조 최우수상 수상 | http://www.inews24.com/view/1914549 |  |
| kifrs | marketnews.co.kr | 풀무원, 한국ESG기준원(KCGS) 지배구조 최우수상 수상…ESG 통합 A+ 등급... | http://www.marketnews.co.kr/news/articleView.html?idxno=73428 |  |
| kifrs | dailian.co.kr | 풀무원, 한국ESG기준원 지배구조 최우수상 수상 | https://www.dailian.co.kr/news/view/1582517/?sc=Naver |  |
| kifrs | joongangenews.com | 풀무원, KCGS 지배구조 부문 '최우수상'… ESG 대표 기업 입지 강화 | https://www.joongangenews.com/news/articleView.html?idxno=472397 |  |
| kifrs | gokorea.kr | 풀무원, 한국ESG기준원(KCGS) 지배구조 최우수상 수상…ESG 통합 A+ 등급... | https://www.gokorea.kr/news/articleView.html?idxno=849229 |  |
| kifrs | businessplus.kr | 풀무원, KCGS 지배구조 최우수상 수상…ESG 통합 A+ 등급 획득 | https://www.businessplus.kr/news/articleView.html?idxno=103602 |  |
| kifrs | womentimes.co.kr | 풀무원, KCGS 지배구조 최우수상 수상...ESG 통합 A+ 등급 | http://www.womentimes.co.kr/news/articleView.html?idxno=92981 |  |
| kifrs | handmk.com | 풀무원, KCGS 지배구조 최우수상…ESG 통합 A+ 등급 획득 | https://www.handmk.com/news/articleView.html?idxno=34544 |  |
| kifrs | srtimes.kr | 풀무원, 한국ESG기준원 지배구조 최우수상 수상…ESG 통합 A+ 등급 획득 | http://www.srtimes.kr/news/articleView.html?idxno=191457 |  |
| kifrs | bosa.co.kr | ESG '지배구조' 최우수상 수상 | http://www.bosa.co.kr/news/articleView.html?idxno=2264706 |  |
| kifrs | theviewers.co.kr | 풀무원, KCGS 지배구조 최우수상 수상…ESG 통합 A+ 획득 | http://theviewers.co.kr/View.aspx?No=3881573 |  |
| kifrs | thefairnews.co.kr | 풀무원, ESG 대표기업 위상 입증 | https://www.thefairnews.co.kr/news/articleView.html?idxno=62401 |  |
| kifrs | biz.heraldcorp.com | 금감원 “손해율·사업비 가정 여전히 미흡”…전 보험사 11월말까지 개... | https://biz.heraldcorp.com/article/10919489?ref=naver |  |
| kifrs | etnews.com | 금감원, 보험사 계리가정 관리 강화…내년부터 CSM 상시감시 | https://www.etnews.com/20261029000067 |  |
| kifrs | insnews.co.kr | 금감원, 보험사 계리가정 관리 강화… 연말 '집중 점검' 예고 | https://www.insnews.co.kr/news/articleView.html?idxno=93587 |  |
| kifrs | delighti.co.kr | 금감원·거래소 회계사 채용 3.4배 급증…미지정 회계사 유입 주목 | https://www.delighti.co.kr/news/articleView.html?idxno=123817 |  |
| kifrs | biz.sbs.co.kr | 금감원·거래소 회계사 채용 3배↑…신입 3명 중 1명 회계사 | https://biz.sbs.co.kr/article_hub/20000342029?division=NAVER |  |
| kifrs | 조세일보 | 기회·함정이 도사린 ‘대도시·정치권’에서 이익·권력·책임을 분별... | http://www.joseilbo.com/news/news_read.php?uid=578104&class=75&grp= |  |
| kifrs | yna.co.kr | 금감원·거래소 회계사 채용 3배↑…미지정 회계사 '흡수처' 부상 | https://www.yna.co.kr/view/AKR20261022146000008?input=1195m |  |
| kifrs | 매일경제 | 렌터카 하루 120만원·통역 160만원…산단 국비 막 쓰는데 회계검토 ‘이... | https://www.mk.co.kr/article/12182721 |  |
| kifrs | imaeil.com | 개인돈 6.3조 삭제됐는데…레버리지 ETF 책임 놓고 당국은 '집안싸움' | https://www.imaeil.com/page/view/2026102210245526847 |  |
| kifrs | mhns.co.kr | 임문영의원 국비 금지 설계·감리비 7억6천만원, 연구활동비로 집행 부... | https://www.mhns.co.kr/news/articleView.html?idxno=765435 |  |
| kifrs | kmib.co.kr | 특사경 갈등 봉합하자 이번엔 레버리지 ETF…금융위·금감원 ‘2차전’... | https://www.kmib.co.kr/article/20261021500570 |  |
| kifrs | 파이낸셜뉴스 | 감사보수 덤핑 '제동'… 한공회, 금감원에 감리 요청 검토 | https://www.fnnews.com/news/202610201818255206 |  |
| kifrs | kyongbuk.co.kr | 한국사학진흥재단, 감사 품질 높인다…지정외부감사 첫 대면 연수 | https://www.kyongbuk.co.kr/news/articleView.html?idxno=4087876 |  |
| kifrs | dkilbo.com | 한국사학진흥재단, '지정외부감사 품질제고를 위한 사학기관 업무 역량... | https://www.dkilbo.com/news/articleView.html?idxno=557841 |  |
| kifrs | 파이낸셜뉴스 | [단독] 감사보수 '덤핑 경쟁'에 칼 빼든 한공회…금감원 특별감리 요청... | https://www.fnnews.com/news/202610201417567368 |  |
| kifrs | breaknews.com | 한국사학진흥재단, 사학기관 회계 실무자 100여 명 대상 역량 강화 연수 | http://www.breaknews.com/1244183 |  |
| kifrs | news.unn.net | 한국사학진흥재단, 사학기관 담당자 첫 대면 연수 개최 | https://news.unn.net/news/articleView.html?idxno=598905 |  |
| kifrs | view.asiae.co.kr | [단독]5년전보다 적은 감사보수…회계법인 빅4 덤핑 심해졌다 | https://view.asiae.co.kr/article/2026101915420950168 |  |
| kifrs | newsverse.kr | [오늘의 경제뉴스] 중앙그룹 '회계부정' 의혹 확산…중앙그룹 4개사 금... | https://www.newsverse.kr/news/articleView.html?idxno=11708 |  |
| kifrs | etoday.co.kr | 금감원·국책은행 지방이전 '산 넘어 산'…법 개정에 인력 이탈까지 [금... | https://www.etoday.co.kr/news/view/2636981 |  |
| kifrs | naeil.com | 회계규제는 중복, 감사는 빈틈…회계기본법 제정 목소리 커져 | https://www.naeil.com/news/read/605290?ref=naver |  |
| kifrs | woodkorea.co.kr | 목조건축, '친환경' 넘어 산업·금융·탄소자산으로…현실의 병목을 짚... | https://www.woodkorea.co.kr/news/articleView.html?idxno=91669 |  |
| kifrs | investchosun.com | [Invest]회계법인, 벌써 내년 감사 경쟁 치열...LG전자·삼성SDI 등 '자유... | https://www.investchosun.com/site/data/html_dir/2026/10/01/2026100180212.html |  |
| kifrs | greened.kr | 유효기간 지난 의약품도 재고로…제약업계 재고자산 회계 관행 '경고등... | https://www.greened.kr/news/articleView.html?idxno=351147 |  |
| kifrs | 조세일보 | [진단] 제각각 회계기준, '회계기본법'으로 통일되나 | http://www.joseilbo.com/news/news_read.php?uid=576635&class=10&grp= |  |
| kifrs | businesspost.co.kr | [Who Is ?] 이강석 대우건설 대표이사 | https://www.businesspost.co.kr/BP?command=article_view&num=448232 |  |
| kifrs | newsway.co.kr | 해외 진출 확대하는 K바이오…계약금·마일스톤 '매출 인식' 주의보 | https://www.newsway.co.kr/news/view?ud=2026093018141769685 |  |
| kifrs | gokorea.kr | 아파트 회계감사 재검증법 국회 발의 | https://www.gokorea.kr/news/articleView.html?idxno=879012 |  |
| kifrs | thepowernews.co.kr | 해태제과, 매출·매출원가 4년간 530억 과대계상…감사인지정 3년 | https://www.thepowernews.co.kr/view.php?ud=202609171445575731de3f0aa1be_7 |  |
| kifrs | kjdaily.com | “예산 세워놓고 반납”…광주·전남 재정운용 곳곳 ‘허점’ | http://www.kjdaily.com/article.php?aid=1789384598686852002 |  |
| kifrs | jndn.com | 광주 ‘선 예산·후 절차’…전남 ‘연말 몰아치기’ 관행 도마 | http://www.jndn.com/article.php?aid=1789379724439623001 |  |
| kifrs | newsis.com | 광주·전남 예산 이월 '고질병'…통합시 재정혁신 시험대 | https://www.newsis.com/view/NISX20260914_0003788087 |  |
| kifrs | naeil.com | ‘감사인 지정제' 확산에 9년…부처 칸막이에 회계개혁 속도 더뎌 | https://www.naeil.com/news/read/601759?ref=naver |  |
| kifrs | news1.kr | 이찬진, 런던서 글로벌 투자자 유치…"한국 장기투자 기반 강화" | https://www.news1.kr/finance/financial-policy/6286022 |  |
| kifrs | pointe.co.kr | 경남도의회, 2025회계연도 결산 심사 집중…교육·복지·의료 등 도정 전... | https://www.pointe.co.kr/news/articleView.html?idxno=84516 |  |
| kifrs | 한국경제 | "회계기본법, 투명성 넘어 정보 연결의 공통 인프라 돼야" | https://www.hankyung.com/article/202609093843r |  |
| kifrs | aflnews.co.kr | 아산시의회 기획행정농업위, 재해복구·전통시장·행정 실효성 점검 | https://www.aflnews.co.kr/news/articleView.html?idxno=327776 |  |
| kifrs | ccdn.co.kr | 전남수 충남 아산시의원, 재해복구사업 '서류 넘어 현장까지' 꼼꼼 점검 | https://www.ccdn.co.kr/news/articleView.html?idxno=1098416 |  |
| kifrs | kukinews.com | 경남도의회, 교복 지원부터 농정·교통·투자까지 현안 집중 점검 | https://www.kukinews.com/article/view/kuk202609080189 |  |
| kifrs | newstnt.com | 전남수 아산시의원, 유휴자금 관리 성과 적극행정 발굴 주문 | https://www.newstnt.com/news/articleView.html?idxno=717264 |  |
| kifrs | daily.hankooki.com | [아산시의회소식] 전남수 의원, 재해복구사업 '서류 넘어 현장까지' 꼼... | https://daily.hankooki.com/news/articleView.html?idxno=1403798 |  |
| kifrs | ccdailynews.com | 아산시의회 전남수 의원,수의계약과 재해복구사업 집중점검 | https://www.ccdailynews.com/news/articleView.html?idxno=2439228 |  |
| kifrs | m-i.kr | 전남수 아산시의원, 유휴자금 성과 포상·재해복구 현장 점검 주문 | https://www.m-i.kr/news/articleView.html?idxno=1411158 |  |
| kifrs | 조세일보 | 안진, 매출 4845억원…전년比 229억 감소 [2026년 회계법인 실적분석] | http://www.joseilbo.com/news/news_read.php?uid=575250&class=10&grp= |  |
| kifrs | hani.co.kr | ‘경영권 경쟁’ 고려아연, ‘거수기 감사위원’ 탈피에 성공할까? | https://www.hani.co.kr/arti/economy/economy_general/1276455.html |  |
| kifrs | news1.kr | 677억 부당 수의계약하고 총장 직무대행 부적정 지정한 사학법인 | https://www.news1.kr/society/education/6280520 |  |
| kifrs | newsis.com | 자녀 수강시키고 A+…'엄마 찬스' 대학교수 감사 적발 | https://www.newsis.com/view/NISX20260904_0003776886 |  |
| kifrs | naeil.com | 영풍 충당부채 3건 ‘고의’ 판단…내부통제 쟁점으로 | https://www.naeil.com/news/read/601202?ref=naver |  |
| kifrs | goodkyung.com | 낙동강 환경피해 주민 대표, 검찰 고발인 조사..."환경오염 은폐, 영풍 ... | https://www.goodkyung.com/news/articleView.html?idxno=290905 |  |
| kifrs | news1.kr | 韓기업 해외 수주전 달라진다…亞개발은행 "기술·친환경도 평가" | https://www.news1.kr/economy/trend/6277822 |  |
| kifrs | newsway.co.kr | 영풍 석포제련소 주민대책위 "압수수색 등 강제수사해야" | https://www.newsway.co.kr/news/view?ud=2026090216110261202 |  |
| kifrs | fntimes.com | 낙동강 주민들 "검찰, 영풍 조직적 회계분식·감사방해 행위 강제수사 ... | https://www.fntimes.com/html/view.php?ud=2026090216224214787de3572ddd_18 |  |
| kifrs | starnewskorea.com | "검찰, 영풍 조직적 회계분식·감사방해 행위 실체규명 위해 강제수사 ... | https://www.starnewskorea.com/business-life/2026/09/02/2026090215593546991 |  |
| kifrs | thescoop.co.kr | 어느 펀드서 벌어진 일…고려아연 최 회장 일가는 왜 '터널'에 빠졌나 | https://www.thescoop.co.kr/news/articleView.html?idxno=311459 |  |
| kifrs | tfmedia.co.kr | 인천세무사회, ‘2026년 회직자 워크숍’성료...소통과 화합의 장 마련 | https://www.tfmedia.co.kr/news/article.html?no=206824 |  |
| kifrs | 일간NTN | 인천지방세무사회, '2026년 회직자 워크숍' 성료…추진 과제 점검 | http://www.intn.co.kr/news/articleView.html?idxno=2052888 |  |
| kifrs | asiatime.co.kr | 영풍·MBK, 한화·LG화학에 박유경 지지 요청…"감사위 정상화 분기점" | https://www.asiatime.co.kr/article/20260828500273 |  |
| kifrs | 한국세정신문 | 인천지방세무사회 회직자 워크숍 "신축회관, 교육환경·편의시설 더욱 ... | https://www.taxtimes.co.kr/news/article.html?no=276565 |  |
| kifrs | greened.kr | 금감원 경력채용도 미달…해외 감독기관은 전문직에 최대 4억원 보수 | https://www.greened.kr/news/articleView.html?idxno=348581 |  |
| kifrs | 한국경제 | 고려아연 임시주총 앞두고 배임 의혹 재점화…금감원·증선위 엇갈린 이... | https://www.hankyung.com/article/202608263655r |  |
| kifrs | dailian.co.kr | 영풍·MBK "최윤범 투자기업에 후속투자"…고려아연 "근거 없는 의혹" | https://www.dailian.co.kr/news/view/1682770/?sc=Naver |  |
| kifrs | mydaily.co.kr | 임시주총 앞두고 ‘원아시아 투자’ 재점화…고려아연·영풍 공방 격돌 | https://www.mydaily.co.kr/page/view/2026082610072151064 |  |
| kifrs | dailybrief.co.kr | [롯데카드 점검④] 대주주 여신심사-감리-조기경보-공시 '구멍' | https://www.dailybrief.co.kr/news/articleView.html?idxno=6590 |  |
| kifrs | asiatime.co.kr | MBK·영풍 "최윤범 일가 선투자 기업에 회사 자금"…고려아연 "명예훼손... | https://www.asiatime.co.kr/article/20260825500485 |  |
| kifrs | news.bizwatch.co.kr | 고려아연 "MBK·영풍, 원아시아 관련 주장 일방적…법적 대응" | https://news.bizwatch.co.kr/article/industry/2026/08/25/0044 |  |
| kifrs | kyongbuk.co.kr | 대학 재정부터 'AI 행정'까지…한국사학진흥재단, 혁신사례 찾는다 | https://www.kyongbuk.co.kr/news/articleView.html?idxno=4081970 |  |
| kifrs | ppss.kr | "주총자료가 거짓" vs "공개자료 근거"…고려아연·영풍·MBK 정면충돌 | https://www.ppss.kr/news/articleView.html?idxno=306577 |  |
| kifrs | thebell.co.kr | [더벨][thebell interview] 최종길 한국종합기술 이사 "배 망칠 공약엔 표... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202608141509212520108616 |  |
| kifrs | 일간NTN | "실제 사주 횡령 자금공백 숨기려 자산 허위계상…자기자본 과대계상" ... | http://www.intn.co.kr/news/articleView.html?idxno=2052633 |  |
| kifrs | srtimes.kr | 소비자보호는 채웠다…이찬진 금감원장 1년, 자본시장 과열은 과제 | http://www.srtimes.kr/news/articleView.html?idxno=210098 |  |
| kifrs | inews24.com | 이찬진 금감원장 1년…AI로 주가조작 잡고 운용사 주주권 강화 | http://www.inews24.com/view/1994811 |  |
| kifrs | 서울경제 | 금감원, 내년부터 감리부서 2→4개…전담 인력도 90명까지 확대 | https://www.sedaily.com/article/20078270?ref=naver |  |
| kifrs | 일간NTN | "공동기업 재무제표 오류 반드시 검토해야"…지분법 평가 오류 사례 공... | http://www.intn.co.kr/news/articleView.html?idxno=2052465 |  |
| kifrs | inews24.com | 안성시의회, 제243회 임시회 개회…추경안 등 심의 | http://www.inews24.com/view/1992704 |  |
| kifrs | thepublic.kr | AI로 생산현장 바꾼다…중소 제조기업 48개 과제 상용화 추진 | https://www.thepublic.kr/news/articleView.html?idxno=313779 |  |
| kifrs | apnews.kr | '역대 최대 과징금' 영풍…당국과 '석포제련소 정화비' 법정 공방 | https://www.apnews.kr/news/articleView.html?idxno=3050212 |  |
| kifrs | newsway.co.kr | '고의 회계부정' 판단에 법정 간 영풍…환경 책임 회피 논란까지 | https://www.newsway.co.kr/news/view?ud=2026080109080295630 |  |
| kifrs | newstomato.com | (단독)한공회, 'CB 뻥튀기' 논란 평가모형 한계 인정…당국 방관 속 장부... | http://www.newstomato.com/ReadNews.aspx?no=1308842&inflow=N |  |
| kifrs | 일간NTN | "회계정책 변경 땐 지분법 재점검해야"…관계기업 투자주식 과소계상 지... | http://www.intn.co.kr/news/articleView.html?idxno=2052279 |  |
| kifrs | 일간NTN | "유상사급재 통제권 없으면 재고자산 인식 안 돼"…매출 총액계상 주의 | http://www.intn.co.kr/news/articleView.html?idxno=2052249 |  |
| kifrs | s-journal.co.kr | 국내서 204억 과징금 받은 영풍, 美선 "세계적 친환경 제련소"로 소개 | https://www.s-journal.co.kr/news/articleView.html?idxno=42708 |  |
| kifrs | s-journal.co.kr | 환경정화 충당부채 과소계상 영풍에 204억 과징금… 美선 석포제련소 '... | https://www.s-journal.co.kr/news/articleView.html?idxno=42637 |  |
| kifrs | sports.donga.com | 환경법 위반 지적 영풍 석포제련소, 미국에선 ‘세계적 친환경 제련소’... | https://sports.donga.com/economy/article/all/20260724/134360444/1 |  |
| kifrs | fntimes.com | 영풍 제련소 미국 현지 홍보에...고려아연 "사전 협의, 기술 연관성 없... | https://www.fntimes.com/html/view.php?ud=2026072417030413287de3572ddd_18 |  |
| kifrs | sentv.co.kr | 국정감사 “영풍, 환경 관련 법 위반 103건”…미국서는 ‘세계적 친환... | https://www.sentv.co.kr/article/view/sentv202607240167 |  |
| kifrs | sidae.com | 대형회계법인 전유물 '대형상장사 지정', 중견회계법인도 가능해진다 | https://www.sidae.com/article/2026072316472439821 |  |
| kifrs | nocutnews.co.kr | "34억이 있었나?"…전남테크노파크, 계좌 잔액도 몰랐다 | https://www.nocutnews.co.kr/news/6552188?utm_source=naver&utm_medium=article&utm_campaign=20260724053210 |  |
| kifrs | asiatime.co.kr | [증권 뉴스브리핑] 증선위, 덱스터스튜디오 감사인지정/상반기, 주식매... | https://www.asiatime.co.kr/article/20260722500483 |  |
| kifrs | news1.kr | 대전시의회 "하수슬러지 감량화 시설 면피성 소송에 90억 혈세 낭비" | https://www.news1.kr/local/daejeon-chungnam/6234265 |  |
| kifrs | news.mtn.co.kr | "주가조작해도 남는 장사" 인식 뿌리 뽑아야…처벌 강화·신속 적발 필요 | https://news.mtn.co.kr/news-detail/2026071417355838060 |  |
| kifrs | job-post.co.kr | 강남구, 장애인복지시설 회계·운영 지적사항 19.2% 감소…73개소 점검 | https://www.job-post.co.kr/news/articleView.html?idxno=235418 |  |
| kifrs | thefairnews.co.kr | "복잡한 연금 업무 손쉽게"…NH농협은행, '알기쉬운 퇴직연금' 2026년 개... | https://www.thefairnews.co.kr/news/articleView.html?idxno=92280 |  |
| kifrs | 임팩트온 | EU 환경규제 대응 수준, 기업 인수가격에도 영향…M&A 실사 5대 항목 | https://www.impacton.net/news/articleView.html?idxno=30404 |  |
| kifrs | gndomin.com | 창원시, 공동주택 입주자대표회의 운영·윤리 교육 실시 | http://www.gndomin.com/news/articleView.html?idxno=494080 |  |
| kifrs | newsgn.com | 창원특례시, 공동주택 입주자대표회의 운영 교육 실시 | https://www.newsgn.com/news/articleView.html?idxno=581054 |  |
| kifrs | geconomy.co.kr | [구리시 행정의 민낯①] 이도환 대변인 업무추진비·법인카드 내역 ‘부... | https://www.geconomy.co.kr/news/article.html?no=324777 |  |
| kifrs | m.skyedaily.com | 폴리텍大, 직업훈련 예산으로 기념품 잔치… 텀블러·전동그라인더 사재... | https://m.skyedaily.com/news_view.html?ID=313436 |  |
| kifrs | gukjenews.com | 영도구, 공동주택 관계자 90여 명 대상 관리 역량 강화 교육 | https://www.gukjenews.com/news/articleView.html?idxno=3730775 |  |
| kifrs | tfmedia.co.kr | [이슈체크] 폴리텍대 '기가찬 돈 씀씀이'...취약층 훈련 예산 홍보비로... | https://www.tfmedia.co.kr/news/article.html?no=208290 |  |
| kifrs | biz.newdaily.co.kr | 취약계층 훈련 예산으로 텀블러·그라인더 샀다 … 폴리텍대 '기막힌 예... | https://biz.newdaily.co.kr/site/data/html/2026/10/23/2026102300034.html |  |
| kifrs | yna.co.kr | 폴리텍대, 직업훈련 예산으로 홍보비 펑펑…텀블러 등 사재기도 | https://www.yna.co.kr/view/AKR20261022160400530?input=1195m |  |
| kifrs | ceoscoredaily.com | [2026 금융포럼] 스테이블코인·STO가 바꿀 금융…“발행 넘어 결제·유... | https://www.ceoscoredaily.com/page/view/2026102116361896481 |  |
| kifrs | newsgn.com | 김영규 거제시의원, "경로당 지원, 숫자가 아닌 어르신들의 생활 기준으... | https://www.newsgn.com/news/articleView.html?idxno=580149 |  |
| kifrs | h21.hani.co.kr | [단독] ‘소보수 집행’ 조항의 역설, 최근 5년간 미공시 ‘깜깜이’ 계... | https://h21.hani.co.kr/arti/society/society_general/60050.html |  |
| kifrs | newsfreezone.co.kr | 거제시의회, 쾌적한 경로당∙투명한 행정∙실효성 있는 복지...'현장 중... | https://www.newsfreezone.co.kr/news/articleView.html?idxno=714804 |  |
| kifrs | ftoday.co.kr | 보험 수수료 분급제 두 달 앞으로…설계사 소득 비상 | http://www.ftoday.co.kr/news/articleView.html?idxno=367612 |  |
| kifrs | metroseoul.co.kr | 울진군, 복지의 신뢰는 투명한 회계에서…부적정 집행 예방 나서 | http://www.metroseoul.co.kr/article/20261016500291 |  |
| kifrs | vegannews.co.kr | 현금주의와 발생주의, 거래 기록 시점은 다르다 | https://www.vegannews.co.kr/news/article.html?no=394286 |  |
| kifrs | kmecnews.co.kr | [궁금한 건설세무 Q&A] (27) 자재 매입세금계산서를 꼭 받아야 하나요? | https://www.kmecnews.co.kr/news/articleView.html?idxno=52294 |  |
| kifrs | goodmorningcc.com | 충남도의회 "주민자치회, 일할 사람과 재정 뒷받침돼야" | https://www.goodmorningcc.com/news/articleView.html?idxno=453915 |  |
| kifrs | queen.co.kr | 한은, 직원에 최대 5000만원 주택자금 저리 대출 … 신현송 "존치 필요성... | http://www.queen.co.kr/news/articleView.html?idxno=464535 |  |
| kifrs | news1.kr | 한은, 직원에 최대 5000만원 저리 주택대출…신현송 "제도 재검토" | https://www.news1.kr/economy/trend/6316790 |  |
| kifrs | shinailbo.co.kr | 서대문구, 어린이집 정기점검 전 예방 컨설팅 도입…운영 오류 사전 예... | https://www.shinailbo.co.kr/news/articleView.html?idxno=5070186 |  |
| kifrs | cnbizm.com | 서대문구, 관내 가정어린이집 26개소와 직장어린이집 6개소 등 총 32개소... | https://www.cnbizm.com/news/articleView.html?idxno=317565 |  |
| kifrs | ohmynews.com | 7명분인데 18명, 10명분인데 25명... 조희대 업추비 자료의 '이상한 인원... | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003273566&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| kifrs | dream.kotra.or.kr | 말레이시아, 그룹 내 대여금 이전가격 가이드라인 신설…본사-현지법인... | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=100&CONTENTS_NO=1&bbsGbn=322&bbsSn=322&pNttSn=244477 |  |
| kifrs | gukjenews.com | 충주교육청, 3분기 '청렴인' 친절직원' 선정 | https://www.gukjenews.com/news/articleView.html?idxno=3713821 |  |
| kifrs | koreadaily.com | 하루 한 명꼴 시민권 박탈 소송…42일간 40명 무더기 피소 | https://www.koreadaily.com/article/20261005200821585 |  |
| kifrs | 매일경제 | 김승원 '회계 의혹'도 접수…중수청 첫 날 고소·고발 '우수수' | http://mbn.mk.co.kr/pages/news/newsView.php?category=mbn00009&news_seq_no=5222745 |  |
| kifrs | newsis.com | 중수청 개청 5시간 기준 고소·고발 26건…'검경 불복' 다수(종합) | https://www.newsis.com/view/NISX20261002_0003812936 |  |
| kifrs | newsis.com | 중수청 첫날부터 고소·고발 줄이어…수원에 '김승원 회계 의혹' 접수 | https://www.newsis.com/view/NISX20261002_0003812577 |  |
| kifrs | wowtv.co.kr | ‘저PBR 탈출’ 첫 약속 나왔다…공표 가르는 잣대는 | http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202610020051&t=NN |  |
| kifrs | ekn.kr | 최혁진 의원, 원주 현안 잇단 직접 행보…단구지구 개발·단계동 주민자... | https://www.ekn.kr/web/view.php?key=20261001029240967 |  |
| kifrs | lecturernews.com | 교육부, 지방교육행·재정통합시스템 'K-에듀파인' 국제표준 인증 획득 | https://www.lecturernews.com/news/articleView.html?idxno=211255 |  |
| kifrs | news.ifm.kr | "경기도민 생명 지키는 공공의료원, 빚내서 버틴다" | https://news.ifm.kr/news/articleView.html?idxno=480437 |  |
| kifrs | newspim.com | 박균택 의원 "조희대, 헌법 부정에 예산 지침 위반까지…탄핵 사유 충분... | https://www.newspim.com/news/view/20260929000225 |  |
| kifrs | enewstoday.co.kr | [디-테일] BGF의 복잡한 셈법···②248억 '웃돈' 준 계열사 인수, 회계... | http://www.enewstoday.co.kr/news/articleView.html?idxno=2474610 |  |
| kifrs | gosiweek.com | 학교 행정시스템 장애 줄이고 대응 빨라진다…‘K-에듀파인’, 국내 첫... | https://www.gosiweek.com/article/1065591065761020 |  |
| kifrs | news.unn.net | 지방교육행·재정통합시스템 'K-에듀파인', 국제표준 인증 획득 | https://news.unn.net/news/articleView.html?idxno=597944 |  |
| kifrs | newsis.com | 전국 첫 교육통합 쏘아 올린 ‘전남광주’…재정·인력·권한 특례 필요 | https://www.newsis.com/view/NISX20260922_0003800247 |  |
| kifrs | newsworker.co.kr | 세종시교육청, 20여 명 실무자 모여 세출예산 집행 및 에너지절약 연수 | https://www.newsworker.co.kr/news/articleView.html?idxno=505175 |  |
| kifrs | newsdream.kr | [대명화학 X-ray⑤] 모다이노칩, 로젠과 합병 결의後 차입금 500억 늘려 | http://www.newsdream.kr/news/articleView.html?idxno=118526 |  |
| kifrs | 한국경제 | 조합원에 15억원대 기프트카드…경기지역 농협 조합장·상임이사 피소 | https://www.hankyung.com/article/202609172303h |  |
| kifrs | 매일경제 | 조합원 1717명에 15억원대 기프트카드…경기지역 농협 조합장 등 경찰 수... | https://www.mk.co.kr/article/12155546 |  |
| kifrs | 머니투데이 | 15억 '무기명 카드' 조합원에 펑펑…경찰, 농협 조합장 수사 | https://www.mt.co.kr/policy/2026/09/17/2026091713291684937 |  |
| kifrs | kmib.co.kr | 조합원에 기프트카드 지급…농협 조합장·상임이사 경찰 수사 | https://www.kmib.co.kr/article/view.asp?arcid=9000012977&cp=nv |  |
| kifrs | news1.kr | 대구교육청, 사립유치원 173곳 회계·인사 개선…공공성·투명성 강화 | https://www.news1.kr/local/daegu-gyeongbuk/6292939 |  |
| kifrs | 조세일보 | '감사'가 '검사'보다 우월하다는 착각 [기고] | http://www.joseilbo.com/news/news_read.php?uid=575807&class=10&grp= |  |
| kifrs | kbsm.net | 대구교육청, 사립유치원 173곳 회계·인사 전반 관리 강화 | https://www.kbsm.net/news/view.php?idx=534439 |  |
| kifrs | newsroad.co.kr | [기자수첩] 장부에 남은 손실, 성과급 계산에서는 빠졌다… BIS가 짚은 ... | http://www.newsroad.co.kr/news/articleView.html?idxno=64385 |  |
| kifrs | news1.kr | 금양 주주연대 "몽골 광산 손상차손 소급 적용 부당…당국 재검토 촉구... | https://www.news1.kr/local/busan-gyeongnam/6291339 |  |
| kifrs | thebk.co.kr | '회계 부정' 인근 지자체 발칵 뒤집힐 때… 경산시, 1만5000건 현미경 조... | https://www.thebk.co.kr/news/articleView.html?idxno=311681 |  |
| kifrs | kyongbuk.co.kr | 경산시, 23개 기관 공금 점검…횡령·회계부정 미적발 | https://www.kyongbuk.co.kr/news/articleView.html?idxno=4084261 |  |
| kifrs | newsworker.co.kr | 순천시의회, '재정 누수 차단'... 2025 결산안 현미경 심사 | https://www.newsworker.co.kr/news/articleView.html?idxno=504055 |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 | https://news.kbs.co.kr/news/pc/view/view.do?ncd=8661039&ref=A |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 | https://news.kbs.co.kr/news/pc/view/view.do?ncd=8660607&ref=A |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 | https://news.kbs.co.kr/news/pc/view/view.do?ncd=8660284&ref=A |  |
| kifrs | joongang.co.kr | [더버터] 디지털자산 기부가 바꾸는 비영리의 미래 | https://www.joongang.co.kr/article/25460614 |  |
| kifrs | namdonews.com | 광양시, 신규 공무원 업무 가이드북 선봬 | https://www.namdonews.com/news/articleView.html?idxno=922805 |  |
| kifrs | newsworker.co.kr | 광양시, '6개 분야 37개 항목'... 신규 공무원 실무 길라잡이 제작 | https://www.newsworker.co.kr/news/articleView.html?idxno=503454 |  |
| kifrs | theviewers.co.kr | [고려아연 임시주총-上] 전문성 vs 독립성…감사위원, 일반주주가 가른... | https://theviewers.co.kr/View.aspx?No=4208321 |  |
| kifrs | 머니투데이 | 공시 쏟아지는데 중요 숫자는 숨바꼭질…한국도 '공시 다이어트' 나설 ... | https://www.mt.co.kr/stock/2026/09/08/2026090722215967112 |  |
| kifrs | 머니투데이 | [단독] 수조원 미래손실 추정치, 법정공시 사업보고서엔 없다 | https://www.mt.co.kr/stock/2026/09/08/2026090710491724209 |  |
| kifrs | globalepic.co.kr | 고려아연 백인규 vs MBK 박유경 … 9월9일 한 사람만 웃는다 | http://www.globalepic.co.kr/view.php?ud=20260907132019935248439a4874_29 |  |
| kifrs | 한국세정신문 | 감사전 재무제표 제출 위반 76곳…9곳 감사인 지정 | https://www.taxtimes.co.kr/news/article.html?no=276700 |  |
| kifrs | sateconomy.co.kr | 호텔롯데, 회계대상 최우수상…롯데 계열사 최초 | https://sateconomy.co.kr/news/view/1065591691171929 |  |
| kifrs | incheonilbo.com | 의정부경전철 시민모임, 시의회 사전의결 누락 및 손해배상 구상권 청구... | https://www.incheonilbo.com/news/articleView.html?idxno=1331183 |  |
| kifrs | segyebiz.com | 넉 달 앞으로 다가온 가상자산 과세…여권에서도 “인프라·실질 반영한... | http://www.segyebiz.com/newsView/20260903511481?OutUrl=naver |  |
| kifrs | etoday.co.kr | 가상자산 세제 개편론 주목⋯"과세 여부보다 제대로 된 과세가 먼저" | https://www.etoday.co.kr/news/view/2621517 |  |
| kifrs | weeklytoday.com | [위클리오늘] 의정부시, 노인일자리 사업 수행기관 10개소 지도점검 완... | http://www.weeklytoday.com/news/articleView.html?idxno=792850 |  |
| kifrs | 매일경제 | “주식은 비과세, 코인은 22%”…2027년 가상자산 과세 논란 | https://www.mk.co.kr/article/12143162 |  |
| kifrs | gukjenews.com | 의정부시, 10개 노인일자리 사업 현장 지도점검 실시 | https://www.gukjenews.com/news/articleView.html?idxno=3683428 |  |
| kifrs | zdnet.co.kr | "보고서 등 각종 공공 콘텐츠 간편 제작"...크리니티, '웍스AI' 공급 확대 | https://zdnet.co.kr/view/?no=20260901210211 |  |
| kifrs | etnews.com | 크리니티, 공공기관 대상 '웍스AI' 공급 확대…공공 AI 파트너 사업 본격... | https://www.etnews.com/20260901000266 |  |
| kifrs | hapt.co.kr | 입주자대표회의로 부과된 과태료의 처리 방법 | https://www.hapt.co.kr/news/articleView.html?idxno=169399 |  |
| kifrs | joongangenews.com | [단독] 금감원, 70개 GA '불법 DB 영업' 검사...벌금·영업정지 '중징계'... | https://www.joongangenews.com/news/articleView.html?idxno=544415 |  |
| kifrs | fntimes.com | 국내외 의결권 자문사 ‘7대1’...고려아연 추천 백인규 압도적 지지, 왜... | https://www.fntimes.com/html/view.php?ud=2026083116474355977de3572ddd_18 |  |
| kifrs | inews24.com | 의결권 자문사 ‘7대1’…박유경 후보, 왜 줄줄이 반대했나 | http://www.inews24.com/view/2000136 |  |
| kifrs | wowtv.co.kr | 국내외 의결권 자문사, 고려아연 추천 후보 지지 | http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202608310248&t=NN |  |
| kifrs | biz.heraldcorp.com | 감사원 “대법원, 법령 근거 없이 대법관들에 月 200만원 현금 지급” | https://biz.heraldcorp.com/article/10857216?ref=naver |  |
| kifrs | view.asiae.co.kr | 감사원 "대법관·법원행정처장에 매달 '현금 격려금' 부당 집행"…3년9개... | https://view.asiae.co.kr/article/2026083110394576578 |  |
| kifrs | lcnews.co.kr | 한양증권 'JTBC 채권' 추가 매입 내부통제 의혹, 민사소송서 정면 쟁점화 | https://www.lcnews.co.kr/news/articleView.html?idxno=207397 |  |
| kifrs | ilyoseoul.co.kr | [학교를 폭파하라-⑩] 학교를 무너뜨린 자리에 무엇을 세울 것인가 | https://www.ilyoseoul.co.kr/news/articleView.html?idxno=521833 |  |
| kifrs | view.asiae.co.kr | 광주 아파트서 12억5천만원 관리비 횡령 의혹 | https://view.asiae.co.kr/article/2026082712510777918 |  |
| kifrs | opinionnews.co.kr | 고려아연 "글로벌 의결권 자문사, MBK·영풍 감사위원 안건 반대" | http://www.opinionnews.co.kr/news/articleView.html?idxno=143626 |  |
| kifrs | kdfnews.com | 글래스루이스, 고려아연 백인규 후보 지지..."감사·내부통제 경험 더 적... | http://www.kdfnews.com/news/articleView.html?idxno=187130 |  |
| kifrs | nbntv.kr | [풍문레이다] 성현회계법인② 인터지스 미수금 대손상각 후 외부감사 수... | https://www.nbntv.kr/news/articleView.html?idxno=340700 |  |
| kifrs | 파이낸셜뉴스 | 사회복지관 운영법인 4곳 '3년치 장부' 본다… 제주도, 회계·후원금 점... | https://www.fnnews.com/news/202608260954465532 |  |
| kifrs | newstomato.com | (잃어버린 경영을 찾아서)귀족의 가면: 이중 중대성 피하려고 이중 공시... | http://www.newstomato.com/ReadNews.aspx?no=1310939&inflow=N |  |
| kifrs | ccdailynews.com | 논산시, 공금 관리 전수 점검, 투명성 강화 | https://www.ccdailynews.com/news/articleView.html?idxno=2435552 |  |
| kifrs | ggilbo.com | 논산시, 공금관리 전수 점검 회계 투명성 강화 | https://www.ggilbo.com/news/articleView.html?idxno=1176757 |  |
| kifrs | chungnamilbo.co.kr | 논산시, 공금 관리 전수 점검… 회계 투명성 강화 총력 | http://www.chungnamilbo.co.kr/news/articleView.html?idxno=905247 |  |
| kifrs | cctimes.kr | 논산시 공금 관리 전수 점검으로 회계 투명성 강화 | http://www.cctimes.kr/news/articleView.html?idxno=922864 |  |
| kifrs | kpanews.co.kr | [위클리이슈] 깐깐해진 잣대·커진 문턱… 혁신형 제약 '생존 레이스' 본... | https://www.kpanews.co.kr/news/articleView.html?idxno=541218 |  |
| kifrs | breaknews.com | 논산시, 공금 관리 실태 전수 실사로 회계 사각지대 없앤다... | http://www.breaknews.com/1230679 |  |
| kifrs | newsworker.co.kr | 논산시, 18개 기관 회계 전반 점검... '투명한 공금 관리' 고삐 | https://www.newsworker.co.kr/news/articleView.html?idxno=500101 |  |
| kifrs | raonnews.com | 생보사들, 즉시연금 충당금 잇따라 환입…삼성생명 이어 교보·KDB·ABL도 | https://www.raonnews.com/news/article.html?no=60425 |  |
| kifrs | consumernews.co.kr | R&D에 올인하더니...종근당, 바이오시밀러 2종 개발 속도내며 자산화 규... | http://www.consumernews.co.kr/news/articleView.html?idxno=761692 |  |
| tax | joongang.co.kr | 국세청, 글로벌 최저한세 세무대리인 간담회 개최 | https://www.joongang.co.kr/article/25474055 |  |
| tax | tleaves.co.kr | [기획] '결제 독점' 메스 댄 방미통위…구글·애플 과징금 637억 '벼락' | https://www.tleaves.co.kr/news/articleView.html?idxno=10079 |  |
| tax | 한국경제 | "세금 1원도 안 낸다"…억만장자들의 5조달러 절세 비법 [밤 사이 해외 ... | https://www.hankyung.com/article/202610292669i |  |
| tax | youthdaily.co.kr | 삼성전자 주가에 "명운"...삼성생명, 넉달 새 지분가치 '46조' 증발 | https://www.youthdaily.co.kr/news/article.html?no=228986 |  |
| tax | 매일경제 | 데이터센터 사모투자, 외국계에 다 내줄 판 | https://www.mk.co.kr/article/12188645 |  |
| tax | khan.co.kr | 내년 ‘세금 할인액’ 최초로 100조원 넘어···대기업 감면액 50% 육박 | https://www.khan.co.kr/article/202610281701001 |  |
| tax | newspim.com | [재정 골든타임] ① 유럽을 뒤덮은 청년들의 분노…한국도 자유롭지 않... | https://www.newspim.com/news/view/20261026001091 |  |
| tax | biz.heraldcorp.com | ‘책·연극’은 되는데 ‘잡지·무용’은 안 된다?...가업승계 세제 개... | https://biz.heraldcorp.com/article/10917412?ref=naver |  |
| tax | g-enews.com | 추미애표 지방세 '소·법·담' 3대 과제 입법 토론회 | https://www.g-enews.com/view.php?ud=2026102808514842078fbfc802b3_1 |  |
| tax | breaknews.com | 국민의힘 장동혁·정점식, 李정권 '남탓·사법파괴' 총공세 | http://www.breaknews.com/1246243 |  |
| tax | 한국경제 | "부자감세냐, 기업 성장이냐? 진짜 문제는 따로 있어"[중산층 상속세④... | https://magazine.hankyung.com/business/article/202610228749b |  |
| tax | sentv.co.kr | 증권사 교육세 부담 가중…NH證 세금·공과금 1년새 3배 | https://www.sentv.co.kr/article/view/sentv202610270128 |  |
| tax | segye.com | 현실 못 담은 세수추계… 4년간 연평균 51조 오차 | https://www.segye.com/newsView/20261027516402?OutUrl=naver |  |
| tax | ceoscoredaily.com | 국산 전기차 세액공제 대상 포함되나…K-배터리, 이차전지 수혜 기대 | https://www.ceoscoredaily.com/page/view/2026102715332188104 |  |
| tax | 서울경제 | “기재부, 국회 패싱해 기금 32조 전용…年 이자만 8330억” | https://www.sedaily.com/article/20106787?ref=naver |  |
| tax | ohmynews.com | 추미애 경기지사, 소방재정 국비 확대·지방세 개편 국회 압박 | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003279338&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| tax | yonhapnewstv.co.kr | 尹정부 세수 부족에 기금 동원…지자체 사업도 차질 | http://www.yonhapnewstv.co.kr/news/MYH20261027154028fH0 |  |
| tax | wowtv.co.kr | 4년간 연평균 50조 세수오차...감사원 "정부 계산 잘못된 탓" | http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202610270129&t=NN |  |
| tax | eroun.net | 후퇴하고 흔들리고...'윤석열표 감세' 되돌리기 | https://www.eroun.net/news/articleView.html?idxno=93505 |  |
| tax | 한국세정신문 | 감사원, 정부 세수추계 4년간 평균 51조5천억 오차 발생해 | https://www.taxtimes.co.kr/news/article.html?no=277486 |  |
| tax | naeil.com | 대규모 세수결손, 정부 계산 잘못 탓 | https://www.naeil.com/news/read/606554?ref=naver |  |
| tax | naeil.com | 중국차 한국시장 급잠식…‘방어막 없어’ | https://www.naeil.com/news/read/606505?ref=naver |  |
| tax | biz.chosun.com | [정책 인사이트] 국회·정부, 전기차 완성차 세액공제 포함 추진… “중... | https://biz.chosun.com/policy/policy_sub/2026/10/27/KTDKOW4FHFFENFYA3M2KONFYUM/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| tax | m-economynews.com | 여야, 조희대 국정조사·공소취소 특검 놓고 정면충돌 | https://www.m-economynews.com/news/article.html?no=72168 |  |
| tax | 조세일보 | 윤 정부 '87조 세수펑크'…애꿎은 지방·기금이 털려 | http://www.joseilbo.com/news/news_read.php?uid=578247&class=32&grp= |  |
| tax | 일간NTN | 세수 오차에 기금 돌려막기까지…감사원, 부실 추계가 부른 '재정 꼼수... | http://www.intn.co.kr/news/articleView.html?idxno=2054323 |  |
| tax | 이데일리 | 정부, 세수 펑크에…국회 심의 대신 32조 기금 돌려막기 | https://www.edaily.co.kr/News/Read?newsId=03696566645617184&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | newsis.com | 감사원 "법인세·양도세 추계오차 81%는 모형 문제 때문" | https://www.newsis.com/view/NISX20261026_0003841744 |  |
| tax | joongang.co.kr | 4년간 50조 세수 오차…감사원 “경기 아닌 정부 추계 모형 오류” | https://www.joongang.co.kr/article/25473170 |  |
| tax | yonhapnewstv.co.kr | 감사원 "尹정부, 세수 부족에 기금 32조원 활용…국회 통제 우회" | http://www.yonhapnewstv.co.kr/news/AKR20261027101332mZ7 |  |
| tax | 머니투데이 | '年 51.5조' 세수 오차, 경기 탓만 아니었다…감사원 "기재부 '추계모형... | https://www.mt.co.kr/politics/2026/10/28/2026102709232357438 |  |
| tax | 머니투데이 | 임이자 "얄팍한 금융기술로 증시 살지 않아…법인세 낮추고 주52시간 완... | https://www.mt.co.kr/politics/2026/10/27/2026102710441025213 |  |
| tax | polinews.co.kr | [진단] 162조 미래대응기금, 누구를 위한 투자인가···성장동력 확보와... | https://www.polinews.co.kr/news/articleView.html?idxno=746957 |  |
| tax | news1.kr | 국힘 "일자리·청년·돌봄 등 민생예산 최우선…다음주 장동혁 직접 보... | https://www.news1.kr/politics/assembly/6332762 |  |
| tax | insidevina.com | 베트남, 올해 소득세 수입 30조 동 급감 전망…공제 확대·세율 구간 축... | https://www.insidevina.com/news/articleView.html?idxno=44356 |  |
| tax | sejungilbo.com | 이정문, 영상콘텐츠 제작 투자·온라인 유통비용에 10% 세액공제 추진 | https://www.sejungilbo.com/news/articleView.html?idxno=60815 |  |
| tax | e-platform.net | [오늘의 국회 에너지 입법 : 전기차·태양광 등의 국내 생산 연계 지원... | http://www.e-platform.net/news/articleView.html?idxno=106431 |  |
| tax | autodaily.co.kr | 여야, 국내 생산 전기차·배터리 세액공제 추진⋯'특정기업 지원' 논란... | https://www.autodaily.co.kr/news/articleView.html?idxno=601508 |  |
| tax | polinews.co.kr | 세라젬 이환성 회장, 신입사원 출신 전문경영인 이경수 대표 '양자 입양... | https://www.polinews.co.kr/news/articleView.html?idxno=746920 |  |
| tax | hankookilbo.com | 국회 압박에 흔들리는 조세정책… ①전기차②가상자산③부동산 대수술 | https://www.hankookilbo.com/news/article/A2026102616090004145?did=NA |  |
| tax | iusm.co.kr | 전기차 국내생산 세액공제 추진…국힘 "11월 처리하자" | https://www.iusm.co.kr/news/articleView.html?idxno=1069633 |  |
| tax | ajunews.com | [강대웅의 정문일침(頂門一鍼)] 추미애 경기지사 소방재정 개혁을 위해... | https://www.ajunews.com/view/20261026135539000 |  |
| tax | livebiz.today | 여야, '전기차 국내생산세액공제' 법안 공동발의...국민의힘 "11월 처리... | https://www.livebiz.today/news/articleView.html?idxno=205920 |  |
| tax | 4th.kr | 중국 전기차 韓 시장 급속 잠식.."전방위 대책 시급" | http://www.4th.kr/news/articleView.html?idxno=2120405 |  |
| tax | 한국세정신문 | 유동수 의원 "국제문화행사 기업 후원비용 10% 법인세 공제" | https://www.taxtimes.co.kr/news/article.html?no=277442 |  |
| tax | sejungilbo.com | [판세] 본세 세액의 유효를 전제로 무신고·과소신고·납부불성실가산세... | https://www.sejungilbo.com/news/articleView.html?idxno=60481 |  |
| tax | etnews.com | 반도체 키우고 곳간 채우고…추미애 경기지사, 산업 육성·세입 확충 구... | https://www.etnews.com/20261023000327 |  |
| tax | dnews.co.kr | 상장리츠 자산총액 4년여만에 2배 늘었는데,시총은 곤두박질 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610231516190610901 |  |
| tax | newstown.co.kr | [추미애 경기도정 대해부③] 지방소비세 40% 추진…자주재원 확충 | http://www.newstown.co.kr/news/articleView.html?idxno=719588 |  |
| tax | newsis.com | "보조금으론 못 막아"…국산차 살릴 '세액 감면' 카드 꺼내나[中 전기차... | https://www.newsis.com/view/NISX20261023_0003838334 |  |
| tax | newsis.com | "부의 대물림 꼼수차단"…가업상속공제 대폭손질[중기 가업승계①] | https://www.newsis.com/view/NISX20261023_0003837948 |  |
| tax | financialpost.co.kr | 재정 부담이냐 산업 보호냐…전기차 세액공제 재추진 '딜레마' | https://www.financialpost.co.kr/news/articleView.html?idxno=282329 |  |
| tax | ddanzi.com | [브라질 대선]TV토론에 드립이 난무했던 이유 : 룰라가 메타를 고발한 ... | http://www.ddanzi.com/897556102 |  |
| tax | ikpnews.net | 수입 김치 범람하는 외식 시장, 김치 자급률 높이는 길은②발제 | http://www.ikpnews.net/news/articleView.html?idxno=71771 |  |
| tax | etoday.co.kr | 추미애 "소방인건비 국가 책임"…경기도, 교부세 59억 미집행·소방차 2... | https://www.etoday.co.kr/news/view/2639579 |  |
| tax | news1.kr | 외국인 결제 장벽에 OTA 환불 제한까지…국감서 관광정책 점검 질타(종... | https://www.news1.kr/industry/hotel-tourism/6330356 |  |
| tax | ekn.kr | [2026 국감] 반도체 둔화 세수펑크나면, 박홍근 “강력한 지출 구조조정... | https://www.ekn.kr/web/view.php?key=20261023029450437 |  |
| tax | ddaily.co.kr | 관광은 성장하는데 제도는 제자리…문체위 국감서 현안 개선 촉구(종합... | https://www.ddaily.co.kr/page/view/2026102316423556530 |  |
| tax | businesspost.co.kr | GC녹십자 '백신산업 세액공제' 논의 덕 볼까, 허은철 독감백신 수익성에... | https://www.businesspost.co.kr/BP?command=article_view&num=450160 |  |
| tax | news1.kr | 中 전기차 공세에 韓 생산기반 '흔들'…생산세액공제 재추진 | https://www.news1.kr/industry/auto-industry/6329847 |  |
| tax | 파이낸셜뉴스 | "이름만 국가직 소방관, 인건비 92% 경기도가 낸다"…추미애 "소방재정... | https://www.fnnews.com/news/202610231401146918 |  |
| tax | wikitree.co.kr | [국감] 이언주 "중국산 전기차 점유율 40%대 육박…구매보조금 넘어 생... | https://www.wikitree.co.kr/articles/1168568 |  |
| tax | view.asiae.co.kr | 전기차 국내생산세액공제 도입 추진…생산량 연동·배터리 투자 지원 필... | https://view.asiae.co.kr/article/2026102217004235621 |  |
| tax | 한국세정신문 | 김상훈 의원 "민간임대주택 장특공 확대…건설 80%·매입 70%·단기 50%" | https://www.taxtimes.co.kr/news/article.html?no=277429 |  |
| tax | megaeconomy.co.kr | [메가분석] 국산 전기차 국내 점유율 첫 50% 붕괴…中 공세에 '생산세액... | https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065575924490679 |  |
| tax | getnews.co.kr | "전월세 공급은 사수, 생애 첫 취득 부담은 낮춘다!"... 김상훈 의원, 전... | https://www.getnews.co.kr/news/articleView.html?idxno=884557 |  |
| tax | news.cpbc.co.kr | 유동수 의원,  '2027 서울 세계청년대회' 후원 세액공제 추진 | https://news.cpbc.co.kr/article/1176540?division=NAVER |  |
| tax | biz.heraldcorp.com | “실수요자 취득 부담 낮춰야” 김상훈, 전월세 안정·내집마련 지원 2... | https://biz.heraldcorp.com/article/10912457?ref=naver |  |
| tax | electimes.com | 중기특별지원 일몰 앞두고 나주 전력기자재 기업 '전전긍긍' | https://www.electimes.com/news/articleView.html?idxno=373756 |  |
| tax | thepublic.kr | '부자 경기도'의 역설…기업은 몰리는데 도 재정은 왜 비어 가나 | https://www.thepublic.kr/news/articleView.html?idxno=323400 |  |
| tax | sejungilbo.com | 이언주, 산단 조성에 수용된 법인 토지 '양도차익 익금불산입' 추진 | https://www.sejungilbo.com/news/articleView.html?idxno=60767 |  |
| tax | sejungilbo.com | 유동수, `27 서울 세계청년대회 후원 세액공제 추진 | https://www.sejungilbo.com/news/articleView.html?idxno=60764 |  |
| tax | the-today.com | [핫이슈] "순전한 오만"…구글, 핀란드 숲 40만 그루 밀었다가 '공사 중... | https://www.the-today.com/news/articleView.html?idxno=92236 |  |
| tax | view.asiae.co.kr | [2026 국감] 이형일 "국내 전기차 생산세액공제 도입 검토중" | https://view.asiae.co.kr/article/2026102222571677892 |  |
| tax | newsis.com | '중국산 공세'에 전기차 세액공제 법 개정 추진…업계·학계 "빠른 처리... | https://www.newsis.com/view/NISX20261022_0003836463 |  |
| tax | biz.chosun.com | 이형일 부총리 “전기차 생산세액공제 적용 검토할 것” | https://biz.chosun.com/policy/policy_sub/2026/10/22/Y7ZQUKYJLNEYPIQX4KS6NEI4WA/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| tax | 매일경제 | 中전기차 공세에 … 이형일 "생산세액공제 검토" | https://www.mk.co.kr/article/12183212 |  |
| tax | news1.kr | 가상자산 과세 '동상이몽'…與 "예정대로 시행" 野 "인프라 미비 유예"(... | https://www.news1.kr/politics/assembly/6329057 |  |
| tax | jeonmae.co.kr | [PICK! 이 안건] 김상훈 등 11인 "해외자원개발 투자에 대한 세제지원 강... | https://www.jeonmae.co.kr/news/articleView.html?idxno=1297939 |  |
| tax | kmaeil.com | 유동수 의원, 2027 서울 세계청년대회 기업 후원금 10% 세액공제 법안 대... | https://www.kmaeil.com/news/articleView.html?idxno=655405 |  |
| tax | mediapen.com | BYD 후발주자 줄줄이 상륙 채비…국내 완성차 생산·투자 지원 '공백' | https://www.mediapen.com/news/view/1131798 |  |
| tax | dailian.co.kr | 中 전기차 점유율 35%로 치솟자…정치권, '국내 생산' 세액공제 추진 | https://www.dailian.co.kr/news/view/1704764/?sc=Naver |  |
| tax | chosun.com | “투자·인력 배치는 노사 교섭서 빼야”…한경협, 정책 의견 119건 건의 | https://www.chosun.com/economy/industry-company/2026/10/22/CULSH3AD4JFGXPAOXDNF45QOJU/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | dailypop.kr | 가상자산 과세 '갑론을박'..."납세자가 받아들일 수 있는 기준 필요" | http://www.dailypop.kr/news/articleView.html?idxno=103575 |  |
| tax | m-joongang.com | 추미애 지사, '14조원 재원 확충' 판 바꾼다 | https://www.m-joongang.com/news/articleView.html?idxno=403214 |  |
| tax | newsway.co.kr | [류영재의 지속가능 경제]주주일 때와 종업원일 때 | https://www.newsway.co.kr/news/view?ud=2026102209001857005 |  |
| tax | 한국경제 | 여야, 中 전기차 공세에 '세액공제 카드' 꺼냈다 | https://www.hankyung.com/article/2026102169951 |  |
| tax | news.kbs.co.kr | [이슈K] 미래대응기금 신설에 교부세 삭감?…지방 재정은 | https://news.kbs.co.kr/news/pc/view/view.do?ncd=8691543&ref=A |  |
| tax | 매일경제 | 여야 “전기차 생산세액공제 반드시 올해 통과” | https://www.mk.co.kr/article/12182078 |  |
| tax | 매일경제 | [단독] K전기차 비상에 '세액공제' 꺼낸 여야 | https://www.mk.co.kr/article/12182059 |  |
| tax | dailian.co.kr | [현장] "AI DC 키운다더니…" 코로케이션 세액공제 제외·그리드 코드 부... | https://www.dailian.co.kr/news/view/1704310/?sc=Naver |  |
| tax | 조세일보 | 중부지방세무사회, '자사주 소각부터 배당까지' 세금 문제 논의 | http://www.joseilbo.com/news/news_read.php?uid=577874&class=10&grp= |  |
| tax | newstown.co.kr | [추미애 경기도정 대해부③] 추미애표 지방재정 개혁, 국회 입법으로 | http://www.newstown.co.kr/news/articleView.html?idxno=719205 |  |
| tax | slownews.kr | 엘리스 폭락에 세계가 충격, “한국이 글로벌 AI 풍향계가 됐다”: 슬로... | https://slownews.kr/168257 |  |
| tax | ajunews.com | [오정근의 아주경제적 시선] 불타는 유럽의 '재정 중독' 보고도 무리한... | https://www.ajunews.com/view/20261019155919234 |  |
| tax | etoday.co.kr | ‘보조금+세액공제’ 기대감 커지는데…전기차는 여전히 소외 [제조업 ... | https://www.etoday.co.kr/news/view/2637813 |  |
| tax | 한국세정신문 | 중부세무사회, 추계회원세미나 성료…"소통·화합 돈독히 하는 시간" | https://www.taxtimes.co.kr/news/article.html?no=277381 |  |
| tax | jeonmae.co.kr | [PICK! 이 안건] 윤영석 등 10인 "농어업경영 및 농어작업 대행용역에 대... | https://www.jeonmae.co.kr/news/articleView.html?idxno=1304426 |  |
| tax | smartbizn.com | [증권UP+] 증권업계, 투자상품 확대·소비자 보호·디지털자산 대응 강화 | https://www.smartbizn.com/news/articleView.html?idxno=157937 |  |
| tax | breaknews.com | 경실련 “방미통위 구글·애플 과징금 637억원, 실효성 부족…상한 높여... | http://www.breaknews.com/1246822 |  |
| tax | news.tf.co.kr | 구글·애플 과징금 철퇴…인앱결제 개선·수수료 인하로 이어질까 | https://news.tf.co.kr/read/economy/2382392.htm |  |
| tax | hansbiz.co.kr | 구글·애플에 637억 철퇴…'인앱결제 갑질' 끝날까 | http://www.hansbiz.co.kr/news/articleView.html?idxno=877565 |  |
| tax | thepublic.kr | 방미통위, 구글·애플에 과징금 637억원…인앱결제 강제 첫 제재 | https://www.thepublic.kr/news/articleView.html?idxno=324219 |  |
| tax | industrynews.co.kr | 구글·애플에 과징금 637억원…결제방식 강제·앱 심사 지연 제재 | https://www.industrynews.co.kr/news/articleView.html?idxno=88449 |  |
| tax | itbiznews.com | 방미통위, '앱마켓 갑질' 구글·애플에 과징금 637억원 부과 | https://www.itbiznews.com/news/articleView.html?idxno=229483 |  |
| tax | segye.com | ‘인앱결제’ 구글·애플에 637억 과징금… 빅테크 규제 칼 뺀 韓 [뉴스... | https://www.segye.com/newsView/20261028520095?OutUrl=naver |  |
| tax | pointdaily.co.kr | [출근길 포인트] 해킹 확산에 당국 긴급 점검·라면 4사 가격 담합·인앱... | https://www.pointdaily.co.kr/news/articleView.html?idxno=324040 |  |
| tax | 머니투데이 | 637억도 모자라… 플랫폼 과징금 손본다 | https://www.mt.co.kr/tech/2026/10/29/2026102819461072230 |  |
| tax | kmib.co.kr | 구글·애플에 총 637억 과징금… ‘인앱결제 강제 금지법’ 첫 적용 | https://www.kmib.co.kr/article/20261028502459 |  |
| tax | newscj.com | 방미통위, 구글·애플에 과징금 637억 부과… '인앱결제 강제' 첫 제재 | https://www.newscj.com/news/articleView.html?idxno=3444011 |  |
| tax | press9.kr | 구글 429억·애플 208억 과징금…앱 결제·심사 관행 제동 | http://www.press9.kr/news/articleView.html?idxno=85141 |  |
| tax | m-i.kr | 구글·애플, 인앱결제 강제에 과징금 637억원…앱 개발사에 수수료 26% 부... | https://www.m-i.kr/news/articleView.html?idxno=2011596 |  |
| tax | byline.network | 인앱결제 강제한 대가, 구글·애플 과징금 637억원 | https://byline.network/?p=9004111222625213 |  |
| tax | gamefocus.co.kr | 방송미디어통신위원회, 구글·애플에 637억 원 과징금 부과 의결... 외부... | https://gamefocus.co.kr/detail.php?number=180116 |  |
| tax | newsian.co.kr | 구글·애플, 인앱결제 강제에 과징금 637억…외부결제 막고 수수료 장벽 | https://www.newsian.co.kr/news/articleView.html?idxno=100146 |  |
| tax | econovill.com | 구글·애플 인앱결제 강제에 방미통위 637억 과징금 '철퇴' | https://www.econovill.com/news/articleView.html?idxno=755234 |  |
| tax | g-enews.com | 구글·애플, 인앱결제 강제에 과징금 637억원…양사 반발 | https://www.g-enews.com/view.php?ud=2026102818483337ea14faf6f5_1 |  |
| tax | biz.heraldcorp.com | 구글·애플에 인앱결제 과징금 637억원…양사 “동의 못 해” [비즈360] | https://biz.heraldcorp.com/article/10918150?ref=naver |  |
| tax | kmib.co.kr | 방미통위 ‘인앱결제 강제’ 구글·애플에 총 637억 과징금 부과 | https://www.kmib.co.kr/article/20261028502281 |  |
| tax | ziksir.com | [이슈 직썰] 구글·애플, 인앱결제 강제로 과징금 637억원…3년 만에 제... | https://www.ziksir.com/news/articleView.html?idxno=151158 |  |
| tax | thisisgame.com | 방미통위, 구글·애플에 결제방식 선택권 보장 등 시정명령…구글 429억... | https://www.thisisgame.com/articles/431482 |  |
| tax | 이데일리 | 애플·구글 인앱결제 과징금 637억원…양사 "유감"(종합) | https://www.edaily.co.kr/News/Read?newsId=05881046645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | wolyo.co.kr | 구글·애플 '인앱결제 강제'에 637억 과징금…앱마켓 갑질 첫 제재 | https://www.wolyo.co.kr/news/articleView.html?idxno=319720 |  |
| tax | bloter.net | 3년 미룬 구글·애플 인앱결제 제재…방미통위, 637억 과징금 부과 | https://www.bloter.net/news/articleView.html?idxno=676986 |  |
| tax | sisafocus.co.kr | 방미통위, 구글·애플에 과징금 총 637억원…"인앤결제 등 강제" | http://www.sisafocus.co.kr/news/articleView.html?idxno=366895 |  |
| tax | segye.com | 구글·애플에 600억원대 과징금… 3년 만에 칼 빼든 한국 | https://www.segye.com/newsView/20261028517171?OutUrl=naver |  |
| tax | hankookilbo.com | '앱 마켓 갑질' 과징금 구글 429억 애플 208억....방미통위, 3년 만에 의... | https://www.hankookilbo.com/news/article/A2026102815000001695?did=NA |  |
| tax | it-b.co.kr | "구글‧애플 '인앱결제' 강제했다"…방미통위, 과징금 637억원 부과 | https://www.it-b.co.kr/news/articleView.html?idxno=90458 |  |
| tax | financialpost.co.kr | 방미통위, 앱 마켓 '갑질' 구글·애플에 637억원 과징금 | https://www.financialpost.co.kr/news/articleView.html?idxno=283144 |  |
| tax | newspim.com | 구글·애플 '인앱결제 강제' 첫 제재…방미통위, 과징금 637억 부과 | https://www.newspim.com/news/view/20261028001560 |  |
| tax | digitaltoday.co.kr | 구글·애플 '인앱결제' 족쇄 풀릴까…앱마켓 시장 변화 주목 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=710724 |  |
| tax | yna.co.kr | 구글·애플에 인앱결제 과징금 637억원…양사 유감·대응 검토(종합2보) | https://www.yna.co.kr/view/AKR20261028139201017?input=1195m |  |
| tax | 서울경제 | ‘인앱결제 강제’ 구글·애플에 과징금 637억 | https://www.sedaily.com/article/20107362?ref=naver |  |
| tax | nocutnews.co.kr | 구글·애플에 637억 과징금…외부결제 허용 명령 | https://www.nocutnews.co.kr/news/6598749?utm_source=naver&utm_medium=article&utm_campaign=20261028055036 |  |
| tax | news.tf.co.kr | 방미통위, '인앱결제 강제' 구글·애플에 과징금 637억원 부과 | https://news.tf.co.kr/read/economy/2382074.htm |  |
| tax | mediaus.co.kr | '인앱결제 강제' 구글·애플 과징금, 3년 전보다 40억 줄어 | https://www.mediaus.co.kr/news/articleView.html?idxno=318703 |  |
| tax | thereport.co.kr | 구글·애플, 외부결제 강제 금지 위반 과징금 637억 | https://www.thereport.co.kr/news/articleView.html?idxno=92775 |  |
| tax | itdaily.kr | "인앱결제 강제는 부당" 방미통위, 구글·애플에 과징금 637억 부과 | https://www.itdaily.kr/news/articleView.html?idxno=242520 |  |
| tax | ngonews.kr | 방미통위, 구글·애플에 과징금 637억원 부과…"인앱결제 강제 첫 제재" | https://www.ngonews.kr/news/articleView.html?idxno=241752 |  |
| tax | abcn.kr | '인앱결제 강제' 구글·애플에 첫 과징금 637억원…"상한 높인다" | https://www.abcn.kr/news/articleView.html?idxno=93729 |  |
| tax | 머니투데이 | '인앱결제' 구글·애플 637억 과징금 철퇴…"법적 대응 검토"(종합) | https://www.mt.co.kr/tech/2026/10/28/2026102817270438634 |  |
| tax | dealsite.co.kr | 구글·애플에 과징금 637억원…인앱결제 강제 첫 제재 | https://dealsite.co.kr/articles/171572 |  |
| tax | dailian.co.kr | 3년 끈 '앱마켓 갑질'에 637억 철퇴…방미통위, '외부결제' 허용 명령(종... | https://www.dailian.co.kr/news/view/1707582/?sc=Naver |  |
| tax | m-i.kr | 구글·애플, 인앱결제 강제 첫 제재…과징금 637억원 | https://www.m-i.kr/news/articleView.html?idxno=2011557 |  |
| tax | delighti.co.kr | 방미통위, 구글·애플에 과징금 637억원…인앱결제 강제 금지법 첫 제재 | https://www.delighti.co.kr/news/articleView.html?idxno=124048 |  |
| tax | ceoscoredaily.com | 구글·애플 ‘인앱결제 강제’ 과징금 637억 ‘철퇴’…“30% 수수료 낮... | https://www.ceoscoredaily.com/page/view/2026102817052049648 |  |
| tax | iminju.net | 방미통위, '앱 마켓 갑질' 첫 제재…구글·애플에 과징금 637억 원 | http://www.iminju.net/news/articleView.html?idxno=171579 |  |
| tax | news.bizwatch.co.kr | '인앱결제 강제' 구글 429억·애플 208억 과징금 | https://news.bizwatch.co.kr/article/mobile/2026/10/28/0042 |  |
| tax | popcornnews.net | 구글·애플, '인앱결제 강제' 과징금 637억…외부결제 제한 시정명령 | http://www.popcornnews.net/news/articleView.html?idxno=137738 |  |
| tax | kgnews.co.kr | 구글 429억·애플 208억 과징금…인앱결제 첫 제재 | https://www.kgnews.co.kr/news/article.html?no=917188 |  |
| tax | youthdaily.co.kr | 구글·애플, 외부결제 제한에 과징금 637억원…수수료 체계 개선 명령 | https://www.youthdaily.co.kr/news/article.html?no=229010 |  |
| tax | businesspost.co.kr | 방미통위 구글·애플에 '인앱결제 강제' 과징금 637억 부과, 사전통지 후... | https://www.businesspost.co.kr/BP?command=article_view&num=450560 |  |
| tax | etoday.co.kr | 구글·애플 '인앱결제 강제'에 과징금 637억원…3년 만에 제재 확정 | https://www.etoday.co.kr/news/view/2641299 |  |
| tax | busan.com | 구글·애플 인앱결제 강제에 637억 원 과징금 부과 | https://www.busan.com/view/busan/view.php?code=2026102817102756873 |  |
| tax | lkp.news | 신협중앙회, 부실채권 정리 '투 트랙'... 매입 여력과 회수 역량 함께 키... | http://www.lkp.news/news/articleView.html?idxno=85530 |  |
| tax | chosun.com | 방미통위, 구글 429억·애플 208억 과징금 부과...“인앱결제 강제해” | https://www.chosun.com/economy/tech_it/2026/10/28/KVXYCIJHBRGM5L47TC6UWL54A4/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | donga.com | ‘인앱결제 강제’ 구글 429억원·애플 208억원 과징금 부과 | https://www.donga.com/news/Economy/article/all/20261028/134926584/2 |  |
| tax | ajunews.com | 600억 과징금 부과한 방미통위 "구글·애플, 결제방식 강제하고 앱 심사... | https://www.ajunews.com/view/20261028135707298 |  |
| tax | newsworks.co.kr | 방미통위, 구글 429억·애플 208억 과징금…'인앱결제 강제 금지법' 첫 ... | https://www.newsworks.co.kr/news/articleView.html?idxno=901146 |  |
| tax | inven.co.kr | [이슈] 구글 429억·애플 208억 과징금, '인앱결제 강제' 첫 제재 | https://www.inven.co.kr/webzine/news/?news=322677 |  |
| tax | kyeonggi.com | 방미통위, 구글·애플 '인앱결제' 정조준…과징금 637억원 부과 | https://www.kyeonggi.com/article/20261028580485 |  |
| tax | it.chosun.com | 3년만에 구글·애플 637억 철퇴…수수료 규제는 빠졌다 | https://it.chosun.com/news/articleView.html?idxno=2023092172997 |  |
| tax | tjb.co.kr | 구글 429억·애플 208억 원…'인앱결제 강제' 첫 철퇴 | https://www.tjb.co.kr/news05/bodo/view/id/105409 |  |
| tax | news.jtbc.co.kr | 구글 429억·애플 208억…방미통위, '앱마켓 갑질' 과징금 부과 | https://news.jtbc.co.kr/article/NB12325298?influxDiv=NAVER |  |
| tax | 이데일리 | 애플·구글 인앱결제 과징금 637억원…"처벌 기준 강화 법개정 준비" | https://www.edaily.co.kr/News/Read?newsId=05421846645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | techm.kr | 방미통위, 구글에 429억 애플에 208억원 과징금...앱 마켓 금지행위 위반 | https://www.techm.kr/news/articleView.html?idxno=156618 |  |
| tax | etnews.com | 방미통위, 구글·애플 인앱결제 강제에 총 637억원 과징금…외부결제 허... | https://www.etnews.com/20261028000439 |  |
| tax | yna.co.kr | 구글·애플에 과징금 637억원…인앱결제 강제 첫 제재(종합) | https://www.yna.co.kr/view/AKR20261028139252017?input=1195m |  |
| tax | digitaltoday.co.kr | 방미통위, 구글·애플 '인앱결제 꼼수' 제동...637억 과징금 부과 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=710715 |  |
| tax | 머니투데이 | 3년 고심 끝 결론…구글·애플 '인앱결제 강제' 637.1억 과징금 부과 | https://www.mt.co.kr/tech/2026/10/28/2026102815445256453 |  |
| tax | zdnet.co.kr | '인앱결제 강제' 구글·애플에 과징금 637억원 | https://zdnet.co.kr/view/?no=20261028163737 |  |
| tax | 파이낸셜뉴스 | 구글·애플 '인앱결제 갑질'에 과징금 637억…3년 만에 제재 확정 | https://www.fnnews.com/news/202610281512312261 |  |
| tax | inews24.com | 정부, '인앱결제 강제' 구글·애플에 과징금 637억원 부과 | http://www.inews24.com/view/2020045 |  |
| tax | biz.heraldcorp.com | [속보] 인앱결제 강제 ‘철퇴’…구글 429억, 애플 208억 과징금 | https://biz.heraldcorp.com/article/10917995?ref=naver |  |
| tax | 서울경제 | [속보] 방미통위, ‘인앱결제’ 구글 429억원·애플 208억1천만원 과징금 | https://www.sedaily.com/article/20107273?ref=naver |  |
| tax | biz.chosun.com | 방미통위, 구글·애플에 인앱 결제 과징금… 구글 429억·애플 208억 | https://biz.chosun.com/it-science/ict/2026/10/28/BBJGOVDNSFGXNJKWV2BMY6IYXY/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| tax | biz.newdaily.co.kr | 방미통위, '인앱결제 강제' 구글·애플에 총 637억 과징금 … 외부결제 ... | https://biz.newdaily.co.kr/site/data/html/2026/10/28/2026102800341.html |  |
| tax | dailian.co.kr | 애플·구글, 인앱결제 강제 등 위법행위…과징금 637억원 부과 | https://www.dailian.co.kr/news/view/1707513/?sc=Naver |  |
| tax | asiatoday.co.kr | 방미통위, 구글·애플에 과징금 637억…외부결제 허용·수수료 개선 명... | https://www.asiatoday.co.kr/kn/view.php?key=20261028010010063 |  |
| tax | newsis.com | 방미통위, 구글·애플에 637억 과징금 철퇴…'앱 마켓 갑질' 첫 법 집행 | https://www.newsis.com/view/NISX20261028_0003845029 |  |
| tax | news1.kr | 구글·애플 '인앱결제 강제' 과징금 637억…3년만에 제재 | https://www.news1.kr/it-science/mobile/6335108 |  |
| tax | mygoyang.com | "수도권 역차별 딛고 서북부 잇는다"...인천2호선 고양연장 예타 통과 해... | http://www.mygoyang.com/news/articleView.html?idxno=90950 |  |
| tax | news.mtn.co.kr | [단독] 볼보코리아, 차량 결함 알고도 1250억원어치 판매…과징금 22억 | https://news.mtn.co.kr/article/2026102714363858477 |  |
| tax | ajunews.com | 손님 줄고 세금은 늘고…생맥주 주세 감면 종료 앞둔 호프집 '한숨' | https://www.ajunews.com/view/20261028144930532 |  |
| tax | 한국세정신문 | 과세자료 일괄 제출 시 운송비용 제출 요건 완화한다 | https://www.taxtimes.co.kr/news/article.html?no=277507 |  |
| tax | kor.theasian.asia | [아시아라운드업 20261028] 프랑스 축구선수 음바페 '마오쩌둥 희화화' ... | http://kor.theasian.asia/archives/420070 |  |
| tax | gukjenews.com | 문진석 의원, 소상공인 우대공제 연장 법안 대표발의…2029년까지 혜택 ... | https://www.gukjenews.com/news/articleView.html?idxno=3734585 |  |
| tax | pointe.co.kr | 매출 7억7000만원이면 공제 500만원 줄어…문진석 "우대공제 연장" | https://www.pointe.co.kr/news/articleView.html?idxno=86672 |  |
| tax | breaknews.com | 문진석 의원 "소상공인 카드 매출 우대공제 3년 연장해야" 개정안 발의 | http://www.breaknews.com/1246012 |  |
| tax | dynews.co.kr | 문진석 의원, 소상공인 매출세액 우대공제 3년 연장 추진 | https://www.dynews.co.kr/news/articleView.html?idxno=871213 |  |
| tax | dream.kotra.or.kr | 2027년 예산안 엿보기: 거시경제 시나리오와 재정운영 방향 점검 | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=80&CONTENTS_NO=2&bbsGbn=242&bbsSn=242&pNttSn=244876 |  |
| tax | chungnamilbo.co.kr | 문진석 의원, '소상공인 보호' 매출액 세액공제 일몰연장법 대표발의 | http://www.chungnamilbo.co.kr/news/articleView.html?idxno=917094 |  |
| tax | sisanews24.co.kr | 문진석 의원, 소상공인 세액공제 3년 연장 법안 발의 | http://www.sisanews24.co.kr/19742 |  |
| tax | 서울경제 | 문진석, 소상공인 카드매출 세액공제 3년 연장 추진 | https://www.sedaily.com/article/20106425?ref=naver |  |
| tax | 한국세정신문 | 문진석 "신용카드 매출 우대공제 3년 연장…1.3%·1천만원 유지" | https://www.taxtimes.co.kr/news/article.html?no=277473 |  |
| tax | hansbiz.co.kr | 신용카드 매출세액 우대공제 3년 연장 추진…공제율·한도 유지 | http://www.hansbiz.co.kr/news/articleView.html?idxno=876515 |  |
| tax | yonhapnewstv.co.kr | 서울 아파트값 상승폭 2주째 둔화…강남3구 하락폭 확대 | http://www.yonhapnewstv.co.kr/news/MYH20261029180205Nfz |  |
| tax | 매일경제 | 강남 약세·강북 강세 내년까지 계속…"稅규제 완화는 기대 접어야" | https://www.mk.co.kr/article/12190185 |  |
| tax | 매일경제 | 가격 떨어진 지금이 적기 … 빌딩 CEO 돼라 | https://www.mk.co.kr/article/12190188 |  |
| tax | wowtv.co.kr | [단독] '주가누르기 방지' 끝장토론 한다…"11월말 처리" | http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202610290166&t=NN |  |
| tax | 매일경제 | 실거주·가격 따라 세부담 차등…똘똘한 한채도 '계속 살 집인가' 따져... | https://www.mk.co.kr/article/12189963 |  |
| tax | imnews.imbc.com | [포커스] '주가 누르기' 끝낼 수 없나‥정부안 부족하다면 어떻게? | https://imnews.imbc.com/replay/2026/nw1400/article/6861681_36974.html |  |
| tax | newspim.com | 서울 아파트값 0.09%↑ 90주 연속 상승…강남·서초는 12주째 하락 | https://www.newspim.com/news/view/20261029000862 |  |
| tax | 서울경제 | “1년 전에 38억에 팔렸는데 7억 떨어져”…은마 집주인들 줄줄이 내놨... | https://www.sedaily.com/article/20107710?ref=naver |  |
| tax | biz.heraldcorp.com | 빵집 열면 상속세 ‘0원’?…실제 경영이 절세 관건 [헤럴딥_이세상_가... | https://biz.heraldcorp.com/article/10918832?ref=naver |  |
| tax | insight.co.kr | 압구정 신현대11차 128억 찍더니 93억 거래... 강남 재건축에 무슨 일이 | https://www.insight.co.kr/news/579663 |  |
| tax | segye.com | 퇴직금 ‘일시금’ 신청 안 하면 연금으로 자동 지급 검토 | https://www.segye.com/newsView/20261029506084?OutUrl=naver |  |
| tax | news.tvchosun.com | 퇴직급여 사외적립 2028년부터 단계 의무화…100인 이상 사업장부터 적... | https://news.tvchosun.com/site/data/html_dir/2026/10/29/2026102990085.html |  |
| tax | news.einfomax.co.kr | 매도 우위라는데 집값 상승세 여전…'강남권 매물발' 착시일까 | https://news.einfomax.co.kr/news/articleView.html?idxno=4441771 |  |
| tax | sejungilbo.com | 정일영, 노선여객자동차 운송사업, 가업상속공제 대상 포함 추진 | https://www.sejungilbo.com/news/articleView.html?idxno=60854 |  |
| tax | fntimes.com | [KFT 모닝 브리프] 2026.10.29 — 오늘 꼭 알아야 할 국내외 경제뉴스 | https://www.fntimes.com/html/view.php?ud=202610290707592832141825007d_18 |  |
| tax | news.sbs.co.kr | 무려 35억 싸게 팔렸다…"빨리 처분해야" 곳곳서 비상 | https://news.sbs.co.kr/news/endPage.do?news_id=N1008820035&plink=ORI&cooper=NAVER |  |
| tax | 서울경제 | “돈 대줄 테니 차익 나누자”…대출 장벽이 부른 ‘사금융 복마전’ | https://www.sedaily.com/article/20107437?ref=naver |  |
| tax | 머니투데이 | '가상자산 과세' 또 미뤄질까… 결론 못낸 당정, 유예론 무게 | https://www.mt.co.kr/politics/2026/10/29/2026102820004660688 |  |
| tax | news.sbs.co.kr | 압구정 아파트 35억 '뚝'…강남권 추가 하락 부르나 | https://news.sbs.co.kr/news/endPage.do?news_id=N1008819904&plink=ORI&cooper=NAVER |  |
| tax | kmib.co.kr | 강남 집값 주춤한 사이 외곽은 급등… 서민 주거 부담 가중 | https://www.kmib.co.kr/article/20261028502568 |  |
| tax | newsworks.co.kr | 이훈기 의원 "상장주식도 순자산 80% 하한을"…주가누르기 방지법 논의 | https://www.newsworks.co.kr/news/articleView.html?idxno=901180 |  |
| tax | news.sbs.co.kr | "미리 팔자" 흐름에 압구정 아파트 35억 '뚝' | https://news.sbs.co.kr/news/endPage.do?news_id=N1008819722&plink=ORI&cooper=NAVER |  |
| tax | kyeongin.com | 추미애 경기도지사 “국가직 소방공무원 인건비 국가가 책임져야” | https://www.kyeongin.com/article/1773615 |  |
| tax | kyeongin.com | ‘소방재정 설화’ 부승찬, 소방재정 국가책임 강화 위한 법안 발의 | https://www.kyeongin.com/article/1773608 |  |
| tax | 파이낸셜뉴스 | [단독] 전월세난에 분쟁·상담 늘었다… 계약갱신요구권 문의 41% | https://www.fnnews.com/news/202610281821359463 |  |
| tax | 한국경제 | 與 서울 의원들 "이대론 부동산 심판당한다" | https://www.hankyung.com/article/2026102814231 |  |
| tax | ajunews.com | [내우외환 완성차] 친환경차 구매 세제 혜택 줄이는데 전기차 생산공제... | https://www.ajunews.com/view/20261028151907689 |  |
| tax | ajunews.com | [내우외환 완성차] 보조금 우대에도 거센 中 공세…정책 엇박자에 국산... | https://www.ajunews.com/view/20261028152715748 |  |
| tax | newstomato.com | CPTPP에 주52시간까지…후퇴 시작은 '대주주 50억' 원복 | http://www.newstomato.com/ReadNews.aspx?no=1318393&inflow=N |  |
| tax | kmib.co.kr | 강남 집값 주춤한 사이 외곽은 급등… 서민 주거 부담 가중 | https://www.kmib.co.kr/article/20261028501956 |  |
| tax | kihoilbo.co.kr | 소방 vs 공공주택? 일몰 앞둔 담배세분 지방교육세 세원 향방은 | https://www.kihoilbo.co.kr/news/articleView.html?idxno=3039196 |  |
| tax | biz.heraldcorp.com | “집 커봐야 세금만 늘어” 강남 재건축, 84㎡서 59㎡로 줄일래요[부동... | https://biz.heraldcorp.com/article/10917984?ref=naver |  |
| tax | newstomato.com | 매물 8만건 육박…강남 급매 조정·강북 오름폭 축소 | http://www.newstomato.com/ReadNews.aspx?no=1318330&inflow=N |  |
| tax | opinionnews.co.kr | 압구정 35억·잠실 5.6억 하락…분담금 급증에 강남 재건축 매수세 주춤 | http://www.opinionnews.co.kr/news/articleView.html?idxno=146318 |  |
| tax | newspim.com | 현금부자들 다시 강남에 눈 돌렸나…은마아파트 일주일 새 13건 손바뀜 | https://www.newspim.com/news/view/20261028001284 |  |
| tax | inews24.com | 반포에 1801가구 '로또 청약'⋯연말 분양시장 들썩 | http://www.inews24.com/view/2019971 |  |
| tax | inews24.com | 첫 전세 만기 앞둔 올림픽파크포레온…귀한 매물에 '1년 계약'까지 [르포... | http://www.inews24.com/view/2019881 |  |
| tax | hani.co.kr | 서울 아파트 매물 석달 새 32% 증가…강남 중심서 전지역 확대 | https://www.hani.co.kr/arti/economy/property/1284571.html |  |
| tax | biz.heraldcorp.com | “아파트 조심해야, 떨어질 가능성 크다” 박현주 회장 경고…집값 정말... | https://biz.heraldcorp.com/article/10917683?ref=naver |  |
| tax | newspim.com | [중국 특징주] 태국 9월 전기차 수입 2배 넘게 급증…99%가 중국산 | https://www.newspim.com/news/view/20261028001001 |  |
| tax | 머니투데이 | 가상자산 '과세 유예' 결론 못 낸 당정…조만간 유예로 가닥 잡힐 듯 | https://www.mt.co.kr/economy/2026/10/29/2026102811295574075 |  |
| tax | viva100.com | 추미애표 지방세 개편안, 국회서 본격 논의 | https://www.viva100.com/article/20261028500386 |  |
| tax | 서울경제 | ‘노·도·강’ 경매 껑충, 강남은 털썩…규제에 엇갈린 아파트 경매지... | https://www.sedaily.com/article/20107024?ref=naver |  |
| tax | nbntv.kr | [윤준의 부동산수첩] 절세 공식이 무조건 맞지 않는 이유 | https://www.nbntv.kr/news/articleView.html?idxno=340994 |  |
| tax | ytn.co.kr | "은마도 난리났는데, 상계주공도 7억 내라?" | https://www.ytn.co.kr/_ln/0102_202610280845429824 |  |
| tax | view.asiae.co.kr | 38억에 팔렸는데 이젠 7억이나 '뚝'…"1.5억 더 못 내, 집 팔래" 은마 매... | https://view.asiae.co.kr/article/2026102714203862668 |  |
| tax | kukinews.com | 경기도, 지방세제 확충 등 구조개편 토론회 30일 국회서 개최 | https://www.kukinews.com/article/view/kuk202610280007 |  |
| tax | 한국경제 | 운동화 만들다 구두 만들면 '탈락'…혁신까지 막는 가업상속세 개편[중... | https://magazine.hankyung.com/business/article/202610227361b |  |
| tax | 서울경제 | 서울 외곽 경매시장 ‘후끈’…노원 고가 낙찰 비중 1년 새 6배[집슐랭] | https://www.sedaily.com/article/20106835?ref=naver |  |
| tax | ccreview.co.kr | 충북 인구감소지역 6곳 중 4권역은 영동뿐 | https://www.ccreview.co.kr/news/articleView.html?idxno=361041 |  |
| tax | biz.chosun.com | 압구정 고점서 35억 뚝… 강남 재건축에 무슨 일 | https://biz.chosun.com/real_estate/real_estate_general/2026/10/28/F3NFXDQCRFEFTOFA4XD6DX5VGY/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| tax | etoday.co.kr | 전기차도 생산세액공제 검토…국내 車 지원체계 전환 ‘분수령’ [韓 자... | https://www.etoday.co.kr/news/view/2640752 |  |
| tax | 한국경제 | [데스크 칼럼] '닥공' 막는 대못부터 뽑아야 | https://www.hankyung.com/article/2026102786391 |  |
| tax | donga.com | 상의, 국회에 국내생산 세액공제 조속 도입 요청 | https://www.donga.com/news/Economy/article/all/20261027/134920020/2 |  |
| tax | donga.com | 압구정 재건축 20억 이상 하락 거래 잇따라 | https://www.donga.com/news/Economy/article/all/20261027/134920030/2 |  |
| tax | donga.com | [광화문에서/박재명]韓 전기차 절반이 중국산… 국내 생산 불이익은 없... | https://www.donga.com/news/Opinion/article/all/20261027/134920927/2 |  |
| tax | safetynews.co.kr | 추미애, 국회서 경기도 재정위기 돌파 총력…"가용재원 44%, 반드시 해법... | https://www.safetynews.co.kr/news/articleView.html?idxno=251229 |  |
| tax | betanews.net | 소방비 국가 55 대 지방 45…추미애, 국회 찾아 '재정 산소통' 호소 | https://www.betanews.net/article/view/beta202610270179 |  |
| tax | incheonilbo.com | 경기도-의회, '입법·예산' 국회 관철 총력전 | https://www.incheonilbo.com/news/articleView.html?idxno=1335272 |  |
| tax | thepublic.kr | 민주당, 조희대 국정조사 내달 5일 | https://www.thepublic.kr/news/articleView.html?idxno=324000 |  |
| tax | 파이낸셜뉴스 | "국내 車생산 400만대 위태… 생산세액공제로 中에 맞서야" [안방 파고드... | https://www.fnnews.com/news/202610271829466508 |  |
| tax | busan.com | [벼랑 끝 지역 부동산] 곡소리 나는 지역 부동산, 안중에도 없는 정부 | https://www.busan.com/view/busan/view.php?code=2026102718190472908 |  |
| tax | segye.com | 현장 반발에 수정·유예 오락가락… ‘국정 난맥상’ 커진다 [이해충돌... | https://www.segye.com/newsView/20261027516575?OutUrl=naver |  |
| tax | sidae.com | [시대&인터뷰] "반도체 세수 특수는 '선진국형 세제 전환' 절호의 기회"... | https://www.sidae.com/article/2026102710475794665 |  |
| tax | kgnews.co.kr | [지방자치의 완성, 재정에서 시작된다]②세금은 중앙에, 재정 부담은 지... | https://www.kgnews.co.kr/news/article.html?no=916991 |  |
| tax | 서울경제 | 노원 ‘웃돈 낙찰’ 1년새 6배 급증…강남은 제자리 | https://www.sedaily.com/article/20106785?ref=naver |  |
| tax | newsis.com | 전기차 이어 항공유·백신도…국내생산세액공제 확대 요구 빗발 | https://www.newsis.com/view/NISX20261027_0003843365 |  |
| tax | kpinews.kr | 압구정 24억 '뚝'…매도 시한·분담금에 쫓기는 강남 재건축 | https://www.kpinews.kr/newsView/1065595966024436 |  |
| tax | ggilbo.com | 대한상의 "초광역특구법 제정으로 AI데이터센터 기반 마련해야" | https://www.ggilbo.com/news/articleView.html?idxno=1189419 |  |
| tax | donga.com | 대한상의 “국내생산 세액공제 조속 도입·기술유출 처벌 강화해야” | https://www.donga.com/news/Economy/article/all/20261027/134917878/1 |  |
| tax | donga.com | 압구정 재건축 단지 ‘급매물’ 속출…20억원씩 떨어졌다 | https://www.donga.com/news/Economy/article/all/20261027/134917607/1 |  |
| tax | newspim.com | [뉴스분석] '대통령 한마디'에 움직이는 국정…속도는 얻었지만 신뢰는... | https://www.newspim.com/news/view/20261027001196 |  |
| tax | dt.co.kr | 매물 2배 쏟아졌는데… ‘급매 소화’ 강남 vs ‘거래 마비’ 한강벨트 | https://www.dt.co.kr/article/12091566?ref=naver |  |
| tax | yonhapnewstv.co.kr | 대한상의, 국회에 국내생산 세액공제 조기 도입 요청 | http://www.yonhapnewstv.co.kr/news/AKR20261027154243otM |  |
| tax | 머니투데이 | 코인과세, 막판 재유예 무게…전문가 "인프라·기본법 선행돼야" | https://www.mt.co.kr/stock/2026/10/27/2026102715224728897 |  |
| tax | biz.newdaily.co.kr | 강경 메시지 뒤 핵심 정책 줄후퇴 … '라코' 논란에 갇힌 이재명 정부 [... | https://biz.newdaily.co.kr/site/data/html/2026/10/27/2026102700199.html |  |
| tax | pinpointnews.co.kr | 서울 집값 잡히나 했더니…경기로 번지는 매수세 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=498933 |  |
| tax | m-i.kr | [기획] 전세난 심각하자 민간임대 규제 완화론 부상 | https://www.m-i.kr/news/articleView.html?idxno=2010912 |  |
| tax | 파이낸셜뉴스 | "'잘해왔다'는 안이함이 가장 큰 적"…中 전기차와 생산비 격차부터 줄... | https://www.fnnews.com/news/202610271403037510 |  |
| tax | 한국경제 | 이재만 前지방국세청장 "세금 지옥 한국…택스 엑소더스 우려" | https://www.hankyung.com/article/202610278083i |  |
| tax | sateconomy.co.kr | 자동차·철강·석유화학업계, 국내생산세액공제 확대 요구 | https://sateconomy.co.kr/news/view/1065589125405106 |  |
| tax | efnews.co.kr | "성장정책, 현장에서 작동하도록" ... 대한상의, 정기국회에 입법과제 ... | http://www.efnews.co.kr/news/articleView.html?idxno=133487 |  |
| tax | newspim.com | 3분기 서울 땅값 1.26% ↑ 전국 평균 2배…토지거래량은 줄어, 농지 거래... | https://www.newspim.com/news/view/20261027000939 |  |
| tax | bigtanews.co.kr | “지금 집값이 문제” | https://www.bigtanews.co.kr/article/view/big202610270018 |  |
| tax | banronbodo.com | "기업 투자·성장 뒷받침할 입법 시급"... 31개 과제 국회에 건의 | https://www.banronbodo.com/news/articleView.html?idxno=33250 |  |
| tax | 매일경제 | 압구정 아파트 3달 만에 20억원 ‘뚝’…재건축 앞두고 급매 속출 | https://www.mk.co.kr/article/12186880 |  |
| tax | 서울경제 | 테슬라·스페이스X 합병 추진에 서학개미 양도세 비상[마켓무버] | https://www.sedaily.com/article/20104873?ref=naver |  |
| tax | sejungilbo.com | [절세톡톡] 5년내 법인전환 사후관리를 위반한 경우 | https://www.sejungilbo.com/news/articleView.html?idxno=60534 |  |
| tax | 일간NTN | [국세 예규] 유한책임사원 출자지분 증여, 가업승계 증여세 과특 적용 ... | http://www.intn.co.kr/news/articleView.html?idxno=2054195 |  |
| tax | dgmbc.com | [글로벌+] 베트남 수출 업체, 부가세 환급받는다!···노점상 풍경 변화... | https://dgmbc.com/NewsArticle/868677 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(62) 지하층만 남은 건물, 과연 '나대지'인가? | http://www.intn.co.kr/news/articleView.html?idxno=2054203 |  |
| tax | sejungilbo.com | [법원] "합병 결손금, 미환류소득서 중복 차감 불가"…국세청 '승리' | https://www.sejungilbo.com/news/articleView.html?idxno=60725 |  |
| tax | ferrotimes.com | 베트남 진출기업 부가세 환급길 열려…장기 지연 애로 해소 | http://www.ferrotimes.com/news/articleView.html?idxno=51011 |  |
| tax | taxwatch.co.kr | 세금만 잘 계산하면 좋은 세무사?…세무상담의 함정 | https://www.taxwatch.co.kr/article/tax/2026/10/19/0003/naver |  |
| tax | viva100.com | 베트남 내국수출입 부가가치세 환급 소급 적용 방침 | https://www.viva100.com/article/20261021500003 |  |
| tax | busan.com | 베트남, 내국수출입 부가세 환급 소급적용…한국기업 유동성에 큰 도움... | https://www.busan.com/view/busan/view.php?code=2026102017145939514 |  |
| tax | polinews.co.kr | 수출 경쟁력 가르는 현지 규제…인증·통관·세무 부담 해법 | https://www.polinews.co.kr/news/articleView.html?idxno=746301 |  |
| tax | dnews.co.kr | 베트남에 묶인 韓기업 400억 부가세, 4년 만에 풀린다 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610201401483130324 |  |
| tax | hellot.net | 정부, 3년 넘게 막힌 베트남 부가세 환급 길 열어...진출기업 유동성 숨... | https://www.hellot.net/news/article.html?no=115621 |  |
| tax | naeil.com | 베트남 진출기업 ‘부가세 사태’ 해결 | https://www.naeil.com/news/read/605679?ref=naver |  |
| tax | straightnews.co.kr | 베트남 진출기업 '부가세 환급 지연' 해결…400억원 이상 자금 부담 완화... | https://www.straightnews.co.kr/news/articleView.html?idxno=313518 |  |
| tax | nbntv.kr | 국세청, 산업통상부·외교부와 베트남 진출기업 최대 난제 '내국수출입... | https://www.nbntv.kr/news/articleView.html?idxno=340989 |  |
| tax | pinpointnews.co.kr | 베트남 진출기업의 내국수출입 부가가치세 환급 길 열렸다 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=496751 |  |
| tax | 일간NTN | [국세 예규] 출연재산 매각대금 사용인 인건비로 지출했다면? 공익목적... | http://www.intn.co.kr/news/articleView.html?idxno=2054048 |  |
| tax | 일간NTN | 베트남 진출기업 부가세 환급길 열려…세무 불확실성 해소 큰 도움 | http://www.intn.co.kr/news/articleView.html?idxno=2054159 |  |
| tax | etnews.com | 베트남 진출 한국기업 부가세 환급길 열렸다…최소 400억원 규모 | https://www.etnews.com/20261019000431 |  |
| tax | tfmedia.co.kr | 묶였던 부가세 환급에 발 동동…범부처 공조로 베트남 진출 기업 숙원 ... | https://www.tfmedia.co.kr/news/article.html?no=208162 |  |
| tax | news1.kr | 베트남 진출기업 '부가세 환급' 숙원 풀려…법 개정 전 거래도 소급 | https://www.news1.kr/economy/trend/6325051 |  |
| tax | news.einfomax.co.kr | 李대통령 "베트남, 韓기업에 부가세 환급 소급 적용…최소 400억 규모" | https://news.einfomax.co.kr/news/articleView.html?idxno=4440003 |  |
| tax | 일간NTN | 베트남 '내국수출입 VAT 소급 환급' 길 열렸다…400억원대 환급 지연 사... | http://www.intn.co.kr/news/articleView.html?idxno=2054158 |  |
| tax | 조세일보 | 베트남 진출기업 부가세 환급 가능해져…과거 거래도 대상 | http://www.joseilbo.com/news/news_read.php?uid=577706&class=7&grp= |  |
| tax | 한국세정신문 | 베트남 진출기업 내국수출입 부가가치세 환급 길 열려 | https://www.taxtimes.co.kr/news/article.html?no=277366 |  |
| tax | 파이낸셜뉴스 | 베트남 진출 기업 최대 애로 '내국수출입 부가가치세 환급지연' 해결 | https://www.fnnews.com/news/202610191714419790 |  |
| tax | sejungilbo.com | 베트남 진출기업 부가세 환급 지연 해결…400억원 이상 환급 길 열렸다 | https://www.sejungilbo.com/news/articleView.html?idxno=60696 |  |
| tax | sejungilbo.com | [판세] 과세전적부심사 기회 안준 경우, 당초 처분 취소하고 재처분 할... | https://www.sejungilbo.com/news/articleView.html?idxno=60480 |  |
| tax | munhwa.com | 국감에서 한전기술이 긍정 사례로 거론된 ‘감사원 사전컨설팅’이란? | https://www.munhwa.com/article/11624283?ref=naver |  |
| tax | 한국세정신문 | "한시간 내 의견서 작성" 센트릭 택스 AI 강력한 기능 눈길 | https://www.taxtimes.co.kr/news/article.html?no=277326 |  |
| tax | seoul.co.kr | 분양가 25%만 내고 입주… GH ‘지분적립형 주택’ 연내 첫선 | https://www.seoul.co.kr/news/publicnews/local_govern/news_local/2026/10/14/20261014021001?wlog_tag3=naver |  |
| tax | dailian.co.kr | “술도 집 앞 배송 안 되나요?”…마트·주점·도매상까지 얽힌 ‘속사... | https://www.dailian.co.kr/news/view/1700461/?sc=Naver |  |
| tax | taxwatch.co.kr | [인터뷰]"코인 스테이킹 과세, 고시만으론 한계…법적 기준 정해야" | https://www.taxwatch.co.kr/article/tax/2026/09/30/0004/naver |  |
| tax | imaeil.com | 부동산 중개수수료 요율표는 상한…부가세 10%, 간이과세 중개업소는 4... | https://www.imaeil.com/page/view/2026101018554473359 |  |
| tax | donga.com | [오늘과 내일/조건희]보이스피싱 ‘칸막이 철거’, 민생 범죄 대응 원칙... | https://www.donga.com/news/Opinion/article/all/20261009/134816529/2 |  |
| tax | sisajournal.com | 78년 형사사법 방파제 무너진 자리…범죄는 질주하고 수사는 표류했다 | https://www.sisajournal.com/news/articleView.html?idxno=389531 |  |
| tax | labortoday.co.kr | [단독] 단체교섭 판단지원위 사용자성 판단 69.3일 걸렸다 | https://www.labortoday.co.kr/news/articleView.html?idxno=237091 |  |
| tax | chosun.com | [단독] 노란봉투법 사용자성 질의 138건… 판단위가 결론 낸 건 10건 | https://www.chosun.com/national/labor/2026/10/03/Q63VUXUYTZALTNUDLCXO6FDABA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | tfmedia.co.kr | [초대석] 김선명 세무사회 부회장, "회원이 현장의 눈, 한국세무사회가... | https://www.tfmedia.co.kr/news/article.html?no=207672 |  |
| tax | junggi.co.kr | 주식증여·이익소각으로 가지급금 정리…승계는 12년 준비 | https://www.junggi.co.kr/news/articleView.html?idxno=37964 |  |
| tax | wikitree.co.kr | 한동훈 “CARF 20%도 못 잡아”…가상자산 과세 2년 유예 요구에 정부는... | https://www.wikitree.co.kr/articles/1162864 |  |
| tax | sejungilbo.com | [판세] 분식회계로 꾸며 임직원들에게 지급한 성과급의 손금불산입 여부 | https://www.sejungilbo.com/news/articleView.html?idxno=60073 |  |
| tax | 이데일리 | “엄마, 이번에 1000만원 드릴게”…추석 용돈에도 세금 붙나요 | https://www.edaily.co.kr/News/Read?newsId=01722006645583400&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | 조세일보 | "늦은 공제 적용, 농특세 가산세는 어떻게?" [세무상담] | http://www.joseilbo.com/news/news_read.php?uid=576080&class=7&grp= |  |
| tax | widedaily.com | "코인 과세 앞두고 자금 유출 우려"…국회 예정처, 국내 거래소 세제 유... | https://www.widedaily.com/news/articleView.html?idxno=301287 |  |
| tax | 조세일보 | 진료비 본인부담금, 현금영수증 미발급 신고하면 포상금 나올까 [국세 ... | http://www.joseilbo.com/news/news_read.php?uid=575949&class=7&grp= |  |
| tax | 일간NTN | [국세 예규] 상시 주거용 임대 오피스텔 양도 때 부가세는? "사실판단 해... | http://www.intn.co.kr/news/articleView.html?idxno=2053355 |  |
| tax | chosun.com | 혼수 자금, 집값에 보태면 증여일까?...뒤탈 없이 절세하는 법 | https://www.chosun.com/special/2026/09/16/KSQHRZ5DSZETJLYMAWCLIBINUM/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | straightnews.co.kr | [심층] "장보러 안동까지"… 영양식자재마트 상품권 '불허 압박'에 뿔난... | https://www.straightnews.co.kr/news/articleView.html?idxno=311053 |  |
| tax | sejungilbo.com | [절세톡톡] 매매계약에 따라 상가로 용도변경후 양도한 경우 부가가치세... | https://www.sejungilbo.com/news/articleView.html?idxno=59962 |  |
| tax | legaltimes.co.kr | [Who's Who Legal Korea 2026] 공정거래 | http://www.legaltimes.co.kr/news/articleView.html?idxno=95851 |  |
| tax | 조세일보 | 세무법인 센트릭, 'CENTRIC TAX AI' 출범…전문가용 AI 본격 가동 | http://www.joseilbo.com/news/news_read.php?uid=575230&class=10&grp= |  |
| tax | tfmedia.co.kr | [현장] 센트릭은 왜 '세무 전용 AI'를 만들었나...50만건 DB로 차별화 | https://www.tfmedia.co.kr/news/article.html?no=207039 |  |
| tax | 한국세정신문 | 세무법인 센트릭, 택스 AI 런칭세미나 성료 "조세전문가 모이는 중심될... | https://www.taxtimes.co.kr/news/article.html?no=276746 |  |
| tax | 조세일보 | "질문 취소하세요~" 종용도…바빠서 답변 못한다는 세제실 | http://www.joseilbo.com/news/news_read.php?uid=575207&class=7&grp= |  |
| tax | tfmedia.co.kr | [펜타곤의 택스노트] 전근·취학·간병으로 집 비웠다면…‘실거주’ 어... | https://www.tfmedia.co.kr/news/article.html?no=206924 |  |
| tax | christiantoday.co.kr | 해외선교 과세 시행령 적용 시 발생할 5대 핵심 문제점 | https://www.christiantoday.co.kr/news/377049 |  |
| tax | news.kbs.co.kr | [전격시사] 박용진 규제합리화위원회 부위원장 - “잘 되라는 것 아니라... | https://news.kbs.co.kr/news/pc/view/view.do?ncd=8647723&ref=A |  |
| tax | fntimes.com | ‘황제주택’ 다음은 금융권?…은행·증권사도 법인자산 점검 | https://www.fntimes.com/html/view.php?ud=2026082611145718362a735e27af_18 |  |
| tax | 매일경제 | “지갑 옮기면 끝?”…가상자산 해외 신고와 소득 과세의 오해 [가온 택... | https://www.mk.co.kr/article/12135538 |  |
| tax | view.asiae.co.kr | 부동산 비율 '49%'로 낮춰 양도세 249억 덜 냈는데…인천국세청 15개월 ... | https://view.asiae.co.kr/article/2026082512095065091 |  |
| tax | 일간NTN | [국세 예규] 거래 단계별 총액 세금계산서 각각 발급·수취?...."사실판단... | http://www.intn.co.kr/news/articleView.html?idxno=2052654 |  |
| tax | 조세일보 | 5조원 원익그룹 지배하는 호라이즌 보통주는 단 15주, 의도는? [기업분석... | http://www.joseilbo.com/news/news_read.php?uid=574393&class=17&grp= |  |
| tax | 한국경제 | 불붙은 고려아연 분쟁, 다시 법정으로…9월 주총 '표 싸움' 시작됐다 | https://magazine.hankyung.com/business/article/202608202210b |  |
| tax | hapt.co.kr | 승강기 교체부터 고철 매각까지 세무･회계처리 | https://www.hapt.co.kr/news/articleView.html?idxno=169253 |  |
| tax | tfmedia.co.kr | [전문가 기고] 코인 세금, 두 가지를 모르면 계산이 틀린다...교환 과세... | https://www.tfmedia.co.kr/news/article.html?no=206316 |  |
| tax | 일간NTN | "양도세 계산은 양자컴퓨터가?" 부동산 세금계산, '경우의 수' 너무 많다 | http://www.intn.co.kr/news/articleView.html?idxno=2052415 |  |
| tax | sejungilbo.com | [판세] 공동상속인의 상속세 연대납부 '상속세 대상'일까? | https://www.sejungilbo.com/news/articleView.html?idxno=59365 |  |
| tax | news.bizwatch.co.kr | "오른 양도세, 결국 매수자에"…'손피' 부활할까? | https://news.bizwatch.co.kr/article/real_estate/2026/08/05/0024 |  |
| tax | 한국경제 | 전세 줄고 매물 잠길라…난해한 부동산 세제 '4가지 맹점' | https://www.hankyung.com/article/2026080447651 |  |
| tax | sejungilbo.com | [판세] 금융기관이 대부중개수수료 상한제를 위반하여 지급한 수수료의... | https://www.sejungilbo.com/news/articleView.html?idxno=59363 |  |
| tax | sejungilbo.com | "철거할 건물인데 부가세 환급"…국세청 자체감사서 매입세액 공제 오류... | https://www.sejungilbo.com/news/articleView.html?idxno=59446 |  |
| tax | news.einfomax.co.kr | [이효지의 숫자 너머] 귀하신 몸이었는데…궁지에 몰린 임대사업자 | https://news.einfomax.co.kr/news/articleView.html?idxno=4427998 |  |
| tax | newspim.com | 더 편리해진 학자금상환…국세청, 증빙서류 없어도 상환유예 'OK' | https://www.newspim.com/news/view/20260728000424 |  |
| tax | kfenews.co.kr | [기획] 7000억 판 깐 정부…'여수 빅딜' 롯데·한화·DL 적자 털까 | https://www.kfenews.co.kr/news/articleView.html?idxno=661194 |  |
| tax | taxwatch.co.kr | 심판원 결정 번복?…국세청, 재심리 추진에 납세자 부담 우려 | https://www.taxwatch.co.kr/article/tax/2026/07/24/0001/naver |  |
| tax | thepowernews.co.kr | 정부, 여수 석화 재편에 7000억 지원…NCC 2기 멈추고 통합법인 만든다 | https://www.thepowernews.co.kr/view.php?ud=202607221342161463de3f0aa1be_7 |  |
| tax | 한국세정신문 | 여수 1호 석화 사업재편 시동…정부, 7천억원 규모 패키지 지원 | https://www.taxtimes.co.kr/news/article.html?no=276086 |  |
| tax | dream.kotra.or.kr | UAE 법인세 도입 후 첫 시행 1년, 기업 주요 문의사항과 연방국세청 답... | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=100&CONTENTS_NO=1&bbsGbn=322&bbsSn=322&pNttSn=242799 |  |
| tax | 일간NTN | [국세 예규] 상시 주거용 임대 오피스텔 양도 때 부가세는? "사실판단 해... | http://www.intn.co.kr/news/articleView.html?idxno=2051869 |  |
| tax | 한국경제 | "직관러들 이젠 굶지 마요" 야구장서 갓 만든 핫도그 판다 | https://www.hankyung.com/article/202607131189i |  |
| tax | 이데일리 | 비트코인의 다양한 분류 | https://www.edaily.co.kr/news/newspath.asp?newsid=01407126645514192 |  |
| tax | 한국경제 | 기업 규제가 키운 로펌…컨설팅·로비 영역까지 장악했다 | https://www.hankyung.com/article/2026070836051 |  |
| tax | tfmedia.co.kr | [데스크 칼럼] 신탁시장 전성시대…시장보다 제도가 먼저다 | https://www.tfmedia.co.kr/news/article.html?no=205573 |  |
| tax | 일간NTN | [국세 예규] 임원·종업원 계열의료기관 비과세 초과 할인금액...."근로... | http://www.intn.co.kr/news/articleView.html?idxno=2051653 |  |
| tax | segye.com | 분양가 10∼25%만 내고 입주… ‘적금 주택’ 실험 궤도에 [오상도의 경... | https://www.segye.com/newsView/20260705507589?OutUrl=naver |  |
| tax | ifs.or.kr | 미국 CLARITY Act 법안의 가상자산 관련 AML 정책 방향 | http://www.ifs.or.kr/bbs/board.php?bo_table=News&wr_id=55873 |  |
| tax | 한국경제 | 세무조사가 달라졌다…'율촌 조세진단팀' 최정예 원팀으로 선제 대응 | https://magazine.hankyung.com/money/article/202606160208c |  |
| tax | greened.kr | 법원 판례 무시한 용인시 행정…공익사업 부가세 10억 자초한 재정 손실 | https://www.greened.kr/news/articleView.html?idxno=343822 |  |
| tax | 한국세정신문 | [초점]연 27조 취득세 '구멍'…성실신고확인제 도입 불 붙나? | https://www.taxtimes.co.kr/news/article.html?no=275760 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(37) 국경을 넘는 지식재산권 서비스와 부가가... | http://www.intn.co.kr/news/articleView.html?idxno=2051628 |  |
| tax | taxwatch.co.kr | 특수관계 거래의 함정…'시가'가 세무리스크 가른다 | https://www.taxwatch.co.kr/article/tax/2026/06/24/0002/naver |  |
| tax | econovill.com | 세무조사관은 털어서 '먼지' 만들러 옵니다 [CEO 상식의 배신] | https://www.econovill.com/news/articleView.html?idxno=743628 |  |
| tax | fieldnews.kr | [단독] 경기주택도시공사, 공공임대 지으려 빈집 철거했다가 취득세 추... | http://www.fieldnews.kr/news/articleView.html?idxno=32624 |  |
| tax | tfmedia.co.kr | [전문가 칼럼] 반복되는 가상자산 과세 유예 논의, 2020년 설계된 과세체... | https://www.tfmedia.co.kr/news/article.html?no=208431 |  |
| tax | fieldnews.kr | [단독] 대방건설, 자회사 돈 늦게 받고 보증은 공짜로…심판원 '부당행... | http://www.fieldnews.kr/news/articleView.html?idxno=32580 |  |
| tax | sejungilbo.com | [판세] 미국에 주소지 둔 원고에게 증여세 납세고지서 공시송달 적법한... | https://www.sejungilbo.com/news/articleView.html?idxno=60673 |  |
| tax | 한국세정신문 | 억울함 막겠다는 국세청…정작 납세자 알 권리는 어디에? | https://www.taxtimes.co.kr/news/article.html?no=277469 |  |
| tax | 이데일리 | 입사 반년 만에 대표된 창업주 장남…국세청에 ‘고액연봉’ 딱 걸려[세... | https://www.edaily.co.kr/News/Read?newsId=01138166645616528&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | 이데일리 | “세금 꼬박꼬박 냈는데”…9년 보유한 집, 양도세 비과세 거절된 이유... | https://www.edaily.co.kr/News/Read?newsId=01079126645616200&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | 머니투데이 | 국세청 조세불복 결정서 94% 비공개…'공개 원칙' 무색 | https://www.mt.co.kr/politics/2026/10/23/2026102310101814451 |  |
| tax | sejungilbo.com | [법원] 16년간 부동산 개발 돕고 받은 31억…법원 "전액 과세 정당" | https://www.sejungilbo.com/news/articleView.html?idxno=60737 |  |
| tax | sisajournal.com | 누가 대통령에게 'NO'를 외치나…李 '만기친람'의 함정 | https://www.sisajournal.com/news/articleView.html?idxno=391193 |  |
| tax | 한국세정신문 | 성공한 사람들의 공통점?…꿈·혁신·감사 습관과 좋은 만남 | https://www.taxtimes.co.kr/news/article.html?no=277415 |  |
| tax | ichannela.com | 인터뷰 전문: 차호 “청와대 국감 반나절만 하는 것은 본 적이 없다, 국... | https://www.ichannela.com/news/main/news_detailPage.do?publishId=000000556286 |  |
| tax | 일간NTN | 이용섭 전 장관 "전문성의 세무사가 나서면 세상 바꿀 수 있다" | http://www.intn.co.kr/news/articleView.html?idxno=2054242 |  |
| tax | news.kbs.co.kr | [전격시사] 최은석 국민의힘 의원 - “국민 기대 짓밟아…레버리지 손실... | https://news.kbs.co.kr/news/pc/view/view.do?ncd=8692226&ref=A |  |
| tax | bigtanews.co.kr | [세무, 아! 그렇군] 부모 전세보증금은 ‘대출’ 아닌 ‘임차권’ | https://www.bigtanews.co.kr/article/view/big202610200020 |  |
| tax | thepublic.kr | 김현지 남편 세무법인, 석 달 새 6명 중 3명 '자리 꿰찼다' | https://www.thepublic.kr/news/articleView.html?idxno=323120 |  |
| tax | newsen.com | 이영애 ‘의녀 대장금’ 언제 보나? 차은우 소속사 169억 자금조달 연기 | https://www.newsen.com/news_view.php?uid=202610211147271910 |  |
| tax | joongang.co.kr | 국세청장이 웬 비서실장? 임광현, 이재명 만남 전 적은 ‘메모’ | https://www.joongang.co.kr/article/25471450 |  |
| tax | pennmike.com | [막전막후] 김현지 논란, 남편과 결혼식 주례로까지 번져…민주당은 국... | https://www.pennmike.com/news/articleView.html?idxno=129941 |  |
| tax | dailian.co.kr | [데일리안 오늘뉴스 종합] 노태우 비자금 수사 속 '550평 호화 묘역' 유... | https://www.dailian.co.kr/news/view/1703864/?sc=Naver |  |
| tax | lawtalknews.co.kr | '상속세 신고 늦었다' 상속재산이 공시지가로 평가…바로 소송 낼 수 있... | https://lawtalknews.co.kr/article/IZQL03WCX9OE |  |
| tax | fieldnews.kr | [단독] 농가 지원비도 '광고비'라는 농협네트웍스…조세심판원 제동 | http://www.fieldnews.kr/news/articleView.html?idxno=32376 |  |
| tax | sisafocus.co.kr | 국힘, ETF·국민연금 특검 추진 거듭 강조 | http://www.sisafocus.co.kr/news/articleView.html?idxno=366441 |  |
| tax | dailian.co.kr | 김현지 남편 세무법인서 '조세심판관'까지 나왔다 | https://www.dailian.co.kr/news/view/1703503/?sc=Naver |  |
| tax | thebell.co.kr | [더벨][thebell desk] 날카로워진 칼날 '공정위'의 역할 | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202610151533441560102533 |  |
| tax | donga.com | 이찬진 “레버리지 ETF, 상장 일정 맞추려 심사 빨리 진행” | https://www.donga.com/news/Economy/article/all/20261020/134870759/2 |  |
| tax | joongang.co.kr | 김현지 남편 세무법인에서 ‘조세심판관’도 나왔다 | https://www.joongang.co.kr/article/25471087 |  |
| tax | pressian.com | '김현지 남편 세무법인 인사 조세심판관 위촉' 논란에 총리실 "적법 절... | https://www.pressian.com/pages/articles/2026101920460818404?utm_source=naver&utm_medium=search |  |
| tax | kukinews.com | 김현지 남편 세무법인서 사외이사·조세심판관 줄줄이…“인사 개입” | https://www.kukinews.com/article/view/kuk202610190216 |  |
| tax | newsis.com | 총리실, '김현지 남편 세무법인 인사 조세심판관 위촉' 논란 제기에 "적... | https://www.newsis.com/view/NISX20261019_0003832335 |  |
| tax | 한국경제 | 김현지 남편 세무법인서 조세심판관 나와 | https://www.hankyung.com/article/2026101915001 |  |
| tax | bigtanews.co.kr | [쇼츠뉴스] 차용증 원본 없는데 증여세 0원, 왜? | https://www.bigtanews.co.kr/article/view/big202610160010 |  |
| tax | donga.com | 이찬진 “레버리지 ETF, 상장 일정 맞추려 빨리 심사”…‘졸속’ 인정 | https://www.donga.com/news/Economy/article/all/20261019/134867017/1 |  |
| tax | thepublic.kr | 김현지 배우자 출자 세무법인서 조세심판관 나와...野 "인맥 자리 나눠... | https://www.thepublic.kr/news/articleView.html?idxno=322735 |  |
| tax | smarttimes.co.kr | 김현지 배우자 출자 '택스탑' 출신, KB·우리캐피탈 사외이사 선임…금... | http://www.smarttimes.co.kr/news/articleView.html?idxno=49834 |  |
| tax | newdaily.co.kr | '김현지 남편' 세무법인서 조세심판관도 배출 … 野 "조직적 인사 농단... | https://www.newdaily.co.kr/site/data/html/2026/10/19/2026101900261.html |  |
| tax | tfmedia.co.kr | [2026 국감] “금융사 이사회에 갖다 꽂았나”…김현지 배우자 세무법인... | https://www.tfmedia.co.kr/news/article.html?no=208137 |  |
| tax | 한국경제 | 김현지 실장 남편 세무법인 인사, 조세심판원 비상임심판원 위촉 | https://www.hankyung.com/article/202610190408i |  |
| tax | ebn.co.kr | "김현지 배우자 세무법인 인사, 우리·KB캐피탈로…인사 개입 의혹" | https://www.ebn.co.kr/news/articleView.html?idxno=1728321 |  |
| tax | joongang.co.kr | [단독] 김현지 배우자 세무법인서 ‘조세심판관’도 배출, 李 캠프 출신... | https://www.joongang.co.kr/article/25470831 |  |
| tax | tvreport.co.kr | '탈세 논란' 차은우, 1월 전역→복귀작부터 난항?…문가영과 7년 만 재회... | https://www.tvreport.co.kr/entertainment/article/1084111/ |  |
| tax | civicnews.com | [부산 변호사 한변의 리얼상담실64] 자동말소 종부세, 소득보다 큰 세금... | http://www.civicnews.com/news/articleView.html?idxno=40501 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(61) '과거 실적의 함정'에 갇힌 비상장주식 평... | http://www.intn.co.kr/news/articleView.html?idxno=2054091 |  |
| tax | sejungilbo.com | [절세톡톡] 수정신고와 중소기업특별세액감면 | https://www.sejungilbo.com/news/articleView.html?idxno=60533 |  |
| tax | dkilbo.com | "무리한 세무조사가 국민 벼랑 끝 내몰았다" | https://www.dkilbo.com/news/articleView.html?idxno=557454 |  |
| tax | hidomin.com | 대구·경북 경기침체에 국감서 쓴소리…"지역경제 살릴 실효성 있는 대... | https://www.hidomin.com/news/articleView.html?idxno=725280 |  |
| tax | 일간NTN | [국세신문 창간 38주년 축사] 이상길 조세심판원장 | http://www.intn.co.kr/news/articleView.html?idxno=2054119 |  |
| tax | 이데일리 | 스테이블코인, 위기 때도 안정적인가 | https://www.edaily.co.kr/News/Read?newsId=01233286645614232&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | wikitree.co.kr | [법과 생활] 공시송달 판결·심판 결정마다 되풀이되는 세무 절차 하자... | https://www.wikitree.co.kr/articles/1166962 |  |
| tax | 머니투데이 | [TheTax]집 팔고 사망한 父, 자녀 상속 포기했는데…대신 양도세 내라? | https://www.mt.co.kr/economy/2026/10/17/2026101616084061317 |  |
| tax | 이데일리 | “4년 농사지었는데”…취득세 절반 날린 '5개월'[세금, 그 후] | https://www.edaily.co.kr/News/Read?newsId=01079126645613904&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | tbc.co.kr | "경제 살릴 방안은?"...지역 경제기관 국감 | https://www.tbc.co.kr/news/view?pno=20261016170548AE07006&id=212239 |  |
| tax | dgmbc.com | "지역 경기 최악인데 세수는 9% 증가"···국세청·한은 국감서 질타 | https://dgmbc.com/NewsArticle/867914 |  |
| tax | phmbc.co.kr | "지역 경기 최악인데 세수는 9% 증가"···국세청·한은 국감서 질타 | http://www.phmbc.co.kr/www/news/desk_news?idx=205013&mode=view |  |
| tax | imaeil.com | [TK 홀대 심화] "무리한 과세에 극단 사례까지…" 대구국세청 '부당 과세... | https://www.imaeil.com/page/view/2026101618114702733 |  |
| tax | newsis.com | 세무조사 받던 포항 납세자 사망…이종욱 의원, 국감서 질타(종합) | https://www.newsis.com/view/NISX20261016_0003829640 |  |
| tax | hankookilbo.com | "세무조사권으로 국민 극단으로 몰아"… 포항 사업가 사망에 국세청 뭇... | https://www.hankookilbo.com/news/article/A2026101615210005561?did=NA |  |
| tax | etoday.co.kr | 여야, 국세청 '무리한 과세' 질타...”납세자 한계 내몰아”[국감] | https://www.etoday.co.kr/news/view/2636800 |  |
| tax | yeongnam.com | 대구경북 경제난에 금융지원 확대 주문, 세무조사도 지적 | https://www.yeongnam.com/web/view.php?key=20261016026274948 |  |
| tax | sejungilbo.com | [`26 국감] 이종욱, "과세 취소 후 또 조사…무리한 세정으로 한계까지... | https://www.sejungilbo.com/news/articleView.html?idxno=60668 |  |
| tax | news1.kr | 세금 전액 취소됐지만 납세자 사망…국세청 결국 고개 숙였다 | https://www.news1.kr/local/daegu-gyeongbuk/6322654 |  |
| tax | newsis.com | 세무조사 받던 포항 납세자 사망…이종욱의원, 국감서 질타 | https://www.newsis.com/view/NISX20261016_0003829257 |  |
| tax | imaeil.com | 축의금 증여세, 500만원 이체도 방명록 없으면 과세…비과세 선은 액수... | https://www.imaeil.com/page/view/2026101518400608899 |  |
| tax | inews24.com | 공정위, 국감 이틀 만에 '조사·심판 통합' 고수…근거로 든 美 FTC는 '독... | http://www.inews24.com/view/2015502 |  |
| tax | tfmedia.co.kr | [설미현의 세무 인사이트] 위법한 세금 부과, 취소하고 다시 부과하면 ... | https://www.tfmedia.co.kr/news/article.html?no=208048 |  |
| tax | naeil.com | 파인스톤CC ‘137억원 세금 심판 소송’ 패소 | https://www.naeil.com/news/read/605231?ref=naver |  |
| tax | sejungilbo.com | 외국계 기업 임원 RSU, 대법 "대한민국에 과세권 있다" | https://www.sejungilbo.com/news/articleView.html?idxno=60633 |  |
| tax | fieldnews.kr | [단독] 조세심판원, 케이뱅크 '518억 전산투자' 세액공제 재조사 결정 | http://www.fieldnews.kr/news/articleView.html?idxno=32245 |  |
| tax | etoday.co.kr | 임광현 국세청장 “가상자산 과세 고시 11월 목표” [국감] | https://www.etoday.co.kr/news/view/2635372 |  |
| tax | biz.sbs.co.kr | 임광현 국세청장 "가상자산 과세 고시 다음 달로 준비" | https://biz.sbs.co.kr/article_hub/20000339715?division=NAVER |  |
| tax | 이데일리 | 법은 90일, 현실은 6년…조세심판원, 세금불복 ‘늑장심판’[단독] | https://www.edaily.co.kr/News/Read?newsId=03345606645612592&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | the-today.com | [단독] LG전자 인도법인, 印 대법원서 재과세 승소…10년 묵은 족쇄 풀었... | https://www.the-today.com/news/articleView.html?idxno=91603 |  |
| tax | 이데일리 | [단독]“다 공개한다더니 0건?”…5개월째 헛도는 조세심판원 개혁 | https://www.edaily.co.kr/News/Read?newsId=01767926645612592&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | g-enews.com | 183일만 피하려다 세금 폭탄 맞는다… 영국 돌아온 왕자 부부가 일깨운... | https://www.g-enews.com/view.php?ud=202610121819248904fbbec65dfb_1 |  |
| tax | news1.kr | 주병기, '재벌 비판' 발언 한발 물러서…"기업 역량 과소평가한 건 과해... | https://www.news1.kr/economy/trend/6317319 |  |
| tax | 한국경제 | 공정위 처분 '고법 직행' 2심제 논란…"시장 경쟁 회복에 신속함 필요" | https://www.hankyung.com/article/202610126708i |  |
| tax | newspim.com | [2026 국감] 주병기 "공정위 사건 2심제로 충분…재판권 침해 아냐" | https://www.newspim.com/news/view/20261012001211 |  |
| tax | inews24.com | [2026 국감] "공정위 2심제, 판사 판단 없이 유지…처분권 총리실로 옮겨... | http://www.inews24.com/view/2014012 |  |
| tax | sejungilbo.com | [판세] 가산세 면제사유인 정당한 사유가 있는지 여부의 판단기준 | https://www.sejungilbo.com/news/articleView.html?idxno=60315 |  |
| tax | 이데일리 | “대통령 가족도 돈 번다는데”…美서 코인 키우자는 법안 막힌 이유 | https://www.edaily.co.kr/News/Read?newsId=01722006645611608&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | 이데일리 | 폐가인데 종부세 내라고요?[세금, 그 후] | https://www.edaily.co.kr/News/Read?newsId=01082406645611280&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | financialreview.co.kr | [강동형 칼럼] 장부와 창고가 어긋날 때, 숫자보다 먼저 물어야 할 것 | http://www.financialreview.co.kr/news/articleView.html?idxno=45384 |  |
| tax | financialreview.co.kr | [장태성 칼럼] 매달 내는데도 압류는 풀리지 않는다: 두 줄의 법, 한 장... | http://www.financialreview.co.kr/news/articleView.html?idxno=45382 |  |
| tax | sejungilbo.com | [심청이] 재개발 '조합원입주권', 종전 부동산으로 감정평가해 상속세 ... | https://www.sejungilbo.com/news/articleView.html?idxno=60475 |  |
| tax | tfmedia.co.kr | [펜타곤의 택스노트] 청약 당첨 엿새 뒤 집을 팔았더니 '3주택자'...대법... | https://www.tfmedia.co.kr/news/article.html?no=207791 |  |
| tax | inews24.com | 일감은 반토막 났는데…조세심판 10건 중 9건 '90일 초과' | http://www.inews24.com/view/2012251 |  |
| tax | 일간NTN | 조세심판청구 결정 10건 중 9건 '90일 초과'…납세자 권리구제 갈수록 지... | http://www.intn.co.kr/news/articleView.html?idxno=2053840 |  |
| tax | tfmedia.co.kr | [예규·판례] 주문은 소비자가, 수입은 업체가…공동구매 관세는 누가 ... | https://www.tfmedia.co.kr/news/article.html?no=207740 |  |
| tax | 일간NTN | 법원 "2년 연속 적자 비상장주식, 상속세 물납 거부 적법" | http://www.intn.co.kr/news/articleView.html?idxno=2053825 |  |
| tax | suwonilbo.kr | [내 세금 사건일지] 사장 아내의 급여 1억 2천만 원, 국세청은 가짜라 했... | https://www.suwonilbo.kr/view.html?id=L2610041618042f67 |  |
| tax | sejungilbo.com | [판세] 배우자상속재산분할기한 지나면 상속받은 금액 공제 받을 수 없... | https://www.sejungilbo.com/news/articleView.html?idxno=60313 |  |
| tax | 이데일리 | 코인 가치평가 지표 MVRV, 그 유용성과 한계 | https://www.edaily.co.kr/News/Read?newsId=01613766645609640&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | wikitree.co.kr | “절차 위반 과세는 취소”… 법원·심판원, ‘적법절차 원칙’ 엄격 적... | https://www.wikitree.co.kr/articles/1163063 |  |
| tax | nocutnews.co.kr | [단독]조세심판 10건 중 9건 '90일 초과'…납세자 권리구제 하세월 | https://www.nocutnews.co.kr/news/6586820?utm_source=naver&utm_medium=article&utm_campaign=20261003091833 |  |
| tax | 이데일리 | 집 팔았는데 돈도 사람도 그대로…'2분 13초'의 비밀[세금, 그 후] | https://www.edaily.co.kr/News/Read?newsId=01115206645609312&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| tax | naeil.com | “콘도회원 우선예약권 부여 … 회원제 골프장” | https://www.naeil.com/news/read/604131?ref=naver |  |
| tax | sejungilbo.com | [심청이] 15억 인건비 줬다더니 '당일 현금 인출'…다단계센터 부부의 ... | https://www.sejungilbo.com/news/articleView.html?idxno=60401 |  |
| tax | sejungilbo.com | [국세청의 '조세심판 대응법'-⑩] 핵심 과세논리 '2~3줄'의 힘 | https://www.sejungilbo.com/news/articleView.html?idxno=60399 |  |
| icfr | the-biz.co.kr | KB금융, 3분기 누적 순익 6조 눈앞… "4분기 NIM 반등 총력" | http://www.the-biz.co.kr/news/articleView.html?idxno=730278 |  |
| icfr | biz.heraldcorp.com | 금감원 “손해율·사업비 가정 여전히 미흡”…전 보험사 11월말까지 개... | https://biz.heraldcorp.com/article/10919489?ref=naver |  |
| icfr | 이데일리 | 美 금리 동결에도 고금리 그늘…은행·카드·보험 부담 지속 | https://www.edaily.co.kr/News/Read?newsId=05264406645617840&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | view.asiae.co.kr | 보험 '계리가정보고서' 12월 시행…금감원, 손해율·사업비 가정산출 개... | https://view.asiae.co.kr/article/2026102911264619990 |  |
| icfr | insnews.co.kr | 금감원, 보험사 계리가정 관리 강화… 연말 '집중 점검' 예고 | https://www.insnews.co.kr/news/articleView.html?idxno=93587 |  |
| icfr | newsworks.co.kr | 금감원, 보험사 계리가정 전면 점검…11월까지 개선계획 받는다 | https://www.newsworks.co.kr/news/articleView.html?idxno=901216 |  |
| icfr | biz.heraldcorp.com | 한공회, 내달 ‘제27회 지속가능성인증포럼’ 개최 | https://biz.heraldcorp.com/article/10919348?ref=naver |  |
| icfr | newsworker.co.kr | [IB탈탈털기] 교보증권, 3000억 수혈에도 종투사 '먼 길'…2년 뒤 찾아올... | https://www.newsworker.co.kr/news/articleView.html?idxno=511265 |  |
| icfr | lec.co.kr | 박준연 미국 변호사의 논 세퀴터 93-잘 만든 컴플라이언스 프로그램, 왜... | http://www.lec.co.kr/news/articleView.html?idxno=752932 |  |
| icfr | gokorea.kr | 대륙아주·린·딜로이트 안진, 기업 AI 컴플라이언스 관리 지원 협약 체... | https://www.gokorea.kr/news/articleView.html?idxno=883266 |  |
| icfr | nbntv.co.kr | 대륙아주·린·딜로이트 안진, 기업 AI 규제 대응·인증 지원 MOU 체결 | https://www.nbntv.co.kr/news/articleView.html?idxno=4026707 |  |
| icfr | 한국경제 | "세금 1원도 안 낸다"…억만장자들의 5조달러 절세 비법 [밤 사이 해외 ... | https://www.hankyung.com/article/202610292669i |  |
| icfr | sports.donga.com | 김포시, ‘공공기관 횡령’ 되풀이 막는다…산하 기관 자금관리 ‘허점... | https://sports.donga.com/region/article/all/20261029/134930156/1 |  |
| icfr | popcornnews.net | 국민연금, 롯데쇼핑 감사위원 후보 찬성...재무 전문성에 힘 실었다 | http://www.popcornnews.net/news/articleView.html?idxno=137809 |  |
| icfr | zdnet.co.kr | 세종텔레콤, ESG 평가 2년 연속 최고등급 획득 | https://zdnet.co.kr/view/?no=20261029091716 |  |
| icfr | etoday.co.kr | 딜로이트 안진·대륙아주, AI 컴플라이언스 체계 구축 '맞손' | https://www.etoday.co.kr/news/view/2641495 |  |
| icfr | ohmynews.com | "국민연금은 실수 안 하나?"... 자산운용사가 작심하고 던진 말 | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003268359&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| icfr | ajunews.com | [로펌라운지] 대륙아주·린, 딜로이트 안진과 MOU 체결…AI 컴플라이언스... | https://www.ajunews.com/view/20261028174034455 |  |
| icfr | hankookilbo.com | [단독] 자체 '워크숍'에 통일캠프는 인원 미달… 남북협력기금 실효성 ... | https://www.hankookilbo.com/news/article/A2026102816010004283?did=NA |  |
| icfr | khan.co.kr | [정동칼럼]현세대에 갇힌 연금 연대 | https://www.khan.co.kr/article/202610282002005 |  |
| icfr | 머니투데이 | 대륙아주·린, 딜로이트 안진과 맞손…기업 AI 컴플라이언스 인증·관리... | https://www.mt.co.kr/society/2026/10/28/2026102818341882353 |  |
| icfr | tokenpost.kr | 비트코인 결제도 손익 신고 대상…중개업체 자료만으로는 부족 | https://www.tokenpost.kr/news/cryptocurrency/427731 |  |
| icfr | 이데일리 | 대륙아주·린, 딜로이트 안진과 MOU… 'AI 컴플라이언스' 협력 | https://www.edaily.co.kr/News/Read?newsId=05576006645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | newsclaim.co.kr | [광주은행 인사 전망] 정일선 첫 연말 인사… 김종훈 지점 3곳 미계약·... | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080430 |  |
| icfr | 매일경제 | 토큰증권시대 대비… 화우 '금융 드림팀' 떴다 | https://www.mk.co.kr/article/12188569 |  |
| icfr | byline.network | [바스리] 오후두시랩, 친환경 소비자를 위한 쇼핑몰을 연 이유 | https://byline.network/?p=9004111222625006 |  |
| icfr | newsworker.co.kr | 해태제과식품, '일부 영업사원' 문제라지만…대표이사 등 감사·재무책... | https://www.newsworker.co.kr/news/articleView.html?idxno=511037 |  |
| icfr | 이데일리 | 공공기관에 묵은 빚 4.9조원 정리한다…누가 얼마나 면제받나 | https://www.edaily.co.kr/News/Read?newsId=04890486645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | ntoday.co.kr | [국감 워치] 대통령비서실, 16개월간 181회 여론조사…내용·기관은 '베... | https://www.ntoday.co.kr/news/articleView.html?idxno=130406 |  |
| icfr | 매일경제 | 끝없이 밀리는 수협은행장 인선에…“위원 전면 교체” 내건 노조 | https://www.mk.co.kr/article/12188187 |  |
| icfr | newswell.co.kr | '윤종규에 패배 쓴잔' 김기홍 JB금융지주 회장, '9년 독재'는 질 수 없지... | http://www.newswell.co.kr/news/articleView.html?idxno=23090 |  |
| icfr | ohmynews.com | 58억 횡령, 행정 실수... 시민구단 왜 사건사고 끊이지 않나 | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003279096&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| icfr | ddaily.co.kr | [빅테크24시] MS, 직원 27%에 희망퇴직 제안…일부 임원도 대상 | https://www.ddaily.co.kr/page/view/2026102809464455757 |  |
| icfr | 이데일리 | 핵잠 선도함은 2035년 진수 목표인데…사업단은 2029년까지 한시 운영 | https://www.edaily.co.kr/News/Read?newsId=03480086645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | etnews.com | “HR 동료 한 명 생긴 느낌”…다우오피스 HR 도입해보니 | https://www.etnews.com/20261028000049 |  |
| icfr | kmaeil.com | [이준호의 N잡러칼럼] 코스닥 상장전략(2), 코스닥의 문을 두드리는 중... | https://www.kmaeil.com/news/articleView.html?idxno=655642 |  |
| icfr | niceeconomy.co.kr | 현대차증권 '탄소금융 인사이트 데이'…배출권 넘어 외부사업 해법 모색 | https://www.niceeconomy.co.kr/news/articleView.html?idxno=91561 |  |
| icfr | labortoday.co.kr | '청구는 회의비, 결제는 와인바' 서울대병원 클린카드 논란 | https://www.labortoday.co.kr/news/articleView.html?idxno=237429 |  |
| icfr | segye.com | 현실 못 담은 세수추계… 4년간 연평균 51조 오차 | https://www.segye.com/newsView/20261027516402?OutUrl=naver |  |
| icfr | consumernews.co.kr | 한미약품, 3분기 누적 매출·영업익 두 자릿수 증가…'선 수금·후 출고... | http://www.consumernews.co.kr/news/articleView.html?idxno=766930 |  |
| icfr | 서울경제 | “기재부, 국회 패싱해 기금 32조 전용…年 이자만 8330억” | https://www.sedaily.com/article/20106787?ref=naver |  |
| icfr | biz.chosun.com | 한미약품, 누적 매출 1조2000억원 돌파…북경한미 리스크 여전 | https://biz.chosun.com/science-chosun/bio/2026/10/27/F4KODOTWUBBLLCXYIFCFBZSAH4/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| icfr | ajunews.com | 하락장에 CB 전환가액 줄지어 하향…코스닥 주주 '한숨' | https://www.ajunews.com/view/20261027163209833 |  |
| icfr | greened.kr | 윤새봄이 키운 '놀이의발견' 6만7000명 정보 유출…프리드라이프 이어 ... | https://www.greened.kr/news/articleView.html?idxno=353125 |  |
| icfr | news.sbs.co.kr | 정부 세수 추계, 2021년부터 4년간 연평균 51조 원 오차 | https://news.sbs.co.kr/news/endPage.do?news_id=N1008817387&plink=ORI&cooper=NAVER |  |
| icfr | wowtv.co.kr | 4년간 연평균 50조 세수오차...감사원 "정부 계산 잘못된 탓" | http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202610270129&t=NN |  |
| icfr | 매일경제 | “尹정부, 세수결손에 기금 34조 끌어다써”…감사원, 국회 우회의도 지... | https://www.mk.co.kr/article/12186988 |  |
| icfr | newsprime.co.kr | [이재용 리더십 4년 ②] 위기의 삼성, 이재용식 해법은 통했나 | http://www.newsprime.co.kr/news/article.html?no=752566 |  |
| icfr | sejungilbo.com | 세수결손 대응 '중대한  하자'…재경부, 국회 패싱하며 '돌려막기', 이자... | https://www.sejungilbo.com/news/articleView.html?idxno=60830 |  |
| icfr | 한국세정신문 | 감사원, 정부 세수추계 4년간 평균 51조5천억 오차 발생해 | https://www.taxtimes.co.kr/news/article.html?no=277486 |  |
| icfr | news1.kr | '尹정부' 기재부 세수추계, 4년간 연평균 51조 오차…추계모형 설계 부... | https://www.news1.kr/politics/pm-bai-comm/6333363 |  |
| icfr | fetv.co.kr | [2026 국감] 수협은행, 도마 위에 오른 '인선 구조'…공적자금 갚아도 정... | https://www.fetv.co.kr/news/articleView.html?idxno=312512 |  |
| icfr | newsclaim.co.kr | [iM금융지주 인사 전망] 황병우 연임 심사… 겸직 수당·무단 계좌개설... | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080217 |  |
| icfr | naeil.com | 대규모 세수결손, 정부 계산 잘못 탓 | https://www.naeil.com/news/read/606554?ref=naver |  |
| icfr | 조세일보 | 윤 정부 '87조 세수펑크'…애꿎은 지방·기금이 털려 | http://www.joseilbo.com/news/news_read.php?uid=578247&class=32&grp= |  |
| icfr | gosiweek.com | 공무원 '보고 단계' 줄이고 AI로 업무 관리…인사처, 일하는 방식 바꾼... | https://www.gosiweek.com/article/1065582110865852 |  |
| icfr | 일간NTN | 세수 오차에 기금 돌려막기까지…감사원, 부실 추계가 부른 '재정 꼼수... | http://www.intn.co.kr/news/articleView.html?idxno=2054323 |  |
| icfr | 이데일리 | 정부, 세수 펑크에…국회 심의 대신 32조 기금 돌려막기 | https://www.edaily.co.kr/News/Read?newsId=03696566645617184&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | view.asiae.co.kr | 현실과 동떨어진 세수추계…2021년부터 4년간 연평균 51조원 오차 | https://view.asiae.co.kr/article/2026102708140098084 |  |
| icfr | yna.co.kr | 정부 세수 추계, 2021년부터 4년간 연평균 51조원 오차 | https://www.yna.co.kr/view/AKR20261027029900001?input=1195m |  |
| icfr | newsis.com | 감사원 "법인세·양도세 추계오차 81%는 모형 문제 때문" | https://www.newsis.com/view/NISX20261026_0003841744 |  |
| icfr | yonhapnewstv.co.kr | 감사원 "尹정부, 세수 부족에 기금 32조원 활용…국회 통제 우회" | http://www.yonhapnewstv.co.kr/news/AKR20261027101332mZ7 |  |
| icfr | 머니투데이 | '年 51.5조' 세수 오차, 경기 탓만 아니었다…감사원 "기재부 '추계모형... | https://www.mt.co.kr/politics/2026/10/28/2026102709232357438 |  |
| icfr | joongang.co.kr | 4년간 50조 세수 오차…감사원 “경기 아닌 정부 추계 모형 오류” | https://www.joongang.co.kr/article/25473170 |  |
| icfr | ohmynews.com | 노동자 숨져도 "결격사유 없음"... 주주 외면한 기관투자자들 | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003275472&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| icfr | 4th.kr | [경제소식] 토스증권, 美 현장 조사 바탕 청년 진로교육 | http://www.4th.kr/news/articleView.html?idxno=2120464 |  |
| icfr | kmaeil.com | [문인찬의 新戰略論] New Strategy Paradigm #61 | https://www.kmaeil.com/news/articleView.html?idxno=655825 |  |
| icfr | newsclaim.co.kr | [BNK금융 인사 전망] 빈대인 연임 첫 연말 인사… 7개 계열사 CEO 인선 | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080169 |  |
| icfr | globalepic.co.kr | [단독] 세 차례 미뤄진 퇴직연금 CEO 간담회 내달 6일 개최 | https://www.globalepic.co.kr/view.php?ud=2026102708511668447cc35ccc5c_29 |  |
| icfr | 이데일리 | 베일 벗은 앤스로픽 IPO…'AI 거품론' 시험대[뉴스새벽배송] | https://www.edaily.co.kr/News/Read?newsId=02771606645617184&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | dailybrief.co.kr | [금융그룹/DB①] 계열사 53곳 늘면서 자산 첫 100조 돌파 | https://www.dailybrief.co.kr/news/articleView.html?idxno=7107 |  |
| icfr | news1.kr | 농·축협 왜 이러나?…수백억 부당대출에 성추행·금권선거 | https://www.news1.kr/local/daegu-gyeongbuk/6331931 |  |
| icfr | yakup.com | [기고] 컴플라이언스, 기업 성장 지키는 경영 안전장치 | https://www.yakup.com/news/index.html?mode=view&cat=12&nid=334254 |  |
| icfr | ekn.kr | [패트롤] 평택시의회-광주시의회-성남시의회-용인시의회 | https://www.ekn.kr/web/view.php?key=20261027028391489 |  |
| icfr | news2day.co.kr | [신(新)인물탐구(70)] LS그룹 구자은 회장⑦ 리스크 관리 - 위험은 미리... | https://www.news2day.co.kr/article/20261024500028 |  |
| icfr | byline.network | 금감원 “AI 보안 역량을 갖춘 금융사부터 망분리 해제 검토” | https://byline.network/?p=9004111222624732 |  |
| icfr | kpanews.co.kr | "불법 개설기관 근절 위해 '특사경' 도입 절실, 강제 수사권 없이 적발... | https://www.kpanews.co.kr/news/articleView.html?idxno=547304 |  |
| icfr | apnews.kr | "지방 전기요금 할인, 민간에 청구서 넘기는 꼴…발전사 연 6600억 부담" | https://www.apnews.kr/news/articleView.html?idxno=3052476 |  |
| icfr | ceoscoredaily.com | [현장] 이석 금감원 국장 “AI 보안역량 갖춘 금융사부터 망분리 전면 해... | https://www.ceoscoredaily.com/page/view/2026102613452597764 |  |
| icfr | smartbizn.com | 실적 뛰고 배당 늘린 DB증권···기업가치 재평가 발목 잡는 '내부통제... | https://www.smartbizn.com/news/articleView.html?idxno=157543 |  |
| icfr | m-economynews.com | 윤호중 “한강버스 136억 지원 사실상 불승인”...국감서 여야 공방 | https://www.m-economynews.com/news/article.html?no=72137 |  |
| icfr | newswhoplus.com | 파행 딛고 다시 선 전남미협…62회 전남미술대전 성료 | https://www.newswhoplus.com/news/articleView.html?idxno=72656 |  |
| icfr | wikitree.co.kr | "파주시민축구단 감사서 21건 지적" 파주시, 후속 조치·제도 개선 착수 | https://www.wikitree.co.kr/articles/1169246 |  |
| icfr | fntimes.com | 다케나카 개혁의 성과와 대가: 레소나은행과 다이에이의 구조조정 [김성... | https://www.fntimes.com/html/view.php?ud=20261026141829433c1c16452b0_18 |  |
| icfr | newsway.co.kr | 금감원 "AI 보안 역량 갖춘 금융사, 망분리 전면 해제 검토" | https://www.newsway.co.kr/news/view?ud=2026102614034161631 |  |
| icfr | womaneconomy.co.kr | CJ올리브네트웍스 첫 A+···보안투자 95억, 그룹 직원정보 유출은 과제 | https://www.womaneconomy.co.kr/news/articleView.html?idxno=260214 |  |
| icfr | koreastocknews.com | 해태제과식품, 530억 과대계상 후폭풍? 주가 어쩌다 4000원대로 | http://www.koreastocknews.com/news/articleView.html?idxno=121924 |  |
| icfr | etnews.com | [ET특징주] '매출 부풀리기' 해태제과식품, 거래 재개 첫날 주가 14% 급락 | https://www.etnews.com/20261026000223 |  |
| icfr | newsworker.co.kr | [진단_금융업계 ⑤현대해상] 순이익 증가에도 소비자 보호·주주환원 제... | https://www.newsworker.co.kr/news/articleView.html?idxno=510474 |  |
| icfr | ohmynews.com | 회장님 SNS까지 걱정하는 주주들, 국민 돈 굴리는 '집사'는 뭐했나 | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003277281&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| icfr | futurechosun.com | [박훈의 나눔과 세금] 법정에서 배운 기부의 신뢰, 세법이 할 일 | https://futurechosun.com/?p=164491 |  |
| icfr | newsclaim.co.kr | [신한금융지주 인사 전망] 진옥동 2기 첫 연말 인사… CEO 12명 심사 | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080006 |  |
| icfr | metroseoul.co.kr | [특징주] 해태제과식품, 거래 재개 첫날 급락…장중 52주 신저가 | http://www.metroseoul.co.kr/article/20261026500139 |  |
| icfr | sateconomy.co.kr | 해태제과식품, 회계 위반 적발 소식에거래 재개 첫날 15%대 급락 | https://sateconomy.co.kr/news/view/1065575951018059 |  |
| icfr | cbci.co.kr | [정치家] 조현 외교부 장관 ⑤ㅣ 한미·한일 협력부터 유엔 다자외교까... | https://www.cbci.co.kr/news/articleView.html?idxno=619201 |  |
| icfr | kmaeil.com | [이준호의 N잡러칼럼] 코스닥 상장전략(1), 상장은 꿈이 아니라 검증이... | https://www.kmaeil.com/news/articleView.html?idxno=655638 |  |
| icfr | biz.chosun.com | [특징주] ’매출 부풀리기' 해태제과식품, 거래 재개하자 12% 급락 | https://biz.chosun.com/stock/stock_general/2026/10/26/PKYDM3Z5AVCCXMWPVVXB42Z5MY/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| icfr | newspim.com | [특징주] 회계 부풀리기 적발에 해태제과식품 11% 급락 | https://www.newspim.com/news/view/20261026000209 |  |
| icfr | koreajoongangdaily.com | Concerns grow over Finance Ministry being sidelined (KOR) | https://www.koreajoongangdaily.com/bilingual-news/concerns-grow-over-finance-ministry-being-sidelined-kor/12937538 |  |
| icfr | businesspost.co.kr | KB금융 양종희 3년 '리딩금융' 지켰다, 마지막 성적표도 '1위'로 유종의... | https://www.businesspost.co.kr/BP?command=article_view&num=450695 |  |
| icfr | isplus.com | 제주 SK, 구자철 관련 의혹에 공식 반박…"감독 선임 개입 없었다" | https://isplus.com/article/view/isp202610290143 |  |
| icfr | newspenguin.com | 삼성생명 숨은 배출량 80% 더 나왔는데..."감축 목표와는 별개" | https://www.newspenguin.com/news/articleView.html?idxno=22362 |  |
| icfr | epnc.co.kr | 마이크로소프트, '프론티어 트랜스포메이션' 제시…AI 도입 넘어 업무·... | https://www.epnc.co.kr/news/articleView.html?idxno=408975 |  |
| icfr | it.donga.com | 창업 유니콘에 도전하는 성북구 1인 창조기업 지원센터 우수기업 (2) | https://it.donga.com/109791/ |  |
| icfr | newsroad.co.kr | 한화에어로, "4분기 회복 전망"… 일회성 비용 빼도 방산 이익률 5.4% | http://www.newsroad.co.kr/news/articleView.html?idxno=66742 |  |
| icfr | ilyo.co.kr | LG생활건강 실적 반등 불씨 살렸지만…‘취임 1년’ 이선주호 부실 자산... | https://ilyo.co.kr/?ac=article_view&entry_id=513357 |  |
| icfr | fieldnews.kr | [이슈X레이] 7년 만에 되돌린 하림산업 합병…양재 땅만 남는 '분할' | http://www.fieldnews.kr/news/articleView.html?idxno=32639 |  |
| icfr | fieldnews.kr | 한미약품, 3분기 순익 69% 급감…'기저효과' 해명에 가려진 본업 부진 | http://www.fieldnews.kr/news/articleView.html?idxno=32648 |  |
| icfr | fieldnews.kr | [단독] 국세청, '모범납세자' 부국증권 세무조사…마무리 수순 속 '추징... | http://www.fieldnews.kr/news/articleView.html?idxno=32654 |  |
| icfr | newsworks.co.kr | 수원특례시의회 정례회 폐회…돌봄·도로·상권·적극행정 과제 제기 | https://www.newsworks.co.kr/news/articleView.html?idxno=901311 |  |
| icfr | 한국경제 | 스타트업 키우는 BNK부산은행…창업·투자 생태계 만든다 | https://www.hankyung.com/article/2026102924281 |  |
| icfr | thevaluenews.co.kr | [현장] '월 40달러 AI 팀', 미국부터 공략…한컴 노마디안의 승부수 | http://www.thevaluenews.co.kr/news/view.php?idx=202794 |  |
| icfr | the-today.com | 키움증권, '친일 논란' 호텔 개발에 4500억…김동준號 PF 위험관리 시험... | https://www.the-today.com/news/articleView.html?idxno=92658 |  |
| icfr | newsroad.co.kr | 현대차, 영업익 늘었지만 순익 24% 감소… 원가 부담은 남았다 | http://www.newsroad.co.kr/news/articleView.html?idxno=66720 |  |
| icfr | econovill.com | 마이크로소프트 프론티어 전환 성적표 공개 "에이전트 관리가 승부처" | https://www.econovill.com/news/articleView.html?idxno=755313 |  |
| icfr | newswell.co.kr | '죄질 불량한데 집행유예' 대명종합건설 지우종, 벌써 '2심' 이야기 나온... | http://www.newswell.co.kr/news/articleView.html?idxno=23158 |  |
| icfr | wikitree.co.kr | 한국축구 레전드인데…'이 의혹' 뜨자 구단서 곧장 강경 대응, 무슨 일 | https://www.wikitree.co.kr/articles/1170183 |  |
| icfr | koreaittimes.com | [인사이트] MS·알파벳 AI 투자에 SK하이닉스 고수익…투자비 회수는 숙... | https://www.koreaittimes.com/news/articleView.html?idxno=158628 |  |
| icfr | techm.kr | 삼성전자 "2028년도 메모리 공급 부족...HBM 점유율, D램 수준 확보"(종합... | https://www.techm.kr/news/articleView.html?idxno=156647 |  |
| icfr | taxwatch.co.kr | [새책]세무조사 통지서 받았다면?…국세청 출신 세무사의 조언 | https://www.taxwatch.co.kr/article/tax/2026/10/29/0004/naver |  |
| icfr | fntoday.co.kr | 쎄트렉아이, 3분기 영업이익 82억 원… 전년 동기 대비 235% 급증 | https://www.fntoday.co.kr/news/articleView.html?idxno=396543 |  |
| icfr | upkoreanews.kr | 대명종합건설 지우종 전 대표, 징역형 집행유예·벌금 138억…오너 일가... | https://www.upkoreanews.kr/news/articleView.html?idxno=100905 |  |
| icfr | techm.kr | 삼성전자, 3분기 ICT 최초 영업익 100조원 돌파...DS·DX, 불균형 심화 | https://www.techm.kr/news/articleView.html?idxno=156625 |  |
| icfr | gamefocus.co.kr | 프론티어 트랜스포메이션 실현 위한 플랫폼 접근법은? 마이크로소프트... | https://gamefocus.co.kr/detail.php?number=180136 |  |
| icfr | zdnet.co.kr | "AI 에이전트 1만개 시대"…MS, 기업용 AI 관리·보안 시장 선점 나서 | https://zdnet.co.kr/view/?no=20261029101209 |  |
| icfr | cbci.co.kr | [속보] 쎄트렉아이, 3분기 영업이익 82억3900만원…전년 동기 대비 235.6... | https://www.cbci.co.kr/news/articleView.html?idxno=620670 |  |
| icfr | goodkyung.com | [뉴욕증시포커스] 연준 동결에 동반 상승…오라클 10.73% 급등 | https://www.goodkyung.com/news/articleView.html?idxno=292881 |  |
| icfr | thebell.co.kr | [더벨][Risk Manager Awards \| 2026년 우수사례] 미래에셋증권, 위험액 산... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202610280632262860105366 |  |
| icfr | thebell.co.kr | [더벨][Risk Manager Awards \| 2026년 우수사례] NH투자증권, 서류 밖 현장... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202610271631179880102057 |  |
| icfr | mstoday.co.kr | AI 실적에 MS 웃고 구글 울었다…차이는 '현금' | https://www.mstoday.co.kr/news/articleView.html?idxno=200306 |  |
| icfr | sisajournal-e.com | KT, '호각 100억 투자' KT스카이라이프 전 대표 2명 자문계약 해지···손... | https://www.sisajournal-e.com/news/articleView.html?idxno=424642 |  |
| icfr | news2day.co.kr | [N2 심층취재｜조지훈 시정 검증②] 전북 전주시, 성과급 43억원 지급 미... | https://www.news2day.co.kr/article/20261029500025 |  |
| icfr | ngonews.kr | 민주주의를 외치는 시민사회, 청년에게는 왜 권력을 주지 않는가 | https://www.ngonews.kr/news/articleView.html?idxno=241801 |  |
| icfr | viva100.com | [통신업계 소식] KT, ‘보이스봇’·‘AI 상담 어시스트’로 고객 경험 ... | https://www.viva100.com/article/20261029500224 |  |
| icfr | asiatime.co.kr | "오너家 절세 기회지만"…일양약품 주주는 '씁쓸' | https://www.asiatime.co.kr/article/20261028500405 |  |
| icfr | bloter.net | 솔루스첨단소재-SK넥실리스 특허전 희비…명운 걸린 전지박 사업 | https://www.bloter.net/news/articleView.html?idxno=676970 |  |
| icfr | g-enews.com | 구글 알파벳 "빅테크 어닝쇼크"... 삼전닉스 K반도체 또 위기? | https://www.g-enews.com/view.php?ud=202610290830218346906806b77b_1 |  |
| icfr | 이데일리 | 영림원소프트랩, 한국품질만족지수 ERP 부문 4년 연속 1위 | https://www.edaily.co.kr/News/Read?newsId=03184886645617840&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | m-i.kr | FOMC 금리 동결·오라클 10% 급등에 뉴욕증시 소폭 상승 [뉴욕증시] | https://www.m-i.kr/news/articleView.html?idxno=2011654 |  |
| icfr | 이데일리 | 임상 반려에 나흘째 흔들린 올릭스…OLX301A 재신청은?[바이오맥짚기] | https://www.edaily.co.kr/News/Read?newsId=02883126645617840&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | thebell.co.kr | [더벨][지배구조 분석 \| KS인더스트리] 경영 전면 나선 김인겸 대표, 정... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202610262305023120103772 |  |
| icfr | segye.com | [오늘 뉴스 4컷] 정치는 국조 충돌, 금융은 해킹 비상…하이닉스는 ‘1... | https://www.segye.com/newsView/20261028520501?OutUrl=naver |  |
| icfr | bntnews.co.kr | 오늘의 운세 띠별 운세 29일 | https://www.bntnews.co.kr/article/view/bnt202610280193 |  |
| icfr | newsclaim.co.kr | [기업분석]LIG D&A 친족회사 채무 공시 82억 차이… 뇌물 사건에 입찰제... | https://www.newsclaim.co.kr/news/articleView.html?idxno=3080325 |  |
| icfr | futurechosun.com | [더나은미래 경제브리핑] SK하이닉스, 분기 매출 첫 100조 돌파…이찬진... | https://futurechosun.com/?p=164825 |  |
| icfr | zdnet.co.kr | AWS, AI로 SAP 코드 전환 자동화…작업량 최대 87% 절감 | https://zdnet.co.kr/view/?no=20261028173811 |  |
| icfr | thelec.kr | LG전자 2026년 3분기 실적발표 컨퍼런스콜 전문 | https://www.thelec.kr/news/articleView.html?idxno=64461 |  |
| icfr | thebell.co.kr | [더벨][지배구조 분석] 해태제과, 독립이사 늘려 내부통제 외부검증 받... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202610261624548000105192 |  |
| icfr | kpenews.com | '713억 베팅' 어뮤즈 "아직은 적자"..신세계인터내셔날, 투자 성과 시험... | https://kpenews.com/View.aspx?No=4286798 |  |
| icfr | mstoday.co.kr | [기획-반도체 신질서] GPU가 반도체 산업의 권력을 바꾸고 있다 ② | https://www.mstoday.co.kr/news/articleView.html?idxno=200304 |  |
| icfr | bntnews.co.kr | 삼성전자 실적발표일 시간 언제? | https://www.bntnews.co.kr/article/view/bnt202610280238 |  |
| icfr | biz.heraldcorp.com | 실적 쇼크·코리 투자 검토 논란…흔들리는 황상연 한미약품 대표 리더... | https://biz.heraldcorp.com/article/10917746?ref=naver |  |
| icfr | hansbiz.co.kr | 저성장 돌파구 찾는 보험업계…AX 전환 속도 | http://www.hansbiz.co.kr/news/articleView.html?idxno=877072 |  |
| icfr | bzeronews.com | 진천군, 주민 체감형 적극행정 이끈 우수공무원 5명 선정 | https://www.bzeronews.com/news/articleView.html?idxno=824460 |  |
| icfr | newsfreezone.co.kr | 전북도민사회 "공공기관 2차 이전, 미래 성장동력으로" | https://www.newsfreezone.co.kr/news/articleView.html?idxno=716432 |  |
| icfr | fetv.co.kr | 한미그룹 오너가 갈등, '북경한미 매출채권' 새 쟁점으로 | https://www.fetv.co.kr/news/articleView.html?idxno=312588 |  |
| icfr | venturesquare.net | 오후두시랩, 신보 ‘퍼스트펭귄’ 선정…20억원 보증 기반 AI 탄소데이터... | https://www.venturesquare.net/1123776/ |  |
| icfr | press9.kr | [CEO 리뷰③] 신재욱·배광수 NH투자증권 대표, 각자경영 본격화 | http://www.press9.kr/news/articleView.html?idxno=85086 |  |
| icfr | newsroad.co.kr | [로드뷰] AI 승부처는 기업 데이터… 삼성SDS·LG CNS 등 '돈 되는 AI' 시... | http://www.newsroad.co.kr/news/articleView.html?idxno=66623 |  |
| icfr | thebigdata.co.kr | SK하이닉스, 2029년까지 메모리 사실상 완판…곽노정 “결실, 주주와 나... | https://www.thebigdata.co.kr/view.php?ud=2026102811055883050ecbf9426b_23 |  |
| icfr | 4th.kr | AI 반도체 피크아웃?…SK하이닉스 "2029년까지 D램·HBM 완판" | http://www.4th.kr/news/articleView.html?idxno=2120562 |  |
| icfr | bizhankook.com | 영업익 늘었는데 순익은 97% 줄었다…한화시스템 '필리조선소' 회계의 ... | https://bizhankook.com/articles/hanwha-systems-philly-shipyard-profit-drop.html |  |
| icfr | fntoday.co.kr | 푸른소나무, 2년 연속 '감사의견 거절'… 장부 미제출로 재무 신뢰성 '바... | https://www.fntoday.co.kr/news/articleView.html?idxno=396416 |  |
| icfr | peoplewatch.co.kr | 브룩필드 90억달러 투자, 네이버 18.7조 보증…AI 팩토리의 속사정 | https://www.peoplewatch.co.kr/article/view/ppw202610280004 |  |
| icfr | newsroad.co.kr | 메모리만 110조 영업익…삼성전자, '세계 1위' 실적 굳히나 | http://www.newsroad.co.kr/news/articleView.html?idxno=66580 |  |
| icfr | ebn.co.kr | 삼성전자, 내일 3Q 확정 실적…반도체 초호황에 연간 영업익 370조원 '청... | https://www.ebn.co.kr/news/articleView.html?idxno=1729405 |  |
| icfr | it.chosun.com | '중국의 로레알'은 탄생할까 ﻿[박지민의 중국과 미래] | https://it.chosun.com/news/articleView.html?idxno=2023092172821 |  |
| icfr | vegannews.co.kr | 메타케어 3분기 매출 194억…영업이익 861% 늘어 | https://www.vegannews.co.kr/news/article.html?no=397640 |  |
| icfr | 이데일리 | “첫 영업흑자에도 107조 적자”…앤스로픽, 2654조짜리 맞나 | https://www.edaily.co.kr/News/Read?newsId=01590806645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| icfr | knnews.co.kr | “대전~남해선 철도 국가철도망 반영을” | https://www.knnews.co.kr/news/articleView.php?idxno=1553782 |  |
| icfr | topstarnews.net | 앤트로픽 IPO에 한국 반도체주 급등…삼성·SK텔레콤 영향은? | https://www.topstarnews.net/news/articleView.html?idxno=16259784 |  |
| icfr | sentv.co.kr | 거래 재개 첫날 주가 급락...해태제과, 크라운해태 발목 잡나 | https://www.sentv.co.kr/article/view/sentv202610270087 |  |
| icfr | biz.newdaily.co.kr | 경영권 분쟁에 실적마저 뒷걸음질 … 한미약품, 3분기 영업익 31% 급감 | https://biz.newdaily.co.kr/site/data/html/2026/10/27/2026102700366.html |  |
| icfr | 매일경제 | 조호, 업무까지 수행하는 AI 에이전트로 한국 기업시장 공략 | https://www.mk.co.kr/article/12187426 |  |
| icfr | asiatoday.co.kr | 한미약품, 3분기 누적 매출 1.2조원…본업 호조에 비만 신약 출격 기대 | https://www.asiatoday.co.kr/kn/view.php?key=20261027010009510 |  |
| icfr | digitaltoday.co.kr | [데일리픽] 2027년 7월 'XRP 시대' 열릴까…앤트로픽 IPO 추진 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=710284 |  |
| icfr | donga.com | 고려대 MBA교우회, 경영대학과 첫 ‘KOREA MBA 포럼’ 개최 | https://www.donga.com/news/Economy/article/all/20261027/134918496/1 |  |
| icfr | greened.kr | '1조 사무장병원' 의혹 랩지노믹스…371억 금융자산 묶이고, 최대주주는... | https://www.greened.kr/news/articleView.html?idxno=353124 |  |
| icfr | womaneconomy.co.kr | AI가 낮춘 리서치 문턱, 자산운용사 경쟁 '분석 이후'에 달렸다 | https://www.womaneconomy.co.kr/news/articleView.html?idxno=260224 |  |
| icfr | womennews.co.kr | 고령문화관광재단 창립 1주년… 대가야 역사·문화 관광자원화에 속도 | https://www.womennews.co.kr/news/articleView.html?idxno=283764 |  |
| icfr | mstoday.co.kr | "AI 투자 효과 0?"…빅테크 수익성 시험대 | https://www.mstoday.co.kr/news/articleView.html?idxno=200288 |  |
| icfr | cbci.co.kr | [속보] 한화시스템, 3분기 영업이익 991억5000만원…전년 동기 대비 60.5... | https://www.cbci.co.kr/news/articleView.html?idxno=619827 |  |
| icfr | ditoday.com | 오픈 AI, 'GPT-6.1 테라' 공개... 가격은 반으로 낮추고 코딩 역량은 높여 | https://ditoday.com/%ec%98%a4%ed%94%88-ai-gpt-6-1-%ed%85%8c%eb%9d%bc-%ea%b3%b5%ea%b0%9c-%ea%b0%80%ea%b2%a9%ec%9d%80-%eb%b0%98%ec%9c%bc%eb%a1%9c-%eb%82%ae%ec%b6%94%ea%b3%a0-%ec%bd%94%eb%94%a9-%ec%97%ad%eb%9f%89/ |  |
| icfr | news.tf.co.kr | 오픈AI, 가성비 AI 'GPT-6.1 테라' 출시…"성능 높이고 API 가격 절반" | https://news.tf.co.kr/read/economy/2381272.htm |  |
| icfr | hansbiz.co.kr | 정종표號 DB손보, 포르테그라 인수로 해외 확장…자본 부담 과제 | http://www.hansbiz.co.kr/news/articleView.html?idxno=876601 |  |
| icfr | pinpointnews.co.kr | 코스콤, 스테이블코인 결제 확산에 경제성 입증 필요 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=498787 |  |
| icfr | globalepic.co.kr | 취임 4주년 이재용 회장… 기술-인재로 삼성 명성 되찾다 | https://www.globalepic.co.kr/view.php?ud=20261027104839386648439a4874_29 |  |
| icfr | newsis.com | "오답률 줄이고 코딩 능력 2배 껑충"…오픈AI, 가성비 AI 'GPT-6.1 테라' 출... | https://www.newsis.com/view/NISX20261027_0003842381 |  |
| icfr | junggi.co.kr | [전문가 칼럼] 31년 묵은 차명주식 40.39%…증빙으로 되찾았다 | https://www.junggi.co.kr/news/articleView.html?idxno=38236 |  |
| icfr | dnews.co.kr | [부산 브리핑 모음(10월27일)] 부산 나눔명문기업 100호 달성…기업 나눔... | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610261611520890211 |  |
| icfr | naeil.com | 금융당국 ‘회계부정 기업’ 중수청 고발…수사체계 개편 후 첫 적용 | https://www.naeil.com/news/read/605796?ref=naver |  |
| icfr | 한국세정신문 | 금융위, '공인회계사 실무수습기관 지정고시' 전부개정안 공고 | https://www.taxtimes.co.kr/news/article.html?no=275561 |  |
| icfr | asiatime.co.kr | [증권 뉴스브리핑] 금감원, 스페이스X 관련 미래에셋 검사/2차 국민참여... | https://www.asiatime.co.kr/article/20260616500361 |  |
| icfr | 파이낸셜뉴스 | 주가조작·회계부정 포상금 '상한선' 없다…26일 시행 | http://www.fnnews.com/news/202605202030212198 |  |
| icfr | tfmedia.co.kr | [회계인포럼] 권재열 경희대 교수 “회계기본법 실질 감리는 회계감독원... | https://www.tfmedia.co.kr/news/article.html?no=204399 |  |
| icfr | 한국세정신문 | "회계기본법은 최초의 회계헌법…회계정보 신뢰성 향상" | https://www.taxtimes.co.kr/news/article.html?no=275061 |  |
| icfr | newsway.co.kr | 상법 바꿔도 못 막았다…국회서 번진 '고의상폐' 제도 허점 | https://www.newsway.co.kr/news/view?ud=2026042114560259817 |  |
| icfr | enewstoday.co.kr | 대동전자 고의상폐 논란···"회사·임원 배상 책임 물어야" | http://www.enewstoday.co.kr/news/articleView.html?idxno=2421445 |  |
| icfr | news.einfomax.co.kr | "합법 가장한 소액주주 강탈"…대동전자 사태로 본 고의상폐 경고장 | https://news.einfomax.co.kr/news/articleView.html?idxno=4410766 |  |
| icfr | 매일경제 | “1200억 있는데 고의로 상폐”…개미 울리는 ‘합법적 주주 강탈’ 칼... | https://www.mk.co.kr/article/12022586 |  |
| icfr | m-joongang.com | "회계개혁 흔들림 없이 계속돼야" | https://www.m-joongang.com/news/articleView.html?idxno=402388 |  |
| icfr | sentv.co.kr | [단독] 국세청이 부과한 3724억, 구글은 ‘돌려받을 자산’으로 적었다 | https://www.sentv.co.kr/article/view/sentv202604150123 |  |
| icfr | gosiweek.com | [최창호 변호사의 법조단상] 사학의 자율성과 국가적 예속 : 사립학교법... | https://www.gosiweek.com/article/1065568920167412 |  |
| icfr | inews24.com | 주가조작 신고하면 '240억 포상금' 가능 | http://www.inews24.com/view/1942782 |  |
| icfr | kukinews.com | ‘신고해도 포상금 쥐꼬리’ 끝낸다…주가조작 ‘내부고발 포상’ 전면... | https://www.kukinews.com/article/view/kuk202602250202 |  |
| icfr | tfmedia.co.kr | [이슈체크] 청년회계사회 ‘세무사 결산검증 조례, 광주시의회 규탄’…... | https://www.tfmedia.co.kr/news/article.html?no=201387 |  |
| icfr | 조세일보 | 위기의 신입 회계사들, 돌파구는 없나 [황병찬 회계사회 부회장 인터뷰... | http://www.joseilbo.com/news/news_read.php?uid=562301&class=10&grp= |  |
| icfr | junggi.co.kr | 외감 대상인데 몰랐다가 '지정'…관리 공백 주의 | https://www.junggi.co.kr/news/articleView.html?idxno=35334 |  |
| icfr | 한국세정신문 | "고의 분식회계 가담한 회사관계자 과징금 상한 10→20%" | https://www.taxtimes.co.kr/news/article.html?no=273308 |  |
| icfr | pinpointnews.co.kr | "과징금 상한에 막혀 분식회계 가담자에게 제대로 된 책임 못 묻던 구조... | https://www.pinpointnews.co.kr/news/articleView.html?idxno=417014 |  |
| icfr | sejungilbo.com | '고의 분식회계' 과징금 2배로 올린다 | https://www.sejungilbo.com/news/articleView.html?idxno=56600 |  |
| icfr | dailypop.kr | 신뢰의 균열⑤ 수천만명 이용하는 잡코리아·알바몬, 실상은 외국계 사... | http://www.dailypop.kr/news/articleView.html?idxno=95130 |  |
| icfr | news.koreanbar.or.kr | 사법개혁부터 비밀유지권 법안 발의까지… '격변의 해' 2025년 법조신문... | https://news.koreanbar.or.kr/news/articleView.html?idxno=34700 |  |
| icfr | newsroad.co.kr | [입법레이더] 디지털·회계·서민금융… '금융 질서' 전면 재정립 | http://www.newsroad.co.kr/news/articleView.html?idxno=50369 |  |
| icfr | 한국세정신문 | 고의 회계부정 1년 넘으면 매년 과징금 30%씩 가중된다 | https://www.taxtimes.co.kr/news/article.html?no=272588 |  |
| icfr | 조세일보 | 회계정보 조작·감사방해 등 3대 범죄행위, '고의 분식회계’ 수준 처벌 | http://www.joseilbo.com/news/news_read.php?uid=557617&class=18&grp= |  |
| icfr | news.bizwatch.co.kr | 감사방해에 무관용 처벌…'고의 분식' 수준으로 제재 | http://news.bizwatch.co.kr/article/market/2025/11/26/0013 |  |
| icfr | thebell.co.kr | [더벨][템퍼코리아 성장 로드맵 점검]'메모리폼'으로 쌓은 안정적 외형... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202511121359582880106947 |  |
| icfr | biz.chosun.com | “非감사 영역도 공시하라” 당국 주문에 회계업계는 “상장사도 아닌... | https://biz.chosun.com/stock/market_trend/2025/10/24/ICMFPFWKSZCCFGUNGLJIPH4YSQ/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| icfr | 조세일보 | 딸회사 부당지원?…서희건설, 복잡한 순환출자에 장부신뢰도 훼손 | http://www.joseilbo.com/news/news_read.php?uid=555138&class=17&grp= |  |
| icfr | 한국세정신문 | 박찬대 "회계개혁제도 지속 완화에 회계투명성 추락" | https://www.taxtimes.co.kr/news/article.html?no=271972 |  |
| icfr | mediapen.com | 김현정 "빅4 회계법인, 감사보다 컨설팅이 주업" | https://www.mediapen.com/news/view/1050104 |  |
| icfr | 머니투데이 | "가격 또 올려?" 한국서 돈 쓸어 담고…"세금 안 낼래" 명품 회사 '꼼수... | https://www.mt.co.kr/stock/2025/10/02/2025100117504827097 |  |
| icfr | 머니투데이 | "저딴 식으로 건들" 국회도 분노한 태도…책임 회피하는 유한책임회사 | https://www.mt.co.kr/stock/2025/10/02/2025100117084218552 |  |
| icfr | 머니투데이 | 머니투데이 오프라인 헤드라인-2일 | https://www.mt.co.kr/industry/2025/10/02/2025100122052875093 |  |
| icfr | 머니투데이 | 돈 쓸어 담고 세금·감사 나 몰라라…명품부터 테무까지 외국계 기업 '꼼... | https://www.mt.co.kr/stock/2025/10/02/2025093020173573333 |  |
| icfr | 머니투데이 | 여야 법안발의 통했지만...MBK·아디다스 회계 감시법 올해도 무산 | https://www.mt.co.kr/stock/2025/10/02/2025093014344217044 |  |
| icfr | lawleader.co.kr | 서울변호사회 '우수 국회의원상' 이정문 "더 나은 정치하라는 당부" | http://www.lawleader.co.kr/news/articleView.html?idxno=17023 |  |
| icfr | fntimes.com | 양종희號 KB금융, 회계·감사 지배구조 우수기업 선정…감사인 지정 3년... | http://www.fntimes.com/html/view.php?ud=202509101648105745e6e69892f_18 |  |
| icfr | news.tvchosun.com | 금융위, 'KT&G·KB금융·현대차증권' 감사인 지정 유예 | https://news.tvchosun.com/site/data/html_dir/2025/09/10/2025091090216.html |  |
| icfr | ajunews.com | 금융위 "KT&G‧KB금융‧현대차증권 감사인 지정 유예" | https://www.ajunews.com/view/20250910164558078 |  |
| icfr | biz.chosun.com | KT&G·KB금융·현대차증권, 감사인 지정 3년간 유예 | https://biz.chosun.com/stock/stock_general/2025/09/10/AQA6B3DIBBHYLEEFNXFBDH4ENU/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| icfr | srtimes.kr | 케이티앤지·KB금융·현대차증권, 회계·감사 지배구조 우수기업 선정 | http://www.srtimes.kr/news/articleView.html?idxno=185638 |  |
| icfr | 머니투데이 | KT&G 등 회계감사 지배구조 우수기업 선정...감사인 지정 유예 혜택 | http://news.mt.co.kr/mtview.php?no=2025091015411521278 |  |
| icfr | hankookilbo.com | '빅4 법인'이 바뀌어야 회계투명성도 제고된다 [기고] | https://www.hankookilbo.com/News/Read/A2025082910090003288?did=NA |  |
| icfr | biz.chosun.com | 이미 상장폐지 됐는데… 회계 부정 퀀타피아 1심서 무죄, 왜? | https://biz.chosun.com/stock/stock_general/2025/07/21/QZRGFNMWKVCVTHDKR3MCMRXC24/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| icfr | 조세일보 | [구재이 세무사회장 인터뷰] "2년간 다져놓은 혁신의 기틀.. '세무사 황... | http://www.joseilbo.com/news/news_read.php?uid=548244&class=10&grp= |  |
| icfr | 일간NTN | 재무제표 허위 작성·공시 ㈜아스트와 ㈜숲에 감사인지정 등 조치 | http://www.intn.co.kr/news/articleView.html?idxno=2044678 |  |
| icfr | m.skyedaily.com | 24년 회계연도 재무제표 감사의견 ‘적정’ 97.5% | https://m.skyedaily.com/news_view.html?ID=276778 |  |
| icfr | view.asiae.co.kr | D&O 고객 잡아라…바빠진 보험사들 | https://view.asiae.co.kr/article/2025061711314654891 |  |
| icfr | sejungilbo.com | 최운열 공인회계사회장, "회계사-세무사 업무, 본질적으로 다르다" | https://www.sejungilbo.com/news/articleView.html?idxno=53485 |  |
| icfr | thebell.co.kr | [더벨][Sanction Radar]안국저축, 건전성 지표 개선 '뚜렷'…경영정상화... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202505260717314940105968 |  |
| icfr | asiatoday.co.kr | 금감원 "외부감사 대상 기업 증가세 둔화" | https://www.asiatoday.co.kr/view.php?key=20250521010010771 |  |
| icfr | 한국세정신문 | 회계‧감사 지배구조 우수기업 주기적 지정 3년 유예…20일부터 시행 | https://www.taxtimes.co.kr/news/article.html?no=269690 |  |
| icfr | 조세일보 | [단독] 대형회계법인 감사수수료 ‘덤핑’ 공세 시작되나 | http://www.joseilbo.com/news/news_read.php?uid=543215&class=18&grp= |  |
| icfr | ltn.kr | [피플] "한 달에 1건 수임"... 생존 외치는 변호사들 | https://www.ltn.kr/news/articleView.html?idxno=48317 |  |
| icfr | etnews.com | 직권지정 중복 완화, 지정점수 개편에도…불만 여전한 감사인 지정제 | https://www.etnews.com/20250415000185 |  |
| icfr | news.koreanbar.or.kr | 법조삼륜 회동… 변호사제도 개선 논의 일부 진전 | https://news.koreanbar.or.kr/news/articleView.html?idxno=33058 |  |
| icfr | 조세일보 | 이그룹 3사 '상폐'에…회계부정 과징금 대상 '실소유주' 포함되나 | http://www.joseilbo.com/news/news_read.php?uid=539283&class=18&grp= |  |
| icfr | news.bizwatch.co.kr | 분식회계 부당이득 산정안돼도 벌금 10억 부과한다 | http://news.bizwatch.co.kr/article/market/2025/03/13/0042 |  |
| icfr | 머니투데이 | '분식회계 이득 없어' 오리발 안통한다...최대 벌금 '10억원' | http://news.mt.co.kr/mtview.php?no=2025031316422926109 |  |
| icfr | 머니투데이 | '외부감사 유예제' 회계논란기업 감점 확대 | http://news.mt.co.kr/mtview.php?no=2025031311271441204 |  |
| icfr | newsis.com | '지배구조 우수기업 평가위' 본격 가동…위원장 최종학 교수 | https://www.newsis.com/view/NISX20250313_0003097358 |  |
| icfr | donga.com | 변협회장 “탄핵심판, 어떤 결론이든 존중을” | https://www.donga.com/news/People/article/all/20250311/131180558/2 |  |
| icfr | donga.com | “탄핵심판 결론, 어떻게 나오든 존중 필요”… 김정욱 신임 대한변협회... | https://www.donga.com/news/Society/article/all/20250310/131176486/1 |  |
| icfr | lec.co.kr | [설문결과] 올 공인회계사 1차, 체감난도 오르며 가채점 점수↓ | http://www.lec.co.kr/news/articleView.html?idxno=749492 |  |
| icfr | lawleader.co.kr | 김정욱 변협회장 "핵심 모토는 소통…공정한 법조인사 추천" 취임사 | http://www.lawleader.co.kr/news/articleView.html?idxno=15494 |  |
| icfr | news.koreanbar.or.kr | '첫 로스쿨, 40대, 3년 임기' 김정욱 제53대 변협회장 취임 | https://news.koreanbar.or.kr/news/articleView.html?idxno=32706 |  |
| icfr | newspim.com | 김정욱 변협 회장 "정치적 중립 고수...네트워크 로펌 상생안 마련" | https://www.newspim.com/news/view/20250224000807 |  |
| icfr | 매일경제 | 한국세무사회 "지자체 민간위탁 결산 검사 관련 회계사회 주장은 허위" | http://mbn.mk.co.kr/pages/news/newsView.php?category=mbn00013&news_seq_no=5094488 |  |
| icfr | nocutnews.co.kr | 세무사회 "지자체 민간위탁 결산 검사 회계사회 주장은 허위" 정면 반박 | https://www.nocutnews.co.kr/news/6293920?utm_source=naver&utm_medium=article&utm_campaign=20250214102053 |  |
| icfr | tfmedia.co.kr | 한국세무사회 "연간 22조 민간위탁사업 회계감사 부실로 세금 낭비 초래... | https://www.tfmedia.co.kr/news/article.html?no=178723 |  |
| icfr | 한국세정신문 | 한국세무사회 "회계감사로 원상회복시 민간위탁 외부검증제 마비될 것" | https://www.taxtimes.co.kr/news/article.html?no=268408 |  |
| icfr | sejungilbo.com | [학회] 한국의 '회계투명성' 문제…국가경쟁력 지표에 영향 미친다 | https://www.sejungilbo.com/news/articleView.html?idxno=51900 |  |
| icfr | joongang.co.kr | 김정욱 새 변협회장 "정치 극단화...철저히 중립 지키겠다" | https://www.joongang.co.kr/article/25311157 |  |
| icfr | ilyo.co.kr | 대한변협 협회장 김정욱 당선…서울변회 선거에 미칠 영향은 | https://ilyo.co.kr/?ac=article_view&entry_id=485973 |  |
| icfr | ltn.kr | 제53대 변협회장 선거 D-day... 김정욱 VS 안병희 | https://www.ltn.kr/news/articleView.html?idxno=47046 |  |
| icfr | ltn.kr | [서울변회장 후보 인터뷰] "법률시장 확대로 변호사 일자리 창출!"... 기... | https://www.ltn.kr/news/articleView.html?idxno=47014 |  |
| icfr | ltn.kr | [뉴스픽] 대한변협·서울변회 '결전의 날' 임박... 법조단체 새 수장 선... | https://www.ltn.kr/news/articleView.html?idxno=46835 |  |
| icfr | ltn.kr | 김정욱·안병희·금태섭... 대한변협 회장 선거 후보 정책토론회 | https://www.ltn.kr/news/articleView.html?idxno=46855 |  |
| icfr | lawtimes.co.kr | “네트워크 로펌, 거부 명분 없는 규제 시행할 터” | https://www.lawtimes.co.kr/news/204460 |  |
| icfr | news.koreanbar.or.kr | [제53대 대한변협회장 선거] 기호 1번 김정욱 후보 공약 | https://news.koreanbar.or.kr/news/articleView.html?idxno=32347 |  |
| icfr | donga.com | 지배구조 우수기업, 감사인 지정 3년 유예 | https://www.donga.com/news/Economy/article/all/20241231/130763786/2 |  |
| icfr | asiatime.co.kr | [증권소식] 지배구조 우수기업엔 감사인 지정 3년 유예/금감원 "내년 3월... | https://www.asiatime.co.kr/article/20241231500335 |  |
| icfr | pinpointnews.co.kr | 보험사 '고무줄 실적' 논란…일반·감독회계 계리가정 분리 제언 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=499810 |  |
| icfr | newstomato.com | 보험사 실적 흔드는 '계리 가정'…이원화 필요성 제기 | http://www.newstomato.com/ReadNews.aspx?no=1318517&inflow=N |  |
| icfr | thebell.co.kr | [더벨][thebell interview] 김범준 가톨릭대 교수 “영업이익 개념 달라질... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202610201030369960108023 |  |
| icfr | smarttimes.co.kr | 김현지 배우자 출자 '택스탑' 출신, KB·우리캐피탈 사외이사 선임…금... | http://www.smarttimes.co.kr/news/articleView.html?idxno=49834 |  |
| icfr | dailybrief.co.kr | [단독] 금감원, 수협중앙회 가계대출-리스크한도 등 28건 위반사항 적발 | https://www.dailybrief.co.kr/news/articleView.html?idxno=6945 |  |
| icfr | sisajournal-e.com | '3조' 달성 바쁜 한화투자증권에 한화생명은 30년간 6% '배당 족쇄'? | https://www.sisajournal-e.com/news/articleView.html?idxno=424063 |  |
| icfr | fntimes.com | JTBC 채권 사태 신한투자증권까지 불똥 튀나…피해자 단체, 이선훈 대표... | https://www.fntimes.com/html/view.php?ud=2026092115252793492a735e27af_18 |  |
| icfr | kbanker.co.kr | JTBC 채권 피해자 국회로…신한증권 대표 국감 증인 요청 | https://www.kbanker.co.kr/news/articleView.html?idxno=225974 |  |
| icfr | kbanker.co.kr | 소비자 마주한 금감원 1년 성과…"변화 긍정적, 체감은 과제" | https://www.kbanker.co.kr/news/articleView.html?idxno=225971 |  |
| icfr | newsway.co.kr | "'사후구제→사전예방' 성과 인정하지만…" 금융소비자들이 진짜 원하는... | https://www.newsway.co.kr/news/view?ud=2026091717000442139 |  |
| icfr | newswhoplus.com | [긴급진단] 금융위, 조각투자 넘어 주식·채권·펀드 토큰화 추진 | https://www.newswhoplus.com/news/articleView.html?idxno=69091 |  |
| icfr | ajunews.com | 2027년 2월 새로운 시장 열린다…주식‧채권‧펀드도 '토큰화' | https://www.ajunews.com/view/20260904093859697 |  |
| icfr | 매일경제 | “내년 주식·채권·펀드까지 토큰화”…토큰증권 3단계 로드맵 공개 | https://www.mk.co.kr/article/12144125 |  |
| icfr | joongangenews.com | [단독] 금감원, 70개 GA '불법 DB 영업' 검사...벌금·영업정지 '중징계'... | https://www.joongangenews.com/news/articleView.html?idxno=544415 |  |
| icfr | 서울경제 | 증선위 중징계 고려아연 원아시아 투자…7년간 감사위원회 반대 ‘0’ ... | https://www.sedaily.com/article/20084070?ref=naver |  |
| icfr | dailybrief.co.kr | [롯데카드 점검④] 대주주 여신심사-감리-조기경보-공시 '구멍' | https://www.dailybrief.co.kr/news/articleView.html?idxno=6590 |  |
| icfr | thebell.co.kr | [더벨][2026 금융사 이사회 평가] 신한은 매월, 키움은 연 2회…증권사 ... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202608041551518640104010 |  |
| icfr | huffingtonpost.kr | 빗썸 상장하려면 이사회 손봐야 하는데 로드맵엔 빠졌다 : 동일인 이정... | https://www.huffingtonpost.kr/article/259300 |  |
| icfr | thetracker.co.kr | 금융지주 회장 ‘3연임 제한’ 제동…법 개정 대신 모범규준으로 후퇴하... | https://thetracker.co.kr/View.aspx?No=4173014 |  |
| icfr | thebell.co.kr | [더벨][기로에 선 현대차그룹 벤더사] 이사회 합류 황선찬 서연이화 CFO... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202607221448381720106978 |  |
| icfr | hansbiz.co.kr | [ESG포커스] 한신공영, 대표·이사회 의장 겸임 유지 | http://www.hansbiz.co.kr/news/articleView.html?idxno=850196 |  |
| icfr | datanews.co.kr | 동박 3사 지배구조 격차…SKC 86.7%, 솔루스 26.7% | http://www.datanews.co.kr/news/article.html?no=145245 |  |
| icfr | datanews.co.kr | 지배구조 준수율, LG화학·한화솔루션 선두…금호석화 60% 그쳐 | http://www.datanews.co.kr/news/article.html?no=145213 |  |
| icfr | hansbiz.co.kr | [기업지배구조 보고서 톺아보기] 태광산업, 밸류업 앞 '이호진 리스크'... | http://www.hansbiz.co.kr/news/articleView.html?idxno=845051 |  |
| icfr | hansbiz.co.kr | ESG행복경제연구소, 유가증권시장 全상장사 '기업지배구조 보고서' 분석 | http://www.hansbiz.co.kr/news/articleView.html?idxno=844626 |  |
| icfr | thebell.co.kr | [더벨][기업지배구조보고서 점검] 프리드라이프로 덩치 키운 웅진, 주주... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202606091451489360107422 |  |
| icfr | consumernews.co.kr | SK텔레콤, 지배구조 핵심지표 15건 모두 준수...SK오션플랜트, SK바이오... | http://www.consumernews.co.kr/news/articleView.html?idxno=757091 |  |
| icfr | popcornnews.net | CJ, 지배구조 선진화 고삐...'주주 친화·이사회 경영'으로 기업가치 높... | http://www.popcornnews.net/news/articleView.html?idxno=123029 |  |
| icfr | popcornnews.net | 해태제과, 감사·내부통제는 강화했지만...승계·배당·이사회 독립성은... | http://www.popcornnews.net/news/articleView.html?idxno=123045 |  |
| icfr | bloter.net | [지배구조 리포트] 시프트업, 사외이사 견제·대표이사 실행력 '투트랙... | https://www.bloter.net/news/articleView.html?idxno=664043 |  |
| icfr | lawissue.co.kr | [이슈 상장기업] 배임 의혹 불거진 MS그룹, 내부통제는 없었다…명신산... | http://www.lawissue.co.kr/view.php?ud=2026060115165158059817d053b9_12 |  |
| icfr | asiatime.co.kr | [증권 뉴스브리핑] 국민성장펀드 3만명, 평균 2000만원 가입·퓨리오사A... | https://www.asiatime.co.kr/article/20260529500380 |  |
| icfr | huffingtonpost.kr | [K-증권사 이사회 점검] 하나증권 대표 강성묵 임추위 빠지며 독립성에... | https://www.huffingtonpost.kr/article/257524 |  |
| icfr | hansbiz.co.kr | [금융지주 보험사 분석]③신한금융, 증권 강세지만...보험·카드 체질개... | http://www.hansbiz.co.kr/news/articleView.html?idxno=840099 |  |
| icfr | huffingtonpost.kr | [지방은행 이사회 점검] JB금융 '양 날개' 광주·전북은행 이사회에 스민... | https://www.huffingtonpost.kr/article/257073 |  |
| icfr | asiatime.co.kr | [증권 뉴스브리핑] 종투사 '발행어음·IMA' 57조 조달…모험자본 9.9조 공... | https://www.asiatime.co.kr/article/20260421500437 |  |
| icfr | fntimes.com | 증권사 사외이사 이사회의장 60% 근접…사외이사인 감사위원 확대 [사외... | http://www.fntimes.com/html/view.php?ud=202604131055549502179ad43907_18 |  |
| icfr | 매일경제 | 부동산신탁사 CEO 만난 금감원 “7월 책무구조도 도입…사익추구 즉각 ... | https://www.mk.co.kr/article/11992833 |  |
| icfr | 머니투데이 | 금감원 "부동산신탁사 7월부터 책무구조도 도입…내부통제 철저" | https://www.mt.co.kr/stock/2026/03/19/2026031917182943096 |  |
| icfr | hankookilbo.com | PF 부실·소송 리스크에…금감원 "신탁사 내부통제·재무 관리 강화" 주... | https://www.hankookilbo.com/news/article/A2026031916480000530?did=NA |  |
| icfr | ebn.co.kr | 금감원, 부동산신탁사 CEO 소집…"외형보다 내실 다져라" | https://www.ebn.co.kr/news/articleView.html?idxno=1702843 |  |
| icfr | 파이낸셜뉴스 | 금감원, 부동산신탁사에 리스크 관리 압박…“내실 다져라” | http://www.fnnews.com/news/202603191523028754 |  |
| icfr | dailian.co.kr | "임직원 사익추구 고질적 문제"…금감원, 부동산신탁사 CEO 간담회 | https://www.dailian.co.kr/news/view/1622898/?sc=Naver |  |
| icfr | ajunews.com | 금감원, 부동산신탁사 CEO 소집…"PF 부실 속 내부통제·유동성 관리 강... | https://www.ajunews.com/view/20260319150611332 |  |
| icfr | newspim.com | 금감원, 부동산신탁사 14곳 CEO 소집…책무구조도·건전성 관리 강화 압... | https://www.newspim.com/news/view/20260319000935 |  |
| icfr | metroseoul.co.kr | 금감원, 부동산신탁사 CEO 소집…내부통제·소비자보호·PF 리스크 전방... | http://www.metroseoul.co.kr/article/20260319500150 |  |
| icfr | nocutnews.co.kr | "몸집보단 책임을 키우자"…금감원, 부동산 신탁사 간담회 | https://www.nocutnews.co.kr/news/6487550?utm_source=naver&utm_medium=article&utm_campaign=20260319030017 |  |
| icfr | etoday.co.kr | 부동산신탁사 CEO 불러모은 금감원…"책무구조도·소비자보호 직접 챙겨... | https://www.etoday.co.kr/news/view/2567140 |  |
| icfr | view.asiae.co.kr | 금감원, 신탁사 책무구조도 앞두고 ‘내부통제·소비자 보호’ 주문 | https://view.asiae.co.kr/article/2026031911071503066 |  |
| icfr | m.skyedaily.com | “책준형 소송 패소 없게”… 당국, 신탁사 책무구조도 앞둔 당부 | https://m.skyedaily.com/news_view.html?ID=300655 |  |
| icfr | financialpost.co.kr | 금감원, 종투사에 "부동산 PF 부실 채권 정리" 등 리스크 관리 당부 | https://www.financialpost.co.kr/news/articleView.html?idxno=251663 |  |
| icfr | asiatime.co.kr | [증권 뉴스브리핑] 이 대통령, 18일 '자본시장 4대 개혁안' 간담회/금감... | https://www.asiatime.co.kr/article/20260313500005 |  |
| icfr | cbci.co.kr | [금융家] 이찬진 금융감독원장 ② ∣ '금융권과 소비자' 동반자 관계로... | https://www.cbci.co.kr/news/articleView.html?idxno=560599 |  |
| icfr | metroseoul.co.kr | 韓 딜로이트 CCG “감사위원회, 외부감사인에 핵심 질문 던져야” | http://www.metroseoul.co.kr/article/20260312500294 |  |
| icfr | 조세일보 | 한국딜로이트그룹, 소통 실질화 위한 4대 핵심 점검 영역 제시 | http://www.joseilbo.com/news/news_read.php?uid=564440&class=10&grp= |  |
| icfr | news.tf.co.kr | "당국 지배구조 압박에…" 금융지주 사외이사 '전문가 모시기' 경쟁 | https://news.tf.co.kr/read/economy/2298824.htm |  |
| icfr | dealsite.co.kr | 신한금융, 3년째 '연 2명' 사외이사 교체…순환구조 굳건 | https://dealsite.co.kr/articles/157829 |  |
| icfr | theviewers.co.kr | [폭풍전야 DB금융②] ‘옥상옥상옥’ 이사회 | https://theviewers.co.kr/View.aspx?No=3981469 |  |
| icfr | ebn.co.kr | [EBN 칼럼] ESG의 현주소와 내부감사 | https://www.ebn.co.kr/news/articleView.html?idxno=1695237 |  |
| icfr | sisaweek.com | 금융위, 상호금융 제도개선 발표… 건전성·부동산PF 규제 강화 | https://www.sisaweek.com/news/articleView.html?idxno=232096 |  |
| icfr | viva100.com | 금융위 “상호금융, 부동산대출에 과도한 의존…반성해야” | https://www.viva100.com/article/20251223500626 |  |
| icfr | 조세일보 | 금융위 “상호금융 체질 개선 불가피”… PF·지배구조 동시 손본다 | http://www.joseilbo.com/news/news_read.php?uid=559357&class=18&grp= |  |
| icfr | srtimes.kr | 상호금융 '부동산 의존' 벗긴다…PF 규제 강화·지배구조 손본다 | http://www.srtimes.kr/news/articleView.html?idxno=192743 |  |
| icfr | widedaily.com | 상호금융권 '대표 장기 집권' 방지 장치 마련… 제재 실효성 높인다 | https://www.widedaily.com/news/articleView.html?idxno=285462 |  |
| icfr | asiatime.co.kr | 상호금융중앙회 대체투자 관리 강화…"손실흡수능력 상향" | https://www.asiatime.co.kr/article/20251223500089 |  |
| icfr | view.asiae.co.kr | 금융위, 상호금융 제도개선 발표…PF대출 한도 신설 | https://view.asiae.co.kr/article/2025122217271287683 |  |
| icfr | newsis.com | 상호금융권 '대표 장기 집권' 방지 장치 마련… 제재 실효성 높인다 | https://www.newsis.com/view/NISX20251222_0003451051 |  |
| icfr | dt.co.kr | 부동산 편중 대출 관행 개선…상호금융권, PF 대출 한도 20% ‘제한’ | https://www.dt.co.kr/article/12036703?ref=naver |  |
| icfr | newsway.co.kr | 금융당국, 상호금융권 체질개선 착수…부동산 대출 줄이고 서민금융 강... | https://www.newsway.co.kr/news/view?ud=2025122217223690670 |  |
| icfr | newsworks.co.kr | 금융위, 상호금융 PF·지배구조 쇄신…'강도 높은 체질개선' 시동 | https://www.newsworks.co.kr/news/articleView.html?idxno=824206 |  |
| icfr | biz.sbs.co.kr | 권대영 "상호금융 자산 1천조…사고 줄이고 생산금융 늘려야" | https://biz.sbs.co.kr/article_hub/20000280168?division=NAVER |  |
| icfr | news1.kr | 상호금융중앙회 자기자본비율 7%로 단계적 높인다…저축은행 수준 | https://www.news1.kr/finance/general-finance/6016863 |  |
| icfr | upkoreanews.kr | 박지원 체제 두산에너빌리티, 실적 폭발 속 '지배구조 D등급'에 '지배구... | https://www.upkoreanews.kr/news/articleView.html?idxno=96307 |  |
| icfr | popcornnews.net | 이선훈 사장 '내부통제' 통했다…신한증권, 지배구조 평가 4년 연속 'A' | http://www.popcornnews.net/news/articleView.html?idxno=104812 |  |
| icfr | dailian.co.kr | '부실 뇌관' 된 상호금융 공동대출…연체율 급등에 경고등 | https://www.dailian.co.kr/news/view/1582310/?sc=Naver |  |
| icfr | asiatime.co.kr | [증권소식] 법원, 방시혁 하이브 주식 1568억 동결/금융위 내년 예산 4.7... | https://www.asiatime.co.kr/article/20251204500440 |  |
| icfr | asiatime.co.kr | [증권소식] 3분기 코스피 누적 순이익 전년비 25.8% 증가/골드만삭스 "미... | https://www.asiatime.co.kr/article/20251118500456 |  |
| icfr | businesspost.co.kr | 키움증권 이사회 갖출 것은 다 갖췄지만, 후계자 김동준 의장 선임으로... | https://www.businesspost.co.kr/BP?command=article_view&num=418535 |  |
| icfr | 한국경제 | BNK금융 겨냥한 이찬진 "회장 선임절차 특이해" | https://www.hankyung.com/article/2025102133871 |  |
| icfr | 임팩트온 | 【김형주, 장정민의 지속가능경영 스토리】한국 기업지배구조, '선언'을... | http://www.impacton.net/news/articleView.html?idxno=16795 |  |
| icfr | asiatime.co.kr | [증권소식] 거래소 "9월 국내 금값, 국제 시세보다 비싸"/박현주 "미래에... | https://www.asiatime.co.kr/article/20251002500007 |  |
| icfr | wemakenews.co.kr | “순이익보다 많은 마케팅 비용…빗썸 ‘먹통 1등’ 오명 벗을까” | http://wemakenews.co.kr/news/view.php?no=22806 |  |
| icfr | thebell.co.kr | [더벨][2025 이사회 평가]삼성바이오로직스, 구성·견제기능·객관성 확... | https://www.thebell.co.kr/free/content/ArticleView.asp?key=202508221445488640109443 |  |
| icfr | newstomato.com | 이억원 금융위원장 후보·이찬진 금감원장 사사건건 '충돌' | http://www.newstomato.com/ReadNews.aspx?no=1273737&inflow=N |  |
| icfr | fntimes.com | 이억원 후보 "스테이블코인 규제 만전···생산적금융 도모" [금융위원... | http://www.fntimes.com/html/view.php?ud=202509022155036395b4a7c6999c_18 |  |
| icfr | metroseoul.co.kr | 한국 딜로이트 그룹, '기업지배기구발전센터 자문위원단 위촉식' 개최 | http://www.metroseoul.co.kr/article/20250901500247 |  |
| icfr | 조세일보 | 한국 딜로이트 그룹, 자문위원단 재편…교수진 합류 | http://www.joseilbo.com/news/news_read.php?uid=551665&class=10&grp= |  |
| icfr | view.asiae.co.kr | 한국 딜로이트 그룹, 기업지배기구센터 자문위원단에 '노준화·박종성·... | https://view.asiae.co.kr/article/2025090110260152154 |  |
| icfr | 머니투데이 | 한국딜로이트, 기업지배기구센터 자문위원단에 '노준화·박종성·임정하... | http://news.mt.co.kr/mtview.php?no=2025090110003387546 |  |
| icfr | biz.chosun.com | 한국 딜로이트, 기업지배기구센터 자문위원단에 ‘노준화·박종성·임정... | https://biz.chosun.com/stock/stock_general/2025/09/01/KMUMOGAKZNDJNHX3TXBV3UVT3Q/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| icfr | etoday.co.kr | 한국 딜로이트그룹, 기업지배기구센터 자문위원단에 노준화·박종성·임... | https://www.etoday.co.kr/news/view/2501778 |  |
| icfr | sisaon.co.kr | 한국증권금융, 김건희 집사 게이트 연루 이어 악재 잇달아…옐로카드 꺼... | http://www.sisaon.co.kr/news/articleView.html?idxno=174448 |  |
| icfr | ajunews.com | [전문가 기고] 상법 개정 이후 기업의 과제 | https://www.ajunews.com/view/20250813105505712 |  |
| icfr | 한국경제 | "주가지수 5000 시대 '첫걸음'…구체적 실행 방안 마련해야"[이재명 ESG ... | https://www.hankyung.com/article/202507198817i |  |
| icfr | finomy.com | GA, 설계사 모시기 과열...당국 '주시' | http://www.finomy.com/news/articleView.html?idxno=234648 |  |
| icfr | hansbiz.co.kr | 현대엘리베이터, 환경 부문 '도약'...온실가스 51% 감축 '조기 달성' [25... | http://www.hansbiz.co.kr/news/articleView.html?idxno=758504 |  |
| icfr | news.bizwatch.co.kr | 김용태 협회장 "GA업계 고질적 문제, 비판 달게 받겠다" | http://news.bizwatch.co.kr/article/finance/2025/06/25/0012 |  |
| icfr | businesspost.co.kr | [Who Is ?] 김용범 대통령실 정책실장 | https://www.businesspost.co.kr/BP?command=article_view&num=400472 |  |
| icfr | dealsite.co.kr | [캡티브영업 정조준] 구멍난 '동회차 참여금지'…만기별로 PI부서 투입 | https://dealsite.co.kr/articles/143341 |  |
| esg | ceoscoredaily.com | 손보사 책임보험금 1년새 20%↑…삼성화재·DB·KB손보가 증가분의 94% 차... | https://www.ceoscoredaily.com/page/view/2026102820534298738 |  |
| esg | newspenguin.com | 삼성생명 숨은 배출량 80% 더 나왔는데..."감축 목표와는 별개" | https://www.newspenguin.com/news/articleView.html?idxno=22362 |  |
| esg | dnews.co.kr | 2027년 건설업계 경영전략은…‘리스크 방어’과 ‘기회 포착’ | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610291028052220705 |  |
| esg | ESG경제 | 한국공인회계사회, '제27회 지속가능성인증포럼' 웨비나 | https://www.esgeconomy.com/news/articleView.html?idxno=17175 |  |
| esg | 1conomynews.co.kr | LG유플러스, ESG 등급 하락하나…해킹 은폐 의혹에 보고서도 오락가락 | https://www.1conomynews.co.kr/news/articleView.html?idxno=51040 |  |
| esg | biz.heraldcorp.com | 한공회, 내달 ‘제27회 지속가능성인증포럼’ 개최 | https://biz.heraldcorp.com/article/10919348?ref=naver |  |
| esg | 임팩트온 | 10월 4주차 국내 ESG 핫클립 | https://www.impacton.net/news/articleView.html?idxno=30458 |  |
| esg | 임팩트온 | 10월 4주차 해외 ESG 핫클립 | https://www.impacton.net/news/articleView.html?idxno=30456 |  |
| esg | 한국경제 | 스튜어드십 코드 개정 및 기관투자자 주주권 행사 강화 관련 기업의 유... | https://www.hankyung.com/article/202610280467r |  |
| esg | 매일경제 | 국제ESG협회, 그린워싱 대응 논의… 환경·경영·법률 전문가 한자리에 | https://www.mk.co.kr/article/12189601 |  |
| esg | 임팩트온 | 【규제트래커】 루프트한자 항공권서 '그린' 삭제…진코 ESS는 리튬 공급... | https://www.impacton.net/news/articleView.html?idxno=30443 |  |
| esg | etoday.co.kr | 리처드 본 에코바디스 부사장 "ESG 등급은 수출 여권이자 금융자산" | https://www.etoday.co.kr/news/view/2640778 |  |
| esg | 임팩트온 | 【공시 모니터링】 한국전력, 전력망 투자 72.8조원 계획...기후위험 재... | https://www.impacton.net/news/articleView.html?idxno=30312 |  |
| esg | 임팩트온 | GHG프로토콜, 기업 반발에 스코프2 현행 방식 당분간 병행 허용 | https://www.impacton.net/news/articleView.html?idxno=30408 |  |
| esg | 임팩트온 | 기후공시, 숫자만으론 부족…기업의 기후위험, 투자 판단으로 연결해야 | https://www.impacton.net/news/articleView.html?idxno=30403 |  |
| esg | ESG경제 | [특별기고] 지속가능성 공시 인증, 제대로 준비해 조기정착해야 | https://www.esgeconomy.com/news/articleView.html?idxno=17131 |  |
| esg | hansbiz.co.kr | [ESG 칼럼] ESG 시대 '솔로의 역설' | http://www.hansbiz.co.kr/news/articleView.html?idxno=876065 |  |
| esg | etoday.co.kr | 글로벌 ESG 공급망 평가기준 개편…韓 기업 대응 분주 [ESGX] | https://www.etoday.co.kr/news/view/2639380 |  |
| esg | lawissue.co.kr | 화우·대한상의, 지속가능성 공시 법률리스크 세미나 개최 | https://www.lawissue.co.kr/view.php?ud=202610231939534382f4ab64559d_12 |  |
| esg | lawtimes.co.kr | 화우·대한상의, 지속가능성 공시·공급망 규제 대응 방안 논의 | https://www.lawtimes.co.kr/news/articleView.html?idxno=228261 |  |
| esg | 일간NTN | 화우-대한상의, '지속가능성 제도화와 기업 대응' 세미나 성료 | http://www.intn.co.kr/news/articleView.html?idxno=2054280 |  |
| esg | weekly.hankooki.com | 화우·대한상의, 지속가능성 공시 앞두고 기업 법률리스크 점검 | https://weekly.hankooki.com/news/articleView.html?idxno=7190429 |  |
| esg | view.asiae.co.kr | [로펌은 지금]화우, '지속가능성 제도화에 따른 기업 리스크와 대응 체... | https://view.asiae.co.kr/article/2026102313294179168 |  |
| esg | ESG경제 | 지속가능성 공시 지배기업 자료 요구권 "재무공시와 동일" | https://www.esgeconomy.com/news/articleView.html?idxno=17103 |  |
| esg | 서울경제 | 화우, ESG 법률리스크 대응 세미나 개최...“국내외 법령충돌 선제 점검... | https://www.sedaily.com/article/20105273?ref=naver |  |
| esg | 머니투데이 | 법무법인 화우, '지속가능성 제도화와 기업 대응' 세미나 성료 | https://www.mt.co.kr/society/2026/10/23/2026102310452370802 |  |
| esg | newspim.com | [로펌이슈] 화우·대한상의, ESG 법률리스크 대응 세미나 개최 | https://www.newspim.com/news/view/20261023000390 |  |
| esg | biz.chosun.com | 법무법인 화우, 지속가능성 공시·ESG 법률리스크 대응 세미나 개최 | https://biz.chosun.com/topics/law_firm/2026/10/23/DY3SFKPKOBE5VDXYLQNZNBDXMM/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| esg | yonhapnewstv.co.kr | 한국형 녹색 대전환…ESG 친환경대전 열려 | http://www.yonhapnewstv.co.kr/news/MYH20261022211311Spl |  |
| esg | venturesquare.net | 마이오렌지, 팁스 R&D 선정…10억6000만원 투입해 AI 임팩트 측정 자동화... | https://www.venturesquare.net/1122021/ |  |
| esg | 한국경제 | [단독] 정부부터 안 지키는 장애인기업 구매의무…외교·산업부도 미달 | https://www.hankyung.com/article/202610228003i |  |
| esg | discoverynews.kr | LG디스플레이-국립생태원, 자연자본 평가부터 생태계 복원까지 협력 | https://www.discoverynews.kr/news/articleView.html?idxno=1104681 |  |
| esg | 임팩트온 | 10월 3주차 국내 ESG 핫클립 | https://www.impacton.net/news/articleView.html?idxno=30356 |  |
| esg | 임팩트온 | 10월 3주차 해외 ESG 핫클립 | https://www.impacton.net/news/articleView.html?idxno=30357 |  |
| esg | mediapen.com | [ESG특별기고]기후를 넘어 자연으로, 자본시장이 던지는 다음 질문 | https://www.mediapen.com/news/view/1131450 |  |
| esg | news1.kr | 포스코 지역사회 문화예술 동행…포항에서 타오르고 광양·서울로 | https://www.news1.kr/industry/general-industry/6328151 |  |
| esg | ekn.kr | [기후경영 포럼] 고순현 에코앤파트너스 부사장 “탄소회계, 제품별 배... | https://www.ekn.kr/web/view.php?key=20261021029149215 |  |
| esg | ccnnews.co.kr | 목원대, 中 산시성 3개 대학과 국제교류 협력 | http://www.ccnnews.co.kr/news/articleView.html?idxno=416556 |  |
| esg | moneystorm.kr | [시장추적] 한화손보, F&F홀딩스,도이치모터스, 체리부로도 부랴부랴 PB... | https://www.moneystorm.kr/news/articleView.html?idxno=7470 |  |
| esg | ddaily.co.kr | 동국제강, 공급망 ESG 우수기업 2곳 선정…동반성장 강화 | https://www.ddaily.co.kr/page/view/2026102109463134575 |  |
| esg | dt.co.kr | [기획] ESG, 끝물 아닌 전환점… AI시대 ‘공생법’ 찾아라 | https://www.dt.co.kr/article/12090207?ref=naver |  |
| esg | jeonmae.co.kr | 목원대 이민재 교수 "눈속임 ESG 안 통한다" | https://www.jeonmae.co.kr/news/articleView.html?idxno=1303364 |  |
| esg | newsworker.co.kr | 콘진원, '지배구조 혁신 인정'... 한국 ESG 혁신정책 대상 5년 연속 수상 | https://www.newsworker.co.kr/news/articleView.html?idxno=509584 |  |
| esg | shindonga.donga.com | 제10회 ‘K사회적가치‧ESG, 경제를 살리다’ 포럼 열린다 | https://shindonga.donga.com/3/all/13/6426055/1 |  |
| esg | ggilbo.com | 목원대 이민재 교수, 이해관계자 행동 통한 '리커플링' 역학 규명 | https://www.ggilbo.com/news/articleView.html?idxno=1188008 |  |
| esg | ibabynews.com | [ESG트렌드] LG유니참, 친환경 생산부터 위생용품 기부까지 ESG 경영 강화... | https://www.ibabynews.com/news/articleView.html?idxno=155384 |  |
| esg | news.einfomax.co.kr | 반도체 공정서도 나오는 '영원한 화학물질'…폐수 관리 사각지대 | https://news.einfomax.co.kr/news/articleView.html?idxno=4440057 |  |
| esg | businesspost.co.kr | [Who Is ?] 이문화 삼성화재 대표이사 사장 | https://www.businesspost.co.kr/BP?command=article_view&num=449248 |  |
| esg | news.dealsitetv.com | 한국의결권자문, 달라지는 주총 셈법 짚는다…내달 17일 세미나 | https://news.dealsitetv.com/articles/177172 |  |
| esg | newstomato.com | 상장협, ESG 법정공시 앞두고 '실무 대비' 본격화 | http://www.newstomato.com/ReadNews.aspx?no=1317186&inflow=N |  |
| esg | viva100.com | 상장협, 2028년 ESG 의무공시 앞두고 상장사 실무교육 | https://www.viva100.com/article/20261019500933 |  |
| esg | biz.heraldcorp.com | 상장협, ESG 법정 공시 핵심 실무 쟁점 미리 챙긴다 | https://biz.heraldcorp.com/article/10907273?ref=naver |  |
| esg | cstimes.com | 공무원연금공단, 상장사 163곳에 기후공시 강화 촉구 투자자 서한 발송 | https://www.cstimes.com/news/articleView.html?idxno=724296 |  |
| esg | ilemonde.com | [기획특집 코리아디스카운트 ①] 이재명 정부의 세 차례 상법 개정…한... | https://www.ilemonde.com/news/articleView.html?idxno=30804 |  |
| esg | thefirstmedia.net | 공무원연금공단, 기후공시 의무화 앞두고 국내 주요 상장사 163곳에 기후... | http://www.thefirstmedia.net/news/articleView.html?idxno=211130 |  |
| esg | biz.heraldcorp.com | 공무원연금공단, 상장기업 163개사에 “기후공시 강화” 요청 | https://biz.heraldcorp.com/article/10905214?ref=naver |  |
| esg | weekly.hankooki.com | 공무원연금공단, 주요 상장기업에 '기후공시 강화 요청' 투자자 서한 | https://weekly.hankooki.com/news/articleView.html?idxno=7189301 |  |
| esg | popcornnews.net | 공무원연금공단 "상장사 163곳에 기후공시 강화 요구…투자 판단에 반영... | http://www.popcornnews.net/news/articleView.html?idxno=136244 |  |
| esg | view.asiae.co.kr | 공무원연금공단 "주요 상장사에 기후공시 강화 요청" | https://view.asiae.co.kr/article/2026101611552695622 |  |
| esg | newsis.com | 공무원연금공단, 163개 상장사에 기후공시 강화 요청…투자자 서한 | https://www.newsis.com/view/NISX20261016_0003828813 |  |
| esg | ESG경제 | [해외브리핑] 美 캘리포니아, 기후공시 규정 최종 승인…첫 배출량 보고... | https://www.esgeconomy.com/news/articleView.html?idxno=17028 |  |
| esg | biz.chosun.com | 스틱 품은 美 미리캐피탈, 韓 중소형주 ‘줍줍’… 올해만 5곳 지분 5% 넘... | https://biz.chosun.com/stock/market_trend/2026/10/16/RU4E4DRRKBHVPBI4QK3ULTRHWI/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| esg | 임팩트온 | 에코바디스, ESG 평가기준 개편…정량목표 기준연도 의무화 | https://www.impacton.net/news/articleView.html?idxno=30267 |  |
| esg | srtimes.kr | 현대제철, '스틸리 어워드' 첫 수상…탄소 배출 기준 공인받아 | http://www.srtimes.kr/news/articleView.html?idxno=214862 |  |
| esg | 임팩트온 | 10월 2주차 해외 ESG 핫클립 | https://www.impacton.net/news/articleView.html?idxno=30256 |  |
| esg | 임팩트온 | 【공시 모니터링】 삼성생명, 투자자산 탄소비용 8826억원 산정…전 직... | https://www.impacton.net/news/articleView.html?idxno=30233 |  |
| esg | e2news.com | "향후 화학산업 경쟁력 탄소중립에 달렸다" | http://www.e2news.com/news/articleView.html?idxno=335043 |  |
| esg | etoday.co.kr | [ESGX 이슈 5] 美 캘리포니아 기후공시 시행규칙 최종 승인…기업 배출... | https://www.etoday.co.kr/news/view/2635609 |  |
| esg | siminilbo.co.kr | [기고] 절차와 기준이 빚어내는 신뢰... 공공기관 ESG, '보여주기'를 넘... | https://www.siminilbo.co.kr/news/newsview.php?ncode=1160286735456383 |  |
| esg | joongang.co.kr | KB금융, 100대 기업 ESG 평가 1위…금융업 선두 속 기업 전반 점수 상승 | https://www.joongang.co.kr/article/25469312 |  |
| esg | dailysecu.com | [기획연재 6] 합법적 권한 뒤에 숨은 '우회 유출'… 앤드포인드 최전방... | https://www.dailysecu.com/news/articleView.html?idxno=208827 |  |
| esg | rapportian.com | [헬스인·싸] 병원 ESG, '공통 지표'와 '단계적 적용'이 필요할 때 | https://www.rapportian.com/news/articleView.html?idxno=241091 |  |
| esg | viva100.com | 동아쏘시오그룹, 제2 협력사 대상 ESG 공급망 교육 개최 | https://www.viva100.com/article/20261011500209 |  |
| esg | ftoday.co.kr | [ESG브리핑-10월2주] 포스코, 광양시와 함께 '파노라마 워크' 조성 외 | http://www.ftoday.co.kr/news/articleView.html?idxno=366976 |  |
| esg | thepublic.kr | 동아쏘시오그룹, 협력사 대상 ESG공급망 교육 개최…상생 경영 실천 | https://www.thepublic.kr/news/articleView.html?idxno=321635 |  |
| esg | bizwnews.com | 동아쏘시오그룹, 협력사 대상 'ESG 공급망 교육' 실시…"관리 역량 강화... | http://www.bizwnews.com/news/articleView.html?idxno=148402 |  |
| esg | job-post.co.kr | 동아쏘시오그룹, 협력사 대상 ESG 공급망 교육 | https://www.job-post.co.kr/news/articleView.html?idxno=231439 |  |
| esg | businesskorea.co.kr | 동아쏘시오그룹, 협력사 ESG 역량 강화 지원... 공급망 리스크 선제 대응 | https://www.businesskorea.co.kr/news/articleView.html?idxno=278524 |  |
| esg | industrynews.co.kr | 동아쏘시오그룹, 제2회 협력사 ESG 공급망 교육 개최…공시 의무화 대응... | https://www.industrynews.co.kr/news/articleView.html?idxno=87253 |  |
| esg | queen.co.kr | 동아쏘시오그룹, 협력사와 ESG 공급망 교육 진행해 | http://www.queen.co.kr/news/articleView.html?idxno=464466 |  |
| esg | swtvnews.com | 동아쏘시오그룹, 협력사 대상 ‘ESG공급망 교육’ 진행…실무 대응력 강... | https://swtvnews.com/news/newsview.php?ncode=1065575432026801 |  |
| esg | newsclaim.co.kr | 유한양행 JW중외제약 동아제약 外(제약보국) | https://www.newsclaim.co.kr/news/articleView.html?idxno=3077917 |  |
| esg | smarttimes.co.kr | [제약·바이오소식] 동아쏘시오그룹ㆍ동아제약ㆍ에스티팜 | http://www.smarttimes.co.kr/news/articleView.html?idxno=49593 |  |
| esg | mydaily.co.kr | [MD 제약바이오] 동아쏘시오그룹, 협력사 대상 ESG 공급망 교육 개최 | https://www.mydaily.co.kr/page/view/2026100816400321566 |  |
| esg | tfmedia.co.kr | 회계사회, ‘지속가능성 공시 사전인증’ 내달 5일 포럼 개최 | https://www.tfmedia.co.kr/news/article.html?no=208480 |  |
| esg | choicenews.co.kr | 하나금융, 지난해 ESG 가치 6.86조원 창출…포용금융 확대 | http://www.choicenews.co.kr/news/articleView.html?idxno=172712 |  |
| esg | view.asiae.co.kr | KICPA, '제27회 지속가능성인증포럼' 개최 | https://view.asiae.co.kr/article/2026102910070391935 |  |
| esg | 일간NTN | 회계사회, 내달 5일 '제27회 지속가능성인증포럼' 개최 | http://www.intn.co.kr/news/articleView.html?idxno=2054378 |  |
| esg | 조세일보 | 회계사회, 지속가능성 공시 인증 준비 본격 논의…내달 5일 포럼 | http://www.joseilbo.com/news/news_read.php?uid=578413&class=10&grp= |  |
| esg | sejungilbo.com | 한공회, 내달 5일 포럼서 '지속가능성 공시 인증 준비와 사전인증' 발표 | https://www.sejungilbo.com/news/articleView.html?idxno=60856 |  |
| esg | 이데일리 | 한공회, 내달 5일 ‘제27회 지속가능성인증포럼’ 개최 | https://www.edaily.co.kr/News/Read?newsId=03148806645617840&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| esg | ESG경제 | 삼성화재·생명에 "석탄 보험·투자 중단하라"…16개 단체 촉구 | https://www.esgeconomy.com/news/articleView.html?idxno=17140 |  |
| esg | newstree.kr | "석탄사업에 보험·투자 중단해야”…시민단체, 삼성화재·삼성생명에 ... | https://www.newstree.kr/newsView/ntr202610270007 |  |
| esg | newsroad.co.kr | 석탄보험은 계속, 철수 시한은 없다…삼성화재·삼성생명 탈석탄 압박 | http://www.newsroad.co.kr/news/articleView.html?idxno=66501 |  |
| esg | ESG경제 | 아이이에스지, 경기 기후테크 컨퍼런스 참가…기후데이터 협력 확대 | https://www.esgeconomy.com/news/articleView.html?idxno=17125 |  |
| esg | 한국경제 | “전환 자금 물꼬 트려면 한국형 기후벤치마크 도입이 필수” | https://magazine.hankyung.com/business/article/202610231900b |  |
| esg | bizhankook.com | '무늬만 친환경' 투자 넘어서려면…한국형 기후 벤치마크의 성공조건 | https://bizhankook.com/articles/korea-climate-finance-investment-strategy.html |  |
| esg | ekn.kr | [기후경영 포럼] “기후공시, 탄소배출량 넘어 기업의 대응 전략·재무... | https://www.ekn.kr/web/view.php?key=20261021025119233 |  |
| esg | ekn.kr | 기업 탄소감축 실행방안 모색…‘대한민국 GX 기후경영포럼’ 개최 | https://www.ekn.kr/web/view.php?key=20261021025068660 |  |
| esg | news2day.co.kr | [ESG 인사이드 (98)] 지속가능성 공시, 기준이 아니라 경영을 보라(下) | https://www.news2day.co.kr/article/20261020500215 |  |
| esg | ekn.kr | 에너지경제·국가녹색기술硏, ‘GX 기후경영 포럼 2026’ 21일 개최 | https://www.ekn.kr/web/view.php?key=20261020020418476 |  |
| esg | 일간NTN | 한국회계연구원(KARI) KARI Accounting and Sustainability Research Seminar... | http://www.intn.co.kr/news/articleView.html?idxno=2054166 |  |
| esg | 임팩트온 | 【공시 모니터링】㈜한화, 폭염으로 인한 재무영향 39억원 추산…임원 ... | https://www.impacton.net/news/articleView.html?idxno=30271 |  |
| esg | 임팩트온 | EU 그린워싱 규제, 기존 재고도 적용...국내 100대 기업, 가장 많이 쓴 ... | https://www.impacton.net/news/articleView.html?idxno=30300 |  |
| esg | 임팩트온 | 【위클리 ESG 행사】 10월 3주차 | https://www.impacton.net/news/articleView.html?idxno=30270 |  |
| esg | newsis.com | 지속가능성기준위 비상임위원에 김정일 대한상의 부회장 선임 | https://www.newsis.com/view/NISX20261015_0003827685 |  |
| esg | 한국경제 | 회계기준원, 지속가능성기준위 비상임위원에 김정일 대한상의 상근부회... | https://www.hankyung.com/article/202610153401r |  |
| esg | greened.kr | [ESG 리더스] 강성묵 하나증권 대표, 채용부터 탄소금융까지...'생활 속... | https://www.greened.kr/news/articleView.html?idxno=351052 |  |
| esg | 머니투데이 | 엔츠 "탄소관리, 엑셀·컨설팅에 의존할 이유 없어…AI가 대신한다" | https://www.mt.co.kr/policy/2026/10/07/2026100708361826345 |  |
| esg | news2day.co.kr | [ESG 인사이드 (97)] 지속가능성 공시, 기준이 아니라 경영을 보라(上) | https://www.news2day.co.kr/article/20261006500162 |  |
| esg | ESG경제 | GHG 프로토콜 AMI 찬성율 높아...개편 후 어떻게 활용되나 | https://www.esgeconomy.com/news/articleView.html?idxno=16927 |  |
| esg | hellot.net | [ESG 칼럼] 글로벌 기후 규제 장벽 도래와 생존을 위한 CBAM 검증 | https://www.hellot.net/news/article.html?no=115296 |  |
| esg | 한국경제 | KB증권, 온실가스 줄여야 자금 조달…지속가능채권 확대 | https://www.hankyung.com/article/2026100647061 |  |
| esg | hellot.net | [ESG 칼럼] 공시 의무화에 따른 공급망과 중견·중소기업 영향 | https://www.hellot.net/news/article.html?no=115294 |  |
| esg | ekn.kr | [사고] ‘대한민국 GX 기후경영 포럼’ 21일 개최 | https://www.ekn.kr/web/view.php?key=20261001026211014 |  |
| esg | wikitree.co.kr | 우리금융, 작년 '이 활동'으로 6조원 가치 창출했다 | https://www.wikitree.co.kr/articles/1163016 |  |
| esg | 임팩트온 | ISO 넷제로 국제표준 제동…Scope3·전환계획 기준 재검토 | https://www.impacton.net/news/articleView.html?idxno=30075 |  |
| esg | 일간NTN | 한국공인회계사회, '제26회 지속가능성인증포럼'성료 | http://www.intn.co.kr/news/articleView.html?idxno=2053666 |  |
| esg | tfmedia.co.kr | 회계사회, 지속가능성 인증기준은 ESG 핵심기반…ISSA 5000에 주목 | https://www.tfmedia.co.kr/news/article.html?no=207520 |  |
| esg | hansbiz.co.kr | [ESG 칼럼] 공시 비례성 vs 정보 유용성 | http://www.hansbiz.co.kr/news/articleView.html?idxno=868262 |  |
| esg | sejungilbo.com | 지속가능성 인증기준 3종 비교해보니…"ISSA 5000, 절차·책임 구체성 강... | https://www.sejungilbo.com/news/articleView.html?idxno=60306 |  |
| esg | 임팩트온 | ESG 홍보는 줄고 투자자 정보는 늘었다…그린허싱 시대의 공시전략 | https://www.impacton.net/news/articleView.html?idxno=20371 |  |
| esg | ESG경제 | 배출권거래제 지침으로 배출량 공시 기업, 보완할 점은? | https://www.esgeconomy.com/news/articleView.html?idxno=16821 |  |
| esg | 임팩트온 | 【기획】국내 대기업 99개사 기후 기회 공시 분석① - 효율·재생전력은... | https://www.impacton.net/news/articleView.html?idxno=30018 |  |
| esg | 임팩트온 | 【공시 모니터링】 하나금융, 기후위험 충당금 2050년 최대 3조원…전환... | http://www.impacton.net/news/articleView.html?idxno=20388 |  |
| esg | hansbiz.co.kr | [ESG 칼럼] 공시는 '양'이 아니라 '질'이다 | http://www.hansbiz.co.kr/news/articleView.html?idxno=866948 |  |
| esg | lec.co.kr | ISSA 5000의 이해와 타 인증기준 비교 분석...회계사회, '제26회 지속가능... | http://www.lec.co.kr/news/articleView.html?idxno=752712 |  |
| esg | 일간NTN | 한국공인회계사회, 21일 '제26회 지속가능성인증포럼' 개최 | http://www.intn.co.kr/news/articleView.html?idxno=2053340 |  |
| esg | tfmedia.co.kr | 회계사회, 21일 ‘지속가능성 인증기준 이해‧비교분석’ 웨비나 | https://www.tfmedia.co.kr/news/article.html?no=207234 |  |
| esg | kdfnews.com | DL, 그룹 ESG 성과 한데 모았다..."기후위험부터 공급망까지" | http://www.kdfnews.com/news/articleView.html?idxno=188037 |  |
| esg | hansbiz.co.kr | ESG행복경제연구소·한스경제, 평가 개편…객관성↑ | http://www.hansbiz.co.kr/news/articleView.html?idxno=865298 |  |
| esg | 조세일보 | 회계사회, 21일 ‘제26회 지속가능성인증포럼’ 개최 | http://www.joseilbo.com/news/news_read.php?uid=575690&class=10&grp= |  |
| esg | 임팩트온 | 【공시 모니터링】신한금융, 전환위험 34조원ㆍ물리적 위험 담보 11.7조... | http://www.impacton.net/news/articleView.html?idxno=20289 |  |
| esg | 매일경제 | 한국회계기준원 “지속가능성 공시 이행지원 강화”…2028년 법정공시 논... | https://www.mk.co.kr/article/12146451 |  |
| esg | 일간NTN | 한국회계기준원, '지속가능성 공시, 새로운 기준의 시대' 세미나 개최 | http://www.intn.co.kr/news/articleView.html?idxno=2053117 |  |
| esg | hansbiz.co.kr | [ESG 칼럼] 모험⸱인내자본 넘어 촉매자본 돼야 | http://www.hansbiz.co.kr/news/articleView.html?idxno=862750 |  |
| esg | 임팩트온 | 【ESG 채용】금호타이어, 대신경제연구소, 포스코경영연구원, 임팩트온 | http://www.impacton.net/news/articleView.html?idxno=20244 |  |
| esg | dnews.co.kr | [법률라운지] 자연 공시는 의무인가 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202609061002123190791 |  |
| esg | hellot.net | [ESG 칼럼] 2028년부터 본격화되는 지속가능성 공시제도, 지금 무엇을 준... | https://www.hellot.net/news/article.html?no=114798 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 곽병진 회계기준원장 “지속가능성 관련 한국 상황…국제... | https://www.tfmedia.co.kr/news/article.html?no=206983 |  |
| esg | etoday.co.kr | 지속가능성 공시 기준 마련됐지만…기업 현장은 ‘데이터 신뢰성’ 숙제 | https://www.etoday.co.kr/news/view/2621715 |  |
| esg | 서울경제 | “ESG 기준에 韓 특수성 반영해야” | https://www.sedaily.com/article/20086981?ref=naver |  |
| esg | smartbizn.com | SK증권, 본업 회복에 ESG 수익원 확대···실적 개선세 이어갈까 | https://www.smartbizn.com/news/articleView.html?idxno=152996 |  |
| esg | insightkorea.co.kr | 전우종·정준호 SK증권 대표, ESG 수익사업 키운다...탄소금융 확대 | https://www.insightkorea.co.kr/news/articleView.html?idxno=253742 |  |
| esg | s-journal.co.kr | 신한금융, 창립 25주년 맞아 "신뢰가 미래 경쟁력" 강조 | https://www.s-journal.co.kr/news/articleView.html?idxno=43406 |  |
| esg | economytalk.kr | [ESG 경영 분석] '비재무 데이터 공시 확대' KB증권…"자연자본·인권·거... | http://www.economytalk.kr/news/articleView.html?idxno=423863 |  |
| esg | 임팩트온 | 【공시 모니터링】 KB금융, 기후위험에 묶인 자본 7.8조 계산…남은 과... | http://www.impacton.net/news/articleView.html?idxno=20157 |  |
| esg | segye.com | 뜨거워지는 바다, 늘어나는 재해… 기후변화는 이미 ‘재무’의 문제다... | https://www.segye.com/newsView/20260830510403?OutUrl=naver |  |
| esg | ESG경제 | [해외브리핑] EU, 회원국 기후적응 계획 수립 의무화 추진 | https://www.esgeconomy.com/news/articleView.html?idxno=17135 |  |
| esg | ESG경제 | [해외브리핑] 중국, 내년 탄소배출권 거래제에 화학·석유화학 추가 | https://www.esgeconomy.com/news/articleView.html?idxno=17099 |  |
| esg | 한국경제 | SK하이닉스, 솔리다임 美 상장 철회 [ESG 뉴스 5] | https://magazine.hankyung.com/business/article/202610230292b |  |
| esg | 조세일보 | 세계회계사대회, 120년 만에 첫 서울 개최…글로벌 금융 수장 총출동 | http://www.joseilbo.com/news/news_read.php?uid=577781&class=10&grp= |  |
| esg | 한국세정신문 | 수출중소기업 10곳 중 6곳 국제녹색규범 준비 안 돼 | https://www.taxtimes.co.kr/news/article.html?no=277375 |  |
| esg | sejungilbo.com | '회계 올림픽' 세계회계사대회, 오는 11월 서울서 최초 개최 | https://www.sejungilbo.com/news/articleView.html?idxno=60710 |  |
| esg | 한국세정신문 | '회계 올림픽' 세계회계사대회, 내달 17일 서울에서 최초 개최 | https://www.taxtimes.co.kr/news/article.html?no=277372 |  |
| esg | 일간NTN | 2026 세계회계사대회(WCOA) 내달 17일부터 3일간 개최 | http://www.intn.co.kr/news/articleView.html?idxno=2054165 |  |
| esg | ESG경제 | [해외브리핑] 美인허가 개편안 논란…"재생E 늘리려다 환경보호 약화" | https://www.esgeconomy.com/news/articleView.html?idxno=16960 |  |
| esg | hansbiz.co.kr | [ESG 칼럼] 재무성과와 ESG, 기업가치를 키우는 연리지 | http://www.hansbiz.co.kr/news/articleView.html?idxno=871660 |  |
| esg | hellot.net | [ESG 칼럼] 2028년부터 본격화되는 지속가능성 공시제도 지금 무엇을 준... | https://www.hellot.net/news/article.html?no=115297 |  |
| esg | kmaeil.com | [문인찬의 新戰略論] New Strategy Paradigm #55 | https://www.kmaeil.com/news/articleView.html?idxno=653535 |  |
| esg | hansbiz.co.kr | [ESG 칼럼] 타자는 '선구안'으로 평가 받는다 | http://www.hansbiz.co.kr/news/articleView.html?idxno=870135 |  |
| esg | biztribune.co.kr | 동아오츠카, 낙동강생물자원관과 광려천 담수생물다양성 모니터링 | http://www.biztribune.co.kr/news/articleView.html?idxno=360056 |  |
| esg | 한국경제 | 영국, 기후공시 의무화 후퇴 [ESG 뉴스 5] | https://magazine.hankyung.com/business/article/202610029358b |  |
| esg | ESG경제 | 국회 'ESG기본법'이 바꿀 기업·금융시장...EU식 통합 규제체계 갖춘다 | https://www.esgeconomy.com/news/articleView.html?idxno=16899 |  |
| esg | etoday.co.kr | [ESGX 이슈 5] 영국, 상장사 기후공시 의무화 철회…‘준수 또는 설명’... | https://www.etoday.co.kr/news/view/2631392 |  |
| esg | economist.co.kr | i-ESG, 글로벌 지속가능성 기관과 협력 확대…신흥국 ESG 데이터 격차 해... | https://economist.co.kr/article/view/ecn202609300053 |  |
| esg | etoday.co.kr | [ESGX 용어 5] EmpCo·eSAF·ETS2·다중 보고체계·전환계획 | https://www.etoday.co.kr/news/view/2630931 |  |
| esg | khan.co.kr | AI 열차의 질주, 자본도 ‘안전’을 책임져야 한다[류영재의 제3의 자본... | https://www.khan.co.kr/article/202609292050005 |  |
| esg | ESG경제 | 美 기업 ESG 데이터 외부검증 75%…4년 새 21%p 증가 | https://www.esgeconomy.com/news/articleView.html?idxno=16849 |  |
| esg | 한국경제 | 미국 빠진 기후외교…중국, 차기 주도권 잡는다 [ESG 뉴스 5] | https://magazine.hankyung.com/business/article/202609288421b |  |
| esg | 임팩트온 | EU, 개정 ESRS 디지털 공시체계 마련…EFRAG XBRL 초안 공개 | http://www.impacton.net/news/articleView.html?idxno=20399 |  |
| esg | ezyeconomy.com | [이지 칼럼] Evolving ESG, 지속가능성 전환(SX)으로 | https://www.ezyeconomy.com/news/articleView.html?idxno=240029 |  |
| esg | asiatime.co.kr | [기후위기㊦] “대응 안하면 배임”… 기후 소송 직면한 기업들 | https://www.asiatime.co.kr/article/20260920500049 |  |
| esg | kbmaeil.com | 영화 ‘오디세이’로 읽는 ESG…‘크세니아의 붕괴와 자본의 역습’ | https://www.kbmaeil.com/article/20260915500434 |  |
| esg | 한국세정신문 | 공인회계사회, 지속가능성인증포럼…'ISSA 5000 이해' | https://www.taxtimes.co.kr/news/article.html?no=276856 |  |
| esg | sejungilbo.com | 한공회, 21일 '제26회 지속가능성인증포럼' 개최 | https://www.sejungilbo.com/news/articleView.html?idxno=60104 |  |
| esg | 이데일리 | 한국공인회계사회, 오는 21일 ‘제26회 지속가능성인증포럼’ 개최 | https://www.edaily.co.kr/News/Read?newsId=03030726645580448&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| esg | 한국경제 | 美, 발전소 탄소규제 전면 폐기 [ESG 뉴스 5] | https://magazine.hankyung.com/business/article/202609154758b |  |
| esg | 이데일리 | "회계사 합격 청년 넷 중 셋집에서 놀았다… 선발인원 200명 줄이자"[만... | https://www.edaily.co.kr/News/Read?newsId=05461206645580120&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| esg | economychosun.com | [국가공헌대상] 심사평 \| ESG 경영과 글로벌 리스크 관리, 함께 추구해야 | https://economychosun.com/site/data/html_dir/2026/09/11/2026091100034.html |  |
| esg | economychosun.com | [국가공헌대상] ‘2026년 국가공헌대상’ 45대 기업·기관 선정 \| AI 역량... | https://economychosun.com/site/data/html_dir/2026/09/11/2026091100033.html |  |
| esg | ESG경제 | "지속가능성 공시, 기후 넘어 인권·환경으로…공공투자에도 원칙 반영... | https://www.esgeconomy.com/news/articleView.html?idxno=16722 |  |
| esg | gasnews.com | [시론] 국제적 ESG 파고에 충실히 대비해야 | https://www.gasnews.com/news/articleView.html?idxno=126726 |  |
| esg | naeil.com | [기고] AX와 SX, 한국 기업의 트윈 트랜스포메이션 | https://www.naeil.com/news/read/601630?ref=naver |  |
| esg | 한국경제 | 포스코 창사 58년 만에 첫 부분파업 [ESG 뉴스 5] | https://magazine.hankyung.com/business/article/202609092930b |  |
| esg | news2day.co.kr | [ESG 인사이드 (95)] ESG 기준, 자본시장이 정리한다 | https://www.news2day.co.kr/article/20260908500111 |  |
| esg | 머니투데이 | 공시 쏟아지는데 중요 숫자는 숨바꼭질…한국도 '공시 다이어트' 나설 ... | https://www.mt.co.kr/stock/2026/09/08/2026090722215967112 |  |
| esg | 머니투데이 | 일본은 '공시 다이어트' 시작…"중복 덜고 투자정보 연결" | https://www.mt.co.kr/stock/2026/09/08/2026090711393373672 |  |
| esg | 머니투데이 | 영업익 1.3조 vs 3010억 적자...같은 회사 다른 공시, 헷갈리는 개미들 | https://www.mt.co.kr/stock/2026/09/08/2026090711323181310 |  |
| esg | 머니투데이 | [단독] 수조원 미래손실 추정치, 법정공시 사업보고서엔 없다 | https://www.mt.co.kr/stock/2026/09/08/2026090710491724209 |  |
| esg | ESG경제 | 미국 공화당 반 기후행동 공세 회계법인 겨냥 | https://www.esgeconomy.com/news/articleView.html?idxno=16608 |  |
| esg | ESG경제 | "글로벌 기후표준 5대 기관, 의사결정 투명성·책임성 곳곳에 빈틈" | https://www.esgeconomy.com/news/articleView.html?idxno=16599 |  |
| esg | 임팩트온 | 9월 1주차 해외 ESG 핫클립 | http://www.impacton.net/news/articleView.html?idxno=20190 |  |
| esg | etoday.co.kr | [ESGX 이슈 5] 기후부 내년 예산 25.7조원…美는 4대 회계법인 기후공시... | https://www.etoday.co.kr/news/view/2620948 |  |
| esg | etoday.co.kr | [ESGX 용어 5] TNFD·LEAP 접근법·스코프 3·SLB·기후 슈퍼펀드 | https://www.etoday.co.kr/news/view/2621099 |  |
| esg | hellot.net | 미오테크·CCX 그린파이낸스 합병…아시아 ESG·공급망 AI 사업 확대 | https://www.hellot.net/news/article.html?no=114690 |  |
| esg | e2news.com | '자연자본공시 안내서 및 LEAP 실무해설서' 공개 | http://www.e2news.com/news/articleView.html?idxno=333767 |  |
| esg | ESG경제 | 국내기업 자연자본 공시, 인식 높아졌지만 TNFD 이행은 '제자리' | https://www.esgeconomy.com/news/articleView.html?idxno=16554 |  |
| esg | ttlnews.com | 글로벌 1000개 기관 제치고 '99점' SK증권, LACP 플래티넘 석권 | http://www.ttlnews.com/news/articleView.html?idxno=3138719 |  |
| esg | etoday.co.kr | [ESGX 이슈 5] 기업 자연자본공시 돕는다…기후부, 실무 안내서 2종 공개 | https://www.etoday.co.kr/news/view/2619908 |  |
| esg | bizwork.co.kr | 기후부, 기업 '자연자본공시' 대응 지원…리프 실무 해설서 공개 | https://www.bizwork.co.kr/news/articleView.html?idxno=418696 |  |
| esg | todayenergy.kr | 기후부, 국내 기업 자연자본공시 준비·작성 지원 | https://www.todayenergy.kr/news/articleView.html?idxno=302188 |  |
| esg | 임팩트온 | 【데일리 ESG 정책 브리핑】자연자본공시 지원·한미 에너지안보 협력 | http://www.impacton.net/news/articleView.html?idxno=20144 |  |
| esg | ESG경제 | [정책브리핑] 기후부, '자연자본공시 안내서 및 실무해설서' 공개 | https://www.esgeconomy.com/news/articleView.html?idxno=16538 |  |
| esg | lak.co.kr | 기후부, ‘자연자본공시 안내서’·‘실무해설서’ 2종 공개 | http://www.lak.co.kr/news/boardview.php?id=23800 |  |
| esg | ikld.kr | 기후부, 국내 기업 자연자본공시 지원 나서 | http://www.ikld.kr/news/articleView.html?idxno=339766 |  |
| esg | viva100.com | 기후부, 자연자본공시 실무 지원 자료 ‘2종’ 배포 | https://www.viva100.com/article/20260830500553 |  |
| esg | womentimes.co.kr | 기업 '자연자본'도 공시해야, 기후부 국제기준 실무지침 마련 | https://www.womentimes.co.kr/news/articleView.html?idxno=105754 |  |
| esg | metroseoul.co.kr | 기업 자연자본공시, 준비부터 작성까지 돕는다… 기후부, 실무 해설서 ... | http://www.metroseoul.co.kr/article/20260830500075 |  |
| esg | ajunews.com | 자연자본공시 준비부터 보고서 작성까지…기후부, 실무서 2종 공개 | https://www.ajunews.com/view/20260830104838542 |  |
| esg | etnews.com | 기업 공시, 탄소 넘어 생물다양성까지…정부 '자연자본공시' 지원 | https://www.etnews.com/20260828000073 |  |
| esg | newsworks.co.kr | 한화에어로, 적자 전환 '어닝 쇼크'…인도일정 순연 및 일회성 비용 반... | https://www.newsworks.co.kr/news/articleView.html?idxno=901330 |  |
| esg | news1.kr | 두산밥캣, 3분기 영업익 1674억원…전년比 25.3% 증가 | https://www.news1.kr/industry/general-industry/6336818 |  |
| esg | sateconomy.co.kr | 삼성전자, 실적 발표일 4.13% 하락…2거래일 수익률은 4.5% 상승 | https://sateconomy.co.kr/news/view/1065599051932236 |  |
| esg | 4th.kr | 5대 금융 3분기 누적 순익 20조 육박…KB금융 1위·리딩뱅크는 신한 | http://www.4th.kr/news/articleView.html?idxno=2120722 |  |
| esg | hansbiz.co.kr | KB금융, 2700억 신종자본증권 발행…BIS 비율 제고 | http://www.hansbiz.co.kr/news/articleView.html?idxno=877819 |  |
| esg | newsprime.co.kr | "KT 독점 끝나자 4G 가입률 15배"…해외 통신업계, 르완다 사업 비판 | http://www.newsprime.co.kr/news/article.html?no=752965 |  |
| esg | 조세일보 | 5대 금융지주, 순익 20조원 육박…‘역대급 실적’에 주주환원 경쟁 | http://www.joseilbo.com/news/news_read.php?uid=578476&class=18&grp= |  |
| esg | ekn.kr | “이러니 SK하이닉스로 가지”…투자자들, 삼성전자에 실망한 이유는 [... | https://www.ekn.kr/web/view.php?key=20261029029502817 |  |
| esg | weeklytoday.com | [위클리오늘] 「제35회 이천시 후계농업경영인·여성농업인 한마음대회... | http://www.weeklytoday.com/news/articleView.html?idxno=800242 |  |
| esg | koit.co.kr | UNIST, 금융 AI 요약 왜곡 잡는다…투자 판단 변화율 19.5%로 낮춰 | https://www.koit.co.kr/news/articleView.html?idxno=209718 |  |
| esg | 서울경제 | “사실 맞아도 맥락 빠지면 오판”…UNIST, 금융 AI 신뢰도 높인 압축 기... | https://www.sedaily.com/article/20107785?ref=naver |  |
| esg | sateconomy.co.kr | 호텔신라, 실적 예상 웃돌아도 한투 목표가 한 달 새 23% 하향 | https://sateconomy.co.kr/news/view/1065590239612284 |  |
| esg | pinpointnews.co.kr | 삼성전자 5% 넘게 급락하자 코스피도 흔들…반도체 호황의 역설 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=499709 |  |
| esg | newstomato.com | (유통 공룡 심층진단)실적 반등한 신세계…'수익성 회복·차입금 관리' ... | http://www.newstomato.com/ReadNews.aspx?no=1318222&inflow=N |  |
| esg | newsworker.co.kr | [IB탈탈털기] 교보증권, 3000억 수혈에도 종투사 '먼 길'…2년 뒤 찾아올... | https://www.newsworker.co.kr/news/articleView.html?idxno=511265 |  |
| esg | donga.com | “그린워싱, 법·공시·소통 함께 풀어야”… 국제ESG협회 30일 부산서 ... | https://www.donga.com/news/Economy/article/all/20261029/134931648/1 |  |
| esg | newsis.com | "금융 AI 판단 왜곡 줄인다"…UNIST 국제학회 논문 4편 발표 | https://www.newsis.com/view/NISX20261029_0003846477 |  |
| esg | mediawatch.kr | 삼성SDI, 3Q 영업益 4078억… 전년 比 흑자 전환 ‘깜짝 실적’ | https://www.mediawatch.kr/news/article.html?no=261539 |  |
| esg | ekn.kr | SK이노베이션, 3분기 정유·윤활기유 ‘쌍끌이’…엔무브發 고수익 지속... | https://www.ekn.kr/web/view.php?key=20261029025402772 |  |
| esg | ekn.kr | “107조 벌었는데 어닝 미스?”…삼성전자 주가 6% 급락한 이유 [이슈+] | https://www.ekn.kr/web/view.php?key=20261029020572742 |  |
| esg | 임팩트온 | 【위클리 ESG 행사】 11월 1주차 | https://www.impacton.net/news/articleView.html?idxno=30460 |  |
| esg | ESG경제 | 삼성전자, 3분기 영업익 반도체만 106조원…빅테크 최초 100조 돌파 | https://www.esgeconomy.com/news/articleView.html?idxno=17168 |  |
| esg | etoday.co.kr | [ESGX 이슈 5] EU 공시 완화 논란부터 AI 데이터센터의 고용 갈등까지 | https://www.etoday.co.kr/news/view/2641631 |  |
| esg | kukinews.com | 순천향대 회계학과, 인공지능(AI) 시대 미래 경쟁력 모색 | https://www.kukinews.com/article/view/kuk202610290051 |  |
| esg | 서울경제 | 삼전, 30조 배당에도 2% 약세…코스피도 하락 전환 [마켓시그널] | https://www.sedaily.com/article/20107598?ref=naver |  |
| esg | fetv.co.kr | [밸류업-롯데지주] PBR 회복 목표 '백 투 더 퓨쳐'…해외사업 속도전 | https://www.fetv.co.kr/news/articleView.html?idxno=312618 |  |
| esg | ppss.kr | SK하이닉스, 3분기 영업이익 83조원 사상 최대...증권가 '메모리 호황 지... | https://www.ppss.kr/news/articleView.html?idxno=317915 |  |
| esg | pinpointnews.co.kr | 배당 확대·자사주 소각 내걸었지만…밸류업 종목 옥석 가리기 '촉각' | https://www.pinpointnews.co.kr/news/articleView.html?idxno=499583 |  |
| esg | raonnews.com | [칼럼] 사회공헌 실적 2조원 넘긴 은행권…’소셜워싱' 지적받은 까닭 | https://www.raonnews.com/news/article.html?no=62304 |  |
| esg | 한국세정신문 | 한국공인회계사회, 내달 5일 제27회 지속가능성인증포럼 개최 | https://www.taxtimes.co.kr/news/article.html?no=277520 |  |
| esg | ESG경제 | [해외브리핑] 트럼프, 석유·가스 업계 메탄 규제 완화안 공식 제안 | https://www.esgeconomy.com/news/articleView.html?idxno=17163 |  |
| esg | 서울경제 | 한공회, ‘지속가능성인증포럼’ 웨비나 연다 [시그널] | https://www.sedaily.com/article/20107505?ref=naver |  |
| esg | newspim.com | 한국공인회계사회, 11월 5일 '제27회 지속가능성인증포럼' 진행 | https://www.newspim.com/news/view/20261029000117 |  |
| esg | fntimes.com | [KFT 모닝 브리프] 2026.10.29 — 오늘 꼭 알아야 할 국내외 경제뉴스 | https://www.fntimes.com/html/view.php?ud=202610290707592832141825007d_18 |  |
| esg | cbci.co.kr | [밸류업 승부수] "주가 저평가됐다" SK하이닉스, 배당·자사주 소각에 연... | https://www.cbci.co.kr/news/articleView.html?idxno=620290 |  |
| esg | e2news.com | "전력거래소, 직접 PPA 거래 확대...계약부터 증빙까지 디지털화" | http://www.e2news.com/news/articleView.html?idxno=335539 |  |
| esg | kdpress.co.kr | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로... | https://www.kdpress.co.kr/news/articleView.html?idxno=209583 |  |
| esg | newscj.com | 순천향대 회계학과, 홈커밍 대회… AI 시대 미래 경쟁력 모색 | https://www.newscj.com/news/articleView.html?idxno=3444027 |  |
| esg | ngonews.kr | "복잡하고 어려운 서류 속에서 길을 찾아 부동산 권리 관계를 명확하게... | https://www.ngonews.kr/news/articleView.html?idxno=241771 |  |
| esg | wikitree.co.kr | "대학 전문성에 주민 참여 더했다" 서정대, 주민 주도형 마을 안전모델... | https://www.wikitree.co.kr/articles/1169947 |  |
| esg | iminju.net | 3분기도 '실적 잔치'…삼전·하닉, 투자 전략 어디로 | http://www.iminju.net/news/articleView.html?idxno=171567 |  |
| esg | businesspost.co.kr | [인터뷰] 동아제약 CDMO 자회사 비티젠 대표 이현민 "품질 관리 자부심 ... | https://www.businesspost.co.kr/BP?command=article_view&num=450532 |  |
| esg | zdnet.co.kr | "재무 안정성 합격점에 기술 경쟁력 확보까지…"네이버 AI팩토리 사업 구... | https://zdnet.co.kr/view/?no=20261028154636 |  |
| esg | ESG경제 | SK하이닉스 3분기 영업익 83조 역대최대...주주환원 총 100조원 | https://www.esgeconomy.com/news/articleView.html?idxno=17158 |  |
| esg | lkp.news | 다올투자증권, 고배당 시대의 경쟁력... 배당성향 41%의 의미 | http://www.lkp.news/news/articleView.html?idxno=85498 |  |
| esg | ccdn.co.kr | 순천향대 회계학과, AI 시대 회계 전문가의 미래 경쟁력 모색 | https://www.ccdn.co.kr/news/articleView.html?idxno=1107603 |  |
| esg | job-post.co.kr | 지투지바이오 3만6750원으로 6.13% 하락…약효지속 플랫폼 개발 점검 | https://www.job-post.co.kr/news/articleView.html?idxno=235071 |  |
| esg | ezyeconomy.com | [EZ 핫이슈] 영업익 83조 vs 주가 반토막…SK하이닉스, '100조 환원'으로... | https://www.ezyeconomy.com/news/articleView.html?idxno=241288 |  |
| esg | 매일경제 | SK하이닉스, 100조원 규모 주주환원…주당 2만원 현금배당 | http://mbn.mk.co.kr/pages/news/newsView.php?category=mbn00003&news_seq_no=5227560 |  |
| esg | newstown.co.kr | SK하이닉스, 역대 최대 3분기 매출 104.6조 원...영업이익 83.3조 원 | http://www.newstown.co.kr/news/articleView.html?idxno=720019 |  |
| esg | newslock.co.kr | [뉴스락 특별기획｜금융권 연말 인사 진단 ① JB금융그룹] 최대 실적 뒤... | http://www.newslock.co.kr/news/articleView.html?idxno=138769 |  |
| esg | opinionnews.co.kr | 하이닉스 호실적에 웃는 코스피, 다음은 'MS·아마존'...AI 수익성 입증... | http://www.opinionnews.co.kr/news/articleView.html?idxno=146306 |  |
| esg | 임팩트온 | 싱가포르, 해외 REC 인정 기준 강화…전력 공급 없으면 재생전력 실적 ... | https://www.impacton.net/news/articleView.html?idxno=30438 |  |
| esg | ohmynews.com | 8년간 250개 기업 문 두드린 국민연금... "한국 주총 현실은" | https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003277671&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news |  |
| esg | kookje.co.kr | “주가 저평가됐다” SK하이닉스 주당 2만 원 현금 배당…올해 100조 푼... | http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20261028.99099008186 |  |
| esg | jeonmae.co.kr | SK하이닉스, 100조원 주주환원 승부수…주가 반등 이끌까 | https://www.jeonmae.co.kr/news/articleView.html?idxno=1306052 |  |
| esg | the-today.com | 신한투자증권, 호실적 뒤 가려진 불안…운용수익 급감·내부통제 역량 ... | https://www.the-today.com/news/articleView.html?idxno=92559 |  |
| esg | investchosun.com | [Invest]SK하이닉스의 주주 달래기…"3년치 메모리 완판, 주주환원 100조... | https://www.investchosun.com/site/data/html_dir/2026/10/28/2026102880072.html |  |
| esg | yna.co.kr | SK하이닉스, 주당 2만원 현금배당…연간 총 100조원 푼다(종합) | https://www.yna.co.kr/view/AKR20261028036251003?input=1195m |  |
| esg | view.asiae.co.kr | 네이버, 엔비디아·브룩필드와 'AI 팩토리' 3자 연합 승부수(종합) | https://view.asiae.co.kr/article/2026102810070496357 |  |
| esg | metroseoul.co.kr | 네이버 해피빈, 기업 사회공헌 연결 확대…파트너스데이 개최 | http://www.metroseoul.co.kr/article/20261028500147 |  |
| esg | dnews.co.kr | [테크 NOW] 네이버ㆍ카카오엔터ㆍNHN페이코 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610280920074320453 |  |
| esg | topstarnews.net | SK하이닉스 영업이익 83조 사상 최대…주당 2만원 배당·100조 주주환원 | https://www.topstarnews.net/news/articleView.html?idxno=16260210 |  |
| esg | moneystorm.kr | SK하이닉스, 3분기 영업이익 83조 역대최대… 100조 풀어 주주와 이익 공... | https://www.moneystorm.kr/news/articleView.html?idxno=7734 |  |
| esg | ESG경제 | [해외브리핑] WMO "온실가스 농도 사상 최고…산업화前 153%달해" | https://www.esgeconomy.com/news/articleView.html?idxno=17150 |  |
| esg | 이데일리 | 네이버 해피빈 "기업 사회공헌도 ‘연결’이 핵심…목적 맞는 파트너 찾... | https://www.edaily.co.kr/News/Read?newsId=03076646645617512&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| esg | view.asiae.co.kr | 지씨셀 기술 이전 아티바, NK 치료제 개발 중단…2명 사망·직원 94% 감원 | https://view.asiae.co.kr/article/2026102809041556996 |  |
| esg | economist.co.kr | i-ESG, 스페인 NEALIS와 MOU…유럽 ESG 사업 확대 | https://economist.co.kr/article/view/ecn202610270037 |  |
| esg | kmaeil.com | [이준호의 N잡러칼럼] 코스닥 상장전략(2), 코스닥의 문을 두드리는 중... | https://www.kmaeil.com/news/articleView.html?idxno=655642 |  |
| esg | ajunews.com | [인문자의 2027년 투자와 인생 이야기 \| 인간·문화·자연] 2027년, 돈은 ... | https://www.ajunews.com/view/20261028083254919 |  |
| esg | khan.co.kr | SK하이닉스 3분기 영업이익 83조원 돌파…60조원 규모 추가 주주환원 | https://www.khan.co.kr/article/202610280838001 |  |
| esg | smartbizn.com | "고점 대비 55% 하락" SK하이닉스, 영업익 77조 전망에도 개미들 '냉담' | https://www.smartbizn.com/news/articleView.html?idxno=157719 |  |
| esg | greenpostkorea.co.kr | 삼전닉스, 주주환원 210조원 전망··· 100주 보유 시 배당금 얼마? | https://www.greenpostkorea.co.kr/news/articleView.html?idxno=307843 |  |
| esg | news1.kr | SK하이닉스, 오늘 사상 최대 3Q 실적 발표…주주환원 방안도 '주목' | https://www.news1.kr/industry/general-industry/6333748 |  |
| esg | dailymedi.com | 지투지바이오 UBT 계약…"기술이전 아닌 검증 단계" | https://www.dailymedi.com/news/news_view.php?wr_id=941948 |  |
| esg | vegannews.co.kr | 한은 “AI 자금조달 외부 의존 커져…금융 취약성 누적” | https://www.vegannews.co.kr/news/article.html?no=397623 |  |
| esg | metroseoul.co.kr | 순천향대 회계학과, AI·ESG 시대 회계 전문가 역할 모색 | http://www.metroseoul.co.kr/article/20261027500681 |  |
| esg | ebn.co.kr | 네이버, 브룩필드와 12조원 AI 인프라 계약…엔비디아 투자 초읽기 | https://www.ebn.co.kr/news/articleView.html?idxno=1729393 |  |
| esg | ujeil.com | 기후변화 공시에서 녹색대전환까지, 울산의 선택 | http://www.ujeil.com/news/articleView.html?idxno=394186 |  |
| esg | newsquest.co.kr | '76조 잔치' 앞둔 SK하이닉스…솔리다임에 뿔난 주주 달랠까 | https://www.newsquest.co.kr/news/articleView.html?idxno=303531 |  |
| esg | kizmom.com | 네이버·엔비디아 AI 팩토리 본격화…브룩필드와 12조원 계약 | https://www.kizmom.com/news/articleView.html?idxno=113577 |  |
| esg | platum.kr | 네이버, 브룩필드와 90억 달러 인프라 계약… 엔비디아 3대 주주 등극 눈... | https://platum.kr/archives/297136 |  |
| esg | yna.co.kr | 네이버, 브룩필드와 12조원 AI인프라 계약…AI팩토리 본격 공략 | https://www.yna.co.kr/view/AKR20261027150700017?input=1195m |  |
| esg | seoulfn.com | 코스피, 앤트로픽발 AI 훈풍에 5600선 회복···삼전·닉스 4~5% 급등 | https://www.seoulfn.com/news/articleView.html?idxno=641121 |  |
| esg | mediapen.com | K-해양방산, 미 함정 시장 공략…현지 생산기반 확보에 사활 | https://www.mediapen.com/news/view/1133550 |  |
| esg | m-i.kr | 불 꺼지는 홈플러스…'청산' 시나리오 현실로 | https://www.m-i.kr/news/articleView.html?idxno=2011999 |  |
| esg | 1conomynews.co.kr | 명노현 LS 부회장 "협력사와 동반성장"…전략적 파트너십 강화 | https://www.1conomynews.co.kr/news/articleView.html?idxno=51037 |  |
| esg | consumernews.co.kr | '2026 LS 협력사 CEO 포럼' 성료...명노현 부회장, "AI 혁신은 도전의 기... | http://www.consumernews.co.kr/news/articleView.html?idxno=767085 |  |
| esg | digitaltoday.co.kr | 세종텔레콤, ESG 평가 2년 연속 1등급...상위 5.9% 기록 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=710903 |  |
| esg | dealsite.co.kr | [재계는 지금] LS그룹, 제5회 협력사 CEO 포럼 성료…소통·협력으로 미... | https://dealsite.co.kr/articles/171610 |  |
| esg | newsworks.co.kr | [IT라운지] 삼성SDS '실적'·세종T 'ESG 1위'·장애인방송 의무지정·MS '... | https://www.newsworks.co.kr/news/articleView.html?idxno=901214 |  |
| esg | 파이낸셜뉴스 | 에어버스 공급망 여는 방사청, 100개 국내 기업 '유럽 항공우주 영토' 개... | https://www.fnnews.com/news/202610290807360651 |  |
| esg | zdnet.co.kr | 세종텔레콤, ESG 평가 2년 연속 최고등급 획득 | https://zdnet.co.kr/view/?no=20261029091716 |  |
| esg | viva100.com | [통신업계 소식] KT, ‘보이스봇’·‘AI 상담 어시스트’로 고객 경험 ... | https://www.viva100.com/article/20261029500224 |  |
| esg | 이데일리 | 세종텔레콤, ESG 2년 연속 1등급…사회·지배구조 모두 최고등급 | https://www.edaily.co.kr/News/Read?newsId=03375126645617840&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| esg | ferrotimes.com | 페로타임즈 손바닥뉴스 10월29일(목) | http://www.ferrotimes.com/news/articleView.html?idxno=51170 |  |
| esg | cstimes.com | 코트라, 세계 공급망 진입 해법 제시 및 영국 명문대 협력·인재 유치 병... | https://www.cstimes.com/news/articleView.html?idxno=725696 |  |
| esg | ccnnews.co.kr | ㈜레이크머티리얼즈, 산업부 '소부장 으뜸기업' 선정 | http://www.ccnnews.co.kr/news/articleView.html?idxno=416923 |  |
| esg | newspim.com | 레드백 이어 '오스탈'까지… 한·호주 방산, 땅에서 바다로 판 키운다 | https://www.newspim.com/news/view/20261028001623 |  |
| esg | digitaltoday.co.kr | 맥북이 바꾼 노트북 20년…PC 업계가 따라한 애플의 선택 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=710636 |  |
| esg | namdonews.com | "호남반도체, 경제민주화·지방자치 획기적 전환 계기 삼아야" | https://www.namdonews.com/news/articleView.html?idxno=927569 |  |
| esg | dnews.co.kr | 이현민 비티젠 대표 “2028년 DS·DP 증설…대형 CDMO와 겹치지 않는 중... | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610281514029480602 |  |
| esg | dt.co.kr | 한화, 美 군함 건조 거점 구축 속도…필리조선소 재편·오스탈 인수 ‘... | https://www.dt.co.kr/article/12091856?ref=naver |  |
| esg | newsway.co.kr | 방사성의약품 '기술' 넘어 '공급망' 경쟁…K바이오의 숙제는[BIX 2026] | https://www.newsway.co.kr/news/view?ud=2026102813083794094 |  |
| esg | yakup.com | “방사성의약품, 후보물질 좋아도 공급망 없으면 사업화 끝” 글로벌 투... | https://www.yakup.com/news/index.html?mode=view&cat=12&nid=334413 |  |
| esg | etoday.co.kr | KPC-코트라, '에코바디스' 세미나 개최⋯"ESG 대응이 수출 경쟁력” | https://www.etoday.co.kr/news/view/2641050 |  |
| esg | newsis.com | 中 BYD, UNGC 가입…"작년 친환경차 460만대 판매, 나무 7억그루 효과" | https://www.newsis.com/view/NISX20261028_0003844393 |  |
| esg | bloter.net | 한화, 오스탈USA 인수계약 협상 본격화 '정식 제안' 임박 | https://www.bloter.net/news/articleView.html?idxno=676906 |  |
| esg | megaeconomy.co.kr | 신한은행, ‘한국형 녹색채권’ 1500억원 발행…태양광 제조 경쟁력 수... | https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065572046799773 |  |
| esg | globale.co.kr | 11월 기업경기 BSI 98.6···반도체 급랭·서비스업 온기 '양극화' | https://www.globale.co.kr/news/articleView.html?idxno=41274 |  |
| esg | ferrotimes.com | 페로타임즈 손바닥뉴스 10월28일(수) | http://www.ferrotimes.com/news/articleView.html?idxno=51154 |  |
| esg | labortoday.co.kr | 공급망 실사 한국은 리스크 취급, 노동자 배제 | https://www.labortoday.co.kr/news/articleView.html?idxno=237427 |  |
| esg | voakorea.com | 미군 주요 기지 ‘90일 자립 계획’ 추진 | https://www.voakorea.com/a/8215816.html |  |
| esg | medipana.com | [종합] 약가 인하부터 미프진까지…국감이 짚은 제약 정책 | https://www.medipana.com/news/articleView.html?idxno=420235 |  |
| esg | it.chosun.com | '중국의 로레알'은 탄생할까 ﻿[박지민의 중국과 미래] | https://it.chosun.com/news/articleView.html?idxno=2023092172821 |  |
| esg | g-enews.com | 거품론 뚫고 번 돈만 139조…월가가 약체 기업부터 쳐내는 까닭 | https://www.g-enews.com/view.php?ud=202610271721325018fbbec65dfb_1 |  |
| esg | 매일경제 | "AI 시대 가장 명확한 투자 기회, 인프라에 있죠" | https://www.mk.co.kr/article/12187388 |  |
| esg | kookbang.dema.mil.kr | [첨단 기술이 바꾸는 전장 지형] ③첨단강군의 보루 ‘부품국산화’ | https://kookbang.dema.mil.kr/newsWeb/20261028/1/ATCE_CTGR_0020060011/view.do |  |
| esg | 임팩트온 | "PPWR, 이제는 설계의 시간"…오정화 에코네트워크 센터장(전 아모레퍼... | https://www.impacton.net/news/articleView.html?idxno=30425 |  |
| esg | sisaon.co.kr | 광산 없는 자원강국의 조건…LS MnM 90년이 보여준 '제련의 가치' [옛날... | https://www.sisaon.co.kr/news/articleView.html?idxno=205516 |  |
| esg | biz.heraldcorp.com | 반도체 호황에 몸값 3배 뛴 ‘이 회사’…국내외 ‘큰 손’ 투자 경쟁 | https://biz.heraldcorp.com/article/10916282?ref=naver |  |
| esg | economist.co.kr | “생산할수록 세금 깎아달라”…재계가 국회에 던진 100가지 요구 | https://economist.co.kr/article/view/ecn202610270011 |  |
| esg | ferrotimes.com | 페로타임즈 손바닥뉴스 10월27일(화) | http://www.ferrotimes.com/news/articleView.html?idxno=51130 |  |
| esg | mtnews.net | LG CNS, 준법경영 시스템 국제표준 'ISO 37301' 인증 획득 | https://www.mtnews.net/news/articleView.html?idxno=26353 |  |
| esg | dream.kotra.or.kr | 덴마크 선박용 내연기관 부품 시장동향 | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=190&CONTENTS_NO=2&bbsGbn=254&bbsSn=254&pNttSn=244658 |  |
| esg | 이데일리 | 허가·병원 재생의료 투트랙…일본으로 향하는 K-세포유전자치료제 | https://www.edaily.co.kr/News/Read?newsId=02742086645617184&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article |  |
| esg | investchosun.com | [Invest]IMM PE '에어퍼스트' 컨티뉴 펀드, 국내외 오버부킹 속 일부는 회... | https://www.investchosun.com/site/data/html_dir/2026/10/26/2026102680174.html |  |
| esg | g-enews.com | 한화오션, 캐나다 희토류 광산 데이터 검토... 2027년 본계약 추진 정황 | https://www.g-enews.com/view.php?ud=20261027032709911320990b2dc5_1 |  |
| esg | wikitree.co.kr | 말레이시아·태국 BLOOM 합류, 중앙은행 3곳 체제로…상품·출시 일정은... | https://www.wikitree.co.kr/articles/1169347 |  |
| esg | mediapen.com | 반도체 수출 날았지만…고비용 늪 빠진 건설에 발목 잡힌 한국 경제 | https://www.mediapen.com/news/view/1132484 |  |
| esg | biotimes.co.kr | 미국, 중국 바이오에 투자 빗장…신약부터 실험실 기술까지 안보 규제 ... | https://www.biotimes.co.kr/news/articleView.html?idxno=35600 |  |
| esg | news.inochong.org | 금속노동자 6명 중 1명만 “공급망 정보 충분”…실사 부담은 하청으로... | http://news.inochong.org/detail.php?number=6648&thread=21r09 |  |
| esg | thefairnews.co.kr | "자석 대면 색 변하는 위조방지 기술"…탄자니아, 나노실리칸 '탭앤체크... | https://www.thefairnews.co.kr/news/articleView.html?idxno=91913 |  |
| esg | 임팩트온 | EU 환경규제 대응 수준, 기업 인수가격에도 영향…M&A 실사 5대 항목 | https://www.impacton.net/news/articleView.html?idxno=30404 |  |
| esg | 한국경제 | 기후인지감수성, 평가할 수 있을까? | https://magazine.hankyung.com/business/article/202610265305b |  |
| esg | dream.kotra.or.kr | 전력수요 늘어나는 캐나다, 송변전∙저장장치 시장에 주목 | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=180&CONTENTS_NO=1&bbsGbn=243&bbsSn=243&pNttSn=244862 |  |
| esg | 임팩트온 | 골드만삭스 산하 LRQA, 공급망 실사데이터 기업 오메가 컴플라이언스 인... | https://www.impacton.net/news/articleView.html?idxno=30393 |  |
| esg | pharmnews.com | 바이넥스 오송공장, 유럽 EMA GMP 실사 통과 | https://www.pharmnews.com/news/articleView.html?idxno=307256 |  |
| esg | boannews.com | [인터뷰] 김종국 레신저스 대표이사 "렌즈를 걷어낸 자리에 '빛의 길'을... | https://www.boannews.com/news/articleView.html?idxno=146714 |  |
| esg | ddaily.co.kr | "단순 불량 아닌 힌지 자체 결함"…애플 '크랙게이트'에 329만원 예약 취... | https://www.ddaily.co.kr/page/view/2026102609080724535 |  |
| esg | ferrotimes.com | 페로타임즈 손바닥뉴스 10월26일(월) | http://www.ferrotimes.com/news/articleView.html?idxno=51107 |  |
| esg | the-today.com | [핫이슈] '친환경 배터리' 뒤에 숨은 석탄과 뇌물…印尼 오비섬 니켈 'E... | https://www.the-today.com/news/articleView.html?idxno=92388 |  |
| esg | 임팩트온 | [ESG 신간] 기후기술 사업화부터 공급망 재편·기후외교·ESG 경영 | https://www.impacton.net/news/articleView.html?idxno=30388 |  |
| esg | 한국경제 | 제조·생산 설비를 갖춘 보육기업의 현장을 투자자와 해양수산 협회 전... | https://magazine.hankyung.com/job-joy/article/202610253663d |  |
| esg | 매일경제 | [매경시평] 대미투자, 큰그림을 보라 | https://www.mk.co.kr/article/12185174 |  |
| esg | metroseoul.co.kr | 노사발전재단, ESG 대응전략 세미나 개최...국제노동규범 공유 | http://www.metroseoul.co.kr/article/20261025500183 |  |
| esg | voakorea.com | [심층: 대북제재] 2. 위장취업·무기거래로 제재 회피…해외 조력자·자... | https://www.voakorea.com/a/8214644.html |  |
| esg | hellot.net | [이슈 포커스] ESG 규제 ‘속도 조절’ 나선 유럽…전문가 “한국엔 오... | https://www.hellot.net/news/article.html?no=115753 |  |
| esg | theguru.co.kr | 삼성전자 하만, 토요타 유럽 '최우수 공급사' 2년 연속 선정…공급망 관... | https://www.theguru.co.kr/news/article.html?no=108578 |  |
| esg | g-enews.com | 시제품 장난감 벗어던진 3D 프린팅…우주선·열차 부품 대량 양산 시대... | https://www.g-enews.com/view.php?ud=202610240642129609fbbec65dfb_1 |  |
| esg | hellot.net | 오승재 서스틴베스트 대표 “AI 시대 경쟁력은 신뢰 가능한 데이터…기... | https://www.hellot.net/news/article.html?no=115749 |  |
| esg | insight.co.kr | 경쟁사 다른 美 조선소 인수 나섰다... 한화의 오스탈USA 인수 가능성은... | https://www.insight.co.kr/news/578981 |  |
| esg | pinpointnews.co.kr | 329만원 '아이폰 듀오'에 쏟아지는 혹평…외신 "한 손 조작·멀티태스킹... | https://www.pinpointnews.co.kr/news/articleView.html?idxno=498015 |  |
| esg | asiatime.co.kr | '329만원' 첫 폴더블 아이폰 듀오의 역설…"불편한 한손 조작, 멀티태스... | https://www.asiatime.co.kr/article/20261023500245 |  |
| esg | biz.newdaily.co.kr | '깊은 주름에 멀티태스킹 먹통' … 커지는 아이폰 듀오 성능 논란 | https://biz.newdaily.co.kr/site/data/html/2026/10/23/2026102300239.html |  |
| esg | 매일경제 | ‘329만원’ 첫 폴더블 아이폰 듀오의 역설… “불편한 한손 조작에 멀... | https://www.mk.co.kr/article/12184171 |  |
| esg | thefairnews.co.kr | "AI가 백신 수율 잡는다"…SK바이오사이언스, 생산부터 R&D까지 'AX 바이... | https://www.thefairnews.co.kr/news/articleView.html?idxno=91689 |  |
| esg | businesskorea.co.kr | SK바이오사이언스, 백신 생산 현장에 AI 도입 | https://www.businesskorea.co.kr/news/articleView.html?idxno=279553 |  |
| esg | 1conomynews.co.kr | 기아, 협력사 인권관리 강조했지만…동희오토 직원 사망에 실효성 도마 | https://www.1conomynews.co.kr/news/articleView.html?idxno=50936 |  |
| esg | theguru.co.kr | 'HD현대 협력' 美 조선소 인수로 선회한 와일드캣...김동관, 오스탈 USA ... | https://www.theguru.co.kr/news/article.html?no=108681 |  |
| esg | ferrotimes.com | 페로타임즈 손바닥뉴스 10월22일(목) | http://www.ferrotimes.com/news/articleView.html?idxno=51057 |  |
| esg | ferrotimes.com | 페로타임즈 손바닥뉴스 10월23일(금) | http://www.ferrotimes.com/news/articleView.html?idxno=51083 |  |
| esg | g-enews.com | 미국, 그린란드 군사 기지 2곳 설치 추진... 북극 군사 거점 확보 | https://www.g-enews.com/view.php?ud=20261023013823942020990b2dc5_1 |  |
| esg | imaeil.com | 한국만 비싼 '애플식 환율'…329만원 아이폰 듀오, 출시 전부터 웃돈 90... | https://www.imaeil.com/page/view/2026102217522104947 |  |
| esg | biz.heraldcorp.com | EU 공급망 실사 법제화… “국내 기업도 노동·인권 대응 과제” | https://biz.heraldcorp.com/article/10911451?ref=naver |  |
| esg | newspim.com | 노사발전재단, 노사 상생 글로벌 ESG 대응 전략 공유 | https://www.newspim.com/news/view/20261022001034 |  |
| esg | mtnews.net | 통상변화대응법 개정 시행… 외국 통상조치 피해 기업으로 지원 확대 | https://www.mtnews.net/news/articleView.html?idxno=26309 |  |
| esg | weeklytrade.co.kr | 갈수록 힘들어지는 미국 수출…이제는 관세는 물론 통관도 큰 장벽 | https://weeklytrade.co.kr/news/view.html?section=1&category=136&item=&no=101836 |  |
| esg | kpanews.co.kr | 삼성바이오로직스부터 후발주자까지, K-CDMO 다음 승부처는 | https://www.kpanews.co.kr/news/articleView.html?idxno=546958 |  |
| esg | biz.heraldcorp.com | 한국평가데이터·Coface “AI 성장 속 산업 편중·차환 위험 경계해야” | https://biz.heraldcorp.com/article/10911168?ref=naver |  |
| esg | ekn.kr | [EE칼럼] 기후위기 시대의 ESG - 그 방향을 묻다 | https://www.ekn.kr/web/view.php?key=20261022024002101 |  |

## collect:noise_keyword (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | g-enews.com | [특징주] 해태제과식품, 회계기준 거래 정지 후 재개 첫날.. '급락' - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPbkZaRjEwOU9SRDR0UFAzcFRJVjNDZlBIYVRja29fcXRlcXY5T05ORVo4cTdtZHV2amlSR3hOOFlzUGFSUXJzNjlBMVNSX2V6RG16bXdUckxxd0hsSUw3b0xZTFNTR2tYX1VMa1RMRURYX1c2LXA0d3BHM0Q2QkJEOGY3VHJ4aUZX?oc=5 |  |
| kifrs | datatooza.com | 데이터볼트 AI, 비트코인 회계 처리 오류로 재무제표 재작성…"과거 실적 신뢰 불가" - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9YcW8xQmxjTUtfVVFuQ1BtTGpGWTA2UFhmSGcyQXFfT3JmREVORmdJcXRqUWd4d2NRNFVVazB3NmFxcldmdzFkM0hsUVhJOWpzVEVGb2szLTFUZzJFMnc5ckd3X1pmTXU5eVhiZFg3c2diWFU?oc=5 |  |
| kifrs | kookje.co.kr | [차호중의 재테크 칼럼] 재무제표와 주식투자 - 국제신문 | https://news.google.com/rss/articles/CBMijgFBVV95cUxQYXduYXB0OEt4UUlDY015R3pmVV8xYm5lLUhFWUUtYWFiV0Y3bGVDMGZtZkJwOW9nMlVYcFNyblI3bFRvcTRXbnVXajZaMzNBNkpYLVhEcWl2RUh4QmcyZlo1aEIySm54dTV2MHBybWs5RkxjV2VRd2NfR0loRDVuNmdvY1lmcHlibS1nWkV3?oc=5 |  |
| kifrs | ajunews.com | [특징주] 회계 부풀리기 해태제과식품, 거래 재개 첫날 12%대 급락 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1OWmJsamxSVFRsV2FPVjZoZ2hRSzN1a2h0LXVOQ3h1MTVZa0JWQ2lrRHdUdjhHZm02Ml96SWpYTUd3akVqUnhtanlMdkpfMk9ES1NaUGw3UDFYd9IBWEFVX3lxTE5HSUxUNTJpSFMzUzdoMEkzQ3ZaZFpDbHd0OU9yYVlCX0tTVTlLUGw3NkJXaUppX1dCMUhSTk04Rmt2OU82MDg3Q1N5T3RVbC1lY3p1cnVfNFg?oc=5 |  |
| kifrs | businesspost.co.kr | NH투자 "에이피알 목표주가 하향, 새 회계기준에 3분기 영업이익 감소 효과" - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5GMS1teFJMQzdyN0FYZFVaRGs3VzNoeks0VUx6UVlkVXZHeDkxdHpPdDMxdHpZekZRNWxuWjNHbUNqMWU3MF9oYU9vVkNBR2x0cUhVZzcxZGxVaWNfNUNCLThseGcxU0t6aUpGdWEtUlFaMTQ?oc=5 |  |

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

## collect:out_of_scope (204건)

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
|  | 정책브리핑(경찰청) | 경찰청, 「2026 안보지킴이 공모전」 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787152&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 한국에서 함께 그린 원자력의 내일, 국제원자력기구 원자력 장관회의 폐막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787151&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | '산림휴양디렉터', 자연휴양림 조성의 길잡이 역할 톡톡 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787149&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 26.11월 국고채, 재정증권, 원화표시 외평채 발행 계획 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787147&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 장관, 코리아 그랜드 페스티벌 수산물 할인행사 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787146&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한국과 아랍에미리트 두바이, 문화협력 확대 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787145&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 부패는 멈추고 청렴은 키우고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787143&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 항공엔진 구조물용 고강도 소재부품 기술개발 심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787144&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 임산물 수출 유망업체 4개사 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787141&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-인도네시아 G20 셰르파 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787139&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, '다누리호' 출항 축하.. 원양산업의 새로운 도약 기대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787134&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 제15차 아시아산림협력기구 총회 개최… 국제산림협력 확대 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787136&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 박홍근 장관, AI 영상 제작 현장방문 및 전문가 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787130&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부 국제질병퇴치기금 출국 납부금 환급 서비스 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787138&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "산림 사업 현장 안전 사각지대 없앤다." - 영주국유림관리소, 안전보건공단 경북지역본부 합동 중대재해 예방 교육 실시 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787129&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 강신철 국방부장관  제13차 아세안 확대 국방장관회의(ADMM-Plus) 참가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787126&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 조용범 차관, 제24회 협동조합정책심의위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787122&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 동부지방산림청, 태백에서 임업인들과 산림규제 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787125&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [차관동정] 정의경 제2차관, "이동로봇, 실증 넘어 상용화 기반 마련할 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787123&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 구혁채 과기정통부 제1차관, 원자력학회 참석 및 경주지역 연구현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787116&pageIndex=1&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 기술에서 시장까지,  K-GX 선도하는 기후테크 혁신기업 본격 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787121&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부, AI 스타트업의 유니콘 도약, 현장 의견으로 정책 완성도 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787120&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중소 제조현장을 피지컬 AI 혁신의 무대로, 「중소제조 피지컬 AI 확산 전략」 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787119&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부·복지부, 글로벌 제약바이오 시장을 선도할 「K-제약바이오 프론티어기업」 200개 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787118&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "멈춰 있던 일상에서 꿈을 향한 첫걸음까지" 청년들의 작은 도전과 성장의 기록 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787113&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 글로벌녹색성장서밋에서 기후대응·성장의 선순환을 위한 국제협력 강조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787114&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한국형 녹색대전환 이끌 기후테크 혁신기업, 기술부터 시장까지 전방위 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787112&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 동포와 함께 여는 대한민국의 미래...동포정책 전문가 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787111&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 편지와 함께 먹거리, 집배원이 그냥드림 전하며 어려움 살핍니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787109&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 법제처, 아동·청소년 대상 성범죄 예방을 위한 현장 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787108&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)국내 수급에 차질 없는 범위 내에서 경유 수출제한 조건부 완화 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787107&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 특송물품 악용한 마약밀수 차단을 위한 검사 강화 현장점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787106&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 2027년 장애인일자리 사업 참여 가능 인원 2,600명 늘어 3만 8천 명으로 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787100&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "AI로 누구도 소외되지 않는 보건체계 구축", 한국-아세안 보건 협력 연결망 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787099&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 국내 물리적 인공지능 산업 육성 가속화를 위한 전문가 소통 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787096&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 공직 전문성 높이고, 일하는 방식 바꾼 공무원 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787103&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [정부합동] 백해무익(百害無益)한 '담배'...유해성분 검사 확대, 정보 제출 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787098&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [정부합동] 정부, 국내 판매 담배 465개 제품 유해성분 검사결과 최초 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787097&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 기부채납 수목원, 국·공립 전환 때 조성면적 기준 10ha에서 2ha로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787093&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림, '기운담길 소원 걷기행사' 연계 산불예방 캠페인 펼쳐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787091&pageIndex=2&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 장애인 건강 수준과 격차, 건강지표로 본다 「2026년 장애인 건강보건통계 콘퍼런스」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787085&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정부, 국내 판매 담배 465개 제품 유해성분 검사결과 최초 공개… | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787084&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 백해무익(百害無益)한 '담배'... 유해성분 검사 확대, 정보 제출 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787083&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제16회 국가정책조정회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787087&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 국토교통부는 타워크레인 안전 강화를 위해 노력중입니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787079&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년 공정거래 학술연구 지원사업 최종발표회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787074&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 부패를 막는 청렴, 갑질을 넘어선 공존... 푸른 숲을 닮은 공직문화를 위하여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787082&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 공학계 리더 초청 간담회, AI 시대 도약 위한 지혜 모아 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787080&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처-소비자원, 집중력 강화·키성장 효과 내세운 해외직구식품 공동조사 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787072&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | [국기연] 제3대 국방기술진흥연구소장 취임 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787071&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 학교·노인복지시설·군부대 대상 '국산 밀·콩 DAY' 추진으로 국산 밀·콩 소비 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787070&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 복지부·중기부, 글로벌 제약바이오 시장 선도할 「K-제약바이오 프론티어기업」 200개 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787069&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(교육부) | "우리 지역, 우리 아이에게 꼭 맞게" 사교육 고민 덜고, 영유아기 교육 선택 돕는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787057&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 한국어로 열리는 진로·취업의 기회, 베트남 한국유학박람회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787056&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 2026년 10월 대학정보공시 분석 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787055&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 필요한 의료는 충분히 보장하고, 의료비 부담은 적정하게, 제11차 의료혁신위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787068&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 신청주의에서 '선제지원 복지'로 전환한다 복지급여 4개법 하위법령 정비 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787049&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 저인산혈증성 구루병 및 골연화증 치료제 11월부터 성인도 건강보험 적용받는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787048&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 원격중환자실, 강원·충북 권역에 이어 11월 서울 권역까지 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787047&pageIndex=3&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "배우자 동의는 모바일로 바로, 추가 서류 제출은 나중에" 기초연금 온라인 신청 문턱 낮춘다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787046&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 인공지능(AI) 시대 개인정보, 안전한 활용의 길을 국민과 함께 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787051&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부와 한국전자통신연구원, 세계 자율주행 레벨 국제표준 개정 주도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787043&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 2026년 10월 퇴직공직자 취업심사 결과 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787050&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 기후위기·AI 시대, 국민 생명지키는 「2027년 국가안전관리 집행계획」 확정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787067&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부, 재난문자 157자 확대 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787065&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부, 민관협업 '디지털서비스 개방  성과공유회' 개최… 우수사례 4건 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787063&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 2026년 5월 생활인구 상반기 최대 규모, 인구감소지역에 활력 더해 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787061&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 인공지능(AI) 시대 개인정보, 안전한 활용의 길을 국민과 함께 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787059&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | '26년 2/4분기 『생활인구』 산정 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787054&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2024년 소득이동통계 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787053&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 집중호우에도 안전한 도시 만든다… 하수도정비 중점관리지역 11곳 추가지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787052&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [10.30.금.조간] 우리나라 손상 발생과 변화를 한눈에, 「손상 발생 현황 INJURY FACTBOOK 2026」 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787045&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | (주)셀트리온의 하도급법 위반행위 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787042&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(감사원) | 서울 서대문구 도시관리공단의 관리·감독과 준예산 집행 관련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787044&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 첨단산업의 경쟁력, 국민생활의 신뢰... 계량측정이 뒷받침한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787041&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 아동용 섬유제품, 완구 등 48개 제품 리콜명령 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787040&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K-배터리, 경쟁력·자생력·협력 강화 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787039&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 생산성 혁신과 지속가능경영으로 기업의 미래를 열다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787038&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 「기획예산처-국회미래연구원 공동세미나」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787037&pageIndex=4&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 현장의 목소리 귀담아 민생규제 합리화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787033&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 국립평화통일민주교육원, 브레드이발소와 협업 제작한 「초콜릿 마을의 지도」편 방영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787094&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 고객센터 개인정보, 불필요한 조회·이용과 일괄 노출 막도록 보호 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787036&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 안전조치 의무 위반 2개 사업자에 38억 8,500만 원 과징금 부과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787035&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 전국 주택 직거래 및 서울·경기 아파트 거래 기획조사 결과···위법의심거래 678건 적발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787027&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 2026년 3분기, 전국 무역항에서4억 691만 톤의 물동량 처리 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787025&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 국내 첫 수산식품수출단지, 목포에 문 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787024&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 인공지능(AI)이 여는 바다, 미래 수산양식 산업을 만나다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787023&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부, 프랑스 극지 및 해양 대사와 2028년 유엔해양총회 개최 협력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787026&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 이장 선출은 '1세대 1표'가 아닌, '1인 1표'로! 농식품부, 성평등 농촌문화 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787022&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 사진 한 장으로 반려동물 건강 체크, 인공지능(AI)로 여는 펫헬스케어 시대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787021&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기상청) | '앙부일귀의 과학적 의의와 가치'를 논하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787034&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 산림복지 관련 공공기관 통합 본격 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787031&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 숲경영체험림 활성화 위해 현장 목소리 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787029&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 아시아 산림협력에 국제기후재원·민간투자 연계 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787019&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국기술교육대, '2026년 일학습병행 OJT Forum & 우수사례 경진대회' 성황 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787017&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국고용노동교육원, '고용노동교육 2.0' 기반 경상남도 노동교육 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787016&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 사내·공동근로복지기금 유용 근절 위한 5,308개 기금법인 '전수 점검' 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787015&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 2026년 9월 사업체노동력조사 및 2026년 4월 산업소분류별 고용통계 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787014&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 해외에서 쌓은 경험, 국내 일자리로 잇는다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787013&pageIndex=5&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 유럽 항공우주기업과 국내 중소기업 간  협력의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787009&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 드론으로 빈틈없이 살핀다… 가을철 산림 불법행위 집중단속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787011&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 89개 방송사, 장애인방송 의무편성 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787007&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 전통시장에서 찾는 일상 속 법 보물... K-법 생활발견 캠페인 '숨은 법 보물찾기' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786997&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 2026년 면세점 쇼핑 축제 「코리아 듀티프리 페스타」 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786999&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청 전자통관시스템(UNI-PASS), '정보기술 서비스 국제표준' 21년 연속 인증 쾌거 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786998&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청-유엔식량농업기구,  통합산림위험관리 협력 2차기 사업 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786996&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부， GS리테일과 독립유공자 산재묘소 스마트 안내판 설치 등 협력 업무협약 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786991&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 수도권 '신규택지 10.4만호' 신속 공급 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786992&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 가을철 산불, 예방부터 대응까지 빈틈없이 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787005&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 인공지능(AI) 행정부터 과학수사, 햇빛소득마을까지, 강원에서 행정안전부 우수정책 세계와 나눈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787003&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 원전 공론화위원회, 공론화평가단 운영한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787001&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 산업용 히트펌프 기술개발 및 실증 확대… 산업부문 탄소중립 앞당긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787000&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년 상호출자제한기업집단 채무보증 현황 및 금융·보험사 의결권 행사 현황 정보 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786988&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림항공본부, 유관기관 합동 가을철 산불예방 캠페인 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786994&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 화장품 핵심기술, 지식재산으로 지킨다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786987&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 우수 임업경영체 현장 방문… 임업인 생생한 목소리 경청 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786986&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 퇴직연금 기능강화를 위한 노사정 합의로 노동자의 든든한 노후소득 보장체계 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786984&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 해외 피싱 조직 끝까지 추적하고,  국민 피해는 사전에 막았다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786981&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 내 손 안의 창경궁, 스마트폰과 함께하는 유산 산책 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786983&pageIndex=6&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 한국의 신명, 유럽을 두드리다… 국립무형유산원 <풍장 KOREA> | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786976&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 튀르키예 퀼테페 유적에서 헬레니즘시대 '모자이크 유구' 최초 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786974&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | '일월오봉도 은차도구' 등 제56회 대한민국공예품대전 수상작 전시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786972&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 제조데이터로 자라는 M.AX, M.AX 얼라이언스 ｢데이터 분과｣ 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786980&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 국민절반이 사용하는 중고거래 플랫폼, 국가표준으로 더 안전하고 편리하게! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786979&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 글로벌 화학 기업 독일 머크(Merck),  대전 바이오 원부자재 제조 거점 개소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786978&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 퇴직연금 기능강화 방안 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786971&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(병무청) | 해외에서도 '전역증 재발급' 손쉽게, 재외공관 서비스 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786969&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(조달청) | '혁신기업의 성장 사다리, 공공조달로 잇는다' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786968&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 민간의 혁신기술로 공공현장의 해법 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786967&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | 국민권익위, "수사기관에 공익신고자 책임감면 적극 협조 요청한다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786966&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "사후관리기간 3년 중 2개월 남기고 고소작업차 양도한 사업주"… 보조금 지원 취소는 '가혹'해 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786965&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "공영주차장 차량 부제로 이용일수 줄면"… 정기주차권 요금·이용기간 조정해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786964&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 김장철 대비 단순처리 농·수산물 생산업체 위생점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786960&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 제2회 특별성과 2개 사례 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786959&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 커피·치킨 등 조리·판매 편의점 및 무인 식품판매점 점검결과...33곳 적발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786958&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 대한민국 대중문화의 어제와 오늘, 국가가 기린다... 고(故) 신해철, 유재석, 한영애, 블랙핑크 등 문화훈장 수훈 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786957&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 미술품 감정서·진품증명서 고시 제정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786956&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 관광개발 사업 성과관리 제도로 재정투자 효율성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786955&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 국제식품규격위원회(CODEX)에서 식품오염물질 국제 기준 논의 주도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786952&pageIndex=7&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, '식품첨가물 향료 바로 알기：자주 묻는 질의·응답집' 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786951&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 동등생물의약품(바이오시밀러) 평가 가이드라인 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786950&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(소방청) | ﻿﻿"대한민국 밧줄(로프) 구조 기술의 도전과 도약" 제4회 ONE TEAM ROPE RESCUE 경연대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786949&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "안전은 특별한 노력이 아닌 당연한 일상이자 문화가 되어야" 소방청, 「제3회 위험물 안전관리 우수사례 경진대회」 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786948&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 2026 코리아 튜닝카 페스티벌 열린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786946&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 국립생물자원관, 도시 야생동물과의 안전한 공존을 위한 과학적 관리 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786947&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 2027년 유기농업자재지원 강화…녹비작물 종자 선택 폭 넓어진다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786945&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 해외에서도 '전역증 재발급' 손쉽게, 재외공관 서비스 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786970&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 양육비 선지급 소득기준 전면 폐지  한부모가족 지원 대상 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786961&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 가까운 공공 생리대 지급기 위치,  온라인 지도로 쉽게 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786953&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 개인투자용 국채 11월 2,000억원 발행 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787006&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 확대 거시경제금융회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786989&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 광진 서민금융통합지원센터 방문, 서민금융 지원 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787127&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(교육부) | [보도참고자료] 대학수학능력시험 스마트안경 활용 부정행위 관련 대응계획 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787012&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(인구전략위원회) | 골목상인들이 함께 만든 최초 직장어린이집,  지역맞춤형 돌봄모델로 전국 확산 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787153&pageIndex=8&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한·필리핀 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786944&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한·인도 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786943&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한-말레이시아 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786942&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리 주재 제35차 새만금위원회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786941&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 인천 강화군 소재 소(牛) 농장 예찰 검사에서 구제역이 확인되어 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786963&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 아시아 8개국 전문가 한자리에...국립산림과학원, 첨단 기술 융합 '도시숲 연구 연대' 강화 - 위성·AI 기술 기반 아시아 도시숲 공동 모니터링 체계 구축 방향 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786940&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한·호주 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786938&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) (약칭)초광역특구법 관련 원포인트 사회적 대화 제6차 실무협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786937&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고)고용노동부, 자체 개발 '재난대응 훈련 시뮬레이터' 소스코드·제작방법 전면 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786936&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한-일본 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786935&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 홈쇼핑 통한 중소기업 지원 실효성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786933&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의 계기 한미 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786906&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(외교부) | AI 시대, 한-메콩 경제협력의 새로운 도약을 모색하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786903&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리 주재 전국상인연합회 오찬간담회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786902&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 국가공무원 7급 공채 제2차시험 합격자 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786901&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 경제외교조정관-앙골라 에너지수자원부 장관 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786900&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림관리소, 가을철 산불방지 총력 대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786898&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 블룸버그 아태 대표 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786894&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 카드뮴 기준 초과 검출된 '가공김' 회수 조치 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786899&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 박홍근 장관, 전북·새만금 현장방문... "피지컬 AI 및 새만금 개발 지원을 통한 지역균형발전 및 미래 성장엔진 확충 적극 추진" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786895&pageIndex=9&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 바이오의약품 원료물질 인증제도 현장과 함께 만든다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786893&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 지역·필수의료 수가 2.7조 원 우선 투입, '27년 1월부터 본격 수가 구조 혁신 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786886&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 봉선사 동종 국보 지정 기념행사서 산림청 규제혁신 성과 홍보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786885&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 구글·애플, 외부결제 허용하고  수수료 체계 개선해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786878&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제46차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786880&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 소나무재선충병 확산 방지를 위한 강원 영서권역 대응 논의에 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786883&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | K-팔란티어, 신안보 혁신기업 육성 본격화…전략분야 선정계획 및 펀드 조성방안 등 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786875&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 고용노동부, 인사혁신 경진대회에서 인공지능 행정 혁신사례로 대상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786877&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "美 은성무공훈장, 73년 만에 고인의 품으로"… 6·25전쟁 영웅, 故 남운수 님의 오랜 한 풀었다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786876&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 민·관 해상교통안전 협력 강화...해경청, 관계기관 합동 토론회로 협력 공고화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786874&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청,경비함정유류비 약 469억 원 추가 확보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786869&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청, 일본 해상보안청과 해양오염 대응 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786868&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 10월 안전보건협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786873&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 적법절차와 인권 보호 강화... 해경청, 변호사 자격 수사심사관 3명 채용 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786867&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 가명정보 활용 현장 경험 공유하고 새로운 연구·사업 기획 지원한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786870&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 수목원조성예정지 지정기간, 연장 포함 최대 8년에서 4년으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786862&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(법무부) | "수형자들의 땀과 성찰이 빚어낸 자활의 결실…" 제55회 교정작품전시회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786863&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 기후대응위, 산업부문 저탄소 전환 정책포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786858&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 세계산림치유포럼서 정원치유 국제협력 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156786855&pageIndex=10&repCodeType=&repCode=&startDate=2025-10-29&endDate=2026-10-29&srchWord=&period= |  |

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

## collect:tax_subject (38건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | karnews.or.kr | [세법톡톡] 2026년 세제개편안 (양도소득세) - 한국부동산뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Ub0liX2hObkdsdUhZc3lES3AycE9NV2xfVHBvMDJNYXpkbkVZNi1FdlZKcklqUndyX0xoZXB1OUFDdHNkZWNHa1BQN1FWMHBMUlZhV2V1ckpvRWUwZVpzZFctNllmUFd3bHZB?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | news.kbs.co.kr | 부부 공동명의는 진짜 불리할까? 세제개편안 오해와 진실 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5yTUo1c2FfUGVDcERxc2lJM0JHSUItNks1N083NkViV1Z2VHFnSWFUdjdHYnRyUE9fSUoydEg0ekNnY0xVRlBiTEkzYWlBYkplV3p4UjctSkVGVlU?oc=5 |  |
| tax | lawtimes.co.kr | 미국 세법 및 판례상 국내원천소득의 증명책임과 상호주의 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB4bmthMkluOF84Uk9raFgzaFlqM2ptOW1oNnJWemdCRHRSMGxKZElNU1VkNG55SUdOUjZtTWp1R3loeFZHMkcxblNiRDJBNlY3NmRMZXZZa1pWTXdVdUhfT3V6SUZSajRxdzduclFB0gFyQVVfeXFMTU84R0QxVWZuQTdqTGJjM2M5UXA4R1JPQThYY1ZPV3RQRWdhcjhmaW0zUXAzRUtEVUlIcDBKYXdCSWltUHozb3liYlA1TnlyUWI4TmRlZkdrV2h3UXBzWmNjWEtLQi14bTJvSF9ldE1oVDJn?oc=5 |  |
| tax | shinailbo.co.kr | 안철수 "정부 세제개편안은 '고려장 세법 개정안'…파기가 답" - 신아일보 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1xSmFfcWRZc09JRzl6dFJRQVlodkhpWWM4aEU4TE1XVUNfXzQ2VFczQnlTVWJ1QUtCMmV1WWRGT19CODd6NXI3NGhsWldHXzlBcUxJRk52MXdkUnplb0NtSWJOUExvV1JQeEtUX3FFMmc?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzA?oc=5 |  |
| tax | newstomato.com | (8·3 세제개편 한 달)종부세 후퇴…정책 신뢰 ‘실종’ - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFAzbGtwN19uMk0xRExHYUtyLTVMalFQeVp5U2FtSno4N2IyOUlVbXRXRE92TnBqUjl2TS0tYW4zdWNoSmRsMjhwZVhPZ04xZUVHVVlEajBMSzF1Y25hdXdfWA?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | joongang.co.kr | 안철수 “李 정부 부동산 세제 개편안 ‘고려장 세법’” 비판 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1rbU5oUml0aWw5SjRrN3p2b2JuZGpzZE55azhFOVZzMTBaWGZSbDk0WjQtLUNJMzhobm00dk14YmhaZ19TRTZpalBfWjJ5N2ZmZTJ3bk9n?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | newspim.com | [뉴스분석] 부동산 세제개편안 정부안 의결…與 내부서 불거지는 수정·보완 목소리 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBaMU94ZFRIbWRacklQenVyOHN0dUxYc3AzM0ZveTR5a3Fvd0NsaW9jcVNNRGN3emRCcUFCQWJsa0J5TEFNWnd3bEc1cExsRlNSVDJCMWNNWEkxOWQz?oc=5 |  |
| tax | 한국세정신문 | 2026년 부동산 세제개편안 주요 내용 총괄표 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9VV05RWWFtWkNqZmNWQktodVFiLS1GckNYcXZ6SGUxcFc5dXhEQi0tN0FmM2tucEROdHF6OU4xUnpmd1NXd29fQUpnMkdRbnVac2pqOEsxUTBaN1JWdjcyVjBHOUE?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | jinju.news | 김태호 의원, 지역균형발전 강화를 위한 지방교부세법 개정안 대표발의 - 진주인터넷뉴스 | https://news.google.com/rss/articles/CBMid0FVX3lxTE44X0w1UUNpbTMtSnZFa2ZpdUF0dHhxeU5GWFlWNF9NZTY0aWRNWGJlS0lLMEJFc1lERHd0MFBubjhHUVBERlVKT204VjQ2TlIxb3drSUJfV3FyMWcxX1RONzUxWE9LMzkxY2VGZVBCVjl5WVlnTUp3?oc=5 |  |
| tax | news.mtn.co.kr | 부동산 세법에 정치권 '시끌'...나경원 "강제 이주 명령" - MTN 머니투데이방송 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5PMFlBZTFJdUYtRUpCdlNGXzQ3SkR5WE10SlBvcGFkWExqX0llN19WZjBCbjZhT0RDNTczTkcwajh2RXM5bmh5UFNJNDl4YzdaQ2o3alNLOVdRM0JULWVhbVFieXI?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | hani.co.kr | 민주 “세제개편안, 정교하게 다듬겠다”…서울 의원들은 여론 주시 - 한겨레 | https://news.google.com/rss/articles/CBMidEFVX3lxTE9ZTzhoZFVjaW01QjdfMGNrUkhSdXJKaUVZSGEtSkJ4M21RbG03cUxDUVZSbHJTZk5tYWtXQ3RQaHVuSWthcHA5cGM2TlZEWFRCVXFBRVItN2JCQjhWcDQ4TlpDQmpmUy0xNUE3Q0pZaURubXZh?oc=5 |  |
| tax | newspim.com | [2026 세제개편] 가업상속공제 최대 1000억으로 확대…경영요건 10년→30년 강화 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1LMUhHbGx0N1NBekZQc1VSbHhZbllJR3VobXJFREtXLXpFejNmUVdua2U3eE81TEU3c0JRUGRwMURmS0FRTlZsOHRjck9mVTA0NXJURUlzNDhERzlH?oc=5 |  |
| tax | newsk.net | 세법 개정안의 주요 변경 사항 : 한인동포신문(몽골) - 뉴스케이 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXdlRVQnREMG5BcGNrUjNUdF9MSEVtbGJzdHBuWjNBM29ZTDBtYXY5TWw4Q1F4OG1QMlVSZnQ1YTNYMEpBcmJKX1hhTDJOczE0UTQ5VnlRY1FmZw?oc=5 |  |
| tax | monthly.chosun.com | 안철수, 정부 발표 세법에 "고려장 세법" 맹비난 - 월간조선 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5tdnJxWXljYlRSN19BOEM1Vm4xWUtwMElyRFlranNCaE1TVUFLU05xRVBRbEkyUC0zejVZZ2RERlYxSHpvdmxWZXR4QWx4dkRFZkFUSnpZclRBeHRVV24xaTBRazNIakc1cG9YTQ?oc=5 |  |
| tax | nbnbiz.co.kr | 정부 세법개정안 속 ISA 대수술에 투자자들 거센 반발 - nbn 시사경제 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE15SE5vWnlDRVAwMGxJRDZfdVlLX2l1SXdjaC1PbHRKd1NVN3VuTG9jdkNFSFFmdGY2MW0xeDFfSmljS1prNlJndHhOdUt5Q05SWGg0a0Z1MXJTWGllOGRfS05ySFk?oc=5 |  |
| tax | imaeil.com | "살면 보유세, 팔면 양도세 폭탄" vs "서울시장 책임" - 매일신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wQTFnTkQ1OWM0OU9vQmh4ck9wdk5Sb0pzdkZZX0tKNzNXbDdNWWlNVGJGTnlyVjliRThaZG9mZUhCVGZjWU9CeUZDSEZMZUV4N3o1cFBZcjVFQ0J4Yi14QXNn?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | hankooki.com | 국민의힘 재경위원들, 정부 세법 개정안 비판 기자회견 - 한국아이닷컴 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9Kbm1OSGFfem03UlVTMUtQVjJ4TGtGU3IycWV3YWRodmE2UVlKSV9Jd01NWXl4VWRfd0Q1enR4Y2RWVko2WHhTY21UVjVHU1FoOHROUnVuTktDM192R0JoWnh1Rmt2cVJRcFJn0gFvQVVfeXFMTjFUZHBkS3BIcGdabXFsMWpSODNMWVVsQW4zM3dUVEdiOXcwcnNkOGVURHdoNmlSSGwxWWMxYl9fWWpYQ0dlLWkwdHNwN0hRQ1JsNzc2cngxUk5hckNyR21Dajh2R1lpLUhjZmVDdnFr?oc=5 |  |
| tax | chosun.com | 수십조원 ‘세수 펑크’ 원인은…세법 개정, 우크라 전쟁 등 변수 반영... | https://www.chosun.com/politics/politics_general/2026/10/27/ICBT5YQXINCPDMGFZSEEMNWJJA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | biz.heraldcorp.com | ‘책 출판’은 되고 ‘잡지 출판’은 안 된다?…가업승계 세제 개편의 ... | https://biz.heraldcorp.com/article/10913027?ref=naver |  |
| tax | 조세일보 | 한국조세법학회·국회입법조사처, 30일 세법개정 쟁점 논의 | http://www.joseilbo.com/news/news_read.php?uid=578449&class=7&grp= |  |
| tax | gukjenews.com | 김남준 의원, '배당+자사주 소각' 합산 주주환원율 세제개편안 발의 | https://www.gukjenews.com/news/articleView.html?idxno=3734375 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

