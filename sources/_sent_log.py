# -*- coding: utf-8 -*-
"""메일 발송 이력 누적 기록 (2026-09-10 사용자 지시).

배경: `notify_mail.py`의 "신규" 판정은 지금까지 PREV_DATA_JSON(수집 실행
직전에 백업해둔 site/data.json)에 없던 id만 봤다. 그런데 구글 뉴스 RSS는
같은 검색어라도 매일 반환하는 결과 집합이 달라진다 — 어제는 응답에 있던
기사가 오늘은 안 잡혀서 site/data.json(과 그 백업인 PREV_DATA_JSON)에서
빠졌다가, 그다음 날 다시 잡히면 "PREV_DATA_JSON에 없던 id"라 신규로
오판된다(실측: "김현정 의원, 고의 분식 회사관계자의 과징금 상향하는 외감법
개정안 발의"/"국내 기업 83% 신외감법 도입 효과…" 2건이 2026-09-09·09-10
이틀 연속 발송됨).

이 모듈은 "한 번 메일로 실제 발송된 id는 그 이후 다시 목록에 들어와도
신규 취급하지 않는다"는, PREV_DATA_JSON과 무관하게 계속 누적되는 별도
기록을 관리한다. PREV_DATA_JSON 비교를 대체하는 게 아니라 그 위에 얹는
추가 필터다(prev 비교가 없으면 전부 신규로 보이는 최초 실행 등의 기존
동작은 그대로 둔다).

data/sent_log.json : {id: "YYYY-MM-DD"}  (그 id가 마지막으로 발송된 날짜)

**git 추적 대상**(crawl.yml의 "변경사항 커밋" 단계 git add 목록에 포함돼야
함) — GitHub Actions는 매 실행 새 VM이라, 이 파일이 커밋돼 있지 않으면
다음 실행이 어제까지 보낸 이력을 알 방법이 없어(`data/source_cache.json`/
`data/source_health.json`과 같은 이유, `_source_health.py` 참고) 매번
초기화된 것처럼 동작한다.

90일이 지난 id는 `prune()`으로 정리한다 — 발송 이력은 계속 쌓이기만 하면
파일이 무한정 커지므로(수집 대상 자체가 `COLLECT_WINDOW_DAYS`=90일 창이라
그보다 오래된 id는 어차피 다시 볼 일이 없다).
"""
from __future__ import annotations

import json
import os
from datetime import date, datetime, timedelta

PATH = "data/sent_log.json"
RETENTION_DAYS = 90
DATE_FMT = "%Y-%m-%d"


def load(path: str = PATH) -> dict[str, str]:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save(sent: dict[str, str], path: str = PATH) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sent, f, ensure_ascii=False, indent=2, sort_keys=True)


def record(sent: dict[str, str], ids: list[str], today: str) -> None:
    """오늘(`today`, "YYYY-MM-DD") 실제로 메일에 실린 id들을 기록한다(제자리
    수정). id가 없는(빈 문자열/None) 항목은 무시한다."""
    for item_id in ids:
        if item_id:
            sent[item_id] = today


def prune(sent: dict[str, str], today: date | None = None,
          retention_days: int = RETENTION_DAYS) -> dict[str, str]:
    """`retention_days`(기본 90일)보다 오래전에 발송된 id를 제거한 새 dict를
    반환한다. 날짜 형식이 깨진 항목은 삭제 대신 보존한다(파싱 실패로 이력을
    조용히 잃는 것보다 낫다 — `_load_tax_subjects()` 등과 같은 원칙)."""
    cutoff = (today or date.today()) - timedelta(days=retention_days)
    out: dict[str, str] = {}
    for item_id, sent_date in sent.items():
        try:
            d = datetime.strptime(sent_date, DATE_FMT).date()
        except (ValueError, TypeError):
            out[item_id] = sent_date
            continue
        if d >= cutoff:
            out[item_id] = sent_date
    return out
