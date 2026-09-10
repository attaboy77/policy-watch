# -*- coding: utf-8 -*-
"""신규 항목 메일 알림 (GitHub Actions 수집 후 실행, 2026-09-02 사용자 요청).

실행: python -m sources.notify_mail

환경변수:
  CURRENT_DATA_JSON   현재 site/data.json 경로 (기본 "site/data.json")
  PREV_DATA_JSON      수집 실행 "전"에 백업해둔 이전 data.json 경로(신규 판정
                       기준점). 워크플로가 채워준다 — 없으면 신규 판정을 못 해
                       스킵(단, FORCE_MAIL이면 "신규 0건"으로 간주하고 진행).
  FORCE_MAIL          "true"면 신규가 없어도 발송(테스트용).
                       workflow_dispatch 입력값을 워크플로가 여기로 전달한다.
  GMAIL_USER          발신 Gmail 계정
  GMAIL_APP_PASSWORD  Gmail 앱 비밀번호
  MAIL_TO             수신자. 쉼표로 구분하면 여러 명(향후 확장 대비, 2026-09-02 지시)
  DASHBOARD_URL       메일 하단 링크(기본값 있음)

시크릿(GMAIL_USER/GMAIL_APP_PASSWORD/MAIL_TO) 중 하나라도 없으면 조용히 스킵
하고 종료한다 — 수집·배포 파이프라인은 메일 기능과 무관하게 계속 진행돼야
하므로, 이 모듈은 무슨 일이 있어도(발송 실패 포함) exit 0으로 끝난다
(main()이 전체를 try/except로 감쌈).

발송 조건(2026-09-02 사용자 지시 — 최초안은 "공식만"이었으나 뉴스도 매일
들어오는 게 아니라 도배 걱정 없다고 판단해 변경): 신규 공식(L1/L2) 항목이나
신규 언론(L3) 항목 중 하나라도 있으면 발송. 본문은 공식 기관 발표(제목+요약+
링크) 섹션이 위, 언론 보도(제목+링크만) 섹션이 아래 — 한쪽이 0건이면 그
섹션 자체를 뺀다. 제목의 "신규 N건"은 공식+언론 합계.

2026-09-10 사용자 지시 — 언론(L3) 발행일 필터: 구글 뉴스가 오래된 기사를
뒤늦게 결과에 포함시키는 경우가 있어(id가 처음 보이면 "신규"로 잡힘), 그게
메일에 나가는 걸 원치 않는다. 발행일이 어제·오늘(KST)이 아닌 언론 기사는
"신규"로 잡혀도 메일 본문에서 뺀다(`is_recent_enough_for_mail()` 참고) —
사이트(site/data.json, 대시보드)에는 그대로 실린다, 메일만 뺀다. **공식
(L1/L2) 항목은 면제** — 발표일이 지나도 챙겨야 하는 자료라 이 필터 대상이
아니다. 발행일을 파싱 못 하는 항목(형식이 깨졌거나 결측)은 보수적으로
포함시킨다 — `finalize_item()`이 이미 published_at 결측 시 collected_at
(오늘 날짜)으로 채워두므로 실제로는 이 경우가 사실상 없다(정책적 선택이라기
보다 안전장치).
"""
from __future__ import annotations

import html
import json
import os
import smtplib
from datetime import datetime, timezone, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from . import _sent_log
from ._config import CATEGORIES, SOURCE_LABELS

_KST = timezone(timedelta(hours=9))
DEFAULT_DASHBOARD_URL = "https://attaboy77.github.io/policy-watch/"


def _now_kst_date_str() -> str:
    return datetime.now(_KST).strftime("%Y.%m.%d")


def _now_kst_date_iso() -> str:
    """`_sent_log`가 쓰는 "YYYY-MM-DD" 형식(`_sent_log.DATE_FMT`)."""
    return datetime.now(_KST).strftime(_sent_log.DATE_FMT)


def load_items(path: str | None) -> list[dict]:
    """path가 없거나 못 읽으면 빈 리스트. 신규 판정에서 "이전이 통째로 없음"과
    "이전엔 0건이었음"을 구분해야 하므로, 호출부(main)가 파일 존재 여부를
    먼저 확인하고 이 함수는 안전한 로딩만 담당한다."""
    if not path or not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f).get("items", [])
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[notify_mail] {path} 읽기 실패: {exc}")
        return []


