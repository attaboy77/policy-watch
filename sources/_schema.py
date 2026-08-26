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

# SPEC-ADDENDUM-2.md §2-1 doc_type 14종 열거값
DOC_TYPES = [
    "제·개정", "공개초안", "검토의견", "적용지침", "모범규준", "질의회신", "FAQ",
    "예시서식", "감사·검토기준", "해설·교육자료", "로드맵·일정", "보도자료",
    "결정례·판례", "기사",
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

_ITEM_SCHEMA = {
    "type": "object",
    "required": [
        "id", "category", "doc_type", "stage", "title", "summary", "impact",
        "published_at", "collected_at", "effective_date", "source",
        "trust_score", "keyword_score", "final_score", "matched_keywords",
        "urls", "law_meta",
    ],
    "properties": {
        "id": {"type": "string"},
        "category": {"enum": CATEGORY_KEYS},
        "doc_type": {"enum": DOC_TYPES},
        "stage": {"enum": STAGES},
        "title": {"type": "string", "minLength": 1},
        "summary": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 3},
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
    },
}

_SCHEDULE_SCHEMA = {
    "type": "object",
    "required": ["id", "category", "title", "effective_date", "status",
                 "importance", "description", "source", "urls"],
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
