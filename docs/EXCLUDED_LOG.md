# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-13 11:20:58 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1672건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 15 |
| excluded:company_event | 1 |
| excluded:company_self_activity | 3 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 20 |
| excluded:financial | 2 |
| excluded:foreign | 1 |
| excluded:industry_specific | 7 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 43 |
| excluded:no_regulatory_signal | 38 |
| excluded:opinion_piece | 1 |
| excluded:reader_content | 1 |
| excluded:similar_news_merged | 30 |
| excluded:smb_only | 1 |
| collect:event_announcement | 5 |
| collect:incident | 1 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 23 |
| collect:noise_keyword | 1 |
| collect:non_kifrs | 25 |
| collect:old_year | 8 |
| collect:out_of_scope | 204 |
| collect:out_of_window | 34 |
| collect:tax_subject | 35 |

## excluded:category_cap (15건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 의무화 ‘초읽기’…기업 대응 분수령 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5VNHp5R2hrNXlXUlR2Tm5KSXRXN0NYcm10MFAzOU9WRG5CN0xmczhMb0ZJd0JUcUxyT0VGUXJUdURLYWVCWWZIbVRROWg5OWRFckZORjBQLUU1UQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | insnews.co.kr | 금융위 “ESG 공시 로드맵 4월 확정… 대기업부터 단계적 의무화” - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1OU3RiY0tWWTdqblg5bE00WUdjZmc2OE13eW5scFl0MGlJLUthQUdhbzBUYVFGMUFOSl9PZzNZZkgtTWQ4dmNmMzkzeENsX3Z1NWl2dEpyb0Y1MGNHcXV3eThVemxzNUpKYVFz0gFvQVVfeXFMTnpMUjBVSC1QQl9YN3U0SEtFWFItRUtqNVBCY2RPY1c0WWgzSXl6WFU1OV8tWHIwZG5EVVQzN01hcmFldVYwbS1PZXozWlFpVkE3OTRWVk1pUHBJRkQ0U3FnUkRfN3kzb1RLYlY4am9j?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 의무화 초읽기…최초 시기·스코프 3 두고 이견 여전 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFA3NTR1NFY1M3RnQ1hWT1g4bzJvNjhUSTdfcTY5ZnQ4eUZISkFoY3pQbVIzWkk4ODQ4SEFIQTJQUjh3Z21lUWhKdUFaMFctaUFmYlFiYjl5RUgzRnNwaW5weDZNYU1sT205U25rZtIBcEFVX3lxTFBpREZVZVFLSnJuUXdfZDloVkxZVHhzNGpXMS1qRU51SkNCbVpRV1dJWmdQclVzemlGQ01YSU1QOV83VGtjam5wTU94MmxzNzVjNWx6ZlNMYzJBQmNtWjFVZ0ZLOGgxRk5SOUx2T1dZMEo?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | electimes.com | ESG 공시 2028년 대기업부터 시작…스코프3는 3년 유예 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB0NEtXNnFZdGJLd01zRG5XaGUtZ1RyX1hFMTB2REQ5VlVJRkZzdVFJODBNVHdqTlhBZzZtQnZtM1N2dXhtc2tma3pMaEMzX3N1cjFjOVl3RE91Sjl6Rm9zV251UDBQYUo5NWtXMNIBcEFVX3lxTE1jYVpBZ1NRcDNjb0ZpaGh3Q09TZFpINmN2b3BxbTJMaGpJeVVqQ1loMHhkRjJYZkp2ZjVkTEN4R0FWM0lrcWtsSUphSW4wUHZ0MWw3ekgwb3JZeE5hcmNfUXE0VkxUcXhWOFdsYXlZVmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 |  |

## excluded:company_self_activity (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |
| esg | ESG경제 | 아시아 각국, ESG 공시 의무화 '질주'...한국은 계속 '헛바퀴'만 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9iT1p3aDQ1bGItZFl4NDZ4Z3QxVGtEUS0wYnpjZ1BkTmF6MF9aakdtRVpBaGdIN3dUSms2bkxKUlBjU1VkT2NUaDRpNVdEaEExdDZjWkZEQlI0RjFQS0gwZ3IwRTVpTmNHNWJTMw?oc=5 |  |
| esg | choicenews.co.kr | KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 | http://www.choicenews.co.kr/news/articleView.html?idxno=173128 |  |

## excluded:corporate_pr (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | munhwa.com | 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5rS2E2d0xlNFhmLTRnWk5BWUNMTTE3V2dFdDlPYlZ5NHg5N3BRWHYyc05NTzZOM2FCRGdSbExyS0JRQ2FEWjhnay0zbHVxNVMw?oc=5 |  |

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

## excluded:foreign (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 임팩트온 | EU, CSRD 외부검증 기준 통일 추진…친환경 매출·투자액 재무제표 대조 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5XRHB3bmhCRW4teUI3MEJsXzFXSlk1VjlVRUx5UzlhQ2dIUXF1RzQzczZCTVBfby1tb2IzbGVycmg3MGlvQlBTcFVMMktnQm5XYWdMWUZyVDlRU0JJeTV0NHc5U1NkZUdxTGc?oc=5 |  |

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

## excluded:news_too_old (43건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | news.koreanbar.or.kr | 서울변회 “외감법 개정안 발의 환영… 국회 조속한 통과 필요” - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5MdnZCcEdDV09IaWw1VTFJcGVzMlUwMjl5X0V1cm5FMUF6V1VTSnhVZkRZS0NOS2NnUmRlOWtmNTN2Ql9pX3g5RUJRMjhFVlRlcURfbGRNbTF1NlRZdGRaSDV6M2d2MVJlMjl6TXY0MA?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9zaTlJci1iWW1GZ2c3TFFYUUxvS3JWTnZJNXZmQm1rdUhGSzMzUTJvM2hwNlBDdGhKdmJ5WU5ZRnR1MDJIYkl6bTlfZFEtMXE3Q1E?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 \| 한울회계법인 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | 머니투데이 | 국내 기업 83% "신외감법 도입 효과…회계 투명성 개선 체감한다" - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9UMncyMC1pU3F2dUoyVUk4YTV5dWVfanIxOTdEcW5IWGtzaUpBLV8xSnZCalJWM1V5aGd2Nl91N0EzcC1nTUhRZU04RUYwVVhMMjZPalNGNkdxTDlhQkY2YVFXSkN2UHl60gFuQVVfeXFMTW9CU0JhTjlHQ0ExcVNUY2xyR01vZ3gwRzlYbFBxRlZINUZyeThmS21IRktHOEN3dkNhUXZTNjZhSE16TGgxdGd3Unk3OHZNQ3hkMlpaSFRGV0JnaUR4VzdQS25xd0dVTHdjQlVKVXc?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | biz.chosun.com | 엇갈리는 신외감법 실효성 평가…“새 정부서 손질해야” - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUzFjNFNPUnBrT3ZjNGFtbDBKVVlQcHFna0puQUZIemxRQ013Z2tNUkRZQW9NQTA4WHhQZlMxYkZ6TmxWb2d4YVg1czBBcWtxTTNmcG52c1d2NDE4TVh1Uy0zekg1YV9mdTVDWDNKc3JyUjFBejlwQUVBWVdIY3pKMkp5ZksxS1ll0gGcAUFVX3lxTFBsa3BrTDBrZTlYWHZjZG1QVk1yRDBDRVFvTU8zbkdqYUppaGcwRmc1Vy1XSDlXRWRxX3RPcnhwSEdoVlNMVTBGMjQzZkxQSmxRdkliNFpiMGNOcHVqN1hzbjFPc0dCTDBCbkJoazEyZHhqRTBzTnd5U0E3cDc4cTlkNnVkTzd5UmppbXlYQ1FaODVmMEZEUTdieWdwYg?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |

