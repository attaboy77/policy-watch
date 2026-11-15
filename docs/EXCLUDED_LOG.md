# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-15 18:22:34 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1682건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 14 |
| excluded:company_event | 1 |
| excluded:company_self_activity | 2 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 20 |
| excluded:financial | 2 |
| excluded:industry_specific | 11 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 43 |
| excluded:no_regulatory_signal | 37 |
| excluded:opinion_piece | 2 |
| excluded:reader_content | 1 |
| excluded:related_news_attached | 1 |
| excluded:similar_news_merged | 17 |
| excluded:smb_only | 1 |
| excluded:standard_setter_governance | 1 |
| collect:event_announcement | 18 |
| collect:incident | 1 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 267 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 205 |
| collect:out_of_window | 40 |
| collect:tax_subject | 36 |

## excluded:category_cap (14건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 머니투데이 | ESG 공시 의무화 코앞인데…대형 상장사 5곳 중 1곳 '보고서 無' | https://www.mt.co.kr/stock/2026/11/11/2026111014243556817 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성 공시 제도 로드맵 초안 및 확정 공시기준 주요 내용 - PwC | https://news.google.com/rss/articles/CBMif0FVX3lxTE1Gd29wMWxoczQwX09wRThxRzhCam43V3VTRHp6LWFzQWgyZUdjeTF5dzJBZUJoYnlLZFdYWEZlbWVmRDNEcHM5eGVpTGhPSThiUEtkNlpBTlVVb2laR1FlSnlCa2ZBeG5uWFFvaHNfdG9LeExxeFRLc1ltdXgzcmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 로드맵 확정…10조 이상 코스피 상장사부터 의무화 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5XUnhUekpXVlVFZEFuR0ZtdldTYlhvX1A4Yk84UVZqc0xCLTVYQVlTT2wwLWZRUkNGb0FpWTZaeEJzUFNXWVpwYlFJQUhvTmR3aEtOS0FKeFVvQzBiVGJObkF4X3phc1VScmJMQdIBcEFVX3lxTE5HcHpjSzJTMnQyakNLT190LUVLX3ZGNXM0LWJKVzA1cXlHcjhVc1dWY1V4OGFrcG42REdfMWJRVmlXVUcwZ2JYTXE5ZE1BamduRllrbGZReTBqbjRUeWVQZUl2cEdfZ09CRVFRemlvS3Q?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | edata.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5ud29WMHQ5RnNleWFLbDR2TFJfSzh2UXlZWjZoWndQUnp6NHI3NWJmaUlfOFgwcXFSM1liQ1E0MEZZZWhDMXRsZjhiT0g2SW91azQybGw1aGVDSUMxZ0E?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 |  |

## excluded:company_self_activity (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | choicenews.co.kr | KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 | http://www.choicenews.co.kr/news/articleView.html?idxno=173128 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (20건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |
| tax | 행정안전부 | 지방세법 시행령 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88292 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| icfr | tfmedia.co.kr | ‘회계사들의 올림픽’ WCOA 2026, 17일 개막…韓 외감법 전면개정 논의 | https://www.tfmedia.co.kr/news/article.html?no=208737 |  |
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 | https://www.impacton.net/news/articleView.html?idxno=30527 |  |
| esg | ESG경제 | 泰, ISSB 지속가능성 공시 의무화 확정…28년 SET50부터 단계적 시행 | https://www.esgeconomy.com/news/articleView.html?idxno=17232 |  |
| esg | ESG경제 | ISSB 자연 관련 공시 실무서 들여다 보니...S1ㆍS2 보완 | https://www.esgeconomy.com/news/articleView.html?idxno=17209 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |
| esg | 임팩트온 | EU 은행 ESG 공시항목 37% 축소…EBA, XBRL 전산규격 확정 | https://www.impacton.net/news/articleView.html?idxno=30289 |  |
| esg | 임팩트온 | ESG 공시 규제 후퇴 vs. 월가는 기후데이터기업 인수 경쟁 | https://www.impacton.net/news/articleView.html?idxno=30224 |  |
| esg | 임팩트온 | ISSB, 22일 자연공시 초안 공개…사업장 위치·가치사슬까지 평가 | https://www.impacton.net/news/articleView.html?idxno=30168 |  |
| esg | ESG경제 | EU 역외 지속가능성 공시대상 국내기업 "20~30곳"...KSSB 공시 정보 활용... | https://www.esgeconomy.com/news/articleView.html?idxno=16805 |  |
| esg | tfmedia.co.kr | [KAI 세미나] 백태영 전 ISSB 위원 “ISSB 전면 도입은 기준 통제권 포기... | https://www.tfmedia.co.kr/news/article.html?no=207254 |  |

## excluded:financial (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | newsworks.co.kr | 금감원, 증권사 발행어음·IMA 내부통제 '고삐'…모범규준·TF 가동 - 뉴스웍스 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1vbk55YWxXWG1IdVdWeUQ4N3hRTENQNTJ2MU5vRHVoSUd3aEFWbzMtMEdSalNOQ0V0c295d3FFbENLQ1oyQWZLZEhwU2xianFXd2hkLUlQcmNIUHYtODg3LWhEblNvV0RVTHpubE1ya9IBc0FVX3lxTFBVWkwtM3MzbHl6RzhDaTRSd3BBVnRINjFTQWVhTms3UGQ1YjJpbU95NmFMd2JacXZnOFlSaHdRQzAyeVI3V05hVzB5amM0UE5qZXdxVVRhX2FpSHBmUzh1aU1mQVR4d3BYVmgyNnZTRDBuNDg?oc=5 |  |
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |

## excluded:industry_specific (11건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 2025년 제1117호 보험계약 | https://kasb.or.kr/front/board/comm020View.do?boardMngNo=&boardNo=&cmtreadSeq=&seq=494&siteCd=002000000000000 |  |
| kifrs | 한국회계기준원 | 2022년 제1117호 '보험계약'과 제1109호 '금융상품'의 최초 적용 - 비교정보 (제1117호 보험계약) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=316&searchfield=ALL&searchword=%EA%B3%B5%ED%91%9C&s_date_start=2022-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2021년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=300&searchfield=ALL&searchword=1117&s_date_start=&s_date_end= |  |
| kifrs | 한국회계기준원 | 2018년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=231&searchfield=ALL&searchword=1117&s_date_start=2018-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2017년 제1104호 ‘보험계약’과 제1109호 '금융상품'의 동시 적용 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=220&searchfield=ALL&searchword=&s_date_start=2017-12-01&s_date_end=2017-12-31 |  |
| kifrs | 한국회계기준원 | 2015년 건설계약 공시 (제1011호 건설계약, 제1037호 충당부채, 우발부채, 우발자산, 제1115호 고객과의 계약에서 생기는 수익, 제2115호 부동산건설약정) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=166&searchfield=ALL&searchword=1115&s_date_start=2015-01-01&s_date_end= |  |
| kifrs | 금융감독원 | K-IFRS 제1117호‘보험계약’관련 사전공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36151&menuNo=200435 |  |
| kifrs | nbnnews.co.kr | 서해구, 공동주택관리 법정교육 실시...화재 대응과 관리비 회계처리 실무 중심 - 내외뉴스통신 | https://news.google.com/rss/articles/CBMibEFVX3lxTE02anQwZC13a3U5VzdTNFdTTW94UDdjMGlSaWh2NkdidHhiaS1ydmhUN3V4dFZ4cVJjMmI5aDUzcFZPajQ2WWx1aFV4cGFuLUExVDgwUmVGYlMwbEw0ekRrRTVCYVpkR29uWGJoStIBcEFVX3lxTFBya195RHJvbklBN0hvTVVZVm5Wb3BWLUIyZzlXMTcwTVVQYnJVRlJWTmo2SjVldmhMM3pXeEdGSi1tN0ZkZV9pa3pvc3NVSlNNX2dWbEJMNVdtNTBRMHFRUi0tS2R4ZThlbVUtTTdNRVg?oc=5 |  |
| kifrs | sejungfocus.com | 서해구, 공동주택관리 법정교육 실시...화재 대응과 관리비 회계처리 실무 중심 - 세정포커스 | https://news.google.com/rss/articles/CBMibkFVX3lxTFA4YzYyelRzMUVCTGNnUHAtT090REo5ZFRIc0RMbW4yZEhRb1ZYQ1J5LU5MV2J4cEpEV2FyeTFUSllaQ21BUEw0Y0ROOWhfUENEeDIxeXBuaUJMc3FucDZieEhyWGt4cmpsVnNiLW5B?oc=5 |  |
| kifrs | webeconomy.co.kr | 서해구, 공동주택관리 법정교육 실시...화재 대응과 관리비 회계처리 실무 중심 - 웹이코노미 | https://news.google.com/rss/articles/CBMickFVX3lxTE5mMXYwVDBwNkpmbzFjTjdWYzFOTHIwLWdnejJrUU1NQ2V5eGp2Q1FEcTJ6LXQ0RjVuaFV2bjlrUG01ZlZibHh0WWZ5ZTNqVGE1TXVud2FWWFNmc2xtX09YYnlUWmFJMGNYbFFTcWV0ZUhOUQ?oc=5 |  |
| kifrs | hapt.co.kr | '공동주택 회계 감리' 법안에 "옥상옥(屋上屋) 규제" 지적 | https://www.hapt.co.kr/news/articleView.html?idxno=169530 |  |

## excluded:manual_id (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |

## excluded:news_too_old (43건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | news.koreanbar.or.kr | 서울변회 “외감법 개정안 발의 환영… 국회 조속한 통과 필요” - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5MdnZCcEdDV09IaWw1VTFJcGVzMlUwMjl5X0V1cm5FMUF6V1VTSnhVZkRZS0NOS2NnUmRlOWtmNTN2Ql9pX3g5RUJRMjhFVlRlcURfbGRNbTF1NlRZdGRaSDV6M2d2MVJlMjl6TXY0MA?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | 머니투데이 | 국내 기업 83% "신외감법 도입 효과…회계 투명성 개선 체감한다" - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9UMncyMC1pU3F2dUoyVUk4YTV5dWVfanIxOTdEcW5IWGtzaUpBLV8xSnZCalJWM1V5aGd2Nl91N0EzcC1nTUhRZU04RUYwVVhMMjZPalNGNkdxTDlhQkY2YVFXSkN2UHl60gFuQVVfeXFMTW9CU0JhTjlHQ0ExcVNUY2xyR01vZ3gwRzlYbFBxRlZINUZyeThmS21IRktHOEN3dkNhUXZTNjZhSE16TGgxdGd3Unk3OHZNQ3hkMlpaSFRGV0JnaUR4VzdQS25xd0dVTHdjQlVKVXc?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | crowe.com | 감사전 재무제표의 제출 시행 안내(외감법, 2013.12.30 개정) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFB3dVdRS2NNTTdZdXQwam9iZ2JmU1ZBcENOMGhER2c1ajh3WWZtZUUtdjg5ckdaZVdJRlNGc1RycGQ4NHBjdHMyOFd6QThCMDRqNkxjd2d4RS0?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | biz.chosun.com | 엇갈리는 신외감법 실효성 평가…“새 정부서 손질해야” - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUzFjNFNPUnBrT3ZjNGFtbDBKVVlQcHFna0puQUZIemxRQ013Z2tNUkRZQW9NQTA4WHhQZlMxYkZ6TmxWb2d4YVg1czBBcWtxTTNmcG52c1d2NDE4TVh1Uy0zekg1YV9mdTVDWDNKc3JyUjFBejlwQUVBWVdIY3pKMkp5ZksxS1ll0gGcAUFVX3lxTFBsa3BrTDBrZTlYWHZjZG1QVk1yRDBDRVFvTU8zbkdqYUppaGcwRmc1Vy1XSDlXRWRxX3RPcnhwSEdoVlNMVTBGMjQzZkxQSmxRdkliNFpiMGNOcHVqN1hzbjFPc0dCTDBCbkJoazEyZHhqRTBzTnd5U0E3cDc4cTlkNnVkTzd5UmppbXlYQ1FaODVmMEZEUTdieWdwYg?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |

