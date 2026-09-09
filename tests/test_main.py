# -*- coding: utf-8 -*-
"""sources/main.py collect_all() 단위 테스트 (2026-09-07 신설).

배경: 국세청(nts.go.kr) 접속 타임아웃으로 그 소스 항목이 하루 통째로 사라졌다가
복귀하면서 notify_mail이 "신규 30건"으로 오판한 사고(docs/NEXT.md 2026-09-07
세션 참고) — collect_all()이 실패한 소스를 0건으로 두는 대신 캐시된 전일
데이터를 쓰는지, 연속 실패 횟수가 올바르게 늘어나는지 검증한다.

실제 네트워크 호출은 절대 하지 않는다 — OFFICIAL_SOURCES/NEWS_SOURCES를
가짜 fetch 함수로 통째로 교체하고, 캐시/헬스 파일 경로도 tmp_path로 돌린다.
"""
import time

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

    def test_empty_result_treated_as_failure_and_falls_back(self, monkeypatch, tmp_path):
        """2026-09-09: 예외 없이 빈 리스트를 반환해도 성공으로 보지 않는다 —
        전엔 이 가드가 NEWS_SOURCES에만 있어서, 프록시 전환 직후 nts가 예외
        없이 0건을 반환한 게 "성공"으로 기록돼 캐시가 빈 값으로 덮어써졌고,
        다음에 nts가 진짜 성공하니 과거분 10건 전체가 "신규"로 오판된 사고가
        실측으로 확인됐다(docs/NEXT.md 참고)."""
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"nts": [{"id": "n1"}, {"id": "n2"}]})
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", lambda: [])])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        items, ok, failed = main.collect_all()
        assert items == [{"id": "n1"}, {"id": "n2"}]  # 전일 캐시로 대체
        assert ok == []
        assert failed[0]["name"] == "nts"
        assert failed[0]["reason"] == "결과 0건(응답 없음 또는 파싱 실패)"
        assert failed[0]["used_fallback"] is True
        assert failed[0]["fallback_count"] == 2
        # 캐시가 빈 값으로 덮어써지지 않고 기존 2건이 그대로 남아있어야 한다.
        assert sh.load_cache()["nts"] == [{"id": "n1"}, {"id": "n2"}]

    def test_empty_result_with_no_prior_cache_yields_zero_items(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", lambda: [])])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])
        items, ok, failed = main.collect_all()
        assert items == []
        assert ok == []
        assert failed[0]["name"] == "nts"
        assert failed[0]["used_fallback"] is False

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


class TestCollectAllSourceTimeout:
    """2026-09-08: GitHub Actions에서 kasb.or.kr이 응답을 안 줘서 크롤링 전체가
    12분+ 멈춘 사고 대응 — 소스 하나가 SOURCE_TIMEOUT_SECONDS를 넘기면
    실패로 간주하고 전일 캐시로 넘어가야 한다. 실제로 60초를 기다리지 않도록
    매 테스트에서 SOURCE_TIMEOUT_SECONDS를 아주 짧게 monkeypatch한다."""

    def test_official_source_exceeding_timeout_falls_back(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"nts": [{"id": "old"}]})
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_SECONDS", 0.05)

        def hangs():
            time.sleep(1)
            return [{"id": "too_late"}]

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", hangs)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])

        items, ok, failed = main.collect_all()

        assert items == [{"id": "old"}]  # 전일 캐시로 대체
        assert ok == []
        assert failed[0]["name"] == "nts"
        assert failed[0]["reason"] == "0.05초 초과(응답 없음)"
        assert failed[0]["used_fallback"] is True

    def test_news_source_exceeding_timeout_falls_back(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        sh.save_cache({"google_news": [{"id": "g1", "category": "kifrs"}]})
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_SECONDS", 0.05)

        def hangs():
            time.sleep(1)
            return {}

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [])
        monkeypatch.setattr(main, "NEWS_SOURCES", [("google_news", hangs, "news")])

        items, ok, failed = main.collect_all()

        assert items == [{"id": "g1", "category": "kifrs"}]
        assert failed[0]["reason"] == "0.05초 초과(응답 없음)"
        assert failed[0]["used_fallback"] is True

    def test_slow_source_does_not_block_later_sources(self, monkeypatch, tmp_path):
        """느린 소스 하나 때문에 뒤 소스들이 전부 밀리지 않는지 확인 — 실행
        시간 자체를 재서 '기다리지 않고 다음으로 넘어갔는지' 검증한다."""
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_SECONDS", 0.05)

        def hangs():
            time.sleep(1)
            return [{"id": "slow"}]

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [
            ("kasb", hangs),
            ("fss", lambda: [{"id": "fast"}]),
        ])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])

        t0 = time.time()
        items, ok, failed = main.collect_all()
        elapsed = time.time() - t0

        assert items == [{"id": "fast"}]
        assert ok == ["fss"]
        assert elapsed < 0.9  # hangs()의 1초 sleep을 기다리지 않고 넘어갔다

    def test_success_within_timeout_unaffected(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_SECONDS", 5)
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", lambda: [{"id": "n1"}])])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])

        items, ok, failed = main.collect_all()

        assert items == [{"id": "n1"}]
        assert ok == ["nts"]
        assert failed == []

    def test_per_source_timeout_override_applies(self, monkeypatch, tmp_path):
        """2026-09-09: law_api만 이틀 연속 60초 초과로 실패해 임시로 120초로
        올렸다 — SOURCE_TIMEOUT_OVERRIDES에 있는 소스는 SOURCE_TIMEOUT_SECONDS가
        아니라 그 값을 쓰는지 확인한다."""
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_SECONDS", 0.05)
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_OVERRIDES", {"law_api": 1})

        def slow_but_within_override():
            time.sleep(0.2)  # 기본 상한(0.05초)은 넘지만 override(1초)는 안 넘음
            return [{"id": "ok"}]

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("law_api", slow_but_within_override)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])

        items, ok, failed = main.collect_all()

        assert items == [{"id": "ok"}]
        assert ok == ["law_api"]
        assert failed == []

    def test_source_without_override_still_uses_default_timeout(self, monkeypatch, tmp_path):
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_SECONDS", 0.05)
        monkeypatch.setattr(main, "SOURCE_TIMEOUT_OVERRIDES", {"law_api": 1})

        def hangs():
            time.sleep(0.2)
            return [{"id": "too_late"}]

        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", hangs)])
        monkeypatch.setattr(main, "NEWS_SOURCES", [])

        items, ok, failed = main.collect_all()

        assert ok == []
        assert failed[0]["name"] == "nts"
        assert failed[0]["reason"] == "0.05초 초과(응답 없음)"

    def test_logs_which_source_is_being_attempted(self, monkeypatch, tmp_path, capsys):
        _isolate_cache_health(monkeypatch, tmp_path)
        monkeypatch.setattr(main, "OFFICIAL_SOURCES", [("nts", lambda: [{"id": "n1"}])])
        monkeypatch.setattr(main, "NEWS_SOURCES", [("google_news", lambda: {}, "news")])

        main.collect_all()

        out = capsys.readouterr().out
        assert "수집 시도: 국세청(nts)" in out
        assert "수집 시도: 구글 뉴스(google_news)" in out


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
