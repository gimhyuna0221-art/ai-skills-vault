# Proposition and Evidence Contract

Runtime reference for FieldPilot v1.5.0. Load this module whenever a business decision,
uncertainty, proposition, evidence requirement, evidence item, method-fit decision, or
evidence calibration is created, revised, or reviewed.

This module implements `R-ARCH-01`, `R-ARCH-02`, `R-ACCESS-01`, `R-STATE-01`,
`R-CLAIM-01`, `R-QUAL-02`, `R-SURVEY-02`, `R-PRICE-01`, `R-PAYMENT-01`,
`R-NEG-01`, `R-TRI-01`, and `R-NUMERIC-01`. Rule class, maturity, enforcement,
scope, and source links are defined in `EXPERT_CORE_RULES.md` and
`METHODOLOGY_SOURCES.md`.

## 1. Non-negotiable runtime rules

1. Begin with the business decision and its material uncertainty, never with a favored
   method.
2. Compile a scoped proposition before finalizing a method.
3. Compile and lock the required-evidence contract before considering convenience,
   access, cost, or speed.
4. Treat evidence strength as claim-relative. Never use a universal ranking such as
   `experiment > survey > interview`.
5. Treat access and execution difficulty as acquisition constraints. They may change
   how evidence is obtained; they MUST NOT silently lower what an unchanged claim
   requires.
6. Keep source/provenance, verification, method validity, execution, approval, and
   resolution on independent state axes. User approval is not truth, method fit, fieldwork,
   or evidence.
7. Calibrate actual evidence against the same dimensions used to define the required
   evidence. A favorable result never upgrades the designed claim envelope.
8. Preserve contradictions, missing populations, negative cases, and plausible rival
   explanations. Multiple methods do not automatically upgrade confidence.
9. Preserve the v1.4.x boundaries: simulated/hypothetical material cannot become market
   evidence; mandated use is not voluntary adoption; a competitor or article anecdote is
   not target-market validation; stated WTP is not payment; one payment or case is not
   market-wide demand.

## 2. Decision-to-proposition compiler

### 2.1 Intake objects

Create the nearest dependency-ready objects. Do not create empty downstream artifacts to
simulate progress.

```yaml
business_decision:
  owner:
  decision_verb:
  options: []                 # include doing nothing when realistic
  deadline:
  stakes:
  reversibility:
  constraints: []
  success_consequences:
  current_default:

uncertainty:
  decision_id:
  unknown:
  why_material:
  current_belief:
  consequence_if_wrong:
  priority:
  resolution_status: OPEN
```

Infer these from the request, earlier turns and accessible material, and show the inferred values
to the user in plain language as labeled assumptions they can correct (v1.9.9-rc04,
`references/modules/PROMPT_SKILL_INDEPENDENCE.md`):

1. What decision will this research change, and what realistic options exist?
2. What is the most decision-relevant unknown, who owns the decision, and by when?

Do not ask the user to formulate these research objects; a beginner cannot be expected to know
them, and asking them tests the user instead of serving them. Ask only a genuinely user-owned fact,
through the QUESTION_GATE (after a bounded answer unless no useful answer is possible), and ask at
most two tightly linked questions per turn unless a safety/ethics interrupt requires more. If the user starts with “run a survey” or another method, store that as a preference;
do not let it bypass proposition and evidence compilation.

The optional uncertainty priority aid is:

```text
decision impact × probability the current belief is wrong × reversibility urgency
```

Label it `[R-DEC-01, Class E, HEURISTIC]`, expose all inputs, allow override, and never
present it as a validated market metric.

### 2.2 Proposition schema

Do not finalize method selection until every material field is supplied or explicitly
`NOT_APPLICABLE` with a reason.

```yaml
proposition:
  id:
  decision_id:
  uncertainty_id:
  type: []                    # extensible; multi-label when needed
  subject_or_unit:
  target_population_or_system:
  construct_or_outcome:
  context_or_channel:
  comparator:
  geography:
  timeframe:
  requested_claim_scope:
  causal_force:
  behavioral_proximity:
  decision_stakes:
  current_belief:
  result_that_would_weaken_it:
```

