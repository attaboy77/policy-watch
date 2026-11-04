# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-04 10:49:24 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1650건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 27 |
| excluded:company_event | 3 |
| excluded:company_self_activity | 9 |
| excluded:corporate_pr | 2 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 29 |
| excluded:financial | 1 |
| excluded:foreign_news | 1 |
| excluded:industry_specific | 9 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 32 |
| excluded:no_regulatory_signal | 88 |
| excluded:nonprofit | 1 |
| excluded:opinion_piece | 1 |
| excluded:similar_news_merged | 69 |
| collect:event_announcement | 11 |
| collect:incident | 4 |
| collect:law_name_mismatch | 5 |
| collect:no_category | 21 |
| collect:noise_keyword | 2 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 208 |
| collect:out_of_window | 30 |
| collect:tax_subject | 50 |

## excluded:category_cap (27건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | investchosun.com | IFRS-18 도입까지 4개월…SK스퀘어부터 현대차까지 회계·공시 대응 분주 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxNajNaYlQwcU1waGhpNVA1Q0ZzaHBWR2dfYkVEOFZKQ3owUm1iMWE2Z2toNWliU1ExcWI4bzBpVXkxWEU1V0FsRTlvdW5uT2VkbG5fYzVXcWtLRkNFd1hnRmNpMzEwZjR4cml0clRyR2FDQTRwRVRWNkRxdTAzallFTFM3OA?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | CPA뉴스 | [ESG 아카데미 9기 강의소개 ④] 국내 지속가능성 공시 로드맵 및 공시기준 최종안의 주요내용 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFAxc1RXbFdiMHBmZFFFeFJyenJDSkhWMDVhZ3Y4aWE0dHVWU091bWdRdHJ1d0pQTmNtdkxNemhOMkZkR3M3WG5IVGY5RVdFTDQ5ZXU3YTNKTXFHNjJQak1rQ01NakJwbFlJ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ESG경제 | ESG 공시 법제화 속도…7월 중 자본시장법 개정안 마련 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1Mc3U4ek1XUW1XdDNoQmFjSW02YW90MWFwdUdWTlpRX0UyRUVEZUprVE0tVGhRS1JTemNfUkprTDk5VFdzRlBGbHFSZkttOVdOQU9LSjZpNlllUHBHZTVLUHR0UlhydVFJLTRqaw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ESG경제 | 금융위, 지속가능성 공시 로드맵 이달 발표 목표 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBIM3YtSXZjVkl3M0Rya2hPZWNjUlNTUGFDR0FXbTlfOG9aVkljRE1fUzJtMUxGb0c0UW1wUFpkbDJGME43MTQyU1V2Q2hpcXRRMUd6ZDUwb3doM0FxdzRPaGlUYlcwajhOZktSSg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ESG경제 | 배출권거래제 지침으로 배출량 공시 기업, 보완할 점은? - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9VNEpBRU90eXB6NHRGamZZc3V6Qlhlcl9KMFp4Ynh4NEtick13c2h5Q3BJbkNnY3BhTkVZaEdtVWFQUGpYUnp4dmxqQWlqT243SmR2U3lQcm5GSEtCdDNKREhQejR6dE1ZMVZyNw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 의무화 시대, '데이터'가 수익률 가른다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ETFBnRTJ0eEttX3pfeU9UeE9CSHl0UnQzX3lhenlxVWllRGVQUnV4RDZLZ3BZTzg2WlNTLXNUSHJoWTl1eUl1NjBYd2pPVnc3SzhuTXlNaGZUdw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | "ESG 공시 의무화 대응, DX·AX 기반 공급망 관리가 생존 열쇠 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5MS2VReV9GWXFmVy1nc0RaSE12R3BUR05heUZUVzlxMmlkX0dIZW9qVER6ZGJNNDRPdVFWSGxxaG81N19CQjV3TnBxU21yd3NpVFVzd2ZRQkdnbnhTSnZCRU44ZXJidTJrUDllNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBwMjd4R2ZGNDZMejN3dFVaVy0td3k4LVRyMVBjZGw4RV9Bd1pGNWprbk1XVERmUnlYc2toaEZtUVNVRXg2T1BuQVFqZFpGdXRNWWgzQmJ4QnFEQQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | womaneconomy.co.kr | ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5EQ01FU3hUMFIzMFljSktfbnJRVHEzaTJoQ3MyTV8yYTBDeW9IN1BnN1dzWjJUaHlKMU1ETHNId1Ixc1VSSnRIU2RmWEQ5NXRhWWhwZnpjOXhTRHNvOHhyc2RyZk5aSGdGZ0FYWml0QXBKZWfSAXdBVV95cUxORHJkdFQzVVNjXzJjR1VKX2NlRTJpOF9Ea05CeDZqRHNhUVFqMWQtdVlUYTczUVF4VDJBM1JDSkxBOVpaVTl6ZHhWSDRlUlpDaF9Mc1B4dllzS29mYm5fM0JhRndxalVBSnZJcE53RXVheDJpSml6OA?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | yna.co.kr | 이억원 "연결자산 10조 이상 코스피 상장사부터 ESG 공시의무화" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBoQnh0am0tSlNDaGp3WlZvdHV6LUYyOWZYOXVkcEN4clo0S2dCYUJ4bmxROWJCZU1Sc2NQa2Jtd0hic0txM1NRaHo0dXlOSmxvWU9hWF9pR2VTZWPSAWBBVV95cUxQeGtfQmVIWGQ3ZVlhV2VRM19SbVRMWlUyWHBYMnFVLWlfbTdlaEE0VHpCQlR4dFI4VkxPV3BCNkNWWHlkeWgyTjdDQmtjclBfMWRDbmJETHQ0Q25YbkRJWks?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | ESG 공시 의무화를 위한 자본시장법 개정안 발의 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBQbDYtUmVJRTdtZEdKYjJiSWxZN3lwUUM0Y1lXWE9DUkVQV2dMOXltRFpaZXBHUnRFZDNXXy1TTnRFd1pFSDRUd2YzR0ozc0VMc1dVVDl0UUJTcVp4MWlPS29BQWMwcVRGemNpd3B30gFyQVVfeXFMTl9nQ2ticnplUnA0Nm95UkVTUlBQaUJPX3NtclgwU3k0LWJWYXFSdkZOSDVBZjBfN29XZnlYcWJHUWxqR0FnUVEwU2plQnQ2WmN1NTRlT1B1b0JDWk83dlZ6VHJvbEhOdVNNZTctOUd3TWN3?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | energydaily.co.kr | ESG 공시 '법정 의무화' 추진… 지속가능보고서 제출·검증 의무 강화 - 에너지데일리 | https://news.google.com/rss/articles/CBMickFVX3lxTE41X1hTNERSeFU0a3VfQ3duWjBQVTROSGxxcVFYem9MbVVnaTRfb3JtNGpNSmR2dk1RTmdOd0FPZGJkX2lPaWRnS203R2lYVUw4ZmFPc3JRVEtJUXk1RHVSNGI2YTRnZ3dNc0F3QUoyaW5NQQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | newstree.kr | 'ESG공시' 10조원 이상부터 의무화?…금융위 최종안에 촉각 - 뉴스;트리 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE44ajRzUW42eTRmVzNnME0zZzJvOHBVaHhxdDBpVk9DWFpfa3NXMWktN2pQTjlsWFlJWmExRmFUUlQwTkNVYzRFa0pPUWZNRW43OUxZVDZraHUxVHR1?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hydrogennews.co.kr | ESG 공시 의무화 앞두고 '양극화'…중소 제조기업 지원 관건 - 수소신문 | https://news.google.com/rss/articles/CBMicEFVX3lxTE5kdXpRWlJQTVRseXpxamJseDlTZ0NHOFNmRm0tYjFnMVhVcVc5RXR4SFRMUHVZZ3dLajYyX0pQMHBCWFlkS1FITkFHWmlxZlZ1eEljVWQza2Z0QjU0V2s2NXIxSF85RWtOSEdOMW9SU3XSAXRBVV95cUxPQi1BNnFqNThPQXhiQnp1SVlNTWJuYkhDMnBjTlJGYXJVX195V2hkbkpQSFpsQ1hLQlBsUTlRZHVJeE5jNElZY3NUTzhNT0pLeXl5d0F5R09rcG1INE56dE8xbnk0aXZqZFRnYkRBLXlSdjhmSQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | safetimes.co.kr | ESG 공시 2028년부터 의무화 … '그린워싱' 책임 강화 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9ya3ltZnBNSTJMSjlvbmdSRHdCV243TTl0WGJXYXhMY0xoN2YteEdETDhIcVhIR2pqLXEzbU9TcmsyZ0pkWTJDOXYxMzVQMTh5TExOcFFhRERVOUV5YmdFNUU3X3YzWlFLS2hpR1Aya9IBc0FVX3lxTE5GYnNFWlNVc0RaN1lWVjJyN2JOdnRuSk5wQ1RpNzdxeHI0WDV5OUo3T0pzbUNQQ0FEb2dQOHR3bXJhQ2syYU52VUJyMEl0MGYxclJnampIZkdVQ01kM1hWVGZwZGJCWTkyNGNyT3dTVlVVSFU?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | kfem.or.kr | 성명서·보도자료 경제·환경 단체 ESG 공시 로드맵 '실효성 논란’제기, 국제 표준 준수해야' - 환경운동연합 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE95OEQtTUd3MTItaER4RjFEUk1fMlRYSHJkNUlBNVhWZ0pFanUtRmlQMklYZXFQQ3d3VWRhYlJIVkkwSWZzekZKLVNfNmlSbnRWTWxvTUg2Q1FfcWFoUmNZUQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ddaily.co.kr | ESG 공시 2028년 법정 의무화… 디스플레이 업계, `스콥3` 탄소·안전 통제 총력 - 디지털데일리 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE5NaEFNUFpxMkltSG5Wc2NMX0VSMTJ4SDdSWHozZjlTU0NsTkVCOEZ6OXU2cFlQQmxaQmFwejJIZEl3dUlWeE5QdGpzQkpYbFdmUUhzS1RhMGo3R1lxMkxFQU1R?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | energydaily.co.kr | 정부, ESG 공시 의무화 대비 전문인력 1000명 양성…온실가스·LCA 교육 대폭 확대 - 에너지데일리 | https://news.google.com/rss/articles/CBMickFVX3lxTE1TMGZfeld5VU1iOFMtZUZScXVtOW5LdFNaRzdfTWZ6blgydmlOcmtUN016NmdhdkpqcExYUnNIaEVDaE9HalVvenVRZ0FBY2xmWU5Mb1gtNFBCSU1lb24zakVpa0ZxUzkwWlZJcVlpZzc5Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hellot.net | ESG 공시 3년 유예에 안심? “지금이 공급망 데이터 준비 골든타임” - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5iaGx6SGNQX1VPUDZ1cEJqcmg2T3FjM2JoRnV0d2hHWVRuYm8xaEhDd0FnVTItSHphSzVsWmpxd3djTVN5dWtGS0RtajZhTU9IT0ZySFFSbDh2R3pPLVFv?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | greenpostkorea.co.kr | 4대 금융지주 ‘2025 ESG보고서’ … KSSB 도입 등 "업계 최초" 경쟁 치열 - 그린포스트코리아 | https://news.google.com/rss/articles/CBMidkFVX3lxTFBYTkk4Si1fYThuZk9xdnBYeEE1MG1TTVhQS1RSdTR0Rk9SdVhGYlZvT3E2R2ZXSjlreDR2RTVNZkpvV1BZRGZlMDJIX293RElqM1lieUZrYVZjRER3SWctai0wT19uQTVoTFd5a2NDYzI3aTBmanfSAXpBVV95cUxNZE9FRGVwd1pjMENfc1FlbXZSdVB1aHF5TmppaUpzOXdlVjZkNG9ZVDJfVDczSGhrV1NUMmREM3RYT0VCZGpvMkhzcXNOSnJPWVJ5T1ZqMDRJeTdHa1BjYWxjQ2MteWZ3ekJRX2tzS3ZRYURHUS1zb1lXUQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | 발표 앞둔 기후·산업정책…ESG 공시·K-GX 등 일정에 쏠리는 눈 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFA3Z2RDRE9XWk1yXzc1VTlmSzlMVllYdzB6V3BQb2pESE1FQXNJY0VrWVk0TG0xMG1wOXJzb3JnZWsxYThaTkZaQlVNXzFBckVCT2lmRzV2T3JCSlVxMC03QXBqMmliYzhqazZTTNIBcEFVX3lxTE1CTWVGbGt1OGdQMG9LVnBZZEZCSGZaUVVrRmRNV3RkbHU4WFc0R1BOdnZqY3hVZXVUYkdsZjk1aHFhNEFTTmN1M3hXSlpReXFoVmN4bExWQVRGMy16OGJtN0FsSUZPOHJnQWxfZFNwaks?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 증선위, 만호제강 회계기준 위반 적발…감사인지정 3년 의결 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1sVHAtUXQ3WjNRbkIwZ0piSjUtRks5R1FQeXRrYXkzUTMtdXZ1YWN5b21yUkwwVnFJYk5YVUd4V3g5WkVkeGtzUFQ3NXlmQll1MEZEdWdfdndQTE5INC1RMVFiMUJ2OUt4dkE?oc=5 |  |
| kifrs | kr.investing.com | 드리븐 브랜즈, 실적 발표 연기·재무제표 재작성 발표 - Investing.com 한국어 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBhX2VwTUpSX2pIVHRXSnlocUtWSEZJVkIwODRPcEkyRjBRcno3a2lWOWZxaVFNYkN2VnRFVG5zTFBvWjd4Z01rRElmcW5feE1CeG1MUjh6V0pKSjVuWGJhYTAwZXl0SlhBdlFHdjZyb24?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ZXAtQlFZQjUwUV9rbDZDZ0dodTF2MGw1MG9NS09xRUFJekhCQlcxVk4wWkJmZVRoYlkwR2xNdGJEbmVrdU5LRV9qZXpzbkNXVVVNeXlDc3BRZ0XSAWBBVV95cUxQVjBoZ29XNWttV2hfYkFPTG1KWjRuTXRadFBtQnhON29lekYyck5PelV1b3hnbHZVa291TmpZQmdRak1FNmhKLTFTWkZsOGJSZnBUQV91eG9kNXNiV0sxcHE?oc=5 |  |

