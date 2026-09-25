# Market Research Deliverables Runtime — v1.9.0 commercial parity + alpha orchestration

This module controls the **customer-facing deliverables** for a full FieldPilot market-research engagement. It does not replace the evidence core, method router, claim grammar, fieldwork, ethics, or analysis/calibration rules. It defines what the user receives and how direct-research gaps are handled.

## 1. Product contract

For a full market-research request, FieldPilot's research spine is:

`FINAL_MARKET_RESEARCH_REPORT.md`

The report is the compiled result of the market research. It is not an investment memo and it is not replaced by a single recommendation or next action. For a substantial commercial brief it is delivered inside the professional `CLIENT_DELIVERABLE_BUNDLE` governed by `references/modules/COMMERCIAL_DELIVERABLE_SYSTEM.md`; one undifferentiated report/chat wall is not the complete customer contract.

Decision support, development-priority advice, commitment ceilings, and next actions may appear in `Expert Interpretation / Recommendations`, but they remain **derived advice from the market research**.

## 2. Full-research trigger

Activate this contract when the user asks for the market to be researched for their service/product, asks for a comprehensive competitor/customer/market assessment, or requests a final market-research report — in any wording ("시장조사 해줘", "다 조사해줘", "보고서로 줘"). Full-engagement routing is semantic; it must not depend on the user knowing research vocabulary, and research vocabulary alone ("analysis", "assessment", "viability") does not trigger it. **A broad judgment asked in ordinary language — whether people will use or pay for the product, who the customers are, whether it can be sold, whether it has a viable market — is answered through the kernel's ordinary broad-viability route (`SKILL.md` Route A, `DECISION_CONTINUITY.md` §2.1/§7.3) with the same decision-critical evidence floor, and that answer offers this full deliverable in one line.** The kernel's route boundary governs; this contract never narrows a requested comprehensive deliverable.

If a missing scope field would materially change the decision or research boundary, apply the QUESTION_GATE (`references/modules/PROMPT_SKILL_INDEPENDENCE.md` §3). Whenever work can proceed safely — the normal case — record a labeled `PROVISIONAL_SCOPE`, expose the assumption and its consequence, continue, and put at most two scope questions at the end instead of turning the engagement into an intake interview. Ask before starting only when the product or case cannot be identified at all.

Do not force this contract for a bounded question such as one competitor fact, one channel choice, one failed campaign diagnosis, or one pricing-method question unless the user asks to expand into a full research engagement.

### DEFAULT_PAID_SERVICE_PACKAGE orchestration

For every full engagement, run a `PACKAGE_APPLICABILITY_AUDIT` and compose the existing modules into this
ordered client service. The IDs enforce orchestration order; they do not create a new research methodology.

```text
PAID_CORE_01  decision, product, scope, assumptions
PAID_CORE_02  foundational market definition, boundaries, structure, current context
PAID_CORE_03  customers, jobs/problems, segments, buying roles, demand and payment evidence
PAID_CORE_04  alternatives, substitutes, workarounds
PAID_CORE_05  competitors and comparative positioning
PAID_CORE_06  pricing, monetization and business-model landscape
PAID_CORE_07  distribution, acquisition and channel landscape
PAID_CORE_08  current trends, material changes and WHY NOW
PAID_CORE_09  success cases under a frozen success definition
PAID_CORE_10  failure, low-outcome or near-miss cases and the recorded negative-case search
PAID_CORE_11  success/failure comparison, mechanisms, alternative explanations, replicability
PAID_CORE_12  user-product gap, strengths, weaknesses, differentiation, opportunities and risks
PAID_CORE_13  residual evidence gaps and only the direct research actually needed
PAID_CORE_14  strategy, prioritized action plan, NOT_YET and DO_NOT_BUILD
PAID_CORE_15  findings, interpretation, recommendations, client evidence appendix and professional envelope
```

`FOUNDATIONAL_MARKET_LAYER` is `PAID_CORE_02` through `PAID_CORE_07`. It must be established before
`ADVANCED_CASE_LAYER` (`PAID_CORE_08` through `PAID_CORE_11`) is used to explain outcomes. Cases and trends
may refine the foundation but may not substitute for it. `PAID_CORE_12` through `PAID_CORE_15` then convert
that evidence into the user's gap, uncertainty, action and complete client deliverable.

Each `PAID_CORE_*` area must end in exactly one visible applicability state:
`PRESENT`, `NOT_APPLICABLE`, `NOT_DEFENSIBLE`, or `UNKNOWN`. Every non-`PRESENT` state carries the reason,
the affected decision/claim ceiling, and—when useful—what evidence could change it. Do not pad a package with
invented market size, willingness to pay, trends, cases, causes, regulations, or direct-research results.

