// data.json fetch 실패 시 폴백. 구조는 site/data.json과 완전히 동일해야 한다
// (SPEC.md §4, §7-7, SPEC-ADDENDUM-2.md §2 doc_type/stage 포함).
// 실사용 데이터가 아니라 오프라인/최초 file:// 실행 등 fetch가 막힐 때만 쓰이는
// 최소 표본이다 — 카테고리당 1~2건 + 일정 2건.
window.POLICY_DATA = {
  meta: {
    schema_version: "1.0",
    generated_at: null,
    window_days: 90,
    total_items: 4,
    counts_by_category: { kifrs: 1, tax: 1, icfr: 1, esg: 1 },
    sources_ok: [],
    sources_failed: [{ name: "data.json", reason: "fetch 실패 — 폴백 표본 데이터 표시 중" }]
  },
  categories: [
    { key: "kifrs", label: "K-IFRS",  color: "#1e3a8a", team: "회계팀" },
    { key: "tax",   label: "세법",     color: "#047857", team: "세무팀" },
    { key: "icfr",  label: "내부회계", color: "#b45309", team: "내부회계관리팀" },
    { key: "esg",   label: "ESG",     color: "#0e7490", team: "ESG팀" }
  ],
  items: [
    {
      id: "fallback0000000a",
      category: "tax",
      doc_type: "공개초안",
      stage: "의견수렴",
      title: "[표본] 법인세법 시행령 일부개정령안 입법예고",
      summary: [
        "이 항목은 data.json을 불러오지 못했을 때 보이는 표본입니다.",
        "실제 데이터가 아니니 새로고침 후 다시 확인해 주세요."
      ],
      impact: null,
      published_at: "2026-08-05",
      collected_at: "2026-08-05T07:00:00+09:00",
      effective_date: null,
      source: { name: "기획재정부", domain: "moef.go.kr", tier: 1, type: "official" },
      trust_score: 100, keyword_score: 60, final_score: 89.5,
      matched_keywords: ["세법", "시행령 개정"],
      urls: { news: null, official: null },
      law_meta: null,
      attachments: null
    },
    {
      id: "fallback0000000b",
      category: "kifrs",
      doc_type: "제·개정",
      stage: "확정",
      title: "[표본] K-IFRS 회계기준 개정 공표",
      summary: ["표본 데이터입니다."],
      impact: null,
      published_at: "2026-08-04",
      collected_at: "2026-08-05T07:00:00+09:00",
      effective_date: "2027-01-01",
      source: { name: "한국회계기준원", domain: "kasb.or.kr", tier: 1, type: "official" },
      trust_score: 100, keyword_score: 50, final_score: 85.0,
      matched_keywords: ["K-IFRS"],
      urls: { news: null, official: null },
      law_meta: null,
      attachments: null
    },
    {
      id: "fallback0000000c",
      category: "icfr",
      doc_type: "적용지침",
      stage: "확정",
      title: "[표본] 내부회계관리제도 평가·보고 가이드라인",
      summary: ["표본 데이터입니다."],
      impact: null,
      published_at: "2026-08-03",
      collected_at: "2026-08-05T07:00:00+09:00",
      effective_date: null,
      source: { name: "금융감독원", domain: "fss.or.kr", tier: 1, type: "official" },
      trust_score: 100, keyword_score: 40, final_score: 80.0,
      matched_keywords: ["내부회계관리제도"],
      urls: { news: null, official: null },
      law_meta: null,
      attachments: null
    },
    {
      id: "fallback0000000d",
      category: "esg",
      doc_type: "로드맵·일정",
      stage: "확정",
      title: "[표본] ESG 공시기준 단계적 의무화 로드맵",
      summary: ["표본 데이터입니다."],
      impact: null,
      published_at: "2026-08-02",
      collected_at: "2026-08-05T07:00:00+09:00",
      effective_date: "2027-01-01",
      source: { name: "금융위원회", domain: "fsc.go.kr", tier: 1, type: "official" },
      trust_score: 100, keyword_score: 40, final_score: 78.0,
      matched_keywords: ["ESG 공시"],
      urls: { news: null, official: null },
      law_meta: null,
      attachments: null
    }
  ],
  schedules: [
    {
      id: "sch_fallback0000000b",
      category: "kifrs",
      title: "[표본] K-IFRS 회계기준 개정 시행",
      effective_date: "2027-01-01",
      status: "upcoming",
      importance: "high",
      description: "표본 데이터입니다.",
      source: { name: "한국회계기준원", domain: "kasb.or.kr", tier: 1, type: "official" },
      urls: { news: null, official: null }
    },
    {
      id: "sch_fallback0000000d",
      category: "esg",
      title: "[표본] ESG 공시기준 1단계 적용",
      effective_date: "2027-01-01",
      status: "upcoming",
      importance: "medium",
      description: "표본 데이터입니다.",
      source: { name: "금융위원회", domain: "fsc.go.kr", tier: 1, type: "official" },
      urls: { news: null, official: null }
    }
  ]
};
