# -*- coding: utf-8 -*-
"""오케스트레이터 (entry point).

각 소스 수집기를 독립적으로 실행하고(한 소스 실패가 전체를 죽이지 않도록),
정제 파이프라인(중복 제거 → 계층별 상한/정렬 → 요약 → 스키마 확정)을 거쳐
site/data.json을 생성한다.

실행: python -m sources.main
"""
from __future__ import annotations

import concurrent.futures
import json
import os
import sys
from datetime import datetime, timezone, timedelta

from . import _excluded_log, _gap_log, _source_health
from ._config import CATEGORIES, COLLECT_WINDOW_DAYS, SOURCE_LABELS
from ._schema import validate as validate_schema
from ._summarize import summarize
from .current_standards import build_current_standards
from ._utils import (apply_applicability_gate, apply_category_caps,
                     apply_company_event_filter, apply_corporate_pr_filter,
                     apply_foreign_news_filter, apply_local_gov_petition_filter,
                     apply_regulatory_gate, attach_related_news, dedupe,
                     dedupe_similar_news, finalize_item, normalize_news_item)
from .schedules import build_schedules

from . import google_news, naver_news
from .official import kasb, fss, moef, nts, fsc
from . import policy_briefing, law_api

_KST = timezone(timedelta(hours=9))
DATA_JSON_PATH = "site/data.json"
SCHEMA_VERSION = "1.0"

# 2026-09-08: GitHub Actions에서 kasb.or.kr(국내 전용 사이트로 추정)가 응답을
# 안 줘서 크롤링 전체가 12분+ 멈춘 사고 발생 후 도입 — 소스 하나(fetch 함수
# 전체)가 이 시간(초) 안에 안 끝나면 실패로 간주하고 전일 캐시로 넘어간다.
# _http.py가 개별 HTTP 요청엔 이미 15초 타임아웃+재시도 3회를 걸어두지만
# (요청 1건당 최대 ~46.5초), 소스 하나가 그런 요청을 여러 번 순차로 하면
# (예: kasb.fetch()는 5개 하위 fetch를 차례로 호출) 합산 시간엔 상한이
# 없었다 — 이 상수가 그 상한 역할을 한다.
SOURCE_TIMEOUT_SECONDS = 60

# 2026-09-09: law_api만 이틀 연속(현재 3일째) 60초를 넘겨 실패 — 로컬 실측은
# 13.5초인데 Actions는 60초 초과라 격차 원인(프록시 왕복 지연/law_api만 유독
# 느림/재시도+백오프 중첩)이 아직 안 밝혀졌다. 원인을 Actions 로그로 확인할
# 때까지 임시로 law_api만 상한을 올려 데이터부터 살린다(사용자 지시 — "상한
# 올리기보다 요청을 줄이는 쪽"이 원칙이었지만 이번엔 원인 파악 전 응급 조치).
# 다른 소스는 기존 60초 그대로 — law_api.py의 요청당 로그(`_timed_get_govt`)로
# 실측 데이터가 모이면 원인 확인 후 이 예외를 다시 없애거나 구조적으로 고칠 것.
SOURCE_TIMEOUT_OVERRIDES = {"law_api": 120}


def _fetch_with_timeout(fetch_fn, *, timeout: float):
    """`fetch_fn()`을 별도 스레드에서 실행하고 `timeout`초 안에 못 끝내면
    `concurrent.futures.TimeoutError`를 올린다.

    파이썬은 실행 중인 스레드를 강제 종료할 수 없다 — 시간을 초과한 스레드는
    백그라운드에서 계속 돌다가 결국(각 HTTP 요청 자체의 타임아웃 덕에) 스스로
    끝난다. 다만 호출부(collect_all)는 이 함수가 예외를 던지는 즉시 그 결과를
    기다리지 않고 다음 소스로 넘어간다 — "소스 하나의 응답 지연이 전체
    크롤링을 막지 않는다"가 목적이라 완전한 강제 종료까지는 필요 없다.

    2026-09-09: 소스마다 다른 상한을 줄 수 있도록 `timeout`을 호출부(collect_all)가
    `SOURCE_TIMEOUT_OVERRIDES`를 참고해 명시적으로 넘기게 바꿨다(기본값 없음 —
    호출부가 매번 어떤 상한을 쓰는지 스스로 결정하게 강제).
    """
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(fetch_fn)
    try:
        return future.result(timeout=timeout)
    finally:
        executor.shutdown(wait=False, cancel_futures=True)

