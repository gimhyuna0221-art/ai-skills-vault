---
name: rect-strip-uv
description: >-
  OBJ 벨트·스트랩·띠의 UV만 긴 직사각형 스트립으로 전개하고 양 끝을 같은 섬에 연결한다.
  원본 좌표·사각 와이어·노멀·그룹을 보존하며 타일맵용 OBJ, 체커, 검수 기록을 만든다.
  두께 없는 열린 사각형 메시용이다. 재모델링, 구멍 가공, 버클·폐곡면의 일반 UV 작업에는 사용하지 않는다.
compatibility: >-
  Python 3.11+ with local shell, file read/write and image viewing.
  NumPy, SciPy, Pillow, Shapely and Numba; see requirements.txt.
  No Blender, 3ds Max, API key or network needed after dependencies are installed.
metadata:
  version: "1.0.1"
  workflow: "uv-only-rectangular-body-attached-ends"
---

# Rectangular Strip UV

## 목적과 고정 규칙

사용자에게 설명만 하지 말고 실제 UV가 들어간 OBJ를 반환한다. **동봉한 스크립트를 실행한다.**
알고리즘을 새로 작성하거나 이전 메시의 정점 번호, 그룹 이름, 축, 파일 경로를 복사하지 않는다.

- 형상은 수정하지 않는다. 정점·면 순서, 쿼드 연결, 노멀, 오브젝트·그룹·스무딩·재질 선언을 유지한다.
- 디시메이션, 리메시, 용접, 스무딩, 구멍, 두께, 면 삼각화를 하지 않는다. 내부 계산용 삼각화만 허용된다.
- 몸통의 긴 UV 경계는 직선으로 만든다. 양 끝은 펼쳐서 같은 섬에 연결한다. 끝을 강제로 네모나게 찌그러뜨리지 않는다.
- 여러 띠는 각각 한 섬으로 만들고 겹치지 않게 배치한다. 타일용 U/V 비율을 유지한다.
- 수치 통과와 시각 통과를 구분한다. 파일·검사·미리보기 확인 전 “완료/문제없음”이라고 보고하지 않는다.

## 적용 범위

입력은 **한 개 이상의 길쭉한, 두께 없는, 구멍 없는 사각형 면 띠**로만 구성된 OBJ다.
각 구성요소는 경계 루프 1개인 디스크여야 한다. 착용 상태로 굽거나 겹쳐져 있어도 된다.
화면에서 둥글게 보이는 벨트와, 양 끝 정점이 실제로 용접된 폐곡면은 다르다.

삼각형·엔곤·버클 같은 폐곡면·두께 있는 솔리드가 섞이면 자동 수정하지 않고 중단한다.
입력이 없으면 OBJ 첨부를 요청한다. `.max` 또는 스크린샷을 OBJ로 추측해 처리하지 않는다.

## 1. 환경과 경로 확인

`SKILL_DIR`은 **이 SKILL.md가 있는 실제 폴더**다. 아래 예시 경로는 실제 경로로 바꾼다.
첨부파일은 런타임에서 경로를 확인한다. 이름만 보고 경로를 만들어내지 않는다.
원본은 작업 폴더 밖에 두며 출력은 별도 `WORK_DIR`에 저장한다.

```bash
python "SKILL_DIR/scripts/rect_strip_uv.py" doctor
```

의존성 누락 때만 해당 실행환경의 패키지 설치 권한을 확인하고 아래 명령을 사용한다.

```bash
python -m pip install -r "SKILL_DIR/requirements.txt"
```

코드 실행 도구나 필요한 패키지를 사용할 수 없으면 그 제한을 알린다. 지침을 읽은 것만으로 UV를 생성했다고 하지 않는다.

## 2. 첫 실행

타일맵이 목적이면 기본 파일 한 개만 생성한다. 재질 이미지나 API 키는 필요 없다.

```bash
python "SKILL_DIR/scripts/rect_strip_uv.py" run --input "INPUT.obj" --work "WORK_DIR"
```

0–1 대안까지 요청된 경우 **첫 실행부터** `--also-01`을 추가한다.
0–1 대안은 전체 UV를 동일 비율로 축소한다. 정사각형을 가득 채우는 비등방 스케일을 쓰지 않는다.

실행 순서는 `inspect → unwrap → export → verify → preview → package`다.
대용량 OBJ는 읽기/쓰기/검수가 UV 계산보다 오래 걸릴 수 있다. 진행 로그를 확인하며 기다린다.

