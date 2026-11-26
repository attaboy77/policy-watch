# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-26 12:48:11 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1552건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:company_event | 2 |
| excluded:company_self_activity | 5 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 3 |
| excluded:foreign_news | 1 |
| excluded:foreign_tax | 18 |
| excluded:industry_specific | 8 |
| excluded:manual_id | 2 |
| excluded:no_regulatory_signal | 82 |
| excluded:related_news_attached | 1 |
| excluded:similar_news_merged | 36 |
| excluded:smb_only | 4 |
| excluded:standard_setter_governance | 1 |
| collect:event_announcement | 46 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 280 |
| collect:noise_keyword | 2 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 210 |
| collect:out_of_window | 145 |
| collect:tax_subject | 34 |

## excluded:company_event (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | GRI, 금융업 공시표준 3종 확정…대출·투자·보험인수 영향까지 공시 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBpcXlqWEtjdEg1SjU2LThva1BfVjIxNFY1dWhaWVpEODJxY1ZWOU9ZYTNvRnNYS09PMF8xenhvOXZ5am85alI4clBuWHJmVUZ5TDhvendLYlpNWHdmb3FPVkk0ci1JaEsyWEE?oc=5 |  |
| tax | financialreview.co.kr | [강동형 칼럼] 대손세액공제, 부도보다 대손확정일이 가른다 | http://www.financialreview.co.kr/news/articleView.html?idxno=46483 |  |

## excluded:company_self_activity (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | paxetv.com | 금호타이어, 지속가능성지수 4년째 정상..."ESG 공시 역량 강화" | http://www.paxetv.com/news/articleView.html?idxno=287805 |  |
| esg | m.ekn.kr | TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1ZRHhKeVl5Yi1rVTdJcGwyQ0dnUUFyR01SZGQtX252WTRVaTU1NEVDQVFmSncwcHYtMDZwbW1qUmhjN052U1IzSks1Ym5ISXhYWHNkdGo5bHg3Qzg?oc=5 |  |
| esg | zdnet.co.kr | 코오롱베니트, ESG 공시 의무화 앞두고 통합관리 사업 확대…공급망 실사까지 지원 - 지디넷코리아 | https://news.google.com/rss/articles/CBMiVkFVX3lxTFBWM0xPLW1iR3p4UmM4NkgzZTk5U1cxY0VoamZ0LWZsQ0JwM3ozdTBnbmQwamt2SDNpZy03VHVCOTkzeEhwWHdzblNXcU52dGxtY0Q5Z3VB?oc=5 |  |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |
| tax | sejungilbo.com | 김주영, 조세특례제한법 개정안 발의…2031년 말까지 연장 | https://www.sejungilbo.com/news/articleView.html?idxno=61103 |  |

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

## excluded:manual_id (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 공정한 표시와 IFRS 회계기준서의 준수 IAS 1 ‘재무제표 표시’[IAS 8 ‘재무제표의 작성 기준’] | https://www.kasb.or.kr/front/board/View016002.do?siteCd=002000000000000&seq=40688&ctgCd=016002&replySummary=Y | 결론이 '별도 기준 제정 없이 현행 규정으로 충분' — 바뀌는 게 없음 (KASB 질의회신 '공정한 표시와 IFRS 회계기준서의 준수', 10/30) |
| tax | 일간NTN | [국세 예규] 상시 주거용 임대 오피스텔 양도 때 부가세는? "사실판단 해... | http://www.intn.co.kr/news/articleView.html?idxno=2053355 | 주거용 오피스텔 임대·양도 부가세 — 제조업 법인과 무관 (일간NTN [국세 예규] 상시 주거용 임대 오피스텔 양도 때 부가세는?, 11/20) |

