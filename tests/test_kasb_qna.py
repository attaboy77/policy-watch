# -*- coding: utf-8 -*-
"""sources/official/kasb.py fetch_qna() — 질의회신 published_at = 공개일 (2026-10-01)."""
from types import SimpleNamespace

from sources._utils import make_id_exact
from sources.official import kasb

# 실제 allReplySummaryList.do 목록 구조(2026-10-01 실측)를 줄인 것 — 첨부 칸 안에
# 중첩 요소가 있고, 회신일은 <p class="board_date">, 공개일은 맨 끝 평문 <td>.
_HEAD = """
<table><thead><tr>
<th class="col_none">번호</th><th class="col_none">분류</th><th>제목</th>
<th class="col_none">첨부</th><th>회신일</th><th>공개일</th>
</tr></thead><tbody>
"""


def _row(seq, title, replied, disclosed):
    return f"""
<tr>
<td class="col_none">2187</td><td class="col_none">IFRS 해석위원회 논의 결과</td>
<td class="left"><a href="javascript:void(0);" onclick="javascript:fn_Detail('{seq}','016002');">{title}</a></td>
<td class="col_none"><div><table><tr><td>중첩</td></tr></table></div></td>
<td><p class="board_date">{replied}</p></td>
<td>{disclosed}</td>
</tr>"""


def _fetch(monkeypatch, html, today="2026-10-01"):
    monkeypatch.setattr(kasb, "_http", SimpleNamespace(get=lambda url, **kw: SimpleNamespace(text=html)))
    monkeypatch.setattr(kasb, "_now_kst_iso", lambda: f"{today}T08:00:00+09:00")
    return kasb.fetch_qna()


def test_published_at_uses_disclosed_date_and_keeps_both(monkeypatch):
    html = _HEAD + _row("40687", "성격별 비용 공시 요구사항의 적용범위", "2026-04-30", "2026-09-29") + "</tbody></table>"
    [it] = _fetch(monkeypatch, html)
    assert it["published_at"] == "2026-09-29"
    assert it["replied_at"] == "2026-04-30"
    assert it["disclosed_at"] == "2026-09-29"


def test_future_disclosed_date_is_clamped_to_collection_date(monkeypatch):
    # 실측: 9/29 아침 수집분이 페이지엔 공개일 9/30으로 표시됨.
    html = _HEAD + _row("40687", "성격별 비용", "2026-04-30", "2026-09-30") + "</tbody></table>"
    [it] = _fetch(monkeypatch, html, today="2026-09-29")
    assert it["published_at"] == "2026-09-29"
    assert it["disclosed_at"] == "2026-09-30"


def test_missing_disclosed_date_falls_back_to_replied_date(monkeypatch):
    html = _HEAD + _row("40687", "성격별 비용", "2026-04-30", "") + "</tbody></table>"
    [it] = _fetch(monkeypatch, html)
    assert it["published_at"] == "2026-04-30"
    assert it["disclosed_at"] is None


def test_id_does_not_depend_on_dates(monkeypatch):
    # 요약 캐시·메일 발송 이력이 id로 연결돼 있어 날짜 기준을 바꿔도 id는 그대로여야 한다.
    a = _fetch(monkeypatch, _HEAD + _row("40687", "t", "2026-04-30", "2026-09-29") + "</tbody></table>")[0]
    b = _fetch(monkeypatch, _HEAD + _row("40687", "t", "2026-04-30", "") + "</tbody></table>")[0]
    assert a["id"] == b["id"] == make_id_exact(f"{kasb.QNA_LIST_URL}#40687") == "0d5770fb95813c22"
