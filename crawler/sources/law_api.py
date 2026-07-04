"""법제처 국가법령정보 Open API — 세법·회계 관련 법령의 최근 시행/개정 조회.

이 소스가 주력이다. API 키(OC) 방식이라 IP 차단이 없어 GitHub Actions에서 안정적이다.

준비:
1. https://open.law.go.kr 회원가입 → OPEN API 활용신청(무료, 대개 자동승인)
2. 본인 이메일 ID가 곧 OC 값 (예: hong@gmail.com → OC=hong)
3. GitHub 저장소 Settings → Secrets → Actions에 LAW_API_OC 로 등록
   (등록 전에는 공개 테스트 계정 'test'로 자동 동작하나, 트래픽 제한이 있으니 꼭 본인 키를 등록하세요.)
"""
import os
import xml.etree.ElementTree as ET
from datetime import datetime

import requests

SEARCH_URL = "https://www.law.go.kr/DRF/lawSearch.do"

# 카테고리별로 추적할 법령 (제목에 이 이름이 들어간 최근 개정 법령을 가져온다)
LAW_GROUPS = {
    "세법": ["법인세법", "소득세법", "부가가치세법", "국세기본법", "국세징수법",
           "상속세 및 증여세법", "종합부동산세법", "조세특례제한법", "관세법"],
    "회계기준": ["주식회사 등의 외부감사에 관한 법률"],
    "법령": ["국가재정법", "국고금 관리법"],
}


def _text(node, tag):
    v = node.findtext(tag)
    return v.strip() if v else ""


def _fmt_date(raw: str) -> str:
    raw = raw.strip().replace(".", "").replace("-", "")
    if len(raw) == 8 and raw.isdigit():
        return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"
    return raw or datetime.today().strftime("%Y-%m-%d")


def fetch(session: requests.Session) -> list[dict]:
    oc = os.environ.get("LAW_API_OC", "test")  # 키 미설정 시 테스트 계정
    items, seen = [], set()

    for category, laws in LAW_GROUPS.items():
        for law in laws:
            try:
                resp = session.get(SEARCH_URL, params={
                    "OC": oc,
                    "target": "eflaw",   # 현행법령(시행일 기준)
                    "type": "XML",
                    "query": law,
                    "display": 3,
                    "sort": "efdes",     # 시행일 내림차순(최신 먼저)
                }, timeout=30)
                resp.raise_for_status()
                root = ET.fromstring(resp.content)
            except Exception as e:
                print(f"  [law_api] {law} 조회 실패: {e}")
                continue

            for node in root.iter("law"):
                name = _text(node, "법령명한글")
                if not name or law not in name:
                    continue
                enf = _fmt_date(_text(node, "시행일자"))
                pub = _fmt_date(_text(node, "공포일자"))
                kind = _text(node, "제개정구분명")
                link = _text(node, "법령상세링크")
                serial = _text(node, "법령일련번호")

                key = (name, enf)
                if key in seen:
                    continue
                seen.add(key)

                url = ("https://www.law.go.kr" + link) if link.startswith("/") else \
                      (link or f"https://www.law.go.kr/법령/{name}")

                items.append({
                    "source": "법제처",
                    "category": category,
                    "title": f"{name} ({kind}, {enf} 시행)" if kind else f"{name} ({enf} 시행)",
                    "url": url,
                    "date": pub or enf,
                })

    print(f"  [law_api] 법령 {len(items)}건 수집")
    return items
