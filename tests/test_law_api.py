# -*- coding: utf-8 -*-
"""sources/law_api.py 단위 테스트 (네트워크 모킹, 실제 요청 없음).

2026-09-08: law_api가 GitHub Actions에서 소스 타임아웃(60초)에 이틀 연속
걸린 사고 대응 — `fetch()`가 법령 하나마다 검색(search_law) + 상세조회
(law_detail) 총 25회 요청을 하던 걸, 시행일자는 검색 응답에서 바로 뽑고
상세조회(개정이유 목적)는 본법에만 하도록 줄였다(25회→14회). 여기서는
그 요청 절감 로직 자체를 검증한다 — 실제 XML 파싱(search_law/law_detail)은
이 어댑터에 기존에 단위테스트가 없었어서 이번에 같이 최소한으로 커버한다.
"""
import time
import xml.etree.ElementTree as ET

import pytest

from sources import law_api


def _search_xml(*rows):
    """<law> 여러 개를 담은 lawSearch.do 응답 XML 생성.
    각 row: (법령명한글, 공포일자, 시행일자)."""
    laws = "".join(
        f"<law><법령명한글><![CDATA[{name}]]></법령명한글><법령ID>{i}</법령ID>"
        f"<법령일련번호>{1000 + i}</법령일련번호><공포일자>{promul}</공포일자>"
        f"<공포번호>1</공포번호><제개정구분명>일부개정</제개정구분명>"
        f"<소관부처명>기획재정부</소관부처명><시행일자>{eff}</시행일자></law>"
        for i, (name, promul, eff) in enumerate(rows)
    )
    return f'<?xml version="1.0" encoding="UTF-8"?><LawSearch>{laws}</LawSearch>'.encode()


def _detail_xml(reason: str = "테스트 개정이유", effective: str = "20260701") -> bytes:
    return (
        f'<?xml version="1.0" encoding="UTF-8"?><법령><기본정보>'
        f"<시행일자>{effective}</시행일자><공포일자>20260101</공포일자>"
        f"<제개정이유><제개정이유내용>{reason}</제개정이유내용></제개정이유>"
        f"</기본정보></법령>"
    ).encode()


class _FakeResp:
    def __init__(self, content: bytes):
        self.content = content


class TestSearchLawExtractsEffectiveDate:
    def test_effective_date_pulled_from_search_response(self, monkeypatch):
        """2026-09-08 핵심 변경 — <시행일자>가 검색 응답에서 바로 나와야 한다."""
        xml = _search_xml(("테스트법", "20260101", "20260701"))
        monkeypatch.setattr(law_api._http, "get_govt", lambda *a, **kw: _FakeResp(xml))

        matches = law_api.search_law("테스트법", oc="test", wanted={"테스트법"})

        assert len(matches) == 1
        assert matches[0]["시행일자"] == "20260701"


class TestFetchReducesDetailCalls:
    """25회→14회 절감의 핵심: law_detail()은 본법에만 호출돼야 한다."""

    def _mock_search(self, monkeypatch, matches_by_root: dict[str, list[tuple]]):
        def fake_search_law(root_name, *, oc=None, wanted=None):
            return [
                {"법령명한글": name, "법령ID": str(i), "법령일련번호": str(2000 + i),
                 "공포일자": promul, "공포번호": "1", "제개정구분명": "일부개정",
                 "소관부처명": "기획재정부", "시행일자": eff}
                for i, (name, promul, eff) in enumerate(matches_by_root[root_name])
            ]
        monkeypatch.setattr(law_api, "search_law", fake_search_law)

    def test_detail_called_only_for_root_law_not_variants(self, monkeypatch):
        self._mock_search(monkeypatch, {
            "테스트법": [
                ("테스트법", "20260101", "20260701"),
                ("테스트법 시행령", "20260102", "20260702"),
                ("테스트법 시행규칙", "20260103", "20260703"),
            ],
        })
        detail_calls = []

        def fake_law_detail(law_name, *, oc=None):
            detail_calls.append(law_name)
            return {"시행일자": "99990101", "제개정이유": "본법 개정이유"}

        monkeypatch.setattr(law_api, "law_detail", fake_law_detail)
        monkeypatch.setattr(time, "sleep", lambda s: None)

        items = law_api.fetch(law_names=["테스트법", "테스트법 시행령", "테스트법 시행규칙"])

        assert detail_calls == ["테스트법"]  # 본법만 상세 조회
        assert len(items) == 3
        by_title = {it["title"]: it for it in items}
        # 본법: law_detail()의 제개정이유가 붙는다(효과 확인용, 시행일자는
        # 검색 응답 값이 우선이라 detail의 더미값 "99990101"로 안 덮인다).
        assert by_title["테스트법"]["revision_reason"] == "본법 개정이유"
        assert by_title["테스트법"]["effective_date"] == "2026-07-01"
        # 시행령/시행규칙: 상세조회를 안 했으니 개정이유는 None, 시행일자는
        # 검색 응답에서 그대로 나와야 한다.
        assert by_title["테스트법 시행령"]["revision_reason"] is None
        assert by_title["테스트법 시행령"]["effective_date"] == "2026-07-02"
        assert by_title["테스트법 시행규칙"]["revision_reason"] is None
        assert by_title["테스트법 시행규칙"]["effective_date"] == "2026-07-03"

    def test_sleep_count_matches_reduced_request_count(self, monkeypatch):
        """루트 2개(각 3건/1건 매치) → search 2회 + detail(본법만) 2회 =
        sleep은 (루트간 1) + (본법 상세조회 2) = 3회여야 한다."""
        self._mock_search(monkeypatch, {
            "가법": [("가법", "20260101", "20260701"),
                     ("가법 시행령", "20260101", "20260701"),
                     ("가법 시행규칙", "20260101", "20260701")],
            "나법": [("나법", "20260101", "20260701")],
        })
        monkeypatch.setattr(law_api, "law_detail", lambda name, **kw: {})
        sleeps = []
        monkeypatch.setattr(time, "sleep", lambda s: sleeps.append(s))

        law_api.fetch(law_names=["가법", "가법 시행령", "가법 시행규칙", "나법"])

        assert len(sleeps) == 3

    def test_detail_failure_falls_back_to_search_response_effective_date(self, monkeypatch):
        """본법 상세조회가 실패해도(예외) 시행일자는 검색 응답 값으로 채워져야 한다."""
        self._mock_search(monkeypatch, {"테스트법": [("테스트법", "20260101", "20260701")]})

        def boom(name, **kw):
            raise RuntimeError("lawService.do 실패")

        monkeypatch.setattr(law_api, "law_detail", boom)
        monkeypatch.setattr(time, "sleep", lambda s: None)

        items = law_api.fetch(law_names=["테스트법"])

        assert len(items) == 1
        assert items[0]["effective_date"] == "2026-07-01"
        assert items[0]["revision_reason"] is None

    def test_search_failure_skips_root_without_crashing(self, monkeypatch):
        def fake_search_law(root_name, *, oc=None, wanted=None):
            raise RuntimeError("lawSearch.do 실패")

        monkeypatch.setattr(law_api, "search_law", fake_search_law)
        monkeypatch.setattr(time, "sleep", lambda s: None)

        items = law_api.fetch(law_names=["테스트법"])

        assert items == []
