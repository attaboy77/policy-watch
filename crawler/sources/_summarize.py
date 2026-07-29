"""제목 기반 자동 요약 생성 — 2줄 요약 + 실무 영향 의견 (규칙 기반).

LLM 없이 정적 환경에서 동작하도록 키워드·패턴 기반으로 생성한다.
"""
import re

# 카테고리별 실무 영향 의견 템플릿
IMPACT_TEMPLATES = {
    "세법": [
        "세무조정·신고 실무에 반영이 필요하며, 시행일 전 관련 규정을 점검하세요.",
        "법인·소득 신고 시 개정 내용 적용 여부를 사전에 확인해야 합니다.",
        "세무팀은 개정 시행일 기준으로 내부 프로세스 업데이트를 검토하세요.",
    ],
    "K-IFRS": [
        "회계정책 및 재무제표 표시에 영향이 있어 결산 전 영향분석이 필요합니다.",
        "감사 대응을 위해 기준서 변경 사항을 회계처리에 선반영하세요.",
        "재무보고 담당자는 공시 서식·주석 변경 여부를 확인해야 합니다.",
    ],
    "내부회계": [
        "내부회계관리제도 운영·평가 절차에 반영이 필요합니다.",
        "감사 대응 및 미비점 개선 계획에 본 개정 사항을 포함하세요.",
        "내부통제 문서화·평가 일정에 영향이 있는지 점검이 필요합니다.",
    ],
    "ESG": [
        "지속가능성 공시 대응 로드맵에 반영해 단계별 준비가 필요합니다.",
        "공급망·배출량 데이터 수집 체계를 사전에 점검하세요.",
        "공시 의무화 일정에 맞춰 내부 데이터 관리 체계를 준비해야 합니다.",
    ],
}


def _pick_impact(category: str, seed: str) -> str:
    tmpls = IMPACT_TEMPLATES.get(category, IMPACT_TEMPLATES["세법"])
    idx = sum(ord(c) for c in seed[:10]) % len(tmpls)
    return tmpls[idx]


def make_summary(item: dict) -> dict:
    """항목에 summary_lines(2줄)와 impact(실무 의견)를 추가해 반환."""
    title = item.get("title", "")
    category = item.get("category", "")
    source = item.get("source", "")
    is_official = item.get("source_type") == "공식원문"

    # 2줄 요약 생성
    if is_official:
        name = re.split(r"[(·]", title)[0].strip()
        enf = re.search(r"(\d{4}-\d{2}-\d{2})\s*시행", title)
        kind = re.search(r"(일부개정|전부개정|타법개정|제정)", title)
        line1 = f"「{name}」 관련 {category} 규정이 {kind.group(1) if kind else '개정'}되었습니다."
        if enf:
            line2 = f"{enf.group(1)}부터 시행되며, 시행 전 실무 반영 여부를 확인해야 합니다."
        else:
            line2 = "공식 원문을 통해 세부 개정 내용과 적용 시점을 확인하세요."
    else:
        line1 = f"{source}가 보도한 {category} 분야 동향입니다."
        line2 = "관련 기관 공식 자료와 함께 실무 적용 사항을 검토할 필요가 있습니다."

    item["summary_lines"] = [line1, line2]
    item["impact"] = _pick_impact(category, title)
    return item
