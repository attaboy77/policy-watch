# -*- coding: utf-8 -*-
"""sources/_config.py 소스 활성/비활성 설정 로더 테스트 (2026-09-09 신설).

배경: moef/fsc/policy_briefing 3개가 프록시 경유 시 0건을 반환하는데 캐시도
없어 폴백할 데가 없어서, 매 실행 로그와 메일에 실패 경고만 계속 쌓였다
(docs/NEXT.md 참고). 코드를 고치지 않고도 소스를 껐다 켰다 할 수 있도록
data/tax_subjects.yml과 같은 패턴(YAML + enabled 플래그)으로 뺐다.
"""
from sources import _config


def _write(tmp_path, content):
    p = tmp_path / "source_toggles.yml"
    p.write_text(content, encoding="utf-8")
    return str(p)


class TestLoadDisabledSources:
    def test_disabled_entries_are_collected_with_reason(self, tmp_path):
        path = _write(tmp_path, """
sources:
  - name: moef
    enabled: false
    reason: "테스트 사유"
  - name: nts
    enabled: true
""")
        assert _config._load_disabled_sources(path) == {"moef": "테스트 사유"}

    def test_enabled_entries_are_not_included(self, tmp_path):
        path = _write(tmp_path, """
sources:
  - name: nts
    enabled: true
""")
        assert _config._load_disabled_sources(path) == {}

    def test_omitting_enabled_defaults_to_true_and_is_not_disabled(self, tmp_path):
        path = _write(tmp_path, """
sources:
  - name: nts
""")
        assert _config._load_disabled_sources(path) == {}

    def test_missing_reason_defaults_to_empty_string(self, tmp_path):
        path = _write(tmp_path, """
sources:
  - name: moef
    enabled: false
""")
        assert _config._load_disabled_sources(path) == {"moef": ""}

    def test_missing_file_returns_empty_dict(self, tmp_path):
        assert _config._load_disabled_sources(str(tmp_path / "nope.yml")) == {}

    def test_malformed_yaml_returns_empty_dict(self, tmp_path):
        path = tmp_path / "bad.yml"
        path.write_text("sources: [this is not: valid: yaml:", encoding="utf-8")
        assert _config._load_disabled_sources(str(path)) == {}

    def test_real_config_file_disables_the_three_reported_sources(self):
        """실제 data/source_toggles.yml — 2026-09-09 사용자 지시로 moef/fsc/
        policy_briefing 3개를 껐다. 파일이 실수로 지워지거나 형식이 깨지면
        이 테스트가 바로 잡아낸다."""
        out = _config._load_disabled_sources()
        assert set(out) == {"moef", "fsc", "policy_briefing"}
