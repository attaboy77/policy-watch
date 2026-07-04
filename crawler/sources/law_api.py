"""법제처 국가법령정보 Open API — 세법·회계 관련 법령의 최근 개정 조회 (주력).

API 키(OC) 방식이라 IP 차단이 없어 GitHub Actions에서 안정적이다.

준비:
1. https://open.law.go.kr 회원가입 → OPEN API 활용신청(무료, 자동승인)
2. 본인 이메일 ID가 OC 값 (예: hong@gmail.com → OC=hong)
3. GitHub 저장소 Settings → Secrets에 LAW_API_OC 로 등록
   (미설정 시 공개 테스트 계정 'test'로 동작하나 트래픽 제한 있음)
"""
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

import requests

SEARCH_URL = "https://www.law.go.kr/DRF/lawSearch.do"

LAW_GROUPS = {
    "세법": ["법인세법", "소득세법", "부가가치세법", "국세기본법", "국세징수법",
           "상속세 및 증여세법", "종합부동산세법", "조세특례제한법", "관세법"],
    "회계기준": ["주식회사 등의 외부감사에 관한 법률"],
    "법령": ["국가재정법", "국고금 관리법"],
}

# 응답 태그명이 버전에 따라 다를 수 있어 후보를 모두 시도
NAME_TAGS = ["법령명한글", "법령명", "법령명한글명"]
PUBDATE_TAGS = ["공포일자"]
ENFDATE_TAGS = ["시행일자"]
KIND_TAGS = ["제개정구분명", "제개정구분"]
LINK_TAGS = ["법령상세링크"]


def _first(node, tags):
    for t in tags:
        v = node.findtext(t)
        if v and v.strip():
            return v.strip()
    return ""


def _fmt_date(raw: str) -> str:
    raw = re.sub(r"[.\-\s]", "", raw or "")
    if len(raw) == 8 and raw.isdigit():
        return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"
    return raw


def fetch(session: requests.Session) -> list[dict]:
    oc = os.environ.get("LAW_API_OC", "test")
    items, seen = [], set()
    debug_shown = False

    for category, laws in LAW_GROUPS.items():
        for law in laws:
            try:
                resp = session.get(SEARCH_URL, params={
                    "OC": oc, "target": "eflaw", "type": "XML",
                    "query": law, "display": 5,
                }, timeout=30)
                resp.raise_for_status()
                root = ET.fromstring(resp.content)
            except Exception as e:
                print(f"  [law_api] {law} 조회 실패: {e}")
                continue

            # 첫 응답 구조를 한 번만 로그로 남겨 디버깅 지원
            if not debug_shown:
                tags = {child.tag for child in root.iter()}
                print(f"  [law_api] 응답 태그 샘플: {sorted(tags)[:15]}")
                debug_shown = True

            # <law> 우선, 없으면 상세링크를 가진 항목 노드를 자동 탐색
            law_nodes = list(root.iter("law"))
            if not law_nodes:
                for child in root:
                    if any(child.findtext(t) for t in NAME_TAGS):
                        law_nodes.append(child)

            for node in law_nodes:
                name = _first(node, NAME_TAGS)
                if not name or law.replace(" ", "") not in name.replace(" ", ""):
                    continue
                pub = _fmt_date(_first(node, PUBDATE_TAGS))
                enf = _fmt_date(_first(node, ENFDATE_TAGS))
                kind = _first(node, KIND_TAGS)
                link = _first(node, LINK_TAGS)

                key = (name, pub, enf)
                if key in seen:
                    continue
                seen.add(key)

                url = ("https://www.law.go.kr" + link) if link.startswith("/") \
                    else (link or f"https://www.law.go.kr/법령/{name}")
                date = pub or enf or datetime.today().strftime("%Y-%m-%d")
                label = f"{name}"
                if kind:
                    label += f" ({kind})"
                if enf:
                    label += f" · {enf} 시행"

                items.append({
                    "source": "법제처",
                    "category": category,
                    "title": label,
                    "url": url,
                    "date": date,
                })

    print(f"  [law_api] 법령 {len(items)}건 수집")
    return items
