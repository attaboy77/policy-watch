# -*- coding: utf-8 -*-
"""ESG 공시 제도화 로드맵(data/esg_roadmap.yml) 읽기.

KSSB 기준서(제1호/제2호 등, doc_type="자발적용") 자체에는 시행일이 없다 —
"누가 언제부터 의무 적용해야 하는가"는 금융위원회의 별개 정책 발표라
자동 크롤링하지 않고 이 파일에서 수동 관리한다(2026-09-02 사용자 지시,
data/esg_roadmap.yml 상단 주석 참고 — fsc.go.kr 보도자료엔 기준서 번호를
자동 연결할 단서가 없어서 수동 등록으로 결정).

`_summarize.py`가 doc_type="자발적용" 항목의 규칙 기반 summary/impact를
만들 때 이 모듈로 로드맵을 읽어 쓴다.
"""
from __future__ import annotations

import yaml

ESG_ROADMAP_PATH = "data/esg_roadmap.yml"


def load(path: str = ESG_ROADMAP_PATH) -> dict:
    """로드맵을 읽는다. 파일이 없거나 파싱 실패하면 빈 dict — 호출부가 그 경우
    로드맵 없이(규칙 기반 요약이 첨부파일 개수 등 기존 대체 문구로) 폴백한다.
    """
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}
    except Exception as exc:  # noqa: BLE001 - 파일 하나 깨져도 전체를 막지 않는다
        print(f"[esg_roadmap] {path} 파싱 실패({exc}) — 로드맵 없이 동작합니다.")
        return {}