def load_meta(path: str | None) -> dict:
    """load_items()와 짝 — 같은 파일에서 meta만 뽑아온다(sources_failed 확인용)."""
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f).get("meta", {})
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[notify_mail] {path} 읽기 실패: {exc}")
        return {}


# 2026-09-08: 구글 뉴스 URL 복원 실패율이 이 값을 넘으면 메일 하단에 경고를
# 띄운다 — 사용자 지시("실패율이 높아지면 알 수 있게"). 시도 건수가 너무
# 적으면(예: 1건 중 1건 실패=100%) 노이즈가 크므로 최소 시도 건수도 같이 본다.
DECODE_FAIL_RATE_THRESHOLD = 0.3
DECODE_MIN_ATTEMPTS_FOR_WARNING = 5


def decode_notice_lines(meta: dict) -> list[str]:
    """meta.google_decode_stats를 보고 구글 뉴스 URL 복원 실패율이 높으면
    경고 한 줄을 만든다(임계값 미만이거나 시도 건수가 적으면 빈 리스트)."""
    stats = meta.get("google_decode_stats") or {}
    attempted = stats.get("attempted") or 0
    success = stats.get("success") or 0
    if attempted < DECODE_MIN_ATTEMPTS_FOR_WARNING:
        return []
    failed = attempted - success
    fail_rate = failed / attempted
    if fail_rate <= DECODE_FAIL_RATE_THRESHOLD:
        return []
    pct = round(fail_rate * 100)
    return [f"구글 뉴스 URL 복원 실패율 높음: {failed}/{attempted}건 실패({pct}%) — 원문 링크가 구글 리다이렉트 링크로 남아있을 수 있습니다."]


def fallback_notice_lines(meta: dict) -> list[str]:
    """2026-09-07: meta.sources_failed 중 전일 캐시로 대체된(used_fallback) 소스를
    "OO 수집 실패로 전일 데이터 사용" 한 줄씩으로 뽑는다. 연속 실패 중이면
    "(연속 N일째)"를 붙여 며칠째 안 고쳐지고 있는지 바로 보이게 한다."""
    lines = []
    for src in meta.get("sources_failed") or []:
        if not src.get("used_fallback"):
            continue
        label = SOURCE_LABELS.get(src.get("name"), src.get("name"))
        consecutive = src.get("consecutive_failures")
        streak = f" (연속 {consecutive}일째)" if consecutive else ""
        lines.append(f"{label} 수집 실패로 전일 데이터 사용{streak}")
    return lines


def find_new_items(prev_items: list[dict], current_items: list[dict],
                    sent_ids: set[str] | None = None) -> list[dict]:
    """id 기준 신규 항목만 추출.

    2026-09-10: `sent_ids`(과거에 실제로 메일 발송된 id, `_sent_log` 참고)가
    주어지면 그것도 함께 제외한다 — 구글 뉴스 RSS 결과가 매일 달라져 어제
    빠졌던 기사가 오늘 PREV_DATA_JSON 비교만으로는 "신규"로 재판정되는 걸
    막기 위함(PREV_DATA_JSON 비교를 대체하는 게 아니라 그 위에 얹는 추가
    필터 — 인자를 안 주면 기존 동작 그대로)."""
    prev_ids = {it.get("id") for it in prev_items}
    excluded_ids = prev_ids | (sent_ids or set())
    return [it for it in current_items if it.get("id") not in excluded_ids]


# 2026-09-10: "어제·오늘"의 "어제"만큼 며칠 전까지 허용할지. 0=오늘만,
# 1=어제·오늘(현재 사용자 요청 범위).
MAIL_NEWS_RECENCY_DAYS = 1


def _parse_date_str(s: str | None):
    """"YYYY-MM-DD"(또는 그 앞부분이 그 형식인) 문자열을 date로. 실패하면 None."""
    if not s:
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def is_recent_enough_for_mail(published_at: str | None, today: object | None = None) -> bool:
    """L3(언론) 항목의 발행일이 메일에 실을 만큼 최근(어제·오늘, KST)인지.

    날짜를 파싱 못 하면(결측/형식 오류) 보수적으로 True(포함) — 위 모듈
    docstring 참고. `today`는 테스트에서 기준일을 고정하기 위한 것으로,
    `datetime.date` 인스턴스를 받는다(생략하면 오늘 KST 날짜).
    """
    base = today or datetime.now(_KST).date()
    d = _parse_date_str(published_at)
    if d is None:
        return True
    return 0 <= (base - d).days <= MAIL_NEWS_RECENCY_DAYS


