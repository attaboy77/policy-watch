# -*- coding: utf-8 -*-
"""메일 하루 신규 건수 상한 테스트 (2026-11-27).

신규가 MAIL_MAX_ITEMS(20)건을 넘으면 본문에는 지금 메일의 표시 순서(공식 → 언론, 섹션 안은
카테고리 순서 → 최신순)로 앞 20건만 싣고, 나머지는 "외 N건 — 대시보드에서 확인"으로 묶는다.
상한에 걸린 날은 맨 위에 "신규 N건 — 많아서 20건만 싣습니다" 한 줄.
"""
import json
from datetime import datetime

import pytest

from sources import notify_mail as nm
from sources._config import MAIL_MAX_ITEMS


def _official(i, cat="kifrs", day="2026-11-01"):
    return {"id": f"o{i}", "category": cat, "title": f"공식 {cat} {i}", "summary": ["요약"],
            "impact": "영향", "published_at": day, "source": {"type": "official"},
            "urls": {"official": f"https://o.example/{i}"}}


def _news(i, cat="kifrs", day=None):
    day = day or datetime.now(nm._KST).date().isoformat()
    return {"id": f"n{i}", "category": cat, "title": f"언론 {cat} {i}", "published_at": day,
            "source": {"type": "news", "name": "매체"}, "urls": {"news": f"https://n.example/{i}"}}


def test_default_limit_is_20():
    assert MAIL_MAX_ITEMS == 20


class TestCapMailItems:
    def test_under_limit_untouched(self):
        off, news = [_official(i) for i in range(5)], [_news(i) for i in range(15)]
        o, n, omitted = nm.cap_mail_items(off, news)
        assert (o, n, omitted) == (off, news, 0)

    def test_official_never_cut_by_news(self):
        off = [_official(i) for i in range(8)]
        news = [_news(i) for i in range(100)]
        o, n, omitted = nm.cap_mail_items(off, news)
        assert len(o) == 8 and len(n) == 12 and omitted == 88

    def test_follows_existing_display_order(self):
        # 카테고리 순서(K-IFRS → 세법 → 내부회계 → ESG), 그 안은 최신순 — 지금 메일 그대로.
        off = ([_official(f"esg{i}", "esg") for i in range(10)]
               + [_official(f"tax{i}", "tax", f"2026-11-{10 + i:02d}") for i in range(15)])
        o, n, omitted = nm.cap_mail_items(off, [])
        assert omitted == 5
        assert {it["category"] for it in o} == {"tax", "esg"}
        assert sum(it["category"] == "tax" for it in o) == 15   # 세법이 ESG보다 앞
        assert sum(it["category"] == "esg" for it in o) == 5

    def test_official_over_limit_drops_all_news(self):
        o, n, omitted = nm.cap_mail_items([_official(i) for i in range(25)], [_news(1)])
        assert len(o) == 20 and n == [] and omitted == 6

    def test_limit_is_configurable(self):
        o, n, omitted = nm.cap_mail_items([_official(i) for i in range(5)], [], limit=3)
        assert len(o) == 3 and omitted == 2


class TestBodyLines:
    def test_text_has_notice_on_top_and_omitted_line(self):
        body = nm.build_body_text([_official(1)], [], "https://dash.example", total=134, omitted=114)
        assert body.splitlines()[0] == "신규 134건 — 많아서 20건만 싣습니다"
        assert "외 114건 — 대시보드에서 확인" in body

    def test_html_has_notice_and_omitted_line(self):
        html = nm.build_body_html([_official(1)], [], "https://dash.example", total=134, omitted=114)
        assert html.index("신규 134건 — 많아서 20건만 싣습니다") < html.index("공식 kifrs 1")
        assert "외 114건 — 대시보드에서 확인" in html

    def test_no_lines_when_not_capped(self):
        body = nm.build_body_text([_official(1)], [], "https://dash.example")
        html = nm.build_body_html([_official(1)], [], "https://dash.example")
        for b in (body, html):
            assert "많아서" not in b and "대시보드에서 확인" not in b


class TestRunWithCap:
    @pytest.fixture(autouse=True)
    def _env(self, monkeypatch, tmp_path):
        monkeypatch.setenv("SENT_LOG_PATH", str(tmp_path / "sent_log.json"))
        monkeypatch.setenv("OPS_STATE_PATH", str(tmp_path / "ops_state.json"))
        monkeypatch.setenv("SOURCE_HEALTH_PATH", str(tmp_path / "source_health.json"))
        monkeypatch.delenv("MAIL_TO_ADMIN", raising=False)
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")

    def test_capped_mail_subject_total_body_20_sent_log_only_shown(self, monkeypatch, tmp_path):
        calls = []
        monkeypatch.setattr(nm, "send_via_gmail", lambda *a, **k: calls.append(a))
        items = [_official(i) for i in range(3)] + [_news(i) for i in range(30)]
        cur, prev = tmp_path / "cur.json", tmp_path / "prev.json"
        cur.write_text(json.dumps({"items": items}), encoding="utf-8")
        prev.write_text(json.dumps({"items": []}), encoding="utf-8")
        monkeypatch.setenv("CURRENT_DATA_JSON", str(cur))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        subject, text, html = calls[0][:3]
        assert "신규 33건" in subject
        assert text.startswith("신규 33건 — 많아서 20건만 싣습니다")
        assert "외 13건 — 대시보드에서 확인" in text
        assert all(f"공식 kifrs {i}" in text for i in range(3))
        sent = json.loads((tmp_path / "sent_log.json").read_text(encoding="utf-8"))
        assert len(sent) == 20 and {"o0", "o1", "o2"} <= set(sent)
