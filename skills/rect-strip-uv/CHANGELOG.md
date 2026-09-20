# Changelog

## 1.1.1 — Corrected dual-resolution delivery and evidence gates, 2026-09-20

- Always retain the UV-only original/high-poly result. Dense input (250k quads OR 500k edges by default) additionally receives a separately verified low-poly companion when safe.
- Correct the unshipped 1.1.0 draft's reversed hierarchy selection. Level 0 is full resolution; increasing indices must decrease quads fourfold. An unchanged duplicate can never satisfy the low-poly contract.
- Preserve original rounded-boundary order, source coordinate/UV samples and metadata boundaries. Gate reduction by every original boundary sample and original surface-vertex interpolation samples, not by a face budget alone.
- Reload and validate low-poly exports, generate cap/wire evidence, and package both real resolutions. Partial completion has an explicit status and exit 4 when safe reduction is blocked.
- Keep the published UV-only implementation byte-for-byte as `scripts/uv_core.py`; add orchestration at the existing `scripts/rect_strip_uv.py` entry point. Keep `parameterize.py`, `mesh_io.py` and the published preview fix unchanged.
- Add dual-resolution regressions and a dense 262,144-quad synthetic CI example. CI receipts bind checks to the actual head SHA and run ID. No private meshes or textures published.
- Add repository agent preflight/write/readback/CI reporting gates and a source-based incident analysis. Current Actions outcomes must be verified separately; historical evidence is not relabeled.

## 1.1.0 — Local draft only; not released to main

- Proposed conditional low-poly output, but the branch selection could reproduce full resolution and the low-poly path lacked independent reload/shape checks.
- Small-example success skipped the low-poly path; the heavy run did not finish. Do not treat that bundle or its compilation check as a validated release. Superseded by 1.1.1.

## Distribution 1.0.1 — GitHub publication, 2026-09-20 (KST)

- Publish a self-contained skill under skills/rect-strip-uv in the existing vault.
- Add Korean/English installation, existing usage terms, publishing benchmark notes and a synthetic-only example generator.
- Fix evidence-image layout: short strips could cover the heading with the previous fixed row height. Rows now follow the actual UV height. UV solving and OBJ preservation algorithms are unchanged.
- The preserved core CLI keeps its original 1.0.0 compatibility identifier. SKILL metadata and these docs identify distribution revision 1.0.1. The exact published script set is identified by code_sha256 in evidence/public_validation.json.
- Preview code changes its hash; use a fresh work directory rather than resuming jobs from the earlier bundle.
- Preserve 14 original automated tests and 12 unexecuted model-evaluation scenarios.
- Separate historical high-resolution evidence from fresh publication tests. Exclude private meshes, production outputs and absolute job paths.
- Retain the repository's existing usage restrictions; no MIT or other new license granted.

## 1.0.0 — Initial portable bundle

- Local UV-only CLI, rectangular bodies and attached ends.
- Topology-based subdivision recovery and UV-only prolongation.
- Checkpoint/resume, output reload verification, checker previews and delivery ZIP.
- 14 automated tests and one historical high-resolution input regression.
