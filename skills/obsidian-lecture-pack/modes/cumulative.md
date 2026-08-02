# General Lecture Mode — Cumulative

## 목적

같은 분야의 일반 강의를 계속 추가하면서
기존 개념·워크플로우·강의 인덱스와 병합한다.

## 선택 조건

- `/obsidianpack-update`
- 같은 분야의 유효한 일반 강의 동기화팩 첨부
- 누적·병합·제2의 뇌 구축 의도 명시
- 일반 강의 지식베이스를 처음부터 누적형으로 시작한다고 명시

## 상태 기록

기존 동기화팩이 없고 누적형을 처음 시작하는 경우:

```yaml
mode: cumulative
processing_status: complete
sync_status: initialized
```

기존 동기화팩과 병합한 경우:

```yaml
mode: cumulative
processing_status: complete
sync_status: updated
```

## 결과 구조

```text
옵시디언_일반강의_업데이트.zip
├─ 볼트에_복사/
│  └─ 분야명/
├─ AI_동기화용/
│  └─ 00_다음_처리에_보낼_AI동기화팩.zip
├─ 검사자료/
│  ├─ 98_검사결과.md
│  └─ package_manifest.json
├─ README.md
└─ SHA256SUMS.txt
```

## 경량 동기화팩 포함 항목

```text
_시스템/
└─ 동기화_manifest.json

분야명/
├─ 00_AI허브.md
├─ 00_과정목차.md
├─ 강의 인덱스.md
├─ 강의/
│  └─ 각 강의/
│     ├─ 00_강의목차.md
│     ├─ 02_북마크.md
│     └─ 03_최종노트.md
├─ 개념/
└─ 워크플로우/
```

## 동기화팩 제외 항목

- `01_원문전사.md`
- 원본 자막·전사·영상
- 이미지
- NotebookLM 원본 분석
- 검사자료
- `.obsidian/`
- `SKILL.md`
- 프롬프트와 개발 문서

정확한 과거 발화가 필요하면 해당 강의의 `01_원문전사.md`를 별도로 요청한다.

## 파일명 호환

새 출력 파일명:

```text
00_다음_처리에_보낼_AI동기화팩.zip
```

다음 구형 파일명은 입력 호환용으로만 허용한다.

```text
00_매주_ChatGPT에_보낼_AI동기화팩.zip
```

다음 출력부터 새 파일명으로 재생성한다.

## 병합 안전

- 동기화팩의 분야가 새 강의 분야와 일치해야 한다.
- CG 동기화팩과 병합하지 않는다.
- 손상되거나 SHA-256이 맞지 않으면 병합하지 않는다.
- 기존 사용자 문장과 경로를 임의로 덮어쓰지 않는다.
- 같은 개념은 중복 파일을 만들지 않고 근거를 추가한다.
- 한 사례만으로 지식 상태를 `standard`로 승격하지 않는다.