## excluded:no_regulatory_signal (37건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | KEMI, 지속가능경영·동반성장 우수기업 9곳 선정 | https://www.esgeconomy.com/news/articleView.html?idxno=17378 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | etnews.com | 에이피알, 국내외 ESG평가서 지속가능경영 역량 입증 | https://www.etnews.com/20261115000039 |  |
| esg | cnbizm.com | 백화점 업계, 상생·지속가능경영 성과 결실 | https://www.cnbizm.com/news/articleView.html?idxno=321436 |  |
| esg | ajunews.com | ESG경영개발원, 지속가능경영·동반성장 우수 기업·공공기관 선정 | https://www.ajunews.com/view/20261113135722843 |  |
| esg | dailysmart.co.kr | "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... | http://www.dailysmart.co.kr/news/articleView.html?idxno=132423 |  |
| esg | gukjenews.com | 청주상의·대한상의, ESG 공시제도 설명회…도내 20개 기업 실무지원 | https://www.gukjenews.com/news/articleView.html?idxno=3750075 |  |
| esg | sateconomy.co.kr | ESG 공시, '작성'보다 '증명'으로…기업가치 가르는 이행능력 | https://sateconomy.co.kr/news/view/1065574204012569 |  |
| esg | cc.newdaily.co.kr | 대전상공회의소, 국내 ESG 공시제도·공급망 규제 설명회 열어 | https://cc.newdaily.co.kr/site/data/html/2026/11/10/2026111000377.html |  |
| esg | etoday.co.kr | AI로 들춰낸 친환경 기업의 민낯⋯ESG 공시 44%는 ‘그린워싱 고위험’ | https://www.etoday.co.kr/news/view/2646387 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | 머니투데이 | "이런 회사는 거들떠보지도 마세요"…회계사가 경고한 재무제표 신호 \| 이대훈 회계사 - 머니투데이 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5JTkZueGtnejVfQkg5QkxUclVDUm8wVkRrVW9wamxneXp6R0lxdE9iRkpGell6N1dnTnhhTF91UlVlZ1EzQ3pIZl94MGZSbUhDcTVF?oc=5 |  |
| kifrs | 한국경제 | 스벅·메가 사이서 버틸 수 있나…“사라질 커피 브랜드, 숫자는 알고 있다” [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9qRldRTGs4OGVtMnRWRnNrdWE2TGxBQmh3eXZGQ2I0SDAtMzFoM1Z0dHMwb0wtb1lnRi1TRlU0aFd5alYzeUZIanpBdEkyS0Z1ellKcmZma3ZfZXdZc2dpU2dua0paZ0NLRHNRVQ?oc=5 |  |
| kifrs | vietnam.vn | 기후 변화는 기업의 재무제표에 직접적인 영향을 미칩니다. - Vietnam.vn | https://news.google.com/rss/articles/CBMimAFBVV95cUxPV2hpcHlnX2FQUWFUWnFIYmJWcDhiUGFCSXJPWWRVblJaQnNmZUVLVzcyLUp5N1hpckhVU2NnU0JUeFY5Zi1zRkdIR2dhTjZyeXFEalgxX3pDeTVBcEJQbVhiS2J6U2cxa3YtaWctRERwRUZfVXFrMm5sSWVBWnlpMlk5Vy1wU2NGOFR0OXNmTXF3UDZ6Ri0yUw?oc=5 |  |
| kifrs | cfnews.kr | [李玄崗의 泮中雜詠] 2025년 7월 감정 결과가 어떻게 2024년 재무제표에?... 성균관 회계 조작의 ‘결정적 물증’ - 유교신문 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1UUTU0NldQWmRmdS10NlZ1NEdhMTdmWC02Vlc2blRuZmVBLTVROXRBQ1VjWk9PcWJzbjI5bVJ4MmNySWVWNUNiRmx1VVRXS2tVT1ZXR29laWV6ZGEzRHVVdw?oc=5 |  |
| kifrs | newstnt.com | 진성범 충남도의회, 충남개발공사 회계처리 부적정 및 내부통제 미흡 문제 질타 - 뉴스티앤티 | https://news.google.com/rss/articles/CBMiakFVX3lxTFB3VFRoNVFSVnFSV0Uwb05nNHp4M0dvVEt2S29JaXIzSGpudTgwQzg4RGp6S1VaWERFMWp3QnRmQnZBMUJmejljc19SVkRMS0VJX1B6NlBmZ1NWYloweTJPc0s5LUZSU3RVeHc?oc=5 |  |
| kifrs | yna.co.kr | '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - 연합뉴스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE01b2lZLWNOMXlZYjFhcXJISHY2UW5oVV91UTRLZEFVaEVTSDJrREZETnl2VHdac1dRMkJBOFUyUXRTMm1HZDRBQk93ajlzYUdDNTAtMWx0UEwycm45XzlCQtIBYEFVX3lxTE01b2lZLWNOMXlZYjFhcXJISHY2UW5oVV91UTRLZEFVaEVTSDJrREZETnl2VHdac1dRMkJBOFUyUXRTMm1HZDRBQk93ajlzYUdDNTAtMWx0UEwycm45XzlCQg?oc=5 |  |
| kifrs | news.bizwatch.co.kr | 상장사 회계감리 20년에 한 번꼴...이찬진 금감원장 "획기적으로 줄일 것" - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE05dWV0Ul9JcGNYOFN2b1drODJqNzNLNnRfMGNXYngzODk3d0I0eS10dTJJWHZ1VEZzZDRqRDRVOXFOM3M4RGFaRnlURGV0c3NwZDFsMnIxZUQ4U0RKMVVTZ2tlUjBBbHZPeFE?oc=5 |  |
| kifrs | kbthink.com | 금감원, 정원 200명 증원 추진…IT검사국 추가·민생특사경 신설 - KB Think | https://news.google.com/rss/articles/CBMickFVX3lxTE1aTFJHUnBwTjZ5eGNoZjlWRDd0R2pBTkVtb0JWRF9KY185U2M0b0g5bVhfTDhxMnhnR3JFY01pVTNWNXB3NGNJSzJwY0RhSkdvdlF6VG13bGV1V0RwOHhJWmNuRkV2M29YUkhLbk81cTVTdw?oc=5 |  |
| kifrs | mydaily.co.kr | [MD포커스] ‘순손실 감수’ KB증권, ‘행정소송 예고’ 메리츠증권…담합 과징금 대응 온도차 - 마이데일리 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9UWHVua0E1dERvRXRKMFUwUTJ0SGlJWXJnUG5qOUs4aDBjanlkSUFUSnlEdUFXU2hRODB0OHlCT1pYdEJSQnJIOGpzZExrNkxNUTZEb3BTYnkzZlg4aGpWUw?oc=5 |  |
| kifrs | digitaltoday.co.kr | 덕산테코피아, 상환전환우선주 파생상품 평가손실 53억 발생 - 디지털투데이 | https://news.google.com/rss/articles/CBMie0FVX3lxTE9DMmJWQ3lFVi1GaWtIYVVFOGU4bVVUNEduV1pKRm15clNwdi14dm1BaU9VYW9Pb3pabC1OelNkZWxwN283X0xWWHZZcWRydkk1QjNnaks4X2dVZDdrNlRmWkpoZDRvVDIwblR6U2dJSHpEOHk1ZlE0YzlqTQ?oc=5 |  |
| kifrs | leadeconomy.co.kr | 코리안리 3분기 영업이익 60% 급감…"환율 효과 제외하면 매출 감소" - 리드경제 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBCYlFSS0Z5bC1ZaXdFMzkxeTZKb1NzYVNFaTBDUVBtbmN5YTk1X2x4QUgzS2VNbFF1dDVLZ3VuVldzZ0dmQklVUjRhZnhUZ3B3RTJaUllSREQyaVMzazN0VjJSLVliaGtlX2ZGa1RrbXQ?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| tax | kgnews.co.kr | 경기도 지방세제 개편 6개 법안 발의…‘14조 확충’ 기대 현실화될까 | https://www.kgnews.co.kr/news/article.html?no=918123 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| icfr | energy-news.co.kr | AI 감사기법 공유로 내부통제 취약점 함께 살핀다 - 에너지신문 | https://news.google.com/rss/articles/CBMickFVX3lxTFBNS0FiQnhzTkhVZXhyQVhfLVc3ZlhDYXc5TE11aGhYYXZBc2tRTF9peHVoOXZwS2Nvb1ZCM24xQ0lBY2lpTEg1WGxDNzlXb00ydTZDMkswYlNVVjdSRzJ2ajE5WElaaEFhT0RnNHJuN05wUQ?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |

## excluded:opinion_piece (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | joongang.co.kr | [사설] ESG 공시 의무화…기업에 부담 떠안겨선 안 된다 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1hOUU4ajk1NHRSRnpIR2FqQ3FvWjNqOEJFc2kzZW40bjljbzVTdGg5d29zNkpQcTQtSWRMVkhsXzc0V1RWc1VsRWllN000NmtwS0NHT1Vn?oc=5 |  |
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:reader_content (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | 'KSSB 공시 의무화 시대, 무엇을 준비해야 하나' 세미나 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE81V1p4YkEyeGp6aWFCY2lCYmcxVXNZYm5ZWEJrV21QR0NOSjZfMFN0RWgza3otTFR4ZjZzTnBoQU9sWkw5SDFkSS05bkRQUXBxY0l2LTVQaW5QbWFOR2FWcUZWVE1oSlpNR193ZQ?oc=5 | event |

## excluded:related_news_attached (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 관련 보도로 붙음: 2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요 |

## excluded:similar_news_merged (17건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 머니투데이 | 코스피 상장사 5곳중 1곳, ESG 공시 준비 안 됐다 | https://www.mt.co.kr/stock/2026/11/11/2026111019562387265 | → 대표: ESG 공시 의무화 코앞인데…대형 상장사 5곳 중 1곳 '보고서 無' |
| esg | ziksir.com | KB금융, 한국ESG기준원 평가 통합 A+ 획득…지속가능경영 성과 인정 | https://www.ziksir.com/news/articleView.html?idxno=153110 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | weekly.hankooki.com | 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 | https://weekly.hankooki.com/news/articleView.html?idxno=7193568 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | fashionbiz.co.kr | 신세계백화점, ESG 평가 2년 연속 A+... 지속가능경영 성과 | https://www.fashionbiz.co.kr/article/231039 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | businessplus.kr | 신세계百, 2년 연속 ESG평가 'A+' 획득…"지속가능경영 결실 맺어" | https://www.businessplus.kr/news/articleView.html?idxno=119709 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | efnews.co.kr | 현대로템, ESG 종합평가 3년 연속 'A+'…지속가능경영 성과 인정 | http://www.efnews.co.kr/news/articleView.html?idxno=133916 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | cstimes.com | 현대로템, KCGS ESG 평가 3년 연속 통합 A+ 획득…지속가능경영 성과 입... | https://www.cstimes.com/news/articleView.html?idxno=727670 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | joongangenews.com | [ESG] 현대로템, ESG 평가 3년 연속 A+ 등급...지속가능경영 성과 인정 | https://www.joongangenews.com/news/articleView.html?idxno=563186 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | globalepic.co.kr | KB금융, 한국ESG기준원 평가서 통합 'A+ 등급'…지속가능경영 리더십 입... | https://www.globalepic.co.kr/view.php?ud=2026111210164730997cc35ccc5c_29 | → 대표: "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... |
| esg | thefairnews.co.kr | KB금융, KCGS ESG 평가서 최고 등급 'A+'…지속가능경영 리더십 입증 | https://www.thefairnews.co.kr/news/articleView.html?idxno=93912 | → 대표: KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 |
| kifrs | 파이낸셜뉴스 | 삼성전자 부사장, '글로벌 회계기준 제정'에 참여…韓 기업 목소리 커진... | https://www.fnnews.com/news/202611061034591232 | → 대표: 국제 회계기준 개정에 韓 목소리↑…자문기구에 삼성 부사장 합류 |
| kifrs | newsis.com | 휴온스, 3분기 매출액 1440억…전년대비 6% 감소 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9XaV93VEFWLVowa2VTYTVkYUZKcm1oVHRqLW9jMXhmbjRiVUhnNGtoVG1CTGR5R2JhR1BaTkNlMDZ3UDNlWElpYnRkVnlRUFo3bUF6bEpXcDNEVzA5dTg3MdIBeEFVX3lxTE5hMGlmSWlqR3BJNTRtOFR2aHNvQ2VHeEJjdnJDbHY4enplazhocUlLZ3psZlFqSVNteEJ5VFI2THdPU282empaekVFbEVHUlRWTzRnaE5wbWxOQ0JDQlhMa3hGbms3dlF3X2ZwM2hjV2tORG01dnYyOQ?oc=5 | → 대표: 코리안리 3분기 영업이익 60% 급감…"환율 효과 제외하면 매출 감소" - 리드경제 |
| kifrs | leadeconomy.co.kr | 네이버 3분기 영업이익 40% 급감…매출은 7.7% 증가 - 리드경제 | https://news.google.com/rss/articles/CBMicEFVX3lxTE8wVlRpZEZ6NE5xS05Rc1AyZDBVUUFkZTJQbWNDRnktMmlEVWk0UzJSdks4OVhzdVRiSzlNV3p1Qi03RDZFYjNDQThjY3Z0ckJSR19XU205V1FDWk9LeHZrRTRkc0ZSb3ZPTWZJNUdZOE4?oc=5 | → 대표: 코리안리 3분기 영업이익 60% 급감…"환율 효과 제외하면 매출 감소" - 리드경제 |
| kifrs | newsis.com | [속보]크래프톤, 3분기 영업이익 2250억…전년 대비 35.5%↓ - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9zSXI2R2xLNGhQQUFUQWJCbGtqN1lQWFB2bnhaYmhLbDJRNG9VX0UwS0dkbnI1QkI0dUdiekdnZFpsOGFYMkNLdnlvUUpXMnVDUFBmUU1WcXlyRlFGUTNWZNIBeEFVX3lxTE03V0Z6QUt2WDRoSkxET3ZrTktVdEdJV055U2YtMGRHUk96c2t0c3BycElNcmlHTDNIaGN4NGlGWjcwR0J2b2ZaM1R0MlFSd0pvVzdrVnhfRFFNSUpWRmFqcGFxajlwdVBNS0NoU3dUTWUyOWNmdU5CUQ?oc=5 | → 대표: 코리안리 3분기 영업이익 60% 급감…"환율 효과 제외하면 매출 감소" - 리드경제 |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## excluded:standard_setter_governance (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국회계기준원 | 2026년 제9회 지속가능성기준위원회(IFRS 재단 정관 개정 공개초안에 대한 검토의견) | https://www.kasb.or.kr/front/board/calViewA.do?seq=1133 |  |

## collect:event_announcement (18건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융감독원 | 금융소비자 중심의 금융감독 실현을 위한 제5차 금융소비자보호자문위원회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249855&menuNo=200218 |  |
|  | 금융감독원 | 제1회 퇴직연금 장기투자 캠페인 출범식 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249713&menuNo=200218 |  |
|  | 금융감독원 | 자동 가입되는 시민안전보험, 보험금 청구까지 꼭 챙기세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249656&menuNo=200218 |  |
|  | 금융감독원 | 2026년 제49회 보험계리사 및 손해사정사 최종 합격자 발표 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229239&menuNo=200218 |  |
|  | 금융감독원 | 의료기관 부당청구 방지 및 보험사기 근절을 위한금융감독원-건강보험심사평가원 간 업무협약 체결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228833&menuNo=200218 |  |
|  | 금융감독원 | 금융위원회, 제5차 금융업권 생산적 금융협의체 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228598&menuNo=200218 |  |
|  | 금융감독원 | 금감원, 보험회사 성과평가 관행 개선 워크숍 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227573&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 제4차 소비자위험대응협의회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226953&menuNo=200218 |  |
|  | 금융감독원 | 보다 다양한 금융회사들이 AI 보안위협에 철저히 대비할 수 있도록 제2차 망분리 규제 긴급 완화 조치를 추진합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226501&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 이화여대와 공동으로 Future Climate Finance in the era of Green Transition 국제 컨퍼런스 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226303&menuNo=200218 |  |
|  | 금융감독원 | 2026년도 제61회 공인회계사시험최종 합격자 1,150명 발표 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226144&menuNo=200218 |  |
|  | 금융감독원 | 금융소비자 중심의 금융감독 실현을 위한 제4차 금융소비자보호자문위원회 회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225621&menuNo=200218 |  |
|  | 금융감독원 | 제10차 지정대리인 심사위원회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225188&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 이화여대와 공동으로 금융권 기후 리스크 관리 관련 국제 컨퍼런스 개최 예정 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223234&menuNo=200218 |  |
|  | 재정경제부 | 제18회 국제금융기구 채용설명회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079925&menuNo=4010100 |  |
|  | 재정경제부 | 제3차 글로벌 핵심 투자자 협의체 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079922&menuNo=4010100 |  |
| esg | biz.chosun.com | 스틱인베스트먼트, KEMI 어워즈서 지속가능경영보고서 우수상 받아 | https://biz.chosun.com/stock/stock_general/2026/11/12/CVYPKCKY6BBB5JDDU6O63T4ODA/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| esg | newstopkorea.com | '최우수 ESG PE' 스틱인베, 지속가능경영보고서 부문 우수상 쾌거 | https://www.newstopkorea.com/news/articleView.html?idxno=49003 |  |

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

## collect:no_category (267건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융감독원 | 금년 세무사시험 수석합격자(한OO씨)의 CPA시험 부정행위 언급과 관련하여 안내드립니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249859&menuNo=200218 |  |
|  | 금융감독원 | 불법사금융 원스톱 지원, 이제 센터 방문 없이도 신청 가능합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249857&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 2026 세계투자자주간 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249856&menuNo=200218 |  |
|  | 금융감독원 | 신뢰받는 자본시장, 현장에서 묻고 답을 찾다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249834&menuNo=200218 |  |
|  | 금융감독원 | 26년도 상반기 기술금융 테크평가 및 품질심사평가 결과 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249830&menuNo=200218 |  |
|  | 금융감독원 | 가상자산사업자에 대한 최고 수준의 보안 강화 조치를 통해 이용자의 자산과 정보를 철저히 지켜나가겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249825&menuNo=200218 |  |
|  | 금융감독원 | 증권사 발행어음, IMA 부문 C-level 임원 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249824&menuNo=200218 |  |
|  | 금융감독원 | 인터넷, SNS상 코스닥 추가대책에 대한 허위정보 관련 투자자 유의사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249822&menuNo=200218 |  |
|  | 금융감독원 | 누가 내 신분증과 위임장을 들고 주민센터에 왔다고요 100% 보이스피싱 사기입니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249820&menuNo=200218 |  |
|  | 금융감독원 | 미공개 무상증자정보를 이용한 내부자등에 대한 중대범죄수사청 고발,통보 조치의결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249817&menuNo=200218 |  |
|  | 금융감독원 | 금융회사 지배구조의 공정성과 투명성을 제고합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249815&menuNo=200218 |  |
|  | 금융감독원 | 26.6월말 금융복합기업집단 자본적정성 비율 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249814&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사,감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249812&menuNo=200218 |  |
|  | 금융감독원 | 건설노동자, 플랫폼노동자와 프리랜서에 대한 포용금융으로 금융이용 문턱 낮아진다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249806&menuNo=200218 |  |
|  | 금융감독원 | 2026년 10월 가계대출 동향(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249804&menuNo=200218 |  |
|  | 금융감독원 | 증권사의 '주식정보 제공서비스' 이용시 숨어있는 이용료를 미리 확인하고 이용하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249801&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 부동산신탁사 임원 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249795&menuNo=200218 |  |
|  | 금융감독원 | 이찬진 금융감독원장, 회계법인CEO 및 전문가 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249790&menuNo=200218 |  |
|  | 금융감독원 | 보이스피싱 피해로 멈춘 일상, 금융권이 '다시, 일상으로' 이어드립니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249776&menuNo=200218 |  |
|  | 금융감독원 | 상장사 대상 '2026년도 찾아가는 불공정거래 예방교육' 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249775&menuNo=200218 |  |
|  | 금융감독원 | 증시 변동성 완화를 위한 신용공여 담보비율 유지의무 면제조치 시행 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249770&menuNo=200218 |  |
|  | 금융감독원 | 군장병 대상 금융교육강사 양성 연수를 실시합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249769&menuNo=200218 |  |
|  | 금융감독원 | 정부와 퇴직연금사업자가 함께 안정성과 수익성을 갖춘 퇴직연금 생태계를 만들어 나가겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249765&menuNo=200218 |  |
|  | 금융감독원 | 국내외 주식시장 변동성 확대로 단계별 대응조치 가동 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249759&menuNo=200218 |  |
|  | 금융감독원 | 금융권은 개인정보 유출 사고에 따른 보이스피싱 예방에 총력 대응하고 있습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249758&menuNo=200218 |  |
|  | 금융감독원 | 포용금융, 이제 차주의 체감성과도 살펴보겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249746&menuNo=200218 |  |
|  | 금융감독원 | AI시대, 거세지는 침해위협에 맞서 全 금융권이 튼튼한 보안체계로 무장하도록 혁신적인 정책과제를 적극 추진하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249742&menuNo=200218 |  |
|  | 금융감독원 | 홍콩 H지수 ELS 관련 은행, 증권사 검사 결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249736&menuNo=200218 |  |
|  | 금융감독원 | 계리가정보고서 도입 등 보험업감독규정 개정안 금융위원회 의결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249734&menuNo=200218 |  |
|  | 금융감독원 | 베트남, 인도네시아 보험감독당국 초청 세미나 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249719&menuNo=200218 |  |
|  | 금융감독원 | 금감원장, 임원회의(11.3.) 당부사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249709&menuNo=200218 |  |
|  | 금융감독원 | 코너스톤투자자 제도 등 도입 관련 자본시장법 시행령 개정안 국무회의 의결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249707&menuNo=200218 |  |
|  | 금융감독원 | 글로벌 해킹 위협에 대비한 국내 가상자산사업자의 사고대응력 제고를 위해 긴밀하고 신속하게 대응해 나가겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249686&menuNo=200218 |  |
|  | 금융감독원 | 생산적 금융의 온기를 지방과 중소기업까지 이어갑니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249682&menuNo=200218 |  |
|  | 금융감독원 | 사회초년생 청년 운전자가 자동차보험 할인혜택을 쉽게 받을 수 있도록 가입 절차를 개선합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249670&menuNo=200218 |  |
|  | 금융감독원 | 2026년 9월 외국인 증권투자 동향 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=248185&menuNo=200218 |  |
|  | 금융감독원 | 보험회사 계리담당 부서장 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247849&menuNo=200218 |  |
|  | 금융감독원 | "금융회사의 부실 확산에 신속, 선제적으로 대응하여 금융시장의 안정 및 소비자 보호를 위한 「금융회사 신속정리제도」 도입을 추진합니다." | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247688&menuNo=200218 |  |
|  | 금융감독원 | 보험사기 연루 보험업종사자에 대한 등록취소, 업무정지 등 제재 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247619&menuNo=200218 |  |
|  | 금융감독원 | 퇴직연금 기능강화를 위한 노사정 합의로 노동자의 든든한 노후소득 보장체계 구축 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247600&menuNo=200218 |  |
|  | 금융감독원 | 26년 3분기 등록 ABS 발행 실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247561&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사, 감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247035&menuNo=200218 |  |
|  | 금융감독원 | 미공개중요정보를 이용한 내부자등에 대한 중대범죄수사청 고발, 통보 등 조치(2건) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=247026&menuNo=200218 |  |
|  | 금융감독원 | 빗썸 등 주요 가상자산사업자들에 대한 해킹사고에 대해 긴밀하고 신속하게 대응하고 있습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=246843&menuNo=200218 |  |
|  | 금융감독원 | 포용금융이 금융권에 뿌리내리도록 평가체계를 도입하고, 공공부문이 앞장서서 부실채권 관리체계를 개편하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=246792&menuNo=200218 |  |
|  | 금융감독원 | 금융회사 민원, 분쟁업무 모범관행 설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=246791&menuNo=200218 |  |
|  | 금융감독원 | 건전한 경쟁질서 확립 및 투자자 피해 예방을 위해 증권업계 이벤트 실시 기준을 대폭 강화합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=246528&menuNo=200218 |  |
|  | 금융감독원 | 이찬진 금융감독원장, 은행지주 이사회 의장 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=246237&menuNo=200218 |  |
|  | 금융감독원 | 일본계 자본의 JYP 주식 공개매수 보도 관련 투자자 유의사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=245702&menuNo=200218 |  |
|  | 금융감독원 | 투자한도 100%는 상품의 원리금 보장성 표시가 아닙니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=245254&menuNo=200218 |  |
|  | 금융감독원 | 증권업계 신용융자 자율관리 강화를 위한 증권사 CRO 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=244991&menuNo=200218 |  |
|  | 금융감독원 | 26.9월중 기업의 직접금융 조달실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=244915&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원이 발급한 무효확인서를 토대로 최초 형사 무죄 판결이 확정되었습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=244231&menuNo=200218 |  |
|  | 금융감독원 | 간호조무사 대상 보험사기 예방교육 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243965&menuNo=200218 |  |
|  | 금융감독원 | 고수익 아르바이트와 통장매매의 유혹! 나도 모르게 금융사기 범죄자가 될 수 있습니다! | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243940&menuNo=200218 |  |
|  | 금융감독원 | 민, 관 합동으로 「지표금리 개편방안(3.30일)」을 차질 없이 추진하고 있습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243717&menuNo=200218 |  |
|  | 금융감독원 | 꼬리 자르기 사채 조직, 몸통까지 쫓는다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243716&menuNo=200218 |  |
|  | 금융감독원 | 여신전문금융업감독규정 개정안 규정변경예고(‘26.10.23.~12.2.) 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243352&menuNo=200218 |  |
|  | 금융감독원 | 26.8월말 국내은행의 원화대출 연체율 현황(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243351&menuNo=200218 |  |
|  | 금융감독원 | 유명 가상자산거래소의 블록체인 네트워크를 사칭한 가짜 체인 사기에 주의하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243282&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사,감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243274&menuNo=200218 |  |
|  | 금융감독원 | 보증금 기반 비대면 신용카드 발급 서비스 등 혁신금융서비스 4건 신규 지정 의결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243112&menuNo=200218 |  |
|  | 금융감독원 | 신용정보법 과징금 부과의 예측 가능성을 한층 높였습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243111&menuNo=200218 |  |
|  | 금융감독원 | 군 장병의 경제관 확립과 금융역량 향상을 위해 국방(부)과 금융(위)이 손을 맞잡다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243107&menuNo=200218 |  |
|  | 금융감독원 | 안정적인 노후생활을 위한 소비자 유의사항 안내 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=243106&menuNo=200218 |  |
|  | 금융감독원 | 2027 사업연도 주기적 지정 등 감사인 지정결과 사전통지 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=242077&menuNo=200218 |  |
|  | 금융감독원 | 한국, IOSCO(국제증권감독기구) 주관 글로벌 투자자보호 AI 프로그램 개발 경진대회 본선 입상 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=242050&menuNo=200218 |  |
|  | 금융감독원 | ‘무기한 선물’ 이용자 유의사항 안내 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241777&menuNo=200218 |  |
|  | 금융감독원 | 「유관기관 증시상황 긴급 점검회의」 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241719&menuNo=200218 |  |
|  | 금융감독원 | 2026년 9월 가계대출 동향(잠정) 및 「가계부채 점검회의」 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241690&menuNo=200218 |  |
|  | 금융감독원 | 잠든 선불충전금, 잊지 말고 사용하세요. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241689&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사, 감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241512&menuNo=200218 |  |
|  | 금융감독원 | 금융권 침해사고 재발방지를 위해 금융보안 관리체계를 전면 강화하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241503&menuNo=200218 |  |
|  | 금융감독원 | 증권사의 영업점 개설 계좌와 관련한 매매수수료 차등 부과 관행을 바로 잡겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241493&menuNo=200218 |  |
|  | 금융감독원 | 금감원, 중소금융업권과 함께 준법제보 활성화 방안을 마련하여 시행합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241492&menuNo=200218 |  |
|  | 금융감독원 | 바젤은행감독위원회의 단순기본자본비율 규제이행평가(RCAP) 결과 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=241461&menuNo=200218 |  |
|  | 금융감독원 | 부동산 프로젝트 금융(PF) 상황 점검회의 겸 주택공급 촉진을 위한 금융지원 대책 점검회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=240529&menuNo=200218 |  |
|  | 금융감독원 | 투자자들이 공시정보를 손쉽게 분석, 활용할 수 있도록 Open DART 개선 및 XBRL 택사노미 정비를 추진합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=240528&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, PEF 운용사에 대한 내부통제 점검 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=239804&menuNo=200218 |  |
|  | 금융감독원 | 금융권의 소멸시효 연장 관행을 개선하기 위해 조건부 대손인정제도가 시행됩니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=239722&menuNo=200218 |  |
|  | 금융감독원 | 금융분쟁조정위원회, 예금부당해지에 따른 금융회사에 대한 책임 인정 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=238317&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 금융지주회사 경영실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=238310&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사,감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=238152&menuNo=200218 |  |
|  | 금융감독원 | "개인간 중고거래 신용카드 안전결제 서비스" 등 혁신금융서비스 24건 신규 지정 의결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=238150&menuNo=200218 |  |
|  | 금융감독원 | 투자자 중심 내부감사기능 강화를 위한 증권사 감사 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=238097&menuNo=200218 |  |
|  | 금융감독원 | 최근 금융권 개인정보 유출사고에 따른 보이스피싱, 스미싱 등 피해에 주의하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=237928&menuNo=200218 |  |
|  | 금융감독원 | 취업준비생의 자산관리 역량 향상과 금융사기 피해 예방을 위한 2026년 청년 금융특강을 실시합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=237663&menuNo=200218 |  |
|  | 금융감독원 | 전환하고 싶어요 한 마디면 보험료가 할인됩니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=237413&menuNo=200218 |  |
|  | 금융감독원 | 全금융권이 비상한 경각심을 갖고 침해위협에 대응해 나가겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=236976&menuNo=200218 |  |
|  | 금융감독원 | 최근 발생하는 금융권 침해위협에 면밀히 대응해 나가겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=234804&menuNo=200218 |  |
|  | 금융감독원 | 불법사금융 근절을 위한 4대 추가 제도 개선 추진 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=234367&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 신설 사모운용사 CEO 대상 설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=234345&menuNo=200218 |  |
|  | 금융감독원 | 노인의 날을 맞아 금감원-금융권 공동 고령층 집중 금융교육을 실시합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=234294&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 파생결합증권, 사채 발행, 운용 현황 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=234293&menuNo=200218 |  |
|  | 금융감독원 | 26년 상반기 가상자산사업자 실태조사 결과 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=233627&menuNo=200218 |  |
|  | 금융감독원 | 대형 IB의 모험자본 공급 현황을 점검하고 리서치보고서의 독립성, 신뢰성 제고 및 중소형주 커버리지 확대 방안을 마련하였습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=233557&menuNo=200218 |  |
|  | 금융감독원 | 보험상품 방송광고 건전화를 위한 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=233554&menuNo=200218 |  |
|  | 금융감독원 | 금융시장 상황점검회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=233555&menuNo=200218 |  |
|  | 금융감독원 | 법인 대표이사의 시세조종행위 등 불공정거래 행위에 대한 적발 조치(3건) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232881&menuNo=200218 |  |
|  | 금융감독원 | 범 금융권, 유관기관과 함께 「사회진출前 금융소양교육」을 전면 실시합니다! | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232662&menuNo=200218 |  |
|  | 금융감독원 | 주요 민원사례로 알아보는 금융채권추심 관련 소비자 유의사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232661&menuNo=200218 |  |
|  | 금융감독원 | 의료계,플랫폼 협력으로 “실손24” 연계율 제고 나선다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232597&menuNo=200218 |  |
|  | 금융감독원 | 26.8월중 기업의 직접금융 조달실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232572&menuNo=200218 |  |
|  | 금융감독원 | 이찬진 금융감독원장, 증권회사 CEO 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232288&menuNo=200218 |  |
|  | 금융감독원 | 취약계층 보호 및 금융소비자 편의 제고를 위해 은행권 최저생계비 조회용 계좌통합조회서비스를 시행합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232271&menuNo=200218 |  |
|  | 금융감독원 | 합동대응단은 명문대 경영동아리 출신 정보카르텔을 적발하여 압수수색을 실시하고 혐의자 재산을 동결하였습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232253&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 금융민원 접수 및 처리 동향 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=232216&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 보험사기 적발현황 및 대응방안 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=231823&menuNo=200218 |  |
|  | 금융감독원 | 휴면자산 환급실적 등을 공개하고 금융회사의 휴면자산 관리체계를 강화합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=231822&menuNo=200218 |  |
|  | 금융감독원 | 금융소비자 보호에 관한 감독규정 개정안 규정변경예고 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=231802&menuNo=200218 |  |
|  | 금융감독원 | 이찬진 금융감독원장, 여명학교 북향민 청소년 대상 특강 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=231785&menuNo=200218 |  |
|  | 금융감독원 | 가상자산시장 불공정거래 혐의자 수사기관 고발,통보 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230579&menuNo=200218 |  |
|  | 금융감독원 | 기업의 가치를 보다 정확히 보여주기 위해 기업의 토지 공시지가가 주석에 공시됩니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230578&menuNo=200218 |  |
|  | 금융감독원 | 메리츠증권(주)에 대한 종합금융투자사업자 지정 및 단기금융업 인가 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230566&menuNo=200218 |  |
|  | 금융감독원 | 신라자산운용(주) 및 제니스투자자문(주)에 대한 금융투자업 인가(등록) 취소 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230565&menuNo=200218 |  |
|  | 금융감독원 | 이찬진 금융감독원장, 은행지주회장 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230549&menuNo=200218 |  |
|  | 금융감독원 | 해외 카드결제 취소시 환율 하락으로 발생하는 소비자 환차손 보상을 한층 강화합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230357&menuNo=200218 |  |
|  | 금융감독원 | 최근 국제분쟁 등으로 변동성, 괴리율이 증가하는 원자재 ETP(ETN, ETF) 투자 시 유의하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230356&menuNo=200218 |  |
|  | 금융감독원 | 온라인투자연계금융업의 포용금융 역할 강화와 신뢰 회복을 지원하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230317&menuNo=200218 |  |
|  | 금융감독원 | '26.7월말 국내은행의 원화대출 연체율 현황[잠정] | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230298&menuNo=200218 |  |
|  | 금융감독원 | 풍성해야 할 한가위, ‘가짜 투자’에 눈물 흘리지 않으려면 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230052&menuNo=200218 |  |
|  | 금융감독원 | 무료 강연, 박람회에서 보험 가입 시 소비자 유의사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230051&menuNo=200218 |  |
|  | 금융감독원 | 투자자 중심 내부통제 강화를 위한 증권사 준법감시인 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230042&menuNo=200218 |  |
|  | 금융감독원 | 주요 민원사례로 알아보는 은행 이용시 소비자 유의사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=230013&menuNo=200218 |  |
|  | 금융감독원 | 추석 명절 전후 보이스피싱 피해에 주의하세요! | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229732&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 금융권과 함께하는 추석맞이 전통시장 나눔 활동 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229241&menuNo=200218 |  |
|  | 금융감독원 | 2026년 8월 외국인 증권투자 동향 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229235&menuNo=200218 |  |
|  | 금융감독원 | 금융소비자보호 성과 대국민 보고대회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229095&menuNo=200218 |  |
|  | 금융감독원 | 금감원, 금융상황 점검회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229066&menuNo=200218 |  |
|  | 금융감독원 | 부실사업장 정상화를 통한 신속한 주택공급 권대영 금융위 부위원장, 캠코펀드 사업장 방문 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=229065&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사, 감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228895&menuNo=200218 |  |
|  | 금융감독원 | 내부자 등 미공개중요정보를 이용한 행위자에 대한 검찰 고발, 통보 및 과징금 부과(4건) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228868&menuNo=200218 |  |
|  | 금융감독원 | PG업권 보안 리스크를 빈틈없이 점검하고 AI 보안위협에도 철저히 대비하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228839&menuNo=200218 |  |
|  | 금융감독원 | 금융권 취업, 어떻게 준비할까 기업이 장애 청년에게 직접 들려준다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228837&menuNo=200218 |  |
|  | 금융감독원 | 26.6월말 기준 보험회사 지급여력비율 현황 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228836&menuNo=200218 |  |
|  | 금융감독원 | 신용정보법 과징금 산정의 투명성과 합리성을 높이도록 하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228834&menuNo=200218 |  |
|  | 금융감독원 | 금감원장, 임원회의(9.15.) 당부사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228620&menuNo=200218 |  |
|  | 금융감독원 | 주택공급 금융지원 프로그램 및 PF 사업장 매각설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228616&menuNo=200218 |  |
|  | 금융감독원 | 보이스피싱으로 인한 카드결제 피해 예방 및 구제를 강화하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228611&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 자동차보험 사업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228597&menuNo=200218 |  |
|  | 금융감독원 | 보험권 소비자보호,보상담당 부서장 확대 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228414&menuNo=200218 |  |
|  | 금융감독원 | 기후금융 협업체계를 강화하여 우리경제 탄소감축과 녹색전환을 충실히 지원하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228399&menuNo=200218 |  |
|  | 금융감독원 | 26년 3분기 혁신금융서비스 지정 정기신청 개시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228070&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 테크파인더 쇼케이스 2026 참가기업 공개모집 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=228069&menuNo=200218 |  |
|  | 금융감독원 | IFRS17 체계下 계리가정 보고서 도입으로 보험부채 평가의 합리성과 신뢰성을 제고하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227769&menuNo=200218 |  |
|  | 금융감독원 | 2026년 2분기 자산운용회사 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227746&menuNo=200218 |  |
|  | 금융감독원 | 금감원장, 금감원-지자체-금융권 공동개최 해외IR 참석 및 영국 금융감독당국 최고위급 등 면담 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227683&menuNo=200218 |  |
|  | 금융감독원 | 2026년 2분기 증권, 선물회사 영업실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227674&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사, 감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227588&menuNo=200218 |  |
|  | 금융감독원 | 삼성증권(주)에 대한 단기금융업 인가 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227563&menuNo=200218 |  |
|  | 금융감독원 | 프런티어 AI 기반 보안위협 대비 강화 등을 위한 전금융권 CISO 간담회 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227558&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 금융업계의 다크패턴 예방을 위한 상시협의체 킥오프 회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227559&menuNo=200218 |  |
|  | 금융감독원 | 공모 목표전환형 펀드 현황 및 투자자 유의사항 안내 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227554&menuNo=200218 |  |
|  | 금융감독원 | 2026년 8월 가계대출 동향(잠정) 및 가계부채 점검회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227555&menuNo=200218 |  |
|  | 금융감독원 | 주택공급 촉진을 위한 금융지원 대책 점검회의 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227556&menuNo=200218 |  |
|  | 금융감독원 | 해외 부동산펀드 등 고위험 펀드의 투자자 보호를 강화하기 위한 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227544&menuNo=200218 |  |
|  | 금융감독원 | 고령층의 금융사기 피해 예방 및 디지털 금융 소외 방지를 위한 FSS 시니어 금융아카데미를 신청하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227394&menuNo=200218 |  |
|  | 금융감독원 | 금융권 보이스피싱 대응역량 제고를 위한 우수사례 포상 추진 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227219&menuNo=200218 |  |
|  | 금융감독원 | 누군가에게 비상장주식 투자 권유를 받고 있다면 회사정보와 투자권유자의 실체를 반드시 확인하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227218&menuNo=200218 |  |
|  | 금융감독원 | 개정 상법 정착 등을 위한 26.3분기 찾아가는 기업공시 설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=227195&menuNo=200218 |  |
|  | 금융감독원 | 사망자 명의의 불법 금융거래, 사망신고 ‘다음 날’부터 즉시 막는다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226954&menuNo=200218 |  |
|  | 금융감독원 | 금융 인허가, 등록 사전협의 절차가 더욱 편리해집니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226952&menuNo=200218 |  |
|  | 금융감독원 | 2026 범금융권 보이스피싱 예방 주간 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226951&menuNo=200218 |  |
|  | 금융감독원 | 금융, 외환, 부동산 등 부문별 리스크 종합 점검 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226661&menuNo=200218 |  |
|  | 금융감독원 | 토큰증권 정책방향 발표 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226659&menuNo=200218 |  |
|  | 금융감독원 | 2024 회계연도 감사전 재무제표 점검결과 및 유의사항 안내 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226487&menuNo=200218 |  |
|  | 금융감독원 | 투자성 상품 가입시간 단축을 위한 가입절차 합리화,간소화 방안 마련 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226486&menuNo=200218 |  |
|  | 금융감독원 | 신속한 주택공급 촉진을 위해 수도권 주거용 PF 사업장의 지연요인을 파악하고 현장 맞춤형 밀착관리를 실시합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226484&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사, 감리결과 조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226359&menuNo=200218 |  |
|  | 금융감독원 | 상장사 IR 담당 임원의 불공정거래 혐의 적발,조치 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226357&menuNo=200218 |  |
|  | 금융감독원 | ‘보이스피싱 근절 종합대책’ 1년, 발생건수 40%,피해액 43% 감소 성과 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226356&menuNo=200218 |  |
|  | 금융감독원 | 26.9.10.부터 자동차보험 치료비 보상 절차가 개편됩니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226318&menuNo=200218 |  |
|  | 금융감독원 | 국민의 건전한 금융 투자 역량을 강화하는 안전한 금융생활 캠페인을 추진합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226317&menuNo=200218 |  |
|  | 금융감독원 | 소상공인의 금융접근성이 높아집니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226307&menuNo=200218 |  |
|  | 금융감독원 | 26.6말 국내은행 부실채권 현황(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226296&menuNo=200218 |  |
|  | 금융감독원 | 금감원장, 임원회의(9.1.) 당부사항 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226145&menuNo=200218 |  |
|  | 금융감독원 | 금융소비자 울리는 허위, 과장광고를 근절하기 위해 금융투자회사 광고 업무절차를 전면 개선합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=226139&menuNo=200218 |  |
|  | 금융감독원 | 軍 복무기간이 자산을 형성하고 금융역량을 키우는 기회가 되도록 지원합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225868&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 토스뱅크와 공동으로 찾아가는 「FSS 어린이 금융스쿨」 병원학교편 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225867&menuNo=200218 |  |
|  | 금융감독원 | 금융소비자보호 성과 대국민 보고대회 개최 예정 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225866&menuNo=200218 |  |
|  | 금융감독원 | 26.6월말 국내은행 BIS기준 자본비율 현황(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225832&menuNo=200218 |  |
|  | 금융감독원 | 불법사채 200만원이 400만원이 될 뻔한 순간, 신고 한 번으로 막을 수 있습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225622&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원 제14기 FSS 대학생 금융교육 봉사단 출범 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225405&menuNo=200218 |  |
|  | 금융감독원 | 주택공급 촉진을 위한 금융,건설업계 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225392&menuNo=200218 |  |
|  | 금융감독원 | 충실한 증권신고서는 신속하게, 부실한 신고서는 엄정하게 심사하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225391&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 저축은행 및 상호금융조합 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225382&menuNo=200218 |  |
|  | 금융감독원 | 감사인 지정제도 온라인 설명회 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225381&menuNo=200218 |  |
|  | 금융감독원 | 26.6월말 보험회사 대출채권 현황 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225383&menuNo=200218 |  |
|  | 금융감독원 | FIU, 자금세탁방지 유관기관 협의회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225288&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 여신전문금융회사 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225267&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 보험회사 경영실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225268&menuNo=200218 |  |
|  | 금융감독원 | 기업에게 알려드립니다 확정급여형(DB) 퇴직연금 이렇게 운용하면 달라집니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225146&menuNo=200218 |  |
|  | 금융감독원 | 지연된 PF 사업장을 청년, 신혼부부 보금자리로 신속하게 공급합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225142&menuNo=200218 |  |
|  | 금융감독원 | 26.7월중 기업의 직접금융 조달실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225136&menuNo=200218 |  |
|  | 금융감독원 | AI 시대 국민의 일상과 생업을 잇는 마이데이터 발전방안을 추진합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224945&menuNo=200218 |  |
|  | 금융감독원 | 소비자 눈높이에 맞는 공모펀드 투자위험 안내를 위하여 펀드 핵심위험 표준안을 도입합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224922&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 자산운용사 의결권 행사, 공시 설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224903&menuNo=200218 |  |
|  | 금융감독원 | 퇴직연금 실물이전 고도화로 소비자 편익을 제고하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224726&menuNo=200218 |  |
|  | 금융감독원 | 제약, 바이오 기업의 공시 서류 작성을 지원하겠습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224713&menuNo=200218 |  |
|  | 금융감독원 | 개명,주민등록번호 변경 시, 금융회사마다 찾아가야 하나요 ‘금융회사 1회 방문’으로 고객 변경정보 연계 추진 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224683&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 국내은행 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224404&menuNo=200218 |  |
|  | 금융감독원 | 2026년 7월 외국인 증권투자 동향 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223983&menuNo=200218 |  |
|  | 금융감독원 | '26.6월말 국내은행의 원화대출 연체율 현황(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223982&menuNo=200218 |  |
|  | 금융감독원 | 수해 피해 가계, 중소기업을 위한 금융지원방안 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223857&menuNo=200218 |  |
|  | 금융감독원 | AI기반 가상자산 불공정거래 시장감시 프로세스 자동화 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223852&menuNo=200218 |  |
|  | 금융감독원 | 금융, 통신, 수사 협업으로 보이스피싱 피해 신고 전에 막는다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223841&menuNo=200218 |  |
|  | 금융감독원 | 「비청산 장외파생상품거래 증거금 교환제도에 대한 가이드라인」 연장 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223828&menuNo=200218 |  |
|  | 금융감독원 | "함께하는 금융, 청년의 미래를 그리다" 「2026 금융권 공동채용 박람회」 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223674&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 2027년도 신입 종합직원(5급) 95명 채용 예정 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=223487&menuNo=200218 |  |
|  | 금융감독원 | 건설회사의 건설계약 관련 우발부채 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=132630&menuNo=200435 |  |
|  | 금융감독원 | 가상자산 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=132533&menuNo=200435 |  |
|  | 금융감독원 | 전기오류수정 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=132530&menuNo=200435 |  |
|  | 금융감독원 | 온실가스 배출권과 배출부채 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36150&menuNo=200435 |  |
|  | 금융감독원 | 개발비 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36149&menuNo=200435 |  |
|  | 금융감독원 | 금융상품(제1109호), 수익(제1115호) 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36147&menuNo=200435 |  |
|  | 금융감독원 | 금융자산 양도 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36146&menuNo=200435 |  |
|  | 금융감독원 | 공정가치 측정 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36145&menuNo=200435 |  |
|  | 금융감독원 | 타 기업에 대한 지분의 공시 관련 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36144&menuNo=200435 |  |
|  | 금융감독원 | 특수관계자거래 주석공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36143&menuNo=200435 |  |
|  | 재정경제부 | 한국 주도로 9개국이 참여하는 글로벌 고신뢰 탄소시장(GVCM) 협력 기반 마련 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079961&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] 2026년 11월 최근 경제동향 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079950&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「월급방위대 TF」 킥오프 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079949&menuNo=4010100 |  |
|  | 재정경제부 | 범부처 민생안정지원단, 청년 취업지원 현장 점검 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079929&menuNo=4010100 |  |
|  | 재정경제부 | 국방분야 혁신제품 최초 지정 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079935&menuNo=4010100 |  |
|  | 재정경제부 | 양극화 대응 TF 총괄반 1차 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079934&menuNo=4010100 |  |
|  | 재정경제부 | 영남권 메가프로젝트 이행 점검 TF 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079927&menuNo=4010100 |  |
|  | 재정경제부 | 비상경제장관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079917&menuNo=4010100 |  |
|  | 금융위원회 | 신진창 금융위원회 부위원장,  씨티그룹 국제부문 총 책임자 면담 | https://www.fsc.go.kr/no010101/88146?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 지역기업과의 동행, 6개 정책금융기관이 현장에서 함께 합니다. | https://www.fsc.go.kr/no010101/88143?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 잠자고 있는 포인트, 지역화폐로 바꿔 골목상권에서 쓴다 | https://www.fsc.go.kr/no010101/88142?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 서울 가격상승폭 둔화·매물 증가…수도권 내년 1분기까지 4만 호 이상 입주 | https://www.fsc.go.kr/no010101/88140?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 신뢰받는 자본시장, 현장에서 묻고 답을 찾다 | https://www.fsc.go.kr/no010101/88139?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 261112(보도참고) 지배구조 개선방안(’11.12일 발표) 관련 설명자료 | https://www.fsc.go.kr/no010101/88138?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ‘26년도 상반기 기술금융 테크평가 및  품질심사평가 결과 | https://www.fsc.go.kr/no010101/88137?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 가상자산사업자에 대한  최고 수준의 보안 강화 조치를 통해 이용자의 자산과 정보를 철저히 지켜나가겠습니다. | https://www.fsc.go.kr/no010101/88133?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 인터넷/SNS상 코스닥 추가대책에 대한  허위정보 관련 투자자 유의사항 | https://www.fsc.go.kr/no010101/88132?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 사업보고서 등에 대한 조사·감리결과 조치 | https://www.fsc.go.kr/no010101/88127?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 「예금자보호법」 일부개정법률안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4188 |  |
|  | 금융위원회 | 「금융산업의 구조개선에 관한 법률」 일부개정법률안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4187 |  |
|  | 금융위원회 | 「한국주택금융공사법 시행령」 일부개정령안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4186 |  |
|  | 금융위원회 | 「여신전문금융업감독규정」 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4185 |  |
|  | 금융위원회 | 「한국산업은행법 시행령」 일부개정령안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4184 |  |
|  | 금융위원회 | ｢전자등록업규정｣ 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4183 |  |
|  | 금융위원회 | 「주식ㆍ사채 등의 전자등록에 관한 법률 시행령」 일부개정령안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4182 |  |
|  | 금융위원회 | ｢증권의 발행 및 공시 등에 관한 규정｣ 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4181 |  |
|  | 금융위원회 | ｢금융투자업규정｣ 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4180 |  |
|  | 금융위원회 | 「자본시장과 금융투자업에 관한 법률 시행령」 일부개정령안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4179 |  |
|  | 금융위원회 | 「신용정보업감독규정」 일부개정고시(안) 규정변경 예고 | https://www.fsc.go.kr/po040301/view?noticeId=4178 |  |
|  | 금융위원회 | ｢은행업감독규정｣ 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4177 |  |
|  | 금융위원회 | ｢금융소비자 보호에 관한 감독규정｣ 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4176 |  |
|  | 금융위원회 | 「자본시장과 금융투자업에 관한 법률 시행규칙」일부개정령안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4175 |  |
|  | 금융위원회 | ｢증권의 발행 및 공시 등에 관한 규정｣ 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4173 |  |
|  | 금융위원회 | ｢자본시장과 금융투자업에 관한 법률 시행령 일부개정령안｣ 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4172 |  |
|  | 금융위원회 | 「보험업감독규정」 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4171 |  |
|  | 금융위원회 | 「자본시장특별사법경찰 집무규칙」일부개정훈령안 행정예고 | https://www.fsc.go.kr/po040301/view?noticeId=4170 |  |
|  | 금융위원회 | 「자본시장조사 업무규정」일부개정고시안 행정예고 | https://www.fsc.go.kr/po040301/view?noticeId=4169 |  |
|  | 금융위원회 | 「단기매매차익 반환 및 불공정거래 조사·신고 등에 관한 규정」일부개정고시안 행정예고 | https://www.fsc.go.kr/po040301/view?noticeId=4168 |  |
|  | 금융위원회 | 「전기통신금융사기 신고포상금에 관한 규정」일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4167 |  |
|  | 금융위원회 | 「전기통신금융사기 피해 방지에 관한 규정」일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4166 |  |
|  | 금융위원회 | 「대부업등 감독규정」 일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4165 |  |
|  | 정책브리핑(금융위원회) | 신진창 금융위원회 부위원장,  씨티그룹 국제부문 총 책임자 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789204&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | '26년도 상반기 기술금융 테크평가 및  품질심사평가 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789090&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 서울 가격상승폭 둔화·매물 증가…수도권 내년 1분기까지 4만 호 이상 입주 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789151&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 261112(보도참고) 지배구조 개선방안('11.12일 발표) 관련 설명자료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789114&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 잠자고 있는 포인트, 지역화폐로 바꿔 골목상권에서 쓴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789173&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 신뢰받는 자본시장, 현장에서 묻고 답을 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789142&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 지역기업과의 동행, 6개 정책금융기관이 현장에서 함께 합니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789179&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |

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
|  | 정책브리핑(산림청) | 부여국유림관리소, 2026년 가을철 산불방지대책본부 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789270&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 부여국유림관리소, 충남 서북권 산림재난 대응총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789268&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 부여국유림관리소, "2026년 산림토목사업장 안전사고 대비 합동 모의훈련 실시" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789266&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 아시아태평양경제협력체(APEC) 최종고위관리회의(CSOM) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789264&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 부여국유림관리소, "하천·계곡 불법시설 정비 및 집중단속" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789263&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 옷 한 벌에 담은 따뜻한 마음, 이주노동자와 함께 나눕니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789260&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 국립공원공단, 겨울철 대설·한파 대비 안전관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789258&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 생활화학제품 정보, 큰 글씨로 보고 휴대폰 카메라로 확인하세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789257&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 하나 된 뜻으로 함께 만드는 화학안전… 제7회 화학안전주간 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789256&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 대규모 전력수요의 합리적 분산을 위한 전력계통영향평가 제도 본격 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789255&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | EDA 소프트웨어 관련 9개 사업자의 부당한 공동행위 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789254&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 「광주 자율주행 실증도시」 본궤도 진입 … 이달 30일 첫 차량 운행 준비 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789253&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 한·인니 통합 해양기술교육센터(KIOTEC), 유네스코 IOC 지역훈련센터(RTC)로 공식 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789252&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해양수산부, 노후선박 교체를 지원하는 연안선박 현대화 펀드 대상자 공모한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789251&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부, 유엔기후변화협약 당사국총회(COP)에서 해양을 통한 기후 위기 대응 방안 공유한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789250&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부, '겨울철 자연 재난 대비 계획' 수립으로 해양수산분야 피해 최소화 한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789249&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부-해양환경공단, 선박 입항신고와 방제증서 발급 업무 '원스톱 서비스' 시작한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789248&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 데이터로 읽는 우리 교육 제18호 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789247&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 의과대학 교육의 새로운 변화, 우수사례 8편 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789246&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-투르크메니스탄 세관상호지원협정 발효 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789245&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 한국 주도로 9개국이 참여하는 글로벌 고신뢰 탄소시장(GVCM) 협력 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789261&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 2026 기후시민회의 최종토론회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789244&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-네팔, 기후변화 공동 대응과 국제감축사업 활성화의 길을 열다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789235&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한중 외교장관 회담 및 만찬 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789234&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 「(약칭) 초광역특구법 관련 원포인트 사회적 대화」제8차 실무협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789233&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관, "본격적인 추위 시작… 겨울철 제설대책 이행 철저" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789232&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 김진아 외교부 2차관, 유엔 정무평화구축국 사무차장 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789231&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)12차 최고가격, 11차 수준으로 동결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789230&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 세계로 향하는 K-Sool, '2026 대한민국 우리술 대축제' 막 올랐다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789229&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | [관계부처 합동] (보도 참고 자료) 구글사 지도 국외 반출 허가 조건이행 결과 협의체 보고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789228&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제8차 평화구축기금 전략대화 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789226&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 민·관이 함께 메가프로젝트 성과확산을 위한  중소기업 역할 강화방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789227&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 제3기 공공디자인위원회 위촉위원 11명에게 위촉장 수여 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789221&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부 장관, 가을철 산불 대비태세 점검… "과학적 재난 대응과 예방에 총력" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789225&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 돔류 업계의 현장 목소리 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789223&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 장관, '코리아 그랜드 페스티벌' 계기 전통시장 소비 활성화에 힘 보태 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789222&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 백령도 소형공항 건설사업,  타당성재조사 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789220&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 연말 김치·배추·무 수출 확대 위해…  민·관 협력 총력전 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789216&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 「제10차 경제안보외교포럼」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789219&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 소나무재선충병 경미지역 집중관리로 청정지역 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789218&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 2026년 제9차 재정투자평가위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789215&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 경북 포항 호미반도 국가해양생태공원 조성 사업 예비타당성조사 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789211&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 정연두 외교전략정보본부장, 제25차 한-유엔 군축·비확산회의 참석 및 나카미츠 유엔 군축고위대표와 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789213&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 금속성 이물 혼입된 수입 코코아분말 회수 조치 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789212&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 전국 경찰수사 심의위원회  첫 연례총회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789214&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 기획예산처-산업연구원 정책간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789210&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림재난 대비 강화 및 산불예방을 위한 산림재난방지법 시행령 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789207&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부, 본격적인 겨울철 앞두고  대설·한파 대비 범정부 대응체계 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789209&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 국제기구와 함께 만드는 성과중심의 전략적·효과적 무상원조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789203&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(법제처) | "누구나 쉽고 가깝게"… 국가법령정보센터, 국민 눈높이에 맞춰 새 단장 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789202&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 영농부산물 파쇄 지원으로 소각산불 발생 사전 차단 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789201&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 가장 고유한 지역(local)의 이야기가 세계(global)를 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789199&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한몽 관계의 황금시대, 미래세대가 이어간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789198&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 제23회 카르텔 업무 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789195&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 원주교도소 이전 개청식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789193&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국방부) | "제주 떠나 강원도 전장에서 산화한 16세 호국영웅, 75년 만에 고향 제주에 잠들다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789191&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제17회 국가정책조정회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789192&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방홍보원, 「창간 62주년 국방일보 보도사진전」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789190&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 포르투갈과 손잡고 산불·산림병해충 공동대응 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789189&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | AI 기반 의료데이터 표준화로 기관 간 정보 연계·활용 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789187&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 「대한민국 인터넷 대상」 및 「디지털 혁신상」 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789196&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 법제처, 2026년 법무담당관 및  법령해석 담당자 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789186&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관, "교통산업의 지속적 성장을 위해 지원 아끼지 않을 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789185&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국사회적기업진흥원, 「2026 제2회 SE 브릿지데이」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789184&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국내 자생 오동나무, 미래 산림자원으로 육성한다! - 국립산림과학원, 전국 26개 우수 개체 선발... 자생 오동나무 신품종 육성 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789183&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(경제사회노동위원회) | [보도자료]「일자리 공론화 특별위원회」 11.14.(토) '30인 시민회의' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789177&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 빈틈없는 마약밀수 저지선 구축을 위한단속 사각지대 집중 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789178&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)구글社 지도 국외반출 허가 조건이행 결과 협의체 보고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789175&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 기업과 대학이 함께 키운 정보통신기술 인재, 연구·교육과정 운영 성과 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789197&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 국민과 함께만든 특별성과! 탁월한 성과에는 파격적인 보상으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789171&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 구글社 지도 국외반출 허가 조건이행 결과 협의체 보고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789167&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 제4차 기금자산운용정책위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789158&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 미사용 포인트 지역화폐 전환 추진방안 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789160&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 규제합리화 대국민 공모전 최종 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789159&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 쌀 생산량조사 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789170&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 올해 쌀 최종 생산량은 예상 대비 1만 톤 감소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789181&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 달 기지(Moon_Base) 건설 참여 확대를 위한 국내 산학연 역량 결집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789168&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 배움과 꿈을 잇는 특별한 하루 「스페이스 패스파인더」 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789169&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 전기통신사업자 이용자 보호업무 평가 개선으로 이용자 보호 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789165&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | ㈜현대홈쇼핑 법인분할 변경승인 신청 승인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789163&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제49차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789161&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제3차 주택공급 정례브리핑, '내 집 어디에 있나' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789157&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 정부, 사도광산 추도식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789156&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 서울 가격상승폭 둔화·매물 증가…수도권 내년 1분기까지 4만 호 이상 입주 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789153&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | '위기가구 찾고, 희망 연결하는' 전국 통합사례관리 담당자 소통의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789154&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 국유품종 민간 보급으로 임업소득 기반 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789147&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | ICAO 항공안전평가 앞두고 범정부 총력 대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789145&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 인도양 해저지형 4곳에 조선시대 지리학자들의 이름을 붙인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789144&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 기상청, 국제민간항공기구 항공안전평가 앞두고 최종 준비 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789149&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "사람과 기술이 함께 성장하는 반도체 산업" 김영훈 장관, 반도체 연구개발 현장의 근로시간제도 운영 실태와 애로사항 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789141&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부, 2027학년도 수능 대비  지진 대응태세 철저히 점검한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789140&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한국국제협력단 이사장에 오현주 전 국가안보실 제3차장 임명 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789138&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 임업직불금 지급 제한 농외소득 4,700만 원으로 상향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789135&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 가을철 맥류 파종 현장 찾아 안전 생산 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789132&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 산·학·연·관 협력 '곤충 단백질' 기능성 소재 발굴·제품화·수출 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789130&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 재외동포청 인사_류승수 신임 기획조정관 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789127&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 성탄절 물들일 국산 포인세티아, 생산자·소비자 함께 고른다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789128&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '슈퍼푸드 귀리' 종자 파괴 없이 영양 성분 빠르게 확인한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789122&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(경제사회노동위원회) | [보도자료]「청년위원회」·「청년일자리 희망 위원회」연석회의 개최 -   3기 청년위원회, 지역 청년 노동시장 진입 실태 및 개선과제 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789126&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 11월 이달의 임산물로 '마가목' 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789125&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 다큐멘터리 국제 경쟁력 강화에 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789116&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "베트남 딸기 수출길 더 넓어진다" 농약 안전사용지침 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789120&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 통상교섭본부장, 민관 원팀으로  EU 고위급 통상외교 총력전 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789119&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 중동 사태 대응 '농자재 절감 기술' 자료집 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789110&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 아동·청소년의 목소리, 개인정보 보호정책에 담는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789112&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 미래 인공지능·정보통신기술 기술 혁신,  한-해외 연구자가 함께 만들어 간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789106&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부， 제2연평해전 전사자 유가족 과수원 일손돕기 진행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789105&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 미국 호시한 지사， 우즈베키스탄 이괄 지사 유해 고국으로 모신다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789104&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 유통분야 표준거래계약서 7종 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789103&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 정부, WTO에서 우리 수출기업 발목 잡는 해외 기술규제 대응 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789109&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 인공지능(AI)으로 공공조달 혁신… 미래 조달행정 청사진 제시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789107&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 국립현대미술관장에 기혜경 씨 임명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789108&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 시설공사 주간('26.11.16.~'26.11.20.)입찰 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789100&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 지역 중심 산림정책 발전방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789102&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 남부지방산림청-고용노동부 숲가꾸기 사업장 합동점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789099&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.13.보도참고자료] 감염병 치료제 연구 가속화를 위한 다부처 성과 교류회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789097&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 「해외에서 운전시 유의 사항」 원스톱 확인 (11.16) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789096&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 공소청과 함께 산림특사경 교육 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789095&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 「작업시간대 조정 집중 지도」 한파 대비 노동자 건강보호 대책 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789088&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | '가짜 3.3' 위장고용, '사업장 쪼개기' 등 노동법 회피 꼼수 기업 기획감독 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789087&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 대한제국의 마지막 황제, 순종 서거 100주년 맞아 초상 2점 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789093&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, '2026 산림디지털 컨퍼런스' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789086&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 「고성 운흥사 대웅전」, 「영천 거동사 대웅전」 국가지정문화유산 보물 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789080&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "기숙사에 살았다고 보상금 제외한다니"… 20년간 실제 거주했다면 생활터전으로 인정해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789078&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 취향이 문화가 되는 '요즘 청년', 대구에서 만나다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789076&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 장애인의 의약외품 안전정보 접근성 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789077&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 제27차 한·불 원자력 공동조정위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789073&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제27차 한·불 원자력공동조정위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789074&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 물류기업과 기술기업이 만나는  '협업의 장' 열린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789071&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 땅속 깊은 곳까지 더 안전하게… 지하수 조사 표준 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789072&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 강금실 대통령 특사, 제31차 유엔기후변화협약 당사국총회(COP31) 정상회의 연설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789075&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 권대영 1차관, 「월급방위대 TF」 킥오프 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789089&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | [보도참고] 2026년 11월 최근 경제동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789113&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 충북 진천 종오리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789084&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 경기 파주 메추리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789083&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 경북 예천 소재 소(牛) 농장 예찰 검사에서 구제역이 확인되어 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789082&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 인천 강화 산란계농장에서 고병원성 조류인플루엔자 발생에 따라 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789081&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 지역상의 방문 및 기업인 규제합리화 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789070&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제9차 외교부-시민사회 정책대화 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789040&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "타지키스탄과의 반부패 협력, 이제는 현실적인 이행으로!" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789038&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 한우농가 인공지능 사육 관리 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789034&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '국가표준식품성분 데이터베이스(DB)', 국민 아이디어로 날개 달다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789032&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 국유림 현장에서 미래 가치를 더하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789037&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 소비자 기호 반영·국산 고구마 산업 발전 방향 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789030&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 전국 3개 도매시장서 신품종 40종 알려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789028&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 장관, 포르투갈 농업해양부 장관과 '해양수산 협력 양해각서(MOU)' 서명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789039&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 가리비 양식업계의 목소리 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789017&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 남재헌 차관, 수산기업 CEO들과 수산업 경쟁력 강화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789016&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 검역 관리급 '토마토 바이러스병' 총력 방제 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789026&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '기력·체력·활력' 채우는 고려인삼 축제, 서울 홍대서 열린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789024&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 고된 노지 감귤 농사에 스마트팜 바람 분다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789022&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 기후위기 대응 '곰팡이독소' 안전관리 전략 논한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789020&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 어미돼지 무리사육, 개체 식별부터 사료 공급까지 자동으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789018&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '토마토갈색주름과실바이러스' 공적 방제 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789014&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 농식품부산물로 사료비 줄인 한우농가 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789012&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 비료는 한 번만, 밀 재배 더 간편하게! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789010&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 김용석 대광위원장,고양창릉 광역교통개선대책 추진상황 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788997&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국내외 전문가 모여 농약 안전성평가 미래 논한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789008&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농업·산림·해양·관광 분야 치유정책 공유…부처 간 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789006&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 겨울철 한파·폭설 대비 사양관리 안내·기술 지원 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789004&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 속까지 붉은 양조용 포도 '쇼콜라누아' 개발, 와인 차별화 기대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789002&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '농업 연구 협업용 인공지능' 첫발 뗐다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789000&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "현장 소통"으로 활용도 높은 디지털육종 완성한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788998&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청, 포스코이앤씨와 깨끗한 바다 위해 맞손 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788996&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 콩 전 과정 기계화·스마트 기술 성과공유회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788994&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 돼지 육질 예측해 우수 씨돼지 고른다…진단 기술 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788992&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 인삼 수확·저장 관리 요령 제시, 상품성 저하 예방 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788990&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 전분 함량 높고 병에 강한 신품종 고구마 '다온미', 제주에서 선보인다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788988&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 토양개량제 지원 받으려면 "수확 끝난 지금 흙부터 검사" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788986&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 더 안전한 축산 환경, 관계 기관·단체 힘 모아 만든다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788983&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 제주 감귤, 검역협상 타결 8개월 만에 우즈베키스탄 첫 수출… 중앙아시아 공략 본격화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788982&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 공익광고로 우리 사회의 선을 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788980&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제25차 한-유엔 군축·비확산회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788979&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청장, 소나무재선충병 방제 현장 안전 점검 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788978&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | [기고문] 가을의 풍요, 작은 불씨 하나에 사라집니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788976&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림?나주시청, 소나무류재선충병 '공동방제구역' 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788974&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 11월 숲가꾸기 체험행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788972&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 의료 정보보호 강화 위한 민관 협력기반 마련, 의료기관 보안 현황 점검 및 개선방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788970&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 고려인 강제 이주 역사 화폭에 새긴 故 신순남 화백, 11월 '이달의 재외동포' 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788968&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 농업계 목소리 듣고,  통상현안 해법 함께 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788966&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부, 장관 주재 「팀코리아 체코 원전사업 추진현황 점검회의」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788967&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 대한민국 최대 할인행사, '코그페' 11월 15일까지 개최··· 전국에서 할인혜택 누리세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788964&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 중장기전략위원회 혁신성장반 분과회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788963&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 임도, 설치를 넘어 현장 활용성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788961&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)충청권 메가프로젝트 착공식 개최, 첨단산업 투자 본격 실행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788962&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 진에어-에어서울-에어부산 합병 인가,  27년 3월 17일부터 진에어로 통합 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788954&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 「에너지 팀코리아」, 글로벌 에너지 전환과 우리 기업 해외 진출 함께 견인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788959&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 민간과 함께 풍동시험 기술과 경험 나눈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788958&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 진에어-에어서울-에어부산 합병 인가,  27년 3월 17일부터 진에어로 통합 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788952&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년도 공정위·한국산업조직학회 공동 정책포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788951&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 인천 강화 산란계 농장에 대한 정기 예찰 검사에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788953&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(국방부) | ｢국방 에너지 전환 계획｣ 최종 검토회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789150&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 영농부산물 파쇄지원으로 가을철 산불예방 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788956&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-15&endDate=2026-11-15&srchWord=&period= |  |