Never silently infer population, geography, timeframe, comparator, causal force, or the
meaning of “validated.” A visible, labeled, defensible inference is allowed (geography never from
conversation language or owner location). If a term is material and ambiguous, preserve it as
unknown, bound the dependent claims, and ask the nearest useful question through the
QUESTION_GATE — normally at the end of the bounded answer.

### 2.3 Proposition taxonomy

| Type | Question compiled | Evidence target |
|---|---|---|
| `DESCRIPTIVE_DISTRIBUTION` | How common, large, or distributed is X? | Eligible defined-population estimate with sampling/model assumptions |
| `MEANING_OR_EXPERIENCE` | How is X understood or experienced? | Situated accounts with purposive coverage and transparent analysis |
| `MECHANISM_OR_JOB` | Why/how/when does a need or behavior arise? | Interviews, observation, traces, cases, and rival-mechanism analysis |
| `ASSOCIATION_OR_DIFFERENCE` | Do variables or groups differ/move together? | Comparative measurement with confounding and uncertainty bounded |
| `CAUSAL_EFFECT` | Did intervention T cause outcome Y? | Credible counterfactual for a defined estimand |
| `PREDICTION_OR_FORECAST` | What future outcome is expected? | Temporally validated model with transport limits |
| `STATED_PREFERENCE_OR_WTP` | What do people state/select under elicitation M? | Method-specific stated-choice evidence |
| `BEHAVIORAL_INTEREST` | Did exposed eligible units take action X? | Instrumented exposure, opportunity denominator, and contextual behavior |
| `ACTUAL_TRANSACTION` | Did an auditable exchange/payment occur? | Verified transaction, offer, refunds/cancellations, and conditions |
| `USABILITY_OR_COMPREHENSION` | Can users understand or complete specified tasks? | Representative-user task evidence in a named context |
| `MARKET_MAGNITUDE` | What is a defined market's volume/value? | Auditable constructed estimate, assumptions, ranges, and sensitivity |
| `SEGMENT_STRUCTURE` | Which groups differ in a decision-useful way? | A-priori or discovered structure with stability/usefulness checks |
| `COMPETITIVE_OR_SUBSTITUTION` | What alternatives/workarounds/do-nothing compete? | Provenanced desk, human, behavioral, and commercial evidence |
| `BUYING_SYSTEM` | Who influences purchase/adoption, how, and with what authority? | Multi-role/multi-level process evidence |
| `IMPLEMENTATION_OR_FEASIBILITY` | Can delivery, access, adoption, or operation work? | Contextual constraint, process, and reliability evidence |
| `SAFETY_OR_CONSTRAINT` | What legal, ethical, physical, or regulatory condition applies? | Applicable authoritative guidance and qualified review when required |

Create a separate proposition and contract for each materially different question.
Prevalence and mechanism, usability and demand, stated WTP and payment, engagement and
learning, one marketplace side and the cross-side mechanism are never one undifferentiated
“validation” proposition.

### 2.4 Claim-scope taxonomy

Scope is a boundary, not a universal strength score:

- `OBSERVED_CASE`: named person, account, site, event, or transaction under named
  conditions.
- `STUDIED_SAMPLE`: only recruited or observed cases.
- `SAMPLING_FRAME`: the accessible frame under the stated design.
- `TARGET_POPULATION`: explicitly defined population under eligible probability or
  justified model-based inference.
- `CAUSAL_ESTIMAND`: effect for eligible units, treatment, outcome, and period under a
  valid design.
- `TRANSPORTED_EFFECT`: effect extended through explicit transport assumptions and
  supporting evidence.
- `FORECAST`: future outcome under a named model, horizon, and validation regime.

## 3. Required Evidence Contract

### 3.1 Contract schema

Compile minimum requirements independently. Never replace them with an overall evidence
score.

