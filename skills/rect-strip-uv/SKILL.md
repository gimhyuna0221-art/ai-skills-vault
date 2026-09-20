---
name: rect-strip-uv
description: >-
  두께 없는 열린 사각형 OBJ 벨트·스트랩의 UV를 긴 직사각형 몸통과 연결된 양 끝으로 편다.
  기본 결과는 원본 형상·와이어·노멀·그룹을 보존한 UV-only 하이폴이다.
  입력의 면·엣지가 많으면 둥근 끝을 보존하는 검수된 로우폴을 별도로 함께 제공한다.
compatibility: >-
  Python 3.11+ with local file read/write, NumPy, SciPy, Pillow, Shapely and Numba.
  Image viewing is required for visual acceptance. No Blender, 3ds Max or API key required.
metadata:
  version: "1.1.1"
  workflow: "uv-only-original-with-conditional-shape-checked-lowpoly"
---

# Rectangular Strip UV

## 고정 계약

사용자에게 방법만 설명하지 말고 동봉한 `scripts/rect_strip_uv.py`를 실행해 실제 OBJ를 반환한다. `uv_core.py`는 보존된 내부 구현이며 직접 호출하는 기본 진입점이 아니다.

**항상 원본 UV-only 결과부터 만든다.** 정점 좌표·v 행·면 연결과 순서·노멀·그룹·재질 선언은 바꾸지 않는다. 스무딩, 주름 추가, 구멍, 두께, 용접, 리메시는 하지 않는다. 기존 UV만 교체한다.

**입력이 무거우면 하이폴과 로우폴을 둘 다 준다.** 기본 자동 기준은 실제 쿼드 `>=250,000` 또는 실제 엣지 `>=500,000`이다. 이 값은 작업 기준이지 보편적인 하드웨어 한계가 아니다. 로우폴은 원본 보존본을 대체하지 않는 별도 파생 결과다. 가벼운 입력은 원본 UV 결과만 제공한다.

**둥근 끝은 네모로 만들지 않는다.** 몸통 UV를 직사각형으로 편다는 뜻이지 메시 전체를 직사각형 격자로 다시 만든다는 뜻이 아니다. 로우폴은 입증된 원본 subdivision 연결 계층만 사용한다. 끝의 원래 경계 순서와 쿼드 흐름을 유지하고 모든 원본 경계 정점의 현 이탈량을 검사한다. 목표 면 수보다 형상 보존을 우선한다.

## 적용 범위

길이/폭 비 4 이상인 얇은 열린 쿼드 띠, 구성요소마다 경계 루프 1개인 디스크가 대상이다. 몸에 맨 형태로 굽고 겹쳐 있어도 된다. 버클·두께 있는 솔리드·삼각형·엔곤·구멍·분기·완전히 용접된 고리까지 처리하는 범용 UV 도구가 아니다. 지원 범위 밖이면 임의로 고치지 않는다.

원본을 작업 폴더 밖에 두고, 실제 첨부 경로를 확인한다. 입력이 없으면 OBJ를 요청한다. 스크린샷으로 메시를 만들어냈다고 하지 않는다. 이전 세션의 정점 번호, 그룹, 단위, 축, 파일 경로를 재사용하지 않는다.

## 기본 실행

`SKILL_DIR`과 파일 경로를 실제 경로로 바꾼다. Python 실행 도구가 필요하다.

```bash
python "SKILL_DIR/scripts/rect_strip_uv.py" doctor
python "SKILL_DIR/scripts/rect_strip_uv.py" run --input "INPUT.obj" --work "WORK_DIR"
```

의존성이 없을 때만 환경 권한을 확인하고 `python -m pip install -r "SKILL_DIR/requirements.txt"`를 사용한다. 낮은 추론 모델은 코드를 재설계하거나 검사를 완화하지 않는다.

기본으로 무거운 입력의 하이폴/로우폴 판단을 자동 수행한다. 0–1 UV 대안까지 명시적으로 요청되었을 때만 첫 실행에 `--also-01`을 추가한다. 가로·세로 동일 배율이다. 타일 UV의 0–1 범위 이탈은 반복 좌표이며, 여러 UDIM 이미지를 만드는 작업은 아니다. 단위를 cm로 추정하지 않는다.

사용자가 하이폴/로우폴 자동 정책을 명시적으로 바꿀 때만 다음 옵션을 사용한다.

```text
--lowpoly off                    # 사용자가 별도로 UV-only만 강제할 때
--lowpoly-face-threshold 250000  # 실제 쿼드 수 기준
--lowpoly-edge-threshold 500000  # 실제 엣지 수 기준
--lowpoly-target-faces 40000     # 강제 수치가 아닌 목표 예산
```

