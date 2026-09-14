# EXECUTIVE_DECISION_LAYER + IMPACT_VERIFICATION

Adjacent P1 safeguards. These standardize behavior FieldPilot already demonstrates in its strongest
outputs; they do not add a new research capability and must not change any evidence rule.

## 1. EXECUTIVE_DECISION_LAYER — universal front layer

Every customer-facing research deliverable opens with a stable layer, before the technical evidence:

```text
DECISION            the decision this research serves, restated from the frozen brief
DIRECT ANSWER       the answer to that decision, at the confidence the evidence supports
DECISIVE INSIGHTS   3-5 insights that actually drive the answer
RECOMMENDATIONS     prioritized, each carrying its impact-verification chain (section 2)
CONFIDENCE          confidence and the conditions under which it holds
COUNTEREVIDENCE     the strongest disconfirming evidence or the best reason not to act
LIMITATIONS         the material limitations a decision-maker must carry
NEXT VERIFICATION   the smallest next action or evidence acquisition that would move the decision
```

Rules:

- A blind reader must be able to recover the decision, the reasoning and the next action from this layer
  alone, without the technical appendix.
- The layer summarizes; it never contains a claim that is stronger than the body supports.
- `COUNTEREVIDENCE` is mandatory and may not be softened into a generic risk sentence. Where the honest
  answer is HOLD, STOP, PIVOT, or "this may not need to exist", the layer says so in the direct answer.
- `NEXT VERIFICATION` follows the existing smallest-next-validation and anti-feature-bloat behavior. It
  is one bounded next step, not a roadmap.
- When the user explicitly asked for exactly one final next action, the deliverable's closing
  instruction names exactly one immediate action; any further step is a labeled conditional follow-up,
  not a second immediate instruction stacked in the same line. See `SINGLE_NEXT_ACTION_CONTRACT`
  (`references/modules/BOUNDED_BEHAVIORAL_CLOSURE_REPAIR.md` §5).
- Technical evidence, sources and the delivery envelope remain below, complete and unabridged. The
  executive layer never becomes a reason to delete evidence or limitations from the body.
- **Exactly one current verdict.** When material new evidence changes the `DIRECT ANSWER` mid-engagement,
  this layer is rewritten in place to the current verdict; a superseded verdict moves to a dated revision/
  history subsection in the body rather than remaining here with a "see later section" pointer. See
  `references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md` §2, which governs the interaction with the v1.7
  refresh/history model in `references/modules/RESEARCH_REFRESH_AND_CHANGE_IMPACT.md`.

## 2. IMPACT_VERIFICATION — recommendation chain

Each consequential recommendation carries, where applicable:

```text
ACTION                what to do
MECHANISM             why it would work — the expected causal path
OBSERVABLE METRIC     the metric or state that would actually move, and that the user can see
MEASUREMENT CONTEXT   where and when it is measured, and against what comparison
DECISION CHECK        what result continues, changes, or stops the action
CAUSAL CAVEAT         what else could produce the same observation
```

Rules:

- **No invented thresholds.** Do not manufacture numeric cut-offs, conversion rates, sample sizes,
  budgets or durations that no evidence supports. A qualitative decision check is correct and complete
  when quantitative precision is not defensible (`R-NUMERIC-01`).
- A numeric threshold may be used only when its source, denominator, context and generalization limit
  travel with it.
- The decision check must be **feasible** for this user with the resources they actually have. A check
  that requires traffic, budget, users, instrumentation or access they do not have is not a check.
- `CAUSAL CAVEAT` is required: name at least one rival explanation for the observation the metric would
  produce (`R-CAUSAL-LANG-01`).
- Prefer tying the check to a natural usage opportunity or the next spend decision rather than inventing
  a calendar window.

## 3. Claim ceiling preservation

Recommendation strength may not exceed evidence strength.

```text
UNKNOWN coverage   -> no directional recommendation; the recommendation is to acquire evidence
PARTIAL coverage   -> recommendation bounded to the covered slice, with the uncovered slice named
ANSWERED coverage  -> recommendation bounded by the claim ceiling of that evidence class
```

Desk evidence, however complete, does not establish this product's demonstrated demand, willingness to
pay, causal effect, or superiority over an alternative. The executive layer inherits every claim ceiling
from the body; it does not get to round them off for readability.

## 4. Preserved behavior

This module does not modify:

- negative evidence and "why this may not need to exist";
- strong substitutes including general AI, manual workarounds and do-nothing;
- `CURRENT_FACT` / `INFERENCE` / `UNKNOWN_BOUNDARY`;
- confidence, falsifier and reversal conditions;
- `STOP` / `HOLD` / `PIVOT` gates;
- the direct-research method-choice contract and `SKIP` semantics;
- `REAL` vs `PLANNED` / `EXAMPLE_ONLY` / `QA` evidence-state separation;
- v1.7 refresh and delta behavior.

Where this layer and any of the above appear to conflict, the preserved behavior governs.

## 5. Rule and source anchors

Rule anchors: `R-DEC-01`, `R-CLAIM-01`, `R-NEG-01`, `R-NUMERIC-01`, `R-CAUSAL-LANG-01`.
Source anchors: `S-ESOMAR`, `S-CAUSAL-LANG`.