## excluded:no_regulatory_signal (82건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | KSSB “EU, ISSB 공시 인정하고 필요한 정보만 추가해야”…해외 공시매체 인터뷰서 밝혀 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1QTEJtQU9nQkpqX1BCR24zM1RuQlNhNGJqQXlTUmpCNWJtNVh0VkM0TS1TbFJmYW5GbHpGNWVzbTdSMUVJSElhOFk2LURqX1B2OWNhby1aTHRqWE5oS0FwazFqNWxRb1pVSGc?oc=5 |  |
| esg | 임팩트온 | 한국 기업 ESG 공시 아태 2위…자발적 공시 평가 반영하니 1위 | https://www.impacton.net/news/articleView.html?idxno=30817 |  |
| esg | 임팩트온 | GRI, 식음료 산업 전용 공시기준 만든다 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE84ZFBJaEdtUlNMazEzdVRFN241MXNlMTRkZUtucld6Ry0xRkROaXlYcjhtdUQ4amE2MGczNDI5SXRhNmNmZXp0X0ZmaFZwRDRRa2hDMHA3RURNUEpJWU13SzYtTmh5WjZ0Z1E?oc=5 |  |
| esg | 임팩트온 | ISSB, 22일 자연공시 초안 공개…사업장 위치·가치사슬까지 평가 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5ibFRYdXJrMWtJRnhPUW1NTUR6bEZ1OWZ1ZUp4UmZIZ3hYNFUwZW5DUk4yZEhUSk5MVTZNdnQzaC1zajl0TzA5Tm9OTjI2SEdKaVE4WnN5NWFrVzRDYlp6MmtzbW5sU0dCX1E?oc=5 |  |
| esg | 임팩트온 | ISSB, 자연위험 노출 자산 금액·비율 공시 제안…공급망 위치도 반영 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5CaDVvOUluQ2JzNGRGNUxQaWctYVY0eEdyS0ZWTXQ3S3d6RmlZaG1CaWdJTkh6NFVuQktFYWZ5UUdVWnl2eWw1VGJDNjFELU9LTy1Ua2ptRFFabVR3aXNpLWhxQ3lsRFFla3c?oc=5 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있어야" - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1wbl9FYkhYT2Q4MXJBcnRNSTJEb2ZrNnZEUXdob1FWRUdqcGdwd2JodXNrQXdGV25UNWVZeC1ZSDBxLUZFYWRRcS1zMzcwb19SbVROYmdIVERrRkZmYkRSQ1FhaHBsQk5lNEE?oc=5 |  |
| esg | 임팩트온 | 스코프3 추정치 줄인다…에코바디스, 공급업체 실데이터 연동 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE80VVdfcHFzTXVLN1JTb0pZNk44cXQybm1wZ1UyeEluSEx3TzBabG0zUmhfTFd3T2hNQlJoS05PZXFBb3Q0UzV0Vl94Q1VkTjhFbEh6TVcxTE5WbkRTRldMM0VLcEhtWUdJZmc?oc=5 |  |
| esg | CPA뉴스 | 2028년 시작되는 지속가능성(ESG) 공시 제도화 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9YWWlTdzE5aE13VmhNQk4yZUJtZ0c1OVFDSzEzTFdlTDM3WnlMTHUxVzVPMVdtTTd0RHNNUko4alpKZXJFcmVlM2x6elFHTmp0TDIzVjVERjdScWk4U3Uza2htRTJuNXBz?oc=5 |  |
| esg | 한국경제 | ESG 공시 표류와 RE100 위기…한국 경제 골든타임은 지금[기고] | https://magazine.hankyung.com/business/article/202611172333b |  |
| esg | kpenews.com | [ESG전략] 사회공헌 프로젝트 인정 한화호텔·최신 ESG 공시 기준 적용 ... | https://kpenews.com/View.aspx?No=4328948 |  |
| esg | netzeronews.kr | 'ISSB 공시기준' 50개국 확산…한국 2027년 적용 - 넷제로뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9NNU5EaEhpSUtyOG9FYzdJcWQ5MGtod0xrQkR6WnoxS3NmenRxVkU3T1kxNHE1NzB0dWFJNk81OUpsbXJDV0tPNFhKelgwdEZfWjFob1VHN2tXNzdhTFBFSzA4UFpnMVVsT0JR0gFuQVVfeXFMUDlfbUpBRmNsNFRkOG9HUVFGemp4bzN0eUt5aWVac3NzTEZmUnlGc0xBSERjUG1uT0txZ0pBMHB3RXFsX3hwb3ZJbGJKZkJwLVdhNmtYbV9qeXhEcnZVNkE2MHVReG5RbVVscEdsdGc?oc=5 |  |
| esg | energydaily.co.kr | [초점] 환경정보 공개가 '기업 경쟁력'…ESG 공시·EU 공급망 규제 대응... | https://www.energydaily.co.kr/news/articleView.html?idxno=205428 |  |
| esg | biztribune.co.kr | 교보증권, ESG 성과 잇따라… 지속가능경영 체계 고도화 | http://www.biztribune.co.kr/news/articleView.html?idxno=363157 |  |
| esg | livebiz.today | 금호타이어, 지속가능성지수 4년 연속 1위...ESG 공시 투명성도 인정 | https://www.livebiz.today/news/articleView.html?idxno=206868 |  |
| esg | kdfnews.com | KB증권, ESG 공시체계 개선 성과…지속가능성보고서상 2년 연속 | http://www.kdfnews.com/news/articleView.html?idxno=191429 |  |
| esg | newsprime.co.kr | 'ESG 경영 내실 다진' 정몽진號 KCC, 지속가능경영 성과 가시화 | http://www.newsprime.co.kr/news/article.html?no=756393 |  |
| esg | viva100.com | 과천도시공사, ESG 공급망 실사 2년 연속 최고등급 S 획득 | https://www.viva100.com/article/20261125500906 |  |
| esg | joseplus.com | 회계기준원, KSSB 공시기준 파일럿 테스트…전문가 TF 논의 착수 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE1RaUpIeDFhcmlxZnNlRzdmaGpSQlVFSmNZVW5SZEE1a3JEQVEtQzc0MGJBWlg4dVRiSF80ZmREakM4NGVqbTJYcFhQNURTVV9DZ0J5T3JBd2TSAVNBVV95cUxQVXlNZWU5R19CVWs4MUZ3S3lnTEhGRGxmTlZCcXcwM1I2RkpwMWhDN2x0TkNkTlhyaGdKZ0FoZmU1T1BxRElhZ1N3M09ZaTJqTDAzYw?oc=5 |  |
| esg | fairn.co.kr | BSI 영국표준협회, 지속가능성 공시 대응 세미나 - 공정뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBwelNZa29VbG4wQ2ItN3hhemZZQk96bmVOMUloemI3bGp2TXBtYnhLMnc3OEtlbC1PMmM4WUtzRUZ3TmJUQmU5bGJ2cHl4bm5WZkswTVplc21mbk91dVI3S1ZUM09TdVhjTmc?oc=5 |  |
| esg | netzeronews.kr | 글로벌 금융기관 15곳, ISSB에 '자연공시' 독립기준 촉구 - 넷제로뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBWSU1hS3pCWXdscVV2YWZpVnlUNDNxRElVemdIeC1ZWWhWMnc4cGJEaDFYUkpyZHM5MGlGM2dGTEFvREYzUV9XbHFyZ0sxNUJXbFVpZ0xPSmdCUk5ONU9rODB0MXF5RTVrbkHSAW5BVV95cUxQQ2F5ZmhEaVFoZkNzSWpPUGtMM3NoYjdMTGYzQXE5LUFPRkFqa2t5ZU5EZTRCVXNwdzRXeXl5SmQtVFBEbzJfeUxmSURiSEdwZ3dFbkViMFBrdV9xbFJZYVV1MEhkNU5PYmFpNmJOdw?oc=5 |  |
| esg | hellot.net | [ESG 칼럼] 2028년부터 본격화되는 지속가능성 공시제도, 지금 무엇을 준비할 것인가 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFBjZ0hCNjdsZ18ySnhycVRpbW5jZk1CVkZrZzVVMnQwdUtNRW1PTjZEMjZDSGZCbXJEQTh6cWhfUmkyNWI5cHFNejczel9GVFpaMkhQWm5sN2l1RnRhemdR?oc=5 |  |
| esg | outsourcing.co.kr | [기획] ESG 공시, 대기업 보고서에서 협력사 장부로…아웃소싱 기업도 데이터 준비 서둘러야 - 아웃소싱타임스 | https://news.google.com/rss/articles/CBMickFVX3lxTFBHQjFYQllHZDR4OFJYT0VOX0hCMjJqUVphZ2RCanhjNVQwUDVQNXNhR01hWUJKOWw4b2lXdFBHN2tQeF9IU281cDBmVU5EX3RidUpWXzZWdVo2QlRjZ2dqU0gyRWxqSURoUkxSNWlKQnpadw?oc=5 |  |
| kifrs | 조세일보 | 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 | http://www.joseilbo.com/news/news_read.php?uid=580131&class=10&grp= |  |
| kifrs | 일간NTN | 한국회계기준원, 투자자 전문위원회 확대 | https://www.intn.co.kr/news/articleView.html?idxno=3000418 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑨] 손익 분류 개편, 현금흐름표는? - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5kYi13cTFSSkpCS0VXWXdpMHBNdkJsMkEzR3ZuSjBvWG9iUkpnRXJxNnJnNllROGhOZWlVTXJ6QXRZU3ZRZ2U0d3h1UGZNYjIwbXdobGpsVUxhcDFjbkZPT1NNbHdCM2xD?oc=5 |  |
| kifrs | 한국세정신문 | "재무제표 정정 또는 고의·중과실로 손실 내면 이미 지급한 성과보수 환수" - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5yN0FYRC1aQ3dWWHFDanRvN3pudVRibXBrYk42bDVpZ3hrZnkwMGlGYkZFWXpGZlQzNGpYQTZYeXJnSnZ1ZkRsdHZaMEpkS0ZMRUg3Y1F6ZnRlSGtDQ284MmVMTTE?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 머니투데이 | "삼성전자 700조 저평가, 손절 말고 버티세요"…재무제표 뜯어보니[부꾸미] - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9pRkMzckl3eFF6Q3dvZEpsMUF3SnBMY0VuM08wR25IdFlIUVJJNV9jOUFSckVGbUdWck52QmZ2cER6SWZZblozbkhhNkNFc1ExTDFxOVlJYzY5ZEQ0X2Rpcmltenhta2t00gFuQVVfeXFMUFpSSDdnYlpoZWNObVJTdkVCYUVsSS1NXy1GZDUzUl9iV1BmRTJqOUFuejBWUkw0a01yeEo0SlYzT0pWaWVlcThWRWF4dVlRNlFrUHdUUkZjeVlaeFpxVDNUanpHTDdmbHZWMzJwUkE?oc=5 |  |
| kifrs | 서울경제 | 금융위, ‘매출 허위 계상’ 피델릭스에 과징금 부과 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5CYnJPTW05UFhwTWVISnpoMkl3dURJQTlKdWVXOTAzQkd5Z1NEYUE3WnVXdG9lOUxuNDB2SVZpLXMteWozcFRJc3JUX0UzWEF2TWfSAVNBVV95cUxQcDZyTURiU0lNQUtxalJ2S0FPSkJ1cDJQUTJJOUtPanNoT203TzFfR0VjNEE4dC10ckdibG5uSVJTZ1R3aXZwckVGN2trWXJKa2d2cw?oc=5 |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성 공시기준에 투자자 수요 반영…전문 위원회 확... | https://www.tfmedia.co.kr/news/article.html?no=209073 |  |
| kifrs | biz.chosun.com | [단독] 10대 그룹 CFO 내달 회동…국제회계기준 발언권 확대 논의 - Chosunbiz | https://news.google.com/rss/articles/CBMihAFBVV95cUxPbm9pdFYyUTV6YUU2ZkpEdVFVNmwyOXcyeF9TV3dMazRZdTRsMEJvYVNrSlJpSG5oODZkb2lJQ0tsRGNjbktXXzZkdlJTalNiYWJBVDhrUmktM3FUT2k0eWJ4SHJBdHNCdDVnNmUtUklSWnVsOU01X1NLcjVqQmhiRHFZNk4?oc=5 |  |
| kifrs | newspim.com | CJ프레시웨이, 공정위 정면 반박...쟁점은 회계 처리 아닌 납품 연계성 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE9LYUQ3QjdPWE1FM0RIYUttT01IZ3B6end4b3R0dmZBRnFJTmZ6TWdaNlFqUmhLTnhRZEl1clZwVm1tZTFGeTBlNmJMYzdsZFNSekVuWGpqZXQwSmct?oc=5 |  |
| kifrs | datatooza.com | 허브 그룹, 신용계약 4차 수정안 체결…미제출 재무제표 제출 기한 내년 1월 31일로 연장 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5lb3lIXzAtZ1kyRFJpczNlYnNRamZGTEQzS2t2LTR6ZzZRRjdoNjVQamV6WjhrZGprTGRXZi1aelRGQ2FBaDRvai1oY21DdU9fSEZKNU1kT3pOaTllajRxWjlQeWlGRnk1c1FvOWxCdHpvbWc?oc=5 |  |
| kifrs | datatooza.com | 블레이즈 홀딩스, 2025년 및 2026년 재무제표 재작성 결정…중국 매출 재검토 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9hM3FVTG5YU2h2YnVoQ2VPZk5CVlFpdGtfOGdGQnAxMkNyekZya19Ick1KbUI2UFJBWnNwTjhwcGs1Z28ybXlSTFRJR0R0LWhkdmdzUm1HdG9xUVVva19rTTFabnpMTmJkVlh4M2hXX3FCUVk?oc=5 |  |
| kifrs | newstomato.com | [IB토마토](공시톺아보기)값 오른 땅만 재평가?…회계기준이 막는 이유 - 뉴스토마토 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBQTnNWcTRNVGhCcWJST1h6dmM0d0lnUTU4N0tDZl9ycFAyQnZZOUItVHNKazROenJRUHZrWHg4LUc5YlY2X3dkNWRYTHd3YlVFNmlxU0JFZFlET1NydUNaOA?oc=5 |  |
| kifrs | tfmedia.co.kr | [2027 예‧결산포럼] 박성진 연세대 교수 “예‧결산 분절 문제, 전망재무제표 통해 같은 언어로 소통해야” - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE0wUk9xOWc1WHJpTXlHOGFvYXQtREVwVThfR25OXzhHbTZ0b1N5bmhsSTdNVXNHc3ZlUGVsUlJIWjVZNG4tNFNGTElyLUtFNm96SmZhVTlQSEFvazBoLXFpV2Nidw?oc=5 |  |
| kifrs | hidomin.com | “좋은 회사는 재무제표부터 다르다” - 경북도민일보 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9hRXJJZDlCZVBjOGMtNGpwLVY3MEdteUpzeUlFSkZJS2FodWNnckhCaXVjRWpqdDNPSnNVU2dUUExPek16TUNCRFcxcWhhZ29ldnRja1VXQVBud3hTNDdLdWNRVVdjbWZMSmc?oc=5 |  |
| kifrs | asiae.co.kr | 금융위, '회계처리위반' 피델릭스·현대회계법인에 과징금 등 부과 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFA3YXU3VWg1akMyeWwxVkFRZmtBbE5iUDQ0NmNvNTFmWmsxbFpYb2tYTXd5NkdvbHZRZ2FaRS1Zc2ZEYW5hbENjTFBqMldBYV9rQUZ2clM4OTN2VG5iMkdZYQ?oc=5 |  |
| kifrs | livebiz.today | [재무제표 이야기] '1조 달러'로도 살 수 없는 SK하이닉스 - 생생비즈플러스 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrSktGcWF6RjB2WXBqWVM0UzlOYUU0Yi1UcnNwVGpnUkJ5SXlVam5RZlRadGh1UFg0SDd3LUszczZWMWRRV28waTIxVnhiNHppdW45dEk1TTRiVkRtYlpKb2Q0cGFTU2JsY0VvMA?oc=5 |  |
| kifrs | opinionnews.co.kr | 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 | https://news.google.com/rss/articles/CBMickFVX3lxTE9WeVlZRG8wdjhmVjFaMHYwQjNRcS1HbGhGc0RfQWF3eWJhb2FreXd2WjBtNDF6Q3pBZHdsT2Rlb1VQVWdkczF2ZDJXMkQyMzJSR0FtR1lXTkI4cmtlM090V2RMQWVBcndYX0YwcHhBb1hzQQ?oc=5 |  |
| kifrs | hansbiz.co.kr | [신간] 좋은 회사 재무제표/월급쟁이 맞춤형 ETF 포트폴리오 등 - 한스경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5mSmM0RGZra3FFejFuVThXZ0o5RWd5R2hDbTJjSGwxbURqNy05UFI0ZjZUbk5BdlFwR1lHQVprNURNdWJZUXNUNThNdnFUUXoySHh6amJTMnAySVJOV2cxV1plR1U5WmlET01B0gFvQVVfeXFMTkRsU1pfaUNWNmhnTVdTdEZoV3B0cmk3VFpiRHV6TmZ2SHJCWUtaQ1lrTXRVbVdzdjVLM1FWdTlmWmFYSmt5ODRaemFaWFVUYlNVY1g5RjVvR2p6Nk1xM2Y4b0NPc0d6OEpEazNQX25N?oc=5 |  |
| kifrs | enewstoday.co.kr | 상장협, 회원사 회계담당자 대상 회계 이슈 강연 - 이뉴스투데이 | https://news.google.com/rss/articles/CBMicEFVX3lxTE92T0RlWXlrRTZSUmpMSnlQdzdGZDIzSUY2U1ZabER1NThGWVhQZzI4ZmtqTllxY2U4c1c1ZGpRR3ZTZVVkVEFlYXhBQXYzSmxTUTdrc3ZCRVc5NTYyR2ZjMGtzR3UxVTJiVW90NE9GelDSAXRBVV95cUxPd2ZHcVJ0czIwMTVKYkgxVjJkbEE1RmJCd18yeERFSnJUX2RpZGlnYUk0ZzJIX196YnNzcGVYYmtDcWpEblFuZ3dsQnpCUnYtU3ZOOFdhVzM5RUw2d2VGdmxRd1dsLVVTV1hwaVRYSkx6OUtfNA?oc=5 |  |
| kifrs | fairn.co.kr | 피델릭스, 5년간 150억원 허위 매출…외부자금 조달 위해 화장빨 회계 조작 - 공정뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5UMW9OeHpJMlFfS1lja1pwQUljbTdNSzRnLVVVYWZOeE9pR0RUUkxSV3NYUzRXUWNMb3FqUHJ3bmtadnZ4ZTJqX1AwLUFwMHhZLVA5S243ZnhTNHFtcFo1N0toMmRYbWNy?oc=5 |  |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| tax | 한국세정신문 | 조세심판원 "재산세 납부 의무자가 반드시 종부세 납세의무자는 아냐" | https://www.taxtimes.co.kr/news/article.html?no=277875 |  |
| tax | 한국세정신문 | 111일 만에 전입신고…실거주 확인 땐 취득세 감면 | https://www.taxtimes.co.kr/news/article.html?no=277876 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(67) 대도시 내 부동산 취득세 중과, '형식' 아닌... | https://www.intn.co.kr/news/articleView.html?idxno=3000354 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(64) 토지의 무상사용과 재산세 비과세의 실질 | http://www.intn.co.kr/news/articleView.html?idxno=2054488 |  |
| tax | 서울경제 | 승용차 개소세 보전 예산 ‘0원’…국내 생산 세액공제도 공회전 | https://www.sedaily.com/article/20119059?ref=naver |  |
| tax | 서울경제 | 與, SK ‘트리니티팹’ 지원 기업 법인세 감면 추진 | https://www.sedaily.com/article/20118946?ref=naver |  |
| tax | 파이낸셜뉴스 | 정부 제동에도… "전기차 세액공제 없으면 싸울 무기 없다" | https://www.fnnews.com/news/202611251819579521 |  |
| tax | 매일경제 | 법인세 늘고 과징금까지 … 금융지주 비상 | https://www.mk.co.kr/article/12211463 |  |
| tax | sejungilbo.com | 이건태, 도시철도건설용역 부가세 영세율 2030년까지 4년 연장 추진 | https://www.sejungilbo.com/news/articleView.html?idxno=61246 |  |
| tax | newsis.com | 여야·업계 이어 산업부도 전기차 생산세액공제 요구…재경부 막판 고심 | https://www.newsis.com/view/NISX20261125_0003883450 |  |
| tax | metroseoul.co.kr | 전기차 국내생산세액공제, 국회서 '갈팡질팡'…중국 추격에도 지원 제외... | http://www.metroseoul.co.kr/article/20261125500360 |  |
| tax | newstomato.com | 대법, 해외 세액공제 기준 제시…"영토 아닌 과세권" | http://www.newstomato.com/ReadNews.aspx?no=1321769&inflow=N |  |
| tax | metroseoul.co.kr | 송치영 소공연 회장 "신용카드 매출 세액공제 축소, 벼룩 간 빼먹나" | http://www.metroseoul.co.kr/article/20261125500388 |  |
| tax | sejungilbo.com | 김석기, 게임물도 세액공제 대상 포함 추진…비수도권 제작 시 공제율 ... | https://www.sejungilbo.com/news/articleView.html?idxno=61213 |  |
| tax | sejungilbo.com | 사무장에게 상호 빌려주고 세금계산서 발급한 회계법인…심판원 "가산세... | https://www.sejungilbo.com/news/articleView.html?idxno=61223 |  |
| tax | fieldnews.kr | [단독] 국세청 조사대로 법인세 낸 인천공항공사, 4년치 환급 거부 뒤집... | http://www.fieldnews.kr/news/articleView.html?idxno=33316 |  |
| tax | updownnews.co.kr | 기아, 현대카드 포인트 부담분 부가세 환급 불발…"결정 존중·소송 취하... | https://www.updownnews.co.kr/news/articleView.html?idxno=319665 |  |
| tax | sejungilbo.com | [판세] 과세기간이 다른 여러 국가의 소득, 외국납부세액공제 계산방식... | https://www.sejungilbo.com/news/articleView.html?idxno=60678 |  |
| tax | dnews.co.kr | 도시철도 영세율 연장 입법 ‘잰걸음’…JTX·수도권서남부선 세 부담 ... | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202611181437550170654 |  |
| tax | news.dealsitetv.com | 中 전기차에 안방 내줘…세액공제 시급 | https://news.dealsitetv.com/articles/178820 |  |
| tax | koit.co.kr | 정보보호 투자·인력 채용에 세액공제 추진 | https://www.koit.co.kr/news/articleView.html?idxno=209966 |  |
| tax | econovill.com | 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 | https://www.econovill.com/news/articleView.html?idxno=757588 |  |
| tax | news.ifm.kr | [인터뷰] 추미애 경기지사, 재정 위기 돌파 총력…지방세제 개편·교부... | https://news.ifm.kr/news/articleView.html?idxno=484643 |  |
| tax | nocutnews.co.kr | 300조원 보조금 받은 中 전기차…한국도 세액공제 절실 | https://www.nocutnews.co.kr/news/6608058?utm_source=naver&utm_medium=article&utm_campaign=20261117133938 |  |
| tax | sejungilbo.com | [판세] 사업 관련성 없는 지출의 매입세액공제 여부와 부가세법상 '수입... | https://www.sejungilbo.com/news/articleView.html?idxno=60677 |  |
| tax | sejungilbo.com | [절세톡톡] 일시적2주택 취득세, 용도변경도 종전주택처분일까요? | https://www.sejungilbo.com/news/articleView.html?idxno=61088 |  |
| tax | fieldnews.kr | [단독] 하나투어, 항공권 부가세 환급 놓고 국세청과 공방…조세심판원... | http://www.fieldnews.kr/news/articleView.html?idxno=32758 |  |
| tax | the-today.com | 미국 보수 세액공제 막힌 구본성…쟁점은 근무지... 왜? | https://www.the-today.com/news/articleView.html?idxno=93441 |  |
| tax | incheonilbo.com | 여야, 앞다퉈 입법…소방·지방세입 확충 구체화 | https://www.incheonilbo.com/news/articleView.html?idxno=1336375 |  |
| tax | sejungilbo.com | [절세톡톡] 매매계약에 따라 상가로 용도변경후 양도한 경우 부가가치세... | https://www.sejungilbo.com/news/articleView.html?idxno=59962 |  |
| tax | fieldnews.kr | [단독] LH, 서울시에 옛 서울의료원 부지 무상 제공했는데 재산세…심판... | http://www.fieldnews.kr/news/articleView.html?idxno=32880 |  |
| tax | fieldnews.kr | [단독] 경기주택도시공사, 공공임대 지으려 빈집 철거했다가 취득세 추... | http://www.fieldnews.kr/news/articleView.html?idxno=32624 |  |
| icfr | 파이낸셜뉴스 | 한국금융인재개발원, '회계실무자윤리인증'으로 내부통제 뒷받침 | https://www.fnnews.com/news/202611251554056091 |  |
| icfr | news1.kr | 최운열 한공회장, 세계에 신외감법 성과 알려…"韓 회계투명성 껑충" - 뉴스1 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE9ITUEzOUMwcWJBVFF4cWRyT2NmZ2xKeHh1V2o0RVhVVmF6T3RkYUxzMGlCRFVtZ0pqNkdMV1hpUTdRaWpCOXVIc0lQY0Q2NUZCcHRoR3pCdnZNTkVyZFpR?oc=5 |  |
| icfr | lawtalk.co.kr | 회사 재무제표를 부풀렸는데 외감법 위반으로 처벌되나요 - 로톡 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SNHVGNVhqcF9pRjBSSFEtUzNPWWtJQldRYVAyY1hXZW1xaFB3ZWdKd1JHcXhXQ2YwQWU4cVBnWXNPcHZwYlhmU3NMWk9fd2M?oc=5 |  |

## excluded:related_news_attached (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 관련 보도로 붙음: 2027년 K-IFRS 제1118호 시행, 준비상황을 점검하세요 |

