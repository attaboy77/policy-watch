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
  };

  var DATA = null;
  var CAT_META = {}; // key -> {label, color, team}
  var calViewDate = new Date(); calViewDate.setDate(1); // 사이드바 캘린더가 표시 중인 달(1일 고정)
  var calFullViewDate = new Date(); calFullViewDate.setDate(1); // 시행일 캘린더 탭의 표시 중인 달

  // ── URL 쿼리 동기화 ──────────────────────────────────────────────────
  function stateFromURL() {
    var p = new URLSearchParams(location.search);
    if (p.get("view") === "today" || p.get("view") === "all" || p.get("view") === "calendar") state.view = p.get("view");
    if (p.get("cat")) state.cats = p.get("cat").split(",").filter(Boolean);
    if (p.get("doctype")) state.doctypes = p.get("doctype").split(",").filter(Boolean);
    if (p.get("from")) state.from = p.get("from");
    if (p.get("to")) state.to = p.get("to");
    if (p.get("sort") === "latest" || p.get("sort") === "importance") state.sort = p.get("sort");
    if (p.get("static") === "1") state.staticOnly = true;
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

    document.getElementById("resultCount").innerHTML = "총 <b>" + filtered.length + "</b>건";

    if (!filtered.length) {
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

    // 정렬 기준이 '중요도순'이어도 날짜 그룹핑은 published_at 기준 내림차순 유지
    var groups = [];
    var byDate = {};
    filtered.forEach(function (it) {
      if (!byDate[it.published_at]) { byDate[it.published_at] = []; groups.push(it.published_at); }
      byDate[it.published_at].push(it);
    });
    groups.sort().reverse();

    var html = groups.map(function (dateKey) {
      var cards = byDate[dateKey].map(renderCard).join("");
      return '<div class="date-group">' +
        '<div class="date-group-header">' + esc(fmtDateHeader(dateKey)) + "</div>" +
        '<div class="card-list">' + cards + "</div></div>";
    }).join("");

    feedEl.innerHTML = html;
  }

  function renderCard(it) {
    var stage = displayStage(it);
    var stageBadge = stage
      ? '<span class="badge badge-stage" style="background:' + STAGE_COLOR[stage] + '">' + esc(stage) + "</span>"
      : "";
    // ADDENDUM-4 §2-3: 상설자료 회색 뱃지.
    var staticBadge = it.is_static ? '<span class="badge badge-static">상설자료</span>' : "";
    // ADDENDUM-7 §3 안 A: 해외기준(IASB/ISSB) 회색 뱃지.
    var foreignBadge = it.doc_type === "해외기준" ? '<span class="badge badge-foreign">해외기준</span>' : "";
    var officialTag = it.source && it.source.tier === 1 ? '<span class="badge-official">공식</span>' : "";
    // ADDENDUM-4 §3: "외 N건 보도" — 유사 기사가 병합된 경우.
    var dupTag = it.duplicate_count > 0 ? '<span class="dup-tag">외 ' + it.duplicate_count + '건 보도</span>' : "";
    // summary가 빈 배열이면(제목/출처를 반복할 뿐인 요약을 백엔드가 만들지 않기로
    // 했으므로, sources/_summarize.py 참고) 요약 영역 자체를 렌더링하지 않는다.
    var summaryHtml = (it.summary && it.summary.length)
      ? '<ul class="card-summary">' + it.summary.map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("") + "</ul>"
      : "";
    var impactHtml = it.impact
      ? '<div class="card-impact"><b>실무 영향:</b> ' + esc(it.impact) + "</div>"
      : "";
    var relatedHtml = renderRelatedNews(it.related_news);

    return (
      '<article class="card">' +
      '<div class="card-top">' +
      '<div class="card-badges">' + catBadge(it.category) +
      '<span class="badge badge-doctype">' + esc(it.doc_type) + "</span>" + stageBadge + staticBadge + foreignBadge + "</div>" +
      '<div class="card-source">출처: ' + esc(it.source ? it.source.name : "-") + officialTag + dupTag + "</div>" +
      "</div>" +
      '<h3 class="card-title">' + esc(it.title) + "</h3>" +
      summaryHtml +
      impactHtml +
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
            var color = (CAT_META[e.category] || {}).color || "#94a3b8";
            // 2026-08-31 사용자 지시: 법제처 시행일과 위원회 회의 일정이 섞이면
            // 헷갈린다 — 회의 일정은 속이 빈 고리(테두리만), 실제 시행일은
            // 꽉 찬 점으로 구분한다(카테고리 색은 둘 다 그대로 유지).
            var style = e.is_meeting
              ? "border:1.5px solid " + color + ";background:transparent;"
              : "background:" + color + ";";
            var title = e.is_meeting ? "위원회 회의 예정" : "시행일";
            return '<span class="cal-dot' + (e.is_meeting ? " cal-dot-meeting" : "") +
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

  function scheduleItemHtml(s) {
    var n = dday(s.effective_date);
    var isPast = s.effective_date < todayISO();
    var ddayClass = s.importance === "high" ? " is-important" : "";
    // 2026-08-31 사용자 지시: 법제처 시행일과 위원회 회의 일정이 캘린더에
    // 섞이면 헷갈린다 — 회의 일정 항목은 뱃지로 명시한다.
    var meetingBadge = s.is_meeting ? '<span class="badge badge-meeting">회의 예정</span>' : "";
    return (
      '<li class="sched-item' + (isPast ? " is-past" : "") + '" data-date="' + s.effective_date + '">' +
      '<div class="sched-top"><span class="dday-badge' + ddayClass + ' tnum">' + ddayLabel(n) + "</span>" + catBadge(s.category) + meetingBadge + "</div>" +
      '<div class="sched-item-title">' + esc(s.title) + "</div>" +
      '<div class="sched-date tnum">' + esc(fmtDot(s.effective_date)) + "</div>" +
      '<div class="sched-desc">' + esc(s.description) + "</div>" +
      '<div class="sched-actions">' + actionButtons(s.urls) + "</div>" +
      "</li>"
    );
  }

  // ── 시행 예정 일정 리스트 (사이드바, 당월 ~ 향후 3개월) ──────────────
  function renderScheduleList() {
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var winStart = today.getFullYear() + "-" + String(today.getMonth() + 1).padStart(2, "0") + "-01";
    var winEndDate = new Date(today.getFullYear(), today.getMonth() + 4, 0); // 향후 3개월 말일
    var winEnd = winEndDate.getFullYear() + "-" + String(winEndDate.getMonth() + 1).padStart(2, "0") + "-" + String(winEndDate.getDate()).padStart(2, "0");

    var list = DATA.schedules.filter(function (s) { return s.effective_date >= winStart && s.effective_date <= winEnd; });
    var html = list.map(scheduleItemHtml).join("");
    document.getElementById("schedList").innerHTML = html || '<li class="sched-desc">해당 기간 내 예정된 일정이 없습니다.</li>';
  }

  // ── 시행일 캘린더 탭: 전체 일정 리스트(기간 제한 없음) ────────────────
  function renderFullScheduleList() {
    var html = DATA.schedules.map(scheduleItemHtml).join("");
    document.getElementById("calFullSchedList").innerHTML = html || '<li class="sched-desc">등록된 일정이 없습니다.</li>';
    document.getElementById("calFullSub").textContent = "시행일순 전체 " + DATA.schedules.length + "건";
  }

  // ── 화면 전환: 오늘의 정책동향 / 전체 동향 / 시행일 캘린더 (ADDENDUM-4 §5-1) ──
  var VIEW_IDS = { today: "viewToday", all: "viewAll", calendar: "viewCalendar" };

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

  // ── 오늘의 정책동향 (ADDENDUM-4 §5) ─────────────────────────────────
  function renderTodayView() {
    // §5-2 "오늘"의 정의: 최근 수집 실행일(meta.generated_at)과 published_at이
    // 같은 날. 그 날 5건 미만이면 최근 3일로 확대(안내 문구 표시). is_static 전부 제외.
    var day = (DATA.meta && DATA.meta.generated_at) ? DATA.meta.generated_at.slice(0, 10) : todayISO();
    var pool = DATA.items.filter(function (it) {
      return !it.is_static && it.doc_type !== "논의자료" && it.doc_type !== "해외기준";
    });
    var todays = pool.filter(function (it) { return it.published_at === day; });
    var expanded = false;
    if (todays.length < 5) {
      var from3 = addDaysISO(day, -2);
      todays = pool.filter(function (it) { return it.published_at >= from3 && it.published_at <= day; });
      expanded = true;
    }

    var official = todays.filter(function (it) { return it.source && it.source.type === "official"; });
    var news = todays.filter(function (it) { return !(it.source && it.source.type === "official"); });
    // §5-5 정렬: 공식 그룹은 tier 오름차순 → final_score 내림차순, 보도 그룹은 final_score 내림차순.
    official.sort(function (a, b) { return (a.source.tier - b.source.tier) || (b.final_score - a.final_score); });
    news.sort(function (a, b) { return b.final_score - a.final_score; });

    document.getElementById("todayTitle").textContent = fmtDateHeader(day) + " 소식";
    document.getElementById("todayCounts").textContent = "공식 " + official.length + "건 · 보도 " + news.length + "건";
    document.getElementById("todayNotice").hidden = !expanded;

    var OFFICIAL_MAX = 12, NEWS_MAX = 12;
    document.getElementById("todayOfficialGrid").innerHTML = official.slice(0, OFFICIAL_MAX).map(renderTodayCard).join("");
    document.getElementById("todayNewsGrid").innerHTML = news.slice(0, NEWS_MAX).map(renderTodayCard).join("");
    document.getElementById("todayOfficialMore").hidden = official.length <= OFFICIAL_MAX;
    document.getElementById("todayNewsMore").hidden = news.length <= NEWS_MAX;
    document.getElementById("todayOfficialSection").hidden = official.length === 0;
    document.getElementById("todayNewsSection").hidden = news.length === 0;
    document.getElementById("todayEmpty").hidden = todays.length > 0;
  }

  function renderTodayCard(it) {
    var meta = CAT_META[it.category] || {};
    var color = meta.color || "#64748b";
    var isOfficial = it.source && it.source.type === "official";
    var borderColor = isOfficial ? color : hexToRgba(color, 0.4);  // §5-4: 보도는 40% 투명도
    var orgBadge = isOfficial
      ? '<span class="badge badge-org">공식기관</span>'
      : '<span class="badge badge-outlet">' + esc(it.source ? it.source.name : "") + "</span>";
    var summaryHtml = (it.summary && it.summary.length)
      ? '<ul class="today-card-summary">' + it.summary.slice(0, 2).map(function (s) { return "<li>" + esc(s) + "</li>"; }).join("") + "</ul>"
      : "";
    var impactHtml = it.impact ? '<div class="today-card-impact">' + esc(it.impact) + "</div>" : "";
    var relatedHtml = isOfficial ? renderRelatedNews(it.related_news) : "";
    var actionUrl = isOfficial ? (it.urls && it.urls.official) : (it.urls && it.urls.news);
    var actionLabel = isOfficial ? "원문 →" : "기사 보기 →";
    var actionHtml = actionUrl
      ? '<a class="btn btn-outline" href="' + esc(actionUrl) + '" target="_blank" rel="noopener">' + actionLabel + "</a>"
      : '<span class="btn btn-outline" aria-disabled="true" title="링크 없음">' + actionLabel + "</span>";

    return (
      '<article class="today-card' + (isOfficial ? "" : " is-news") + '" style="border-left-color:' + borderColor + '">' +
      '<div class="today-card-badges">' + catBadge(it.category) + orgBadge + "</div>" +
      '<h3 class="today-card-title">' + esc(it.title) + "</h3>" +
      summaryHtml + impactHtml + relatedHtml +
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

    ["todayOfficialMore", "todayNewsMore", "todayGoAllBtn"].forEach(function (id) {
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
        wireViews();
        renderMeta();
        renderCalendar();
        renderFullScheduleList();
        applyAndRender();
        switchView(state.view);  // URL의 ?view= 반영 + 진입 화면 렌더(기본값 today, 캘린더 탭도 여기서 필요시 렌더)
      })
      .catch(function (err) {
        console.error("[policy-watch] 데이터 로드 완전 실패:", err);
        var msg = '<div class="error-state">데이터를 불러오지 못했습니다. 새로고침해 보시고, 계속되면 관리자에게 문의해 주세요.</div>';
        // 기본 진입 화면(오늘의 정책동향)이 스켈레톤에 멈춰있지 않도록 거기에도 표시한다.
        document.getElementById("todayTitle").textContent = "오늘의 정책동향";
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
