# Obsidian Lecture Pack — CG Omnibus

여러 학생이 서로 다른 캐릭터 제작 단계에서 순차 피드백받는 CG 옴니버스 수업 전용 스킬입니다.

현재 버전: `4.5.0`

## v4.5 핵심

- 사용자 실제 실수·near miss를 `캐릭터 워크플로우/00_오답노트.md`에 누적
- 각 워크플로우 단계에 `오답노트` 섹션 추가
- critical/high 실수는 관련 단계의 예방 Gate로 승격
- `02 블록아웃과 비례`에 RF→BP→FiT→CHECK→SIL→TM→RF→LOCK→DT 서브워크플로우 명시
- SpotLight/ZAppLink/Transpose Master 비율 수정에 `SAVE STATE GATE` 적용
- ZPR / ZSL / VWS 저장 역할을 분리해 운영
- `/obsidian-cg-mistake` 명령 추가
- NotebookLM 프롬프트는 v4.4 유지

## v4.4 기반 안전성 유지

- 실제 수업일 `lecture_date`와 영상 업로드일 `upload_date` 분리
- 사용자 확인 학생 이름·요일·반을 normalized source 최우선으로 사용
- 여러 날짜 강의를 한 번에 batch ingest 가능
- 모든 날짜별 북마크를 `00_통합 북마크.md`로 전체 재생성
- 학생 사례를 사용자 업데이트 ZIP에 전체 스냅샷으로 포함
- stale AI 동기화팩 감지
- 경로 rename 교정 시 삭제/rename 목록 제공
- `(1)/(2)/(3)` 충돌 복사본 생성 금지
- `/obsidian-cg-repair` clean rebuild 복구 모드 추가

## 호출

```text
/obsidian-cg
/obsidianpack-cg
/obsidian-cg-full
/obsidian-cg-sync-rebuild
/obsidian-cg-lint
/obsidian-cg-query
/obsidian-cg-repair
/obsidian-cg-mistake
```

## 지식 구조

```text
강의
학생 사례
개념
캐릭터 워크플로우
00_통합 북마크.md
```

## 통합 북마크

모든 `강의/*/02_북마크.md`를 매 병합마다 다시 읽어 완전 재생성합니다.

유일 키:

```text
youtube_id + t_seconds
```

검색 기준:

- 제작 단계
- 날짜·반
- 학생·세션
- 도구·키워드

## 학생 사례

`학생 사례/`는 사용자 업데이트 ZIP에 항상 전체 스냅샷으로 포함합니다.
학생 목차만 전체이고 파일은 일부인 패키지를 만들지 않습니다.

## 날짜 교정

수업일을 나중에 정정하면 frontmatter만 고치지 않습니다.

강의 경로·ID·링크·학생 이력·개념 근거·워크플로우 근거·인덱스·manifest를 같이 교정합니다.

## 복구

Vault에 `강의 (1)/`, `파일 (1).md` 같은 충돌 복사본이 다수 생기면 `/obsidian-cg-repair`를 사용합니다.

최신 valid sync pack을 canonical 기준으로 clean 폴더를 재구축하고, sync에서 제외된 원문전사만 기존 Vault에서 회수합니다.


## 오답노트

`오답노트`는 강의에 나온 일반 실패 목록이 아니라 사용자가 실제로 겪은 실수만 기록합니다.

```text
캐릭터_모델링/캐릭터 워크플로우/00_오답노트.md
```

동일 실수는 안정 ID(`O-001` 등)를 유지하고 재발 이력을 추가합니다.
예방이 중요한 실수는 관련 단계의 Gate로 승격됩니다.

## SAVE STATE GATE

비율 수정에서 다음 저장 상태를 분리합니다.

```text
Transpose Master / Project → ZPR
SpotLight set              → ZSL
ZAppLink Views             → VWS
```

ZPR 하나를 SpotLight·ZAppLink View의 완전 백업으로 간주하지 않습니다.