def is_official(item: dict) -> bool:
    """L1/L2(공식 소스) 여부. 뉴스 어댑터(google_news/naver_news)는 항상
    source.type == "news"로 표시된다(sources/main.py의 NEWS_SOURCES 참고,
    공식 어댑터는 전부 source.type == "official")."""
    return (item.get("source") or {}).get("type") == "official"


def group_by_category(items: list[dict]) -> list[tuple[str, list[dict]]]:
    """CATEGORIES 선언 순서(K-IFRS→세법→내부회계→ESG) 그대로 그룹핑하고, 그룹
    내에서는 최신순(published_at 내림차순)으로 정렬한다."""
    by_cat: dict[str, list[dict]] = {}
    for it in items:
        by_cat.setdefault(it.get("category"), []).append(it)
    ordered = []
    for key, meta in CATEGORIES.items():
        group_items = by_cat.get(key)
        if group_items:
            group_items = sorted(group_items, key=lambda x: x.get("published_at") or "", reverse=True)
            ordered.append((meta["label"], group_items))
    return ordered


def parse_recipients(mail_to: str | None) -> list[str]:
    """쉼표로 구분된 수신자 목록 → 공백 제거 + 빈 항목 제외 리스트."""
    if not mail_to:
        return []
    return [addr.strip() for addr in mail_to.split(",") if addr.strip()]


def _item_link(item: dict) -> str:
    urls = item.get("urls") or {}
    return urls.get("official") or urls.get("news") or ""


def build_subject(count: int, date_str: str | None = None) -> str:
    return f"[Policy Watch] 신규 {count}건 - {date_str or _now_kst_date_str()}"


_FOOTER_NOTE = "이 메일은 신규 항목이 있을 때만 발송됩니다."


def _sections(new_official: list[dict], new_news: list[dict]):
    """텍스트/HTML 두 렌더러가 같은 구조를 공유하도록 공통 추출.
    (섹션 제목, 카테고리별 그룹 목록, 요약 표시 여부) 튜플의 리스트.
    공식은 요약/실무영향까지, 언론은 제목+링크만(요약 없음, 2026-09-02 지시)."""
    out = []
    if new_official:
        out.append(("공식 기관 발표", group_by_category(new_official), True))
    if new_news:
        out.append(("언론 보도", group_by_category(new_news), False))
    return out


def build_body_text(new_official: list[dict], new_news: list[dict], dashboard_url: str, forced: bool = False,
                     fallback_lines: list[str] | None = None) -> str:
    """HTML을 못 읽는 클라이언트용 대체본. 링크를 제목에 걸 수 없으니 원문
    그대로("링크: URL") 표시한다 — HTML 버전과 달리 이건 정상(주 경로가 아님)."""
    lines = []
    if forced and not new_official and not new_news:
        lines.append("신규 항목이 없습니다. (workflow_dispatch의 force_mail 옵션으로 강제 발송된 테스트 메일입니다.)")
        lines.append("")
    for section_title, groups, show_summary in _sections(new_official, new_news):
        lines.append(f"■ {section_title}")
        lines.append("")
        for label, group_items in groups:
            lines.append(f"[{label}] ({len(group_items)}건)")
            for it in group_items:
                lines.append(f"- {it.get('title', '')}")
                if show_summary:
                    for s in (it.get("summary") or []):
                        lines.append(f"    · {s}")
                    if it.get("impact"):
                        lines.append(f"    실무영향: {it['impact']}")
                link = _item_link(it)
                if link:
                    lines.append(f"    링크: {link}")
            lines.append("")
    lines.append("──────────")
    for note in (fallback_lines or []):
        lines.append(f"⚠ {note}")
    if fallback_lines:
        lines.append("")
    lines.append(f"대시보드: {dashboard_url}")
    lines.append(_FOOTER_NOTE)
    return "\n".join(lines)


def _esc(s) -> str:
    return html.escape(str(s or ""))


