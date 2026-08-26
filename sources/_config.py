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
        # "세무조사"는 여기 없다 — 단독 매칭 시 검찰 수사·압수수색 기사를 끌어오는 게
        # 확인돼(SPEC-ADDENDUM-3.md §5-2) TAX_INVESTIGATION_COMBO로 따로 뺐다.
        "combine":  ["개정안", "시행령 개정", "조세특례제한법", "부가가치세법",
                     "법인세법", "예규", "판례", "조세심판원"],
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
        "moef.go.kr": "기획재정부", "mofe.go.kr": "기획재정부",  # moef.go.kr이 301로 리다이렉트되는 실제 도메인(SOURCE_PROBE.md D1)
        "fss.or.kr": "금융감독원", "kicpa.or.kr": "한국공인회계사회",
        "k-icfr.org": "내부회계관리제도운영위원회",
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

# ── 계층별 상한 (SPEC-ADDENDUM.md §1) ───────────────────────────────────────
# L1(공식 원문)/L2(공식 보도자료)는 무조건 노출·노이즈 필터 면제·상한 미적용.
# L3(뉴스)만 상한을 적용한다 — 기존 MAX_ITEMS_PER_CATEGORY(60)를 대체.
MAX_NEWS_PER_CATEGORY = 15      # L3 카테고리당 상한(기존 60 → 15)
MAX_TIER4_PER_CATEGORY = 5      # L3 중 tier4(종합 경제지)는 카테고리당 최대 5건
MAX_OFFICIAL_PER_CATEGORY = None  # L1/L2는 상한 없음(그대로 전량 노출)

# ── 문서 종류 판정 (SPEC-ADDENDUM-2.md §2-1, §4) ───────────────────────────
# 앞쪽 규칙이 우선한다(순서 중요). doc_type_of()가 이 순서대로 제목을 검사한다.
DOC_TYPE_RULES = [
    ("공개초안",      ["공개초안", "공개 초안", "개정안", "제정안", "입법예고", "(안)", "의견조회", "의견수렴"]),
    ("검토의견",      ["검토의견", "의견서", "의견수렴 결과", "코멘트"]),
    ("적용지침",      ["적용지침", "시행지침", "평가·보고 지침", "평가 및 보고", "적용 가이드", "가이드라인"]),
    ("모범규준",      ["모범규준", "설계·운영", "설계 및 운영"]),
    ("감사·검토기준", ["감사기준", "검토기준", "감사인", "검토·감사"]),
    ("질의회신",      ["질의회신", "질의 회신", "유권해석", "예규", "서면질의", "질의응답"]),
    ("FAQ",          ["FAQ", "자주 묻는", "Q&A"]),
    ("예시서식",      ["예시", "서식", "템플릿", "양식", "샘플"]),
    ("로드맵·일정",   ["로드맵", "도입 일정", "적용 일정", "단계별 적용", "시행 일정"]),
    ("해설·교육자료", ["해설", "교육", "설명회", "안내서", "핸드북", "실무"]),
    ("결정례·판례",   ["결정례", "판례", "심판례", "조세심판"]),
    ("제·개정",       ["제정", "개정", "공표", "의결", "확정"]),
    ("보도자료",      ["보도자료", "보도참고", "발표"]),
]

# ── 세법 카테고리 노이즈 보강 (SPEC-ADDENDUM.md §5, L3에만 적용) ────────────
INCIDENT_KEYWORDS = [
    "검찰", "수사", "압수수색", "구속", "기소", "혐의", "고발",
    "로비", "비리", "은닉", "포탈", "탈세 혐의", "구형", "선고",
]
# INCIDENT_KEYWORDS가 걸려도 이 중 하나가 같이 있으면 "제도 관련 기사"로 보고 살린다
# (예: "탈세 혐의 판결에 따른 예규 변경" — 단순 배제가 아니라 AND 조건인 이유).
PROCEDURAL_KEYWORDS = ["개정", "시행령", "예규", "지침"]

# "세무조사"는 단독으로 두면 검찰 수사·압수수색 기사를 끌어온다(SPEC-ADDENDUM-3.md §5-2).
# 아래 조합 중 하나가 같이 있을 때만 매칭한다.
TAX_INVESTIGATION_COMBO = {
    "trigger": "세무조사",
    "qualifiers": ["사전통지", "대상 선정", "운영규정", "절차", "기간 연장", "납세자권리"],
}

# ── 세목 화이트리스트 (SPEC-ADDENDUM-3.md §2) ───────────────────────────────
TAX_SUBJECTS_YML_PATH = "data/tax_subjects.yml"


def _load_tax_subjects(path: str = TAX_SUBJECTS_YML_PATH):
    """data/tax_subjects.yml을 읽어 (subjects, features)를 반환한다.

    파일이 없거나 파싱에 실패하면 **전체 세목 통과**로 동작하도록 빈 리스트를
    반환하고 경고를 남긴다(ADDENDUM-3 §2-1: "조용히 0건이 되는 것보다 낫다").
    `subjects`가 빈 리스트면 `match_tax_subject()`가 전부 통과시키는 걸로 약속한다.
    """
    try:
        import yaml
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        subjects = [s for s in data.get("subjects", []) if s.get("enabled", True)]
        features = data.get("features", {})
        label = ", ".join(s["label"] for s in subjects) or "(없음)"
        print(f"[tax] 활성 세목 {len(subjects)}개: {label}")
        return subjects, features
    except FileNotFoundError:
        print(f"[tax] {path} 없음 — 세목 화이트리스트 없이 전체 세목 통과로 동작합니다.")
        return [], {}
    except Exception as exc:  # noqa: BLE001 - YAML 파싱 실패 등, 조용히 죽는 것보다 낫다
        print(f"[tax] {path} 파싱 실패({exc}) — 전체 세목 통과로 동작합니다.")
        return [], {}


TAX_SUBJECTS, TAX_FEATURES = _load_tax_subjects()
