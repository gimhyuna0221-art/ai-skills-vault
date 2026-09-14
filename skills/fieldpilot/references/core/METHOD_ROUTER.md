# Method Router — Runtime Contract

Load this reference after `PROPOSITION_AND_EVIDENCE.md` and domain preflight, and before creating a `MethodDecision`. Detailed cards live in `methods/`. This router is proposition-driven: it never uses `interview -> survey -> pilot`, `experiment > survey > interview`, or another universal sequence/ranking.

## Inputs and blocking checks

Require these active revisions:

```yaml
router_input:
  business_decision:
  proposition:
  required_evidence_contract:
  domain_preflight:
  existing_evidence: []
  decision_stakes:
  access_constraints: []
  time_cost_constraints: []
  ethics_legal_constraints: []
```

Do not finalize a route if the decision, proposition, or evidence contract is materially incomplete. Do not treat a preferred method as a proposition. Preserve the preference, explain the fit test, and continue from the decision-relevant question.

## Admissibility algorithm

1. Validate decision, uncertainty, proposition, requested scope, and evidence contract.
2. Activate every applicable domain adapter. An unresolved permission, safety, safeguarding, unit-of-analysis, or claim-validity field blocks affected fieldwork.
3. For each candidate card, compare every mandatory evidence dimension: construct, behavioral proximity, sampling/coverage, comparison, context, temporal, precision, replication, provenance, and ethics.
4. Reject any method that fails a hard dimension. Scores, low cost, user preference, or easy access cannot compensate.
5. Instantiate the surviving cards' sample, instrument, execution, analysis, access, and ethics prerequisites.
6. Select the least burdensome sufficient method, or the smallest sufficient portfolio. “Least burdensome” applies only among admissible routes.
7. If equally sufficient, prefer in order: lower ethics/legal/safeguarding risk; lower execution-failure risk; lower participant burden; lower decision-relevant time/cost. Preserve user-supplied weights and show tradeoffs. Use stable method-card ID only as a reproducibility fallback.
8. Emit allowed and forbidden claim grammar, supported and unsupported propositions, rejected alternatives, unresolved dimensions, access plan, and expected failures.
9. Persist the active card/rule revisions and dependencies.
10. If no route is sufficient, return one explicit reality outcome below. Never revise the contract silently.

Admissibility is Boolean per mandatory dimension. A favorable aggregate score cannot rescue a failed dimension.

## Reality outcomes

Return exactly one of:

- `CONTRACT_SATISFIABLE`: the selected route can meet the active contract.
- `CONTRACT_SATISFIABLE_WITH_DESIGN_CHANGES`: a valid route exists after named acquisition/design changes.
- `CONTRACT_PARTIALLY_SATISFIABLE`: identify every unsupported dimension and cap the claim.
- `CLAIM_NARROWING_REQUIRED`: propose a new proposition/contract revision and state what it no longer covers; require explicit acknowledgement.
- `NOT_CURRENTLY_ANSWERABLE`: retain the unmet contract and blocking reality.
- `ETHICS_OR_LEGAL_BLOCK`: stop and name the required qualified review or safe route.

If access is difficult, first try an equivalent frame/channel/site/instrument, trust or burden redesign, warm introduction, different evidence-holder, or parallel access path that preserves the contract. `CONTACT_ATTEMPT_FAILED`, `DELIVERED_NO_RESPONSE`, `REFUSED_RESEARCH`, and `REFUSED_OFFER` are different evidence. Access failure is not demand failure; when commercially material, create a separate `IMPLEMENTATION_OR_FEASIBILITY` or `BUYING_SYSTEM` proposition.

## Question-to-family candidate map

This map proposes candidates; the evidence contract and card determine admissibility.

