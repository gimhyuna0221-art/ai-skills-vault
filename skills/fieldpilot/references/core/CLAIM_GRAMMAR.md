# Claim-Grammar Gate and Numeric Provenance

Runtime reference for FieldPilot v1.5.0. This is an output compiler, not writing advice.
Load it before displaying or persisting any substantive claim in chat, artifacts, headings,
summaries, tables, charts, Findings, Interpretation, Recommendation rationales, or exported
data.

This module implements `R-CLAIM-01`, `R-QUAL-02`, `R-SURVEY-02`, `R-SURVEY-03`,
`R-CONCEPT-01`, `R-BEHAVIOR-01`, `R-FAKEDOOR-01`, `R-PRICE-01`,
`R-PAYMENT-01`, `R-EXP-01`, `R-EXP-03`, `R-CAUSAL-LANG-01`, `R-NUMERIC-01`,
`R-AI-01`, `R-ENTERPRISE-01`, `R-MEDIA-01`, and `R-EDU-01`.

## 1. Hard output contract

1. Every material claim MUST link to eligible evidence and an active
   `EvidenceCalibration` revision.
2. Parse semantics and scope, not just banned words. If a material dimension is unknown,
   incomparable, or cannot be parsed confidently, fail closed.
3. A candidate claim passes only when every dimension fits one calibrated supported claim
   envelope or one valid predeclared/justified synthesis envelope.
4. A favorable result cannot upgrade the design's maximum envelope.
5. A rewrite is not output-safe until it is re-parsed and passes.
6. Preserve the candidate, parsed form, all violations, rewrite, decision, rule snapshot,
   actor, and time.
7. Never combine unrelated evidence into a “Frankenstein claim” by borrowing population
   scope from one method, causal force from another, and behavior from a third.
8. All material numbers MUST pass the Numeric Claim Guard in Section 6.

## 2. Candidate claim envelope

Extract or require every field below. Use `NOT_APPLICABLE` only with a reason; use
`UNKNOWN` when material information is missing.

```yaml
claim:
  candidate_text:
  language:
  subject_scope:
  quantifier:
  construct:
  verb_strength:
  causal_force:
  behavioral_level:
  population_geography_time:
  comparison:
  numeric_value_and_precision:
  conditions:
  evidence_ids: []
```

The linked calibration MUST emit:

```yaml
supported_claim_envelope:
  proposition_id:
  evidence_bundle_ids: []
  calibration_revision:
  allowed_subjects_and_units: []
  allowed_scope_relations: []
  allowed_quantifier_types: []
  allowed_constructs_and_mappings: []
  allowed_verbs_and_behavioral_levels: []
  allowed_causal_forces: []
  allowed_comparators: []
  geography_and_context_bounds: []
  temporal_bounds: []
  numeric_precision_and_interval_bases: []
  required_conditions_and_qualifiers: []
  prohibited_inferences: []
```

The formal predicate is:

```text
within(candidate_claim, supported_claim_envelope)
```

`within(...)` is true only when every parsed claim dimension is explicitly allowed,
contained by a recorded bound, or linked through a recorded valid construct mapping.
Never infer scope containment because one label sounds broader or stronger.

## 3. Deterministic gate algorithm

Execute in this order:

1. Parse the candidate claim. If a material semantic dimension cannot be parsed, return
   `BLOCKED_MISSING_EVIDENCE` and propose a bounded template or clarifying input.
2. Resolve every evidence ID, its raw/processed lineage, active lifecycle, human/synthetic
   status, analysis, and active calibration revision.
3. Run the ethics/legal/safety output check.
4. Run source and evidence provenance eligibility checks.
5. Run the Numeric Claim Guard for every material number.
6. Compare each parsed claim dimension to one supported envelope.
7. If one valid synthesis is used, require an `AnalysisResult` that defines integration,
   independence/conflict handling, and its own calibrated envelope.
