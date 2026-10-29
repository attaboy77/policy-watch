# -*- coding: utf-8 -*-
"""항목별 처음 수집일 기록 (2026-10-29 사용자 지시 — 10/20 보류했던 ②(b)).

배경: 메일은 "새로 잡힌 id"를, 화면 "최근 정책동향"은 "발행일이 기간 안"을 골라 서로
어긋났다 — 9/10~10/29 재현에서 메일로 간 공식 자료 36건 중 28건이 그날 최근 정책동향에
없었다(입법예고 첫 수집분, 법제처 법령, 질의회신 등 발행일이 수집일보다 한참 앞선 자료).
최근 정책동향은 공식 자료만 max(발행일, 처음 수집일)로 고른다(`site/app.js`). 언론은
발행일 그대로 — 구글이 뒤늦게 돌려준 옛 기사가 "최근"으로 올라오는 걸 막기 위해서다.

data/first_seen.json : {id: {"first": "YYYY-MM-DD", "last": "YYYY-MM-DD"}}
  first = 최종 data.json에 처음 들어간 날(KST), last = 마지막으로 들어간 날.

**git 추적 대상**(crawl.yml "변경사항 커밋" 단계의 git add 목록에 있어야 함) — Actions는
매 실행 새 VM이라 커밋돼 있지 않으면 매일 모든 항목이 "오늘 처음 본 것"이 된다
(`_sent_log.py`와 같은 이유).

정리는 **last 기준** `RETENTION_DAYS`일 — first 기준으로 지우면 상설 자료·연간 해설처럼
매일 다시 보이는 항목이 지워진 다음 날 "처음 본 것"으로 재등장한다.

초기값은 2026-10-29에 git 이력의 site/data.json 스냅샷(8/26~)에서 한 번 채웠다. 첫
스냅샷부터 있던 항목은 실제 처음 수집일을 몰라 first = 발행일로 뒀다(= 예전 화면 동작).
메일 신규 판정은 이 파일을 쓰지 않는다(PREV_DATA_JSON + `_sent_log` 그대로, 사용자 결정).
"""
from __future__ import annotations

import json
import os
from datetime import date, timedelta

PATH = "data/first_seen.json"
RETENTION_DAYS = 120


def load(path: str = PATH) -> dict[str, dict]:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save(store: dict[str, dict], path: str = PATH) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=1, sort_keys=True)


def update(store: dict[str, dict], ids: list[str], today: str) -> None:
    """오늘(`today`, "YYYY-MM-DD") data.json에 든 id들을 반영한다(제자리 수정).
    처음 보는 id는 first=today, 이미 있으면 last만 today로."""
    for item_id in ids:
        if not item_id:
            continue
        entry = store.get(item_id)
        if entry is None:
            store[item_id] = {"first": today, "last": today}
        else:
            entry["last"] = today


def prune(store: dict[str, dict], today: date, retention_days: int = RETENTION_DAYS) -> dict[str, dict]:
    """last가 `retention_days`일보다 오래된 id를 뺀 새 dict. 날짜가 깨진 항목은 보존한다."""
    cutoff = (today - timedelta(days=retention_days)).isoformat()
    out = {}
    for item_id, entry in store.items():
        last = entry.get("last") if isinstance(entry, dict) else None
        if isinstance(last, str) and len(last) == 10 and last < cutoff:
            continue
        out[item_id] = entry
    return out


def first_of(store: dict[str, dict], item_id: str) -> str | None:
    entry = store.get(item_id)
    return entry.get("first") if isinstance(entry, dict) else None
