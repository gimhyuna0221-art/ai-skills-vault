# Bounded Best-of-AI Distillation — v1.9.2

This module adds exactly four generalizable behavior deltas. It does not encode any benchmark answer,
named benchmark competitor, required price, fixed sample size, or universal research sequence. All v1.9.1
factuality, provenance, uncertainty, negative-evidence, regulatory, ethics, and decision-checkpoint controls
remain governing.

## 1. `LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE`

Activate when the user asks whether a product can charge, what to charge, whether a proposed price is
plausible, or how to divide free and paid value.

Use the smallest decision-sufficient set of relevant **local paid direct and indirect substitutes** that can
be verified through permitted sources. For every anchor preserve geography, currency, amount or range,
billing cadence, taxes/fees, plan/package, eligibility or limits, access time, source role, and locator. Then
position the user's proposed price against those observed packages and state what additional value, scope,
or proof would be needed to justify the comparison.

An observed competitor price is a `COMPARABLE_MODEL_PRIOR`, never evidence that this product has the same
WTP. This holds in both directions: it is not evidence to justify a *proposed* price for this product, and
it is equally not evidence that the *competitor's own* charged price has been proven to convert, retain, or
work — a listed/charged price only proves the price point exists in the market (v1.9.3,
`references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md` §1 `wtp_overclaim_check`). A proposed price bracket is
allowed only as `EXPERIMENT_DESIGN`; show how the anchors and the user's economics informed it, and label it
as unmeasured. Do not transfer foreign storefront prices into a local recommendation without an auditable
currency/tax/cadence comparison. If suitable local anchors are not available, record the bounded search and
leave the price footing `UNKNOWN` instead of inventing one.

For v1.9.3, also record each anchor's `commercial_mode` (e.g. subscription, pay-per-run/hosted execution,
one-time download) alongside this product's actual `commercial_mode`. When they differ materially, record
`SALE_MODE_MISMATCH` and narrow the comparison to what actually transfers (typically price magnitude as a
loose prior) rather than treating the anchor as a like-for-like pricing model.

Exit states:

- `ANCHORED`: verified scoped anchors and a client-visible comparison are present.
- `ANCHORS_UNAVAILABLE`: the bounded route and evidence loss are disclosed; no price is fabricated.
- `NOT_APPLICABLE`: the decision does not concern price, paid value, or monetization.

## 2. `RETRACEABLE_LOCATOR_FALLBACK_GATE`

For a material source, record both whether the locator was observed and whether the cited content was
retrievable during the run.

```yaml
retrieval_status: CONTENT_RETRIEVED | PARTIAL_RENDER | BLANK_OR_SCRIPT_SHELL | ACCESS_BLOCKED | NOT_ATTEMPTED
retrieval_failure_mode:
alternate_locator:
alternate_locator_origin: OBSERVED_IN_RETRIEVAL | USER_SUPPLIED | OFFICIAL_METADATA | NOT_AVAILABLE
alternate_retrieval_status:
alternate_route_limit:
```

When a provided primary locator does not expose the cited content, preserve it and the observed failure.
If a lawful alternate route or stable identifier was actually observed and exposes the same bounded evidence,
render that alternate with its own role and ceiling. If no alternate is available, say so, keep the truthful
limitation client-visible, and narrow the claim. Never guess a URL, reconstruct a slug, bypass access control,
or imply that an untested locator renders.

`PROVENANCE_OUTPUT_GATE` fails a material claim with `MATERIAL_LOCATOR_NOT_RETRACEABLE` when its provided
locator is recorded as failed and the record has neither (a) an observed retrievable alternate nor (b) an
explicit no-alternate limitation plus a claim ceiling narrowed to what the client can verify.

## 3. `VALIDATION_RESOLUTION_GATE`

Activate when a client-facing recommendation proposes primary research, a pilot, a behavioral test, a pricing
test, or an operational validation whose result is meant to change a decision.

Before calling the plan executable or `READY`, resolve:

```yaml
validation_plan:
  decision_and_proposition:
  observation_unit_and_nested_structure:
  eligible_population_or_case_universe:
  planned_count_or_range:
  count_rationale:
  duration_or_opportunity_window:
  duration_rationale:
  metrics: []
  price_test_brackets: []
  price_bracket_state: NOT_APPLICABLE | EXPERIMENT_DESIGN
  bracket_derivation:
  decision_rules:
  ethics_privacy_consent_controls:
  unresolved_dependencies: []
  dependency_resolution_rule_or_owner:
  readiness: READY | PROPOSED_NOT_READY | SKIPPED_BY_USER
```

Every number must follow the existing numeric guard. Counts and duration derive from the chosen method,
decision precision or qualitative aim, expected variation, recurrence/opportunity window, clustering,
attrition, feasibility, and safety—not from a universal magic number. If count or duration cannot yet be
defended, expose the dependency and the concrete rule or owner that will resolve it; the plan remains
`PROPOSED_NOT_READY`. Pricing brackets remain experiments, not measured WTP. This gate does not select a
method for the user, authorize recruitment, or override SKIP.

## 4. `LITERATURE_HIERARCHY_COMPLETENESS_GATE`

Activate when one or more individual studies are used to characterize the direction, consistency, magnitude,
or uncertainty of a broader evidence base and that characterization materially affects the decision.

Before closing the claim, run a bounded check for an eligible systematic review or meta-analysis. When found,
represent the pooled synthesis and decision-relevant individual positive, null, negative, or contradictory
studies together. Preserve population, setting, intervention/exposure, comparator, outcome, study window,
heterogeneity, publication/search limits, and transferability ceiling. Do not double-count a review and its
included studies as independent corroboration.

If no eligible higher-tier synthesis is found within the bounded search, record `SYNTHESIS_SEARCHED_NOT_FOUND`,
the exact search boundary, and keep the claim study-specific. A pooled effect from another domain never becomes
the user's domain effect size. Stop once the material characterization is supported or bounded; this gate does
not authorize a broad literature hunt.

## 5. Combined exit check

The four gates are independent user-visible behaviors and are the complete v1.9.2 delta set. Existing matrix,
plain-language, claim-state, negative-evidence, regulatory, ethics, STOP/MODIFY/CONTINUE, and source-key rules
remain regression obligations rather than new deltas.

Fail delivery when any applicable gate is unresolved. Passing this module proves structural compliance only;
it does not prove market demand, WTP, research effectiveness, generalization, or release readiness.