`--also-lowpoly-auto`는 호환 별칭이며 기본 동작과 같다. 로우폴 허용 오차는 기본 경계 샘플 최대/벨트 폭 1%, 표면 정점 보간 샘플 최대/벨트 폭 3%다. 이를 통과시키려고 임의로 올리지 않는다. 안전한 레벨이 목표 예산보다 무거우면 그대로 더 많은 면을 남긴다.

## 중단과 재개

단계: `inspect → unwrap → export → verify → preview → lowpoly → package`.

```bash
python "SKILL_DIR/scripts/rect_strip_uv.py" status --work "WORK_DIR"
python "SKILL_DIR/scripts/rect_strip_uv.py" resume --work "WORK_DIR"
```

`--stop-after inspect`, `--stop-after unwrap`, `--stop-after lowpoly`로 단계별 저장이 가능하다. 입력·코드·설정이 달라지면 새 작업 폴더를 쓴다. 이전 버전의 성공 로그나 `.part`를 재사용하지 않는다. `RUNNING`은 저장된 상태이며 프로세스가 살아 있다는 증거는 아니다. 실제 프로세스를 확인하고, 가능한 실행도구에서는 세션 실행/폴링을 사용한다. 같은 짧은 timeout으로 무작정 다시 시작하지 않는다.

## 검수와 실패 처리

하이폴은 저장 OBJ를 다시 읽어 원본 보존, 모든 UV 참조, 두 섬 이상의 분리, UV 뒤집힘·퇴화·겹침 조건을 검사한다. 로우폴은 별도로 면 수가 실제 줄었는지, 원본 좌표 샘플·상속 UV·쿼드 연결·면별 그룹/재질 상태가 저장 후 일치하는지 검사한다. 원본의 재질/그룹 경계를 가로지르는 축소는 거부한다. 로우폴 노멀은 호스트가 다시 계산하고 하이폴 노멀은 보존한다.

반드시 읽을 결과: `QA_report.json`, `QA_report_lowpoly.json`, `DELIVERY.json`.

반드시 열어 볼 이미지: `UV_layout.png`, `UV_checker.png`, `UV_checker_front.png`. 로우폴이 있으면 `LOWPOLY_checker.png`, `LOWPOLY_layout.png`, 특히 `LOWPOLY_ends.png`를 추가로 연다. 원본 끝 외곽선과 실제 로우폴 와이어를 비교한다. 이 이미지의 국소 투영은 검사 자료이지 모든 뷰의 보증이 아니다.

성공 상태는 `NUMERIC_PASS_VISUAL_REVIEW_REQUIRED`다. 수치 통과나 이미지 생성 자체를 시각 승인이라고 말하지 않는다. 시각 도구가 없으면 그 제한을 명시한다.

안전한 축소를 입증할 수 없으면 `HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED`와 종료 코드 4를 반환한다. 이때 원본 UV 결과와 검수 ZIP은 남는다. **로우폴은 미완료라고 말한다. 같은 고폴 파일을 로우폴이라 이름만 바꾸거나 끝을 네모 격자로 만들어 통과시키지 않는다.** 코드 2는 처리/검수 중단, 3은 의존성 누락이다.

## 반환

`WORK_DIR/rect_strip_uv_delivery.zip`과 `delivery/INPUT_UV_tile.obj`를 제공한다. 무거운 입력의 로우폴이 검증되었으면 `delivery/INPUT_lowpoly_UV_tile.obj`도 반드시 함께 제공한다. 전자는 원본 보존 하이폴, 후자는 작업용 파생 로우폴임을 구분한다. 선택적인 `_01.obj`는 해당 해상도 메시의 UV 대안이다.

하이폴/로우폴 면 수, 실제 감소율, 끝 형상 확인 결과, 남은 제한을 보고한다. 정점 샘플 오차는 연속 곡면 전체의 Hausdorff 보증이 아니며 미세 디테일이 달라질 수 있다. MTL·텍스처·노멀맵을 생성/동봉했다고 꾸미지 않는다. 원본 작업 파일을 GitHub 등으로 업로드하지 않는다.

[방법](references/METHOD.md) · [로우폴 규칙](references/LOWPOLY.md) · [진단](references/TROUBLESHOOTING.md)

## 유지보수와 원격 반영

저장소 업데이트 요청에는 루트 `AGENTS.md`와 [재발 방지 기록](references/INCIDENT_2026-09-20.md)을 읽는다. 현재 연결 도구와 실제 main/커밋/CI를 확인하기 전 불가·완료·과거 업로드 부정을 단정하지 않는다. 로컬 준비, 원격 커밋, main 반영, 같은 SHA의 CI 통과를 분리한다. 사용자 작업용 OBJ·텍스처는 공개하지 않고 합성 예제로 테스트한다.