| Proposition/question | Consider first | Do not assume |
|---|---|---|
| Existing fact, constraint, benchmark, definition | `SECONDARY_DESK` | A source statistic transfers to the target market |
| Alternatives, workarounds, switching, do nothing | `COMPETITOR_ALTERNATIVE` | Feature presence proves preference or demand |
| Defined market magnitude/capacity | `MARKET_SIZING` | Market size proves demand |
| Decision-useful group differences | `SEGMENTATION` | Familiar labels or one cluster run reveal natural types |
| Meaning, experience, mechanism, customer language | `HUMAN_DEPTH_INTERVIEW`; optionally `AI_MODERATED_INTERVIEW` with mode safeguards | Case patterns estimate prevalence |
| Situated workflow, workaround, task behavior | `OBSERVATION_CONTEXTUAL` | Observed behavior reveals unobserved motive or voluntariness |
| Interaction, shared language, contested meaning | `FOCUS_GROUP` | Group utterance counts are independent prevalence |
| Recurrence, journey, delayed or changing context | `DIARY_LONGITUDINAL` | Entries are verified behavior unless linked to traces |
| Defined-population distribution/difference | `PROBABILITY_SURVEY` when an eligible design exists | A survey is causal or timeless |
| Recruited-sample description/exploration | `NONPROBABILITY_SURVEY` | Opt-in size, quotas, or weighting create ordinary population MOE |
| Response to a standardized idea/stimulus | `CONCEPT_TEST` | Appeal proves usability, purchase, retention, or performance |
| Can specified users complete specified tasks? | `PROTOTYPE_USABILITY` | Task success proves demand or production reliability |
| Instrumented use, pathway, repeat, churn | `BEHAVIORAL_ANALYTICS` | Behavior alone reveals motive or cause |
| Contextual interest action | `FAKE_DOOR_LANDING` | A click/waitlist proves purchase demand or WTP |
| Value/workflow under assisted delivery | `CONCIERGE_WIZARD_OF_OZ` | Assisted success proves self-service, scale, or unit economics |
| What people state/select about price/tradeoffs | `STATED_PRICING_WTP` | Stated WTP equals payment; no fixed correction factor |
| Did a real payment/transaction occur? | `ACTUAL_PAYMENT_PAID_PILOT` | One offer proves market-wide price acceptance or retention |
| Did treatment cause a bounded effect under random assignment? | `AB_RANDOMIZED_EXPERIMENT` | The effect transports across populations/channels/time |
| Is a causal effect identifiable without randomization? | `QUASI_EXPERIMENT` | A favorable before/after or comparison is causal |

## Portfolio compiler

Use multiple methods only when their declared relationship is one of:

- `CONVERGENCE`: independent approaches address the same proposition;
- `COMPLEMENTARITY`: each covers a different required decision dimension;
- `SEQUENCE`: one designs, samples, or tests the next;
- `DISSONANCE_TEST`: one is intended to challenge another.

Record the coverage contribution and integration/analysis path for each method. Do not pool incompatible denominators or assemble a “Frankenstein claim” by borrowing population scope, causal force, or behavior from unrelated evidence. Divergence remains visible and may narrow the claim.

## MethodDecision output

```yaml
method_decision:
  proposition_ids: []
  contract_id_and_revision:
  domain_preflight_id_and_revision:
  considered_methods: []
  selected_method_or_portfolio: []
  portfolio_relationship:
  dimension_coverage: []
  exact_propositions_answered: []
  exact_propositions_not_answered: []
  prerequisites: []
  claim_envelope:
  allowed_claim_templates: []
  forbidden_claim_patterns: []
  access_reality_plan:
  ethics_privacy_safeguarding_conditions: []
  rejected_alternatives_and_rationale: []
  unresolved_dimensions: []
  satisfiability_outcome:
  pinned_method_card_versions: []
  rule_ids: [R-ARCH-01, R-ARCH-02, R-ACCESS-01, R-TRI-01]
```

Before fieldwork, load `SAMPLE_AND_FIELDWORK.md` and every selected method card. Before reporting, run calibration and the Claim-Grammar Gate; a planned envelope may be retained or narrowed after execution, never upgraded because results are favorable.
