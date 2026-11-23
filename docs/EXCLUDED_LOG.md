# 필터 제외 목록 (EXCLUDED_LOG)

생성 시각: 2026-11-23 11:00:33 +0900

이번 수집 실행에서 필터에 걸려 빠진 항목 전부다(2026-10-29부터 — 규칙과 사유 코드는
`docs/FILTER_RULES.md`). `excluded:…`는 정제 파이프라인(`main.build_data_json`),
`collect:…`는 수집 단계(각 어댑터)에서 빠진 것이다. 여기 없는데 안 보이면 필터가
아니라 메일·화면 표시 조건이거나, 그 소스가 실패해 전일 캐시를 쓴 경우다.
**과다 필터링 점검용**: 실제로는 우리에게 적용되는 항목이 있으면(오제외)
`sources/_config.py`의 해당 키워드를 빼거나 예외 조건을 추가할 것.

- 네이버 검색 결과 중 카테고리 미분류: 1611건 (제목은 남기지 않음)

| 사유 | 건수 |
|---|---|
| excluded:category_cap | 12 |
| excluded:company_event | 1 |
| excluded:company_self_activity | 5 |
| excluded:corporate_pr | 1 |
| excluded:doc_variant_merged | 1 |
| excluded:duplicate_exact | 6 |
| excluded:financial | 1 |
| excluded:foreign_tax | 18 |
| excluded:industry_specific | 8 |
| excluded:manual_id | 2 |
| excluded:news_too_old | 36 |
| excluded:no_regulatory_signal | 79 |
| excluded:opinion_piece | 1 |
| excluded:reader_content | 1 |
| excluded:related_news_attached | 1 |
| excluded:similar_news_merged | 50 |
| excluded:smb_only | 4 |
| excluded:standard_setter_governance | 1 |
| collect:event_announcement | 19 |
| collect:incident | 1 |
| collect:law_name_mismatch | 7 |
| collect:no_category | 272 |
| collect:non_kifrs | 26 |
| collect:old_year | 8 |
| collect:out_of_scope | 209 |
| collect:out_of_window | 40 |
| collect:tax_subject | 36 |

## excluded:category_cap (12건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | PwC | 지속가능성 공시 제도 로드맵 초안 및 확정 공시기준 주요 내용 - PwC | https://news.google.com/rss/articles/CBMif0FVX3lxTE1Gd29wMWxoczQwX09wRThxRzhCam43V3VTRHp6LWFzQWgyZUdjeTF5dzJBZUJoYnlLZFdYWEZlbWVmRDNEcHM5eGVpTGhPSThiUEtkNlpBTlVVb2laR1FlSnlCa2ZBeG5uWFFvaHNfdG9LeExxeFRLc1ltdXgzcmM?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 머니투데이 | 韓 ESG 공시 입법 공회전할 때…日은 면책·인증 세부안 내놨다 | https://www.mt.co.kr/stock/2026/11/22/2026111914551313723 | 뉴스 카테고리당 15건 상한 |
| esg | PwC | 지속가능성(ESG) 공시 제도화 확정 - PwC | https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFhyeXl2dTMtUEhMSDJRNHlmWGhZVFNuVGt2SzBTYnRzNTJhQ21NVlAzRHk3Ym9ESl9MbWZibnh4aG15V1lnLUdId0ZBY2RqR2VZd25QbjNhSlB5M19wQk5JcXdGVEdpRkFSYjZvRDFRSzRlNVNjSWtQQkV5UUlfSWJoVGFlVTh0MUsxYVZoQmp4MWhDTWxuX0c0V1EyV3B5SHBjX0dZRGNWZw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 확정…10조 이상 기업부터 첫 적용 - 한경매거진 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBNSi1jOHJWMGZBWlJGbFEtODYxLUptaVliMWI1THFGNjhEU2NEYWpta0FtRlFieFN4MkpjcWp2RHFYcmcxQks0VUN2TWxpdFp0eHJ1cXdkS2FRaFBFZTU4UFBfWG5aR1BLSGRlZg?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | 한국경제 | ESG 공시 로드맵 초안 공개...쟁점과 과제 남겼다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fUHhtNHpadHZiaHFKSWx1V2Rkd19hZzhkUkp1b1dIUGpMc1ZFWnZMMzhtcjg4cjhTeTNnNlpsYzhRZFNUMzlhN25mbURURVhjT2JvcVVqZUV0Zw?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | dailian.co.kr | 생산성본부, 에코바디스·KOTRA와 협력 강화…지속가능경영으로 수출길... | https://www.dailian.co.kr/news/view/1717891/?sc=Naver | 뉴스 카테고리당 15건 상한 |
| esg | samsungsds.com | 2026년 ESG 공시 의무화 동향과 시사점 고찰 \| 인사이트리포트 \| 삼성SDS - Samsung SDS | https://news.google.com/rss/articles/CBMiigFBVV95cUxPUUJ2WkFSOUN6N25YS1RjUTRlWS1EeWx6MUdhSVlVdjdMeWV2NHNyRTFwTVpuWDRvUElPVm43ZXJXQ3pLQ0M4NFlLdTJyZURiOTYwb3VXTHRBUnJQMFFTU3ZMYjRUcUF2OXZsWHlrYWhWSmJIWHV1WWJpOGFoTGc0VWNmdnl4NnBXYkE?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | ccej.or.kr | [공동기자회견] 금융위원회는 반쪽짜리 ESG 공시 로드맵을 즉각 폐기하고 국제 기준에 부합하는 법정 공시 체계로 전환하라 - 경제정의실천시민연합 | https://news.google.com/rss/articles/CBMiR0FVX3lxTE1LQk5PUE9HQUtOM3pKNFFYRlY2OHdpSWt3LUpCajlNdl9xY2ZWdDVBUENEaEdOSmV2eV9FS1BWbFNlVUp4T2xr?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | lawtimes.co.kr | 금융위원회, 지속가능성 공시 로드맵 발표: ESG 공시 제도화의 본격 개막과 시사점 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1nVEVSX2pWYkx2QUFiakxBejZKeEE4R2NSUTdZTklmaDdSSzBldDd2ampaUnBadjlfWEgtU3FPcHBKNGc1SEM3b2tROFU4NWNZUzVpXzRvNEY1V1oyaHNfZnNIQy1IZjVoZHpHc3l30gFyQVVfeXFMTS1NcDE3Sm5xZVFlbjJ2ajJqVGNpWmRUVFM2X0tjM0tIdE9NSHp2NmtyNEcwc1JPU1o4MXdEVXJVWnJfdmJLN090T1JRU3JEai1aejhxMVhxQXpGdVJvY0xGSTA1NlJIcElPTUoyVlZnUFpR?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | m.ekn.kr | ESG 공시 의무화 충돌…“글로벌 기준에 맞춰” vs “기업 부담 적게” - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EWXdPc0xMbjZHaDlIS3JCaHlveDRwUXV4d0Qzenpud0gzdjRabWQzQW5zMmxyTVJzZmVqUTZYazRfb3h1dlcyaDJTNHJydGpNYnZsY3ZBQnhtVkk?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | hani.co.kr | 금융위 ‘ESG 공시 로드맵’ 후퇴에…시민단체, 폐기 촉구 - 한겨레 | https://news.google.com/rss/articles/CBMibEFVX3lxTE04ZHlySHlQd0VkVWdGQTRsOTdXUTJQRkpxRFQxWjc5Q3FEUmt5dVJJY21BLXZwakk4bTJpaUhmNW9rekRMUzEwYmR2TDRjbjdMZENpWkRqc195TE5LRWUxTHM0bEp3VDU4LURtNQ?oc=5 | 뉴스 카테고리당 15건 상한 |
| esg | dhdaily.co.kr | KSSB, 지속가능성 공시기준 첫 세트 공표…기업 대응전략은 - 대한데일리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1qTnFWLWFlSWx2cjVmaEswUXdpRUVlLU5BZHpTN3VlQWZWOHd4NEhqSVZxOThmRXR0eHpVbTlmcjNacFQ2RVl4Mlpmd0g3eXY4eGxVNDhzWUtTaEdCUUl3OHdNdVJfcnBHQnlr?oc=5 | 뉴스 카테고리당 15건 상한 |

## excluded:company_event (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | financialreview.co.kr | [강동형 칼럼] 대손세액공제, 부도보다 대손확정일이 가른다 | http://www.financialreview.co.kr/news/articleView.html?idxno=46483 |  |

## excluded:company_self_activity (5건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | futurechosun.com | 회계기준은 제각각, 보고는 중복…‘회계기본법’ 제정 목소리 나와 | https://futurechosun.com/?p=163501 |  |
| tax | sejungilbo.com | 김주영, 조세특례제한법 개정안 발의…2031년 말까지 연장 | https://www.sejungilbo.com/news/articleView.html?idxno=61103 |  |
| esg | ESG경제 | 아시아 각국, ESG 공시 의무화 '질주'...한국은 계속 '헛바퀴'만 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTE9iT1p3aDQ1bGItZFl4NDZ4Z3QxVGtEUS0wYnpjZ1BkTmF6MF9aakdtRVpBaGdIN3dUSms2bkxKUlBjU1VkT2NUaDRpNVdEaEExdDZjWkZEQlI0RjFQS0gwZ3IwRTVpTmNHNWJTMw?oc=5 |  |
| esg | ekn.kr | TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 | https://www.ekn.kr/web/view.php?key=20261118024331201 |  |
| esg | choicenews.co.kr | KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 | http://www.choicenews.co.kr/news/articleView.html?idxno=173128 |  |

## excluded:corporate_pr (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| tax | 조세일보 | 국힘 "법인세 전 구간 1%p 인하·주52시간제 완화 추진해야" | http://www.joseilbo.com/news/news_read.php?uid=579620&class=32&grp= |  |

## excluded:doc_variant_merged (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 금융감독원 | 내부회계관리제도 평가·보고 지침 Clean ver. ('24.12.23 개정) | https://www.fss.or.kr/fss/bbs/B0000155/view.do?nttId=189616&menuNo=201177&pageIndex=1 | → 대표: 내부회계관리제도 평가·보고 지침 ('24.12.23 개정) |

## excluded:duplicate_exact (6건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | 내부회계관리제도운영위원회 | 모범규준 | https://www.k-icfr.org/sub/menu/guideline.asp |  |
| icfr | 내부회계관리제도운영위원회 | 중소기업 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 제정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=38&rGotoPage=1&rSchText=&rType=1 |  |
| icfr | 내부회계관리제도운영위원회 | 내부회계관리제도 설계 및 운영 적용기법 전문(2021.5.11. 개정) | https://www.k-icfr.org/sub/menu/guideline.asp?rWork=TblRead&rNo=36&rGotoPage=1&rSchText=&rType=1 |  |
| tax | 행정안전부 | 지방세법 시행령 일부개정령안 입법예고 | https://opinion.lawmaking.go.kr/gcom/ogLmPp/88292 |  |
| esg | mediapen.com | [ESG특별기고]데이터 내부통제체계, 지속가능성 공시 신뢰도 확보의 초... | https://www.mediapen.com/news/view/1138165 |  |
| esg | tfmedia.co.kr | 회계기준원, 지속가능성 공시기준에 투자자 수요 반영…전문 위원회 확... | https://www.tfmedia.co.kr/news/article.html?no=209073 |  |

## excluded:financial (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| icfr | businesspost.co.kr | 카드사 준법감시조직 확대, '여전업권 내부통제 모범규준' 시행 앞두고 긴장 - 비즈니스포스트 | https://news.google.com/rss/articles/CBMic0FVX3lxTE9XcUxKY1p0b2VRblVXa2txOXp6OHpwcmRtVXQwMXpqNzI3a25KMFVaeVRqNFhiRWFBd3ZsX19rV0tJQmJDN3l6cHUtN3h4OGhhZVc2N3VKZDQwRjI1MU5fN1NMTjdXaUp0d1ZNdTVOY25IQTA?oc=5 |  |

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

