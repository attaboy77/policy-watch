# -*- coding: utf-8 -*-
"""sources/main.py collect_all() 단위 테스트 (2026-09-07 신설).

배경: 국세청(nts.go.kr) 접속 타임아웃으로 그 소스 항목이 하루 통째로 사라졌다가
복귀하면서 notify_mail이 "신규 30건"으로 오판한 사고(docs/NEXT.md 2026-09-07
세션 참고) — collect_all()이 실패한 소스를 0건으로 두는 대신 캐시된 전일
데이터를 쓰는지, 연속 실패 횟수가 올바르게 늘어나는지 검증한다.

실제 네트워크 호출은 절대 하지 않는다 — OFFICIAL_SOURCES/NEWS_SOURCES를
가짜 fetch 함수로 통째로 교체하고, 캐시/헬스 파일 경로도 tmp_path로 돌린다.
"""
from sources import main, _source_health as sh


def _isolate_cache_health(monkeypatch, tmp_path):
    monkeypatch.setattr(sh, "CACHE_PATH", str(tmp_path / "source_cache.json"))
    monkeypatch.setattr(sh, "HEALTH_PATH", str(tmp_path / "source_health.json"))


class TestCollectAllOfficialFallback:
    def test_success_populates_cache(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", lambda: [{"id": "n1"}])])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        items, ok, failed = main.collect_all()
        assert items == [{"id": "n1"}]
        assert ok == ["nts"]
        assert failed == []
        assert sh.load_cache() == {"nts": [{"id": "n1"}]}

    def test_failure_with_no_prior_cache_yields_zero_items(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)

        def boom():
            raise RuntimeError("connect timeout")

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", boom)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        items, ok, failed = main.collect_all()
        assert items == []
        assert ok == []
        assert failed == [{"name": "nts", "reason": "connect timeout",
                            "consecutive_failures": 1, "used_fallback": False}]

    def test_failure_with_prior_cache_falls_back_to_it(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"nts": [{"id": "n1"}, {"id": "n2"}]})

        def boom():
            raise RuntimeError("connect timeout")

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", boom)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        items, ok, failed = main.collect_all()
        assert items == [{"id": "n1"}, {"id": "n2"}]
        assert ok == []
        assert failed == [{"name": "nts", "reason": "connect timeout",
                            "consecutive_failures": 1, "used_fallback": True, "fallback_count": 2}]

    def test_consecutive_failures_increment_across_runs(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"nts": [{"id": "n1"}]})

        def boom():
            raise RuntimeError("timeout")

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", boom)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        _, _, failed1 = main.collect_all()
        _, _, failed2 = main.collect_all()
        _, _, failed3 = main.collect_all()
        assert [f["consecutive_failures"] for f in (failed1[0], failed2[0], failed3[0])] == [1, 2, 3]

    def test_recovery_resets_consecutive_failures_and_refreshes_cache(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)

        def boom():
            raise RuntimeError("timeout")

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", boom)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        sh.save_cache({"nts": [{"id": "old"}]})
        main.collect_all()  # 1일째 실패, "old"로 폴백
        main.collect_all()  # 2일째 실패, 여전히 "old"로 폴백

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", lambda: [{"id": "fresh"}])])
        items, ok, failed = main.collect_all()  # 3일째 복구
        assert items == [{"id": "fresh"}]
        assert ok == ["nts"]
        assert failed == []
        assert sh.load_health()["nts"]["consecutive_failures"] == 0
        assert sh.load_cache()["nts"] == [{"id": "fresh"}]


class TestCollectAllNewsFallback:
    def test_empty_result_treated_as_failure_and_falls_back(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"google_news": [{"id": "g1", "category": "kifrs"}]})
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [])
        monkeypatch.setattr(main, "NEWS_SOURCES", [("google_news", lambda: {}, "news")])
        items, ok, failed = main.collect_all()
        assert items == [{"id": "g1", "category": "kifrs"}]
        assert ok == []
        assert failed[0]["name"] == "google_news"
        assert failed[0]["used_fallback"] is True
        assert failed[0]["fallback_count"] == 1

    def test_exception_falls_back_same_as_empty_result(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"google_news": [{"id": "g1", "category": "kifrs"}]})

        def boom():
            raise RuntimeError("rss down")

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [])
        monkeypatch.setattr(main, "NEWS_SOURCES", [("google_news", boom, "news")])
        items, ok, failed = main.collect_all()
        assert items == [{"id": "g1", "category": "kifrs"}]
        assert failed[0]["reason"] == "rss down"
        assert failed[0]["used_fallback"] is True

    def test_success_caches_normalized_items_not_raw(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        raw = {"kifrs": [{
            "id": "g1", "category": "kifrs", "title": "제목", "url": "https://x.example/1",
            "published": None, "source_name": "예시신문", "source_domain": "x.example",
            "trust_tier": 4, "trust_score": 50, "keyword_score": 3, "matched_keywords": ["기준"],
            "is_noise": False,
        }]}
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [])
        monkeypatch.setattr(main, "NEWS_SOURCES", [("google_news", lambda: raw, "news")])
        items, ok, failed = main.collect_all()
        assert ok == ["google_news"]
        assert failed == []
        cached = sh.load_cache()["google_news"]
        assert cached[0]["id"] == "g1"
        assert cached[0]["urls"] == {"news": "https://x.example/1", "official": None}