# (소스명, fetch 함수) — 이미 최종 스키마에 가까운 모양을 반환하는 어댑터들.
OFFICIAL_SOURCES = [
    ("kasb", kasb.fetch),
    ("fss", fss.fetch),
    ("moef", moef.fetch),
    ("nts", nts.fetch),
    ("fsc", fsc.fetch),
    ("policy_briefing", policy_briefing.fetch),
    ("law_api", law_api.fetch),
]
# (소스명, fetch_all 함수) — 카테고리별 raw item을 돌려주는 뉴스 어댑터. normalize 필요.
NEWS_SOURCES = [
    ("google_news", google_news.fetch_all, "news"),
    ("naver_news", naver_news.fetch_all, "news"),
]


def _now_kst_iso() -> str:
    return datetime.now(_KST).isoformat(timespec="seconds")


def _use_fallback(name: str, reason: str, cache: dict, health: dict, now_iso: str,
                   items: list[dict], sources_failed: list[dict]) -> None:
    """소스 실패 공통 처리(2026-09-07): 연속 실패 횟수 갱신 + 캐시에 어제 성공분이
    있으면 그대로 이번 실행 items에 합쳐 "그 소스만 0건"이 되는 걸 막는다.
    캐시가 없으면(이 소스가 아직 한 번도 성공한 적 없음) 어쩔 수 없이 0건 그대로."""
    consecutive = _source_health.record_failure(health, name, reason, now_iso)
    label = SOURCE_LABELS.get(name, name)
    fallback_items = cache.get(name) or []
    entry = {"name": name, "reason": reason, "consecutive_failures": consecutive}
    if fallback_items:
        items.extend(fallback_items)
        entry["used_fallback"] = True
        entry["fallback_count"] = len(fallback_items)
        print(f"[main] {label}({name}) 수집 실패({reason}) → 전일 캐시 {len(fallback_items)}건으로 대체 "
              f"(연속 {consecutive}일째 실패)")
    else:
        entry["used_fallback"] = False
        print(f"[main] {label}({name}) 수집 실패({reason}) → 캐시된 이전 데이터 없음, 0건 "
              f"(연속 {consecutive}일째 실패)")
    sources_failed.append(entry)