## excluded:news_too_old (36건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | eiec.kdi.re.kr | 회계감리절차의 신속성과 투명성 제고 - KDI 경제교육·정보센터 | https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY2E1RjdJcE9WeU1XbWRSeExkOGFwTmdUQWVWdHZ6WmxKd0U5bW4zY1lkY0xRb2hBSDhCMFo3azBJY2JKZHNtUGlXcTF3UGowdjhBZkFsYktxcURVVk5PSXJ5VHdjQUZtM2lnTE41YVNZcExveDVaeFkya0RzZU4zWjJvWjdoekhnRGZiZENVeTEwdTc5QzNEMExfR3NTeE1ObFdzRXlobUpLQ1k?oc=5 |  |
| icfr | EY한영 | EY한영 설문조사, 국내 기업들 신외감법 도입 효과 확연… 83% 회계투명성 개선 체감 \| EY - Korea - EY | https://news.google.com/rss/articles/CBMif0FVX3lxTE1SVm4xNGFDcVUzcDBKZWVPb09fd05NcFB5RmpuOW9jeVVrVXMtTjhOQU80MHZEWHJCUVh5VE9pMGJBeU1QYk1UWU1DZVBnUjQ4ZGNvTDhvb1V5ZkRiTDZ5ZnBVT2FtWFdGOEc3dE5VN09mLWZVbmQ4aXZLdVE1ZDQ?oc=5 |  |
| icfr | dealsite.co.kr | 더코디, 회계조작 정황에 외감법 위반 의혹까지 - 딜사이트 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE1lVFFZeTZTYjczY0ZEWURUMHlDT1U3UjE5Mk1UVUExaDg1bDFJektIZDdwY25iRGxVWEliRWo1NEphSzRNYmdNdWdCQUpjQlU?oc=5 |  |
| icfr | joongang.co.kr | "5년 간 감사비용만 2배" '신외감법', 정부는 "일부만 보완" 왜 - 중앙일보 | https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CWGlXei1TcmFmakl1RUhIbmh0R3pJS2xIWmY4cFh4V3ppT2tvOHUtcjdLaTl0VDBuUTBhWENyX3dFcVhtTE92VDU0RmVWT3NBWE9IakVR?oc=5 |  |
| icfr | 매일경제 | 내부회계관리제도 모범규준 규정화된다 - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUEFVX3lxTE5jbEMtcmhHcFdSd2lSYU9xbWtFY21HVnI2bTNwcXcxUnVSUmZJaktVSzZzelZEM2xYOUgxZVNkbkZkNU9yU0t6emU3NnJvdDhr?oc=5 |  |
| icfr | news.bizwatch.co.kr | '신외감법 아버지' 최운열, 한공회 회장 당선 - 비즈워치 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1ETWIzSm5ORHhWOFBHZ3BCYmt2N1laVVVIQXRPaDJVWmEyYXNYc1B5RmJYSUhZaWdwdDFnV2dmekY1bG9aQjZzazQ0Q1NEY1BNM0h1dlVoMnVEVkdhVzhXTUtyaDJsNDNtNkE?oc=5 |  |
| icfr | lawtimes.co.kr | 유한회사에 대한 외감법 적용 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1FLUo3c1YzSlVQbVNDSHZZUFdfUDVyZ1FqZm93dzl3MFpUbVhXZTY1YXdBYjB4WFF2cjlFU2pVbHNIdlcwdGtOYzJrYUVwcGxOSEM1OXVsUXBiTi02M0E0dFN5ZEVIUGx5cWx2YXVn0gFyQVVfeXFMTldaZG54anZ2MkVIQW81YloyNFZISUNPVUhvdUJCNXd6YnJ6aV9XdWRWOXA0Y1FMeGRPcFowb0dSWExpMG1wSTJMc1JKM1ZPMmFEUzh5MlZURV9EZVFrNExocTREQTcyMGh5TF9rVUVIc1ln?oc=5 |  |
| icfr | crowe.com | 신외감법 시행 이후 과징금 부과현황 및 시사점입니다. - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ONmp6d3VTVEVzdFBQUUprMEFZaXh3SzJ1Wml1dHdHWV9DR2NBQVpsZHJhMU5PSUtWOEwwN1RDbEthcnBYTGcxTHo1Q3hnOXFKeHZIclhiTEE?oc=5 |  |
| icfr | skkuw.com | 신외감법, 얼룩진 회계부정 지울 수 있을까 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBQUkRSQWdfMzd6aHpxOG84TDhqYXFyeVNJUzJnYjQ5eF8wc2pPdU9Pa0hFVC1sbTIzWnZhd3NiWGl5T1hzbGhlUmtaLTEwX29rLUZRaXV6eDhfbjhRS3Y1SUo2ckTSAWhBVV95cUxQc2tHUFNoSWM1U2c4ZzF0WkZuTU5JVlZPbEJHaGxqQ1BvNDhZMk9qU1o1SjFnT0M3YTRPbEJiZS0wcHlRNTNZU1p4a0tKZ3FoOWNWd0I1czNiRHZqVm80aklhZjdYbEg3aw?oc=5 |  |
| icfr | ESG경제 | 공인회계사회 새 회장에 최운열 전 의원 당선..."신외감법 유지해야" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5wczU3VWVubFMtUTdpOUI4Sm5XQUozYW9mVjRwQVY5TlEtRE5heC1nSnZrWV8waWZjNktsX2MxZk14TC1sRTdCdUxhbDdtZldlQkhsRElIVFBya25mLW5PLUFMd2xpR3c0X3VV?oc=5 |  |
| icfr | 한국세정신문 | 금감원, 상장사 내부회계관리제도 평가·보고기준 마련 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTFBvVVdNMHBLV3hMUzBpZTRsejB5VEp5d0w0UkhLbkxObXJGVk5mN3lDYW8tNUYzdlQ1UDd0cmZQZWsyczRXSWkyMXRINXc1VUQ1djJhODBHaGtoeC01eVE5eVFQS2g?oc=5 |  |
| icfr | lawtimes.co.kr | 주식회사 등의 외부감사에 관한 법률 시행 및 시행령/시행규칙 개정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5YczBOSVZJRVJMTGtyQkRxaXF0Vm01ZlR0Y01HZ25hakVXOWhoUWJRLXhfV3Ftc3ZNNWZsSldQaURSUUliZW56dmd6eDZ6aGdmelFqWkt1U0xMbHkwYUJzQzRvUGF1UlJpaTh4Z0Rn0gFyQVVfeXFMT3BKcmdfUEJVc3dmRjVzZFhPQzAyNEdUMEtMNW1MZmdTeUZaRkYtYVVneDJwbzViS3l5NEdvaW9mUVBoRFNCck9XZDM2aDhuWTB5RG1tOE9vQ010MXlqV2c4RGQ5UG9BODN1YkFzT3BYell3?oc=5 |  |
| icfr | 한국경제 | 新외감법 4년 만에…회계사 몸값, 상장사보다 더 뛰어 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE8tT01TR29FZkUtcHpOSmVST2VFZEV5RUh4d2tFT3hQcTktMUFfRnFwbUF4dnpLQTNKODRXUEI3QTVGbW5OMWVXRkliR3huY09CTEVneHZId3VaZw?oc=5 |  |
| icfr | crowe.com | 내부회계관리제도 위반에 대한 점검결과 및 유의사항 - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ER3ZUdU1Wb1FkYjhrSWhCSUtWOWZ5dHllWU5tMHpPQ3NXSlRRNi1PM3BnNDliZjY0TXEtNkZNdHlyRFM4SVB6M3RMRFpvendjN241alBNc2M?oc=5 |  |
| icfr | news.koreanbar.or.kr | “기업 외부 감사인에 변호사 반드시 포함”… 이정문 의원, 외감법 발의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE5ET254R1JIeWVNLWFKNlBVTUNJdkdzdHJqSTVKTURkeVZMYkxpc2RxZzlSU0p2a3pXbWxCNFQ0U0tRbVpaWk9zajZEYWZwSW5UQmY1ZFlnSmxpUFdqT2YxWFI3Wkp2R2RsUFljS2FDYw?oc=5 |  |
| icfr | 매일경제 | 윤훈수 삼일회계 “외감법 3년 기업 회계 투명성 제고 기여” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiT0FVX3lxTFA4VjhHOTRoUnJKU1JHaE1pY2ZsY2IxRFJ3b2hqVmJwUU1pV3JTTXNLeFJ5dmwzVnRTQWw4ZWxvZVBqc0pScUpicnp2TW9xRGc?oc=5 |  |
| icfr | skkuw.com | 양날의 검 신외감법, 좋게 쓰려면 - 성대신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pb05fYnpsS1lVRWNJcEdocHRMdDF2LVc3ODVrOFp5YWttRHVEdDYyV1FwSERlZzcxUEFLQnF0emhvNnFpYW11U1hROWlEM0VwMGR1Um1pa0xRajlxSVktM0VEQ2rSAWhBVV95cUxNOTN1dzB0OG02SEJDY2J2WHVaVGF1eHdyVnBEYS1jN3JORE1kbUhSbW8zbTUzT09xWm5zVDRXdU1UZ0V0T0YxcVRXZXV3Nm04elpZRE9obzVLM3BmZkxtUFNzd3NYSDN0Vw?oc=5 |  |
| icfr | hitnews.co.kr | 新외감법, 연말 ‘밀어내기’ 잘못하면 포렌식 당한다 - 히트뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1SdW1ibmVsdHg0UGZIX2NnQmlWM0hEWUlBZHRMQXdPQzlDQzdnOXA0eHhKOVFsTFVZWGlLTnBlZmZsV3E5TlNrYWZBZS1MTW1OVi1MWjNFYVU2X3FmVEUyZ25mZzZtY3JDMHc?oc=5 |  |
| icfr | lawtimes.co.kr | 「주식회사등의 외부감사에 관한 법률 시행령」 개정안 입법예고 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE1GUXd1R3FkbUJ2eU9BWTVIT1ZDZ2x6dHdOa3JVWmZ1VkxQby03V0dXeVJ3NzNCR1JaV2tjaTEyUTN2ZG5LdmozYUNQYXBjRlhSeHRJTWJmRUVpU09MV1dyWTZBX0RWOU5iLVdlNUJn0gFyQVVfeXFMUEdsbDB4aXg5dWhKMERoOS1NcVh4S3FBT3NRTXc0X0VieXpWZ1VKcWpSMTM4QlBTa24zQTRYSFZmVm1scFhwU1FOYkNSb0gwaWdZLW5sVVB5NlRiYk5NOXlWRk1tWXpBTl9uaFhVd2RPUS13?oc=5 |  |
| icfr | 이데일리 | 국내 기업들 83% "회계투명성 개선 체감"...신외감법 도입 효과적 - 마켓인 | https://news.google.com/rss/articles/CBMic0FVX3lxTE01cF9QZC1aZEw0WDJzWTNlNmJ5eXFwZU13dW9ndmFOMHRtWTR0NFlrbzJFTTRacVhEZUM3Nms0NmtsdFl5MlFQN3BnU2lTSlZMWF9YeW96RENNLXAwbU1mRUVhWDRoNll0XzZ0SHo5RDdwUUU?oc=5 |  |
| icfr | newsis.com | 초유의 오스템임플란트 횡령, '신 외감법 무용론' 번지나 - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SR1lOd2VmanJnVW9FQXRwSVJYUlIzSkNnRndGNEcyRmlxUGxiUUE4VHkyZUwxbFZOMk1wMWZ0dXh3QUlkOXlUWHNvYlh2Qm80QlhOMGlydTJvTXNyQVF3N9IBeEFVX3lxTE1CUVJtSHR0MHpJa2JOZ1dtODNsZUp4ZlEtZ0g0ZEFpNDVzNHM5RlZndGdpS2xoc3hDcUVuOUsybGxVQUotSzJmdlRadEdPX1lhMlVMTzN2RzJaakNuWmJrZko3ajBfbmVNVXZ6eWpOemh4ZVNrOWEzcQ?oc=5 |  |
| icfr | crowe.com | 외감법 시행령 개정안(금융위, 2014.3.24.) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5VTm1YRW9LcGZYRnJXLWNYcGhVeTZDemhhU2J4c1dBQ3NEeGZsaVNwYkxxNEZNS1lzNDlRNTFPamhNY3Y0T3RvdWlhdmRIWjVsOHZMTlB1RUE?oc=5 |  |
| icfr | 매일경제 | 신외감법 적용으로 2020년 달라지는 규정. - 매일경제 | https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXT3J2cVgzODYtbnFFZkVxcHVsNHYtd0R5LU54SmRyWXFBTy1UWnU1dHJQYUpoSW5tUlRUTGM2SHc3b0dtN3JPSnBxQUNTSUVwcXhR?oc=5 |  |
| icfr | 한국경제 | [한경 CFO Insight] 신외감법 2년...감사비용 70% 폭등 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBCc1VNZVE2U181NVZDQzlZYnpVM2E1MEtxdXRDS00tUGVlN0ZSTFVzNTRhWFQxc1NKUFFtYjVKWEFDUmZkZVItN21jdkJvSFphVUVVY19QNVVlUQ?oc=5 |  |
| icfr | biz.chosun.com | 엇갈리는 신외감법 실효성 평가…“새 정부서 손질해야” - Chosunbiz | https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUzFjNFNPUnBrT3ZjNGFtbDBKVVlQcHFna0puQUZIemxRQ013Z2tNUkRZQW9NQTA4WHhQZlMxYkZ6TmxWb2d4YVg1czBBcWtxTTNmcG52c1d2NDE4TVh1Uy0zekg1YV9mdTVDWDNKc3JyUjFBejlwQUVBWVdIY3pKMkp5ZksxS1ll0gGcAUFVX3lxTFBsa3BrTDBrZTlYWHZjZG1QVk1yRDBDRVFvTU8zbkdqYUppaGcwRmc1Vy1XSDlXRWRxX3RPcnhwSEdoVlNMVTBGMjQzZkxQSmxRdkliNFpiMGNOcHVqN1hzbjFPc0dCTDBCbkJoazEyZHhqRTBzTnd5U0E3cDc4cTlkNnVkTzd5UmppbXlYQ1FaODVmMEZEUTdieWdwYg?oc=5 |  |
| esg | PwC | 아시아·태평양 14개국 지속가능성(ESG) 공시 현황 - PwC | https://news.google.com/rss/articles/CBMihwFBVV95cUxOZXlXZzdsZGtiYXBTTlM2b2pfYWJGbVEwWU5xVTJ2alhvOUdLeHVRVkZVMnRTWGJQbXVENW5Fbk1GUnIxSFdKSEtlbVFMbklWSmpwMmlyM3czSlRyN1ZCRnlXQXgwMVFyUFZIbWhEUzlIZTlGOExkaXFSYnpKczMxd0tlM0E5ems?oc=5 |  |
| esg | greenpeace.org | ESG 공시는 무엇이고 왜 중요할까요? 글로벌 ESG 공시 의무화 이해하기 ① - Greenpeace | https://news.google.com/rss/articles/CBMikgFBVV95cUxNLW1pY1JGTUNqTUZKakJCemhOdW5famNyeVNBSmc0Rno4ZFk4a3VJRFVlM3NYa3g4elhWVXkzaGdtZlRRc21ROVNhdXdMejlMTGlfWGZRZTJqSXVJZU43ZV9EYUZYRTRubHBPenZPTGFEakpjTkhTTHBrdThOMTE2SkFhMXh3azIzU29yRDNWdFl5Zw?oc=5 |  |
| esg | ESG경제 | KSSB, 지속가능성 공시기준 12월 의결...내년 기업 대상 파일럿 테스트 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5GUDZYRVVFNTRYLV9YNEd3ODdtQjNFQjlxci1ya2FRblU1dndlYm5nS1FLM2NsSnNBOVpyZG1IS0VlQ28tOXZJNklnRW1BRFZuMGFCWnVoYXhiT0dQUk91UUZ0LUlzbUlJT2lR?oc=5 |  |
| esg | hani.co.kr | ESG 공시 의무화 미루던 정부, 경제 불확실성 내세워 ‘신중론’ - 한겨레 | https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBBNGw4dVZlb0dyekFQOHI5Z3RucTdHNThoWTRvcGVnV0tIY2pJQnRsU1EwLXpwelUxOU13M1VJbm5jRnV4dGpxTVRJV21qaUR6UDBjcGVCdUgwdDZDVDhPUVEtaU9wcXM?oc=5 |  |
| esg | 임팩트온 | ESG 공시 의무화, “스코프3 포함하여, 사업보고서에 2년 내 공시” - 임팩트온 | https://news.google.com/rss/articles/CBMiakFVX3lxTE1fTi1xaGVFNUNFb0RzakhKYkJ6dEgxUkhDSndoV1JOUTFKdVpxdGNRNDFxUC1RUjViVE9uM2xva1hhMDZLQXRrOFdvaU5SSFBocS11LTlXWV9vWm1paW1rS2tWMk0yTXUzZ3c?oc=5 |  |
| esg | ESG경제 | KSSB, ESG공시 기준서 권고안 의결 연기...로드맵 발표 결국 내년으로 - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE1Rc1JfaXo1Y2pHTkxyMGFwam55Q0IzUlVkMmhSaEVjYjRJVkVvd09vbERpVWtxU3U3SkduT2xWRDQzOEQwcEREVFFFVzVDcjBscWxJa0cyTlZIcjVSNXVHZTZYckZIdEJCaWw4?oc=5 |  |
| esg | 한국경제 | 금융위, ESG 공시 손 놓았나…국내 기업은 눈치 게임 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTE1oemxQY2ZnOVZEdVdUaUFyaXYzTUpYR1Y2VDRZbEk3dHhlYVVXR0hfYkpNN0VXWG5iX2U3c29lRFlQLVlpaGdwSUp3aUZkYndLdURQMGRFY2kxUQ?oc=5 |  |
| esg | 임팩트온 | ESG 공시의무화 2단계 적용하나...정부 공시 기본방안은? - 임팩트온 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE10SGgydk8wUXJqOWg5VVI0WUFLNVFRT3d1TWVKX3phQ1lFd2M2UzB3M2RyamZ4WmIwTzFaYlN6ZjVvM0VNQUZlSGhBdVBIMzdBTmFjeFBNYWFOUHVHdnl4WjRLb3JJMFZ5?oc=5 |  |
| esg | 금융위원회 | 보 도 자 료 - 금융위원회 | https://news.google.com/rss/articles/CBMijgFBVV95cUxPemhwMnRORE1fYU91ZUxxeU53UkROdFQyTHVlWHRZRXB0cHJza01WSGI1WHF6aXl0U2FyM3d6M2pHVlJLNU1RZzVsb3RkX2hCNmRGV0gwbUQwOHRrSnp3RU53WmdnVkIxem11R0VfcjA5LTlwYmdqSmx0UE1VS0Zac3o4ZWVyVXl3Z2ZFMlpn?oc=5 |  |
| esg | ESG경제 | 국내 ESG 공시, "27년부터 법정 공시로 순차적 전환" - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE94R3l4RXlud2VfYjMwMGNvcldzQXhYaXo4UFBpdXlINW5qV2ZfRHJCeFdhNlJLdWdjNXpjV19CbGc0RXlFZV95SW5SemxZa2M2RG1VQ25RbS1zeXJCWEMzUzJ0a2p3X05fZ2hv?oc=5 |  |
| esg | ESG경제 | KSSB 지속가능성 공시기준 초안...'유감'과 '기대' - ESG경제 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5IbzRUeVpVLUVnVUk4MGRxWHBfRmN2ZW0yU3VDYkxLbUdteXFPWGdVb05ueXNwTzBSS0ExSUU2V1BTd0xLYUo4eDlLVjc3LTFJS1QtQVVJNVdtZzNvcHF4UjdsVjFFUHdKZnJJ?oc=5 |  |