After the applicability audit, compile the existing `PAID_CORE_*` results through the v1.9.0 commercial
delivery module. The executive brief and first report pages state the decision and recommendation before
detail; addressable matrices, evidence/source register, data handoff, validation plan, deck/outline and
delivery/revision note remain linked to the same evidence dependencies. This compilation adds no new research
facts and may not raise an applicability or coverage state.

## 3. Required research coverage

Include only applicable sections, but a full engagement must explicitly assess whether each of these is applicable:

- the frozen `CLIENT_DECISION_BRIEF`: decision, decision owner/user, objective and material questions;
- the frozen `SUBJECT_FRAME`: user product/case, target customer/segment, geography where decision-relevant, channel/platform, business model and lifecycle stage, each provenance-labeled;
- service/product and research scope;
- market definition and boundaries;
- market structure and current context;
- customers, jobs/problems, segments, and buying roles where relevant;
- alternatives, workarounds, and substitutes;
- competitors and comparative positioning;
- pricing and monetization landscape;
- distribution/acquisition landscape;
- trends and material changes, with the trend/freshness radar, validated trend states and `WHY_NOW` where timing is material;
- the frozen success definition and case-eligibility criteria, fixed before cases are selected;
- success cases and failure/low-outcome/near-miss cases, plus the recorded negative-case search;
- cross-case common patterns kept distinct from candidate success mechanisms, with the comparator discrimination check;
- causal/alternative explanations and replicability limits;
- service-vs-market assessment and the five-valued user-case gap diagnosis;
- prioritized actions (`P0 / P1 / P2 / NOT_YET`) and do-not-build, each with its evidence basis;
- source discovery and selection strategy, and the evidence independence profile;
- conditional regulatory/jurisdiction context where material;
- remaining evidence gaps;
- direct-research status;
- `COVERAGE_AUDIT` per material question (`ANSWERED / PARTIAL / UNKNOWN`);
- Findings / Interpretations / Recommendations;
- sources, evidence scope, contradictions, and limitations;
- the `PROFESSIONAL_DELIVERY_ENVELOPE` / `RESEARCH_QA_AND_AI_DISCLOSURE` end matter.

`Market size` is included only when it is decision-relevant and supportable. Do not create pseudo-precise TAM/SAM/SOM merely to fill a report section.

## 4. Service-vs-market assessment

A full report must distinguish market facts from the user's service facts, then compare them explicitly.

Required assessment labels when evidence permits:

```text
STRENGTHS
WEAKNESSES
DIFFERENTIATION / POSITIONING
OPPORTUNITIES
RISKS / ENTRY BARRIERS
REPLICABLE SUCCESS MECHANISMS
NON-REPLICABLE ASSETS / ADVANTAGES
UNVERIFIED PRODUCT-SPECIFIC QUESTIONS
```

Every material strength or weakness must be tied to an observable service attribute plus market/competitor/customer evidence. If the user's product facts are missing, read accessible product material first, then mark the comparison as unavailable/UNKNOWN and continue; ask only through the QUESTION_GATE (before answering only when the product cannot be identified at all). Do not invent the product.

### Product-fact provenance firewall

Treat the user's stated service facts as a closed set. A described outcome does not establish the implementation that produces it. In particular, do not infer AI/LLM use, automation method, cloud processing, storage, integrations, data retention, security controls, variable inference cost, or model accuracy unless the user or a verified product source supplied that fact. Keep each such mechanism `UNKNOWN / NOT PROVIDED` and phrase resulting risks conditionally. Never use FieldPilot's own use of AI as evidence that the user's product uses AI.

## 5. Direct-research method choice

### Research ownership boundary

FieldPilot owns all web/desk/existing-source/AI-assisted research that can be answered defensibly with available search, public documents, accessible databases, current vendor/platform sources, or other existing evidence. It researches those questions and gives the evidence, interpretation, limitations, and result to the user; it must not convert web-resolvable work into novice homework. User execution is reserved for irreducible primary evidence that existing sources cannot supply or defensibly infer, such as this product's observed target-user behavior, conversion, actual payment/WTP, usability, or retention.

### Evidence gap before method choice

Only after the existing evidence is exhausted, identify the exact material residual proposition as an `EVIDENCE GAP`. State why existing evidence cannot answer it, what stronger evidence could change, and what no direct-research method can establish by itself. Do not jump from an evidence gap to one preselected method.

### METHOD OPTIONS before CUSTOM KIT

When two or more defensible direct-research routes can address the same material gap, present multiple appropriate METHOD OPTIONS before generating a full kit. For every material option explain, in practical language:

