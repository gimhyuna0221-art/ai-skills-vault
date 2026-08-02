# Obsidian Lecture Pack — General

일반 설명형·실습형·주제형 강의를 Obsidian 지식팩으로 바꾸는 독립 스킬입니다.

현재 버전: `1.3.0`  
상태: `stable draft`

## 사용 대상

- 설교·인문학·철학·웹소설 작법·디자인·도구 강의
- 일반 YouTube 강의와 튜토리얼
- 학생별 피드백이 없는 CG 튜토리얼

학생별 진도와 재등장 세션을 추적하는 CG 옴니버스 수업은 별도
`obsidian-lecture-pack-cg`를 사용합니다.

## 두 실행 모드

두 모드 모두 일반 강의용입니다.

차이는 분석 대상이 아니라 기존 일반 강의 지식베이스와 병합하는지,
그리고 다음 처리를 위한 동기화팩을 생성하는지입니다.

### 단독 모드 — 기본값

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

상태 기록:

```yaml
mode: standalone
processing_status: complete
sync_status: none
```

### 누적 모드

같은 분야의 일반 강의를 계속 쌓으며 기존 개념·워크플로우·강의 인덱스와 병합할 때 사용합니다.

```text
/obsidianpack-update
```

같은 분야의 유효한 일반 강의 동기화팩을 첨부해도 누적 모드가 선택됩니다.

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

동기화팩은 누적 모드에서만 생성하며, 과거 원문전사는 넣지 않습니다.

기존 동기화팩이 없는 첫 누적 실행:

```yaml
mode: cumulative
processing_status: complete
sync_status: initialized
```

기존 동기화팩과 병합한 실행:

```yaml
mode: cumulative
processing_status: complete
sync_status: updated
```

## CG 동기화팩과의 차이

일반 누적 모드는 CG 스킬처럼 다음 처리용 동기화 ZIP을 생성하지만,
저장하는 데이터의 목적과 구조는 다릅니다.

일반 누적 모드:

- 같은 분야의 일반 강의 인덱스
- 일반 개념
- 분야별 워크플로우
- 강의별 목차·북마크·최종노트

CG 옴니버스 스킬:

- 학생별 안정적 ID와 aliases
- 이전 피드백과 반영 여부
- 현재 제작 단계
- 재등장 세션
- 캐릭터 제작 11단계 통합 워크플로우

두 동기화팩은 서로 병합하지 않습니다.

## 어떤 모드를 쓰는가

```text
영상 한 편만 정리
→ /obsidianpack
→ 단독 모드

같은 분야를 계속 누적
→ /obsidianpack-update
→ 누적 모드

유효한 같은 분야 동기화팩 첨부
→ 누적 모드 자동 선택
```

## NotebookLM 프롬프트

```text
prompts/notebooklm-general.md
```

단독·누적 모드 모두 같은 프롬프트를 사용합니다.
분석 방식은 같고 패키징과 병합 여부만 다릅니다.

## 모드 정의

```text
modes/standalone.md
modes/cumulative.md
```

## 앵커 검증

시작·끝 앵커는 원문전사 안의 한 시간 구간에서
연속된 5~15어절을 사용해야 합니다.

서로 다른 시간 구간의 문장을 연결하거나
시간 제목을 가로지르는 앵커는 검증 실패입니다.

## v1.3.0 실제 재생성 확인

2026-08-02에 기도 응답 설교 자료로 단독 모드 결과를 다시 생성했습니다.

사용자 수동 확인:

- `02_북마크.md` 생성
- 북마크 시간 링크를 누르면 YouTube 해당 시점 재생
- `03_최종노트.md`의 시간 링크를 누르면 YouTube 해당 시점 재생
- 개념 노트 생성
- 워크플로우 노트 생성
- 과정목차·AI 허브·강의 인덱스 생성
- Obsidian 그래프 연결 표시
- 한 강의에서 추출한 지식을 `standard`로 과장하지 않음

아직 패키지 파일 자체로 재검증해야 하는 항목:

- 단독 결과 ZIP에 `AI_동기화용/`이 없는지
- 모든 시작·끝 앵커의 원문 연속 일치
- 전체 내부 링크의 깨짐·모호함 0개
- SHA-256과 manifest 일치
- 누적 모드의 경량 동기화팩 구조
- 같은 분야 두 번째 강의 병합
