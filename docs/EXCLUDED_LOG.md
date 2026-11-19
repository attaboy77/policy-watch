# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-19 11:57:26 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1661건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 10 |
| excluded:company_self_activity | 4 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 16 |
| excluded:financial | 3 |
| excluded:industry_specific | 8 |
| excluded:manual_id | 1 |
| excluded:news_too_old | 38 |
| excluded:no_regulatory_signal | 42 |
| excluded:opinion_piece | 1 |
| excluded:reader_content | 1 |
| excluded:related_news_attached | 1 |
| excluded:similar_news_merged | 14 |
| excluded:smb_only | 1 |
| excluded:standard_setter_governance | 1 |
| collect:event_announcement | 16 |
| collect:incident | 1 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 270 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 211 |
| collect:out_of_window | 40 |
| collect:tax_subject | 36 |

## excluded:category_cap (10건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | dhdaily.co.kr | KSSB, 지속가능성 공시기준 첫 세트 공표…기업 대응전략은 - 대한데일리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1qTnFWLWFlSWx2cjVmaEswUXdpRUVlLU5BZHpTN3VlQWZWOHd4NEhqSVZxOThmRXR0eHpVbTlmcjNacFQ2RVl4Mlpmd0g3eXY4eGxVNDhzWUtTaEdCUUl3OHdNdVJfcnBHQnlr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | etoday.co.kr | [ESGX 이슈 5] ISSB, 자연자본 공시 지침 초안 발표…물·생태계 위험 반... | https://www.etoday.co.kr/news/view/2639995 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_self_activity (4건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ekn.kr | TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 | https://www.ekn.kr/web/view.php?key=20261118024331201 |  |
| esg | e-science.co.kr | HK이노엔, 지속가능경영 체질 강화…ESG 평가 최고 등급 | https://www.e-science.co.kr/news/articleView.html?idxno=140121 |  |
| esg | choicenews.co.kr | KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 | http://www.choicenews.co.kr/news/articleView.html?idxno=173128 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (16건)

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
| tax | sejungilbo.com | [판세] 사업 관련성 없는 지출의 매입세액공제 여부와 부가세법상 '수입... | https://www.sejungilbo.com/news/articleView.html?idxno=60677 |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
| icfr | tfmedia.co.kr | ‘회계사들의 올림픽’ WCOA 2026, 17일 개막…韓 외감법 전면개정 논의 | https://www.tfmedia.co.kr/news/article.html?no=208737 |  |
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 | https://www.impacton.net/news/articleView.html?idxno=30527 |  |
| esg | ESG경제 | 泰, ISSB 지속가능성 공시 의무화 확정…28년 SET50부터 단계적 시행 | https://www.esgeconomy.com/news/articleView.html?idxno=17232 |  |
| esg | ESG경제 | ISSB 자연 관련 공시 실무서 들여다 보니...S1ㆍS2 보완 | https://www.esgeconomy.com/news/articleView.html?idxno=17209 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 | https://www.impacton.net/news/articleView.html?idxno=30366 |  |

## excluded:financial (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 머니투데이 | 금감원 "대부업권 해킹 취약점 방치하면 엄정 제재"…보안점검 강화 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMicEFVX3lxTE4yeFVDRXpQbXNJbnNpS3VUdklPeUs3Tkt6OTBYTkVXbjlKR05za1doX1E0TWlGQ1hNTEdka0h0WjFsd1hiVWRzQ3FaZm5pd29Nd0tON3lqeFZvckxTQXRTQk9EQldaZU5JTWxGdVBPQW_SAXBBVV95cUxOMnhVQ0V6UG1zSW5zaUt1VHZJT3lLN05LejkwWE5FV245SkdOc2tXaF9RNE1pRkNYTUxHZGtIdFoxbHdYYlVkc0NxWmZuaXdvTXdLTjd5anhWb3JMU0F0U0JPREJXWmVOSU1sRnVQT0Fv?oc=5 |  |
| icfr | mobile.newsis.com | 금융권 해킹에 대부업권도 보안 점검…"취약점 방치 시 엄정 제재" - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE9VR09TSFF0WGZFR3VuSjVBNnZQNUtRczd2b3ZYTDhleldTd3NKWFVocnRoeDUyUDVVV0VDakVIbWZFV1htbkVlTnBTY3A1SHVpaVZFVEY4UlZ4N0txbkVnNlhrY2o5YVpSOE8tS0Q0enB2VUctOWRCddIBeEFVX3lxTE9VR09TSFF0WGZFR3VuSjVBNnZQNUtRczd2b3ZYTDhleldTd3NKWFVocnRoeDUyUDVVV0VDakVIbWZFV1htbkVlTnBTY3A1SHVpaVZFVEY4UlZ4N0txbkVnNlhrY2o5YVpSOE8tS0Q0enB2VUctOWRCdQ?oc=5 |  |
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |

## excluded:industry_specific (8건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 2025년 제1117호 보험계약 | https://kasb.or.kr/front/board/comm020View.do?boardMngNo=&boardNo=&cmtreadSeq=&seq=494&siteCd=002000000000000 |  |
| kifrs | 한국회계기준원 | 2022년 제1117호 '보험계약'과 제1109호 '금융상품'의 최초 적용 - 비교정보 (제1117호 보험계약) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=316&searchfield=ALL&searchword=%EA%B3%B5%ED%91%9C&s_date_start=2022-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2021년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=300&searchfield=ALL&searchword=1117&s_date_start=&s_date_end= |  |
| kifrs | 한국회계기준원 | 2018년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=231&searchfield=ALL&searchword=1117&s_date_start=2018-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2017년 제1104호 ‘보험계약’과 제1109호 '금융상품'의 동시 적용 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=220&searchfield=ALL&searchword=&s_date_start=2017-12-01&s_date_end=2017-12-31 |  |
| kifrs | 한국회계기준원 | 2015년 건설계약 공시 (제1011호 건설계약, 제1037호 충당부채, 우발부채, 우발자산, 제1115호 고객과의 계약에서 생기는 수익, 제2115호 부동산건설약정) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=166&searchfield=ALL&searchword=1115&s_date_start=2015-01-01&s_date_end= |  |
| kifrs | 금융감독원 | K-IFRS 제1117호‘보험계약’관련 사전공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36151&menuNo=200435 |  |
| kifrs | hapt.co.kr | '공동주택 회계 감리' 법안에 "옥상옥(屋上屋) 규제" 지적 | https://www.hapt.co.kr/news/articleView.html?idxno=169530 |  |

## excluded:manual_id (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |

## excluded:news_too_old (38건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | ESG경제 | 공인회계사회 새 회장에 최운열 전 의원 당선..."신외감법 유지해야" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5wczU3VWVubFMtUTdpOUI4Sm5XQUozYW9mVjRwQVY5TlEtRE5heC1nSnZrWV8waWZjNktsX2MxZk14TC1sRTdCdUxhbDdtZldlQkhsRElIVFBya25mLW5PLUFMd2xpR3c0X3VV?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | hitnews.co.kr | 新외감법, 연말 ‘밀어내기’ 잘못하면 포렌식 당한다 - 히트뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1SdW1ibmVsdHg0UGZIX2NnQmlWM0hEWUlBZHRMQXdPQzlDQzdnOXA0eHhKOVFsTFVZWGlLTnBlZmZsV3E5TlNrYWZBZS1MTW1OVi1MWjNFYVU2X3FmVEUyZ25mZzZtY3JDMHc?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | crowe.com | 감사전 재무제표의 제출 시행 안내(외감법, 2013.12.30 개정) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFB3dVdRS2NNTTdZdXQwam9iZ2JmU1ZBcENOMGhER2c1ajh3WWZtZUUtdjg5ckdaZVdJRlNGc1RycGQ4NHBjdHMyOFd6QThCMDRqNkxjd2d4RS0?oc=5 |  |
| icfr | 한국경제 | [한경 CFO Insight] 신외감법 2년...감사비용 70% 폭등 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCc1VNZVE2U181NVZDQzlZYnpVM2E1MEtxdXRDS00tUGVlN0ZSTFVzNTRhWFQxc1NKUFFtYjVKWEFDUmZkZVItN21jdkJvSFphVUVVY19QNVVlUQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | eiec.kdi.re.kr | ESG 공시의 의의와 쟁점 및 전략적 대응 방안 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9tYXBvOF9wUFVHeXFfS3JGVTItZkR4RmVkbHBac0lhdWdRXzZCN3M2V2JzU3dra0ZDczdCSDFwaDRqNlhrNGtwR0Npb3pCTkNoTmxzdU1nRnJpcXFJSl9WQXUtME8wOGFNdEE0?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |

## excluded:no_regulatory_signal (42건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | KEMI, 지속가능경영·동반성장 우수기업 9곳 선정 | https://www.esgeconomy.com/news/articleView.html?idxno=17378 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 매일경제 | “글로벌 투자자들, 재무제표급 ESG공시 원해” | https://www.mk.co.kr/article/12211811 |  |
| esg | 매일경제 | "ESG공시, 재무제표급으로" | https://www.mk.co.kr/article/12211428 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | raonnews.com | 107개사 ESG 공시 내년 실적부터 적용…근거법은 아직 국회 통과 전 | https://www.raonnews.com/news/article.html?no=62862 |  |
| esg | mediapen.com | 수자원공사·WWF, '물·자연 통합 복원' 나선다…기업 ESG 공시 대응 지... | https://www.mediapen.com/news/view/1138078 |  |
| esg | cnbizm.com | 백화점 업계, 상생·지속가능경영 성과 결실 | https://www.cnbizm.com/news/articleView.html?idxno=321436 |  |
| esg | ajunews.com | ESG경영개발원, 지속가능경영·동반성장 우수 기업·공공기관 선정 | https://www.ajunews.com/view/20261113135722843 |  |
| esg | dailysmart.co.kr | "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... | http://www.dailysmart.co.kr/news/articleView.html?idxno=132423 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| esg | vtimes.kr | BSI 영국표준협회, 지속가능성 공시 대응 과제 조명 세미나 개최 - 벤처타임즈 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE82eGVua2NvUTUzRnk2MjdUc3J1RTBlaGkwcEwxRWQ0d0lPRWoxX3M1UzduRlE5UWFjUkNGZVNPbGMyZmRmcjE3bTNhUVhnT0hQcjlhd0Z3N0JHdk9nakJnaFpnU1VkQQ?oc=5 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | 매일경제 | “글로벌 투자자들, 재무제표급 ESG공시 원해” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5wb2Z4TVdNX0NsQndNU08tQldGZ2JGOFhpTmVTM2x2b0FtY2xYOEVPWGFRaFdhTWw3Rk1jQWNnRHJ3WldSa3RyV1RldHRhLXZsaVE?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 컴투스 10년의 잔혹사 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBLLTQzb1pZam9pTm5QTXhNc0trU1dDZ25RMnFHQzNqT205STRTbTZ2dDl5TG4zTnhLTy1zczNIcUIwcGtNRm9iUUdNN1YzOXNiTTllXzdFaGRPbndkQkxhb0ZoWjdiMFhBbHloeQ?oc=5 |  |
| kifrs | newsspace.kr | [신간] ‘나쁜 회사 피하기’에서 ‘좋은 회사 고르기’로…이대훈 회계사의 『좋은 회사 재무제표』 - 뉴스스페이스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBDekZUalE5SG1xTWN2emRYYzd5S29LM3FRU0xnOTNBQkZaLUx0SXFQNnVHSDZVbm02TkJmTVVuT0xMcTRQYl9VeGJBeDZPbzdpa0htNG1rUzUteW4tNjlRLQ?oc=5 |  |
| kifrs | panewslab.com | 앱은 실현되는데 자산은 증발한다: 세 장의 재무제표로 해부한 암호화폐 업계 고통의 근원 - PANews | https://news.google.com/rss/articles/CBMif0FVX3lxTE9mTTZDWjBCV2tKRUgzaHRfV0hHOGtrQ2lLVFFIR2JSWW5sRFVTN0pLS1czTS1FQXJkQ1NzNm9RNzM3Y1RFREt2dTNGVTIwNTRSZnEySnF6azg2SlpxX0I1MG95MHlpQnNROWx4X0dFOVBfM0RzbXVVUUhLYU1FOFU?oc=5 |  |
| kifrs | industrynews.co.kr | 두나무·빗썸 실적 '희비'…가상자산 평가손실 '회계기준'이 좌우해 - 인더스트리뉴스 | https://news.google.com/rss/articles/CBMickFVX3lxTFBfTndtNzZCY2tiYk1BWjdCX1EzSnN0ZkVrX1F5WF9oQVVlcE5QOHVQU19QQVNIZkE0T0k0T2RUM3lfREhHY0VLYk9qbnF3T1FRVl9lMVdJRnBsazltSWlyaUYtcEJVZU80Y0lBenFYZ25UQQ?oc=5 |  |
| kifrs | newsfc.co.kr | 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5VMDZCcHJKdEg2cElfV3VMeGltTkdzamhGcXVCYVVnVE1DeGZOc3BoTlZacTVOakRiRTR2dDlaaG5kbXo3RkJUMkM4T0VhWmVPSkpzRDFpOE5QamZxX3JVeG1qemg5Nm9iNWc?oc=5 |  |
| kifrs | g-enews.com | 300억 달러 XRP 소각 요구 파장…전문가 "재무제표 스스로 지울 기업은 없다" - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxOOUFlbXlWWmo1SWw1OU5tYWFGSkw2SEMwRmJKNU1sclZ4b21Xa0stdWVJM2ZjV3A4NEEyOXJ4cVRyZXppVklfdHNiZkR4ZFlyekllS3RQcHE3YWF1OFp1N2NWeS1xQjJaV3dFYnFYdjJ3RzhGdm93THhaTFJNbGR0S2hCekllN3Zo?oc=5 |  |
| kifrs | asiatoday.co.kr | 비용 반영? 우발부채?…국고채 과징금 직면한 금융권, 자의적 회계처리 논란 - 아시아투데이 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5admNuOThERUZlR0JDRmtFdkJxXzRLR0doR3htVTIzcnZrbDVicTcyb0cweExNd2JQSEtGa044RkVTLVByV1hMMGJPMUZ2WjRIaVpjU1RHQUV5SThvcXdQOGE0MncyY1AwWlZmX3hn?oc=5 |  |
| kifrs | gokorea.kr | 가상자산 거래소 두나무와 빗썸의 운명을 가른 회계 처리 차이 - 공감신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE41aWlnRHBobDR2VmtwZFcwMFhlWTRycmJJQkN1MTBTSWFGci1VS2o1SE5uUzVQR3daVVlEZmZqNlZZUXdjWUpuQmFNeXZCWWxfdUc2NGc0WVR5RFpWNk9EdVRNUmRWZ0xL?oc=5 |  |
| kifrs | news.jkn.co.kr | 두나무는 흑자, 빗썸은 적자…가상자산 회계기준이 갈랐다 : 가상화폐 - 재경일보 | https://news.google.com/rss/articles/CBMiS0FVX3lxTE1mZ0EzSUxPNUI0YThHamNIRGpSVktnbTBaWWt3OEdIOWNQbkJkajFZRlRQb2l5UjBSQ05raUQ3UWxWUWlIRHNGQTZEUQ?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] 'SPC' 떼고 '상미당' 입은 까닭 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTE0zRURrYnhsLVhxYWJBMkVUQUNMeWF6NFBwUWFqdmwteXdlcTZTYWhsaThoY3R1ay15OEQ2Nk5zSFZVOVRZUUhFY2ItNzdVd1hpd0E1RUY4LVItRlphSHpUZzdvRG1fM21uQmkyTA?oc=5 |  |
| kifrs | vietnam.vn | 기후 변화는 기업의 재무제표에 직접적인 영향을 미칩니다. - Vietnam.vn | https://news.google.com/rss/articles/CBMimAFBVV95cUxPV2hpcHlnX2FQUWFUWnFIYmJWcDhiUGFCSXJPWWRVblJaQnNmZUVLVzcyLUp5N1hpckhVU2NnU0JUeFY5Zi1zRkdIR2dhTjZyeXFEalgxX3pDeTVBcEJQbVhiS2J6U2cxa3YtaWctRERwRUZfVXFrMm5sSWVBWnlpMlk5Vy1wU2NGOFR0OXNmTXF3UDZ6Ri0yUw?oc=5 |  |
| kifrs | tradingkey.com | LYCA\|Lycia Therapeutics Ord Shs\|가격:31.200\|Chg%:-1.630 - TradingKey | https://news.google.com/rss/articles/CBMibEFVX3lxTFA4MkV1MFh2eVp0Qkg4RHdMUTdZY0VXR0VZVGxPOUVESHBKSTBaY2hQdjBxcDR1NHhmZ2RidkFXVWNRWF9yNmsyM08xdkc1bUN6alVveWNYN3lBb2tCYWhmUlJzUERnSFBYUEhlUQ?oc=5 |  |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| icfr | mediapen.com | [ESG특별기고]데이터 내부통제체계, 지속가능성 공시 신뢰도 확보의 초... | https://www.mediapen.com/news/view/1138165 |  |
| icfr | asiatoday.co.kr | 신한금융, AX 전략 회계업무까지 확장… 그룹 내부통제 고도화 | https://www.asiatoday.co.kr/kn/view.php?key=20261119010007250 |  |
| icfr | lawtalk.co.kr | 회사 재무제표를 부풀렸는데 외감법 위반으로 처벌되나요 - 로톡 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SNHVGNVhqcF9pRjBSSFEtUzNPWWtJQldRYVAyY1hXZW1xaFB3ZWdKd1JHcXhXQ2YwQWU4cVBnWXNPcHZwYlhmU3NMWk9fd2M?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| tax | gpkorea.com | '중국차 대응' 국내생산 세액공제가 뭐길래…소득세 법인세 공제 | https://www.gpkorea.com/news/articleView.html?idxno=148759 |  |
| tax | news.ifm.kr | 추미애 경기지사, 재정 위기 돌파 총력…지방세제 개편·교부단체 전환... | https://news.ifm.kr/news/articleView.html?idxno=484643 |  |
| tax | sejungilbo.com | AI 덕에 반등한 법인세수, 올해 세법심사서 '세율인하' 결론은? | https://www.sejungilbo.com/news/articleView.html?idxno=61111 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:reader_content (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | ESG경제 | 'KSSB 공시 의무화 시대, 무엇을 준비해야 하나' 세미나 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE81V1p4YkEyeGp6aWFCY2lCYmcxVXNZYm5ZWEJrV21QR0NOSjZfMFN0RWgza3otTFR4ZjZzTnBoQU9sWkw5SDFkSS05bkRQUXBxY0l2LTVQaW5QbWFOR2FWcUZWVE1oSlpNR193ZQ?oc=5 | event |

