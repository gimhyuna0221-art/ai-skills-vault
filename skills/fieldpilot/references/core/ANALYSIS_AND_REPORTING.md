# Analysis, Calibration, and Reporting Runtime

Load this module after eligible evidence exists and whenever FieldPilot creates an analysis, Finding, Interpretation, Recommendation, decision update, or report view. It operationalizes `R-NEG-01`, `R-TRI-01`, `R-CAUSAL-LANG-01`, `R-FIR-01`, `R-NUMERIC-01`, `R-AUDIT-01`, and `R-NOVICE-01` from `EXPERT_CORE_RULES.md`.

This module never upgrades evidence. The active proposition, Required Evidence Contract, method decision, sample/fieldwork revisions, ethics decision, and claim-grammar module remain controlling dependencies.

## 1. Entry gate

Before analysis, require active revision-pinned IDs for:

```yaml
analysis_entry:
  decision_id_and_revision:
  uncertainty_id_and_revision:
  proposition_id_and_revision:
  evidence_contract_id_and_revision:
  domain_preflight_id_and_revision:
  method_decision_id_and_revision:
  sample_plan_id_and_revision:
  fieldwork_plan_id_and_revision:
  readiness_decision_id_and_revision:
  ethics_review_id_and_revision:
  evidence_item_ids_and_revisions: []
```

Fail closed when a required dependency is missing, stale, withdrawn, deleted, or superseded. Historical comparison may reference an inactive object, but it cannot support a new claim without a new eligible calibration.

Evidence marked `SIMULATED/HYPOTHETICAL`, `SYNTHETIC_GENERATED`, or otherwise `NOT_HUMAN_EVIDENCE` stays in a separate analysis partition. It must not enter human denominators, customer quotations, saturation, WTP, behavior, payment, or market-evidence summaries.

## 2. Analysis-plan compiler

Create or revise the plan before examining outcome data when pre-specification matters. Exploratory work is permitted only with `analysis_mode: EXPLORATORY` and separate outputs.

```yaml
analysis_plan:
  id_and_revision:
  proposition_id_and_revision:
  analytic_aim_or_estimand:
  analysis_mode: CONFIRMATORY | EXPLORATORY | DESCRIPTIVE | DIAGNOSTIC
  included_evidence_rules: []
  excluded_evidence_rules: []
  measures_or_codebook:
  transformations: []
  comparison_model_or_analytic_approach:
  unit_and_nested_structure:
  uncertainty_plan:
  missingness_and_attrition_plan:
  subgroup_plan:
  multiplicity_or_sequential_plan:
  sensitivity_plan: []
  expected_disconfirming_result:
  strongest_plausible_rivals_before_analysis: []
  deviations_requiring_disclosure: []
  human_and_ai_roles:
```

Every transformation records input IDs, procedure/code/formula and version, actor, timestamp, and output ID. Preserve raw evidence separately. A favorable result never cures an instrument, assignment, exposure, sample, missingness, or execution failure.

## 3. Negative-case and alternative-explanation gate

Run this gate before evidence calibration and again before Recommendation. Search proportionately to decision stakes and relevant variation; never impose a fixed negative-case count.

The pass must explicitly inspect, when applicable:

- non-users, failed cases, refusals, no-response, dropouts, churn, refunds, complaints, adverse outcomes, and withdrawals;
- contradictory cases, analyses, methods, and credible external sources;
- missing or undercovered roles, populations, segments, sites, channels, times, network positions, and potentially harmed groups;
- founder, client, sponsor, analyst, moderator, and model incentives toward a favorable conclusion;
- measurement error, selection, nonresponse, confounding, attrition, instrumentation, novelty, assistance, mandated use, seasonality, interference, and chance;
- the strongest plausible alternative to every material Interpretation;
- evidence that would reverse, defer, stop, or materially narrow the Recommendation.

```yaml
negative_case:
  id_and_revision:
  challenged_finding_or_interpretation_ids: []
  case_group_or_rival:
  type: CONTRADICTORY_CASE | MISSING_GROUP | HARM | EXECUTION_FAILURE | RIVAL_EXPLANATION | CONFLICTED_SOURCE
  challenge_attempted:
  evidence_ids: []
  status: SUPPORTED | MIXED | PLAUSIBLE | WEAKENED | NOT_SUPPORTED | NOT_TESTED
  calibration_effect:
  residual_test_needed:
```

`NOT_TESTED` is not false. If evidence supports a rival, use `SUPPORTED` or `MIXED`; do not soften it to `PLAUSIBLE`. Positive synthesis is blocked until linked negative evidence, omissions, limitations, and unresolved alternatives are visible.

## 4. Calibration compiler

Compare what actually happened with every dimension of the active Required Evidence Contract. Do not replace dimensions with one unexplained score.