```yaml
required_evidence_contract:
  proposition_id:
  minimum_measurement:
    construct_definition:
    eligible_measure_or_mapping:
    invalid_proxies: []
  sampling_or_coverage:
    required_units_and_roles: []
    target_link_required:
    subgroup_or_case_variation: []
  comparison_or_assignment:
    comparator:
    counterfactual_or_identification:
  context:
    channel:
    setting:
    price_offer_support_conditions:
  behavioral_proximity:
    minimum_level:
    disallowed_substitutes: []
  temporal:
    window:
    recurrence_or_lag:
    seasonality_or_retention:
  precision_or_uncertainty:
    decision_relevant_precision:
    interval_or_sensitivity_basis:
  replication_or_triangulation:
    independent_sources_or_settings:
    integration_purpose:
  provenance:
    allowed_provenance: []
    independence_or_verification:
    human_synthetic_boundary:
  ethics_legal_safety:
    mandatory_conditions: []
    qualified_review_required:
  maximum_intended_claim:
  contract_status:
  revision_reason:
```

For each dimension answer:

| Dimension | Mandatory question |
|---|---|
| Construct/measurement | Does the measure represent the proposition rather than a convenient proxy? |
| Directness/behavioral proximity | Is the required evidence an account, intention, interest action, use, repeat use, transaction, or outcome? |
| Sampling/coverage | Which people, roles, accounts, sites, events, or systems must be represented? |
| Comparison/counterfactual | Is baseline, comparator, assignment, or identification required? |
| Context/ecological realism | Which channel, location, workflow, price, support, or use condition must be present? |
| Temporal relevance | Which window, recurrence, lag, novelty, seasonality, or retention period matters? |
| Precision/uncertainty | What precision, interval, sensitivity, or stopping logic changes the decision? |
| Replication/triangulation | Are independent settings, sources, or planned challenges necessary? |
| Provenance/independence | Must evidence be human, observed, external, independent, or transaction-verified? |
| Ethics/legal/safety | Which consent, privacy, safeguarding, reporting, jurisdiction, or professional controls are mandatory? |

### 3.2 Contract locking and revision

Once acquisition or method feasibility is being optimized, the active contract is
immutable. A change to population, scope, construct, causal force, behavioral proximity,
time, or precision creates a new revision and requires explicit acknowledgement of what
the revised claim no longer covers.

The contract/router outcome MUST be one of:

- `CONTRACT_SATISFIABLE`
- `CONTRACT_SATISFIABLE_WITH_DESIGN_CHANGES`
- `CONTRACT_PARTIALLY_SATISFIABLE` with unsupported dimensions named
- `CLAIM_NARROWING_REQUIRED`
- `NOT_CURRENTLY_ANSWERABLE`
- `ETHICS_OR_LEGAL_BLOCK`

Never edit the contract silently to make the easiest method appear sufficient.

### 3.3 Necessary Evidence Guard

After the contract is locked, feasibility may change only acquisition. If the preferred
route fails, persist exactly one primary outcome:

1. `EQUIVALENT_VALID_ROUTE`: another frame, channel, source, site, instrument, or design
   provides the same required evidence.
2. `ACCESS_REDESIGN`: preserve the evidence floor while changing burden, timing, trust,
   language, partner, warm introduction, role, or parallel access route.
3. `EXPLICIT_PROPOSITION_REVISION`: revise the proposition and contract, state the lost
   claim scope, and obtain acknowledgement.
4. `DECISION_DEFERRAL`: preserve the unresolved proposition and consequence of acting.
5. `NOT_CURRENTLY_ANSWERABLE`: preserve the unmet contract and blocking reality.
6. `ETHICS_OR_LEGAL_STOP`: stop/escalate because no lawful, safe, acceptable route exists.

`DIFFICULT` never means `UNNECESSARY`. Non-contact, no response, research refusal, offer
refusal, and ineligibility are distinct events. Access failure may justify a separate
`IMPLEMENTATION_OR_FEASIBILITY` or `BUYING_SYSTEM` proposition; it is not demand failure.

