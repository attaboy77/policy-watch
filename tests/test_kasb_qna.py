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


def test_link_is_detail_page_but_id_stays_list_anchor(monkeypatch):
    # 2026-10-20: 링크는 상세 페이지로, id는 예전 목록+#seq 그대로(요약 캐시·sent_log 연결 유지).
    html = _HEAD + _row("40687", "t", "2026-04-30", "2026-09-29") + "</tbody></table>"
    [it] = _fetch(monkeypatch, html)
    assert it["urls"]["official"] == (
        "https://www.kasb.or.kr/front/board/View016002.do"
        "?siteCd=002000000000000&seq=40687&ctgCd=016002&replySummary=Y")
    assert it["id"] == "0d5770fb95813c22"


def test_detail_url_follows_category_code(monkeypatch):
    html = (_HEAD + _row("40689", "제1118호 정착지원 TF 논의 내용(5차)", "2026-10-16", "")
            .replace("'016002'", "'016008'") + "</tbody></table>")
    [it] = _fetch(monkeypatch, html)
    assert "/View016008.do?" in it["urls"]["official"]
    assert "seq=40689&ctgCd=016008" in it["urls"]["official"]
    assert it["id"] == make_id_exact(f"{kasb.QNA_LIST_URL}#40689")


# ── 2026-10-20: 첨부 hwpx 발췌(attachment_text) ──────────────────────────────
import io
import zipfile

_NS = 'xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph"'


def _hwpx(paras):
    body = "".join(f"<hp:p><hp:run><hp:t>{p}</hp:t></hp:run></hp:p>" for p in paras)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("mimetype", "application/hwp+zip")
        z.writestr("Contents/section0.xml", f'<hs:sec xmlns:hs="x" {_NS}>{body}</hs:sec>')
    return buf.getvalue()


def _row_with_file(seq, name, file_no="-49993299"):
    return _row(seq, "제1118호 정착지원 TF 논의 내용(5차)", "2026-10-16", "").replace(
        "<td>중첩</td>",
        f"""<td><li class="down_hwp"><a href="javascript:void(0)" onclick="javascript:fileDownload('{file_no}','1'); return false;"><span>{name}</span></a></li></td>""")


def _fetch_with_files(monkeypatch, html, files):
    calls = []

    def get(url, **kw):
        if url == kasb.FILE_DOWNLOAD_URL:
            calls.append(kw["params"])
            content = files[kw["params"]["fileNo"]]
            if isinstance(content, Exception):
                raise content
            return SimpleNamespace(content=content)
        return SimpleNamespace(text=html)

    monkeypatch.setattr(kasb, "_http", SimpleNamespace(get=get))
    monkeypatch.setattr(kasb, "_now_kst_iso", lambda: "2026-10-20T08:00:00+09:00")
    return kasb.fetch_qna(), calls


def test_hwpx_attachment_text_is_extracted_from_list_row(monkeypatch):
    html = _HEAD + _row_with_file("40689", "5차회의_논의내용_FN.hwpx") + "</tbody></table>"
    files = {"-49993299": _hwpx(["/", "K-IFRS 제1118호 정착지원 TF", "순    서", "1. 교환사채",
                                 "안건.1", "교환사채 손익 범주", "1. 현황", "현황 설명",
                                 "3. 주요 논의내용", "□ 대부분의 위원은 을설을 지지함",
                                 "1. 관련 기준서 등", "B73 기준서 문단"])}
    [it], calls = _fetch_with_files(monkeypatch, html, files)
    assert calls == [{"fileNo": "-49993299", "fileSeq": "1"}]  # 상세 페이지는 안 연다
    assert it["attachment_text"] == ("K-IFRS 제1118호 정착지원 TF\n순    서\n1. 교환사채\n"
                                     "안건.1 교환사채 손익 범주\n3. 주요 논의내용\n□ 대부분의 위원은 을설을 지지함")


def test_hwp_and_pdf_attachments_are_skipped(monkeypatch):
    html = (_HEAD + _row_with_file("40678", "3차회의_논의내용_F.hwp", "-1")
            + _row_with_file("40688", "IAS 1.pdf", "-2") + "</tbody></table>")
    items, calls = _fetch_with_files(monkeypatch, html, {})
    assert calls == []
    assert [it["attachment_text"] for it in items] == [None, None]


def test_attachment_failure_keeps_item_without_text(monkeypatch):
    html = (_HEAD + _row_with_file("40689", "a.hwpx", "-1") + _row_with_file("40679", "b.hwpx", "-2")
            + "</tbody></table>")
    files = {"-1": RuntimeError("timeout"), "-2": b"not a zip"}
    items, _ = _fetch_with_files(monkeypatch, html, files)
    assert len(items) == 2
    assert [it["attachment_text"] for it in items] == [None, None]
    assert items[0]["id"] == make_id_exact(f"{kasb.QNA_LIST_URL}#40689")


def test_excerpt_splits_limit_across_agendas():
    paras = ["순서"]
    for n in (1, 2, 3):
        paras += [f"안건.{n}", f"안건{n} 제목", "3. 주요 논의내용", f"결론{n}", "가" * 1000]
    text = kasb._qna_excerpt(paras, limit=900)
    assert len(text) <= 900
    assert all(f"결론{n}" in text for n in (1, 2, 3))  # 뒤 안건 결론도 남는다


def test_excerpt_without_agendas_cuts_from_start():
    text = kasb._qna_excerpt(["앞부분", "나" * 100], limit=50)
    assert text.startswith("앞부분") and len(text) == 50 and text.endswith("…")


def test_excerpt_keeps_member_opinions_without_discussion_heading():
    # 5차 안건 5: "3. 주요 논의내용" 제목 없이 쟁점 뒤에 위원 의견이 바로 온다.
    paras = ["순서", "안건.5", "임대수익 범주", "2. 쟁점사항", "갑설 설명",
             "□ 다수의 위원들이 갑설을 지지하였으며", "1. 관련 기준서 등", "□ 기준서 문단"]
    text = kasb._qna_excerpt(paras)
    assert "□ 다수의 위원들이 갑설을 지지하였으며" in text
    assert "갑설 설명" not in text and "기준서 문단" not in text
