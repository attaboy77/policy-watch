# 적용 대상 판정 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-10-23 09:18:32 +0900

SPEC-ADDENDUM-6.md §1(적용 대상 판정 게이트)에서 제외된 항목이다.
L1/L2/L3 전 계층 대상 — 공식 소스도 면제되지 않는다(§1-2).
2026-10-08부터 §5 중복 제거(`duplicate_exact`/`similar_news_merged`)와
§1 규제성 게이트(`no_regulatory_signal`)에서 빠진 뉴스도 함께 기록한다.
**과다 필터링 점검용**: 아래 목록 중 실제로는 우리에게 적용되는 항목이
있으면(오제외) 해당 키워드를 `sources/_config.py`의 `APPLICABILITY`에서
빼거나 예외 조건을 추가할 것(§9-2).

| 사유 | 건수 |
|---|---|
| excluded:company_self_activity | 3 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 29 |
| excluded:financial | 3 |
| excluded:foreign_news | 1 |
| excluded:industry_specific | 9 |
| excluded:news_too_old | 34 |
| excluded:no_regulatory_signal | 68 |
| excluded:opinion_piece | 1 |
| excluded:public | 1 |
| excluded:similar_news_merged | 54 |
| excluded:standard_setter_governance | 1 |

## excluded:company_self_activity (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBhZ3dNVjNHQldlUXYzVlltVzgwTGtmb1ZMWlh1SHZwNDBhemYtTkF6c1dPVmxyNHE1dlVuSTg1ck1yUHB4MzVqdlRjQ3R5R296RXc?oc=5 |  |
| kifrs | hani.co.kr | 수출입은행, 회계처리 위반 기업에 여신 54조…“심사·관리 강화해야” - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8xX2I3MlBacWZXSVAtZUxfb3Z3amdGYm1OOVVEVGZtMG92V0VkdnEtTDJ1WVMwSVU3UWVCa0J6bVluTkh0U0luY05Bbm1Vb2tKT0VVbTc1S1R5Mk0wUmFWSUNmcF9CdGs?oc=5 |  |
| esg | hani.co.kr | ESG공시, 공약은 ‘신속 추진’ 로드맵은 ‘늦장 추진’ [왜냐면] - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBQR0NwWHowWHdLZ2lPVG8tdm5fcm9pRm5pc1hVdVh0S2s4U2ZnRUx0VGJ2a2Rxb0xWNjF1V0J5bWJadkdwTnVjUWJDYkNwYjJOZS1OSERWWHlwQW1oWmJwT1V0MTY5cTg?oc=5 |  |

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
| kifrs | core.asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTFBCZkpUZzR6MDU1TFpsb3YzajlvTUt0eW01Mk1WX1FZamlEb0w3UEY3dFdOWjBJQVJkbE12cThnT3pXbWc2WVl3UU1lM2IySEQ1U192b1NnWlNBX2d6UVdJY0d3?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-화학섬유 제조회사의 해외 자회사 동원 매출 허위 계상 [... | http://www.joseilbo.com/news/news_read.php?uid=573578&class=18&grp= |  |
| tax | 조세일보 | 부가세 '0원'이면 세금계산서 발급 안 해도 될까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575492&class=7&grp= |  |
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
| esg | 임팩트온 | KSSB '2030년 병목' 우려…"인증 앞당기고 스코프3 유예 분산해야" | http://www.impacton.net/news/articleView.html?idxno=20126 |  |
| esg | ESG경제 | KSSB 공시, '위험관리'가 핵심인 이유 | https://www.esgeconomy.com/news/articleView.html?idxno=16502 |  |
| esg | 임팩트온 | 【기획】국내 대기업 99개사 KSSB 전수 분석⑤ - 현대모비스 97점 1위…재... | http://www.impacton.net/news/articleView.html?idxno=20092 |  |
| esg | ESG경제 | 하나금융, 공시 넘어 기후금융 관리 강화…KSSB·전환금융 동시 대응 | https://www.esgeconomy.com/news/articleView.html?idxno=16446 |  |
| esg | 임팩트온 | 【기획】국내 대기업 99개사 KSSB 전수 분석④ - 기후 사업기회 94곳 제... | http://www.impacton.net/news/articleView.html?idxno=20037 |  |
| esg | 임팩트온 | 일본 금융청, 인적자본에 주목한 이유..."ESG 공시, 투자자에게 쓸모 있... | http://www.impacton.net/news/articleView.html?idxno=20387 |  |

## excluded:financial (3건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |
| icfr | 서울경제 | 카드·캐피탈사 순환근무 강화…금감원 내부통제 모범규준 정비 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5yMmlfZHJmeGF0N3BFaW0tS1NmZUZXM2dEQXBCUmM5NHV5aEJwcXNCN0Z4bG5ZWlhsaGpuU3FGUDgwQlZ3NTRWM3R4QVRVUUcyVHfSAVNBVV95cUxPZ2JSaTVKelZ2S2NNQTQtNzRyaHQzODQ2THVqOWFOVHhVaEltN3NpdmRfR3VIaG9WZzRXanRaOWdndkJHYUFMWDRXUWh4NS1HWVFoTQ?oc=5 |  |
| esg | segye.com | 증권사 지속가능경영…‘포괄적 ESG 활동’서 본업 연계 ‘지속가능금융... | https://www.segye.com/newsView/20260824517331?OutUrl=naver |  |

## excluded:foreign_news (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 임팩트온 | EU 은행 ESG 공시항목 37% 축소…EBA, XBRL 전산규격 확정 | https://www.impacton.net/news/articleView.html?idxno=30289 |  |

## excluded:industry_specific (9건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | 2025년 제1117호 보험계약 | https://kasb.or.kr/front/board/comm020View.do?boardMngNo=&boardNo=&cmtreadSeq=&seq=494&siteCd=002000000000000 |  |
| kifrs | 한국회계기준원 | 2022년 제1117호 '보험계약'과 제1109호 '금융상품'의 최초 적용 - 비교정보 (제1117호 보험계약) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=316&searchfield=ALL&searchword=%EA%B3%B5%ED%91%9C&s_date_start=2022-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2021년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=300&searchfield=ALL&searchword=1117&s_date_start=&s_date_end= |  |
| kifrs | 한국회계기준원 | 2018년 제1117호 보험계약 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=231&searchfield=ALL&searchword=1117&s_date_start=2018-01-01&s_date_end= |  |
| kifrs | 한국회계기준원 | 2017년 제1104호 ‘보험계약’과 제1109호 '금융상품'의 동시 적용 | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=220&searchfield=ALL&searchword=&s_date_start=2017-12-01&s_date_end=2017-12-31 |  |
| kifrs | 한국회계기준원 | 2015년 건설계약 공시 (제1011호 건설계약, 제1037호 충당부채, 우발부채, 우발자산, 제1115호 고객과의 계약에서 생기는 수익, 제2115호 부동산건설약정) | https://www.kasb.or.kr/front/board/comm020View.do?siteCd=002000000000000&seq=166&searchfield=ALL&searchword=1115&s_date_start=2015-01-01&s_date_end= |  |
| kifrs | tournews21.com | 수협, '재무제표 이면 읽는다'… AI 기반 기업신용분석 심화 교육 - 투어코리아 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBLYWdEalBlZnFWNXJIQXV0ZVR0M3BBSVYyQVRydjBVV1B5NFE5NGFIYXVSMGZRWE1zeVpIaFRzVl9jSzhOWEVHc3BMaVJuckNLQUtyVDJuOG53ekVQdWxfM3U4SU1nMi0wNHBLME9R?oc=5 |  |
| kifrs | hapt.co.kr | ‘공동주택 회계 감리’ 법안에 “옥상옥(屋上屋) 규제” 지적 - 한국아파트신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1zVlZtb2JHeEpyV204Q3FUVTRVU1JiRWswRmZuR3RDUEk0TFVhRlI3OVgzek00MlZwOGlQUmp4elFQRkFjMDh2YThBV05WZlhzeV9SZmhWMEl4WF9DcUZDc0ZwOWh3aEcy?oc=5 |  |
| kifrs | hapt.co.kr | '공동주택 회계 감리' 법안에 "옥상옥(屋上屋) 규제" 지적 | https://www.hapt.co.kr/news/articleView.html?idxno=169530 |  |

## excluded:news_too_old (34건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | 조세일보 | 김현정 "尹 정부, 3년간 신외감법 무력화" - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JdDQ0dDRwdlpDdGhzcnpHZ3hhZ3V3OXFqbXplRXJ5SlFFeU5VWXhlZHg1clRpNHVfQ3B6YXB2RDZBR21GSWlzVnJ4RnY3NDRpaURGVVBBTW5UWWtzQnd3?oc=5 |  |
| icfr | dealsite.co.kr | 여전업권, 금융사고 사라지나…'내부통제 모범규준' 시행 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE01R0VBYjlSdExiWjN3MUE3NFFaUU5zSEJFck1fTUFfZG16WVk1WmZYYXNGRkxSOVlpdWNxV21YSDU0aE80R0RvNVRfbjhTclE?oc=5 |  |
| icfr | fortunekorea.co.kr | 글로벌 기업 깜깜이 실적 드러날까… 금융위 외감법 개선 검토 - 포춘코리아 | https://news.google.com/rss/articles/CBMickFVX3lxTE9GQnJfSm5OMk5pOWVUUC14aFBrQUJUZEJuMnVzLS01MU0tM3M5UzA5RzNPTnVfS21iUzI1QzZxNmU0a09iUG1RU0ZEY1hPdUtzNEFDME9pS1JqdmlFZkhULXUyWXh6ejZ5WU8xWTRmMFhYUdIBdkFVX3lxTE1Md0FkSEpRTmxlZENOUXBSRmtDMzBoZjl6dE1xTi1QcmtsN0d0OTR0NXhyVjdGUGpGSlc3dXpoRnNBQldzcWlzU2NzRlhsdlJieGhUS3o0ZUtFcnFTLWdCdmtDbmdaOVVIR0RRMU10LURKRXBIUlE?oc=5 |  |
| icfr | news.koreanbar.or.kr | 서울변회 “외감법 개정안 발의 환영… 국회 조속한 통과 필요” - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5MdnZCcEdDV09IaWw1VTFJcGVzMlUwMjl5X0V1cm5FMUF6V1VTSnhVZkRZS0NOS2NnUmRlOWtmNTN2Ql9pX3g5RUJRMjhFVlRlcURfbGRNbTF1NlRZdGRaSDV6M2d2MVJlMjl6TXY0MA?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | m.ekn.kr | 금융당국, 여전사 내부통제 모범규준 시행...동일부서 5년 초과근무 금지 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzUkZ2RFlzUjE5OUZ4b3ZxOURwN3ZORVo1UWFXTDBrckdQREVSMmVpbUFkU0VqQzlHNkVVVjBvLWRPUURzenpUNkVjZXBrTlpMblpmMDdmWXFjcnc?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | asiae.co.kr | [단독]기업 부담만 키운 신외감법.."4년간 감사보수 84.1% 올랐지만 품질은 '미미" - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE5RMHZERGlUd2hxZmhqQjV6X3VTcjBBb1c5RG9UU3E3MldUd3VKTUxtTFBMdUt0YXFoYVFmSkJUZU1PdGpUemtDQktTWlpLUnktaEgtM1VPa3lvdUVkejJNbQ?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 매일경제 | "신외감법 시행 3년…외국인 투자자도 기업 투명성 개선 인정" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE4wVlVodXJlT256M0hxZEJESVQtX1J0S0I2aUk5b3VNUlFscHZ4NEhzcU1XQnhxcmlIczFkeVRyalo3X1h0MGNlRV9YS3B4b0k?oc=5 |  |
| icfr | biz.chosun.com | 엇갈리는 신외감법 실효성 평가…“새 정부서 손질해야” - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUzFjNFNPUnBrT3ZjNGFtbDBKVVlQcHFna0puQUZIemxRQ013Z2tNUkRZQW9NQTA4WHhQZlMxYkZ6TmxWb2d4YVg1czBBcWtxTTNmcG52c1d2NDE4TVh1Uy0zekg1YV9mdTVDWDNKc3JyUjFBejlwQUVBWVdIY3pKMkp5ZksxS1ll0gGcAUFVX3lxTFBsa3BrTDBrZTlYWHZjZG1QVk1yRDBDRVFvTU8zbkdqYUppaGcwRmc1Vy1XSDlXRWRxX3RPcnhwSEdoVlNMVTBGMjQzZkxQSmxRdkliNFpiMGNOcHVqN1hzbjFPc0dCTDBCbkJoazEyZHhqRTBzTnd5U0E3cDc4cTlkNnVkTzd5UmppbXlYQ1FaODVmMEZEUTdieWdwYg?oc=5 |  |
| icfr | seoulfn.com | 신외감법, 기업 회계투명성 강화 효과 체감···부정·지배구조는 '과제' - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5YMGxIN0haZUlMVzZveTl0RzRvYlh3OHNMYXhkY19lb1lfcXd4ZWhPY3VZU3ZaRFBKVmswcklsZ3VlRkNPRFByY3AxQml2dVZzVUFsdGZGYzlKbjFWNDJ6STVOdGdCTmV0clE?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | etoday.co.kr | 新외감법 피해 ‘유한책임회사’로…실적 공개 피하는 외국계 자본“[밸류업 결핍과 과잉](하)③ - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE56V0JDSGxxRXBKTlliQWl4VXl3bWtoWHVJcDZkY0xOVWk2d3R4X25iemVFTVNxbzdjSjBqYktYazlZWkwxbk9hOXRaXzBTS1hOTzFBSg?oc=5 |  |
| icfr | joongang.co.kr | [이코노미스트]신(新)외감법에 재계 ‘회계쇼크’ - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE93QzZ4VnROZFduSUtaQ0FZN1YtOUZienl5WjVGRVltSHQ3cUdZdXowTFRHTTYyd2cycnpZNEFKWlh5TUlFaDNOeXB0SGs3ZjNNUzJ0eWdn?oc=5 |  |
| icfr | etoday.co.kr | [관심法] 新외감법 비웃는 외국계기업…유한책임회사 전환 꼼수 막는다 - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wdmN3Unhyc0xVckNseGhEN19nczZCaHMyWHFFZUwwNm9iYzNsSWFjZ3l4YWcyRUt4enFQbHpvMU1ra09yelphYWxWRElMLWtNcThFNw?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | khan.co.kr | 은행권, 내부통제 모범규준 마련...고위험 비예금상품 판매시 손실위험 정확히 설명해야 - 경향신문 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUQ0l5TDdIX0ZNeVBKcWROYW9vZ0liZWJ1bzNGaVZhdHlDdUdYWm1xSWMtWkhQSUJ2LVMyOWQ3NU4xRWhCQ3R3VVBsMWJhMklxYUpJTEhaZ2d0d9IBX0FVX3lxTFA5X21XQUxJSnI1Um9ZaGNScHFsOFYtQ2xRQjMwa0hUQjJoeU5NeWtpVURONTVnSkd0cTYtN2ZZSFpmd0RLTWRRa2NpSzdSdmFzbU9IMG1TT0dzYU9CT3Fz?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |

## excluded:no_regulatory_signal (68건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 일간NTN | 한국회계기준원, IASB 위원 초청 K-IFRS 제1118호 ‘재무제표 표시와 공시’ 투자자 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE43SzV1ZWNkVHBRQzZUUkJ4OW5zQWoyekgtQ2pvZ0FJTXQ4NHVLNjYwa0lPa1RqVHpMemJzRUNxLUJyeXpuT29LWGVJbFNLMWZtelJseHBfNWNoVTBuVVJtb2xoWlpEQ1oyY3c?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑧] 현금흐름표도 함께 바뀐다 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5OWVd5Z0VCYWFKcFRxZ2MydDVicTBORGU5YzhnTFpXQ1NLRFJ0ZHNLVzRKd3N2SEZuQlJqTFZWb1ZidWN2MGJfQmM5ZzdWZmVvVXBTcGNlNFRhT2ZTT2pqYnZ6bEc3aXJv?oc=5 |  |
| kifrs | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QQkdfaGlxSmJXLWJ6ZWxsbmxpZVhYZHJHRWl4V0VIalhpZEJEYXJIUy1CSFQ1MzF3TEM5Y1JWdkxvVmkzZDNQSUpyVTNFSExWS2t6Q01Qem9VTkM1TzVheWpUS3Y?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, 회계기준위원회 비상임위원 1인 선임 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9zc3J5QVRHa2J2SUN1eHkxRkpjZGFBNHFfUHdCZ01VNUJYMmhLRG9FNGRxX19LbmJ4VjZVVUpLcnF1aGZTVEtpZmVuV2FlUzZsc1lobDBRRjEteXJ3ZV83QWtPRm84VmRNdmc?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | 일간NTN | ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5WSGRySVEzMFNUd2RSSHh1Um90bVZmUFZLVGxuZkotbHhwQW5YNllVNUpPVm1kYlJlZnljS2hMTmhFZkZ2WXNzeUh2Q29xbXBCRG9SWVNVM25pMDlkM2NBdG90Z1g2U19ST1E?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원, ‘지속가능성 공시, 새로운 기준의 시대’ 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBPT3dBRVdDZDVhdEFkU1ZZWmx0Z2daaHZkbGtpY3ppa1FWUVpmOGdldEdwcHRHUDM4RmhPOGVuZXNGeE1RVXpid1dnblpnYm1LV216TUlFMkhjazhmeEtwVG5kY0JRcHlwc3c?oc=5 |  |
| kifrs | 일간NTN | 한국회계기준원-한국환경산업기술원, 지속가능성 공시기준 이행지원 세미나 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1Dbm80OFRBdTd1QjFhRDA5dTFRMjNzR3QwaXpkQnBzdllCaVk2SXNVekZ3WVNIaXJhTXhScTF5QTYzS2dTWHlDcW9KcU9ITjJkWmtrTnhSNmN2UWJfS1ExOWhlLUJtZnhUeVE?oc=5 |  |
| kifrs | 일간NTN | 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE1OV0h5TUE1U1VyU0R1eG5FWTkzbmJyM1RrQkpwVkxVQUhfNzFJcmcxTGpGT3U3SUlSWjNsZU1YVVBxQVFyc0Y4MTZRSXhfVDJyaEtoMndWWlhXOWVQMmJpWnRMalQxWjNudWc?oc=5 |  |
| kifrs | 조세일보 | [진단] 제각각 회계기준, '회계기본법'으로 통일되나 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iZExnWDViSmtJa1VsVmpUS3MtTHpYcDNDQU1iWkFWMlBkYi1QMjljcW9za0MwUjE5Vmg4V2dkdDg5blhYZjFrNkhDRmRkbnZ2bjVla0pOR2xMenlvUEc4?oc=5 |  |
| kifrs | 일간NTN | 증선위, 영풍·고려아연 회계기준 위반 적발…감사인지정·과징금 조치 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBVYjhpbjhCWGZMXy11SUxRNkVneDZyek1hclFyTzB1WU1KRkdQRFN6NElBczZpWHN4U3BhRXhwMlYzSUZrSmFiZGhubjRGMll0ZGx3TUlwak9qakpONUZpRjk1OG1fRFk0SlE?oc=5 |  |
| kifrs | 일간NTN | 금융위, 만호제강·의왕백운PF 회계기준 위반 제재…과징금 9억9640만원 부과 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTFBlQnVuWTBYYm5OdDc0Nm40UGVzZmU2TEpUNE1iRkJiZzNDMjRjNlZXbjR2UWpmQXkwRURFemN3U2pvRWo5ZXpIZnNxNE1sdHQxSlNxRG1aM0RmUHR6VjN0SlBrRVg3eTN3bGc?oc=5 |  |
| kifrs | 일간NTN | “공동기업 재무제표 오류 반드시 검토해야”…지분법 평가 오류 사례 공개 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE56cTAyejRleHo1aGMyUWRaTkxPa0NnTFJoODJJTkk1M2hjRkNpV1dWNlMya2tzLVZjVGpzaEJGV1hEdk9JQ19FX2NCQ0N4UlVQOFExSEt5YW9OVTUwNmQzQUNaYk5fRjdpTlE?oc=5 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑥] 두 개의 영업이익 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5FRUxaZW9oYmNpYTBhR3h5d0VOQ0NtQmxKU0NHTTFsc3ltYkhTQURmNmV6TGMwNnBtOE85QjFvT1l5Sk9zRHpUX1lwZUYycTVsY1NYRW9seGpuN0QxaDZqdVZLeGczMk1i?oc=5 |  |
| kifrs | CPA뉴스 | [재무제표 수다떨기] 놓치기 쉬운 핵심 공시, ‘주요사항 보고서’ 핵심 짚어보기 - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFAtc3EzVklob0RPbkdLREg2RUEtbE9aeFBVend3VS1RNzZMeXF6cm1PejFKMFo4c3Jxak0yMHRKNk1xcWVHTzZJYkRPQjY3dFVSY2c4SllrR3NmTklwd25EbFR1QlJ6SUFD?oc=5 |  |
| kifrs | EY한영 | EY한영 설문조사, K-IFRS 제1118호 준비 완료 기업 16%에 불과 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE93b0lTOVNRRHk3am03YUdVT0hoVWQ4WHZfWTI4NFRZVmVidDV3Y2hJNEtneTBIMnFOb2w5WEItT0ZtT1BjMW14U2psY0xqcWd2d19feUs1cUNncnl5Ukg3N180U05ad1FlWGo2TXo4UzcyVVdub2pZSzlxNUdBdzg?oc=5 |  |
| kifrs | PwC | GAAP 2026.06 - PwC | https://news.google.com/rss/articles/CBMiYkFVX3lxTE10WnRURVJhbE95UUxFdUVuVnlWakhCaEhMaXVxczhhdjlnbzJXQ251by1aUEd5NlpHTG9mbkZyMlBGREppZk9xYXNpVDRBc25ZdkhOVFgxQlBidTVIR3J4UzdR?oc=5 |  |
| kifrs | 파이낸셜뉴스 | "재무제표보다 현장 기술력"...기보, 소공인 전용 기술평가모형 개발 추진 - 파이낸셜뉴스 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5jNVNRZ3dQUkdpTFJJS01aWktfVHZOTmtOZWhjc01fN0VMYWRNNWhIR2VIWXg4T2k4aFdBcnpUYUdrZ1N2OFBwV1BWZnBOeWtfWkxwN3ZGaWFKUQ?oc=5 |  |
| kifrs | 한국경제 | ‘몸값 6000억원?’…중앙일보 진짜 가격표는 [재무제표 AI 독해] - 한경매거진 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBWY2JySGZfamQ4NmJGQ0U3cTVMaTRzeXNYT1AzUklyZnlJNnBXYnZ4elNfN3k3QU5ZRl96bVhRX19vd1htWEZUeVVwejlhMGNzcGtxMC1jRXhYbEhwSXNCQ01xTy1GR0k?oc=5 |  |
| kifrs | 이데일리 | IFRS18에 코스닥 환기종목 변수…5년 연속 적자 판정 달라지나 - 이데일리 | https://news.google.com/rss/articles/CBMigAFBVV95cUxOY3VxY0RvRjliem5HMnN0UXhFcXM3ek5TSElSMEo5ZU9BLWpiVllHcVhIcmVzVndLZ3lXUkFxbUNYdVJ2b0NQdmVfSFZSUEkzQWlHS2FuYzBBRjRiSHM4TjNNbmYwXzB0cXlmSFhaMXFWaVVfRjM2NVJXTWotbFFzYQ?oc=5 |  |
| kifrs | 서울경제 | 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE41YkVzeThWTUVTaGpkSnBmRDVfWVprSTY2UncyajZDOUpiZFVYTDN5eENqM3ZQcENzZm80RjZwTVNxalhNaWQ3bDRkYTV3S1JnNFHSAVNBVV95cUxOSy1rVnBqeks0alRJRUZOaGVubDNZSmpBYU9TaTY0ME5RT1NnLUtUZjdfZGp5QkVvSTNQMmRvS2pUTlpJR2RXYlcxTklYNW5wNlVxRQ?oc=5 |  |
| kifrs | 매일경제 | “가만히 있는데 장부에 118억 더 찍혔네요”…회계사에 따지면 안됩니다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTFBMRVFIR3VudmJIQ05Ca2Vqcnc5UTlIbUpGMHFNZUdJR1Q2NGdkd3VqbmZmNWVWZG9yd0NEcVZxRWJKRVdmR3RyNUNmcEk5U2xIUXc?oc=5 |  |
| kifrs | m.ekn.kr | [기후경영 포럼] 윤나영 한국회계기준원 팀장 “온실가스 배출량 측정, 조직경계·산정기준부터 따져야” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBwSENJcGZ1alVPdzFhZEREMjZSamRuYTFyLUJYS2xhX25zd1RIXzd2SjZzQlVyZVBqQXp2VnQyUkNTSXNEamFuZU9UaGQzZ1lDQVJXbXpRWXp5TEE?oc=5 |  |
| kifrs | dailybrief.co.kr | 빗썸, VIP고객에 1.4억 카드 판촉비 회계처리…"탈세 조사해야" - 데일리브리프 | https://news.google.com/rss/articles/CBMibkFVX3lxTE56a1N5Zm1ZQ2UyMVg4cUQtWjQyVExvMEFNbjRNZmE5UjZGMjQ2LWJoZzc4YXg2b21HWWNya0g5eDRMbmttOFo3XzQwcTI1WGE4QUlocTRDa0hHWFBDaHAtMUJWbHlTc3FQV21LSm1B?oc=5 |  |
| kifrs | dailyguard.co.kr | 노원구의회, 2025년 결산 심사 마무리...집행부 '예비비 집행·239억 회계처리 문제' 도마 - 더 데일리가드 | https://news.google.com/rss/articles/CBMicEFVX3lxTE9laXlwcWFVd3FzSF9wU3oya2NGMFlsUVdpTHNDTGtkbkNiVllVQ0FSUWpNbWVmYzRaSHI1NUVLaU4tX01xN0wwaHRuZ3phVE5BU2pZT0tXYU5fZ0t2cU8yOS1Wb2R4WmFDX243MzZpbmI?oc=5 |  |
| kifrs | newsdy.co.kr | 담양군, 회계 실무교육 실시… 예산 집행·회계처리 역량 높여 - 담양군민신문 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5LRnJacEVwMU1XWkRuMzQzek9aaHVSNlVwak1aNVFUR29Ia2VXWWEtR3U1ZE9PWDUyaWJnd3dUVDJSc0NqbXZZRVh1RVJfQmZzZW9NeVRaZ0E0cWNkR2c3ZnVVRmh5cWNfU0E?oc=5 |  |
| kifrs | news.tf.co.kr | 유안타증권, 개인투자자 대상 'Y투자교실' 개최…재무제표 분석부터 절세까지 - 더팩트 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE0yUEc5WnNtMGVuYkN1Zm00VlBrUHE4UmpBUmp0eS1nSGJNV1o5MkhycGhGaktwWUM0Wm13dkN3b05PbmRPbWpRcW5Yd0YwYnBZTzNyLTdxZnp4UdIBVEFVX3lxTE1lUV96SHkzRm5VUlQycXRFcFBoYjQ3NDlMYnRTNjZpd3p5NGdTeHhFRTNfakVuY292OG1WbXNtU3ZFZUg0aGU1UkZQYVprc2NQVXB1Ug?oc=5 |  |
| kifrs | crowe.com | K-IFRS 제1118호 영향 관련 사전 주석공시 모범사례 마련 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE13d18yem9ReWp0R1hMQXhJaVctcGpyTzgxRm9XSXBNOXZxcnNZaDhfZVgzajBhR0gwNm9EQnBmZElrWWhsQ01mbE05dzc5NmVWbksxVVE5STk?oc=5 |  |
| kifrs | m.ekn.kr | [기후경영 포럼] “기후공시, 탄소배출량 넘어 기업의 대응 전략·재무 영향 담아야” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9PV1NmaHVhQ29pZ01WaXRzeVdCZmhOWGdGZE1ORGdxTHdTU0NqUkFmN3ltQmo1d2xnSEtvbC1qM2NqTWVmUk56NDRSanFMWXVQbW5pdzJhMmpvNzA?oc=5 |  |
| kifrs | m-i.kr | 안산시, 복식부기 회계처리 정확성 높인다…11월까지 컨설팅 추진 - 매일일보 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5kMXpHWEhyOUpvVzVwbmM0RFQ1ZGgtNjFTY1VETHU3RDlQd1d5MmExWDMzS0NYUGlEZlYtQzhEQW16Y015UnQ5X2IwbjBRWU1rLWg4R0xnUUZZTk9WR1N4RUs4OGE?oc=5 |  |
| kifrs | joongang.co.kr | 기준 바꾸니 27조 흑자가 적자로…새 회계기준에 지주사 ‘비상’ - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE4ybk5IZk1jY3dMRTE3a21sWnlBZ0RYcVpPYnduMW56UzJhek1fellTTEdkMmJSelc1LVBIME55clJXYko5Z0lnbkpEakVFbmVkdmdzbHB3?oc=5 |  |
| kifrs | insnews.co.kr | 내년부터 영업손익 표시 기준 변경… 기업 실적 비교 달라져 - 한국보험신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBrQTBtRWFpSWZSTUV4ZTU4LVVmV3NoZlVzNXlSeFJXblQ0WG93WjVUMFMzSXhjVllVWll2RWpBc1YwMHlJZTgzVlZhelZUQlYyWXAtUXpJOTA0U0FGY2dUWEM1Vk1kWG9kZ1NMYllqTdIBb0FVX3lxTFBrQTBtRWFpSWZSTUV4ZTU4LVVmV3NoZlVzNXlSeFJXblQ0WG93WjVUMFMzSXhjVllVWll2RWpBc1YwMHlJZTgzVlZhelZUQlYyWXAtUXpJOTA0U0FGY2dUWEM1Vk1kWG9kZ1NMYllqTQ?oc=5 |  |
| kifrs | news.bizwatch.co.kr | [SFS 2.0]재무제표 밖 거래망까지 읽는다…AI가 넓힌 신용평가 - 비즈워치 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBBOFR0QWktVXlHMWpfSjFlTVEzTk1kTm9QQzhjN2VTYWpOVFcwVnlMUnNxNXZ5MzRqOWJBNnY0aWlPY2JWZ2NGNWdkV3hlMXpRdmxjQmtucVc3aHVDRVgxMHlVNGJhRGtQVldr?oc=5 |  |
| kifrs | lawtimes.co.kr | 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE05MDRqekxIcGRMRFZhMmdwVnM0OWZ3R2lMRGhka0NDWU1EblRBMFplYXc2bldHUDJvMnJtaG0tSnFaX2U3ckt1WXY1U2FxNk1zVm1yb0lUb09Mb2o5elV4S3ZNWVRfSUJPdmxvRHhR0gFyQVVfeXFMUFhvWmtXbVVXc2lzOTFnYnp6bGFkWnc3T2kzcC03bFVzam5Sb25NNWZsSmt6Q29WVmUyZ0EtYVY4SC1IVlB5QmtXTVIxR005WDVzdDYwcDhramd6dXRGOGh5eHdZRnVrTTBoYV9FNzBFbnVn?oc=5 |  |
| kifrs | yna.co.kr | 2025년 재무제표 '비적정' 상장사 53개…전년대비 소폭 감소 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMOWoySmx2N1Voc05Ba04zNC1ZYzBBZ1A5aUdXNzEzVms5N2hyTHA1ald3Zjc5dnRNRHh3LU9XLWtmTWJfR2Q5eV9aSzBnQVBCX3VHTzNsUnNKT2PSAWBBVV95cUxPTmZ3M2J3VVctVkFTTmRhU01tZkRBTkROS3Rmb195V1R6OTJrYjRUNG1uUXh3Z29sTkJXRDhpaS1ZTUQ1ZkdrRHZJdnV5SDhCRktQQ1JYaWtEWlBTTm1od1I?oc=5 |  |
| kifrs | news.bizwatch.co.kr | 회계감리 중징계 영풍…내부통제 시스템 허점 논란 - 비즈워치 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5aNFQ0V2JXaVMtOVBoRVNNV2RZNE1GYS1mcE1Gd0J2NDA2YnhGaUV3cFJmZldxRDh3eUdNdkxvRktUNEFkQ1NkMVFCaVpBZG9TenNBYVR0Y09KUkZnS0poeUxQNjhEaXhKVVVSVg?oc=5 |  |
| kifrs | yna.co.kr | 감사 전 재무제표 제출 위반 76건…전년보다 24건↑ - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lODhfd3R3TUpXOFZneW5tMjJ0OEVEeXBMWExHS1F1MzNOdExVUlNsdTFwYVpFZTRxLXNTZzZoZzRmQnhhYW5ZZlhtUjJJM1M4YXA0ZWNCbU5ubzjSAWBBVV95cUxNUWMwYlBCMlpvS2R1a2dOaVdCYkRqcE04YXNwb0JCSC0xb3NSc05OM194Z2dCcVhiSFU1elMzQklVZHNCc2dtRG1wMk5kSTJmMW1rVWZWdDFQcjZrZFVRTno?oc=5 |  |
| kifrs | biz.chosun.com | 감사전 재무제표 안 낸 기업 76곳… 1년 새 46% 급증 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxQdEUzbGllWjZjQjdvMUF6Zlp6c0lZWmVXLUdkN1lmV0t6cDU4bDBLM2lYZl8xbk0yVjBaQnZFSWwwcGZIZ1UtUllaNDRpaHU5YXJWdHJBYXlwcU5DUU1lLWVDZXE5VVpHNE5QcnlNWHU1cjl0cFJHMkNqSEI3SUtfZTh0T0FpMmFT0gGcAUFVX3lxTE1yVFhFN1pTU2dHYTBZUWJTMEJDY29Zb00yMjJjN0FDTlJtLVdCeFJsZmh5bXVtWkZ2S3hrYXptVExzMC0zNVNuUkVZa21nVUoyVk5vVEpyUU1neWlROXY1bkdPQkg1OEZuT0ZZVDc4Z0h3alJPWUFuRW5QT1JEajhFZVBWNGhmMzJ1Vm5zYzhhaWtRNHdwSVBUWEpCUA?oc=5 |  |
| kifrs | hapt.co.kr | 승강기 교체부터 고철 매각까지 세무･회계처리 - 한국아파트신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9mSmFsQnZBTmRvNzZha0dudUFIN2I4Q3lwWTJleVlqTERKaTdIUklzT1dobzA5dGViTWxmNlFGOW01dnJycmpYZUhudHNMdV9TbGhoUy1wSnF1MG0yTjZvTUFDS2U0bGY4?oc=5 |  |
| kifrs | news.kbs.co.kr | 금양, 회계처리 위반…“행정소송 맞대응” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE8yTHV4QVF4ODRCdkZraVFaV0ljWkV1Wk5QOFVQRUF3SEZRaXhrNll0bU9ONkxuZTBzaHhNOUtLTDRXVFR5bFZMWWlTM21YSHRrOVJaTHlabWphRzg?oc=5 |  |
| kifrs | yna.co.kr | 증선위, '회계기준 위반' 금양에 감사인지정·과징금 조치(종합2보) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE84VG44Qzl6Wm1UcmV6LUVNNWFhXzNSdXlDLXE0bmhrLXBLSWpCQldRYy1uTkxMY1V1WWVmRFdLcmxnZUZGdHRXU3hVTzY1akhNbGFGUXVhM0Z5dWvSAWBBVV95cUxQT0RISWQycmFQX2pXQXZtN3g2Wk9xYm12OURoVXduNk1zUmNmUllsRGV0cG14bFJxU1c4bGFIQy1QNGZzZjJMQ180b1BoSHBJT2d6NGliMUJvS1N4dnRpRHc?oc=5 |  |
| kifrs | news.einfomax.co.kr | 증선위, '회계처리 위반' 해태제과에 감사인 지정 조치 - 연합인포맥스 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBzREN4d0RmcDJBMXFhZ3BfZVVTRXJOalhqNmNYYVRoUFNzQmJoNHdqb3pmaXVqX3RGTlpMbGVYUGh1dGNHbEpBbXBmQkE3cEI0dVFMS05DaHdjUkswWTk3Vy1qam5vYXhpckdud2xoX1k?oc=5 |  |
| kifrs | tfmedia.co.kr | 20년 회계감리 손본다…코스피 10년·코스닥 5년 검토 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE9JTUozdU44YWVPcHIxbFdVVS0yZXBQMHpxVVEtTGN6M2FSSU5QTVd0c2xSU0djRkJPZ1VNdEVrb2dNOHg0Y0FlNE4yWXo2R2hQd2hSQ3VTZ1c1bFBlMlowZ0wxTQ?oc=5 |  |
| kifrs | news.kbs.co.kr | 잦은 사업 이월, ‘회계처리 부적정’ 도마 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE5tQWI5RHBpTVRkQWY4TEhWVXdJek5VRG50QTBTLW5ZTU4yNDVoUW9wRWtXZldMdXBjMldnSkxzVDV2blFoU1RpMndUX0pWdTNDVDlPYXB5T05RY2s?oc=5 |  |
| kifrs | ajunews.com | 중앙그룹 채권투자자들, 금감원에 중앙그룹 5개사 회계 감리 요청 | https://www.ajunews.com/view/20260726212534288 |  |
| esg | 한국세정신문 | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.taxtimes.co.kr/news/article.html?no=277314 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 머니투데이 | '납 배출 주사'로 급락한 DN오토 주식…與박상혁 "ESG공시 법정화 필요" | https://www.mt.co.kr/politics/2026/10/20/2026102015130134030 |  |
| esg | 머니투데이 | 상장협, ESG 공시 대비해 실무자 쟁점 미리 챙긴다 | https://www.mt.co.kr/stock/2026/10/19/2026101913585170575 |  |
| esg | 한국경제 | ESG 공시 법제화 초읽기…기업 대응 역량 키운다 | https://magazine.hankyung.com/business/article/202610066517b |  |
| esg | 한국경제 | ESG 공시 법제화 대응 돕는다…실전 실무에서 데이터 플랫폼 체험까지 | https://magazine.hankyung.com/business/article/202609217807b |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | dt.co.kr | [기획] “美·EU보다 더 빨리”… ‘발등의 불’ 된 ESG 공시 | https://www.dt.co.kr/article/12090224?ref=naver |  |
| esg | energydaily.co.kr | 한전KDN, 지속가능경영 10년의 성과와 미래 전략을 담다 | https://www.energydaily.co.kr/news/articleView.html?idxno=204207 |  |
| esg | newscj.com | 충남북부상의, 지역기업 ESG 공시·규제 대응 지원 | https://www.newscj.com/news/articleView.html?idxno=3441094 |  |
| esg | straightnews.co.kr | ESG 공시 확대에 협력사도 대응…동아쏘시오그룹, 공급망 교육 | https://www.straightnews.co.kr/news/articleView.html?idxno=312824 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| esg | greened.kr | [ESG 리더스] 장성백 현대차증권 지속가능경영팀장 "금융배출량 자체 배... | https://www.greened.kr/news/articleView.html?idxno=350736 |  |
| esg | kyeonggi.com | [생각 더하기] ESG 공시상 중요성이해와 중대재해 예방 | https://www.kyeonggi.com/article/20260917580266 |  |
| esg | hansbiz.co.kr | [ESG 칼럼]ESG공시, 기후 넘어 자연과 사람으로 | http://www.hansbiz.co.kr/news/articleView.html?idxno=860684 |  |
| icfr | betanews.net | [로컬 게시판] 남부발전, '내부통제와 내부회계관리제도 전문교육' | https://www.betanews.net/article/view/beta202610220148 |  |
| icfr | datatooza.com | OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 | https://news.google.com/rss/articles/CBMic0FVX3lxTE85anpGNUU3UzhJX2JBTDA1dFRqRHhkQ2dhdXZGZ0ZVcHRkVU9Gc29Ca1hXWnNSMUYwOEJEWlR3NmFlblRvSmtIVHhwemFzVFpockFoWFFla0VfUmVVekFaRXAwZEUxSGc4RGt2Y1M4WmFHRmM?oc=5 |  |
| icfr | daily.hankooki.com | 남부발전, 경영진·이사진 대상 내부통제·회계관리 교육 진행 | https://daily.hankooki.com/news/articleView.html?idxno=1417630 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| tax | cctimes.kr | 지방세제 개편 입법 착수 … `재정난' 충북 단비될까 | http://www.cctimes.kr/news/articleView.html?idxno=930631 |  |
| tax | dailypharm.com | 카드 세액공제 연 500만원 축소…매약 매출 높은 약국 부담 - 데일리팜 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1ZakNScUpnQ09qa0VVX2RlSVlwRFltUmwxczAxOGdNb3h1Nlh1Yl9OalRvakt2dTJQdERPMU1wOWFaYWtaR0xBby00MEdVODdQNVdEU1Bn?oc=5 |  |

