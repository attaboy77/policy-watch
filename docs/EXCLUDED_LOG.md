# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-27 15:12:36 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 금감원 심사·감리지적사례 중 FSS/24xx 이전·공개번호 없는 행: 178건 (제목은 남기지 않음)
- 네이버 검색 결과 중 카테고리 미분류: 1582건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:company_event | 3 |
| excluded:company_self_activity | 5 |
| excluded:corporate_pr | 2 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 3 |
| excluded:financial | 1 |
| excluded:foreign_news | 1 |
| excluded:foreign_tax | 18 |
| excluded:industry_specific | 9 |
| excluded:manual_id | 2 |
| excluded:no_regulatory_signal | 96 |
| excluded:nonprofit | 1 |
| excluded:other_industry_tax | 17 |
| excluded:related_news_attached | 1 |
| excluded:similar_news_merged | 44 |
| excluded:smb_only | 3 |
| excluded:standard_setter_governance | 1 |
| collect:event_announcement | 40 |
| collect:incident | 3 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 287 |
| collect:noise_keyword | 1 |
| collect:non_kifrs | 31 |
| collect:old_year | 8 |
| collect:out_of_scope | 209 |
| collect:out_of_window | 182 |
| collect:tax_subject | 34 |

## excluded:company_event (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 매일경제 | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5mdFY1aERzd2ZQLUpWWHVjVWxVZEZHMWZFVTc3WHQ3MzQ4ckVHd3hpMlRTVHd6MFdUb2NvTlBaUmZzUTNCdUFqdC03bkZkR1FZNWc?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ZXAtQlFZQjUwUV9rbDZDZ0dodTF2MGw1MG9NS09xRUFJekhCQlcxVk4wWkJmZVRoYlkwR2xNdGJEbmVrdU5LRV9qZXpzbkNXVVVNeXlDc3BRZ0XSAWBBVV95cUxQVjBoZ29XNWttV2hfYkFPTG1KWjRuTXRadFBtQnhON29lekYyck5PelV1b3hnbHZVa291TmpZQmdRak1FNmhKLTFTWkZsOGJSZnBUQV91eG9kNXNiV0sxcHE?oc=5 |  |
| tax | financialreview.co.kr | [강동형 칼럼] 대손세액공제, 부도보다 대손확정일이 가른다 | http://www.financialreview.co.kr/news/articleView.html?idxno=46483 |  |

