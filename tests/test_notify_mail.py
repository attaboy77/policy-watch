# -*- coding: utf-8 -*-
"""sources/notify_mail.py 단위 테스트 (2026-09-02 신설 — 신규 항목 메일 알림).

실제 SMTP 발송은 하지 않는다 — send_via_gmail을 monkeypatch로 대체하고
"호출됐는지/안 됐는지, 어떤 인자로 호출됐는지"만 검증한다.
"""
import json
from datetime import date, datetime

import pytest

from sources import notify_mail as nm


def _item(**overrides):
    base = {
        "id": "x1", "category": "kifrs", "title": "K-IFRS 제1118호 제정",
        "summary": ["요약1"], "impact": "실무영향 텍스트",
        "published_at": "2026-09-01",
        "source": {"type": "official"},
        "urls": {"official": "https://official.example/x1", "news": None},
    }
    base.update(overrides)
    return base


class TestLoadItems:
    def test_missing_path_returns_empty(self, tmp_path):
        assert nm.load_items(str(tmp_path / "nope.json")) == []

    def test_none_path_returns_empty(self):
        assert nm.load_items(None) == []

    def test_malformed_json_returns_empty_not_raise(self, tmp_path):
        p = tmp_path / "broken.json"
        p.write_text("{not valid", encoding="utf-8")
        assert nm.load_items(str(p)) == []

    def test_reads_items_field(self, tmp_path):
        p = tmp_path / "data.json"
        p.write_text(json.dumps({"items": [_item()]}), encoding="utf-8")
        out = nm.load_items(str(p))
        assert len(out) == 1
        assert out[0]["id"] == "x1"


class TestFindNewItems:
    def test_no_prev_all_new(self):
        current = [_item(id="a"), _item(id="b")]
        assert {it["id"] for it in nm.find_new_items([], current)} == {"a", "b"}

    def test_excludes_ids_present_in_prev(self):
        prev = [_item(id="a")]
        current = [_item(id="a"), _item(id="b")]
        out = nm.find_new_items(prev, current)
        assert [it["id"] for it in out] == ["b"]

    def test_no_new_items(self):
        prev = [_item(id="a")]
        current = [_item(id="a")]
        assert nm.find_new_items(prev, current) == []

    # 2026-09-10: 구글 뉴스 RSS 결과가 매일 달라져 prev에 없어도 이미 발송된
    # id는 다시 신규로 잡으면 안 된다.
    def test_excludes_ids_present_in_sent_ids(self):
        current = [_item(id="a"), _item(id="b")]
        out = nm.find_new_items([], current, sent_ids={"a"})
        assert [it["id"] for it in out] == ["b"]

    def test_sent_ids_none_behaves_like_before(self):
        current = [_item(id="a")]
        assert nm.find_new_items([], current, sent_ids=None) == current

    def test_sent_ids_and_prev_ids_combine(self):
        prev = [_item(id="a")]
        current = [_item(id="a"), _item(id="b"), _item(id="c")]
        out = nm.find_new_items(prev, current, sent_ids={"b"})
        assert [it["id"] for it in out] == ["c"]


class TestLoadMeta:
    def test_missing_path_returns_empty(self, tmp_path):
        assert nm.load_meta(str(tmp_path / "nope.json")) == {}

    def test_none_path_returns_empty(self):
        assert nm.load_meta(None) == {}

    def test_malformed_json_returns_empty_not_raise(self, tmp_path):
        p = tmp_path / "broken.json"
        p.write_text("{not valid", encoding="utf-8")
        assert nm.load_meta(str(p)) == {}

    def test_reads_meta_field(self, tmp_path):
        p = tmp_path / "data.json"
        p.write_text(json.dumps({"items": [], "meta": {"sources_ok": ["kasb"]}}), encoding="utf-8")
        assert nm.load_meta(str(p)) == {"sources_ok": ["kasb"]}

    def test_missing_meta_field_returns_empty(self, tmp_path):
        p = tmp_path / "data.json"
        p.write_text(json.dumps({"items": []}), encoding="utf-8")
        assert nm.load_meta(str(p)) == {}


