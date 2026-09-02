# -*- coding: utf-8 -*-
"""sources/notify_mail.py 단위 테스트 (2026-09-02 신설 — 신규 항목 메일 알림).

실제 SMTP 발송은 하지 않는다 — send_via_gmail을 monkeypatch로 대체하고
"호출됐는지/안 됐는지, 어떤 인자로 호출됐는지"만 검증한다.
"""
import json

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


class TestBuildBody:
    def test_official_only_has_official_section_not_news(self):
        body = nm.build_body([_item()], [], "https://dash.example")
        assert "공식 기관 발표" in body
        assert "언론 보도" not in body
        assert "https://dash.example" in body

    def test_news_only_has_news_section_not_official(self):
        news_item = _item(source={"type": "news"}, summary=[], impact=None,
                           urls={"official": None, "news": "https://news.example/x1"})
        body = nm.build_body([], [news_item], "https://dash.example")
        assert "언론 보도" in body
        assert "공식 기관 발표" not in body
        assert "https://news.example/x1" in body

    def test_news_section_excludes_summary_text(self):
        news_item = _item(source={"type": "news"}, summary=["이 요약은 보이면 안 됨"],
                           urls={"official": None, "news": "https://news.example/x1"})
        body = nm.build_body([], [news_item], "https://dash.example")
        assert "이 요약은 보이면 안 됨" not in body

    def test_both_sections_present_official_before_news(self):
        news_item = _item(id="n1", source={"type": "news"},
                           urls={"official": None, "news": "https://news.example/n1"})
        body = nm.build_body([_item()], [news_item], "https://dash.example")
        assert body.index("공식 기관 발표") < body.index("언론 보도")

    def test_forced_empty_mentions_test_send(self):
        body = nm.build_body([], [], "https://dash.example", forced=True)
        assert "테스트" in body
        assert "https://dash.example" in body

    def test_not_forced_empty_has_no_test_note_but_still_has_dashboard(self):
        body = nm.build_body([], [], "https://dash.example", forced=False)
        assert "https://dash.example" in body


class TestRunGating:
    """_run()이 각 상황에서 send_via_gmail을 호출하는지/안 하는지만 검증
    (실제 SMTP는 monkeypatch로 막음)."""

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
        (subject, body, recipients, user, password), _ = calls[0]
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
        news_item = _item(id="b", source={"type": "news"})
        self._write_data(current, [_item(id="a"), news_item])
        self._write_data(prev, [_item(id="a")])
        monkeypatch.setenv("CURRENT_DATA_JSON", str(current))
        monkeypatch.setenv("PREV_DATA_JSON", str(prev))
        nm._run()
        assert len(calls) == 1

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
