# -*- coding: utf-8 -*-
"""site/data.json JSON Schema (SPEC.md §4 + SPEC-ADDENDUM-2.md stage/doc_type
+ SPEC-ADDENDUM.md §4-3 attachments).

`python -m sources._schema site/data.json`로 단독 실행해 기존 파일을 검증할
수도 있다(SPEC.md §8 Phase 4 완료조건: "JSON Schema 검증 스크립트 포함").
"""
from __future__ import annotations

import json
import sys

from jsonschema import Draft202012Validator

# SPEC-ADDENDUM-2.md §2-1 doc_type 14종 열거값 + "논의자료"(2026-08-28 사용자
# 피드백 — TF·실무그룹 중간 산출물, `_utils.is_discussion_material()` 참고) +
# "해외기준"(SPEC-ADDENDUM-7.md §3 안 A — IASB/ISSB, `_utils.is_foreign_standard()`) +
# "자발적용"(2026-09-02 사용자 지시 — KASB sstnb_stndrList.do "자발적용가능" 탭.
# KSSB 공시기준서는 제정·공표는 됐지만 시행일이 아직 없어 강제 적용 대상이
# 아니다. 의무 적용 확정물인 "제·개정"과 구분하려고 별도 타입으로 뺐다 —
# stage는 compute_stage()의 기본값("참고")으로 자동 처리된다.)
DOC_TYPES = [
    "제·개정", "공개초안", "검토의견", "적용지침", "모범규준", "질의회신", "FAQ",
    "예시서식", "감사·검토기준", "해설·교육자료", "로드맵·일정", "보도자료",
    "결정례·판례", "기사", "논의자료", "해외기준", "자발적용",
]
# SPEC-ADDENDUM-2.md §2-2 stage. data.json에는 "확정"까지만 저장(시행예정/시행중은 프론트 계산)
STAGES = ["의견수렴", "확정", "참고"]
CATEGORY_KEYS = ["kifrs", "tax", "icfr", "esg"]

_SOURCE_SCHEMA = {
    "type": "object",
    "required": ["name", "domain", "tier", "type"],
    "properties": {
        "name": {"type": "string"},
        "domain": {"type": ["string", "null"]},
        "tier": {"type": "integer", "minimum": 1, "maximum": 5},
        "type": {"type": "string"},
    },
}

_URLS_SCHEMA = {
    "type": "object",
    "required": ["news", "official"],
    "properties": {
        "news": {"type": ["string", "null"]},
        "official": {"type": ["string", "null"]},
    },
}

_RELATED_NEWS_ITEM_SCHEMA = {
    "type": "object",
    "required": ["title", "source", "url", "published_at"],
    "properties": {
        "title": {"type": "string"},
        "source": {"type": "string"},
        "url": {"type": ["string", "null"]},
        "published_at": {"type": ["string", "null"]},
    },
}

