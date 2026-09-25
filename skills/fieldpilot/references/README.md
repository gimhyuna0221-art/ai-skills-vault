# FieldPilot Runtime References

이 폴더는 FieldPilot current FieldPilot package이 런타임에서 사용하는 내부 규칙 모음입니다.
일반 사용자는 이 파일들을 직접 선택하거나 읽을 필요가 없습니다.

- `core/` — 증거 규칙, 윤리, 주장 문법, 조사·분석 라우팅
- `domains/` — 제품/시장 유형별 추가 제약
- `methods/` — 인터뷰, 설문, 실험, 가격, 세분화 등 조사 방법 카드
- `delivery/` — 고객용 의사결정 요약과 전문 산출물 계약
- `modules/` — 이전 릴리스에서 누적되어 현재 current FieldPilot package도 사용하는 시장·GTM·품질 모듈

`modules/`는 구버전 보관함이 아닙니다. 현재 current FieldPilot package에서 계속 사용하는 활성 모듈을
버전 폴더 없이 한곳에 정리한 것입니다.


## Lifecycle routing — v1.9.9-rc03

- `modules/LIFECYCLE_DECISION_ROUTER.md` — 아이디어 → MVP/개발 → 출시 전/판매 전 → 출시 후 무반응 → 관심 있으나 미결제 → 수익화 → 재평가를 하나의 `/fieldpilot` 진입점에서 단계·증상별로 라우팅한다.
- 단계별로 기존 `DECISION_CONTINUITY`, `DECISION_SURFACES`, `DEMAND_DISTRIBUTION_DIAGNOSTICS`, `PRODUCT_READINESS_AND_SIGNAL_INTEGRITY`, `FREE_FIRST_AND_CHANNEL_ROUTING` 등을 조건부 로드한다.
- 대박/망함, 레드오션, 틈새, 고객, 광고 성과를 증거보다 강하게 단정하지 않는다.