## excluded:similar_news_merged (36건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | sentv.co.kr | 금호타이어, 지속가능성 평가 4년 연속 1위…ESG 공시 역량도 인정 | https://www.sentv.co.kr/article/view/sentv202611250120 | → 대표: 한국 기업 ESG 공시 아태 2위…자발적 공시 평가 반영하니 1위 |
| esg | m-i.kr | ESG 공시 의무화·탄소 규제 대응…대·중소기업 공급망 상생 해법 모색 - 매일일보 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MZUlrWUhhZjZmenNFXy16Nko2cFJmc0J6WW9fOWlNM2t5V0xfWUM2NmZ6ZG9NOF9sWTFyY2Q0VEhLSVR2eWpRcWNzY3dVX2Q4dTNqMlYtSlgxeHg4aFIzV3hPTXY?oc=5 | → 대표: 정일택 금호타이어 사장 "ESG 공시 의무화 선제 대응…데이터 관리 고도... |
| esg | m-i.kr | ESG 공시 의무화·탄소 규제 대응…대·중소기업 공급망 상생 해법 모색 | https://www.m-i.kr/news/articleView.html?idxno=2023645 | → 대표: 정일택 금호타이어 사장 "ESG 공시 의무화 선제 대응…데이터 관리 고도... |
| esg | edata.ekn.kr | ESG 공시 의무화 코앞으로…기업별 데이터 관리 ‘제각각’ - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE4tMXlWRVBfMUpGeEtzWDZ3RjNjV2VRd2lyRThnVzRtcFlFNW92blhGZFNMSXN1Mk1icDZLVzlQWmIyblBJNDVCa0dkalVlMFQzblo5UF9NelBIZ0VwcEE?oc=5 | → 대표: 정일택 금호타이어 사장 "ESG 공시 의무화 선제 대응…데이터 관리 고도... |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBycHhoWWZqWWRDeFVnV3k5UHZWYktkOFRyaUdodjBSV21ZRmhPSzZNaXk0b3JrVW5UbmFzaklYNmtTWFlza0ticG9fS2JRNnl0VFNYQndsLTVxZXY2VDZyRWtzeVdtWXdyTGc?oc=5 | → 대표: 회계기준원, KSSB 공시기준 파일럿 테스트…전문가 TF 논의 착수 - 조세플러스 |
| esg | paxetv.com | 상장협, ESG 공시 실무교육 실시…2028년 의무화 대비 지원 - 팍스경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBWVlJBV0tobXZxeWRCVEctRkpCeVptamdtX3czV2F1UldncUNvMzQwRmg1QnlhbVhXcTdRbjVJVEVhWWVoSzdKbmt5clJCSHIycHVUUHVYRmFuaFMtV3UzMzRDLVMtbUph?oc=5 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 - 여성경제신문 |
| kifrs | 한국경제 | 회계기준원, 투자자 전문위원회 12인으로 확대…위원장에 이현승 LHS운용... | https://www.hankyung.com/article/202611200435r | → 대표: 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 |
| kifrs | popcornnews.net | 회계기준원, 투자자 전문위원회 12명으로 확대 | http://www.popcornnews.net/news/articleView.html?idxno=140944 | → 대표: 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 |
| kifrs | 일간NTN | ‘재무제표 정정·고의·중과실 손실 발생 시 이미 지급한 임원 성과급 환수’ - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5yYUg1NHFSanRPdE0zcFNJZEhTWk11VFNtSldJdFZNOG5LT0tLaFhZZE5WT1JmSWNtV0dSaEsySmZhbmZuMWo2UWt3cVlCNlVvZG1QeklNUmpxc01kX2VmQi02bTZBRWE0RUE?oc=5 | → 대표: "재무제표 정정 또는 고의·중과실로 손실 내면 이미 지급한 성과보수 환수" - 한국세정신문 |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= | → 대표: 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... |
| kifrs | 이데일리 | 금융위, '허위 매출' 피델릭스에 과징금 2억8690만 부과 결정 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxNeDhFT1BzNjY2NEFYS3NGZVhGbDNHbUFrRnIycThMTFp3V1J4cHhCdGJfbnJhclgzcnVuMnl1SVdqWHhNMjg5ekNSMkYtd243RWlTa0tBXzRuTVNNNDgzbXFtWG9ubi1RUDBQdlJzbW5hRXQyVEFGY19rWVJYZmRHUA?oc=5 | → 대표: 금융위, ‘매출 허위 계상’ 피델릭스에 과징금 부과 - 서울경제 |
| kifrs | datatooza.com | 아메리칸 리소시스, 과거 재무제표 '신뢰 불가' 판정…2025년 지배주주 순이익 5541만→1835만 달러로 정정 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5hMjVILUs3X2toMUV2UU16dWJNeVlYNTFXUHgwUHBBUTBxdGxva0xvbHJUdEhudHNkRWYyMENqbXlTMDMwT0tlZGdveENHQW5CMmpaRGpWWFRsbzUwS1plU0wwdzJPaUdIMHlCU19ycEFRbU0?oc=5 | → 대표: 블레이즈 홀딩스, 2025년 및 2026년 재무제표 재작성 결정…중국 매출 재검토 - 데이터투자 |
| kifrs | biz.sbs.co.kr | 엔비디아 회계장부 들여다보는 美 SEC…매출 공시·회계 처리 조사 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5iWm9mNWpzT2hVYmR1MkVOc0tVWHBpVm5Ebllyclh6RnlzUmZHM2hDY0lSWkpDV0h4amNJUFBOdG1GWDFBNXJ2RVdsWUlVNkhWRExZ0gFYQVVfeXFMUFFiUGh0azUxYUVFeHZzS1dqT0c1bE40TEdJYkV0OENjdjFqMjF6N2pseVlxOWRyYjVfdVhselFsQzJYeThBVFRyVzF3SjdRbUdHWHZ0WGhCLQ?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | gokorea.kr | SEC, 엔비디아 조사 착수: 회계 처리 방식 논란 속 파장 커지나 - 공감신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBfTFIxN2N4MU9VcU1DMUlqRmZ1NTlyckhzRW5pUm55NUd0OFRlVFVha1lxU0ZJallETWFWYy1KX2oxVk1fdzg3NUpHMkxKWFFtM2NUUHB4MlEzSVdfSGRxLVV2TnY3Smpm?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | blockmedia.co.kr | 미 SEC, 엔비디아 회계처리 조사… AI 반도체 공룡에 규제 압박(종합) - 블록미디어 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5rOVlzZmJuMlh0MWVseXdRaHhucVlZWC1RbmZZSjJ0X1I2Uks0TXBFSWxFRXpzTmlUbkxwUlhvLWRTdjU1VGFpNkpIZlN1QW02VXdUbExZcFg?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| tax | 매일경제 | "전입신고 늦어도 실거주땐 취득세 감면" | https://www.mk.co.kr/article/12214810 | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | news1.kr | 조세심판원 "첫 집 전입신고 111일 만에 마쳤어도 취득세 감면 인정" | https://www.news1.kr/politics/president/6360765 | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | biz.sbs.co.kr | 조세심판원 "전입신고 늦어도 실거주 땐 취득세 감면 유효" | https://biz.sbs.co.kr/article_hub/20000347776?division=NAVER | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | yonhapnewstv.co.kr | 조세심판원 "전입신고 늦어도 실거주 땐 취득세 감면" | http://www.yonhapnewstv.co.kr/news/AKR20261120103447oGO | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | yna.co.kr | 조세심판원 "전입신고 지연돼도 실거주 확인시 취득세 감면" | https://www.yna.co.kr/view/AKR20261119156700001?input=1195m | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | taxwatch.co.kr | 111일 만에 전입신고…취득세 감면 인정된 이유 | https://www.taxwatch.co.kr/article/tax/2026/11/19/0002/naver | → 대표: 111일 만에 전입신고…실거주 확인 땐 취득세 감면 |
| tax | 한국경제 | 국산 전기차 법인세 감면 놓고…당정 막판 조율 | https://www.hankyung.com/article/2026112502631 | → 대표: 與, SK ‘트리니티팹’ 지원 기업 법인세 감면 추진 |
| tax | biz.sbs.co.kr | 김정관 "자동차도 반도체처럼 지원"…전기차 400만원 세액공제 되나? | https://biz.sbs.co.kr/article_hub/20000349021?division=NAVER | → 대표: 정부 제동에도… "전기차 세액공제 없으면 싸울 무기 없다" |
| tax | smedaily.co.kr | 전기차 세액공제 국회서 이틀째 제동…정부 대책 27일로 연기 | http://www.smedaily.co.kr/news/articleView.html?idxno=366581 | → 대표: 정부 제동에도… "전기차 세액공제 없으면 싸울 무기 없다" |
| tax | view.asiae.co.kr | [세제돋보기] 전기차 생산세액공제 포함 주목…정부 대책 앞두고 국회 ... | https://view.asiae.co.kr/article/2026112411245023254 | → 대표: 정부 제동에도… "전기차 세액공제 없으면 싸울 무기 없다" |
| tax | theopiniontimes.news | 중국산 전기차 점유율 4년 새 1%→34%…국산 전기차 세액공제, 국회 첫 ... | https://theopiniontimes.news/%ec%a4%91%ea%b5%ad%ec%82%b0-%ec%a0%84%ea%b8%b0%ec%b0%a8-%ec%a0%90%ec%9c%a0%ec%9c%a8-4%eb%85%84-%ec%83%88-1%e2%86%9234%ea%b5%ad%ec%82%b0-%ec%a0%84%ea%b8%b0%ec%b0%a8-%ec%84%b8%ec%95%a1%ea%b3%b5/ | → 대표: 정부 제동에도… "전기차 세액공제 없으면 싸울 무기 없다" |
| tax | news.bizwatch.co.kr | 국산 전기차 세액공제 확대 가닥에도…정부 막판까지 고심 이유 | https://news.bizwatch.co.kr/article/industry/2026/11/20/0030 | → 대표: 정부 제동에도… "전기차 세액공제 없으면 싸울 무기 없다" |
| tax | dnews.co.kr | 대법 “괌ㆍ사이판 세액공제 한도, 美본토와 따로 계산” | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202611251240008580561 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | widedaily.com | 대법원 "미국 본토와 미국령은 세법상 '다른 국가'…법인세 공제한도 따... | https://www.widedaily.com/news/articleView.html?idxno=304702 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | lawissue.co.kr | 대법원, 괌과 북마리아나제도 '미국'에 포함되지 않는 별개 국가 법인세... | https://www.lawissue.co.kr/view.php?ud=2026112419194157929a8c8bf58f_12 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | news1.kr | 대법 "괌·사이판은 美와 별개 '국가'…외국납부세액 공제한도 따로 계... | https://www.news1.kr/society/court-prosecution/6363869 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | newsis.com | 대법 "美본토-미국령은 세법상 '다른 국가'…법인세 공제 따로" | https://www.newsis.com/view/NISX20261124_0003880987 | → 대표: [예규·판례] 대법 "미국령은 세법상 '다른 국가'…법인세 공제 시 따로... |
| tax | newspim.com | 중국산 전기차 침투 속도 韓 3위…"국내생산세액공제 필요성 커" | https://www.newspim.com/news/view/20261122000099 | → 대표: 전기차 국내생산세액공제, 국회서 '갈팡질팡'…중국 추격에도 지원 제외... |
| tax | news1.kr | "韓, 中 전기차 안방 됐다 아시아 최다 수출국"…세액공제 시급 | https://www.news1.kr/industry/auto-industry/6356396 | → 대표: 中 전기차에 안방 내줘…세액공제 시급 |
| tax | zdnet.co.kr | 中 전기차 공습에 국산차 점유율 '뚝'…국내 생산세액공제 힘 받나 | https://zdnet.co.kr/view/?no=20261117105815 | → 대표: 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 |

## excluded:smb_only (4건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | gnmaeil.com | 부가세 간이과세 2억원으로 상향 추진 | http://www.gnmaeil.com/news/articleView.html?idxno=598793 |  |
| tax | yangsanilbo.com | 윤영석, 부가세 간이과세 기준 2억원 상향 추진 | http://www.yangsanilbo.com/news/articleView.html?idxno=128709 |  |
| tax | biz.chosun.com | 송치영 회장 “소상공인 줄폐업 위기”…노동법 개정·세액공제 축소 반... | https://biz.chosun.com/industry/business-venture/2026/11/25/QBTZFH5375EDLPQGKE2MPICGQM/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| tax | imaeil.com | 부동산 중개수수료 요율표는 상한…부가세 10%, 간이과세 중개업소는 4... | https://www.imaeil.com/page/view/2026101018554473359 |  |

## excluded:standard_setter_governance (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국회계기준원 | 2026년 제9회 지속가능성기준위원회(IFRS 재단 정관 개정 공개초안에 대한 검토의견) | https://www.kasb.or.kr/front/board/calViewA.do?seq=1133 |  |

## collect:event_announcement (46건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
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
|  | 재정경제부 | ‘쉬었음’ 청년을 다시 내:일로… 청년일자리팀, 제2회 ‘국민 체감 대상’ | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080028&menuNo=4010100 |  |
|  | 금융위원회 | “다음 금융은 이미 시작됐다” 제8회 「코리아 핀테크 위크 2026」 개막 | https://www.fsc.go.kr/no010101/88216?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
| kifrs | 파이낸셜뉴스 | 회계기준 바꿨을 뿐인데… 똑같이 벌어도 영업이익 달라진다 [제18회 국제회계포럼] - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBSSEpaZHdneFhyM3RyUzVXaEduOFRGZkp3c21SNXZycHlMMTUzM2NyOE8wT21TaS1ONHJxUlpScVpVRDREVHJKaGtPUFo4RldhRHBOaFVxWFZZUQ?oc=5 |  |
| kifrs | ajunews.com | 상장사 회계담당자 120명 한자리에…상장협, 회계 실무 워크숍 개최 - 아주경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5HdjFqOU5lcmc4LUxwaUl6Z1JLSW1WUlVyQTJuTVRmejV3RzhPSVI0TWVDOGZaMjJBUVFPT0l0V0hSVTdNVWhTSTJtRkUxcTlDQjdDbzhlZFdEZ9IBWEFVX3lxTE12YnFWT2RfZWhGNlFOdTgxc2ZBR0xHR0llQmd2QklEb0tRaVZrYl8wRUMwandfXzJIR2pJam1YakdQa1E0TkFibnk0ZHFYWVFSSVpCRW5PTUM?oc=5 |  |
| kifrs | newsis.com | 상장협, 상장사 회계담당자 대상 워크숍 개최 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBrdW9aYXV0UEtXUVB1d3RRcUNJcGpSNzVjand2eXE2SXg2OTBDU01aQ2ZkckVmN2gxZTQzQ0IzZjNnMlZ1TC1LUVFTeE1ERmZYUDZkY18tdE5OT1pjbTJNbtIBeEFVX3lxTE1Rb2pnSHVCNnNVaXlkaTlHLWQySEFhUEpFclpHN2N6UVduR2Y4MVJoUUhBN1FJb25NdkVVeDJkRjNnRm5IX2UzR1Y4ZHNTUWR0bURRTDZSSVotaEYxOWE2S01HUzBEbGlyTWlGVWhHb1hNMGFTZHZLUA?oc=5 |  |
| kifrs | 머니투데이 | 상장협, 코스피 회계담당자 워크숍…K-IFRS 1118호 대비 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMidkFVX3lxTE5EMTFVcXVPbmhsR1FqZEpIZ0ZWUFJTR0VvSUR5a2RHbTliQWJpbGtQaWM5YVNXMWs1bHdCRmx3NjlaaDROZm12OHZFVlpiOTE1WTd0U0N4d2haTkNqOEc5SHNXeGhrOWJVaUtPWjlob0tCR05XVkHSAXtBVV95cUxOb2RqUmhYQVRsM21pdEhHcHhpcDdFRF82Q3h4ZFROM0oyZ1k1T2thbGVCbUFqSjBYZGRNS0hLbE1vUkxzQVg5OUE4dDBMdXJUaVlRMUFtZmxmdzJkczRTZ05XcFdtZGNNaEFiZm44aTFQR3IwQXRyQ2pPR0U?oc=5 |  |
| kifrs | 파이낸셜뉴스 | "새 회계기준 안착하도록 제도적 뒷받침 필요" [제18회 국제회계포럼] - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ST0FLRjNmYjNJRHRqZ2R3QS1WeWVKbVNnTHB0OXR1ODY4R1RuOElXZ1oxYW44NmN2b0daS3IyOTd4UFF5N091T3NzX1dEcmtSMTVOVFNqY0l3QQ?oc=5 |  |
| kifrs | etoday.co.kr | 상장협, '2026 회계담당자 워크숍' 개최 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFB0TTlSbXIwUmxrSFcxZkhvLVlXT2psUW1mSmdDX2lBbFZSMWtIQ0M3VmRTY3NOeFd0X0FyQkpsNjVLeUl1XzQwbjE5MEV4VHRJcjRPMw?oc=5 |  |
| kifrs | dailian.co.kr | "회계현안 실무대응 모색"…상장협, 상장사 회계담당자 워크숍 - 데일리안 | https://news.google.com/rss/articles/CBMiogJBVV95cUxNYmtUQ1ZzRWU3Z2NERS0yNUE0N3lpZXBtcVlDS29DQWROV3pWU29jMHZjcUNiaFZiV2p6RzR2a1JJbDR1Zk9SYnlqTjhtUFRydjhubE55aGZ2eXJGRzUtbXc1TmFlRlFNS1JWLXBhbWRJOHJqNFR5VmRQSnlmdjdCa19LQ1J3Z1JCWnRnbDJ4bDRRWTVhLVdqWC1jbmhJdFExWFBXS2VQRS1haHFZd0w0WTk3U09rLXZNczh6NzVGdVlrMkZYRmpwYmtOU0swbFM0MGdXNkZSQkgtUjlnMTVpbWpOa2VfQlFWNXNoTmh3NF9OTjJEOU00dllHdWVLZWNPc0xWYWlFQ2VfWUxzdTlPZTktR2J1b0tIVk1Ta1FZTGIyZw?oc=5 |  |
| esg | news1.kr | "ESG 공시 정교화"…KCC, 지속가능성보고서 12년 연속 수상 - 뉴스1 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1hcjlQcXhLWjFRZmhhajFIMTFHaG5tUW9rRzNNdDVyUjdYMTNCRTNjdExIVl8zeGp0bjZQcUo4S2N1clJvc0dNU0gzWTFCRUQ1MHdlRXV4bktiWUFk?oc=5 |  |
| esg | thepublic.kr | KCC, 지속가능성보고서상 12년 연속 수상…ESG 공시 체계 강화 - 더퍼블릭 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5pU2piLTlJdkNBUDRQa3lHZ2hUVEU3cVpnYnVUOEp6VUllWndCNjdOUVFMXzlTSGdqTFJOMG5zeUZTOXdsbG40dW4ydk1zN056bTBEYjBCRExWeklYbmxfOS12XzN3bHhiZjRTY0ZJa9IBb0FVX3lxTE5pU2piLTlJdkNBUDRQa3lHZ2hUVEU3cVpnYnVUOEp6VUllWndCNjdOUVFMXzlTSGdqTFJOMG5zeUZTOXdsbG40dW4ydk1zN056bTBEYjBCRExWeklYbmxfOS12XzN3bHhiZjRTY0ZJaw?oc=5 |  |
| esg | viva100.com | KB증권, 지속가능성보고서상 2년 연속 수상…ESG 공시 역량 인정 - 브릿지경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBIS1U5YTZWMkJPMGRheUhwbURGd3N1bFI3dG9Bb2ZkX3gxLWlOTlhuRTEtaTZGay1QWG16WGl0V1VEdlZFM3pGM1ltTEdEcVJuem5ZRDBxOHFjQQ?oc=5 |  |
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
| esg | etoday.co.kr | KCC, ESG 공시 경쟁력 빛났다…12년 연속 우수보고서상 수상 | https://www.etoday.co.kr/news/view/2652544 |  |
| esg | megaeconomy.co.kr | 우성, ESG 공시 역량 인정…지속가능성보고서상 수상·평가등급 두 단계... | https://www.megaeconomy.co.kr/news/newsview.php?ncode=1065578156983631 |  |
| esg | lcnews.co.kr | 호텔롯데, 지속가능성보고서상 첫 수상…ESG 공시 확대 | https://www.lcnews.co.kr/news/articleView.html?idxno=212060 |  |

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

## collect:no_category (280건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
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
|  | 금융감독원 | 금융감독원 제14기 FSS 대학생 금융교육 봉사단 출범 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225405&menuNo=200218 |  |
|  | 금융감독원 | 주택공급 촉진을 위한 금융,건설업계 간담회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225392&menuNo=200218 |  |
|  | 금융감독원 | 충실한 증권신고서는 신속하게, 부실한 신고서는 엄정하게 심사하겠습니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225391&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 저축은행 및 상호금융조합 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225382&menuNo=200218 |  |
|  | 금융감독원 | 감사인 지정제도 온라인 설명회 실시 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225381&menuNo=200218 |  |
|  | 금융감독원 | 26.6월말 보험회사 대출채권 현황 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225383&menuNo=200218 |  |
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
|  | 재정경제부 | 개인투자용 국채 12월 발행 미실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080049&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] 2026년 3/4분기 가계동향조사 결과 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080050&menuNo=4010100 |  |
|  | 재정경제부 | AI시대, 전략산업의 미래를 위한 정책과제 제안 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080058&menuNo=4010100 |  |
|  | 재정경제부 | 권대영 1차관, 「월급방위대 TF」 2차 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080055&menuNo=4010100 |  |
|  | 재정경제부 | 이형일 부총리, 임금체계 개편 우수기업 방문 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080064&menuNo=4010100 |  |
|  | 재정경제부 | 2026 다자개발은행(MDB) 프로젝트 플라자 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080029&menuNo=4010100 |  |
|  | 재정경제부 | 「아세안+3 재무차관 및 중앙은행 부총재회의」 참석 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080035&menuNo=4010100 |  |
|  | 재정경제부 | 긴급 시장상황점검회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080021&menuNo=4010100 |  |
|  | 재정경제부 | '26.11월 국고채 「모집 방식 비경쟁인수」 발행 미실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080007&menuNo=4010100 |  |
|  | 금융위원회 | 건전성 규제, 금융 공급, 연체채권 관리체계를 종합적으로 정비해 일회성이 아닌,  지속가능한 포용금융을 실현하겠습니다.. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88232?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 언론사 기자 등의 부정거래행위 등  불공정거래 행위에 대한 조치 의결(2건) | https://www.fsc.go.kr/no010101/88228?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융시장 위기 대비체계를  한층 더 강화하였습니다. - 자체정상화·부실정리계획(RRP)을 연계한 관계기관 합동 모의훈련 최초 실시 | https://www.fsc.go.kr/no010101/88224?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 금융회사가 기업의 저탄소 전환에  필요한 자금을 지원할 수 있도록 실무기준을 마련하였습니다. | https://www.fsc.go.kr/no010101/88223?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 국민성장펀드는 중소기업에 대한 지원을 확대할 계획입니다. | https://www.fsc.go.kr/no010101/88220?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 공인회계사 자격·징계위원회 개최 결과 - 2027년 공인회계사 최소선발예정인원 결정 | https://www.fsc.go.kr/no010101/88212?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 「디지털자산업의 혁신과 이용자 보호에 관한 법률」 제정안 입법 추진 | https://www.fsc.go.kr/no010101/88199?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 보험업법 시행령‧금융기관검사및제재에관한규정 개정안 입법예고(’26.11.25.~’27.1.4.) 실시 | https://www.fsc.go.kr/no010101/88198?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
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
|  | 정책브리핑(금융위원회) | 건전성 규제, 금융 공급, 연체채권 관리체계를 종합적으로 정비해 일회성이 아닌,  지속가능한 포용금융을 실현하겠습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790921&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |

## collect:noise_keyword (2건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | tfmedia.co.kr | 회계기준원, 공시분석이 주가형성에 미치는 효과…기관은 유용, 개인은 미흡 - 조세금융신문 | https://news.google.com/rss/articles/CBMiZkFVX3lxTE5taF9ONk9TcXpNbWFfcklJcWtvdjNDTG1ERWNtUDMwRjRNRFRjdmlJeTNhMUpHaUxDNzhaR2VCTjhzc0FjZFZyLWc4clcxTkJ5a3VmeDNJS1BDYm9RdXBMcGd3STROQQ?oc=5 |  |
| tax | biz.chosun.com | 생맥주 가격 안 오를 수도…국회, 주세법 재검토 요청 | https://biz.chosun.com/policy/politics/assembly/2026/11/25/GOKIPKGU6VG7NJH2GDIW3F5D3M/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |

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

## collect:out_of_scope (210건)

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
|  | 정책브리핑(조달청) | '나라장터 원산지 관리 강화' 관련 조달업체 교육 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790973&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 아이들의 상처 난 마음, 현장의 세심한 손길로 보듬다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790959&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(교육부) | "아이의 성장 속도를 지켜주세요" 영유아 사교육 개선을 위한 공동 실천 약속 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790958&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 수업을 바꾸는 교사들, 교실 너머로 변화를 나누다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790957&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 일하는 즐거움으로 여는 당당한 내일, 역대 최대 118만 개 노인일자리 사업에 참여하세요! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790949&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | AI 시대, 의료데이터 더 안전하고 쉽게 활용 「보건의료데이터 활용 가이드라인」 전부개정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790948&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 내 정보, 더 안전하게 전송하여 국민 편익 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790953&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | '인공지능의 모든 순간에 사이버보안, 대한민국 인공지능 보안 역량을 하나로' 2026 인공지능 해킹 방어대회(ACDC) 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790946&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | 2026년 11월 퇴직공직자 취업심사 결과 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790952&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 공무원이 직접 만든 AI 서비스 한자리에... '제2회 AI 정부 실험실 이용자 포럼' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790971&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 올해 전국 빗물받이 898만 회 정비, 우수사례 30건 사례집 발간·배포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790969&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 재난관리물품 보관부터 현장 운송까지, 민관 협력으로 재난대응 역량 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790967&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부, '제5회 한-아세안 재난관리 장관회의' 아세안과 재난관리 협력 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790965&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 국민 생활 바꿀 공공데이터×AI 아이디어, 왕중왕전 최종 승자 가려졌다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790963&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 지역을 품은 '마을기업',  백화점과 상생협력 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790961&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 3/4분기 가계동향조사 결과 보도자료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790956&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 올해 전국 빗물받이 898만 회 정비, 우수사례 30건 사례집 발간·배포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790955&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 물의 미래를 바꾸는 도전, 2026 대한민국 물산업 혁신 창업대전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790954&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 날씨 예측은 더 정밀하게, 위험정보는 더 빠르게! 한층 촘촘해진 겨울철 기상 안전 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790951&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.27.금.조간] 2026년 청소년건강행태조사 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790947&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 애플 부당 광고 사건 심의 절차 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790945&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 제2026-19회 원자력안전위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790944&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 통합돌봄 뒷받침할 '다양한 돌봄 공급주체' 키운다 복합사회서비스 운영모델 실증 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790943&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 양자컴퓨터 시대, 암호 전환의 길을 찾다, 제1회 양자내성암호 전환 경진대회･해커톤 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790930&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 물류창고 화재, 설계부터 운영·현장 대응까지 안전관리 강화한다 - 관계부처 합동 「물류창고 화재안전 강화방안」 마련 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790937&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 국토와 환경이 함께 만드는 지속가능한 미래 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790936&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 북항 방문을 보다 편리하게, 해수부, 부산북항 재개발 배후도로 준공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790935&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 우리나라 해양법 전문가 김현정 교수, 해양법자문위원회(ABLOS) 위원으로 선출 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790934&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 주행거리가 긴 렌터카부터 전기차로…제주 렌터카 업계와 전동화 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790939&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 국토와 환경이 함께 만드는 지속가능한 미래 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790938&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 찬 바람 속에서도 따뜻한 마음으로, 반려동물과 겨울 동행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790933&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 돼지유행성설사(PED) 방어항체 보유율 하락, 양돈농가 방역 강화 필요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790932&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | '올해의 창작 K-Sool', 최고의 작품은? | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790931&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 공정거래위원장,  중소기업 현장 소통 간담회 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790929&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 해외 밀반입부터 국내 불법 판매까지, 무허가 수입 의약품 등 유통 일당 적발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790925&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 행안부·국토부, 관계기관과 함께 도로살얼음 사고 예방 캠페인 전개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790923&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행안부·국토부, 관계기관과 함께 도로살얼음 사고 예방 캠페인 전개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790928&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처-경찰청 수사협력 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790914&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | '가짜 K-상표' 정부가 직접 막는다! 범정부 적극행정 우수상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790913&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 우리 기업의 국제 특허경쟁력 강화, 「해외특허 길잡이」가 함께합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790912&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 국민의 생명과 안전을 지키는 현장 최고의 발명은 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790911&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 동포는 전국에서 김장 중, 동포와 지역주민이 함께하는 김장 체험 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790908&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 한국산업인력공단, '인공지능(AI) 훈련 우수사례 경진대회' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790918&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 개인정보위, 기업결합 관련 사전 실태점검 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790910&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | 사전적정성 검토제, 사전 협의에 그치지 않고 현장까지 챙긴다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790909&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 국민안전 지키는 현장의 아이디어, 최고의 발명품은? | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790917&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국민 가계통신비 부담 덜고 속도와 안정성은 높이고... 전국 시내·광역버스 약 3.3만 대 와이파이 7 고도화 완료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790903&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈증명서 10종， 전국 무인민원발급기에서 무료 발급 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790902&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 공직사회에 새로운 변화를 불어넣다! 행안부, 조직문화 개선·공간혁신 우수기관 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790916&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 개인투자용 국채 12월 발행 미실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790919&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | [11.26.행사시작(10시)이후] 현장과 함께 만드는 감염병 대응의 미래, 「2026 감염병관리 콘퍼런스」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790904&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 누리호 1·2·3단 모사체 이송 점검 완료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790926&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] K-FIND, 건강한 일상과 식품산업 성장을 이끈다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790907&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 산림복지시설 동절기 안전사고 제로화 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790906&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 유럽국장 튀르키예 방문 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790901&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 국립수목원, 11월 '우리의 정원식물'로 비자나무 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790900&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 인공지능(AI), 기술 진화에서 산업 대전환까지 표준이 함께 한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790893&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한국과 아세안 싱크탱크, 미래 경제 통상 협력방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790892&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한-사우디, 원유 수급부터 비축까지 중동전쟁 위기 대응 공조 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790891&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)美 무역대표부, 과잉생산 301조 조사결과 발표, 한미 관세합의 수준 15% 기본 제안 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790890&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "사람과 기술이 함께 성장하는 반도체 산업" 김영훈 장관, 반도체 연구개발 종사자들과 근로시간제도 운영 실태 등 현장 의견 청취 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790882&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 한국전통문화대학교, 디지털 기술과 국제협력으로 세계유산의 미래 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790886&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 국립과천과학관 Sci-POP, 페루 학교로 간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790895&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | 방위사업청·국방기술품질원,  국방 표준화 발전방향 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790881&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 2026년 하반기 범부처 통합식품안전정보망 운영협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790880&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, GLP-1 계열 비만치료제 안전사용정보 안내 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790879&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 2026 적극행정 우수사례 경진대회 '국무총리상' 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790878&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | K-푸드 국제규격 개발 위해 민·관 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790877&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | AI 가짜 의사 추천 광고행위 금지 본격 시행 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790876&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 4개월 연속, 방한 외국인 관광객 월 200만 명 돌파 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790875&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부는 시도교육청과 함께 안정적 학교 운영에 만전을 기하겠습니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790941&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부·한국교육과정평가원, 2026년 고교학점제 성과공유회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790874&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 주택시장 안정과 주거복지 향상,  금융·인공지능(AI) 활용 방안 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790872&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 시민과학자와 함께한 섬 생물탐사, 국내 미기록종 발견으로 이어져 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790873&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | [보도참고] 2026년 3/4분기 가계동향조사 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790972&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 권대영 1차관, 「월급방위대 TF」 2차 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790883&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | AI시대, 전략산업의 미래를 위한 정책과제 제안 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790920&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 24년의 도피, 그 끝은 구속이었다! (경기청) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790871&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한-오만 외교장관회담(11.25.) 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790870&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 김진아 외교부 제2차관, 한국국제교류재단 제주 본부 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790869&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 고령·밀양 지역특화특구 신규지정… 역사문화·스마트농산업 거점 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790847&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부, 한경협과 함께  '도약(Jump-up) 기업' 현장 찾아  중견기업으로 도약 지원 의지 밝혀 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790846&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제6차 한-중미 특별라운드테이블 개최 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790845&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 제3회 국토대전환 미래전략 포럼 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790844&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 노사와 지역사회가 함께 만드는 안전문화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790843&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 전국 임도 관계자 한자리에···우수사례 공유 및 정책 발전 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790840&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 기업·공공기관과 산림 ESG 성공사례 공유 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790838&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 그린바이오, 화장품 기업과 손잡고 소재 산업화에 속도 낸다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790836&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 인사발령(3급 승진) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790832&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정중심복합도시건설청) | 국민이 그리는 세종 국가상징구역, 짧은 영상(숏폼)에 담다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790831&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 고국에서 맞는 겨울, 고려인동포 가정에 온정 전한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790835&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 도로 살얼음으로 터널 안 연쇄 추돌·화재 올해 네 번째 레디 코리아 훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790834&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 벤조피렌 초과 검출된 '향미유' 회수 조치 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790830&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제52차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790826&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, 국가 어업지도선 '무궁화10호' 취항 축하 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790897&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 해외로 달아나도 끝까지 쫓는다...인터폴 추적망, 이제 범정부가 함께 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790820&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 붉은악마, 북중미 월드컵 정부합동 신속대응팀에 대한 감사패 전달 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790825&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 제6차 인도 진출 우리 기업 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790817&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 2026 범죄예방대상 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790816&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 민관 전문가 머리 맞대고 '정부혁신 청사진' 그린다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790819&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 송미령 농식품부 장관, 콩기름 등 국산 콩 소비 확대 주제로 선재스님과 함께하는 차담회 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790813&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농촌 재능나눔 우수 활동자 포상·격려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790812&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 백승보 조달청장, 에밀리아 가토  주한 이탈리아 대사 조달시장 활성화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790811&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 영암국유림관리소, 산불 예방 총력… '찾아가는 영농부산물 파쇄' 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790815&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해양수산부 장관, 어류 양식업계의 현장 목소리 듣는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790896&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 제31차 유엔기후변화협약  산림분야 성과 거둬 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790810&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 황종우 해수부 장관, 전남광주 지역 김 양식장 현장 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790828&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 국가 R&D 특허성과 입력, 더 쉽고 간편해진다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790803&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 국제 특허출원, 달라지는 제도 한눈에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790802&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산 데이터, 국가데이터와 만나 새로운 가치를 만든다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790801&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 합리적인 행정형벌 기준 마련을 위한  형벌 합리화 자문위원회  제1차 대면회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790800&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 2025년 임산물 생산액 7조 6천억 원, 전년보다 3%↑ | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790798&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 정부혁신 박람회와 함께, 국정철학·국정과제 전국 현장으로 확산 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790805&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 전국 농촌공간정책심의위원 150명 한자리에… '농촌공간정책심의회 합동 포럼' 세종서 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790792&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 어린이부터 어르신·장애인까지 취약계층을 위한 전국 급식 안전망 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790799&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 「회복적 경찰활동」 발전 방안을 위한 국내·외 전문가 초청 세미나 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790806&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 겨울철 시설 수박, 해충 예방·생육 관리 철저 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790795&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 강릉산림항공관리소, 규제합리화 대표 사례 전파 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790791&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "지능형 농업기술" 개발 위한 농업-산업기술 융합 연구 협력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790793&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "분야별 성과를 하나로!" 2026년 농촌지도사업 종합평가회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790788&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 청년농업인 성장 돕는 현장 중심 교육·기술 지원 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790786&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 가을비로 파종 늦어진 사료작물, 얼기 전 눌러주고 배수로 정비 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790784&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 잦은 비에 조생종 감귤 수부증 주의… 수확 전후 관리 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790782&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '한국농업전문지도연구협의회' 창립 30주년, 새로운 도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790780&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "청년·창업농도 우수 경영체"로, 인공지능 기반 양액 공급 자동화 시스템 국내 최초 구현 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790778&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 여주 지역 맞춤 벼('수원693') 밥맛 평가회 열어 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790776&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '농업기술명인', 유기적 협력 체계 구축으로 지역 농업 발전 견인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790774&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 2026농산물소득조사·농식품 소비정보 데이터 활용  아이디어 경진대회 성료 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790772&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청-생활개선회, 민관 협력으로 '현장 밀착형 농촌 공익 모형' 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790770&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 대관령 한우 방목 마치고 축사로…겨울철 보온 관리 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790768&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "선별기 데이터 표준화·연계"로 디지털 유통 기반 마련 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790766&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '2026 농업인 안전365 캠페인 공모전' 수상작 20편 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790763&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 잦은 비 대응 주요 채소 생육·병해 현장 살펴 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790761&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 기후변화 대응 해법 농업 현장에서 찾는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790759&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 근로복지공단, 2026년 녹색경영 우수기업 '한국환경산업기술원장상' 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790753&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 여과 액비로 경축 순환 농업 확산 방안 찾아 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790757&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 육아휴직 중에 승진, 주 35시간 근무, 일·생활 균형 우수기업 124개소 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790752&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 동서울변환소 사업 협의서(안) 합의… 감일지구 주민투표 거쳐 최종 확정 예정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790765&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 법령정보 실험실(LAB)에 초대합니다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790751&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 생명지킴추진본부, 생명대사 참여 자살예방 인식 개선 캠페인 영상 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790754&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 2026년 국제개발협력의 날 기념식 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790747&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(법무부) | "어디서나 참여할 수 있는 전자주주총회" 법무부, 기업이 어떻게 준비해야 할지 기준 제시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790750&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 포도 과수원 양분 과잉 주의, 토양 검정 후 맞춤 관리해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790748&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 술잔 없이도 이어지는 마음, 2026년 음주폐해예방의 달 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790742&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 이달의 신간 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790740&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 개정 정보통신망법·시행령의 현장 안착을 위한 기업 대상 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790736&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 2026 인공지능·소프트웨어 인재 축제 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790735&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 초격차 소버린 에너지 기술 확보를 위한 국가연구소 개소(성균관대) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790734&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 지식재산 데이터, 국가데이터와 만나 새로운 가치를 만든다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790746&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 동물대체시험 전문인력 양성 정부·공공기관·대학이 함께 나선다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790745&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 우리 차 가치를 높이고 K-Tea의 미래를 연다 제2차 차산업 발전 기본계획('27~'31) 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790737&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 우주물체 추락·충돌 재난 관리체계 강화를 위한 워크숍 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790889&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 정부혁신 박람회서 농사 도우미 'AI 이삭이' 첫선 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790738&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 고군산군도 새만금사업지역 면적 80.8% 해제 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790743&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 한국국제협력단 이사장 임명장 전수식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790726&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 사회혁신 창업의 도전, 정부·민간이 함께 응원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790724&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 법령데이터와 인공지능(AI)으로 학교 행정 돕는 '돌쇠' 제14회 범정부 창업경진대회 왕중왕전 우수상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790723&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 앱 개발자 "수수료 부담", 이용자는 "해지 어려워" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790718&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 우주신기술 지정 분야 확대 제3차 우주신기술 4건 지정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790888&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 정읍국유림관리소, 산불예방을 위한 화목보일러 일제점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790722&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 약 2만 임업인에게 임업직불금 522억원 지급 시작 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790717&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 2026 적극행정 우수사례 경진대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790714&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(인사혁신처) | "국민 안전·불편 해소 이끈 적극행정, 올해 주인공은?" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790711&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | "국민 안전·불편 해소 이끈 적극행정,  올해 주인공은?" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790713&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 기상청, 극한기상 대응을 위한 한일 공동연구 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790710&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 국민 2가구 중 1가구 "사회서비스 필요", 문화·여가, 신체건강 수요 높아 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790701&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 정보보호 공시 의무 대상 확대에 따른 기업 대상 전국 순회 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790698&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 선박·어선 검사증서 발급부터 후속 민원 서류 준비까지, 34종 서류 정부24에서 한 번에! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790709&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | '정부24'에서 선박·어선 검사증서 발급부터 후속 민원 서류 준비까지 한 번에! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790700&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 10월 국내인구이동통계 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790707&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 9월 및 3분기 인구동향(출생, 사망, 혼인, 이혼) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790706&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | "공사장 소음부터 밭 옆 가로등까지" 생활 속 환경분쟁, 이야기로 쉽게 푼다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790705&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 제31차 유엔기후변화협약 당사국총회가 남긴 과제, 국민과 함께 답을 찾다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790704&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 자동차 온실가스 전과정평가, 민관이 함께 준비한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790703&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 씨제이프레시웨이(주)의 부당한 고객유인행위 사건 심의 절차 개시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790697&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(감사원) | 제주특별자치도 기관정기감사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790699&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 걸프 7개국과 기술규제·인증 애로 해소 설명회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790696&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | K-Quality로 완성하는 초격차 대한민국 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790695&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | AI 시대, K-팹리스 도약의 열쇠는 '상생' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790694&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | '26년 10월 주요 유통업체 매출 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790693&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 이형일 부총리, 임금체계 개편 우수기업 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790942&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 국립6·25전쟁납북자기념관, 특별전시 《되;돌아 RE;Member》 개막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790692&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 100년 기업, 세대를 넘어 성장합니다. - 2026년 명문장수기업 수여식 개최 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790690&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 통일·북한 분야 신진연구자 워크숍 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790691&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 글로벌다자외교조정관, 유엔 평화유지활동(PKO) 기여 강화 방안 협의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790689&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '케이-웹툰' 산업 성장과 저작권 보호 경험, 아태 지역에 전수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790688&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 12월부터 13~18세 청소년도 모두의카드 이용 가능 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790685&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 해수부, '제4차 유엔해양총회'의 성공 개최를 위해 주한 3개국 외교단과 국제 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790684&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 선박 안전을 위협하는 항행장애물 대응 능력을 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790683&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 염전 노동자 고용 실태 합동 전수 조사 및 노동법 위반 의심 염전 근로 감독 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790682&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 송미령 장관, 국제농업개발기금(IFAD) 총재 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790720&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 염전 노동자 고용 실태 합동 전수 조사 및 노동법 위반 의심 염전 근로 감독 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790687&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 관세청, 디지털 소통 분야 6관왕 달성…  국민 눈높이 콘텐츠로 소통 역량 입증 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790686&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 수출 1조 달러의 빛나는 조연, K-소비재 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790681&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 구직자에게는 새로운 도약을,  기업에는 성장의 기회를! 맞춤형 고용서비스가 함께합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790680&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 대한민국 첫 수출 1조 달러 달성, 공공조달이 수출 성장 이어간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790678&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(국민통합위원회) | 국민통합위원회, 대한민국 공공브랜드 대상 수상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790679&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |
|  | 정책브리핑(조달청) | Korea Reaches USD 1 Trillion in Annual Exports for First Time, Paving the Way for Sustained Export Growth | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790673&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-26&endDate=2026-11-26&srchWord=&period= |  |