## 4. Evidence model and compatibility

### 4.1 Evidence-item minimum

```yaml
evidence_item:
  evidence_type:
  proposition_ids: []
  source_or_provenance:
  provenance_status:
  verification_status:
  method_id_and_revision:
  sample_case_or_frame:
  unit_and_nested_structure:
  raw_evidence_link:
  context_geography_time:
  behavioral_level:
  voluntary_or_required:
  assisted_or_independent:
  human_n:
  synthetic_n:
  quality_limitations: []
  transformations: []
  conflicts_or_negative_cases: []
```

Use the following distinct evidence types; do not collapse them:

- `EXTERNAL_FACT`: inspected source establishes a fact in its own scope.
- `INDIRECT_SIGNAL`: a proxy, transfer source, article, competitor, or contextual signal.
- `DIRECT_SELF_REPORT`: a real person's reported experience, belief, or intention.
- `OBSERVED_BEHAVIOR`: recorded behavior under named exposure and conditions.
- `REPEATED_BEHAVIOR`: behavior across a decision-relevant repeat opportunity/window.
- `STATED_PREFERENCE`: choice or preference stated under a named elicitation.
- `STATED_WTP`: price response stated/selected under a named elicitation.
- `TRANSACTION_PAYMENT`: verified payment/exchange, including offer and reversals.
- `QUANTITATIVE_ESTIMATE`: computed estimate with population/frame/model and uncertainty.
- `INFERENCE`: an analytic or model-derived conclusion, never raw evidence.
- `EXPERT_RECOMMENDATION`: advice with values/tradeoffs, never evidence.
- `UNKNOWN`: material information not established.
- `SYNTHETIC_GENERATED`: model output; never human evidence.

### 4.2 Ordinary compatibility boundaries

These are maximum ordinary boundaries when the underlying design and analysis are valid.
The Claim-Grammar Gate may narrow them further.

| Evidence/design | May ordinarily support | Does not by itself support |
|---|---|---|
| Inspected desk source | What that source establishes in its definitions, population, place, and time | Current target-market truth or independent convergence |
| Competitor/vendor material | Documented offer, price, availability, or what the vendor claims | Customer preference, demand, adoption, or market validation |
| Article/customer anecdote | The reported case or source assertion | Target-population proof or prevalence |
| Human qualitative interview | Studied participants' accounts, meanings, mechanisms, and bounded patterns | Population percentage, prevalence, behavior, or payment |
| Focus group | Interaction, shared language, dissent, and group-context response | Independent prevalence or private willingness |
| Observation/contextual study | Behavior/process observed in sampled settings | Unobserved motive, voluntariness, or prevalence |
| Diary | Participant/window-bound reported or verified patterns | Population frequency or unobserved behavior |
| Probability survey | Defined-population estimate if frame, selection, response, weighting, and design support it | Broader population, timeless truth, or causality |
| Opt-in/nonprobability survey | Sample description or explicit model-based estimate with assumptions | Automatic representativeness or conventional population MOE |
| Concept test | Comprehension and stated/contextual response to the shown stimulus | Usability, purchase, retention, reliability, or demand |
| Prototype usability | Performance in tested users/tasks/prototype conditions | Market demand, production reliability, or actual-use safety |
| Instrumented analytics | Recorded behavior in the eligible instrumented population/window | Motive, causality, or market-wide adoption |
| Fake door/landing page | Contextual interest action among exposed eligible units | Purchase demand, WTP, retention, or “market validation” |
| Mandated/forced use | Usability/workflow evidence under required-use conditions | Voluntary adoption, retention, or preference |
| Assisted/concierge use | Use/outcome under the recorded support level | Self-service, scale, independent adoption, or unit economics |
| Stated WTP | Stated/selected response under the named pricing method | Actual payment or universal price acceptance |
| Actual payment | Verified transaction under named offer/channel/time conditions | Market-wide WTP, retention, scalable demand, or PMF |
| Valid randomized experiment | Bounded causal estimand for eligible units, treatment, metric, and window | Transport to all markets, channels, populations, or times |
| Quasi-experiment | Conditional causal estimate under explicit identification assumptions | Randomized certainty or unrestricted transport |
| Synthetic respondents | What model M produced under configuration C | Any human experience, prevalence, behavior, WTP, saturation, or demand |