## excluded:company_self_activity (9건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBhZ3dNVjNHQldlUXYzVlltVzgwTGtmb1ZMWlh1SHZwNDBhemYtTkF6c1dPVmxyNHE1dlVuSTg1ck1yUHB4MzVqdlRjQ3R5R296RXc?oc=5 |  |
| kifrs | idnfinancials.com | 아고스 프로조사스미토, 재무제표 발표 앞두고 BRMS 주식 550만 주 매입 - IDNFinancials | https://news.google.com/rss/articles/CBMimANBVV95cUxNQVc5WlBJeEJ0Zzd4b3RxVnZmWGxiMXlkbFNqb3JNX1QxQ0NFcXlRUVR4OWgyZlMxMEM3Z194M0lBYlhDRG95alJMdjdHV1R3N3BhTE5KN1BlSjBadFE0b3V6UWZxMGhRcGw3ZnBFUEFNUEhINl84MXU1cm93cGxVOG9OQkhiVFFCSUxXSlZ6aHBZSUN3dVVHTFZoTEJzRnhwNzBRVFo3ekJtTXAxSTVSYnoxVllERG1ncm00dkVuZkVzU1V0cEtHSlhmeEhnMWY3OXZiNVVNYS0tUXpnaUljc0JYd0RSTXR5dEhMOURoN0EwN2s3STlCa3BidTRNWVZSNUp0dDRVSTZ2THA5eWUxWTNDUW1DRFVUNjdHYmFqd3FwSGY0Z2d6WGNGSkxwbHd6YTRDYmE5UmJHUEcyS3Excy12OTVtSUhEQklPSjFqMlhTcFh3d214bnhNYjFzNVhjekU3Qno4TW9zeWhud1hfM1B6aU94WFEtbDNKc0NyaThYcWh1a252R1BxRWRyWVpqelFyb01QNW8?oc=5 |  |
| esg | ESG경제 | 하나금융, 공시 넘어 기후금융 관리 강화…KSSB·전환금융 동시 대응 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1IUFFLR0dBamZfTThZako0aEZUZGdSVjQ2eWxLVmRsOGV3WEp0VU11dGVsS1hwR2FNcVRYZkx1a1FoaGFBckVRd1ctdXdrMkRCR1lMSVQwdmwyV0xBQ2dkMFJRVDVzNF9XX0MwWA?oc=5 |  |
| esg | thepowernews.co.kr | KCC글라스, 생물다양성·해외사업장 ESG 공시 강화…여섯 번째 보고서 발... | https://www.thepowernews.co.kr/view.php?ud=20261104103704860de3f0aa1be_7 |  |
| esg | cenews.kr | 롯데건설, 글로벌 ESG 공시 기준 담은 지속가능경영보고서 발간 - 건설이코노미뉴스 | https://news.google.com/rss/articles/CBMiZkFVX3lxTFA2MHZhNXlOZncwT2hiUEYzeHUyeUhsci1lQTlLTmxHRzliR21Hc284ck8yaVgxSmJQT2ttRnZncGRJc3pOM0FwQWlpTUhGOXNXeU5OWVNQM2tFempCS25rQ1JINEhrZw?oc=5 |  |
| esg | zdnet.co.kr | 코오롱베니트, ESG 공시 의무화 앞두고 통합관리 사업 확대…공급망 실사까지 지원 - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTFBWM0xPLW1iR3p4UmM4NkgzZTk5U1cxY0VoamZ0LWZsQ0JwM3ozdTBnbmQwamt2SDNpZy03VHVCOTkzeEhwWHdzblNXcU52dGxtY0Q5Z3VB?oc=5 |  |
| esg | thedailyeconomy.kr | ESG 공시, 2028년부터 대폭 확대…자산 10조 이상 코스피 기업 의무화 - https://www.thedailyeconomy.kr/ | https://news.google.com/rss/articles/CBMicEFVX3lxTE1jZm5pSjVVaVN2aEl4YmZuOFI3MkpCYlNrNEtCT1NEYVJJOGdMWnNCOXBCSXpFbG1id2pWZERGTUE3U1hYbl94d0JZQmJHY0NzNnBBdTJqMDcwTExYWGJBZ3pNNkZxMUpYbi1jekdZUjg?oc=5 |  |
| esg | kbthink.com | "ESG 공시, 홍보가 아니라 책임"…2028년 의무화에 재계 '긴장' - KB Think | https://news.google.com/rss/articles/CBMickFVX3lxTE5abVIyYkJSajVjMEhXZ21uVFl3WThTNXlhVDlobDBIWVBZeDBiVzdDTWRzOU4xVFktVFdpWm9WVHJ2WXVZclRKUjNZX3B6NEgyUnhrR0VWZUdwTmZsSWVydEdxU0s5V0ZxNUZUR2ppdGMzQQ?oc=5 |  |
| esg | newspim.com | [종합] 당정, ESG공시 법정공시 전환 확정...2028년 107社 대상 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE8tYWZaS1REeTVxSXNDaFFWNWwtZlBnSGY1Uk03M1UwUURhZkFiVlVVZkoxM3BZTzFGNlIxT1hOSGRqLTY5MThLOW1aRjlsTEtQbEZNRTJYMDYxNTFZ?oc=5 |  |

## excluded:corporate_pr (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | 【클릭ESG】“누가 읽기는 하나요”…지속가능경영보고서 발간 뒤의 씁쓸한 뒷맛 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBjbUtYWW5zWVg4RTh3RmN4bWhZWmpzZWl2cVljeFJXYTlpSjZJRW1oLUljUE1WS0UzU0NNU19CSG90UFJJS2lVc1FIT04zYkw5MUthQlBrV0wtMjNTSERDZFVtMVNQZ1g3c1E?oc=5 |  |
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
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE5XOVdUY012NVZXOUtHdWtzX1JnYTd1aUlOOWJJb2FwSHlqZ1d0N0VWVk50bkMwcGNqbTFxNjhKd2JEeFAzWURZ?oc=5 |  |
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
| esg | 임팩트온 | EU 은행 ESG 공시항목 37% 축소…EBA, XBRL 전산규격 확정 | https://www.impacton.net/news/articleView.html?idxno=30289 |  |
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
| esg | 임팩트온 | ESG 공시 규제 후퇴 vs. 월가는 기후데이터기업 인수 경쟁 | https://www.impacton.net/news/articleView.html?idxno=30224 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |

## excluded:financial (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |

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

## excluded:news_too_old (32건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | 조세일보 | 김현정 "尹 정부, 3년간 신외감법 무력화" - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JdDQ0dDRwdlpDdGhzcnpHZ3hhZ3V3OXFqbXplRXJ5SlFFeU5VWXhlZHg1clRpNHVfQ3B6YXB2RDZBR21GSWlzVnJ4RnY3NDRpaURGVVBBTW5UWWtzQnd3?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9zaTlJci1iWW1GZ2c3TFFYUUxvS3JWTnZJNXZmQm1rdUhGSzMzUTJvM2hwNlBDdGhKdmJ5WU5ZRnR1MDJIYkl6bTlfZFEtMXE3Q1E?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
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

