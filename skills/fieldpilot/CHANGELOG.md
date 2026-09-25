# FieldPilot Changelog

## v1.9.9-rc04 — Prompt-Skill Independence (candidate)

Product requirement: a buyer who does not know research vocabulary or prompt writing must not get a shallower investigation, weaker evidence, a worse judgment, more questions or more homework than a buyer who does. "개떡같이 말해도 찰떡같이 알아듣습니다" is now a runtime contract.

- Added `references/modules/PROMPT_SKILL_INDEPENDENCE.md`, loaded first in every route:
  - `CASE_FRAME` request restoration: typos, spacing, slang, banmal, fragments, mixed languages, vague referents, several questions in one message, worried questions, and solution questions whose premise must be checked (the XY problem).
  - `COVERAGE_FLOOR` set by the case state, not by vocabulary, with a universal decision floor and case rows (alternatives, product state, money, post-launch causes, payment, channel, local, delta, narrow, full).
  - `QUESTION_GATE` — one deterministic rule for asking: FINDABLE → look it up; INFERABLE → labeled assumption; USER_OWNED → `ASK_AFTER` a complete answer by default, `ASK_FIRST` only when no useful bounded answer is possible; ≤2 questions; never ask for modes, formats, permission to research, findable facts or research-brief definitions.
  - `FRIENDLY_EXPERT` delivery as the default register: direct answer first, one-line restored case, plain headings, no internal tokens as main text, protective distinctions kept in plain words.
  - `EXPERT_TWIN` equivalence check before sending.
- Kernel (`SKILL.md`): new STEP 0 and invariants 16–18; invariant 15 geography timing fixed (bounded answer first, geography question at the end — no guessing, no blocking); plain-language delivery is the default rather than opt-in; Route B selection follows an explicit research/report request in any wording, research vocabulary alone does not select it, and broad Route A answers offer the full report in one line.
- Aligned the scattered question rules to the gate: lifecycle stage, geography (kernel, Korea-local, regulatory, competitor method), product-fact gaps, monetization facts, Route B intake (the user is no longer asked to formulate the decision/owner/deadline), provisional scope, market prior, analysis/reporting, runtime-core novice rules, channel prerequisites, and direct-research method choice (post-answer option only).
- Lifecycle router routes by the restored case; "should I advertise?" gets a premise check before channel advice.
- Description adds everyday trigger phrases so casual asks activate the skill without `/fieldpilot`.
- Worked example card rewritten plain-first with identifiers in parentheses.
- Added static contract + policy lint tests and a behavioral prompt-robustness eval suite (same intent / different language, missing context, user burden, friendly delivery, hard cases) with graders and a runner.

Unchanged: truth before fluency, UNKNOWN, provenance, counterevidence, competitor recall and gap safeguards, commercial/WTP ceilings, product-state and coverage honesty, geography no-guessing, Korea-local coverage, demand-vs-distribution diagnosis, signal integrity, first-paid-proof discipline, returning-evidence continuity, the full professional route, approval gates for external execution, and the role boundary. No score, guarantee or new mandatory research is added.

## v1.9.9-rc03 — Lifecycle Decision Routing

- Added one lifecycle router for plain-language `/fieldpilot` use across:
  - idea validation;
  - MVP / build decisions;
  - pre-launch / pre-sell;
  - launched with no response;
  - launched with interest but no payment;
  - monetizing products;
  - returning evidence / decision updates.
- Wired existing demand-vs-distribution diagnostics, signal-integrity checks, channel routing, pricing/payment logic, competitor/substitute research, product-state comparison and decision surfaces into the lifecycle route.
- Added post-launch guards so "no response" is not collapsed into a single product or advertising cause.
- Added product-specific promotion/channel output with one first route, one fallback, an exact test and measurement logic.
- Added explicit guardrails for red-ocean, niche, customer and jackpot/no-hope claims.
- Added runtime contract tests for lifecycle routing and updated Korea-local tests to expect rc03.
- Updated public README descriptions and usage examples.

This release does not add a success-probability score, guaranteed advertising channel, PMF/WTP certification, direct code editing, autonomous spend, or proof of a niche from search absence.
