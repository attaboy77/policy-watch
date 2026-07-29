"""정책모니터 수집기 — 모든 소스를 수집해 data/items.json 과 site/data.js 를 갱신.

소스: 법제처 API·금융위 RSS(공식원문, Worker 경유) + 구글/네이버 뉴스(언론).
실행: python crawler/main.py
"""
import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from sources import law_api, fsc, google_news, naver_news, _common  # noqa: E402

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "items.json"
SITE_DATA = ROOT / "site" / "data.js"

# 공식원문(정확) → 뉴스(속보성). 순서대로 수집.
SOURCES = [law_api, fsc, google_news, naver_news]
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/126.0 Safari/537.36"),
    "Accept": "application/rss+xml, application/xml, text/xml, application/json, */*",
    "Accept-Language": "ko-KR,ko;q=0.9",
}
KEEP_DAYS = 180  # 뉴스는 최근 6개월만 유지
ALLOWED_CATEGORIES = {"세법", "K-IFRS", "내부회계", "ESG"}
# 옛 카테고리로 저장된 공식원문 항목 변환
CATEGORY_MIGRATION = {"회계기준": "K-IFRS", "법령": "세법"}
# 공식원문은 오래 유지, 뉴스만 6개월 컷
OFFICIAL_SOURCES = {"법제처", "금융위원회"}


def load_existing() -> list[dict]:
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []
        cleaned = []
        for it in data:
            cat = it.get("category")
            if cat in CATEGORY_MIGRATION:
                it["category"] = CATEGORY_MIGRATION[cat]
            if it.get("category") in ALLOWED_CATEGORIES:
                # official 필드 없는 옛 항목 보강
                if "official" not in it:
                    it["official"] = _common.official_links(it["category"])
                if "source_type" not in it:
                    it["source_type"] = "공식원문" if it.get("source") in OFFICIAL_SOURCES else "뉴스"
                cleaned.append(it)
        return cleaned
    return []


def main():
    session = requests.Session()
    session.headers.update(HEADERS)

    existing = load_existing()
    new_items, failures = [], []

    for mod in SOURCES:
        name = mod.__name__.split(".")[-1]
        try:
            fetched = mod.fetch(session)
            new_items.extend(fetched)
            print(f"[{name}] {len(fetched)}건 수집")
        except Exception as e:
            failures.append(f"{name}: {e}")
            print(f"[{name}] 실패: {e}")
        time.sleep(1)

    # 전체 병합 후 중복 제거 (공식원문 우선 → 뉴스)
    # 공식원문을 앞에 두어 같은 주제면 공식원문이 살아남도록
    official = [it for it in (new_items + existing) if it.get("source_type") == "공식원문"]
    news = [it for it in (new_items + existing) if it.get("source_type") != "공식원문"]

    # 공식원문은 제목+날짜로 중복 제거
    seen, official_dedup = set(), []
    for it in official:
        k = (it.get("title", ""), it.get("date", ""))
        if k in seen:
            continue
        seen.add(k)
        official_dedup.append(it)

    # 뉴스는 제목 유사도로 중복 제거
    news_dedup = _common.dedup(news)

    merged = official_dedup + news_dedup

    # 날짜 컷: 뉴스만 6개월, 공식원문은 유지
    cutoff = (datetime.today() - timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d")
    merged = [it for it in merged
              if it.get("source_type") == "공식원문" or it.get("date", "") >= cutoff]

    merged.sort(key=lambda x: x.get("date", ""), reverse=True)

    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")

    payload = {"updated": datetime.now().strftime("%Y-%m-%d %H:%M"), "items": merged}
    SITE_DATA.write_text(
        "window.POLICY_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";",
        encoding="utf-8",
    )

    # 카테고리별 집계
    by_cat = {}
    for it in merged:
        by_cat[it["category"]] = by_cat.get(it["category"], 0) + 1
    print(f"\n총 {len(merged)}건 저장  {by_cat}")
    if failures:
        print("실패 소스:")
        for f in failures:
            print("  -", f)
    sys.exit(0)


if __name__ == "__main__":
    main()