## excluded:no_regulatory_signal (88건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE43SzV1ZWNkVHBRQzZUUkJ4OW5zQWoyekgtQ2pvZ0FJTXQ4NHVLNjYwa0lPa1RqVHpMemJzRUNxLUJyeXpuT29LWGVJbFNLMWZtelJseHBfNWNoVTBuVVJtb2xoWlpEQ1oyY3c?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, 회계기준위원회 비상임위원 1인 선임 - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5acXJMcUxsamFWTzZRRU1MVU5nazdpUTVUUDhMLU1NVFdjYlItenhWQXJPcENrZW54a3RXZG9XeFljdnZNVXVjbUxmemdtUWNEbGpKRnJ4RGxHRDhLY1Q5RTlQamE?oc=5 |  |
| kifrs | CPA뉴스 | [재무제표 수다떨기] 기업 인수 뒤의 숨은 이야기, 외부평가 의견서와 M&A 공시 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFA4UVFYV2FvWGtPaTZjbVIxQjBESjVJenlJallEaERzQXhUczVGMm1KVmdYb1BwMzRlXzE0dXlhUXA5eS1ya0VwNVFRSnVWM08ybWJlalFfLUUzOUI0OTdVNUlaelFMTEFL?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QQkdfaGlxSmJXLWJ6ZWxsbmxpZVhYZHJHRWl4V0VIalhpZEJEYXJIUy1CSFQ1MzF3TEM5Y1JWdkxvVmkzZDNQSUpyVTNFSExWS2t6Q01Qem9VTkM1TzVheWpUS3Y?oc=5 |  |
| kifrs | 일간NTN | 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1OV0h5TUE1U1VyU0R1eG5FWTkzbmJyM1RrQkpwVkxVQUhfNzFJcmcxTGpGT3U3SUlSWjNsZU1YVVBxQVFyc0Y4MTZRSXhfVDJyaEtoMndWWlhXOWVQMmJpWnRMalQxWjNudWc?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원-한국환경산업기술원, 지속가능성 공시기준 이행지원 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1Dbm80OFRBdTd1QjFhRDA5dTFRMjNzR3QwaXpkQnBzdllCaVk2SXNVekZ3WVNIaXJhTXhScTF5QTYzS2dTWHlDcW9KcU9ITjJkWmtrTnhSNmN2UWJfS1ExOWhlLUJtZnhUeVE?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, ‘지속가능성 공시, 새로운 기준의 시대’ 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBPT3dBRVdDZDVhdEFkU1ZZWmx0Z2daaHZkbGtpY3ppa1FWUVpmOGdldEdwcHRHUDM4RmhPOGVuZXNGeE1RVXpid1dnblpnYm1LV216TUlFMkhjazhmeEtwVG5kY0JRcHlwc3c?oc=5 |  |
| kifrs | 한국세정신문 | 빗썸, VIP '블랙카드' 운영비 편법 회계처리로 탈세 의혹 일어 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1kdDl3OTdXT1NxX1V2SHhwbkQzeTh5eWg4R2RYcVROVFlKV3NtRlJ5SHhIRzhWa0tvcG16MDF3YWtZRFpLbGh6UE00YWgyTVZEcHhtX3lnSHBsaGx3NklFRmpMeks?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑧] 현금흐름표도 함께 바뀐다 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5OWVd5Z0VCYWFKcFRxZ2MydDVicTBORGU5YzhnTFpXQ1NLRFJ0ZHNLVzRKd3N2SEZuQlJqTFZWb1ZidWN2MGJfQmM5ZzdWZmVvVXBTcGNlNFRhT2ZTT2pqYnZ6bEc3aXJv?oc=5 |  |
| kifrs | CPA뉴스 | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5nWU1iSkc0YXQ1V1ZsVWF6RVVlMmVRUkVHMEpWZVNlemtPVHpiR244S2JKc0c4UHE0TXRQWmd4OGhwTkdWczJ2elRCbkRGVEhnMkxmaV9EdUx5bnJacFA4NExtOXlQYzBP?oc=5 |  |
| kifrs | 일간NTN | 증선위, 영풍·고려아연 회계기준 위반 적발…감사인지정·과징금 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBVYjhpbjhCWGZMXy11SUxRNkVneDZyek1hclFyTzB1WU1KRkdQRFN6NElBczZpWHN4U3BhRXhwMlYzSUZrSmFiZGhubjRGMll0ZGx3TUlwak9qakpONUZpRjk1OG1fRFk0SlE?oc=5 |  |
| kifrs | 일간NTN | 금융위, 만호제강·의왕백운PF 회계기준 위반 제재…과징금 9억9640만원 부과 - Daily NTN | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9MTW43ZkRaY0EwNkh5N3FrSFAtU2tkVmZmTmQxMWg5N3lVYllzZl9qX2lCSkhXSGNIVXVHVW1Mbnpib2dweXUydUNkc2JRaHRtWnQzVE56b2xYeVFWU08zYmd3QUI?oc=5 |  |
| kifrs | 일간NTN | “공동기업 재무제표 오류 반드시 검토해야”…지분법 평가 오류 사례 공개 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE56cTAyejRleHo1aGMyUWRaTkxPa0NnTFJoODJJTkk1M2hjRkNpV1dWNlMya2tzLVZjVGpzaEJGV1hEdk9JQ19FX2NCQ0N4UlVQOFExSEt5YW9OVTUwNmQzQUNaYk5fRjdpTlE?oc=5 |  |
| kifrs | 조세일보 | [진단] 제각각 회계기준, '회계기본법'으로 통일되나 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iZExnWDViSmtJa1VsVmpUS3MtTHpYcDNDQU1iWkFWMlBkYi1QMjljcW9za0MwUjE5Vmg4V2dkdDg5blhYZjFrNkhDRmRkbnZ2bjVla0pOR2xMenlvUEc4?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑥] 두 개의 영업이익 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5FRUxaZW9oYmNpYTBhR3h5d0VOQ0NtQmxKU0NHTTFsc3ltYkhTQURmNmV6TGMwNnBtOE85QjFvT1l5Sk9zRHpUX1lwZUYycTVsY1NYRW9seGpuN0QxaDZqdVZLeGczMk1i?oc=5 |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 매일경제 | ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE51S0dscjIzU0MxMnhMZXB0elJqR3lfNnFHTzh5QzA2UzNhbUtVX0hhVnVHTzNIU01QZzV4YVZodnJSLW1vZmktQmcxOGRkWWhPeUE?oc=5 |  |
| kifrs | 매일경제 | “잘 나가던 ‘K뷰티 공룡’ 에이피알, 환율에 발목”…목표가↓ - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE1HM2t2VVRDRHVjTHZGYXVlY256bjFMb0RMcE9GX3VvSWlXQTFkSkk2TGFxbWVuaFRfcEpzMEx2U2VSLVlRZzZ3T3VvbFFLWDFIYlE?oc=5 |  |
| kifrs | 한국경제 | ‘몸값 6000억원?’…중앙일보 진짜 가격표는 [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1MbUtmTVBIS3ptTXgzUzNIRHZ2eXc3NnUzSXVlSEhxU0ZOcVI1VTZ1MENuVUFCNTFmMlJaMXE0SHlaSGU1WVVhZnk4S3dFWWwtRWx1aGY3cml2VDlyQVowVXdORnhJWlZwTERtRA?oc=5 |  |
| kifrs | 서울경제 | 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE41YkVzeThWTUVTaGpkSnBmRDVfWVprSTY2UncyajZDOUpiZFVYTDN5eENqM3ZQcENzZm80RjZwTVNxalhNaWQ3bDRkYTV3S1JnNFHSAVNBVV95cUxOSy1rVnBqeks0alRJRUZOaGVubDNZSmpBYU9TaTY0ME5RT1NnLUtUZjdfZGp5QkVvSTNQMmRvS2pUTlpJR2RXYlcxTklYNW5wNlVxRQ?oc=5 |  |
| kifrs | datatooza.com | CVR 에너지, 인수 예정 마라톤 정유 사업부 감사 재무제표 공시 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE40U3BmZ2lvbE9ZMHV6Y201eEd3XzJXUlBXVkwxZjNpM3R3VjhEc1J5ZlhVQmluQ2ZubkRsNmgxQUVEQTR0LS1DejJrdUd6SUZuQlQ0dTNubXlUa3FFTmJpRzJWMFlxSGl3NF95YXNEcEwzLUU?oc=5 |  |
| kifrs | livebiz.today | [K-자동차 밸류업 체크] 현대차 125조 원 비전...무시할 수 없는 재무제표의 경고 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBZOHpTbGpYNTNZeHZ1YUtiX3RkYm5oSFJHOW9tRlI3MXlRYXZQa0ZhTnNmLXR5RVVkbG9hX0Fjc3NwU1hhYl83WmxwUU85cENEMzFUNGNGVEF1blRHNS1qV3BWaWRKOEhFMmFJcA?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| kifrs | snmnews.com | [현대제철 IR] 3분기 요약 별도·별도재무제표 - 철강금속신문 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBOWWEyWll4OHFHeG9MWHUyNUdYbksxcnRhZ09jQlFBdE9RUkJnRDk3d0RoWWtQSWhQcGpXU0gyNmJqZF9sUEpORjNDWVhKNkRQZnltamhiVXQzeUFjVDRXZzVvLUlCeEVkZnc?oc=5 |  |
| kifrs | sentv.co.kr | 금융위, 해태제과식품 회계처리기준 위반에 과징금 약 13억원 부과 - 서울경제TV | https://news.google.com/rss/articles/CBMiZEFVX3lxTFAtX2dCMTRIT3lLOU1qUWtVd2l3RVBWbjBHaURXMHowbnhsSmdGSS1qd24tOVZkV09BSkVMTzdFTm1pdTVweFl6ZzBNVG9KdkVIQ2xuWW85TWRPanlGbFlSSlVldUg?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1118호 영향 관련 사전 주석공시 모범사례 마련 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE13d18yem9ReWp0R1hMQXhJaVctcGpyTzgxRm9XSXBNOXZxcnNZaDhfZVgzajBhR0gwNm9EQnBmZElrWWhsQ01mbE05dzc5NmVWbksxVVE5STk?oc=5 |  |
| kifrs | edata.ekn.kr | [기후경영 포럼] 윤나영 한국회계기준원 팀장 “온실가스 배출량 측정, 조직경계·산정기준부터 따져야” - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE9ZZ1ZfbmRGdGQ3aVVyQ2xjN3FLdlVieXNqNW85MXdCeEd6M0ZLT2ZDTUU3RnVid2xTQ2NXUVR4RDNsVGRWQUJUN3BSb0FhN3A3U0ZKbjNYd29fX19vVFE?oc=5 |  |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 해태제과식품에 9억 과징금·감사인지정 3년 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBobFhCYWR4N0lQcGVqalJueHV6TzVVUVdxZmVWVFQtaGlOcGM4akhva1hsYkdkMXhURkRNcnNvb0Vka2RMOHFpZE5YQTRtRElLYzBJcktKWHVLV1JXSzZSZg?oc=5 |  |
| kifrs | hani.co.kr | 한때 ‘2차전지 대표주’ 금양, 과징금 91억…회계처리 기준 위반 - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1xOEhJcFZFUW9tYmN2aFB4UFltWlZEaVAwb2o2Z2FyMEM5OVlPSzk0TWJOSFNpN1dYNG9lSlRJMUtPSnpIVk9hX0h3RXVzbmtqN0s0WUZHbmU2M19FMmx1UV9NSmMwX0E?oc=5 |  |
| kifrs | etnews.com | [기고] 회계감리 대응, 숫자만 고쳐선 끝나지 않는다...거래실질·자료제출·내부통제까지 본다 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE9HZ09Dc3F4WjdxRnByRmlYU3FjN1dGVzEyVXF5N08waVNablpCWWF6SFhXbHJjWGRkUGVGalhOY3VxQzllNTFDdjZUb0ZGdw?oc=5 |  |
| kifrs | joongang.co.kr | 기준 바꾸니 27조 흑자가 적자로…새 회계기준에 지주사 ‘비상’ - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE4ybk5IZk1jY3dMRTE3a21sWnlBZ0RYcVpPYnduMW56UzJhek1fellTTEdkMmJSelc1LVBIME55clJXYko5Z0lnbkpEakVFbmVkdmdzbHB3?oc=5 |  |
| kifrs | m-i.kr | 안산시, 복식부기 회계처리 정확성 높인다…11월까지 컨설팅 추진 - 매일일보 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5kMXpHWEhyOUpvVzVwbmM0RFQ1ZGgtNjFTY1VETHU3RDlQd1d5MmExWDMzS0NYUGlEZlYtQzhEQW16Y015UnQ5X2IwbjBRWU1rLWg4R0xnUUZZTk9WR1N4RUs4OGE?oc=5 |  |
| kifrs | lawtimes.co.kr | 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE05MDRqekxIcGRMRFZhMmdwVnM0OWZ3R2lMRGhka0NDWU1EblRBMFplYXc2bldHUDJvMnJtaG0tSnFaX2U3ckt1WXY1U2FxNk1zVm1yb0lUb09Mb2o5elV4S3ZNWVRfSUJPdmxvRHhR0gFyQVVfeXFMUFhvWmtXbVVXc2lzOTFnYnp6bGFkWnc3T2kzcC03bFVzam5Sb25NNWZsSmt6Q29WVmUyZ0EtYVY4SC1IVlB5QmtXTVIxR005WDVzdDYwcDhramd6dXRGOGh5eHdZRnVrTTBoYV9FNzBFbnVn?oc=5 |  |
| kifrs | news.bizwatch.co.kr | 회계감리 중징계 영풍…내부통제 시스템 허점 논란 - 비즈워치 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5aNFQ0V2JXaVMtOVBoRVNNV2RZNE1GYS1mcE1Gd0J2NDA2YnhGaUV3cFJmZldxRDh3eUdNdkxvRktUNEFkQ1NkMVFCaVpBZG9TenNBYVR0Y09KUkZnS0poeUxQNjhEaXhKVVVSVg?oc=5 |  |
| kifrs | news.kbs.co.kr | 금양, 회계처리 위반…“행정소송 맞대응” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE8yTHV4QVF4ODRCdkZraVFaV0ljWkV1Wk5QOFVQRUF3SEZRaXhrNll0bU9ONkxuZTBzaHhNOUtLTDRXVFR5bFZMWWlTM21YSHRrOVJaTHlabWphRzg?oc=5 |  |
| kifrs | news.bizwatch.co.kr | [SFS 2.0]재무제표 밖 거래망까지 읽는다…AI가 넓힌 신용평가 - 비즈워치 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBBOFR0QWktVXlHMWpfSjFlTVEzTk1kTm9QQzhjN2VTYWpOVFcwVnlMUnNxNXZ5MzRqOWJBNnY0aWlPY2JWZ2NGNWdkV3hlMXpRdmxjQmtucVc3aHVDRVgxMHlVNGJhRGtQVldr?oc=5 |  |
| kifrs | yna.co.kr | 2025년 재무제표 '비적정' 상장사 53개…전년대비 소폭 감소 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMOWoySmx2N1Voc05Ba04zNC1ZYzBBZ1A5aUdXNzEzVms5N2hyTHA1ald3Zjc5dnRNRHh3LU9XLWtmTWJfR2Q5eV9aSzBnQVBCX3VHTzNsUnNKT2PSAWBBVV95cUxPTmZ3M2J3VVctVkFTTmRhU01tZkRBTkROS3Rmb195V1R6OTJrYjRUNG1uUXh3Z29sTkJXRDhpaS1ZTUQ1ZkdrRHZJdnV5SDhCRktQQ1JYaWtEWlBTTm1od1I?oc=5 |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5tQWI5RHBpTVRkQWY4TEhWVXdJek5VRG50QTBTLW5ZTU4yNDVoUW9wRWtXZldMdXBjMldnSkxzVDV2blFoU1RpMndUX0pWdTNDVDlPYXB5T05RY2s?oc=5 |  |
| kifrs | news.einfomax.co.kr | 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBzREN4d0RmcDJBMXFhZ3BfZVVTRXJOalhqNmNYYVRoUFNzQmJoNHdqb3pmaXVqX3RGTlpMbGVYUGh1dGNHbEpBbXBmQkE3cEI0dVFMS05DaHdjUkswWTk3Vy1qam5vYXhpckdud2xoX1k?oc=5 |  |
| kifrs | yna.co.kr | 감사 전 재무제표 제출 위반 76건…전년보다 24건↑ - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lODhfd3R3TUpXOFZneW5tMjJ0OEVEeXBMWExHS1F1MzNOdExVUlNsdTFwYVpFZTRxLXNTZzZoZzRmQnhhYW5ZZlhtUjJJM1M4YXA0ZWNCbU5ubzjSAWBBVV95cUxNUWMwYlBCMlpvS2R1a2dOaVdCYkRqcE04YXNwb0JCSC0xb3NSc05OM194Z2dCcVhiSFU1elMzQklVZHNCc2dtRG1wMk5kSTJmMW1rVWZWdDFQcjZrZFVRTno?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 영풍에 과징금 204억…고려아연은 84억 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sVlBmQzJPbXZuSTFOai1kaDhGb1hLVkpCdktFWnZaU1YweGRJWllmVk9zbUdZQTdpUTVRaFpHM1RlQXllWkhpdVpJUFlqLVV1SEJESnZkVUcyZEnSAWBBVV95cUxQZTlEXzktdDljVUR2UENmbHJnUzFKNE04U3BxTzNETFZBTlA3alY4VGJtREYwdmVvSldHM1JlM1kyNWlsVXJFbUxCaHhaQlBlU3VHTVY2UUh0Uk1aS1U4MzM?oc=5 |  |
| kifrs | dbr.donga.com | “회계 기준 지켜도 재무 실체 숨길 수 있어 AI 군비경쟁 시대, 숫자의 행간 읽어야” - 동아비즈니스리뷰 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5qMUhEM1BDNkZicXpqTE1BQ29zYzVrM0FfdXYwLXhvS201RXE5NmVJLWFZaU1Xcl91XzRocV9BMVduQU1JYWw3cldobElDWHo4Q3hoNVF2cE5NWjhjRWJRSnhGT2pNWFU?oc=5 |  |
| esg | ESG경제 | ISSB 자연 관련 공시 실무서 들여다 보니...S1ㆍS2 보완 | https://www.esgeconomy.com/news/articleView.html?idxno=17209 |  |
| esg | ESG경제 | [신간] ESG공시 대응 한 권에…'지속가능경영 보고와 검증' - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE85d3c3VHFuQXNkNG5UQkFNb1M4TERPYVRjNDExOElUcEc4aHZGXy1keExOMmU3VHlLOHZ1cGtKc2JDczVMRmo2Y2hlZlVFeHF0OFY3c1JyNnhKOXdnZ0dWOW9kV29hTjlyZ19nVg?oc=5 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5CaDVvOUluQ2JzNGRGNUxQaWctYVY0eEdyS0ZWTXQ3S3d6RmlZaG1CaWdJTkh6NFVuQktFYWZ5UUdVWnl2eWw1VGJDNjFELU9LTy1Ua2ptRFFabVR3aXNpLWhxQ3lsRFFla3c?oc=5 |  |
| esg | 임팩트온 | GRI, 식음료 산업 전용 공시기준 만든다 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE84ZFBJaEdtUlNMazEzdVRFN241MXNlMTRkZUtucld6Ry0xRkROaXlYcjhtdUQ4amE2MGczNDI5SXRhNmNmZXp0X0ZmaFZwRDRRa2hDMHA3RURNUEpJWU13SzYtTmh5WjZ0Z1E?oc=5 |  |
| esg | ESG경제 | [해외브리핑] 싱가포르, ESG 공시기준 초안 공개...스코프1·2 먼저 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB2d2RieWdDdXRHVU1aY2VlSkVIX1hQS2gtencwUkFZWVJwY094Yk0tcFlTZjliWVZ5YUhodU1McW5veTBNN0JRNTgtcDVqMG0tdjI2d0FzdGtUa1ZHTFNJeGt4eVhkaWdRQUV3cA?oc=5 |  |
| esg | 임팩트온 | ISSB, 22일 자연공시 초안 공개…사업장 위치·가치사슬까지 평가 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5ibFRYdXJrMWtJRnhPUW1NTUR6bEZ1OWZ1ZUp4UmZIZ3hYNFUwZW5DUk4yZEhUSk5MVTZNdnQzaC1zajl0TzA5Tm9OTjI2SEdKaVE4WnN5NWFrVzRDYlp6MmtzbW5sU0dCX1E?oc=5 |  |
| esg | ESG경제 | 포스코홀딩스, ‘KSSB 공시’ 발빠른 대응...법정공시 TF 가동 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBZU0hCR1BNMjFUY3FHRXZaRWVicy0weEZrSFNKekh3bVRqdE5DbmIyaGo3M3Z1S1JaVzlmbGpmWnpfWjZrSUhhNHFuWWVRd2stTWxfbEtyNE91c29JWE5pUTY1aGRCcFVjajlodA?oc=5 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 임팩트온 | 【기획】국내 대기업 99개사 KSSB 전수 분석⑤ - 현대모비스 97점 1위…재무·경영 연계서 격차 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9rTS05cDJWUENMM20tVGJLcDd6Z21Wd3p6TTFFRGZ1YVdzRlh4and5andCSThBQy1wNHFRT3VpMDUzNDBPNUhYb21vb2xLMENKZXlsTWRUeG5sV3BfWXcycWtwNmJFdGtEN2c?oc=5 |  |
| esg | 임팩트온 | 【클릭ESG】 “3월엔 추정치, 6월엔 정정?”…ESG 공시에 IR 부서가 난색 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9oay01YjlVajVfZ3NoS0V6OHJTbVZaZHJIaTlqQlZzZkhNeWRaeEpQU0tET1l4VVNDdlE1Zm1QM2k4NjdvcGtjbFFtRndwUUtyaFdVdzU4MXlOY2tqMmtkeE1WelRiNVBYTlE?oc=5 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있어야" - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1wbl9FYkhYT2Q4MXJBcnRNSTJEb2ZrNnZEUXdob1FWRUdqcGdwd2JodXNrQXdGV25UNWVZeC1ZSDBxLUZFYWRRcS1zMzcwb19SbVROYmdIVERrRkZmYkRSQ1FhaHBsQk5lNEE?oc=5 |  |
| esg | 임팩트온 | KSSB 첫 공시 준비 5개월 앞…엔츠, 연결공시 AI ‘엔스코프’ 출시 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5nTE9nOFVSLU9EODAyM1lJeXRpTTJvSWdiWEhLVk9LSkxCN1pKVDJkOF9mZUVJNElJVU1lVGVGcjRDclExT2dzZW9LRnVqOUw2VlU0cjZldGtNNHhEcFRXSGE5dnRnbjAwZ1E?oc=5 |  |
| esg | 임팩트온 | 【공시 모니터링】삼성물산 KSSB 기후공시…기후 피해 33억원 산정, LNG 전환위험 재무영향은 공백 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1TWElWQVpZZGgyYndFaHluQl9uWUhBSzI5NWVCS3FIcnlKQjJhUXZlVmJVQ2VLYnpWYXVEMzNlbDlWU3haTTBBMHBpVWFSV0dXZmRVaWN5cC1jNXVxZlN1VVdQMVVib2NRQ3c?oc=5 |  |
| esg | 임팩트온 | 【공시 모니터링】APR, 첫 지속가능경영보고서…온실가스 배출량이 없다 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE13LUgxNzVXanZWYlRva2pFVFloekNBRWNpRmthZWxMSHB6TmEySS0zZ21lWWVMRkxhWGlydWlpMjdfenVEZURCTzkyOHJNZl9KWEw4RnluaDRyT2FIWlYwYnkwcTNYUExaNlE?oc=5 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | 임팩트온 | 스코프3 추정치 줄인다…에코바디스, 공급업체 실데이터 연동 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE80VVdfcHFzTXVLN1JTb0pZNk44cXQybm1wZ1UyeEluSEx3TzBabG0zUmhfTFd3T2hNQlJoS05PZXFBb3Q0UzV0Vl94Q1VkTjhFbEh6TVcxTE5WbkRTRldMM0VLcEhtWUdJZmc?oc=5 |  |
| esg | 임팩트온 | 【공시 모니터링】기후 위험 계산 끝낸 SK증권...남은 과제는 ‘익스포저 공개’ - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1UankzaERWWV9IV1FFTkE1cldMX0VLblFCRHZjTVZzS1VBdDc3WEVJY2w0NjZwTXoyY1ZOWUx4RU1oYWp1T3dYLWxKT2RYWTg1OGg1cEFPRFlXQmhScEM2UEx6ckVzODdhZ3c?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 머니투데이 | 상장협, ESG 공시 대비해 실무자 쟁점 미리 챙긴다 | https://www.mt.co.kr/stock/2026/10/19/2026101913585170575 |  |
| esg | 한국경제 | ESG 공시 퍼스트 무버, '경로 기반 정량화'로 신뢰를 더하다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBHUjE2cTNrQkpRelQ3R1BaZGNQQXU1VkZxdjU1S3R4VDhOS2NBSEtSSnZhU0JvUzlHbjZwM0QxaEVLN1pzZjBsd0xUczZrdjlGY3BrZmZRZm5odw?oc=5 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | joongangenews.com | KCC글라스, 생물다양성 영향까지 공개…해외 법인 ESG 공시 확대 | https://www.joongangenews.com/news/articleView.html?idxno=561023 |  |
| esg | worklaw.co.kr | ESG 공시, 직원 성장 이끄는 장치가 돼야 | http://www.worklaw.co.kr/view/view.asp?accessSite=Naver&accessMethod=Search&accessMenu=News&in_cate=101&in_cate2=0&gopage=1&bi_pidx=39682 |  |
| esg | asiatime.co.kr | [윤영민 칼럼] ESG 공시 시대, 보여주기식 경영의 종말 | https://www.asiatime.co.kr/article/20261023500342 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | sdgnews.net | 【ESG 공시 대전환④】 ESG는 규제가 아니라 국가 경쟁력…'지속가능성 자본주의' 시대가 열린다 - SDG뉴스 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1HanZVZ1ppRm9vRlBRXzhMMUlRQWtqWUxDTGV4ZzV0LWhTMlhLZE1DM0NsTVIwbmZ4M2pHNC1LUFdJR29PQlBkWXdMQzRCWUJqdzRkWWZ2ZmdVa0hySXNrRGVsaWZoaFnSAWtBVV95cUxOam1qc05UNEQ1Tm1xbWNXVUZRNXpxZThXT1psdnBDWW1yU01UR0ZpVXU5dWpBMS11X243RUlIVmZlYnFpQmdoOGE1Y0NIVWRVUVdKNDk4QnBvVkQyX2hTZFktX3Uta3hlZEQycw?oc=5 |  |
| esg | news.mtn.co.kr | 염정섭 기후부 녹색전환정책과장 "ESG 공시 기업 부담 낮출 것" [2026 ESG 경제포럼] - MTN 머니투데이방송 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1VS29JSWN0VmEzdXRNbWg0VExwRlYtQ243U3RXTlRoN254dTRtVXctcDkwclcyQndHRGlVZWZZRURKdjRxdkJVaEFPNEd4OHEyR1J4dFktNG9JRkFfTmVkX1ZBME0?oc=5 |  |
| esg | safetimes.co.kr | 경실련 'ESG 공시 늦추면 한국기업 경쟁력 잃는다' - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE01bXN0NkxjUE1tTTk5b3dMb0FRczRZc2hNS0E3c21sWmtzb3htanZObUh1bV9aSUFrMnFscEFMQUwybDBfcXJseWo2aGo5dHV6Smk1T2ZCeUJEVEl4RVl2eVBSR1dHU2FMSVQtRVZJd9IBc0FVX3lxTE1uYk5kX05fWkJPMi1ENW41TWdYczhYN0luQmlxNjVYM3l4RFdDTjRnUWYyS2NNQ3U0SE9VSWsxTzczNFNZU3FSOERNLWQwd1NYakhkUHJEazJOdi1QRDljak11a3dZdlk2b1k1MTZ6cDBNOGc?oc=5 |  |
| esg | newscj.com | 충남북부상의, 지역기업 ESG 공시·규제 대응 지원 | https://www.newscj.com/news/articleView.html?idxno=3441094 |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| esg | hellot.net | [ESG 칼럼] 2028년부터 본격화되는 지속가능성 공시제도, 지금 무엇을 준비할 것인가 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFBjZ0hCNjdsZ18ySnhycVRpbW5jZk1CVkZrZzVVMnQwdUtNRW1PTjZEMjZDSGZCbXJEQTh6cWhfUmkyNWI5cHFNejczel9GVFpaMkhQWm5sN2l1RnRhemdR?oc=5 |  |
| esg | news2day.co.kr | [ESG 인사이드 (97)] 지속가능성 공시, 기준이 아니라 경영을 보라(上) - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTFBlZEU4bFlrVWI0Unk0WFZRNUFzU2d5cV9nQUtQMGk1bXdSV2hhN3dNN084Q1hzeEV4THdoc2pyUFY1OU5pTHY4SV81M1l0OE5PZkh6QjVOQ21FWTNuNWc?oc=5 |  |
| esg | hellot.net | [ESG 칼럼] ESG 경영의 주객전도, 보고서가 아닌 운영체계가 필요하다 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE9tWktmcTYyVFQ0LXlXN01SNUFBUFB1S1MtY0NVaXVNMUpxd0d6aGFvd0EycU95Z0JzQW93Ul9OQllDRFBTcDFsUjdYZzhfLUVreE92LWFwSmtwd2tpaHJB?oc=5 |  |
| esg | ecofile.kr | 2028년 ‘ESG 의무 공시’... 우리 기업, 무엇을 어떻게 준비해야 하나? - 강찬수의 에코파일 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5VX2FFQ1lVNlIxbGxDT0NUdEN5QUN4cG52aGtZN3lNVTJtWGZPamdkcVVPaGJJRHlLYjJqU2ZZN2hDLW1XZnhmTXRFNkVxWUFpSTJzTF82Uk9oOXc?oc=5 |  |
| tax | 한국경제 | 경기도 재정난, 국회서 지방세제 개편 요구 | https://www.hankyung.com/article/202611044774h |  |
| tax | 서울경제 | 경기도, 지방세제 개편 입법 논의 본격화 | https://www.sedaily.com/article/20107006?ref=naver |  |
| tax | weeklytoday.com | [위클리오늘] 추미애 경기지사, 지방재정 위기 해법으로 '지방세제 개편... | http://www.weeklytoday.com/news/articleView.html?idxno=800450 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| icfr | insjournal.co.kr | GA 검사 대응, 정도영업이 답이다③ "서류만 갖춰선 부족하다"… '상시 내부통제'로 취약점부터 잡아야 - 보험저널 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1wNE1tMXlPTk1hQXNhbzcxdm1CbkFKbHBnNzk3VGRKc3FwX1c0cU1seVVWNmlKMVA0Uzl2dGR0cllJSHZpa2w4a3hpT0Z0TzhKby0yUm9OaUtieC03aGlnU2M1WXp1NmdVdGJzNnNfTQ?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |

## excluded:nonprofit (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | CPA뉴스 | 한국공인회계사회, 『공익법인회계기준 실무사례와 해설』 발간 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFB1T0FfdnRKR0ExSkF3WmpfeE04WFlIc0Y2bFNSOGRxS3g1Um1uUjJycWgwUHk4a3hsd01DZnM1SzI1NGlmd3dQQk5TT3ktQklMWFg4aEd5OEZZbzdIVExsdUdsWTFfaFVl?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | 【칼럼】기후 공시 의무화, 그 다음은? TISFD로 보는 사회 공시의 미래 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9zZ3BvOTJGbXQ1YVZSZF96elB5RUV0NGVkYzdNS25reW9teVhZbnk1dzE1RlFKdGdRQm9VSWxiTGNqSmw5Z3NBZzJlWjlrcEhVTDU3SVF3cFdveF9ZbGpFWWJxV25xSkZCeGc?oc=5 |  |

## excluded:similar_news_merged (69건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | joseplus.com | 회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 세미나 개최 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBOTGZHQncyWkZkNWphSDRhUGV1S3ZSNDYxWmxtRVpVUkV4SzVxaGV0eWZ1allzUnJ1REVBTXBsY1BLcGpoVU9JblZRWjZQcy1MSFh4Ym5RWEnSAVNBVV95cUxORWdjXzk0bGwzdHhMMzJMQjNCWm5Rb0xxTWctc2lOaFZmQ215Tl9iZS1ZTGlwckpUTjBmUnVmQ2h1V0ZEdHQtUHJrOUhBZEtCUnJ5QQ?oc=5 | → 대표: 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중심으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFBQcFZGSDROYXJzRmRvdFlZOHJfbDNQME56R1plWDNLM3c3YUU5bmJWUDhpYXVHdU05YzdGOUxLbl9ma3hUeTJCSnpTUUt3LVk5dl9IY1Y3TFJvV082d1Nz?oc=5 | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | joseplus.com | 회계기준원, 김정일 대한상의 상근부회장 지속가능성기준위 비상임위원에 선임 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBWQUt1dDZwX0VzYmZtTTBLcDhpQ1pJZWFrdzhwSW5oTF9sRUV6SDVKSVNqenNEV2o4S2VrdVV5b0d2dmE1RGw3c2hrQzZsRmY3OXZTaXNUcHXSAVNBVV95cUxQTWZfbl9xdnBpZ0I3aWgwSm9HN2t5SVRQaWluVjYycU0xMmZ4WDhHcEJFcktlV25Lc3Voa25iU3BNVkUtaGhENkxfbG1XUEdYUG1Gdw?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | seoulfn.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE51SEdGb0VqY2lPZEJIbFZVNHp4QmR5X18tb1NBMlpxOThhU2pTWFgtS3FtaFhZdzk2eGJ5cU5kcjVnMFM2d19laXNxTG5jYm9HUElEMXdwbml1VWFxTGlfMXRuejlocFVNT2c?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | 일간NTN | 금감원, 감사前 재무제표 제출 위반 76건 적발…9개사 감사인 지정 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9FelZSMGExRC1CYVJ4OUFrTHhCdjMwUy1tSjBoQmZFNER3WWo0Ry04dGZSSmttZlBFM2l3VnpZVnRtdV9ZcGdlcTEteW53WURpR1BMZTdmVm1GYWJ6amNQTmhZZXpXUjdianc?oc=5 | → 대표: 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN |
| kifrs | joseplus.com | 한국회계기준원, 개원 27주년 기념세미나 개최 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE4xOEF6UlV0Z0ExRGxMUzN5YWVTRGNPazdURThqS0pfcmZZOGxJMVhwT3ZOYzJkNElCc2MxMG1BajVQWU5SSVBHcVBFd3piekxYTU9yWEtjSEHSAVNBVV95cUxPUVYtSk81em5Vb0RHd3czSmU4WF9VajllWlNIbzE3b3pRWDFhWUZOaWNSTjF4SS1XNVdVdlU5YVJNN3FqeWJ4N2VvZTZtNWNRNEp1cw?oc=5 | → 대표: 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBJYkpxaXBTcjhUQkZPcHVfay1mQnptQXRhMklhUVNBQ3VSZy1WYWpzeVp4eGdkMmF2bHhDclR6ZHMtMnNJQlNWYVFmb2tsWWxYYndaTEFrcVVHZUnSAWBBVV95cUxPelVLaldNY3hnelFDQzFqaVY0UDBDX3EwY2xkU0QzS3JBc0JBUm5STlFaVlhxRnlpN0FmbXNSQjdEd28zTXFCQWctb2JYN3JLWGZQcUZFdEM3MzJtOFhTTlk?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 |
| kifrs | tfmedia.co.kr | 금융위, '회계처리 위반' 해태제과에 9억 과징금·감사인지정 3년 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE1nVW9jUjhaYTVIc1p6ZjFubzYwSEFsUDl4Zkw3dkpKN2hoeHJoUHFBVDFVa3kwZm5XSEpwM0lXcUd3ZjRiZkhVcThYYlNRa0dfOFZCdUFENUpLVGFWclp2UTNvcw?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - CPA뉴스 |
| kifrs | 조세일보 | 영업이익 새 판 짠다…K-IFRS 1118호 시행 석 달 앞으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFB0MnpUYjZVSVNaY2VaT21MQUJDY0Z1N21nWEtCbVNZVWxZNmE3ZTlrcEI3VFdEb2dlZWpVZ0k1bXVzNlBYUENtcnJSUVlLTWFhNjNzZTZyQmphNy13dmtz?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | 이데일리 | 내년 K-IFRS 제1118호 의무 적용…금감원 "기업들, 도입 준비 철저히 해야" - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5ld2NBM0dGUjlxX25jVjFiQmV3cVdPQ0FLYzFUQU8yX2lqUEItQ0JJZ0hEdVBVai1rNmlrZXc5b2stUHhoYWdkdDZpQTAyTWdBM3ZnQUNYX3ZMMjI0cXNKUjBRcjN0UjJXYWNkYkdvSzNOT2c?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | junggi.co.kr | 2027년 K-IFRS 제1118호 시행…기업, 도입 점검 필요 - 중기이코노미 | https://news.google.com/rss/articles/CBMiakFVX3lxTE41S2l3VmRscy1LUlowVVNJaW5BdExCQ3FIQ0Y1N3Zlb0FhSW1qSXpBVzZSVXRpRFJzdHNKN2RqTlhxSEk0Rm9SSkpRaks0d0JHNV9VVDFBUGZYeE9keW5WNVVtM3hMdGhVVHc?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPOGFldExqZEFIdGQycE1SbC05ZHV2Z1JaajVGU2YwOWtuSkJ2bmc5aFFSQmJEdGlSVG91anA4RXIyanNELXJDOEd3bkVFclVVRGlSa3E5V01Tb3lyOFZOVVpzQjZYSHo0MUlzSjlEd3dBeTdKeHh5dHlGNUc0VEcxZzFIdW5HRHhB?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | thevaluenews.co.kr | 손해보험사 영업이익 산출·공시 기준 바뀐다...K-IFRS 제1118호 내년 시행 - 더밸류뉴스 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE14eS1FSzVMV0x5TmlpOUpXUHBwSFpuazk0alpNQWhKdXhNLV9mY0piRXlRVVRFVk5DZmNEMm5HZXJqWEpISG5FVks3X1luTGVOSUNMTw?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | yna.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VYm1UdW9mM2l1SG84VFJPSnBhSHNGa1dpUzJobWpjNnJ1aXliX2RGMkhNR3FPM09rYjQtREI1d0hBTHU3V2V5aGcwRzJfUEpvaFdvc1V3WENNeVHSAWBBVV95cUxQT2JUYXQzVE5hTGZwR0dROTBxLU93YWYyUDdjMkVxbjBtaEFMYzltaWNJRzRKLVh1OG1ZLWx1ZEJTOWktcHZFRmNOR1lfZzdjZG5wdnB5YzM0M3dra0hXaDU?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | news.kbs.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE83QWNpcGNnbWJVTGVnclJaTDdkblBWbmRVNl9uLU5TRl91NHdlN0h1WEhiQzNNNGhFd2dkbjNKWmVYaGMwQ19sbEh4TU9zZjRlMVBWNkRPb3RBTkk?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | 매일경제 | 내년부터 바뀌는 기업 영업이익 기준에 투자자 혼란 커질라…금감원, 사전검증 주문 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE1XbEZYTE0xMXk5NmdzaTRnR0h3MkFfNU9IQXVoMkozdFdQVUgteGQxeW1jQTZNQWdQZlRvSG5QdFR1d3ItSi1yU2tlOGJrQ1I1SkE?oc=5 | → 대표: 내년부터 새 손익 회계기준 도입…시장서는 "당분간 혼란 불가피" - 한국경제 |
| kifrs | etoday.co.kr | 내년부터 기업 손익계산서 바뀐다⋯금감원 "새 회계기준 대비해야" - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5vbWtNd2xlMWZDeGdsX1BKWU5PSVAycU5qX2tqYXRGRV9hWXMzMTM2RUViZW1JYTh1TktzSXlQaVY3NDZWYy00aTRadmR1QlFwZnZJNQ?oc=5 | → 대표: 내년부터 새 손익 회계기준 도입…시장서는 "당분간 혼란 불가피" - 한국경제 |
| kifrs | datatooza.com | 드리븐 브랜즈, 유형자산 회계 오류로 재무제표 또 재작성…3분기 보고서 제출 지연 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9kMHZnMUViSlVyZXk1N2RPTFI4SFJqY3l6SXJTcW10dWFfR2oxelAyVTFScno4Z1J1NDM2WlRCVXJkXzVudk5XZU90VFl6a1NfSHdsQWh2bWFCcWdoZEdzM2hfV0lYaG8xTTR5MXJ1Z0VTM28?oc=5 | → 대표: 드리븐 브랜즈, 실적 발표 연기·재무제표 재작성 발표 - Investing.com 한국어 |
| kifrs | datatooza.com | 인퓨시스템, 3분기 실적 발표 연기…ERP 시스템 회계 처리 재검토 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5QaEdHRE13dm9KMG5pVTFvMV9TeDZQMjZVb2phTkNXLWRnNHNBNTliTG1MZzFQakJRckNYcGFic1pQVjdjMnVQdEV2dngxYld1UHh5RkR0RlRleTJLazNOc1VjR21hUEZ4QVZfMFRKb2M4SXM?oc=5 | → 대표: 드리븐 브랜즈, 실적 발표 연기·재무제표 재작성 발표 - Investing.com 한국어 |
| kifrs | datatooza.com | 호손 뱅크셰어스, 인수한 FSC 뱅크셰어스 2025년 감사 재무제표 공시 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5rcmd4T293cW1FeWpYRFQwRUtqdS14ZW9HZlFwcnJIUEpBSHRlSWloMTg1R3p3QmZMeVBBMl85SVMxdXRSb1RNVmRuX3dBOWVmY0VDeWxtSnd3NFZ1cGxpamtWX1VmaUdUcTJZLWJSc0stN3c?oc=5 | → 대표: CVR 에너지, 인수 예정 마라톤 정유 사업부 감사 재무제표 공시 - 데이터투자 |
| kifrs | newsis.com | 내년부터 'K-IFRS 1118' 시행…"실제 재무제표 산출·검증해야" - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFB5M3puck1JNk05dVZDajFVRjhtR0s0MDc5bm8tWGVSSXQ4QlppWGV2UXlwVHc5U1JQaEZhTjVqZWkwU09jM3U4RFlXTkYyN1dfQWhNaTF3Uzl4OGtzUkFuc9IBeEFVX3lxTE5CNHE0czVVcE1TUXBYcGg2WTRLdTR5X0c1Uks4SkYxOHF3cE0yXy1KUGhIY1lIeXBvMmR3UXBkUkVNblUyNDF4blJ4eTBNcXYyY1h5U1MwVWNnQThXU3RBYmtCZnZtWkJJbWNpUjNWVUdJUmExYjFGUA?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | insnews.co.kr | 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5PTnlLYzlLQklteE1MaW50MjZwRV9RQkRtZDAyal9rdVpCc1pvNXk0M2tCS2hLOVpFa18tVDFmd0VQTDh6bmVBZGR3dkdIU1VFR0ZrWWFrOFpRRkZ1a0Z1eUxsNG9UOG5ncjZF0gFvQVVfeXFMT3dydTBxd2xRSzI3ekVzdF9GVEdtakV1TURuT0VTOEFSbkloTURQV0UzX0F2NWk2MVFqYVBFaDdZN0M2V2xTOGhwR3N1RTB6QnNWUlhNLU9RNkVEbUpmZk12cXlUb3NXUmJJc2dWcFFn?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | alphabiz.co.kr | 내년 새 회계기준 시행…금감원, 기업에 사전 준비 당부 - 알파경제 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1DVjBKVS1Bai03amhmX0k4Zlg1X29uN1RWQjFRNElnYzBDX3JsZHIxVldxTUYzY21EZElaRlJ4eTlYYUdrb3BIWnlTbjZ0T095ZzNMMWlRTEtfeG1QcG9NYnctNXV4SXJodVBZNjJR?oc=5 | → 대표: 내년 달라지는 재무제표…‘K-IFRS 1118’ 시행 앞두고 기업 준비 본격화 - 보험저널 |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE8teDVTVFFGcExHbG5QekVJcDJNbkxQNVVOamZvdmpheXlIQ2E2WndnOHR2RVA1YnQxZ1JXek5RcW1DZXJrWW9vWE9oblVUZjFxQUFKeWJEeVEwSlc0ZS1MSw?oc=5 | → 대표: 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 |
| kifrs | safetimes.co.kr | 금융위 '회계처리 위반' 금양에 과징금 76억 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE85NENZdTJ1VVl2Zl85aFlqUnVCa2tuZ19BWk1BRWpOUkhrQXZVVzNIR1djeEh1YkVBY0hld1FkOGtiTEtlS3lUd29DcVNDdF9XSGVKMUxLeUc5RlQwUXpwbkRkWjFDNWNqb3Q4RzJKa9IBc0FVX3lxTE1MdWw3dTRUX2o2eEtKNFg1Wlgyb2tSY193eml3cUJ6M2ZoZDNRNFVoLXgxRWZZblBJN2xqZklteFExdDEtaEppU0RvZ1I1ZFFUYTExaGVteUxxSkxhOVJQMzhqTlluMGs0MFpGLVdNQ2lpQjQ?oc=5 | → 대표: 한때 ‘2차전지 대표주’ 금양, 과징금 91억…회계처리 기준 위반 - 한겨레 |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 | → 대표: 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 |
| kifrs | joongang.co.kr | 법무법인 지평, ‘AI회계감리대응센터’ 확대 개편 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE9vMHpYaEZibllYVUpNMThST2MxRi1ZelNUd3BBWG5qbVM4M2lSNEttSDRzRG5Vd3NrWGxyTFp0VHpBajV3Qll6ZmJIU3dtT2x3OGlpdU5n?oc=5 | → 대표: 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 |
| kifrs | crowe.com | 2026년 재무제표에 대한 중점심사 회계이슈 사전예고 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5lYjFWby1TbVI5SWdPLTdTQXdhX3lfdi1GektuUG5LQ0FLMDlDbWVsYm11S3o0ZDlXeEIwTlVxZzlmYVdDajVSUWJDY3FVSGZxSG1Ublg2M2E?oc=5 | → 대표: 「2026년 재무제표에 대한 중점심사 회계이슈 사전예고」 발표 - 법률신문 |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 | → 대표: ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 - 임팩트온 |
| esg | netzeronews.kr | 한정애 의원, 'ESG 공시 의무화' 법안 발의 - 넷제로뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE53MnVvandUR3lCRjExelB4MUhjVTBtRHU1eXlvVWcxTTFwQndfNzAwbHZXcUJscWN6QTY2VXEzbWpjQXlST3Q5ZkFNVlY1TjNHZEloQ0s0N1daOUtfVVRic1RYTG10ZjEwMFHSAW5BVV95cUxPTnl3czhTNWJlaWxSd0lYV1hJUW5CblZyV0ZfNDhNeGwxYkxGYTBPdnQxV2RUeFFMQ0V1dmgwN1hMOS0yVjh2MVZJMWEzRW0zVC1CZFNmUFlia19reFpQSm5lck5tS3RaM1ppaHU4Zw?oc=5 | → 대표: 한정애 의원, ESG 공시 의무화 법안 발의…사업보고서 공시·제3자 인증 의무화 - 임팩트온 |
| esg | asiae.co.kr | 與한정애, 'ESG공시 의무화' 발의…"초기 3년은 책임 면제" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5kc0hVZ1gwZWZJNEx0YlJQZ1JyaFVoM3ljSEpZU2c1SmVmODhDRW55NG94cTFlek5CcEEyX2ttRGl3cG9ydFV3S0poaXVtb1EwU1E5Z0FqUXktN0JiTUcyNw?oc=5 | → 대표: 한정애 의원, ESG 공시 의무화 법안 발의…사업보고서 공시·제3자 인증 의무화 - 임팩트온 |
| esg | netzeronews.kr | 닻 올린 'KSSB 법정공시 전환' 실전 나침반 "눈길" - 넷제로뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1XdmdXS2VwaGRQaGI0Zi16Zm40bkZYOHZYX1A0VDJmQkYxUEFhUVpkRHFocDdfaDAwTUNmd3AzWEFhMVEzdExpZzUxbVFjdlhNcmVwOXhjYUplUno0V2UwOWRqVUJBUWNNYlE?oc=5 | → 대표: [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 |
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | CPA뉴스 | 2028년 시작되는 지속가능성(ESG) 공시 제도화 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9YWWlTdzE5aE13VmhNQk4yZUJtZ0c1OVFDSzEzTFdlTDM3WnlMTHUxVzVPMVdtTTd0RHNNUko4alpKZXJFcmVlM2x6elFHTmp0TDIzVjVERjdScWk4U3Uza2htRTJuNXBz?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | news.mtn.co.kr | ESG 공시 의무화 본궤도…기후·거버넌스 대응 주목 - MTN 머니투데이방송 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1ZYjdkVUM3UXFLc1I4MndSOGxjVlBTLVdzQUUtcEdaaU9JSUU3ZVNIY1RuSHRlX0JCMGZYa2NLQUNISG02UmlCWEYxRnBZblB2ZnJVZHhpcHJZejlDcl9TM2Z1QW0?oc=5 | → 대표: "ESG 공시 의무화 대응, DX·AX 기반 공급망 관리가 생존 열쇠 - 한경매거진 |
| esg | 이데일리 | ESG 공시 의무화, 10조 이상 상장사로 확대…제도 안착 시험대 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9fZ280ZEZXcEFOWWxXV3Z5X2JXcGczQTRPcUNvTXVDdW5hQmlhZEVLTVhJZ0VRYnpJTHQ3cHdlMjg5QmlYZnBWN1BDU2hWZDlRMW5ub1lpMmk4QVFoODZpcndnVE1PcHU5Qmhsbmw1eU5iWHM?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | joongang.co.kr | 2028년부터 자산 10조 상장사 ESG공시 의무화…재계선 “기업 부담 가중" - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE00a0pwNnpEYU9UbzdhYUVGWThwVlY3OUlmRzVLaFM0azBDVkpHMGtDMVpPODZuZGJIbTJ4ZEI0XzRiMnV3aXpLbmk0T0QtcU95UXUyVWln?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | joongang.co.kr | [사설] ESG 공시 의무화…기업에 부담 떠안겨선 안 된다 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1hOUU4ajk1NHRSRnpIR2FqQ3FvWjNqOEJFc2kzZW40bjljbzVTdGg5d29zNkpQcTQtSWRMVkhsXzc0V1RWc1VsRWllN000NmtwS0NHT1Vn?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | kbthink.com | '자산 10조' 코스피 상장사부터 ESG공시 의무화…적용대상 3배 확대 - KB Think | https://news.google.com/rss/articles/CBMickFVX3lxTFB2cEF6d3NXUndnTFZnekVyU2x3clFpMHRDN250YVh5ZVRJMEp4bGw1b3lySlVkek5pQlRYZENZSDdKcDdtek11dkhqdk9XV01sRG9nOXk1ejExajZTS2dCZFBDN2QzVXI3dEdGZElfb2s4QQ?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | edata.ekn.kr | 2028년 ESG 공시 의무화…10조 이상 기업부터 적용 - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE9JT2doTTBTd2habVdUZVAwSWx6bWZnS0txQnF3SzF2U0ViU3d6TFMzOHBWa2FzMVBoUDY2cF9BRk1RQnZPekpZN2ZDMjdMYnNxcFg0ZjhFVElIY1FtbGc?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | newstree.kr | 'ESG 공시' 2028년 전격 도입...'자산 10조 이상 상장사' 의무화 - 뉴스;트리 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE54SllKYmtLZ0JmSEMydXBsTmNZVExUSm9wU0JpeUl6bnNCZXg5S1JQdWduMTJ0WjhRbHBxOV9HYVhQbDZRX1dfZTF5YjVESkhaOGR3LVdwaE11ZjlL?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | busan.com | 코스피 10조 이상 상장사, 내후년부터 ESG 공시 의무화 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTE1SUzNES21YX3JvS0hjM2RrSDRLMWY3T0VWOVBVV2k0UGZiM1NhalJ5MVltcHBPYmNqYlhPZzBuTDBPdDhBVmZOalo2cm5VVWV4SG5za3pieXg0c0J5OTRyMWp6NS1vOW0tS3V5NWM2ckNBeDhu?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | industrynews.co.kr | 2028년부터 ESG 공시 의무화…10조원 이상 코스피 상장사 대상 - 인더스트리뉴스 | https://news.google.com/rss/articles/CBMickFVX3lxTFBnbUN1eUlyd2Z1VXJaX3NPaU5kYmY5d2g5STNfUHFRS0YtdzhQNTBwdnpfTHJDd2JpLU9XLW14cGd5UUdIcm91c04tQnB3NmN6OFd1SzhpZWUtRVczV3lELTFFai1lRHFGdFV0OTRNOHlHUQ?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | dailyenews.co.kr | 2028년부터 연결자산 10조원 이상 코스피 상장사 ‘ESG 공시’ 의무화 - 데일리e뉴스 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5hMk8zYmhVcnF2ZkJsNjF3NDNJbkc1emcydW81Z0FyNGN5RmROVkgxanVqTjVuQ1l5WDNxTHNQRDBoYUlTbEJLWFVJcDBUXzFRYmtXeU40RndrZ3ZnaGtHUV9IU2hXLWJPMTVRemk0OA?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | news.kbs.co.kr | 2028년부터 자산 10조 이상 코스피 상장사 ESG 공시 의무화 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yUDBMT09RbHdJS3lzaFViRlBFTzNVTWNlazdaQjFTVW1Od3NoYkl4YzJsYjJMVWpaMGRZQW5YN19zb3ZLbWRtbE91TmUzRnhIVlJHaVN1cXNiX2M?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | newstomato.com | ESG 공시 속도전…2028년부터 10조 코스피 상장사 의무화 - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9ZeXBmQ2t4SVdHM0lZLWRqeGZtNUZtNVpNemExdTBtdVljaDkwbXo2REFqek1ucnFZZzUxT0VRakZMb2Z2WWg1YWRXdjAtcDlocm9ycXd6cmhiMTNhd2FqVA?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | ddaily.co.kr | ESG 공시 2028년부터 의무화…자산 10조 이상 코스피 상장사부터 적용 - 디지털데일리 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1YUXNzRnlKOTl2ZEl1M2ZZaUE3UzFEUDdzM1hpTS0wOVZmZU04OGc1LTFLRkFyTHI3VVlVa2VHVm1CMnByMHF1d3htY3lmZXhsN0k5M01aRWVmQ1hDWEsxVzJlU3U?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | seouleconews.com | 2028년부터 ESG 공시 의무화…“자산 10조 이상 코스피 상장사부터” - 서울이코노미뉴스 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1uXzhoQlR2VmpvZjBVaGdmZ0VkRHZkSEhOZjBycjVMVjFOb2E0dzFfaUJFTGUxc2NfTThwaE5QZ21GZ0RYSEpmWjhaOFFha1g0OXZ2ZS1IT1J4eEZiWWQ1OUtuMFhWb3BqcHhZUjZB?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | netzeronews.kr | ESG 공시, 2028년 자산 10조 대기업부터 의무화 - 넷제로뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1INGV3TERLZzY4TU81cmJYZjJNOGlhLWI1NV9abEtCYUNIUTdERkRhdjc2YkFDUFlnUkt6dDlyNE1RQjZKUkM1RGNFLVVpcFJtbHpPdHB4ZWdtWVhVQXp1NUxhbS1wX3hjcHfSAW5BVV95cUxPZ1UzMEY1SGNCcUpYUjFzTFhtMmRfZVRfNTl5MTQyRG9qX3A5bmFSUXY3UlhROWtvOTBiRFVSZF9TX1Q1QWh4dTQ1Y3VnTjk1aC1YcTV5YldnbTR4aVdiVGVIeGk3bndaV25Tc1VOdw?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | todayenergy.kr | 당정, ESG공시 법정 의무화...2028년부터 10조원 이상 코스피 상장사 대상 - 투데이에너지 | https://news.google.com/rss/articles/CBMibkFVX3lxTE95dVFuS3o4NUg1X2pQRGhTU0RyaVRCZXpkN0RldjJwb2hwOFhUVkU5TGFaQ0tGMVFCclVuaXFnVzN2UHBqenNoZlNFekhLYUw0dFltVm5wdWxMUklZWWpyOWtUZ3NSWTdDWUlkRUVn?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | newstomato.com | 당정 "2028년 10조 이상 코스피 상장사부터 ESG 공시 의무화" - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5DS1l5RDB1cmNuNVhUVmVKOS1ITTdzcE5FREZhRlcxS3l5cHhIRGdMUzVVM05zTE96OXJ3N190dUhmQjBWc2Vma2VHSnRXZmJxdVI0eHd1dHVMbThvMzlTMg?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | meconomynews.com | 당정, 2028년 ESG 공시 의무화... 10조 이상 코스피 상장사부터 - 시장경제신문 | https://news.google.com/rss/articles/CBMicEFVX3lxTE9VdlFtUmFYU3dDbWtJWml0R2ItcW5xRGFiR3dBSXZhSWFDdE94TmxZVFBPcjdOcTdsYmVSQ0EwNXNRVFZfaTBCSnhTR3BlUmwzUGw1bXFHRzlwVjdsMHNIZmstOGhjeVpDM211amNZZG0?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | thedailyeconomy.kr | ESG 공시 의무화 앞당긴다…2028년부터 자산 10조 이상 상장사 적용 - thedailyeconomy.kr | https://news.google.com/rss/articles/CBMicEFVX3lxTE9iUlgtTzA4U1Y1bmNLWTh6MkZtdHkzMFZ3WW1ER2RVb2VYWlhzajVVVzhTQ1R6aDBOUXpfaEVOdEZRMkFrWHA5X01VRm9KZlhVZmFhNDl4Y2RDUE5iVUVSWk9YOTJmLVI5aGptRktVUl8?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | hankookilbo.com | 당정 "2028년 '10조 이상' 코스피 상장사부터 ESG 공시 의무화" - 한국일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTE4yWXJVNm9pOHdLemdOMlZvX0VpRmJUUVREaXhUR1RNamVHRHY5YS1HRGtkT25yQWprbk5EUVZJdVFHcDdYRnk1M2hEUkIyemtPc2cxR2hJTDdZWld4YXpKdFE5RTRQLXdLWC1EMkZn0gFzQVVfeXFMUDQ0UnRCYXpTZzdnMGtGMFA5NVZibzlUbGxTaUtSNWZNMXlnTS1NbURhTzNld2ptZ3hTelBCVEpWYUtQak9YTndEVlZrM1RVcFR1bEdIV2Zfa2Q0eUZyUmRTeWxQNldtcXFYZUF5d21JTjdtUQ?oc=5 | → 대표: 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 |
| esg | 이데일리 | 이억원 "연결자산 10조 이상 코스피 기업부터 ESG 공시 의무" - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5YTjEwbmxBTWlJZUlPSkVCQ3JaTzJhOEZUUlVDaXh5LUx1cUZVXzE3QVYzUVFoaU1UU2ljMWhlRTZhRHFrODNKWUdRWTdFWUkwTjREanRHaEQwcmNoS0VkZXl1X0ZOTEZWNjI4RTFURTZkcUU?oc=5 | → 대표: 이억원 "연결자산 10조 이상 코스피 상장사부터 ESG 공시의무화" - 연합뉴스 |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| esg | biz.heraldcorp.com | KCC글라스, ESG 공시 해외로 확대…인도네시아 법인 성과 첫 공개 | https://biz.heraldcorp.com/article/10924977?ref=naver | → 대표: KCC글라스, 생물다양성 영향까지 공개…해외 법인 ESG 공시 확대 |
| esg | news1.kr | KCC글라스, ESG 공시 범위 확대…자연자본·해외 사업장 담아 | https://www.news1.kr/industry/general-industry/6342251 | → 대표: KCC글라스, 생물다양성 영향까지 공개…해외 법인 ESG 공시 확대 |
| esg | womaneconomy.co.kr | ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 | https://www.womaneconomy.co.kr/news/articleView.html?idxno=259937 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 |
| esg | paxetv.com | 상장협, ESG 공시 실무교육 실시…2028년 의무화 대비 지원 | http://www.paxetv.com/news/articleView.html?idxno=284514 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 |
| esg | enewstoday.co.kr | 상장협, 'ESG 공시담당자 실무 쟁점' 과정 개설 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2481878 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 |
| esg | dailian.co.kr | "차질 없는 대응 지원"…상장협, ESG 공시 핵심실무 쟁점 대비 | https://www.dailian.co.kr/news/view/1703168/?sc=Naver | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 |
| esg | newsis.com | 상장협, ESG 공시담당자 대상 실무 과정 진행 | https://www.newsis.com/view/NISX20261019_0003831375 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 |
| esg | seconomy.kr | ESG 공시 2028년 의무화···자산 10조 기업부터 ‘탄소 성적표’ 공개 - 공유경제신문 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9qMnQ5d3NHZXBuaEV3TV9nbUVLaW4zQ0VvN2owejZfcW1ZVHM5WmRVSVlJaV9XcEJFQzBXSE1TTmRjQzA0S1o3bDRkaUQzWnIwcTBXbFhMUTdCRG9lLVhfbG5tb3FqY3RmMUE?oc=5 | → 대표: ESG 공시, 2028년부터 대폭 확대…자산 10조 이상 코스피 기업 의무화 - https://www.thedailyeconomy.kr/ |
| esg | socialimpactnews.net | 경제·환경 단체, ESG 공시 로드맵 '실효성 논란’ 제기…"국제 표준 준수해야” - 소셜임팩트뉴스 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5MWWUxdDB2Zm1PSWJWYUJ5aWZnc1pYWE1iVUJ5ekppZ1NrNUJBT3p2bzFFYUF1X0RCMl9hQ3JXSE5sT0V0alA3TnhTa1F2MVRFWldOckNVbzcyRWZYY1phcmthR3ZKeEN2ZmJraGI3eUU5bk0?oc=5 | → 대표: 성명서·보도자료 경제·환경 단체 ESG 공시 로드맵 '실효성 논란’제기, 국제 표준 준수해야' - 환경운동연합 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## collect:event_announcement (11건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | 2026년 글로벌 ESG 교육 워크숍 안내 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2199 |  |
|  | 금융위원회 | 생산적 금융의 온기를 지방과 중소기업까지 이어갑니다.   - 이억원 금융위원장, 제6차 생산적 금융 대전환 회의 개최 | https://www.fsc.go.kr/no010101/88052?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 제9회 ‘회계의 날’ 기념식 및 회계업계 간담회 개최 | https://www.fsc.go.kr/no010101/88031?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
| kifrs | 임팩트온 | 【ESG 동향】한국회계기준원, 지속가능성기준 자문위원 10인 위촉 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5GdEh2bUpxaThMUk9PMWdLREFEYmpoVTBmV2o2M2JUY2RINHVqNVBWQ1I0ZVVVMWhUSzNHMFJFTFlKanVTT2NOV0FhQTZ2aWJWcXBDZzVXU1ZteEl5RWh3bmd5V3pFUExRV1E?oc=5 |  |
| tax | 한국세정신문 | 세무법인 아성·아성ENL, 제1회 아성ENL 특강서 지목한 기피하는 세무대리는? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE4tU0lVb0ZaQUNvSlR4RTVuemtKcF9LemhSTk16SHNiNEZ1dEpUc1F4MGFWbEhZdFVib3l5SnhWQ0lLaGFPdDloazNGU1Y4WWxDLUY0OW80Z3pWZjExeVlBblVGZE4?oc=5 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| esg | betanews.net | 네이버, ‘2026 지속가능경영유공 정부포상’ 대통령 표창 수상 | https://www.betanews.net/article/view/beta202610300070 |  |
| esg | ESG경제 | [알림] KSSB·ESRS 이중중대성 평가 웨비나 초청 | https://www.esgeconomy.com/news/articleView.html?idxno=17019 |  |
| esg | news.tf.co.kr | 동아ST 지속가능경영보고서, '2025 LACP 비전 어워즈' 수상 | https://news.tf.co.kr/read/economy/2361168.htm |  |
| esg | ttlnews.com | 동아에스티, 지속가능경영 유공 종합 ESG 분야 산업통상부 장관 표창 | http://www.ttlnews.com/news/articleView.html?idxno=3157355 |  |

## collect:incident (4건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | ddaily.co.kr | “부채비율 179%가 119%로, 왜?”…제이알리츠 주주연대, 회계처리 수사 요구 - 디지털데일리 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1acUhETFNSZWJUakZLTHRvTWxNaHpGTjJmU1k1NG1uenh6ZEFVYWRIeUNiLWNrNEVQMl9XMVV6cExzUml0UVhOQlpfVlRtSXctQm9GUDBqdjgwNVdJNTlXODI0dWQ?oc=5 |  |
| kifrs | 머니투데이 | 증선위, 코스닥 상장사 피델릭스 '회계기준 위반' 고발 조치 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBzNHNDbVFWaDFDNk1nWXdVWW9hZnBpWV9qMXNTSkxBTEthWHM1RFZFb3UtaFE3M1hvZXR5d2ROdC1WaDRMSVJuZ0d6TEJabTR5VmtJbVB6eVZNbWRfNW5Yc3ZBLVJ4UUJ00gFuQVVfeXFMT21rM0lwdWF2UFFfLU5PN0FQUHFtMzl3OW1aZ2UwRm1BTGwtTHY4WWhFb2d3bC0yczhJM3Vmemd1VjFoWk0xc3VKVUF2RzFyU21vT3ZBbnE4RHQxRjRlQnMwajhTSlVuQW85Yk55RVE?oc=5 |  |
| kifrs | news.einfomax.co.kr | 금융당국, '상폐 위기' 금양 검찰 고발…회계기준 위반 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE4tV2cwN0F0UnBSSEg1N2FxSnlKY2JBSk5URk1SelBmemVXOHRwdllqZXFObW1RV002dUczNjI2UHMxMFdZcl9fNFNtSk5QM090ck5MNnBRdjJTcVJyUXFXU2c5eWUtSllrdTZwbmdQNjU?oc=5 |  |
| icfr | 한국경제 | 외감법은 경찰, 자본법은 중수청…분식회계 수사 차질 불가피 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wOF91b3FKNTlVV3FUM3J2amdHek9VS29CTHZ1N3d3NFJiOWtOakNkRVRPSzhFd3ZKMHM3RkRmcW9QeE9hRFV4NHNhbmQ5Q0RSNUpIbEYyOG9zUQ?oc=5 |  |

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
|  | 금융위원회 | 2027년 금융위원회 예산안에 대해  자세히 설명드립니다. | https://www.fsc.go.kr/no010101/88074?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 코너스톤투자자 제도 등 도입 관련  자본시장법 시행령 개정안 국무회의 의결 | https://www.fsc.go.kr/no010101/88071?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 글로벌 해킹 위협에 대비한 국내 가상자산사업자의 사고대응력 제고를 위해 긴밀하고 신속하게  대응해 나가겠습니다. | https://www.fsc.go.kr/no010101/88054?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융정보분석원, 국제자금세탁방지기구(FATF) 총회 참석 | https://www.fsc.go.kr/no010101/88048?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 불법 가상자산 취급업자(특금법상 미신고 가상자산사업자)에 대한 수사의뢰(DAXA, 3건) 및 접속차단(2건) 요청 | https://www.fsc.go.kr/no010101/88039?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 한국의 풀뿌리 금융,  미소금융이 다시 한번 도약합니다. - 미소금융 재원 기부 협약식 개최 | https://www.fsc.go.kr/no010101/88029?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 국민성장펀드가 국내 최대 태양광 발전소 건설과 반도체 밸류체인 경쟁력 강화를 지원합니다. | https://www.fsc.go.kr/no010101/88028?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 퇴직연금 기능강화를 위한 노사정 합의로 노동자의 든든한 노후소득 보장체계 구축 | https://www.fsc.go.kr/no010101/88027?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(국세청) | 주식 양도소득 기본공제 누락분, 국세청이 먼저 찾아 돌려드립니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787734&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 코너스톤투자자 제도 등 도입 관련  자본시장법 시행령 개정안 국무회의 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787776&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 2027년 금융위원회 예산안에 대해  자세히 설명드립니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787795&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |

## collect:noise_keyword (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | g-enews.com | [특징주] 해태제과식품, 회계기준 거래 정지 후 재개 첫날.. '급락' - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPbkZaRjEwOU9SRDR0UFAzcFRJVjNDZlBIYVRja29fcXRlcXY5T05ORVo4cTdtZHV2amlSR3hOOFlzUGFSUXJzNjlBMVNSX2V6RG16bXdUckxxd0hsSUw3b0xZTFNTR2tYX1VMa1RMRURYX1c2LXA0d3BHM0Q2QkJEOGY3VHJ4aUZX?oc=5 |  |
| kifrs | kookje.co.kr | [차호중의 재테크 칼럼] 재무제표와 주식투자 - 국제신문 | https://news.google.com/rss/articles/CBMijgFBVV95cUxQYXduYXB0OEt4UUlDY015R3pmVV8xYm5lLUhFWUUtYWFiV0Y3bGVDMGZtZkJwOW9nMlVYcFNyblI3bFRvcTRXbnVXajZaMzNBNkpYLVhEcWl2RUh4QmcyZlo1aEIySm54dTV2MHBybWs5RkxjV2VRd2NfR0loRDVuNmdvY1lmcHlibS1nWkV3?oc=5 |  |

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
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(5차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 본인 인증 서비스 일시 점검 안내(2026. 10. 17.(토) 21:00 ~ 2026. 10. 18.(일) 05:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [한국회계기준원] 2026년 하반기 추가채용(연구직-회계기준 연구원) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [KARI REPORT] IFRS 16 도입 이후 리스 기반 영업구조 하방위험 가시화와 정보적 함의 : 사용권자산 손상차손을 중심으로 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 회계기준위원회 상임위원 초빙 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [세미나] IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/calViewA.do?seq=1129 |  |
|  | 한국회계기준원 | [세미나] 회계기준원-환경산업기술원, 지속가능성 공시기준 이행지원 세미나 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1127 |  |
|  | 한국회계기준원 | [세미나] 한국회계기준원 개원 27주년 세미나: 지속가능성 공시, 새로운 기준의 시대 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1125 |  |
|  | 정책브리핑(교육부) | 의대 신설 지역/대학 선정 및 정원 배정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787886&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 복잡한 외자구매 간소화해 수요기관 부담 낮춰 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787888&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 의대 신설 지역/대학 선정 및 정원 배정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787884&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 계약현장과 소통하며 공공조달 개선방안 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787887&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 순국선열의 날 기념식， 한 편의 뮤지컬 서사극인 '공연형 정부기념식'으로 새롭게 선보인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787879&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기상청) | [2026년 10월 기후특성] 변동 컸던 10월, 상순 건조 → 중순 이상고온 → 하순 잦은 강수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787885&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 중국 산동행정 연수단, 조정원 방문…선진 분쟁조정 노하우 배운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787878&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 우수 임업경영체 찾아 현장중심 산림지원 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787883&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 충청북도 산불 대응 역량 강화 교육실tl | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787881&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 네이버와 중소 IT 기업, 공동으로 재취업지원서비스 시행! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787877&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 'AI(인공지능) 기반 디지털 감사 및 적극행정, 사전컨설팅 활성화'를 위한 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787876&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | '통합적 진로교육을 위한 생태계 구축' 추계학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787875&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 안전 필수템 '위험성평가'를 통해 모든 일터를 안전하게! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787874&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 희귀？중증난치질환자 건강보험 본인부담률 10% → 7% 인하 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787872&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 실물 인공지능 융합 기업의 현장 목소리 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787873&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 「지식재산과 혁신」 지식재산처 제1호 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787871&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 제33회 ｢외국인 인권보호 및 권익증진협의회｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787870&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) '바다의 경주' 태안 마도해역에서 고려 난파선 두 척(5·6호선) 발굴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787865&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 한국전통문화대학교, 전통회화전공 기획전시 「Memory: 전통과 오늘이 만나는 자리」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787862&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 5극 3특, M.AX로 여는 새로운 투자기회 ｢인베스트 코리아 서밋(IKS) 2026｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787869&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 제33회 ｢외국인 인권보호 및 권익증진협의회｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787861&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부, APEC 외교통상합동각료회의서실용적 협력과 기업친화적 통상환경 조성 강조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787868&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한-프, 통상현안 및 첨단산업·기술 협력 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787867&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | AI와 탄소소재, 첨단산업의 미래를 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787866&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부-AMD, 인공지능 반도체 협력 본격 가동... AMD 대표 인공지능 행사도 한국서 첫 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787858&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K팝 추고 태권도 품새까지…킨텍스 달군 K-로봇 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787860&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 중견기업을 세계적 기업으로 날아오르게 할 10대 초격차 기술 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787859&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '한글 점자' 탄생 100년, 「점자법」 제정 10년 만에  첫 점자 교원 20명 나와 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787856&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한글 점자 '훈맹정음' 반포 100주년 의미 되새긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787855&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식품안전나라 'AI 기반 검색'·'자주 찾는 민원'으로 쉽고 빠르게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787852&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 생성형 인공지능 시대, 저작권 기술의 미래를 논하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787854&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 덜 짜고 덜 단 식품 선택의 폭 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787851&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-폴란드, 방산·배터리·인프라 분야 실질협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787853&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "소방차량 오염관리, 현장에서 해법 찾는다" 국립소방연구원, 산업안전보건연구원과 소방차량 오염환경 공동 평가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787850&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청, 제79회 '불조심 강조의 달' 운영 국민과 함께 겨울철 화재예방 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787849&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 2026 아시아태평양경제협력체(APEC) 외교통상합동각료회의 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787847&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 전국 동물원 질병관리 실무자 한자리에 모여 선진 관리 체계 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787848&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부 장관, 배추 등 가격 하락 김장채소류 실질적 소비촉진 대책 추진 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787857&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국민인공지능서비스혁신추진단, 전문임기제공무원 2차 공개 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787846&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 청년들의 창의적 아이디어로  합성생물학의 미래를 열다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787845&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 최휘영 장관, 전북도지사 만나 '2036 하계올림픽' 유치 현안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787813&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 응급실 등 필수의료분야 수사 가이드라인 마련 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787811&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제7차 한-스위스 정책협의회 개최(11.3.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787812&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 상습체불사업주 777명,  1년간 신용제재 받는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787810&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 정부, 여수·순천 10·19사건 희생자 고(故)박찬길 검사 유족 제기 국가배상소송 항소 포기 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787809&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 새로운 IgA 신병증 희귀 치료제 허가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787808&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 위기채무자 지원 강화를 위한 업무협약 체결식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787806&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 김진아 2차관, 국제해양법재판소(ITLOS) 소장 접견(11.3.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787805&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "중복지적으로 인한 5,159세대 대지권 미등기 문제, 16년 만에 조정으로 해결" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787803&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 인제 자작나무 유아숲체험원 안전관리실태 특별점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787802&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 고 안성호 이등중사 호국의 영웅 귀환 행사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787800&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 한파 오기 전 한랭질환 예방 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787799&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | "새만금에서 일하고, 전북에서 함께 살아요" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787792&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 모듈러주택 산업 현장소통을 위한 규제합리화 현장캠프 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787791&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 휴머노이드가 '일하는 법' 배우는  데이터 생산기지 문 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787790&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세평가분류원, 2026년 '관세평가·품목분류 연구논문 및 판례평석 공모전' 우수작 선정·발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787788&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 대한민국 제조업 판 바꾼다... 산업부, 제조AI 4단계 확산전략 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787789&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 생활공간에서 의료서비스 받는다, 전국 최초 의료집중형 장애인거주시설 대전 '로뎀' 개소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787787&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 소비자생활협동조합 지원과 육성을 위한 ｢소비자생활협동조합법 시행령 개정안｣ 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787785&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 원안위원장, 한빛 원전 현장 안전점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787786&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "예술 활동이 멈춘 때에도,  고용보험이 힘이 됩니다" 근로복지공단, 방송 연기자 축제 찾아 예술인 고용·산재보험 안내 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787784&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 민관이 함께 자살예방·생명존중 위해 협력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787780&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 말하기 어려웠던 연구 현장의 목소리, 익명의 문자 한 통(1551-1441)으로 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787779&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과학 탐구의 결실 한자리에, 제72회 전국과학전람회 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787778&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 공무원미술전·공직문학상 수상자 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787781&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 지역 교육의 새로운 도약, 43개 교육혁신선도지역 시동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787782&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | "배고파 훔친 즉석밥, 경찰은 처벌보다 생필품을 건넸다" 경찰청, 경미범죄 심사위원회 우수사례 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787783&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 안전한 대불산단, 실천으로 이뤄낸다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787775&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 산업안전보건본부장, 대불산단 불시점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787761&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 외국인투자기업,  한국 산업의 든든한 동반자 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787764&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 「고용상 연령차별금지 및 고령자고용촉진에 관한 법률 시행령」 및 「남녀고용평등과 일·가정 양립 지원에 관한 법률 시행령」 개정안 국무회의 심의·의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787760&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 소비자생활협동조합법 시행령 개정안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787758&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 생산자·소비자 함께 '감탄' 벼 수확·유기농업 가치 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787769&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 2026년 농촌 체험학습 프로그램 우수 사례 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787767&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 폴리텍대학, 정규수업으로  '한국인정기구 합격증'까지 챙긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787759&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 행정규제기본법 시행령 개정안 국무회의 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787762&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 11월 12일부터 다세대·다가구주택  면적 제한 1,000㎡로 완화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787763&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 국산 열풍건초 이용 확대 현장 목소리 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787765&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 가을철 시설 딸기 잿빛곰팡이병, 습도 관리 중요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787755&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 보행 불편한 장애아동·어르신 주차 편의 높인다, 「장애인 등 편의증진법 시행령」 개정안 국무회의 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787757&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 특허심판 분쟁, 현장에서 답을 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787754&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 해외 생산제품과 달라도 기술·기능 유사하면 국내복귀 인정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787751&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 건축내화재 KS, 현장 제품 특성 반영과 안전성 강화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787750&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K-수출스타 참여기업 수출액 34% 증가 '모두의 수출'  성과 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787748&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 적극행정 공무원 보호 강화...'보호지원단' 신설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787753&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 디지털 미디어 문해교육, 학교 현장에서 새롭게 만들어 가다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787739&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | '국가 긴급현안' 해결 속도 높인다, 국민 안전을 위한 긴급과제 기술개발 즉시 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787732&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 정부 인사업무 특화된 인공지능 업무시스템 첫 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787735&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 동아시아 기록관리 전문가, 한 자리에 모여 기록관리의 미래를 논하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787745&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 폭염 피해자 지원 사각지대 최소화, 관계기관·전문가 TF 첫 회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787743&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 디지털네이션스 · OECD 무대에서  인공지능(AI) 정부의 미래 논의 선도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787741&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제3차 고준위 방사성폐기물 관리 기본계획 수립을 위한 국민 의견수렴 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787738&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 숨은 물그릇 확보, 홍수예측 고도화로 올여름 홍수 대응 역량 높였다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787737&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 11월 멸종위기 야생생물로 고니 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787736&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 가축전염병의 선제적 차단과 확산방지를 위한 K-가축방역 개선대책 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787733&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 산불방지대책본부 운영, 예방활동강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787722&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 군부대 "맞춤형 산불 안전교육" 성료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787720&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국장애인고용공단,  노사 함께 중증장애인 문화 체험활동 펼쳐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787726&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 서울-양평 고속도로 신규 타당성조사 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787718&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | GTX 삼성역 안전 확보 방안, 안전 최우선으로 검증 거쳐 연내 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787717&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 인공지능(AI)과 공간정보가 바꿀 미래 11월 4일 킨텍스에서 만나세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787716&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해양수산 공적개발원조의 새로운 길을 찾는다, '2026 해양수산 국제협력 콘퍼런스' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787715&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | Blue connect : 미래의 바다로, 이어진 기술로! '2026 해양수산과학기술주간' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787714&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 수산 현장의 아이디어를 성과로 이끈 '2026년 수산신지식인' 3명 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787713&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 한 컷으로 만나는 미래의 씨앗  '제2회 종자사진 공모전' 수상작 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787712&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 검역본부 서울지역본부, 광견병 항체가 시험 분야에서 국제공인시험기관(KOLAS) 인정 획득 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787711&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 해외 바이어부터 필리핀 정부까지…  K-농기계 수출 확대 협력의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787710&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | AI·디지털·로봇 식품 제조부터 고령친화식품까지…K-푸드의 미래 성장 해법을 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787709&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 청소년의 시선으로 전하는 따뜻한 위로, '너의 곁엔 항상 우리가 함께해' 특별전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787724&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 간병인력 전문성 제고 위한표준교육과정 시범운영 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787723&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제47차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787706&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 교제폭력이 시작되는 '지배·통제' 단계부터 피해자를 선제적으로 보호하는 「스토킹처벌법」 개정 적극 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787705&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 민간·공공 협력으로 결핵 발생 66.2% 감소, 지속 가능한 결핵 퇴치 전략 모색(11.3.화) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787704&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 해외취업 지원사업 우수사례 공유의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787702&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 한빛(영광) 원자력안전정보공유센터 본격 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787700&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 안데스 산맥 빙하호 범람 가능성 대비 본부-공관 합동 상황점검회의(11.3.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787699&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 사전예방 중심 보호체계 혁신, 인공지능 보안 대응 방향에 대해 각계가 함께 모색한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787701&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | "연결을 넘어, 인공지능 만드는 새로운 가치"  「2026 대한민국 지능형 사물인터넷 주간(2026 AIoT Week Korea)」 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787697&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 국제 신용평가사 Fitch, 한국 연례협의 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787703&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공시의무 위반에 대한 과태료 부과 고시 개정·시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787695&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 청년 노동자의 장시간·공짜 노동 근절을 위한  장시간 노동 기획감독 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787696&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 2026년 제14차 아세안+3 HRD 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787694&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 2026년 공공백신 연구개발 성과교류회 개최(11.3.화) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787689&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금 개발 대전환  - 개발목표 2050년에서 15년 앞당겨 2035년으로 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787690&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 국민 10명 중 7명 "노동교육 필요"… 의무교육 제외 경험률은 8.8% | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787685&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 11월은 고용차별예방 강조의 달..전국 6개 차별개선센터 합동 캠페인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787684&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, '제4회 특별성과 포상금제' 수상자 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787688&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(조달청) | '혁신조달 탑티어' 레메디 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787730&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 군수품 '무분별 입찰' 막고 장병 안전 지킨다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787729&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 국립문화유산연구원, 한국고고학회와 「제50회 한국고고학전국대회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787681&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 공장인허가 사전진단 서비스, 더 쉽고 편리해 진다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787683&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 글로벌 의약품 규제의 미래, 서울에서 논의한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787674&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | (국영문 동시배포) 국제 전문가들과 무형유산 정기조사 발전 방향 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787679&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청-대한암협회, 암 투병 중인 전승자에 치료비·간병비 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787672&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 2차 중앙행정기관 이전, 국민 의견 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787678&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(감사원) | [사전컨설팅 12] 개정고시 시행 전 위반행위  완화된 과태료 기준 적용으로 국민부담 경감 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787746&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | "모두의 꿈이 꿈틀대고 연결되는 곳" 2026 청소년비즈쿨 페스티벌 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787675&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 적극행정 우수 공무원 선정... 20년간 쌓은 행정 자료 인공지능(AI)로 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787671&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 세계 최고 수준의 3,600톤급 디젤잠수함 '서희함' 진수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787670&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "11월에도 달리는 국민신문고는 전국 순회 중"… 이번에는 거제·하동·진안으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787668&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 세계 무대에 나갈 우리 글과 그림, '2026 대한민국 그림책상' 수상작 9편 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787667&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '2026 월드 웹툰 어워즈' 본상 수상작 10편 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787666&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 5·18 민주화운동의 진실을 세계에 알린 '고(故) 위르겐 힌츠페터 10주기 특별전' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787665&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 가을배추·무 풍작, 올해 김장은 부담 없이 '한 포기 더' 담그세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787658&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 10월 소비자물가동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787662&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 10월 소비자물가는 2.8% 기록, 김장재료 수급안정 위해 역대 최대규모 김장대책(640억원) 시행, 동절기 농축수산물 수급 안정 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787669&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 가을배추·무 풍작, 올해 김장은 부담 없이 '한 포기 더' 담그세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787657&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 축·수산물 안심, PLS 확대로 한층 PLuS! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787659&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-불가리아 경제공동위 7년 만에 재개…교역·투자 확대 및 방산·원전 협력 강화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787661&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 국립소방연구원, 공주 신청사 시대 열다... 새로운 도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787664&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 공장 지을 곳 더 찾기 쉬워진다,  스마트폰으로 입지·규제 미리 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787656&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 성평등가족부, 청소년 디지털 안전을 위한 플랫폼 사업자 책임강화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787773&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 다양성(DEI), 이해를 넘어 경영 현장 적용으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787771&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | '26.10월 소비자물가 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787687&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 물가관계차관회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787686&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(인구전략위원회) | 김진오 인구전략위 부위원장, 국립재활원 현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787731&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제17차 한일 차관 전략대화(11.2.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787655&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 가습기살균제 배상 심의위원회 위촉식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787654&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 가을철 산불방지대책본부 본격 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787622&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 더 강한 해경, 더 안전한 바다 구현...2027년도 예산안 2조 2,291억원 국회 심사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787620&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청, 현장 중심 특별성과 발굴해 포상금 1억 360만 원 지급 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787619&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 변화하는 수사 환경에 맞춰 전문성 높인다... 해경청, 전국 수사경찰관 역량 강화 연수 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787618&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 송미령 농림축산식품부 장관, 충남 서산 벼 수확 및 쌀 수매현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787617&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 규제합리화 라이브클럽 현장 간담회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787616&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 「의료데이터의 안전한 학습·검증·활용을 위한 국가 AI 인프라 구축」 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787615&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 제69주년 '112의 날' 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787614&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부 장관, 쇼핑축제 현장 찾아 세계인의 장바구니에 K-소비재를 채우다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787613&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년도 대규모 통계조사 업무 유공 포상 전수식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787612&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 콩 생산자·가공업계 손잡고,  국산 콩 소비 확대 나선다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787608&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 문체부와 국토부, 관광교통 칸막이 허물고 '지방관광 시대' 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787609&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 무주국유림관리소, 가을철 산불조심기간 대비 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787611&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 제7회 임업인의 날 기념행사에서 정부포상 전수 등 임업인 격려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787605&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 문체부-국토부, 관광교통 칸막이 허물고 '지방관광 시대' 연다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787603&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 기업이 만드는 지속가능한 노인일자리, 기업 상생 협력 성과 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787606&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함양산림항공관리소, 가을철 산불 대비 총력 대응 체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787602&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 유엔생물다양성협약(CBD) 당사국총회 공식 문서에 이름 올려, 글로벌 산림 리더십 입증 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787600&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국가 드론·대드론 전략 추진단 출범식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787596&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 충남 서산 야생포유류 삵에서 고병원성 조류인플루엔자(AI) 검출… 예찰·방역 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787595&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 넷제로 챌린지X 민간 투자기관 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787594&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국무조정실장 개발협력주간 홍보존 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787593&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처장 화장품 점자QR코드 자율표시 지원 행보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787592&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 박홍근 장관, 호국 보훈단체 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787591&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 미셸 박 스틸 주한미국대사 접견 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787589&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국가기후위기대응위원회) | 넷제로 챌린지X, 민간투자 5개 기관 신규 합류 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787588&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 시민과학으로 함께 지키는 산림유전자원보호구역 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787587&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 공공공사 페이퍼컴퍼니 차단부터 AI 업무혁신까지…조달청, 직원 11명 특별성과 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787728&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 우리의(지구를 위한) 기후행동, 전기차 전환 서명에 동참해 주세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787692&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 국내외 석학·현장 과학수사관 한자리... AI시대 과학수사관의 가치와 역할 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787583&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한국과 베트남, 문화산업 분야 협력 강화 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787582&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(소방청) | '가을철 산불 예방 위해 전국 화재위험경보 경계 발령"… 소방청, 화재위험경보 대응체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787663&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "기술 배우고 싶은 국민 누구나" 폴리텍, 직업교육과정 교육생 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787581&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 표준과 지식재산으로 여는 피지컬 AI 시대, 글로벌 주도권 확보 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787578&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 기획예산처, 2045 국가발전전략 수립을 위해 미래전략 전문가와 심층 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787576&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함양국유림관리소 "가을철 산불방지대책본부 가동" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787571&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함양국유림관리소, 소나무재선충병 차단 '공동방제' 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787569&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한-싱가포르 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787567&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 아세안 확대 국방장관회의(ADMM-Plus) 계기  한·베트남 국방장관회담 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156787566&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-04&endDate=2026-11-04&srchWord=&period= |  |

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

## collect:tax_subject (50건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | karnews.or.kr | [세법톡톡] 2026년 세제개편안 (양도소득세) - 한국부동산뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Ub0liX2hObkdsdUhZc3lES3AycE9NV2xfVHBvMDJNYXpkbkVZNi1FdlZKcklqUndyX0xoZXB1OUFDdHNkZWNHa1BQN1FWMHBMUlZhV2V1ckpvRWUwZVpzZFctNllmUFd3bHZB?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | news.kbs.co.kr | 부부 공동명의는 진짜 불리할까? 세제개편안 오해와 진실 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5yTUo1c2FfUGVDcERxc2lJM0JHSUItNks1N083NkViV1Z2VHFnSWFUdjdHYnRyUE9fSUoydEg0ekNnY0xVRlBiTEkzYWlBYkplV3p4UjctSkVGVlU?oc=5 |  |
| tax | lawtimes.co.kr | 가업상속공제 제도 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE0tZHB3U0FDMU95aVE4TFFlMFh1ZW1zRkJyQ0ptMXowNTdiOXF6dFhXczE1ZVdDNTRxZ0kxUEhlVVNHZDhKdkl5TWFUR3lmQk5WNGNEYVpzRl9lMDlySGVSak01S3psQ1RCNTdxZXN30gFyQVVfeXFMUEpkOVBWUEI2ODBteGUyTHZMOWxkSVJGS0twRmk4V3ZmZ2g3RkliS3VyTzBJR3VEQVYxSWlaZmo5bDluYVpZTThqdGYwMXlESnpraENELU9vcVViTkp2dEVoaWxfU3NnUmVIaU1oREpQbTlB?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzDSAWBBVV95cUxOeDlrTWJMLVFFUHdRdGFKSnZYenV2UWl2UnZxTUtyamE4YUNfSjVfSzNHY2U4eEQ1X096RGc2aE9BN3dMUGlnaE56N1I2c2c0bkZkVTR0a1lJR1pUQWxUSGk?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | newstomato.com | (8·3 세제개편 한 달)종부세 후퇴…정책 신뢰 ‘실종’ - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFAzbGtwN19uMk0xRExHYUtyLTVMalFQeVp5U2FtSno4N2IyOUlVbXRXRE92TnBqUjl2TS0tYW4zdWNoSmRsMjhwZVhPZ04xZUVHVVlEajBMSzF1Y25hdXdfWA?oc=5 |  |
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
| tax | jinju.news | 김태호 의원, 지역균형발전 강화를 위한 지방교부세법 개정안 대표발의 - 진주인터넷뉴스 | https://news.google.com/rss/articles/CBMid0FVX3lxTE44X0w1UUNpbTMtSnZFa2ZpdUF0dHhxeU5GWFlWNF9NZTY0aWRNWGJlS0lLMEJFc1lERHd0MFBubjhHUVBERlVKT204VjQ2TlIxb3drSUJfV3FyMWcxX1RONzUxWE9LMzkxY2VGZVBCVjl5WVlnTUp3?oc=5 |  |
| tax | kookje.co.kr | 정부 세제개편안 국민 찬성 3.1% 불과…입법예고 기간 ‘반대 의견’ 쏟아져 - 국제신문 | https://news.google.com/rss/articles/CBMijgFBVV95cUxNRHNJc0pOSy1JMGZwempWODVMWDZzeUpqSXZNb1FNMTM5bUNJcGxGSkk2ZV9fZXNodDIzLWJ4YXpDSHpLR2ZHLXk5d3ZwZVptRE5SazBpTWEyeHlLOTNZU1ZSemc5ZVFTdUZiTC1uMUNtWk9hUzdHV2lmTHlxWEZ4TjhVMlZIOFFXS3RrZ2pB?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | newsk.net | 세법 개정안의 주요 변경 사항 : 한인동포신문(몽골) - 뉴스케이 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBXdlRVQnREMG5BcGNrUjNUdF9MSEVtbGJzdHBuWjNBM29ZTDBtYXY5TWw4Q1F4OG1QMlVSZnQ1YTNYMEpBcmJKX1hhTDJOczE0UTQ5VnlRY1FmZw?oc=5 |  |
| tax | nbnbiz.co.kr | 정부 세법개정안 속 ISA 대수술에 투자자들 거센 반발 - nbn 시사경제 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE15SE5vWnlDRVAwMGxJRDZfdVlLX2l1SXdjaC1PbHRKd1NVN3VuTG9jdkNFSFFmdGY2MW0xeDFfSmljS1prNlJndHhOdUt5Q05SWGg0a0Z1MXJTWGllOGRfS05ySFk?oc=5 |  |
| tax | newsis.com | 이형일 부총리, 세법 개정안 관련 제안설명 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE14d2tkM2pvUlBhZ1lJRlFtdVVoWnU0RVd6X3Q5UWhQWC1VcHJiSUJJWTAtRFpCSjY2Z3ZCV25id2cwSGtYX3pDemxTVEk0YThibk90a3MyeVdhUE83QWYwdw?oc=5 |  |
| tax | imaeil.com | "살면 보유세, 팔면 양도세 폭탄" vs "서울시장 책임" - 매일신문 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wQTFnTkQ1OWM0OU9vQmh4ck9wdk5Sb0pzdkZZX0tKNzNXbDdNWWlNVGJGTnlyVjliRThaZG9mZUhCVGZjWU9CeUZDSEZMZUV4N3o1cFBZcjVFQ0J4Yi14QXNn?oc=5 |  |
| tax | paxmedicalnews.com | 2026 세법개정안에 병원계 ‘발끈’… “가업상속공제 제외는 필수의료 사형선고” - 팍스메디컬뉴스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1Dd3lHSEFoSWkzMDJXZVAwcnpDVjkyLXJYa0gwVURLSWJjeGhfTVZnV2pnVTZfdWdqTU1sZU9wM093UDhoT2dmUDdtVThCc3o3VlZEY3lVbzFuQTZCX3N6bHlvSDhrekpTdFFKcWpId3A?oc=5 |  |
| tax | thevaluenews.co.kr | 국회예산정책처 “2026년 세법개정안, 5년간 세수 14.5조 증가” | http://www.thevaluenews.co.kr/news/view.php?idx=202849 |  |
| tax | ftoday.co.kr | 국회예산정책처, "세법개정안 따라 5년간 세수 14.5조원 증가" | http://www.ftoday.co.kr/news/articleView.html?idxno=368597 |  |
| tax | chosun.com | 수십조원 ‘세수 펑크’ 원인은…세법 개정, 우크라 전쟁 등 변수 반영... | https://www.chosun.com/politics/politics_general/2026/10/27/ICBT5YQXINCPDMGFZSEEMNWJJA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | gokorea.kr | 국회 부동산 세제 개편안 논란, 비거주자 세금 폭탄의 진실은? | https://www.gokorea.kr/news/articleView.html?idxno=884004 |  |
| tax | womennews.co.kr | 서울 아파트 매물 8만건 넘어...8.3 세제 개편 이후 33%↑ | https://www.womennews.co.kr/news/articleView.html?idxno=284089 |  |
| tax | tfmedia.co.kr | [전문가 칼럼] 2026년 가업승계 세제개편안…승계 가능한 업종과 제외되... | https://www.tfmedia.co.kr/news/article.html?no=208392 |  |
| tax | 일간NTN | 부동산 세제개편 놓고 전문가 공방…"징벌적 과세" vs "담세력 반영" | http://www.intn.co.kr/news/articleView.html?idxno=2054490 |  |
| tax | 매일경제 | “비거주자 징벌 과세” vs “과세 정상화”…부동산 세제개편 전문가도... | https://www.mk.co.kr/article/12195307 |  |
| tax | segyebiz.com | ‘실거주 중심’ 부동산 세제개편 공방… 징벌적 과세 vs 과세 형평성 개... | http://www.segyebiz.com/newsView/20261103520127?OutUrl=naver |  |
| tax | joongang.co.kr | “집주인 뺨때리다 세입자 잡는다”…세제개편안 우려 쏟아졌다 | https://www.joongang.co.kr/article/25475421 |  |
| tax | gokorea.kr | 부동산 세제개편 실거주 과세 전문가 의견 갈렸다 | https://www.gokorea.kr/news/articleView.html?idxno=883887 |  |
| tax | 서울경제 | “징벌적 과세” vs “방향은 옳아”...세제개편 공청회 보유세 공방 | https://www.sedaily.com/article/20109806?ref=naver |  |
| tax | news.einfomax.co.kr | 부동산 세제개편안 공청회…"실거주 중시 방향성 타당" vs "세금 폭력" | https://news.einfomax.co.kr/news/articleView.html?idxno=4442814 |  |
| tax | hankookilbo.com | "국가의 세금 폭력" "국채 상환 먼저"… 세제개편안·미래대응기금 질타 | https://www.hankookilbo.com/news/article/A2026110316200005920?did=NA |  |
| tax | 머니투데이 | 부동산 세제개편 공청회 공방…"주거안정 목표" vs "세금 폭력" | https://www.mt.co.kr/politics/2026/11/03/2026110316431926124 |  |
| tax | 매일경제 | 실거주 아니면 껑충 뛰는 ‘세부담’…꼬이는 부동산 세제개편안 셈법... | https://www.mk.co.kr/article/12194970 |  |
| tax | sejungilbo.com | [공청회] "`26 세제개편, 국민 향한 세금폭력이다" | https://www.sejungilbo.com/news/articleView.html?idxno=60929 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