## excluded:no_regulatory_signal (38건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE43SzV1ZWNkVHBRQzZUUkJ4OW5zQWoyekgtQ2pvZ0FJTXQ4NHVLNjYwa0lPa1RqVHpMemJzRUNxLUJyeXpuT29LWGVJbFNLMWZtelJseHBfNWNoVTBuVVJtb2xoWlpEQ1oyY3c?oc=5 |  |
| kifrs | 일간NTN | 증선위, 셀바스헬스케어·대우산업개발 회계기준 위반 적발 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9tQmxSTkNsdGZjelBnMlcyWUpmYWszeEtOdThRZmlyeXl5cUJERjd3WEx2WGpIRWxSZEl1bXNLYTV0R0c4VnRtR0xIN2sxZTh0QzY5bVdkd2RaQnFZTzRNdmZ2RHNwZmx1WXc?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 이데일리 | 증선위, '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxNcF9OSW01OEJMZVhqOHJpSUZEcGtraFA5eWhGVnlIUFlnVnJscEpCMlJOR2MwbFNoQUNucEtHYjV1bGcxOUlZUk1aVUdJLVVIdG91RWU2NHB0RWJWaHphNnVFVlhHUmxEQ2E5VklxVXBjZWRMcDZRaHVnMzUxcU9uZA?oc=5 |  |
| kifrs | 파이낸셜뉴스 | IFRS18부터 PRS까지… 재무제표 바꿀 변수 쏟아진다 - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1qMmQyTGZyUUpzOFBMOVF0Z1I4WHNUcUFZLUo5ODRlMkdOMGNqZ2pvSXJGODl1eUFYT1lDanRka29kdkRuWEJPNGRYdWNxWHBXZlA1ZGFqMGJJZw?oc=5 |  |
| kifrs | 한국경제 | 스벅·메가 사이서 버틸 수 있나…“사라질 커피 브랜드, 숫자는 알고 있다” [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9qRldRTGs4OGVtMnRWRnNrdWE2TGxBQmh3eXZGQ2I0SDAtMzFoM1Z0dHMwb0wtb1lnRi1TRlU0aFd5alYzeUZIanpBdEkyS0Z1ellKcmZma3ZfZXdZc2dpU2dua0paZ0NLRHNRVQ?oc=5 |  |
| kifrs | jabon.co.kr | 컬리·풀무원 재무제표…좋은 숫자만 믿으면 생기는 일 - 자본시장뉴스 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE96S0pOeklqUjhkWngyNlYtaHJzN1VTREtXcXpzN0JjSTRVTWU2NEFHeEpsUEFwYU16SVA5TXpxM1gycDN6T3o5eE01Q1ozVzl2ekVWbm01Q0o5c0o4bG5pTDdPUlpKVjg?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 재무제표는 기업 운명의 '신호등'...가수 이무진, 전 소속사 재무제표만 봤더라면 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBuQnFpOHhKeU0wNHI4NVQzOTZfaW44UFBRVGRJSl9OY2RCSlVYV3FyeW5CSEVsUDIzdHZyTEVwbUlMc2tZN3FRWUJkVXoteC1CSmhPbF94djFTdkpYX3d2TVg5WHNPQjNvLU5IUg?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 흑자 전환 컬리...그래도 여전히 '미생(未生)' - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1CZHpNRmxVcHB3N3hSazFQYkNJelpma2U0UzVNSjBkcThaNmUxcWlfZGVRWS1STGZzcF9vVVZRb1hfdWdhMEJWRWw4M1RwWjdQM1FGa2tEOXhZdDlaMnZCU0hrV3M0LWd0a0xNcw?oc=5 |  |
| kifrs | wikitree.co.kr | 테더 골드, KPMG 감사서 적정 의견…22억 달러 금 확인했지만 보고서는 비공개 - 위키트리 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE9Vd0llNURtSHhZLXdTRS1xZjlHQlA4UGtVeHlPTk5PazZVdmdiZnU2SDVaZW91RUF4MWgtTGw5eS12Y19pQU1fczExeXE4cGY4NW4tbnlB?oc=5 |  |
| kifrs | gamemeca.com | 위메이드 3분기 영업이익 264억 원, 비용 절감으로 유지 - 게임메카 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9XczlMZ3FTYUpVRmZ4UkFJekNTbjAxRk5vRGt2VXRZNEFQNFl5bzNxdkstREdveTlFOUxqOXpqUnVHRS1Wc0ZkMFdXSzRRODdwbE54VXZ0c1PSAVtBVV95cUxNbHZRcUVoNS1lcXNYX1pZNnlMbW5JUWYxMlpHSjZuUHRGVUoyd1BVSGFydXNNWFNRMkM3eHMwekJkT3hpQW90U2NKZEE0X3BMUWlVNXBLX2NsVWow?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| esg | ESG경제 | KEMI, 지속가능경영·동반성장 우수기업 9곳 선정 | https://www.esgeconomy.com/news/articleView.html?idxno=17378 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | ziksir.com | KB금융, 한국ESG기준원 평가 통합 A+ 획득…지속가능경영 성과 인정 | https://www.ziksir.com/news/articleView.html?idxno=153110 |  |
| esg | weekly.hankooki.com | 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 | https://weekly.hankooki.com/news/articleView.html?idxno=7193568 |  |
| esg | dailysmart.co.kr | "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... | http://www.dailysmart.co.kr/news/articleView.html?idxno=132423 |  |
| esg | gukjenews.com | 청주상의·대한상의, ESG 공시제도 설명회…도내 20개 기업 실무지원 | https://www.gukjenews.com/news/articleView.html?idxno=3750075 |  |
| esg | sateconomy.co.kr | ESG 공시, '작성'보다 '증명'으로…기업가치 가르는 이행능력 | https://sateconomy.co.kr/news/view/1065574204012569 |  |
| esg | cc.newdaily.co.kr | 대전상공회의소, 국내 ESG 공시제도·공급망 규제 설명회 열어 | https://cc.newdaily.co.kr/site/data/html/2026/11/10/2026111000377.html |  |
| esg | etoday.co.kr | AI로 들춰낸 친환경 기업의 민낯⋯ESG 공시 44%는 ‘그린워싱 고위험’ | https://www.etoday.co.kr/news/view/2646387 |  |
| esg | vtimes.kr | BSI 영국표준협회, 지속가능성 공시 대응 과제 조명 세미나 개최 - 벤처타임즈 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE82eGVua2NvUTUzRnk2MjdUc3J1RTBlaGkwcEwxRWQ0d0lPRWoxX3M1UzduRlE5UWFjUkNGZVNPbGMyZmRmcjE3bTNhUVhnT0hQcjlhd0Z3N0JHdk9nakJnaFpnU1VkQQ?oc=5 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| icfr | seoul.co.kr | 손정화 서울시의원, 서울연구원 회계관리 부실 지적...내부통제 체계 점... | https://www.seoul.co.kr/news/publicnews/local_govern/smc_movement/2026/11/11/20261111500024?wlog_tag3=naver |  |
| icfr | energy-news.co.kr | AI 감사기법 공유로 내부통제 취약점 함께 살핀다 - 에너지신문 | https://news.google.com/rss/articles/CBMickFVX3lxTFBNS0FiQnhzTkhVZXhyQVhfLVc3ZlhDYXc5TE11aGhYYXZBc2tRTF9peHVoOXZwS2Nvb1ZCM24xQ0lBY2lpTEg1WGxDNzlXb00ydTZDMkswYlNVVjdSRzJ2ajE5WElaaEFhT0RnNHJuN05wUQ?oc=5 |  |
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

## excluded:similar_news_merged (30건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | newspim.com | 증선위, 셀바스헬스케어·대우산업개발 회계처리 위반 제재 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE5xVHFZUm5oMzU2dGxzZ1ltTnpaS0pOQl90cm9vRGh1Q0NGTzFRVVhpSVlhWkZMaGlxZ1NENzVSRkZ2Ykt5WEtzYUdmZVZ4TkFCS0Y3OHlXOG9EZWsy?oc=5 | → 대표: 증선위, 셀바스헬스케어·대우산업개발 회계기준 위반 적발 - Daily NTN |
| kifrs | 파이낸셜뉴스 | 삼성전자 부사장, '글로벌 회계기준 제정'에 참여…韓 기업 목소리 커진... | https://www.fnnews.com/news/202611061034591232 | → 대표: 국제 회계기준 개정에 韓 목소리↑…자문기구에 삼성 부사장 합류 |
| kifrs | yna.co.kr | '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - 연합뉴스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE01b2lZLWNOMXlZYjFhcXJISHY2UW5oVV91UTRLZEFVaEVTSDJrREZETnl2VHdac1dRMkJBOFUyUXRTMm1HZDRBQk93ajlzYUdDNTAtMWx0UEwycm45XzlCQtIBYEFVX3lxTE01b2lZLWNOMXlZYjFhcXJISHY2UW5oVV91UTRLZEFVaEVTSDJrREZETnl2VHdac1dRMkJBOFUyUXRTMm1HZDRBQk93ajlzYUdDNTAtMWx0UEwycm45XzlCQg?oc=5 | → 대표: 증선위, '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - 이데일리 |
| kifrs | 이데일리 | 이찬진 금감원장 “20년 회계 감리주기, 3~5년으로 단축할 것” - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxOX3NLU0l0OVZ4ODJfMU5SSnBUM1NCa3VoVFNnUGw1SUNLQjJJcTJnR2pyb1pjQXpjRDVDSkdRM3BPS2ZwUjY5WnYyQWp0UFlOMk80aWVoRHBzZ1BkNzV5QVNCWTJram5JRHMzVER6OHBSX1hzbUdPdFhUclFUNnZTWA?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | news.bizwatch.co.kr | 상장사 회계감리 20년에 한 번꼴...이찬진 금감원장 "획기적으로 줄일 것" - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE05dWV0Ul9JcGNYOFN2b1drODJqNzNLNnRfMGNXYngzODk3d0I0eS10dTJJWHZ1VEZzZDRqRDRVOXFOM3M4RGFaRnlURGV0c3NwZDFsMnIxZUQ4U0RKMVVTZ2tlUjBBbHZPeFE?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | dnews.co.kr | 이찬진 금감원장 "상장사 회계감리 주기, 20년→ 美3년·英5년 수준으로 단축" - 대한경제 | https://news.google.com/rss/articles/CBMidEFVX3lxTE1fbUk5RzFyejJNVjBxbGxhVHB3Z01UczUzTFZ1YlUxZXlwVEc3VzVaVHNuQ2FfT1BwaVRRNVVOV2hGeGF0ZWwydDNXWVNtRk5SeEFWc3hZd29QY1VxTHdZQno2cXpQZDRZZmtZVVZvSFIybWdf?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | hdnews.co.kr | 금감원장 “고의적 회계 부정 무관용”…상장사 회계감리 대폭 강화 - 현대경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE05WFQwV1hKd1QtV2NBSXFranVhWU1qeWxpb2E0dGpmWlk3SWpwUm1qN012S0tEdDQwNjZwWEVFWUxyS2tuNXpZSzR4bEpfS1VERUxMN1BrLWZrZmg4N2o0b2FqeXZqd29NdGpF?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | newspim.com | 이찬진 금감원장 "회계 감리주기 단축 추진…고의 분식회계 무관용 제재" - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE5idmFUaEJWUEF0bEdzNWl3dDVETFREdHFUdTVkNHBYeGFiSm0xSVhQYWh6MGlzd1JtUmNsTWJfNWRnYVdMUm04aTNuZ3dHNjNWNkF4OC1MVVZ2eVBa?oc=5 | → 대표: 이찬진 금감원장 "상장사 회계감리 20년 주기 단축"…감사품질 감독 강화 By EBN - Investing.com 한국어 |
| kifrs | safetimes.co.kr | 금감원 20년 걸리는 상장사 회계감리 주기 '단축' - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBha2RUM2lwVUQ5SnFaQTFFXzdRR3o4YmpPUDlmVVI4SmE1X1g5bHY3RFBFLVFtaUloX2hZak9BWlFmVEdaYXFpNlByLVl6cWNkRm1qQW1FYzJaNGw1Tm5nUUVQNmp0TXQxSWttQ0MtVdIBc0FVX3lxTFBQbDRmNi1JeE9xeGoxSEtpZEN6b1lHUTV2QXlLUldNSDQxYmh2Njc0eXZzb1IzNWZwNzVUdjdpZXFZS3Q1NndQYi1aOVl3d0pFQkhEX1ptQTkyNmpFS1I1VllGTGZaZUdNTHZpSHNPVDRkdjQ?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | tradersunion.com | 금융감독원, 상장사 회계감리 주기 단축 추진 - Traders Union | https://news.google.com/rss/articles/CBMiqwFBVV95cUxNV0pIdEw4MTIxY08xeTI5Uy1XWXBfckhHbWFDMUVXMWxGcnBhRm1FMXhuaUtEZHBBQVpwcFR1dzBQZEJfbGJUUUpWQnVDaTIzNDRFYjdPRU8zRENXYndiUmFPNklaZy1XUDFHbV82NWx5allzTi14cVNEMW9RemN4b0hacEJydldlZHVCdWZfMmZQbWp0RW4xZFhEd1p2WFIzdGpsZ2JiYVp0R2M?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | metroseoul.co.kr | 상장사 회계감리 ‘20년 주기’ 줄인다…부실감사 징후 땐 집중 점검 - 메트로신문 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1NQlE3LWNaVDUtWXBLWHhKSHRHc0tvaUJHX25lV1hlNG1HZUtQaGdxeEVabTBYQ0N4VnZxS3JvUmZjOFJMdnE4WXN2cm9UanA0QWNaWTFQN0pSdE5tbnYzUg?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | seoulfn.com | 금감원, 상장사 회계감리 주기 단축 추진···부실감사 감독 강화 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5MNW1fZE5GWFc3X2Fzc1NIUE1zVkZ1RXh6U05KeTd3WFVGd25tZkJEcWxEYkVqUGY5SHkzZmhYNWllX1NUTThuaHRjZHVHWGhvWDV0em9VdTZwVnhHbEhOUGh5WG9DbmNrd0E?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | ezyeconomy.com | 상장사 회계감리 20년에 한 번꼴...금감원, 감독 주기 대폭 줄인다 - 이지경제 | https://news.google.com/rss/articles/CBMibkFVX3lxTE0yWnJ2N1NRZm5EVjhnSTFYTVN3eXdxdlZaM1BwSmZETjluOXFYbnN2ZzlBRkZsa1pjRDRfM2Z5NTBDQWlsY3FFMEI4QzQ2aTA2cHVoenhfYnhDYW1qYzA3MTZteGtGcGFhYm9FdjB3?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | woorieconomy.com | 금감원, 상장사 회계감리 주기 20년서 3~5년으로 단축 추진 - 우리경제신문 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE44T3ZSTzVIYzB4c2NmRkpaX05acHk0S2hMa1B3dGhLWXNfYU8teW9ZdUZGY0FsVkpDbGlXVlBvRFBTVXZvLUxpVmxlMEVyb2Y3SmRaczlHcS0?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | ajunews.com | 금감원, 상장사 회계감리 20년 주기 대폭 단축…부실감사 무관용 제재 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFByTU5hM0NwZFdlNzNQem5RV1lFT1Bfel9CTG9OODQyUjQ3WWpFSFBtdmdwNVhLZ2wzVmtIbmNGakFObWZNdVEycF9MN2RKY0ViUzVhZENGT3hEUdIBWEFVX3lxTE00UnhZRmFfNlpCcE9fVnAxNmRXc3ZLNnBVNTZfYjVHN1RRUW8xdlFzVFltc3hjOE51LUtaMWlJNGZzZjFLeG1FbURWOV9uLTBOamNKVm5XM1I?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | sidae.com | 금감원, 회계감리 주기 단축 추진 - 동행미디어 시대 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE9KemduSlRJeFU5V21ObXNvR1preTBsdE02OTYydHJSZ3lIR0dVUXZxTTkyV3RUemxFSkstRkpLdFREOGxlN3BhQlI2bGxoNFVYaEZWM2RnTVU0MHptVUE?oc=5 | → 대표: 20년에 한 번꼴 상장사 회계감리… 금감원, 주기 단축·책임강화 추진 - 문화일보 |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 |
| esg | 임팩트온 | ESG 공시 의무화, 투자자는 무엇을 보나…숫자보다 '숫자 뒤 설명' | https://www.impacton.net/news/articleView.html?idxno=30637 | → 대표: ESG 공시 의무화, 투자자는 무엇을 보나…숫자보다 '숫자 뒤 설명' - 임팩트온 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | 머니투데이 | 코스피 상장사 5곳중 1곳, ESG 공시 준비 안 됐다 | https://www.mt.co.kr/stock/2026/11/11/2026111019562387265 | → 대표: ESG 공시 의무화 코앞인데…대형 상장사 5곳 중 1곳 '보고서 無' |
| esg | electimes.com | ESG 공시 로드맵 확정…10조 이상 코스피 상장사부터 의무화 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5XUnhUekpXVlVFZEFuR0ZtdldTYlhvX1A4Yk84UVZqc0xCLTVYQVlTT2wwLWZRUkNGb0FpWTZaeEJzUFNXWVpwYlFJQUhvTmR3aEtOS0FKeFVvQzBiVGJObkF4X3phc1VScmJMQdIBcEFVX3lxTE5HcHpjSzJTMnQyakNLT190LUVLX3ZGNXM0LWJKVzA1cXlHcjhVc1dWY1V4OGFrcG42REdfMWJRVmlXVUcwZ2JYTXE5ZE1BamduRllrbGZReTBqbjRUeWVQZUl2cEdfZ09CRVFRemlvS3Q?oc=5 | → 대표: ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 |
| esg | globalepic.co.kr | KB금융, 한국ESG기준원 평가서 통합 'A+ 등급'…지속가능경영 리더십 입... | https://www.globalepic.co.kr/view.php?ud=2026111210164730997cc35ccc5c_29 | → 대표: KB금융, 한국ESG기준원 평가 통합 A+ 획득…지속가능경영 성과 인정 |
| esg | fashionbiz.co.kr | 신세계백화점, ESG 평가 2년 연속 A+... 지속가능경영 성과 | https://www.fashionbiz.co.kr/article/231039 | → 대표: 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 |
| esg | businessplus.kr | 신세계百, 2년 연속 ESG평가 'A+' 획득…"지속가능경영 결실 맺어" | https://www.businessplus.kr/news/articleView.html?idxno=119709 | → 대표: 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 |
| esg | efnews.co.kr | 현대로템, ESG 종합평가 3년 연속 'A+'…지속가능경영 성과 인정 | http://www.efnews.co.kr/news/articleView.html?idxno=133916 | → 대표: 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 |
| esg | cstimes.com | 현대로템, KCGS ESG 평가 3년 연속 통합 A+ 획득…지속가능경영 성과 입... | https://www.cstimes.com/news/articleView.html?idxno=727670 | → 대표: 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 |
| esg | joongangenews.com | [ESG] 현대로템, ESG 평가 3년 연속 A+ 등급...지속가능경영 성과 인정 | https://www.joongangenews.com/news/articleView.html?idxno=563186 | → 대표: 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 |
| esg | kyeonggi.com | 현대로템, ESG 종합평가 3년 연속 ‘A+’…지속가능경영 활동 성과 인정... | https://www.kyeonggi.com/article/20261112580060 | → 대표: 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 |
| esg | thefairnews.co.kr | KB금융, KCGS ESG 평가서 최고 등급 'A+'…지속가능경영 리더십 입증 | https://www.thefairnews.co.kr/news/articleView.html?idxno=93912 | → 대표: KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## collect:event_announcement (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | 제18회 국제금융기구 채용설명회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079925&menuNo=4010100 |  |
|  | 재정경제부 | 제3차 글로벌 핵심 투자자 협의체 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079922&menuNo=4010100 |  |
| esg | globalhumantimes.kr | BSI 영국표준협회, ‘지속가능성 세미나 2026’ 개최… 의무 공시 및 검증 시대 대응 전략 제시(BSI Korea to Host 'Sustainability Seminar 2026' on Strategies for Mandatory Disclosure and Verification Era) - 글로벌휴먼타임즈 | https://news.google.com/rss/articles/CBMickFVX3lxTE9XdmpZUGo5SVRFOGVzOVB4aWozVzlWLUdib1V1ekdRZDVES25XUTJTQ1c2WnAtWnVKZWI4cUUwaEhQMjNpQ3dKbFlDNXdDM3dodUVUSGJTdUQxMkJvZEFiOUFSdGYzSkFIYTcyLXB4dllFdw?oc=5 |  |
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

## collect:no_category (23건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 재정경제부 | [보도참고] 2026년 11월 최근 경제동향 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079950&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「월급방위대 TF」 킥오프 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079949&menuNo=4010100 |  |
|  | 재정경제부 | 범부처 민생안정지원단, 청년 취업지원 현장 점검 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079929&menuNo=4010100 |  |
|  | 재정경제부 | 국방분야 혁신제품 최초 지정 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079935&menuNo=4010100 |  |
|  | 재정경제부 | 양극화 대응 TF 총괄반 1차 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079934&menuNo=4010100 |  |
|  | 재정경제부 | 영남권 메가프로젝트 이행 점검 TF 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079927&menuNo=4010100 |  |
|  | 재정경제부 | 비상경제장관회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079917&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] '26.10월 고용동향 및 평가 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079916&menuNo=4010100 |  |
|  | 금융위원회 | 서울 가격상승폭 둔화·매물 증가…수도권 내년 1분기까지 4만 호 이상 입주. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88140?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 신뢰받는 자본시장, 현장에서 묻고 답을 찾다. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88139?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 261112(보도참고) 지배구조 개선방안(’11.12일 발표) 관련 설명자료. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88138?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | ‘26년도 상반기 기술금융 테크평가 및  품질심사평가 결과. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88137?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 가상자산사업자에 대한  최고 수준의 보안 강화 조치를 통해 이용자의 자산과 정보를 철저히 지켜나가겠습니다. | https://www.fsc.go.kr/no010101/88133?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 인터넷/SNS상 코스닥 추가대책에 대한  허위정보 관련 투자자 유의사항 | https://www.fsc.go.kr/no010101/88132?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 사업보고서 등에 대한 조사·감리결과 조치 | https://www.fsc.go.kr/no010101/88127?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융회사 지배구조의  공정성과 투명성을 제고합니다. | https://www.fsc.go.kr/no010101/88125?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 2026년 10월 가계대출 동향(잠정) | https://www.fsc.go.kr/no010101/88124?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 미공개 무상증자정보를 이용한 내부자등에 대한 중대범죄수사청 고발·통보 조치 의결 | https://www.fsc.go.kr/no010101/88123?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | '26년도 상반기 기술금융 테크평가 및  품질심사평가 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789090&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 서울 가격상승폭 둔화·매물 증가…수도권 내년 1분기까지 4만 호 이상 입주 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789151&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 261112(보도참고) 지배구조 개선방안('11.12일 발표) 관련 설명자료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789114&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 신뢰받는 자본시장, 현장에서 묻고 답을 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789142&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국세청) | 내년도 오피스텔 및 상업용 건물 기준시가 사전열람, 12월 2일까지 의견 제출하세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788907&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |

## collect:noise_keyword (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | munhwa.com | 與 이훈기 의원 “주가 낮출수록 상속세 줄어…상증세법 개정 정부안 폐... | https://www.munhwa.com/article/11630912?ref=naver |  |

## collect:non_kifrs (25건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 종전기업회계기준과 일반기업회계기준 질의회신 비교표 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40533&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 24-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40531&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 21-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40530&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 20-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40529&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 19-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40528&ctgCd=016009&replySummary=Y |  |
| kifrs | 한국회계기준원 | 일반기업회계기준 질의회신 정비목록 17-1 | https://www.kasb.or.kr/front/board/View016009.do?siteCd=002000000000000&seq=40527&ctgCd=016009&replySummary=Y |  |
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
|  | 한국회계기준원 | [공지사항] 홈페이지 게시_본인 인증 서비스 일시 점검 안내(2026. 11. 14.(토) 22:00 ~ 2026. 11. 15.(일) 04:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI 실무 세미나 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] IASB 정보요청서, IFRS 9 '금융상품', IFRS 7 '금융상품: 공시' 위험회피회계 사후이행검토(PIR) 국내 의견조회 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] ISSB 자연 관련 공시 실무서 공개초안 요약자료(Snapshot) 국문본, ISSB 아웃리치 세션 및 국내 의견수렴 일정 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(5차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 본인 인증 서비스 일시 점검 안내(2026. 10. 17.(토) 21:00 ~ 2026. 10. 18.(일) 05:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 정책브리핑(산림청) | 산림청, 국유품종 민간 보급으로 임업소득 기반 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789147&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | ICAO 항공안전평가 앞두고 범정부 총력 대응 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789145&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 인도양 해저지형 4곳에 조선시대 지리학자들의 이름을 붙인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789144&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 기상청, 국제민간항공기구 항공안전평가 앞두고 최종 준비 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789149&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "사람과 기술이 함께 성장하는 반도체 산업" 김영훈 장관, 반도체 연구개발 현장의 근로시간제도 운영 실태와 애로사항 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789141&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부, 2027학년도 수능 대비  지진 대응태세 철저히 점검한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789140&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한국국제협력단 이사장에 오현주 전 국가안보실 제3차장 임명 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789138&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 임업직불금 지급 제한 농외소득 4,700만 원으로 상향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789135&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 가을철 맥류 파종 현장 찾아 안전 생산 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789132&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 산·학·연·관 협력 '곤충 단백질' 기능성 소재 발굴·제품화·수출 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789130&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 재외동포청 인사_류승수 신임 기획조정관 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789127&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 성탄절 물들일 국산 포인세티아, 생산자·소비자 함께 고른다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789128&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '슈퍼푸드 귀리' 종자 파괴 없이 영양 성분 빠르게 확인한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789122&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(경제사회노동위원회) | 「청년위원회」·「청년일자리 희망 위원회」연석회의 개최 -   3기 청년위원회, 지역 청년 노동시장 진입 실태 및 개선과제 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789126&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 11월 이달의 임산물로 '마가목' 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789125&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 다큐멘터리 국제 경쟁력 강화에 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789116&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "베트남 딸기 수출길 더 넓어진다" 농약 안전사용지침 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789120&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 통상교섭본부장, 민관 원팀으로  EU 고위급 통상외교 총력전 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789119&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 중동 사태 대응 '농자재 절감 기술' 자료집 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789110&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 아동·청소년의 목소리, 개인정보 보호정책에 담는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789112&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 미래 인공지능·정보통신기술 기술 혁신,  한-해외 연구자가 함께 만들어 간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789106&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부， 제2연평해전 전사자 유가족 과수원 일손돕기 진행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789105&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 미국 호시한 지사， 우즈베키스탄 이괄 지사 유해 고국으로 모신다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789104&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 유통분야 표준거래계약서 7종 개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789103&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 정부, WTO에서 우리 수출기업 발목 잡는 해외 기술규제 대응 나서 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789109&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 인공지능(AI)으로 공공조달 혁신… 미래 조달행정 청사진 제시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789107&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 국립현대미술관장에 기혜경 씨 임명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789108&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 시설공사 주간('26.11.16.~'26.11.20.)입찰 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789100&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 지역 중심 산림정책 발전방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789102&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 남부지방산림청-고용노동부 숲가꾸기 사업장 합동점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789099&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.13.보도참고자료] 감염병 치료제 연구 가속화를 위한 다부처 성과 교류회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789097&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 「해외에서 운전시 유의 사항」 원스톱 확인 (11.16) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789096&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 공소청과 함께 산림특사경 교육 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789095&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 「작업시간대 조정 집중 지도」 한파 대비 노동자 건강보호 대책 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789088&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | '가짜 3.3' 위장고용, '사업장 쪼개기' 등 노동법 회피 꼼수 기업 기획감독 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789087&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 대한제국의 마지막 황제, 순종 서거 100주년 맞아 초상 2점 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789093&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, '2026 산림디지털 컨퍼런스' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789086&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 「고성 운흥사 대웅전」, 「영천 거동사 대웅전」 국가지정문화유산 보물 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789080&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "기숙사에 살았다고 보상금 제외한다니"… 20년간 실제 거주했다면 생활터전으로 인정해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789078&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 취향이 문화가 되는 '요즘 청년', 대구에서 만나다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789076&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 장애인의 의약외품 안전정보 접근성 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789077&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 제27차 한·불 원자력 공동조정위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789073&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제27차 한·불 원자력공동조정위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789074&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 물류기업과 기술기업이 만나는  '협업의 장' 열린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789071&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 땅속 깊은 곳까지 더 안전하게… 지하수 조사 표준 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789072&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 강금실 대통령 특사, 제31차 유엔기후변화협약 당사국총회(COP31) 정상회의 연설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789075&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 권대영 1차관, 「월급방위대 TF」 킥오프 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789089&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | [보도참고] 2026년 11월 최근 경제동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789113&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 충북 진천 종오리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789084&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 경기 파주 메추리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789083&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 경북 예천 소재 소(牛) 농장 예찰 검사에서 구제역이 확인되어 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789082&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 인천 강화 산란계농장에서 고병원성 조류인플루엔자 발생에 따라 방역관리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789081&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 지역상의 방문 및 기업인 규제합리화 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789070&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제9차 외교부-시민사회 정책대화 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789040&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "타지키스탄과의 반부패 협력, 이제는 현실적인 이행으로!" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789038&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 한우농가 인공지능 사육 관리 현장 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789034&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '국가표준식품성분 데이터베이스(DB)', 국민 아이디어로 날개 달다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789032&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 국유림 현장에서 미래 가치를 더하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789037&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 소비자 기호 반영·국산 고구마 산업 발전 방향 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789030&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 전국 3개 도매시장서 신품종 40종 알려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789028&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 장관, 포르투갈 농업해양부 장관과 '해양수산 협력 양해각서(MOU)' 서명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789039&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) '농어민과의 대화' 계기, 가리비 양식업계의 목소리 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789017&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 남재헌 차관, 수산기업 CEO들과 수산업 경쟁력 강화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789016&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 검역 관리급 '토마토 바이러스병' 총력 방제 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789026&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '기력·체력·활력' 채우는 고려인삼 축제, 서울 홍대서 열린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789024&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 고된 노지 감귤 농사에 스마트팜 바람 분다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789022&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 기후위기 대응 '곰팡이독소' 안전관리 전략 논한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789020&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 어미돼지 무리사육, 개체 식별부터 사료 공급까지 자동으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789018&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '토마토갈색주름과실바이러스' 공적 방제 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789014&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 농식품부산물로 사료비 줄인 한우농가 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789012&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 비료는 한 번만, 밀 재배 더 간편하게! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789010&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 김용석 대광위원장,고양창릉 광역교통개선대책 추진상황 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788997&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국내외 전문가 모여 농약 안전성평가 미래 논한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789008&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농업·산림·해양·관광 분야 치유정책 공유…부처 간 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789006&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 겨울철 한파·폭설 대비 사양관리 안내·기술 지원 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789004&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 속까지 붉은 양조용 포도 '쇼콜라누아' 개발, 와인 차별화 기대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789002&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '농업 연구 협업용 인공지능' 첫발 뗐다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789000&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "현장 소통"으로 활용도 높은 디지털육종 완성한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788998&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(해양경찰청) | 해경청, 포스코이앤씨와 깨끗한 바다 위해 맞손 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788996&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 콩 전 과정 기계화·스마트 기술 성과공유회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788994&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 돼지 육질 예측해 우수 씨돼지 고른다…진단 기술 개발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788992&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 인삼 수확·저장 관리 요령 제시, 상품성 저하 예방 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788990&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 전분 함량 높고 병에 강한 신품종 고구마 '다온미', 제주에서 선보인다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788988&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 토양개량제 지원 받으려면 "수확 끝난 지금 흙부터 검사" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788986&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 더 안전한 축산 환경, 관계 기관·단체 힘 모아 만든다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788983&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 제주 감귤, 검역협상 타결 8개월 만에 우즈베키스탄 첫 수출… 중앙아시아 공략 본격화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788982&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 공익광고로 우리 사회의 선을 잇는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788980&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제25차 한-유엔 군축·비확산회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788979&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청장, 소나무재선충병 방제 현장 안전 점검 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788978&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | [기고문] 가을의 풍요, 작은 불씨 하나에 사라집니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788976&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림?나주시청, 소나무류재선충병 '공동방제구역' 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788974&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 11월 숲가꾸기 체험행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788972&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 의료 정보보호 강화 위한 민관 협력기반 마련, 의료기관 보안 현황 점검 및 개선방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788970&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 고려인 강제 이주 역사 화폭에 새긴 故 신순남 화백, 11월 '이달의 재외동포' 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788968&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 농업계 목소리 듣고,  통상현안 해법 함께 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788966&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부, 장관 주재 「팀코리아 체코 원전사업 추진현황 점검회의」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788967&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 대한민국 최대 할인행사, '코그페' 11월 15일까지 개최··· 전국에서 할인혜택 누리세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788964&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 중장기전략위원회 혁신성장반 분과회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788963&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 임도, 설치를 넘어 현장 활용성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788961&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)충청권 메가프로젝트 착공식 개최, 첨단산업 투자 본격 실행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788962&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 진에어-에어서울-에어부산 합병 인가,  27년 3월 17일부터 진에어로 통합 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788954&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 「에너지 팀코리아」, 글로벌 에너지 전환과 우리 기업 해외 진출 함께 견인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788959&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 민간과 함께 풍동시험 기술과 경험 나눈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788958&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 진에어-에어서울-에어부산 합병 인가,  27년 3월 17일부터 진에어로 통합 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788952&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년도 공정위·한국산업조직학회 공동 정책포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788951&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 인천 강화 산란계 농장에 대한 정기 예찰 검사에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788953&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국방부) | ｢국방 에너지 전환 계획｣ 최종 검토회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789150&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 영농부산물 파쇄지원으로 가을철 산불예방 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788956&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 하나원, 지역주민 건강지원 및 무료 이발 봉사 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788950&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 근로복지공단, 제47회 노동자문화예술제 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788949&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국민통합위원회) | 통합위, 오는 15일 MBN 서울마라톤서 「대한민국 국민통합 런」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788948&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 문체부, 미등록 대중문화예술기획업체 16개소 수사 의뢰 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788944&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 국민과의 "소통"은 더욱 강화하고,악의적 특이민원은 엄정 대응하겠습니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788940&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | "행동하는 인공지능 시대, 이용자 보호 방안은" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788942&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 유엔 참전용사의 헌신 기록하고 가족이 된 17세 소녀 박채은 양 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788941&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 금융업계와 함께하는 기후행동, 현금처럼 쓰는 포인트 혜택까지 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788939&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 중견 건설사 대상 민관협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788930&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금개발청, 트래블쇼에 참가해 새만금 홍보와 투자유치 활동 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788937&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금청, 새만금지역 지적측량기준점 2,378점 측량성과 고시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788935&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 부여국유림관리소, 가을철 영농부산물 파쇄 캠페인 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788927&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능 안전 국민 모니터링단 「인공지능 안전 지킴이」 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788925&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방 분야 혁신제품 최초 지정, 민간 혁신기술의 군 활용 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788921&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | '고용행정 데이터로 청년 일자리부터 산업전환까지… 노동시장 현안 해법 찾는다' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788923&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국방부) | "제주 떠나 강원도 전장에서 산화한 16세 호국영웅,  75년 만에 고향 제주에 잠들다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788920&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 노동부 장관-전국 지방노동관서장, 중대재해 취약현장 일제 불시점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788922&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 구미국유림관리소, 가을철 소나무류 취급업체 무단이동 특별단속 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788917&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 「해외에서 운전시 유의 사항」 원스톱 확인 (11.16.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788918&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 민간 첨단기술과 국방의 연결, 제4회 미래 국방 기술교류회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788915&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 「2026 국제 마약수사 컨퍼런스」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788914&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 위기이웃 살피는 11만 7천 명의 복지안전망, 제20회 지역사회보장협의체 전국대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788913&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 인공지능시대의 올바른 디지털 문화를 놀이로 익힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788911&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 방한 외국인 관광객 2,000만 명 돌파, 대한민국 관광의 새 역사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788908&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 4.16의 기록, 오늘의 교육이 되다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788904&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 복지서비스, 현장에서 상담부터 신청까지…AI로 더 똑똑해진 '모바일 행복이음' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788899&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 사물인터넷 제품, 제조사의 적극적 보안 강화와 소비자의 보안 수칙 실천이 필요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788896&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부, '정부24' 우수 성과 13개국에 공유… 세계가 주목하는 K-디지털정부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788906&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 정지궤도 환경·해양 위성인 천리안위성 6호의 청사진 공개한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788898&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 기후행동에 재미를 더하다… 온라인 숲에서 춤까지, 즐거운 기후행동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788903&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 보고 느끼는 친환경 이동수단의 가능성…기후부, 전기차 전시·체험 행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788902&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 정지궤도 환경·해양위성(천리안위성 6호)의 청사진 공개, 산학연 참여의 장 열어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788901&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 정지궤도 환경·해양위성(천리안위성 6호)의 청사진 공개 산·학·연 참여의 장 열어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788900&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(감사원) | 원주시 정기감사(별도처리) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788947&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 송미령 장관, 김장 한 포기 더 담고 이웃과 따뜻한 정 나누기 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788894&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K-온디바이스 AI반도체, '상생'으로 속도낸다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788895&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 「2026 인도-인권 상호대화」 3차 행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788919&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국가방제대응단 상황관리 회의 개최 및 경미지역 국가 역량 집중 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788893&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 조경의 오늘과 미래를 한눈에, 「제1회 대한민국 조경박람회」 13일 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788891&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 공공재개발 사업수수료 3%→1% 한시 인하 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788890&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '26년 기본형 공익직불금 2조 3,788억 원 지급을 시작합니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788889&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 50년 한일 농림수산 기술협력,  미래 농업기술 공동연구로 이어간다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788888&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농촌의 가능성을 창업으로! 농촌의 미래를 바꿀 주인공을 찾습니다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788887&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영주국유림관리소, 산불무인감시카메라 확충으로 산불 감시기능 강화 - 첨단 산불 감시망 구축, 올해 조망형카메라 4대 추가 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788884&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 인근 약국 없는 군부대·공항에서 안전상비의약품 취급 등 의약품 접근성 개선 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788876&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영주국유림관리소, 고성능임업기계를 활용한 영농부산물 파쇄로 소각산불 예방 총력  - 단순목재 파쇄를 넘어 고성능 임업기계 활용률을 높이고, 산불 예방 및 국민 체감 행정 실현 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788875&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | [기품원] 폴란드 군비청  품질전문가 초청 토론회(세미나) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788873&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | [기품원] 폴란드 군비청  품질전문가 초청 토론회(세미나) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788873&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 「월간 재정동향」 2026년 11월호 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788867&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 에듀테크 분야 개인정보 처리 실태점검 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788879&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 안전조치 의무 위반한삼양그룹 소속 4개사 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788878&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 8개 알뜰폰 사업자의  개인정보 처리에 대한 조사 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788877&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 실험실의 상상, 세상의 비즈니스가 되다"  「2026 대한민국 딥테크 사업화 페스티벌」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788869&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능 시대의 사회적 쟁점,  국민과 함께 해법 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788868&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 11월 가뭄 예·경보 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788881&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지재위, 기업 영업비밀 보호방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788866&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 겨울철 대비 계절근로자 숙소 문제, 1345로 신고하세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788865&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 방위사업 자료열람,  더 넓은 공간에서 더 여유롭게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788862&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림, 가을철 산불 예방 '화목보일러' 집중 안전 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788864&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국립문화유산연구원, 한국 선사고고학 학술대회 공동개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788861&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 2026 지속가능발전 국제 심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788857&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 군용전지 표준화로 장비 간 호환성 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788856&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 전승공예품으로 꾸민 특별한 집 'K-크래프트 하우스', 더현대 서울서 만난다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788853&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산수리 손해배상보험·공제 가입 전면 의무화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788852&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 한 해 동안 청년의 열정으로 지킨 세계유산 보호 성과 나눈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788850&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 구축함(KDDX) 전투체계 육상체계통합시험장 개소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788855&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 인사발령(과장급 전보) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788847&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 고용노동부, 금년 마지막 5회차외국인 노동자(E-9) 고용허가 접수 안내 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788842&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 위기 앞에서도 빛난 노사 신뢰! 2026년 노사문화대상 10개 사 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788841&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 생산적 금융 시대, 지식재산(IP) 금융으로 실현한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788840&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 유럽연합 탄소국경조정제도(CBAM)  국내 첫 검증기관 인정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788844&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 복잡한 외자구매…이젠 더 쉽고, 더 빠르게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788843&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 양극화 대응 TF 총괄반 1차 회의 개최 모두의 성장으로 대전환을 위해 전 부처 역량 결집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788838&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 대중문화예술 작품 뒤 숨은 주역 10명(팀),  무대 위 주인공으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788837&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 문화진흥 4개 기관 통합 추진으로  국민 문화 향유 혁신 기반 마련한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788836&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 공개토론회로 「관광진흥법」 시행규칙 개정안 의견 수렴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788835&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '2026 오늘전통축제' 개막, 전통문화를 오늘의 즐거움으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788834&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 인공지능과 저작권의 상생 모델 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788833&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 한국-유럽 의료기기 규제정보 공유로 해외시장 진출 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788832&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 유럽 주요 위해평가기관과 식품안전협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788831&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, PICS 평가국 참여 글로벌 의약품 규제 위상 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788830&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 필수 항암·항생제 3품목 주문 제조로 국내 안정공급 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788829&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청, 전국 초고층 건축물 등 512개동 재난대응체계 집중 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788985&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 전세사기피해자등 480건 추가 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788827&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 유럽연합 탄소국경조정제도(CBAM) 국내 첫 검증기관 인정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788828&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 얇은 렌즈로 밝은 야외에서도 뚜렷하게, 일상 속 증강현실 안경에 한 걸음 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788826&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 국방분야 혁신제품 최초 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156788924&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-13&endDate=2026-11-13&srchWord=&period= |  |

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