- `WHAT` — the method and exact proposition it tests;
- `EVIDENCE` — evidence it can produce and what it cannot prove;
- `WHERE` — realistic channels/places/environments for this service and target;
- `WHO` — participant/customer/unit criteria and material exclusions;
- `HOW` — operational outline;
- `COST / TIME / EFFORT` — relative burden or a defensible practical tradeoff, without invented exact cost/response/sample claims;
- `RISKS / BIAS` — selection, instrumentation, access, interpretation, or other major failure modes;
- `WHEN TO USE` — why this option may be preferable to alternatives in the user's situation.

If only one route is genuinely defensible, say why the apparent alternatives cannot answer the proposition; do not manufacture options to satisfy a count.

### Recommendation is not selection

FieldPilot may rank or recommend the options and explain why, but the final method choice belongs to the user unless the user explicitly delegates it (for example, `네가 정해줘`). Record recommendation and selection separately. Valid user outcomes are:

```yaml
direct_research_status: DO_IT_SELECTED | SKIPPED_BY_USER
method_choice_status: PENDING | USER_SELECTED | EXPLICITLY_DELEGATED_TO_FIELDPILOT
selected_methods: []
```

If the user has already said `DO IT`, persist that intent and do **not** repeat the old `DO IT / SKIP` A/B gate merely because a report or options page was generated. Instead, if method choice is still pending, present METHOD OPTIONS plus the ability to `SKIP`. If the user has already named a concrete method, treat it as the method selection and proceed to the tailored kit. A defensible combination is allowed when the methods answer complementary parts of the gap; explain why the combination is coherent and do not add irrelevant instruments.

Required interaction shape:

```text
EVIDENCE GAP
→ METHOD OPTIONS
→ FIELDPILOT RECOMMENDATION (optional; not selection)
→ USER CHOICE / DEFENSIBLE COMBINATION / SKIP
→ CUSTOM KIT (only for selected method(s))
```

Requesting a final report is not itself a `SKIP` choice. `SKIP` remains valid at the method-choice stage and must not block the final market-research report. The method choice is offered after the delivered answer or report, never asked before it (QUESTION_GATE); if the user does not respond, `direct_research_status` stays not tested, which is not negative evidence. The user may skip because of access, time, cost, safety, privacy, inability to recruit, or personal preference. Do not shame or block the user solely for skipping.

### Execution and return boundary

FieldPilot informs, recommends, and generates the selected-method materials. The user performs real-world actions that the AI cannot perform. Do not claim FieldPilot itself recruited participants, interviewed them, purchased anything, observed offline behavior, collected payment, or completed fieldwork unless verifiable authorized tooling actually did so. When the user returns REAL evidence, preserve raw provenance, check fieldwork/measurement integrity, integrate it with desk/web evidence, separate observations from interpretation, consider negative evidence and alternative explanations, update claim ceilings, and update the professional market-research report.

## 6. Skip semantics

When the user skips, persist/report:

```yaml
direct_research_status: SKIPPED_BY_USER
unresolved_propositions: []
claims_weakened_or_blocked: []
report_sections_affected: []
maximum_claim_scope_after_skip:
recommended_future_research:
```

Rules:

- `SKIPPED_BY_USER` means **not tested**, not negative evidence.
- Do not infer refusal, no demand, no WTP, no retention, or product failure from the skip.
- Continue all research that remains valid without that direct evidence.
- Generate the final market-research report anyway unless the user cancels the task.
- In the final report, visibly distinguish `verified / supported / inferred / unverified / not tested` according to the controlling evidence rules.

## 7. Research Kit file contract

Only after the user selects one method, a defensible combination, or explicitly delegates method selection may FieldPilot generate the CUSTOM KIT. `DO_IT_SELECTED` with `method_choice_status: PENDING` is not authorization to pre-generate a full method kit. Generate only the files required by the selected method(s); do not create empty, irrelevant, or complete kits for unselected alternatives.

Possible files include:

```text
MARKET_RESEARCH_KIT/
  01_RESEARCH_PLAN.md
  02_RECRUITMENT_GUIDE.md
  03_RECRUITMENT_MESSAGE.md
  04_INTERVIEW_GUIDE.md
  05_SURVEY.md
  06_OBSERVATION_OR_TEST_PLAN.md
  07_TEST_ARTIFACT.md
  08_COMPETITOR_MATRIX.csv
  09_EVIDENCE_TRACKER.csv
  10_RESULT_INPUT_GUIDE.md
```

The exact set depends on the recorded MethodDecision and readiness. A qualitative interview does not require a survey file; an instrumented behavior test does not receive an interview guide unless interviews were also selected; a combination receives only the union of relevant materials. A desk-only task does not require recruitment files.

Every generated execution file must be directly usable by a novice and must preserve the method/evidence limits from the core modules.

Before delivering the kit, run an internal executability check:

- every comparison metric must have a defined collection time and schema for every arm that uses it;
- a control-arm measurement prompt is itself an intervention and must be represented in the design and claim ceiling;
- every field referenced by an analysis or interpretation rule must exist in the supplied record files and be collectible as written;
- if analysis requires per-participant or per-unit derived metrics, supply an analysis worksheet with the computed-metric columns already named or a deterministic parser that produces that table; do not make a novice invent the bridge from raw exports to the stated formulas;
- every allowed value, missing-value code, unit, and denominator must be defined in a codebook or adjacent instructions;
- if a survey uses branching/conditional skip, name the exact feature in the selected survey tool and state the applicable question type/setup path. Do not say only “skip to question N”;
- if the instrumentation defines snooze/disable/reenable or other auxiliary events, the analysis guide must explicitly say whether each event enters each denominator/numerator or a separate state bucket, so two competent users classify the same event the same way;
- duration, allocation, version/settings lock, storage location, retention period, compensation, safety contact, and stop rule must be filled with a recommended default or a concrete user-owned choice rule before recruitment begins;
- positive / negative / ambiguous branches must use preregistered, reproducible operational definitions. Do not invent universal magic numbers, but do define auditable event-level or ordinal rules, minimum interpretable opportunity conditions, and how mixed results map to `CONTINUE / CHANGE / STOP / INCONCLUSIVE` so two analysts cannot silently choose opposite verdicts after seeing the data.
- words such as `majority`, `repeated`, `high`, `low`, `broadly consistent`, `clear pattern`, or `enough opportunities` may not appear in a branch predicate unless the same file defines them as an exact count, formula, ordered category, or event condition. A scoped preregistered count is allowed when justified for this study; present it as a decision rule, not a universal market truth.
- placeholders are allowed only for facts the user alone must supply, such as a real contact address. List those inputs once in a `BEFORE RECRUITMENT` checklist. All other files must use the same filled default; do not leave one file at `0 compensation` while another says `[none/enter amount]`.
- blank data-collection CSV files should be header-only. If an example row is genuinely necessary, add an explicit `row_status=EXAMPLE_ONLY`, use impossible example IDs, and give a deterministic exclusion rule. Never seed `PASS`, `COMPLETED`, observed events, participant IDs, or evidence-looking records while fieldwork is `NOT YET RUN`.
- a planned future interview or observation is not a source. In matrices and trackers mark it `TO_COLLECT / PLANNED_INTERVIEW`; never label a row `participant interview`, `participant report`, or equivalent empirical provenance until returned evidence exists.
- apply data minimization to safety fields. Do not collect a broad `health_status`, diagnosis, or clinical detail for ordinary product research. If a safety flag is necessary, define a narrow nonclinical field such as `safety_stop_event = NONE / PARTICIPANT_STOP / DISTRESS / PRIVACY_RISK / OTHER` and record no diagnostic detail.

If a comparison cannot satisfy these checks, redesign it, downgrade it to descriptive evidence, or leave the affected causal claim `NOT TESTED`; do not ship a non-computable plan.

### Minimum kit requirements

For any direct-research method, the generated set must collectively contain:

- research question / proposition;
- target participant/evidence source;
- recruitment/access route;
- exact user-facing artifact or script where applicable;
- execution steps;
- observation/measurement mechanism;
- record location/schema;
- measurement-health or execution-integrity check;
- interpretation guidance for positive / negative / ambiguous outcomes;
- what the result can and cannot establish;
- stop/escalation/safety conditions where applicable.

Additionally, when the selected method actually collects primary evidence, the kit must record the
following **where applicable to that method** — as design fields to be filled by execution, never as
pre-filled results:

- target population, eligibility criteria and explicit exclusions;
- recruitment source / sampling frame, and the access route's known reach limits;
- sample-size rationale for quantitative designs, **or** a saturation/information-power rationale for
  qualitative designs; no invented minimum n;
- segmentation, quotas or coverage targets where a decision-relevant subgroup must be represented;
- consent, privacy and sensitivity handling where participants are involved;
- fieldwork QC checks and the invalid-response / exclusion rule, defined before collection;
- a deviation log for what actually differed from the plan during execution;
- a pre-specified analysis / synthesis approach, fixed before the data is seen;
- the generalization limit: which population the result can and cannot speak for.

These fields are **design and disclosure fields only**. They do not change the method-choice contract:
`EVIDENCE GAP -> METHOD OPTIONS -> FIELDPILOT RECOMMENDATION (optional) -> USER CHOICE / defensible
combination / SKIP -> CUSTOM KIT` is unchanged, recommendation is still not selection, `SKIP` remains
available and non-terminal, and only the selected method's files are generated. They are also never
retro-filled: an unexecuted design field stays empty or `NOT YET RUN`, and returned `REAL` evidence
stays separate from `PLANNED` / `EXAMPLE_ONLY` / `QA` material. When the kit's fields are later
reported to the client, they populate the sample QC and fieldwork QC items of the delivery envelope
with what actually happened — and nothing that did not.