# 2026-09-02 사용자 지시: 구글 뉴스 RSS 링크가 200자를 넘어가서 본문에 URL을
# 그대로 노출하면(위 build_body_text 방식) 메일이 안 읽힌다 — HTML로 보내
# 제목 자체에 링크를 걸고(<a href>), URL 문자열은 화면에 아예 안 보이게 한다.
# 아웃룩(Word 렌더링 엔진)에서 깨지지 않도록 <div>/<p>/<a>/<b>/<hr> 같은 기본
# 태그 + 인라인 style만 쓰고, flexbox/grid/외부 CSS/이미지는 쓰지 않는다.
def build_body_html(new_official: list[dict], new_news: list[dict], dashboard_url: str, forced: bool = False,
                     fallback_lines: list[str] | None = None) -> str:
    parts = ['<div style="font-family:Arial, Helvetica, sans-serif; font-size:14px; '
             'color:#111111; line-height:1.6;">']
    if forced and not new_official and not new_news:
        parts.append(
            '<p style="color:#b45309; margin:0 0 16px;">신규 항목이 없습니다. '
            '(workflow_dispatch의 force_mail 옵션으로 강제 발송된 테스트 메일입니다.)</p>'
        )
    for section_title, groups, show_summary in _sections(new_official, new_news):
        parts.append(f'<h2 style="font-size:16px; margin:20px 0 8px;">■ {_esc(section_title)}</h2>')
        for label, group_items in groups:
            parts.append(
                f'<h3 style="font-size:14px; color:#1e3a8a; margin:14px 0 6px;">'
                f'[{_esc(label)}] ({len(group_items)}건)</h3>'
            )
            for it in group_items:
                title = _esc(it.get("title", ""))
                link = _item_link(it)
                title_html = (
                    f'<a href="{_esc(link)}" style="color:#1a73e8; text-decoration:none; font-weight:bold;">{title}</a>'
                    if link else f'<b>{title}</b>'
                )
                parts.append(f'<p style="margin:0 0 10px;">{title_html}')
                if show_summary:
                    for s in (it.get("summary") or []):
                        parts.append(f'<br><span style="color:#555555;">· {_esc(s)}</span>')
                    if it.get("impact"):
                        parts.append(f'<br><span style="color:#333333;">실무영향: {_esc(it["impact"])}</span>')
                parts.append("</p>")
    parts.append('<hr style="border:none; border-top:1px solid #e2e8f0; margin:20px 0;">')
    for note in (fallback_lines or []):
        parts.append(f'<p style="color:#b45309; font-size:12px; margin:0 0 4px;">⚠ {_esc(note)}</p>')
    parts.append(
        f'<p style="margin:0 0 8px;"><a href="{_esc(dashboard_url)}" style="color:#1a73e8;">'
        f'대시보드: {_esc(dashboard_url)}</a></p>'
    )
    parts.append(f'<p style="color:#888888; font-size:12px; margin:0;">{_esc(_FOOTER_NOTE)}</p>')
    parts.append("</div>")
    return "".join(parts)


def send_via_gmail(subject: str, text_body: str, html_body: str, recipients: list[str],
                    user: str, app_password: str) -> None:
    # 2026-09-02 사용자 지시: 발신자 표시 이름을 "Policy Watch"로 — formataddr가
    # "Policy Watch <user@gmail.com>" 형식을 만들어준다(RFC 2822 준수, 특수문자
    # 이스케이프까지 알아서 처리).
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = formataddr(("Policy Watch", user))
    msg["To"] = ", ".join(recipients)
    # alternative 컨테이너는 "단순한 것부터" 순서로 붙인다 — 클라이언트가 이해하는
    # 마지막 파트를 렌더링하므로(RFC 2046), text/plain을 먼저·text/html을 나중에
    # 붙여야 HTML을 지원하는 클라이언트는 HTML을, 아니면 plain text를 보여준다.
    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(user, app_password)
        server.sendmail(user, recipients, msg.as_string())