def collect_all() -> tuple[list[dict], list[str], list[dict]]:
    """모든 소스를 독립적으로 수집한다. 하나가 죽어도 나머지는 계속 진행(SPEC §9-4).

    2026-09-07: 소스가 실패하면 예전처럼 0건으로 두지 않고, 마지막으로 성공했을
    때 캐시해둔 결과(`data/source_cache.json`)를 그대로 쓴다 — id가 유지되므로
    다음 실행에서 그 소스가 다시 살아나도 notify_mail이 "신규"로 오판하지 않는다.

    2026-09-08: 소스마다 시작 직전에 "수집 시도: {라벨}" 로그를 남기고,
    `_fetch_with_timeout()`으로 감싸 `SOURCE_TIMEOUT_SECONDS`(60초) 안에
    못 끝내면 실패로 간주해 전일 캐시로 넘어간다 — GitHub Actions에서 국내
    전용 사이트(kasb.or.kr로 추정)가 응답을 안 줘서 크롤링 전체가 12분+
    멈춘 사고 대응.

    2026-09-09: OFFICIAL_SOURCES도 NEWS_SOURCES처럼 "예외 없이 반환했지만
    빈 리스트"도 실패로 본다(전에는 성공으로 처리돼 캐시가 빈 값으로
    덮어써졌다 — 다음에 그 소스가 진짜 성공하면 과거분 전체가 "신규"로
    오판되는 사고로 이어짐, nts 9/4·9/9 재발 실측으로 확인).
    """
    items: list[dict] = []
    sources_ok: list[str] = []
    sources_failed: list[dict] = []
    cache = _source_health.load_cache()
    health = _source_health.load_health()
    now_iso = _now_kst_iso()

    for name, fetch_fn in OFFICIAL_SOURCES:
        label = SOURCE_LABELS.get(name, name)
        timeout = SOURCE_TIMEOUT_OVERRIDES.get(name, SOURCE_TIMEOUT_SECONDS)
        print(f"[main] 수집 시도: {label}({name})")
        try:
            got = _fetch_with_timeout(fetch_fn, timeout=timeout)
            if got:
                items.extend(got)
                sources_ok.append(name)
                cache[name] = got
                _source_health.record_success(health, name, now_iso)
            else:
                # 2026-09-09: 예외 없이 빈 리스트가 와도 실패로 본다 — 그대로
                # "성공"으로 두면 cache[name]이 빈 값으로 덮어써져서, 다음에
                # 이 소스가 진짜로 성공할 때 과거분 전체가 "신규"로 오판된다
                # (nts 9/4·9/9 재발 사고, docs/NEXT.md 참고). NEWS_SOURCES는
                # 이미 이 가드가 있었는데 OFFICIAL_SOURCES엔 빠져 있었다.
                _use_fallback(name, "결과 0건(응답 없음 또는 파싱 실패)",
                              cache, health, now_iso, items, sources_failed)
        except concurrent.futures.TimeoutError:
            _use_fallback(name, f"{timeout}초 초과(응답 없음)",
                          cache, health, now_iso, items, sources_failed)
        except Exception as exc:  # noqa: BLE001 - 소스 단위 격리
            _use_fallback(name, str(exc), cache, health, now_iso, items, sources_failed)

    for name, fetch_all_fn, source_type in NEWS_SOURCES:
        label = SOURCE_LABELS.get(name, name)
        timeout = SOURCE_TIMEOUT_OVERRIDES.get(name, SOURCE_TIMEOUT_SECONDS)
        print(f"[main] 수집 시도: {label}({name})")
        try:
            by_category = _fetch_with_timeout(fetch_all_fn, timeout=timeout)
            normalized = [
                normalize_news_item(raw, source_type=source_type)
                for raw_items in by_category.values()
                for raw in raw_items
            ]
            if normalized:
                items.extend(normalized)
                sources_ok.append(name)
                cache[name] = normalized
                _source_health.record_success(health, name, now_iso)
            else:
                # 전부 빈 결과 — naver_news는 자격증명 없으면 조용히 빈 dict를 준다(graceful degradation).
                _use_fallback(name, "결과 0건(자격증명 미설정 또는 응답 없음)",
                              cache, health, now_iso, items, sources_failed)
        except concurrent.futures.TimeoutError:
            _use_fallback(name, f"{timeout}초 초과(응답 없음)",
                          cache, health, now_iso, items, sources_failed)
        except Exception as exc:  # noqa: BLE001
            _use_fallback(name, str(exc), cache, health, now_iso, items, sources_failed)

    _source_health.save_cache(cache)
    _source_health.save_health(health)
    return items, sources_ok, sources_failed


def _log_stage(stage: str, items: list[dict]) -> None:
    """ADDENDUM-5 §7: 단계별 카테고리별 건수 로그(과다 필터링 확인용)."""
    counts: dict[str, int] = {}
    for it in items:
        counts[it["category"]] = counts.get(it["category"], 0) + 1
    parts = ", ".join(f"{k} {v}" for k, v in counts.items())
    print(f"  [필터] {stage}: 합계 {len(items)}건 ({parts})")


def _record_excluded(excluded: list[dict]) -> None:
    """excluded_reason이 채워진 항목들을 _excluded_log에 기록(과다 필터링 검토용).
    apply_applicability_gate()와 2026-09-02 신규 필터 3종이 공유하는 헬퍼."""
    for it in excluded:
        _excluded_log.record(
            category=it.get("category", ""), title=it.get("title", ""),
            url=(it.get("urls") or {}).get("official") or (it.get("urls") or {}).get("news"),
            source=(it.get("source") or {}).get("name"),
            reason=it["excluded_reason"],
        )