## excluded:no_regulatory_signal (79건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 조세일보 | 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 | http://www.joseilbo.com/news/news_read.php?uid=580131&class=10&grp= |  |
| kifrs | 일간NTN | 한국회계기준원, 투자자 전문위원회 확대 | https://www.intn.co.kr/news/articleView.html?idxno=3000418 |  |
| kifrs | CPA뉴스 | [K-IFRS 제1118호 시리즈 ⑨] 손익 분류 개편, 현금흐름표는? - CPA뉴스 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5kYi13cTFSSkpCS0VXWXdpMHBNdkJsMkEzR3ZuSjBvWG9iUkpnRXJxNnJnNllROGhOZWlVTXJ6QXRZU3ZRZ2U0d3h1UGZNYjIwbXdobGpsVUxhcDFjbkZPT1NNbHdCM2xD?oc=5 |  |
| kifrs | 일간NTN | ‘재무제표 정정·고의·중과실 손실 발생 시 이미 지급한 임원 성과급 환수’ - Daily NTN | https://news.google.com/rss/articles/CBMiakFVX3lxTE5yYUg1NHFSanRPdE0zcFNJZEhTWk11VFNtSldJdFZNOG5LT0tLaFhZZE5WT1JmSWNtV0dSaEsySmZhbmZuMWo2UWt3cVlCNlVvZG1QeklNUmpxc01kX2VmQi02bTZBRWE0RUE?oc=5 |  |
| kifrs | 조세일보 | 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... | http://www.joseilbo.com/news/news_read.php?uid=575253&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... | http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp= |  |
| kifrs | 조세일보 | 감리지적사례-회사 자금 유용 [재무회계] 회계부정 적발과 분식회계 중... | http://www.joseilbo.com/news/news_read.php?uid=575552&class=18&grp= |  |
| kifrs | 머니투데이 | "삼성전자 700조 저평가, 손절 말고 버티세요"…재무제표 뜯어보니[부꾸미] - 머니투데이 - 머니투데이 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE9pRkMzckl3eFF6Q3dvZEpsMUF3SnBMY0VuM08wR25IdFlIUVJJNV9jOUFSckVGbUdWck52QmZ2cER6SWZZblozbkhhNkNFc1ExTDFxOVlJYzY5ZEQ0X2Rpcmltenhta2t00gFuQVVfeXFMUFpSSDdnYlpoZWNObVJTdkVCYUVsSS1NXy1GZDUzUl9iV1BmRTJqOUFuejBWUkw0a01yeEo0SlYzT0pWaWVlcThWRWF4dVlRNlFrUHdUUkZjeVlaeFpxVDNUanpHTDdmbHZWMzJwUkE?oc=5 |  |
| kifrs | 매일경제 | “글로벌 투자자들, 재무제표급 ESG공시 원해” - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE5wb2Z4TVdNX0NsQndNU08tQldGZ2JGOFhpTmVTM2x2b0FtY2xYOEVPWGFRaFdhTWw3Rk1jQWNnRHJ3WldSa3RyV1RldHRhLXZsaVE?oc=5 |  |
| kifrs | tfmedia.co.kr | 회계기준원, 지속가능성 공시기준에 투자자 수요 반영…전문 위원회 확... | https://www.tfmedia.co.kr/news/article.html?no=209073 |  |
| kifrs | tleaves.co.kr | 미래에셋증권·스마일게이트 IPO 소송 2심…‘계약 취지’ vs ‘회계기준’ - 더리브스 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9kVTFRajhxMHdYZ3kwMkczZ3lQa3gxWXlMN0JySnZHbXM1dFlNZVNCN2tyQlRmU1VDdUNhNFA1VjBSYk9zWkhRQmpKNnRmQ0dmdmRRXzY5TUZKNFU1ZnF5TEJHMmw3QlctWHBR?oc=5 |  |
| kifrs | opinionnews.co.kr | 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 | https://news.google.com/rss/articles/CBMickFVX3lxTE9WeVlZRG8wdjhmVjFaMHYwQjNRcS1HbGhGc0RfQWF3eWJhb2FreXd2WjBtNDF6Q3pBZHdsT2Rlb1VQVWdkczF2ZDJXMkQyMzJSR0FtR1lXTkI4cmtlM090V2RMQWVBcndYX0YwcHhBb1hzQQ?oc=5 |  |
| kifrs | industrynews.co.kr | 두나무·빗썸 실적 '희비'…가상자산 평가손실 '회계기준'이 좌우해 - 인더스트리뉴스 | https://news.google.com/rss/articles/CBMickFVX3lxTFBfTndtNzZCY2tiYk1BWjdCX1EzSnN0ZkVrX1F5WF9oQVVlcE5QOHVQU19QQVNIZkE0T0k0T2RUM3lfREhHY0VLYk9qbnF3T1FRVl9lMVdJRnBsazltSWlyaUYtcEJVZU80Y0lBenFYZ25UQQ?oc=5 |  |
| kifrs | newsfc.co.kr | 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 | https://news.google.com/rss/articles/CBMiakFVX3lxTE5VMDZCcHJKdEg2cElfV3VMeGltTkdzamhGcXVCYVVnVE1DeGZOc3BoTlZacTVOakRiRTR2dDlaaG5kbXo3RkJUMkM4T0VhWmVPSkpzRDFpOE5QamZxX3JVeG1qemg5Nm9iNWc?oc=5 |  |
| kifrs | asiatoday.co.kr | 비용 반영? 우발부채?…국고채 과징금 직면한 금융권, 자의적 회계처리 논란 - 아시아투데이 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5admNuOThERUZlR0JDRmtFdkJxXzRLR0doR3htVTIzcnZrbDVicTcyb0cweExNd2JQSEtGa044RkVTLVByV1hMMGJPMUZ2WjRIaVpjU1RHQUV5SThvcXdQOGE0MncyY1AwWlZmX3hn?oc=5 |  |
| kifrs | gokorea.kr | 가상자산 거래소 두나무와 빗썸의 운명을 가른 회계 처리 차이 - 공감신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE41aWlnRHBobDR2VmtwZFcwMFhlWTRycmJJQkN1MTBTSWFGci1VS2o1SE5uUzVQR3daVVlEZmZqNlZZUXdjWUpuQmFNeXZCWWxfdUc2NGc0WVR5RFpWNk9EdVRNUmRWZ0xL?oc=5 |  |
| kifrs | safemoney.co.kr | 두나무 3분기 누적 898억 흑자 … 빗썸은 1102억 적자 - 세이프머니 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5IZlplYWhHQ01fRmlfTDBOenlLWWtQTDFPVllUOWhkR21fbDhYQ1N6aUI1a2YyaG1INmNRcmdUVkx2bVZoei1FZHZQT1YtX0dTNldhMFp6ZHp5aEw0VWRaNW5Oa3ZNOHc5TEdZbllR?oc=5 |  |
| kifrs | g-enews.com | 금감원 "내년 K-IFRS 제1118호 본격 적용…기업들, 점검 철저히" | https://www.g-enews.com/view.php?ud=202610130814147179923c501012_1 |  |
| kifrs | ebn.co.kr | '감독회계 포획'에 갇힌 K-IFRS17…보험사 회계 착시와 주주환원 훼손 | https://www.ebn.co.kr/news/articleView.html?idxno=1729955 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(67) 대도시 내 부동산 취득세 중과, '형식' 아닌... | https://www.intn.co.kr/news/articleView.html?idxno=3000354 |  |
| tax | 일간NTN | 세무법인HKL '稅相 읽기'(64) 토지의 무상사용과 재산세 비과세의 실질 | http://www.intn.co.kr/news/articleView.html?idxno=2054488 |  |
| tax | 머니투데이 | 전기차도 국내생산세액공제 대상 포함 유력…이르면 이번주 결론 | https://www.mt.co.kr/industry/2026/11/22/2026112210573377519 |  |
| tax | 매일경제 | "전입신고 늦어도 실거주땐 취득세 감면" | https://www.mk.co.kr/article/12214810 |  |
| tax | 매일경제 | 법인세 늘고 과징금까지 … 금융지주 비상 | https://www.mk.co.kr/article/12211463 |  |
| tax | 서울경제 | [단독] 추미애표 ‘지방법인세’에 재경부 난색…교부세 재원 감소 우려... | https://www.sedaily.com/article/20113784?ref=naver |  |
| tax | 서울경제 | [단독] 재경부, 추미애 제안 ‘지방법인세’ 신설에 “중장기 검토” 제... | https://www.sedaily.com/article/20113591?ref=naver |  |
| tax | sejungilbo.com | 김석기, 게임물도 세액공제 대상 포함 추진…비수도권 제작 시 공제율 ... | https://www.sejungilbo.com/news/articleView.html?idxno=61213 |  |
| tax | news.bizwatch.co.kr | 국산 전기차 세액공제 확대 가닥에도…정부 막판까지 고심 이유 | https://news.bizwatch.co.kr/article/industry/2026/11/20/0030 |  |
| tax | newspim.com | 중국산 전기차 침투 속도 韓 3위…"국내생산세액공제 필요성 커" | https://www.newspim.com/news/view/20261122000099 |  |
| tax | updownnews.co.kr | 기아, 현대카드 포인트 부담분 부가세 환급 불발…"결정 존중·소송 취하... | https://www.updownnews.co.kr/news/articleView.html?idxno=319665 |  |
| tax | sejungilbo.com | [판세] 과세기간이 다른 여러 국가의 소득, 외국납부세액공제 계산방식... | https://www.sejungilbo.com/news/articleView.html?idxno=60678 |  |
| tax | dnews.co.kr | 도시철도 영세율 연장 입법 ‘잰걸음’…JTX·수도권서남부선 세 부담 ... | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202611181437550170654 |  |
| tax | news.dealsitetv.com | 中 전기차에 안방 내줘…세액공제 시급 | https://news.dealsitetv.com/articles/178820 |  |
| tax | koit.co.kr | 정보보호 투자·인력 채용에 세액공제 추진 | https://www.koit.co.kr/news/articleView.html?idxno=209966 |  |
| tax | econovill.com | 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 | https://www.econovill.com/news/articleView.html?idxno=757588 |  |
| tax | news.ifm.kr | 추미애 경기지사, 재정 위기 돌파 총력…지방세제 개편·교부단체 전환... | https://news.ifm.kr/news/articleView.html?idxno=484643 |  |
| tax | nocutnews.co.kr | 300조원 보조금 받은 中 전기차…한국도 세액공제 절실 | https://www.nocutnews.co.kr/news/6608058?utm_source=naver&utm_medium=article&utm_campaign=20261117133938 |  |
| tax | sejungilbo.com | AI 덕에 반등한 법인세수, 올해 세법심사서 '세율인하' 결론은? | https://www.sejungilbo.com/news/articleView.html?idxno=61111 |  |
| tax | sejungilbo.com | [판세] 사업 관련성 없는 지출의 매입세액공제 여부와 부가세법상 '수입... | https://www.sejungilbo.com/news/articleView.html?idxno=60677 |  |
| tax | sejungilbo.com | [절세톡톡] 일시적2주택 취득세, 용도변경도 종전주택처분일까요? | https://www.sejungilbo.com/news/articleView.html?idxno=61088 |  |
| tax | biz.chosun.com | 자사주 팔아 남겨도 법인세 안 낸다… 손실 비용처리도 폐지 | https://biz.chosun.com/industry/company/2026/11/15/IXNR6UW5WJDKBGYPBVV2URUQXI/?utm_source=naver&utm_medium=original&utm_campaign=biz |  |
| tax | the-today.com | 미국 보수 세액공제 막힌 구본성…쟁점은 근무지... 왜? | https://www.the-today.com/news/articleView.html?idxno=93441 |  |
| tax | fieldnews.kr | [단독] 하나투어, 항공권 부가세 환급 놓고 국세청과 공방…조세심판원... | http://www.fieldnews.kr/news/articleView.html?idxno=32758 |  |
| tax | incheonilbo.com | 여야, 앞다퉈 입법…소방·지방세입 확충 구체화 | https://www.incheonilbo.com/news/articleView.html?idxno=1336375 |  |
| tax | kyeonggi.com | 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUkZjcmNGVThXaXFwdlpfS0pUVjVMQXJMYUJ4YnF5TVo0SjRHcXZiekNScnkzeWhaT25kWkhFTlhabGZZdmxnSllpU2YwWG53YjFfT3lzUWlSMkE?oc=5 |  |
| tax | sejungilbo.com | [절세톡톡] 매매계약에 따라 상가로 용도변경후 양도한 경우 부가가치세... | https://www.sejungilbo.com/news/articleView.html?idxno=59962 |  |
| tax | fieldnews.kr | [단독] LH, 서울시에 옛 서울의료원 부지 무상 제공했는데 재산세…심판... | http://www.fieldnews.kr/news/articleView.html?idxno=32880 |  |
| tax | fieldnews.kr | [단독] 경기주택도시공사, 공공임대 지으려 빈집 철거했다가 취득세 추... | http://www.fieldnews.kr/news/articleView.html?idxno=32624 |  |
| esg | ESG경제 | ESG공시 인증 환경 변화...AA1000 기준 어떻게 활용될까 | https://www.esgeconomy.com/news/articleView.html?idxno=17471 |  |
| esg | ESG경제 | EU, ISSA 5000 기반 지속가능성 공시 인증기준 초안 공개 | https://www.esgeconomy.com/news/articleView.html?idxno=17391 |  |
| esg | ESG경제 | KEMI, 지속가능경영·동반성장 우수기업 9곳 선정 | https://www.esgeconomy.com/news/articleView.html?idxno=17378 |  |
| esg | ESG경제 | [ESG 신간] 'KSSB 법정공시 전환 2026' 실전 가이드북 - ESG경제 | https://news.google.com/rss/articles/CBMibEFVX3lxTFBrUzRGU3pWdmpXamtLdlFab3psaXNSNWQ4UzVhTm12SDlsNkt1U2xxVFY0VFVGY2JScGxPX1o3cGRaY2JqSlJWT2QxRURKSGItTWVyLW4zY2h6bTNRYy1EOS1YUE9wUWJxamd5ZA?oc=5 |  |
| esg | 임팩트온 | 노르웨이 국부펀드, EU 역외기업 공시에 자발적 ISSB 보고서 활용 요구 | https://www.impacton.net/news/articleView.html?idxno=30527 |  |
| esg | ESG경제 | ISSB 자연 관련 공시 실무서 들여다 보니...S1ㆍS2 보완 | https://www.esgeconomy.com/news/articleView.html?idxno=17209 |  |
| esg | ESG경제 | 지속가능성 공시 파일럿 테스트에서 수집된 기업의 애로는? | https://www.esgeconomy.com/news/articleView.html?idxno=17196 |  |
| esg | KPMG | 지속가능성 의무공시 시대, 기업의 공시는 어떻게 달라지는가? - kpmg.com | https://news.google.com/rss/articles/CBMibkFVX3lxTE1qWkg4MnRXWGhoQ0RHdFdwMlJOUTg4bm1FSWtobWw4X1JNdE0tTUlndWJ6QmktSHFidGgxVUFxQVBQeUhNbE9VTFdvcTV1OXVWYTdObFhLdElZYTg0NkQ0MUwwN0ZabGlVU3hMeWFR?oc=5 |  |
| esg | 매일경제 | “글로벌 투자자들, 재무제표급 ESG공시 원해” | https://www.mk.co.kr/article/12211811 |  |
| esg | 매일경제 | "ESG공시, 재무제표급으로" | https://www.mk.co.kr/article/12211428 |  |
| esg | 한국경제 | ESG 의무공시 본격화, 기업 밸류업 골든타임 왔다 - 한국경제 | https://news.google.com/rss/articles/CBMiWkFVX3lxTFBMMkdOYi1ka3NqWVdLWHZPalRkcWplcUhuOWw2ODJwSTF3SUtUd3AwTlhhc2ZQZElaczlkdjRwSnotLVFyLWtHaDRIdG9RcW12VDB0UlRNNFk5QQ?oc=5 |  |
| esg | insnews.co.kr | [시론] ESG 공시와 보험계약자 권익 보호 | https://www.insnews.co.kr/news/articleView.html?idxno=93911 |  |
| esg | metroseoul.co.kr | 한국보험연구원 "보험금 지급·민원 처리도 ESG 공시로" | http://www.metroseoul.co.kr/article/20261122500040 |  |
| esg | insnews.co.kr | (사)한국보험연구원, '2028년 ESG 공시와 보험업의 과제' 세미나 개최 | https://www.insnews.co.kr/news/articleView.html?idxno=93975 |  |
| esg | finomy.com | 보험업 ESG 공시, 소비자 신뢰 회복 계기 활용 논의 본격화 | http://www.finomy.com/news/articleView.html?idxno=267488 |  |
| esg | enewstoday.co.kr | '지속가능경영보고서' 세계 6위···부산항만공사, 국제시상식서 최고... | http://www.enewstoday.co.kr/news/articleView.html?idxno=2495286 |  |
| esg | raonnews.com | 107개사 ESG 공시 내년 실적부터 적용…근거법은 아직 국회 통과 전 | https://www.raonnews.com/news/article.html?no=62862 |  |
| esg | mediapen.com | 수자원공사·WWF, '물·자연 통합 복원' 나선다…기업 ESG 공시 대응 지... | https://www.mediapen.com/news/view/1138078 |  |
| esg | biz.newdaily.co.kr | 한국생산성본부, 에코바디스·코트라와 중소·중견기업 공급망 실사 지... | https://biz.newdaily.co.kr/site/data/html/2026/11/20/2026112050115.html |  |
| esg | dailyt.co.kr | "넷제로 2050" 보험사 줄줄이 선언하는데…기준 없는 지속가능성 공시,... | https://www.dailyt.co.kr/newsView/dlt202611150019 |  |
| esg | cnbizm.com | 백화점 업계, 상생·지속가능경영 성과 결실 | https://www.cnbizm.com/news/articleView.html?idxno=321436 |  |
| esg | ajunews.com | ESG경영개발원, 지속가능경영·동반성장 우수 기업·공공기관 선정 | https://www.ajunews.com/view/20261113135722843 |  |
| esg | kbmaeil.com | ‘지속가능성 공시’ | https://www.kbmaeil.com/article/20261112500036 |  |
| esg | dailysmart.co.kr | "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... | http://www.dailysmart.co.kr/news/articleView.html?idxno=132423 |  |
| esg | seoulfn.com | 회계기준원, KSSB 공시기준 전문가 TF 가동···실무 쟁점 52건 논의 | https://www.seoulfn.com/news/articleView.html?idxno=641503 |  |
| esg | lawtimes.co.kr | 국내 ESG 공시 제도화 본격 시동 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5kbk1xU0x1a0cwQVljOE04dEhreG85a3BjM0t6c1FxSDlhNjlwYWFLTTY4SnV0OVNzNkhCYzBRcW00bm5BUUZTa3Mzc2MtaEZQbzljanBEeE1RaEx1bUstRDdZNHl5ZDF6dXl0Z0Rn0gFyQVVfeXFMTUVhTndvYnNDYmRtMnFfVFI4Y3FNNEotRU1jZEdyRVROb3gtdktfYUV0UTFaSWRELXZCZktPX1VqSU9mTGd3b3VoU0FyTHo5Qm5ybjkzTVNIVmVKLXRyb0F0bVp3eC1oMjVJa3lROVgycTlR?oc=5 |  |
| esg | lawtimes.co.kr | ESG 공시 제도화 관련 이슈리포트 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5EMkpMWHJyY2VNTVVVNmtTY3kwZWZYWVZiVUJJckppUG1jVXVKNTgtVVNNUUR3ZjhRM1ZET1lVQjhsRVZsRUhiSUdkSTg4Zk1zbURTVWRoYXNrc0hzMjFmNFI0RDhqSDlZNWU5NGFR0gFyQVVfeXFMTjVFZ25veU9tNzdSeXRNRmFEc0t5MlY0ZVBOaV9mUTctZW1JeG5DNnA4amE4TmZRVEFxa2FfN1RDNkN2ZmkzVXNpeWk4V21FOXdYaURLWmc5eTZ2SE9nV3dScVFzM3JmTVNsUWlvSjZkZTNn?oc=5 |  |
| icfr | mediapen.com | [ESG특별기고]데이터 내부통제체계, 지속가능성 공시 신뢰도 확보의 초... | https://www.mediapen.com/news/view/1138165 |  |
| icfr | news1.kr | 최운열 한공회장, 세계에 신외감법 성과 알려…"韓 회계투명성 껑충" - 뉴스1 | https://news.google.com/rss/articles/CBMiX0FVX3lxTE9ITUEzOUMwcWJBVFF4cWRyT2NmZ2xKeHh1V2o0RVhVVmF6T3RkYUxzMGlCRFVtZ0pqNkdMV1hpUTdRaWpCOXVIc0lQY0Q2NUZCcHRoR3pCdnZNTkVyZFpR?oc=5 |  |
| icfr | lawtalk.co.kr | 회사 재무제표를 부풀렸는데 외감법 위반으로 처벌되나요 - 로톡 | https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SNHVGNVhqcF9pRjBSSFEtUzNPWWtJQldRYVAyY1hXZW1xaFB3ZWdKd1JHcXhXQ2YwQWU4cVBnWXNPcHZwYlhmU3NMWk9fd2M?oc=5 |  |
| icfr | news.koreanbar.or.kr | ‘통과 목전’ 비밀유지권부터 외감법까지… 변협 추진 입법, 어디까지 왔나 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTE9rRC1majFwY1RhWm1sblJhbnFmcXppU2owcjhmRmZOcmxNb3drX3MwWTNPR0Q5VjFUTGNLWXRaOC1ZZmJNWVhTT2VlV3UySWh0UmVXQTRmMTg1bXRxVlo2S0g5VWZ4Y0xJdC1oY201VQ?oc=5 |  |

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