class TestFallbackNoticeLines:
    def test_no_sources_failed_returns_empty(self):
        assert nm.fallback_notice_lines({}) == []

    def test_failed_without_fallback_ignored(self):
        meta = {"sources_failed": [{"name": "naver_news", "reason": "x", "used_fallback": False}]}
        assert nm.fallback_notice_lines(meta) == []

    def test_fallback_used_produces_line_with_known_label(self):
        meta = {"sources_failed": [
            {"name": "nts", "reason": "timeout", "used_fallback": True, "consecutive_failures": 1},
        ]}
        lines = nm.fallback_notice_lines(meta)
        assert lines == ["국세청 수집 실패로 전일 데이터 사용 (연속 1일째)"]

    def test_unknown_source_name_falls_back_to_raw_name(self):
        meta = {"sources_failed": [
            {"name": "mystery_source", "reason": "x", "used_fallback": True, "consecutive_failures": 3},
        ]}
        lines = nm.fallback_notice_lines(meta)
        assert lines == ["mystery_source 수집 실패로 전일 데이터 사용 (연속 3일째)"]

    def test_multiple_fallback_sources_each_get_a_line(self):
        meta = {"sources_failed": [
            {"name": "nts", "reason": "x", "used_fallback": True, "consecutive_failures": 1},
            {"name": "google_news", "reason": "y", "used_fallback": True, "consecutive_failures": 2},
        ]}
        assert nm.fallback_notice_lines(meta) == [
            "국세청 수집 실패로 전일 데이터 사용 (연속 1일째)",
            "구글 뉴스 수집 실패로 전일 데이터 사용 (연속 2일째)",
        ]


class TestDecodeNoticeLines:
    def test_no_stats_returns_empty(self):
        assert nm.decode_notice_lines({}) == []

    def test_below_min_attempts_returns_empty_even_if_all_failed(self):
        # 시도 4건(임계 5건 미만)은 전부 실패해도 경고 안 띄움 — 표본이 너무 작음.
        meta = {"google_decode_stats": {"attempted": 4, "success": 0}}
        assert nm.decode_notice_lines(meta) == []

    def test_low_fail_rate_returns_empty(self):
        meta = {"google_decode_stats": {"attempted": 40, "success": 38}}  # 5% 실패
        assert nm.decode_notice_lines(meta) == []

    def test_high_fail_rate_produces_warning_line(self):
        meta = {"google_decode_stats": {"attempted": 38, "success": 20}}  # 47% 실패
        lines = nm.decode_notice_lines(meta)
        assert len(lines) == 1
        assert "18/38건 실패(47%)" in lines[0]

    def test_exactly_at_threshold_returns_empty(self):
        meta = {"google_decode_stats": {"attempted": 10, "success": 7}}  # 정확히 30% 실패
        assert nm.decode_notice_lines(meta) == []


class TestIsRecentEnoughForMail:
    """2026-09-10 사용자 지시 — 언론(L3) 메일 발행일 필터(어제·오늘, KST)."""

    def test_today_is_recent(self):
        today = date(2026, 9, 11)
        assert nm.is_recent_enough_for_mail("2026-09-11", today=today) is True

    def test_yesterday_is_recent(self):
        today = date(2026, 9, 11)
        assert nm.is_recent_enough_for_mail("2026-09-10", today=today) is True

    def test_two_days_ago_is_not_recent(self):
        today = date(2026, 9, 11)
        assert nm.is_recent_enough_for_mail("2026-09-09", today=today) is False

    def test_far_past_is_not_recent(self):
        today = date(2026, 9, 11)
        assert nm.is_recent_enough_for_mail("2026-08-01", today=today) is False

    def test_missing_date_is_conservatively_included(self):
        today = date(2026, 9, 11)
        assert nm.is_recent_enough_for_mail(None, today=today) is True

    def test_malformed_date_is_conservatively_included(self):
        today = date(2026, 9, 11)
        assert nm.is_recent_enough_for_mail("not-a-date", today=today) is True

    def test_default_today_uses_kst_now(self):
        # today 인자를 안 주면 실제 오늘(KST) 기준 — 오늘 날짜 문자열은 항상 True.
        today_str = datetime.now(nm._KST).strftime("%Y-%m-%d")
        assert nm.is_recent_enough_for_mail(today_str) is True