8. Apply material negative cases, conflicts, limitations, and transport boundaries.
9. Choose the gate outcome using the precedence below.
10. If a narrower accurate statement exists, generate it, parse it from scratch, and
    persist/display it only when the new statement passes.
11. Persist the decision before output.

### 3.1 Outcomes and precedence

```text
PASS                       claim fits the active supported envelope
REWRITE_REQUIRED           an otherwise eligible narrower accurate form is available
BLOCKED_MISSING_EVIDENCE   no defensible substantive form exists for the intended claim
BLOCKED_PROVENANCE         evidence/source is absent, inactive, synthetic-as-human, or ineligible
BLOCKED_NUMERIC_PROVENANCE a material number lacks required lineage or uncertainty fields
BLOCKED_ETHICS              output would violate a safety, ethics, privacy, legal, or safeguarding control
```

Precedence is:

```text
BLOCKED_ETHICS
  > BLOCKED_PROVENANCE
  > BLOCKED_NUMERIC_PROVENANCE
  > BLOCKED_MISSING_EVIDENCE
  > REWRITE_REQUIRED
  > PASS
```

Retain every detected violation even when a higher-precedence outcome is returned.

For `REWRITE_REQUIRED`, show:

- the original overreach;
- the proposed bounded sentence;
- the missing evidence dimension;
- the evidence needed for the stronger claim.

## 4. Mandatory claim boundaries

The following examples are executable regression expectations. Use equivalent bounded
language when project details differ; retain the named unit, denominator, population,
context, geography, and time.

### 4.1 Qualitative interview

Allowed:

- “Among these 8 participants, 6 described pattern X.”
- “8명 중 6명에게서 이 패턴이 관찰되었습니다.”

Block or rewrite:

- “75% of market customers have this problem.”
- “시장 고객의 75%가 이 문제를 겪습니다.”

Reason: a purposive qualitative count is a studied-case pattern, not a target-population
prevalence estimate. Quotations illustrate evidence; they do not create prevalence.

### 4.2 Opt-in or nonprobability sample

Allowed, subject to valid analysis:

- “In this recruited sample, A was higher than B.”
- “이 표본에서는 A가 B보다 높았습니다.”

Block absent an eligible target-linking model and model-based uncertainty:

- “40% of the total population ±3%.”
- “전체 모집단의 40% ±3%.”

Never label ordinary opt-in uncertainty as conventional margin of sampling error. Quotas
or weighting do not automatically create representativeness.

### 4.3 Single observed case or site

Allowed:

- “At site S, during T, under conditions C, X occurred.”
- “이 현장에서 작동했습니다.”

The compiled form MUST retain the site, period, and material conditions even when the
short Korean form is shown.

Block or rewrite:

- “Validated in the market.”
- “시장에서 검증됐습니다.”

### 4.4 Fake door or landing page

Allowed:

- “Among audience A exposed to message/placement/context C, interest action X was
  observed.”
- “이 audience/message/context에서 관심 행동이 관찰됐습니다.”

Block or rewrite:

- “Purchase demand was validated.”
- “구매 수요가 검증됐습니다.”

The passing claim requires an eligible exposure/opportunity denominator and an explicit
action definition. A click, visit, waitlist registration, and payment are different actions.

### 4.5 Stated willingness to pay

Allowed:

- “Respondents stated or selected price X under elicitation method M.”
- “응답자가 X 가격에서 지불 의향을 진술했습니다.”

Block or rewrite:

- “They will actually pay X.”
- “실제로 X를 지불합니다.”

No fixed hypothetical-bias discount or universal best WTP method may be applied.

### 4.6 Actual payment

Allowed:

- “N verified payments occurred at price X under offer/channel/time C.”
- “이 조건에서 실제 결제가 발생했습니다.”

The compiled Finding MUST retain count, offer, price/currency, eligibility, channel, time,
discount/incentive, refunds/cancellations, delivery, and assistance when applicable.

Block or rewrite:

- “The whole market accepts this price.”
- “시장 전체가 이 가격을 받아들입니다.”