def build_data_json(items: list[dict]) -> dict:
    """수집된 raw item 리스트 → site/data.json 전체 구조(메타 제외 조립은 main()에서).

    필터 순서: ADDENDUM-6 §1(적용 대상 게이트, 전 계층) → dedupe(정확일치) →
    ADDENDUM-5 §5(유사기사 병합) → §1(규제성 게이트) → ADDENDUM-7 §1(개별 기업
    소식 제외) → 2026-09-02 지자체 건의·민원 제외 → 해외 전용 뉴스 제외 →
    ADDENDUM-5 §3(홍보성 제외, ESG 개별기업 홍보 문구 포함) → 상한 적용.
    §1(적용 대상)을 맨 앞에 두는 건 §1-1 설계 그대로("카테고리 분류 직후,
    다른 모든 필터 이전")다. ADDENDUM-5 §1/§3을 §5 뒤로 옮긴 것은 2026-08-31
    사용자 지시(SPEC-ADDENDUM-5.md §7 원안은 §1→§3→...→§5 순서였음) — 그래야
    §1/§3에 걸려 사라질 기사도 §5 중복 병합의 후보에 먼저 포함된다.
    ADDENDUM-7 §1(개별 기업 소식)은 그 원안 §5 처리순서(규제성 게이트 다음,
    홍보성 제외 이전)대로 §1과 §3 사이에 끼워 넣는다. 2026-09-02 신규 필터
    2종(지자체 건의·해외 뉴스)도 같은 자리(§1 이후, §3 이전)에 끼워 넣는다 —
    개별 기업 소식 제외와 같은 성격("규제 자체가 아니라 프레이밍 문제")이라
    같은 처리 단계가 맞다.
    """
    items, excluded = apply_applicability_gate(items)  # ADDENDUM-6 §1, 전 계층
    _record_excluded(excluded)
    _log_stage("ADDENDUM-6 §1(적용 대상) 게이트 후", items)
    deduped = dedupe(items)
    deduped = dedupe_similar_news(deduped)  # ADDENDUM-5 §5: L3 유사 기사 병합
    _log_stage("§5 중복 제거 후", deduped)
    deduped = apply_regulatory_gate(deduped)  # ADDENDUM-5 §1
    _log_stage("§1 규제성 게이트 후", deduped)
    deduped = apply_company_event_filter(deduped)  # ADDENDUM-7 §1
    _log_stage("ADDENDUM-7 §1(개별 기업 소식) 제외 후", deduped)
    deduped, excluded = apply_local_gov_petition_filter(deduped)  # 2026-09-02
    _record_excluded(excluded)
    _log_stage("지자체 건의·민원 제외 후", deduped)
    deduped, excluded = apply_foreign_news_filter(deduped)  # 2026-09-02
    _record_excluded(excluded)
    _log_stage("해외 전용 뉴스 제외 후", deduped)
    deduped, excluded = apply_corporate_pr_filter(deduped)  # ADDENDUM-5 §3
    _record_excluded(excluded)
    _log_stage("§3 홍보성 제외 후", deduped)
    capped = apply_category_caps(deduped)
    # ADDENDUM-4 §4: 공식(L1/L2) 항목에 관련 L3 기사를 연결하고, 그렇게 붙은 L3는
    # 피드 중복 노출을 막기 위해 여기서 제외한다(layer 필드가 남아있는 동안 처리 —
    # finalize_item()이 layer를 지우므로 그 전에 해야 함).
    capped = attach_related_news(capped)

    finalized = []
    for it in capped:
        s = summarize(it)  # `_body`가 있으면 여기서 활용(finalize_item이 지우기 전에 먼저 호출)
        it["summary"], it["impact"] = s["summary"], s["impact"]
        it["ai_generated"] = s["ai_generated"]  # ADDENDUM-8 §5-1: 카드에 "(AI 생성)" 라벨 표시용
        finalized.append(finalize_item(it))

    # 2026-09-08: 위 필터를 전부 통과해 실제로 살아남은 항목만 대상으로 구글
    # 뉴스 리다이렉트 링크(news.google.com/rss/articles/...)를 실제 원문 URL로
    # 디코딩한다(파이프라인 초입에서 하면 나중에 걸러질 항목까지 구글에
    # 요청을 보내게 됨). 실패하면 항목을 버리지 않고 원래 링크를 그대로 둔다.
    google_news.resolve_finalized_urls(finalized)

    schedules = build_schedules(finalized)

    counts_by_category = {c: 0 for c in CATEGORIES}
    for it in finalized:
        counts_by_category[it["category"]] = counts_by_category.get(it["category"], 0) + 1

    categories = [
        {"key": key, "label": c["label"], "color": c["color"], "team": c["team"]}
        for key, c in CATEGORIES.items()
    ]

    # 2026-09-02: "현행 기준" 탭용 — 새로 크롤링하지 않고 위 finalized(최종
    # 확정 아이템)에서 바로 뽑는다(sources/current_standards.py 참고).
    current_standards = build_current_standards(finalized)

    return {
        "categories": categories,
        "items": finalized,
        "schedules": schedules,
        "current_standards": current_standards,
        "_counts_by_category": counts_by_category,  # main()에서 meta 조립용, 최종 출력엔 안 들어감
    }


