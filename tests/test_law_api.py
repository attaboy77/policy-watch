# -*- coding: utf-8 -*-
"""sources/law_api.py 단위 테스트 (네트워크 모킹, 실제 요청 없음).

2026-09-08: law_api가 GitHub Actions에서 소스 타임아웃(60초)에 이틀 연속
걸린 사고 대응 — `fetch()`가 법령 하나마다 검색(search_law) + 상세조회
(law_detail) 총 25회 요청을 하던 걸, 시행일자는 검색 응답에서 바로 뽑고
상세조회(개정이유 목적)는 본법에만 하도록 줄였다(25회→14회). 여기서는
그 요청 절감 로직 자체를 검증한다 — 실제 XML 파싱(search_law/law_detail)은
이 어댑터에 기존에 단위테스트가 없었어서 이번에 같이 최소한으로 커버한다.

2026-10-01: 개정이유를 lawService.do(법령 전문) 대신 lsRvsDocInfoR.do(개정이유
단독 페이지)로 받고, 최근 30일 내 개정된 시행령/시행규칙도 받도록 바뀌어
TestFetchRevisionReasons/TestRevisionReasonPage로 교체했다.
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


class TestFetchRevisionReasons:
    """2026-10-01: 개정이유는 revision_reason()(lsRvsDocInfoR.do)으로 — 본법은 항상,
    시행령/시행규칙은 공포일 최근 30일 이내만, 45초 예산이 지나면 건너뛴다."""

    TODAY = "2026-10-01"

    def _mock_search(self, monkeypatch, matches_by_root: dict[str, list[tuple]]):
        def fake_search_law(root_name, *, oc=None, wanted=None):
            return [
                {"법령명한글": name, "법령ID": str(i), "법령일련번호": str(2000 + i),
                 "공포일자": promul, "공포번호": "1", "제개정구분명": "일부개정",
                 "소관부처명": "기획재정부", "시행일자": eff}
                for i, (name, promul, eff) in enumerate(matches_by_root[root_name])
            ]
        monkeypatch.setattr(law_api, "search_law", fake_search_law)

    def _fix_today(self, monkeypatch):
        class _DT(law_api.datetime):
            @classmethod
            def now(cls, tz=None):
                return law_api.datetime(2026, 10, 1, 7, 0, tzinfo=tz)
        monkeypatch.setattr(law_api, "datetime", _DT)

    def _record_reasons(self, monkeypatch):
        calls = []

        def fake_reason(lsi_seq, *, label=""):
            calls.append(label)
            return f"{label} 개정이유"
        monkeypatch.setattr(law_api, "revision_reason", fake_reason)
        return calls

    def test_root_always_and_recent_variants_only(self, monkeypatch):
        self._fix_today(monkeypatch)
        self._mock_search(monkeypatch, {
            "테스트법": [
                ("테스트법", "20251223", "20260101"),          # 본법: 오래돼도 받는다
                ("테스트법 시행령", "20260930", "20261001"),   # 1일 전: 받는다
                ("테스트법 시행규칙", "20260831", "20260901"), # 31일 전: 안 받는다
            ],
        })
        calls = self._record_reasons(monkeypatch)
        monkeypatch.setattr(time, "sleep", lambda s: None)

        items = law_api.fetch(law_names=["테스트법", "테스트법 시행령", "테스트법 시행규칙"])

        assert calls == ["테스트법", "테스트법 시행령"]
        by_title = {it["title"]: it for it in items}
        assert by_title["테스트법"]["revision_reason"] == "테스트법 개정이유"
        assert by_title["테스트법 시행령"]["revision_reason"] == "테스트법 시행령 개정이유"
        assert by_title["테스트법 시행규칙"]["revision_reason"] is None
        # 시행일자는 검색 응답 값 그대로.
        assert by_title["테스트법 시행규칙"]["effective_date"] == "2026-09-01"

    def test_lawservice_detail_is_no_longer_called(self, monkeypatch):
        """법령 전문(약 0.8MB)을 받는 law_detail()은 fetch()에서 쓰지 않는다."""
        self._fix_today(monkeypatch)
        self._mock_search(monkeypatch, {"테스트법": [("테스트법", "20260101", "20260701")]})
        self._record_reasons(monkeypatch)

        def boom(*a, **kw):
            raise AssertionError("law_detail()이 호출되면 안 된다")
        monkeypatch.setattr(law_api, "law_detail", boom)
        monkeypatch.setattr(time, "sleep", lambda s: None)

        assert len(law_api.fetch(law_names=["테스트법"])) == 1

    def test_variants_skipped_after_budget_but_root_still_fetched(self, monkeypatch):
        self._fix_today(monkeypatch)
        self._mock_search(monkeypatch, {
            "테스트법": [("테스트법", "20260930", "20261001"),
                         ("테스트법 시행령", "20260930", "20261001")],
        })
        calls = self._record_reasons(monkeypatch)
        monkeypatch.setattr(time, "sleep", lambda s: None)
        clock = iter([0.0] + [100.0] * 20)  # fetch_t0=0, 이후 전부 100초 경과로 보이게
        monkeypatch.setattr(time, "monotonic", lambda: next(clock))

        items = law_api.fetch(law_names=["테스트법", "테스트법 시행령"])

        assert calls == ["테스트법"]
        assert {it["title"]: it["revision_reason"] for it in items}["테스트법 시행령"] is None

    def test_sleep_count_matches_request_count(self, monkeypatch):
        """루트 2개 → 검색 2회 + 개정이유(본법 2 + 최근 시행령 1) 3회 = 요청 5회,
        sleep은 (루트간 1) + (개정이유 3) = 4회, 간격은 0.3초."""
        self._fix_today(monkeypatch)
        self._mock_search(monkeypatch, {
            "가법": [("가법", "20260101", "20260701"),
                     ("가법 시행령", "20260920", "20260920"),
                     ("가법 시행규칙", "20260101", "20260701")],
            "나법": [("나법", "20260101", "20260701")],
        })
        self._record_reasons(monkeypatch)
        sleeps = []
        monkeypatch.setattr(time, "sleep", lambda s: sleeps.append(s))

        law_api.fetch(law_names=["가법", "가법 시행령", "가법 시행규칙", "나법"])

        assert sleeps == [0.3] * 4

    def test_reason_failure_keeps_item(self, monkeypatch):
        self._fix_today(monkeypatch)
        self._mock_search(monkeypatch, {"테스트법": [("테스트법", "20260101", "20260701")]})

        def boom(lsi_seq, **kw):
            raise RuntimeError("lsRvsDocInfoR.do 실패")
        monkeypatch.setattr(law_api, "revision_reason", boom)
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


# lsRvsDocInfoR.do 실제 구조(2026-10-01 실측)를 줄인 것.
_RVS_HTML = """<html><body><div id="rvsConBody">
<p class="sbj02"> 【제정·개정이유】 <span><a href="#rvsTop"><img alt="제정·개정문보기"/></a></span></p>
<div class="pgroup"><div><ul><li style="width:auto;">[일부개정] <br />◇ 개정이유 <br />  법인세율을 1퍼센트씩 인상함. <br /><br />&lt;법제처 제공&gt;</li></ul></div></div>
<p class="sbj02"> 【제정·개정문】 </p>
<div class="pgroup"><p class="pcon01">국회에서 의결된 법인세법 일부개정법률을 이에 공포한다.</p></div>
</div></body></html>""".encode("utf-8")


class TestRevisionReasonPage:
    def test_extracts_reason_block_only(self, monkeypatch):
        seen = {}

        def fake_get_govt(url, *, params=None, **kw):
            seen.update(url=url, params=params, **kw)
            return _FakeResp(_RVS_HTML)
        monkeypatch.setattr(law_api._http, "get_govt", fake_get_govt)

        text = law_api.revision_reason("280349", label="법인세법")

        assert text == "[일부개정]\n◇ 개정이유\n법인세율을 1퍼센트씩 인상함.\n<법제처 제공>"
        assert "공포한다" not in text
        assert seen["url"] == law_api.REVISION_REASON_URL
        assert seen["params"] == {"lsiSeq": "280349"}
        assert seen["timeout"] == 10 and seen["retries"] == 1

    def test_returns_none_when_block_missing(self, monkeypatch):
        monkeypatch.setattr(law_api._http, "get_govt",
                            lambda *a, **kw: _FakeResp(b"<html><body>no</body></html>"))
        assert law_api.revision_reason("1") is None
