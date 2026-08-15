# Obsidian Lecture Pack — CG Omnibus

여러 학생이 서로 다른 캐릭터 제작 단계에서 순차 피드백받는 CG 옴니버스 수업 전용 스킬입니다.

현재 버전: `4.4.0`

## v4.4 핵심

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
