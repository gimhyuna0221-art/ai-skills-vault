---
name: recursive-capability-improvement
description: Improve a reusable agent method, skill, charter, workflow, prompt, reference set, or evaluation after a failure or repeated correction. Mandatory rule: never repair from model intuition alone. Retrieve internal references first, add external task-matched references when needed, build a bounded challenger, compare against the current champion, and promote only when evidence shows improvement without hard regressions.
metadata:
  version: "1.0.0"
---

# Recursive Capability Improvement

## Core rule

**No reference, no repair.**

A reusable method may not change because the model merely thinks another approach is better.

Use this loop:

FAILURE -> REFERENCES -> HYPOTHESIS -> CHALLENGER -> EVAL -> PROMOTE/REJECT -> ENCODE -> REUSE

## Trigger

Use when:
- the owner says a result is bad, wrong, generic, weak, or unusable;
- an independent reviewer returns REIMAGINE or upstream blocked;
- a deterministic test or CI fails;
- the same correction appears more than once;
- a current method becomes stale;
- a new skill/tool/source directly targets a known weakness;
- a reusable workflow should improve from real task evidence.

Do not use for trivial one-off edits with no reuse value.

## Step 1 — Observe

Capture the external signal:
- owner feedback;
- independent review;
- actual artifact inspection;
- deterministic test;
- real user/customer/market behavior;
- cost/latency/rework;
- source conflict;
- tool failure.

Do not preserve hidden chain-of-thought. Store only observable evidence and compact conclusions.

## Step 2 — Diagnose

Classify the cause:
- EVIDENCE_GAP
- MESSAGE_GAP
- REFERENCE_GAP
- TOOL_GAP
- MODEL_GAP
- PROMPT_GUIDANCE_GAP
- EXECUTION_GAP
- QUALITY_BAR_GAP
- RIGHTS_SAFETY_GAP
- PROCESS_GAP

Do not jump directly from bad result to a random rewrite.

## Step 3 — Reference gate

This is mandatory.

1. Run the Reference Intelligence preflight.
2. Retrieve prior internal references, failure notes, exemplars, profession packs and current project truth.
3. If these are insufficient, stale or contradictory, search external task-matched references.
4. Open the exact source. Search-result snippets alone do not count.
5. Extract what the source actually supports, why it fits this task, what it does not prove, and what concrete rule follows.

If no adequate reference exists, stop with REPAIR_BLOCKED_BY_REFERENCE_GAP.

## Step 4 — Change hypothesis

Record:
- TARGET_FAILURE
- REFERENCE_BASIS
- WHAT_CHANGES
- WHAT_STAYS_LOCKED
- EXPECTED_OBSERVABLE_IMPROVEMENT
- POSSIBLE_REGRESSION

The change must target the diagnosed cause.

## Step 5 — Champion / challenger

Keep the current accepted method as CHAMPION.
Create a bounded CHALLENGER.
Never overwrite the champion first.

A challenger may change prompt/instruction, worker charter, skill, tool route, reference family, script, evaluation, task decomposition, or copy/design system.

## Step 6 — Evaluate

Compare champion and challenger on the smallest representative task that can detect the target improvement.

Possible gates:
- factual fidelity;
- claim honesty;
- task success;
- reference-relative quality;
- actual-pixel/artifact quality;
- human preference;
- owner acceptance;
- cost;
- latency;
- robustness;
- rights/security;
- responsive/channel fit.

Self-score alone cannot pass.

## Step 7 — Promote or reject

Promote only if:
- the target failure materially improves;
- there is no hard regression;
- evidence is stronger than model self-judgment;
- promotion scope matches the evidence.

Otherwise mark REJECTED, WATCH, or RETEST.

## Step 8 — Encode

When promoted:
- update the relevant skill/charter/profession pack;
- update Reference Catalog / Hot Index when broadly reusable;
- add a regression case;
- update failure/prevention ledger;
- preserve rollback pointer.

## Step 9 — Reuse

The next matching task should retrieve the promoted method before new research.

## Quality terminal

Do not use 100% as a model score.

For owner-gated work, completion means required hard gates pass, the actual artifact works in its real medium, independent review passes when required, and owner accepts.

Owner rejection reopens the loop as evidence.

## External method basis

This skill is informed by Reflexion, Self-Refine, DSPy, Promptfoo, and the internal Reference Intelligence system.
These references justify the loop architecture, not universal superiority.

See references/SOURCES.md.