# EVIDENCE_PLAN + COVERAGE_AUDIT — method, coverage and sufficiency contract

Applies to every material research question frozen in `CLIENT_DECISION_BRIEF`.

Source count is not coverage. Eight sources or twenty-nine sources are equally uninformative about
whether the decision-relevant population, geography and time period were actually covered. This module
replaces "how much did we gather" with "why does this evidence resolve this question, and what is still
uncovered".

## 1. EVIDENCE_PLAN — before collection

For each **material** question (not for every question, and never for a question the brief already
answers), record one compact row:

```text
research_question_id
uncertainty_to_resolve
method_or_source_class
why_fit_for_purpose               why this method/source class can actually resolve this uncertainty
target_population_or_source_universe
unit_of_analysis
coverage_segment                  decision-relevant segments/buyer roles this must cover
coverage_geography
coverage_time_period              period the evidence must describe, and freshness requirement
evidence_independence             first-party / independent / community / administrative / vendor / primary
known_weakness_or_bias            expected error mode of this method/source class
triangulation_partner             complementary or counter-source that offsets that weakness
alternative_explanation_check     what rival explanation this evidence must be able to distinguish
sufficiency_rule                  what state of evidence answers this question well enough to decide
stop_rule                         when to stop collecting for this question
```

### Plan design rules

- **Complementarity over volume.** Prefer the smallest evidence set whose weaknesses offset each other.
  Two sources with different failure modes beat six sources with the same failure mode.
- **No arbitrary minimum source counts.** Never impose "at least N sources" as a quality bar, and never
  report a source count as if it were evidence of sufficiency.
- **Stop when the stop rule fires.** Once the sufficiency rule for a question is met, additional similar
  sources do not expand the search. Redundant collection is not thoroughness.
- **Vendor material is vendor material.** A vendor's own page is evidence of what the vendor claims and
  publishes. It never becomes independent proof of that vendor's performance or superiority.
- **Short form for short jobs.** For a bounded desk question, the plan is a few compact lines held
  internally, surfaced as the method and coverage rationale of the answer. Do not impose agency-scale
  paperwork on a single-question request.
- The plan is written **before** collection so that it constrains collection. A plan reconstructed after
  the fact to justify whatever was found is not an evidence plan.

## 2. COVERAGE_AUDIT — at synthesis

For each material question, produce a terminal coverage state:

```text
question_id
coverage_state        ANSWERED | PARTIAL | UNKNOWN
evidence_basis        what actually resolved it (or failed to)
material_gap          the exclusion/uncovered segment/period/geography that remains
claim_ceiling_effect  the strongest claim this evidence state can support
```

### Coverage-state definitions — these are distinct and must not be collapsed

```text
ANSWERED   the question's sufficiency rule is met by evidence that covers the decision-relevant
           population, geography and time period. Residual uncertainty is bounded and stated.

PARTIAL    real evidence exists and constrains the answer, but a material segment, geography, time
           period or mechanism is uncovered, or the available evidence cannot separate rival
           explanations. Claims are bounded to the covered slice and the uncovered slice is named.

UNKNOWN    eligible evidence does not resolve the question. No directional claim is made. If primary
           evidence is what is missing, this is the boundary at which the existing direct-research
           flow is invoked, not a place to speculate.
```

Rules:

- `PARTIAL` is never reported as `ANSWERED` with a caveat sentence. The state itself is the disclosure.
- A conclusion may not generalize past the coverage recorded for the questions it rests on. A hidden or
  uncovered subgroup caps the claim; it does not get averaged away.
- A stale source cannot support a current-fact claim. Either refresh it, or downgrade the claim to a
  historical/scoped statement (`R-SOURCE-01`, `R-NUMERIC-01`).
- A geography mismatch between the evidence and the decision is a coverage gap, not a detail.
- `UNKNOWN` at a primary-evidence boundary routes into the unchanged direct-research flow:
  `EVIDENCE GAP -> METHOD OPTIONS -> USER CHOICE / defensible combination / SKIP`. It never routes into invention.
- When the user selects `SKIP`, the affected questions stay `UNKNOWN` or `PARTIAL` and the claim ceiling
  is recorded. `SKIP` does not upgrade a coverage state.

## 3. Triangulation and alternative explanations

For every material conclusion, the plan must have arranged evidence that can, at least in principle,
distinguish the conclusion from its strongest rival explanation. Where it cannot, say so: the conclusion
is then association-bounded, not causal (`R-CAUSAL-LANG-01`, `R-TRI-01`).

Triangulation means sources whose errors are *independent*. Three outlets reprinting one press release
is one source.

## 4. Interaction with existing contracts

- Coverage states feed claim ceilings; they never override them. An `ANSWERED` coverage state on a
  desk-research question still cannot manufacture demonstrated demand, WTP, TAM precision, causality or
  superiority.
- Negative evidence and disconfirming findings are not "gaps to be closed". A question can be `ANSWERED`
  with an answer the user does not want.
- The direct-research method-choice contract is unchanged: this module identifies *which* questions
  still need primary evidence; the user still chooses the method, a defensible combination, or `SKIP`.
- For a returning-user refresh, the coverage audit is recomputed only for revalidated dependencies;
  untouched questions keep their prior coverage state with its baseline pointer.

## 5. Failure modes this module exists to prevent

- source-count theatre standing in for coverage;
- plausible but incomplete recommendations built on an uncovered segment or geography;
- stale numbers presented as current facts;
- vendor marketing promoted to independent performance evidence;
- redundant collection that inflates cost without reducing uncertainty;
- `PARTIAL` evidence quietly narrated as a settled answer.

## 6. Rule and source anchors

Rule anchors: `R-DESK-01`, `R-SOURCE-01`, `R-TRI-01`, `R-NEG-01`, `R-CAUSAL-LANG-01`, `R-NUMERIC-01`,
`R-CLAIM-01`.
Source anchors: `S-ESOMAR`, `S-ISO-20252`, `S-TRIANGULATION`, `S-AAPOR-DISC`.

These anchor professional duties of method fitness, coverage reasoning and disclosure. The three-state
coverage vocabulary and the stop-rule contract are FieldPilot operational rules, not external
prescriptions.