## excluded:company_self_activity (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국세정신문 | 화우, 장석일 전 금융감독원 전문심의위원 영입 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5VRG5McUJSRjdzQXBoblpGYjBXaW4xTndXX0ZMTDhqbm5VQ0JrV1lQUzJKWDZtOWNrclV0ZjZZUFNYRW9UNEt3b3UwcFBtZjc4SXVSN0t3UHk3WmVPQTFFNkdNRm4?oc=5 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBhZ3dNVjNHQldlUXYzVlltVzgwTGtmb1ZMWlh1SHZwNDBhemYtTkF6c1dPVmxyNHE1dlVuSTg1ck1yUHB4MzVqdlRjQ3R5R296RXc?oc=5 |  |
| esg | ESG경제 | TNFD, ISSB에 자연 관련 공시 기준서 도입 촉구 | https://www.esgeconomy.com/news/articleView.html?idxno=17565 |  |
| esg | fntimes.com | 동양생명, ESG 경영 내실 강화…우리금융과 지속가능경영 시너지 [보험... | https://www.fntimes.com/html/view.php?ud=2026112618041682009efc5ce4ae_18 |  |
| tax | sejungilbo.com | 김주영, 조세특례제한법 개정안 발의…2031년 말까지 연장 | https://www.sejungilbo.com/news/articleView.html?idxno=61103 |  |

## excluded:corporate_pr (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성 공시기준에 투자자 수요 반영…전문 위원회 확대‧강화 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTFB5REltcVJCVXFjN1o0WHJPOUlxQ0hYSGdMS2VZcWhuaGtkMkdDWU5tZmpNa3dSdzhQVUxmNUNLcy1hTkRPV01fU2UyZGxXNGk3R0ZIQmZ0Sm1sWDE4WUZrQjNZTQ?oc=5 |  |
| icfr | asiae.co.kr | 중대 보안 취약점 방치 땐 CEO 책임…금융당국, 금융사 내부통제 강화 추진 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wVHBFeHhiNjhDb1pVRzYwbXFYTmRrZmhpOFNWS0laVUNkeGZ4NUdGQVY2eGJBWmdlRHJ6SFFsaEM5bW5RQ0FyazRqY0tUWmhnRHJYVjdLSUZwUjJRd2Y3TQ?oc=5 |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |

## excluded:financial (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | newsworks.co.kr | 금감원, 증권사 발행어음·IMA 내부통제 '고삐'…모범규준·TF 가동 - 뉴스웍스 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1vbk55YWxXWG1IdVdWeUQ4N3hRTENQNTJ2MU5vRHVoSUd3aEFWbzMtMEdSalNOQ0V0c295d3FFbENLQ1oyQWZLZEhwU2xianFXd2hkLUlQcmNIUHYtODg3LWhEblNvV0RVTHpubE1ya9IBc0FVX3lxTFBVWkwtM3MzbHl6RzhDaTRSd3BBVnRINjFTQWVhTms3UGQ1YjJpbU95NmFMd2JacXZnOFlSaHdRQzAyeVI3V05hVzB5amM0UE5qZXdxVVRhX2FpSHBmUzh1aU1mQVR4d3BYVmgyNnZTRDBuNDg?oc=5 |  |

## excluded:foreign_news (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | tfmedia.co.kr | [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... | https://www.tfmedia.co.kr/news/article.html?no=209185 |  |

## excluded:foreign_tax (18건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | dgmbc.com | [글로벌+] 베트남 수출 업체, 부가세 환급받는다!···노점상 풍경 변화... | https://dgmbc.com/NewsArticle/868677 |  |
| tax | ferrotimes.com | 베트남 진출기업 부가세 환급길 열려…장기 지연 애로 해소 | http://www.ferrotimes.com/news/articleView.html?idxno=51011 |  |
| tax | viva100.com | 베트남 내국수출입 부가가치세 환급 소급 적용 방침 | https://www.viva100.com/article/20261021500003 |  |
| tax | busan.com | 베트남, 내국수출입 부가세 환급 소급적용…한국기업 유동성에 큰 도움... | https://www.busan.com/view/busan/view.php?code=2026102017145939514 |  |
| tax | dnews.co.kr | 베트남에 묶인 韓기업 400억 부가세, 4년 만에 풀린다 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202610201401483130324 |  |
| tax | hellot.net | 정부, 3년 넘게 막힌 베트남 부가세 환급 길 열어...진출기업 유동성 숨... | https://www.hellot.net/news/article.html?no=115621 |  |
| tax | naeil.com | 베트남 진출기업 ‘부가세 사태’ 해결 | https://www.naeil.com/news/read/605679?ref=naver |  |
| tax | straightnews.co.kr | 베트남 진출기업 '부가세 환급 지연' 해결…400억원 이상 자금 부담 완화... | https://www.straightnews.co.kr/news/articleView.html?idxno=313518 |  |
| tax | pinpointnews.co.kr | 베트남 진출기업의 내국수출입 부가가치세 환급 길 열렸다 | https://www.pinpointnews.co.kr/news/articleView.html?idxno=496751 |  |
| tax | 일간NTN | 베트남 진출기업 부가세 환급길 열려…세무 불확실성 해소 큰 도움 | http://www.intn.co.kr/news/articleView.html?idxno=2054159 |  |
| tax | etnews.com | 베트남 진출 한국기업 부가세 환급길 열렸다…최소 400억원 규모 | https://www.etnews.com/20261019000431 |  |
| tax | tfmedia.co.kr | 묶였던 부가세 환급에 발 동동…범부처 공조로 베트남 진출 기업 숙원 ... | https://www.tfmedia.co.kr/news/article.html?no=208162 |  |
| tax | news1.kr | 베트남 진출기업 '부가세 환급' 숙원 풀려…법 개정 전 거래도 소급 | https://www.news1.kr/economy/trend/6325051 |  |
| tax | news.einfomax.co.kr | 李대통령 "베트남, 韓기업에 부가세 환급 소급 적용…최소 400억 규모" | https://news.einfomax.co.kr/news/articleView.html?idxno=4440003 |  |
| tax | 조세일보 | 베트남 진출기업 부가세 환급 가능해져…과거 거래도 대상 | http://www.joseilbo.com/news/news_read.php?uid=577706&class=7&grp= |  |
| tax | 한국세정신문 | 베트남 진출기업 내국수출입 부가가치세 환급 길 열려 | https://www.taxtimes.co.kr/news/article.html?no=277366 |  |
| tax | 파이낸셜뉴스 | 베트남 진출 기업 최대 애로 '내국수출입 부가가치세 환급지연' 해결 | https://www.fnnews.com/news/202610191714419790 |  |
| tax | sejungilbo.com | 베트남 진출기업 부가세 환급 지연 해결…400억원 이상 환급 길 열렸다 | https://www.sejungilbo.com/news/articleView.html?idxno=60696 |  |

## excluded:industry_specific (9건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 2025년 제1117호 보험계약 | https://kasb.or.kr/front/board/comm020View.do?boardMngNo=&boardNo=&cmtreadSeq=&seq=494&siteCd=002000000000000 |  |
| kifrs | 한국회계기준원 | 2022년 제1117호 '보험계약'과 제1109호 '금융상품'의 최초 적용 - 비교정보 (제1117호 보험계약) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=316&searchfield=ALL&searchword=%EA%B3%B5%ED%91%9C&s_date_start=2022-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2021년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=300&searchfield=ALL&searchword=1117&s_date_start=&s_date_end= |  |
| kifrs | 한국회계기준원 | 2018년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=231&searchfield=ALL&searchword=1117&s_date_start=2018-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2017년 제1104호 ‘보험계약’과 제1109호 '금융상품'의 동시 적용 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=220&searchfield=ALL&searchword=&s_date_start=2017-12-01&s_date_end=2017-12-31 |  |
| kifrs | 한국회계기준원 | 2015년 건설계약 공시 (제1011호 건설계약, 제1037호 충당부채, 우발부채, 우발자산, 제1115호 고객과의 계약에서 생기는 수익, 제2115호 부동산건설약정) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=166&searchfield=ALL&searchword=1115&s_date_start=2015-01-01&s_date_end= |  |
| kifrs | 금융감독원 | K-IFRS 제1117호‘보험계약’관련 사전공시 모범사례 | https://www.fss.or.kr/fss/bbs/B0000128/view.do?nttId=36151&menuNo=200435 |  |
| kifrs | hapt.co.kr | ‘공동주택 회계 감리’ 법안에 “옥상옥(屋上屋) 규제” 지적 - 한국아파트신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1zVlZtb2JHeEpyV204Q3FUVTRVU1JiRWswRmZuR3RDUEk0TFVhRlI3OVgzek00MlZwOGlQUmp4elFQRkFjMDh2YThBV05WZlhzeV9SZmhWMEl4WF9DcUZDc0ZwOWh3aEcy?oc=5 |  |
| kifrs | hapt.co.kr | '공동주택 회계 감리' 법안에 "옥상옥(屋上屋) 규제" 지적 | https://www.hapt.co.kr/news/articleView.html?idxno=169530 |  |

## excluded:manual_id (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |
| tax | 일간NTN | [국세 예규] 상시 주거용 임대 오피스텔 양도 때 부가세는? "사실판단 해... | http://www.intn.co.kr/news/articleView.html?idxno=2053355 | 주거용 오피스텔 임대·양도 부가세 — 제조업 법인과 무관 (일간NTN [국세 예규] 상시 주거용 임대 오피스텔 양도 때 부가세는?, 11/20) |

## excluded:no_regulatory_signal (96건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, 제9대 회계기준위원회 상임위원 선임 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBxNGhCdE9jdjB1WWp4WGdJd3BHNmxpVVRkMHBoaWdlc1NSbHlydTJIR0JyR0pLanJlVEtlcndHTmFkSjEyWnhiM2pnOHVLeUxPam04T1pNNUgycW9vREx1VklyREJ0WmdDT0E?oc=5 |  |
| kifrs | CPA뉴스 | [재무제표 수다떨기] 중소기업 결산 부담 덜어주는 '회계처리 특례' 핵심 정리 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBKelZUejQ5TnZobWNMcmZGbWZ3YU1Yd2toSHI1VDUtanM1aW9pWjY5YU1QZFo3amNMZzk3Sk1PTlNDYWx4MWo5cWJwbFgzYjFmS05mNGZtM2pJVTJzdXVNRThfbzR0c1Jh?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, 투자자 전문위원회 확대 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBzeU9rNU1EdHUxZlZPOGFLOFljdWxrLXE5bDlVS0xod0kxUXl1dm5TNXRFTzVVYVlpNUtfaFpzdERFNkxYdmIxTm5vdFZTUm5GWnJvQVM5SDBfaDhid29DXzk2YWJLRllWeEE?oc=5 |  |
| kifrs | 조세일보 | 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 | http://www.joseilbo.com/news/news_read.php?uid=580131&class=10&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | 한국세정신문 | "재무제표 정정 또는 고의·중과실로 손실 내면 이미 지급한 성과보수 환수" - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5yN0FYRC1aQ3dWWHFDanRvN3pudVRibXBrYk42bDVpZ3hrZnkwMGlGYkZFWXpGZlQzNGpYQTZYeXJnSnZ1ZkRsdHZaMEpkS0ZMRUg3Y1F6ZnRlSGtDQ284MmVMTTE?oc=5 |  |
| kifrs | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QQkdfaGlxSmJXLWJ6ZWxsbmxpZVhYZHJHRWl4V0VIalhpZEJEYXJIUy1CSFQ1MzF3TEM5Y1JWdkxvVmkzZDNQSUpyVTNFSExWS2t6Q01Qem9VTkM1TzVheWpUS3Y?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | CPA뉴스 | '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBIQTJ0X1JOSU9ma2J1MTBkVG5aVVo5bmtPUF9PVy0tT3R4NFN1NE5CcndSOE9EQjgtVUNydXJXak9UcFpTZTFydUxzdnhnY1pqdy10U21mdVVSbVNNT0I2NEVocnhURmw4?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑥] 두 개의 영업이익 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5FRUxaZW9oYmNpYTBhR3h5d0VOQ0NtQmxKU0NHTTFsc3ltYkhTQURmNmV6TGMwNnBtOE85QjFvT1l5Sk9zRHpUX1lwZUYycTVsY1NYRW9seGpuN0QxaDZqdVZLeGczMk1i?oc=5 |  |
| kifrs | CPA뉴스 | [재무제표 수다떨기] 기업 인수 뒤의 숨은 이야기, 외부평가 의견서와 M&A 공시 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFA4UVFYV2FvWGtPaTZjbVIxQjBESjVJenlJallEaERzQXhUczVGMm1KVmdYb1BwMzRlXzE0dXlhUXA5eS1ya0VwNVFRSnVWM08ybWJlalFfLUUzOUI0OTdVNUlaelFMTEFL?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑧] 현금흐름표도 함께 바뀐다 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5OWVd5Z0VCYWFKcFRxZ2MydDVicTBORGU5YzhnTFpXQ1NLRFJ0ZHNLVzRKd3N2SEZuQlJqTFZWb1ZidWN2MGJfQmM5ZzdWZmVvVXBTcGNlNFRhT2ZTT2pqYnZ6bEc3aXJv?oc=5 |  |
| kifrs | 조세일보 | [진단] 제각각 회계기준, '회계기본법'으로 통일되나 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iZExnWDViSmtJa1VsVmpUS3MtTHpYcDNDQU1iWkFWMlBkYi1QMjljcW9za0MwUjE5Vmg4V2dkdDg5blhYZjFrNkhDRmRkbnZ2bjVla0pOR2xMenlvUEc4?oc=5 |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | 머니투데이 | "삼성전자 700조 저평가, 손절 말고 버티세요"…재무제표 뜯어보니[부꾸미] - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9pRkMzckl3eFF6Q3dvZEpsMUF3SnBMY0VuM08wR25IdFlIUVJJNV9jOUFSckVGbUdWck52QmZ2cER6SWZZblozbkhhNkNFc1ExTDFxOVlJYzY5ZEQ0X2Rpcmltenhta2t00gFuQVVfeXFMUFpSSDdnYlpoZWNObVJTdkVCYUVsSS1NXy1GZDUzUl9iV1BmRTJqOUFuejBWUkw0a01yeEo0SlYzT0pWaWVlcThWRWF4dVlRNlFrUHdUUkZjeVlaeFpxVDNUanpHTDdmbHZWMzJwUkE?oc=5 |  |
| kifrs | 매일경제 | “글로벌 투자자들, 재무제표급 ESG공시 원해” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5wb2Z4TVdNX0NsQndNU08tQldGZ2JGOFhpTmVTM2x2b0FtY2xYOEVPWGFRaFdhTWw3Rk1jQWNnRHJ3WldSa3RyV1RldHRhLXZsaVE?oc=5 |  |
| kifrs | 매일경제 | ‘회계처리기준 위반’ 해태제과식품, 거래 재개 첫날 급락…11%대 ‘뚝’ - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE51S0dscjIzU0MxMnhMZXB0elJqR3lfNnFHTzh5QzA2UzNhbUtVX0hhVnVHTzNIU01QZzV4YVZodnJSLW1vZmktQmcxOGRkWWhPeUE?oc=5 |  |
| kifrs | 서울경제 | 금융위, ‘매출 허위 계상’ 피델릭스에 과징금 부과 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5CYnJPTW05UFhwTWVISnpoMkl3dURJQTlKdWVXOTAzQkd5Z1NEYUE3WnVXdG9lOUxuNDB2SVZpLXMteWozcFRJc3JUX0UzWEF2TWfSAVNBVV95cUxQcDZyTURiU0lNQUtxalJ2S0FPSkJ1cDJQUTJJOUtPanNoT203TzFfR0VjNEE4dC10ckdibG5uSVJTZ1R3aXZwckVGN2trWXJKa2d2cw?oc=5 |  |
| kifrs | 머니투데이 | "이런 회사는 거들떠보지도 마세요"…회계사가 경고한 재무제표 신호 \| 이대훈 회계사 - 머니투데이 | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5JTkZueGtnejVfQkg5QkxUclVDUm8wVkRrVW9wamxneXp6R0lxdE9iRkpGell6N1dnTnhhTF91UlVlZ1EzQ3pIZl94MGZSbUhDcTVF?oc=5 |  |
| kifrs | 파이낸셜뉴스 | IFRS18부터 PRS까지… 재무제표 바꿀 변수 쏟아진다 - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1qMmQyTGZyUUpzOFBMOVF0Z1I4WHNUcUFZLUo5ODRlMkdOMGNqZ2pvSXJGODl1eUFYT1lDanRka29kdkRuWEJPNGRYdWNxWHBXZlA1ZGFqMGJJZw?oc=5 |  |
| kifrs | 서울경제 | [단독] 금감원, 제이알글로벌리츠 회계감리 착수…자산평가 논란 재점화하나 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9ncUJvZWtlNmZ2VnZHNUhpZnFoN2RrcTUwR2RBQUV0QkVpejJ5ZW5tQUVjMWRBalQ0Snp6Slpob28zeDNBazdIQ19XQmVEcDZUcFHSAVNBVV95cUxOcGpaa1J0eGxlaXl5TXB3aS1hMFlqVllzM3F5ZkhKem1JbE1WX2JyU3ZZRi10UUFnV3hzTXJmLWVWajVJODB5WlBxYThTS3BCSDlLOA?oc=5 |  |
| kifrs | joseplus.com | 회계기준원, 회계기준위원회 상임위원에 김재호 회계기준실장 선임 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE02WFRCZnBNZXhhQVJLT2hKd0U2Slk3T1djSGZNdmY3bHRkM2lhU0xYVDdiVE8zdkp0WWxiSmFrdWhNbDJ3SVNTLUl0SEd4Unh0b2JJVlF2a2TSAVNBVV95cUxOVWdYS09ETTh0STZDbnJmb05fcjVUUWg2ZTZEelpHOXcxaU5DNWdGNDNFLWNROG52MWcwYXRMUTJtdmZTckhJMm5NbUhhaWdqbTBPZw?oc=5 |  |
| kifrs | joseplus.com | 회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 세미나 개최 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBOTGZHQncyWkZkNWphSDRhUGV1S3ZSNDYxWmxtRVpVUkV4SzVxaGV0eWZ1allzUnJ1REVBTXBsY1BLcGpoVU9JblZRWjZQcy1MSFh4Ym5RWEnSAVNBVV95cUxORWdjXzk0bGwzdHhMMzJMQjNCWm5Rb0xxTWctc2lOaFZmQ215Tl9iZS1ZTGlwckpUTjBmUnVmQ2h1V0ZEdHQtUHJrOUhBZEtCUnJ5QQ?oc=5 |  |
| kifrs | tfmedia.co.kr | 제9대 회계기준위 상임위원에 김재호 회계기준실장 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTFBWdFhiU0RQekZiVE9zb1VzYWNYODdpZzVSbmE0U2pkNlc4aHlGS21FUVdpang4bHJ0TXo3d1J1ZU5BNWRqVm1xZXpETlhLLU5GYmNJV3FwaFoxbkJrTXFyZlRYTQ?oc=5 |  |
| kifrs | biz.chosun.com | [단독] 10대 그룹 CFO 내달 회동…국제회계기준 발언권 확대 논의 - Chosunbiz | https://news.google.com/rss/articles/CBMihAFBVV95cUxPbm9pdFYyUTV6YUU2ZkpEdVFVNmwyOXcyeF9TV3dMazRZdTRsMEJvYVNrSlJpSG5oODZkb2lJQ0tsRGNjbktXXzZkdlJTalNiYWJBVDhrUmktM3FUT2k0eWJ4SHJBdHNCdDVnNmUtUklSWnVsOU01X1NLcjVqQmhiRHFZNk7SAZgBQVVfeXFMTlVZMGMxWGMwdXg3SktMZ0JMSmZacFR1Z0g2WlFBZXZscVBvck9qYmdDa01qMFlJUEVCNjhaX1VIMkVKdkV0OERYYkRpWTdkQU96SDEzX0NXbFppN0hUMG9waHlEbHdwd05YQXM5UUZXV3J3cno2TzZpNjBhcG9zaUwtQ21zU05rWWdYVExsZFJlOERuQzNSSzI?oc=5 |  |
| kifrs | youthdaily.co.kr | 항공기 팔아 당기순익 늘린 제주항공…부채비율 하락은 "대출 회계처리" - 청년일보 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5KMmdhVzV1UzlzSXo4SU5UNGFlQmNOTHF0RUFtTFc2NFFJMVlqZGZkZkFWaTU4M1hVWC1kdUhMTFJlY1lSeU1NN1loM0JLYlhsVGIxblhMVWVGREdXNXNlQ3hSbl9oY1U?oc=5 |  |
| kifrs | newspim.com | CJ프레시웨이, 공정위 정면 반박...쟁점은 회계 처리 아닌 납품 연계성 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9LYUQ3QjdPWE1FM0RIYUttT01IZ3B6end4b3R0dmZBRnFJTmZ6TWdaNlFqUmhLTnhRZEl1clZwVm1tZTFGeTBlNmJMYzdsZFNSekVuWGpqZXQwSmct?oc=5 |  |
| kifrs | datatooza.com | 허브 그룹, 신용계약 4차 수정안 체결…미제출 재무제표 제출 기한 내년 1월 31일로 연장 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5lb3lIXzAtZ1kyRFJpczNlYnNRamZGTEQzS2t2LTR6ZzZRRjdoNjVQamV6WjhrZGprTGRXZi1aelRGQ2FBaDRvai1oY21DdU9fSEZKNU1kT3pOaTllajRxWjlQeWlGRnk1c1FvOWxCdHpvbWc?oc=5 |  |
| kifrs | datatooza.com | 블레이즈 홀딩스, 2025년 및 2026년 재무제표 재작성 결정…중국 매출 재검토 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9hM3FVTG5YU2h2YnVoQ2VPZk5CVlFpdGtfOGdGQnAxMkNyekZya19Ick1KbUI2UFJBWnNwTjhwcGs1Z28ybXlSTFRJR0R0LWhkdmdzUm1HdG9xUVVva19rTTFabnpMTmJkVlh4M2hXX3FCUVk?oc=5 |  |
| kifrs | ibtomato.com | 값 오른 땅만 재평가?…회계기준이 막는 이유 - IB토마토 | https://news.google.com/rss/articles/CBMiakFVX3lxTE01cElLMmVjNU5YUW5EeXNGcWVkTGhuQl8xY1BxbzJSeC1NWVIyZmdMTndjazlVMzRvLWQ1SlRqdTNwOTZBdmFNcW1vaGx6R184XzRQeVA4Zi1wUDljdFFYdzJnOWFMQUxoZnc?oc=5 |  |
| kifrs | asiae.co.kr | 금융위, '회계처리위반' 피델릭스·현대회계법인에 과징금 등 부과 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFA3YXU3VWg1akMyeWwxVkFRZmtBbE5iUDQ0NmNvNTFmWmsxbFpYb2tYTXd5NkdvbHZRZ2FaRS1Zc2ZEYW5hbENjTFBqMldBYV9rQUZ2clM4OTN2VG5iMkdZYQ?oc=5 |  |
| kifrs | opinionnews.co.kr | 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 | https://news.google.com/rss/articles/CBMickFVX3lxTE9WeVlZRG8wdjhmVjFaMHYwQjNRcS1HbGhGc0RfQWF3eWJhb2FreXd2WjBtNDF6Q3pBZHdsT2Rlb1VQVWdkczF2ZDJXMkQyMzJSR0FtR1lXTkI4cmtlM090V2RMQWVBcndYX0YwcHhBb1hzQQ?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1118호 영향 관련 사전 주석공시 모범사례 마련 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE13d18yem9ReWp0R1hMQXhJaVctcGpyTzgxRm9XSXBNOXZxcnNZaDhfZVgzajBhR0gwNm9EQnBmZElrWWhsQ01mbE05dzc5NmVWbksxVVE5STk?oc=5 |  |
| kifrs | bloter.net | 스마일게이트 'IPO 소송' 2심 돌입…CB 회계처리 공방 - 블로터 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE8wR2FkT0VGYmlIWVgxQW1tYW5xQTBFd0ZXMFRsekU5Q0lPRDdLcjF0bVBDd1pITTBxNmllQUtjRmlqVEcyV005d3BKNzl1cDZiVHFSd0U4YmpPazkwNXoxRzQ0Y2F6a3gx0gFsQVVfeXFMTWtiQnFpS1ZBOHVuSWV5amI3VWRFaWdTbUZ4eU1lMWFNVXhFblI1c2U2TkFOV2dWcE5rS0VIQllrc2N1SFRPWjl2eDdOa2hvamhUeWtaVG1vTGw2b2phUWowZndzMXNTNmVBOVFU?oc=5 |  |
| kifrs | fairn.co.kr | 피델릭스, 5년간 150억원 허위 매출…외부자금 조달 위해 화장빨 회계 조작 - 공정뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5UMW9OeHpJMlFfS1lja1pwQUljbTdNSzRnLVVVYWZOeE9pR0RUUkxSV3NYUzRXUWNMb3FqUHJ3bmtadnZ4ZTJqX1AwLUFwMHhZLVA5S243ZnhTNHFtcFo1N0toMmRYbWNy?oc=5 |  |
| kifrs | joseplus.com | 회계기준원, KSSB 공시기준 파일럿 테스트…전문가 TF 논의 착수 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE1RaUpIeDFhcmlxZnNlRzdmaGpSQlVFSmNZVW5SZEE1a3JEQVEtQzc0MGJBWlg4dVRiSF80ZmREakM4NGVqbTJYcFhQNURTVV9DZ0J5T3JBd2TSAVNBVV95cUxQVXlNZWU5R19CVWs4MUZ3S3lnTEhGRGxmTlZCcXcwM1I2RkpwMWhDN2x0TkNkTlhyaGdKZ0FoZmU1T1BxRElhZ1N3M09ZaTJqTDAzYw?oc=5 |  |
| kifrs | edata.ekn.kr | [기후경영 포럼] 윤나영 한국회계기준원 팀장 “온실가스 배출량 측정, 조직경계·산정기준부터 따져야” - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE9ZZ1ZfbmRGdGQ3aVVyQ2xjN3FLdlVieXNqNW85MXdCeEd6M0ZLT2ZDTUU3RnVid2xTQ2NXUVR4RDNsVGRWQUJUN3BSb0FhN3A3U0ZKbjNYd29fX19vVFE?oc=5 |  |
| kifrs | koreancenter.or.kr | 올해 두나무 흑자·빗썸 적자…"배경엔 회계기준 차이" - 연합뉴스 한민족센터 | https://news.google.com/rss/articles/CBMidEFVX3lxTE83blp1VndyUEJCa05jNlVoSUdtRU1OYlFKaUt1WmppdDZyRGlyTi1qakJncnloR3NFWGE1ek9tTm00Y3NxOHlHWEZJQUk5WG1XNzR6eHJlaXJWQjd1VVBScHh5YmpLU1NNVGlpYUhmdnlPdmRz?oc=5 |  |
| kifrs | donga.com | 차액가맹금 줄소송과 재무제표의 침묵[기고/김진욱] - 동아일보 | https://news.google.com/rss/articles/CBMidkFVX3lxTE5zUFg0OWxBNDZzdm95b19JdmhudVVOdk9zREVXam9sMkJ2NzB2bjlyTUhLUm91anJMYWZuaVFGamUwMGY0Zmk2VHBLNmcybmIzamx5eGhvRkZ0TDdTOUt6ZWVCV3NmSG9SMXlOVmNuZU8zNnVNalHSAWZBVV95cUxNazdhTXZ5aksxR3ctbTVwUklUX19CR2JMN0pyYzNXOENFSDgyN1hnZk9pR2lrZFRmZ1FKWUY2UzBobU1BdEFmRmVaYS01OElLT2RQcld6amR1UzNnVDNQR242UG5yZWc?oc=5 |  |
| kifrs | safetimes.co.kr | 금감원 20년 걸리는 상장사 회계감리 주기 '단축' - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBha2RUM2lwVUQ5SnFaQTFFXzdRR3o4YmpPUDlmVVI4SmE1X1g5bHY3RFBFLVFtaUloX2hZak9BWlFmVEdaYXFpNlByLVl6cWNkRm1qQW1FYzJaNGw1Tm5nUUVQNmp0TXQxSWttQ0MtVdIBc0FVX3lxTFBQbDRmNi1JeE9xeGoxSEtpZEN6b1lHUTV2QXlLUldNSDQxYmh2Njc0eXZzb1IzNWZwNzVUdjdpZXFZS3Q1NndQYi1aOVl3d0pFQkhEX1ptQTkyNmpFS1I1VllGTGZaZUdNTHZpSHNPVDRkdjQ?oc=5 |  |
| kifrs | lawtimes.co.kr | 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE05MDRqekxIcGRMRFZhMmdwVnM0OWZ3R2lMRGhka0NDWU1EblRBMFplYXc2bldHUDJvMnJtaG0tSnFaX2U3ckt1WXY1U2FxNk1zVm1yb0lUb09Mb2o5elV4S3ZNWVRfSUJPdmxvRHhR0gFyQVVfeXFMUFhvWmtXbVVXc2lzOTFnYnp6bGFkWnc3T2kzcC03bFVzam5Sb25NNWZsSmt6Q29WVmUyZ0EtYVY4SC1IVlB5QmtXTVIxR005WDVzdDYwcDhramd6dXRGOGh5eHdZRnVrTTBoYV9FNzBFbnVn?oc=5 |  |
| kifrs | news.bizwatch.co.kr | 회계감리 중징계 영풍…내부통제 시스템 허점 논란 - 비즈워치 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5aNFQ0V2JXaVMtOVBoRVNNV2RZNE1GYS1mcE1Gd0J2NDA2YnhGaUV3cFJmZldxRDh3eUdNdkxvRktUNEFkQ1NkMVFCaVpBZG9TenNBYVR0Y09KUkZnS0poeUxQNjhEaXhKVVVSVg?oc=5 |  |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBJYkpxaXBTcjhUQkZPcHVfay1mQnptQXRhMklhUVNBQ3VSZy1WYWpzeVp4eGdkMmF2bHhDclR6ZHMtMnNJQlNWYVFmb2tsWWxYYndaTEFrcVVHZUnSAWBBVV95cUxPelVLaldNY3hnelFDQzFqaVY0UDBDX3EwY2xkU0QzS3JBc0JBUm5STlFaVlhxRnlpN0FmbXNSQjdEd28zTXFCQWctb2JYN3JLWGZQcUZFdEM3MzJtOFhTTlk?oc=5 |  |
| kifrs | joongang.co.kr | 기준 바꾸니 27조 흑자가 적자로…새 회계기준에 지주사 ‘비상’ - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE4ybk5IZk1jY3dMRTE3a21sWnlBZ0RYcVpPYnduMW56UzJhek1fellTTEdkMmJSelc1LVBIME55clJXYko5Z0lnbkpEakVFbmVkdmdzbHB3?oc=5 |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1waW5qQW1YOXhwYmFLQk1JR2VfajhXSWptWWd4SUxEYXF2bFI4cE5WTlFUX3VnVWRmdVBpcXE4YlhMUndRUXMwLTFqRGdEMjl5aHJkTjJpbzhEZXc?oc=5 |  |
| kifrs | hellot.net | [이슈 포커스] 기업 반발에 탄소회계 기준 후퇴 논란…과학계·투자자는 “그린워싱 우려” - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFB4bmx2T2E5RnZBMmpMTGh2aVBrcHhsQWNoRHJlMy1SdjYyLUIxUU1JZ2cwSUtFYlFweUdSaHMyOE5yanVkSGVuOXhOeU1QVDVocXQ2bkhjcFR3cjVIRWQ4?oc=5 |  |
| kifrs | yna.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VYm1UdW9mM2l1SG84VFJPSnBhSHNGa1dpUzJobWpjNnJ1aXliX2RGMkhNR3FPM09rYjQtREI1d0hBTHU3V2V5aGcwRzJfUEpvaFdvc1V3WENNeVHSAWBBVV95cUxQT2JUYXQzVE5hTGZwR0dROTBxLU93YWYyUDdjMkVxbjBtaEFMYzltaWNJRzRKLVh1OG1ZLWx1ZEJTOWktcHZFRmNOR1lfZzdjZG5wdnB5YzM0M3dra0hXaDU?oc=5 |  |
| kifrs | news.bizwatch.co.kr | [SFS 2.0]재무제표 밖 거래망까지 읽는다…AI가 넓힌 신용평가 - 비즈워치 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBBOFR0QWktVXlHMWpfSjFlTVEzTk1kTm9QQzhjN2VTYWpOVFcwVnlMUnNxNXZ5MzRqOWJBNnY0aWlPY2JWZ2NGNWdkV3hlMXpRdmxjQmtucVc3aHVDRVgxMHlVNGJhRGtQVldr?oc=5 |  |
| kifrs | yna.co.kr | 감사 전 재무제표 제출 위반 76건…전년보다 24건↑ - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lODhfd3R3TUpXOFZneW5tMjJ0OEVEeXBMWExHS1F1MzNOdExVUlNsdTFwYVpFZTRxLXNTZzZoZzRmQnhhYW5ZZlhtUjJJM1M4YXA0ZWNCbU5ubzjSAWBBVV95cUxNUWMwYlBCMlpvS2R1a2dOaVdCYkRqcE04YXNwb0JCSC0xb3NSc05OM194Z2dCcVhiSFU1elMzQklVZHNCc2dtRG1wMk5kSTJmMW1rVWZWdDFQcjZrZFVRTno?oc=5 |  |
| kifrs | yna.co.kr | 증선위, '회계기준 위반' 금양에 감사인지정·과징금 조치(종합2보) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE84VG44Qzl6Wm1UcmV6LUVNNWFhXzNSdXlDLXE0bmhrLXBLSWpCQldRYy1uTkxMY1V1WWVmRFdLcmxnZUZGdHRXU3hVTzY1akhNbGFGUXVhM0Z5dWvSAWBBVV95cUxQT0RISWQycmFQX2pXQXZtN3g2Wk9xYm12OURoVXduNk1zUmNmUllsRGV0cG14bFJxU1c4bGFIQy1QNGZzZjJMQ180b1BoSHBJT2d6NGliMUJvS1N4dnRpRHc?oc=5 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| esg | 임팩트온 | KSSB “EU, ISSB 공시 인정하고 필요한 정보만 추가해야”…해외 공시매체 인터뷰서 밝혀 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1QTEJtQU9nQkpqX1BCR24zM1RuQlNhNGJqQXlTUmpCNWJtNVh0VkM0TS1TbFJmYW5GbHpGNWVzbTdSMUVJSElhOFk2LURqX1B2OWNhby1aTHRqWE5oS0FwazFqNWxRb1pVSGc?oc=5 |  |
| esg | 한국경제 | ESG 공시 표류와 RE100 위기…한국 경제 골든타임은 지금[기고] | https://magazine.hankyung.com/business/article/202611172333b |  |
| esg | kpenews.com | [ESG전략] 사회공헌 프로젝트 인정 한화호텔·최신 ESG 공시 기준 적용 ... | https://kpenews.com/View.aspx?No=4328948 |  |
| esg | news2day.co.kr | [2026 대한민국 지속가능경영 소통대상] 한국환경산업기술원, 녹색금융... | https://www.news2day.co.kr/article/20261126500379 |  |
| esg | hansbiz.co.kr | ESG 공시 입법 지연…2028년 거래소 의무공시 대안 부상 | http://www.hansbiz.co.kr/news/articleView.html?idxno=887652 |  |
| esg | news2day.co.kr | [2026 대한민국 지속가능경영 소통대상] LG생활건강, 국회 산자중기위원... | https://www.news2day.co.kr/article/20261126500142 |  |
| esg | energydaily.co.kr | [초점] 환경정보 공개가 '기업 경쟁력'…ESG 공시·EU 공급망 규제 대응... | https://www.energydaily.co.kr/news/articleView.html?idxno=205428 |  |
| esg | sentv.co.kr | 금호타이어, 지속가능성 평가 4년 연속 1위…ESG 공시 역량도 인정 | https://www.sentv.co.kr/article/view/sentv202611250120 |  |
| esg | biztribune.co.kr | 교보증권, ESG 성과 잇따라… 지속가능경영 체계 고도화 | http://www.biztribune.co.kr/news/articleView.html?idxno=363157 |  |
| esg | kdfnews.com | KB증권, ESG 공시체계 개선 성과…지속가능성보고서상 2년 연속 | http://www.kdfnews.com/news/articleView.html?idxno=191429 |  |
| esg | newsprime.co.kr | 'ESG 경영 내실 다진' 정몽진號 KCC, 지속가능경영 성과 가시화 | http://www.newsprime.co.kr/news/article.html?no=756393 |  |
| tax | 한국세정신문 | 조세심판원 "재산세 납부 의무자가 반드시 종부세 납세의무자는 아냐" | https://www.taxtimes.co.kr/news/article.html?no=277875 |  |
| tax | 한국세정신문 | 111일 만에 전입신고…실거주 확인 땐 취득세 감면 | https://www.taxtimes.co.kr/news/article.html?no=277876 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(67) 대도시 내 부동산 취득세 중과, '형식' 아닌... | https://www.intn.co.kr/news/articleView.html?idxno=3000354 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(64) 토지의 무상사용과 재산세 비과세의 실질 | http://www.intn.co.kr/news/articleView.html?idxno=2054488 |  |
| tax | 한국경제 | 데이터센터 경쟁력 막는 세액공제 제도 | https://www.hankyung.com/article/2026112631761 |  |
| tax | 서울경제 | 승용차 개소세 보전 예산 ‘0원’…국내 생산 세액공제도 공회전 | https://www.sedaily.com/article/20119059?ref=naver |  |
| tax | 서울경제 | 與, SK ‘트리니티팹’ 지원 기업 법인세 감면 추진 | https://www.sedaily.com/article/20118946?ref=naver |  |
| tax | 매일경제 | 법인세 늘고 과징금까지 … 금융지주 비상 | https://www.mk.co.kr/article/12211463 |  |
| tax | sejungilbo.com | 이건태, 도시철도건설용역 부가세 영세율 2030년까지 4년 연장 추진 | https://www.sejungilbo.com/news/articleView.html?idxno=61246 |  |
| tax | news.tvchosun.com | 내년부턴 '종부세 폭탄'…세액 공제 혜택 확 줄어 | https://news.tvchosun.com/site/data/html_dir/2026/11/26/2026112690264.html |  |
| tax | koscaj.com | "하도급받은 공사액보다 더 큰 세금계산서는 가공거래" | https://www.koscaj.com/news/articleView.html?idxno=327682 |  |
| tax | newstomato.com | 대법, 해외 세액공제 기준 제시…"영토 아닌 과세권" | http://www.newstomato.com/ReadNews.aspx?no=1321769&inflow=N |  |
| tax | sejungilbo.com | 김석기, 게임물도 세액공제 대상 포함 추진…비수도권 제작 시 공제율 ... | https://www.sejungilbo.com/news/articleView.html?idxno=61213 |  |
| tax | sejungilbo.com | 사무장에게 상호 빌려주고 세금계산서 발급한 회계법인…심판원 "가산세... | https://www.sejungilbo.com/news/articleView.html?idxno=61223 |  |
| tax | fieldnews.kr | [단독] 국세청 조사대로 법인세 낸 인천공항공사, 4년치 환급 거부 뒤집... | http://www.fieldnews.kr/news/articleView.html?idxno=33316 |  |
| tax | updownnews.co.kr | 기아, 현대카드 포인트 부담분 부가세 환급 불발…"결정 존중·소송 취하... | https://www.updownnews.co.kr/news/articleView.html?idxno=319665 |  |
| tax | sejungilbo.com | [판세] 과세기간이 다른 여러 국가의 소득, 외국납부세액공제 계산방식... | https://www.sejungilbo.com/news/articleView.html?idxno=60678 |  |
| tax | dnews.co.kr | 도시철도 영세율 연장 입법 ‘잰걸음’…JTX·수도권서남부선 세 부담 ... | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202611181437550170654 |  |
| tax | koit.co.kr | 정보보호 투자·인력 채용에 세액공제 추진 | https://www.koit.co.kr/news/articleView.html?idxno=209966 |  |
| tax | sejungilbo.com | [판세] 사업 관련성 없는 지출의 매입세액공제 여부와 부가세법상 '수입... | https://www.sejungilbo.com/news/articleView.html?idxno=60677 |  |
| tax | sejungilbo.com | [절세톡톡] 일시적2주택 취득세, 용도변경도 종전주택처분일까요? | https://www.sejungilbo.com/news/articleView.html?idxno=61088 |  |
| tax | fieldnews.kr | [단독] 하나투어, 항공권 부가세 환급 놓고 국세청과 공방…조세심판원... | http://www.fieldnews.kr/news/articleView.html?idxno=32758 |  |
| tax | the-today.com | 미국 보수 세액공제 막힌 구본성…쟁점은 근무지... 왜? | https://www.the-today.com/news/articleView.html?idxno=93441 |  |
| tax | incheonilbo.com | 여야, 앞다퉈 입법…소방·지방세입 확충 구체화 | https://www.incheonilbo.com/news/articleView.html?idxno=1336375 |  |
| tax | sejungilbo.com | [절세톡톡] 매매계약에 따라 상가로 용도변경후 양도한 경우 부가가치세... | https://www.sejungilbo.com/news/articleView.html?idxno=59962 |  |
| tax | fieldnews.kr | [단독] LH, 서울시에 옛 서울의료원 부지 무상 제공했는데 재산세…심판... | http://www.fieldnews.kr/news/articleView.html?idxno=32880 |  |
| icfr | 파이낸셜뉴스 | 한국금융인재개발원, '회계실무자윤리인증'으로 내부통제 뒷받침 | https://www.fnnews.com/news/202611251554056091 |  |
| icfr | insjournal.co.kr | GA 검사 대응, 정도영업이 답이다...③"서류만 갖춰선 부족", 상시 내부통제로 '취약점'부터 잡아야 - 보험저널 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1wNE1tMXlPTk1hQXNhbzcxdm1CbkFKbHBnNzk3VGRKc3FwX1c0cU1seVVWNmlKMVA0Uzl2dGR0cllJSHZpa2w4a3hpT0Z0TzhKby0yUm9OaUtieC03aGlnU2M1WXp1NmdVdGJzNnNfTQ?oc=5 |  |
| icfr | datatooza.com | 인터내셔널 페이퍼, 내부통제 '중대한 취약점' 공개…미 법무부 골판지 가격 조사 소환장도 받아 - datatooza.com | https://news.google.com/rss/articles/CBMic0FVX3lxTFBfdzBCVmNOaUNUdG1xVEtINDhURGVWYUhoZGttNk14c3V3dXNmS3FYZTlyUWZyUFo3Nmp5UXNsdUJlTFJTTEhBdVgzLTZYaS1uY042ekNBV3U5T1NkX0N2dERPYlV6Wkt0UWZ0SGYzZkJucG8?oc=5 |  |
| icfr | datatooza.com | 리소시스 커넥션, 내부통제 중대한 취약점 미해소… 1분기 구조조정 비용 41만 7000달러 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE4xYy1JWnFhRGhwbDJwMzRiVkgxUjdfMlYyWl9yMzVQd1NMS3kwanZRR2p2LU9oU0Fob19kbzN0M2NSaE9iSUhBX2hWb1JGTFUyUF81LXp6S0lHa0hLaThtaWhnSTl5MlZVYXJQR255RUVYa1k?oc=5 |  |
| icfr | datatooza.com | 웨어 푸드 컴스 프롬, 내부통제 취약점 발견으로 연간보고서 정정 제출 - datatooza.com | https://news.google.com/rss/articles/CBMic0FVX3lxTE1iSno5am5SSzE3aGxRY2xxU0Zlc3hlQjktMjVxREliQThsYVlRUWw0NVNtaXJkNWIwRlg3WWFpaC1fNzFTXzVsR1F4WEVEQkctMll1LUJEZi0wR3dudDQzeGdWUjUyRjc5T1VuRVpsZFJwNXc?oc=5 |  |
| icfr | news1.kr | 최운열 한공회장, 세계에 신외감법 성과 알려…"韓 회계투명성 껑충" - 뉴스1 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE9ITUEzOUMwcWJBVFF4cWRyT2NmZ2xKeHh1V2o0RVhVVmF6T3RkYUxzMGlCRFVtZ0pqNkdMV1hpUTdRaWpCOXVIc0lQY0Q2NUZCcHRoR3pCdnZNTkVyZFpR?oc=5 |  |
| icfr | lawtalk.co.kr | 회사 재무제표를 부풀렸는데 외감법 위반으로 처벌되나요 - 로톡 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SNHVGNVhqcF9pRjBSSFEtUzNPWWtJQldRYVAyY1hXZW1xaFB3ZWdKd1JHcXhXQ2YwQWU4cVBnWXNPcHZwYlhmU3NMWk9fd2M?oc=5 |  |

