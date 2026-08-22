# Changelog

## 4.5.0 — 2026-08-23

### Added

- 사용자 실제 실수·near miss 전용 `캐릭터 워크플로우/00_오답노트.md`
- 안정 오답 ID `O-001` 계열과 `reported_at / occurred_at / severity / status` 스키마
- critical/high 실수를 작업 순서 앞의 재발 방지 Gate로 승격하는 규칙
- `/obsidian-cg-mistake` 명령
- `02 블록아웃과 비례`의 RF→BP→FiT→CHECK→SIL→TM→RF→LOCK→DT 서브워크플로우
- SpotLight·ZAppLink Properties·Transpose Master용 `SAVE STATE GATE`
- ZPR / ZSL / VWS 저장 역할 분리

### Changed

- 워크플로우 본문 스키마에 `오답노트` 섹션 추가
- AI 동기화팩과 사용자 업데이트 ZIP에 오답노트를 필수 포함
- 사용자 실제 실수와 강의의 일반 실패 사례를 별도 지식 계층으로 관리
- high/critical 오답이 연결된 단계의 질의 시 예방 Gate를 먼저 제시
- NotebookLM 프롬프트는 v4.4를 그대로 유지

### Validation

- Maxon 공식 문서 기준 Transpose Master ZPR 저장, SpotLight ZSL 저장, ZAppLink Views VWS 저장 경로 교차확인
- 기존 11단계 캐릭터 워크플로우 구조 유지
- 학생·북마크·메타데이터·repair 규칙 회귀 없음


## 4.4.0 — 2026-08-12

### Added

- 실제 수업일 `lecture_date`와 영상 업로드일 `upload_date` 분리
- 여러 날짜 강의를 한 번에 처리하는 batch ingest 교차검증
- `00_통합 북마크.md` 전체 rebuild
- `/obsidian-cg-repair` clean rebuild 복구 모드
- stale AI 동기화팩 감지
- identity/lecture metadata correction 기록

### Changed

- 학생 사례를 사용자 업데이트 ZIP에 전체 스냅샷으로 포함
- 사용자 확인 학생 이름·요일·반을 normalized source의 최우선으로 사용
- 날짜·반 교정은 frontmatter 수정이 아닌 path-level migration으로 처리
- 사용자 전달 ZIP을 canonical path 중심으로 강화
- 북마크·시간 위치 질문은 전체 통합 북마크를 먼저 검색

### Fixed

- 학생 목차에는 존재하지만 실제 학생 파일이 ZIP에 빠져 빈 Obsidian 노트가 생성되던 문제
- 영상 업로드일을 실제 수업일로 임시 확정할 수 있던 문제
- NotebookLM/ASR이 다른 학생을 동일인으로 합치는 위험
- 오래된 동기화팩을 사용해 최근 누적 강의가 사라질 수 있던 문제
- 여러 보정 ZIP 적용 후 `강의 (1)/`, `파일 (1).md` 같은 충돌 복사본이 누적되는 문제
- 날짜별 북마크가 많아질수록 기술 위치를 전체 검색하기 어려운 문제

### Validation

- 7강 / 학생 47 / 개념 35 / 통합 북마크 281 상태에서 clean rebuild 검증
- 깨진 링크 0
- 모호한 링크 0
- 중복 ID 0
- `(1)/(2)/(3)` 충돌 복사본 0