## excluded:similar_news_merged (50건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | 한국경제 | 회계기준원, 투자자 전문위원회 12인으로 확대…위원장에 이현승 LHS운용... | https://www.hankyung.com/article/202611200435r | → 대표: 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 |
| kifrs | popcornnews.net | 회계기준원, 투자자 전문위원회 12명으로 확대 | http://www.popcornnews.net/news/articleView.html?idxno=140944 | → 대표: 회계기준원, 투자자 전문위원회 12인으로 확대…첫 회의 개최 |
| kifrs | greened.kr | 새출발기금, 회계처리 오류로 과거 손실 600억 늘어…재무제표 다시 작성 - 녹색경제신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE5VWExRb21kWUZMSWk4d0NUUVpqQ3UzQXdtOHZzY3QybEJ1Vk9NbDhVQ2RaWVlISUY2bE9tQkg4clltVEVfLWFvcm9PMDNicHdvdV9FNzIybVZoN3JtdXlTemRHZmxzc1Z1?oc=5 | → 대표: ‘재무제표 정정·고의·중과실 손실 발생 시 이미 지급한 임원 성과급 환수’ - Daily NTN |
| kifrs | auto-today.co.kr | 김현정·민주당, 재무제표 정정되거나 고의·중과실로 손실 내면 이미 지급한 성과보수 환수 … 퇴직자 포함 - 오토투데이 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBiTHFsYXdCbXFQVzdtbkFwUEE1cy1DRDlfdEdPMmp3NGVYUTdWLW4zNVpoZVNQR1ltNUF0QWp5SlVvRERkS09pXzhSSEhBcmpmR05KSExrVlJQcUhuMEFzakJxVHQwOGVDRUQxRkNWVQ?oc=5 | → 대표: ‘재무제표 정정·고의·중과실 손실 발생 시 이미 지급한 임원 성과급 환수’ - Daily NTN |
| kifrs | 조세일보 | 감리지적사례-하도급계약: 유상사급 거래 [재무회계] 회계부정 적발과 ... | http://www.joseilbo.com/news/news_read.php?uid=575130&class=18&grp= | → 대표: 감리지적사례-회계기준 관련 [재무회계] 회계부정 적발과 분식회계 중심... |
| kifrs | 조세일보 | 감리지적사례-전환사채 [재무회계] 회계부정 적발과 분식회계 중심으로 | http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp= | → 대표: 감리지적사례-매출채권 허위계상 [재무회계] 회계부정 적발과 분식회계... |
| kifrs | 매일경제 | 올해 두나무 흑자·빗썸 적자…"배경엔 회계기준 차이" - 매일경제 마켓 | https://news.google.com/rss/articles/CBMiUkFVX3lxTE9LX2JDMFhsRXJOQThUVDh1OTFTcl82am5FcUJ0NGQzdXZtVE5wRUNudF9qTkZHSFAtdmw3V1VIWXlwWEdZVmI5Y1hwUEx0ZFotV2c?oc=5 | → 대표: “글로벌 투자자들, 재무제표급 ESG공시 원해” - 매일경제 마켓 |
| kifrs | biz.sbs.co.kr | 엔비디아 회계장부 들여다보는 美 SEC…매출 공시·회계 처리 조사 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5iWm9mNWpzT2hVYmR1MkVOc0tVWHBpVm5Ebllyclh6RnlzUmZHM2hDY0lSWkpDV0h4amNJUFBOdG1GWDFBNXJ2RVdsWUlVNkhWRExZ0gFYQVVfeXFMUFFiUGh0azUxYUVFeHZzS1dqT0c1bE40TEdJYkV0OENjdjFqMjF6N2pseVlxOWRyYjVfdVhselFsQzJYeThBVFRyVzF3SjdRbUdHWHZ0WGhCLQ?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | gokorea.kr | SEC, 엔비디아 조사 착수: 회계 처리 방식 논란 속 파장 커지나 - 공감신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTFBfTFIxN2N4MU9VcU1DMUlqRmZ1NTlyckhzRW5pUm55NUd0OFRlVFVha1lxU0ZJallETWFWYy1KX2oxVk1fdzg3NUpHMkxKWFFtM2NUUHB4MlEzSVdfSGRxLVV2TnY3Smpm?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | blockmedia.co.kr | 미 SEC, 엔비디아 회계처리 조사… AI 반도체 공룡에 규제 압박(종합) - 블록미디어 | https://news.google.com/rss/articles/CBMiWEFVX3lxTE5rOVlzZmJuMlh0MWVseXdRaHhucVlZWC1RbmZZSjJ0X1I2Uks0TXBFSWxFRXpzTmlUbkxwUlhvLWRTdjU1VGFpNkpIZlN1QW02VXdUbExZcFg?oc=5 | → 대표: 美 증권위, 엔비디아 회계 처리 방식 조사 - 오피니언뉴스 |
| kifrs | sentv.co.kr | 양대 거래소 두나무 흑자·빗썸 적자…회계기준 차이가 갈랐다 - 서울경제TV | https://news.google.com/rss/articles/CBMiZEFVX3lxTE14YzJVYUVpOU4zZXNOa1pUSVNaWDNLcGhHdUpDOXN4cjlhS2dsUVBQQW5qaDJhS2VOcTJEbWxuelhHaExKVEt6UHVjNjJtSFRRTFF0b2wydm9GUVYxY1lCOTI4bkc?oc=5 | → 대표: 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 |
| kifrs | polinews.co.kr | 두나무 898억 흑자·빗썸 1102억 적자…가상자산 회계기준 차이가 순손익 갈랐다 - 폴리뉴스 Polinews | https://news.google.com/rss/articles/CBMibkFVX3lxTE4xSHVHdlk3dk84N0JydWY3azBtME14WmtRUVprRU5zdWVidGxLYVpneGNZNHZnYlFBT2V6eG9rVS1vX2g3NThNRzZ4cGRuTVVkVks4cHRRa0tqdEk2azNQNTRvUzUtTTZRV2cySERn?oc=5 | → 대표: 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 |
| kifrs | biz.sbs.co.kr | 두나무 흑자·빗썸 적자 배경엔…업계 회계기준 차이 - SBS Biz | https://news.google.com/rss/articles/CBMiU0FVX3lxTE5SQzNMZUM0ZUszQm52d2lneHpLTzJndC11OUx3MmdZVHFGeVIta1lCcUtkS1IzZU1WUEROR2hyVUxRcTd0Z0lpckNma0ZMdlBHal9J0gFYQVVfeXFMT3luQV9zaXFjc3U1NGtYYmVtbGQzT3BKVllmWjN0clZvY2l1UHowdkhzdHhHS2xVSnVtcTFzZFpIZXVpdzcxU21SYXptVjlvd2xJZ0VxdHI0Rg?oc=5 | → 대표: 두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비자뉴스 |
| tax | 매일경제 | 국힘 “민주당 종부세 반란 4일 천하”…법인세율 1%P 인하 촉구 | https://www.mk.co.kr/article/12207950 | → 대표: 국힘 "법인세 전 구간 1%p 인하·주52시간제 완화 추진해야" |
| tax | 파이낸셜뉴스 | 野 "법인세 1%p 인하·주52시간제 완화 추진해야" | https://www.fnnews.com/news/202611130943014682 | → 대표: 국힘 "법인세 전 구간 1%p 인하·주52시간제 완화 추진해야" |
| tax | sejungilbo.com | 박수영, 법인세율 전 구간 1%p 인하 추진…2026년 인상 이전 수준 환원 | https://www.sejungilbo.com/news/articleView.html?idxno=61067 | → 대표: 국힘 "법인세 전 구간 1%p 인하·주52시간제 완화 추진해야" |
| tax | news1.kr | 조세심판원 "첫 집 전입신고 111일 만에 마쳤어도 취득세 감면 인정" | https://www.news1.kr/politics/president/6360765 | → 대표: "전입신고 늦어도 실거주땐 취득세 감면" |
| tax | biz.sbs.co.kr | 조세심판원 "전입신고 늦어도 실거주 땐 취득세 감면 유효" | https://biz.sbs.co.kr/article_hub/20000347776?division=NAVER | → 대표: "전입신고 늦어도 실거주땐 취득세 감면" |
| tax | yonhapnewstv.co.kr | 조세심판원 "전입신고 늦어도 실거주 땐 취득세 감면" | http://www.yonhapnewstv.co.kr/news/AKR20261120103447oGO | → 대표: "전입신고 늦어도 실거주땐 취득세 감면" |
| tax | yna.co.kr | 조세심판원 "전입신고 지연돼도 실거주 확인시 취득세 감면" | https://www.yna.co.kr/view/AKR20261119156700001?input=1195m | → 대표: "전입신고 늦어도 실거주땐 취득세 감면" |
| tax | taxwatch.co.kr | 111일 만에 전입신고…취득세 감면 인정된 이유 | https://www.taxwatch.co.kr/article/tax/2026/11/19/0002/naver | → 대표: "전입신고 늦어도 실거주땐 취득세 감면" |
| tax | bizwnews.com | 인천시, 전국 광역자치단체와 친환경 버스 부가세 면제 유지 공동 대응... | http://www.bizwnews.com/news/articleView.html?idxno=151202 | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | biz.heraldcorp.com | 서울시 “친환경 버스 부가세 면제 유지해야”…15개 지자체와 공동 | https://biz.heraldcorp.com/article/10929011?ref=naver | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | inews24.com | "전기버스 1대당 3500만 원 세금 폭탄"… 인천시, 부가세 면제 유지 총력 | http://www.inews24.com/view/2023254 | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | ic.newdaily.co.kr | " ‘친환경 버스 부가세 면제’ 현행대로 유지해야 " …인천시, 전국 지... | https://ic.newdaily.co.kr/site/data/html/2026/11/06/2026110600034.html | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | segye.com | “친환경버스 부가세 면제 유지해야” | https://www.segye.com/newsView/20261105515473?OutUrl=naver | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | seoul.co.kr | 전국 16개 지자체 “친환경버스 부가세 면제 특례 유지” 촉구 | https://www.seoul.co.kr/news/publicnews/local_govern/2026/11/06/20261106019008?wlog_tag3=naver | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | nspna.com | [정책 짚어보기] 친환경 버스 부가세 면제 축소 추진…인천시 “내년 7... | https://www.nspna.com/news/?mode=view&newsid=834837 | → 대표: 서울시 “친환경버스 부가세 면제 유지해 달라” |
| tax | donga.com | 저가 중국산 전기차 공습 시작에 불과…車업계 “생산세액공제 필요” | https://www.donga.com/news/Economy/article/all/20261122/135068653/1 | → 대표: 전기차 생산세액공제 도입 공감대…'공제액·수출차·통상 마찰' 변수 |
| tax | donga.com | ‘저가’ 中전기차, 韓 잠식 세계 3번째 빨라… “국산 세액공제 필요” | https://www.donga.com/news/Economy/article/all/20261123/135070386/2 | → 대표: 국산 전기차 세액공제 확대 가닥에도…정부 막판까지 고심 이유 |
| tax | news1.kr | "韓, 中 전기차 안방 됐다 아시아 최다 수출국"…세액공제 시급 | https://www.news1.kr/industry/auto-industry/6356396 | → 대표: 中 전기차에 안방 내줘…세액공제 시급 |
| tax | zdnet.co.kr | 中 전기차 공습에 국산차 점유율 '뚝'…국내 생산세액공제 힘 받나 | https://zdnet.co.kr/view/?no=20261117105815 | → 대표: 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 |
| tax | donga.com | 중국 전기차 큰 손 된 한국… 국내 생산세액공제 논의 불붙나 | https://www.donga.com/news/Economy/article/all/20261117/135036997/2 | → 대표: 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 |
| tax | news1.kr | 靑, 전기차 생산세액공제 조건부 포함 가닥…국회 논의 주목 | https://www.news1.kr/politics/president/6354053 | → 대표: 국산 전기차 과반 무너져...생산세액공제 문 다시 열린다 |
| tax | econovill.com | 中 전기차 공세 거세지자…국내 생산 세액공제 논의 탄력 | https://www.econovill.com/news/articleView.html?idxno=757505 | → 대표: 300조원 보조금 받은 中 전기차…한국도 세액공제 절실 |
| tax | etoday.co.kr | 중국산 전기차 보조금 수혜 확대…국내생산세액공제 입법 논의 골든타임... | https://www.etoday.co.kr/news/view/2647835 | → 대표: 300조원 보조금 받은 中 전기차…한국도 세액공제 절실 |
| tax | viva100.com | 정부, 국회와 전기차 세액공제 논의 ‘본격화'… 부처별 온도차는 과제 | https://www.viva100.com/article/20261115500528 | → 대표: 300조원 보조금 받은 中 전기차…한국도 세액공제 절실 |
| tax | cstimes.com | 인천시, 전국 16개 시도와 친환경 버스 부가가치세 면제 특례 유지 '한목... | https://www.cstimes.com/news/articleView.html?idxno=726889 | → 대표: 인천시, 친환경 버스 부가세 면제 유지 공동 대응 |
| tax | news.ifm.kr | 추미애 지사 '지방세제 개편안' 국회로…지방소비세율 25.3%→40.3% - 경인방송 뉴스 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE0yTlpFX243TktMVXNrRWxyUGF4ZjVRNUMzQ1J6Vm5JTFhYM3BLR04zNjFGWkVMeXp5SG9JTE90WHZnajloQkRXNjB6dl82eC1tWURISjV5d3BjYXM2c1FWNVdON0vSAWhBVV95cUxNNWdtNnZSYW0wN0hDR2QzUFRuNFVVOE1WeFBlTXZnSDNjRVRKa2ZaWW5pNHZkbnNkLXZ1b3B6UXRNc0N6NGJWTWpPYXR6RFFXdTllcUNYVFVPMWlJeVhoZmxRT1FXenhNZg?oc=5 | → 대표: 추미애 제안 ‘지방세제 개편 3대 과제’ 국회 입법 절차 돌입 - 경기일보 |
| esg | lawtimes.co.kr | 금융위, 지속가능성(ESG) 공시 로드맵을 통한 제도화 방안 확정 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9HODdkYURIX08xRXZZWV80VG1LOExsYUlhYnhpbUlFWlJ6enFCM3ExRUdkekhEY180Sk9OS3lqenJhQmZ0WHRuVENaVWEyWTZQQ1lUTTkyUFgyT2pxdC01ek1JRXpOWm1hZXhPNTBn0gFyQVVfeXFMUFdFT2FsVlNLc1UyZHRRQUdzOGgzN2FXSWs4dnpXdncxVlMwbUlvRThTNi1OZldobktzSkVvS01PUk1IRHNHWVFXdXh2WXVHZHBMaUlRb1RkeGFBbjJnOVFhZk5pNmloSXp4OFBIdlZpTFV3?oc=5 | → 대표: 지속가능성(ESG) 공시 제도화 확정 - PwC |
| esg | fins.co.kr | 보험사 ESG 공시, 보험금 지급·민원처리까지 담아야 | http://www.fins.co.kr/news/articleView.html?idxno=110656 | → 대표: 한국보험연구원 "보험금 지급·민원 처리도 ESG 공시로" |
| esg | m.ekn.kr | TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 - 에너지경제신문 | https://news.google.com/rss/articles/CBMiW0FVX3lxTE1ZRHhKeVl5Yi1rVTdJcGwyQ0dnUUFyR01SZGQtX252WTRVaTU1NEVDQVFmSncwcHYtMDZwbW1qUmhjN052U1IzSks1Ym5ISXhYWHNkdGo5bHg3Qzg?oc=5 | → 대표: TNFD, “자연공시 실무서 아닌 공시기준으로”…ISSB에 제도 강화 권고 |
| esg | news.bbsi.co.kr | 부산항만공사, 지속가능경영보고서 3년 연속 최고 등급 | https://news.bbsi.co.kr/news/articleView.html?idxno=4119928 | → 대표: '지속가능경영보고서' 세계 6위···부산항만공사, 국제시상식서 최고... |
| esg | seoul.co.kr | 부산항만공사 지속가능경영보고서, 국제 대회서 3년 연속 최고등급 | https://www.seoul.co.kr/news/society/2026/11/20/20261120500249?wlog_tag3=naver | → 대표: '지속가능경영보고서' 세계 6위···부산항만공사, 국제시상식서 최고... |
| esg | view.asiae.co.kr | 부산항만공사, 美 LACP 지속가능경영보고서 평가 3년 연속 최고등급 수... | https://view.asiae.co.kr/article/2026112015500531580 | → 대표: '지속가능경영보고서' 세계 6위···부산항만공사, 국제시상식서 최고... |
| esg | ziksir.com | KB금융, 한국ESG기준원 평가 통합 A+ 획득…지속가능경영 성과 인정 | https://www.ziksir.com/news/articleView.html?idxno=153110 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | weekly.hankooki.com | 신세계百, ESG 평가 2년 연속 종합 A+…지속가능경영 성과 | https://weekly.hankooki.com/news/articleView.html?idxno=7193568 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | fashionbiz.co.kr | 신세계백화점, ESG 평가 2년 연속 A+... 지속가능경영 성과 | https://www.fashionbiz.co.kr/article/231039 | → 대표: 백화점 업계, 상생·지속가능경영 성과 결실 |
| esg | globalepic.co.kr | KB금융, 한국ESG기준원 평가서 통합 'A+ 등급'…지속가능경영 리더십 입... | https://www.globalepic.co.kr/view.php?ud=2026111210164730997cc35ccc5c_29 | → 대표: "지속가능경영의 정점을 찍다"… KB금융그룹, 한국ESG기준원 평가서 통... |
| esg | thefairnews.co.kr | KB금융, KCGS ESG 평가서 최고 등급 'A+'…지속가능경영 리더십 입증 | https://www.thefairnews.co.kr/news/articleView.html?idxno=93912 | → 대표: KB금융, ESG 평가서 A+ 획득...지속가능경영 강화 |

