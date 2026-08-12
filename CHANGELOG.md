# Changelog

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
