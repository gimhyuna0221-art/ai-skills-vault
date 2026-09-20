# 직사각형 스트립 UV — v1.1.1

벨트·스트랩의 UV를 **긴 직사각형 몸통 + 연결된 양 끝**으로 펴는 실행형 스킬입니다. 기본 결과는 사용자가 준 오브젝트의 형상·와이어·노멀·그룹을 그대로 유지한 UV-only 원본입니다. **입력이 너무 무거우면 이 하이폴 결과와 별도로 검수된 로우폴도 함께 제공합니다.**

[English](README.md) · [모델용 지침](SKILL.md) · [로우폴 방법](references/LOWPOLY.md) · [변경 이력](CHANGELOG.md)

## 설치와 실행

저장소 소유자 또는 별도 사용 허가받은 사용자용입니다. 공개되어 있다는 이유로 자유 이용 라이선스가 부여되지는 않습니다. [기존 이용 조건](LICENSE.txt)은 바꾸지 않았습니다.

```bash
npx skills add gimhyuna0221-art/ai-skills-vault --skill rect-strip-uv
```

선택 설치 도구에는 Node.js가 필요합니다. Python과 패키지까지 설치하는 명령은 아니며, 특정 호스트의 설치 완료를 뜻하지 않습니다. 직접 등록할 때는 전체 스킬 폴더를 `.agents/skills/rect-strip-uv/`에 둡니다.

스킬 폴더에서 실행:

```bash
python -m pip install -r requirements.txt
python scripts/rect_strip_uv.py doctor
python scripts/rect_strip_uv.py run --input "belt.obj" --work "belt_uv_job"
```

Python 3.11 이상, 파일 읽기/쓰기, 패키지와 시각 확인 도구가 필요합니다. Max/Blender/API 키는 필요하지 않습니다. Windows에서는 `py -3`도 가능하며 공백·한글 경로를 따옴표로 감쌉니다. 원본은 작업 폴더 밖에 둡니다.

다른 모델에 전달할 지시:

> SKILL.md를 읽고 scripts/rect_strip_uv.py를 실행하라. 원본의 UV만 편 하이폴은 반드시 보존하라. 입력이 무거우면 둥근 끝을 보존한 로우폴도 별도로 함께 제공하라. 코드를 임의 재작성하거나 검사를 낮추지 말고, 결과 OBJ 재검수와 미리보기를 확인하라. 중단 시 저장된 상태를 확인해 resume하라.

## 어떤 파일을 받는가

- 항상: `delivery/belt_UV_tile.obj` — 원본 정점·쿼드·노멀·메타데이터를 보존한 하이폴 UV 결과.
- 무거운 입력이며 안전한 축소가 가능할 때: `delivery/belt_lowpoly_UV_tile.obj` — 실제 면 수를 줄이고 다시 읽어 검사한 별도 로우폴.
- 전체: `rect_strip_uv_delivery.zip`, 하이폴/로우폴별 QA와 `DELIVERY.json`, 체커·UV 배치·끝부분 확인 이미지.

기본 무거움 기준은 쿼드 250,000개 이상 **또는** 엣지 500,000개 이상입니다. 작업용 기준이며 보편적인 하드웨어 한계는 아닙니다. 로우폴 목표는 40,000면이지만 **형상 보존이 우선**이라 더 많이 남을 수 있습니다. 가벼운 입력은 UV 결과만 제공합니다.

0–1 UV 대안이 필요할 때만 첫 실행에 `--also-01`을 추가합니다. 같은 해상도의 `_tile.obj`와 `_01.obj`는 UV 배치만 다른 대안입니다. 타일 UV의 0–1 밖 좌표는 반복 텍스처용이며 여러 UDIM 이미지를 만드는 기능이 아닙니다. 0–1은 모든 섬에 같은 비율을 적용합니다. 단위는 cm로 가정하지 않습니다.

## 둥근 끝과 형상 보존

UV 몸통을 직사각형으로 편다고 메시 끝까지 네모 격자로 다시 만들지 않습니다. 로우폴은 원본에서 입증된 subdivision 계층의 더 거친 쿼드 연결만 사용합니다. 살아남은 정점 좌표와 UV는 원본 샘플을 사용하며 스무딩·구멍·두께·새 주름을 추가하지 않습니다.

모든 원본 경계 정점의 대응 현 거리와 원본 표면 정점 보간 오차를 검사합니다. 기본 최대 오차는 각각 벨트 폭의 1%, 3%입니다. 재질·그룹·스무딩 경계를 가로지르는 축소를 거부합니다. 이 검사는 연속 표면 전체의 거리 보증은 아니므로 미세한 형상 차이는 남을 수 있습니다. 하이폴은 그대로이며 로우폴 노멀은 가져오는 프로그램에서 다시 계산됩니다.

안전한 축소가 없으면 고폴을 이름만 바꿔 로우폴로 제공하지 않습니다. 하이폴과 보고서는 남기고 `HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED`/종료 코드 4로 부분 완료를 명시합니다. UV 자체가 지원 범위 밖이면 처리 중단입니다.

## 재개와 확인

```bash
python scripts/rect_strip_uv.py status --work "belt_uv_job"
python scripts/rect_strip_uv.py resume --work "belt_uv_job"
```

원본·코드·설정이 같을 때 완료 단계의 해시를 확인해 재사용합니다. 버전이 바뀌면 새 작업 폴더를 사용합니다. `.part`는 완성본이 아니며 살아 있는 프로세스를 확인하지 않고 중복 실행하거나 잠금을 지우지 않습니다.

수치 통과 상태 `NUMERIC_PASS_VISUAL_REVIEW_REQUIRED`는 시각 승인이 아닙니다. 기본 세 이미지와 로우폴의 `LOWPOLY_checker.png`, `LOWPOLY_layout.png`, `LOWPOLY_ends.png`를 직접 엽니다. `QA_report_lowpoly.json`에 실패한 후보, 남긴 레벨, 실제 면 수와 재검수 결과가 기록됩니다.

## 합성 예제와 테스트

```bash
python examples/make_example.py --output demo-input/strap.obj
python scripts/rect_strip_uv.py run --input demo-input/strap.obj --work demo-job --also-01
python examples/make_dense_example.py --output demo-input/dense.obj
python scripts/rect_strip_uv.py run --input demo-input/dense.obj --work dense-job
python -m unittest discover -s tests -v
```

예제 생성기는 기존 파일을 덮어쓰지 않습니다. 밀집 예제는 262,144쿼드의 합성 둥근 스트랩으로 실제 기본 임계값을 넘겨 두 해상도 경로를 검사합니다. 실제 사용자 OBJ/텍스처는 공개하지 않습니다. 현재 결과는 **해당 커밋의 GitHub Actions**에서 확인해야 하며, `evidence/public_validation.json`의 기존 기록을 새 버전 통과 증거로 재사용하지 않습니다.

두께 없는 열린 쿼드 디스크·길이/폭 비 4 이상이 지원 범위입니다. 버클·삼각형·엔곤·솔리드·구멍·분기는 처리하지 않습니다. 기본 300만 입력 면, 15만 제어 정점, 32개 구성요소 제한을 유지합니다. 설치 성공률, 다른 낮은 추론 모델들의 성공률, 3ds Max 왕복 및 시각 검수는 자동 코드 테스트와 별개입니다. 상태는 `stable draft`를 유지합니다.

[기존 업로드 벤치마킹](references/BENCHMARKING.md) · [원인 분석/재발 방지](references/INCIDENT_2026-09-20.md) · [알고리즘](references/METHOD.md) · [출처](references/SOURCES.md)
