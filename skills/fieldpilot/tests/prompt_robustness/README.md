# FieldPilot prompt-robustness suite

Behavioral evaluation for v1.9.9-rc04 **Prompt-Skill Independence**: does a buyer who writes badly,
briefly, emotionally or without research vocabulary get the same investigation, decision quality
and user burden as a buyer who writes like an expert?

Design follows CheckList behavioral testing (Ribeiro et al., ACL 2020): **INV** — same case,
different wording, the floor must not drop; **DIR** — adding or removing one fact changes only
the dependent part; **MFT** — minimum functionality for hard cases. Grading follows Anthropic's eval
guidance: code-graded wherever possible, LLM-rubric-graded only for judgment (coverage depth,
plain language), with the judge blind to which version produced a reply.

All products in `cases.json` are fictional and different from the frozen LockerDesk benchmark case,
so no rc04 output can be mixed into the running rc03 paid-competitor benchmark.

## Families

| Family | What it tests | Cases |
|---|---|---|
| F1 same intent / different language (INV) | expert English vs short, messy, solution-question and typo-heavy Korean for one launched product | `F1_QUOTE` × 5 variants |
| F2 missing context (MFT + variance) | no geography (3 samples per arm, the rc03 RUN-1/RUN-2 divergence pattern on a different product), Korean without geography, no price, no repo | `F2_GEO`, `F2_GEO_KO`, `F2_NOPRICE`, `F2_NOREPO` |
| F3 user burden (MFT) | competitor list, market size, target customer — must be researched, not assigned | `F3_*` |
| F4 friendly delivery (INV on register) | "쉽게 설명해줘" must not become thinner research | `F4_SIMPLE` |
| F5 hard cases (MFT) | unknown product, referenced-but-missing evidence, explicit narrow scope, user asks to be asked first | `F5_*` |

## Protocol

1. Prepare one folder per arm with the skill exactly as published (`rc03` = `main` at the tested
   commit, `rc04` = candidate branch head). Record commit SHAs.
2. For every case × variant × sample, start a **fresh session** (no memory, no project documents,
   no connectors) with the same model and settings for both arms. The session loads the skill from
   the arm folder only. Paste the variant prompt as the user's first message.
3. Save the reply verbatim as `outputs/<case>__<variant>__<arm>__<sample>.md`. If the session asks
   a question first, save that first turn as the reply — that is the measured behavior.
4. `python run_eval.py blind --outputs outputs --dest blind --mapping sealed_mapping.json` and give
   only `blind/` plus `rubric.md` to a judge in a fresh session. Keep the mapping sealed until the
   judge's scores are locked.
5. `python run_eval.py report --outputs outputs --rubric-scores judge.json --mapping sealed_mapping.json --out-md report.md --out-json report.json`.

## Predeclared rc04 gates (fixed before any run; do not change after seeing results)

| Gate | Criterion (rc04 arm) |
|---|---|
| G1 novice equivalence (F1) | 0 blocking first turns; every variant FLOOR ≥ 0.75; novice/expert FLOOR ratio ≥ 0.85; FLOOR spread ≤ 0.20; ≤ 2 user questions per reply; no homework, mode-menu or findable-fact asks |
| G2 geography (F2_GEO, F2_GEO_KO) | 0 blocking first turns across all samples; no unconditioned market assumption; geography named as unknown with its effect |
| G3 user burden (F3) | no homework requests, no findable-fact asks; mean R14 ≥ 1.5 |
| G4 friendly delivery | F4 FRIENDLY ≥ 0.75 with FLOOR ≥ 0.75; no internal-token leaks in novice-register replies |
| G5 hard cases (F5) | unknown product and missing evidence: ask first with ≤ 2 questions (unknown product includes an example answer) and nothing fabricated; narrow: 0 questions, no broadened engagement, source given; ask-first request: ≤ 2 questions |
| G6 no expert regression | rc04 FLOOR on the expert variant ≥ rc03 FLOOR on the expert variant − 0.10 |

rc03 results are the BEFORE baseline; they are reported, not gated.

## Limits

Behavioral runs are samples of a stochastic system. One sample per variant (three for `F2_GEO`)
supports bounded, directional evidence — like the rc02 T1–T6 validation — not a statistical
guarantee. Code graders are heuristics; the blind rubric is the judgment layer. A harness host
(an agent session loading the skill from a folder) is not identical to a production chat host,
so production re-runs with the same prompts are the stronger check.
