# Prompt Router v2.1.1

사용자의 요청을 더 좋은 질문으로 바꾸고, 필요한 사고·검증·도구·현실 판단·관계 분석 모드를 자동 선택합니다.

## 대표 호출

```text
/autoprompt
내 요청을 실행 가능한 프롬프트로 바꿔줘.
```

```text
/autoroute
이 문제에 필요한 방식을 알아서 골라 해결해줘.
```

```text
/realthink
듣기 좋은 말로 포장하지 말고, 네 최종 판단과 근거를 말해줘.
```

```text
/politics
이 상황의 이해관계, 권한, 비용, 평판과 연쇄효과를 분석해줘.
```

## 주요 모드

- 재작성: `/human`, `/rewrite`, `/summary`, `/prompt`
- 이해: `/background`, `/eli5`, `/ladder`, `/socratic`, `/why`, `/decompose`
- 분석: `/clarify`, `/assumptions`, `/compare`, `/priority`, `/risk`, `/diagnose`, `/redteam`, `/devils-advocate`
- 현실 판단: `/realthink`
- 관계·판세: `/politics`
- 실행: `/step`, `/plan`, `/roadmap`, `/sop`, `/todo`, `/refactor`
- 검증: `/critique`, `/factcheck`, `/verify`, `/selfcheck`, `/selfconsistency`, `/selfrefine`, `/qa`, `/tests`
- 도구: `/research`, `/tooluse`

## 핵심 구분

### `/realthink`

아첨이나 과도한 완곡어법 없이 가장 현실적인 최종 판단을 제시합니다.
비공개 내부 사고과정을 그대로 공개하는 명령이 아니라, 검토 가능한 근거·불확실성·행동을 직접 제시하는 모드입니다.
직설적인 판단과 공격적이거나 무례한 표현을 구분합니다.

### `/politics`

정당 정치가 아니라 사람·관계·돈·권한·약속·평판·집단 신호를 분석합니다.
상대를 완벽히 읽지 못해도 실패하지 않는 선택 구조와 실제 전달 문장을 설계합니다.
거짓말, 기만, 여론 조작, 부당한 압박은 정치적 기술로 취급하지 않습니다.

## 조합 예시

```text
관계의 판세를 읽고 솔직한 최종 판단까지 필요함
→ /politics + /realthink
```

```text
플랫폼 규칙이나 계약 조건이 관계 판단에 영향을 줌
→ /research + /factcheck + /politics + /risk
```

## 사용 원칙

- 사실관계가 전략의 전제가 되면 먼저 검증합니다.
- 사용자가 통제할 수 없는 결과를 역량 실패로 평가하지 않습니다.
- 손실 회수와 손실 확산 방지를 구분합니다.
- 모드는 필요한 것만 최소 조합합니다.
