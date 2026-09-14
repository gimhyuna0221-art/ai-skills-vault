# CLIENT_DECISION_BRIEF — universal pre-research decision contract

Applies to every substantive FieldPilot research run: full market research, bounded desk question,
returning-user refresh, and any run that will produce a customer-facing deliverable.

This module answers one question before evidence collection starts: **whose decision is this research
for, and what would change it?** A technically sophisticated report that answers the topic instead of
the buyer's decision is a professional failure even when every fact in it is correct.

It is a framing contract, not an intake questionnaire. It must never become a gate that delays a simple
request.

## 1. Required brief fields

Freeze these before substantive evidence collection. Every field carries an explicit provenance label.

```text
decision_to_be_made
decision_owner_or_primary_user
decision_horizon_or_deadline          (when material)
stakes_or_cost_of_wrong_decision
current_hypothesis_or_assumptions
primary_research_objective
secondary_research_questions          (material questions only; typically 3-7)
scope_in
scope_out
constraints                           (geography, budget, timing, evidence access, compliance/sensitivity)
what_evidence_would_change_the_decision
intended_action_or_choice_set
desired_decision_effect               (success criterion / intended business impact)
```

`secondary_research_questions` are the **material questions**: the ones whose answer could change the
decision, the chosen action, or the confidence attached to it. A question that cannot change anything
is not material and does not belong in the brief, no matter how interesting it is.

## 1a. Subject frame — whose market is being researched

A decision frame alone does not identify the market. Before broad evidence collection, also fix
what the research is *about*, so the run investigates the user's actual market rather than the
topic that superficially resembles it.

```text
SUBJECT_FRAME
  user_product_or_case              what the user actually built or is considering
  target_customer_or_segment        who is supposed to use it, and who pays if different
  geography                         when decision-relevant
  channel_or_platform               where it reaches users: store, web, marketplace, direct, offline
  business_model                    free, ad-supported, subscription, one-off, usage-based,
                                    marketplace take, B2B contract, internal tool, undecided
  lifecycle_stage                   idea, prototype, internal pilot, launched, monetizing, scaling
```

Rules:

- Every field carries a section 2 provenance label. `INFERRED` and `ASSUMED` values are rendered
  to the user with their label so they can be corrected; `UNRESOLVED` is a legitimate terminal
  state that propagates into scope, coverage and the delivery envelope.
- Include only fields that are material to this decision. An immaterial field is marked
  `NOT_MATERIAL`, not filled with a guess.
- **This is not an intake questionnaire.** Section 3's question economy governs unchanged: ask only
  where a missing value would change the recommended next step and cannot be defensibly inferred,
  and batch what you ask. A simple request is never gated behind a form.
- Never invent a target customer, geography, channel, business model or stage the user has not
  given and that cannot be defensibly inferred. The product-fact provenance firewall in
  `references/modules/MARKET_RESEARCH_DELIVERABLES.md` section 4 continues to apply: a described
  outcome does not establish the implementation behind it.
- `geography` also feeds the conditional regulatory check in
  `references/modules/REGULATORY_CONTEXT_CHECK.md`, and `decision_horizon_or_deadline` feeds the
  scoped freshness policy in `references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md`. Neither is asked
  for a second time.

## 2. Field provenance labels — never silently invent

Every field is one of:

```text
STATED        the user said it
INFERRED      derived from what the user said or showed; the derivation is defensible and visible
ASSUMED       a working default adopted to proceed; not derived from user input
ASKED         resolved by a clarifying question in this run
UNRESOLVED    still open and material; recorded as an open brief item
```

Rules:

- `INFERRED` and `ASSUMED` fields must be rendered to the user with their label so they can be corrected.
  A safe inference is allowed; a silent one is not.
- A material field may not be filled with `ASSUMED` content presented as fact.
- `UNRESOLVED` is a legitimate terminal state for a field. It propagates into `EVIDENCE_PLAN` scope and
  into the delivery envelope's assumption list. It does not silently disappear.
- Never invent a decision owner, a budget, a deadline, a geography, a buyer, or a success criterion the
  user has not given and that cannot be defensibly inferred.

## 3. Question economy — ask only decision-changing questions

Ask the user only when **all** of these hold for the missing field:

1. the field is material to the decision;
2. it cannot be defensibly inferred from what the user already provided;
3. different plausible values would lead to a materially different method, scope, or conclusion.

If a missing value would not change the work, adopt a labeled `ASSUMED`/`INFERRED` default and proceed.

Batch all genuinely necessary questions into one short block. Do not serialize clarification across
several turns. A simple bounded request must not be converted into an intake interview: for a short
single question, the brief may be compiled internally in compact form and surfaced only as the scope and
assumption lines of the answer.

This preserves the existing novice contract (`R-NOVICE-01`) and the recommendation-first behavior for
bounded questions.

## 4. Freeze, reference, and change control

- The brief is **frozen** before substantive evidence collection and pinned to the run.
- Every material finding, interpretation, and recommendation in the final deliverable must trace to a
  frozen objective or research question. An insight that traces to nothing is either out of scope or the
  brief was wrong.
- Scope changes are **visible**, never silent. When the run expands beyond `scope_in`, record a scope
  change: what changed, why, who requested or authorized it, and its effect on effort and claim ceilings.
- Anything in `scope_out` that a reader might expect stays listed as an explicit exclusion in the
  delivery envelope. Silent scope creep and silent scope shrink are both defects.

## 5. Interaction with existing contracts

- The brief does **not** replace or reorder the direct-research contract. `EVIDENCE GAP -> METHOD OPTIONS
  -> FIELDPILOT RECOMMENDATION (optional) -> USER CHOICE / defensible combination / SKIP -> CUSTOM KIT`
  is unchanged. The brief only establishes what the gap is a gap *for*.
- For a returning-user refresh, the prior brief is reused when a valid `ResearchBaseline` exists. Record
  which brief fields changed since the baseline; a changed decision or horizon is itself a material
  change that can invalidate prior recommendations.
- `desired_decision_effect` is a success criterion for the decision, not a promise of outcome, and never
  a basis for a superiority or demand claim (`R-CLAIM-01`).

## 6. Failure modes this module exists to prevent

- topic-shaped research that never names the decision it serves;
- invented stakeholders, budgets, deadlines or buyers;
- silent scope drift that inflates effort and confuses acceptance;
- clarification loops that punish simple requests;
- final recommendations that answer a question nobody asked.

## 7. Rule and source anchors

Rule anchors: `R-DEC-01`, `R-CLAIM-01`, `R-NOVICE-01`, `R-AUDIT-01`.
Source anchors: `S-ESOMAR`, `S-ISO-20252`.

These anchor professional duties of decision framing, agreed scope and client communication. They do not
prescribe the field list above, which is a FieldPilot operational contract.