## collect:out_of_window (40건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융위원회 | 「금융위원회와 그 소속기관 직제 시행규칙」 일부개정령(안) 입법예고 (게시 2026-08-11) | https://www.fsc.go.kr/po040301/view?noticeId=4164 |  |
|  | 금융위원회 | ｢자본시장과 금융투자업에 관한 법률 시행령｣ 일부개정령안 입법예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4163 |  |
|  | 금융위원회 | ｢증권의 발행 및 공시 등에 관한 규정｣ 일부개정고시안 규정변경예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4162 |  |
|  | 금융위원회 | 「자본시장과 금융투자업에 관한 법률 시행령｣ 일부개정령안 입법예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4161 |  |
|  | 금융위원회 | ｢외부감사 및 회계 등에 관한 규정 일부개정고시안｣ 규정변경예고 (게시 2026-07-24) | https://www.fsc.go.kr/po040301/view?noticeId=4160 |  |
|  | 금융위원회 | 「전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법 시행령 일부개정령안」입법예고 (게시 2026-07-15) | https://www.fsc.go.kr/po040301/view?noticeId=4159 |  |
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

## collect:tax_subject (36건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | 2026년 부동산 세제개편안 주요 내용 총괄표 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9VV05RWWFtWkNqZmNWQktodVFiLS1GckNYcXZ6SGUxcFc5dXhEQi0tN0FmM2tucEROdHF6OU4xUnpmd1NXd29fQUpnMkdRbnVac2pqOEsxUTBaN1JWdjcyVjBHOUE?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | metroseoul.co.kr | 여야 재경위 간사, 부동산 세법개정안 놓고 충돌…처리 험로 예고 - 메트로신문 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBZcjJmaVBhZjBIZmZPMjB0bFRoNV8tX3lQemRnYkJRWmZrN0ZnWENJY21NVFMwaDdqSTkwTmtMVGFLZWRrNGZaWDFBTFZLQ1FaaUNSRUJLbmRxdnYzWUY5OA?oc=5 |  |
| tax | v.daum.net | [초동시각]부동산세제, 지속가능성이 중요하다 - Daum | https://news.google.com/rss/articles/CBMiT0FVX3lxTE9UYzRKeHVCVjJWdlBwMmxlaUpUcUwtUFRXemdUZmJtajctUEkyNk9hbTFyS2laRWlOZHM4eEtJOVVFVndmZmZOY1RnNGY1SHc?oc=5 |  |
| tax | sejungilbo.com | [토론회] “체감 경기 회복 vs 과세 예측가능성”…`26 세제개편 쟁점은? - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE14eTJsdUFhend0enBURENHX2dBT0pFdS1mcU9pcGo3UllMbXZsU2x3OG1jb183aFBKZFJQb3ZGWlgxQUVqM1YwZDNRV1JlX0F6SWdiVHdyTzRQRXNnY0FqczZNZ1Ixam80UGFMZw?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | daenews.co.kr | 정부 세법개정안, 세수 얼마나 바뀌나…국회서 여야·전문가 토론:동아경제신문 & daenews.co.kr - 동아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1zamFET0V6bVlRR1NOd3A5OWk2UFc0anBVbUxMSEN4WGJHWGk1ZUVTemRXMVpQSHZRM1ItUnFKOFd0cEdNc0ZEYXhORlNWdVJzakZJUFJ4b1l4RGc2d3lCUFJR0gFiQVVfeXFMTXNqYURPRXptWVFHU053cDk5aTZQVzRqcFVtTExIQ3hYYkdYaTVlRVN6ZFcxWlBIdlEzUi1ScUo4V3RwR01zRkRheE5GU1Z1UnNqRklQUnhvWXhEZzZ3eUJQUlE?oc=5 |  |
| tax | doctorsnews.co.kr | "병원은 기업 아닌 지역의료 인프라" 가업상속공제 제외 철회 촉구 - 의협신문 | https://news.google.com/rss/articles/CBMickFVX3lxTFBNVTV1QkxNT2l0a2V6clJfQ1ZUZ25TeWgzNkZrVUpuRE9ISU5CTEpEVlFyRExqeWdQNF9FY3RNdS1IcG05eWJCLTFsNzkyY01GbV9ud2dsalBSQ2NBTVhiS2NQNF9Yc2hZa3Bsd09ZLXE1Zw?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzDSAWBBVV95cUxOeDlrTWJMLVFFUHdRdGFKSnZYenV2UWl2UnZxTUtyamE4YUNfSjVfSzNHY2U4eEQ1X096RGc2aE9BN3dMUGlnaE56N1I2c2c0bkZkVTR0a1lJR1pUQWxUSGk?oc=5 |  |
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | sejungilbo.com | [칼럼] 판례 80건을 해부하며 본 ‘세법 책’의 변화 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5tMFlsREN2MC01T09YUEYyOGVwTmNfRUdCc1gzSjJzSHZtUFdJNjlETjYwRGZHRnVFeUNiNm9IbkNlSXluMXZoRFkyU3FsX1NqVFNCOGo1eW1oRTkwb0VocGM5cTFJeUZPX2lzZw?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | womannews.net | 국회예산정책처, 2026년 세법개정안 토론회 개최 - 여성종합뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9oZG1XLVJaV3F3bEhYNlZNWnluMDJQZmRKRjJjby1fM1ZDdW5DUFZpWHFKeXIzX0wtdGpKSzAzbDZzTlRfUldJeV9FcHdJQzlHRGl1ak15R3l0QQ?oc=5 |  |
| tax | press24.co.kr | 국회예산정책처, 2026년 세법개정안 토론회 개최 - press24(프레스24) | https://news.google.com/rss/articles/CBMiZkFVX3lxTE52S3FvcTZXUHh0OWRSamVwa3dncEREakFMNVY0dkxmUW1DT0ZDVWFIRDB3RzAtRHV4elVFM0cyc3hqT09KbjExZGRibXRma3JtdHJPYzNqYXZpeFZMOE5nR0VpVVRiUQ?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | mbnmoney.mbn.co.kr | 국세청 세법 개정건의 10건 중 8건 반영 못 해…'실적 쌓기' 지적 - 매일경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wYjVGQjdSbkZCY2RpRjFvUjNyX0tpSFFDazNZVnFkcHdXY2hCd1Z5MUJKbmdNVG56NGdRc2trbnQzYXVoSUhGM25DRy05anRvNnhPYnlOYWdDSjdKOV9wSFgtbjgyaFBo?oc=5 |  |
| tax | paxmedicalnews.com | 2026 세법개정안에 병원계 ‘발끈’… “가업상속공제 제외는 필수의료 사형선고” - 팍스메디컬뉴스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1Dd3lHSEFoSWkzMDJXZVAwcnpDVjkyLXJYa0gwVURLSWJjeGhfTVZnV2pnVTZfdWdqTU1sZU9wM093UDhoT2dmUDdtVThCc3o3VlZEY3lVbzFuQTZCX3N6bHlvSDhrekpTdFFKcWpId3A?oc=5 |  |
| tax | newspim.com | [뉴스분석] 부동산 세제개편안 정부안 의결…與 내부서 불거지는 수정·보완 목소리 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBaMU94ZFRIbWRacklQenVyOHN0dUxYc3AzM0ZveTR5a3Fvd0NsaW9jcVNNRGN3emRCcUFCQWJsa0J5TEFNWnd3bEc1cExsRlNSVDJCMWNNWEkxOWQz?oc=5 |  |
| tax | asiae.co.kr | '부동산 세제개편' 여야 시각차…종부세 두고선 당정 이견 표출 - 아시아경제 | https://news.google.com/rss/articles/CBMiggFBVV95cUxOOTJPbk5qYmx0OGFIamxWdUVqNVV0d1RodFBhVzJfMjJCMWpQN01fb2ptU0N5ZDh4MkQteS1vUEM4UE9Fb1hVbHVlZ21ETW5jTXBub0M0UEMycG1SeUF5VWRoTHp6aUdSNlFFYUYxV2syV1YtVVptUHlVaFRkdjdlSGhn?oc=5 |  |
| tax | sportsseoul.com | 국회예산정책처, ‘2026년 세법개정안 토론회’ 성료 - 스포츠서울 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAxY2luMmRVY3NUUEZNdkVZQzVPUURuSXZYRW1uU3EtLTFRcXRDUGp6WTgxX0o2NzNaamducGdHbENLYlY4bU1iOUZHNThXUnNaMGMtNHU1S2U?oc=5 |  |
| tax | speconomy.com | 민주당, 부동산 대책 TF 가동…세제 개편 논의 - 스페셜경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1MaHJHMnlyV1V6amNhbzZnM01tcS1qS2pEV0NfMjEwMjVxRUdLOW9qNlZkQzFxRWFQTldZMjZjaklQeTdwYVdqblBIc1RsenlZenM2MUFCYUt0QkJKc2p5azZWclZaUERxclktZA?oc=5 |  |
| tax | sejungilbo.com | [판세] 구 소득세법 17조의 '잉여금', 기업회계와 세무조정 중 어느쪽 잉... | https://www.sejungilbo.com/news/articleView.html?idxno=60676 |  |
| tax | 조세일보 | 세법개정, 소득재분배 효과…부동산은 복잡 [토론회] | http://www.joseilbo.com/news/news_read.php?uid=579256&class=7&grp= |  |
| tax | 일간NTN | [판례평석] 구 상증세법 시행규칙 제17조의3 제1항 각 호의 사유가 있으... | http://www.intn.co.kr/news/articleView.html?idxno=2054518 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