## excluded:nonprofit (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | CPA뉴스 | 한국공인회계사회, 『공익법인회계기준 실무사례와 해설』 발간 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFB1T0FfdnRKR0ExSkF3WmpfeE04WFlIc0Y2bFNSOGRxS3g1Um1uUjJycWgwUHk4a3hsd01DZnM1SzI1NGlmd3dQQk5TT3ktQklMWFg4aEd5OEZZbzdIVExsdUdsWTFfaFVl?oc=5 |  |

## excluded:other_industry_tax (17건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | ajunews.com | 中 전기차 공세 거센데…세액공제 이견에 정부 대책 연기 | https://www.ajunews.com/view/20261127092823622 |  |
| tax | metroseoul.co.kr | 전기차 국내생산세액공제, 국회서 '갈팡질팡'…중국 추격에도 지원 제외... | http://www.metroseoul.co.kr/article/20261125500360 |  |
| tax | smedaily.co.kr | 전기차 세액공제 국회서 이틀째 제동…정부 대책 27일로 연기 | http://www.smedaily.co.kr/news/articleView.html?idxno=366581 |  |
| tax | view.asiae.co.kr | [세제돋보기] 전기차 생산세액공제 포함 주목…정부 대책 앞두고 국회 ... | https://view.asiae.co.kr/article/2026112411245023254 |  |
| tax | theopiniontimes.news | 중국산 전기차 점유율 4년 새 1%→34%…국산 전기차 세액공제, 국회 첫 ... | https://theopiniontimes.news/%ec%a4%91%ea%b5%ad%ec%82%b0-%ec%a0%84%ea%b8%b0%ec%b0%a8-%ec%a0%90%ec%9c%a0%ec%9c%a8-4%eb%85%84-%ec%83%88-1%e2%86%9234%ea%b5%ad%ec%82%b0-%ec%a0%84%ea%b8%b0%ec%b0%a8-%ec%84%b8%ec%95%a1%ea%b3%b5/ |  |
| tax | news1.kr | 전기차 생산세액공제 도입 공감대…'공제액·수출차·통상 마찰' 변수 | https://www.news1.kr/industry/auto-industry/6362100 |  |
| tax | news.bizwatch.co.kr | 국산 전기차 세액공제 확대 가닥에도…정부 막판까지 고심 이유 | https://news.bizwatch.co.kr/article/industry/2026/11/20/0030 |  |
| tax | newspim.com | 중국산 전기차 침투 속도 韓 3위…"국내생산세액공제 필요성 커" | https://www.newspim.com/news/view/20261122000099 |  |
| tax | news.dealsitetv.com | 中 전기차에 안방 내줘…세액공제 시급 | https://news.dealsitetv.com/articles/178820 |  |
| tax | econovill.com | 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 | https://www.econovill.com/news/articleView.html?idxno=757588 |  |
| tax | etoday.co.kr | 전기차 국내생산세액공제 발표 또 연기…중국산 배터리·할인율 막판 변... | https://www.etoday.co.kr/news/view/2653989 |  |
| tax | biz.heraldcorp.com | 전기차 세액공제 또 미뤄졌다 | https://biz.heraldcorp.com/article/10951683?ref=naver |  |
| tax | newsis.com | 국산 전기차 세액공제 막판 검토…"배터리·소재 생산지까지 따져야 실... | https://www.newsis.com/view/NISX20261126_0003885091 |  |
| tax | chosun.com | [기고] 흔들리는 전기차 제조 기반, 국내 생산 세액공제 서둘러야 | https://www.chosun.com/opinion/contribution/2026/11/26/FYFX77N3URAEZHY62Q6SHRXLPM/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news |  |
| tax | khan.co.kr | ‘국내 전기차 세액공제’ 논의 난항 | https://www.khan.co.kr/article/202611262048005 |  |
| tax | khan.co.kr | 전기차 세액공제 논의 난항···정부, 경쟁력 강화방안 발표 연기 | https://www.khan.co.kr/article/202611261747001 |  |
| tax | 서울경제 | 전기차 생산세액공제 국회 논의 지연…지원대책 발표 또 연기 | https://www.sedaily.com/article/20119476?ref=naver |  |

## excluded:related_news_attached (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE9nRjdudGFRU2U4Ung3OGVXVWFnQ0xuLWFpZjhQVWxVbV9iZWwtNURvem1KX3EzbWttUnRRYVpXZC1sZW5iLXNWdGdwSGZZbjVwODUyRFpiQnZZbkQzRjFDcHNGUQ?oc=5 | → 관련 보도로 붙음: 2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요 |

## excluded:similar_news_merged (44건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, 투자자 전문위원회 확대 | https://www.intn.co.kr/news/articleView.html?idxno=3000418 | → 대표: 한국회계기준원, 투자자 전문위원회 확대 - Daily NTN |
| kifrs | 한국경제 | 회계기준원, 투자자 전문위원회 12인으로 확대…위원장에 이현승 LHS운용... | https://www.hankyung.com/article/202611200435r | → 대표: 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 |
| kifrs | joseplus.com | 회계기준원, 투자자 전문위원회 12인으로 3인 확대. - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBIaHFndzBsVnRHVzdQV1VGLU5QRjdIQWhfYVFmdkdmeHN5eDVISTNPcTcwZ0kwRnM4MkhVU2U3c0pJQUp4T3hTdVFSVlhfa2hvcW9XR3BiZkzSAVNBVV95cUxPUUwzT3BBMUs4SXl3UGVheW11Rmlad25HcEpRMnpBZFU2aE8tZEtkdUhWMlF3Umt0Rm1ySXpJVHFzWjhHc3gtWHdTeGtfS1Q3M25POA?oc=5 | → 대표: 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | 일간NTN | ‘재무제표 정정·고의·중과실 손실 발생 시 이미 지급한 임원 성과급 환수’ - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5yYUg1NHFSanRPdE0zcFNJZEhTWk11VFNtSldJdFZNOG5LT0tLaFhZZE5WT1JmSWNtV0dSaEsySmZhbmZuMWo2UWt3cVlCNlVvZG1QeklNUmpxc01kX2VmQi02bTZBRWE0RUE?oc=5 | → 대표: "재무제표 정정 또는 고의·중과실로 손실 내면 이미 지급한 성과보수 환수" - 한국세정신문 |
| kifrs | greened.kr | 새출발기금, 회계처리 오류로 과거 손실 600억 늘어…재무제표 다시 작성 - 녹색경제신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5VWExRb21kWUZMSWk4d0NUUVpqQ3UzQXdtOHZzY3QybEJ1Vk9NbDhVQ2RaWVlISUY2bE9tQkg4clltVEVfLWFvcm9PMDNicHdvdV9FNzIybVZoN3JtdXlTemRHZmxzc1Z1?oc=5 | → 대표: "재무제표 정정 또는 고의·중과실로 손실 내면 이미 지급한 성과보수 환수" - 한국세정신문 |
| kifrs | 한국경제 | 화우, 장석일 전 금감원 전문심의위원 영입…회계·감리 대응 강화 [로앤비즈 브리핑] - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCVW1xY0w0Z3V6ZmNNdl95dVl0cXpURnV6SnlaVkpmMGdoM3VFbEk0VGZjN0NsMTBTdGxTYlRKNl9aZHg5Rmd4d0JQNkRtam51RTJabFE3dUc4Zw?oc=5 | → 대표: 화우, 장석일 전 금융감독원 전문심의위원 영입 - 한국세정신문 |
| kifrs | asiae.co.kr | 화우, 장석일 전 금감원 전문심의위원 영입…회계감리 대응 강화 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBCaTFDSTlieXVXR254ODlNQnZXWUZyeFYySkE1dVRBNEY4blNJbjFDRzJjalREMjAteGhtSnhOaEZYcW56N0EtMFV0ejRDdExYbE1GNnA1TE9scW5WMzhqdQ?oc=5 | → 대표: 화우, 장석일 전 금융감독원 전문심의위원 영입 - 한국세정신문 |
| kifrs | view.asiae.co.kr | 화우, 장석일 전 금감원 전문심의위원 영입…회계감리 대응 강화 | https://view.asiae.co.kr/article/2026112613375378875 | → 대표: 화우, 장석일 전 금융감독원 전문심의위원 영입 - 한국세정신문 |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= | → 대표: 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... |
| kifrs | 일간NTN | 증선위, 셀바스헬스케어·대우산업개발 회계기준 위반 적발 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9tQmxSTkNsdGZjelBnMlcyWUpmYWszeEtOdThRZmlyeXl5cUJERjd3WEx2WGpIRWxSZEl1bXNLYTV0R0c4VnRtR0xIN2sxZTh0QzY5bVdkd2RaQnFZTzRNdmZ2RHNwZmx1WXc?oc=5 | → 대표: '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - CPA뉴스 |
| kifrs | dailymedi.com | 셀바스헬스케어, 회계기준 위반…외부감사인 2년 - 데일리메디 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE4xaVlFekdIcGhMSndrR09HejgtSUlJY2ZodnRYRFpUTjhZRi11Q0JSbVBnUTA4RHhFNF9BQThOQVh4b0R4VE5qUVliV3hFVmItRUJadHZnLXZfX1N1b01Xd0hfdjF3QWpI?oc=5 | → 대표: '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - CPA뉴스 |
| kifrs | yna.co.kr | '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBlWi1sVUpRM1UyVkI4d0pnT1VOb2JFQ3V4NlE3SnExYU9DelBONXhGcHMtdUNSaklsTGs2d3Fhb3k5VmIxSlNZVFpjbUJYclJGRlhmcVREcHFlMFnSAWBBVV95cUxNNW9pWS1jTjF5WWIxYXFySEh2NlFuaFVfdVE0S2RBVWhFU0gya0RGRE55dlR3WnNXUTJCQThVMlF0UzJtR2Q0QUJPd2o5c2FHQzUwLTFsdFBMMnJuOV85QkI?oc=5 | → 대표: '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - CPA뉴스 |
| kifrs | newspim.com | 증선위, 셀바스헬스케어·대우산업개발 회계처리 위반 제재 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE5xVHFZUm5oMzU2dGxzZ1ltTnpaS0pOQl90cm9vRGh1Q0NGTzFRVVhpSVlhWkZMaGlxZ1NENzVSRkZ2Ykt5WEtzYUdmZVZ4TkFCS0Y3OHlXOG9EZWsy?oc=5 | → 대표: '회계처리 위반' 셀바스헬스케어·대우산업개발에 감사인지정 - CPA뉴스 |
| kifrs | 이데일리 | 금융위, '허위 매출' 피델릭스에 과징금 2억8690만 부과 결정 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxNeDhFT1BzNjY2NEFYS3NGZVhGbDNHbUFrRnIycThMTFp3V1J4cHhCdGJfbnJhclgzcnVuMnl1SVdqWHhNMjg5ekNSMkYtd243RWlTa0tBXzRuTVNNNDgzbXFtWG9ubi1RUDBQdlJzbW5hRXQyVEFGY19rWVJYZmRHUA?oc=5 | → 대표: 금융위, ‘매출 허위 계상’ 피델릭스에 과징금 부과 - 서울경제 |
| kifrs | 한국경제 | 유한종 삼성전자 재경팀 부사장, 국제회계기준委 GPF위원 선임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5SYy05eHZBcVRBaTcxbXlRNG5USFFUMjJ0ajNuZktXbF9NZEJlRWFVcC1WbXF1WjJNTXFvR2VtVDRWVk9DeG01R2oxaUV4V2ZBRnVHbElSVEhtZw?oc=5 | → 대표: 유한종 삼성전자 부사장, GPF 위원 선임…국제회계기준 제·개정 자문 - 뉴시스 |
| kifrs | 이데일리 | 내년 K-IFRS 제1118호 의무 적용…금감원 "기업들, 도입 준비 철저히 해야" - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5ld2NBM0dGUjlxX25jVjFiQmV3cVdPQ0FLYzFUQU8yX2lqUEItQ0JJZ0hEdVBVai1rNmlrZXc5b2stUHhoYWdkdDZpQTAyTWdBM3ZnQUNYX3ZMMjI0cXNKUjBRcjN0UjJXYWNkYkdvSzNOT2c?oc=5 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 매일경제 마켓 |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 매일경제 마켓 |
| kifrs | insnews.co.kr | 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5PTnlLYzlLQklteE1MaW50MjZwRV9RQkRtZDAyal9rdVpCc1pvNXk0M2tCS2hLOVpFa18tVDFmd0VQTDh6bmVBZGR3dkdIU1VFR0ZrWWFrOFpRRkZ1a0Z1eUxsNG9UOG5ncjZF0gFvQVVfeXFMT3dydTBxd2xRSzI3ekVzdF9GVEdtakV1TURuT0VTOEFSbkloTURQV0UzX0F2NWk2MVFqYVBFaDdZN0M2V2xTOGhwR3N1RTB6QnNWUlhNLU9RNkVEbUpmZk12cXlUb3NXUmJJc2dWcFFn?oc=5 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 매일경제 마켓 |
| kifrs | dhdaily.co.kr | 내년 K-IFRS 제1118호 도입 앞두고 기업 혼선 - 대한데일리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE0wM3RhZzFMWlZuajAxa0kzU29yekNKVU9yZVNKeXR0Z2p2STZlRDgwQkFOVDBndGg1Y2FFSExwRHdRcWpIeVNxUnJsSV8wenJNWktTVTk4MWlOTEU4ZWl0S194ejhHYjlhalBz?oc=5 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 매일경제 마켓 |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 매일경제 마켓 |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성 공시기준에 투자자 수요 반영…전문 위원회 확... | https://www.tfmedia.co.kr/news/article.html?no=209073 | → 대표: 회계기준원, 지속가능성 공시기준에 투자자 수요 반영…전문 위원회 확대‧강화 - 조세금융신문 |
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 대표: 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 - 조세금융신문 |
| kifrs | biz.sbs.co.kr | 엔비디아 회계장부 들여다보는 美 SEC…매출 공시·회계 처리 조사 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5iWm9mNWpzT2hVYmR1MkVOc0tVWHBpVm5Ebllyclh6RnlzUmZHM2hDY0lSWkpDV0h4amNJUFBOdG1GWDFBNXJ2RVdsWUlVNkhWRExZ0gFYQVVfeXFMUFFiUGh0azUxYUVFeHZzS1dqT0c1bE40TEdJYkV0OENjdjFqMjF6N2pseVlxOWRyYjVfdVhselFsQzJYeThBVFRyVzF3SjdRbUdHWHZ0WGhCLQ?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | es.tradingview.com | 소식통에 따르면, 엔비디아의 회계 처리 방식이 미국 증권거래위원회(SEC)의 조사 대상이라고 한다 - TradingView | https://news.google.com/rss/articles/CBMid0FVX3lxTFBqbDhCYmRhTEJNVHNybEdwVl96RnctWmgtWTBTazRtRV9GTEVpUUdKWU9MaEFXMkc1Yy02dmRZWS1TbWpUUnB5MTVwbG4zNzlLZ09qc2c5V0cyNlRQTUpydnBoSG1YaHh1dkM0S2plaS0yb3A0dXUw?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 | → 대표: 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 |
| kifrs | news.bizwatch.co.kr | 상장사 회계감리 20년에 한 번꼴...이찬진 금감원장 "획기적으로 줄일 것" - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE05dWV0Ul9JcGNYOFN2b1drODJqNzNLNnRfMGNXYngzODk3d0I0eS10dTJJWHZ1VEZzZDRqRDRVOXFOM3M4RGFaRnlURGV0c3NwZDFsMnIxZUQ4U0RKMVVTZ2tlUjBBbHZPeFE?oc=5 | → 대표: 금감원 20년 걸리는 상장사 회계감리 주기 '단축' - 세이프타임즈 |
| kifrs | dnews.co.kr | 이찬진 금감원장 "상장사 회계감리 주기, 20년→ 美3년·英5년 수준으로 단축" - 대한경제 | https://news.google.com/rss/articles/CBMidEFVX3lxTE1fbUk5RzFyejJNVjBxbGxhVHB3Z01UczUzTFZ1YlUxZXlwVEc3VzVaVHNuQ2FfT1BwaVRRNVVOV2hGeGF0ZWwydDNXWVNtRk5SeEFWc3hZd29QY1VxTHdZQno2cXpQZDRZZmtZVVZvSFIybWdf?oc=5 | → 대표: 금감원 20년 걸리는 상장사 회계감리 주기 '단축' - 세이프타임즈 |
| kifrs | joongang.co.kr | 법무법인 지평, ‘AI회계감리대응센터’ 확대 개편 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE9vMHpYaEZibllYVUpNMThST2MxRi1ZelNUd3BBWG5qbVM4M2lSNEttSDRzRG5Vd3NrWGxyTFp0VHpBajV3Qll6ZmJIU3dtT2x3OGlpdU5n?oc=5 | → 대표: 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 |
| kifrs | tfmedia.co.kr | 금융위, '회계처리 위반' 해태제과에 9억 과징금·감사인지정 3년 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE1nVW9jUjhaYTVIc1p6ZjFubzYwSEFsUDl4Zkw3dkpKN2hoeHJoUHFBVDFVa3kwZm5XSEpwM0lXcUd3ZjRiZkhVcThYYlNRa0dfOFZCdUFENUpLVGFWclp2UTNvcw?oc=5 | → 대표: 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - 연합뉴스 |
| kifrs | news.einfomax.co.kr | 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBzREN4d0RmcDJBMXFhZ3BfZVVTRXJOalhqNmNYYVRoUFNzQmJoNHdqb3pmaXVqX3RGTlpMbGVYUGh1dGNHbEpBbXBmQkE3cEI0dVFMS05DaHdjUkswWTk3Vy1qam5vYXhpckdud2xoX1k?oc=5 | → 대표: 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - 연합뉴스 |
| esg | m-i.kr | ESG 공시 의무화·탄소 규제 대응…대·중소기업 공급망 상생 해법 모색 | https://www.m-i.kr/news/articleView.html?idxno=2023645 | → 대표: 정일택 금호타이어 사장 "ESG 공시 의무화 선제 대응…데이터 관리 고도화" - 파이낸셜뉴스 |
| esg | edata.ekn.kr | ESG 공시 의무화 코앞으로…기업별 데이터 관리 ‘제각각’ - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE4tMXlWRVBfMUpGeEtzWDZ3RjNjV2VRd2lyRThnVzRtcFlFNW92blhGZFNMSXN1Mk1icDZLVzlQWmIyblBJNDVCa0dkalVlMFQzblo5UF9NelBIZ0VwcEE?oc=5 | → 대표: 정일택 금호타이어 사장 "ESG 공시 의무화 선제 대응…데이터 관리 고도화" - 파이낸셜뉴스 |
| tax | 매일경제 | "전입신고 늦어도 실거주땐 취득세 감면" | https://www.mk.co.kr/article/12214810 | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | news1.kr | 조세심판원 "첫 집 전입신고 111일 만에 마쳤어도 취득세 감면 인정" | https://www.news1.kr/politics/president/6360765 | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | biz.sbs.co.kr | 조세심판원 "전입신고 늦어도 실거주 땐 취득세 감면 유효" | https://biz.sbs.co.kr/article_hub/20000347776?division=NAVER | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | yonhapnewstv.co.kr | 조세심판원 "전입신고 늦어도 실거주 땐 취득세 감면" | http://www.yonhapnewstv.co.kr/news/AKR20261120103447oGO | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | yna.co.kr | 조세심판원 "전입신고 지연돼도 실거주 확인시 취득세 감면" | https://www.yna.co.kr/view/AKR20261119156700001?input=1195m | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | taxwatch.co.kr | 111일 만에 전입신고…취득세 감면 인정된 이유 | https://www.taxwatch.co.kr/article/tax/2026/11/19/0002/naver | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | dnews.co.kr | 대법 “괌ㆍ사이판 세액공제 한도, 美본토와 따로 계산” | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202611251240008580561 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | widedaily.com | 대법원 "미국 본토와 미국령은 세법상 '다른 국가'…법인세 공제한도 따... | https://www.widedaily.com/news/articleView.html?idxno=304702 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | lawissue.co.kr | 대법원, 괌과 북마리아나제도 '미국'에 포함되지 않는 별개 국가 법인세... | https://www.lawissue.co.kr/view.php?ud=2026112419194157929a8c8bf58f_12 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | newsis.com | 대법 "美본토-미국령은 세법상 '다른 국가'…법인세 공제 따로" | https://www.newsis.com/view/NISX20261124_0003880987 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | news1.kr | 대법 "괌·사이판은 美와 별개 '국가'…외국납부세액 공제한도 따로 계... | https://www.news1.kr/society/court-prosecution/6363869 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |

## excluded:smb_only (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | gnmaeil.com | 부가세 간이과세 2억원으로 상향 추진 | http://www.gnmaeil.com/news/articleView.html?idxno=598793 |  |
| tax | yangsanilbo.com | 윤영석, 부가세 간이과세 기준 2억원 상향 추진 | http://www.yangsanilbo.com/news/articleView.html?idxno=128709 |  |
| tax | imaeil.com | 부동산 중개수수료 요율표는 상한…부가세 10%, 간이과세 중개업소는 4... | https://www.imaeil.com/page/view/2026101018554473359 |  |

## excluded:standard_setter_governance (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국회계기준원 | 2026년 제9회 지속가능성기준위원회(IFRS 재단 정관 개정 공개초안에 대한 검토의견) | https://www.kasb.or.kr/front/board/calViewA.do?seq=1133 |  |

## collect:event_announcement (40건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융감독원 | 금융에 이야기와 상상을 더하다 제21회 금융공모전 시상식 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250034&menuNo=200218 |  |
|  | 금융감독원 | 불법사금융 근절 및 피해예방, 지원 협력체계 구축을 위한 금융감독원-부산광역시-부산경찰청간 업무협약 체결 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249960&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원은 제8기 옴부즈만을 신규로 위촉하였습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249917&menuNo=200218 |  |
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
| kifrs | 머니투데이 | 상장협, 코스피 회계담당자 워크숍…K-IFRS 1118호 대비 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMidkFVX3lxTE5EMTFVcXVPbmhsR1FqZEpIZ0ZWUFJTR0VvSUR5a2RHbTliQWJpbGtQaWM5YVNXMWs1bHdCRmx3NjlaaDROZm12OHZFVlpiOTE1WTd0U0N4d2haTkNqOEc5SHNXeGhrOWJVaUtPWjlob0tCR05XVkHSAXtBVV95cUxOb2RqUmhYQVRsM21pdEhHcHhpcDdFRF82Q3h4ZFROM0oyZ1k1T2thbGVCbUFqSjBYZGRNS0hLbE1vUkxzQVg5OUE4dDBMdXJUaVlRMUFtZmxmdzJkczRTZ05XcFdtZGNNaEFiZm44aTFQR3IwQXRyQ2pPR0U?oc=5 |  |
| kifrs | yna.co.kr | [게시판] 상장협, 코스피 기업 회계담당자 워크숍 개최 - 연합뉴스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1Xak11SldzRkYyOXJWNncxNXBJbjZfal9KRllETml0NnphZ1lsQ2h5WEtVNFBEaWlXdUhKcEZBUFQwMzkzMDNqa3h5QzRzQUxmcUR2QS01cjZ2NVFrZDgyeNIBYEFVX3lxTE1Xak11SldzRkYyOXJWNncxNXBJbjZfal9KRllETml0NnphZ1lsQ2h5WEtVNFBEaWlXdUhKcEZBUFQwMzkzMDNqa3h5QzRzQUxmcUR2QS01cjZ2NVFrZDgyeA?oc=5 |  |
| kifrs | 파이낸셜뉴스 | "새 회계기준 안착하도록 제도적 뒷받침 필요" [제18회 국제회계포럼] - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ST0FLRjNmYjNJRHRqZ2R3QS1WeWVKbVNnTHB0OXR1ODY4R1RuOElXZ1oxYW44NmN2b0daS3IyOTd4UFF5N091T3NzX1dEcmtSMTVOVFNqY0l3QQ?oc=5 |  |
| kifrs | dailian.co.kr | "회계현안 실무대응 모색"…상장협, 상장사 회계담당자 워크숍 - 데일리안 | https://news.google.com/rss/articles/CBMiogJBVV95cUxNYmtUQ1ZzRWU3Z2NERS0yNUE0N3lpZXBtcVlDS29DQWROV3pWU29jMHZjcUNiaFZiV2p6RzR2a1JJbDR1Zk9SYnlqTjhtUFRydjhubE55aGZ2eXJGRzUtbXc1TmFlRlFNS1JWLXBhbWRJOHJqNFR5VmRQSnlmdjdCa19LQ1J3Z1JCWnRnbDJ4bDRRWTVhLVdqWC1jbmhJdFExWFBXS2VQRS1haHFZd0w0WTk3U09rLXZNczh6NzVGdVlrMkZYRmpwYmtOU0swbFM0MGdXNkZSQkgtUjlnMTVpbWpOa2VfQlFWNXNoTmh3NF9OTjJEOU00dllHdWVLZWNPc0xWYWlFQ2VfWUxzdTlPZTktR2J1b0tIVk1Ta1FZTGIyZw?oc=5 |  |
| esg | viva100.com | KB증권, 지속가능성보고서상 2년 연속 수상…ESG 공시 역량 인정 - 브릿지경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBIS1U5YTZWMkJPMGRheUhwbURGd3N1bFI3dG9Bb2ZkX3gxLWlOTlhuRTEtaTZGay1QWG16WGl0V1VEdlZFM3pGM1ltTEdEcVJuem5ZRDBxOHFjQQ?oc=5 |  |
| esg | news1.kr | "ESG 공시 정교화"…KCC, 지속가능성보고서 12년 연속 수상 - 뉴스1 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1hcjlQcXhLWjFRZmhhajFIMTFHaG5tUW9rRzNNdDVyUjdYMTNCRTNjdExIVl8zeGp0bjZQcUo4S2N1clJvc0dNU0gzWTFCRUQ1MHdlRXV4bktiWUFk?oc=5 |  |
| esg | smartbizn.com | 한샘, ESG 공시 기준 선제 반영···지속가능성보고서상 2년 연속 수상 - 스마트비즈 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBuc09XVE42Z3AxdFRsaktRNWNxZkRuZ29YSnhLblpmdFVqVlBJdUY2U3VsOHE4YWI5bC1yVEV3T0swYURoU0N3X3I0MXIxSmIwNG9YVFB2ekoxWk5OZ3g4RXVnUHNmZEQtdWNBTg?oc=5 |  |
| esg | sateconomy.co.kr | KB증권, 지속가능성보고서상 2년 연속 수상…투자자 중심 ESG 공시 강화 | https://sateconomy.co.kr/news/view/1065573636733530 |  |
| esg | smartbizn.com | 한샘, ESG 공시 기준 선제 반영···지속가능성보고서상 2년 연속 수상 | https://www.smartbizn.com/news/articleView.html?idxno=160624 |  |
| esg | thefirstmedia.net | 한샘, 지속가능성보고서상 2년 연속 수상…글로벌 ESG 공시 기준 반영 | http://www.thefirstmedia.net/news/articleView.html?idxno=214622 |  |
| esg | ziksir.com | KB증권, ESG 공시 경쟁력 인정…지속가능성보고서상 2년 연속 수상 | https://www.ziksir.com/news/articleView.html?idxno=154641 |  |
| esg | newsis.com | KB증권, '지속가능성보고서상' 2년 연속 수상…"ESG 공시 우수성 입증" | https://www.newsis.com/view/NISX20261125_0003882475 |  |
| esg | newslock.co.kr | 한샘, 지속가능성보고서상 2년 연속 수상…ESG 공시 기준 반영 | http://www.newslock.co.kr/news/articleView.html?idxno=140912 |  |
| esg | viva100.com | KB증권, 지속가능성보고서상 2년 연속 수상…ESG 공시 역량 인정 | https://www.viva100.com/article/20261125500542 |  |
| esg | ilyoseoul.co.kr | KB증권, '지속가능성보고서상' 금융부문 수상… KSSB 반영해 ESG 공시 체... | https://www.ilyoseoul.co.kr/news/articleView.html?idxno=525532 |  |
| esg | news1.kr | 한샘, ESG 공시 투명성 인정…KRCA 2년 연속 수상 | https://www.news1.kr/industry/general-industry/6365297 |  |
| esg | joongangenews.com | KB증권, KSSB 기준 반영한 ESG 보고서로 2년 연속 수상 | https://www.joongangenews.com/news/articleView.html?idxno=566386 |  |
| esg | kpenews.com | KB증권, ESG 공시 신뢰성 높인다..지속가능성보고서상 2년 연속 수상 | https://kpenews.com/View.aspx?No=4328140 |  |
| esg | thepublic.kr | KCC, 지속가능성보고서상 12년 연속 수상…ESG 공시 체계 강화 | https://www.thepublic.kr/news/articleView.html?idxno=328481 |  |
| esg | news1.kr | "ESG 공시 정교화"…KCC, 지속가능성보고서 12년 연속 수상 | https://www.news1.kr/industry/sb-founded/6366089 |  |
| esg | thefirstmedia.net | KCC, 지속가능성보고서상 12년 연속 수상…ESG 공시 체계 고도화 | http://www.thefirstmedia.net/news/articleView.html?idxno=214593 |  |
| esg | the-pr.co.kr | KCC, 지속가능경영 12년 내공…보고서상 연속 수상 | https://www.the-pr.co.kr/news/articleView.html?idxno=63488 |  |
| esg | bizwnews.com | KCC, '12년 연속 우수보고서상' 수상…"지속가능경영 경쟁력 입증" | http://www.bizwnews.com/news/articleView.html?idxno=153071 |  |
| esg | megaeconomy.co.kr | 우성, ESG 공시 역량 인정…지속가능성보고서상 수상·평가등급 두 단계... | https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065578156983631 |  |

## collect:incident (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | nbnbiz.co.kr | 삼성·SK하이닉스 LTA, 재무제표 '물음표'…구속력 논란 - nbn 시사경제 | https://news.google.com/rss/articles/CBMiakFVX3lxTE0yOGVRb3FjX2VDRWhialZLWFJjU0txZWpmUVFsSFpIOW9XM3d1b2JQRU1tSWI1Q2tMU00zNFd1RVlMTVFlUU55V2ltX3cyNTJmRXJ1WjBNNzIwbVdLbEZ2WHJQUk5GN05ialE?oc=5 |  |
| kifrs | news.einfomax.co.kr | 금융당국, '상폐 위기' 금양 검찰 고발…회계기준 위반 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTE4tV2cwN0F0UnBSSEg1N2FxSnlKY2JBSk5URk1SelBmemVXOHRwdllqZXFObW1RV002dUczNjI2UHMxMFdZcl9fNFNtSk5QM090ck5MNnBRdjJTcVJyUXFXU2c5eWUtSllrdTZwbmdQNjU?oc=5 |  |
| kifrs | kyeonggi.com | 낙동강 주민들, 영풍 회계처리 의혹 검찰 조사…"강제수사 나서야" - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5UY1hjRFAyc3RPaDhqSjZZQUhzdHE0SWphNXppN0xFby0wMDQwQ2FpN3pPblBPSzlqeVhVWFpjc3NySEtDRjJaVnlpTE5XOTlRVUpybEg0M3lLSjg?oc=5 |  |

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

## collect:no_category (287건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융감독원 | 2026년도 금융회사 지역재투자 평가결과 발표 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250066&menuNo=200218 |  |
|  | 금융감독원 | 금융시장 동향 및 증시안정조치 진행상황 점검 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250058&menuNo=200218 |  |
|  | 금융감독원 | 금융회사 검사, 제재, 인허가 전반의 공공성과 투명성을 제고합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250056&menuNo=200218 |  |
|  | 금융감독원 | 2026년 1~3분기 국내은행 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250053&menuNo=200218 |  |
|  | 금융감독원 | 26.9월말 보험회사 대출채권 현황 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250054&menuNo=200218 |  |
|  | 금융감독원 | 다음 미션만 성공하면 수익금이 2배 나만 아는 '꿀알바'가 아닌 '팀미션사기' 입니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250035&menuNo=200218 |  |
|  | 금융감독원 | 26년 부적격 유사투자자문업자 직권말소 처리 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250033&menuNo=200218 |  |
|  | 금융감독원 | 이용은 편리하게, 보호는 두텁게 선불전자지급수단을 개선하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250032&menuNo=200218 |  |
|  | 금융감독원 | 보험 판매수수료의 과도한 경쟁을 억제하여 소비자의 보험료 부담을 낮추겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250030&menuNo=200218 |  |
|  | 금융감독원 | 포용금융 활성화를 위한 기획형 샌드박스 사업자 모집 개시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250029&menuNo=200218 |  |
|  | 금융감독원 | 건전성 규제 금융 공급 연체채권 관리체계를 종합적으로 정비해 일회성이 아닌 지속가능한 포용금융을 실현하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250028&menuNo=200218 |  |
|  | 금융감독원 | 26.9말 국내은행 부실채권 현황(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250026&menuNo=200218 |  |
|  | 금융감독원 | 언론사 기자 등의 부정거래행위 등 불공정거래 행위에 대한 조치 의결(2건) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250022&menuNo=200218 |  |
|  | 금융감독원 | AI 금융사기 대응역량 강화를 위한 2026 세계투자자주간 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250018&menuNo=200218 |  |
|  | 금융감독원 | 금융시장 위기 대비체계를 한층 더 강화하였습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250017&menuNo=200218 |  |
|  | 금융감독원 | 금융회사가 기업의 저탄소 전환에 필요한 자금을 지원할 수 있도록 실무기준을 마련하였습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250016&menuNo=200218 |  |
|  | 금융감독원 | 환매중단펀드를 보유한 퇴직연금 계좌도 실물이전이 가능해집니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250013&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 모험자본 활성화 추진 성과 및 향후 계획 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250012&menuNo=200218 |  |
|  | 금융감독원 | 2026년 1~9월 보험회사 경영실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=250011&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 건전한 시장질서 확립 및 투자자 보호를 위한 증권사 랩어카운트 담당 임원 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249967&menuNo=200218 |  |
|  | 금융감독원 | 「디지털자산업의 혁신과 이용자 보호에 관한 법률」 제정안 입법 추진 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249968&menuNo=200218 |  |
|  | 금융감독원 | 불법공매도 합동점검TF 운영 개시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249965&menuNo=200218 |  |
|  | 금융감독원 | 보험업법 시행령, 금융기관검사및제재에관한규정 개정안 입법예고(’26.11.25.~’27.1.4.) 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249964&menuNo=200218 |  |
|  | 금융감독원 | 부산 해양금융 경쟁력 강화를 위한 2026 부산 해양금융위크 및 해양금융컨벤션 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249959&menuNo=200218 |  |
|  | 금융감독원 | 개정 특금법에 따른 기존 가상자산사업자 신고접수 결과 및 향후 심사절차 안내 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249958&menuNo=200218 |  |
|  | 금융감독원 | 사업보고서 등에 대한 조사,감리결과 조치 - 제20차 금융위원회('26.11.23.) 조치 의결 - | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249953&menuNo=200218 |  |
|  | 금융감독원 | 주요국 증시 변동성 확대에 따른 단계별 시장안정조치 시행 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249949&menuNo=200218 |  |
|  | 금융감독원 | 불법 사채 무력화 속도전, 무효 확인에 AI 투입 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249944&menuNo=200218 |  |
|  | 금융감독원 | 카카오페이,토스,네이버페이에서도 '주민등록증 진위확인' 가능... 전자금융거래 안전성 강화 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249945&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 가상자산사업자 대상 침해사고 대응 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249933&menuNo=200218 |  |
|  | 금융감독원 | 2026년 10월 외국인 증권투자 동향 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249931&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 퇴직연금 사업자 임원 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249922&menuNo=200218 |  |
|  | 금융감독원 | 깜빡 잊고 지나가버린 지난 3년간 실손보험금, ‘실손24’를 통해 한방에 청구하고 받을 수 있습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249919&menuNo=200218 |  |
|  | 금융감독원 | 저축성보험, 만기 후에도 최대 3년까지 연금으로 전환할 수 있습니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=249916&menuNo=200218 |  |
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
|  | 재정경제부 | 시장상황점검회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080084&menuNo=4010100 |  |
|  | 재정경제부 | 「한중일 및 아세안+3 재무차관 및 중앙은행  부총재 회의」 참석 및 주요인사 면담 결과 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080066&menuNo=4010100 |  |
|  | 재정경제부 | 개인투자용 국채 12월 발행 미실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080049&menuNo=4010100 |  |
|  | 재정경제부 | 26.12월 국고채, 재정증권, 원화표시 외평채 발행 계획 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080077&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] 2026년 종합부동산세 고지 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080076&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] 2026년 3/4분기 가계동향조사 결과 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080050&menuNo=4010100 |  |
|  | 재정경제부 | AI시대, 전략산업의 미래를 위한 정책과제 제안 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080058&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「월급방위대 TF」 2차 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080055&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 임금체계 개편 우수기업 방문 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080064&menuNo=4010100 |  |
|  | 재정경제부 | 2026 다자개발은행(MDB) 프로젝트 플라자 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080029&menuNo=4010100 |  |
|  | 금융위원회 | 2026년도 금융회사 지역재투자 평가결과 발표. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88261?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융시장 동향 및  증시안정조치 진행상황 점검. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88256?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융회사 검사‧제재‧인허가 전반의  공공성과 투명성을 제고합니다. - 「금융행정 쇄신방안」 마련. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88250?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 이억원 금융위원장, 메리츠지주 김용범 부회장과 만나 민간 자본시장 개혁기구 구성 및 운영방안 논의 | https://www.fsc.go.kr/no010101/88245?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | “다음 미션만 성공하면 수익금이 2배?” ☞ 나만 아는 ‘꿀알바’가 아닌 ‘팀미션사기‘ 입니다. | https://www.fsc.go.kr/no010101/88240?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 이용은 편리하게, 보호는 두텁게선불전자지급수단을 개선하겠습니다 | https://www.fsc.go.kr/no010101/88238?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | AI 친화적인 금융공공데이터를 추가로 개방합니다 | https://www.fsc.go.kr/no010101/88237?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 보험 판매수수료의 과도한 경쟁을 억제하여 소비자의 보험료 부담을 낮추겠습니다. | https://www.fsc.go.kr/no010101/88236?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 포용금융 활성화를 위한  기획형 샌드박스 사업자 모집 개시 | https://www.fsc.go.kr/no010101/88235?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 건전성 규제, 금융 공급, 연체채권 관리체계를 종합적으로 정비해 일회성이 아닌,  지속가능한 포용금융을 실현하겠습니다. | https://www.fsc.go.kr/no010101/88232?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 「상호금융업 감독규정」 일부개정고시(안) 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4192 |  |
|  | 금융위원회 | ｢금융기관검사및제재에관한규정 일부개정고시안｣ 규정변경예고 | https://www.fsc.go.kr/po040301/view?noticeId=4191 |  |
|  | 금융위원회 | 「보험업법 시행령」 일부개정령안 입법예고 | https://www.fsc.go.kr/po040301/view?noticeId=4190 |  |
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
|  | 정책브리핑(금융위원회) | 금융회사 검사·제재·인허가 전반의  공공성과 투명성을 제고합니다. - 「금융행정 쇄신방안」 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791126&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(금융위원회) | 금융시장 동향 및  증시안정조치 진행상황 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791173&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국세청) | 2026년 종합부동산세, 12월 15일까지 납부하세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791055&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |

## collect:noise_keyword (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | biz.chosun.com | 생맥주 가격 안 오를 수도…국회, 주세법 재검토 요청 | https://biz.chosun.com/policy/politics/assembly/2026/11/25/GOKIPKGU6VG7NJH2GDIW3F5D3M/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |

## collect:non_kifrs (31건)

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
| kifrs | 금융감독원 | 매출 및 매출원가 허위계상 (FSS/2505-01) — 관련 기준서: 일반기업회계기준 제2장, 제16장 | https://www.fss.or.kr/fss/bbs/B0000135/view.do?nttId=194369&menuNo=200448 |  |
| kifrs | 금융감독원 | 무형자산(개발비) 과대계상 (FSS/2409-11) — 관련 기준서: 일반기업회계기준 제11장 | https://www.fss.or.kr/fss/bbs/B0000135/view.do?nttId=138392&menuNo=200448 |  |
| kifrs | 금융감독원 | 재고자산 허위계상 및 감사인의 독립성 의무 위반 (FSS/2409-07) — 관련 기준서: 일반기업회계기준 제7장 | https://www.fss.or.kr/fss/bbs/B0000135/view.do?nttId=138383&menuNo=200448 |  |
| kifrs | 금융감독원 | 공사수익 및 공사미수금 과대계상 (FSS/2405-03) — 관련 기준서: 일반기업회계기준 제16장, 제5장 | https://www.fss.or.kr/fss/bbs/B0000135/view.do?nttId=135710&menuNo=200448 |  |
| kifrs | 금융감독원 | 매출 및 매출원가 허위계상 (FSS/2405-02) — 관련 기준서: 일반기업회계기준 제16장 | https://www.fss.or.kr/fss/bbs/B0000135/view.do?nttId=135709&menuNo=200448 |  |

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

## collect:out_of_scope (209건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 한국회계기준원 | [공지사항] '26년 12월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] K-IFRS 제1118호 정착지원 TF 논의 내용(6차) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] 홈페이지 게시_본인 인증 서비스 일시 점검 안내(2026. 11. 14.(토) 22:00 ~ 2026. 11. 15.(일) 04:00 ) | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI 실무 세미나 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] IASB 정보요청서, IFRS 9 '금융상품', IFRS 7 '금융상품: 공시' 위험회피회계 사후이행검토(PIR) 국내 의견조회 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] ISSB 자연 관련 공시 실무서 공개초안 요약자료(Snapshot) 국문본, ISSB 아웃리치 세션 및 국내 의견수렴 일정 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] '26년 11월 KARI Accounting and Sustainability Research Seminar 안내 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] [외부행사 안내] EFRAG, 비EU 기업 대상 ESRS-40a 공개초안 글로벌 아웃리치 세미나 개최 | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [공지사항] (영상공개) IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/comm010List.do |  |
|  | 한국회계기준원 | [세미나] IASB 위원(Nick Anderson) 초청 투자자 세미나: K-IFRS 제1118호 ‘재무제표 표시와 공시’ | https://www.kasb.or.kr/front/board/calViewA.do?seq=1129 |  |
|  | 한국회계기준원 | [세미나] 회계기준원-환경산업기술원, 지속가능성 공시기준 이행지원 세미나 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1127 |  |
|  | 한국회계기준원 | [세미나] 한국회계기준원 개원 27주년 세미나: 지속가능성 공시, 새로운 기준의 시대 | https://www.kasb.or.kr/front/board/calViewA.do?seq=1125 |  |
|  | 정책브리핑(보건복지부) | 정부, 국가필수의약품 안정공급 강화 위해 민·관 협력 체계 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791214&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [부처합동] 정부, 국가필수의약품 안정공급 강화 위해 민·관 협력 체계구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791213&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 신속하고 정확한 국민안전 긴급구조를 위한 민관협의체 구성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791209&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공정거래위원회-한국공정거래조정원-한국규제학회 공동 학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791207&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공정위·조정원, 상생협력 모범사례 및 하도급대금 연동 우수사례 발표회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791206&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 국방과학연구소, 대한민국 내부통제경영대상에서 '대상' 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791212&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 제8회 국방사업관리사  국가자격검정 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791211&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국군사관학교창설추진단 신설 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791208&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립신시도자연휴양림, 전북대학교와 함께 해안 정화활동 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791205&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 국가자격시험 부정행위 방지대책, 시험 전·중·후 단계별로 빈틈없이 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791202&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 시장상황점검회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791203&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(병무청) | 병무청, 한국생명존중희망재단과 협력으로 청년 병역의무자 정신건강 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791201&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 함께 쓰는 연구 장비, 함께 여는 연구개발 미래 공동활용 우수성과 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791196&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청-지방정부, 산림분야 NDC 실행력 강화에 뜻 모아 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791199&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(병무청) | 병역처분은 공정하게, 부정한 병멱면탈은 끝까지 확인합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791194&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 무균의약품 GMP 이행지원 가이드라인 2종 제정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791193&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 소나무재선충병 현장 중심의 방제 실행력 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791191&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한반도 물길에서 찾는 평화·상생의 해법 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791192&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부, 국군사관학교 창설 관련  육·해·공군 사관생도 설문조사 결과 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791187&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K-바이오 혁신을 이끄는 산업인 한 자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791189&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부 장관, 베트남 중앙정책전략위원장 만나 첨단산업·원전·공급망 등  전략적 경제 협력 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791188&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 유출 긴급대응 및 점검지원 체계 가동 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791185&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 딥페이크·온라인 폭력 등 AI 시대 아동 위기, '아동의 시선'으로 해법 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791184&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 인공지능 활용 능력과 현장 대응력 갖춘지역 문제 해결사 389명이 간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791183&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부 장관, 청년 농업인 협업경영 현장 찾아 경영모델 다양화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791181&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 2026년 K-라이스벨트 성과공유회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791180&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 대한민국, 국제전기통신연합 전권회의에서 디지털 의제 주도 및 세계적 지도력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791175&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | "인공지능 전환 대응, 핵심 인재 역량·전략 개발해야" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791178&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 학교에서 시작된 인공지능(AI) 교육의 변화, 전국으로 확산한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791179&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방홍보원-MBN, 국민과 군을 잇는 미디어 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791186&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 소나무재선충병 대응 국제심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791170&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 전체 유료방송 103,974 가입자 감소, 인터넷멀티미디어방송 100,241 가입자 증가 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791166&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 뉴스페이스 펀드 운용사와 민간투자 활성화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791171&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금개발청, 새만금 관광분야 개발 방향 전문가 의견 수렴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791162&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "신체 닿기 전 '뚝' 멈추는 체인톱… 산림 현장의 고민,  '국민안전 발명품'으로 재탄생!" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791158&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(관세청) | K-관세행정시스템, 중남미 수출 교두보 확보... 과테말라 전자통관시스템(유니패스) 개통 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791146&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 추위 깊어져도 보호 빈틈 없도록 복지부·시도가 함께 메웁니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791160&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 공공정책급여로 필수진료체계 유지하고, 지역 가산분 본인부담 면제로 의료비 부담 완화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791159&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 통일부 국회와 「북한자료 공개 확대 그 이후 정책토론회」 공동개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791154&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 겨울 앞두고 산림 주변 화목보일러 안전 살펴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791156&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부， SKT와 히어로즈 패밀리에 특별한 하루 AI영상 헌정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791139&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 2026년 안중근의사 유해찾기 국제학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791138&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 모두의 성장으로 대전환을 위해 전 부처 역량 결집- 「양극화 대응 TF」 지역간 격차완화반 2차 회의 개최 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791140&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | "사회연대경제가 일상으로" 제8회 대한민국 사회연대경제박람회 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791152&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 모두의 성장으로 대전환을 위해 전 부처 역량 결집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791150&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 올해 현장 곳곳 누빈 '지방세입 체납관리단', 성공적 안착 넘어 더 큰 도약 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791148&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 극한 환경 재현한 민간 최대 규모 '드론 비행시험평가 기반' 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791145&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영덕국유림관리소, 영농부산물 파쇄와 함께  산림분야 규제합리화 적극 홍보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791144&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 범정부 적극행정 우수사례 경진대회에서 최우수상(국무총리상) 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791142&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 스마트건설기술 활성화로 공공공사 디지털 전환 가속화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791133&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 12월 대형사업 총 182건, 3조 2,259억 원 상당 입찰 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791132&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 법무부, 중국 시안(西安)·선전(深圳)에서 '현장 밀착형' 법률지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791136&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청 시설공사 주간('26.11.30.~'26.12.4.)입찰 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791131&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | '국가유산 보호'로 사회에 공헌한 기업들의 한 해 성과 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791134&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 근로복지공단, 일하는 부모와 함께한 보육 30년 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791172&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 건설기계·장비사고 예방, 전국 8개 권역 릴레이 세미나 마무리 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791128&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능 시대 연구개발 경쟁력의 핵심, '국가연구데이터' 생태계 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791130&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | "물에서 수소로, 수소에서 전기로…" 국립과천과학관에서 수소에너지와 수소도시를 만난다. '수소에너지 작은 박람회' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791176&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(감사원) | [사전컨설팅 보도자료 13] 희귀·난치병 학생 의료비 지원 확대 … 전년도 연말(10~12월) 지출한 의료비도 당해 연도에 지원 가능 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791177&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 조류인플루엔자 인체감염증 국내 유입 대비 제주공항 검역 현장 점검(11.27.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791123&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 기업 간 상생협력, 성과로 이어지다   「성과공유제 우수사례 공유회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791122&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 대·중소기업 상생협력의 주역 한자리에,   「2026 올해의 상생기업대상」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791121&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | AI 로봇이 배우는 동작 데이터, 국가표준(KS)으로 체계화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791120&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부·국조실, 창업·벤처 규제애로 전담 자문기구 '창업벤처규제혁신위원회' 출범 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791117&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부, 더 나은 의료서비스를 위한 비대면진료 스타트업 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791116&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 현장 목소리를 담아 안전과 무관한 수입식품 행정규제 정비 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791115&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 첨단재생의료 범위 확대로 희귀질환 환자 치료의 길 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791114&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 의료기기 사용적합성 평가,심사 안내서 2종 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791113&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 문체부, 국민 체감 정책홍보부터 노사 상생 협력까지 혁신과 소통 이끈 직원 12명에게 6차 특별성과 포상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791110&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 도서관정책 현안과 발전 방향 논의에 중앙과 지방이 머리 맞댄다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791109&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식품위생 관리체계 정비로 안전은 강화하고, 영업자 부담은 낮춘다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791112&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식품 알레르기 유발물질 표시대상 4종 추가...소비자 알 권리 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791111&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 의약품 부작용 예측을 위한 통합 데이터 플랫폼 시범운영 착수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791108&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 국제 식품위생 기준 논의에서 우리나라 의견 적극 제시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791107&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 영·유아용 화장품 사용 시 올바른 사용법 안내 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791106&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 어린이집 급식시설 위생관리 실태 점검...7곳 적발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791105&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 식품.의약품 등 시험.검사기관 기획 점검 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791104&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 물류창고 화재, 설계부터 운영·현장 대응까지 안전관리 강화한다 - 관계부처 합동 「물류창고 화재안전 강화방안」 마련 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791137&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청, 시도와 머리 맞대고 현장 중심 화재예방 정책 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791103&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(소방청) | "배터리(1차·2차 전지)의 화재안전성 강화를 위한" 중앙소방학교 주관, 산·학·관 학술대회 발표회(세미나) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791102&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 시내버스 두 대 중 한 대 이상은 저상버스 교통약자 이동환경의 꾸준한 개선, 모두를 위한 변화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791099&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 기업 자연자본 영향 공개 기준 구체화… 자연자본공시 지원연합에서 해법 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791101&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 생성형 인공지능 시대 시험 공정성 지킨다… 기후부, 부정행위 차단 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791100&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.27.금.석간] '무작위 표본 검역조사' 법제화, 항공기·선박 검역 사각지대 줄인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791098&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 땅속 광섬유로 '작은 지진'의 파열 순간을 1000분의 1초 단위로 포착 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791097&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 「한중일 및 아세안+3 재무차관 및 중앙은행  부총재 회의」 참석 및 주요인사 면담 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791153&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 국립대학 양성평등 추진 성과공유회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791118&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(인구전략위원회) | 김진오 인구위 부위원장, 전북대병원에서 출산·소아의료 여건 살피고 이원택 전북지사와 인구정책 협의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791197&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고)노동자 74명의 임금·퇴직급여 등  11억 4천만원 체불한 제조업체 대표 구속 (대구서부지청) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791096&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 전남광주통합특별시 나주 육용오리 농장에서 H5형 조류인플루엔자 항원 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791119&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 감의 새로운 가치, 푸드테크로 찾는다 - 국립산림과학원, 산청 숲푸드 현장설명회서 감 고부가가치  활용 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791095&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 산림유전자원보호구역 확대 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791093&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) ESS 중앙계약시장 14개소 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791125&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 차관보, 이라크 방문 및 현지 진출 우리 기업 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791071&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 대기오염과 해양보호 등 환경 도전에 대한 동북아 공동 대응 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791070&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방관이 직접 만든 인공지능(AI)... 소방청, 공공 인공지능(AI) 대전환 도전 잇기(챌린지) 5개 팀 입상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791129&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 위성정보로 미래를 여는 도전 「2026 스페이스 해커톤」 결선 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791069&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 재외공관 역할 재창조 이행 특별성과 포상금 지급 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791067&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 청년과 함께 만들어가는 대한민국 무상원조의 미래 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791066&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기본사회위원회) | "국민의 생각이 기본사회 정책으로!" 기본사회위원회, 정책아이디어 공모전 최종 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791065&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 중부지방산림청, 영농부산물 파쇄 지원으로 산불 예방 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791064&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 송미령 농림축산식품부 장관, 토마토갈색주름과실바이러스(ToBRFV) 피해농가 현장 방문 및 총력대응 요청 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791062&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 2026년 적극 행정 우수사례 경진대회 대상(대통령상) 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791057&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 기후위기대응 권역별(경기) 포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791059&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제23차 부동산 불법행위 대응협의회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791058&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부장관, 외국사관학교 졸업 현역장교 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791056&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 박윤주 외교부 제1차관, 온두라스·과테말라 외교차관 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791050&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영주국유림관리소, 산림현장 찾아  임가소통 및 규제합리화 사례 적극홍보 - 임업인 대상 애로사항 청취 및 산림 규제합리화 사례 홍보 등 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791049&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가기후위기대응위원회) | 제4차 기후위기대응 권역별 포럼 개최(경기) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791043&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 무역기반 재정·금융 편취 범죄(TBFC)근절 협업을 위해 6개 기관과 양해각서(MOU) 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791042&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | '26년 전세사기 기획조사 실시 결과 전세사기 의심 88건 적발… 22명 수사의뢰 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791038&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 따뜻한 겨울 나기 '사랑의 땔감 나누기' 행사 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791040&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-이란 외교장관 통화(11.26.) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791037&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정은경 장관, 그냥드림과 우체국 협업한 찾아가는 서비스 운영 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791036&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 국민의 아이디어를 통해 불편·불합리한 법령을 정비합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791034&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 2027년 비급여 보고·공개항목 확대 등 비급여 관리방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791035&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청 항공연구회, 공무원 우수 연구모임 4년 연속 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791033&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 무역위, 중국산 폴리염화비닐 서스펜션 수지, 석도강판 덤핑조사 예비판정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791030&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 해외직구 겨울용 섬유제품, 전기찜질기 등 31개 제품 안전기준 부적합 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791029&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한-일 정부와 민간, 반도체·AI 등 미래성장 협력 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791028&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 산업부 장관, 체코 원전사업 계획의 철저한 이행과 체코와의 신뢰 공고화 방안 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791027&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, '어복버스' 지원 기업·기관에게 감사 표시 전해 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791054&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 2026 라틴아메리카 협력센터 심포지엄 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791019&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 「2026 개인정보 미래포럼」 제5차 전체회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791021&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 인공지능 기반 보이스피싱 탐지 서비스로 적극행정 우수사례 경진대회 대상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791020&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 국가데이터처, 실용통계교육 컨퍼런스 개최 보도자료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791022&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 2026년도 재외공관장회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791017&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관, 용인 반도체 국가산단 및 공공주택지구 현장점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791016&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | "참여자의 의지와 역량에 맞게" 맞춤형 자활 2차 시범사업 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791015&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국민통합위원회) | 통합위, 김포공항 1차 행사에 이어 제주공항에서 두 번째 행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791014&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 지역·필수·공공의료 강화 위한 공공보건의료기관 협력 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791005&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 숙의(熟議) 거친 의료혁신 시민패널 84%, "연명의료 유보 중단 시점 말기까지 확대 필요" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791004&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | '꿈의 시작, 내일을 심다!' 제19회 드림스타트 사업보고대회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791003&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 지역·필수의료 강화부터 존엄한 임종까지, 의료혁신위, 대정부 권고안 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791002&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | AI 시대 보건의료데이터의 윤리적 활용 방안 논의 제9회 국가생명윤리포럼 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791001&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 국무조정실, 개인정보 유출사고를 낸 공공기관 대상 복무 점검 검토 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791011&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 검찰총장 제청대상자 추가 천거 공고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791000&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능 시대, 우리 사회가 마주한 쟁점을 논하는｢인공지능 사회정책포럼｣ 공개 발표회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790997&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 『5세대 이동통신 단독 모드 전국망』 시대,  국민과 산업을 위한 통신서비스 혁신 본격 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790996&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 내년 수도권 공공주택 5.6만호 입주자 모집…집 짓는 속도도 더 빠르게! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790999&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부 장관, 전국 1호 '햇빛소득마을' 김해 초전마을 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791009&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 국가데이터처, 유엔마약범죄사무소(UNODC)와 범죄분류 공동세미나 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791007&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 2035 제주, '녹색문명'의 새 길을 열다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791006&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 지역과 학교가 함께하는 아토피·천식 예방관리 성과 공유(11.26.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790998&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 역대 최대 규모 '컴업(COMEUP) 2026'의 시작을 알리다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790994&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 교원 대상 무고성 아동학대 신고 제도개선 방안 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790993&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 함께 모은 미선나무 자원, 공동연구로 보존·활용 가능성 넓힌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790983&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 국민의 생명과 안전을 지키는 현장 최고의 발명은? | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790988&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제18회 국가정책조정회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790977&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 일하는 사람 기본법, 현장의 목소리로 말하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790976&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 노동부, 최초 지방감독 위임 사업장 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790975&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, 한국항만협회 창립 50주년 기념 행사 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156791053&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | "민방위 재난문자 오발송 막는다"전국 민방위 경보 담당자 교육·훈련 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790990&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 국립보건연구원, 뇌질환 연구기반 구축 성과 공유 및 연구협력 확대 모색(11.26.목) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790974&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(조달청) | '나라장터 원산지 관리 강화' 관련 조달업체 교육 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790973&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 아이들의 상처 난 마음, 현장의 세심한 손길로 보듬다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790959&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(교육부) | "아이의 성장 속도를 지켜주세요" 영유아 사교육 개선을 위한 공동 실천 약속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790958&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 수업을 바꾸는 교사들, 교실 너머로 변화를 나누다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790957&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 일하는 즐거움으로 여는 당당한 내일, 역대 최대 118만 개 노인일자리 사업에 참여하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790949&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | AI 시대, 의료데이터 더 안전하고 쉽게 활용 「보건의료데이터 활용 가이드라인」 전부개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790948&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 내 정보, 더 안전하게 전송하여 국민 편익 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790953&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | '인공지능의 모든 순간에 사이버보안, 대한민국 인공지능 보안 역량을 하나로' 2026 인공지능 해킹 방어대회(ACDC) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790946&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 2026년 11월 퇴직공직자 취업심사 결과 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790952&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 공무원이 직접 만든 AI 서비스 한자리에... '제2회 AI 정부 실험실 이용자 포럼' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790971&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 올해 전국 빗물받이 898만 회 정비, 우수사례 30건 사례집 발간·배포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790969&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 재난관리물품 보관부터 현장 운송까지, 민관 협력으로 재난대응 역량 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790967&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부, '제5회 한-아세안 재난관리 장관회의' 아세안과 재난관리 협력 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790965&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 국민 생활 바꿀 공공데이터×AI 아이디어, 왕중왕전 최종 승자 가려졌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790963&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 지역을 품은 '마을기업',  백화점과 상생협력 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790961&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 3/4분기 가계동향조사 결과 보도자료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790956&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 올해 전국 빗물받이 898만 회 정비, 우수사례 30건 사례집 발간·배포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790955&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 물의 미래를 바꾸는 도전, 2026 대한민국 물산업 혁신 창업대전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790954&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 날씨 예측은 더 정밀하게, 위험정보는 더 빠르게! 한층 촘촘해진 겨울철 기상 안전 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790951&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.27.금.조간] 2026년 청소년건강행태조사 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790947&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 애플 부당 광고 사건 심의 절차 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790945&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 제2026-19회 원자력안전위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790944&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 통합돌봄 뒷받침할 '다양한 돌봄 공급주체' 키운다 복합사회서비스 운영모델 실증 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790943&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 양자컴퓨터 시대, 암호 전환의 길을 찾다, 제1회 양자내성암호 전환 경진대회･해커톤 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790930&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 물류창고 화재, 설계부터 운영·현장 대응까지 안전관리 강화한다 - 관계부처 합동 「물류창고 화재안전 강화방안」 마련 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790937&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 국토와 환경이 함께 만드는 지속가능한 미래 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790936&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 북항 방문을 보다 편리하게, 해수부, 부산북항 재개발 배후도로 준공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790935&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 우리나라 해양법 전문가 김현정 교수, 해양법자문위원회(ABLOS) 위원으로 선출 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790934&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 주행거리가 긴 렌터카부터 전기차로…제주 렌터카 업계와 전동화 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790939&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 국토와 환경이 함께 만드는 지속가능한 미래 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790938&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 찬 바람 속에서도 따뜻한 마음으로, 반려동물과 겨울 동행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790933&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 돼지유행성설사(PED) 방어항체 보유율 하락, 양돈농가 방역 강화 필요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790932&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '올해의 창작 K-Sool', 최고의 작품은? | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790931&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공정거래위원장,  중소기업 현장 소통 간담회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790929&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 해외 밀반입부터 국내 불법 판매까지, 무허가 수입 의약품 등 유통 일당 적발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790925&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 행안부·국토부, 관계기관과 함께 도로살얼음 사고 예방 캠페인 전개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790923&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부·국토부, 관계기관과 함께 도로살얼음 사고 예방 캠페인 전개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790928&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처-경찰청 수사협력 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790914&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | '가짜 K-상표' 정부가 직접 막는다! 범정부 적극행정 우수상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790913&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 우리 기업의 국제 특허경쟁력 강화, 「해외특허 길잡이」가 함께합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790912&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 국민의 생명과 안전을 지키는 현장 최고의 발명은 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790911&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 동포는 전국에서 김장 중, 동포와 지역주민이 함께하는 김장 체험 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790908&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국산업인력공단, '인공지능(AI) 훈련 우수사례 경진대회' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790918&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-27&endDate=2026-11-27&srchWord=&period= |  |

