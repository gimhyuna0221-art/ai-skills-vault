# Changelog

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