_ITEM_SCHEMA = {
    "type": "object",
    "required": [
        "id", "category", "doc_type", "stage", "title", "summary", "impact",
        "published_at", "collected_at", "effective_date", "source",
        "trust_score", "keyword_score", "final_score", "matched_keywords",
        "urls", "law_meta",
        "is_static", "date_estimated", "duplicate_count", "duplicate_sources", "related_news",
        "is_meeting_schedule", "ai_generated", "revision_reason",
    ],
    "properties": {
        "id": {"type": "string"},
        "category": {"enum": CATEGORY_KEYS},
        "doc_type": {"enum": DOC_TYPES},
        "stage": {"enum": STAGES},
        "title": {"type": "string", "minLength": 1},
        # minItems 0: 본문도 없고 카드에 없는 추가 사실(첨부파일·시행일)도 없으면
        # 제목·출처 반복을 피하려고 빈 요약을 그대로 둔다(2026-08-28 피드백 반영,
        # 프론트는 빈 배열이면 요약 영역 자체를 렌더링하지 않는다).
        "summary": {"type": "array", "items": {"type": "string"}, "minItems": 0, "maxItems": 3},
        "impact": {"type": ["string", "null"]},
        "published_at": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"},
        "collected_at": {"type": "string"},
        "effective_date": {"type": ["string", "null"], "pattern": r"^\d{4}-\d{2}-\d{2}$|^$"},
        "source": _SOURCE_SCHEMA,
        "trust_score": {"type": "number"},
        "keyword_score": {"type": "number"},
        "final_score": {"type": "number"},
        "matched_keywords": {"type": "array", "items": {"type": "string"}},
        "urls": _URLS_SCHEMA,
        "law_meta": {"type": ["object", "null"]},
        "attachments": {"type": ["array", "null"]},
        # SPEC-ADDENDUM-4.md §2: 상시 비치 자료(게시판 자체가 상설 참고자료) 플래그.
        "is_static": {"type": "boolean"},
        # published_at을 제목에서 못 뽑아 collected_at으로 대체했으면 true.
        "date_estimated": {"type": "boolean"},
        # §3: 유사 기사 병합 결과. 0/[]이면 중복 없음.
        "duplicate_count": {"type": "integer", "minimum": 0},
        "duplicate_sources": {"type": "array", "items": {"type": "string"}},
        # §4: 공식 항목에 연결된 관련 L3 기사(최대 3건). 비어있으면 렌더 생략.
        "related_news": {"type": "array", "items": _RELATED_NEWS_ITEM_SCHEMA, "maxItems": 3},
        # effective_date가 "시행일"이 아니라 위원회 "회의 진행일자"면 true
        # (kasb.py fetch_schedule(), 2026-08-31 사용자 지시).
        "is_meeting_schedule": {"type": "boolean"},
        # ADDENDUM-8 §4/§5-1: summary/impact가 규칙 기반이 아니라
        # data/summary_cache.json(Claude Code가 직접 작성)에서 왔으면 true —
        # 프론트가 "(AI 생성)" 라벨을 붙인다.
        "ai_generated": {"type": "boolean"},
        # 2026-09-02: law_api.py가 lawService.do의 <제개정이유내용>을 그대로
        # 담는 필드(law.go.kr 항목만 채워짐, 그 외 소스는 null). 원문을 그대로
        # 카드에 노출하지 않는다 — "타법개정"이면 개정 대상 법과 전혀 무관한
        # 내용(예: 정부조직법 개편)이 들어올 수 있어(실측 확인: 부가가치세법
        # 사례) 기계적으로 자르지 않고, 요약 캐시 파이프라인(summary/impact)이
        # 이 필드를 원문 삼아 건별로 판단한 결과만 카드에 보인다.
        "revision_reason": {"type": ["string", "null"]},
    },
}

_SCHEDULE_SCHEMA = {
    "type": "object",
    "required": ["id", "category", "title", "effective_date", "status",
                 "importance", "description", "source", "urls", "is_meeting"],
    "properties": {
        "id": {"type": "string"},
        "category": {"enum": CATEGORY_KEYS},
        "title": {"type": "string"},
        "effective_date": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"},
        "status": {"type": "string"},
        "importance": {"enum": ["high", "medium", "low"]},
        "description": {"type": "string"},
        "source": _SOURCE_SCHEMA,
        "urls": _URLS_SCHEMA,
        # 법제처 시행일 등 실제 "시행일정"이면 false, 위원회 "회의 일정"이면
        # true(2026-08-31 사용자 지시 — 캘린더에서 둘을 구분 표시).
        "is_meeting": {"type": "boolean"},
    },
}

DATA_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["meta", "categories", "items", "schedules"],
    "properties": {
        "meta": {
            "type": "object",
            "required": ["schema_version", "generated_at", "window_days", "total_items",
                         "counts_by_category", "sources_ok", "sources_failed"],
            "properties": {
                "schema_version": {"type": "string"},
                "generated_at": {"type": "string"},
                "window_days": {"type": "integer"},
                "total_items": {"type": "integer"},
                "counts_by_category": {"type": "object"},
                "sources_ok": {"type": "array", "items": {"type": "string"}},
                "sources_failed": {"type": "array", "items": {"type": "object"}},
            },
        },
        "categories": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["key", "label", "color", "team"],
                "properties": {
                    "key": {"enum": CATEGORY_KEYS},
                    "label": {"type": "string"},
                    "color": {"type": "string"},
                    "team": {"type": "string"},
                },
            },
        },
        "items": {"type": "array", "items": _ITEM_SCHEMA},
        "schedules": {"type": "array", "items": _SCHEDULE_SCHEMA},
    },
}


def validate(data: dict) -> list[str]:
    """오류 메시지 리스트를 반환한다(비어있으면 스키마 100% 일치)."""
    validator = Draft202012Validator(DATA_SCHEMA)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    return [f"{'/'.join(str(p) for p in e.path) or '(root)'}: {e.message}" for e in errors]


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "site/data.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    errors = validate(data)
    if not errors:
        print(f"OK: {path}는 스키마와 100% 일치합니다.")
        sys.exit(0)
    print(f"FAIL: {path}에서 {len(errors)}건의 스키마 위반 발견:")
    for e in errors[:50]:
        print(f"  - {e}")
    sys.exit(1)