## collect:out_of_window (182건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
|  | 금융위원회 | 「대부업등 감독규정」 일부개정고시안 규정변경예고 (게시 2026-08-27) | https://www.fsc.go.kr/po040301/view?noticeId=4165 |  |
|  | 금융위원회 | 「금융위원회와 그 소속기관 직제 시행규칙」 일부개정령(안) 입법예고 (게시 2026-08-11) | https://www.fsc.go.kr/po040301/view?noticeId=4164 |  |
|  | 금융위원회 | ｢자본시장과 금융투자업에 관한 법률 시행령｣ 일부개정령안 입법예고 (게시 2026-07-30) | https://www.fsc.go.kr/po040301/view?noticeId=4163 |  |
| tax | 국민참여입법센터 | 법인세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-07) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88012 |  |
| tax | 국민참여입법센터 | 법인세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87940 |  |
| tax | 국민참여입법센터 | 부가가치세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87934 |  |
| tax | 국민참여입법센터 | 소득세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-07) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88010 |  |
| tax | 국민참여입법센터 | 소득세법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87942 |  |
| tax | 국민참여입법센터 | 국제조세조정에 관한 법률 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87944 |  |
| tax | 국민참여입법센터 | 조세특례제한법 일부개정법률안 입법예고 (예고 시작 2026-08-04) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/87946 |  |
| tax | 국민참여입법센터 | 지방세법 일부개정법률안 입법예고 (예고 시작 2026-08-27) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88260 |  |
| tax | 국민참여입법센터 | 지방세법 시행령 일부개정령안 입법예고 (예고 시작 2026-08-27) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88292 |  |
| tax | 국민참여입법센터 | 지방세특례제한법 일부개정법률안 입법예고 (예고 시작 2026-08-27) | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88256 |  |
| kifrs | tfmedia.co.kr | 회계기준원 ‘비외감 종속기업 연결면제’…신속 질의회신 요약 10건 공개 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTFBrVHByeUZ5UURxbFBTSGFsSnJPUWVlang0Z2kwdWx2UFhpZ1NDV0dXUi1ReVRJcUNyVzNXbnZMNDA3OE42MUpxZmVHcjF5bnZQZWREMGpwU1dFRkR6MHJreml5WQ?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | lawtimes.co.kr | 「2026년 재무제표에 대한 중점심사 회계이슈 사전예고」 발표 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBfbVVSbWFCOXVUa0JiekQyWVFwNmx3UWtJa1ViUGRteU1GQWZVM05ld2FKaUg5VkpKZEhMRk5lQ2JHTThUcnhEV0haQVYtMTMxd2tHeWlJYjlNa1Q5dHcyTzIzYzZFVzlIcE40aUtB0gFyQVVfeXFMUHlsUnhFOFZVRUlnSzJaeDVXWWhqaldGNlVTZ2xud25WdEdWVUM0Q3Y1WkZ6MHVZZTVUXzhleE82UU1UbENkam4xQzE4WUZWbmEwU3RrTzRaaHZFbk9mVjRveU1kcFFrb2lXZXBrWnRld1FB?oc=5 |  |
| kifrs | crowe.com | 2026년 재무제표에 대한 중점심사 회계이슈 사전예고 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5lYjFWby1TbVI5SWdPLTdTQXdhX3lfdi1GektuUG5LQ0FLMDlDbWVsYm11S3o0ZDlXeEIwTlVxZzlmYVdDajVSUWJDY3FVSGZxSG1Ublg2M2E?oc=5 |  |
| kifrs | 일간NTN | 금융위, 만호제강·의왕백운PF 회계기준 위반 제재…과징금 9억9640만원 부과 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBlQnVuWTBYYm5OdDc0Nm40UGVzZmU2TEpUNE1iRkJiZzNDMjRjNlZXbjR2UWpmQXkwRURFemN3U2pvRWo5ZXpIZnNxNE1sdHQxSlNxRG1aM0RmUHR6VjN0SlBrRVg3eTN3bGc?oc=5 |  |
| kifrs | hapt.co.kr | 승강기 교체부터 고철 매각까지 세무･회계처리 - 한국아파트신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9mSmFsQnZBTmRvNzZha0dudUFIN2I4Q3lwWTJleVlqTERKaTdIUklzT1dobzA5dGViTWxmNlFGOW01dnJycmpYZUhudHNMdV9TbGhoUy1wSnF1MG0yTjZvTUFDS2U0bGY4?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈- ②] 손익계산서, 이렇게 달라진다 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5IdHFEOXBDenRyV1dVZ1loZ3FhZWMzSG5WOU1VZTZMNm9mYmRETU50U2I4NS1NME50eW9MYkJ6UUhkQk5HbDQ4Ym9IZk1fVHJZWTFvRTcxSEJJbDhZUXVxVVFjZDZpalE2?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제 1118호 영향 관련 사전 주석공시 모범사례 마련 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9zRzZZWnBpdUE1aklrUVM3MWw2cUVXTzF0dTgwZy1uc2NzdUJpeDhDYjFBNmFWaDQ4bW45a2ZIOWJxMkJtdW0wbWFMdGkzbTV5TXhNV2RjVTk?oc=5 |  |
| kifrs | dbr.donga.com | “회계 기준 지켜도 재무 실체 숨길 수 있어 AI 군비경쟁 시대, 숫자의 행간 읽어야” - 동아비즈니스리뷰 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5qMUhEM1BDNkZicXpqTE1BQ29zYzVrM0FfdXYwLXhvS201RXE5NmVJLWFZaU1Xcl91XzRocV9BMVduQU1JYWw3cldobElDWHo4Q3hoNVF2cE5NWjhjRWJRSnhGT2pNWFU?oc=5 |  |
| icfr | 한국경제 | 외감법은 경찰, 자본법은 중수청…분식회계 수사 차질 불가피 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wOF91b3FKNTlVV3FUM3J2amdHek9VS29CTHZ1N3d3NFJiOWtOakNkRVRPSzhFd3ZKMHM3RkRmcW9QeE9hRFV4NHNhbmQ5Q0RSNUpIbEYyOG9zUQ?oc=5 |  |
| icfr | newsroad.co.kr | "내부통제 효과적" 자평한 빗썸 경영진…감사·회계법인은 "취약점 발견" - 뉴스로드 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5Cdzl4cjBaTmg1YmMwNTFrUm16YmVUcW9lTlBfcU1YWFBXR3kzeGkzWEtibERzajFnMG92Wk9oYWh6Y3FHRTdDNEJJVkNVZWxXLVdLYWpTUm5CWThiTGV0cURIcldhZDRMYU04?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| icfr | mediapen.com | 신외감법 후 외부감사 기업 증가…지난해 4만 2891사 - 미디어펜 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE1scWRLWExwNnFZVlItbzk2QnhHMGo4VkdGc0Y5Y2dseDMtOGFxNDB0LWhTalFDV3J2ODNudEFnTllWZS1odGEweG52dU0zVGlLRFpNVdIBWEFVX3lxTE9KMnZUVy1CTWIybHRmSFFvZ1lqWkJibTIyNzN5eWg2V3lVeVRlLWhYaXJ2VnRKSmVOMXR4b1FxQVpnTnFya3kzV2tLbEh3OUJ4X2hSUVhiTEI?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | biz.chosun.com | 신외감법 효과 끝났나… 회계법인, 성장세 주춤 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUm1NS2l2eUNoQmVvMGxQTmIzdDRMRmhWcnBDRkhSMDl3MFdkVGZTNUI2cXRUVENWVkdtRGw0anhYWU1rZk5BRE9vYXhkMG8ycklqbmY1WlBRVk4wcVpPRUw2cVJWeXotSGVvZTltUHk0RFdMcHhVRzNhY3hXNF9zQ1VqZkprMVpF0gGcAUFVX3lxTFBvOXhIVjJnMVdEd2F2bVNnZnRZdkY5ZFJRZU5ESVN0cnlvMk9aYmd5cjlKbTZWTDV2TEF6dG1nTGk5a1daQi0xOE91bno4RUltazMtZUFocEk2d0NkM1h2XzBxYTZ6eHgyMTFQOFNBYW42VUpVZUF4Vlo3cUcyVTZHbWEwLUVLb0J6MDk5OW5uc0tjTVhhZzc0RmlRZg?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | ESG경제 | 공인회계사회 새 회장에 최운열 전 의원 당선..."신외감법 유지해야" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5wczU3VWVubFMtUTdpOUI4Sm5XQUozYW9mVjRwQVY5TlEtRE5heC1nSnZrWV8waWZjNktsX2MxZk14TC1sRTdCdUxhbDdtZldlQkhsRElIVFBya25mLW5PLUFMd2xpR3c0X3VV?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | newstomato.com | (신외감법 도입 4년④)"유례 없는 감사인지정제 폐지해야" - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SYVZyanVjZE9LQzY5OTdsWEtDNWhDMmxFZmh4eGNyYnN5RWZkZmNhdjd4M3Rra1FrRVh5dVFwem9CUjM1WkpOUlBaSUZ2ZzBzalJnaFN2M0tFSlQzaTJFeQ?oc=5 |  |
| icfr | ceoscoredaily.com | 금감원, ‘여전업권 내부통제 모범규준’ 마련 - CEO스코어데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uT1g3UWpVTlBNRkRaZ0lXdFpDT1RuekF3QmIwVlE2NFJaTTJYRmZSaU5fRERFUWdoaldUc3BYZ05pU3h6RldDSFA3cUxpME1nMzRtMG1QWmdrNU1jcUgzRDM2WmdnZw?oc=5 |  |
| icfr | hitnews.co.kr | 新외감법, 연말 ‘밀어내기’ 잘못하면 포렌식 당한다 - 히트뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1SdW1ibmVsdHg0UGZIX2NnQmlWM0hEWUlBZHRMQXdPQzlDQzdnOXA0eHhKOVFsTFVZWGlLTnBlZmZsV3E5TlNrYWZBZS1MTW1OVi1MWjNFYVU2X3FmVEUyZ25mZzZtY3JDMHc?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | newspim.com | '신외감법 도입' 회계사 인력난 가속도...시간제 고용도 나와 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9jN0V1bGFpbDFpcGJOcTRFR0JOR0lCT0ZKUy0yS21MQ1NQYVUwbHY0RWFKRUs4M0cwUVJsZEhuR2tGUjlLUlBDeU4zRjlWRFhpUjg5Ukc0VGY5UzNX?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | m.ekn.kr | 코스닥협회 ``신외감법 시행으로 상장사 규제비용 15년간 124% 증가`` - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1IR3cyN2t5c0NGQWRqM0k5dnRWSWxyd1VJZDgxQUp0X1FmMjlTb0tiXy0tajI1MWZTNjFabk53Mnl6Z2lJeHdRazRCOXQ5T1ROMVc1RUdGNXNVclU?oc=5 |  |
| icfr | 매일경제 | “외부감사 대상인지도 모르는데”…감사인 선임부터 하라는 외감법 - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBfb3RIa3ZJZXVfMGlqNXVPSzh1bXhyMDdxRXY5Zm9tM2xselczNFhncmwwWGk3VE1McW5RZ1cwY0tydHBEdW5oRWpfUm9JMEVINFdhUg?oc=5 |  |
| icfr | ibtomato.com | 신외감법 시대…발등에 불 떨어진 코스닥 - IB토마토 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1wTnhJTjNyNlBDcXBLejBQRm16NmxYYjlGa2htY1poZkVTTVVMcGFkNW15M2xwMUFYRDZlLUN1SEE2M3JpT1oxZ3MtYlFIai1nWHdKTTlkVDB5VFlUTVR6MnAxVFJWendn?oc=5 |  |
| icfr | m.ekn.kr | 금융당국, 여전사 내부통제 모범규준 시행...동일부서 5년 초과근무 금지 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzUkZ2RFlzUjE5OUZ4b3ZxOURwN3ZORVo1UWFXTDBrckdQREVSMmVpbUFkU0VqQzlHNkVVVjBvLWRPUURzenpUNkVjZXBrTlpMblpmMDdmWXFjcnc?oc=5 |  |
| icfr | 머니투데이 | 신외감법 주도했던 회계전문가…'회계기본법' 제정까지 힘 싣는다 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9zZ2tGSkR1eU54TFk4RnYyTUlzcFhjbWNDdlpuTHkxNUppQnVQdHhQcjRtY1RsT2JkT0xudVpxdlVHSG9MSW9nWDhNa3FvRS1pUl9qTFlRcUtQMkRUY3hqSHphMTNRN0Yz0gFuQVVfeXFMTTlSZmpjcWZ5eDdQZTVwRjZPQzBmSXFScEN0bFlyanVlLUlTdGN2Mi10alpTZTd5ckVxei0zTGxWLUNPQTVISTNhb05PeUpXaFFwcXRHTzdUYm1xRG5zSDRLcUxsUXlVcy14LUhqQUE?oc=5 |  |
| icfr | joseplus.com | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5YdU02NTVNcUpacFpVMVJmT1YxZnR5amRUOFk4Q1hXM2VuZ25MZUc4U2ItbEc4ZGpUVmlFZTQxZ2tDclQxaFlTakp5eVptTHdkQThsanc0TFjSAVNBVV95cUxNSTNmUGJpUVlGTXlxODlYR0h4RXJ5eVdwV3cyMVdTN1A5WllFcVQyMEVmZ2FJZFpqVWRpNUlQcjJpb0tnVWk1RktqdEdxMDd1aU81dw?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | investchosun.com | 두산에너빌리티, 회계 논란…신 외감법 이후 강화한 제재에 치열한 공방전 예고 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPd3hmMGM1TkJ4dFQwVkt5a3hmYmdZbmctQy1GYnpoR2JyUGN1MURsVWFyUWhtVENCaF9wUk1wZW5sYWhXSmp2OTBLeHFQN0pPRk5ESnZHTndNXzJzbmFjc1E4aTlzcXJOLUNKV3I0UVhhNXdFVS1wbUMtYmR3TElGVTRCMA?oc=5 |  |
| icfr | core.asiae.co.kr | [Why&Next]‘회계사의 꽃’ 파트너 승진, 신외감법 도입 후 최저수준 전락 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE1GQ0paYVh4cms0bTZZVFotNGI5OUI2cnpILU9TVi1qZmZ1MHFlbnRrZnhRNUJ6Y280OGl4TFV0QkpTOGtOV0UtM2Y2Q1JvdmVJTmxLLUxobk9jLV9CM3locm1B?oc=5 |  |
| icfr | 한국경제 | 회계기준 위반 내부감사에 과징금…외감법 개정 후 첫사례 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5lQlUwNGVxRFhSVUUzSlRnemExbzQ2M0Zka3ZMS0pna0RFOFZVODRiLWJwN1Z1dF8ydS1JaEdFdXhHeVlUM3c3UHpXZ05oamt6a0NBY000a1NEdw?oc=5 |  |
| icfr | zdnet.co.kr | "중견·중소기업도 '신외부감사법' 곧 적용...미리 준비해야" - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE94ODR2UVJKYTdMMjEwVWZRRW9vUlFQdkc0enB5RFBiVTgxRjBKUENtLTFUeXpneU5nZ1k5THlfa05PZWdZZTAyZFFVZFBmaEt6MFlJY2h3?oc=5 |  |
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |
| icfr | sisaweekly.com | [단독] 금감원, ‘선행매매’ 하나금융투자 내부통제 취약점 조사한다 - 시사주간 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5fXzBXR0Z0R0h0TVJsZmRvcFZEZ1hmc0duTDNNb1lRMGN6RlBPZjB3b1M2a05IZm1saXlhM0M3SFNWVU9uNTQ1WDNQRHNDUXBwa2NwSUhXemlsblZZWThTeFdrSWNYQXFxRDVqRQ?oc=5 |  |
| icfr | 한국경제 | 新외감법 5년간 감사보수 급증…"중소기업 회계비용 부담 심각" - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5ieTJMTTF5dmsteU5Vbk9DTWR0LXI2REVHb1lTZTF0aDVPMVIydTN5bGV4RU9hRDFOeE5jejVaNkF6NlRaVXpuY0s4eWZmN25lY2pyeUpxZmIwZw?oc=5 |  |
| icfr | newspim.com | '비외감법인' 데이터도 공개..."비상장기업 투자에 적극 활용" - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9RN0FQbk5JNG55OWZCTXN1bi1XLXNPUHR4WWJiUnZNSHl5eFk0M04yRGlYaTQ2Njd3bE5MbnRRenBIUm1RUGxGaVljRXNUWVZQVThxQVNhdk9FOUdP?oc=5 |  |
| icfr | byline.network | ‘신외감법’ 적용받는 유한회사 – 글로벌 빅테크 기업들 - 바이라인네트워크 | https://news.google.com/rss/articles/CBMiTEFVX3lxTFA5WXBCTzF6LXIyb3R6MDNzazViYWVBNzVjOHVCMlJncXdyUTdxQmdmMTFPNVpNckVFYXBlTVp5TkFZY0MxcWROUy1NdDk?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| icfr | crowe.com | 감사전 재무제표의 제출 시행 안내(외감법, 2013.12.30 개정) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFB3dVdRS2NNTTdZdXQwam9iZ2JmU1ZBcENOMGhER2c1ajh3WWZtZUUtdjg5ckdaZVdJRlNGc1RycGQ4NHBjdHMyOFd6QThCMDRqNkxjd2d4RS0?oc=5 |  |
| icfr | fortunekorea.co.kr | 글로벌 기업 깜깜이 실적 드러날까… 금융위 외감법 개선 검토 - 포춘코리아 | https://news.google.com/rss/articles/CBMickFVX3lxTE9GQnJfSm5OMk5pOWVUUC14aFBrQUJUZEJuMnVzLS01MU0tM3M5UzA5RzNPTnVfS21iUzI1QzZxNmU0a09iUG1RU0ZEY1hPdUtzNEFDME9pS1JqdmlFZkhULXUyWXh6ejZ5WU8xWTRmMFhYUdIBdkFVX3lxTE1Md0FkSEpRTmxlZENOUXBSRmtDMzBoZjl6dE1xTi1QcmtsN0d0OTR0NXhyVjdGUGpGSlc3dXpoRnNBQldzcWlzU2NzRlhsdlJieGhUS3o0ZUtFcnFTLWdCdmtDbmdaOVVIR0RRMU10LURKRXBIUlE?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | paxetv.com | [1분 영상] 최운열 신임 공인회계사회장 "회계투명성 높이려면 신외감법 유지해야...감사 비용은 투자" - 팍스경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9tWWdmYkxZY2dXTDVBV2xJeFUtLXU0S213RklleTJDZUlCd0ZSQTFyc0FPdjVhYXBGZjBQTXNaUHNsYXpGMzZlMWNMNGMyVlZSNWc2WEd6c0NtX0VibnVjVXphVmdpbldj?oc=5 |  |
| icfr | 매일경제 | 삼일PwC 윤훈수 대표 연임 신외감법 회계품질 강화 성과 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE83a3Z3OEV1NUlXYkduTHJ6SkRldDk1V0JyaVBXdTNqdlFJUnNhVkZybkdRekhNTHFUOVFNWGVvNTVyZzRwOVh6b1dxZU9jM0xQ?oc=5 |  |
| icfr | newsis.com | 초유의 오스템임플란트 횡령, '신 외감법 무용론' 번지나 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SR1lOd2VmanJnVW9FQXRwSVJYUlIzSkNnRndGNEcyRmlxUGxiUUE4VHkyZUwxbFZOMk1wMWZ0dXh3QUlkOXlUWHNvYlh2Qm80QlhOMGlydTJvTXNyQVF3N9IBeEFVX3lxTE1CUVJtSHR0MHpJa2JOZ1dtODNsZUp4ZlEtZ0g0ZEFpNDVzNHM5RlZndGdpS2xoc3hDcUVuOUsybGxVQUotSzJmdlRadEdPX1lhMlVMTzN2RzJaakNuWmJrZko3ajBfbmVNVXZ6eWpOemh4ZVNrOWEzcQ?oc=5 |  |
| icfr | zdnet.co.kr | 더존비즈온, 내부회계관리제도 시스템 'DICS' 출시 - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE5ZWDVfQU95b2dIdy1LZE1MZWxXRUNPY3gzTUxjLUNMdDVjU0draEpfMWZJOEJzN1gtb05BVUZiNE1xODV3LW5TTmR0VnA1YnJYV1ZhbEZB?oc=5 |  |
| icfr | g-enews.com | 여전업권 ‘내부통제 모범규준’ 발표…금융사고 예방 - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPdnN1VDh3OWtkWUZQSlUwaGZqdFVtYWpZcC14YXhnMlBKTDlkczNkRl9DQ1drMGRrdE04dzJvaktvYmR0V2JDakp2YkpqUVhZbVdwdC1nY1lNS3NGLVBDU0o0TmxEaV9ocWJxWjhmTzh5S0M3bXRIb1kyaGtTamlKZWtsWQ?oc=5 |  |
| icfr | investchosun.com | 올해 외감법 전면 시행, 표준감사시간제 도입 등 실무적용 진통 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPU094cWNReEdYMkZncmkzdVR4eXkyX1BITTU2RXlEZzhBdDc3eVRSM3B0LUJ3VW85dzFZVF93NHBIVEdXc1ZqdFRXUGN2R0VlQUFadkw4V0ktTVE5N2t0clhDZ0NneUxWa3diWWExT0FhV21GVmpiZkxtN3JmSmo3MnZiRQ?oc=5 |  |
| icfr | news2day.co.kr | 한국캐피탈, 내부회계관리제도 고도화 나서…투명성·신뢰성 제고 - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE1fVjl2UnRnek5jelpoRk9reU55VW5IR2ZuSGpGbkVzNkVuYllnbExVWUZlMTU0N2JLalhEdmhwSmtPcDdYQ01ua3RJTkU0dFBxUVBQdEtmdHBaOWl5Z1E?oc=5 |  |
| icfr | newsis.com | 한국캐피탈, 내부회계관리제도 고도화 착수 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9SdTRtUmJ0UUdyZ2FXclFzekhGM1lHT3BHVGd5MF9kRnhOS1JySFFLMmk2RXRpcC1SZUNfcl9MRmNYeVczOUZwcjJBT2I5dno1UWFfVHRPX2xMd1lWZW1XSdIBeEFVX3lxTE45RGlXZXltSnhFbGlRQ3ZENEt3YjhTVmJnX0hmTVI2cGtTa1ZhemxFOUlqWlRxTUZmOFFlQWVjaGUxd0MxVmJOQzdwM0Ryam1PZ3lPcG1XVy0taTFHWU92RlJCYjVGNTV4R2FENmk3aG9DRDBjcU1xTw?oc=5 |  |
| icfr | 한국경제 | [한경 CFO Insight] 신외감법 2년...감사비용 70% 폭등 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCc1VNZVE2U181NVZDQzlZYnpVM2E1MEtxdXRDS00tUGVlN0ZSTFVzNTRhWFQxc1NKUFFtYjVKWEFDUmZkZVItN21jdkJvSFphVUVVY19QNVVlUQ?oc=5 |  |
| icfr | newswell.co.kr | ‘신외감법’은 분식회계 때려잡았을까 [사자경제] - 뉴스웰 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1uanRDX2xxdzlFYkx5MHQzcGh6YlUyWFlBdEl1ZmZNbU9KVVptbzNaNEpFWUFYN3BVd2tXdGpUb29hODR5RGtuaVlsaDVhdS1xY3IzZi1wOUZxeWdrVzk3UFdab3I1MDliLVNB?oc=5 |  |
| icfr | etnews.com | 씨에이에스, 新외감법 대응 위한 내부회계관리시스템 'ControlWare' 재출시 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTE03bTFIY0VhM3FDbE83bncta3kwdFFMNHFpY1NVb0lZV3drZWpOWUViNzZSekhXM0VxVmJCZ0VPSmdHQTlocUdkY3IzNlNTQQ?oc=5 |  |
| icfr | newscj.com | 금감원, 여전업 내부통제 모범규준 4종 제·개정 - 천지일보 | https://news.google.com/rss/articles/CBMiakFVX3lxTFB0QTlNOVN0VHVIT0FTSjljVGVFaGkxV1BCYzRZZnFWNFpCZWMweHFnN000WExSTXhlN1FYTlhZRlZHa0xDcElIa3l2cWF5LXdITktTYjNZQVNYOWNFT3ZPbEEyaXM2MWp5R2c?oc=5 |  |
| icfr | metroseoul.co.kr | 여전업권 금융사고 막는다…'내부통제 모범규준' 시행 - 메트로신문 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9NRVlrbVRkd2xLRXh2ZU8zdTFwTFVOQlVHN1laeXUwWDhZSlRwMkkyNVgwTDRGU0ZfRGNfYXYtbWRUS0hjdlNLVHh0dTU2bHQ4d25JZHJ3a3BMRWZuZWptUA?oc=5 |  |
| icfr | ajunews.com | [경계불문 DX] 신외감법 시행에 ERP 회사 더존비즈온 바빠졌다 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5DUVhuQ0cyWmN2YmtERDB3aWRYTmVGMGlfek8yQ3lQTVpkTFdMLTZKVkpqZDN6RnhpQUhLcTVUa19CdlROS25TdUdkcU9rc0IyNkRYMUhKM2tIQdIBWEFVX3lxTE5NT1pQdWFtT0RrNS1SbG1Fdmx1SmhJYlVMcjQzSmpMenpNbFhtUWVNZldfc3FyekduZTkyakl0YTlHZ0R4MkZxN002Zy02cWV4cTlGMGlfR1Y?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| icfr | donga.com | 카드사 고위험업무 5년 초과 근무 못한다…여전업권 ‘내부통제 모범규준’ 시행 - 동아일보 | https://news.google.com/rss/articles/CBMidkFVX3lxTFB0NUVYMHh1RFBxTUpQTG9IbGVXRkRKRGQzcFdBanRCWUZsbkFlU0c2ZTVhYTdCWDZwRURKYkIyN1hIY1JtYjJyVnVBaW5VMWdteFNvZldWQkhlTHdrdVgyQlgzb1IzcW9uZlRtSGZXaXBkcnd4MFHSAWZBVV95cUxNMVltbFQybjRZSU5tN2w1X2ZOeWFnZ3gyVVFrTkJZTUNiU2NIZjQzc0JOYm40VlNibDVjYXZhTVNZRlgtMU1kWG05WUMzWVR2VXdoRk51QS1nc1JNR19MX3BEV0V5cGc?oc=5 |  |
| icfr | investchosun.com | 외감법 개정에 연봉 공개하라는데…'발끈'하는 회계법인 임원들 - 인베스트조선 | https://news.google.com/rss/articles/CBMigwFBVV95cUxPR09HalljVnVnT25LS1EyYWQ4b3R5emJ0aUoyUnlTNUFISUNKWlVkc2x6ckl0MkFTbmNFSTJ2Zk5hQkhub0tsNFh6SW5ERGNDb290dEVNdVJUdFI2UWdublRUd0x4a294eFVjeHZReGJZdXRndFh4NFNRajR5RTdmdnVuSQ?oc=5 |  |
| icfr | itdaily.kr | 더존비즈온, 내부회계관리제도 시스템 ‘DICS’ 출시 - 아이티데일리 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE1CODVGNXBKQjRGMjhVY1pUU3JiQXIwU25Ga2NkeU9IR0xaVzlwYXVxdkZSeFVWWG00WXprcHlIRlM4R0ljbFhvWmFMeGRPTlRnbm1uT19JWHdrS1FzdFhTbTJjZEU2QQ?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| icfr | 일간NTN | 외감법인 주주 500명 이상이면 정기공시 의무발생…"IPO 예정기업 유의해야" - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE90S3ctZnFaZkQ2T0t1VmVXRWNnS3Y4ZjUzVVJPalhHbUxuU0dtWkZiM1l0R1RHZlNsdU9SZXlMaE9hczI4al9rM2ZKazljbmhSN3lXVThzUkV1ZF9iZWpRemVPbENUa2RFd3c?oc=5 |  |
| icfr | newsis.com | 금감원, 여전업 내부통제 모범규준 시행…"금융사고 방지" - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE0tdGJEbkh1Wlp2VEU2M3BjYWMwRTlJd3ZFUEp4TnVRdHZGVXVXNGZZQ3NyLU9JdHNPMERIMnBENnZaenVwUl9tMkNhLVcwdTZhMURXZnhlU3hEd3JVOEdNOdIBeEFVX3lxTFBVdXNnNG9ycGs3LUNfV0NfLW1vUlUtTkp6b1ZhMFpxSWpSUTc5eUdMR1dSZzVDT2xXWHRyNEIwOWVwWmJoYlh1ZWpnRDlHRUtodVpqX0lHZUR3azR2a21pMXRSczRlZFp0SllnOC1kNzVFamkzTUM4TA?oc=5 |  |
| icfr | fntimes.com | 신외감법 시행 4년차…감사인 선임제도 위반 기업 전년비 177%↑ - 금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE1scHBINWVyT3R0NmVEdzNYeVAyLW9qaEJic2JFSjlJc1ZHTHdydzlYOHJQRXh3X3Rqa1RqcVlVM0tYREQ5UjBhMUNVbFAzQ3JyTU1obGlkeVRSM0tzV0NSMkcySy1vZlM4TWwyQUplTWNOcWo2aWg0NC1DcVE?oc=5 |  |
| icfr | fntimes.com | 금융당국 '회계개혁 평가·개선 추진단' 구성…"외감법 개선안 연내 도출" - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTFBGUXkzSDVpRXVnTXJFYk9nNmtHc0g5d2N1THZHNlJfYUpzTk1iLWlOR2ZQUWRjOW9GMFNnMXpZdVZuLTREd3htelFCd0JhZ0FOZjdwNE5fS1RBaktzcEJWZS0waUIzS0U0MUp0ZTk0VGg5OGRQaGQxbktwcTE?oc=5 |  |
| icfr | biztribune.co.kr | 금감원-여신금융협회, 금융사고 예방 '여전업권 내부통제 모범규준' 시행 - 비즈트리뷴 | https://news.google.com/rss/articles/CBMicEFVX3lxTE1lVGxvUjhBejhNT0I0M1R1QkY2czc3VUxBWWFoZjAyeEJycXJtNGxIMFdHaFppOVlSX3RrU3lqOUdtYkE0cGZmRlNJaVBIZW10ZVB3VnJQTFRYOU5WYkZ0WDlSN1pPRDBmVEJoVEZDdVQ?oc=5 |  |
| icfr | fntimes.com | [프로필] 최운열 한국공인회계사회 회장…신외감법 주도한 전문가 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE4wWUZmaWJVbHVCRHNmQng0VFYxZG9kTGVuQmhqSmtlekt4MEZtODRIWTU0ZjhYczd1dzZIaWlCTzJBNURnWVJqRmp3ejA3end6ZUZMTzZtbkxYMmV6b2dCQWJKVGRjc2QxV2dUVUdSSWNydy1YdndvbzBZTWg?oc=5 |  |
| icfr | 서울경제 | 카드·캐피탈사 순환근무 강화…금감원 내부통제 모범규준 정비 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5yMmlfZHJmeGF0N3BFaW0tS1NmZUZXM2dEQXBCUmM5NHV5aEJwcXNCN0Z4bG5ZWlhsaGpuU3FGUDgwQlZ3NTRWM3R4QVRVUUcyVHfSAVNBVV95cUxPZ2JSaTVKelZ2S2NNQTQtNzRyaHQzODQ2THVqOWFOVHhVaEltN3NpdmRfR3VIaG9WZzRXanRaOWdndkJHYUFMWDRXUWh4NS1HWVFoTQ?oc=5 |  |
| icfr | sejungilbo.com | [재계리포트] 新외감법 ‘그룹 연결회계관리’ 비상…더존비즈온 ‘EFIS 10’ 주목 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTFAwMkJtZHdlX3lNSUxIMWRMMkNZb0tRbjJkNHF2Sm0zbm5GeFdjeGE0R2RRRFhyX3FSbXJRTXpPVmpBSHlKR0R2NzVPTGtES1pTZjhhd1hkbjNzQ0dXZGFxWVZ4dnZaelltNnZ1Zg?oc=5 |  |
| icfr | newsis.com | 외부감사인 선임 45일내로 단축…'新외감법'시행 본격화 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE9oc0dCbXI4OXR0SU9FSVdXM0ZQOXgxSHZNRGplVFhZX1pUZms0ZFpWWWZnX2RFbEVnWGlIWnBNc0JNUU9KOUxBS1EtczhhTGlOZnFQcEIyUTJkMWM5eTRtNNIBeEFVX3lxTFA3ZXU1SVRsUU4tMDd6ZzcxZnRYU0tIaEJWeUFZclVKVlpUT19HM0Q2QTBxbnRicjJQRHo3ajlxYWx3V3FLMnlrTWRUZS15T0dfTmtqc3NRazdnSGVrMUNPUm9LSWVBQ004TGNpRTZpY05abGpuWExWeA?oc=5 |  |
| icfr | news2day.co.kr | “新 외감법, 부담 가중” 경제인 앓는 소리 진짜였다… 감사 보수액, 4년새 2배 '훌쩍' - 뉴스투데이 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Jd2hPSnlTb2h1bmhZbXFvSmI4d1JrZEQwTzV3eFZfX0V5c201YWF6Nlk3YmdhQjlnejN1UjB5TDQ4V1Nfc0R0aUdUTjludGN0QzF5MW9OTl96ZUhtWGc?oc=5 |  |
| icfr | 매일경제 | ‘新외감법’으로 상장사 회계법인 교체 쓰나미-삼성전자 감사인 누가?…빅4 판도(삼일·삼정·한영·안진) ‘흔들’ - 매일경제 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFA5cno2VzNKMGd0UlJ4UjI1Q3hSamxObEItQWNqYThZcElJYm4tR25UZGVOYkhVNUhYcXBMNlpGV1hLQ0hOQUZnck1jdFBHWXlLcXk4Vw?oc=5 |  |
| icfr | newsis.com | 회계 부정시 증선위 신고 의무화…외감법 개정안 재발의 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1KXzZNNWFieTVwWkNTQkxSYjZzc2FWc0hzSWZGRWZNSzhqMlppYnl2RDk0cV9TdUstUGNlTVo1NHFTV2N2OUxKSi04ZUlEWGxWU0hBSXR0SmVhY213QXpjUNIBeEFVX3lxTE5uRGU4MUVuRGlCS2pqQnFLTWVwcE5jWEszTlU5TmdseTgwVXpNRURKelZjekdwSWptWHhSWW9pdHYzQ0xaS2w2XzJzVExoRVlhSng1akxwSlh4VUd1TUY2UVc4aExYYmJpVngxR1ktZ3phSm1VaUR3SA?oc=5 |  |
| icfr | m.bikorea.net | 더존비즈온, ‘딕스’ 출시 - BI KOREA | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1oSE9NUDlTaGlDenVfdHhWYVZMcVFJSUxGUU95ZHAtNVh6Q1hQSlZSNmVFM3RZWUdDb2ZfZmFnNmpyWm96RUVGOFBWM0RBdXlISlBuSkt2QU9weEYybFZMUkF0TUE?oc=5 |  |
| icfr | etoday.co.kr | 28개사 ‘내부회계관리’ 비적정…“내년엔 더 문제” - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBMOW1idWYtTDJmTzJCazdzXzF6dVRNbzRsYklQaHFSRkc1Zm1MVFRiX0hwZ1ltNHVJTFM4Y0JZYTh1OHc4Zmp5MnkwR2tSYUdYMmo2SA?oc=5 |  |
| icfr | 파이낸셜뉴스 | [인터뷰] 채이배 의원 "외감법 개정의 주역이 회계개혁 완수해야" - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9wdUF6OXdLMktRWk9RTlBNaEIybnUzb1NaYmgzTkZ6Q3VLcndXNmRCQlhzeFhyTWFBZnU5WXVIVl9aQWplZFdnT3ZReGkzaDJDMTNVUkJhTXhndw?oc=5 |  |
| icfr | fntimes.com | 삼성 등 금융그룹, 내부통제 구축·통합 공시 도입…감독 모범규준 5월 시행 - 한국금융신문 | https://news.google.com/rss/articles/CBMifEFVX3lxTE5GRTk0ekFOakRta0tINzdwNTFSQU1yb3hzNkRKbHN4dkxVSkwwWXRHa3l6UVBSdFdBV2JxT2JGV2tlbzQ2RU1nUGRIdDVYVTNPWmh6eFJZT2ZaUEJVWGduZXdOOXhiOFFCaWJhQmktelFFcjJ0U3FJS2lpQ2Q?oc=5 |  |
| icfr | etoday.co.kr | ‘신외감법 영향’ 지난해 외부감사대상 기업 전년비 2.1% 감소 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE9rVUNpWXJWdkI4eERCSTQ1cHNkUGtZTzl1cllxeTBfZ3F2OWhoODVFWVdVUVpjMTYwYmZ3RXVjM3gwTXJZRHVHQWlmRGVodjVQRk54Sw?oc=5 |  |
| icfr | biz.sbs.co.kr | 씨에이에스, 외감법 개정따라 내부회계관리운영 소프트웨어 재출시 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE9CdDhZWEJKNm1ZdWRTcDM0RndZMkY5dGo0cjZCU3RucHBFM1BVeUk3cVFzMEF6WGdMWC0yNEsycTNJRWtTYlltcXNIa0pjaTZDaHhn0gFYQVVfeXFMT3lNY1Y5VUxSOHVnU0ZiWEZyb1M1V1ZMVElxZnIyU0U4TlEtTHE5aHVwekdxU2p5amVVcDYtaWpzcHBqUl9JT3RyM0RELVpKTmJ1RzJYSGszUg?oc=5 |  |
| icfr | mdtoday.co.kr | 새 외감법 시행으로 상장폐지사유 발생 기업 증가 - 메디컬투데이 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5Ial8wQ3JZWnhiVWprVkhOMV9JUTNyZXk5Q01CMWFsbXBReURBN1pJd2xsX0VhY2JmMEN2QzFVZlJIc040bTZkLTEtVzJ6UzYtdWFuTlhsOHlHUlR1Y2l5R1QwdGh5bURtLU5MdQ?oc=5 |  |
| icfr | 일간NTN | 여전업권 금융사고 예방을 위한 '여전업권 내부통제 모범규준' 시행 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5YVW5sNE1GN19VOTFHTVd6OGxFWE04LTA1d09Id25RTVd4VVhiU2pQdlAwRGlaUklEZjRzOU5oRDZJWmdDTGJ3ckU4U3Y5Z2t5OXVEUF8tdnY1WVFHQjFaeFYzYzVxa2RjbFE?oc=5 |  |
| icfr | ebn.co.kr | 대우조선 부실감사 재발 막는다…외감법 개정안 국무회의 통과 - ebn.co.kr | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE13bFBOWEl0Q3JlUjNzd3RxUUo2WG8zZDVCbEVFMmg3ck9ONkwyUHJZNVlUY1NRYWxTNUZTYlFtSExKTm9WaTZ5VWtYLVhkMUoyZlJsTDlJeWNMVnVSTUhlbG9SMmdVM3M?oc=5 |  |
| icfr | ajunews.com | [기업쇄신]최종만 부회장 “신외감법으로 회계부정 어려울 것 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE04aDRvZjFQWkc5Tl94eFpxYmRaWFczbG5VdHBGREhIN0JaSy1MRnBqZ3hTdlpodmItZHhrR2lsRmpWRTdWdTZkQ0FYUFZkcndwNDF3QnRPbUY3d9IBWEFVX3lxTE8zdlk3LWJBOFZWZzVRbmtsWjhUNU1Sci0wazNJRVZtNDA4VXEySXBzWXhPcWVibmhGb1FDc2hBQjFpSm5PTU5BR2o2VlAzU1F4c1Y5YWtZYUQ?oc=5 |  |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 |  |
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 |  |
| esg | ESG경제 | 정부·여당 ESG 공시 입법안 나왔다…제3자 인증 의무화 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE44WUtnTkREZjU4RzdtSFZIcG1PcUo2czNDX0RKdWFITEVsZXppZDk1QU5aS0JMdHRfTVFXOGR3WjVNc3R4eVNKZU9GeXVuNVplZkFIdjhwRmhTcGVxazZxeTNDSzRZbjQ4MUZmOQ?oc=5 |  |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 |  |
| esg | PwC | 지속가능성 공시 제도 로드맵 초안 및 확정 공시기준 주요 내용 - PwC | https://news.google.com/rss/articles/CBMif0FVX3lxTE1Gd29wMWxoczQwX09wRThxRzhCam43V3VTRHp6LWFzQWgyZUdjeTF5dzJBZUJoYnlLZFdYWEZlbWVmRDNEcHM5eGVpTGhPSThiUEtkNlpBTlVVb2laR1FlSnlCa2ZBeG5uWFFvaHNfdG9LeExxeFRLc1ltdXgzcmM?oc=5 |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | 임팩트온 | 【종합】2028년 ESG 공시 의무화 로드맵…핵심쟁점 6가지 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9ERWRJb29XX3JMMmd4b2pLZU1SZmZoQURQOFZpdjZYeXlyandLUXhkdThRMDV1RUM5OUdLeDVYc3BDV2pWY3I3bHp2M3BLcW1SSnZuajBKRXZVQ05Qdm52MTg4OHVGcXozUXc?oc=5 |  |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 |  |
| esg | ESG경제 | ESG 공시 로드맵, 첫술에 배부를 순 없다 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBPX2hhTW1EMXNjREQ0VUNMX1JwMmNuWERxcm5QQ25RMkNvM0VaTXR6aGwwVmtvcXF1YnY3aWYtUGtsNW1ibFJ3QUtETlVEZ3AxU3lwU0tIam1XaHdvd3pTcXVBQ1BOYUktaWs4VA?oc=5 |  |
| esg | 임팩트온 | ESG 공시 로드맵 또 연기…국회 일정에 당정 협의 보류 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE10b2lHcFJxSk1ZN0ZNMUZFLUxzajM4XzktSUZzU1NaQ1B2WDNGX194UF9EUnVOZTJPcjBjTC1FbDI2R0xGSWFQTUc5d01xZ2NVRWZQVEwzcXlQQXM0aFFUYTJmS09iSGZjX2c?oc=5 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | 임팩트온 | 이웅희 위원, "ESG 공시 로드맵, 당정청 조율 단계"...상반기 발표 목표 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1FSV9UekJiTzFXSUd6SWYxOWpyY3RIMkFSajZFVC1GYWJhRjYtd3JCTTBkbEpQMWJkcWNpRjN3LV9HSDBCWnFlUE1BbTJpQTdGZDBfV2pwZV85SWN2YXJNN3Q1WmhaODlYYUE?oc=5 |  |
| esg | 임팩트온 | ESG 공시 로드맵 확정, 사업보고서 공시로 시작...2029년 3171개사 영향권 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9iV29YRzlVTjJNb1JmalR6LTZLOXJlajZQeDdUN016eU1SSGNFZm9pWWVLYVhZcEk4OC1WejFaODdFZzFxVlF4aXpwd3pONHVncXp1UlBBQnlZanV6S3NJR19VQk5RQjZkbHc?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | ESG경제 | ESG공시 로드맵 확정 막판 진통...발표 5월 초로 연기 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5Sd0U3WnpadDd3RUJXbGhrb001NW03SWZPYXI5SUlrX3VtVjBucGJDN1lYUU4taEpNSFZEVjVLaDJwRzNOcUwzSTBsV3JzVWoyZ01BeUp4ajhGbmxJVE9kOVB0NmpIa3RkZE1SQw?oc=5 |  |
| esg | edata.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5ud29WMHQ5RnNleWFLbDR2TFJfSzh2UXlZWjZoWndQUnp6NHI3NWJmaUlfOFgwcXFSM1liQ1E0MEZZZWhDMXRsZjhiT0g2SW91azQybGw1aGVDSUMxZ0E?oc=5 |  |
| esg | ESG경제 | [단독] ESG 공시 2028년 법정공시·2029년 검인증 의무화 법안 발의 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5IMl8tNnVMY0FDVnRMSDRSYkEwX29od3lMeXg5Q0tVX0pVbEx0VW42Z0d4TUF5elRZaG12UC1qTUlqeXB0QmFHTEs4LXpnNjluMUNPcnRERDYyQ1l5UjNLZG1DM05aTk84OC1ocQ?oc=5 |  |
| esg | 임팩트온 | 【단독】청와대, 국민연금 CIO 긴급면담…ESG 공시로드맵 전면 수정하나 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5EZEpERUZyWFJJZUd1dDY4blhENWMwajk3SU9kcGVzeDlsUzRLOG5PVkdRUTJEVnZITHNZcXZtNm1RN0l2aXpuZHQ5a25BRkExOVhMODV6czRtNjJDb2htbFJHQ3lrb214Umc?oc=5 |  |
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 |  |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 |  |
| esg | ESG경제 | 국민연금, 금융위에 ESG 공시 로드맵 '전면 수정' 의견 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9sYWtZaXA5dUczZUZJTGxWWTBuUnMzazBxLUc4cUFGTi03OFFSWFo2Yi03QWNfaVhFckhfTi1BQXUyWjNPeHpwbnA0dGRncnFDVzVKSXFnWHcwQTBXUHlvZXUySGM0VllDNnU5Nw?oc=5 |  |
| esg | ESG경제 | 'KSSB 공시 의무화 시대, 무엇을 준비해야 하나' 세미나 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE81V1p4YkEyeGp6aWFCY2lCYmcxVXNZYm5ZWEJrV21QR0NOSjZfMFN0RWgza3otTFR4ZjZzTnBoQU9sWkw5SDFkSS05bkRQUXBxY0l2LTVQaW5QbWFOR2FWcUZWVE1oSlpNR193ZQ?oc=5 |  |
| esg | futurechosun.com | “글로벌 기준도 정부 정책도 엇박자…ESG 공시 로드맵 전면 수정해야” - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBsLWxqdU8tTVotNHNXZUk4WWpOeHBhbXNqNGpQMmFaek5leGF2Qk5KelpoYktBUEpDLVlZZUJwdWZWeXR4MmtOYW1zVk03Nk45Znc?oc=5 |  |
| esg | hani.co.kr | ESG공시, 공약은 ‘신속 추진’ 로드맵은 ‘늦장 추진’ [왜냐면] - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBQR0NwWHowWHdLZ2lPVG8tdm5fcm9pRm5pc1hVdVh0S2s4U2ZnRUx0VGJ2a2Rxb0xWNjF1V0J5bWJadkdwTnVjUWJDYkNwYjJOZS1OSERWWHlwQW1oWmJwT1V0MTY5cTg?oc=5 |  |
| esg | dhdaily.co.kr | KSSB, 지속가능성 공시기준 첫 세트 공표…기업 대응전략은 - 대한데일리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1qTnFWLWFlSWx2cjVmaEswUXdpRUVlLU5BZHpTN3VlQWZWOHd4NEhqSVZxOThmRXR0eHpVbTlmcjNacFQ2RVl4Mlpmd0g3eXY4eGxVNDhzWUtTaEdCUUl3OHdNdVJfcnBHQnlr?oc=5 |  |
| esg | ESG경제 | [단독] 지속가능성 공시 로드맵 내년 1월 발표 계획 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5wNV9rc2dQMTJKQTVLcnpSbmY2R21OYjRuUzBCSjU4YnNVbGdJMUtsRm53NGlKYVZ5bXg0a05wbmlfYnJzT29UR3R3N2JHaHMxQ1ktdmVxTk5rLXBIWUdDeHJ0bW9oU0haUkliQw?oc=5 |  |
| esg | ESG경제 | 아시아 각국, ESG 공시 의무화 '질주'...한국은 계속 '헛바퀴'만 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9iT1p3aDQ1bGItZFl4NDZ4Z3QxVGtEUS0wYnpjZ1BkTmF6MF9aakdtRVpBaGdIN3dUSms2bkxKUlBjU1VkT2NUaDRpNVdEaEExdDZjWkZEQlI0RjFQS0gwZ3IwRTVpTmNHNWJTMw?oc=5 |  |
| esg | ESG경제 | KSSB “연내 지속가능성 공시 기준 제정...정부 로드맵 기대” - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBQcXVQeC1yRDJjTUtFalZtUlkwd2owdlNKbU5GQlNKWlZrVEUxOWM1WW9iNUFQbVNRZUdCRVVvanV3endMWU1IRU9fMHFIUHdnRGczbzV6eFNOX2lubE1SbEoyOWRvc0F3QkxBNA?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시기준 초안 뜯어보니...ISSB 기준 기반, 기후공시부터 의무화 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBLVlVLT1pHMDUwWVA2Nk1xMXFUNENZdzZRT2luYjdJdXdxT1ZsYkg1LXJtcEQzbE1jY3h6LWtWeHFGb3ZvWmhoQXN0OEUxeE9GcE8xWWtqc25kRUtjSU9yRThFLUpmbU53Y1dN?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | ESG경제 | KSSB 지속가능성 공시기준 초안...'유감'과 '기대' - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5IbzRUeVpVLUVnVUk4MGRxWHBfRmN2ZW0yU3VDYkxLbUdteXFPWGdVb05ueXNwTzBSS0ExSUU2V1BTd0xLYUo4eDlLVjc3LTFJS1QtQVVJNVdtZzNvcHF4UjdsVjFFUHdKZnJJ?oc=5 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| kifrs | 임팩트온 | 기후위험, 재무제표 주석까지 들어온다…회계기준원, 공시 사례 공개 | http://www.impacton.net/news/articleView.html?idxno=19406 |  |
| kifrs | ESG경제 | 재무공시와 기후공시 연계 강화...회계기준원, 기후위험 공시 사례 제시 | https://www.esgeconomy.com/news/articleView.html?idxno=15878 |  |
| kifrs | tfmedia.co.kr | 회계기준원 IFRS 20 간담회에 에너지 기업 ‘쫑긋’…IASB 부위원장도 참... | https://www.tfmedia.co.kr/news/article.html?no=204787 |  |
| kifrs | 일간NTN | 회계기준원 지속가능성기준위원회, 지속가능성 공시기준 첫번째 세트 의... | http://www.intn.co.kr/news/articleView.html?idxno=2049269 |  |
| kifrs | tfmedia.co.kr | 회계기준원 KSSB, 지속가능성 공시기준 첫 번째 세트 의결 | https://www.tfmedia.co.kr/news/article.html?no=201983 |  |
| kifrs | 매일경제 | 국제회계기준 해석委, 일탈회계 관련 기준개정 필요없다 의견 | https://www.mk.co.kr/article/11489251 |  |
| kifrs | 이데일리 | 한국회계기준원 "국제회계기준 해석위, 일탈회계 극히 예외적…기준개... | http://www.edaily.co.kr/news/newspath.asp?newsid=04060646642397208 |  |
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