## collect:out_of_window (145건)

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
| kifrs | 금융위원회 | 알림마당 - 금융위원회 | https://news.google.com/rss/articles/CBMiTEFVX3lxTFBRdXVWSmo1Q05xMzhXeW42YTdHNnJqNXZUT3FxeGNFU2pzcDFKUE1sMklESEVqd3ljN1VRVlVpZ243Qjdaa045MGF0QW0?oc=5 |  |
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |
| icfr | 한국경제 | 외감법은 경찰, 자본법은 중수청…분식회계 수사 차질 불가피 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wOF91b3FKNTlVV3FUM3J2amdHek9VS29CTHZ1N3d3NFJiOWtOakNkRVRPSzhFd3ZKMHM3RkRmcW9QeE9hRFV4NHNhbmQ5Q0RSNUpIbEYyOG9zUQ?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | safetimes.co.kr | '한국판 삭스법' 완화될까 … '신외감법' 5년만 누더기 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE1TSjE4VU1MTkcybmtWUFhvYTM4U0tJS19EZlhWMy12Y2FhLTZJRnRHcy1uQkVaNUZqMDJkLWRnVm4yWEYwWGpvSkhYN1FkOTdQTGRkU3JoYUhDd3JmVFhHREpqWFZWaDFlTm8xejNIZ9IBc0FVX3lxTE9YYUxEcFBCLW1xZ19RcTEwX1hzamVlY0QySi1yQ2RrOHNWVGNjbUdJYTg2eEtkd0N0Y2RDT1lUVEI1ckZ2Q0tvM2FBTVBMYV93NnVQSWNVcXNXejg3VWdtNWR5SFE0aFlDbGJSVnFBVmQ4LTQ?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | hitnews.co.kr | 新외감법, 연말 ‘밀어내기’ 잘못하면 포렌식 당한다 - 히트뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1SdW1ibmVsdHg0UGZIX2NnQmlWM0hEWUlBZHRMQXdPQzlDQzdnOXA0eHhKOVFsTFVZWGlLTnBlZmZsV3E5TlNrYWZBZS1MTW1OVi1MWjNFYVU2X3FmVEUyZ25mZzZtY3JDMHc?oc=5 |  |
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |
| icfr | 한국경제 | 회계기준 위반 내부감사에 과징금…외감법 개정 후 첫사례 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5lQlUwNGVxRFhSVUUzSlRnemExbzQ2M0Zka3ZMS0pna0RFOFZVODRiLWJwN1Z1dF8ydS1JaEdFdXhHeVlUM3c3UHpXZ05oamt6a0NBY000a1NEdw?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | newsis.com | 초유의 오스템임플란트 횡령, '신 외감법 무용론' 번지나 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SR1lOd2VmanJnVW9FQXRwSVJYUlIzSkNnRndGNEcyRmlxUGxiUUE4VHkyZUwxbFZOMk1wMWZ0dXh3QUlkOXlUWHNvYlh2Qm80QlhOMGlydTJvTXNyQVF3N9IBeEFVX3lxTE1CUVJtSHR0MHpJa2JOZ1dtODNsZUp4ZlEtZ0g0ZEFpNDVzNHM5RlZndGdpS2xoc3hDcUVuOUsybGxVQUotSzJmdlRadEdPX1lhMlVMTzN2RzJaakNuWmJrZko3ajBfbmVNVXZ6eWpOemh4ZVNrOWEzcQ?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | 한국경제 | [한경 CFO Insight] 신외감법 2년...감사비용 70% 폭등 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCc1VNZVE2U181NVZDQzlZYnpVM2E1MEtxdXRDS00tUGVlN0ZSTFVzNTRhWFQxc1NKUFFtYjVKWEFDUmZkZVItN21jdkJvSFphVUVVY19QNVVlUQ?oc=5 |  |
| icfr | 한국경제 | 감사비용 폭등…기업 '新외감법 공포' - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE9ycjhVYWoySi1PTG91cTZBMF9BNjZtd21taUZxb0ViQ1NUbWMtUFdJQzNLb1Z0YUtjZlBldEc0VUtLVDVxUmlKTUk0RmxyUE93bEhKRWowOU54dw?oc=5 |  |
| icfr | etoday.co.kr | 여전사도 준법감시 인원 의무화된다…내부통제 모범규준 시행 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5FQjRaZWtNTGJlSnBSUm5rRU9GczQ5cnVuVEtkeDRKaU4tVVduUUNmVFhxRENMV2FJMkRaZkZOVVJ5aGtYY194TGI5NzNKSXR3T2Zzdg?oc=5 |  |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 |  |
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | ESG경제 | 정부·여당 ESG 공시 입법안 나왔다…제3자 인증 의무화 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE44WUtnTkREZjU4RzdtSFZIcG1PcUo2czNDX0RKdWFITEVsZXppZDk1QU5aS0JMdHRfTVFXOGR3WjVNc3R4eVNKZU9GeXVuNVplZkFIdjhwRmhTcGVxazZxeTNDSzRZbjQ4MUZmOQ?oc=5 |  |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 |  |
| esg | joongang.co.kr | 2028년부터 자산 10조 상장사 ESG공시 의무화…재계선 “기업 부담 가중" - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE00a0pwNnpEYU9UbzdhYUVGWThwVlY3OUlmRzVLaFM0azBDVkpHMGtDMVpPODZuZGJIbTJ4ZEI0XzRiMnV3aXpLbmk0T0QtcU95UXUyVWln?oc=5 |  |
| esg | lawtimes.co.kr | 지속가능성(ESG) 공시 제도화 방안 확정에 따른 기업의 대응 전략 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFB2aGRwZ0x1V05meG5NY3I0ZFUtSmQ5bkZQSFN2c19wbzAxNjVZVzRNRElMSDdhWjJPeXdPRUd5Q2RBcWhwVWtQbkxka3FjQW1NOE9IR1dFeGtta3N3YVdOSDZzcTB3NFZjbVd3NHdn0gFyQVVfeXFMT1hzSVFtUURPX2hWY1VYeXYxS1I5OHUxQzE4enl0eFhLOGlFek5tdGxIUWRMNkpyYUdISm5mbmRXQ0V4WXJmT2xmR1J5eno3YW9pamo4MnpoVlkwZmVtLXh6WFRGRjJkd29iRVdJNzAyckRR?oc=5 |  |
| esg | 임팩트온 | ESG 공시 로드맵 또 연기…국회 일정에 당정 협의 보류 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE10b2lHcFJxSk1ZN0ZNMUZFLUxzajM4XzktSUZzU1NaQ1B2WDNGX194UF9EUnVOZTJPcjBjTC1FbDI2R0xGSWFQTUc5d01xZ2NVRWZQVEwzcXlQQXM0aFFUYTJmS09iSGZjX2c?oc=5 |  |
| esg | 임팩트온 | 한정애 의원, ESG 공시 의무화 법안 발의…사업보고서 공시·제3자 인증 의무화 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBvTG5aUFpieFNTQTRBMzNjcWk3X0tjQWlmYWdtT3A3SkhwcUhNZzdqLU5LLXBTeVllZk1IMkNEMGNyanRQNFh6cDlRZmNBZG9GX3RTUk0xZWprZG9icUk2MjBzOWZTMDhQcnc?oc=5 |  |
| esg | joongang.co.kr | [사설] ESG 공시 의무화…기업에 부담 떠안겨선 안 된다 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1hOUU4ajk1NHRSRnpIR2FqQ3FvWjNqOEJFc2kzZW40bjljbzVTdGg5d29zNkpQcTQtSWRMVkhsXzc0V1RWc1VsRWllN000NmtwS0NHT1Vn?oc=5 |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | 임팩트온 | 이웅희 위원, "ESG 공시 로드맵, 당정청 조율 단계"...상반기 발표 목표 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1FSV9UekJiTzFXSUd6SWYxOWpyY3RIMkFSajZFVC1GYWJhRjYtd3JCTTBkbEpQMWJkcWNpRjN3LV9HSDBCWnFlUE1BbTJpQTdGZDBfV2pwZV85SWN2YXJNN3Q1WmhaODlYYUE?oc=5 |  |
| esg | electimes.com | ESG 공시 로드맵 확정…10조 이상 코스피 상장사부터 의무화 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5XUnhUekpXVlVFZEFuR0ZtdldTYlhvX1A4Yk84UVZqc0xCLTVYQVlTT2wwLWZRUkNGb0FpWTZaeEJzUFNXWVpwYlFJQUhvTmR3aEtOS0FKeFVvQzBiVGJObkF4X3phc1VScmJMQdIBcEFVX3lxTE5HcHpjSzJTMnQyakNLT190LUVLX3ZGNXM0LWJKVzA1cXlHcjhVc1dWY1V4OGFrcG42REdfMWJRVmlXVUcwZ2JYTXE5ZE1BamduRllrbGZReTBqbjRUeWVQZUl2cEdfZ09CRVFRemlvS3Q?oc=5 |  |
| esg | 임팩트온 | 【데일리 ESG정책 브리핑】ESG 공시 로드맵 확정, 무인 자율주행차 안전기준 마련 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBUNkxVMHJJQmdhQ1JkVTlRbGxqcl9NclhBeHMzWnVIbWlTWVRXLUVsbm9uektFRm5IUDNTaUUzMGpFdE85em80V3p4X2pQMmdQVWsySmZabTZTeVFMVkpRcGwxNjJJVGVSMmc?oc=5 |  |
| esg | 임팩트온 | ESG 공시 로드맵 확정, 사업보고서 공시로 시작...2029년 3171개사 영향권 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9iV29YRzlVTjJNb1JmalR6LTZLOXJlajZQeDdUN016eU1SSGNFZm9pWWVLYVhZcEk4OC1WejFaODdFZzFxVlF4aXpwd3pONHVncXp1UlBBQnlZanV6S3NJR19VQk5RQjZkbHc?oc=5 |  |
| esg | edata.ekn.kr | 2028년 ESG 공시 의무화…10조 이상 기업부터 적용 - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE9JT2doTTBTd2habVdUZVAwSWx6bWZnS0txQnF3SzF2U0ViU3d6TFMzOHBWa2FzMVBoUDY2cF9BRk1RQnZPekpZN2ZDMjdMYnNxcFg0ZjhFVElIY1FtbGc?oc=5 |  |
| esg | hellot.net | [ESG 칼럼] ESG 경영의 주객전도, 보고서가 아닌 운영체계가 필요하다 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE9tWktmcTYyVFQ0LXlXN01SNUFBUFB1S1MtY0NVaXVNMUpxd0d6aGFvd0EycU95Z0JzQW93Ul9OQllDRFBTcDFsUjdYZzhfLUVreE92LWFwSmtwd2tpaHJB?oc=5 |  |
| esg | hellot.net | ESG 공시 3년 유예에 안심? “지금이 공급망 데이터 준비 골든타임” - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5iaGx6SGNQX1VPUDZ1cEJqcmg2T3FjM2JoRnV0d2hHWVRuYm8xaEhDd0FnVTItSHphSzVsWmpxd3djTVN5dWtGS0RtajZhTU9IT0ZySFFSbDh2R3pPLVFv?oc=5 |  |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 |  |
| esg | hydrogennews.co.kr | ESG 공시 의무화 앞두고 '양극화'…중소 제조기업 지원 관건 - 수소신문 | https://news.google.com/rss/articles/CBMicEFVX3lxTE5kdXpRWlJQTVRseXpxamJseDlTZ0NHOFNmRm0tYjFnMVhVcVc5RXR4SFRMUHVZZ3dLajYyX0pQMHBCWFlkS1FITkFHWmlxZlZ1eEljVWQza2Z0QjU0V2s2NXIxSF85RWtOSEdOMW9SU3XSAXRBVV95cUxPQi1BNnFqNThPQXhiQnp1SVlNTWJuYkhDMnBjTlJGYXJVX195V2hkbkpQSFpsQ1hLQlBsUTlRZHVJeE5jNElZY3NUTzhNT0pLeXl5d0F5R09rcG1INE56dE8xbnk0aXZqZFRnYkRBLXlSdjhmSQ?oc=5 |  |
| esg | etnews.com | '자산 10조' ESG 공시 의무화…상장사 부담 커진다 - 전자신문 | https://news.google.com/rss/articles/CBMiTkFVX3lxTFAxclQ0TTYtZDdKc1VBMVhrVlhhZ0oycmdLU21rTHUwWk1UNTV0aUZzREZQa1FscWRVQU4yc0dFajJ4QVFpV1ZEUldBeW5YZw?oc=5 |  |
| esg | sdgnews.net | [SDG 13] 정부·여당, ESG 공시 의무화 로드맵 확정…2028년부터 자산 10조원 이상 코스피 상장사 적용 - SDG뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBkNmVtVi15eHJESnRrNW5QeXEzU0dpRmJwdlpyMVQxUnR1cmh3YXdrQWZ1NzZrUE5kcTQtSmhJdmp5NWVYNjBCeWRaZUNsYm1WaU94RnU3U2RfM0I3M2tBZTRuVjFHLXVDYncw0gFrQVVfeXFMUGQ2ZW1WLXl4ckRKdGs1blB5cTNTR2lGYnB2WnIxVDFSdHVyaHdhd2tBZnU3NmtQTmRxNC1KaEl2ank1ZVg2MEJ5ZFplQ2xibVZpT3hGdTdTZF8zQjcza0FlNG5WMUctdUNidzA?oc=5 |  |
| esg | 이데일리 | ESG 공시 의무화, 10조 이상 상장사로 확대…제도 안착 시험대 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9fZ280ZEZXcEFOWWxXV3Z5X2JXcGczQTRPcUNvTXVDdW5hQmlhZEVLTVhJZ0VRYnpJTHQ3cHdlMjg5QmlYZnBWN1BDU2hWZDlRMW5ub1lpMmk4QVFoODZpcndnVE1PcHU5Qmhsbmw1eU5iWHM?oc=5 |  |
| esg | ESG경제 | 이억원 금융위원장, "ESG공시 일본보다 적극적인 안으로 확정" - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE83TWVDTHh5Y091YkphbVBfemk1R01QbXE2RXh3dWowb3JvTDBZdnhJVTZWZnZFWC1Ld2tXcUFnc2o1b0pXQmlFN2lNZlJGRS1LTUpfdW9kN1dvVVd2OHI0bnFNaU1GUTZINHdYVw?oc=5 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 한국경제 | 자산 10조 넘으면 ESG 공시 의무화…상장사 부담 더 커졌다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBwMjd4R2ZGNDZMejN3dFVaVy0td3k4LVRyMVBjZGw4RV9Bd1pGNWprbk1XVERmUnlYc2toaEZtUVNVRXg2T1BuQVFqZFpGdXRNWWgzQmJ4QnFEQQ?oc=5 |  |
| esg | newstree.kr | 'ESG공시' 10조원 이상부터 의무화?…금융위 최종안에 촉각 - 뉴스;트리 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE44ajRzUW42eTRmVzNnME0zZzJvOHBVaHhxdDBpVk9DWFpfa3NXMWktN2pQTjlsWFlJWmExRmFUUlQwTkNVYzRFa0pPUWZNRW43OUxZVDZraHUxVHR1?oc=5 |  |
| esg | dailyenews.co.kr | 2028년부터 연결자산 10조원 이상 코스피 상장사 ‘ESG 공시’ 의무화 - 데일리e뉴스 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5hMk8zYmhVcnF2ZkJsNjF3NDNJbkc1emcydW81Z0FyNGN5RmROVkgxanVqTjVuQ1l5WDNxTHNQRDBoYUlTbEJLWFVJcDBUXzFRYmtXeU40RndrZ3ZnaGtHUV9IU2hXLWJPMTVRemk0OA?oc=5 |  |
| esg | netzeronews.kr | 닻 올린 'KSSB 법정공시 전환' 실전 나침반 "눈길" - 넷제로뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1XdmdXS2VwaGRQaGI0Zi16Zm40bkZYOHZYX1A0VDJmQkYxUEFhUVpkRHFocDdfaDAwTUNmd3AzWEFhMVEzdExpZzUxbVFjdlhNcmVwOXhjYUplUno0V2UwOWRqVUJBUWNNYlE?oc=5 |  |
| esg | greened.kr | ESG 공시 2028년 의무화…건설사 4곳 첫 대상 예상 - 녹색경제신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nVjVuUEFfNndhRDNqdndTXy1VWHVwc05Xbk1zVFpCaHo4SjItamNJeWlpZE5faTVwOWlSb09iV2ROYVFHMHV4U3JzVlAwVDNiT0dVcWUwMkFVMldHY0dRQm92Y1V5ZWZn?oc=5 |  |
| esg | ESG경제 | [해외브리핑] 싱가포르, ESG 공시기준 초안 공개...스코프1·2 먼저 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB2d2RieWdDdXRHVU1aY2VlSkVIX1hQS2gtencwUkFZWVJwY094Yk0tcFlTZjliWVZ5YUhodU1McW5veTBNN0JRNTgtcDVqMG0tdjI2d0FzdGtUa1ZHTFNJeGt4eVhkaWdRQUV3cA?oc=5 |  |
| esg | 임팩트온 | KSSB ‘2030년 병목’ 우려…“인증 앞당기고 스코프3 유예 분산해야” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9hN1YtS0x6aXE5Y0xKZDRWM3AwTmpISnhXQWExOG5nTGdDbXhjT3pIRnduUTB0cl9wd1gxNzhmWFF6cDJ1VzNyWm9oLW52NG9Gbk12SjQ1Wnd2LVlRcE1ncEY1RTAwZFpuaFE?oc=5 |  |
| esg | 임팩트온 | ISSB, 자연공시 의무화 대신 '권고' 택했다...10월 초안 공개 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE94NlVxeGhCUm9GM21Gc1Jibm1HWlN0dHVMb2ROYlJHSS1KbHFzNEtmT2JYc1lxS0ZGV3hFblc3cUFZUTBwZG5mMGRNY3YwYTJjMXVYa3ltbkxnSzR2XzNuMkJGcjJ6cUVVNkE?oc=5 |  |
| esg | greenpostkorea.co.kr | 4대 금융지주 ‘2025 ESG보고서’ … KSSB 도입 등 "업계 최초" 경쟁 치열 - 그린포스트코리아 | https://news.google.com/rss/articles/CBMidkFVX3lxTFBYTkk4Si1fYThuZk9xdnBYeEE1MG1TTVhQS1RSdTR0Rk9SdVhGYlZvT3E2R2ZXSjlreDR2RTVNZkpvV1BZRGZlMDJIX293RElqM1lieUZrYVZjRER3SWctai0wT19uQTVoTFd5a2NDYzI3aTBmanfSAXpBVV95cUxNZE9FRGVwd1pjMENfc1FlbXZSdVB1aHF5TmppaUpzOXdlVjZkNG9ZVDJfVDczSGhrV1NUMmREM3RYT0VCZGpvMkhzcXNOSnJPWVJ5T1ZqMDRJeTdHa1BjYWxjQ2MteWZ3ekJRX2tzS3ZRYURHUS1zb1lXUQ?oc=5 |  |
| esg | energydaily.co.kr | ESG 공시 '법정 의무화' 추진… 지속가능보고서 제출·검증 의무 강화 - 에너지데일리 | https://news.google.com/rss/articles/CBMickFVX3lxTE41X1hTNERSeFU0a3VfQ3duWjBQVTROSGxxcVFYem9MbVVnaTRfb3JtNGpNSmR2dk1RTmdOd0FPZGJkX2lPaWRnS203R2lYVUw4ZmFPc3JRVEtJUXk1RHVSNGI2YTRnZ3dNc0F3QUoyaW5NQQ?oc=5 |  |
| esg | newstree.kr | 'ESG 공시' 2028년 전격 도입...'자산 10조 이상 상장사' 의무화 - 뉴스;트리 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE54SllKYmtLZ0JmSEMydXBsTmNZVExUSm9wU0JpeUl6bnNCZXg5S1JQdWduMTJ0WjhRbHBxOV9HYVhQbDZRX1dfZTF5YjVESkhaOGR3LVdwaE11ZjlL?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 |  |
| esg | ESG경제 | ESG공시 로드맵 확정 막판 진통...발표 5월 초로 연기 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5Sd0U3WnpadDd3RUJXbGhrb001NW03SWZPYXI5SUlrX3VtVjBucGJDN1lYUU4taEpNSFZEVjVLaDJwRzNOcUwzSTBsV3JzVWoyZ01BeUp4ajhGbmxJVE9kOVB0NmpIa3RkZE1SQw?oc=5 |  |
| esg | edata.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 기후에너지데이터뱅크 | https://news.google.com/rss/articles/CBMiXkFVX3lxTE5ud29WMHQ5RnNleWFLbDR2TFJfSzh2UXlZWjZoWndQUnp6NHI3NWJmaUlfOFgwcXFSM1liQ1E0MEZZZWhDMXRsZjhiT0g2SW91azQybGw1aGVDSUMxZ0E?oc=5 |  |
| esg | thedailyeconomy.kr | ESG 공시, 2028년부터 대폭 확대…자산 10조 이상 코스피 기업 의무화 - https://www.thedailyeconomy.kr/ | https://news.google.com/rss/articles/CBMicEFVX3lxTE1jZm5pSjVVaVN2aEl4YmZuOFI3MkpCYlNrNEtCT1NEYVJJOGdMWnNCOXBCSXpFbG1id2pWZERGTUE3U1hYbl94d0JZQmJHY0NzNnBBdTJqMDcwTExYWGJBZ3pNNkZxMUpYbi1jekdZUjg?oc=5 |  |
| esg | 임팩트온 | 【기획】국내 대기업 99개사 KSSB 전수 분석⑤ - 현대모비스 97점 1위…재무·경영 연계서 격차 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9rTS05cDJWUENMM20tVGJLcDd6Z21Wd3p6TTFFRGZ1YVdzRlh4and5andCSThBQy1wNHFRT3VpMDUzNDBPNUhYb21vb2xLMENKZXlsTWRUeG5sV3BfWXcycWtwNmJFdGtEN2c?oc=5 |  |
| esg | sdgnews.net | 【ESG 공시 대전환④】 ESG는 규제가 아니라 국가 경쟁력…'지속가능성 자본주의' 시대가 열린다 - SDG뉴스 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1HanZVZ1ppRm9vRlBRXzhMMUlRQWtqWUxDTGV4ZzV0LWhTMlhLZE1DM0NsTVIwbmZ4M2pHNC1LUFdJR29PQlBkWXdMQzRCWUJqdzRkWWZ2ZmdVa0hySXNrRGVsaWZoaFnSAWtBVV95cUxOam1qc05UNEQ1Tm1xbWNXVUZRNXpxZThXT1psdnBDWW1yU01UR0ZpVXU5dWpBMS11X243RUlIVmZlYnFpQmdoOGE1Y0NIVWRVUVdKNDk4QnBvVkQyX2hTZFktX3Uta3hlZEQycw?oc=5 |  |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 |  |
| esg | 이데일리 | 이억원 "연결자산 10조 이상 코스피 기업부터 ESG 공시 의무" - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5YTjEwbmxBTWlJZUlPSkVCQ3JaTzJhOEZUUlVDaXh5LUx1cUZVXzE3QVYzUVFoaU1UU2ljMWhlRTZhRHFrODNKWUdRWTdFWUkwTjREanRHaEQwcmNoS0VkZXl1X0ZOTEZWNjI4RTFURTZkcUU?oc=5 |  |
| esg | electimes.com | ESG 공시 전기공사업계도 영향권…대응 필요성↑ - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5zdnpGNTJVMUItUEV0UEJsbU5rZ3M1VkhoNWNpLUw2a0pmcVRIRjNtdk1sVjRlYzVpdktsaWd6NllkdGJHcmU0MDdFWk9GZ1hCVTQwcnRpUXVYdmpXS3ByMjVrQm55TVJFWGVXcNIBcEFVX3lxTFByODduNTdfbVZtZ1BpQUVlYlJ5Tk5jSHN6MkJ4MTd6Vi1oaUpXZ2tkWHI1VExxdHlDZkJRVkluaHdFODhVN2F2NVFqWVFkX2ZMM0xfRUQyRk16WlU5anA3NllfSl9SLXAyN210RmhKblA?oc=5 |  |
| esg | newspim.com | [종합] 당정, ESG공시 법정공시 전환 확정...2028년 107社 대상 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE8tYWZaS1REeTVxSXNDaFFWNWwtZlBnSGY1Uk03M1UwUURhZkFiVlVVZkoxM3BZTzFGNlIxT1hOSGRqLTY5MThLOW1aRjlsTEtQbEZNRTJYMDYxNTFZ?oc=5 |  |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE5XOVdUY012NVZXOUtHdWtzX1JnYTd1aUlOOWJJb2FwSHlqZ1d0N0VWVk50bkMwcGNqbTFxNjhKd2JEeFAzWURZ?oc=5 |  |
| esg | busan.com | 코스피 10조 이상 상장사, 내후년부터 ESG 공시 의무화 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTE1SUzNES21YX3JvS0hjM2RrSDRLMWY3T0VWOVBVV2k0UGZiM1NhalJ5MVltcHBPYmNqYlhPZzBuTDBPdDhBVmZOalo2cm5VVWV4SG5za3pieXg0c0J5OTRyMWp6NS1vOW0tS3V5NWM2ckNBeDhu?oc=5 |  |
| esg | energyprosumer.info | ESG 공시 의무화 대응 전문인력 양성과정 확대 편성 - 에너지프로슈머 | https://news.google.com/rss/articles/CBMiTEFVX3lxTE96QmpoQXJwVXRPcnlwN2VrRFZZZHpzSVZ1RzZiV2haajRTRmxDZklkRGVkVFhmRWszWmM0eE1JLUR1T1JqOTlVSHc3dmM?oc=5 |  |
| esg | seconomy.kr | ESG 공시 2028년 의무화···자산 10조 기업부터 ‘탄소 성적표’ 공개 - 공유경제신문 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9qMnQ5d3NHZXBuaEV3TV9nbUVLaW4zQ0VvN2owejZfcW1ZVHM5WmRVSVlJaV9XcEJFQzBXSE1TTmRjQzA0S1o3bDRkaUQzWnIwcTBXbFhMUTdCRG9lLVhfbG5tb3FqY3RmMUE?oc=5 |  |
| esg | socialimpactnews.net | 경제·환경 단체, ESG 공시 로드맵 '실효성 논란’ 제기…"국제 표준 준수해야” - 소셜임팩트뉴스 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5MWWUxdDB2Zm1PSWJWYUJ5aWZnc1pYWE1iVUJ5ekppZ1NrNUJBT3p2bzFFYUF1X0RCMl9hQ3JXSE5sT0V0alA3TnhTa1F2MVRFWldOckNVbzcyRWZYY1phcmthR3ZKeEN2ZmJraGI3eUU5bk0?oc=5 |  |
| esg | kbthink.com | "ESG 공시, 홍보가 아니라 책임"…2028년 의무화에 재계 '긴장' - KB Think | https://news.google.com/rss/articles/CBMickFVX3lxTE5abVIyYkJSajVjMEhXZ21uVFl3WThTNXlhVDlobDBIWVBZeDBiVzdDTWRzOU4xVFktVFdpWm9WVHJ2WXVZclRKUjNZX3B6NEgyUnhrR0VWZUdwTmZsSWVydEdxU0s5V0ZxNUZUR2ppdGMzQQ?oc=5 |  |
| esg | netzeronews.kr | 한정애 의원, 'ESG 공시 의무화' 법안 발의 - 넷제로뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE53MnVvandUR3lCRjExelB4MUhjVTBtRHU1eXlvVWcxTTFwQndfNzAwbHZXcUJscWN6QTY2VXEzbWpjQXlST3Q5ZkFNVlY1TjNHZEloQ0s0N1daOUtfVVRic1RYTG10ZjEwMFHSAW5BVV95cUxPTnl3czhTNWJlaWxSd0lYV1hJUW5CblZyV0ZfNDhNeGwxYkxGYTBPdnQxV2RUeFFMQ0V1dmgwN1hMOS0yVjh2MVZJMWEzRW0zVC1CZFNmUFlia19reFpQSm5lck5tS3RaM1ppaHU4Zw?oc=5 |  |
| esg | ESG경제 | 하나금융, 공시 넘어 기후금융 관리 강화…KSSB·전환금융 동시 대응 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1IUFFLR0dBamZfTThZako0aEZUZGdSVjQ2eWxLVmRsOGV3WEp0VU11dGVsS1hwR2FNcVRYZkx1a1FoaGFBckVRd1ctdXdrMkRCR1lMSVQwdmwyV0xBQ2dkMFJRVDVzNF9XX0MwWA?oc=5 |  |
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 |  |
| esg | yna.co.kr | 이억원 "연결자산 10조 이상 코스피 상장사부터 ESG 공시의무화" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBoQnh0am0tSlNDaGp3WlZvdHV6LUYyOWZYOXVkcEN4clo0S2dCYUJ4bmxROWJCZU1Sc2NQa2Jtd0hic0txM1NRaHo0dXlOSmxvWU9hWF9pR2VTZWPSAWBBVV95cUxQeGtfQmVIWGQ3ZVlhV2VRM19SbVRMWlUyWHBYMnFVLWlfbTdlaEE0VHpCQlR4dFI4VkxPV3BCNkNWWHlkeWgyTjdDQmtjclBfMWRDbmJETHQ0Q25YbkRJWks?oc=5 |  |
| esg | 임팩트온 | 【클릭ESG】 “3월엔 추정치, 6월엔 정정?”…ESG 공시에 IR 부서가 난색 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9oay01YjlVajVfZ3NoS0V6OHJTbVZaZHJIaTlqQlZzZkhNeWRaeEpQU0tET1l4VVNDdlE1Zm1QM2k4NjdvcGtjbFFtRndwUUtyaFdVdzU4MXlOY2tqMmtkeE1WelRiNVBYTlE?oc=5 |  |
| esg | safetimes.co.kr | ESG 공시 2028년부터 의무화 … '그린워싱' 책임 강화 - 세이프타임즈 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9ya3ltZnBNSTJMSjlvbmdSRHdCV243TTl0WGJXYXhMY0xoN2YteEdETDhIcVhIR2pqLXEzbU9TcmsyZ0pkWTJDOXYxMzVQMTh5TExOcFFhRERVOUV5YmdFNUU3X3YzWlFLS2hpR1Aya9IBc0FVX3lxTE5GYnNFWlNVc0RaN1lWVjJyN2JOdnRuSk5wQ1RpNzdxeHI0WDV5OUo3T0pzbUNQQ0FEb2dQOHR3bXJhQ2syYU52VUJyMEl0MGYxclJnampIZkdVQ01kM1hWVGZwZGJCWTkyNGNyT3dTVlVVSFU?oc=5 |  |
| esg | newsfc.co.kr | '자산 10조' 코스피 상장사부터 ESG공시 의무화 - 금융소비자뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5renNiRTJnemsyc0NGTFdta0M4N1NiY0ZfZDcwbHY1dzJYSXRjaHRxMkpOZXVtT24wdXRYQ0NpVWxLTmdoSllyVFE0REc4cnNqQ0Z5RG5xUnZGMktCUk5McFVkd2hiRnBJekE?oc=5 |  |
| esg | news.mtn.co.kr | ESG 공시 의무화 본궤도…기후·거버넌스 대응 주목 - MTN 머니투데이방송 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1ZYjdkVUM3UXFLc1I4MndSOGxjVlBTLVdzQUUtcEdaaU9JSUU3ZVNIY1RuSHRlX0JCMGZYa2NLQUNISG02UmlCWEYxRnBZblB2ZnJVZHhpcHJZejlDcl9TM2Z1QW0?oc=5 |  |
| esg | ESG경제 | 금융위, 지속가능성 공시 로드맵 이달 발표 목표 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBIM3YtSXZjVkl3M0Rya2hPZWNjUlNTUGFDR0FXbTlfOG9aVkljRE1fUzJtMUxGb0c0UW1wUFpkbDJGME43MTQyU1V2Q2hpcXRRMUd6ZDUwb3doM0FxdzRPaGlUYlcwajhOZktSSg?oc=5 |  |
| esg | 임팩트온 | 【칼럼】기후 공시 의무화, 그 다음은? TISFD로 보는 사회 공시의 미래 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE9zZ3BvOTJGbXQ1YVZSZF96elB5RUV0NGVkYzdNS25reW9teVhZbnk1dzE1RlFKdGdRQm9VSWxiTGNqSmw5Z3NBZzJlWjlrcEhVTDU3SVF3cFdveF9ZbGpFWWJxV25xSkZCeGc?oc=5 |  |
| esg | ESG경제 | [단독] ESG 공시 2028년 법정공시·2029년 검인증 의무화 법안 발의 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5IMl8tNnVMY0FDVnRMSDRSYkEwX29od3lMeXg5Q0tVX0pVbEx0VW42Z0d4TUF5elRZaG12UC1qTUlqeXB0QmFHTEs4LXpnNjluMUNPcnRERDYyQ1l5UjNLZG1DM05aTk84OC1ocQ?oc=5 |  |
| esg | ecofile.kr | 2028년 ‘ESG 의무 공시’... 우리 기업, 무엇을 어떻게 준비해야 하나? - 강찬수의 에코파일 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5VX2FFQ1lVNlIxbGxDT0NUdEN5QUN4cG52aGtZN3lNVTJtWGZPamdkcVVPaGJJRHlLYjJqU2ZZN2hDLW1XZnhmTXRFNkVxWUFpSTJzTF82Uk9oOXc?oc=5 |  |
| esg | news.mtn.co.kr | 염정섭 기후부 녹색전환정책과장 "ESG 공시 기업 부담 낮출 것" [2026 ESG 경제포럼] - MTN 머니투데이방송 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1VS29JSWN0VmEzdXRNbWg0VExwRlYtQ243U3RXTlRoN254dTRtVXctcDkwclcyQndHRGlVZWZZRURKdjRxdkJVaEFPNEd4OHEyR1J4dFktNG9JRkFfTmVkX1ZBME0?oc=5 |  |
| esg | ESG경제 | 국회 정무위서 지속가능성 공시 로드맵 후퇴 지적 나와 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1GcHI4QTVOSEY0VUcxaXJEZzNSWW1wU2VRaEZYNXpwMkZ5Zk41aGpVWm1nSmJQLWdtRDU5dlpaZkwtTG9xNEdjaV80azh6Y09NOGZTbEp2UkRqZ2VLaUk5VzNRSkU2ZlA4c3pXOQ?oc=5 |  |
| esg | 임팩트온 | 【단독】청와대, 국민연금 CIO 긴급면담…ESG 공시로드맵 전면 수정하나 - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5EZEpERUZyWFJJZUd1dDY4blhENWMwajk3SU9kcGVzeDlsUzRLOG5PVkdRUTJEVnZITHNZcXZtNm1RN0l2aXpuZHQ5a25BRkExOVhMODV6czRtNjJDb2htbFJHQ3lrb214Umc?oc=5 |  |
| esg | businesspost.co.kr | [기후경쟁력포럼] 자본시장연구원 송홍선 "ESG 공시는 '공급망 전체 의무화'가 핵심" - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTFBNbzJXbVcwV091eVFlbFc3cEU3YjNBREdCc3dnQkFGblRTRHhHWWFiNlBmMTRnX0FfdU56SHR2djR2aG5XeDd6aFlyajBRQjZRNkpWNzBnWVpKUTB6VGdyRHlWelNGbFRjczBwNUNKR0JvSDA?oc=5 |  |
| esg | ESG경제 | ICGN, 한국 ESG공시 로드맵 환영…“다른 시장에 모범사례로 소개” - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBTLTY2U1hGTkZOWWYteWlnNWR0enZjQUY4YVdIb1hYNEZubmhNaGIyX2NUR2NPZUtsTjdCbVNzYmhmODdjUV9PWGpiQWxHVVNmOGJta0VSbzNmRHFxMV9HcXYxWUNjUzFXZlNtZg?oc=5 |  |
| esg | seouleconews.com | 2028년부터 ESG 공시 의무화…“자산 10조 이상 코스피 상장사부터” - 서울이코노미뉴스 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1uXzhoQlR2VmpvZjBVaGdmZ0VkRHZkSEhOZjBycjVMVjFOb2E0dzFfaUJFTGUxc2NfTThwaE5QZ21GZ0RYSEpmWjhaOFFha1g0OXZ2ZS1IT1J4eEZiWWQ1OUtuMFhWb3BqcHhZUjZB?oc=5 |  |
| esg | bizwnews.com | 'ESG 공시' 의무화 앞둔 제약·바이오, '스코프3' 기준 마련 필요성↑ - 비즈월드 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1LeGhNM2VieHAzRGFlamR3YUJSWUFPbXZMbEhxbUNfQ09rcHJLMWVjdm1MMGk1bGFRTEYzUkplUF96alhzTTZETTgydU00SFF0ZEVGLVpBVlBQVHY4S1otTDdvZ3U5cEhuNVV3?oc=5 |  |
| kifrs | 한국경제 | 회계기준원, 지속가능성기준 자문위원 10명 위촉…공시 이행지원 강화 | https://magazine.hankyung.com/business/article/202608126865b |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성기준 자문위 신임 위원 10명 위촉 | https://www.tfmedia.co.kr/news/article.html?no=206420 |  |
| kifrs | 임팩트온 | 기후위험, 재무제표 주석까지 들어온다…회계기준원, 공시 사례 공개 | http://www.impacton.net/news/articleView.html?idxno=19406 |  |
| kifrs | ESG경제 | 재무공시와 기후공시 연계 강화...회계기준원, 기후위험 공시 사례 제시 | https://www.esgeconomy.com/news/articleView.html?idxno=15878 |  |
| kifrs | tfmedia.co.kr | 회계기준원 IFRS 20 간담회에 에너지 기업 ‘쫑긋’…IASB 부위원장도 참... | https://www.tfmedia.co.kr/news/article.html?no=204787 |  |
| kifrs | 일간NTN | 회계기준원 지속가능성기준위원회, 지속가능성 공시기준 첫번째 세트 의... | http://www.intn.co.kr/news/articleView.html?idxno=2049269 |  |
| kifrs | tfmedia.co.kr | 회계기준원 KSSB, 지속가능성 공시기준 첫 번째 세트 의결 | https://www.tfmedia.co.kr/news/article.html?no=201983 |  |
| kifrs | 매일경제 | 국제회계기준 해석委, 일탈회계 관련 기준개정 필요없다 의견 | https://www.mk.co.kr/article/11489251 |  |
| kifrs | 이데일리 | 한국회계기준원 "국제회계기준 해석위, 일탈회계 극히 예외적…기준개... | http://www.edaily.co.kr/news/newspath.asp?newsid=04060646642397208 |  |
| tax | 일간NTN | [국세 예규] 거래 단계별 총액 세금계산서 각각 발급·수취?...."사실판단... | http://www.intn.co.kr/news/articleView.html?idxno=2052654 |  |
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
| tax | yna.co.kr | 野의원모임 "부동산 세법개정안 수정해야…총선 연계 안돼" - 연합뉴스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5PeE5NMGNMMW94bzdUZi1YV1RkdFdTZjNuTkVPS2VtTGtqdjFBdmc4b2dZdDhwUzFjZDlWaTdKb3dpX0dWcVRjRUdZSDZwRTRXQVh3a2xqOHE0QUhzdWxoRtIBYEFVX3lxTE5PeE5NMGNMMW94bzdUZi1YV1RkdFdTZjNuTkVPS2VtTGtqdjFBdmc4b2dZdDhwUzFjZDlWaTdKb3dpX0dWcVRjRUdZSDZwRTRXQVh3a2xqOHE0QUhzdWxoRg?oc=5 |  |
| tax | everynews.co.kr | 국힘·개혁신당 '수도권 주거 혁신포럼' 의원들 "부동산 세법개정안 전면 수정하라" - 에브리뉴스 EveryNews | https://news.google.com/rss/articles/CBMibkFVX3lxTFBFN2ZhWEk2ZTZqcnNhTWdaY0g3WDl5V09BWkkzZ0EzOWFWdVJPWDlPd1ZNUDZoUGhVSHpnSE41b3c5eWhfVUdESFlzNGhZdzh1QVJLUlk0aVF3cmZJSHNVV3c5Z3hsTnBSbWV6YmxB?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | mobile.newsis.com | 수도권 주거혁신포럼, 이재명정부의 세법개정안 입장문 전달 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTFBsSy1rQkROS293RjhOSWt0VUhZX1VuTDRwMlJfQWk3d3lUbzR6b1Y3MjdKZTJGWkJQVVVoSFpoQXpkYWwzcjM0ZnNoYVUyZmw4UHQ4Z2o4aXNha3J1ZTBneWdiRW50YVVkeElVYVBrRzQ1V3JZRjBNetIBeEFVX3lxTFBsSy1rQkROS293RjhOSWt0VUhZX1VuTDRwMlJfQWk3d3lUbzR6b1Y3MjdKZTJGWkJQVVVoSFpoQXpkYWwzcjM0ZnNoYVUyZmw4UHQ4Z2o4aXNha3J1ZTBneWdiRW50YVVkeElVYVBrRzQ1V3JZRjBNeg?oc=5 |  |
| tax | hankookilbo.com | 野, 이재명 정부 세법 개정안 비판 "다음 총선은 부동산 심판 선거" - 한국일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9vNWpPeUZmQTVWTEhvMDBWY1REc0FuU2w2c3BVRWdqZi1hTnY1LS1nUVdPYU9XcjlSanJTd0l6TjNOZDlfQ0g3b2ZzR0FFZGI2V1Z0bEwyZThNU2xmalp0UzlfQkZ2QXZDRkZNaHVn?oc=5 |  |
| tax | pressian.com | 익산참여연대 "정부 지방교부세법 개정안 철회 촉구…지방과 충분히 협의해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTE0tTFE0Nzd0b0stb1gyNDFJU3hiMllsR2xxdl9KYV9LWi1DWGtLYS1waHo5U0dZbzhLY2tzdU1fblp6RnQ0TTZndGFzOHlxNXFpcjBMSUs0Yl9UN0ZHWDA1bFVxYWlxZmtXdVEw?oc=5 |  |
| tax | news1.kr | 수도권 주거혁신포럼, '정부 세법개정안 수정 요청' - 뉴스1 | https://news.google.com/rss/articles/CBMiS0FVX3lxTFB0OTdJOTBZVGs0VTF0cmdIVXkxWGFHUE5Vb1JGSXZ4RkcxQ21XTy10QVl1Z0RJYmZRS2hILVA4S2pYZ1pUb0Z1bWhPSQ?oc=5 |  |
| tax | mobile.newsis.com | 수도권 주거혁신포럼 재경부 차관에 이재명정부 세법개정안 입장문 전달 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE5BVkdQU3Zxc09DLW5VVlM0ZEU4M1phM001dW1zbmlBYzh3a0dqME1IUzBSeWFjbDVZUHRGWkExanVvNlB4YVIwQXZmc3JYenNrdGxEWmlZR3prV09fS0FJYUU0THZkZTVRV2I3UWplRkNPV0pvWWF6YdIBeEFVX3lxTE5BVkdQU3Zxc09DLW5VVlM0ZEU4M1phM001dW1zbmlBYzh3a0dqME1IUzBSeWFjbDVZUHRGWkExanVvNlB4YVIwQXZmc3JYenNrdGxEWmlZR3prV09fS0FJYUU0THZkZTVRV2I3UWplRkNPV0pvWWF6YQ?oc=5 |  |
| tax | sejungilbo.com | 국민의힘·개혁신당 수도권 의원 모임 “정부 세법 개정안, 국민 이사 발목 잡아…4대 원칙·8대 수정 요구” - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1GWWZObzhTMTA5b2lQbjdNQkFZNTQ1cmlDeVVWbEZHWVk3Y3JjNmk2Nl9MbTFyOG5UcTdNYm9pd3V2TWQ5TklVRVhRTzBhaVZ0b2J4RTl5TGczWVJJcUwxQWEtSFRvcVNCaXBVUg?oc=5 |  |
| tax | yna.co.kr | 수도권주거혁신포럼, 정부 세법개정안 관련 입장발표 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WeXlSSUIwZUVTUEg2amFnNWJqbTRLa0prcFBodkozdVpGRzVTMW44YkVoS0haLU43TDc1Vnh1T2hQdFhCN0JtbENmRl9iNjNHYVJrLTI2Ukt4QkXSAWBBVV95cUxPM3ducDJrU2lIdTJELXlCSk5SSi1xMUx2M1dYODU4NUF3UWR6STF0d21RbWkzTjFoYlVyc2xiNE5aS28wSmczTjVuWldkM0NXWjBRMWgwRGFVUnVvbHVzTE4?oc=5 |  |
| tax | newsis.com | 세법개정안 관련 입장 밝히는 박수민 의원 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1zU1RabUZhMDVpYzNPUG8wXzk0UEtlSXp0d1FCR3hxSk5SQ080OG50SG14VElTWGlPQ3QxZWVSb21EWkNxdjd0dHNIaWFwNFNraDl5V1dRTkYweGFDb292cQ?oc=5 |  |
| tax | mobile.newsis.com | 이재명 정부 세법개정안에 대한 입장 발표 기자회견 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE9RNUVkeUJpOTA5UVoxM2Q3UHdjTEs3Y0ZBT1F3YUdSb0V3cjd0b3lvd0dlM2pRZHF1eWNKN3ZCX292TjU5WkpzTEczemlrbVdKYW90My1wWnhEQnJhVzBPTE8wVDQwYnFoeXJUZUpjc0NDZVNVaTZvMdIBeEFVX3lxTE9RNUVkeUJpOTA5UVoxM2Q3UHdjTEs3Y0ZBT1F3YUdSb0V3cjd0b3lvd0dlM2pRZHF1eWNKN3ZCX292TjU5WkpzTEczemlrbVdKYW90My1wWnhEQnJhVzBPTE8wVDQwYnFoeXJUZUpjc0NDZVNVaTZvMQ?oc=5 |  |
| tax | news1.kr | 재경위원장에게 정부 세법개정안 수정요구서 전달하는 박수민 의원 - 뉴스1 | https://news.google.com/rss/articles/CBMiS0FVX3lxTFA3QmpNY1VFMklHZ2ZQdkpKRlc0Q1VHWFpvcjdnWjd5c29nRlVGcVZGRTRyTXV5SzE0cENMVzhDUU9BaDV2OEpsSVoxaw?oc=5 |  |
| tax | newsis.com | 국힘·개혁신당 '주거혁신포럼', 재경위 조세소위에 세법개정안 수정안 전달 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTFBsR2hwV0w1Sm1CS1hJY2dQSU91Vk1tMEJHZEppMHRRWW5mWGp6eThtam02SDNKYkxFWWI3YU8zc2hmMnAxUlE1N2hwdzV6ZTZ1ZEZLZ3pJdUZFc19BeTQzUNIBeEFVX3lxTFBTQ3RqRHJUdkJKdERiNkRQTWhhMFZZM1gta3M5MU5MSk14Y3RRYmM5d0ZPd2hQcGRiQ3FlZG9VMjJSRlRaNDlkUlYtNkpCTVNSZTM0UEpwYk5WaWZpal9EN0RVdUNYZUEzVmtGUWtkeV9EbjVuVk80MA?oc=5 |  |
| tax | mobile.newsis.com | 세법개정안 입장문 전달하는 수도권 주거혁신포럼 - 뉴시스 | https://news.google.com/rss/articles/CBMieEFVX3lxTE15ZEZlZnkwSFdDUjZfT0tULUR6RnJJQmtrRC1TcDNJb3JvSjk0cTdvdTMxRWtYZWZseVNvZ1diVFU1SjBGNURLNzFodTkxMk9EbnI1WmZvNUZFN0RXWE9JQThubndCZDZsczdrU3JwNm9JOENiSUxQbdIBeEFVX3lxTE15ZEZlZnkwSFdDUjZfT0tULUR6RnJJQmtrRC1TcDNJb3JvSjk0cTdvdTMxRWtYZWZseVNvZ1diVFU1SjBGNURLNzFodTkxMk9EbnI1WmZvNUZFN0RXWE9JQThubndCZDZsczdrU3JwNm9JOENiSUxQbQ?oc=5 |  |
| tax | newsis.com | 정부 세법개정안에 대한 입장 발표 기자회견 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5tRERrc0RPWUs2OERhbzV3V0R4V3ppMEpfSEF0MklRUzAtMEVveGw1VzJlTXJyV3RvQkZFa2N5bmlaZXFlUHdtNnc5QXU2Rjk2RjRTZHd3MkpwNFpxcHNUTA?oc=5 |  |
| tax | vietnam.vn | 국회는 2027년부터 시행되는 3개 세법 개정안을 통과시켰습니다. - Vietnam.vn | https://news.google.com/rss/articles/CBMilgFBVV95cUxQTTYwemJGU2FaVl82ekJuZ3ZEa1ZSRXY5Vmx0VS1nbXVkZGJ1M0psbjdaNTdUZnpKQ1o5dUxycV9sTjdJRHA2bzQybVBKQXlMT1RGbmMyYXFLbHc3cGRLQ2Jja3lnUnpneFVGUUNSZ19zMEZuRXBUemJISkdJejRoQzhIUTI5YzFsUDRBdUJLeTlyRFJQNVE?oc=5 |  |
| tax | naeil.com | “미국-미국령, 세법상 다른 국가” | https://www.naeil.com/news/read/610044?ref=naver |  |
| tax | 조세일보 | 전기차 추가 검토, 비거주 종부세 차등은 고수…정부 세제개편 '촉각' | http://www.joseilbo.com/news/news_read.php?uid=580352&class=7&grp= |  |
| tax | dream.kotra.or.kr | 모로코, 2027년 재정법안 발표, 수입 선납금 도입 등 세제 개편 추진 | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=80&CONTENTS_NO=2&bbsGbn=242&bbsSn=242&pNttSn=245194 |  |
| tax | newsnjoy.or.kr | "법 지키고 싶은데 방법 모르겠다"…개정 세법 앞 해외 선교 현장 고민... | https://www.newsnjoy.or.kr/news/articleView.html?idxno=400920 |  |
| tax | goodnews1.com | 개정세법 시행 9개월째…해외 선교비 집행 여전히 난항 | https://www.goodnews1.com/news/articleView.html?idxno=466437 |  |
| tax | 조세일보 | 세법개정, 소득재분배 효과…부동산은 복잡 [토론회] | http://www.joseilbo.com/news/news_read.php?uid=579256&class=7&grp= |  |
| tax | sisunnews.co.kr | [생활법률_칼럼] 세제개편안 '실거주' 한 끗에 양도세 10억 갈린다?...마... | http://www.sisunnews.co.kr/news/articleView.html?idxno=250148 |  |
| tax | khan.co.kr | “세제개편안 지라시로 받았다”···주거정책 시급한데 청와대 국토비... | https://www.khan.co.kr/article/202611260600051 |  |
| tax | 파이낸셜뉴스 | "내년 봄 줄폐업 쓰나미 온다"...소공연, 노동법·세제 개편 반발 | https://www.fnnews.com/news/202611251504247587 |  |
| tax | 매일경제 | 부동산 세제 개편 정부안에…국회 “매매·전월세 매물 줄어들 우려” | https://www.mk.co.kr/article/12218282 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |

