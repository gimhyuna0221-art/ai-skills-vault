# AI Skills Vault

내가 반복해서 사용하는 AI 작업 방식을 플랫폼과 분리해 보관하는 저장소입니다.

## 현재 스킬

| 폴더 | 역할 | 상태 |
|---|---|---|
| `skills/prompt-router` | 요청을 분석해 적절한 사고·검증·도구 모드를 자동 선택 | stable draft |
| `skills/obsidian-lecture-pack` | 자막·NotebookLM·YouTube를 근거로 Obsidian 강의팩 생성 | stable |
| `skills/fieldpilot` | 외부 사용자 모집부터 파일럿·설문·개선까지 단계별 운영 | stable draft |

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

## GitHub에 올리는 방법

1. GitHub에서 `ai-skills-vault` 저장소를 만든다.
2. 이 ZIP을 컴퓨터에서 압축 해제한다.
3. 저장소의 `Add file → Upload files`에서 압축 해제한 내부 파일을 업로드한다.
4. 커밋 메시지에 `Initialize AI skills vault`를 입력한다.
5. `Commit changes`를 누른다.

ZIP 파일 자체만 올리지 말고 압축을 풀어 폴더와 Markdown 파일을 올린다.