def _run() -> None:
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD")
    mail_to = os.environ.get("MAIL_TO")
    if not (gmail_user and gmail_password and mail_to):
        print("[notify_mail] GMAIL_USER/GMAIL_APP_PASSWORD/MAIL_TO 중 미설정 항목이 있어 메일 단계를 건너뜁니다.")
        return
    recipients = parse_recipients(mail_to)
    if not recipients:
        print("[notify_mail] MAIL_TO에 유효한 수신자가 없어 건너뜁니다.")
        return

    forced = os.environ.get("FORCE_MAIL", "").strip().lower() == "true"
    current_path = os.environ.get("CURRENT_DATA_JSON", "site/data.json")
    prev_path = os.environ.get("PREV_DATA_JSON")
    sent_log_path = os.environ.get("SENT_LOG_PATH", _sent_log.PATH)

    current_items = load_items(current_path)
    if not current_items and not forced:
        print(f"[notify_mail] {current_path}를 읽을 수 없어 건너뜁니다.")
        return

    # 2026-09-10: 90일 지난 항목을 정리한 상태를 먼저 저장해둔다 — 발송 여부와
    # 무관하게(신규가 없어 메일을 안 보내는 날에도) 이 파일은 계속 정리·유지돼야
    # 한다("매일 수집 결과와 무관하게 계속 쌓이게"라는 요구사항의 반대편:
    # 안 쌓이는 부분인 90일 정리도 매일 반영).
    sent_log = _sent_log.prune(_sent_log.load(sent_log_path))
    _sent_log.save(sent_log, sent_log_path)

    if prev_path and os.path.exists(prev_path):
        new_items = find_new_items(load_items(prev_path), current_items, sent_ids=set(sent_log))
    else:
        print("[notify_mail] 이전 data.json 백업이 없어 신규 판정을 못 합니다"
              + ("(강제 발송이라 신규 0건으로 진행)" if forced else " — 건너뜁니다."))
        if not forced:
            return
        new_items = []

    new_official = [it for it in new_items if is_official(it)]
    new_news = [it for it in new_items if not is_official(it)]

    # 2026-09-10: 언론(L3)만 발행일 어제·오늘 필터 — 공식(L1/L2)은 면제.
    # site/data.json(대시보드)엔 이미 반영돼 있으므로 여기서 빼도 대시보드는
    # 그대로다 — 메일 본문에서만 뺀다.
    recent_news = [it for it in new_news if is_recent_enough_for_mail(it.get("published_at"))]
    stale_count = len(new_news) - len(recent_news)
    if stale_count:
        print(f"[notify_mail] 발행일이 오래된 언론 기사 {stale_count}건 메일에서 제외")
    new_news = recent_news

    if not new_official and not new_news and not forced:
        print("[notify_mail] 신규 항목이 없어 메일을 보내지 않습니다.")
        return

    current_meta = load_meta(current_path)
    fallback_lines = fallback_notice_lines(current_meta) + decode_notice_lines(current_meta)

    dashboard_url = os.environ.get("DASHBOARD_URL", DEFAULT_DASHBOARD_URL)
    subject = build_subject(len(new_official) + len(new_news))
    text_body = build_body_text(new_official, new_news, dashboard_url, forced=forced, fallback_lines=fallback_lines)
    html_body = build_body_html(new_official, new_news, dashboard_url, forced=forced, fallback_lines=fallback_lines)

    send_via_gmail(subject, text_body, html_body, recipients, gmail_user, gmail_password)
    print(f"[notify_mail] 메일 발송 완료: 공식 {len(new_official)}건, 언론 {len(new_news)}건 → {len(recipients)}명")

    # 2026-09-10: 실제로 메일에 실린 id만 발송 이력에 남긴다(발송 자체가
    # 실패하면 이 아래는 실행되지 않으므로 안 보낸 id가 "보냄"으로 잘못
    # 기록될 일은 없다) — 다음 실행부터 find_new_items()가 이 id들을
    # 다시 신규로 잡지 않는다.
    sent_now = [it.get("id") for it in new_official + new_news if it.get("id")]
    if sent_now:
        _sent_log.record(sent_log, sent_now, _now_kst_date_iso())
        _sent_log.save(sent_log, sent_log_path)


def main() -> None:
    try:
        _run()
    except Exception as exc:  # noqa: BLE001 - 메일 발송 실패가 파이프라인을 막으면 안 됨
        print(f"[notify_mail] 처리 중 오류(무시하고 계속 진행): {exc}")


if __name__ == "__main__":
    main()
