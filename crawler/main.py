"""정책모니터 수집기 — 모든 소스를 수집해 data/items.json 과 site/data.js 를 갱신.

실행: python crawler/main.py
"""
import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from sources import law_api, korea_kr  # noqa: E402  (법제처 주력, 정책브리핑 보조)

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "items.json"
SITE_DATA = ROOT / "site" / "data.js"

SOURCES = [law_api, korea_kr]
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/126.0 Safari/537.36"),
    "Accept": "application/rss+xml, application/xml, text/xml, */*",
    "Accept-Language": "ko-KR,ko;q=0.9",
}
KEEP_DAYS = 365  # 1년 이상 지난 항목은 정리


def load_existing() -> list[dict]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def main():
    session = requests.Session()
    session.headers.update(HEADERS)

    existing = load_existing()

    def dedup_key(it):
        # 법령은 URL이 바뀔 수 있어 제목+날짜로 식별
        return (it.get("title", ""), it.get("date", ""))

    seen_keys = {dedup_key(it) for it in existing}
    new_items, failures = [], []

    for mod in SOURCES:
        name = mod.__name__.split(".")[-1]
        try:
            fetched = mod.fetch(session)
            fresh = []
            for it in fetched:
                k = dedup_key(it)
                if k in seen_keys:
                    continue
                seen_keys.add(k)
                it["collected_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                fresh.append(it)
            new_items.extend(fresh)
            print(f"[{name}] {len(fetched)}건 수집, 신규 {len(fresh)}건")
        except Exception as e:
            failures.append(f"{name}: {e}")
            print(f"[{name}] 실패: {e}")
        time.sleep(2)  # 서버 부담 최소화

    merged = new_items + existing
    cutoff = (datetime.today() - timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d")
    merged = [it for it in merged if it.get("date", "") >= cutoff]
    merged.sort(key=lambda x: x.get("date", ""), reverse=True)

    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")

    # 정적 사이트가 file:// 로도 열리도록 JS 파일로도 출력
    payload = {
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": merged,
    }
    SITE_DATA.write_text(
        "window.POLICY_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";",
        encoding="utf-8",
    )

    print(f"\n총 {len(merged)}건 저장 (신규 {len(new_items)}건)")
    if failures:
        print("파싱 실패 소스 — 사이트 구조 변경 여부를 확인하세요:")
        for f in failures:
            print("  -", f)
        sys.exit(0)  # 일부 실패해도 배포는 진행


if __name__ == "__main__":
    main()