## collect:tax_subject (35건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | 2026년 부동산 세제개편안 주요 내용 총괄표 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9VV05RWWFtWkNqZmNWQktodVFiLS1GckNYcXZ6SGUxcFc5dXhEQi0tN0FmM2tucEROdHF6OU4xUnpmd1NXd29fQUpnMkdRbnVac2pqOEsxUTBaN1JWdjcyVjBHOUE?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | sunnews.co.kr | 국회예산정책처, '2026년 세법개정안 토론회' 성료 - 썬뉴스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5yQjhCa0p1ZjlJYXFLc05WOGRyd1F0U19HMDFrejMwb3h6NU91WnhQNGVaWEd2QXdOeWMzWXM0Y1k4UWxWRy1uYVFESUlqZ0FSRDNpUFU0UkIxMkhUTDhuWDR3TVVNS0NYYUk2UQ?oc=5 |  |
| tax | sejungilbo.com | [토론회] “체감 경기 회복 vs 과세 예측가능성”…`26 세제개편 쟁점은? - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE14eTJsdUFhend0enBURENHX2dBT0pFdS1mcU9pcGo3UllMbXZsU2x3OG1jb183aFBKZFJQb3ZGWlgxQUVqM1YwZDNRV1JlX0F6SWdiVHdyTzRQRXNnY0FqczZNZ1Ixam80UGFMZw?oc=5 |  |
| tax | newspim.com | [뉴스분석] 부동산 세제개편안 정부안 의결…與 내부서 불거지는 수정·보완 목소리 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBaMU94ZFRIbWRacklQenVyOHN0dUxYc3AzM0ZveTR5a3Fvd0NsaW9jcVNNRGN3emRCcUFCQWJsa0J5TEFNWnd3bEc1cExsRlNSVDJCMWNNWEkxOWQz?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | daenews.co.kr | 정부 세법개정안, 세수 얼마나 바뀌나…국회서 여야·전문가 토론:동아경제신문 & daenews.co.kr - 동아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1zamFET0V6bVlRR1NOd3A5OWk2UFc0anBVbUxMSEN4WGJHWGk1ZUVTemRXMVpQSHZRM1ItUnFKOFd0cEdNc0ZEYXhORlNWdVJzakZJUFJ4b1l4RGc2d3lCUFJR0gFiQVVfeXFMTXNqYURPRXptWVFHU053cDk5aTZQVzRqcFVtTExIQ3hYYkdYaTVlRVN6ZFcxWlBIdlEzUi1ScUo4V3RwR01zRkRheE5GU1Z1UnNqRklQUnhvWXhEZzZ3eUJQUlE?oc=5 |  |
| tax | doctorsnews.co.kr | "병원은 기업 아닌 지역의료 인프라" 가업상속공제 제외 철회 촉구 - 의협신문 | https://news.google.com/rss/articles/CBMickFVX3lxTFBNVTV1QkxNT2l0a2V6clJfQ1ZUZ25TeWgzNkZrVUpuRE9ISU5CTEpEVlFyRExqeWdQNF9FY3RNdS1IcG05eWJCLTFsNzkyY01GbV9ud2dsalBSQ2NBTVhiS2NQNF9Yc2hZa3Bsd09ZLXE1Zw?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | sejungilbo.com | [칼럼] 판례 80건을 해부하며 본 ‘세법 책’의 변화 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5tMFlsREN2MC01T09YUEYyOGVwTmNfRUdCc1gzSjJzSHZtUFdJNjlETjYwRGZHRnVFeUNiNm9IbkNlSXluMXZoRFkyU3FsX1NqVFNCOGo1eW1oRTkwb0VocGM5cTFJeUZPX2lzZw?oc=5 |  |
| tax | 한국세정신문 | [기고]2026 세제개편안, 문턱 높아진 가업상속공제 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9taThKdzN3dkRBcF9jVFpJZzI5TklRYW9BNF9ScmF1Rkw5cU5ralItNUxOZjR0aTJ2Rk8xZGZIZTh3NUlkaHVTZW9jRGJjbHFrVzh2cjlMUk1UWk9HWlFHWmcwSjM?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | asiae.co.kr | '부동산 세제개편' 여야 시각차…종부세 두고선 당정 이견 표출 - 아시아경제 | https://news.google.com/rss/articles/CBMiggFBVV95cUxOOTJPbk5qYmx0OGFIamxWdUVqNVV0d1RodFBhVzJfMjJCMWpQN01fb2ptU0N5ZDh4MkQteS1vUEM4UE9Fb1hVbHVlZ21ETW5jTXBub0M0UEMycG1SeUF5VWRoTHp6aUdSNlFFYUYxV2syV1YtVVptUHlVaFRkdjdlSGhn?oc=5 |  |
| tax | newsis.com | '1주택자 부담 완화'…세제개편 반발에 보완 입법 잇따라 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFB1bHQ2LUtKTnRzQlJiVmsxbDVLOFp4UjA5Rk9ZU2hYVEdzQ3dFb2w0aGVtWkUyRVE3MW9Naml0X1g4UHI5bU51VmRXZkZGNjVHS2VBV3J6MDd1a01aN2huR9IBeEFVX3lxTE5SNUt4QVREWjFrTmpDWXcwNkZ3QTVQbnJCaTRrek1DRXJ6Zlllc010cm41TmpiLUxBM2JsRl9wWnBmU1lxRGktZzB2Q2dMYmdoMHBZdU9CdERtZ0lDeERzRW9XcFNTZnNGQTQ4ZEMwSW9vRW12Wi02UA?oc=5 |  |
| tax | press24.co.kr | 국회예산정책처, 2026년 세법개정안 토론회 개최 - press24(프레스24) | https://news.google.com/rss/articles/CBMiZkFVX3lxTE52S3FvcTZXUHh0OWRSamVwa3dncEREakFMNVY0dkxmUW1DT0ZDVWFIRDB3RzAtRHV4elVFM0cyc3hqT09KbjExZGRibXRma3JtdHJPYzNqYXZpeFZMOE5nR0VpVVRiUQ?oc=5 |  |
| tax | mbnmoney.mbn.co.kr | 국세청 세법 개정건의 10건 중 8건 반영 못 해…'실적 쌓기' 지적 - 매일경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wYjVGQjdSbkZCY2RpRjFvUjNyX0tpSFFDazNZVnFkcHdXY2hCd1Z5MUJKbmdNVG56NGdRc2trbnQzYXVoSUhGM25DRy05anRvNnhPYnlOYWdDSjdKOV9wSFgtbjgyaFBo?oc=5 |  |
| tax | mobile.newsis.com | '종부세 14억 공제' 요구한 與, 靑 "기존 입장 변함 없어"… 당내서도 이견(종합) - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE53ZHNfeHE4NmRkMWJTM2txcGpzZlBURGloUE1sV1F4NXplcjhjMnZvalZuNG9QNU9iZ0xfSmxjSlc4dDAwUHpXS0xrNktPMEZoMUMzel9xcGRDWEM1LVNxNTBVWVU4R3F6WEFlSFAtYkJjeGF4TkVEetIBeEFVX3lxTE53ZHNfeHE4NmRkMWJTM2txcGpzZlBURGloUE1sV1F4NXplcjhjMnZvalZuNG9QNU9iZ0xfSmxjSlc4dDAwUHpXS0xrNktPMEZoMUMzel9xcGRDWEM1LVNxNTBVWVU4R3F6WEFlSFAtYkJjeGF4TkVEeg?oc=5 |  |
| tax | paxmedicalnews.com | 2026 세법개정안에 병원계 ‘발끈’… “가업상속공제 제외는 필수의료 사형선고” - 팍스메디컬뉴스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1Dd3lHSEFoSWkzMDJXZVAwcnpDVjkyLXJYa0gwVURLSWJjeGhfTVZnV2pnVTZfdWdqTU1sZU9wM093UDhoT2dmUDdtVThCc3o3VlZEY3lVbzFuQTZCX3N6bHlvSDhrekpTdFFKcWpId3A?oc=5 |  |
| tax | sportsseoul.com | 국회예산정책처, ‘2026년 세법개정안 토론회’ 성료 - 스포츠서울 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAxY2luMmRVY3NUUEZNdkVZQzVPUURuSXZYRW1uU3EtLTFRcXRDUGp6WTgxX0o2NzNaamducGdHbENLYlY4bU1iOUZHNThXUnNaMGMtNHU1S2U?oc=5 |  |
| tax | speconomy.com | 민주당, 부동산 대책 TF 가동…세제 개편 논의 - 스페셜경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1MaHJHMnlyV1V6amNhbzZnM01tcS1qS2pEV0NfMjEwMjVxRUdLOW9qNlZkQzFxRWFQTldZMjZjaklQeTdwYVdqblBIc1RsenlZenM2MUFCYUt0QkJKc2p5azZWclZaUERxclktZA?oc=5 |  |
| tax | 매일경제 | 2026년 세법개정안 토론회 - 매일경제 | https://news.google.com/rss/articles/CBMiRkFVX3lxTE1OZjRDYkM3MUdVUExlMzRxZkZxM1VzTG41TDR6MXQ0ZDNBZHYtaGRBRGdOMFdQeV9MenRxWHFkSUxTMWpVMEE?oc=5 |  |
| tax | sejungilbo.com | [판세] 구 소득세법 17조의 '잉여금', 기업회계와 세무조정 중 어느쪽 잉... | https://www.sejungilbo.com/news/articleView.html?idxno=60676 |  |
| tax | 조세일보 | 세법개정, 소득재분배 효과…부동산은 복잡 [토론회] | http://www.joseilbo.com/news/news_read.php?uid=579256&class=7&grp= |  |
| tax | 일간NTN | [판례평석] 구 상증세법 시행규칙 제17조의3 제1항 각 호의 사유가 있으... | http://www.intn.co.kr/news/articleView.html?idxno=2054518 |  |
| tax | the-stock.kr | [이상현의 숫자IN] 세제개편안은 확정됐다는데 왜 또 공청회일까 | https://www.the-stock.kr/news/articleView.html?idxno=33794 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

