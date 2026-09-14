# v1.6 — Demand vs Distribution Diagnostics

A funnel symptom is not a single-cause diagnosis.

## Diagnostic schema

```text
SYMPTOM
PLAUSIBLE_CAUSES[]
EVIDENCE_FOR_EACH_CAUSE
MEASUREMENT_HEALTH
CHEAPEST_DISCRIMINATING_TEST
CLAIMS_CURRENTLY_BLOCKED[]
NEXT_DECISION
```

If measurement is unreliable, diagnose instrumentation before product or market conclusions.
If the core value path is technically unreliable, load `PRODUCT_READINESS_AND_SIGNAL_INTEGRITY.md` before interpreting the funnel as demand evidence.

## States

### NO_IMPRESSIONS
Possible causes: indexing/delivery, tiny audience, bid/relevance, platform mismatch, no search volume, measurement failure.

Blocked claim: "there is no demand."

### IMPRESSIONS_NO_CLICKS
Possible causes: message, creative, placement, search-intent mismatch, trust, audience mismatch.

Blocked claim: "the product is bad."

### CLICKS_NO_SIGNUPS
Possible causes: landing mismatch, page failure, CTA friction, trust, wrong clicks, instrumentation.

Blocked claim: "the market is uninterested."

### SIGNUPS_NO_ACTIVATION
Possible causes: onboarding, promise-product mismatch, wrong audience, activation definition, product bug.

Blocked claim: "the acquisition channel is bad."

### ACTIVATION_NO_RETENTION
Possible causes: low repeat value, natural usage frequency, novelty, bugs, segment mismatch, reminder dependency.

Blocked claim: "more marketing will fix it."

### RETENTION_NO_PAYMENT
Possible causes: free tier solves enough, pricing/packaging, user-payer split, purchasing authority, payment friction, monetization model mismatch.

Blocked claim: "users never pay for this."

### PAYMENT_NO_RENEWAL
Possible causes: one-off use case, insufficient ongoing value, billing/support, acquisition mismatch, price/value mismatch.

Blocked claim: "lower CAC alone solves the business."

### ORGANIC_POST_NO_RESPONSE / COMMUNITY_NO_RESPONSE
Possible causes: low exposure, wrong community, low account trust, self-promo rules, message, relevance, timing.

Blocked claim: product demand failure.

### OUTREACH_NO_RESPONSE
Possible causes: deliverability, list quality, role mismatch, ICP mismatch, subject/message, offer, access friction.

Blocked claim: product value failure.

### CREATOR_OUTREACH_FAILURE
Possible causes: creator mismatch, weak mutual value, poor pitch/demo, trust, scale mismatch.

Blocked claim: creator channel is impossible.

### PAID_AD_POOR_RESPONSE
Possible causes: delivery/auction, audience, tracking, creative, offer, landing, optimization event, downstream product value.

Blocked claim: product failure until the funnel is decomposed.

### CORE_VALUE_FLOW_UNRELIABLE
Possible causes: crashes, blocked primary action, incomplete backend workflow, broken integration, unusable output, persistent error states.

Blocked claim: weak demand/value until users can receive the promised core outcome.

### PAYMENT_OR_BILLING_FAILURE
Possible causes: checkout, webhook, subscription-state, store billing, tax/region, entitlement or account-state failure.

Blocked claim: weak willingness to pay when the payment path itself is not shown to work.

### OUTPUT_QUALITY_FAILURE
Possible causes: hallucinated/incorrect AI output, unstable generation, bad source grounding, insufficient domain data, unacceptable task accuracy.

Blocked claim: underlying problem has no demand. The delivered solution may be failing the job.

### PERFORMANCE_OR_STABILITY_FAILURE
Possible causes: latency, timeout, concurrency, database/query, device/network, resource limits.

Blocked claim: market rejection when users abandon before value because the experience is unreliable.

### TRUST_PRIVACY_OR_SECURITY_BLOCK
Possible causes: permissions, data-handling concern, missing credibility, procurement/security requirement, visible privacy or auth weakness.

Blocked claim: no underlying job demand. Trust/delivery feasibility may still make the current product commercially weak.

## Cross-channel logic

If multiple channels fail at the same downstream stage, investigate shared downstream causes before declaring each channel bad.

Example:

- organic and paid both produce clicks but no activation → landing/onboarding/value mismatch becomes more plausible;
- no impressions across unrelated channels → measurement/access definitions may be wrong;
- one channel produces qualified activation while another produces only views → channel/audience fit differs; do not average them.

## One-step diagnostic rule

Choose the cheapest test that would most change the posterior ranking of plausible causes. Do not run broad multi-variable changes if one smaller discriminating test can isolate the bottleneck.
