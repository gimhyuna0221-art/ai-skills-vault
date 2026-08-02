# General Lecture Mode — Standalone

## 목적

서로 독립적인 일반 강의 한 편을 Obsidian에 보관한다.
과거 강의와 병합하거나 다음 처리용 지식 스냅샷을 만들지 않는다.

## 선택 조건

- `/obsidianpack-new`
- 한 편만 정리
- 기존 일반 강의 동기화팩 없음
- 누적 의도 없음
- 모드가 불명확한 `/obsidianpack` 요청

## 상태 기록

```yaml
mode: standalone
processing_status: complete
sync_status: none
```

`initialized`나 `updated`를 사용해 누적 상태처럼 보이게 하지 않는다.

## 결과 구조

```text
옵시디언_일반강의팩.zip
├─ 볼트에_복사/
│  └─ 분야명/
├─ 검사자료/
│  ├─ 98_검사결과.md
│  └─ package_manifest.json
├─ README.md
└─ SHA256SUMS.txt
```

다음 폴더는 만들지 않는다.

```text
AI_동기화용/
```

## 검사 기준

- 일반 강의 필수 노트가 모두 존재한다.
- 사용자용 볼트에 검사·개발 문서가 없다.
- 내부 링크와 앵커 검사를 통과한다.
- AI 동기화팩이 생성되지 않았음을 검사결과에 기록한다.

## 나중에 누적으로 전환

사용자가 나중에 같은 분야를 누적하려면 다음 중 하나를 제공한다.

- 현재 Obsidian의 해당 분야 폴더
- 이전 단독 결과 ZIP
- 해당 분야의 최신 누적 동기화팩

검증 후 누적 모드의 초기 스냅샷을 생성한다.
