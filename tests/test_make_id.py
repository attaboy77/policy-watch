# -*- coding: utf-8 -*-
"""뉴스 URL id(make_id) — 추적 파라미터 블랙리스트 (2026-11-20).

예전 make_id()는 쿼리를 통째로 지워 articleView.html?idxno=… 꼴 사이트의 서로 다른
기사가 같은 id가 됐고, 정확 일치 중복 제거에서 한 건만 남고 사라졌다(10/29~ 32건).
공식 소스는 make_id_exact()로 이미 고쳤고 뉴스만 남아 있었다.
"""
from sources._utils import dedupe, make_id


def test_different_articles_same_site_get_different_ids():
    # 실측: 일간NTN 두 기사가 같은 id(e36946ad3101fae1)였다.
    a = make_id("http://www.intn.co.kr/news/articleView.html?idxno=2053355")
    b = make_id("http://www.intn.co.kr/news/articleView.html?idxno=2052654")
    assert a != b


def test_unknown_params_are_kept():
    # 기사번호 파라미터 이름을 미리 알 필요가 없다(블랙리스트 방식).
    assert make_id("https://x.kr/v.php?zz_article=1") != make_id("https://x.kr/v.php?zz_article=2")


def test_param_order_does_not_matter():
    assert make_id("https://x.kr/a?no=1&cat=2") == make_id("https://x.kr/a?cat=2&no=1")


def test_tracking_params_dropped():
    base = make_id("https://www.ohmynews.com/at_pg.aspx?CNTN_CD=A0003278115")
    for tracked in ("&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news",
                    "&fbclid=abc", "&gclid=abc", "&igshid=abc", "&UTM_Source=X"):
        assert make_id("https://www.ohmynews.com/at_pg.aspx?CNTN_CD=A0003278115" + tracked) == base


def test_url_without_kept_params_keeps_old_id():
    # 쿼리 없는 URL·추적 파라미터만 있는 URL은 예전 id 그대로(마이그레이션 대상 아님).
    import hashlib
    old = lambda u: hashlib.sha1(u.strip().lower().split("?")[0].split("#")[0].encode()).hexdigest()[:16]
    for u in ("https://www.dt.co.kr/article/12090224",
              "https://www.yna.co.kr/view/AKR20261101044700003?utm_source=x",
              "https://news.google.com/rss/articles/CBMiABC?oc=5"):   # 구글 뉴스 id 불변
        assert make_id(u) == old(u)


def test_dedupe_keeps_both_articles_from_same_site():
    def item(i, url, title):
        return {"id": make_id(url), "title": title, "final_score": 50, "_i": i}
    items = [
        item(1, "http://www.joseilbo.com/news/news_read.php?uid=576157&class=18&grp=", "감리지적사례-매출채권 허위계상"),
        item(2, "http://www.joseilbo.com/news/news_read.php?uid=576027&class=18&grp=", "감리지적사례-전환사채"),
    ]
    assert len(dedupe(items)) == 2


def test_officetel_article_excluded_alone():
    # 2026-11-20: 일간NTN 두 기사 중 오피스텔 기사만 개별 제외(세금계산서 기사는 유지).
    from sources._config import EXCLUDED_IDS
    assert make_id("http://www.intn.co.kr/news/articleView.html?idxno=2053355") in EXCLUDED_IDS
    assert make_id("http://www.intn.co.kr/news/articleView.html?idxno=2052654") not in EXCLUDED_IDS
