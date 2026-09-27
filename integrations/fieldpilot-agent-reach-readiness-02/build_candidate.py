#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import shutil
import subprocess
import sys
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
BASE = REPO / "integrations" / "fieldpilot-broker-exec-01" / "build_candidate.py"
PARTS = [HERE / f"payload2.{i:02d}" for i in range(16)]

TRIAL_ZIP_SHA256 = "ed3a149ab4fa83da5b3322973e012ebae6a1ce8048f0e156a555c0b115c2599f"
BASE_COMMIT = "55b1aa7824627b23304be869187dbc25d66e540d"
AGENT_REACH_PIN = "a19a171fa980a0785849596492e0af4db800c82f"


def make_frontmatter_yaml_safe(skill_path: Path) -> None:
    text = skill_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise RuntimeError("SKILL.md frontmatter missing")
    for i, line in enumerate(lines):
        if line.startswith("description: "):
            description = line[len("description: "):]
            lines[i:i+1] = ["description: >-", "  " + description]
            skill_path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
            return
        if line == "description: >-" or line == "description: |":
            return
        if i > 0 and line == "---":
            break
    raise RuntimeError("SKILL.md description field missing")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    out = Path(args.output).resolve()
    if out.exists():
        shutil.rmtree(out)

    subprocess.run(
        [sys.executable, str(BASE), "--output", str(out)],
        check=True,
        cwd=REPO,
    )

    skill = out / "fieldpilot"
    if not (skill / "SKILL.md").is_file():
        raise RuntimeError("broker base candidate missing fieldpilot/SKILL.md")

    encoded = "".join(p.read_text(encoding="utf-8") for p in PARTS)
    files = json.loads(
        zlib.decompress(base64.b64decode(encoded)).decode("utf-8")
    )

    for rel, file_content in files.items():
        dest = skill / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(file_content, encoding="utf-8")

    make_frontmatter_yaml_safe(skill / "SKILL.md")

    print(
        json.dumps(
            {
                "status": "BUILT",
                "output": str(skill),
                "overlaid_files": len(files),
                "trial_zip_sha256": TRIAL_ZIP_SHA256,
                "base_commit": BASE_COMMIT,
                "agent_reach_pin": AGENT_REACH_PIN,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
