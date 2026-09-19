# Rect Strip UV

**UV-only rectangular unwrapping for thin, open quad belts and straps.**

[한국어 사용 설명서](README_KO.md) · [Agent instructions](SKILL.md) · [Validation](evidence/public_validation.json) · [Publishing benchmarks](references/BENCHMARKING.md)

Version **1.0.1** · Repository status **stable draft**, not a general-purpose UV tool.

Creates a long rectangular body with connected ends, one UV island per strip. Preserves original vertex records, quad connectivity, normals, groups and material declarations. Uses local Python rather than asking an AI model to invent a new UV algorithm.

## Install the skill

For the repository owner or separately authorized users; see [usage terms](LICENSE.txt). Public visibility does not grant an open-source license.

```bash
npx skills add gimhyuna0221-art/ai-skills-vault --skill rect-strip-uv
```

List discoverable skills without installing:

```bash
npx skills add gimhyuna0221-art/ai-skills-vault --list
```

The optional installer needs Node.js and downloads the skill; it does **not** install Python dependencies. The command follows the [Vercel Skills CLI](https://github.com/vercel-labs/skills#readme). Host installation was not executed in the publishing container; a compatible folder structure is not a claim of marketplace approval.

For manual Codex installation, place this entire folder at `.agents/skills/rect-strip-uv/` in a project or under your home directory. See [official skill documentation](https://developers.openai.com/codex/skills).

```text
$rect-strip-uv Unwrap this OBJ for a repeating texture. Keep the geometry and quads; use rectangular bodies and attached ends. Run the bundled scripts and inspect the exported results.
```

## Run directly

From this skill folder, with Python 3.11+ and a separate job folder:

```bash
python -m pip install -r requirements.txt
python scripts/rect_strip_uv.py doctor
python scripts/rect_strip_uv.py run --input "belt.obj" --work "belt_uv_job"
```

Windows Python Launcher users may replace `python` with `py -3`. Quote paths with spaces. Do not put the input inside the work directory.

Add `--also-01` on the first run only when a uniformly scaled 0–1 alternative is needed. Repeat UVs deliberately exceed 0–1; they are not a multi-image UDIM set. `--tile-width` means scene units per UV tile, never assumed centimeters.

Outputs: `belt_uv_job/rect_strip_uv_delivery.zip`, `delivery/belt_UV_tile.obj`, QA JSON and three preview PNGs. The optional `belt_UV_01.obj` is an alternative, not a second object to import.

## Try a reproducible synthetic example

No customer mesh or textures are included.

```bash
python examples/make_example.py --output "demo-input/strap.obj"
python scripts/rect_strip_uv.py run --input "demo-input/strap.obj" --work "demo-job" --also-01
python -m unittest discover -s tests -v
```

The generator refuses to overwrite a file. Choose fresh demo paths for a repeat run.

## Resume instead of restarting

```bash
python scripts/rect_strip_uv.py status --work "belt_uv_job"
python scripts/rect_strip_uv.py resume --work "belt_uv_job"
```

Stages: inspect → unwrap → export → verify → preview → package. Source, configuration and code must match. Completed checkpoints are hashed. Incomplete stages can run again; `.part` files are not final output. Check active processes before touching a lock. See [troubleshooting](references/TROUBLESHOOTING.md).

## Scope and limits

Supported inputs are long, thin, open, consistently oriented quad disks with no holes or branches. Buckles, thick solids, triangle meshes, welded closed rings and geometry repair are out of scope. The script rejects them instead of silently changing topology.

Default safety limits are 3 million input faces, 150,000 control vertices and 32 components; these are not performance guarantees. Ordered subdivision can reduce the UV solve while preserving every original mesh vertex and quad. End selection can be ambiguous. Curves and ends can retain local UV distortion.

A successful script reports `NUMERIC_PASS_VISUAL_REVIEW_REQUIRED`. Open `UV_layout.png`, `UV_checker.png` and `UV_checker_front.png`; numerical validation is not visual acceptance. MTL/textures are not invented or bundled.

## Evidence and maintenance

The 14 original solver/workflow tests are included. Publication checks, current synthetic results and historical high-resolution evidence are distinguished in [public validation](evidence/public_validation.json). Historical private input is not distributed. Tests of other lower-reasoning models and DCC round trips have **not** been performed. The 12 scenarios in [model_evals.json](tests/model_evals.json) are an evaluation plan, not measured model success rates.

[Changelog](CHANGELOG.md) · [Method](references/METHOD.md) · [Sources](references/SOURCES.md)

Report reproducible issues without uploading private production assets or credentials. Existing repository contribution and usage policies apply; no new license permissions are granted by this skill.
