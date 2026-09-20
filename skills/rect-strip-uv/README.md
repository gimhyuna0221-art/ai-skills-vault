# Rect Strip UV — 1.1.1

**UV-only original, plus a checked low-poly companion when the input is dense.**

[한국어](README_KO.md) · [Agent instructions](SKILL.md) · [Low-poly method](references/LOWPOLY.md) · [Changelog](CHANGELOG.md)

The high-poly result preserves original vertex records, quad connectivity/order, normals, groups and material declarations. Bodies become long rectangular UV strips with attached ends. Dense input additionally gets a separate, strictly smaller low-poly companion; the original is never replaced.

## Install / run

For the repository owner or separately authorized users only; [existing usage terms](LICENSE.txt) remain unchanged. Public visibility is not an open-source license.

```bash
npx skills add gimhyuna0221-art/ai-skills-vault --skill rect-strip-uv
python -m pip install -r requirements.txt
python scripts/rect_strip_uv.py doctor
python scripts/rect_strip_uv.py run --input "belt.obj" --work "belt_uv_job"
```

The optional installer requires Node.js and does not install Python dependencies. Manual host installation uses the entire `.agents/skills/rect-strip-uv/` folder. Installation on every agent host is not claimed. Python 3.11+, file tools and image review are required; no DCC app or API key is needed. On Windows, `py -3` may replace `python`. Keep input outside the work directory.

Automatic low-poly triggers at **250,000 quads or 500,000 edges**. These configurable thresholds are workflow defaults, not universal hardware limits. Default target: 40,000 quads, subject to shape/metadata gates. Use `--lowpoly off` only for an explicit UV-only override. `--also-lowpoly-auto` is a compatibility alias for the default. Optional `--also-01` adds a uniformly scaled UV alternative at each delivered resolution.

Outputs: `delivery/belt_UV_tile.obj` (original/high-poly), `delivery/belt_lowpoly_UV_tile.obj` when safely reducible, per-resolution QA, `DELIVERY.json`, previews, and `rect_strip_uv_delivery.zip`. Repeat UVs outside 0–1 are intentional, not a multi-image UDIM set. A resolution's `_tile` and `_01` outputs are alternative UV layouts.

## Rounded ends are not square remeshes

Only proven original four-child subdivision blocks are coarsened. The surviving positions and UV samples come from the original; no smoothing, UV quantization, generic decimation, welding, holes, thickness or new folds. Levels are ordered full-resolution first and must decrease by a factor of four. Metadata seams cannot be crossed.

Every original boundary vertex is checked against its corresponding surviving chord. Original surface vertices are checked against hierarchical bilinear interpolation. Defaults: maximum boundary error / strip width <= 1%, surface sample error / width <= 3%. These are sampled checks, not a continuous Hausdorff guarantee. A component can retain extra density when its next candidate fails. Low-poly normals are recomputed by the importing host; original normals remain in high-poly.

If no strictly smaller safe result exists, return the high-poly output with `HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED` (exit 4), never a fake low-poly duplicate. Processing failures use exit 2; missing dependencies use exit 3.

## Resume / evidence

```bash
python scripts/rect_strip_uv.py status --work "belt_uv_job"
python scripts/rect_strip_uv.py resume --work "belt_uv_job"
```

Stages: inspect → unwrap → export → verify → preview → lowpoly → package. Source/code/config must match; completed artifacts are hashed. Changed versions need fresh work directories. Check actual process state rather than repeatedly restarting a timed-out stage.

`NUMERIC_PASS_VISUAL_REVIEW_REQUIRED` is not visual acceptance. Open the three high-poly UV previews and, when present, `LOWPOLY_checker.png`, `LOWPOLY_layout.png`, `LOWPOLY_ends.png`. Both exports are reloaded and checked independently. The ZIP contains both actual resolutions when the low-poly branch succeeds.

```bash
python -m unittest discover -s tests -v
python examples/make_dense_example.py --output demo-input/dense.obj
python scripts/rect_strip_uv.py run --input demo-input/dense.obj --work dense-job
```

The dense synthetic rounded strap has 262,144 quads and tests the actual automatic threshold. User geometry is not published. Validate the exact commit's Actions jobs and generated CI receipt; historical `evidence/public_validation.json` is not fresh evidence for this version.

Scope remains thin, open, hole-free, long quad disks; buckles, solids, triangles, welded rings and repair are unsupported. Existing limits remain 3 million input faces, 150,000 control vertices and 32 components. Lower-reasoning-model performance, DCC round trips, host installation and visual review are separate from automated solver tests. Status remains `stable draft`.

[Publishing benchmarks](references/BENCHMARKING.md) · [Incident/prevention](references/INCIDENT_2026-09-20.md) · [UV method](references/METHOD.md) · [Sources](references/SOURCES.md)