## excluded:smb_only (4건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| kifrs | crowe.com | 일반기업회계기준 및 한국채택국제회계기준 제•개정(금융위, 증선위) - Crowe | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAzN1JEWkExdldzcU9LdWhzZGE5NnN5eW0xRG5FUmM4LUlMOHhzQ2tacGttTllYNkJteDdGdG9mX3hfV0xGUmU3bW9OY05FOWVWOXZoLWF4eG4?oc=5 |  |
| tax | gnmaeil.com | 부가세 간이과세 2억원으로 상향 추진 | http://www.gnmaeil.com/news/articleView.html?idxno=598793 |  |
| tax | yangsanilbo.com | 윤영석, 부가세 간이과세 기준 2억원 상향 추진 | http://www.yangsanilbo.com/news/articleView.html?idxno=128709 |  |
| tax | imaeil.com | 부동산 중개수수료 요율표는 상한…부가세 10%, 간이과세 중개업소는 4... | https://www.imaeil.com/page/view/2026101018554473359 |  |

## excluded:standard_setter_governance (1건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
| esg | 한국회계기준원 | 2026년 제9회 지속가능성기준위원회(IFRS 재단 정관 개정 공개초안에 대한 검토의견) | https://www.kasb.or.kr/front/board/calViewA.do?seq=1133 |  |

