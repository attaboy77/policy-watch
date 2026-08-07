# -*- coding: utf-8 -*-
"""오케스트레이터 (entry point).

각 소스 수집기를 독립적으로 실행하고(한 소스 실패가 전체를 죽이지 않도록),
정제 파이프라인(노이즈 제거 → 중복 제거 → 신뢰도 점수 → 요약)을 거쳐
site/data.json을 생성한다.

실행: python -m sources.main

STATUS: Phase 0 스캐폴딩 placeholder — Phase 4에서 구현 예정.
"""


def main() -> None:
    raise NotImplementedError("Phase 4에서 구현 예정 (SPEC.md §8)")


if __name__ == "__main__":
    main()
