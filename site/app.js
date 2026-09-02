// Policy Watch — SPEC.md §7 구현 (site/app.js)
// data.json fetch 실패 시 data.js(window.POLICY_DATA) 폴백, 그것도 실패하면 오류 표시.
(function () {
  "use strict";

  // ── 상수 ──────────────────────────────────────────────────────────────
  var DOC_TYPE_ORDER = [
    "제·개정", "공개초안", "검토의견", "적용지침", "모범규준", "질의회신", "FAQ",
    "예시서식", "감사·검토기준", "해설·교육자료", "로드맵·일정", "보도자료",
    "결정례·판례", "기사", "논의자료", "해외기준",  // ADDENDUM-7 §3 안 A
  ];

  var STAGE_COLOR = {
    "의견수렴": "var(--stage-opinion)",
    "확정": "var(--navy)",
    "시행예정": "var(--stage-upcoming)",
    "시행중": "var(--stage-active)",
  };

  var todayISO = function () {
    var d = new Date();
    d.setHours(0, 0, 0, 0);
    var y = d.getFullYear(), m = String(d.getMonth() + 1).padStart(2, "0"), day = String(d.getDate()).padStart(2, "0");
    return y + "-" + m + "-" + day;
  };

  var addDaysISO = function (iso, days) {
    var d = new Date(iso + "T00:00:00");
    d.setDate(d.getDate() + days);
    var y = d.getFullYear(), m = String(d.getMonth() + 1).padStart(2, "0"), day = String(d.getDate()).padStart(2, "0");
    return y + "-" + m + "-" + day;
  };

  var fmtDot = function (iso) { return iso ? iso.replace(/-/g, ".") : ""; };

  // ADDENDUM-8 §1: 검색. 공백 제거 + 소문자 변환(백엔드 _norm()과 같은 규칙).
  var norm = function (s) { return String(s == null ? "" : s).replace(/\s+/g, "").toLowerCase(); };

  // §1-3 검색 대상 필드.
  function searchTargetsOf(it) {
    return [
      it.title,
      it.source ? it.source.name : "",
      (it.summary || []).join(" "),
      it.impact || "",
      (it.matched_keywords || []).join(" "),
    ].join(" ");
  }

  // §1-4 매칭 규칙(AND). addendum 원문 pseudo-code는 공백을 지운 뒤에 공백으로
  // split해서 사실상 토큰이 하나로 뭉개지는 버그가 있었다 — 원문 query를 먼저
  // 공백으로 나눠 토큰화한 뒤 토큰별로 norm()한다(다국어 대소문자·띄어쓰기
  // 무시는 그대로 유지).
  function matchesQuery(it, query) {
    if (!query) return true;
    var tokens = query.trim().split(/\s+/).filter(Boolean).map(norm);
    if (!tokens.length) return true;
    var hay = norm(searchTargetsOf(it));
    return tokens.every(function (t) { return hay.indexOf(t) !== -1; });
  }

  // 2026-09-01 사용자 지시: 시행일 캘린더의 일정 제목 앞에 붙은 "OOOO년"은
  // 시행일이 아니라 KASB 제개정현황(D) 소스가 붙인 "의결연도"다(같은
  // 기준서가 여러 해에 걸쳐 제·개정되면 제목이 완전히 같아져서 dedupe()가
  // 구분을 못 하는 문제를 막으려고 서버 쪽이 일부러 붙였다 — docs/NEXT.md
  // 2026-08-31 세션 기록 참고). 옆의 sched-date가 실제 시행일을 보여주는데
  // 제목의 연도와 달라 헷갈린다는 지적 — 원본 데이터(dedupe 근거)는 그대로
  // 두고 화면에 그릴 때만 뗀다.
  var _SCHEDULE_TITLE_YEAR_PREFIX_RE = /^(?:19|20)\d{2}년\s*/;
  function displayScheduleTitle(title) {
    return (title || "").replace(_SCHEDULE_TITLE_YEAR_PREFIX_RE, "");
  }

  var WEEKDAY_KO = ["일", "월", "화", "수", "목", "금", "토"];

  var fmtDateHeader = function (iso) {
    var d = new Date(iso + "T00:00:00");
    return fmtDot(iso) + " (" + WEEKDAY_KO[d.getDay()] + ")";
  };

  var dday = function (iso) {
    var target = new Date(iso + "T00:00:00");
    var today = new Date(); today.setHours(0, 0, 0, 0);
    return Math.round((target - today) / 864e5);
  };
  var ddayLabel = function (n) { return n === 0 ? "D-DAY" : n > 0 ? "D-" + n : "D+" + (-n); };

  // 2026-09-02: "오늘 챙길 것" 한 줄용 — dayISO가 속한 주(월요일 시작)의 시작일.
  var startOfWeekISO = function (dayISO) {
    var d = new Date(dayISO + "T00:00:00");
    var dow = d.getDay(); // 0=일 ... 6=토
    d.setDate(d.getDate() - (dow === 0 ? 6 : dow - 1));
    var y = d.getFullYear(), m = String(d.getMonth() + 1).padStart(2, "0"), day = String(d.getDate()).padStart(2, "0");
    return y + "-" + m + "-" + day;
  };

  // ADDENDUM-4 §5-4: 언론 보도 카드의 좌측 컬러바는 카테고리 색상의 40% 투명도.
  var hexToRgba = function (hex, alpha) {
    var h = (hex || "#64748b").replace("#", "");
    var r = parseInt(h.substring(0, 2), 16), g = parseInt(h.substring(2, 4), 16), b = parseInt(h.substring(4, 6), 16);
    return "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
  };

  // ── 데이터 로드 ───────────────────────────────────────────────────────
  function loadData() {
    return fetch("data.json", { cache: "no-store" })
      .then(function (res) {
        if (!res.ok) throw new Error("data.json HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        if (!data || !Array.isArray(data.items)) throw new Error("data.json 형식 오류");
        return data;
      })
      .catch(function (err) {
        if (window.POLICY_DATA && Array.isArray(window.POLICY_DATA.items)) {
          console.warn("[policy-watch] data.json fetch 실패, data.js 폴백 사용:", err);
          return window.POLICY_DATA;
        }
        throw err;
      });
  }

  // ── 상태 ─────────────────────────────────────────────────────────────
  var state = {
    view: "today",  // ADDENDUM-4 §5-1: today | all | calendar — 기본 진입 화면은 오늘의 정책동향
    cats: [],       // 빈 배열 = 전체
    doctypes: [],   // 빈 배열 = 전체
    staticOnly: false,  // ADDENDUM-4 §2-4: "상설자료만" 빠른 버튼
    from: addDaysISO(todayISO(), -30),
    to: todayISO(),
    sort: "importance",
    q: "",  // ADDENDUM-8 §1: 검색어. 오늘의 정책동향/전체 동향 둘 다에 적용(§1-1).
  };

  var DATA = null;
  var CAT_META = {}; // key -> {label, color, team}
  var calViewDate = new Date(); calViewDate.setDate(1); // 사이드바 캘린더가 표시 중인 달(1일 고정)
  var calFullViewDate = new Date(); calFullViewDate.setDate(1); // 시행일 캘린더 탭의 표시 중인 달

  // ── URL 쿼리 동기화 ──────────────────────────────────────────────────
  function stateFromURL() {
    var p = new URLSearchParams(location.search);
    if (["today", "all", "calendar", "standards"].indexOf(p.get("view")) !== -1) state.view = p.get("view");
    if (p.get("cat")) state.cats = p.get("cat").split(",").filter(Boolean);
    if (p.get("doctype")) state.doctypes = p.get("doctype").split(",").filter(Boolean);
    if (p.get("from")) state.from = p.get("from");
    if (p.get("to")) state.to = p.get("to");
    if (p.get("sort") === "latest" || p.get("sort") === "importance") state.sort = p.get("sort");
    if (p.get("static") === "1") state.staticOnly = true;
    if (p.get("q")) state.q = p.get("q");
  }

  function syncURL() {
    var p = new URLSearchParams();
    if (state.view !== "today") p.set("view", state.view);
    if (state.cats.length) p.set("cat", state.cats.join(","));
    if (state.doctypes.length) p.set("doctype", state.doctypes.join(","));
    if (state.staticOnly) p.set("static", "1");
    p.set("from", state.from);
    p.set("to", state.to);
    if (state.sort !== "importance") p.set("sort", state.sort);
    if (state.q) p.set("q", state.q);
    var qs = p.toString();
    history.replaceState(null, "", location.pathname + (qs ? "?" + qs : ""));
  }

  // ── 필터/정렬 ────────────────────────────────────────────────────────
  // ADDENDUM-4 §2-4 + 2026-08-28 피드백: 상설자료는 "기본 조회"(빠른 선택 범위인
  // 최근 90일 이내)에서는 아예 제외한다. 90일보다 넓게(직접 시작일을 더 과거로)
  // 잡으면 실제 published_at으로 정상 필터링해 노출한다 — "상설자료만" 버튼은
  // 그와 별개로 항상(날짜 무관) 상설자료만 보여준다.
  var STATIC_DEFAULT_WINDOW_DAYS = 90;

  function isWideDateRange() {
    return (new Date(state.to) - new Date(state.from)) / 864e5 > STATIC_DEFAULT_WINDOW_DAYS;
  }

  // 2026-08-28 피드백: "논의자료"(TF·실무그룹 중간 산출물)는 기본 조회/오늘의
  // 정책동향에서 제외하고, 문서종류 필터에서 "논의자료"를 직접 선택했을 때만
  // 보여준다. 상설자료와 달리 발행일이 최근일 수 있어 날짜 범위로는 못 거르므로
  // (상설자료의 "기간을 넓히면 보임" 방식이 아니라) 문서종류 선택 여부로만 게이팅한다.
  function showsDiscussionMaterial() {
    return state.doctypes.indexOf("논의자료") !== -1;
  }

  // ADDENDUM-7 §3 안 A: "해외기준"(IASB/ISSB)도 논의자료와 같은 방식 —
  // 완전 제외가 아니라 기본 조회/오늘의 정책동향에서만 빼고, 문서종류 필터에서
  // 직접 선택했을 때만 보여준다.
  function showsForeignStandard() {
    return state.doctypes.indexOf("해외기준") !== -1;
  }

  function filterItems(items) {
    var wideRange = isWideDateRange();
    var showDiscussion = showsDiscussionMaterial();
    var showForeign = showsForeignStandard();
    return items.filter(function (it) {
      if (state.cats.length && state.cats.indexOf(it.category) === -1) return false;
      if (state.doctypes.length && state.doctypes.indexOf(it.doc_type) === -1) return false;
      if (it.doc_type === "논의자료" && !showDiscussion) return false;
      if (it.doc_type === "해외기준" && !showForeign) return false;
      if (!matchesQuery(it, state.q)) return false;
      if (state.staticOnly) {
        // "상설자료만": 상설자료가 아니면 제외. 상설자료는 개정일이 오래돼 보통
        // 조회 기간 밖에 있는 게 정상이므로 이 모드에서는 날짜 필터를 건너뛴다.
        return !!it.is_static;
      }
      if (it.is_static && !wideRange) return false;
      if (it.published_at < state.from || it.published_at > state.to) return false;
      return true;
    });
  }

  function sortItems(items) {
    var out = items.slice();
    var cmp = (state.sort === "latest")
      ? function (a, b) { return a.published_at < b.published_at ? 1 : a.published_at > b.published_at ? -1 : b.final_score - a.final_score; }
      : function (a, b) { return b.final_score - a.final_score || (a.published_at < b.published_at ? 1 : -1); };
    out.sort(function (a, b) {
      // ADDENDUM-4 §2-3: 상시 비치 자료는 정렬 기준과 무관하게 신규 항목보다 아래로.
      var sa = a.is_static ? 1 : 0, sb = b.is_static ? 1 : 0;
      if (sa !== sb) return sa - sb;
      return cmp(a, b);
    });
    return out;
  }

  // ── stage 표시값 계산 (ADDENDUM-2 §2-2: 확정만 저장, 시행예정/시행중은 프론트 계산) ──
  function displayStage(item) {
    if (item.stage === "참고") return null;
    if (item.stage === "의견수렴") return "의견수렴";
    // stage === "확정"
    if (!item.effective_date) return "확정";
    return item.effective_date >= todayISO() ? "시행예정" : "시행중";
  }

  // ── 렌더: 뱃지/버튼 공통 조각 ────────────────────────────────────────
  function catBadge(catKey) {
    var meta = CAT_META[catKey] || { label: catKey };
    return '<span class="badge badge-cat" data-cat="' + catKey + '">' + esc(meta.label) + "</span>";
  }

  function actionButtons(urls) {
    var news = urls && urls.news;
    var official = urls && urls.official;
    var newsBtn = news
      ? '<a class="btn btn-outline" href="' + esc(news) + '" target="_blank" rel="noopener">뉴스 기사 보기</a>'
      : '<span class="btn btn-outline" aria-disabled="true" title="뉴스 링크 없음">뉴스 기사 보기</span>';
    var offBtn = official
      ? '<a class="btn btn-solid" href="' + esc(official) + '" target="_blank" rel="noopener">관련 기관 공식 원문 보기 🔗</a>'
      : '<span class="btn btn-solid" aria-disabled="true" title="원문 링크 없음">공식 원문 보기 🔗</span>';
    return newsBtn + offBtn;
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // ── 피드 렌더 ────────────────────────────────────────────────────────
  function renderFeed() {
    var feedEl = document.getElementById("feed");
    var filtered = sortItems(filterItems(DATA.items));

    // §1-2: 결과 건수 표시에 검색어 반영 — 총 12건 (검색: "법인세")
    var countHtml = "총 <b>" + filtered.length + "</b>건";
    if (state.q) countHtml += ' (검색: "' + esc(state.q) + '")';
    document.getElementById("resultCount").innerHTML = countHtml;

    if (!filtered.length) {
      // §1-6: 검색어가 있을 때는 검색 전용 빈 상태 메시지 + 버튼 2개.
      if (state.q) {
        feedEl.innerHTML =
          '<div class="empty-state">"' + esc(state.q) + '"에 해당하는 항목이 없습니다.' +
          '<div><button type="button" class="btn btn-outline" id="clearQueryBtn">검색어 지우기</button> ' +
          '<button type="button" class="btn btn-outline" id="widenAllBtn">전체 기간으로 조회</button></div></div>';
        document.getElementById("clearQueryBtn").addEventListener("click", function () {
          setQuery("");
          applyAndRender();
        });
        document.getElementById("widenAllBtn").addEventListener("click", function () {
          state.from = "2000-01-01";
          state.to = todayISO();
          refreshDateInputs();
          applyAndRender();
        });
        return;
      }
      feedEl.innerHTML =
        '<div class="empty-state">조건에 맞는 항목이 없습니다. 기간을 넓히거나 카테고리를 추가해 보세요.' +
        '<div><button type="button" class="btn btn-outline" id="widen90Btn">최근 90일로 보기</button></div></div>';
      document.getElementById("widen90Btn").addEventListener("click", function () {
        state.from = addDaysISO(todayISO(), -90);
        state.to = todayISO();
        refreshDateInputs();
        applyAndRender();
      });
      return;
    }

    // 2026-09-01 수정: 이전엔 정렬 기준이 '중요도순'이어도 날짜 그룹 자체는
    // 항상 published_at 내림차순으로 고정돼 있었다 — sortItems()가 계산한
    // final_score 순서가 그룹 내부에만 적용되고, 그룹 간 순서(=화면에서 실제로
    // 보이는 큰 흐름)는 날짜가 덮어써서 "중요도순인데 화면은 날짜순으로만
    // 내려간다"는 사용자 관측 그대로였다. '중요도순'일 때는 날짜 그룹을 없애고
    // final_score 순서 그대로 평평한 목록으로 렌더링한다(각 카드에 날짜를
    // 표기해 정보 손실은 없게 함 — renderCard 참고). '최신순'은 날짜 그룹이
    // 곧 정렬 기준과 일치하므로 기존 방식을 유지한다.
    var html;
    if (state.sort === "importance") {
      html = '<div class="card-list">' + filtered.map(renderCard).join("") + "</div>";
    } else {
      var groups = [];
      var byDate = {};
      filtered.forEach(function (it) {
        if (!byDate[it.published_at]) { byDate[it.published_at] = []; groups.push(it.published_at); }
        byDate[it.published_at].push(it);
      });
      groups.sort().reverse();

      html = groups.map(function (dateKey) {
        var cards = byDate[dateKey].map(renderCard).join("");
        return '<div class="date-group">' +
          '<div class="date-group-header">' + esc(fmtDateHeader(dateKey)) + "</div>" +
          '<div class="card-list">' + cards + "</div></div>";
      }).join("");
    }

    feedEl.innerHTML = html;
  }

  function renderCard(it) {
    var stage = displayStage(it);
    // 2026-09-02 디자인 개선(배지 위계): 꽉 채운 배경 대신 outline(테두리+글자
    // 색만)으로 톤다운 — .badge-stage 기본 스타일(styles.css) 참고.
    var stageBadge = stage
      ? '<span class="badge badge-stage" style="border-color:' + STAGE_COLOR[stage] + ';color:' + STAGE_COLOR[stage] + '">' + esc(stage) + "</span>"
      : "";
    // ADDENDUM-4 §2-3: 상설자료 회색 뱃지.
    var staticBadge = it.is_static ? '<span class="badge badge-static">상설자료</span>' : "";
    // ADDENDUM-7 §3 안 A: 해외기준(IASB/ISSB) 회색 뱃지.
    var foreignBadge = it.doc_type === "해외기준" ? '<span class="badge badge-foreign">해외기준</span>' : "";
    // 2026-09-02: impact가 null이어도(예: 법제처 항목의 개정이유가 회사와
    // 무관하다고 판단한 경우) AI가 요약했다는 사실 자체는 뱃지로 항상 보이게.
    var aiBadge = it.ai_generated ? '<span class="badge badge-ai">AI 요약</span>' : "";
    var officialTag = it.source && it.source.tier === 1 ? '<span class="badge-official">공식</span>' : "";
    // ADDENDUM-4 §3: "외 N건 보도" — 유사 기사가 병합된 경우.
    var dupTag = it.duplicate_count > 0 ? '<span class="dup-tag">외 ' + it.duplicate_count + '건 보도</span>' : "";
    // summary가 빈 배열이면(제목/출처를 반복할 뿐인 요약을 백엔드가 만들지 않기로
    // 했으므로, sources/_summarize.py 참고) 요약 영역 자체를 렌더링하지 않는다.
    var summaryHtml = (it.summary && it.summary.length)
      ? '<ul class="card-summary">' + it.summary.map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("") + "</ul>"
      : "";
    // ADDENDUM-8 §5-1: AI가 생성한 준비사항은 박스 색을 바꿔 구분한다("AI 요약"
    // 뱃지가 위쪽 배지 줄에 따로 붙으므로 여기 텍스트에 "(AI 생성)"을 또 반복하진
    // 않는다 — 2026-09-02 정리, impact가 null인 경우까지 뱃지로 커버하려고
    // 이 표시를 배지 자리로 옮겼다).
    var impactLabel = it.ai_generated ? "준비사항" : "실무 영향";
    var impactHtml = it.impact
      ? '<div class="card-impact' + (it.ai_generated ? " is-ai" : "") + '"><b>' + impactLabel + ':</b> ' + esc(it.impact) + "</div>"
      : "";
    // 2026-09-02 사용자 피드백: "AI 요약" 뱃지는 있는데 summary/impact가 둘 다
    // 비어있으면(=AI가 검토했지만 회사와 무관하다고 판단한 경우) 카드가 텅 빈
    // 것처럼 보여 헷갈린다 — 짧은 안내 문구로 "검토는 했다"는 걸 알려준다.
    var aiEmptyHtml = (it.ai_generated && !summaryHtml && !impactHtml)
      ? '<div class="card-ai-empty">AI 검토 결과 팜한농 해당사항 없음</div>'
      : "";
    var relatedHtml = renderRelatedNews(it.related_news);
    var revisionReasonHtml = renderRevisionReason(it);

    return (
      '<article class="card">' +
      '<div class="card-top">' +
      '<div class="card-badges">' + catBadge(it.category) +
      '<span class="badge badge-doctype">' + esc(it.doc_type) + "</span>" + stageBadge + staticBadge + foreignBadge + aiBadge + "</div>" +
      // '중요도순'에서는 날짜 그룹 헤더가 없으므로(renderFeed 참고) 카드 안에
      // 날짜를 직접 표기한다 — '최신순'에서도 항상 보여 일관성 유지.
      '<div class="card-source">' + esc(fmtDot(it.published_at)) + ' · 출처: ' + esc(it.source ? it.source.name : "-") + officialTag + dupTag + "</div>" +
      "</div>" +
      '<h3 class="card-title">' + esc(it.title) + "</h3>" +
      summaryHtml +
      impactHtml +
      aiEmptyHtml +
      revisionReasonHtml +
      relatedHtml +
      '<div class="card-actions">' + actionButtons(it.urls) + "</div>" +
      "</article>"
    );
  }

  // ADDENDUM-4 §4: 공식 카드에 붙은 관련 뉴스 접이식 목록. 기본 접힘, 비어있으면
  // 이 행 자체를 렌더하지 않는다.
  function renderRelatedNews(relatedNews) {
    if (!relatedNews || !relatedNews.length) return "";
    var rows = relatedNews.map(function (n) {
      var link = n.url
        ? '<a href="' + esc(n.url) + '" target="_blank" rel="noopener">' + esc(n.title) + "</a>"
        : esc(n.title);
      return '<li><span class="related-source">' + esc(n.source) + "</span> " + link +
        (n.published_at ? '<span class="related-date tnum">' + esc(fmtDot(n.published_at)) + "</span>" : "") +
        "</li>";
    }).join("");
    return (
      '<details class="related-news">' +
      '<summary>관련 보도 ' + relatedNews.length + "건</summary>" +
      '<ul class="related-news-list">' + rows + "</ul>" +
      "</details>"
    );
  }

  // 2026-09-02: 법제처 개정이유 원문(law_api.py가 채우는 revision_reason,
  // law.go.kr 항목만 있음) — 빈 줄 2개 이상을 문단 구분으로 보고 <p>로
  // 나눈다. 원문 자체가 "◇ 개정이유" 같은 소제목·항목마다 빈 줄로 떨어져
  // 있어(법제처 원문 서식), 이렇게 나누면 그 구조가 대체로 그대로 산다.
  function formatRevisionReason(text) {
    return text
      .split(/\n\s*\n/)
      .map(function (p) { return p.trim(); })
      .filter(Boolean)
      .map(function (p) { return "<p>" + esc(p).replace(/\n/g, "<br>") + "</p>"; })
      .join("");
  }

  // revision_reason이 없는 항목(법제처 소스가 아니거나 파싱 실패)은 토글 자체를
  // 렌더하지 않는다 — 빈 토글을 눌렀다가 아무것도 안 나오는 상황 방지.
  function renderRevisionReason(it) {
    if (!it.revision_reason) return "";
    return (
      '<details class="revision-reason">' +
      "<summary>개정이유 전문 보기</summary>" +
      '<div class="revision-reason-body">' + formatRevisionReason(it.revision_reason) + "</div>" +
      "</details>"
    );
  }

  // ── 캘린더 ───────────────────────────────────────────────────────────
  function schedulesByDate() {
    var map = {};
    DATA.schedules.forEach(function (s) {
      if (!map[s.effective_date]) map[s.effective_date] = [];
      map[s.effective_date].push(s);
    });
    return map;
  }

  // gridId/titleId를 받아 사이드바 미니 캘린더와 §5-1 전체화면 캘린더가 로직을
  // 공유한다. onCellClick(iso)는 날짜 클릭 시 호출된다.
  function renderCalendarInto(viewDate, gridId, titleId, onCellClick) {
    var y = viewDate.getFullYear(), m = viewDate.getMonth();
    document.getElementById(titleId).textContent = y + "년 " + (m + 1) + "월";

    var byDate = schedulesByDate();
    var firstDow = new Date(y, m, 1).getDay();
    var daysInMonth = new Date(y, m + 1, 0).getDate();
    var today = todayISO();

    var cells = [];
    for (var i = 0; i < firstDow; i++) cells.push('<div class="cal-cell is-empty"></div>');

    for (var d = 1; d <= daysInMonth; d++) {
      var iso = y + "-" + String(m + 1).padStart(2, "0") + "-" + String(d).padStart(2, "0");
      var evs = byDate[iso] || [];
      var isToday = iso === today;
      var dotsHtml = "";
      if (evs.length) {
        var shown = evs.slice(0, 3);
        dotsHtml = '<div class="cal-dots">' +
          shown.map(function (e) {
            // 2026-09-01 사용자 지시: 시행 완료(과거) 항목은 카테고리 색 대신
            // 회색으로 찍어 "이미 지난 일정"임을 한눈에 구분한다 — 지금까지는
            // 과거/미래 구분 없이 전부 카테고리 색이라, 지난달 이전으로
            // 넘겨봐도 시행 예정과 똑같이 보여 구분이 안 갔다.
            var isPast = e.effective_date < today;
            var color = isPast ? "#94a3b8" : ((CAT_META[e.category] || {}).color || "#94a3b8");
            // 2026-08-31 사용자 지시: 법제처 시행일과 위원회 회의 일정이 섞이면
            // 헷갈린다 — 회의 일정은 속이 빈 고리(테두리만), 실제 시행일은
            // 꽉 찬 점으로 구분한다(카테고리 색은 둘 다 그대로 유지).
            // 2026-09-02 사용자 지시: 로드맵 예정(is_roadmap_estimate)도 확정
            // 시행일과 섞이면 안 된다 — 회의 일정(실선 고리)과도 구분되게
            // 점선 고리로 세 번째 스타일을 준다.
            var style = e.is_meeting
              ? "border:1.5px solid " + color + ";background:transparent;"
              : e.is_roadmap_estimate
              ? "border:1.5px dashed " + color + ";background:transparent;"
              : "background:" + color + ";";
            var extraClass = e.is_meeting ? " cal-dot-meeting" : (e.is_roadmap_estimate ? " cal-dot-roadmap" : "");
            var title = e.is_meeting ? "위원회 회의 예정"
              : e.is_roadmap_estimate ? "로드맵 예정(미확정)"
              : (isPast ? "시행 완료" : "시행 예정");
            return '<span class="cal-dot' + extraClass +
              '" style="' + style + '" title="' + title + '"></span>';
          }).join("") +
          (evs.length > 3 ? '<span class="cal-more">+' + (evs.length - 3) + "</span>" : "") +
          "</div>";
      }
      cells.push(
        '<div class="cal-cell' + (evs.length ? " is-clickable" : "") + (isToday ? " is-today" : "") + '" data-date="' + iso + '">' +
        '<span class="cal-daynum">' + d + "</span>" + dotsHtml + "</div>"
      );
    }

    var dow = WEEKDAY_KO.map(function (w) { return '<div class="cal-dow">' + w + "</div>"; }).join("");
    var gridEl = document.getElementById(gridId);
    gridEl.innerHTML = dow + cells.join("");

    Array.prototype.forEach.call(gridEl.querySelectorAll(".cal-cell.is-clickable"), function (cell) {
      cell.addEventListener("click", function () { onCellClick(cell.getAttribute("data-date")); });
    });
  }

  function renderCalendar() {
    renderCalendarInto(calViewDate, "calGrid", "calTitle", function (iso) { highlightScheduleDate(iso, "schedList"); });
  }

  function renderCalendarFull() {
    renderCalendarInto(calFullViewDate, "calFullGrid", "calFullTitle", function (iso) { highlightScheduleDate(iso, "calFullSchedList"); });
  }

  function highlightScheduleDate(iso, listId) {
    var target = document.querySelector('#' + listId + ' .sched-item[data-date="' + iso + '"]');
    if (!target) return;
    document.getElementById(listId).classList.add("is-expanded");
    target.classList.add("is-highlight");
    target.scrollIntoView({ behavior: "smooth", block: "center" });
    setTimeout(function () { target.classList.remove("is-highlight"); }, 2000);
  }

  // hideDdayIfPast: ADDENDUM-8 §2-3 "과거 항목은 D-Day 대신 날짜만 표시"는
  // 시행일 캘린더 탭의 전체 목록(renderFullScheduleList())에만 해당한다 —
  // §2-4가 사이드바 위젯(renderScheduleList())은 "변경 없음"이라 명시했으므로,
  // 이 옵션을 안 넘기는 기존 호출부는 과거 항목이어도 D-Day를 그대로 보여준다.
  function scheduleItemHtml(s, hideDdayIfPast) {
    var isPast = s.effective_date < todayISO();
    var ddayClass = s.importance === "high" ? " is-important" : "";
    // 2026-08-31 사용자 지시: 법제처 시행일과 위원회 회의 일정이 캘린더에
    // 섞이면 헷갈린다 — 회의 일정 항목은 뱃지로 명시한다.
    var meetingBadge = s.is_meeting ? '<span class="badge badge-meeting">회의 예정</span>' : "";
    // 2026-09-02 사용자 지시: KSSB 자발적용 기준서처럼 esg_roadmap.yml 예정
    // 날짜로 채운 effective_date는 K-IFRS 같은 확정 시행일과 섞이면 안 된다
    // — 별도 뱃지로 명시한다(같은 항목이 회의 일정이면서 로드맵 예정일 수는
    // 없으므로 meetingBadge와 배타적으로 취급해도 무방).
    var roadmapBadge = s.is_roadmap_estimate ? '<span class="badge badge-roadmap">로드맵 예정</span>' : "";
    var ddayHtml = (isPast && hideDdayIfPast) ? "" :
      '<span class="dday-badge' + ddayClass + ' tnum">' + ddayLabel(dday(s.effective_date)) + "</span>";
    return (
      '<li class="sched-item' + (isPast ? " is-past" : "") + '" data-date="' + s.effective_date + '">' +
      '<div class="sched-top">' + ddayHtml + catBadge(s.category) + meetingBadge + roadmapBadge + "</div>" +
      '<div class="sched-item-title">' + esc(displayScheduleTitle(s.title)) + "</div>" +
      '<div class="sched-date tnum">' + esc(fmtDot(s.effective_date)) + "</div>" +
      '<div class="sched-desc">' + esc(s.description) + "</div>" +
      '<div class="sched-actions">' + actionButtons(s.urls) + "</div>" +
      "</li>"
    );
  }

  // ADDENDUM-8 §2-2: 미래 일정(가까운 순) 먼저, 그다음 과거 일정(최근 순).
  function sortSchedules(schedules) {
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var future = [], past = [];
    schedules.forEach(function (s) {
      (new Date(s.effective_date + "T00:00:00") >= today ? future : past).push(s);
    });
    future.sort(function (a, b) { return new Date(a.effective_date) - new Date(b.effective_date); });
    past.sort(function (a, b) { return new Date(b.effective_date) - new Date(a.effective_date); });
    return { future: future, past: past };
  }

  // ── 시행 예정 일정 리스트 (사이드바, 당월 ~ 향후 3개월) ──────────────
  function renderScheduleList() {
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var winStart = today.getFullYear() + "-" + String(today.getMonth() + 1).padStart(2, "0") + "-01";
    var winEndDate = new Date(today.getFullYear(), today.getMonth() + 4, 0); // 향후 3개월 말일
    var winEnd = winEndDate.getFullYear() + "-" + String(winEndDate.getMonth() + 1).padStart(2, "0") + "-" + String(winEndDate.getDate()).padStart(2, "0");

    var list = DATA.schedules.filter(function (s) { return s.effective_date >= winStart && s.effective_date <= winEnd; });
    // bare .map(scheduleItemHtml)은 Array#map이 두 번째 인자로 index를 넘겨
    // hideDdayIfPast에 index가 들어가버린다 — §2-4가 "변경 없음"이라 명시한
    // 사이드바이므로 명시적으로 인자 1개만 넘긴다.
    var html = list.map(function (s) { return scheduleItemHtml(s); }).join("");
    document.getElementById("schedList").innerHTML = html || '<li class="sched-desc">해당 기간 내 예정된 일정이 없습니다.</li>';
  }

  // ── 시행일 캘린더 탭: 전체 일정 리스트(기간 제한 없음) ────────────────
  // 2026-09-01 수정(사용자 지시): ADDENDUM-8 §2-3 원안은 과거 항목을 "최근
  // 10건"이라는 고정 개수로 잘랐는데, KASB 제개정현황(List2006.do) 소스가
  // 2016~2024년 과거 개정 이력까지 몰고 들어오면서 시행 완료가 71건까지
  // 불어났다(실측). 개수 기준은 최근 몇 달에 몰려 있으면 오히려 정작 최근
  // 것도 다 못 보여주고, 뜸한 시기엔 몇 년 전 것까지 끌고 오는 문제가 있어
  // "최근 12개월 이내"라는 날짜 기준으로 바꿨다.
  var PAST_SCHEDULE_RECENT_MONTHS = 12;

  function pastScheduleCutoffISO() {
    var d = new Date(); d.setHours(0, 0, 0, 0);
    d.setMonth(d.getMonth() - PAST_SCHEDULE_RECENT_MONTHS);
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }

  function renderFullScheduleList() {
    var g = sortSchedules(DATA.schedules);
    var html = "";

    // .map(scheduleItemHtml) 그대로 쓰면 Array#map이 (item, index, array)를
    // 넘겨서 두 번째 인자(hideDdayIfPast)에 인덱스가 들어가버린다(0번째 항목만
    // falsy라 D-Day가 안 지워짐) — 반드시 래퍼로 감싸서 true만 넘긴다.
    if (g.future.length) {
      html += '<li class="sched-group-label">시행 예정 (' + g.future.length + "건)</li>";
      html += g.future.map(function (s) { return scheduleItemHtml(s, true); }).join("");
    }
    if (g.past.length) {
      if (g.future.length) html += '<li class="sched-divider" aria-hidden="true"></li>';
      // 이 라벨은 의도적으로 "필터 전" 총계(g.past.length)를 쓴다 — 아래
      // recentPast/olderPast 분리는 "어느 항목을 보여줄지"만 정하고, 라벨은
      // "시행 완료가 총 몇 건인지"를 알려주는 용도라 다른 숫자다(버그 아님).
      html += '<li class="sched-group-label">시행 완료 (' + g.past.length + "건)</li>";
      var cutoff = pastScheduleCutoffISO();
      var recentPast = g.past.filter(function (s) { return s.effective_date >= cutoff; });
      var olderPast = g.past.filter(function (s) { return s.effective_date < cutoff; });
      html += recentPast.map(function (s) { return scheduleItemHtml(s, true); }).join("");
      if (olderPast.length) {
        html += olderPast.map(function (s) {
          return scheduleItemHtml(s, true).replace('class="sched-item', 'class="sched-item is-more-past');
        }).join("");
        html += '<li class="show-more-past-wrap"><button type="button" class="show-all-btn" id="pastMoreBtn">이전 일정 더 보기 (' +
          olderPast.length + "건)</button></li>";
      }
    }
    if (!g.future.length && !g.past.length) {
      html = '<li class="sched-desc">등록된 일정이 없습니다.</li>';
    }

    document.getElementById("calFullSchedList").innerHTML = html;
    document.getElementById("calFullSub").textContent = "시행 예정 " + g.future.length + "건 · 시행 완료 " + g.past.length + "건";

    var moreBtn = document.getElementById("pastMoreBtn");
    if (moreBtn) {
      moreBtn.addEventListener("click", function () {
        Array.prototype.forEach.call(document.querySelectorAll("#calFullSchedList .is-more-past"), function (li) {
          li.classList.remove("is-more-past");
        });
        moreBtn.parentElement.remove();
      });
    }
  }

  // ── "현행 기준" (2026-09-02 사용자 요청) ────────────────────────────────
  // DATA.current_standards(sources/current_standards.py가 새로 크롤링 없이
  // 기존 수집 데이터에서 조립)를 그대로 표로 렌더링만 한다 — 필터/검색 상태와
  // 무관한 정적 참고 화면이라 다른 뷰처럼 switchView()마다 다시 그릴 필요
  // 없이 init()에서 한 번만 렌더링한다.
  function _stdEmptyRow(colspan, text) {
    return '<tr><td colspan="' + colspan + '" class="std-empty">' + esc(text) + "</td></tr>";
  }

  function _stdLinkCell(url) {
    return url
      ? '<a href="' + esc(url) + '" target="_blank" rel="noopener">원문</a>'
      : '<span class="std-no-link">-</span>';
  }

  function renderKifrsStandards(section) {
    var s = section || { catalog_url: "", recent: [] };
    var rows = s.recent.length
      ? s.recent.map(function (r) {
          return "<tr><td>" + esc(r.standard_no) + "</td>" +
            '<td class="tnum">' + esc(fmtDot(r.latest_revision_date)) + "</td>" +
            '<td class="tnum">' + esc(fmtDot(r.effective_date)) + "</td>" +
            "<td>" + _stdLinkCell(r.url) + "</td></tr>";
        }).join("")
      : _stdEmptyRow(4, "표시할 개정 이력이 없습니다.");
    document.getElementById("stdKifrs").innerHTML =
      '<h2 class="std-title">K-IFRS</h2>' +
      '<a class="std-catalog-link" href="' + esc(s.catalog_url) + '" target="_blank" rel="noopener">전체 기준서 목록 보기(회계기준원) →</a>' +
      '<p class="std-note">아래는 개정 이력이 있는 기준서 중 최근 5건만 표시합니다 — 전체 기준서 목록은 위 링크를 참고하세요.</p>' +
      '<div class="std-table-wrap"><table class="std-table"><thead><tr><th>기준서</th><th>최종 개정일</th><th>시행일</th><th>링크</th></tr></thead>' +
      "<tbody>" + rows + "</tbody></table></div>";
  }

  function renderEsgStandards(section) {
    var s = section || { catalog_url: "", recent: [] };
    var rows = s.recent.length
      ? s.recent.map(function (r) {
          // 2026-09-02 사용자 지시: 시행 예정일만 보이면 팜한농 자체 적용일로
          // 오독할 수 있어(팜한농은 1차 대상이 아니라 후속 단계) 대상 범위를
          // 괄호로 병기한다 — "(로드맵 예정)" 같은 모호한 표현보다 구체적.
          var eff = esc(fmtDot(r.effective_date)) + (r.effective_date_scope_note ? " (" + esc(r.effective_date_scope_note) + ")" : "");
          return "<tr><td>" + esc(r.title) + "</td>" +
            '<td class="tnum">' + esc(fmtDot(r.issued_date)) + "</td>" +
            '<td class="tnum">' + eff + "</td>" +
            "<td>" + _stdLinkCell(r.url) + "</td></tr>";
        }).join("")
      : _stdEmptyRow(4, "표시할 공시기준서가 없습니다.");
    document.getElementById("stdEsg").innerHTML =
      '<h2 class="std-title">지속가능성 공시</h2>' +
      '<a class="std-catalog-link" href="' + esc(s.catalog_url) + '" target="_blank" rel="noopener">전체 공시기준서 목록 보기(회계기준원) →</a>' +
      '<div class="std-table-wrap"><table class="std-table"><thead><tr><th>기준서</th><th>제정일</th><th>시행(예정)</th><th>링크</th></tr></thead>' +
      "<tbody>" + rows + "</tbody></table></div>";
  }

  function renderTaxStandards(section) {
    var s = section || { laws: [] };
    var rows = s.laws.length
      ? s.laws.map(function (r) {
          return "<tr><td>" + esc(r.law_name) + "</td>" +
            '<td class="tnum">' + esc(fmtDot(r.promulgation_date)) + "</td>" +
            '<td class="tnum">' + esc(fmtDot(r.enforcement_date)) + "</td>" +
            "<td>" + _stdLinkCell(r.url) + "</td></tr>";
        }).join("")
      : _stdEmptyRow(4, "표시할 법령이 없습니다.");
    document.getElementById("stdTax").innerHTML =
      '<h2 class="std-title">세법</h2>' +
      '<p class="std-note">법제처 국가법령정보 현행 조문 기준입니다(본법/시행령/시행규칙).</p>' +
      '<div class="std-table-wrap"><table class="std-table"><thead><tr><th>법령명</th><th>최종 개정일</th><th>현행 시행일</th><th>링크</th></tr></thead>' +
      "<tbody>" + rows + "</tbody></table></div>";
  }

  function renderIcfrStandards(section) {
    var s = section || { catalog_url: "", buckets: [] };
    var bucketsHtml = s.buckets.map(function (b) {
      var rows = b.documents.length
        ? b.documents.map(function (d) {
            return "<tr><td>" + esc(d.title) + "</td>" +
              '<td class="tnum">' + esc(fmtDot(d.revision_date)) + "</td>" +
              "<td>" + _stdLinkCell(d.url) + "</td></tr>";
          }).join("")
        : _stdEmptyRow(3, "표시할 문서가 없습니다.");
      return '<div class="std-bucket"><h3 class="std-bucket-title">' + esc(b.label) + "</h3>" +
        '<div class="std-table-wrap"><table class="std-table"><thead><tr><th>문서명</th><th>개정일</th><th>링크</th></tr></thead>' +
        "<tbody>" + rows + "</tbody></table></div></div>";
    }).join("");
    document.getElementById("stdIcfr").innerHTML =
      '<h2 class="std-title">내부회계</h2>' +
      '<a class="std-catalog-link" href="' + esc(s.catalog_url) + '" target="_blank" rel="noopener">k-icfr.org 바로가기 →</a>' +
      bucketsHtml;
  }

  function renderCurrentStandards() {
    var cs = DATA.current_standards || {};
    renderKifrsStandards(cs.kifrs);
    renderEsgStandards(cs.esg);
    renderTaxStandards(cs.tax);
    renderIcfrStandards(cs.icfr);
  }

  // ── 화면 전환: 오늘의 정책동향 / 전체 동향 / 시행일 캘린더 / 현행 기준 (ADDENDUM-4 §5-1) ──
  var VIEW_IDS = { today: "viewToday", all: "viewAll", calendar: "viewCalendar", standards: "viewStandards" };

  function switchView(view) {
    state.view = view;
    Object.keys(VIEW_IDS).forEach(function (v) {
      document.getElementById(VIEW_IDS[v]).classList.toggle("is-active", v === view);
    });
    Array.prototype.forEach.call(document.querySelectorAll("#navTabs button"), function (btn) {
      btn.classList.toggle("is-active", btn.getAttribute("data-view") === view);
    });
    if (view === "today") renderTodayView();
    if (view === "calendar") renderCalendarFull();
    syncURL();
  }

  // ── 최근 정책동향 (ADDENDUM-4 §5, 2026-09-01 이름·로직 수정) ─────────────
  // 사용자 지적: 원래 이름 "오늘의 정책동향"은 실측 결과 대부분의 날에 안 맞는다
  // — K-IFRS/세법/내부회계/ESG를 통틀어도 공식 발행물이 "오늘" 나오는 날 자체가
  // 드물어서(고정 3일로 확대해도 0건인 날이 흔함), 회계연도 내내 "오늘"이라는
  // 이름이 사실과 다른 걸 보여주는 셈이었다. 두 가지로 대응한다:
  // (1) 탭 이름을 "최근 정책동향"으로 바꿔 날짜 프레이밍 자체를 느슨하게 하고,
  // (2) 고정 3일 대신 최소 5건이 찰 때까지 1→3→7→14→30일 순으로 점진적으로
  //     기간을 넓힌다("최근"이라는 이름에 맞게 30일 이상은 안 넓힌다 — 그보다
  //     오래된 건 "전체 동향" 탭에서 날짜를 직접 넓혀서 보면 된다).
  // 헤더의 기간 안내도 "확대됐을 때만" 뜨던 걸 넓힌 기간을 항상 명시하도록 바꿨다.
  var TODAY_VIEW_WINDOWS = [1, 3, 7, 14, 30];
  var TODAY_VIEW_MIN_ITEMS = 5;

  function renderTodayView() {
    var day = (DATA.meta && DATA.meta.generated_at) ? DATA.meta.generated_at.slice(0, 10) : todayISO();
    var pool = DATA.items.filter(function (it) {
      return !it.is_static && it.doc_type !== "논의자료" && it.doc_type !== "해외기준";
    });

    var windowDays = TODAY_VIEW_WINDOWS[0];
    var from = day;
    var todays = [];
    for (var i = 0; i < TODAY_VIEW_WINDOWS.length; i++) {
      windowDays = TODAY_VIEW_WINDOWS[i];
      from = addDaysISO(day, -(windowDays - 1));
      todays = pool.filter(function (it) { return it.published_at >= from && it.published_at <= day; });
      if (todays.length >= TODAY_VIEW_MIN_ITEMS) break;
    }
    var expanded = windowDays > 1;

    // ADDENDUM-8 §1-1: 검색은 날짜 범위를 정한 다음 그 안에서만 좁힌다 —
    // 검색어 때문에 기간 확대 안내가 잘못 뜨지 않도록.
    if (state.q) todays = todays.filter(function (it) { return matchesQuery(it, state.q); });

    var official = todays.filter(function (it) { return it.source && it.source.type === "official"; });
    var news = todays.filter(function (it) { return !(it.source && it.source.type === "official"); });
    // §5-5 정렬: 공식 그룹은 tier 오름차순 → final_score 내림차순, 보도 그룹은 final_score 내림차순.
    official.sort(function (a, b) { return (a.source.tier - b.source.tier) || (b.final_score - a.final_score); });
    news.sort(function (a, b) { return b.final_score - a.final_score; });

    document.getElementById("todayTitle").textContent = windowDays === 1
      ? fmtDateHeader(day) + " 소식"
      : "최근 " + windowDays + "일 소식";
    document.getElementById("todayCounts").textContent = "공식 " + official.length + "건 · 보도 " + news.length + "건";
    var noticeEl = document.getElementById("todayNotice");
    noticeEl.hidden = !expanded;
    if (expanded) {
      noticeEl.textContent = "오늘 발표된 소식이 적어 최근 " + windowDays + "일(" +
        fmtDot(from) + "~" + fmtDot(day) + ") 범위로 넓혀 보여줍니다.";
    }

    var OFFICIAL_MAX = 12, NEWS_MAX = 12;
    document.getElementById("todayOfficialGrid").innerHTML = official.slice(0, OFFICIAL_MAX).map(renderTodayCard).join("");
    document.getElementById("todayNewsGrid").innerHTML = news.slice(0, NEWS_MAX).map(renderTodayCard).join("");
    document.getElementById("todayOfficialMore").hidden = official.length <= OFFICIAL_MAX;
    document.getElementById("todayNewsMore").hidden = news.length <= NEWS_MAX;
    document.getElementById("todayOfficialSection").hidden = official.length === 0;
    document.getElementById("todayNewsSection").hidden = news.length === 0;
    document.getElementById("todayEmpty").hidden = todays.length > 0;
    // §1-6: 검색 결과가 0건이면 검색 전용 문구/버튼으로 바꾼다.
    var emptyText = document.getElementById("todayEmptyText");
    var emptyActions = document.getElementById("todayEmptyActions");
    if (state.q) {
      emptyText.textContent = '"' + state.q + '"에 해당하는 항목이 없습니다.';
      emptyActions.innerHTML =
        '<button type="button" class="btn btn-outline" id="todayClearQueryBtn">검색어 지우기</button> ' +
        '<button type="button" class="btn btn-outline" id="todayGoAllBtn">전체 동향에서 검색</button>';
      var clearBtn = document.getElementById("todayClearQueryBtn");
      if (clearBtn) clearBtn.addEventListener("click", function () { setQuery(""); applyAndRender(); });
    } else {
      emptyText.textContent = "최근 " + windowDays + "일간 새로 발표된 소식이 없습니다. 주말·공휴일이거나 아직 수집 전일 수 있습니다.";
      emptyActions.innerHTML = '<button type="button" class="btn btn-outline" id="todayGoAllBtn">전체 동향 보기</button>';
    }
    var goAllBtn = document.getElementById("todayGoAllBtn");
    if (goAllBtn) goAllBtn.addEventListener("click", function () { switchView("all"); });
  }

  function renderTodayCard(it) {
    var meta = CAT_META[it.category] || {};
    var color = meta.color || "#64748b";
    var isOfficial = it.source && it.source.type === "official";
    var borderColor = isOfficial ? color : hexToRgba(color, 0.4);  // §5-4: 보도는 40% 투명도
    var orgBadge = isOfficial
      ? '<span class="badge badge-org">공식기관</span>'
      : '<span class="badge badge-outlet">' + esc(it.source ? it.source.name : "") + "</span>";
    // 2026-09-02: impact가 null이어도(예: 법제처 항목의 개정이유가 회사와
    // 무관하다고 판단한 경우) AI가 요약했다는 사실 자체는 뱃지로 항상 보이게
    // — renderCard()와 동일한 이유로 impact 박스 안이 아니라 뱃지 자리로 옮김.
    var aiBadge = it.ai_generated ? '<span class="badge badge-ai">AI 요약</span>' : "";
    var summaryHtml = (it.summary && it.summary.length)
      ? '<ul class="today-card-summary">' + it.summary.slice(0, 2).map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("") + "</ul>"
      : "";
    var impactHtml = it.impact
      ? '<div class="today-card-impact' + (it.ai_generated ? " is-ai" : "") + '">' + esc(it.impact) + "</div>"
      : "";
    // 2026-09-02 사용자 피드백: renderCard()와 동일 — AI 검토는 했는데 둘 다
    // 비어있으면 빈 카드처럼 보이니 짧은 안내 문구를 넣는다.
    var aiEmptyHtml = (it.ai_generated && !summaryHtml && !impactHtml)
      ? '<div class="card-ai-empty">AI 검토 결과 팜한농 해당사항 없음</div>'
      : "";
    var relatedHtml = isOfficial ? renderRelatedNews(it.related_news) : "";
    var revisionReasonHtml = renderRevisionReason(it);
    var actionUrl = isOfficial ? (it.urls && it.urls.official) : (it.urls && it.urls.news);
    var actionLabel = isOfficial ? "원문 →" : "기사 보기 →";
    var actionHtml = actionUrl
      ? '<a class="btn btn-outline" href="' + esc(actionUrl) + '" target="_blank" rel="noopener">' + actionLabel + "</a>"
      : '<span class="btn btn-outline" aria-disabled="true" title="링크 없음">' + actionLabel + "</span>";

    return (
      '<article class="today-card' + (isOfficial ? "" : " is-news") + '" style="border-left-color:' + borderColor + '">' +
      '<div class="today-card-badges">' + catBadge(it.category) + orgBadge + aiBadge + "</div>" +
      '<h3 class="today-card-title">' + esc(it.title) + "</h3>" +
      summaryHtml + impactHtml + aiEmptyHtml + revisionReasonHtml + relatedHtml +
      '<div class="today-card-bottom">' +
      "<span>" + esc(it.source ? it.source.name : "-") + " · " + esc(fmtDot(it.published_at)) + "</span>" +
      actionHtml +
      "</div></article>"
    );
  }

  // ── 문서종류 드롭다운 ────────────────────────────────────────────────
  function buildDoctypeMenu() {
    var present = {};
    DATA.items.forEach(function (it) { present[it.doc_type] = true; });
    var ordered = DOC_TYPE_ORDER.filter(function (t) { return present[t]; });
    var menu = document.getElementById("doctypeMenu");
    menu.innerHTML = ordered.map(function (t) {
      return '<label><input type="checkbox" value="' + esc(t) + '"> ' + esc(t) + "</label>";
    }).join("");
    Array.prototype.forEach.call(menu.querySelectorAll('input[type="checkbox"]'), function (cb) {
      cb.addEventListener("change", function () {
        var checked = Array.prototype.map.call(menu.querySelectorAll('input:checked'), function (c) { return c.value; });
        state.doctypes = checked;
        updateDoctypeSummary();
        applyAndRender();
      });
    });
  }

  function updateDoctypeSummary() {
    var summary = document.getElementById("doctypeSummary");
    summary.textContent = state.doctypes.length ? "문서 종류: " + state.doctypes.length + "개 선택" : "문서 종류: 전체";
    var menu = document.getElementById("doctypeMenu");
    Array.prototype.forEach.call(menu.querySelectorAll('input[type="checkbox"]'), function (cb) {
      cb.checked = state.doctypes.indexOf(cb.value) !== -1;
    });
  }

  // ── 필터 바 이벤트 ───────────────────────────────────────────────────
  function updateCatChipsUI() {
    Array.prototype.forEach.call(document.querySelectorAll(".chip"), function (chip) {
      var cat = chip.getAttribute("data-cat");
      var active = cat === "all" ? state.cats.length === 0 : state.cats.indexOf(cat) !== -1;
      chip.classList.toggle("is-active", active);
    });
    document.getElementById("staticOnlyBtn").classList.toggle("is-active", state.staticOnly);
  }

  function refreshDateInputs() {
    document.getElementById("dateFrom").value = state.from;
    document.getElementById("dateTo").value = state.to;
  }

  function applyAndRender() {
    syncURL();
    renderFeed();
    renderScheduleList();
    updateCatChipsUI();
    // ADDENDUM-8 §1-1: 검색은 오늘의 정책동향에도 적용된다 — 그 탭이 보이는
    // 중이면 같이 다시 그린다(다른 필터는 today 탭에 영향 없음, 검색만 예외).
    if (state.view === "today") renderTodayView();
  }

  // ADDENDUM-8 §1: 검색창 두 개(필터 바 / 오늘의 정책동향 헤더)를 같은
  // state.q로 동기화한다. 한쪽에 입력해도 다른 쪽 표시값과 X 버튼이 맞게 갱신된다.
  function setQuery(q) {
    state.q = q || "";
    var input1 = document.getElementById("searchInput");
    var input2 = document.getElementById("todaySearchInput");
    if (input1 && input1.value !== state.q) input1.value = state.q;
    if (input2 && input2.value !== state.q) input2.value = state.q;
    document.getElementById("searchClear").hidden = !state.q;
    document.getElementById("todaySearchClear").hidden = !state.q;
  }

  function wireSearch() {
    var DEBOUNCE_MS = 200;
    var timer = null;
    function onInput(e) {
      var val = e.target.value;
      clearTimeout(timer);
      timer = setTimeout(function () {
        setQuery(val);
        applyAndRender();
      }, DEBOUNCE_MS);
    }
    ["searchInput", "todaySearchInput"].forEach(function (id) {
      document.getElementById(id).addEventListener("input", onInput);
    });
    ["searchClear", "todaySearchClear"].forEach(function (id) {
      document.getElementById(id).addEventListener("click", function () {
        clearTimeout(timer);
        setQuery("");
        applyAndRender();
      });
    });
  }

  function wireFilterBar() {
    document.getElementById("catChips").addEventListener("click", function (e) {
      var chip = e.target.closest(".chip");
      if (!chip) return;
      var cat = chip.getAttribute("data-cat");
      if (cat === "all") {
        state.cats = [];
      } else {
        var idx = state.cats.indexOf(cat);
        if (idx === -1) state.cats.push(cat); else state.cats.splice(idx, 1);
      }
      applyAndRender();
    });

    document.getElementById("applyDateBtn").addEventListener("click", function () {
      var from = document.getElementById("dateFrom").value;
      var to = document.getElementById("dateTo").value;
      if (from) state.from = from;
      if (to) state.to = to;
      Array.prototype.forEach.call(document.querySelectorAll(".quick-range"), function (b) { b.classList.remove("is-active"); });
      applyAndRender();
    });

    Array.prototype.forEach.call(document.querySelectorAll(".quick-range"), function (btn) {
      btn.addEventListener("click", function () {
        var days = parseInt(btn.getAttribute("data-days"), 10);
        state.to = todayISO();
        state.from = addDaysISO(state.to, -days);
        refreshDateInputs();
        Array.prototype.forEach.call(document.querySelectorAll(".quick-range"), function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        applyAndRender();
      });
    });

    // [data-doctype]로 한정: "상설자료만"(#staticOnlyBtn)도 .quick-doctype 클래스를
    // 공유하지만 doc_type 필터가 아니라 별도 토글이라 여기서 걸러야 한다(아래 참고).
    Array.prototype.forEach.call(document.querySelectorAll(".quick-doctype[data-doctype]"), function (btn) {
      btn.addEventListener("click", function () {
        state.doctypes = [btn.getAttribute("data-doctype")];
        updateDoctypeSummary();
        applyAndRender();
      });
    });

    document.getElementById("staticOnlyBtn").addEventListener("click", function () {
      state.staticOnly = !state.staticOnly;
      this.classList.toggle("is-active", state.staticOnly);
      applyAndRender();
    });

    document.getElementById("sortSelect").addEventListener("change", function (e) {
      state.sort = e.target.value;
      applyAndRender();
    });

    document.getElementById("schedShowAll").addEventListener("click", function () {
      document.getElementById("schedList").classList.toggle("is-expanded");
    });

    document.getElementById("calPrev").addEventListener("click", function () {
      calViewDate.setMonth(calViewDate.getMonth() - 1);
      renderCalendar();
    });
    document.getElementById("calNext").addEventListener("click", function () {
      calViewDate.setMonth(calViewDate.getMonth() + 1);
      renderCalendar();
    });

    document.getElementById("calToggle").addEventListener("click", function () {
      var body = document.getElementById("calBody");
      var isOpen = body.classList.toggle("is-open");
      this.setAttribute("aria-expanded", String(isOpen));
    });
  }

  // ── 화면 전환 + 시행일 캘린더 탭 이벤트 (ADDENDUM-4 §5) ───────────────
  function wireViews() {
    document.getElementById("navTabs").addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-view]");
      if (!btn) return;
      switchView(btn.getAttribute("data-view"));
    });

    document.getElementById("calFullPrev").addEventListener("click", function () {
      calFullViewDate.setMonth(calFullViewDate.getMonth() - 1);
      renderCalendarFull();
    });
    document.getElementById("calFullNext").addEventListener("click", function () {
      calFullViewDate.setMonth(calFullViewDate.getMonth() + 1);
      renderCalendarFull();
    });

    // todayGoAllBtn은 renderTodayView()가 매번 다시 그리며 직접 바인딩한다
    // (검색 유무에 따라 문구가 바뀌는 버튼이라 정적 바인딩이 유지되지 않음).
    ["todayOfficialMore", "todayNewsMore"].forEach(function (id) {
      document.getElementById(id).addEventListener("click", function () { switchView("all"); });
    });
  }

  // ── 네비게이션 스크롤 그림자 ─────────────────────────────────────────
  function wireNavScroll() {
    var nav = document.getElementById("nav");
    window.addEventListener("scroll", function () {
      nav.classList.toggle("is-scrolled", window.scrollY > 4);
    }, { passive: true });
  }

  // ── 갱신 시각 표시 ───────────────────────────────────────────────────
  function renderMeta() {
    var el = document.getElementById("navUpdated");
    var g = DATA.meta && DATA.meta.generated_at;
    if (!g) { el.textContent = "마지막 갱신 정보 없음"; return; }
    var d = new Date(g);
    var y = d.getFullYear(), m = String(d.getMonth() + 1).padStart(2, "0"), day = String(d.getDate()).padStart(2, "0");
    var hh = String(d.getHours()).padStart(2, "0"), mm = String(d.getMinutes()).padStart(2, "0");
    el.textContent = "마지막 갱신 " + y + "." + m + "." + day + " " + hh + ":" + mm;
  }

  // 2026-09-02 사용자 요청: 헤더 아래 "오늘 챙길 것" 한 줄 — 가장 임박한 일정
  // (D-day, 회의 예정/로드맵 포함 — sortSchedules()가 이미 미래 전체를 다룸)과
  // 이번 주(월요일 시작) 신규 수집 건수만 보여준다. 기준일은 "오늘의 정책동향"과
  // 동일하게 DATA.meta.generated_at(데이터가 실제로 언제 수집됐는지)을 우선
  // 쓴다 — 클라이언트 로컬 날짜만 쓰면 크롤링이 늦어진 날 "이번 주 신규 0건"처럼
  // 실제와 다르게 보일 수 있어서다.
  function renderHeaderHighlight() {
    var el = document.getElementById("navHighlight");
    var textEl = document.getElementById("navHighlightText");
    if (!el || !textEl) return;

    var day = (DATA.meta && DATA.meta.generated_at) ? DATA.meta.generated_at.slice(0, 10) : todayISO();
    var weekStart = startOfWeekISO(day);
    var newCount = DATA.items.filter(function (it) {
      return it.published_at >= weekStart && it.published_at <= day;
    }).length;

    var nearest = sortSchedules(DATA.schedules || []).future[0];
    var parts = [];
    if (nearest) {
      parts.push(ddayLabel(dday(nearest.effective_date)) + " " + displayScheduleTitle(nearest.title));
    }
    parts.push("이번 주 신규 " + newCount + "건");

    textEl.textContent = parts.join(" · ");
    el.hidden = false;
  }

  // ── 초기화 ───────────────────────────────────────────────────────────
  function init() {
    wireNavScroll();
    loadData()
      .then(function (data) {
        DATA = data;
        (DATA.categories || []).forEach(function (c) { CAT_META[c.key] = c; });

        stateFromURL();
        refreshDateInputs();
        buildDoctypeMenu();
        updateDoctypeSummary();
        document.getElementById("sortSelect").value = state.sort;

        wireFilterBar();
        wireSearch();
        setQuery(state.q);  // URL에 ?q=가 있었으면 입력창에 반영
        wireViews();
        renderMeta();
        renderHeaderHighlight();
        renderCalendar();
        renderFullScheduleList();
        renderCurrentStandards();
        applyAndRender();
        switchView(state.view);  // URL의 ?view= 반영 + 진입 화면 렌더(기본값 today, 캘린더 탭도 여기서 필요시 렌더)
      })
      .catch(function (err) {
        console.error("[policy-watch] 데이터 로드 완전 실패:", err);
        var msg = '<div class="error-state">데이터를 불러오지 못했습니다. 새로고침해 보시고, 계속되면 관리자에게 문의해 주세요.</div>';
        // 기본 진입 화면(최근 정책동향)이 스켈레톤에 멈춰있지 않도록 거기에도 표시한다.
        document.getElementById("todayTitle").textContent = "최근 정책동향";
        document.getElementById("todayOfficialGrid").innerHTML = msg;
        document.getElementById("todayNewsSection").hidden = true;
        document.getElementById("feed").innerHTML = msg;
        document.getElementById("resultCount").textContent = "총 0건";
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