## excluded:opinion_piece (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | hellot.net | [ESG 칼럼] 미뤄졌던 ESG 공시 의무화, 2028년부터 단계적 시행 - 헬로티 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BdXB6anZGSm9NNDRObEsyRjJJbGJlOUxnWk8yOFVUVXRsLTAxU0FMUDMwMXo1TXZzakNuanlEeHBaWnpFLXRWR3lXZ0ZJemhIcEo1MDVDX3JONFNvN20w?oc=5 |  |

## excluded:public (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | lcnews.co.kr | [공기업 Pick] 한전KDN·한국도로공사, 지속가능경영 고도화와 스마트 인... | https://www.lcnews.co.kr/news/articleView.html?idxno=209951 |  |

## excluded:similar_news_merged (54건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE5KOThWQnpwcDE0U2VwYTh0enJFalI0RlZHaGRHcUtIWkVLeFhRQzhjYkFKc1NQdmZvTF9iWmxjakowNWVmZ0hFN21FZDhncjNLc3RsbmdlVTZYVk5TYmdVZnJTXzJBS1gzaXZONFZPWGN6R28?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | joseplus.com | 회계기준원, 김정일 대한상의 상근부회장 지속가능성기준위 비상임위원에 선임 - 조세플러스 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFBWQUt1dDZwX0VzYmZtTTBLcDhpQ1pJZWFrdzhwSW5oTF9sRUV6SDVKSVNqenNEV2o4S2VrdVV5b0d2dmE1RGw3c2hrQzZsRmY3OXZTaXNUcHXSAVNBVV95cUxQTWZfbl9xdnBpZ0I3aWgwSm9HN2t5SVRQaWluVjYycU0xMmZ4WDhHcEJFcktlV25Lc3Voa25iU3BNVkUtaGhENkxfbG1XUEdYUG1Gdw?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | seoulfn.com | 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE51SEdGb0VqY2lPZEJIbFZVNHp4QmR5X18tb1NBMlpxOThhU2pTWFgtS3FtaFhZdzk2eGJ5cU5kcjVnMFM2d19laXNxTG5jYm9HUElEMXdwbml1VWFxTGlfMXRuejlocFVNT2c?oc=5 | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 - 한국세정신문 |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중심으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFBQcFZGSDROYXJzRmRvdFlZOHJfbDNQME56R1plWDNLM3c3YUU5bmJWUDhpYXVHdU05YzdGOUxLbl9ma3hUeTJCSnpTUUt3LVk5dl9IY1Y3TFJvV082d1Nz?oc=5 | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | 머니투데이 | 금융당국, 허위로 매출 부풀린 해태제과에 9억원대 과징금 - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5NU0l5NHY0TnZvOU5zZmdzUWNEZEZzcmRhUWxTdXpMb0g3UjY2ckVtb3J2Qm1Rc2Z6MmkzcFB3dlVFUU80Y2FZTnM3dlNhU1p3VEpTV1g3M1c1a25nTzdrX0VaSzR1bWpH0gFuQVVfeXFMUG1CRzlWN21wY1ZRVzFMVmg0UnNyWmdtS2lheElkMENrdjVJS2c0a2FNeVBuNUN2d2xhN3M1U2pjSHZwckp2V3NDTWtKMnF6ZUtuUUZwcU1BU3V0WHhER0owYUc4Vk5ZMFpUOXVwOVE?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | sentv.co.kr | 금융위, 해태제과식품 회계처리기준 위반에 과징금 약 13억원 부과 - 서울경제TV | https://news.google.com/rss/articles/CBMiZEFVX3lxTFAtX2dCMTRIT3lLOU1qUWtVd2l3RVBWbjBHaURXMHowbnhsSmdGSS1qd24tOVZkV09BSkVMTzdFTm1pdTVweFl6ZzBNVG9KdkVIQ2xuWW85TWRPanlGbFlSSlVldUg?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | core.asiae.co.kr | 금융위, '회계처리기준 위반' 해태제과식품에 9억 과징금·감사인지정 3년 - 아시아경제 | https://news.google.com/rss/articles/CBMiYkFVX3lxTE51NzR2NVdEeWlqZ2NCM1llbXpDdF9kV0IwSmQzUTI2RVR4SFY0dEN0RmFpWEY5cFMwQnNWSnRPeVlJLWY0M25kcHZMT1kxZ0lqekJJeFd1eDRIVEVhNjVhUl9B?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | dailian.co.kr | 금융위, 해태제과에 회계처리기준 위반 과징금 9.3억 부과 - 데일리안 | https://news.google.com/rss/articles/CBMiowJBVV95cUxQb1IzQXJja2M3eFF3bkxudzZMbWcwalpFTmdyVDAtQ2xpNHZmQi03ZVZhUnZoZjZDWTZzZ3BDSGF0cjAwTnpELUh5UjZXUmxnT0dDb3BNYjVxME9pRWpUeDN4ZDNDSDVpWGRVclpwWFFDbVZZbHRYY3NmRzA1TEwyU0ZDdWV5YzlkV1lhMHZjWm1KeEVoUm5tNHlPOU1xWVk5b2p6TVFoMDFSYS0zRWF4QjZOaERlUU5wSGlFT2lKTnZQbjViSkV4Vkl5cGwtencxakRwWXBYUjZrMWN6X2xXQzhoQ0hJMXR2V1F2YU53di1EcnQ0d0dDLWtKU09FU3c1aGNQeDRGSG9pSWNSc1pTLTBtT1ZqVWZKM09XdzBpdmthbXM?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | ilemonde.com | 회계처리 위반 해태제과, 과징금 13억 부과 - 르몽드디플로마티크 | https://news.google.com/rss/articles/CBMiakFVX3lxTE80eXlxMXdTYzVJTlhVTEJEMThxdTh6RUpqX2NBNnp4SXlXaW9JX0Q3WWEwdFRabGRCRkN1d0hsMC01NzAxN05FNkY1c0RiVTRUc2k5VTkyOVNTbVVIdXJFVjJDMDBld2dTbXfSAW5BVV95cUxQa0F2WS1Zd0p6UEw1VXpCWnBDT3NOZW5KdVZuRm5tOHRUSllSb1kwakZSVnNoQktlY1Q0UjJQV040dGIxZjZwRER1MVZUcHlHWXo3ZUlvQVFaUnh1ejJpczV1QXVxTk9ZOGktcC1tdw?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | seoultimes.news | 금융위, 해태제과식품 530억원 회계처리 위반 적발...과징금 13억원 부과 - 서울타임즈뉴스 | https://news.google.com/rss/articles/CBMia0FVX3lxTFB1M09XWTdwbm9OMnc2S0hTS2lHdmJhWmhRUkVXSFZ4blZEM3N2OXp6ak5BZUhEbTM3TXBlZ0Q3emFSZF84VkNiazBFUFM2U3diQXZSXzhWcVZqLVJFTWNMODN2VEp1dkRhVjg4?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | yna.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBJYkpxaXBTcjhUQkZPcHVfay1mQnptQXRhMklhUVNBQ3VSZy1WYWpzeVp4eGdkMmF2bHhDclR6ZHMtMnNJQlNWYVFmb2tsWWxYYndaTEFrcVVHZUnSAWBBVV95cUxPelVLaldNY3hnelFDQzFqaVY0UDBDX3EwY2xkU0QzS3JBc0JBUm5STlFaVlhxRnlpN0FmbXNSQjdEd28zTXFCQWctb2JYN3JLWGZQcUZFdEM3MzJtOFhTTlk?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | tfmedia.co.kr | 금융위, '회계처리 위반' 해태제과에 9억 과징금·감사인지정 3년 - 조세금융신문 | https://news.google.com/rss/articles/CBMiY0FVX3lxTE1nVW9jUjhaYTVIc1p6ZjFubzYwSEFsUDl4Zkw3dkpKN2hoeHJoUHFBVDFVa3kwZm5XSEpwM0lXcUd3ZjRiZkhVcThYYlNRa0dfOFZCdUFENUpLVGFWclp2UTNvcw?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | news1.kr | 금융위, '회계처리 위반' 해태제과에 과징금 13억원 부과 - 뉴스1 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE1Bb0E2bi1kT0MzVUQzUW5mWHBIU1NKOVM5a29NNW5rMGNWY3ZNS3pmQVJTTmV3SzR3QlhHYlFPUEV0dXZibGdwZjFDUG9xVDBLVEpuWDUwcDJlaGVk?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | news.sbs.co.kr | 금융위, '회계처리 위반' 해태제과·관계자들에 13억 과징금 - news.sbs.co.kr | https://news.google.com/rss/articles/CBMiZkFVX3lxTE9yVWJ2YUNlLURCOV9pa2M4Rk1EbUFxVThPZzliTEhLd1dOUnZFY1B4YWs1SDhRM0JDZGlpSmlqUUhlU3VSZHpMcGROSzNKa3ppYUVyMTJoekV5YTFUcm95S3pSVTI1dw?oc=5 | → 대표: ‘매출 부풀리기’ 해태제과, 과징금 13억 ‘직격탄’…금융위, 530억 과대계상에 중징계 - Daily NTN |
| kifrs | 조세일보 | 영업이익 새 판 짠다…K-IFRS 1118호 시행 석 달 앞으로 - 조세일보 | https://news.google.com/rss/articles/CBMiX0FVX3lxTFB0MnpUYjZVSVNaY2VaT21MQUJDY0Z1N21nWEtCbVNZVWxZNmE3ZTlrcEI3VFdEb2dlZWpVZ0k1bXVzNlBYUENtcnJSUVlLTWFhNjNzZTZyQmphNy13dmtz?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | tfmedia.co.kr | 회계기준원, 내년 K-IFRS 제1118호 시행…투자자들에 주요이슈 설명 | https://www.tfmedia.co.kr/news/article.html?no=208000 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | junggi.co.kr | 2027년 K-IFRS 제1118호 시행…기업, 도입 점검 필요 - 중기이코노미 | https://news.google.com/rss/articles/CBMiakFVX3lxTE41S2l3VmRscy1LUlowVVNJaW5BdExCQ3FIQ0Y1N3Zlb0FhSW1qSXpBVzZSVXRpRFJzdHNKN2RqTlhxSEk0Rm9SSkpRaks0d0JHNV9VVDFBUGZYeE9keW5WNVVtM3hMdGhVVHc?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | mediapen.com | 'K-IFRS 제1118호' 내년 본격 시행…금감원 "기업들 준비상황 점검해야" - 미디어펜 | https://news.google.com/rss/articles/CBMiVEFVX3lxTFBYS3hIc2t3aEZ4bFhJWU12aF9fTjQwZnd4UGttSDgtaHRLbGkyd1UtdU5haFFSZGJGT0xzUGtfREphOEVLQnlESm11X0gxQ3lXd0c4eNIBWEFVX3lxTE5kNXVjbk5qaGlDLVA0MTNvZ0ZsMEhCTzJsSXpXa1BoZGUtQ3RzM05RUnVTd1RNLWhjTjM5Zms5LW1KdGdtekdwb3QyVjZlTzNUYTY5WERRaTU?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" - 글로벌이코노믹 | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPOGFldExqZEFIdGQycE1SbC05ZHV2Z1JaajVGU2YwOWtuSkJ2bmc5aFFSQmJEdGlSVG91anA4RXIyanNELXJDOEd3bkVFclVVRGlSa3E5V01Tb3lyOFZOVVpzQjZYSHo0MUlzSjlEd3dBeTdKeHh5dHlGNUc0VEcxZzFIdW5HRHhB?oc=5 | → 대표: 영업손익 개념 바뀐다…2027년 ‘K-IFRS 제1118호’ 시행 3개월 앞으로 - Daily NTN |
| kifrs | 일간NTN | 금감원, 감사前 재무제표 제출 위반 76건 적발…9개사 감사인 지정 - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE9FelZSMGExRC1CYVJ4OUFrTHhCdjMwUy1tSjBoQmZFNER3WWo0Ry04dGZSSmttZlBFM2l3VnpZVnRtdV9ZcGdlcTEteW53WURpR1BMZTdmVm1GYWJ6amNQTmhZZXpXUjdianc?oc=5 | → 대표: 곽병진 한국회계기준원 원장, '한국회계기준원 개원 27주년 기념세미나' 개최 - Daily NTN |
| kifrs | yna.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VYm1UdW9mM2l1SG84VFJPSnBhSHNGa1dpUzJobWpjNnJ1aXliX2RGMkhNR3FPM09rYjQtREI1d0hBTHU3V2V5aGcwRzJfUEpvaFdvc1V3WENNeVHSAWBBVV95cUxQT2JUYXQzVE5hTGZwR0dROTBxLU93YWYyUDdjMkVxbjBtaEFMYzltaWNJRzRKLVh1OG1ZLWx1ZEJTOWktcHZFRmNOR1lfZzdjZG5wdnB5YzM0M3dra0hXaDU?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | news.kbs.co.kr | 증선위, 해태제과에 감사인지정 등 조치…회계처리 위반 - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE83QWNpcGNnbWJVTGVnclJaTDdkblBWbmRVNl9uLU5TRl91NHdlN0h1WEhiQzNNNGhFd2dkbjNKWmVYaGMwQ19sbEh4TU9zZjRlMVBWNkRPb3RBTkk?oc=5 | → 대표: 증선위, 한주에이알티에 감사인지정 등 조치…회계처리 위반 - 서울경제 |
| kifrs | etoday.co.kr | 내년부터 기업 손익계산서 바뀐다⋯금감원 "새 회계기준 대비해야" - 이투데이 | https://news.google.com/rss/articles/CBMiVEFVX3lxTE5vbWtNd2xlMWZDeGdsX1BKWU5PSVAycU5qX2tqYXRGRV9hWXMzMTM2RUViZW1JYTh1TktzSXlQaVY3NDZWYy00aTRadmR1QlFwZnZJNQ?oc=5 | → 대표: 내년부터 새 손익 회계기준 도입…시장서는 "당분간 혼란 불가피" - 한국경제 |
| kifrs | chosun.com | 기업이 보유한 땅, 재무제표에 공시지가 공개 의무화 - 조선일보 | https://news.google.com/rss/articles/CBMijgFBVV95cUxQNDV6UndadzRmWERwX1UwOE15cVlDZ1IxMW1VZEdmMTk1TkxDMXFOODFfSld1bzNLbVZCcnF4R1dVRDB6aDFXTW54TmQ1YTZBd1BfVWpkSkdqQXVSdHBUY000YmIzWXVvOExvbFZ4U0diMFdObU9lUTI5Zy1NVFBndnpfV2RNcnhPX2FDZllR?oc=5 | → 대표: 기업 토지 '공시지가' 주석 공시 의무화…기업회계기준서 개정 |
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 | → 대표: 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 - 더나은미래 |
| kifrs | biz.chosun.com | 내년부터 K-IFRS 1118호 도입…금감원, 기업에 사전준비 주문 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxPem92cmstLVM2NjhYa25fWHlES3J3TUVqeVhTY3NLQll6UzlHZEdXQmpEaExhNjNyVnN6b1ZBX3h4cVpxZGdoXzdjTzZpUGRITTg0SUE2YzZzX1EwX0MwYkkybTNXM3N2dHVXZE4zaklpTTRpQlVSdUxMbmtVZE5HVlJPTmVlQ0Jv0gGcAUFVX3lxTE9DSDQzaEs3Uy1kRTEtZ0QwdWRwMzVPdXpWMTdlT1JpaGVrejNyMlIwZXg3cFdGTGlqb0lZVmhMZkl3djNuNy1BbE5FTVRxRmYwdGdveHY1X3hRSVFLSFdDVmVJaEE2TE5YX3lpZ2lPTFdpZWN2YTIyT1JIUWwzOVpVRU54RDRFa0Q2OWYtZWZlQ0VzMC1saXZlRUNUTA?oc=5 | → 대표: 내년부터 'K-IFRS 1118' 시행…"실제 재무제표 산출·검증해야" - 뉴시스 |
| kifrs | seoulfn.com | 금감원 "내년 MPM 공시의무 신설···기업별 재무제표 사전 점검 필요" - 서울파이낸스 | https://news.google.com/rss/articles/CBMiakFVX3lxTFBQc3RBaFduX21VU2pXNEhrSlBLV3Nia0MwN0VDVy12Y19ZZjRITGVBVUFQMHl4eHBWV3pSM2txQXZocXhMd1FTSlNweGhsMFFqV0VncS1DVjlNa2xjVWRaOVlkbGFNc2YydHc?oc=5 | → 대표: 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 |
| kifrs | newspim.com | 금감원, 새 회계기준 도입 준비 점검 당부 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE02Nk9mc3hILTlXeDBVVnpHN3JWckZfLWw1M1JCNFhDQk91TjFEcFhSNnZUWWt1dWtFRFdqT3ZRX3FqYkNTOTdYcHViU2U3VEZyY2ZpUDJjMlNzdG5w?oc=5 | → 대표: 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 |
| kifrs | alphabiz.co.kr | 내년 새 회계기준 시행…금감원, 기업에 사전 준비 당부 - 알파경제 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1DVjBKVS1Bai03amhmX0k4Zlg1X29uN1RWQjFRNElnYzBDX3JsZHIxVldxTUYzY21EZElaRlJ4eTlYYUdrb3BIWnlTbjZ0T095ZzNMMWlRTEtfeG1QcG9NYnctNXV4SXJodVBZNjJR?oc=5 | → 대표: 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 |
| kifrs | yna.co.kr | 내년 새 회계기준 도입…금감원 "기업 준비상황 점검해야" - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HdzNlalNOQ0Z1V1Bvc3htT0dPUTdRUG9xQWtTZmx4Ty1YdGRVNHEwZHM1RmZnMDNNYy1ta3k4Rkp4c1c5ak5abFRaemlkMVJxSndadFVYbXBWV2PSAWBBVV95cUxNMmJYczY2eWxWNlcybDIyMGlQbFJleWNWRUZJMi1Sb0V5d2EyTzlWcm5mbER2WXdzOGpRQ0JHREtubElCVl9PV3ZtN1I0N0JYTmpfY19YYjhPZkQxelRwM0o?oc=5 | → 대표: 금감원, 내년 새 회계기준 시행… 기업 준비상황 점검 당부 - 한국보험신문 |
| kifrs | news.kbs.co.kr | 금융위, 금양에 과징금 76억 부과…“회계처리기준 위반” - KBS 뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFBWaTRGZl9ncHJaNnNyVVJYa2tNLVZ1WU5uTG1iMjNfZzVOTFZPM19BamE2RHIyalNKMFdrcnZRbWh1amNza0JGUmxVdDg5NjdMTWdsSlpnQ3BwbE0?oc=5 | → 대표: 금융위, '회계 기준 위반' 금양에 76억 3천만 원 과징금 의결 - SBS 뉴스 |
| kifrs | asiae.co.kr | 금융위, '회계처리기준 위반' 금양에 과징금 76억원 - 아시아경제 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE8teDVTVFFGcExHbG5QekVJcDJNbkxQNVVOamZvdmpheXlIQ2E2WndnOHR2RVA1YnQxZ1JXek5RcW1DZXJrWW9vWE9oblVUZjFxQUFKeWJEeVEwSlc0ZS1MSw?oc=5 | → 대표: 금융위, '회계 기준 위반' 금양에 76억 3천만 원 과징금 의결 - SBS 뉴스 |
| kifrs | hani.co.kr | 한때 ‘2차전지 대표주’ 금양, 과징금 91억…회계처리 기준 위반 - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1xOEhJcFZFUW9tYmN2aFB4UFltWlZEaVAwb2o2Z2FyMEM5OVlPSzk0TWJOSFNpN1dYNG9lSlRJMUtPSnpIVk9hX0h3RXVzbmtqN0s0WUZHbmU2M19FMmx1UV9NSmMwX0E?oc=5 | → 대표: 수출입은행, 회계처리 위반 기업에 여신 54조…“심사·관리 강화해야” - 한겨레 |
| kifrs | yna.co.kr | 금융위, '회계기준 위반' 금양에 76억3천만원 과징금 의결 - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ZXAtQlFZQjUwUV9rbDZDZ0dodTF2MGw1MG9NS09xRUFJekhCQlcxVk4wWkJmZVRoYlkwR2xNdGJEbmVrdU5LRV9qZXpzbkNXVVVNeXlDc3BRZ0XSAWBBVV95cUxQVjBoZ29XNWttV2hfYkFPTG1KWjRuTXRadFBtQnhON29lekYyck5PelV1b3hnbHZVa291TmpZQmdRak1FNmhKLTFTWkZsOGJSZnBUQV91eG9kNXNiV0sxcHE?oc=5 | → 대표: 수출입은행, 회계처리 위반 기업에 여신 54조…“심사·관리 강화해야” - 한겨레 |
| kifrs | joongang.co.kr | 법무법인 지평, ‘AI회계감리대응센터’ 확대 개편 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE9vMHpYaEZibllYVUpNMThST2MxRi1ZelNUd3BBWG5qbVM4M2lSNEttSDRzRG5Vd3NrWGxyTFp0VHpBajV3Qll6ZmJIU3dtT2x3OGlpdU5n?oc=5 | → 대표: 지평, ‘AI회계감리대응센터’ 확대 개편 - 법률신문 |
| kifrs | newspim.com | 상장사 재무제표·내부회계 비적정 동반 감소…내부회계 6년 이래 최저 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTE81TWRyNUpHREE3djFpQTJQc2tsUjBjTXQ2TmlZdEJjSmhubkMxelFzUTN5M3dlX0VtZWtMY3l1ZjE0Y0MtM0xKVEFycTN5TUJpeTFJZzBCbEZlenZh?oc=5 | → 대표: 2025년 재무제표 '비적정' 상장사 53개…전년대비 소폭 감소 - 연합뉴스 |
| kifrs | biz.chosun.com | 감사 전 재무제표 위반 76건…1년 새 46% 늘어 - 조선비즈 - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxQRG8zUjI4cHZMeUh3VGs3MjIydHpoaTlFT1ZvSkQ2NTdJMlpzYXZhU1p5dU1xSHhJWXZ2dnhMU3V5cFk1MDRkM0RZWnh1MkNpRDRZSVc0am1ha2tPYXh3YTlMUENUR3VNMGpGZXJKZ09hbV8wYXczbnNlTEFBUGdlYTNicm5FWkVk0gGcAUFVX3lxTFBITXlFQmNFd1AzZDFOb0V4OEgxZmkwNHJ1OEY0RjVmV1Z2cUY0a1pNam9fZXNmakRkaWxUZVd0V2lKUlhqN0hlZkdTalNpWl9WM182WFB1ZHhDdVQ4NWMtbGI3R0w1MVVZd05jMmNKVmVtVmg2ODVWQzI4TnEyM2hKUnRka2Y5aGJzbVpzVGx6eXc2WkdNR3hWRWNQSA?oc=5 | → 대표: 감사 전 재무제표 제출 위반 76건…전년보다 24건↑ - 연합뉴스 |
| esg | ESG경제 | "ESG 공시 강화에 중견기업·협력사 부담 가중…대응 격차 우려" | https://www.esgeconomy.com/news/articleView.html?idxno=17072 | → 대표: "ESG 공시 강화에 중견기업·협력사 부담 가중…대응 격차 우려" - ESG경제 |
| esg | 이데일리 | 회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 | https://www.edaily.co.kr/News/Read?newsId=02978246645613248&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article | → 대표: 한국회계기준원, KSSB 비상임위원에 김정일 대한상의 상근부회장 선임 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | electimes.com | ESG 공시 2028년 대기업부터 시작…스코프3는 3년 유예 - 전기신문 | https://news.google.com/rss/articles/CBMibEFVX3lxTFB0NEtXNnFZdGJLd01zRG5XaGUtZ1RyX1hFMTB2REQ5VlVJRkZzdVFJODBNVHdqTlhBZzZtQnZtM1N2dXhtc2tma3pMaEMzX3N1cjFjOVl3RE91Sjl6Rm9zV251UDBQYUo5NWtXMNIBcEFVX3lxTE1jYVpBZ1NRcDNjb0ZpaGh3Q09TZFpINmN2b3BxbTJMaGpJeVVqQ1loMHhkRjJYZkp2ZjVkTEN4R0FWM0lrcWtsSUphSW4wUHZ0MWw3ekgwb3JZeE5hcmNfUXE0VkxUcXhWOFdsYXlZVmM?oc=5 | → 대표: ESG 공시 불확실성, 5년만에 마침표…'2028년 시작' 로드맵 4월 확정 - 머니투데이 - 머니투데이 |
| esg | 한국경제 | 'ESG 공시 법제화 대응 클래스' 개최 | https://www.hankyung.com/article/2026100538041 | → 대표: ESG 공시 법제화 초읽기…기업 대응 역량 키운다 |
| esg | paxetv.com | 상장협, ESG 공시 실무교육 실시…2028년 의무화 대비 지원 | http://www.paxetv.com/news/articleView.html?idxno=284514 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | enewstoday.co.kr | 상장협, 'ESG 공시담당자 실무 쟁점' 과정 개설 | http://www.enewstoday.co.kr/news/articleView.html?idxno=2481878 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | dailian.co.kr | "차질 없는 대응 지원"…상장협, ESG 공시 핵심실무 쟁점 대비 | https://www.dailian.co.kr/news/view/1703168/?sc=Naver | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| esg | newsis.com | 상장협, ESG 공시담당자 대상 실무 과정 진행 | https://www.newsis.com/view/NISX20261019_0003831375 | → 대표: ESG 공시 의무화 앞두고 기업 실무 점검···상장협, 대응 교육 강화 |
| icfr | datatooza.com | 크레수드, 2026 회계연도 지배주주 순이익 1772억 페소로 증가…내부통제 취약점 해소 - 데이터투자 | https://news.google.com/rss/articles/CBMicEFVX3lxTFBnNFQycEFSeEhqZTRqekp4cnFJc3dQQVVyRWZRNEpaamtHcFFfV2VQUDI3OTZGMXFRdUVmSHpoQUM5VHVjVzdVZ2NIVUdIU0RpU0xiSmFQcmNYdjdrTGVBZFJFdGlCcWl5UTNsa1lUeHo?oc=5 | → 대표: OMS 에너지, 2026회계연도 연차보고서 정정 제출…내부통제 취약점 및 세그먼트 공시 보완 - 데이터투자 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | hankookilbo.com | 추미애표 지방세제 개편 3개 과제 입법 절차 돌입 - 한국일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTFA1M05NLUNhTTY2ekVWVUZIUG82WHltbkJ2OUNvQnpHZEY2M1IyUlZCdjRyRGMyYzM4NGZMdzVnT3NDSE1hYVlUSUNWaUh2Z29idG5WQjdBMjlYTVBtcHJSZ0JkVWlnZkV5VENjLUFn0gFzQVVfeXFMUHVhOTRjZkJMMUxoSG0takFvaFA0THJfc2xEQmZoMi1yaEtrek1wbUFOR1Q5Q1Z3dzJNdmlVYXFOVDhBLW9QREtNR3I4RDlaZUxlaHo4MU9kWjlkRmdJSUFEWW1mLWZ3dFUtUXcyQlhpOTJiQQ?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | discoverynews.kr | 추미애표 지방세제 개편안 국회로…재정분권 입법 본격화 - 디스커버리뉴스(DISCOVERYNEWS) | https://news.google.com/rss/articles/CBMickFVX3lxTE1NYnhfZDhHV2taQUtZRmRsQ0lrS0YzX1BYZllnSVVaSVJQNHo3eGJyTFE1d3NTUERyUDJXdXNpN3VLQVc0MEREMllTUjNhRTY0MnJOV0JDSUc0d3FxeGNQTnFseTZNdVRUOHVDTkJvTnZ5dw?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | newspim.com | 추미애 지사 제안 '지방세제 개편 3대 과제' 국회 입법 본격화 | https://www.newspim.com/news/view/20261001001411 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | bukbuissue.com | 지방소비세율 25.3%→40.3% 인상 등 지방세제 구조개편 입법절차 돌입 - 경기북부이슈 | https://news.google.com/rss/articles/CBMiRkFVX3lxTE5aN1FqVDg1Q0dJeE1XRUlSYjEzV0YxeWhPcVlOZl92VGxnN0lRSzAwZmRaelVUYzdEUXpxZkFhVTFKYVktWlE?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| tax | gpsimin.com | 추미애 지사 제안한 지방세제 구조 개편안 국회 입법 절차 돌입 - 김포시민신문 | https://news.google.com/rss/articles/CBMiQkFVX3lxTFBISHRGT2NlMURBSTIzNW1laFlLWmtCTFdGWDNfY1ZxSl8tVnQ2SDNlNTRJNTlOWmg1WlU3WURkdmpBUQ?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |

## excluded:standard_setter_governance (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국회계기준원 | IFRS 재단 '정관 개정 공개초안' 검토의견 조회 | https://www.kasb.or.kr/front/board/comm010View.do?seq=2193 |  |

