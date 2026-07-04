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
from sources import korea_kr, law_api  # noqa: E402

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "items.json"
SITE_DATA = ROOT / "site" / "data.js"

SOURCES = [korea_kr, law_api]
HEADERS = {"User-Agent": "Mozilla/5.0 (PolicyWatch prototype; contact: you@example.com)"}
KEEP_DAYS = 365  # 1년 이상 지난 항목은 정리


def load_existing() -> list[dict]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def main():
    session = requests.Session()
    session.headers.update(HEADERS)

    existing = load_existing()
    seen_urls = {it["url"] for it in existing}
    new_items, failures = [], []

    for mod in SOURCES:
        name = mod.__name__.split(".")[-1]
        try:
            fetched = mod.fetch(session)
            fresh = [it for it in fetched if it["url"] not in seen_urls]
            for it in fresh:
                it["collected_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
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