## collect:event_announcement (19건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
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
|  | 금융감독원 | 제10차 지정대리인 심사위원회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225188&menuNo=200218 |  |
|  | 금융위원회 | 금융정보분석원 설립 25주년 및 제20회 「자금세탁방지의 날」 기념식 개최. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88183?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 정책브리핑(금융위원회) | 금융정보분석원 설립 25주년 및 제20회 「자금세탁방지의 날」 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790315&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
| esg | metroseoul.co.kr | 부산항만공사, 미국서 지속가능경영 부문 '플래티넘' 수상 | http://www.metroseoul.co.kr/article/20261122500211 |  |
| esg | cnbnews.com | BPA, 미 LACP '지속가능경영보고서' 3년 연속 플래티넘 수상 | https://www.cnbnews.com/news/articleView.html?idxno=1024701 |  |

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

## collect:no_category (272건)

| 카테고리 | 출처 | 제목 | 링크 | 비고 |
|---|---|---|---|---|
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
|  | 금융감독원 | FIU, 자금세탁방지 유관기관 협의회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225288&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 여신전문금융회사 영업실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225267&menuNo=200218 |  |
|  | 금융감독원 | 2026년 상반기 보험회사 경영실적(잠정) | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225268&menuNo=200218 |  |
|  | 금융감독원 | 기업에게 알려드립니다 확정급여형(DB) 퇴직연금 이렇게 운용하면 달라집니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225146&menuNo=200218 |  |
|  | 금융감독원 | 지연된 PF 사업장을 청년, 신혼부부 보금자리로 신속하게 공급합니다 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225142&menuNo=200218 |  |
|  | 금융감독원 | 26.7월중 기업의 직접금융 조달실적 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=225136&menuNo=200218 |  |
|  | 금융감독원 | AI 시대 국민의 일상과 생업을 잇는 마이데이터 발전방안을 추진합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224945&menuNo=200218 |  |
|  | 금융감독원 | 소비자 눈높이에 맞는 공모펀드 투자위험 안내를 위하여 펀드 핵심위험 표준안을 도입합니다. | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224922&menuNo=200218 |  |
|  | 금융감독원 | 금융감독원, 자산운용사 의결권 행사, 공시 설명회 개최 | https://www.fss.or.kr/fss/bbs/B0000188/view.do?nttId=224903&menuNo=200218 |  |
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
|  | 재정경제부 | 긴급 시장상황점검회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080021&menuNo=4010100 |  |
|  | 재정경제부 | '26.11월 국고채 「모집 방식 비경쟁인수」 발행 미실시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000080007&menuNo=4010100 |  |
|  | 재정경제부 | 2026년 3분기말 대외채권채무 동향 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079995&menuNo=4010100 |  |
|  | 재정경제부 | 전략경제자문단 우주분과 현장 방문 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079999&menuNo=4010100 |  |
|  | 재정경제부 | 대외경제협력기금-시민사회 간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079991&menuNo=4010100 |  |
|  | 재정경제부 | 「양극화 대응 TF」 세대 격차 완화반 1차 회의 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079988&menuNo=4010100 |  |
|  | 재정경제부 | 경남창원 수출플러스간담회 개최 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079984&menuNo=4010100 |  |
|  | 재정경제부 | 국산 중고차 수출 원산지 증명 간소화 추진 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079957&menuNo=4010100 |  |
|  | 재정경제부 | [보도참고] '26년 국제통화기금(IMF) 연례협의 결과 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079980&menuNo=4010100 |  |
|  | 재정경제부 | 「세무사 시험 부정행위 대응 TF」 킥오프 회의 및 세무사 시험 부정행위자 시험 무효 절차 개시 | https://mofe.go.kr/nw/nes/detailNesDtaView.do?searchBbsId1=MOSFBBS_000000000028&searchNttId1=MOSF_000000000079971&menuNo=4010100 |  |
|  | 금융위원회 | 이억원 금융위원장, 글로벌 금융안정 공조와 한-유럽 금융협력 강화로  한국 금융의 지평 넓혀. 금일 등록된 게시글 | https://www.fsc.go.kr/no010101/88182?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 깜빡 잊고 지나가버린 지난 3년간 실손보험금, ‘실손24’를 통해  한방에 청구하고 받을 수 있습니다 | https://www.fsc.go.kr/no010101/88173?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 핀테크 기업에 필요한 지원사업을 AI가 찾아드립니다. | https://www.fsc.go.kr/no010101/88171?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 全금융권이 상시적으로 철저하게 보안 관리에 임하도록 IT자산 식별·관리를 의무화하고 취약점 점검·평가 제도를 내실화하겠습니다. | https://www.fsc.go.kr/no010101/88162?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 지역이 발굴하면 금융이 뒷받침한다. 지역 핵심 중소·중견기업에 4.5조원 공급 | https://www.fsc.go.kr/no010101/88160?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 정부는 최근 발생한 금융보안원의 침해사고와 관련하여 철저한 원인조사 및 재발방지 대책 마련을 지시하였습니다. | https://www.fsc.go.kr/no010101/88152?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 이억원 금융위원장,  글로벌 금융안정 공조 및 유럽 주요 금융당국과 협력 강화 나선다 | https://www.fsc.go.kr/no010101/88151?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 불법사금융 원스톱 지원,  이제 센터 방문 없이도 신청 가능합니다. | https://www.fsc.go.kr/no010101/88150?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
|  | 금융위원회 | 신진창 금융위원회 부위원장,  씨티그룹 국제부문 총 책임자 면담 | https://www.fsc.go.kr/no010101/88146?srchCtgry=&curPage=1&srchKey=&srchText=&srchBeginDt=&srchEndDt= |  |
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
|  | 정책브리핑(금융위원회) | 이억원 금융위원장, 글로벌 금융안정 공조와 한-유럽 금융협력 강화로  한국 금융의 지평 넓혀 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790306&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국세청) | 국세청, 세계에 내놓을 2026 우리 대표술 12종 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790164&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |

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