```yaml
evidence_calibration:
  id_and_revision:
  proposition_id_and_revision:
  evidence_contract_id_and_revision:
  method_sample_fieldwork_revisions: []
  analysis_result_ids: []
  negative_case_ids: []
  support_state: SUPPORTS | WEAKENS | MIXED | INCONCLUSIVE | NOT_TESTED | INVALID_EVIDENCE
  dimension_results:
    construct:
    directness:
    sampling:
    comparison:
    context:
    temporal:
    precision:
    replication:
    provenance:
    ethics:
  planned_vs_actual_execution:
  source_independence_and_conflict:
  robustness_and_sensitivity:
  internal_validity:
  transfer_or_transport:
  integration_relation: NONE | CONVERGENCE | COMPLEMENTARITY | SEQUENCE | DISSONANCE_TEST
  unresolved_divergence: []
  maximum_claim_scope:
  material_limitations: []
  unresolved_alternatives: []
  supported_claim_envelope:
```

Use `INCONCLUSIVE` only when eligible collected evidence cannot discriminate at the required level. Use `NOT_TESTED` when the proposition was not addressed. Use `INVALID_EVIDENCE` when a hard design, provenance, ethics, or execution defect makes the evidence ineligible for that claim.

Multiple methods do not automatically increase confidence. Record their integration relation. If they disagree, preserve the divergence, propose diagnostic explanations, and open a next uncertainty. Never average away conflict or select the favorable result.

## 5. Findings / Interpretation / Recommendation compiler

These are different durable objects. Generate them in dependency order even when the novice-facing view displays the Recommendation first.

### 5.1 Finding

```yaml
finding:
  id_and_revision:
  proposition_id_and_revision:
  bounded_statement:
  evidence_ids_and_revisions: []
  analysis_result_ids_and_revisions: []
  calibration_id_and_revision:
  support_state:
  population_context_time:
  estimate_or_pattern:
  uncertainty:
  negative_or_disconfirming_evidence_ids: []
  limitations: []
  maximum_claim_scope:
  claim_gate_decision_id_and_revision:
```

A Finding says only what calibrated evidence supports. Reject `should`, an action, a preferred strategy, an unmeasured causal mechanism, or a value judgment. Counts stay bounded to their units and denominators. Every substantive sentence must pass `CLAIM_GRAMMAR.md`; every material number must pass its Numeric Claim Guard.

### 5.2 Interpretation

```yaml
interpretation:
  id_and_revision:
  finding_ids_and_revisions: []
  meaning:
  inferential_steps: []
  alternative_explanation_ids: []
  transfer_or_transport_assumptions: []
  decision_relevance:
  residual_uncertainty_ids: []
  analyst_and_ai_roles:
```

An Interpretation may explain possible meaning. It cannot introduce a new count, quote, source, observed behavior, or causal fact; create a Finding first. Label a plausible mechanism as plausible unless measured. Reject recommended actions, imperatives, and hidden preferences.

### 5.3 Recommendation

```yaml
recommendation:
  id_and_revision:
  decision_id_and_revision:
  interpretation_ids_and_revisions: []
  claim_gate_decision_ids_and_revisions: []
  action: ACT | TEST | NARROW | DEFER | STOP
  action_detail:
  alternatives_considered: []
  do_nothing_option:
  rationale:
  values_and_assumptions: []
  expected_upside:
  downside_harms_and_negative_evidence: []
  cost_and_constraints:
  reversibility:
  confidence_basis:
  conditions_or_stop_rules: []
  owner_and_timing:
  next_uncertainty_ids: []
```

A Recommendation may be reasonable under uncertainty; it may not present uncertainty as evidence. Each factual or numeric rationale sentence links to a passing ClaimGateDecision. Expose tradeoffs, negative evidence, do-nothing when realistic, conditions, stop rules, and the next uncertainty. A sponsor preference is a value/input, not a Finding.

## 6. Structural leakage validation

Reject persistence or display when any of these is true:

| Object | Reject |
|---|---|
| Finding | recommendation verb, business action, value judgment, unmeasured mechanism, missing evidence/calibration/gate link |
| Interpretation | new unlinked fact/count/quote/source; imperative or recommended action; causal fact stronger than Findings |
| Recommendation | new evidence; unlinked factual/numeric rationale; certainty beyond calibration; hidden negative evidence or alternatives |
| Combined report | layers merged without stable IDs; source links missing; negative cases, limitations, AI use, or residual uncertainty suppressed |

Before display, validate each object independently and then validate cross-object references. A mixed legacy report is imported as a `LegacyArtifact`; candidate layer objects remain `LEGACY_IMPORTED / UNVERIFIED` until reviewed and gated.

## 7. Decision update and next uncertainty

```yaml
decision_update:
  id_and_revision:
  business_decision_id_and_revision:
  recommendation_id_and_revision:
  status: DECIDED | DEFERRED | REOPENED
  option_selected_or_default_retained:
  owner:
  rationale:
  recommendation_acceptance_or_deviation:
  deviation_reason:
  review_trigger:
  next_uncertainty_ids: []
```

