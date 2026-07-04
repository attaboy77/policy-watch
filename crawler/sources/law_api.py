"""법제처 국가법령정보 Open API — 세법·회계 관련 법령 개정 이력 조회.

사용 전 준비:
1. https://open.law.go.kr 에서 회원가입 후 API 활용 신청 (무료)
2. 발급받은 이메일 ID(OC 값)를 환경변수 LAW_API_OC 에 설정
   예) export LAW_API_OC=your_id
"""
import os
import xml.etree.ElementTree as ET

import requests

API_URL = "http://www.law.go.kr/DRF/lawSearch.do"
TARGET_LAWS = ["법인세법", "소득세법", "부가가치세법", "국세기본법", "주식회사 등의 외부감사에 관한 법률"]


def fetch(session: requests.Session) -> list[dict]:
    oc = os.environ.get("LAW_API_OC")
    if not oc:
        print("  [law_api] LAW_API_OC 환경변수 없음 — 건너뜀")
        return []

    items = []
    for law in TARGET_LAWS:
        resp = session.get(API_URL, params={
            "OC": oc, "target": "law", "type": "XML",
            "query": law, "display": 5, "sort": "ddes",  # 공포일 내림차순
        }, timeout=30)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)

        for node in root.iter("law"):
            name = (node.findtext("법령명한글") or "").strip()
            date = (node.findtext("공포일자") or "").strip()   # YYYYMMDD
            kind = (node.findtext("제개정구분명") or "").strip()  # 일부개정 등
            link = (node.findtext("법령상세링크") or "").strip()
            if not name:
                continue
            items.append({
                "source": "법제처",
                "category": "법령",
                "title": f"{name} {kind}" if kind else name,
                "url": "http://www.law.go.kr" + link if link.startswith("/") else link,
                "date": f"{date[:4]}-{date[4:6]}-{date[6:8]}" if len(date) == 8 else date,
            })
    return items