### User-facing current-fact and source-characterization integrity

- Cross-currency evidence/comparisons must be auditable in the output that uses them: show original amount/currency, conversion rate or defensible basis, rate source, rate date/access date where freshness matters, and the resulting converted value. If a verified current rate is unavailable, state the limitation or avoid the exact/cross-currency comparative claim. Never fabricate a live rate.
- Characterize a privacy/security/store source no more strongly than the source itself. A store statement that the developer does not collect user data does not, by itself, establish local-only storage, no server transmission, no retention, or implementation details. Preserve the source grade and exact claim scope.

## 8. Returned user evidence

When the user returns completed files, notes, survey exports, interview notes, analytics, screenshots, transaction evidence, or other results:

1. preserve raw evidence separately;
2. check provenance, sample/access/fieldwork deviations, and signal integrity;
3. analyze under the active method/analysis contracts;
4. separate Findings / Interpretations / Recommendations;
5. run `RETURNED_RESEARCH_INGESTION` from `references/modules/COMMERCIAL_DELIVERABLE_SYSTEM.md` and update only affected report/bundle component revisions rather than treating the new evidence as an isolated chat answer.

Do not claim FieldPilot executed fieldwork unless verifiable authorized tooling actually did so.

## 9. Final report schema

Default filename:

`FINAL_MARKET_RESEARCH_REPORT.md`

Recommended structure, omitting only genuinely inapplicable sections:

```text
# Final Market Research Report

## 0. Executive Decision Layer
### Decision
### Direct Answer
### Decisive Insights
### Prioritized Recommendations
### Confidence and Conditions
### Strongest Counterevidence
### Material Limitations
### Next Verification
## 1. Executive Summary
## 2. Service / Product and Research Scope
## 3. Research Questions and Methodology
### 3a. Client Decision Brief (frozen)
### 3b. Evidence Plan and Method-Selection Rationale
## 4. Evidence Base and Source Quality
### 4a. Coverage Audit — ANSWERED / PARTIAL / UNKNOWN
### 4b. Source Discovery and Selection Strategy
### 4c. Evidence Independence Profile
## 5. Market Definition and Structure
### 5a. Regulatory and Jurisdiction Context (conditional)
## 6. Market Size / Range (when applicable)
## 7. Target Customers / Jobs / Segments
## 8. Customer Problems, Behavior, Workarounds, Existing Spend
## 9. Competitors and Alternatives
## 10. Pricing and Monetization Landscape
## 11. Distribution / Acquisition Landscape
## 12. Market Trends and Material Changes
### 12a. Trend and Freshness Radar
### 12b. Trend Validation and Trend States
### 12c. WHY NOW — Timing
## 13. Success Cases
### 13a. Success Definition and Case Eligibility Criteria
### 13b. Success Case Register
## 14. Failure / Low-Outcome Cases
### 14a. Comparator Set and Negative-Case Search Record
## 15. Why Those Cases May Have Succeeded / Failed
### 15a. Cross-Case Common Patterns
### 15b. Candidate Success Mechanisms and Discrimination Check
#### Explicit Two-Sided Factor Test and Classification (required before mechanism promotion)
## 16. Replicability for This User
## 17. User Service vs Market
### Strengths
### Weaknesses
### Differentiation / Positioning
### Opportunities
### Risks / Entry Barriers
### 17a. User-Case Gap Diagnosis
## 18. Direct Research Status and Results
## 19. Unverified / Not-Tested Questions
## 20. Findings
## 21. Interpretation
## 22. Expert Recommendations
### 22a. Prioritized Actions — P0 / P1 / P2 / NOT_YET
### 22b. Do Not Build
## 23. Further Research
## 24. Client Evidence Appendix — Sources / Evidence Register
## 25. Limitations / Claim Ceilings
## 26. Professional Delivery Envelope
### Agreed Brief, Scope, Exclusions, Assumptions
### Method / Source-Selection / Coverage Rationale
### Evidence-State Definitions
### Provenance, Publication and Access Dates, Claim Pointers
### Unknowns and Causal Boundaries
### AI / Synthetic / Tool-Use Disclosure
### Human Oversight and Accountability
### Research QA — Freshness / Dedup / Inclusion-Exclusion / Verification
### Sample and Fieldwork QC (when applicable)
### Ethics / Privacy / Confidentiality Boundary (when applicable)
### Research Ethics Scaffolding for Proposed Primary Research (when people are involved)
### AI Processing of Client Material — Confidentiality Controls
### Research Timing Log
### Reproducibility and Traceability Notes
```

For a substantial brief, section 0 and the essential executive summary occupy the first one to two
pages/slides of the bundle. The report follows a decision narrative from scope to evidence, analysis,
recommendation, action, limitations, and appendix. Decision-useful competitor/price/segment/case/risk/action/
evidence-gap tables precede long prose where applicable. Every material table/chart follows the finding-led
title, source/date, claim-state, and `SO WHAT / IMPLICATION` contract in the v1.9.0 module.

The client evidence appendix is not a second provenance system. It is the readable rendering of the existing
source discovery record, evidence register, coverage audit, timing log and professional envelope. For every
decision-relevant claim it exposes the source role, publication/access date where available, independence or
conflict context, coverage, contradiction, limitation and AI/tool disclosure in plain language. Missing evidence
remains visible; internal state tokens may be retained in a labeled technical appendix but are never pasted into
the client narrative as unexplained runtime output.

The v1.9.1 rendering path is governed by
`references/modules/CLIENT_VISIBLE_EVIDENCE_PROVENANCE.md`. Material claims display source keys that resolve to
exactly one delivered register record. Access date-times are actual RFC 3339 execution values, never blank,
placeholder, example, or stale hardcoded dates. Each material record exposes an observed direct locator or an
explicit truthful locator limitation, plus publication/observation state, source role/character, claim boundary,
corroboration state, evidence state, and claim ceiling. `PROVENANCE_OUTPUT_GATE: PASS` is required before the
client bundle is delivered.

For v1.9.3, a `FINAL_MARKET_RESEARCH_REPORT` (or delta report) is not exempt from the other delivery gates
merely because it was produced inline rather than as a "substantial commercial engagement bundle." Before
delivery, also resolve `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`
(`references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md`) and any triggered v1.9.0-v1.9.2 gate
(`LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE`, `RETRACEABLE_LOCATOR_FALLBACK_GATE`, `VALIDATION_RESOLUTION_GATE`,
`LITERATURE_HIERARCHY_COMPLETENESS_GATE`) per `references/delivery/PROFESSIONAL_DELIVERY_ENVELOPE.md` §6.

For v1.9.4, before the same delivery moment, also resolve `BOUNDED_BEHAVIORAL_CLOSURE_REPAIR`
(`references/modules/BOUNDED_BEHAVIORAL_CLOSURE_REPAIR.md`): every module this task's routing triggered is
actually loaded and applied (not covered by the governing-layer summary alone), a whitespace/no-direct-
competitor claim carries a completed `DIRECT_COMPETITOR_RECALL_CLOSURE`, any commercial claim names its
actual `commercial_evidence_ladder` rung, third-party pricing rows in a current comparison table are
current-first-party or explicitly labeled historical, and the closing instruction names exactly one
immediate action when the user explicitly asked for one.

For v1.9.5, once the report reaches the delivery moment above with a PASS, render it via
`PROFESSIONAL_REPORT_RENDERING_CONTRACT` (`references/modules/RENDERING_CONTRACT.md`) into
`report.html` and, when a local browser is available, `report.pdf`, both derived from this
same finalized Markdown content with none of it rewritten, summarized, or renumbered. Tell
the user where `report.md`/`report.html`/`report.pdf` are — do not require them to ask for a
file separately.

For v1.9.6, before that render, the same Markdown source additionally marks a
`## CUSTOMER_DECISION_REPORT` part — opening with the plain-language what/decision/why/next-
action summary, then competitor/substitute comparison with confirmed-vs-unknown overlap
classification, commercial evidence, a practical-fit section when material, counterevidence,
limitations, and sources — separate from a `## AUDIT_METHOD_PROVENANCE_APPENDIX` part carrying
internal gate names, package-internal file paths, YAML implementation blocks, and version-
regression history (`references/modules/BUYER_FACING_DECISION_REPORT.md`). `report.html`/
`report.pdf` render the two parts with different visual hierarchy while remaining subject to
the same `renderer_consistency_gate`, plus the new `buyer_facing_structure_gate`,
`overlap_overclaim_gate`, and `practical_feasibility_gate`.

The report must not pad unavailable sections with generic prose. Mark `NOT APPLICABLE`, `NOT TESTED`, `SKIPPED_BY_USER`, or `INSUFFICIENT EVIDENCE` where appropriate.

This anti-padding rule governs the v1.7.2 subsections with equal force. A market with no defensible comparable cases produces `INSUFFICIENT EVIDENCE` plus the disclosed search boundary in 13b/14a — never a generic archetype, an unnamed "typical competitor", or a list of failure risks standing in for a real failure case. A decision where timing is not material produces a short `NOT APPLICABLE` with its reason in 12c, not invented urgency.

## 9c. v1.7.2 market-intelligence sections — what each must contain

These sections are governed by `references/modules/`. They are rendered where decision-relevant and marked `NOT APPLICABLE` with a reason where they are not.

- **4b / 4c** — the `SOURCE_DISCOVERY_RECORD` and the independence profile from `references/modules/SOURCE_DISCOVERY_AND_SELECTION.md`. A cited list is not a discovery strategy. `INDEPENDENT_EVIDENCE: SEARCHED_NOT_FOUND` is a legitimate outcome that lowers the ceiling on market-structure claims; it is never repaired by promoting a derivative source. No minimum source count is introduced, and counts remain description rather than sufficiency.
- **5a** — the conditional check from `references/modules/REGULATORY_CONTEXT_CHECK.md`, with one of the four states. When geography is `UNRESOLVED` and regulation is material, surface the dependency and its decision impact; do not omit it and do not guess a jurisdiction.
- **12a / 12b / 12c** — the radar, trend validation and `WHY_NOW` from `references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md`. Every material current claim carries as-of/access/source dates, geography, source type, independence and corroboration. Trend states are ordinal and justified in words; no trend score, percentage or invented threshold. `NO_CURRENT_TIMING_ADVANTAGE` is a valid and often correct conclusion.
- **13a / 13b / 14a / 15a / 15b / 17a / 22a / 22b** — the case, factor, mechanism, gap and priority objects from `references/modules/MARKET_CASE_COMPARISON_AND_GAP.md`. Success is defined before cases are selected; the negative-case search is recorded whether or not it found anything; `COMMON_PATTERN` and `LIKELY_SUCCESS_MECHANISM` stay distinct. Section 15b contains one explicit row per material candidate success factor with named evidence and `PRESENT / ABSENT / UNKNOWN / NOT_COMPARABLE` states on both outcome sides, a `SHARED_NON_DISCRIMINATING / PLAUSIBLY_DISCRIMINATING / UNKNOWN_UNTESTABLE` classification, directly compared alternative explanations and the evidence ceiling. Section 17a explicitly reconnects each material user-case row to both the successful and negative/low-outcome findings. A difference from the success set is not automatically a weakness; an action whose evidence basis is `UNKNOWN` may only be a validation action.
- **Section 18 and 26** — direct-research status and the ethics scaffolding for any recommended people-involving method, per `references/modules/RESEARCH_ETHICS_DESIGN_SCAFFOLDING.md`. Ethics fields are design fields; unexecuted stays `NOT YET RUN` with a truthful `fieldwork_status`.

None of these sections may weaken the negative evidence, substitutes, falsifiers, claim ceilings, STOP/HOLD/PIVOT content, evidence-state separation, or the direct-research method-choice contract that the body already carries.

## 9a. Decision brief, evidence plan and coverage audit

Before substantive evidence collection, freeze a `CLIENT_DECISION_BRIEF` per `references/delivery/CLIENT_DECISION_BRIEF.md` and build an `EVIDENCE_PLAN` for the material questions per `references/delivery/EVIDENCE_PLAN_AND_COVERAGE_AUDIT.md`. At synthesis, produce the `COVERAGE_AUDIT`.

- Every material finding, interpretation and recommendation in the report must trace to a frozen objective or research question.
- Brief fields that were inferred or assumed rather than stated are rendered with their label so the user can correct them. Material values are never silently invented.
- Report sections inherit their claim ceiling from the coverage state of the questions they rest on. A `PARTIAL` question does not produce an unqualified section.
- Source counts may be reported as description. They are never presented as evidence of sufficiency, and no minimum source count is imposed.
- A `UNKNOWN` state that requires real-world primary evidence routes into the existing evidence-gap and method-choice flow in section 5. It is never resolved by speculation, and `SKIPPED_BY_USER` does not raise it.

## 9b. Professional delivery envelope — required end matter

Every delivered report carries the `PROFESSIONAL_DELIVERY_ENVELOPE` / `RESEARCH_QA_AND_AI_DISCLOSURE` end matter defined in `references/delivery/PROFESSIONAL_DELIVERY_ENVELOPE.md`, rendered as section 26.