## excluded:related_news_attached (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 관련 보도로 붙음: 2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요 |

## excluded:similar_news_merged (14건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | m.ekn.kr | TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1ZRHhKeVl5Yi1rVTdJcGwyQ0dnUUFyR01SZGQtX252WTRVaTU1NEVDQVFmSncwcHYtMDZwbW1qUmhjN052U1IzSks1Ym5ISXhYWHNkdGo5bHg3Qzg?oc=5 | → 대표: TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 |
| esg | ziksir.com | KB금융, 한국ESG기준원 평가 통합 A+ 획득…지속가능경영 성과 인정 | https://www.ziksir.com/news/articleView.html?idxno=153110 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | weekly.hankooki.com | 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 | https://weekly.hankooki.com/news/articleView.html?idxno=7193568 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | fashionbiz.co.kr | 신세계백화점, ESG 평가 2년 연속 A+... 지속가능경영 성과 | https://www.fashionbiz.co.kr/article/231039 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | globalepic.co.kr | KB금융, 한국ESG기준원 평가서 통합 'A+ 등급'…지속가능경영 리더십 입... | https://www.globalepic.co.kr/view.php?ud=2026111210164730997cc35ccc5c_29 | → 대표: "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... |
| esg | thefairnews.co.kr | KB금융, KCGS ESG 평가서 최고 등급 'A+'…지속가능경영 리더십 입증 | https://www.thefairnews.co.kr/news/articleView.html?idxno=93912 | → 대표: KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 |
| kifrs | 매일경제 | 올해 두나무 흑자·빗썸 적자…"배경엔 회계기준 차이" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9LX2JDMFhsRXJOQThUVDh1OTFTcl82am5FcUJ0NGQzdXZtVE5wRUNudF9qTkZHSFAtdmw3V1VIWXlwWEdZVmI5Y1hwUEx0ZFotV2c?oc=5 | → 대표: “글로벌 투자자들, 재무제표급 ESG공시 원해” - 매일경제 마켓 |
| kifrs | 파이낸셜뉴스 | 삼성전자 부사장, '글로벌 회계기준 제정'에 참여…韓 기업 목소리 커진... | https://www.fnnews.com/news/202611061034591232 | → 대표: 국제 회계기준 개정에 韓 목소리↑…자문기구에 삼성 부사장 합류 |
| kifrs | sentv.co.kr | 양대 거래소 두나무 흑자·빗썸 적자…회계기준 차이가 갈랐다 - 서울경제TV | https://news.google.com/rss/articles/CBMiZEFVX3lxTE14YzJVYUVpOU4zZXNOa1pUSVNaWDNLcGhHdUpDOXN4cjlhS2dsUVBQQW5qaDJhS2VOcTJEbWxuelhHaExKVEt6UHVjNjJtSFRRTFF0b2wydm9GUVYxY1lCOTI4bkc?oc=5 | → 대표: 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 |
| kifrs | polinews.co.kr | 두나무 898억 흑자·빗썸 1102억 적자…가상자산 회계기준 차이가 순손익 갈랐다 - 폴리뉴스 Polinews | https://news.google.com/rss/articles/CBMibkFVX3lxTE4xSHVHdlk3dk84N0JydWY3azBtME14WmtRUVprRU5zdWVidGxLYVpneGNZNHZnYlFBT2V6eG9rVS1vX2g3NThNRzZ4cGRuTVVkVks4cHRRa0tqdEk2azNQNTRvUzUtTTZRV2cySERn?oc=5 | → 대표: 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 |
| kifrs | biz.sbs.co.kr | 두나무 흑자·빗썸 적자 배경엔…업계 회계기준 차이 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5SQzNMZUM0ZUszQm52d2lneHpLTzJndC11OUx3MmdZVHFGeVIta1lCcUtkS1IzZU1WUEROR2hyVUxRcTd0Z0lpckNma0ZMdlBHal9J0gFYQVVfeXFMT3luQV9zaXFjc3U1NGtYYmVtbGQzT3BKVllmWjN0clZvY2l1UHowdkhzdHhHS2xVSnVtcTFzZFpIZXVpdzcxU21SYXptVjlvd2xJZ0VxdHI0Rg?oc=5 | → 대표: 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 |
| kifrs | safemoney.co.kr | 두나무 3분기 누적 898억 흑자 … 빗썸은 1102억 적자 - 세이프머니 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5IZlplYWhHQ01fRmlfTDBOenlLWWtQTDFPVllUOWhkR21fbDhYQ1N6aUI1a2YyaG1INmNRcmdUVkx2bVZoei1FZHZQT1YtX0dTNldhMFp6ZHp5aEw0VWRaNW5Oa3ZNOHc5TEdZbllR?oc=5 | → 대표: 두나무는 흑자, 빗썸은 적자…가상자산 회계기준이 갈랐다 : 가상화폐 - 재경일보 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:smb_only (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |

## excluded:standard_setter_governance (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국회계기준원 | 2026년 제9회 지속가능성기준위원회(IFRS 재단 정관 개정 공개초안에 대한 검토의견) | https://www.kasb.or.kr/front/board/calViewA.do?seq=1133 |  |

## collect:event_announcement (16건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융감독원 | 회계부정, 안심하고 신고하세요. 국민권익위원회-금융감독원, 신고자 보호 강화를 위한 업무협약 체결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249890&menuNo=200218 |  |
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
| kifrs | aimatters.co.kr | 엔비디아, 3분기 매출 154조 원…1년 전보다 103% 증가 - AI 매터스 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE1sZmU4bndidWZmbEhpMXNnU3BKRFRrREtZSDl0TmFsQWxsZmlwbzBIUE5zdUVaUmk4ejBaekhPU0R0aHdKX0dlVG5QNGZMTTRtckp4eQ?oc=5 |  |
| tax | 한국세정신문 | 세무법인 아성·아성ENL, 제1회 아성ENL 특강서 지목한 기피하는 세무대리는? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE4tU0lVb0ZaQUNvSlR4RTVuemtKcF9LemhSTk16SHNiNEZ1dEpUc1F4MGFWbEhZdFVib3l5SnhWQ0lLaGFPdDloazNGU1Y4WWxDLUY0OW80Z3pWZjExeVlBblVGZE4?oc=5 |  |

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

## collect:no_category (270건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융감독원 | 금융소비자보호처장, 인천대학교 방문 교육 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249914&menuNo=200218 |  |
|  | 금융감독원 | 26.6월말 기준 금융회사 해외 부동산 대체투자 현황 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249913&menuNo=200218 |  |
|  | 금융감독원 | 전동킥보드로 사고 내고 음주운전 차량 표적 사고 유발까지... 자동차 보험사기, 이렇게 예방하세요 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249905&menuNo=200218 |  |
|  | 금융감독원 | 자산운용사 침해사고 대응 관련 릴레이간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249903&menuNo=200218 |  |
|  | 금융감독원 | 26.9월말 국내은행의 원화대출 연체율 현황(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249902&menuNo=200218 |  |
|  | 금융감독원 | 全금융권이 상시적으로 철저하게 보안 관리에 임하도록 IT자산 식별, 관리를 의무화하고 취약점 점검, 평가 제도를 내실화하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249899&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 금융권 침해사고 관련 대부업권 설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249888&menuNo=200218 |  |
|  | 금융감독원 | 전금업자, 온투업자 침해사고 대응 관련 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249883&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 전자금융업 영업실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249882&menuNo=200218 |  |
|  | 금융감독원 | 흔들리지 않는 노후 준비의 기본 원칙 퇴직연금 가이드북을 적극 활용하세요! | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249868&menuNo=200218 |  |
|  | 금융감독원 | 랩 어카운트 관련 주요 분쟁사례 및 투자자 유의사항 안내 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249867&menuNo=200218 |  |
|  | 금융감독원 | 정부는 최근 발생한 금융보안원의 침해사고와 관련하여 철저한 원인조사 및 재발방지 대책 마련을 지시하였습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249862&menuNo=200218 |  |
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
|  | 재정경제부 | 경남창원 수출플러스간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079984&menuNo=4010100 |  |
|  | 재정경제부 | 대외경제협력기금-시민사회 간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079991&menuNo=4010100 |  |
|  | 재정경제부 | 「양극화 대응 TF」 세대 격차 완화반 1차 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079988&menuNo=4010100 |  |
|  | 재정경제부 | 국산 중고차 수출 원산지 증명 간소화 추진 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079957&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] '26년 국제통화기금(IMF) 연례협의 결과 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079980&menuNo=4010100 |  |
|  | 재정경제부 | 「세무사 시험 부정행위 대응 TF」 킥오프 회의 및 세무사 시험 부정행위자 시험 무효 절차 개시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079971&menuNo=4010100 |  |
|  | 재정경제부 | 전략경제자문단 AI에이전트커머스분과 현장방문 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079966&menuNo=4010100 |  |
|  | 재정경제부 | 국유재산 안전관리 체계 고도화 추진 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079967&menuNo=4010100 |  |
|  | 재정경제부 | 경제현안간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079962&menuNo=4010100 |  |
|  | 재정경제부 | 한국 주도로 9개국이 참여하는 글로벌 고신뢰 탄소시장(GVCM) 협력 기반 마련 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079961&menuNo=4010100 |  |
|  | 금융위원회 | 全금융권이 상시적으로 철저하게 보안 관리에 임하도록 IT자산 식별·관리를 의무화하고 취약점 점검·평가 제도를 내실화하겠습니다. | https://www.fsc.go.kr/no010101/88162?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 지역이 발굴하면 금융이 뒷받침한다. 지역 핵심 중소·중견기업에 4.5조원 공급 | https://www.fsc.go.kr/no010101/88160?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 정부는 최근 발생한 금융보안원의 침해사고와 관련하여 철저한 원인조사 및 재발방지 대책 마련을 지시하였습니다. | https://www.fsc.go.kr/no010101/88152?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 이억원 금융위원장,  글로벌 금융안정 공조 및 유럽 주요 금융당국과 협력 강화 나선다 | https://www.fsc.go.kr/no010101/88151?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 불법사금융 원스톱 지원,  이제 센터 방문 없이도 신청 가능합니다. | https://www.fsc.go.kr/no010101/88150?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 신진창 금융위원회 부위원장,  씨티그룹 국제부문 총 책임자 면담 | https://www.fsc.go.kr/no010101/88146?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 지역기업과의 동행, 6개 정책금융기관이 현장에서 함께 합니다. | https://www.fsc.go.kr/no010101/88143?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 잠자고 있는 포인트, 지역화폐로 바꿔 골목상권에서 쓴다 | https://www.fsc.go.kr/no010101/88142?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 서울 가격상승폭 둔화·매물 증가…수도권 내년 1분기까지 4만 호 이상 입주 | https://www.fsc.go.kr/no010101/88140?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 신뢰받는 자본시장, 현장에서 묻고 답을 찾다 | https://www.fsc.go.kr/no010101/88139?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 「전자금융감독규정 」일부개정고시안 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4189 |  |
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
|  | 정책브리핑(금융위원회) | 全금융권이 상시적으로 철저하게 보안 관리에 임하도록 IT자산 식별·관리를 의무화하고 취약점 점검·평가 제도를 내실화하겠습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789689&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |

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

## collect:out_of_scope (211건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(6차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 홈페이지 게시_본인 인증 서비스 일시 점검 안내(2026. 11. 14.(토) 22:00 ~ 2026. 11. 15.(일) 04:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI 실무 세미나 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] IASB 정보요청서, IFRS 9 '금융상품', IFRS 7 '금융상품: 공시' 위험회피회계 사후이행검토(PIR) 국내 의견조회 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] ISSB 자연 관련 공시 실무서 공개초안 요약자료(Snapshot) 국문본, ISSB 아웃리치 세션 및 국내 의견수렴 일정 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(5차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [세미나] IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/calViewA.do?seq=1129 |  |
|  | 한국회계기준원 | [세미나] 회계기준원-환경산업기술원, 지속가능성 공시기준 이행지원 세미나 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1127 |  |
|  | 한국회계기준원 | [세미나] 한국회계기준원 개원 27주년 세미나: 지속가능성 공시, 새로운 기준의 시대 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1125 |  |
|  | 정책브리핑(보건복지부) | 14개 권역심뇌혈관질환센터 재지정 평가 결과, 3개소는 조건부 재지정, 매년 별도 점검·관리 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789883&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 민·관이 함께하는 국유림 경영 합동 모니터링 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789880&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 인분 뿌리고 래커 테러까지... 전국을 무대로 한 보복대행 범죄조직 검거, 포상금 1,500만 원 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789876&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처 아시아·태평양 국가들과 식품안전 위기대응 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789872&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 더 나은 주거환경, 더 든든한 주거안정 "최저주거기준 높이고 공공임대 선택 넓힌다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789871&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해양수산부, 유엔환경계획(UNEP)과 유엔해양총회(UNOC) 개최 협력의향서 서명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789869&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 민·관이 함께 충남 태안군 가로림만 갯벌 복원을 추진한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789870&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 우리 바다 해수면 온도,  기상청이 3개월 후까지 미리 알려드립니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789874&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 「동남아시아·동아시아·태평양 지역  스캠 대응 연락그룹회의 원칙 성명」 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789875&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | '모두의 성장'으로 대전환을 위해 전 부처 역량 결집 - 양극화 대응 TF 사회격차완화반 1차 회의 개최 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789873&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 노사발전재단, 한·일 실노동시간 단축 정책 심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789868&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 기업의 기술보호, 진단부터 예방·대응까지 한눈에! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789866&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | "실패의 자산으로 AI 시대를 열다" 2026년 세계 기업가정신 주간 한국행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789864&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 2026년 1~3분기 벤처투자 및  벤처펀드 결성 역대 최대 실적 달성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789863&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 대한민국 우주 스타트업,  유럽 최대 우주 전시회에 함께 서다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789862&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 특허 정보에서 찾은 산업의 미래, '2026 캠퍼스 특허 유니버시아드 시상식' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789865&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 고소작업대 과부하방지장치(AML) '위법 개조' A제조업체 적발(익산지청) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789867&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 공공기관 자체조달 점검으로 공정한 입찰환경 조성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789861&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청 용역분야('26.11. 23.~'26. 11. 30.) 입찰동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789860&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처-육군본부, 육군 훈련병 대상 마약 예방교육극 첫선 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789856&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 일본과 데이터 이전 및 인공지능 프라이버시 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789857&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 국가보훈부 노사 상생워크숍 개최, 조직 발전방향 등 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789853&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 모두의 성장으로 대전환을 위해 전 부처 역량 결집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789855&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 모두의 성장으로 대전환을 위해 전 부처 역량 결집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789859&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 항생제 내성 대응, 인공지능·박테리오파지 등 첨단기술에서 해법 찾는다(11.19.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789854&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 한 해의 끝, 공정한 동행 가을겨울호와 다시 새기는 공정의 의미 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789852&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국립과천과학관, 수능 마친 학생들에게 '7가지 특별한 선물' 선사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789877&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 화생방 분야 기업과의 상생 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789846&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 대·중소기업, AI로 연결하고 상생으로 도약한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789845&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중소기업의 혁신성과와 미래비전을 한자리에, '중소기업 혁신대전' 처음으로 충청권에서 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789844&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, GLP-1 계열 비만치료제 온라인 불법판매 등 집중 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789843&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 주태국한국문화원, 개원 13년 만에 국유청사 마련해 새 출발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789842&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 2027년 열린 관광지 조성 사업 대상지 30개소 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789841&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 희망사다리 정책으로 더 나은 미래로 향한 이야기 19편 시상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789840&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 정부, '케이-콘텐츠' 수출 핵심 '케이-게임' 육성 의지 강조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789839&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처 '튼튼먹거리 탐험대' 박물관에서도 만나요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789838&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | '26년 중소기업 R&D 우수성과 한자리에 기술혁신 성과 확산의 장 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789836&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 실패를 넘어 새로운 가능성으로, '2026 재도전의 날' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789835&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 사용자 중심의 의료기기 개발을 위한 가이드라인 2종 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789834&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방 신기술·신제품, 11월에 국민의견 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789833&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제81차 유엔총회 3위원회 북한인권결의 채택 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789832&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 도전하는 장애경제인, 성장하는 대한민국! 중기부, 「제21회 전국장애경제인대회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789831&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 온라인과 오프라인을 잇는 소상공인 매장, 서울숲에 문 연다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789830&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 아·태 교통협력 넓힌다 … 한국의 인공지능 등 미래 교통기술 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789828&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 2027년 1월 1일부터 원전 차액계약 적용 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789829&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 수능 부정행위 결코 용납하지 않겠습니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789837&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 「2026년 국가기상레이더 활용 국제 워크숍」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789882&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 주택공급 활성화를 위한 경기도권 지자체장 만찬간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789827&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] "수능 부정행위, 결코 용납하지 않겠습니다." 범정부, 모든 역량 총동원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789826&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리 주재 제6차 12·29여객기참사 피해자 지원 및 희생자 추모위원회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789825&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 한성숙 국무총리,  제6차 12·29 여객기참사 지원·추모위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789824&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 2035년까지 전 세계 전기화 35% 목표, 라이즈 아시아로 이행 협력 본격화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789804&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 서민금융 현장방문 및 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789801&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국립문화유산연구원, '한국고고학 최신 연구 성과' 디지털로 잇고 세계와 나눈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789849&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 「청송 고와리 백석탄 돌개구멍」 천연기념물 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789847&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 우리만의 작은 일상, 국경을 넘어 세계의 마음을 연결하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789800&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, Java 보안 취약점 관련 개인정보 대량 유출 예방조치 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789798&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '2026 대한민국 게임대상',  헌신과 열정으로 올 한 해 빛낸 '케이-게임' 주역들 격려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789797&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, '26년 불법사금융 특별단속 성과 및 분석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789799&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(병무청) | 병무청-세븐일레븐, 사회복무요원 복지증진 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789793&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정은경 장관, 안성맞춤 재택간호센터 방문… 지역의료-간호 연계 점검 및 현장 의견 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789794&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 누리호 5차 발사 결과 검토회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789790&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 양평권역 소나무재선충병 방제 전략 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789789&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 소나무재선충병 총력 대응을 위한 전국 관계관 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789787&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 산림사업 현장에서 뇌졸중·심근경색 위험신호 알려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789785&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(통일부) | '북한 억류자 가족들이 호소할 수 있는 부서조차 없다'는 내용 관련 보도설명자료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789783&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | '수험생 안전 최우선', 수능 대비 대설·한파 대응체계 총력 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789782&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 한중 자유무역협정(FTA) 서비스·투자 후속협상 실질타결 선언 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789780&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)한-중 FTA 서비스·투자 후속협상  실질타결 선언 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789779&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제50차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789776&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금청, 새만금 크루즈 활성화 TF회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789774&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금청, 트래블쇼 2026 관람객 참여 최우수상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789772&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] '새만금국제공항 개발사업 기본계획 취소소송' 항소심 판결 관련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789767&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 강윤진 국가보훈부 차관， 독립기념관 기능개혁 추진상황 점검 및 현장 소통 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789766&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 여름철 재난 선제적 대응, 지방세 체납액 감소, 주민등록증 진위확인 서비스 확대 등 특별성과 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789770&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 우주 주권 시대 우주수송 역량 확대 필요성 토론회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789768&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 피지컬 인공지능(AI) 테스트베드 4곳 개소,지역 기업에 개방하여 실무인력 양성에 활용 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789765&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 오늘 가꾸는 숲, 미래를 지키는 건강한 숲으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789764&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 제약산업 혁신 민·관협의체 열고 국내개발신약 개발 촉진 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789762&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국유림 대부·사용허가 갱신, 이제 '모바일메시지'로 안내받는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789761&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "인공지능(AI) 시대 직업훈련의 미래는?" 한국기술교육대,  개교 35주년 고용·평생직업능력개발  발전 전략 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789759&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 근로복지공단,  '인공지능(AI) 윤리준수기관 확인마크' 획득 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789756&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (2026년 사업주훈련 우수사례 경진대회) '빙그레' 대·중견기업 부문 대상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789755&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 건설근로자공제회, SK 용인 반도체 클러스터 건설현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789754&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제14회 해오(海吾) 외교관상 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789753&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | '송이 감염묘 기술'로 인공 재배 송이버섯 10년 연속 수확 성공 - 국립산림과학원, 송이 감염묘 기술 안정성 입증...고성 산불피해지도 4년 연속 결실 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789752&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부, 차관 주재 「한수원 추진계획 점검회의」 2차 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789750&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | "공직사회, 새로운 업무 방식 보장하는 지도자 필요" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789737&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 전기장판·전기난로 안전사용 하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789749&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 데이터에서 정책으로… 생활인구, 인구감소지역 맞춤처방에 쓰인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789747&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 말이나 사진으로도 정책 제안 뚝딱 행안부, '모두의 광장' 새롭게 연다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789745&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 외국인주민의 일상 속 불편을 해결하고, 지역사회의 이웃으로 함께하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789743&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 사회조사 결과(가족, 교육과 훈련, 건강, 범죄와 안전, 생활환경) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789741&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 3분기 지역경제동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789740&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 데이터에서 정책으로… 생활인구, 인구감소지역 맞춤처방에 쓰인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789739&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 방류수 수질관리도 인공지능으로 고도화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789738&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.19.목.조간] (관계부처합동) 나부터 바른 복용, 다 함께 내성 예방 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789736&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 한신공영(주)의 자회사 행위제한규정 위반행위 제재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789734&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 전자상거래법에 따른 국내대리인 지정 가이드라인 제정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789735&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 2027 수능 강화된 부정행위 예방조치에 따른 수험생 유의사항 추가 안내 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789733&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영주국유림관리소, 산림 현장 찾아  임가 소통 및 규제합리화 사례 적극 홍보 - 임업인 대상 애로사항 청취 및 산림 규제합리화 사례 홍보 등 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789729&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 위치정보 산업의 미래, '2026 코리아 엘비에스 데이'에서 함께 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789719&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 쟁점 없는 특허심사 더욱 빠르게! 특허심사 '신속결정' 도입 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789726&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국무조정실장 주재 청년친화도시 지정식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789727&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 인공지능(AI) 활용 창작의 현재와 미래,  지식재산의 역할 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789725&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제22차 한-중동 협력포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789724&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 전파산업의 성과와 미래를 한자리에,  「2026 전파방송산업 진흥주간」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789718&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | '함께 만드는 교통문화, 함께 웃는 대한민국' 교통안전 유공자 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789723&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | "국민과 함께 만드는 안전한 철도" 자율보고 우수사례 16건 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789722&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 건설현장 사망사고 재발 막는다… 안전관리 강화 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789721&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 경남창원 수출플러스간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789716&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 2025년 산림휴양복지활동 조사결과 발표…국민 83.4% 경험 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789713&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 지역사회 문제 해결에 도움되는 자치법규 제정·개정,  법제처가 도와드립니다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789704&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 지역·필수·공공 의료 AX 가속화 위해 의료 현장-헬스케어 AI 민간 투자 연결 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789705&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, WWF·씨티은행과 숲에서 배우고 실천하는 ESG 활동 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789702&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부， 백범 김구 고품격 공예상품 6종 출시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789700&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 지방세, 지방행정제재·부과금 고액·상습 체납자 명단 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789709&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부, '지역기반 사회연대경제 혁신허브' 조성 대상지 6곳 선정… 지역문제 공동 해결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789707&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 수능시험일 위급재난문자가 발송됩니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789715&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 수능시험일 위급재난문자가 발송됩니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789717&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 최근 3개월간 대규모기업집단 소속회사 변동 현황 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789699&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(병무청) | 수능시험일(11월19일) 병역판정검사 휴무 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789703&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | "40년 신뢰의 K-의약품, 인류의 내일로" 제40회 약의 날 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789697&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부, 당정협의에서국군사관학교 창설 기본계획 수정안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789698&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청 양산국유림관리소, 규제합리화 현장지원센터 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789696&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 남부지방산림청, 산림사업장 안전보건 점검 및 문화 확산 캠페인 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789694&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 사비백제 왕릉·왕궁 규명 위한 조사 성과, 3권의 보고서로 발간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789691&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청 물품구매('26.11.23. ~ '26.11.30.) 입찰동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789688&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 안전 지킨 기업·공로자에 최고 영예... '제25회 대한민국 안전대상' 시상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789771&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능 시대의 불확실성, 시민이 묻고 답하다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789730&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 해군 최신예 3,600톤급 호위함 「평택함(FFG-833)」 진수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789687&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "시민의 권익 보호, 더욱 충실하게"… 울산광역시와 행정심판 '업무협약' 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789685&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 2027년 전국의료관련감염감시체계(KONIS) 참여 의료기관 모집(11.18.수) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789686&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 「제10차 한미 민관합동 경제포럼」 개최(11.17) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789684&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리, 충남 태안해역 위치소실 어선 관련 긴급지시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789683&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 대한민국 관광기념품으로 가득한 '케이-굿즈마을'에  '산타 대감'이 찾아옵니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789680&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 'AI로 여는 식품위해평가의 새로운 지평' 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789681&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 제9기 국가도서관위원회,  서울에서 제2차 도서관 현장 소통 이어간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789679&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 일본 정부에 글로벌 해썹 운영 현장 소개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789678&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 생산단계 농산물 안전관리 기준 적용 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789677&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 경북 상주에서 규모 3.6 지진 발생 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789682&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 경북 상주시 인근 규모 3.6 지진 관련, 원자로 시설 안전에는 영향 없는 것으로 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789676&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청, 누구나 쉽게 이용하는 소방안전 자료(데이터) 조회 서비스 제공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789673&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 자바(Java) 보안 취약점 관련  긴급 점검 및 보안조치 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789711&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 해광호 연락두절 가용자원을 최대한 동원하여 선박수색에 최선을 다할 것 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789731&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부 장관, 충남 태안군 해역 인근 위치소실 어선 발생 관련 긴급지시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789675&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 수능 끝낸 청소년, 휴식과 새로운 도전 시작한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789802&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 대외경제협력기금-시민사회 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789795&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 「양극화 대응 TF」 세대 격차 완화반 1차 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789792&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 국산 중고차 수출 원산지 증명 간소화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789710&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 김성환 장관, 유엔기후변화 총회에서 한국형 녹색대전환 기반 지구적 협력 확대 강조 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789672&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림치유로 중장년 남성 '사회적 고립' 해소 효과 확인 - 국립산림과학원, 동대문구정신건강복지센터와 연계 시범 운영 결과, 참여자 63.6% 대인관계·정서적 활력 개선 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789671&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 제4회 적극 행정 우수사례 7건 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789669&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한·호주, 유엔기후변화 총회에서 탈탄소 협력 모범사례 제시… 파리협정 이행 선도 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789668&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 겨울철 고병원성 AI 예방을 위한 방역상황점검회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789667&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 2026년 하반기 여행업계와의 안전간담회(11.17.) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789642&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 김용석 대광위원장, 타지키스탄 교통부 차관 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789641&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(관세청) | [동정] 이종욱 관세청장, 탄자니아 조세청장 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789638&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 폴리텍대학, 미국 WITCC와 손잡고 글로벌 인재 양성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789637&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '축산의 미래를 만나다' 제4회 스마트축산 AI 경진대회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789636&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "회계부정, 안심하고 신고하세요!" 국민권익위-금감원, 신고자 보호 강화를 위한 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789635&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 소속 공무원 대상 산불 현장 대응 교육·훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789633&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 국민연금, KB금융지주 주주총회에 대한 의결권 행사 방향 결정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789634&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 난임지원제도 개선 위한 의료계 의견 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789630&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, 부산대학교병원 해양의료연구센터 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789878&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 국가 희귀·특산식물 보전기관 3곳 신규 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789626&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 중장년, 일과 삶이 있는 녹색지대를 걷다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789627&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부 장관, 수출 1조 달러 앞두고 수출 최전선인 인천신항 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789628&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [담화문] 수능 부정행위 대응 관련 대국민 담화문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789621&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 「2025년도 주거실태조사」 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789623&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 전남광주통합특별시 장성 종오리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789622&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 정부, 페루 엘니뇨 피해 대비 인도적 지원 제공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789618&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청·SK임업, 기업림 최초 산림OECM 등록 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789616&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부장관, 합동군사대학교 및 육해공군대학 총장, 학생장교 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789620&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부, NATO 우주발사협력체계(스타리프트(STARLIFT)) 양해각서(MOU) 서명 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789619&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | "한국과 세계를 연결하는 K-Pop" 외교부, 미래 공공외교 주역들과 만남 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789617&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 구미국유림관리소, 산양삼 재배 현장 찾아 임업인 애로 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789614&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청 양산국유림관리소, 규제합리화 현장지원센터 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789612&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청장, 소나무재선충병 피해목 방제 현장 안전 점검 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789610&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 반도체 검사 핵심기술 경쟁력 강화를 위해 산업현장 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789608&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 해외 '가짜 K-브랜드', 정부가 기업과 함께 막는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789607&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제8기 FEALAC 국민대표단, 청년 민간외교관 활동 성황리에 마무리 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789606&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 방송미디어 산업 인공지능 전환 세미나 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789602&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 「(약칭) 초광역특구법 관련 원포인트 사회적 대화」제9차 실무협의체 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789600&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 재선충병 확산 차단 및 중요 소나무 숲 보호 기반 마련을 위한 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789597&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 아·태 및 아프리카 세관공무원, 한국 관세행정 배운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789595&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금청, 코리아 마이스 엑스포 참가해 새만금 마이스 유치·홍보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789593&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 사상 첫 '방한 관광 2천만 명 시대' 개막… '대체불가 관광대국 대한민국' 향해 민·관·정 뜻 모아 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789592&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 폴리텍대학, 뿌리산업 빈 일자리 해결을 위해 네 번째 뿌리산업센터 개소 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789591&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 국립평화통일민주교육원,  해외 전문가 특강 및 세미나 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789599&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 인공지능 시대 국가지식정보 활용 혁신 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789581&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 중앙·지방이 함께 국민의 목소리를 정책에 반영, 2026년 제8회 중앙지방정책협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789590&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 「고등교육기관의 평가·인증 등에 관한 규정」 및 「고등교육법 시행령」 일부개정령안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789588&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 「특수외국어 교육 진흥에 관한 법률 시행령」 일부개정령안 국무회의 통과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789587&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 국가데이터처, 제10회 저출생·고령화 국제 심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789586&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 이종욱 관세청장, 주한 유럽연합(EU) 대사 면담...  한-유럽연합(EU) 관세협력 강화 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789579&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 벌목현장 특별점검으로 산림사업장 안전확보 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789577&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 2026년 10월의 관세인에 이다혜 주무관 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789578&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 일터의 안전부터 관광레저와 자원의 가치까지, 공공의 책임을 위한 감사 협력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156789567&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-19&endDate=2026-11-19&srchWord=&period= |  |

## collect:out_of_window (40건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융위원회 | 「금융위원회와 그 소속기관 직제 시행규칙」 일부개정령(안) 입법예고 (게시 2026-08-11) | https://www.fsc.go.kr/po040301/view?noticeId=4164 |  |
|  | 금융위원회 | ｢자본시장과 금융투자업에 관한 법률 시행령｣ 일부개정령안 입법예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4163 |  |
|  | 금융위원회 | ｢증권의 발행 및 공시 등에 관한 규정｣ 일부개정고시안 규정변경예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4162 |  |
|  | 금융위원회 | 「자본시장과 금융투자업에 관한 법률 시행령｣ 일부개정령안 입법예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4161 |  |
|  | 금융위원회 | ｢외부감사 및 회계 등에 관한 규정 일부개정고시안｣ 규정변경예고 (게시 2026-07-24) | https://www.fsc.go.kr/po040301/view?noticeId=4160 |  |
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
| tax | christiantoday.co.kr | [특별기고] 해외선교비 세법개정(1) 시행령 개정 3가지 제안 | https://www.christiantoday.co.kr/news/376875 |  |
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
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | daenews.co.kr | 정부 세법개정안, 세수 얼마나 바뀌나…국회서 여야·전문가 토론:동아경제신문 & daenews.co.kr - 동아경제 | https://news.google.com/rss/articles/CBMiRkFVX3lxTE9FcWU2RXNFenNRUnYyVUVzdFVjZHdvWGJhbEw2c2VWc0NmaWh2RHV5T29iRUlyVGtseHMyRHkxRlN3RG84QlHSAWJBVV95cUxNc2phRE9Fem1ZUUdTTndwOTlpNlBXNGpwVW1MTEhDeFhiR1hpNWVFU3pkVzFaUEh2UTNSLVJxSjhXdHBHTXNGRGF4TkZTVnVSc2pGSVBSeG9ZeERnNnd5QlBSUQ?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzDSAWBBVV95cUxOeDlrTWJMLVFFUHdRdGFKSnZYenV2UWl2UnZxTUtyamE4YUNfSjVfSzNHY2U4eEQ1X096RGc2aE9BN3dMUGlnaE56N1I2c2c0bkZkVTR0a1lJR1pUQWxUSGk?oc=5 |  |
| tax | sejungilbo.com | [토론회] “체감 경기 회복 vs 과세 예측가능성”…`26 세제개편 쟁점은? - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE14eTJsdUFhend0enBURENHX2dBT0pFdS1mcU9pcGo3UllMbXZsU2x3OG1jb183aFBKZFJQb3ZGWlgxQUVqM1YwZDNRV1JlX0F6SWdiVHdyTzRQRXNnY0FqczZNZ1Ixam80UGFMZw?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | mbnmoney.mbn.co.kr | 국세청 세법 개정건의 10건 중 8건 반영 못 해…'실적 쌓기' 지적 - 매일경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wYjVGQjdSbkZCY2RpRjFvUjNyX0tpSFFDazNZVnFkcHdXY2hCd1Z5MUJKbmdNVG56NGdRc2trbnQzYXVoSUhGM25DRy05anRvNnhPYnlOYWdDSjdKOV9wSFgtbjgyaFBo?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편(안) - 관세 관련 주요 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1yTlpBMnR1ckFpME9OejMzRlZtR2F6M1dIVnRXX045ai1JRzVSay1rSFlBM0NyMUtpSmpxd3BrejdsRjJqS2h0V1c1Nkk2bnBBQ0lienBVcTN6cGdtQWFILWI1LWdFZ3BsUVFfRXBB0gFyQVVfeXFMTU5pOE82QWtSQ0xwZnM3TjNmRWhIMkFwRWFEMlJKcGJwaThDc3gyOENnbld1ZkgtdjZ2SE9fTzd1a0VNWk9mVl9jM2pKUE1oemMwSFJpYVNVMWRrNzhWbHpKV0JlaWNRUy1lc3JNd3RNR2FR?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | yna.co.kr | 신문협회 "가업상속공제 대상서 신문·잡지 제외 법안 반대" - 연합뉴스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFB6SnRXeHRNMnV0eXZLR2R4MjczVy1lZUk4SFBOZ1FQNVpPNTdrZGhLaEpTNGF4SFZjX242d2ROZnpZdmhjWWFRd3Z3RnJzY0tQdXl2Q05PdnY5OHJyUk96OdIBYEFVX3lxTFB6SnRXeHRNMnV0eXZLR2R4MjczVy1lZUk4SFBOZ1FQNVpPNTdrZGhLaEpTNGF4SFZjX242d2ROZnpZdmhjWWFRd3Z3RnJzY0tQdXl2Q05PdnY5OHJyUk96OQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 자기주식 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE10Z2JDX19vOTFPSjh5emQxNU5VS3ZSSWIzUEl2VGttU25JYkRHakRnc1J4aTNxSGlucERoeVJ3eVVQb2p5RF8xaWpuSDBBNGRoUGpTTXR6aUJoRHV2NkJTSElON21BaHZGY1BwdEJR0gFyQVVfeXFMTXhQbVZzYkttYnNseFB0a2VORGYzTXVObkhxQXNPSDZ6SlZiU2R5bVA4eUZlX2p2Zm5IY1p3dTFrelo3dmprMDVUaTlKcjFTb2R0RmstU3l2LW1SWTNYZXRsYTZjc3BTbkc3UUFQeVF2MlRR?oc=5 |  |
| tax | 한국세정신문 | 대통령 업무보고까지 했으나…국세청 '세무플랫폼 감독규정 명문화' 불발 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1WUmhWcEZCbHdGN2h1RTR4aHdsaFV0bTVjWDVfWHdGVVdKREpvTnAyVUM1djVfYTdLbFhRWE1tV2Rwd25tRzZYQWNpZF8xU2lyYmtJVHFaRUNscWJobHBTQ3VRdWw?oc=5 |  |
| tax | lawtimes.co.kr | (29) 법률가와 세법 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9UYnRhb200WmtsSXk2QUxnQ1NPQkVVS00ySENCS2Q1TlNZV3BIU3JPUEhsUURCU2JYTU1kY1c1UFVOVDdkRVBlXzhHbVlZVnBhclZreEI1OWYtWUhUQXhrV2NGUnNULV9JZlNtZlZn0gFyQVVfeXFMT0cycGlqMEhfNDJEX1ZqNWxycnlIX0pUMEN1bDB5ejlTUi1wdEt5RkM3UTdMT0Q0X2Yxajdzc0JqTllEdkpBdXo1UGlGMWZhUlJSMkNlS3oxRHZoMHhHQWNIR3g1TzlGaGEtX3YtLU5jQ2lR?oc=5 |  |
| tax | pressian.com | 익산참여연대 "정부 지방교부세법 개정안 철회 촉구…지방과 충분히 협의해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTE0tTFE0Nzd0b0stb1gyNDFJU3hiMllsR2xxdl9KYV9LWi1DWGtLYS1waHo5U0dZbzhLY2tzdU1fblp6RnQ0TTZndGFzOHlxNXFpcjBMSUs0Yl9UN0ZHWDA1bFVxYWlxZmtXdVEw?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | nodongilbo.com | 국회예산정책처, 2026년 세법개정안 토론회 개최 - 노동일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5Sc2Zjd0pLdFN1WVVVVUtkSUMwRXgyOGNUd3hsU0tsT1ZzY181TmlFb2hGSFRNekNBYmVNYWQ3NVROZUtUbG11X09WMW40cFJCRXpzTmszR0dVMEFNQnB2UXVQRzFISUZqalNRY3p3?oc=5 |  |
| tax | newspim.com | [뉴스분석] 부동산 세제개편안 정부안 의결…與 내부서 불거지는 수정·보완 목소리 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBaMU94ZFRIbWRacklQenVyOHN0dUxYc3AzM0ZveTR5a3Fvd0NsaW9jcVNNRGN3emRCcUFCQWJsa0J5TEFNWnd3bEc1cExsRlNSVDJCMWNNWEkxOWQz?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | newneek.co | '월급방위대 TF' 출범, 내년 월세 공제·교통비 환급 어떻게 달라질까? 💰 - 뉴닉 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE1HYjd1QjBqWEE4ZzRNVzhOV00xTGhaeGl6YlpZSUx4OVdRZmJFc0YtMzdpeXhHN1JCTGlqX0xEb1JUcERRVV9zZkh5SFJOZVBGM3Yw?oc=5 |  |
| tax | metroseoul.co.kr | 바뀐 세법에 재건축도 '소형' 쟁탈전…압구정도 "평수 줄이자" - 메트로신문 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE4xdVlMUlBtV3pZdEtBRm9Ea25ya1lKb2Q0STd6UEJFUllLem9HTjV3VFU1aHBEbjdHdGF3WVdLSnFWRXpkRDZpZHRmS081RHdxRkFBRTZYcVdNenRUUUtGbQ?oc=5 |  |
| tax | seoulapt.co.kr | 아파트 관리업무 한눈에…LH, 법령·판례 담은 공동주택관리 매뉴얼 배포 - 서울아파트신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE0yVHpLSHZ2YjBvUzRCTF8yVUVxelBlOXJiUEZnRy01VWp0Qm8xRzRrZGtQVHMxYWtHRkp0RlplV2lqaXcxQ2hvR1RacjVCcEVES0hFdFlOS0szTG5zZTV5N2RWQmQ5RzZpZGRv?oc=5 |  |
| tax | sportsseoul.com | 국회예산정책처, ‘2026년 세법개정안 토론회’ 성료 - 스포츠서울 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAxY2luMmRVY3NUUEZNdkVZQzVPUURuSXZYRW1uU3EtLTFRcXRDUGp6WTgxX0o2NzNaamducGdHbENLYlY4bU1iOUZHNThXUnNaMGMtNHU1S2U?oc=5 |  |
| tax | sejungilbo.com | [판세] 구 소득세법 17조의 '잉여금', 기업회계와 세무조정 중 어느쪽 잉... | https://www.sejungilbo.com/news/articleView.html?idxno=60676 |  |
| tax | 조세일보 | 세법개정, 소득재분배 효과…부동산은 복잡 [토론회] | http://www.joseilbo.com/news/news_read.php?uid=579256&class=7&grp= |  |
| tax | 파이낸셜뉴스 | '비거주 차등과세' 부동산 세제 개편 담판 돌입 | https://www.fnnews.com/news/202611181806111022 |  |
| tax | dnews.co.kr | [단독] 지방거주자 보유 서울주택 17만호… ‘실거주 유도’ 세제개편 ... | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202611171459280860481 |  |
| tax | m.skyedaily.com | [이재명의 세무테크] 2026년 세제개편안 시행령 | https://m.skyedaily.com/news_view.html?ID=314646 |  |
| tax | joongboo.com | 경기도 집합건물 20년 초과 보유자 35.1% 급증…"8·3 세제개편안 등 영... | https://www.joongboo.com/news/articleView.html?idxno=363742703 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |
| tax | 서울경제 | 법 해석 하나에 수십억 오간다…기업들은 지금 ‘조세 법률전쟁’ 중 | https://www.sedaily.com/article/20102602?ref=naver |  |

