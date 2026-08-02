# GitHub 문서 정합화 적용 방법

이 패키지는 스킬 실행 규칙 자체를 바꾸지 않고
README·검증 기록·변경 기록만 현재 구조와 실제 확인 결과에 맞춥니다.

교체 파일:

```text
README.md

skills/obsidian-lecture-pack/
├─ README.md
├─ CHANGELOG.md
├─ VALIDATION_LOG.md
├─ SHA256SUMS.txt
└─ validation/
   └─ case-001-prayer-response.md

skills/obsidian-lecture-pack-cg/
├─ README.md
├─ CHANGELOG.md
├─ VALIDATION_LOG.md
└─ SHA256SUMS.txt
```

수정하지 않는 파일:

```text
skills/obsidian-lecture-pack/SKILL.md
skills/obsidian-lecture-pack/manifest.json
skills/obsidian-lecture-pack/modes/
skills/obsidian-lecture-pack/prompts/

skills/obsidian-lecture-pack-cg/SKILL.md
skills/obsidian-lecture-pack-cg/manifest.json
skills/obsidian-lecture-pack-cg/prompts/
```

## 업로드

GitHub 저장소 루트 `ai-skills-vault/`에서:

1. `Add file`
2. `Upload files`
3. 압축을 푼 뒤 `README.md`와 `skills` 폴더를 업로드
4. 다음 경로로 표시되는지 확인

```text
README.md
skills/obsidian-lecture-pack/README.md
skills/obsidian-lecture-pack-cg/README.md
```

커밋 메시지:

```text
Align Obsidian skill documentation and validation records
```

## 복붙 방식

각 GitHub 파일을 열고 연필 아이콘을 누른 뒤,
이 패키지의 같은 상대 경로 파일 내용을 전체 복사해 덮어씁니다.

가능하면 모든 변경을 한 커밋으로 묶습니다.