### 4.7 Valid randomized A/B test

Allowed:

- “Assignment to treatment caused estimated effect E on metric M among eligible units
  during T.”
- “이 실험 조건에서 처치의 인과효과가 관찰됐습니다.”

The compiled form MUST name the treatment, control/comparator, assignment unit, eligible
units, metric/estimand, interval, and window.

Block or rewrite:

- “The same effect applies in every market.”
- “모든 시장에서 동일합니다.”

Transport requires separate assumptions and evidence. A/B validity also fails or narrows
for assignment, exposure, instrumentation, SRM, interference, attrition, or analysis
integrity failures.

### 4.8 Synthetic respondents

Allowed:

- “Model M produced pattern P under prompt/configuration C.”
- “모델 M이 설정 C에서 패턴 P를 생성했습니다.”

Block:

- “Customers prefer A, n=10,000.”
- any human percentage, prevalence, saturation, lived experience, WTP, behavior,
  representativeness, or market-demand claim derived from synthetic cases.

Set `human_n: 0`; never add `synthetic_n` to a human denominator.

### 4.9 B2B role evidence

Allowed:

- “This champion reported and supported X.”

Block or rewrite:

- “The account will buy.”
- “Procurement is approved.”
- “The enterprise market needs X.”

One role supplies only role-specific evidence. User, beneficiary, champion, buyer, payer,
approver, technical/security/legal evaluator, procurement, gatekeeper, veto holder,
implementation owner, and renewal owner may differ and may overlap only when evidenced.

### 4.10 Mandated and assisted use

Allowed:

- “Under required-use conditions, participants completed task X.”
- “Under support level S, these cases used/completed X.”

Block or rewrite:

- “Users voluntarily adopted X.”
- “The product retains customers.”
- “The workflow scales without assistance.”

### 4.11 Education and ad-supported media

Education engagement allowed:

- “Learners used/completed X during T.”

Block:

- “X improved learning” without valid learning-outcome evidence, correct units, and an
  eligible causal or bounded comparative design.

Media allowed:

- “Qualified exposures/interactions/leads were recorded as defined.”

Block:

- “The ad caused incremental sales” from impressions, clicks, engagement, leads, intent,
  or attributed conversions alone. Delivery, attention, interaction, intent, visitation,
  transaction, attribution, and causal incrementality are distinct.

### 4.12 Observational association and causal language

For observational association, allow bounded association/difference language. Block
`caused`, `effect`, `impact`, or a rollout directive unless a credible counterfactual or
explicitly labeled untested causal assumption exists. If a sentence mixes a result,
mechanism, and action—such as “Feature X caused retention and should be rolled out”—split
it into Finding, Interpretation, and Recommendation objects and gate each factual claim.

## 5. Verb, quantifier, and scope controls

- `said`, `described`, `reported`, and `selected` mean self-report, not observed behavior.
- `clicked`, `joined`, `used`, `returned`, and `paid` are distinct observed actions and
  never substitute for one another.
- `required`, `assigned`, `incentivized`, `assisted`, and `voluntary` are material
  conditions and MUST remain visible.
- `caused`, `effect`, and `impact` require an eligible counterfactual or explicit untested
  assumptions.
- `customers`, `the market`, `people`, `businesses`, and population percentages require
  an identified and eligible population link.
- `validated`, `proven`, `works`, `will`, `best`, and `representative` require a compiled
  definition and supported envelope; otherwise rewrite to an observable bounded result.
- Counts carry denominator and unit whenever meaningful. A percentage never hides a small
  or nonrepresentative denominator.
- Separate case, participant, user, account, site, household, classroom, event,
  transaction, session, and time denominators. Nested/repeated observations are not
  independent units automatically.
- Precision cannot exceed the source measurement, input precision, or sample/model
  uncertainty.
- Geography, context, business type, workflow, channel, price/offer, support, recency, and
  time bounds remain visible when they constrain the claim.

