# AI Skills Vault

내가 반복해서 사용하는 AI 작업 방식을 플랫폼과 분리해 보관하는 저장소입니다.

## 현재 스킬

| 스킬 | 역할 | 상태 |
|---|---|---|
| [Prompt Router](skills/prompt-router/) | 요청을 분석해 적절한 사고·검증·도구 모드를 자동 선택 | stable draft |
| [Obsidian Lecture Pack — General](skills/obsidian-lecture-pack/) | 일반 강의를 단독 강의팩 또는 같은 분야 누적 지식베이스로 변환 | stable draft |
| [Obsidian Lecture Pack — CG Omnibus](skills/obsidian-lecture-pack-cg/) | 학생별 CG 옴니버스 피드백을 학생 이력·개념·11단계 워크플로우에 누적 | stable draft |
| [Field Pilot](skills/fieldpilot/) | 외부 사용자 모집부터 파일럿·설문·개선까지 단계별 운영 | stable draft |

## Obsidian Lecture Pack 구조

Obsidian 강의팩은 독립 스킬 두 개로 나뉩니다.

```text
skills/
├─ obsidian-lecture-pack/      일반 강의
└─ obsidian-lecture-pack-cg/   CG 학생별 옴니버스 피드백
```

두 스킬은 프롬프트, 동기화팩, 학생 이력, 지식베이스를 자동 혼합하지 않습니다.

### 1. 일반 강의 스킬

```text
skills/obsidian-lecture-pack/
```

대상:

- 설교, 인문학, 철학, 웹소설 작법, 디자인, 도구 강의
- 일반 YouTube 강의와 튜토리얼
- 학생별 피드백이 없는 CG 튜토리얼

일반 강의 스킬 안에는 두 실행 모드가 있습니다.

#### 단독 모드 — 기본값

한 편을 독립적으로 정리할 때 사용합니다.

```text
/obsidianpack
/obsidianpack-new
```

결과:

```text
옵시디언_일반강의팩.zip
├─ 볼트에_복사/
├─ 검사자료/
├─ README.md
└─ SHA256SUMS.txt
```

`AI_동기화용/`은 생성하지 않습니다.

#### 누적 모드

같은 분야의 일반 강의를 계속 쌓으면서 기존 개념·워크플로우·강의 인덱스와 병합할 때 사용합니다.

```text
/obsidianpack-update
```

같은 분야의 유효한 일반 강의 동기화팩이 제공되면 누적 모드를 선택할 수 있습니다.

결과:

```text
옵시디언_일반강의_업데이트.zip
├─ 볼트에_복사/
├─ AI_동기화용/
│  └─ 00_다음_처리에_보낼_AI동기화팩.zip
├─ 검사자료/
├─ README.md
└─ SHA256SUMS.txt
```

일반 누적 동기화팩은 분야별 경량 스냅샷입니다.

포함:

- AI 허브, 과정목차, 강의 인덱스
- 각 강의의 목차·북마크·최종노트
- 일반 개념과 분야별 워크플로우
- 동기화 manifest

제외:

- 과거 원문전사
- 원본 자막·영상·이미지
- NotebookLM 원본
- 검사자료와 개발 문서

### 2. CG 학생별 옴니버스 피드백 스킬

```text
skills/obsidian-lecture-pack-cg/
```

대상:

- 여러 학생이 서로 다른 캐릭터 제작 단계에서 순차적으로 피드백받는 수업
- 같은 학생이 이후 강의에 다시 등장하는 수업
- 이전 피드백 반영 여부와 현재 제작 단계를 이어서 추적해야 하는 수업

호출:

```text
/obsidian-cg
/obsidianpack-cg
```

CG 스킬은 기본적으로 누적형입니다.

매주 최신 동기화팩을 다음 처리에 다시 제공하여 다음을 이어갑니다.

- 학생별 안정적 ID와 aliases
- 이전 피드백과 반영 여부
- 현재 제작 단계와 다음 과제
- 재등장 세션 연결
- 공용 개념
- 캐릭터 제작 11단계 통합 워크플로우

결과:

```text
옵시디언_CG_주간업데이트.zip
├─ 볼트에 덮어쓸 새 파일과 갱신 파일
└─ 00_매주_ChatGPT에_보낼_AI동기화팩.zip
```

일반 강의 누적팩과 CG 동기화팩은 목적과 데이터 구조가 다르므로 서로 병합하지 않습니다.

## 빠른 선택표

| 입력 | 사용할 스킬·모드 |
|---|---|
| 일반 강의 한 편 | General 단독 모드 |
| 같은 분야의 일반 강의를 계속 누적 | General 누적 모드 |
| 학생별 피드백이 없는 CG 튜토리얼 | General 단독 또는 누적 모드 |
| 여러 학생의 CG 작업을 순차 피드백 | CG Omnibus |
| 동일 학생의 과거 피드백·재등장 추적 | CG Omnibus |

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
│  ├─ fieldpilot/
│  ├─ obsidian-lecture-pack/
│  └─ obsidian-lecture-pack-cg/
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