## collect:out_of_scope (209건)

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
|  | 정책브리핑(지식재산처) | 지식재산처, 인공지능(AI) 수술로봇 기업 찾아 특허 경쟁력 강화 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790326&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | '27년 상반기 변리사 실무수습 집합교육 참가자 모집 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790325&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산 통계정보, 인공지능(AI) 친화형 제공 방식으로 전환 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790324&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 지식재산처, 차세대 태양광 특허 현장소통 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790323&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(개인정보보호위원회) | "개인정보 보호법 인공지능 특례" 세부 기준 마련 … 개인정보 보호법 시행령 개정안 입법예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790321&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(법제처) | 국민 누구나 쉽고 편리하게 이용하는 '차세대 찾기 쉬운 생활법령정보' 개통 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790319&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 세계 한인 정치인들 알마티에 모여...동포 사회 권익 신장과 협력 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790314&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 세포기반 인공혈액부터 드론 수송까지... 수혈의학 미래 발전 방향 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790320&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(방송미디어통신위원회) | 2026년 제51차 위원회 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790317&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 제31차 유엔기후변화협약 당사국총회 폐막 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790322&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 은행 및 상호저축은행 분야 불공정 약관 시정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790305&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 바다 아래 잠든 천년의 기록 길어 올린 '한국 수중발굴' 50년 역사, 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790312&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 아라가야 왕성 「함안 가야리 유적」의 성벽 축조 기술과 생활공간 변화 양상 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790310&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청, '대한민국 정부혁신 박람회'에서 디지털콘텐츠 20여 편 전시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790308&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 예비문화유산 선정 기념 「우리 삶의 기록, 미래의 유산으로」 사진전 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790296&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부, 라트비아에서 재외국민보호를 위한 신속대응팀 모의훈련 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790302&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | [기품원] 제10회 국방품질경영상 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790301&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, '산림분야 정상화 과제' 추진 박차 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790294&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 「범죄피해자 보호주간」 운영, 범죄피해자 보호에 의지를 다지다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790304&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(방위사업청) | [국기연] 「2026 국방 실물 인공지능 토론회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790292&pageIndex=1&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 모두의 성장으로 대전환을 위해 전 부처 역량 결집 ｢양극화 대응 TF｣ 산업·기업반 1차 회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790291&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | "중소기업의 기술 융합·협업 성과 한자리에" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790295&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 굴·딸기 등 K-푸드 수출 유망 현장 찾아  민관 원팀으로 지원한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790290&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한국, 전기·전자 국제표준 리더십 이어간다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790289&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 권역별 성장엔진, 투자지원 액션플랜 만든다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790288&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 예비사회인 고3!  '내 노동권익은 내가 지킨다' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790286&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | "경찰청 최초로 정책 수립과정에 국민 숙의 절차 도입" 관계성범죄 관련 「경찰정책 국민참여단」 숙의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790303&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, 불공정조달행위 6개사 부당이득금 환수 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790285&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 2026년 11월 1일 ~ 11월 20일 수출입 현황 [잠정치] | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790280&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 카카오페이·토스·네이버페이에서도 '주민등록증 진위확인' 가능...  전자금융거래 안전성 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790284&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 겨울철 자연재난도 '풍수해·지진재해보험'으로 든든하게 대비하세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790282&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 소아청소년 만성콩팥병 환아의 건강한 성장을 위한 영양·식생활 가이드 발간(11.23.월) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790276&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 사람부터 환경까지 전 분야의 항생제 사용과 내성 현황을 한눈에(11.23.월) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790275&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "행정기관의 착오로 누락한 지장물 보상"… '손실보상 시정권고'로 국민의 재산권 지켜 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790274&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 금오산에 울려 퍼진 산불예방메시지 안동산림항공관리소 합동 캠페인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790273&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 한-카타르, 변화하는 에너지 환경에 대응해 협력 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790271&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 인공지능 학습을 위한 저작물 이용허락 표준계약서(안) 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790270&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | '스트레이 키즈' 필릭스, 한복의 새로운 물결을 일으키다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790269&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 식·의약 분야 특사경 수사역량 강화 직무교육 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790266&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부, 인공지능 반도체 업계 현안 점검...국제 협력·공급망 대응 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790264&pageIndex=2&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 식약처, 바이오의약품 인허가 지원 워크숍 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790265&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | K-컬쳐와 공공외교, 국민들과 함께하는 외교정책 강연 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790267&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부, 「대입 허위 원서접수 신고센터 」 설치 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790263&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(재정경제부) | 긴급 시장상황점검회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790262&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 해양수산부 장관, 실종 어선 '해광호' 선체 확인에 따른 실종자 구조 총력 지시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790277&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | K-ODA로 함께 여는 상생의 미래 '2026년 개발협력주간' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790261&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | "추위가 재해가 되기 전에" 겨울철 한랭질환 예방 집중점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790231&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 국가기술자격증 불법 대여, 정부 합동단속으로 뿌리 뽑는다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790230&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 기상 변동성 큰 올겨울, 농업 기상재해 선제 대응한다! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790228&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '우리흑돈' 가공·유통 산업화 확대 방안 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790226&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 제주 청년농업인과 영농 정착 위한 기술 지원 방향 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790224&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | '제13회 고구마의 날' 기념행사 경기도 여주서 열려 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790222&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국산 감귤·차 품종 확산, 제주 농업 경쟁력 높인다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790220&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | "현장에 답 있다"…농촌진흥청, 제주 지역 선도 농업인 간담회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790218&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 쫄깃함 살린 '버섯 기반 단백질 식품 소재' 시장 경쟁력 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790216&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 지역 농산물의 맛있는 변신! 농산물종합가공센터 우수 상품 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790214&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 젖소농장 한파 대비 점검·케토시스 관리 기술지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790212&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국립축산과학원–성운대학교, 국산 열풍건초 이용 확대 업무협약 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790210&pageIndex=3&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 제주 애플망고 품질 향상·재배 다양화 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790208&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 경남 함양 양파 모종 아주심기 상황 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790206&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 제주 한우농가 찾아 사료비 절감 기술 확산 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790204&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 국산 나물용 콩 생산 기반 확충한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790202&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 재배 쉽고 수발아 강한 '바로미4' 개발… 가루쌀 안정 생산 기반 확보 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790200&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 기후 위기 대응 '더위에 강한 뒤영벌' 계통 육성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790198&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 토마토갈색주름과실바이러스 피해 농가 손실보상 강화… 재정식 허용 기준 등 사후관리 방안 의결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790196&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 토마토갈색주름과실바이러스 확산 차단 총력…관계기관 합동 대응 강화 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790194&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 쌀 가공식품 산업 활성화 민관 협의회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790192&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 국산 트리티케일 확산 이끌 현장 전문가 양성 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790190&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 겨울철 돼지 건강, 사육 단계별 온도·물 공급부터 챙기세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790188&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, '제3회 RDA 인사이트 데이' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790185&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 우리 품종 '금강밀' 유전체 완전 해독으로  출수기 예측 "디지털 육종 성큼" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790183&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 아열대작물실증센터 공사 진행 상황·안전 관리 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790181&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 공공데이터 활용 "통통 튀는 친환경농업 연구 아이디어 찾는다" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790179&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 겨울철 축사, 환기는 유지하고 보온은 꼼꼼하게 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790177&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 운영자 역량 강화로 '농촌관광' 활성화 기반 다진다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790175&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 토마토갈색주름과실바이러스 위기 단계 '경계' 격상…전방위적 차단 방역 총력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790173&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 국립식량과학원, 현장 의견에 답하고 민관 협력 강화한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790171&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 닭 몸무게·달걀 무게 차이, 유전정보에서 단서 찾았다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790169&pageIndex=4&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 마늘·양파 안전한 겨울나기, 덮개 씌우고 물길 정비해야 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790167&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농촌진흥청) | 농촌진흥청, 겨울철 농업재해 대책 마련 "피해 예방·안전 제고" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790165&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 대체인력 사고도 보장한다 발달장애인지원사업 종합공제 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790163&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2025년 대리점 분야 공정거래협약 이행평가 결과 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790162&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | 중고차 광고에 수수료까지 표시 … 실제 구매비용 한눈에 확인 「자동차관리법」 하위법령 개정안 입법예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790161&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 올해 일등어촌에 '경기 화성 궁평리마을' 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790160&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 민간·공공 협력으로 동유럽 물류거점 확보에 박차를 가한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790159&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | 김장철을 맞아 천일염과 젓갈에 대한 원산지 표시를 더 꼼꼼하게 점검한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790158&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 김장독에서 세계인의 식탁으로, 뉴욕서 '글로벌 김치 비전' 선포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790299&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 민간 소독시설 활용 확대로 축산차량 방역체계 현장 중심으로 개선 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790157&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 케이(K)-철도, 95조 원 베트남 고속철도 사업 진출 첫발 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790156&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 105병상 규모 대구보훈병원 서관동 증축 공사 23일 착공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790155&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 영유아보육 분야 규제 개선을 위한 「영유아보육법 시행규칙 」 개정 공포 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790154&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 2026 개발협력주간 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790268&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(성평등가족부) | 여성청소년 생리용품 이용권, 연말까지 사용하세요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790278&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [차관동정] 정의경 제2차관, "안전을 최우선으로 탈선 현장 복구 및 이용객 불편 최소화할 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790153&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 우리 사회의 인공지능을 생각하고 토론하는 축제의 장, ｢AI 인사이트 페스티벌 시상식｣ 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790152&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(해양수산부) | (동정) 해광호 실종 사고, 현장 상황을 점검하고 실종자 가족 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790300&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 경부선 소정리역 화물열차 탈선 사고 대응에 만전을 기하고 있습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790144&pageIndex=5&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 미래의 피지컬 AI 전문가 발굴!  「2026 청소년 로보틱스 챌린지」 결선 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790143&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고)노동부 장관, 국가자격시험장 현장 살핀다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790142&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교부 공관장 인사 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790141&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 외교관과 함께 이야기하는 개발협력, 청년의 시선으로 미래를 그리다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790139&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 배경훈 부총리 겸 과기정통부 장관, 아랍에미리트 건국 55주년 국경일 기념행사 참석 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790138&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 행정안전부 장관, 도로살얼음 취약구간 안전관리 실태 점검 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790137&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 제12차 한-일 국장급 중동정책협의회 개최 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790135&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 한성숙 국무총리 주재 수능 부정행위 대응TF 1차 회의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790134&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 사회대개혁위원회, 대한민국 대전환 제3차 국민토론회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790133&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방부, 제5회 국방 AI 경진대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790131&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부 장관, 현장·전문가와 함께  농촌 사회연대경제 활성화를 위한 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790125&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | K-이니셔티브 해외 확산을 위한 제2차 관계부처 회의 개최(11.20.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790126&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 민주유공자법 국회 본회의 통과, 보훈부 후속조치 만전 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790132&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 여성폭력 근절을 위해 3부(입법부, 사법부, 행정부) 및 여성폭력 피해자 지원단체가 힘을 모았습니다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790124&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 통일부 장관, 유엔군사령관과 판문점 방문 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790123&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 민간 AI 솔루션 기업 A사 개인정보 유출...유출 대상에 2차 모두의 창업 참가자 818명 포함 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790122&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 군인 헌법교육 강화 위한 국방부-법제처 업무협약 체결 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790130&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금개발청, 크루즈·마이스(MICE) 전문가 초청 자문회의 및 현장 팸투어 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790116&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국방부) | 국방홍보원-매일경제, 국방·안보 협력 위해 맞손 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790129&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(새만금개발청) | 새만금개발청, 크루즈·마이스(MICE) 전문가 초청 자문회의 및 현장 팸투어 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790113&pageIndex=6&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 교육부, 대학별고사 관련 부정행위 대응방안 점검 및 긴급 대응체계 구축 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790115&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기획예산처) | 중장기전략위원회 미래사회전략반, 거버넌스개혁반 분과회의 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790111&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 청년의 아이디어로 지역에 새 활력을, '청년희망터' 5기 성과 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790110&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] '27년 부동산 공시가격 시세반영률은 전년 수준 유지 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790108&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(중소벤처기업부) | 중기부, 공공구매 유공 39점 포상… 중소기업 공공조달시장 진출 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790098&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(외교부) | 박윤주 제1차관, 우루과이 외교차관 면담(11.20.) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790097&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림신품종 출원에서 등록까지 한눈에!! | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790096&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 건설산업을 빚낸 기능인 38명 영예의 수상…  제17회 건설기능인의 날 기념식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790092&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 근로복지공단, 아이의 성장과 상생을 담은 직장어린이집 우수사례 33건 시상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790091&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 2026 지속가능발전 숏폼 영상 공모전 시상식 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790093&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(소방청) | 소방청, 수능 당일 전국에서 116건 소방활동 펼쳐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790090&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [참고] 테슬라 FSD 특례 신청, 자료 보완 필요 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790094&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | (참고자료)산업부·경제 6단체, 수출 1조 달러 넘어 '질적 성장' 도약 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790088&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 통상교섭본부장, 우루과이 외교부 차관 면담 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790087&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 산림보호분야 제도개선 국민공모제 6건 시상 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790086&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(관세청) | 숫자로 풀어 보는 수출 1조 달러 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790083&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(통일부) | 통일부 장관, 미셸 박 스틸 주한 미국대사 접견 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790084&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 구미국유림관리소, 겨울철 한랭질환·안전사고 예방 '총력' | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790081&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 위기의 순간, 한 번 더 생각할 기회 제공 「2026년 자살수단 차단사업 참여기관 간담회」 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790082&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정은경 장관, 제주 맞춤형 의료지원체계 구축과 도내 의료격차 해소방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790078&pageIndex=7&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 산림청, 전국 산지관리 담당자 워크숍 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790077&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 우리 사회 따뜻한 혁신기업 12개사, 「올해의 사회적기업」 첫 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790079&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 국내발생 추정 콜레라 환자 10년 만에 발생, 예방수칙 준수 당부(11.20.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790073&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 북부지방산림청, 산림교육과 산림치유를 통한 대국민 서비스 제공 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790075&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 청년 시선으로 찾은 정신건강 해법 공유, 영마인드 링크LINK 3기 7개월간 활동 마무리 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790071&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 기초연구의 오늘과 미래를 잇는  ｢대한민국 기초연구 커넥트｣ 행사 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790067&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 국민과 세계인이 함께 맛보고 버무린  '제7회 김치의 날', 성황리 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790107&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 에볼라바이러스병 해외유입 대비, 관계기관 합동 훈련 실시(11.20.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790069&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국토교통부) | [장관동정] 홍지선 장관, "겨울철 국민 안전 최우선… 비상대응체계 확립" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790070&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년 공정거래위원회-한국유통법학회 공동 학술대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790066&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 정은경 장관, 제주서 일차의료 현장 목소리 청취… "지역 여건 반영한 실효성 있는 사업 만들 것" | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790065&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 현장 대응 역량을 갖춘 준비된 경찰, 국민 곁으로 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790064&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(교육부) | MS·Google·AWS와 손잡고 교사의 인공지능(AI)·융합교육 역량을 키운다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790063&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 과기정통부-기후부,  인공지능 데이터센터 신속 구축을 위한 전력계통영향평가 제도 개선 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790068&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가데이터처) | 2026년 고추, 참깨, 고랭지감자 생산량조사 결과 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790062&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 과기정통부-기후부, AI 데이터센터 신속 구축을 위한 전력계통영향평가 제도 개선 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790061&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(우주항공청) | 한-폴란드, 우주정책·기술 공유하고 산업협력 기회 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790060&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 특허, 기술을 넘어 제품으로! 돈이 되는 특허전략 한자리에 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790059&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(지식재산처) | 돈 되는 특허, '소통형 특허심사'로 민관이 함께한다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790058&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(교육부) | 스마트기기 등 전자기기 관련 부정행위 적발 현황 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790057&pageIndex=8&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 서울 서대문구 일대 중·소 건설현장 일제 패트롤 점검, 한파·추락 등 기본 안전조치 집중 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790056&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | (참고) 모두의 성장으로 대전환을 위해 전 부처 역량 결집 - 양극화 대응 TF 「노동시장 이중구조 개선반」 1차 회의 개최 - | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790055&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(고용노동부) | 딱딱한 정책은 이제 그만,  친근하게 만나는 청년고용정책 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790054&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기상청) | 기상청, 기후변화에 관한 정부 간 협의체(IPCC) 7차 전지구 기후변화시나리오 첫 산출 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790053&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 인플루엔자 입원·중증환자 급증! 신속한 예방접종 및 예방수칙 준수 당부(11.20.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790051&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국무조정실) | [보도자료] 조세심판원 '26년 3분기 주요 심판결정 공개 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790050&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(경찰청) | 경찰청, 어린이 보호구역 현장 캠페인과 함께 어린이 교통안전대책 강화 추진 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790049&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 대릉원 이전 신라의 지배층 무덤, 그 실체를 찾다. | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790046&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가유산청) | 국가유산청, 민관협력으로 사찰·민속마을에 난연복 530벌 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790044&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(보건복지부) | 보건복지부, 하반기 헌혈 이어가기 행사 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790037&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 보훈부 포스코， 상이 국가유공자 등 28명에게 첨단 보조기구 전달 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790029&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국가보훈부) | 2026년 보훈문화 체험활동 우수 프로그램 경진대회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790028&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 지방세제 혁신 아이디어 발굴·확산을 위한 '2026년 지방세 발전 포럼' 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790043&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 지역자율방재단,  겨울철 대비 역량 강화 교육 실시 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790041&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 민생 안정과 지속 가능한 지방재정, 지방교부세가 발판을 마련하겠습니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790039&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(농림축산식품부) | 농식품부, 미(美) CIA 방문해 한식 교육협력 및 발전 방안 논의 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790112&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(공정거래위원회) | 2026년 중소기업 간 하도급거래 모범업체 선정 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790027&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 제조설비 데이터 수집 활용가이드,  국가표준화(KS)로 제조AX 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790036&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 중앙·지방 힘 모아 지역 성장엔진에 외국인투자유치 집중 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790035&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 한-베, 상호 호혜적이고 지속가능한 미래 성장 방안을 논의하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790034&pageIndex=9&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 수출통제 시대, 기업의  자율준수(CP)가 새로운 경쟁력 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790033&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산업통상부) | 중견기업계, 혁신과 도전으로산업경쟁력 제고에 기여 다짐 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790032&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(원자력안전위원회) | 제2026-18회 원자력안전위원회 개최 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790022&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | 시민참여형 서포터즈 '홍릉숲지킴이' 발대식 개최 - 국립산림과학원, 시민 참여로 홍릉숲 가치 확산 및 연구시험림 보호 앞장 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790021&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(행정안전부) | 대한민국, 국제연합(UN) 전자정부평가 12년 만에 세계 1위 탈환 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790024&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 조달청, AI 시대 공공조달의 미래전략 모색 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790019&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(조달청) | 시설공사 주간('26.11.23.~'26.11.27.)입찰 동향 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790018&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(산림청) | "현장 목소리로 산림 규제 푼다" 울진국유림관리소, 모니터링단 운영 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790016&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(법무부) | 예비 사회초년생의 안전한 사회진출을 위한 생활밀착형 법교육 확대 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790013&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 인공지능 데이터센터 신속 구축을 위한 「인공지능 데이터센터 특별법」 하위법령 제정안 입법예고 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790072&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(과학기술정보통신부) | 2026년 들어 가장 큰 슈퍼문, '좀생이별'과 만남 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790140&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | (참고) 국제에너지기구(IEA)「세계에너지전망 2026」 발표 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790017&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(질병관리청) | 한·미, 감염병 위협 공동 대응을 위한 협력 논의(11.20.금) | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790012&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(국민권익위원회) | "토론을 통해 실효성 있는 행정심판을"…  국민권익위, 한국행정법학회와 함께하다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790011&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | [보도참고] 마약류 진통제는 통증조절이 되지 않는 심한 통증에만 사용해야 합니다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790010&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(문화체육관광부) | 옥스퍼드대에 '케이-컬처' 연구 거점 마련, 세계와 함께 본격적으로 '케이-컬처' 미래 연구 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790007&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 식약처, 겨울철 노로바이러스 식중독 주의 당부 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790009&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(식품의약품안전처) | 한-멕시코 정부, 수입 수산물의 안전 확보를 위해 맞손 잡다 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790008&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(기후에너지환경부) | 경북 산불 피해 지역 숲속 인공둥지에서 하늘다람쥐 번식 확인 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790006&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |
|  | 정책브리핑(재외동포청) | 재외동포청, 한상 연결망 활용해 국내 AI 스타트업 미국시장 진출 지원 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156790026&pageIndex=10&repCodeType=&repCode=&startDate=2025-11-23&endDate=2026-11-23&srchWord=&period= |  |

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
| kifrs | 조세일보 | 감리지적사례-보안솔루션업: 실질 없는 중간 끼워넣기 거래로 상품매출... | http://www.joseilbo.com/news/news_read.php?uid=574281&class=18&grp= |  |
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
| tax | 한국세정신문 | 2026년 세제개편안, 세무사들의 대비책은? - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE5MY3F0V29rRWF6TlBaNk5FeU5jTExvYmJOaVc2cV80MGlqX1RPdkMzbktjeTZMTzdhM3BIMUl5SnVkQUZ6MUh0ZVZNaDZBNmZhNlpsOXNOeFQ3S3RrOENJMjZtVjQ?oc=5 |  |
| tax | lawtimes.co.kr | 2026년 정부 세제개편안 – 가업승계 관련 개정사항 - 법률신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTFBBNGJIZVlYa0tTNmc1NF9hYUZBVzVIcFRDc21aV0NUOTdtbmF1Ukw0VDQxNUY2T3k3b0ZQbTMwNGROTGpSTFdrTHZpT0JmTGR6NS1IQmQtYzF1cEpLLUdEY2h2WWFmdzk3UmJKX2930gFyQVVfeXFMTzNRUzY1VTZGZ091OHFLRzluTTJVQ2RLQmZENTVQNl9uZlJpdk5abXI0a2VmRlc1d05sUUduZ2d2akdfbTUwUUNCWW5hdGYwUnd6YmtGZGpVLXcwZGsydGhjMzlQdDlkS3pLT3kzeHhNZnhR?oc=5 |  |
| tax | news.koreanbar.or.kr | [국회단상] 세법개정안과 ‘거주’의 정의 - 법조신문 | https://news.google.com/rss/articles/CBMib0FVX3lxTFBYUmhtbTZ0UFVnckgyalZVakZIbTR6b0RoY0ZkckN0N2RvYzZYVDU4cUVpOGtKT1loUXB1aXhaSUFXMnZmeGw0YjQzbTJpR1NZUXRKVmlsQUl3N1dyemVwckk0eDdMQmV5ZmR6dDdTaw?oc=5 |  |
| tax | sejungilbo.com | 국회예산정책처, 오는 9일 `26 세법개정안 토론회 개최 - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE5RRXJZOHc1RzlVakJaMnltS2VRVExTb3l2UHFpeGctSGR2SFJXdFBrWHY1dzAtVW1ob0doeDFBRmo1QWFTRDFwajU4YU1PcVctb1V6YzZNVV9wY2pBYi1VOXROWFRna1UxMllfTQ?oc=5 |  |
| tax | busan.com | 국세청, 재경부에 건의한 세법개정안, 반영률 18.7% 그쳐 - 부산일보 | https://news.google.com/rss/articles/CBMidEFVX3lxTFBKVUtHdkhVdjJxdHpONlM0VVhvQ0dDRktsMWh3UVdOMk0xbG9ZZjVpUUhYdk9LM0M3V3ZsZmtkV000Zm1XTEtybzJGem12bXUyTkVaQ3h4UGU1SXhGMWxiODl1N18zWmx1TWotSUpFWXppYXNK?oc=5 |  |
| tax | ignnews.kr | 고동진 의원, 부동산 세제개편안에 강남구민 의견 반영 촉구 - 강남포스트 | https://news.google.com/rss/articles/CBMiZkFVX3lxTFB2Q0lDVUNRVF9IQUpkdkxleFpFU3pJX1RkcDBLdnhLbXNITDVvdjVkN29JMGdCM0FRTmg2NUNKN240MUFGMFF1Y2plcWpyZThkV1NRTXlVbzhNNlVnUmRTRmxTVUI4Zw?oc=5 |  |
| tax | pressian.com | 익산참여연대 "정부 지방교부세법 개정안 철회 촉구…지방과 충분히 협의해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTE0tTFE0Nzd0b0stb1gyNDFJU3hiMllsR2xxdl9KYV9LWi1DWGtLYS1waHo5U0dZbzhLY2tzdU1fblp6RnQ0TTZndGFzOHlxNXFpcjBMSUs0Yl9UN0ZHWDA1bFVxYWlxZmtXdVEw?oc=5 |  |
| tax | jejusori.net | 미래기금 이어 세제개편...제주 세입 낙수효과 혼돈 - 제주의소리 | https://news.google.com/rss/articles/CBMia0FVX3lxTE9sMjYzMlVwSzJRMFhCSjFaZGxIZlp5cDFYVjNrbE9UVmdCQ1BiQlV3eDhzcEdyWTh3S3FqenhiaWNGRWctYTJwb0lmWkcxQU0xd3VQUFFpT2pOZUkycDRPMnlVWXZ2aW5BMmdZ?oc=5 |  |
| tax | newsnjoy.or.kr | "법 지키고 싶은데 방법 모르겠다"…개정 세법 앞 해외 선교 현장 고민들 - 뉴스앤조이 | https://news.google.com/rss/articles/CBMibkFVX3lxTE9hU3p2LTdMRW9YcTVfbkxPV1BnUlJORUt6V0ZySFFtT1dJUXBZbGFwbkNCVGJIbGNMc2NvX2h1b3VTYzlCcWFMamo5Rk9iNFRGQ2VvSThsS05MSFktV05ma0U1LU5LOVFRSWVMUlp3?oc=5 |  |
| tax | mediagn.co.kr | 강민국 의원, “세제개편안 찬성 3%대...국회서 전면 재검토” - 경남미디어 | https://news.google.com/rss/articles/CBMia0FVX3lxTE5VeWVKWU9nRnVMVkhQU0ZYdzJNQm4xbERsZkoyYUtPZmVrcV9OWnFobUpYaTZiTWRHR2phd0VVTjJ3dm1GSzFjQWFseks5UWs4bWlDRlFDbU1FTEp1Z2F5dlJmTU04bGRNYkgw?oc=5 |  |
| tax | yna.co.kr | "국세청 세법 개정 건의에 재경부 80% 퇴짜…재탕 174건"(종합) - 연합뉴스 | https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6UUFHY0dqdE41eEpQMml4TE1fRDI3aVcwMG5IMTlmZGxyWTJrQUdPVURyLWFkRHo2WXQzUjFaZzZYYnFLS0I4UHZRS1VwVDQyeXUxUmRlYk1sQzDSAWBBVV95cUxOeDlrTWJMLVFFUHdRdGFKSnZYenV2UWl2UnZxTUtyamE4YUNfSjVfSzNHY2U4eEQ1X096RGc2aE9BN3dMUGlnaE56N1I2c2c0bkZkVTR0a1lJR1pUQWxUSGk?oc=5 |  |
| tax | nodongilbo.com | 국회예산정책처, 2026년 세법개정안 토론회 개최 - 노동일보 | https://news.google.com/rss/articles/CBMibkFVX3lxTE5Sc2Zjd0pLdFN1WVVVVUtkSUMwRXgyOGNUd3hsU0tsT1ZzY181TmlFb2hGSFRNekNBYmVNYWQ3NVROZUtUbG11X09WMW40cFJCRXpzTmszR0dVMEFNQnB2UXVQRzFISUZqalNRY3p3?oc=5 |  |
| tax | 한국세정신문 | 한국조세법학회·국회입법조사처, 30일 '세법개정안 쟁점' 추계학술대회 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1yMHdHRnYwQWhEN0s5V2ZxNG02aFloamNqalgtc19vdFNwQjI5UldRTXhtTzhyeDB1ZVNiU0FObndnM1p4WFJtWV9scnIyRHJwa05iWHF0eUtuUzdROTllOVNuMWE?oc=5 |  |
| tax | sejungilbo.com | [토론회] “체감 경기 회복 vs 과세 예측가능성”…`26 세제개편 쟁점은? - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE14eTJsdUFhend0enBURENHX2dBT0pFdS1mcU9pcGo3UllMbXZsU2x3OG1jb183aFBKZFJQb3ZGWlgxQUVqM1YwZDNRV1JlX0F6SWdiVHdyTzRQRXNnY0FqczZNZ1Ixam80UGFMZw?oc=5 |  |
| tax | pressian.com | 조국, 이번엔 세제개편안 비판…"표 준 국민의 이익에 충실해야" - 프레시안 | https://news.google.com/rss/articles/CBMia0FVX3lxTFBxYXRWTTMwSGViTHdRYWZleHpDQ3IzcWROZ2dCbjlTZVlLbFppdUZmajF1V3hjemdrcEh5aHlxRThOM0djczF2bWdpTDQ1NjF6bG02ODRSSEFKaTlGbUt3SWxIZWx0X3NJU3lB?oc=5 |  |
| tax | 한국세정신문 | 대통령 업무보고까지 했으나…국세청 '세무플랫폼 감독규정 명문화' 불발 - 한국세정신문 | https://news.google.com/rss/articles/CBMiZEFVX3lxTE1WUmhWcEZCbHdGN2h1RTR4aHdsaFV0bTVjWDVfWHdGVVdKREpvTnAyVUM1djVfYTdLbFhRWE1tV2Rwd25tRzZYQWNpZF8xU2lyYmtJVHFaRUNscWJobHBTQ3VRdWw?oc=5 |  |
| tax | newsis.com | 종부세 부담 완화에도 세수효과 '3.4조' 그대로…이유는? - 뉴시스 | https://news.google.com/rss/articles/CBMiYEFVX3lxTE1nQ3VQRWc1eTQtZTBhUHM5MldmT3ZfWDhOcDV5QW9mMzJUNGdXSkdVT0hJdExHbjBRZzlVMmhZSHdXRFBRZ2ZGU2V3U05wcXBjN0x0TTVxNHJxUEJaOXNrQtIBeEFVX3lxTFBQd2xfbHZ1S1ZwWkJscUpsQThHWWdtRVVmYk4ybGEzaHc5LVhhWldIZVdPYWRxTVdSNFA4UFVnNEc1WFdyb1YybFBYelNXUnNJcDI0NlNQdWpHRUJJbVRPSjNpMUdhVjZ1a19UcVFzSXFtR2M1R1BrRw?oc=5 |  |
| tax | mbnmoney.mbn.co.kr | 국세청 세법 개정건의 10건 중 8건 반영 못 해…'실적 쌓기' 지적 - 매일경제TV | https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wYjVGQjdSbkZCY2RpRjFvUjNyX0tpSFFDazNZVnFkcHdXY2hCd1Z5MUJKbmdNVG56NGdRc2trbnQzYXVoSUhGM25DRy05anRvNnhPYnlOYWdDSjdKOV9wSFgtbjgyaFBo?oc=5 |  |
| tax | onseoul.net | 고동진 의원, 이재명 정부의 부동산 세제개편안 관련 강남구민 의견 국회에 전달 - 서울자치신문 | https://news.google.com/rss/articles/CBMiaEFVX3lxTE1BWW9URzFQSURrQ3RaRGVXWE1XeUM3LXhqTXZVNDB3WHRkaUxNMURkNnNHczh5ei1yU0VNU2FHYjNwQWRjN2pEQnV1Q3dDWll4Vjh4czlhLU1ZZndIdXpfQTNaTkU1ZXdH?oc=5 |  |
| tax | newspim.com | [뉴스분석] 부동산 세제개편안 정부안 의결…與 내부서 불거지는 수정·보완 목소리 - 뉴스핌 | https://news.google.com/rss/articles/CBMiXEFVX3lxTFBaMU94ZFRIbWRacklQenVyOHN0dUxYc3AzM0ZveTR5a3Fvd0NsaW9jcVNNRGN3emRCcUFCQWJsa0J5TEFNWnd3bEc1cExsRlNSVDJCMWNNWEkxOWQz?oc=5 |  |
| tax | sejungilbo.com | 국민의힘·개혁신당 수도권 의원 모임 “정부 세법 개정안, 국민 이사 발목 잡아…4대 원칙·8대 수정 요구” - 세정일보 | https://news.google.com/rss/articles/CBMibEFVX3lxTE1GWWZObzhTMTA5b2lQbjdNQkFZNTQ1cmlDeVVWbEZHWVk3Y3JjNmk2Nl9MbTFyOG5UcTdNYm9pd3V2TWQ5TklVRVhRTzBhaVZ0b2J4RTl5TGczWVJJcUwxQWEtSFRvcVNCaXBVUg?oc=5 |  |
| tax | jeonmae.co.kr | 고동진 국회의원, 정부 부동산 세제개편안 제도적 보완 촉구 - 전국매일신문 | https://news.google.com/rss/articles/CBMibkFVX3lxTE95Z0FvR3Q1TDhVMEJSeUp0RjQ5OHpJZWMzOVBkRG50bm11OGktRVNIMXBGTlRmc0FjMHFiUkFYX21OWUtDSy0wcTktT21Vd0k3MVlLVXhmaHhiWkxPbzkwemdXZG1JVS1DTTBaSmFB?oc=5 |  |
| tax | sportsseoul.com | 국회예산정책처, ‘2026년 세법개정안 토론회’ 성료 - 스포츠서울 | https://news.google.com/rss/articles/CBMiWEFVX3lxTFAxY2luMmRVY3NUUEZNdkVZQzVPUURuSXZYRW1uU3EtLTFRcXRDUGp6WTgxX0o2NzNaamducGdHbENLYlY4bU1iOUZHNThXUnNaMGMtNHU1S2U?oc=5 |  |
| tax | vietnam.vn | 국회는 2027년부터 시행되는 3개 세법 개정안을 통과시켰습니다. - Vietnam.vn | https://news.google.com/rss/articles/CBMilgFBVV95cUxQTTYwemJGU2FaVl82ekJuZ3ZEa1ZSRXY5Vmx0VS1nbXVkZGJ1M0psbjdaNTdUZnpKQ1o5dUxycV9sTjdJRHA2bzQybVBKQXlMT1RGbmMyYXFLbHc3cGRLQ2Jja3lnUnpneFVGUUNSZ19zMEZuRXBUemJISkdJejRoQzhIUTI5YzFsUDRBdUJLeTlyRFJQNVE?oc=5 |  |
| tax | 매일경제 | 2026년 세법개정안 토론회 - 매일경제 | https://news.google.com/rss/articles/CBMiRkFVX3lxTE5GRjhGNk5UVWxaUTVnVFVlN0RUZTc1NmtwN2dnTF9qZm1wTExqbXFmWkc2cndORUs4S0hzLS0tWlRId0xGLWc?oc=5 |  |
| tax | dream.kotra.or.kr | 모로코, 2027년 재정법안 발표, 수입 선납금 도입 등 세제 개편 추진 | http://dream.kotra.or.kr/kotranews/cms/news/actionKotraBoardDetail.do?SITE_NO=3&MENU_ID=80&CONTENTS_NO=2&bbsGbn=242&bbsSn=242&pNttSn=245194 |  |
| tax | newsnjoy.or.kr | "법 지키고 싶은데 방법 모르겠다"…개정 세법 앞 해외 선교 현장 고민... | https://www.newsnjoy.or.kr/news/articleView.html?idxno=400920 |  |
| tax | goodnews1.com | 개정세법 시행 9개월째…해외 선교비 집행 여전히 난항 | https://www.goodnews1.com/news/articleView.html?idxno=466437 |  |
| tax | 조세일보 | 세법개정, 소득재분배 효과…부동산은 복잡 [토론회] | http://www.joseilbo.com/news/news_read.php?uid=579256&class=7&grp= |  |
| tax | 서울경제 | 국힘·개혁신당 “종부세 실거주 차별 폐지”…세제개편 8대 수정 요구 | https://www.sedaily.com/article/20117639?ref=naver |  |
| tax | newswhoplus.com | 내년 공동주택 공시가격 현실화율 69% 동결…집값·세제개편發 보유세 ... | https://www.newswhoplus.com/news/articleView.html?idxno=75043 |  |
| tax | ajunews.com | 미래기금·세제개편·인사청문회…국회 곳곳에 '지뢰밭' | https://www.ajunews.com/view/20261122182939350 |  |
| tax | newsis.com | "보유세는 14억까지, 양도세는 그대로"… 세무사가 내다본 세제개편 전... | https://www.newsis.com/view/NISX20261122_0003878172 |  |
| tax | 조세일보 | 채권최고액, 순자산가액 부채로 볼 수 있을까 [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575604&class=7&grp= |  |
| tax | 조세일보 | 父 먼저 살던 임대주택에 자녀 전입…특례 기간은? [국세 유권해석] | http://www.joseilbo.com/news/news_read.php?uid=575258&class=7&grp= |  |
| tax | tfmedia.co.kr | [신간] 정종채 변호사, 26년 조세현장 경험 담은 《조세법 대계》 펴내 | https://www.tfmedia.co.kr/news/article.html?no=206845 |  |

