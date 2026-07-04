"""법제처 국가법령정보 Open API — 세법·회계 관련 법령의 최근 시행/개정 조회.

데이터 품질이 가장 정확한 소스(실제 법령 개정 이력).
law.go.kr이 해외 IP를 차단하므로 공용 프록시(_http)를 경유한다.

API 키(OC): https://open.law.go.kr 가입 → OPEN API 활용신청(무료) → 이메일 ID가 OC.
GitHub Secrets에 LAW_API_OC로 등록. 미설정 시 'test' 계정 사용(트래픽 제한 있음).
"""
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urlencode

from . import _http

BASE = "https://www.law.go.kr/DRF/lawSearch.do"

LAW_GROUPS = {
    "세법": ["법인세법", "소득세법", "부가가치세법", "국세기본법", "국세징수법",
           "상속세 및 증여세법", "종합부동산세법", "조세특례제한법", "관세법"],
    "회계기준": ["주식회사 등의 외부감사에 관한 법률"],
    "법령": ["국가재정법", "국고금 관리법"],
}

NAME_TAGS = ["법령명한글", "법령명"]
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


def fetch(session):
    oc = os.environ.get("LAW_API_OC", "test")
    items, seen = [], set()
    debug_shown = False

    for category, laws in LAW_GROUPS.items():
        for law in laws:
            qs = urlencode({"OC": oc, "target": "eflaw", "type": "XML",
                            "query": law, "display": 5})
            url = f"{BASE}?{qs}"
            content = _http.fetch_bytes(session, url, tag=f"law/{law[:6]}")
            if not content:
                continue
            try:
                root = ET.fromstring(content)
            except Exception as e:
                print(f"  [law/{law[:6]}] XML 파싱 실패: {str(e)[:40]}")
                continue

            if not debug_shown:
                tags = sorted({c.tag for c in root.iter()})[:12]
                print(f"  [law_api] 응답 태그 샘플: {tags}")
                debug_shown = True

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

                url_detail = ("https://www.law.go.kr" + link) if link.startswith("/") \
                    else (link or f"https://www.law.go.kr/법령/{name}")
                label = name
                if kind:
                    label += f" ({kind})"
                if enf:
                    label += f" · {enf} 시행"

                items.append({
                    "source": "법제처", "category": category,
                    "title": label, "url": url_detail,
                    "date": pub or enf or datetime.today().strftime("%Y-%m-%d"),
                })

    print(f"  [law_api] 법령 {len(items)}건 수집")
    return items