실행도구의 시간 제한이 짧으면 한 번에 종료를 기다리는 대신, 제공되는 프로세스 실행/폴링 기능으로 같은 실행을 계속 관찰한다.
작업 중 새 프로세스를 중복 실행하지 않는다. 단순히 매번 동일한 짧은 timeout으로 재시작하지 않는다.

단계별 호출이 필요한 경우:

```bash
python "SKILL_DIR/scripts/rect_strip_uv.py" run --input "INPUT.obj" --work "WORK_DIR" --stop-after inspect
python "SKILL_DIR/scripts/rect_strip_uv.py" resume --work "WORK_DIR" --stop-after unwrap
python "SKILL_DIR/scripts/rect_strip_uv.py" resume --work "WORK_DIR"
```

## 3. 중단 복구

```bash
python "SKILL_DIR/scripts/rect_strip_uv.py" status --work "WORK_DIR"
python "SKILL_DIR/scripts/rect_strip_uv.py" resume --work "WORK_DIR"
```

`state.json`, `progress.jsonl`, `run.lock` 및 현재 프로세스를 확인한다.
`RUNNING`은 마지막으로 기록된 상태일 뿐 실제 프로세스가 살아 있다는 증거는 아니다.
같은 입력·같은 옵션·같은 코드이면 검증된 **완료 단계**를 재사용한다. 중단된 단계의 내부 계산은 다시 할 수 있다.
`.part` 파일은 결과물이 아니다. 원본/코드/체크포인트 해시 불일치 시 새 작업 폴더를 사용한다.
예전 성공 로그나 예전 파일을 새 실행의 성공 근거로 쓰지 않는다.

## 4. 기계 검수 + 시각 검수

스크립트는 저장한 OBJ를 다시 읽고 아래 항목을 검사한다.

1. 원본 정점 좌표·원본 v 행, 면 인덱스·순서·노멀 참조·그룹 선언이 그대로인가.
2. 모든 면 코너에 유효한 UV가 있고, 뒤집힌/면적 0인 UV 삼각형과 비볼록 UV 쿼드가 없는가.
3. 각 섬이 단일 디스크·단순 경계이며, 면적 합과 경계 면적이 일치하는가. 섬끼리 분리되어 있는가.

`delivery/QA_report.json`을 읽은 뒤 **실제 이미지 세 개를 열어 본다**:
`UV_layout.png`, `UV_checker.png`, `UV_checker_front.png`.
몸통 경계의 직선, 양 끝의 연결, 체커의 심한 늘어짐·접힘·누락을 확인한다.
시각 판단 도구가 없으면 수치 검사만 통과했다고 명확히 표시한다.

스크립트의 성공 상태는 `NUMERIC_PASS_VISUAL_REVIEW_REQUIRED`다. 이것을 시각 승인으로 바꾸어 해석하지 않는다.
직사각형 전개는 곡면의 왜곡을 완전히 없애지 않는다. 끝의 위상이나 원본의 깊은 주름 때문에 국소 왜곡은 남을 수 있다.

## 5. 반환

`WORK_DIR/rect_strip_uv_delivery.zip`과 `delivery/INPUT_UV_tile.obj` 링크를 먼저 제공한다.
요청된 경우 `INPUT_UV_01.obj`를 함께 제공하되 **동일 메시의 UV 대안이므로 둘 다 임포트하지 않도록** 설명한다.
두 확인 이미지 링크와 핵심 검수 수치를 덧붙인다. 원본에 없던 재질이나 MTL을 임의로 만들지 않는다.

권장 문구:
“UV 전개본을 저장했습니다. 원본 형상·와이어를 유지하고 몸통을 직사각형 스트립, 양 끝을 연결된 섬으로 처리했습니다.
수치 검사 결과는 …이며, 시각 확인 결과/남은 제한은 …입니다. 타일 버전의 0–1 범위 이탈은 의도한 반복 배치입니다.”

## 실패 시

종료 코드 `2`는 처리/검수 중단, `3`은 의존성 누락이다.
오류의 원인과 현재 저장 단계만 보고한다. **검사를 삭제하거나 임의 리메시로 통과시키지 않는다.**
자세한 진단은 [TROUBLESHOOTING.md](references/TROUBLESHOOTING.md), 알고리즘 설명은 [METHOD.md](references/METHOD.md)를 필요한 경우에만 읽는다.
`--endpoints` 같은 고급 옵션은 자동 끝점 선택이 실패하거나 명백히 잘못된 때만 사용한다.
낮은 추론 모델의 기본 경로는 위의 명령 실행과 결과 확인이며 수학 재설계가 아니다.
