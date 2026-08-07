// data.json fetch 실패 시 폴백. 구조는 data.json과 완전히 동일해야 한다(SPEC.md §4, §7-7).
// STATUS: Phase 0 스캐폴딩 placeholder — Phase 5에서 더미/실데이터로 갱신 예정.
window.POLICY_DATA = {
  meta: {
    schema_version: "1.0",
    generated_at: null,
    window_days: 90,
    total_items: 0,
    counts_by_category: { kifrs: 0, tax: 0, icfr: 0, esg: 0 },
    sources_ok: [],
    sources_failed: []
  },
  categories: [
    { key: "kifrs", label: "K-IFRS",  color: "#1e3a8a", team: "회계팀" },
    { key: "tax",   label: "세법",     color: "#047857", team: "세무팀" },
    { key: "icfr",  label: "내부회계", color: "#b45309", team: "내부회계관리팀" },
    { key: "esg",   label: "ESG",     color: "#0e7490", team: "ESG팀" }
  ],
  items: [],
  schedules: []
};