## collect:tax_subject (34건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | donga.com | 국힘-개혁신당 “세법개정안 철회해야…다음 총선은 부동산 심판선거” - 동아일보 | https://news.google.com/rss/articles/CBMid0FVX3lxTE9NUjFGS2pzLXpPNHBCRjBsUWUtcXdSZ0RVajdvSDgwQ0FXNHI1Z0RtR3oxVXVMZDh0bTV3cU1rUnZ0dzczbVV2cnFmNFhjVVQ5bUsxZ2R3THdVcHdfakxNLURnWHhFbXVreGZranlfVEg1Y25NNlNN0gFmQVVfeXFMUHQzdkRLQ0YyOWs2VzNpNWtTSUxKRDBpVnNpdlVZR0NGQmpyZ2I0amtzNTBpZmZrVTI4T2FKZnJRTkVfeWJMUlgwTGJzOHJvYm9qZjd0MElTaHRRdGFVaGFCVnB3VkdB?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | yna.co.kr | 野의원모임 "부동산 세법개정안 수정해야…총선 연계 안돼" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzdXhCa01adXlFOGFCRVBMUkJIZW9EU2I3M0JjXzRsZ19Ka0tyQzlhdXhSS0NVSWR2akJlbEFkdUR3V1d6bXhqSlUtN28yTmZ0ZEJpZFRXTzdueDDSAWBBVV95cUxOT3hOTTBjTDFveG83VGYtWFdUZHRXU2Yzbk5FT0tlbUxranYxQXZnOG9nWXQ4cFMxY2Q5Vmk3Sm93aV9HVnFUY0VHWUg2cEU0V0FYd2tsajhxNEFIc3VsaEY?oc=5 |  |
| tax | newsis.com | 국힘·개혁신당 '주거혁신포럼', 재경위 조세소위에 세법개정안 수정안 전달 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBsR2hwV0w1Sm1CS1hJY2dQSU91Vk1tMEJHZEppMHRRWW5mWGp6eThtam02SDNKYkxFWWI3YU8zc2hmMnAxUlE1N2hwdzV6ZTZ1ZEZLZ3pJdUZFc19BeTQzUNIBeEFVX3lxTFBTQ3RqRHJUdkJKdERiNkRQTWhhMFZZM1gta3M5MU5MSk14Y3RRYmM5d0ZPd2hQcGRiQ3FlZG9VMjJSRlRaNDlkUlYtNkpCTVNSZTM0UEpwYk5WaWZpal9EN0RVdUNYZUEzVmtGUWtkeV9EbjVuVk80MA?oc=5 |  |
| tax | everynews.co.kr | 국힘·개혁신당 '수도권 주거 혁신포럼' 의원들 "부동산 세법개정안 전면 수정하라" - 에브리뉴스 EveryNews | https://news.google.com/rss/articles/CBMibkFVX3lxTFBFN2ZhWEk2ZTZqcnNhTWdaY0g3WDl5V09BWkkzZ0EzOWFWdVJPWDlPd1ZNUDZoUGhVSHpnSE41b3c5eWhfVUdESFlzNGhZdzh1QVJLUlk0aVF3cmZJSHNVV3c5Z3hsTnBSbWV6YmxB?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | yna.co.kr | 수도권주거혁신포럼, 정부 세법개정안 관련 입장발표 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WeXlSSUIwZUVTUEg2amFnNWJqbTRLa0prcFBodkozdVpGRzVTMW44YkVoS0haLU43TDc1Vnh1T2hQdFhCN0JtbENmRl9iNjNHYVJrLTI2Ukt4QkXSAWBBVV95cUxPM3ducDJrU2lIdTJELXlCSk5SSi1xMUx2M1dYODU4NUF3UWR6STF0d21RbWkzTjFoYlVyc2xiNE5aS28wSmczTjVuWldkM0NXWjBRMWgwRGFVUnVvbHVzTE4?oc=5 |  |
| tax | mobile.newsis.com | 세법개정안 입장문 전달하는 수도권 주거혁신포럼 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE15ZEZlZnkwSFdDUjZfT0tULUR6RnJJQmtrRC1TcDNJb3JvSjk0cTdvdTMxRWtYZWZseVNvZ1diVFU1SjBGNURLNzFodTkxMk9EbnI1WmZvNUZFN0RXWE9JQThubndCZDZsczdrU3JwNm9JOENiSUxQbdIBeEFVX3lxTE15ZEZlZnkwSFdDUjZfT0tULUR6RnJJQmtrRC1TcDNJb3JvSjk0cTdvdTMxRWtYZWZseVNvZ1diVFU1SjBGNURLNzFodTkxMk9EbnI1WmZvNUZFN0RXWE9JQThubndCZDZsczdrU3JwNm9JOENiSUxQbQ?oc=5 |  |
| tax | mobile.newsis.com | 수도권 주거혁신포럼, 이재명정부의 세법개정안 입장문 전달 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTFBsSy1rQkROS293RjhOSWt0VUhZX1VuTDRwMlJfQWk3d3lUbzR6b1Y3MjdKZTJGWkJQVVVoSFpoQXpkYWwzcjM0ZnNoYVUyZmw4UHQ4Z2o4aXNha3J1ZTBneWdiRW50YVVkeElVYVBrRzQ1V3JZRjBNetIBeEFVX3lxTFBsSy1rQkROS293RjhOSWt0VUhZX1VuTDRwMlJfQWk3d3lUbzR6b1Y3MjdKZTJGWkJQVVVoSFpoQXpkYWwzcjM0ZnNoYVUyZmw4UHQ4Z2o4aXNha3J1ZTBneWdiRW50YVVkeElVYVBrRzQ1V3JZRjBNeg?oc=5 |  |
| tax | mobile.newsis.com | 수도권 주거혁신포럼 재경부 차관에 이재명정부 세법개정안 입장문 전달 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE5BVkdQU3Zxc09DLW5VVlM0ZEU4M1phM001dW1zbmlBYzh3a0dqME1IUzBSeWFjbDVZUHRGWkExanVvNlB4YVIwQXZmc3JYenNrdGxEWmlZR3prV09fS0FJYUU0THZkZTVRV2I3UWplRkNPV0pvWWF6YdIBeEFVX3lxTE5BVkdQU3Zxc09DLW5VVlM0ZEU4M1phM001dW1zbmlBYzh3a0dqME1IUzBSeWFjbDVZUHRGWkExanVvNlB4YVIwQXZmc3JYenNrdGxEWmlZR3prV09fS0FJYUU0THZkZTVRV2I3UWplRkNPV0pvWWF6YQ?oc=5 |  |
| tax | newsis.com | 세법개정안 관련 입장 밝히는 박수민 의원 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1zU1RabUZhMDVpYzNPUG8wXzk0UEtlSXp0d1FCR3hxSk5SQ080OG50SG14VElTWGlPQ3QxZWVSb21EWkNxdjd0dHNIaWFwNFNraDl5V1dRTkYweGFDb292cQ?oc=5 |  |
| tax | mobile.newsis.com | 이재명 정부 세법개정안에 대한 입장 발표 기자회견 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE9RNUVkeUJpOTA5UVoxM2Q3UHdjTEs3Y0ZBT1F3YUdSb0V3cjd0b3lvd0dlM2pRZHF1eWNKN3ZCX292TjU5WkpzTEczemlrbVdKYW90My1wWnhEQnJhVzBPTE8wVDQwYnFoeXJUZUpjc0NDZVNVaTZvMdIBeEFVX3lxTE9RNUVkeUJpOTA5UVoxM2Q3UHdjTEs3Y0ZBT1F3YUdSb0V3cjd0b3lvd0dlM2pRZHF1eWNKN3ZCX292TjU5WkpzTEczemlrbVdKYW90My1wWnhEQnJhVzBPTE8wVDQwYnFoeXJUZUpjc0NDZVNVaTZvMQ?oc=5 |  |
| tax | hankookilbo.com | 野, 이재명 정부 세법 개정안 비판 "다음 총선은 부동산 심판 선거" - 한국일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9vNWpPeUZmQTVWTEhvMDBWY1REc0FuU2w2c3BVRWdqZi1hTnY1LS1nUVdPYU9XcjlSanJTd0l6TjNOZDlfQ0g3b2ZzR0FFZGI2V1Z0bEwyZThNU2xmalp0UzlfQkZ2QXZDRkZNaHVn?oc=5 |  |
| tax | pressian.com | 익산참여연대 "정부 지방교부세법 개정안 철회 촉구…지방과 충분히 협의해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTE0tTFE0Nzd0b0stb1gyNDFJU3hiMllsR2xxdl9KYV9LWi1DWGtLYS1waHo5U0dZbzhLY2tzdU1fblp6RnQ0TTZndGFzOHlxNXFpcjBMSUs0Yl9UN0ZHWDA1bFVxYWlxZmtXdVEw?oc=5 |  |
| tax | sejungilbo.com | 국민의힘·개혁신당 수도권 의원 모임 “정부 세법 개정안, 국민 이사 발목 잡아…4대 원칙·8대 수정 요구” - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1GWWZObzhTMTA5b2lQbjdNQkFZNTQ1cmlDeVVWbEZHWVk3Y3JjNmk2Nl9MbTFyOG5UcTdNYm9pd3V2TWQ5TklVRVhRTzBhaVZ0b2J4RTl5TGczWVJJcUwxQWEtSFRvcVNCaXBVUg?oc=5 |  |
| tax | news1.kr | 수도권 주거혁신포럼, '정부 세법개정안 수정 요청' - 뉴스1 | https://news.google.com/rss/articles/CBMiS0FVX3lxTFB0OTdJOTBZVGs0VTF0cmdIVXkxWGFHUE5Vb1JGSXZ4RkcxQ21XTy10QVl1Z0RJYmZRS2hILVA4S2pYZ1pUb0Z1bWhPSQ?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | news1.kr | 재경위원장에게 정부 세법개정안 수정요구서 전달하는 박수민 의원 - 뉴스1 | https://news.google.com/rss/articles/CBMiS0FVX3lxTFA3QmpNY1VFMklHZ2ZQdkpKRlc0Q1VHWFpvcjdnWjd5c29nRlVGcVZGRTRyTXV5SzE0cENMVzhDUU9BaDV2OEpsSVoxaw?oc=5 |  |
| tax | newsis.com | 정부 세법개정안에 대한 입장 발표 기자회견 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5tRERrc0RPWUs2OERhbzV3V0R4V3ppMEpfSEF0MklRUzAtMEVveGw1VzJlTXJyV3RvQkZFa2N5bmlaZXFlUHdtNnc5QXU2Rjk2RjRTZHd3MkpwNFpxcHNUTA?oc=5 |  |
| tax | news1.kr | 세법개정안 관련 입장 밝히는 수도권 주거혁신포럼 - 뉴스1 | https://news.google.com/rss/articles/CBMiS0FVX3lxTE5FS2Q2UHg4NHRralR1ZHplQnVNT01meXpjc3N5TjlwcGgyYWFWQmZCaU5UdzZmYkhkTzdDZ3hwUXZTQnBXamd0WnlvVQ?oc=5 |  |
| tax | 한국세정신문 | 올해 달라진 종합부동산세 법령 내용은? | https://www.taxtimes.co.kr/news/article.html?no=277928 |  |
| tax | naeil.com | “미국-미국령, 세법상 다른 국가” | https://www.naeil.com/news/read/610044?ref=naver |  |
| tax | 조세일보 | 전기차 추가 검토, 비거주 종부세 차등은 고수…정부 세제개편 '촉각' | http://www.joseilbo.com/news/news_read.php?uid=580352&class=7&grp= |  |
| tax | dream.kotra.or.kr | 모로코, 2027년 재정법안 발표, 수입 선납금 도입 등 세제 개편 추진 | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=80&CONTENTS_NO=2&bbsGbn=242&bbsSn=242&pNttSn=245194 |  |
| tax | newsnjoy.or.kr | "법 지키고 싶은데 방법 모르겠다"…개정 세법 앞 해외 선교 현장 고민... | https://www.newsnjoy.or.kr/news/articleView.html?idxno=400920 |  |
| tax | goodnews1.com | 개정세법 시행 9개월째…해외 선교비 집행 여전히 난항 | https://www.goodnews1.com/news/articleView.html?idxno=466437 |  |
| tax | thepublic.kr | [집중분석]민주당도 우려한 부동산 세제개편…장특공제‧종부세등 '도마... | https://www.thepublic.kr/news/articleView.html?idxno=328668 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |

