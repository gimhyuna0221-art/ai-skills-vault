# Bounded Delivery-Quality Repair — v1.9.3

This module is a **wiring and cross-report QA repair**, not a new research capability. It does not add a
new benchmark, scoring system, router, or evidence architecture. All v1.6.1-v1.9.2 factuality, provenance,
uncertainty, negative-evidence, regulatory, ethics, decision-checkpoint, and pricing-anchor controls remain
governing; this module closes one confirmed gap between them and delivery.

## 0. Why this module exists

`references/delivery/PROFESSIONAL_DELIVERY_ENVELOPE.md` §6 previously required only `PROVENANCE_OUTPUT_GATE: PASS`
before delivery. The v1.9.0-v1.9.2 gates (`LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE`, `RETRACEABLE_LOCATOR_FALLBACK_GATE`,
`VALIDATION_RESOLUTION_GATE`, `LITERATURE_HIERARCHY_COMPLETENESS_GATE`) were fully specified in
`references/modules/BOUNDED_BEST_OF_AI_DISTILLATION.md` but were only wired as mandatory in
`references/modules/COMMERCIAL_DELIVERABLE_SYSTEM.md` §11, i.e. only for a "substantial commercial engagement
bundle." A default single-reply `FINAL_MARKET_RESEARCH_REPORT` — the most common delivery shape, and the
exact shape of the Issue #16 real-buyer self-test — never triggered them. Separately, the v1.6 RUNTIME EXIT
CHECK salience checklist in `SKILL.md` was never extended past its original 24 items, so none of the v1.9.0+
gates were part of the pre-answer self-audit either. Both are repaired directly (see `PROFESSIONAL_DELIVERY_ENVELOPE.md`
§6, `MARKET_RESEARCH_DELIVERABLES.md`, and the `SKILL.md` checklist items 25-26) rather than duplicated here.

This module adds the one class of check that did not exist anywhere before v1.9.3: cross-report
numeric/entity/commercial consistency, current-verdict singularity, and current subject/sale-mode locking.

## 1. `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`

Activate before any customer-facing deliverable ships and after every refresh/revision, alongside
`PROVENANCE_OUTPUT_GATE`. Run a bounded internal consistency pass over the summary, body, and any table/figure
of the deliverable being rendered — not a new research task, just a re-read of what is about to be sent.

Check for, and resolve before delivery:

```yaml
numeric_entity_check:
  conflicting_figures: []       # e.g. "3,000,000" (market-wide claim) vs "300,000" (named competitor's
                                 # actual user count) used interchangeably for the same referent
  metric_identity_check: []     # e.g. "users" vs "interactions/sessions/messages" treated as the same number
  unit_period_geography_scope: []  # currency, billing cadence, date window, country/market, or population
                                    # scope silently swapped between two numbers being compared
product_state_currency_check:
  claim: ""
  basis: CURRENT_VERIFIED | STALE_ASSUMPTION | UNKNOWN
  # A claim about this product's OWN current state (supported runtime/environment, feature set, pricing mode)
  # is CURRENT_VERIFIED only if checked against this engagement's actual current evidence (the skill's own
  # declared scope, the user's statement, or a live check) in this run. Carrying forward an earlier
  # engagement's framing (e.g. "Claude-only") without re-checking is STALE_ASSUMPTION, not fact.
commercial_mode_check:
  product_sale_mode: ""         # this product's actual distribution/commercial mechanism, e.g. downloaded
                                 # one-time skill install, pay-per-run hosted execution, or subscription
  anchor_sale_mode: ""          # each pricing/positioning anchor's actual mechanism
  mode_compatible: PASS | SALE_MODE_MISMATCH | UNKNOWN
  # Comparing a subscription/pay-per-run hosted competitor directly against a downloaded one-time-install
  # product without disclosing the mode difference is a SALE_MODE_MISMATCH; narrow the comparison to what
  # actually transfers (e.g. price magnitude as a loose prior) rather than treating them as equivalent.
wtp_overclaim_check:
  claim: ""
  evidence_type: LISTED_OR_CHARGED_PRICE | OBSERVED_CONVERSION | OBSERVED_RETENTION | UNKNOWN
  # A comparator's listed or currently-charged price is evidence that the PRICE POINT exists and is not
  # rejected by the platform; it is never, by itself, evidence of THIS product's proven willingness to pay,
  # conversion, or retention. This extends `LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE`'s existing
  # `COMPARABLE_MODEL_PRIOR` rule (`references/modules/BOUNDED_BEST_OF_AI_DISTILLATION.md` §1): the rule already
  # covered anchoring a *proposed* price; this closes the same gap for framing an *observed competitor's*
  # price as validated demand ("premium pricing works") rather than as a prior.
incomparable_anchor_check:
  anchor: ""
  comparability_gap: ""
  # Record when an anchor is materially incomparable (different buyer, different job-to-be-done, different
  # sale mode, different maturity/user-base stage) and is nonetheless being used as a direct price/positioning
  # anchor. Narrow the claim to what the anchor can actually support.
resolution: PASS | NARROWED | HOLD
```

If a conflict, mismatch, or overclaim is found and cannot be resolved from evidence already in hand, narrow
or remove the claim and state the narrower, defensible version. If the unresolved item is decision-controlling
(it would change the recommendation), the deliverable's verdict for that decision becomes `HOLD` rather than
inventing certainty — this reuses the existing `STOP`/`HOLD`/`PIVOT` vocabulary
(`references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` §4), it does not add a new state.

Exit states: `PASS` (no conflicts found or all found were resolved), `NARROWED` (claims were narrowed and the
narrowing is visible in the deliverable), `HOLD` (a decision-controlling conflict could not be resolved).
There is no silent pass-through: a check that surfaces nothing to fix still records `PASS`, not silence.

## 2. Current-verdict synthesis (single live verdict)

This section binds `references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` §1 (`EXECUTIVE_DECISION_LAYER`)
together with `references/modules/RESEARCH_REFRESH_AND_CHANGE_IMPACT.md` §9 (history-preserving revision) for the
one case neither fully covered alone: new material evidence arriving **within the same continuous engagement**
(not only across a separate refresh run).

- When material new evidence changes the `DIRECT ANSWER`, the comparison, the pricing/differentiation
  position, or the recommendation, the `EXECUTIVE_DECISION_LAYER` at the top of the deliverable is REWRITTEN
  in place to state the current verdict. It is not left in place with an inline note such as "this is
  partially stale, see section N for the current view" — that pattern makes a superseded conclusion the
  first, and for a skimming reader the only, thing read.
- The superseded verdict and the insights that depended on it move to a dated "Revision History /
  Superseded Conclusions" subsection in the body, each entry naming what changed it and pointing forward to
  the current verdict's section. This preserves the audit trail (`references/modules/...` §9's requirement to
  never edit historical wording in place) while keeping exactly one current verdict live at the top.
- Every dependent recommendation, pricing position, and differentiation claim is re-evaluated against the new
  evidence before the executive layer is finalized — a `RECONFIRMED`/`CHANGED`/`WEAKENED`/`STRENGTHENED`/
  `NOT_CURRENTLY_REVALIDATABLE` state per `references/modules/...` §7 for each, not just the single headline
  insight that prompted the update.
- This applies whether the new evidence arrived through an explicit user-triggered refresh or through new
  material shared mid-conversation in one continuous deliverable; the trigger differs, the currency
  requirement on the executive layer does not.

## 3. `SUBJECT_AND_SALE_MODE_LOCK`

Before finalizing a recommendation that depends on who the buyer is, what environment/runtime the product
runs in, or how it is sold, confirm each of the following from live or user-provided evidence in this
engagement — never from an earlier engagement's framing or from the model's own training-time assumption:

```yaml
current_product: ""            # what is actually being evaluated, as of this engagement
current_buyer: ""              # who actually buys/uses it, as stated or evidenced now
execution_environment: ""      # where/how it actually runs now (e.g. which host runtimes it is compatible
                                # with) — verified against this engagement's evidence, not carried forward
commercial_mode: ""            # how it is actually sold/distributed now
as_of: ""                      # the date/session this state was confirmed
confirmation_basis: LIVE_CHECK | USER_STATED | SKILL_DECLARED_SCOPE | UNKNOWN
```

Never assume access to developer-private state (unreleased roadmap, internal metrics, unannounced platform
support) on behalf of a normal buyer persona; if the current state of any field above cannot be confirmed,
it stays `UNKNOWN` rather than being asserted either way (including reused from a stale prior claim). An
`UNKNOWN` execution-environment or commercial-mode claim narrows the recommendation; it does not block
delivery of the rest of the report.

## 4. Combined exit check

Fail delivery when `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE` is unresolved (not `PASS`, `NARROWED`, or a
recorded `HOLD`), when the executive layer carries more than one live verdict for the same decision, or when
`SUBJECT_AND_SALE_MODE_LOCK` fields material to the recommendation were asserted rather than confirmed or
marked `UNKNOWN`.

Passing this module proves internal consistency and verdict currency only; it does not itself prove market
demand, WTP, or release readiness — those ceilings are unchanged and remain governed by the existing v1.9.0-
v1.9.2 gates and `references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` §3.
