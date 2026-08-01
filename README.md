# AI Skills Vault

내가 반복해서 사용하는 AI 작업 방식을 플랫폼과 분리해 보관하는 저장소입니다.

## 현재 스킬

| 스킬 | 역할 | 상태 |
|---|---|---|
| [Prompt Router](skills/prompt-router/) | 요청을 분석해 적절한 사고·검증·도구 모드를 자동 선택 | stable draft |
| [Obsidian Lecture Pack](skills/obsidian-lecture-pack/) | 자막·NotebookLM·YouTube를 근거로 Obsidian 강의팩 생성 | stable draft |
| [Field Pilot](skills/fieldpilot/) | 외부 사용자 모집부터 파일럿·설문·개선까지 단계별 운영 | stable draft |

## 저장 원칙

- 프로젝트 고유 사실은 각 프로젝트 저장소에 둔다.
- 여러 프로젝트에 재사용할 작업 방식만 이 저장소에 둔다.
- API 키, 비밀번호, 연락처, 실제 참여자 정보는 저장하지 않는다.
- 수정할 때는 `CHANGELOG.md`에 변경 이유를 기록한다.
- 실제로 검증되지 않은 내용은 `stable`이라고 표시하지 않는다.

## 기본 구조

```text
ai-skills-vault/
├─ skills/
│  ├─ prompt-router/
│  ├─ obsidian-lecture-pack/
│  └─ fieldpilot/
├─ templates/
│  └─ skill-template/
└─ adapters/
   ├─ chatgpt-projects/
   ├─ claude-code/
   └─ codex/
```

## 현재 단계

이 저장소의 스킬은 실제 사용과 검증을 거치며 개선하고 있습니다.

상세 기준: [Skill Validation Standard](VALIDATION.md)

- `stable`: 반복 사용과 기본 검증이 완료된 스킬
- `stable draft`: 구조는 완성됐지만 추가 사례와 검증이 필요한 스킬
- `experimental`: 초기 실험 단계의 스킬

현재 공개된 자료는 포트폴리오와 기능 평가를 위한 버전입니다.


## Usage and licensing

Copyright © 2026 gimhyuna0221-art. All rights reserved.

이 저장소는 포트폴리오 공개 및 평가 목적으로 게시되었습니다.

저장소 소유자의 사전 서면 허가 없이 이 자료를 복제, 수정, 재배포,
재판매, 재허가하거나 상업적으로 이용할 수 없습니다.

개인적인 열람과 평가를 넘어 사용하려는 경우 저장소 소유자에게
별도 허가를 받아야 합니다.

Commercial licensing inquiries may be directed to the repository owner.

## Contributions

현재 이 저장소는 외부 코드·문서 기여와 Pull Request를 받지 않습니다.

오류 제보와 개선 의견은 GitHub Issue로 제안할 수 있지만,
제안된 내용을 실제 저장소에 반영할지는 저장소 소유자가 결정합니다.

상업화와 라이선스 정책이 확정된 뒤 기여 정책을 다시 검토할 예정입니다.