## 6. Numeric Claim Guard

### 6.1 Required object

Every material numeric claim or model input links to:

```yaml
numeric_provenance:
  id:
  claim_or_input_id:
  value_or_range:
  numerator:
  denominator:
  unit:
  target_population_or_base:
  geography:
  period_and_reference_date:
  currency_and_base_year:
  source_ids: []
  source_table_page_variable:
  original_or_derived:
  formula_or_transformation:
  assumptions: []
  missingness_exclusions_weighting:
  uncertainty_or_interval_type:
  sensitivity_scenarios: []
  rounding:
  human_n:
  synthetic_n:
```

`NOT_APPLICABLE` requires a reason. `UNKNOWN` material fields cap or block the claim.

### 6.2 Guard checks

Before output, require:

1. a defined value/range, unit, base, geography, period/reference date, and denominator
   where meaningful;
2. an inspectable original source or a clearly labeled `SECONDARY_UNVERIFIED` status;
3. exact table/page/variable when available;
4. formula/transformation and all input IDs for derived numbers;
5. assumptions and base/conservative/expansive sensitivity where material;
6. missingness, exclusions, weighting/modeling, and uncertainty/interval basis;
7. currency conversion rate, source, and date; inflation index and base year when used;
8. rounding consistent with input precision and uncertainty;
9. distinct human and synthetic counts.

For surveys, label intervals as probability-design, model-based, bootstrap, Bayesian, or
other actual basis. Conventional probability-sampling margin of error is prohibited for
ordinary opt-in samples. Weighting requires benchmark provenance, diagnostics, weighted
and unweighted results, effective sample size/weight variability, and residual selection
risk before any target estimate can pass.

For market size, distinguish `KNOWN_INPUT`, `ASSUMPTION`, `CALCULATION`, `RANGE`, and
`UNVERIFIED_GAP`. Never render `TAM`, `SAM`, or `SOM` as a discovered fact unless that
project defines the term and supports every input. `SOM = arbitrary percentage of TAM` is
an assumption, not evidence.

The expression `human_n + synthetic_n` is forbidden. A model-assisted estimator-
efficiency diagnostic, when experimentally eligible, uses its own fully defined field and
must never be rendered as recruited N, human N, response rate, representativeness, or
ordinary human-sample precision.

## 7. Multiple-evidence and conflict rules

One claim must be supported in full by one calibrated evidence bundle. Combining evidence
is permitted only when an `AnalysisResult` specifies:

- the propositions and evidence items integrated;
- the role of each method (`CONVERGENCE`, `COMPLEMENTARITY`, `SEQUENCE`, or
  `DISSONANCE_TEST`);
- source independence and shared dependencies;
- treatment of contradictory evidence and missing populations;
- construct mappings and transport assumptions;
- the integration method and uncertainty;
- a new calibrated supported claim envelope.

Material conflict returns `MIXED`, narrows the envelope, or blocks the claim. Never select
the favorable result silently or claim confidence merely because several methods/sources
were used.

## 8. Persisted gate decision

```yaml
claim_gate_decision:
  id:
  schema_version:
  revision:
  candidate_text_and_language:
  parsed_claim:
  evidence_bundle_ids: []
  calibration_id_and_revision:
  rule_snapshot_id:
  evaluated_rule_ids: []
  dimension_comparisons: []
  all_violations: []
  outcome:
  violation_or_block_reason:
  proposed_rewrite:
  rewrite_parsed_claim:
  rewrite_gate_outcome:
  accepted_rewrite:
  actor_and_time:
```

Only `PASS` content may appear as an unqualified substantive claim. A
`REWRITE_REQUIRED` candidate itself remains blocked; only its separately passing rewrite
may be displayed or persisted as an accepted claim.

Pass the output to the strict Findings / Interpretation / Recommendation structures in
`ANALYSIS_AND_REPORTING.md`, and persist lifecycle and audit behavior through
`AUDIT_STATE_SCHEMA.md`.
