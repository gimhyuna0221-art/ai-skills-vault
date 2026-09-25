# Market Case Comparison and User-Case Gap Runtime — v1.7.4

This module governs how FieldPilot defines success, selects comparable cases, extracts patterns
and mechanisms, diagnoses the user's own case against them, and converts that diagnosis into
prioritized decisions.

It is **additive**. It does not replace `references/modules/SUCCESS_FAILURE_AND_REPLICABILITY.md`,
which remains the controlling contract for causal explanation, endowment-versus-tactic separation
and the Replicability Engine. This module supplies the case-selection discipline and the
user-facing gap diagnosis that sit around it.

Activate for a full market-research engagement, and for any bounded question that turns on
comparable-case evidence (`성공 사례 분석`, `왜 성공했어`, `비슷한 앱 성공`, "what do the winners
do", "why did those fail"). Do not activate it for a single competitor fact or one channel choice.

Rule anchors: `R-COMP-01`, `R-COMP-02`, `R-NEG-01`, `R-TRI-01`, `R-CAUSAL-LANG-01`, `R-CLAIM-01`,
`R-NUMERIC-01`, `R-FIR-01`, `R-SOURCE-01`, `R-DESK-01`.
Source anchors: `S-SHMUELI`, `S-TRANSPORT`, `S-DRISKO`, `S-ESOMAR`; discovery reporting structure
adapted from `V16-S29`; survivorship boundary already recorded on `V16-S24` and `V16-S25`.

## 1. SUCCESS_DEFINITION — frozen before any case is selected

Success is defined **for this decision**, before cases are chosen. Selecting cases first and
defining success afterwards is a post-hoc rationalization and is prohibited.

```text
SUCCESS_DEFINITION
  decision_this_serves
  success_metric(s)                 what outcome actually counts here
  threshold_basis                   why this level counts as success, in words
  measurement_period
  geography_or_segment_scope
  required_evidence_quality         what evidence would have to exist to accept a case
  eligibility_criteria              what makes a case admissible
  exclusion_criteria                what disqualifies a case
  provenance_label                  STATED / INFERRED / ASSUMED / ASKED / UNRESOLVED
```

Fit-for-purpose metrics may include revenue, profitability, retention, active usage, paid
conversion, growth, sustained operation under a stated outcome test, category or niche position,
or customer-satisfaction evidence. Choose what this decision actually depends on. A definition
that cannot be evidenced for any candidate case is not a usable definition — say so and widen or
weaken it explicitly rather than quietly scoring cases against it anyway.

### Prohibited stand-alone success criteria

None of the following may serve **alone** as the definition of success. Each may appear only
alongside an outcome metric that is not itself a survivorship artefact:

- being well known, frequently discussed, or heavily covered in press;
- mere continued existence or "still operating" (this is survivorship restated as an outcome);
- funding raised, valuation, or investor identity (a financing signal, not demand, PMF or
  business economics);
- follower, subscriber, download or install counts;
- store presence, featuring, or editorial placement;
- awards, rankings and listicles.

If the user supplies one of these as their success criterion, do not refuse the request. Record it
as `USER_SUPPLIED_CRITERION`, state plainly what it does and does not evidence, and propose the
outcome metric that would have to accompany it.

## 2. SUCCESS_CASE_REGISTER

Where evidence permits, select **more than one** case. A single anecdote is not a case set, and a
case set assembled from one source or one publisher is not independent.

```text
CASE_ID
  name_and_locator
  why_it_qualifies              against the frozen SUCCESS_DEFINITION, explicitly
  outcome_evidence              what is actually observed, with source and date
  evidence_class                CURRENT_FACT / VENDOR_CLAIM / SECONDARY_CASE /
                                COMMUNITY_ANECDOTE / INFERENCE / UNKNOWN_BOUNDARY
  context                       market, period, platform, geography
  business_model
  target_segment
  timing                        when it happened, and what the market looked like then
  material_constraints          endowments, capital, audience, partnerships, timing luck
  known_selection_risk          how this case was found, and what that biases toward
```

Rules:

- A case that cannot be evidenced against the frozen definition is not admitted. Record it under
  `CONSIDERED_AND_EXCLUDED` with the reason; do not silently drop it.
- Vendor and founder accounts are evidence of what the vendor or founder **says**, never of
  causation. Preserve the `PROVENANCE_CLASS` from the success/failure module.
- If no defensible case can be found after a bounded search, state
  `INSUFFICIENT EVIDENCE — see NEGATIVE_CASE_SEARCH and discovery record`. Never invent a case,
  and never substitute a generic archetype for a named one.

## 3. COMPARATOR_SET and the NEGATIVE_CASE_SEARCH record

Failure, underperformer and near-miss comparators are a **survivor-bias control**, not an
optional balance gesture.

The discovery channel is itself biased: successes are published and failures are not. Recording
only the failures that happened to surface re-imports the bias while appearing to have removed it.
FieldPilot therefore records the **search**, not only the result.

```text
NEGATIVE_CASE_SEARCH
  performed                     PERFORMED / NOT_PERFORMED
  where_sought                  e.g. shutdown and sunset notices, store delistings, archived or
                                disappeared pricing pages, abandoned repositories, community
                                post-mortems, acquisition-and-wind-down coverage, dormant
                                changelogs, support forums for discontinued products
  search_dates
  limits_and_restrictions       language, geography, period, access barriers
  outcome                       FOUND / SEARCHED_NOT_FOUND
  known_blind_spots
```

```text
COMPARATOR_CASE
  CASE_ID
  comparator_type               FAILURE / UNDERPERFORMER / NEAR_MISS / DISCONTINUED / PIVOTED
  what_outcome_is_observed
  evidence_and_date
  matched_on                    product type, period, platform, geography, model, scale,
                                starting audience, segment
  unmatched_on                  differences that block clean comparison
  why_it_is_informative
```

Ceiling rules, applied without exception:

- `NOT_PERFORMED` — no cross-case finding may be called a success mechanism. Patterns may still be
  reported, labelled `COMMON_PATTERN`, `UNTESTED_NO_COMPARATOR`.
- `SEARCHED_NOT_FOUND` — this is a legitimate, reportable outcome. Cross-case mechanism claims are
  admitted at reduced strength, and the report states that the absence of observable failures may
  reflect publication bias rather than an absence of failures.
- `FOUND` — mechanism claims proceed to the discrimination step in section 4.

Where the low-performing group is poorly observed, label the comparison weak rather than
pretending balance. This preserves the existing matched-comparison rule.

## 4. CROSS_CASE_PATTERNS, EXPLICIT_TWO_SIDED_FACTOR_TEST and MECHANISM_DISCRIMINATION

`COMMON_PATTERN` and `LIKELY_SUCCESS_MECHANISM` are **different objects** and must never be
collapsed. A pattern is something observed across cases. A mechanism is a claim about why an
outcome occurred.

```text
COMMON_PATTERN
  pattern
  present_in_cases
  absent_in_cases
  exceptions
  what_it_describes             behaviour, structure, timing, positioning, endowment
```

Before promotion from pattern to candidate mechanism, run an explicit factor-by-factor comparison. Every material
candidate success factor receives a row; a mechanism list written after separate case narratives is not a substitute.

```text
EXPLICIT_TWO_SIDED_FACTOR_TEST
  candidate_factor
  success_side_cases             named eligible success cases
  success_side_evidence          source-backed observation(s), not a narrative assumption
  success_side_state             PRESENT / ABSENT / UNKNOWN / NOT_COMPARABLE
  negative_side_cases            named verified comparator(s)
  negative_side_evidence         source-backed observation(s), including limits
  negative_side_state            PRESENT / ABSENT / UNKNOWN / NOT_COMPARABLE
  factor_classification          SHARED_NON_DISCRIMINATING /
                                 PLAUSIBLY_DISCRIMINATING / UNKNOWN_UNTESTABLE
  observed_outcome_difference    descriptive only
  alternative_explanations       competing explanations compared across both outcome sides
  evidence_ceiling               comparator count, match quality, access and publication-bias limits
```

State rules:

- `PRESENT` requires affirmative evidence on that named side. `ABSENT` requires affirmative evidence that the
  factor was not present; silence, an inaccessible source, or an omitted detail is `UNKNOWN`, not `ABSENT`.
- `NOT_COMPARABLE` means the factor cannot be evaluated across the named cases because context or measurement is
  materially incompatible. It is not evidence of difference.
- `SHARED_NON_DISCRIMINATING` means the factor is evidenced on both outcome sides and therefore cannot explain the
  outcome difference by itself.
- `PLAUSIBLY_DISCRIMINATING` requires an evidenced difference across the two sides. It remains a candidate, not
  causal proof, and must carry alternative explanations and the evidence ceiling.
- `UNKNOWN_UNTESTABLE` applies when either side is `UNKNOWN` or `NOT_COMPARABLE`, or when no verified comparator
  exists. It may support only an evidence-gathering action.
- One close confirmed negative comparator is sufficient to run this bounded comparison. State that the negative
  side is thin and do not generalize beyond the named cases.
- An unconfirmed, excluded, or merely searched-for negative case never enters `negative_side_cases`. It remains in
  `CONSIDERED_AND_EXCLUDED` or `NEGATIVE_CASE_SEARCH` as search-gap evidence; never promote it to a comparator fact.

Only after this table is complete may a factor enter the compatible mechanism discrimination object:

```text
MECHANISM_DISCRIMINATION
  candidate_mechanism
  explicit_two_sided_factor_row pointer to the completed factor test
  present_in_success_set        legacy-compatible rendering of named success-side evidence
  present_in_comparator_set     legacy-compatible rendering of named negative-side evidence
  verdict                       DISCRIMINATING / NON_DISCRIMINATING / UNTESTED_NO_COMPARATOR
  alternative_explanations
  endowment_or_tactic           per SUCCESS_FAILURE_AND_REPLICABILITY endowment separation
  causal_confidence             HIGH / MEDIUM / LOW / UNKNOWN
  what_would_falsify_it
```

Rules:

- `NON_DISCRIMINATING` — the feature also appears among comparators. It may not be called a
  success mechanism, and it may not be the basis of a build recommendation. Report it as a
  category norm or table-stakes attribute.
- `UNTESTED_NO_COMPARATOR` — may not be named a `LIKELY_SUCCESS_MECHANISM`, and may not by itself
  justify a `P0` build action. It may justify a validation action.
- `DISCRIMINATING` — still not causal proof. Carry `alternative_explanations` and
  `causal_confidence` forward into the report exactly as the causal contract requires.
- Map `SHARED_NON_DISCRIMINATING` to `NON_DISCRIMINATING`, `PLAUSIBLY_DISCRIMINATING` to
  `DISCRIMINATING`, and `UNKNOWN_UNTESTABLE` to `UNTESTED_NO_COMPARATOR` for compatibility. The richer factor
  classification and both per-side states remain visible in the client-facing comparison.

**No fake precision.** This is a descriptive check over a handful of named cases. Do not compute
or state percentages, rates, proportions, success probabilities, significance, sample-derived
confidence, or any invented base rate from the case set. Verdicts are ordinal and justified in
words. Small named counts may be shown as counts of named cases and never generalized to a
population.

## 5. USER_CASE_GAP_DIAGNOSIS

Compare the user's case against the case set and the surviving mechanisms. Every material
difference receives exactly one of five values.

```text
GAP_ROW
  attribute                     the specific, observable difference
  user_case_state
  success_side_comparison       state and finding from the named success side
  negative_side_comparison      state and finding from the named negative/low-outcome side
  two_sided_factor_basis        pointer to EXPLICIT_TWO_SIDED_FACTOR_TEST, or stated unavailable reason
  market_case_state             compact synthesis of both sides
  classification                STRENGTH / WEAKNESS / DIFFERENTIATOR /
                                IRRELEVANT_DIFFERENCE / UNKNOWN_NEEDS_TEST
  why_this_classification       tied to a mechanism verdict or to stated evidence
  decision_impact               what it changes for the frozen decision
  what_evidence_would_reclassify_it
```

Classification definitions — these are distinct and must not be collapsed:

- `STRENGTH` — the user's state is better placed against an evidenced mechanism.
- `WEAKNESS` — the user's state is worse placed against an evidenced mechanism.
- `DIFFERENTIATOR` — a difference that is not a deficiency; it may be an advantage, a deliberate
  narrower scope, or an unexploited position. **A difference from successful cases is not
  automatically a weakness.**
- `IRRELEVANT_DIFFERENCE` — a real difference with no evidenced link to the outcome. Naming it as
  such is a finding, not a gap.
- `UNKNOWN_NEEDS_TEST` — the classification depends on evidence that does not exist yet.

Rules:

- Every row carries `what_evidence_would_reclassify_it`. A classification without a reclassifier
  is labelling, not diagnosis.
- When a verified negative comparator exists, every material row explicitly consumes both
  `success_side_comparison` and `negative_side_comparison`; comparing the user only with leaders is incomplete.
  If the negative side is thin, preserve that evidence ceiling in the row rather than dropping the side.
- A difference from the success set defaults to **nothing**. It must be argued into `WEAKNESS`
  against a `DISCRIMINATING` mechanism, or it is `DIFFERENTIATOR`, `IRRELEVANT_DIFFERENCE` or
  `UNKNOWN_NEEDS_TEST`.
- A row resting on a `NON_DISCRIMINATING` or `UNTESTED_NO_COMPARATOR` mechanism may not be
  `WEAKNESS`. It is at most `UNKNOWN_NEEDS_TEST`.
- An unresolved `UNKNOWN_NEEDS_TEST` may **not** later be silently re-labelled `WEAKNESS` or
  `DIFFERENTIATOR`. Reclassification requires the named evidence to actually arrive.
- If the user's product facts are missing, read accessible product material first, then mark the
  row unavailable/UNKNOWN and continue; ask only through the QUESTION_GATE
  (`references/modules/PROMPT_SKILL_INDEPENDENCE.md` §3 — before answering only when the product
  cannot be identified at all). Do not invent the product. The product-fact provenance firewall in
  `references/modules/MARKET_RESEARCH_DELIVERABLES.md` section 4 continues to apply.

### Routing UNKNOWN_NEEDS_TEST — one path only

A `UNKNOWN_NEEDS_TEST` row that requires real-world primary evidence enters the **existing**
direct-research contract unchanged:

```text
EVIDENCE GAP
→ METHOD OPTIONS
→ FIELDPILOT RECOMMENDATION (optional; not selection)
→ USER CHOICE / DEFENSIBLE COMBINATION / SKIP
→ CUSTOM KIT (only for selected method(s))
```

This module creates **no** second direct-research path, no parallel kit, and no new gate.
Recommendation is still not selection. `SKIP` remains available and non-terminal: on skip, the row
stays `UNKNOWN_NEEDS_TEST`, `direct_research_status: SKIPPED_BY_USER` is recorded, the affected
conclusions and claim ceiling are stated, and the report still completes.

## 6. PRIORITIZED_ACTION_AND_DO_NOT_BUILD

The gap diagnosis becomes decisions, not a feature wishlist.

```text
PRIORITIZED_ACTION
  band                          P0 / P1 / P2 / NOT_YET / DO_NOT_BUILD
  action
  mechanism                     why this is expected to change the outcome
  expected_decision_value       what it lets the user decide that they cannot decide now
  evidence_basis                pointer to the GAP row, mechanism verdict, or finding
  basis_coverage_state          ANSWERED / PARTIAL / UNKNOWN, inherited from the COVERAGE_AUDIT
  required_evidence             what must be true or observed for this to be worth doing
  stop_hold_pivot_condition     where applicable
```

Band definitions:

- `P0` — must be validated or fixed now, because the decision cannot be made without it.
- `P1` — next, if value is confirmed by the P0 result.
- `P2` — later or at scale stage.
- `NOT_YET` — defensible eventually, but premature on current evidence.
- `DO_NOT_BUILD` — actively advised against on current evidence, with the reason and the
  condition that would reopen it.

Hard rule — **recommendation strength may not exceed evidence strength**:

> An action whose `basis_coverage_state` is `UNKNOWN` may only be a **validation** action. It may
> never be a build, spend, hire, launch or commitment action, at any band.

An action resting on a `NON_DISCRIMINATING` or `UNTESTED_NO_COMPARATOR` mechanism inherits the
same restriction. Every material action additionally carries its `IMPACT_VERIFICATION` chain
(`ACTION -> MECHANISM -> OBSERVABLE METRIC/STATE -> MEASUREMENT CONTEXT -> DECISION CHECK ->
CAUSAL CAVEAT`) with no invented numeric thresholds, exactly as
`references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` requires.

## 7. Interaction with existing contracts

- Causal explanation, endowment-versus-tactic separation, the Replicability Engine and Founder
  Feasibility remain governed by `references/modules/SUCCESS_FAILURE_AND_REPLICABILITY.md`.
- Coverage states, sufficiency and claim ceilings remain governed by
  `references/delivery/EVIDENCE_PLAN_AND_COVERAGE_AUDIT.md`. Source counts are never sufficiency.
- The final-report rendering of every object above is defined in
  `references/modules/MARKET_RESEARCH_DELIVERABLES.md` section 9.
- Nothing here weakens negative evidence, substitutes, falsifiers, STOP/HOLD/PIVOT, evidence-state
  separation, or the direct-research method-choice contract.
- The explicit two-sided factor test does not authorize new research or a fabricated comparator. It operates on
  the verified case set already available and preserves exclusions and search gaps exactly as recorded.

## 8. Failure modes this module exists to prevent

- Famous, funded or merely surviving products entering the case set as "successes" by default.
- A single success anecdote generalized into a market pattern.
- Comparators omitted, then their absence presented as balance.
- "We found no failures" silently substituted for "we did not look".
- A shared feature of winners promoted to a causal success factor without a comparator check.
- A factor table that treats silence on either side as evidence of absence.
- A user-case diagnosis that cites only successful cases after a negative comparator was verified.
- Every difference from the winners rendered as a weakness, erasing legitimate differentiation.
- `UNKNOWN` quietly hardening into `WEAKNESS` between drafts.
- A priority list that reads as a plan while resting on untested mechanisms.
- Case-set arithmetic presented as statistics.
