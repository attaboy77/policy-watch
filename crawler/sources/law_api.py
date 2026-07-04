"""법제처 국가법령정보 Open API — 세법·회계 관련 법령 개정 이력 조회 (선택).

API 키(OC)가 없으면 자동으로 건너뛴다.
사용하려면 https://open.law.go.kr 에서 무료 신청 후 LAW_API_OC 환경변수 설정.
"""
import os
import xml.etree.ElementTree as ET

import requests

API_URL = "http://www.law.go.kr/DRF/lawSearch.do"
TARGET_LAWS = ["법인세법", "소득세법", "부가가치세법", "국세기본법",
               "주식회사 등의 외부감사에 관한 법률"]


def fetch(session: requests.Session) -> list[dict]:
    oc = os.environ.get("LAW_API_OC")
    if not oc:
        return []  # 키 없으면 조용히 건너뜀

    items = []
    for law in TARGET_LAWS:
        try:
            resp = session.get(API_URL, params={
                "OC": oc, "target": "law", "type": "XML",
                "query": law, "display": 3, "sort": "ddes",
            }, timeout=30)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
        except Exception as e:
            print(f"  [law_api] {law} 조회 실패: {e}")
            continue

        for node in root.iter("law"):
            name = (node.findtext("법령명한글") or "").strip()
            date = (node.findtext("공포일자") or "").strip()
            kind = (node.findtext("제개정구분명") or "").strip()
            link = (node.findtext("법령상세링크") or "").strip()
            if not name:
                continue
            items.append({
                "source": "법제처",
                "category": "법령",
                "title": f"{name} {kind}".strip(),
                "url": ("http://www.law.go.kr" + link) if link.startswith("/") else link,
                "date": f"{date[:4]}-{date[4:6]}-{date[6:8]}" if len(date) == 8 else date,
            })
    return items