One successful pilot supports only that case and its recorded conditions. Ten observations
from one account do not become ten independent accounts. Repeated events from one person
do not expand the participant denominator. Counts do not create target-population linkage.

### 4.3 Source and transfer discipline

For every external item retain original author/publisher, URL/identifier, version/date,
access date, publication/review status, funding/conflict, population, geography, timeframe,
method, sample/frame, definition, unit, inspected-original status, target similarity,
transfer caveats, and credible conflicts. A snippet, screenshot, press release, syndicated
duplicate, or vendor blog is not independent original provenance.

If the original numeric source cannot be inspected, set
`verification_status: UNVERIFIED`, add `SECONDARY_UNVERIFIED`, and prohibit the value from
being the sole basis for a high-stakes decision. Never promote a source beyond its rule-
specific class, maturity, applicability, or transfer boundary.

## 5. Evidence calibration

After collection and analysis, compare actual execution with every contract dimension.

```yaml
evidence_calibration:
  proposition_id:
  contract_id_and_revision:
  evidence_bundle_ids: []
  analysis_result_ids: []
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
  plan_execution_fit:
  source_independence_and_conflict:
  analysis_robustness_and_sensitivity:
  internal_validity:
  transfer_or_transport:
  maximum_claim_scope:
  material_limitations: []
  unresolved_alternatives: []
  negative_case_ids: []
```

Use these meanings exactly:

- `SUPPORTS`: eligible evidence discriminates in favor of the proposition within the
  calibrated envelope.
- `WEAKENS`: eligible evidence discriminates against it within the envelope.
- `MIXED`: eligible evidence materially conflicts or varies; preserve the pattern.
- `INCONCLUSIVE`: eligible evidence was collected but cannot discriminate at the required
  level.
- `NOT_TESTED`: the proposition was not actually addressed.
- `INVALID_EVIDENCE`: a hard design, provenance, ethics, or execution failure makes the
  evidence ineligible for the intended claim.

Before calibration, require a proportionate search for failures, refusals, non-users,
dropouts, churn, refunds, complaints, adverse outcomes, missing roles/groups/sites/times,
measurement error, confounding, selection, attrition, instrumentation failure, novelty,
support, seasonality, chance, and the strongest plausible alternative explanation. Record
alternatives as `SUPPORTED`, `MIXED`, `PLAUSIBLE`, `WEAKENED`, `NOT_SUPPORTED`, or
`NOT_TESTED`. Never render `NOT_TESTED` as false.

With multiple methods, record `CONVERGENCE`, `COMPLEMENTARITY`, `SEQUENCE`, or
`DISSONANCE_TEST`. Do not average disagreement away or borrow unrelated dimensions to
manufacture a stronger conclusion.

## 6. Runtime output from this module

Return one novice-readable next-action view:

```text
RECOMMENDATION
WHY THIS IS THE RIGHT NEXT MOVE
WHAT IT WILL TELL US
WHAT IT WILL NOT PROVE
WHAT YOU NEED TO DO
```

Also preserve machine state for `Known`, `Unknown`, `Why it matters`, and `Next action`.
When blocking, name the unsupported claim, the failed evidence dimension, and the nearest
valid repair. Do not claim that FieldPilot recruited, interviewed, observed, paid, enrolled,
or otherwise executed fieldwork unless verifiable evidence from an authorized external
system exists.

Before displaying or persisting any substantive sentence, pass it to
`CLAIM_GRAMMAR.md`. Before advancing readiness, resolution, or a business decision, apply
`AUDIT_STATE_SCHEMA.md`.
