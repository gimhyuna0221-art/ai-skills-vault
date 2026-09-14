# v1.6 — Monetization & Unit-Economics Routing

## Governing rule

There is no universal winner among ads, subscription, one-time purchase, freemium, credits, or usage-based pricing.

A monetization recommendation is a **model-fit hypothesis** constrained by:

```text
recurring_value
usage_frequency
payer_vs_user
marginal_cost_per_use
API_or_infrastructure_cost
ad_inventory_and_session_depth
price_sensitivity_and_switching_cost
retention_and_renewal
purchase_complexity
platform_and_geography
competitive_model_distribution
founder_runway
```

Comparable-product patterns create a `MONETIZATION_PRIOR`; they do not prove this product will monetize the same way.

## Local paid-substitute anchor

When the decision asks whether or what to charge, inspect a bounded set of current, locally relevant
paid direct substitutes and paid indirect alternatives when they are available at zero extra cost.
Record observed price, billing unit, geography/currency, offer scope, access time, and source key.
This is a decision anchor, not proof of willingness to pay. Any recommended test price or range remains
an explicitly experimental bracket with rationale; do not copy a competitor price, invent a local
equivalent, or expand into an exhaustive reference hunt. If no retrievable paid anchor is available,
state that limitation and narrow the pricing recommendation.

## Evidence hierarchy for monetization

Keep these lanes separate:

1. **Comparable model observed** — competitors use ads/subscriptions/etc.
2. **Stated preference / WTP** — people say what they would pay or prefer.
3. **Behavioral pricing evidence** — clicks to paid plan, checkout initiation, plan selection.
4. **Actual payment** — money was paid under known terms.
5. **Repeat economics** — renewal, repeat purchase, refunds, churn, support and marginal cost.

Do not convert an upper lane into the next one without evidence.

## Routing questions

### Ads / ad-supported
Plausible when repeated sessions or meaningful inventory exist and the expected ad yield can plausibly cover product and acquisition costs in the relevant geography/format.

Must inspect:
- session frequency and duration;
- ad placement constraints and user-experience cost;
- geography/device mix;
- actual or defensible ad-yield estimates;
- effect of ads on activation/retention where measurable.

Must not infer: `free users exist -> ads are viable`.

### Subscription
Plausible when value recurs over time and users/payers have a reason to keep access active.

Must inspect:
- recurring job/value frequency;
- retention before or alongside payment;
- payer identity and budget;
- cancellation/renewal behavior;
- marginal cost of service.

Must not infer: `competitors subscribe -> this product should subscribe` or `AI API cost -> subscription is automatically right`.

### One-time purchase
Plausible when value is concentrated, ownership has enduring utility, and ongoing service cost is limited or separately covered.

Must inspect:
- expected support/hosting/update burden after purchase;
- upgrade/maintenance expectations;
- platform fee/tax context when material.

### Freemium
Plausible when free use materially helps acquisition, trial, sharing, or habit formation without making paid value unnecessary or creating unsustainable marginal cost.

Must inspect:
- what free users actually do;
- whether free tier substitutes for the paid job;
- free-to-paid behavior under real offers;
- marginal cost and abuse risk.

### Credits / usage-based
Plausible when cost and customer value scale with usage or workloads vary materially.

Must inspect:
- cost per unit vs perceived value per unit;
- predictability/transparency for users;
- low-usage vs heavy-usage economics;
- purchase friction and replenishment behavior.

## Required user-facing monetization output

When the user asks `광고 vs 구독 vs 유료 vs 무료` or similar, do not answer with personal preference or a generic market slogan.

Return:

```text
COMPARABLE_MODEL_PRIOR
WHY_THOSE_MODELS_APPEAR_IN_THIS_CATEGORY
THIS_PRODUCT_COST_STRUCTURE
RECURRING_VALUE_AND_USAGE_FREQUENCY
PAYER_AND_PAYMENT_FRICTION
CURRENT_EVIDENCE
LOCAL_PAID_DIRECT_AND_INDIRECT_SUBSTITUTE_ANCHORS
RECOMMENDED_MODEL_TO_TEST_FIRST
WHY_THIS_MODEL_FIRST
EXACT_TEST_OR_ARTIFACT
WHAT_TO_MEASURE
WHAT_POSITIVE_RESULT_SUPPORTS
WHAT_NEGATIVE_RESULT_DOES_NOT_PROVE
FALLBACK_MODEL_OR_NEXT_TEST
```

If product facts are insufficient, ask only the minimum questions that materially change routing (for example usage frequency, marginal/API cost, who pays, and whether the job recurs).

## Unit-economics guard

Do not use a universal LTV:CAC multiple, payback period, retention cutoff, ad RPM, or conversion threshold.

If a numeric boundary is recommended it must be:
- derived from the user's actual costs/revenue/test design; or
- source-backed and scoped to a current platform/category context;
- accompanied by uncertainty and what would change the recommendation.

## Common failure modes

- choosing ads because the user fears charging;
- choosing subscription because recurring revenue sounds attractive;
- choosing free because acquisition is currently hard;
- pricing below competitors without testing whether price is the real switching barrier;
- ignoring marginal AI/API cost;
- treating one payment as durable monetization;
- scaling acquisition before renewal/retention or contribution economics are interpretable.