- Items that do not apply to this engagement are marked `NOT APPLICABLE`, `NONE`, or `NOT PERFORMED`. They are not omitted.
- The AI/tool disclosure states the actual execution mode of this run and which stages were AI-assisted, and separates what was independently verified against a source from model synthesis and inference.
- The human-oversight record states only what actually happened: `NONE`, `USER_DECISION`, `USER_SUPPLIED_EVIDENCE`, or `INDEPENDENT_HUMAN_REVIEW`. **Never invent a human reviewer, professional sign-off, consent, certification, QC pass, respondent, fieldwork event, or verification.** FieldPilot's own self-audit is not human review. `NONE` is a legitimate and frequently correct answer.
- QA that was not run is recorded as `NOT PERFORMED` with its claim-ceiling effect. Recording an unrun check as performed is a fabrication in the same class as a fabricated source.
- Every material recommendation in section 22 carries its `IMPACT_VERIFICATION` chain: `ACTION -> MECHANISM -> OBSERVABLE METRIC/STATE -> MEASUREMENT CONTEXT -> DECISION CHECK -> CAUSAL CAVEAT`, with no invented numeric thresholds.
- Section 0 and section 26 summarize; they never weaken the negative evidence, substitutes, falsifiers, claim ceilings or STOP/HOLD/PIVOT content in the body.

## 10. Final report quality bar

A paying user should be able to answer these after reading the report:

- What market am I actually entering?
- Who is the likely customer/buyer and what are they already doing?
- What are the real alternatives and competitors?
- How are comparable products priced, monetized, and distributed?
- What appears to have helped similar products succeed or fail, and what is actually replicable?
- Where is my service stronger or weaker than the market/alternatives, and why?
- Which conclusions are well-supported and which are still uncertain?
- What direct research did I do, skip, or still need?
- What should I improve, investigate, or try next **because of the market evidence**?
- Which source supports each material market claim and what are the limitations?
- Which decision was this research actually for, and what was in and out of scope?
- For each material question, was it answered, partially answered, or left unknown — and what is still uncovered?
- What did AI actually do in producing this, and did any human review it?
- What counts as success here, who decided that, and why do these specific cases qualify?
- Which comparable products did badly, and was anyone actually looking for them?
- Which shared traits of the winners survive a check against the ones that failed?
- For each material candidate factor, what is actually evidenced on the successful and negative/low-outcome sides, which factors are shared versus plausibly discriminating versus untestable, and what alternative explanations remain?
- How does my case compare with both outcome sides rather than only with market leaders?
- Where is my case genuinely different rather than simply worse, and which differences do not matter at all?
- What do I do first, what do I deliberately not build yet, and what evidence is each of those resting on?
- What is actually moving in this market right now, how do I know it is more than a spike, and is there any reason to act now rather than later?
- If this research recommends that I talk to or observe people, what do I owe those people before I start?

A report that is mostly generic methodology education, a scorecard, an unsupported success probability, or a one-page next-action memo fails this contract.

### Client-facing register

Internal runtime and state tokens do not appear in client-facing prose. Their meaning is rendered in plain language instead, per the client-facing register rule in `references/delivery/PROFESSIONAL_DELIVERY_ENVELOPE.md` section 7. Translation is required; deletion of the underlying disclosure is prohibited, and the rule never licenses softening an unfavourable status.

### Comparable-case and current-fact integrity

- When success and failure/low-outcome cases are requested or material, use named, source-backed cases. A generic list of failure risks is not a substitute for a comparable failure, shutdown, withdrawal, pivot, stalled/weak outcome, or documented low-performance case.
- Prefer a close comparable. If only an adjacent case is supportable, state why it is adjacent, which mechanism transfers, and which differences block transfer. If no defensible case can be found after a bounded search, disclose the search boundary and keep the section `INSUFFICIENT EVIDENCE`; never invent a case.
- One close confirmed negative comparator is enough to perform the bounded two-sided factor test when the report exposes the thin-negative-evidence ceiling. Unconfirmed or excluded negative cases stay in the search/exclusion record and are never promoted to facts. Silence about a factor is `UNKNOWN`, not evidence that it was absent.
- For current prices, plans, user counts, and product status, record the source URL, access date, plan name, billing cadence, currency, and whether the fact came from an official page, a search snippet, or another source. Do not turn an inaccessible or ambiguous page into a precise price.
- Reconcile contradictions before reporting. If sources or fresh checks disagree, show both scoped observations and explain the unresolved difference; do not silently choose whichever value makes the comparison easier.

## 11. Output and file-generation rule

Run the v1.9.0 `ARTIFACT_CAPABILITY_AUDIT` before promising a format. When the environment supports both
creation and verification, render the useful report/bundle/data/deck components as actual files and verify
their identity, non-emptiness, expected structure and readable output. When those capabilities are unavailable,
produce the complete structured content package, exportable table/schema, exact chart specifications and
executive deck outline, and state which files were not materialized. Do not pretend a file or verification exists.

## 12. Evidence and commercial boundaries

- Market research quality does not prove FieldPilot itself has market demand or WTP.
- Market evidence does not prove this user's product demand.
- Recommendations may discuss further development, resource commitment, or priority, but they must remain tied to the market research and claim ceilings.
- The final report is **market-research output**, not regulated investment advice and not a guarantee of success.