class TestIsOfficial:
    def test_official_type_true(self):
        assert nm.is_official(_item(source={"type": "official"})) is True

    def test_news_type_false(self):
        assert nm.is_official(_item(source={"type": "news"})) is False

    def test_missing_source_false(self):
        assert nm.is_official({"id": "x"}) is False


class TestGroupByCategory:
    def test_orders_by_categories_declaration_order(self):
        items = [_item(id="e", category="esg"), _item(id="k", category="kifrs"),
                 _item(id="t", category="tax")]
        labels = [label for label, _ in nm.group_by_category(items)]
        assert labels == ["K-IFRS", "세법", "ESG"]

    def test_sorts_within_group_by_published_at_desc(self):
        items = [
            _item(id="old", category="kifrs", published_at="2026-08-01"),
            _item(id="new", category="kifrs", published_at="2026-09-01"),
        ]
        _, group_items = nm.group_by_category(items)[0]
        assert [it["id"] for it in group_items] == ["new", "old"]

    def test_empty_input_returns_empty(self):
        assert nm.group_by_category([]) == []


class TestParseRecipients:
    def test_single_address(self):
        assert nm.parse_recipients("a@x.com") == ["a@x.com"]

    def test_multiple_comma_separated_with_spaces(self):
        assert nm.parse_recipients("a@x.com, b@x.com ,c@x.com") == ["a@x.com", "b@x.com", "c@x.com"]

    def test_trailing_comma_and_blanks_ignored(self):
        assert nm.parse_recipients("a@x.com,,  ,b@x.com,") == ["a@x.com", "b@x.com"]

    def test_none_or_empty_returns_empty_list(self):
        assert nm.parse_recipients(None) == []
        assert nm.parse_recipients("") == []


class TestBuildSubject:
    def test_format(self):
        assert nm.build_subject(3, "2026.09.02") == "[Policy Watch] 신규 3건 - 2026.09.02"

    def test_zero_count(self):
        assert nm.build_subject(0, "2026.09.02") == "[Policy Watch] 신규 0건 - 2026.09.02"


class TestBuildBodyText:
    """plain text 대체본 — HTML을 못 읽는 클라이언트용. 여긴 원래대로 raw URL을
    "링크: ..." 형태로 보여준다(대체본이라 링크를 제목에 걸 방법이 없음)."""

    def test_official_only_has_official_section_not_news(self):
        body = nm.build_body_text([_item()], [], "https://dash.example")
        assert "공식 기관 발표" in body
        assert "언론 보도" not in body
        assert "https://dash.example" in body

    def test_news_only_has_news_section_not_official(self):
        news_item = _item(source={"type": "news"}, summary=[], impact=None,
                           urls={"official": None, "news": "https://news.example/x1"})
        body = nm.build_body_text([], [news_item], "https://dash.example")
        assert "언론 보도" in body
        assert "공식 기관 발표" not in body
        assert "https://news.example/x1" in body

    def test_news_section_excludes_summary_text(self):
        news_item = _item(source={"type": "news"}, summary=["이 요약은 보이면 안 됨"],
                           urls={"official": None, "news": "https://news.example/x1"})
        body = nm.build_body_text([], [news_item], "https://dash.example")
        assert "이 요약은 보이면 안 됨" not in body

    def test_both_sections_present_official_before_news(self):
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        body = nm.build_body_text([_item()], [news_item], "https://dash.example")
        assert body.index("공식 기관 발표") < body.index("언론 보도")

    def test_forced_empty_mentions_test_send(self):
        body = nm.build_body_text([], [], "https://dash.example", forced=True)
        assert "테스트" in body
        assert "https://dash.example" in body

    def test_not_forced_empty_has_no_test_note_but_still_has_dashboard(self):
        body = nm.build_body_text([], [], "https://dash.example", forced=False)
        assert "https://dash.example" in body

    def test_footer_note_present(self):
        body = nm.build_body_text([_item()], [], "https://dash.example")
        assert "이 메일은 신규 항목이 있을 때만 발송됩니다" in body

    def test_no_fallback_lines_by_default(self):
        body = nm.build_body_text([_item()], [], "https://dash.example")
        assert "전일 데이터 사용" not in body

    def test_fallback_lines_appear_before_dashboard(self):
        body = nm.build_body_text([_item()], [], "https://dash.example",
                                   fallback_lines=["국세청 수집 실패로 전일 데이터 사용 (연속 1일째)"])
        assert "국세청 수집 실패로 전일 데이터 사용 (연속 1일째)" in body
        assert body.index("전일 데이터 사용") < body.index("https://dash.example")


