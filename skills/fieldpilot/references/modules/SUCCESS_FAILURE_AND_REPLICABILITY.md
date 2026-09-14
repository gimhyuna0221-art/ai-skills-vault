# v1.6 — Success/Failure Explanation, Replicability & Founder Feasibility

This module answers two different questions:

1. **Why might comparable products have succeeded or failed?**
2. **Can this user realistically reproduce the useful parts?**

## Success/failure explanation contract

Treat each alleged success factor as a claim, not as a story.

Required fields:

```text
OBSERVED_FACT
DOCUMENTED_TACTIC
TEMPORAL_ASSOCIATION
EVIDENCE_FOR_ASSOCIATION
EVIDENCE_FOR_CAUSALITY
MECHANISM_PLAUSIBILITY
COMPARISON_EVIDENCE
ALTERNATIVE_EXPLANATIONS
UNOBSERVED_CONFOUNDING
CAUSAL_CONFIDENCE = HIGH / MEDIUM / LOW / UNKNOWN
WHAT_CANNOT_BE_CONCLUDED
PROVENANCE_CLASS
```

### Evidence interpretation

- Randomized experiments can support causal claims within their tested conditions; external validity remains separate.
- Natural/quasi experiments can support causal inference when identification assumptions are explicit and credible.
- Channel attribution + time series can support contribution hypotheses, not automatic causal certainty.
- Founder interviews are strong evidence of **what founders report doing**, weak evidence that the action caused success.
- Ad libraries document creative/tactic existence; they do not show profitability or causal contribution.
- Post-hoc success stories are hypothesis generators.
- "Successful company used X" is not causal evidence.

### Case selection, comparators and the user-case gap

This module explains **why** cases may have succeeded or failed and whether the user can reproduce
the useful parts. It does not by itself govern how success is defined, how cases become eligible,
how the negative-case search is recorded, or how the user's own gaps are classified and prioritized.

Those are governed by `references/modules/MARKET_CASE_COMPARISON_AND_GAP.md`, which sits around this
module and feeds it: the success definition and case register are frozen there before selection,
the comparator set and its search record are built there, and each candidate mechanism identified
here is taken back there for the discrimination check against comparators. The causal fields,
endowment-versus-tactic separation and Replicability Engine below remain controlling and unchanged.

In v1.7.4, **every material candidate success factor** returns through that module's
`EXPLICIT_TWO_SIDED_FACTOR_TEST` before it may be called a mechanism or feed the user-case diagnosis. Both named
outcome sides retain `PRESENT / ABSENT / UNKNOWN / NOT_COMPARABLE` evidence states; silence never becomes absence.
The comparison separates `SHARED_NON_DISCRIMINATING`, `PLAUSIBLY_DISCRIMINATING`, and
`UNKNOWN_UNTESTABLE`, and compares alternative explanations across the outcomes. One close confirmed negative
comparator is sufficient for a bounded test with a disclosed ceiling. An unconfirmed negative remains excluded or
search-gap evidence and is never promoted merely to satisfy the table.

### Matched comparison rule

When feasible, compare similar products across:

- product type/category;
- launch period;
- platform;
- geography;
- price/business model;
- team/funding scale;
- starting audience;
- target segment.

Include low-performing or discontinued cases where observable. If the low-performing group is poorly observed, label the comparison weak rather than pretending balance.

## Endowment vs tactic

Separate non-replicable or partly replicable endowments from tactics:

```text
existing_audience
brand
capital
team_size
proprietary_data
network_effects
installed_base
platform_privilege
partnerships
creator_relationships
regulatory_access
IP/licensing
first_mover_timing
luck/exogenous_exposure
```

A tactic can be documented even when its causal contribution is unknown.

## Replicability Engine

For each candidate success factor:

```text
SUCCESS_FACTOR
EVIDENCE
MECHANISM
REQUIRED_RESOURCES
USER_HAS_RESOURCES = YES / NO / PARTIAL / UNKNOWN
ENTRY_BARRIER
DEPENDENCY_ON_EXISTING_AUDIENCE
DEPENDENCY_ON_CAPITAL
DEPENDENCY_ON_TEAM_OR_SKILL
DEPENDENCY_ON_PLATFORM
DEPENDENCY_ON_NETWORK_EFFECTS
TIME_TO_REPRODUCE
OPERATIONAL_BURDEN
REPLICABILITY = HIGH / MEDIUM / LOW / UNKNOWN
CHEAPER_SUBSTITUTE
CHEAPEST_TEST
WHAT_WOULD_FALSIFY_REPLICABILITY
```

Unknown user resources remain `UNKNOWN`. Do not infer that a solo builder has video, sales, SEO, community, or ad skills.

## Founder Feasibility Profile

Collect only fields that could materially change the route:

```text
budget
weekly_time
runway
team
technical_capability
sales_capability
content_capability
existing_audience
brand/trust
partnership_access
analytics_instrumentation
customer_support_capacity
regulatory_constraints
proprietary_assets
paid_data_access
```

Ask the user only when a missing field would change the recommended next step and cannot be reasonably inferred.

## Entry barrier classes

At minimum consider:

- acquisition capital / CAC exposure;
- content production burden;
- direct-sales burden;
- trust/reputation requirements;
- data access;
- network effects / marketplace liquidity;
- platform dependency;
- regulation/compliance;
- licensing/IP;
- support/operations;
- switching costs/incumbency;
- technical imitability / feature commoditization and how quickly substitutes can be reproduced;
- non-code value such as reliability, workflow integration, data, distribution, trust, service/support, brand, compliance, or network effects;
- time-to-accumulate assets such as SEO authority or community.

## Output language

Do not say:

> "This company succeeded because of TikTok, so copy TikTok."

Prefer:

> "TikTok activity and growth moved together, but the available evidence does not isolate TikTok as the cause. The founder also had an existing audience. The replicable part for your current situation is the short product-demo format, not the audience advantage. The cheapest way to test that mechanism is ..."

## Forbidden shortcuts

- success story → success law;
- VC funding → product demand;
- large founder audience → channel strategy reproducible by an audience-zero user;
- traffic spike → sustainable retention;
- correlation → causal certainty;
- one winner's tactic → universal channel recommendation;
- low software build barrier → zero willingness to pay or zero commercial value.
