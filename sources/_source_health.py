# -*- coding: utf-8 -*-
"""소스별 수집 상태 추적 + 실패 시 폴백용 캐시 (2026-09-07 신설).

배경: 2026-09-03 국세청(nts.go.kr) 접속 타임아웃으로 그 소스 항목 10건이 그날
데이터에서 통째로 사라졌다가 9/4에 사이트가 정상화되며 그대로 복귀 — 그런데
`notify_mail.py`의 "전일 대비 없던 id" 판정은 그 10건을 "신규"로 오판해
2017~2026년치 개정세법 해설이 한꺼번에 "신규 30건" 메일로 나가버렸다
(원인 진단은 docs/NEXT.md "2026-09-07 세션" 참고). 근본 원인은 `main.py`가
소스 하나가 실패하면 그 소스 항목을 그냥 0건으로 두고 넘어간다는 것 —
이 모듈은 그 대신 "마지막으로 성공했을 때의 결과"를 캐시해뒀다가 실패 시
그대로 재사용하게 한다(id가 그대로 유지되므로 notify_mail도 "신규"로
오판하지 않는다).

data/source_cache.json  : {source_name: [item, ...]}
    OFFICIAL_SOURCES는 fetch()가 돌려주는 모양 그대로, NEWS_SOURCES는
    normalize_news_item() 통과 후 모양 그대로 캐시한다 — 둘 다 main.py의
    build_data_json() 파이프라인에 그대로 다시 넣을 수 있는 모양이라
    실패 시 이 캐시를 이번 실행의 raw_items에 그대로 합치면 된다.
data/source_health.json : {source_name: {consecutive_failures, last_success_at,
                                          last_failure_at, last_failure_reason}}

**둘 다 git 추적 대상**(crawl.yml의 "변경사항 커밋" 단계 git add 목록에 포함
돼야 함) — GitHub Actions는 매 실행 새 VM이라, 이 파일들이 커밋돼 있지 않으면
"어제 성공했던 결과"를 다음 실행이 알 방법이 없다.
"""
from __future__ import annotations

import json
import os

CACHE_PATH = "data/source_cache.json"
HEALTH_PATH = "data/source_health.json"


def _load(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def _save(path: str, data: dict) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_cache() -> dict:
    return _load(CACHE_PATH)


def save_cache(cache: dict) -> None:
    _save(CACHE_PATH, cache)


def load_health() -> dict:
    return _load(HEALTH_PATH)


def save_health(health: dict) -> None:
    _save(HEALTH_PATH, health)


def record_success(health: dict, name: str, when_iso: str) -> None:
    """성공 기록 — 연속 실패 카운트를 0으로 리셋한다."""
    health[name] = {
        "consecutive_failures": 0,
        "last_success_at": when_iso,
        "last_failure_at": health.get(name, {}).get("last_failure_at"),
        "last_failure_reason": None,
    }


def record_failure(health: dict, name: str, reason: str, when_iso: str) -> int:
    """실패 기록 후 갱신된 연속 실패 횟수를 반환(며칠째 계속 실패 중인지 추적용)."""
    entry = health.setdefault(name, {"consecutive_failures": 0, "last_success_at": None})
    entry["consecutive_failures"] = entry.get("consecutive_failures", 0) + 1
    entry["last_failure_at"] = when_iso
    entry["last_failure_reason"] = reason
    return entry["consecutive_failures"]


class PartialFetch(Exception):
    """2026-10-14: 소스 안의 하위 수집 일부만 실패했음을 main.collect_all()에 알린다.

    배경: fss.fetch()는 B2(금감원 게시판)와 B3(k-icfr.org)를 합쳐 돌려주는데, B2가
    실패해도 B3가 살아 있으면 "fss 성공"으로 처리돼 전일 캐시 대체가 안 됐다.
    10/9~10/10 B2 항목 6건이 data.json에서 빠졌다가 10/11 복귀하면서 신규 메일로
    나갔다(docs/NEXT.md 2026-10-14 세션). 어댑터는 성공한 부분의 items와 실패한 부분
    {부분키: 사유}를 이 예외로 올리고, main은 실패한 부분만 캐시에서 `part_of(item)`로
    골라 채운다. 하위 수집이 전부 실패하면 어댑터는 이 예외 대신 일반 예외를 올린다
    (소스 단위 폴백)."""

    def __init__(self, items: list[dict], failed: dict[str, str], part_of):
        super().__init__(", ".join(f"{p}: {r}" for p, r in failed.items()))
        self.items = items
        self.failed = failed
        self.part_of = part_of