class TestBuildBodyHtml:
    """HTML 버전 — 2026-09-02 지시: URL을 그대로 노출하지 않고 제목 자체에
    링크를 건다(구글 뉴스 RSS 링크가 200자 넘어가는 문제 해결)."""

    def test_title_is_wrapped_in_anchor_with_href(self):
        it = _item(title="K-IFRS 제1118호 제정", urls={"official": "https://official.example/x1", "news": None})
        body = nm.build_body_html([it], [], "https://dash.example")
        assert '<a href="https://official.example/x1"' in body
        assert "K-IFRS 제1118호 제정</a>" in body

    def test_raw_url_not_shown_as_visible_link_label(self):
        # "링크: https://..." 같은 plain-text 전용 라벨이 HTML에는 없어야 한다
        # (제목 자체가 링크이므로 URL을 별도로 또 안 보여준다).
        it = _item(urls={"official": "https://official.example/x1", "news": None})
        body = nm.build_body_html([it], [], "https://dash.example")
        assert "링크:" not in body

    def test_news_only_has_news_section_not_official(self):
        news_item = _item(source={"type": "news"}, summary=[], impact=None,
                           urls={"official": None, "news": "https://news.example/x1"})
        body = nm.build_body_html([], [news_item], "https://dash.example")
        assert "언론 보도" in body
        assert "공식 기관 발표" not in body
        assert '<a href="https://news.example/x1"' in body

    def test_news_section_excludes_summary_text(self):
        news_item = _item(source={"type": "news"}, summary=["이 요약은 보이면 안 됨"],
                           urls={"official": None, "news": "https://news.example/x1"})
        body = nm.build_body_html([], [news_item], "https://dash.example")
        assert "이 요약은 보이면 안 됨" not in body

    def test_both_sections_present_official_before_news(self):
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        body = nm.build_body_html([_item()], [news_item], "https://dash.example")
        assert body.index("공식 기관 발표") < body.index("언론 보도")

    def test_forced_empty_mentions_test_send(self):
        body = nm.build_body_html([], [], "https://dash.example", forced=True)
        assert "테스트" in body

    def test_footer_note_present(self):
        body = nm.build_body_html([_item()], [], "https://dash.example")
        assert "이 메일은 신규 항목이 있을 때만 발송됩니다" in body

    def test_dashboard_link_is_anchor(self):
        body = nm.build_body_html([_item()], [], "https://dash.example")
        assert '<a href="https://dash.example"' in body

    def test_no_fallback_lines_by_default(self):
        body = nm.build_body_html([_item()], [], "https://dash.example")
        assert "전일 데이터 사용" not in body

    def test_fallback_lines_appear_before_dashboard(self):
        body = nm.build_body_html([_item()], [], "https://dash.example",
                                   fallback_lines=["국세청 수집 실패로 전일 데이터 사용 (연속 1일째)"])
        assert "국세청 수집 실패로 전일 데이터 사용 (연속 1일째)" in body
        assert body.index("전일 데이터 사용") < body.index("https://dash.example")

    def test_title_special_chars_are_escaped(self):
        it = _item(title="A & B <제정>", urls={"official": None, "news": None})
        body = nm.build_body_html([it], [], "https://dash.example")
        assert "A & B <제정>" not in body
        assert "A &amp; B &lt;제정&gt;" in body

    def test_missing_link_falls_back_to_bold_text_no_anchor(self):
        # 대시보드 링크(<a href>)는 항상 있으므로, 이 항목의 제목 자체가
        # 앵커 없이(<b>) 렌더링됐는지를 직접 확인한다.
        it = _item(title="링크없는제목", urls={"official": None, "news": None})
        body = nm.build_body_html([it], [], "https://dash.example")
        assert "<b>링크없는제목</b>" in body


class TestRunGating:
    """_run()이 각 상황에서 send_via_gmail을 호출하는지/안 하는지만 검증
    (실제 SMTP는 monkeypatch로 막음)."""

    @pytest.fixture(autouse=True)
    def _isolate_sent_log(self, monkeypatch, tmp_path):
        # 2026-09-10: _run()이 기본값(data/sent_log.json)을 쓰면 테스트가 실제
        # 저장소 파일을 건드린다 — 모든 테스트를 tmp_path로 격리.
        monkeypatch.setenv("SENT_LOG_PATH", str(tmp_path / "sent_log.json"))

    def _patch_send(self, monkeypatch):
        calls = []
        monkeypatch.setattr(nm, "send_via_gmail", lambda *a, **k: calls.append((a, k)))
        return calls

    def _write_data(self, path, items):
        path.write_text(json.dumps({"items": items}), encoding="utf-8")

    def test_skips_when_secrets_missing(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.delenv("GMAIL_USER", raising=False)
        monkeypatch.delenv("GMAIL_APP_PASSWORD", raising=False)
        monkeypatch.delenv("MAIL_TO", raising=False)
        nm._run()
        assert calls == []

    def test_skips_when_no_new_items_and_not_forced(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        self._write_data(current, [_item(id="a")])
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert calls == []

    def test_sends_when_new_official_item_exists(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com,b@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        self._write_data(current, [_item(id="a"), _item(id="b")])
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1
        (subject, text_body, html_body, recipients, user, password), _ = calls[0]
        assert "신규 1건" in subject
        assert recipients == ["a@x.com", "b@x.com"]

    def test_sends_when_new_news_only_item_exists(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        # 2026-09-10: 언론 발행일 필터가 생겨서, 고정된 과거 날짜(_item()
        # 기본값)로는 필터에 걸려 빠질 수 있다 — 이 테스트 목적(뉴스-only
        # 신규가 발송되는지)과 무관하므로 오늘 날짜로 맞춘다.
        news_item = _item(id="b", source={"type": "news"}, published_at=nm._now_kst_date_iso())
        self._write_data(current, [_item(id="a"), news_item])
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1

    # ── 언론(L3) 발행일 필터 연동 (2026-09-10) ──────────────────────────────
    def test_stale_news_excluded_but_official_not_affected(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        # is_recent_enough_for_mail을 "전부 오래됨"으로 고정 — 그런데도 공식
        # 항목이 살아남으면 이 필터가 공식(L1/L2)엔 아예 적용 안 된다는 뜻
        # (날짜 계산 자체는 TestIsRecentEnoughForMail이 이미 검증).
        monkeypatch.setattr(nm, "is_recent_enough_for_mail", lambda *a, **k: False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        official_item = _item(id="o1", source={"type": "official"})
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        self._write_data(current, [official_item, news_item])
        self._write_data(prev, [])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1
        (subject, text_body, *_rest), _ = calls[0]
        assert "신규 1건" in subject
        assert "공식 기관 발표" in text_body
        assert "언론 보도" not in text_body

    def test_only_stale_news_no_official_skips_send(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        monkeypatch.setattr(nm, "is_recent_enough_for_mail", lambda *a, **k: False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        self._write_data(current, [news_item])
        self._write_data(prev, [])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert calls == []

    def test_recent_news_included_when_filter_passes(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        monkeypatch.setattr(nm, "is_recent_enough_for_mail", lambda *a, **k: True)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        self._write_data(current, [news_item])
        self._write_data(prev, [])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1

    def test_stale_news_id_not_recorded_in_sent_log(self, monkeypatch, tmp_path):
        """메일에서 빠진 항목은 "발송"이 아니므로 발송 이력에도 안 남는다."""
        self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        monkeypatch.setattr(nm, "is_recent_enough_for_mail", lambda *a, **k: False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        official_item = _item(id="o1", source={"type": "official"})
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        self._write_data(current, [official_item, news_item])
        self._write_data(prev, [])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        sent_log_path = tmp_path / "sent_log.json"
        monkeypatch.setenv("SENT_LOG_PATH", str(sent_log_path))
        nm._run()
        recorded = json.loads(sent_log_path.read_text(encoding="utf-8"))
        assert set(recorded) == {"o1"}

    def test_force_mail_sends_even_with_no_new_items(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.setenv("FORCE_MAIL", "true")
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        self._write_data(current, [_item(id="a")])
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1
        (subject, *_rest), _ = calls[0]
        assert "신규 0건" in subject

    def test_force_mail_with_missing_prev_backup_still_sends(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.setenv("FORCE_MAIL", "true")
        current = tmp_path / "current.json"
        self._write_data(current, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(tmp_path / "nope.json"))
        nm._run()
        assert len(calls) == 1

    def test_missing_prev_backup_not_forced_skips(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        self._write_data(current, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(tmp_path / "nope.json"))
        nm._run()
        assert calls == []

    def test_fallback_notice_reaches_sent_body(self, monkeypatch, tmp_path):
        """2026-09-07: meta.sources_failed에 used_fallback=True가 있으면 실제로
        발송되는 본문(text/html 둘 다)에 안내 줄이 들어가는지 종단 검증."""
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        current.write_text(json.dumps({
            "items": [_item(id="a"), _item(id="b")],
            "meta": {"sources_failed": [
                {"name": "nts", "reason": "timeout", "used_fallback": True, "consecutive_failures": 2},
            ]},
        }), encoding="utf-8")
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1
        (_subject, text_body, html_body, *_rest), _ = calls[0]
        assert "국세청 수집 실패로 전일 데이터 사용 (연속 2일째)" in text_body
        assert "국세청 수집 실패로 전일 데이터 사용 (연속 2일째)" in html_body

    # ── 발송 이력(_sent_log) 연동 (2026-09-10) ───────────────────────────────
    def test_reappeared_item_already_sent_is_not_resent(self, monkeypatch, tmp_path):
        """구글 뉴스 RSS가 어제 빠졌다가 오늘 다시 돌려준 기사 재현: prev
        백업에는 없지만(그래서 순수 id-diff로는 신규) 과거에 이미 발송 이력이
        남아있으면 다시 보내지 않는다."""
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        self._write_data(current, [_item(id="a")])
        self._write_data(prev, [])  # "a"가 어제 응답에서 빠짐
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        sent_log_path = tmp_path / "sent_log.json"
        monkeypatch.setenv("SENT_LOG_PATH", str(sent_log_path))
        sent_log_path.write_text(json.dumps({"a": "2026-09-09"}), encoding="utf-8")
        nm._run()
        assert calls == []

    def test_sent_item_ids_recorded_after_successful_send(self, monkeypatch, tmp_path):
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        self._write_data(current, [_item(id="a"), _item(id="b")])
        self._write_data(prev, [])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        sent_log_path = tmp_path / "sent_log.json"
        monkeypatch.setenv("SENT_LOG_PATH", str(sent_log_path))
        nm._run()
        assert len(calls) == 1
        recorded = json.loads(sent_log_path.read_text(encoding="utf-8"))
        assert set(recorded) == {"a", "b"}

    def test_no_send_does_not_record_ids(self, monkeypatch, tmp_path):
        """신규가 없어 메일을 안 보내는 날엔 발송 이력에 아무것도 추가되지
        않는다(파일 자체는 정리 목적으로 계속 존재/갱신될 수 있음)."""
        calls = self._patch_send(monkeypatch)
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.delenv("FORCE_MAIL", raising=False)
        current = tmp_path / "current.json"
        prev = tmp_path / "prev.json"
        self._write_data(current, [_item(id="a")])
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        sent_log_path = tmp_path / "sent_log.json"
        monkeypatch.setenv("SENT_LOG_PATH", str(sent_log_path))
        nm._run()
        assert calls == []
        recorded = json.loads(sent_log_path.read_text(encoding="utf-8"))
        assert recorded == {}

    def test_send_failure_does_not_raise_via_main(self, monkeypatch, tmp_path):
        monkeypatch.setattr(nm, "send_via_gmail", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("smtp down")))
        monkeypatch.setenv("GMAIL_USER", "u@gmail.com")
        monkeypatch.setenv("GMAIL_APP_PASSWORD", "pw")
        monkeypatch.setenv("MAIL_TO", "a@x.com")
        monkeypatch.setenv("FORCE_MAIL", "true")
        current = tmp_path / "current.json"
        self._write_data(current, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(tmp_path / "nope.json"))
        nm.main()  # 예외가 안 올라오면 통과
