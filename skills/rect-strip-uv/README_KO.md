# 직사각형 스트립 UV — v1.0.1

벨트·스트랩의 **형상과 사각 와이어를 바꾸지 않고 UV만** 길게 펴는 실행형 스킬입니다. 몸통은 긴 직사각형, 양 끝은 같은 섬에 연결합니다. 낮은 추론 모델은 수학을 새로 설계하지 않고 동봉한 명령을 실행하고 결과를 검사합니다.

[English](README.md) · [모델용 지침](SKILL.md) · [실행 검증](evidence/public_validation.json) · [업로드 벤치마킹](references/BENCHMARKING.md)

## 설치

기존 저장소 소유자 또는 별도로 사용 허가받은 사용자를 위한 설치 명령입니다. 공개 저장소라고 자유 이용 라이선스가 부여되는 것은 아닙니다. [기존 이용 조건](LICENSE.txt)을 유지합니다.

```bash
npx skills add gimhyuna0221-art/ai-skills-vault --skill rect-strip-uv
```

Node.js는 위 선택 설치 도구에 필요합니다. 설치 도구가 Python과 의존성까지 설치해 주지는 않습니다. 위 명령은 Vercel 공식 CLI 문법에 맞췄지만, 이번 게시 환경에서 실제 호스트 설치까지 실행한 것은 아닙니다.

Codex에 직접 등록할 때는 이 폴더 전체를 프로젝트 또는 사용자 홈의 `.agents/skills/rect-strip-uv/`에 둡니다. 호출 예:

```text
$rect-strip-uv 이 OBJ의 UV만 펴라. 몸통은 긴 직사각형, 양 끝은 같은 섬으로 연결하라. 형상과 사각 와이어를 유지하고 실제 OBJ와 검수 결과를 반환하라.
```

다른 도구 지원 모델에는 스킬 폴더와 OBJ를 제공하고 다음과 같이 요청합니다.

> SKILL.md를 읽고 동봉한 scripts/rect_strip_uv.py를 실행하라. UV만 수정하고 원본 형상·와이어는 유지하라. 중단 시 같은 작업을 resume하라. 저장 OBJ의 검수 기록과 미리보기 세 개를 확인하고 결과 파일을 반환하라. 검사나 코드를 임의로 완화하지 마라.

파일 읽기·Python 실행·이미지 확인 도구가 필요합니다. 텍스트 전용 모델이 지침을 읽는 것만으로 OBJ가 수정되지는 않습니다.

## 직접 실행

이 스킬 폴더에서 실행합니다. Python 3.11 이상이 필요하며 Max/Blender/API 키는 필요하지 않습니다.

```bash
python -m pip install -r requirements.txt
python scripts/rect_strip_uv.py doctor
python scripts/rect_strip_uv.py run --input "belt.obj" --work "belt_uv_job"
```

Windows에서 Python Launcher를 사용하면 `python` 대신 `py -3`을 쓸 수 있습니다. 공백·한글 경로는 따옴표로 감쌉니다. 원본은 작업 폴더 밖에 둡니다.

기본 반환은 `belt_uv_job/rect_strip_uv_delivery.zip`과 `delivery/belt_UV_tile.obj`입니다. 0–1 대안이 필요할 때만 첫 실행에 `--also-01`을 붙입니다. 두 OBJ는 동일 모델의 UV 대안이므로 하나만 임포트합니다.

타일용 UV가 0–1을 벗어나는 것은 의도한 반복 좌표입니다. UDIM 이미지 여러 장을 생성하는 기능은 아닙니다. 0–1 대안은 가로·세로를 같은 비율로 축소합니다. `--tile-width`는 한 타일에 대응하는 모델 좌표 길이이며 cm로 가정하지 않습니다.

## 작은 예제로 먼저 확인

실제 작업 원본을 공개하지 않도록 새로 만든 예제 생성기만 넣었습니다.

```bash
python examples/make_example.py --output "demo-input/strap.obj"
python scripts/rect_strip_uv.py run --input "demo-input/strap.obj" --work "demo-job" --also-01
python -m unittest discover -s tests -v
```

예제 생성기는 이미 있는 파일을 덮어쓰지 않습니다. 다시 실행할 때는 새로운 경로를 사용합니다.

## 중간에 끊겼을 때

```bash
python scripts/rect_strip_uv.py status --work "belt_uv_job"
python scripts/rect_strip_uv.py resume --work "belt_uv_job"
```

원본·코드·설정이 같은 경우 완료된 단계를 해시 검사 후 재사용합니다. 중단된 단계 내부 계산은 다시 할 수 있습니다. 같은 이름이어도 입력 내용이 바뀌었으면 새 작업 폴더를 사용합니다. 실행 중인 프로세스를 확인하지 않고 잠금을 삭제하거나 중복 실행하지 않습니다.

## 지원 범위와 검수

두께 없는 열린 쿼드 띠, 구성요소마다 경계 루프 1개, 구멍·분기 없음, 길이/폭 비 4 이상이 대상입니다. 버클, 두께 있는 솔리드, 삼각형·엔곤, 완전히 용접된 고리는 자동 처리하지 않습니다. 기본 상한 300만 면·제어망 15만 정점·32개 구성요소는 안전 제한이지 성능 보장이 아닙니다.

정점 좌표와 원래 v 행, 면 순서와 쿼드 연결, 노멀 참조, 그룹·재질 선언을 보존합니다. 기존 UV는 교체합니다. 디시메이션·구멍·두께·스무딩은 하지 않습니다. 기존 MTL과 텍스처는 임의 생성하거나 자동 묶음 처리하지 않습니다.

완료 상태 `NUMERIC_PASS_VISUAL_REVIEW_REQUIRED`는 **수치 통과 후 시각 확인이 필요하다**는 뜻입니다. `UV_layout.png`, `UV_checker.png`, `UV_checker_front.png`를 실제로 열어 확인합니다. 끝부분·깊은 주름에는 국소 왜곡이 남을 수 있습니다.

[검증 기록](evidence/public_validation.json)은 이번 실행과 과거 고해상도 실행을 분리합니다. 낮은 추론 모델 여러 개의 성공률이나 3ds Max 자체 왕복 검증은 아직 측정하지 않았습니다. 모델 평가용 12개 시나리오는 미실행 계획이며 실측 성능표가 아닙니다. 저장소 상태는 `stable draft`로 유지합니다.

[알고리즘](references/METHOD.md) · [실패 진단](references/TROUBLESHOOTING.md) · [출처](references/SOURCES.md) · [변경 이력](CHANGELOG.md)