def main() -> None:
    # 2026-09-02: Windows 콘솔(cp949 등)에서 "✓"/"—" 같은 유니코드 기호를
    # print()하면 UnicodeEncodeError로 죽는 문제 방지(실측 확인 — 로컬에서
    # 이 필터 작업을 검증하려고 직접 돌리다 발견). GitHub Actions(Ubuntu,
    # UTF-8 기본)엔 영향 없음 — reconfigure는 이미 UTF-8이면 사실상 no-op.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001 - 콘솔 재설정 실패해도 수집 자체는 계속
        pass
    print("=== Policy Watch 수집 시작 ===")
    _gap_log.clear()  # 이 프로세스 실행 동안 모인 gap만 반영(재실행 시 누적 방지)
    _excluded_log.clear()  # ADDENDUM-6 §1: 이번 실행에서 제외된 항목만 반영
    raw_items, sources_ok, sources_failed = collect_all()
    print(f"  원본 수집: {len(raw_items)}건 (성공 소스 {len(sources_ok)}개, 실패 {len(sources_failed)}개)")

    built = build_data_json(raw_items)  # 내부에서 google_news.resolve_finalized_urls() 호출
    counts_by_category = built.pop("_counts_by_category")
    # 2026-09-08: build_data_json()이 방금 채운 모듈 전역 통계를 읽어온다 —
    # collect_all()처럼 반환값 시그니처를 바꾸면 기존 테스트가 깨지므로 피한다.
    google_decode_stats = google_news.get_decode_stats()

    data = {
        "meta": {
            "schema_version": SCHEMA_VERSION,
            "generated_at": _now_kst_iso(),
            "window_days": COLLECT_WINDOW_DAYS,
            "total_items": len(built["items"]),
            "counts_by_category": counts_by_category,
            "sources_ok": sources_ok,
            "sources_failed": sources_failed,
            "google_decode_stats": google_decode_stats,
        },
        **built,
    }

    errors = validate_schema(data)
    if errors:
        print(f"  ⚠ 스키마 검증 실패 {len(errors)}건:")
        for e in errors[:20]:
            print(f"    - {e}")
    else:
        print("  ✓ 스키마 검증 통과")

    os.makedirs(os.path.dirname(DATA_JSON_PATH) or ".", exist_ok=True)
    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"  총 {len(built['items'])}건 → {DATA_JSON_PATH} 저장 완료")
    print(f"  카테고리별: {counts_by_category}")
    print(f"  일정: {len(built['schedules'])}건")

    _gap_log.flush()
    gap_count = len(_gap_log.gaps())
    if gap_count:
        print(f"  ⚠ 시행일 수동 검토 필요: {gap_count}건 → docs/EFFECTIVE_DATE_GAPS.md")

    _excluded_log.flush()
    excluded_count = len(_excluded_log.excluded())
    if excluded_count:
        print(f"  ⚠ 적용 대상 게이트 제외: {excluded_count}건 → docs/EXCLUDED_LOG.md (과다 필터링 여부 검토 필요)")

    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
