# Bounded Behavioral-Closure Repair — v1.9.4

This module is a **bounded follow-up repair**, not a new benchmark campaign or architecture change.
It does not add a multi-agent system, crawler, fixed-query-count search bureaucracy, knowledge graph,
new pricing engine, or renderer. All v1.6.1-v1.9.3 factuality, provenance, uncertainty, negative-evidence,
regulatory, ethics, decision-checkpoint, pricing-anchor, and delivery-consistency controls remain
governing; this module closes the five confirmed gaps found by the real v1.9.3 buyer-like retest
(GitHub Issue #19) against the frozen v1.9.2 evidence baseline.

## 0. Why this module exists

The Issue #19 retest correctly invoked the real Skill and completed live web research, but the final
report still shipped with material defects the v1.9.3 gates should have caught:

1. The report disclosed that it "used the governing layer without individually loading detailed
   reference modules." Being *routed to* a module by name in `SKILL.md` is not the same as the module's
   checks having actually been read and applied in this run — that gap let every v1.9.0-v1.9.3 gate be
   satisfied on paper while never executing.
2. A near-exact direct competitor (SwimRead, `https://swimread.com/en`) was missed before the report
   claimed no strong direct competitor / a whitespace gap.
3. A competitor's listed or preorder price was framed close to proof of paid demand, a finer-grained
   version of the overclaim `LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE` and v1.9.3's `wtp_overclaim_check`
   already bound, but with more evidence states than the existing binary rung distinguished.
4. Current and historical pricing/state figures for the same competitor were blended in one table
   without a time basis, a case `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE` was specified to catch for
   *this product's own* state but had not been extended to third-party pricing rows.
5. The user asked for exactly one final next action; the report closed with a compound two-step
   instruction ("option B → option A") instead.

## 1. `MODULE_LOAD_NO_SKIP_GATE`

Before any `FINAL_MARKET_RESEARCH_REPORT`, refresh, or other deliverable that ships a current
recommendation is finalized, every reference module that `SKILL.md`'s routing tables and version-gate
list mark as triggered for this task must be individually loaded and its checks applied in this run —
not merely cited by name because the governing-layer summary already mentions it.

```yaml
module_load_record:
  module: ""                    # e.g. references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md
  status: LOADED_AND_APPLIED | NOT_APPLICABLE_TO_THIS_DECISION
  applicability_reason: ""      # required when status is NOT_APPLICABLE_TO_THIS_DECISION
```

A module that is triggered by the active task has no third state. Describing a triggered module as
covered because "the governing layer already summarizes it" is the same defect class as recording an
unrun QA check as `PASS` (the existing `PROFESSIONAL DISCLOSURE` self-audit item): an unrun gate
reported as satisfied is a fabrication, not a shortcut. A model may not skip this because the task
looks small or the request is phrased informally — task size is not a gate exemption anywhere else in
this runtime and is not one here.

Exit states: `PASS` (every triggered module has a `LOADED_AND_APPLIED` record), `BLOCKED` (a triggered
module has no record, or is marked `NOT_APPLICABLE_TO_THIS_DECISION` without a reason). `BLOCKED` fails
delivery of the affected deliverable; the runtime loads the missing module and reruns the affected
checks before shipping.

## 2. `DIRECT_COMPETITOR_RECALL_CLOSURE`

Before a report states or implies "no strong direct competitor," "white space," "nobody fills this
gap," or an equivalent claim, run a bounded semantic closure pass. This extends
`references/methods/secondary-and-competitors.md` and `references/modules/MARKET_CASE_COMPARISON_AND_GAP.md`
for exactly this claim class; it does not add a parallel competitor-research path.

Required search angles (no fixed query count — semantic coverage, not a quota):

- exact capability/category phrasing (what the product literally does, in its own words);
- adjacent/synonym phrasing (alternate terms a buyer or the product itself might use);
- current product/app/tool discovery surfaces relevant to the category (app stores, current search
  engines, category directories/listings as applicable);
- first-party page inspection of any near-exact candidate the search surfaces, to confirm or rule out
  the overlap before it is included or excluded.

```yaml
competitor_recall_closure:
  claim: ""                     # e.g. "no strong direct competitor"
  angles_run: []                # which of the four angles above were actually executed
  near_exact_candidates_found: []
  first_party_pages_checked: []
  result: CLOSURE_CONFIRMED_NONE_FOUND | NEAR_EXACT_FOUND_INCLUDED | COVERAGE_INCOMPLETE
```

If a near-exact candidate exists (same or near-identical capability, same buyer, currently live or in
public beta), it must be added to the competitor set and the claim, the affected material questions
(for example the equivalent of "does an alternative already exist" and "what's technically feasible"),
and any technical-feasibility counterevidence/next-verification logic must be updated before the report
ships. If the closure search itself is incomplete (an angle could not be run, or time/tooling bounded
it), the claim ceiling is `SEARCHED_NOT_FOUND` / `COVERAGE_INCOMPLETE`, never a bare "no competitor."

## 3. `COMMERCIAL_EVIDENCE_TAXONOMY_GATE`

Extends `references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md` §1 `wtp_overclaim_check`. That check
correctly forbade promoting `LISTED_OR_CHARGED_PRICE` straight to willingness-to-pay; this gate keeps
the same non-promotion rule but distinguishes the evidence states it collapsed into one rung, because a
preorder deposit, an active checkout, and an observed repeat purchase are not the same evidence weight.

```yaml
commercial_evidence_ladder:            # strictly ascending; a claim may cite its actual rung only
  - LISTED_PRICE                       # a price is published; nothing is confirmed to have transacted
  - ACTIVE_OFFER                       # a live, purchasable offer exists at that price now
  - PREORDER_OFFER                     # a deposit/preorder is being collected against future delivery
  - OBSERVED_PURCHASE                  # at least one real transaction is evidenced
  - OBSERVED_REPEAT_PURCHASE_OR_RETENTION   # repeat/renewal behavior is evidenced
  - PROVEN_WTP                         # only when evidence genuinely supports willingness-to-pay at scale
```

Rules:

- A price page or an active/preorder offer, alone, never becomes "people actually pay," "WTP exists,"
  "pricing works," conversion, or retention. Each rung requires its own evidence; none is inferred from
  a lower rung plus narrative confidence.
- Regression examples this gate must hold: Catch's video-analysis page listing £39.99 / £29.99 Gold
  (`https://www.catchswim.com/video-analysis`) is `ACTIVE_OFFER` (a listed, purchasable price), not
  `OBSERVED_PURCHASE`; MySwimEdge's publicly listed $750 preorder with delivery beginning Oct 2026
  (`https://myswimedge.com/`) is `PREORDER_OFFER`, not `OBSERVED_PURCHASE`/`PROVEN_WTP` — a preorder
  evidences intent to reserve, not completed adoption.
- Record the rung actually evidenced next to the claim; do not round up to the nearest more persuasive
  rung because the lower one reads as weak.

## 4. `CURRENT_STATE_PRICING_FRESHNESS_HIERARCHY`

`references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md` §1 `product_state_currency_check` verifies that a
claim about *this product's own* current state is `CURRENT_VERIFIED` rather than a carried-forward
`STALE_ASSUMPTION`. This gate applies the same basis to third-party pricing/product-state rows that
appear in a current-market comparison table:

```yaml
third_party_pricing_currency_check:
  vendor: ""
  claimed_value: ""
  basis: CURRENT_FIRST_PARTY | LABELED_HISTORICAL | STALE_UNLABELED
  source: ""                    # prefer the vendor's current pricing/product page over older articles
```

- Prefer the vendor's current first-party pricing/product-state page over older articles or stale
  snippets for any row entering a *current* comparison table.
- A historical number may still be used, but only if the row is explicitly dated/labeled as historical
  (for example "as of 2025") rather than presented as the current figure.
- `STALE_UNLABELED` for a row that is decision-controlling routes through
  `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`'s `numeric_entity_check` exactly as a same-referent conflict:
  unresolved and non-decision-controlling narrows the claim, unresolved and decision-controlling is
  `HOLD`.
- Regression examples this gate must hold: FORM's current US product pages show $149 LT / $199 Smart
  Swim 2 / $259 PRO as three distinct current SKUs, not a blended $149-$279 range presented as one
  current price; TritonWear's current official pricing is $287/athlete/year or $31/month with an annual
  commitment and the unit included, which must not be mixed with an older $149/yr + $39 motion-analysis
  structure unless that older structure is explicitly labeled historical.

## 5. `SINGLE_NEXT_ACTION_CONTRACT`

Extends `references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` §1 `NEXT VERIFICATION`. That section
already requires one bounded next step rather than a roadmap; this closes the case where the user
explicitly asks for exactly one final action and the deliverable's closing instruction still names two.

When the user's request explicitly asks for one final next action (for example, "마지막에는 내가 다음에
해야 할 행동을 하나만 정해줘" / "give me exactly one thing to do next"), the deliverable's terminal
instruction line names exactly one immediate action. Any further step the evidence supports is demoted
to an explicitly labeled conditional follow-up that is contingent on the outcome of the first action
(for example, "이 결과가 X이면 다음은 Y" / "if that comes back X, the follow-up is Y") and is not phrased
or sequenced as a second thing to do now ("do A, then do B" as one immediate instruction). This does not
reduce `RECOMMENDATIONS` plurality earlier in the report or remove `NEXT VERIFICATION`'s existing content
— it bounds only the closing single-action instruction the user explicitly asked for.

## 6. Combined exit check

Fail delivery when any of the following holds and is unresolved:

- `MODULE_LOAD_NO_SKIP_GATE` is `BLOCKED` (a triggered module has no load record, or is marked
  not-applicable without a reason);
- a whitespace/no-direct-competitor-class claim ships without a `DIRECT_COMPETITOR_RECALL_CLOSURE`
  record, or with `result: NEAR_EXACT_FOUND_INCLUDED` but the candidate is not actually reflected in the
  claim and dependent sections;
- a commercial claim cites a `commercial_evidence_ladder` rung higher than the evidence recorded for it;
- a `third_party_pricing_currency_check` row is `STALE_UNLABELED`, decision-controlling, and unresolved;
- the user explicitly asked for exactly one final next action and the deliverable's closing instruction
  names more than one immediate action.

Passing this module proves invocation completeness, competitor-recall closure, commercial-evidence
rung discipline, pricing currency, and single-action closure only; it does not itself prove market
demand, WTP, or release readiness — those ceilings are unchanged and remain governed by the existing
v1.9.0-v1.9.3 gates and `references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` §3.
