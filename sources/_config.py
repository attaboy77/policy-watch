# -*- coding: utf-8 -*-
"""단일 진실 공급원(Single Source of Truth).

카테고리별 키워드, 노이즈 키워드, 출처 신뢰도 등 모든 수집 정책값은
이 파일에서만 정의한다. 다른 모듈에 키워드 문자열을 하드코딩하지 말 것.
"""

CATEGORIES = {
    "kifrs": {
        "label": "K-IFRS", "team": "회계팀", "color": "#1e3a8a",
        "required": ["K-IFRS", "한국채택국제회계기준", "회계기준원", "금융위원회", "회계감리"],
        "combine":  ["개정", "제정", "공표", "MPM", "경영진성과측정치",
                     "기준서", "주석 공시", "회계처리 지침", "감리 지적사례"],
        # 네이버 API는 (A OR B) AND (C OR D) 구문을 지원하지 않음 → 단순 질의를 나열
        "naver_queries": ["K-IFRS 개정", "회계기준 개정", "회계기준원 공표",
                          "회계감리 지적사례", "회계처리 지침"],
    },
    "tax": {
        "label": "세법", "team": "세무팀", "color": "#047857",
        "required": ["세법", "세제개편", "국세청", "유권해석", "기획재정부"],
        "combine":  ["개정안", "시행령 개정", "조세특례제한법", "부가가치세법",
                     "법인세법", "예규", "판례", "조세심판원", "세무조사"],
        "naver_queries": ["법인세법 개정", "부가가치세법 개정", "세제개편안",
                          "국세청 유권해석", "조세심판원 결정"],
    },
    "icfr": {
        "label": "내부회계", "team": "내부회계관리팀", "color": "#b45309",
        "required": ["내부회계관리제도", "내부통제", "외감법"],
        "combine":  ["감사 전환", "모범규준", "취약점", "외감법 개정",
                     "연결 내부회계", "평가 가이드라인", "내부통제 미비점"],
        "naver_queries": ["내부회계관리제도", "연결 내부회계", "외감법 개정",
                          "내부회계 모범규준"],
    },
    "esg": {
        "label": "ESG", "team": "ESG팀", "color": "#0e7490",
        "required": ["ESG 공시", "지속가능경영", "ISSB", "KSSB", "GRI"],
        "combine":  ["의무화", "공시기준", "로드맵", "스코프3", "Scope 3",
                     "공급망 실사", "글로벌 스탠다드", "가이드라인"],
        "naver_queries": ["ESG 공시 의무화", "KSSB 공시기준", "ISSB 기준",
                          "지속가능성 공시", "공급망 실사"],
    },
}

NOISE_KEYWORDS = [
    "테마주", "수혜주", "주가", "급등", "상한가", "매수 리포트", "특징주",
    "개미", "재테크", "비트코인", "투자 유망", "증시 일정", "목표주가", "상승률",
]

TRUST_TIERS = [
    (1, 100, {
        "kasb.or.kr": "한국회계기준원", "fsc.go.kr": "금융위원회",
        "law.go.kr": "국가법령정보센터", "nts.go.kr": "국세청",
        "moef.go.kr": "기획재정부", "fss.or.kr": "금융감독원",
        "kicpa.or.kr": "한국공인회계사회",
    }),
    (2, 80, {
        "intn.co.kr": "일간NTN", "taxtimes.co.kr": "한국세정신문",
        "joseilbo.com": "조세일보", "impacton.net": "임팩트온",
        "esgeconomy.com": "ESG경제", "cpanews.co.kr": "CPA뉴스",
    }),
    (3, 70, {
        "samil.com": "삼일회계법인", "pwc.com": "PwC",
        "kr.kpmg.com": "삼정KPMG", "kpmg.com": "KPMG",
        "samjong.co.kr": "삼정KPMG", "ey.com": "EY한영",
        "deloitte.com": "딜로이트", "deloitte.kr": "딜로이트 안진",
        "anjin.co.kr": "딜로이트 안진",
    }),
    (4, 50, {
        "mk.co.kr": "매일경제", "hankyung.com": "한국경제",
        "sedaily.com": "서울경제", "edaily.co.kr": "이데일리",
        "fnnews.com": "파이낸셜뉴스", "mt.co.kr": "머니투데이",
    }),
]
DEFAULT_TIER, DEFAULT_TRUST = 5, 20

COLLECT_WINDOW_DAYS = 90     # 수집 기간
MAX_ITEMS_PER_CATEGORY = 60  # 카테고리당 상한