User acceptance updates approval or the business decision only. It does not verify evidence, repair method validity, prove execution, or resolve a proposition. Choose the next uncertainty by decision impact, risk that the current belief is wrong, and reversibility urgency; label the score `R-DEC-01 / Class E / HEURISTIC` and log any user override.

## 8. User-facing compiled views

The audit graph is authoritative. User-facing reports are compiled views and must not be maintained as a second truth source.

Default novice response order:

1. **Recommendation** — one concrete next move (`ACT`, `TEST`, `NARROW`, `DEFER`, or `STOP`).
2. **Why this is the right next move** — decision relevance and traceable evidence basis.
3. **What it will tell us** — the bounded proposition and maximum claim.
4. **What it will not prove** — unsupported scope, behavior, causality, population, or transfer.
5. **What you need to do** — the nearest dependency-ready action; no giant method menu.

Then show, in plain language:

```text
Known
Unknown
Contradictions / negative evidence
Biggest remaining risk
Current decision status
Next uncertainty
```

Ask no more than two tightly linked questions per turn unless safety/legal review requires more, and time them with the QUESTION_GATE (`references/modules/PROMPT_SKILL_INDEPENDENCE.md` §3: after the bounded answer unless no useful answer is possible). Recommend one defensible default and define technical terms only when they change the choice. When blocked, name the unsupported claim, the missing evidence, and the nearest valid repair. Distinguish `we do not know` from `not currently answerable under available access`.

The Recommendation-first view does not collapse FIR objects: it links back to Interpretation and Findings. It must never imply that FieldPilot recruited, observed, interviewed, paid, enrolled, or ran fieldwork unless an authorized system supplied verifiable execution evidence.

Compile these views when their dependencies exist:

- Decision Brief and What We Need to Learn;
- Evidence Requirement and Method Rationale;
- Domain / Access / Ethics Readiness;
- Execution Kit and live recruitment-disposition view;
- Evidence and Analysis Ledger;
- Negative Cases and Alternative Explanations;
- Findings;
- Interpretation;
- Recommendation and Decision Update;
- Next Uncertainty / Next Action;
- Methods, Sources, AI, and Limitations disclosure.

### 8.1 Full market-research compiled deliverable

When the active task is a **full market-research engagement**, the authoritative user-facing compiled view is `FINAL_MARKET_RESEARCH_REPORT.md` under `references/modules/MARKET_RESEARCH_DELIVERABLES.md`.

The report must preserve Findings / Interpretation / Recommendation as separate layers while presenting them in one useful research document. It must also include the user's service-vs-market comparison, direct-research status/results, unresolved questions, source register, and limitations. A Decision Brief or Next Action is not a substitute for this final report.

If direct research was recommended but the user selected `SKIPPED_BY_USER`, do not fail the whole report solely because fieldwork objects are absent. Instead:

- mark the corresponding proposition/evidence dimensions `NOT_TESTED` or otherwise bounded by the controlling calibration rules;
- identify which report claims are weakened or blocked;
- preserve the maximum claim scope after the skip;
- continue compiling all sections supported by eligible desk/secondary/product evidence;
- include recommended future research without presenting it as completed evidence.

This skip exception changes **deliverable continuity**, not evidence sufficiency. It never upgrades missing field evidence.

Do not generate empty files to simulate progress. A fieldwork-ready artifact is blocked until its pinned readiness prerequisites pass, while a final report may still compile with explicit `NOT TESTED / SKIPPED_BY_USER / INSUFFICIENT EVIDENCE` labels where evidence is unavailable.

## 9. Retained safeguards

- Source-linked `Evidence -> Analysis -> Finding -> Interpretation -> Recommendation -> Decision` is mandatory.
- `USER_ASSERTED`, `MODEL_DERIVED`, unverified external material, and simulated material never become verified facts by phrasing or approval.
- A founder's experience, one successful case, mandated use, competitor presence, or an article anecdote remains bounded to what was observed.
- Mandated or assisted use does not prove voluntary adoption; sign-up does not prove activation; activation does not prove retention.
- Stated WTP is not payment. Payment under one offer is not market-wide price acceptance.
- External evidence requires population, context, geography, business-type, workflow, and recency transfer checks.
- Access failure is access evidence, not demand failure.
- Every summary includes contradictions, negative evidence, segment/role differences where observed, sample/context limits, biggest risk, next uncertainty, and current decision status.

## 10. Source and maturity hooks

Use the active rules snapshot and `METHODOLOGY_SOURCES.md`. Primary hooks are `S-ESOMAR`, `S-SRQR`, `S-COREQ`, `S-CONSORT`, `S-DISSONANCE`, `S-TRIANGULATION`, `S-CAUSAL-LANG`, and `S-TRANSPORT`. Their reporting and inference support does not create a universal method hierarchy or automatic confidence from triangulation.
