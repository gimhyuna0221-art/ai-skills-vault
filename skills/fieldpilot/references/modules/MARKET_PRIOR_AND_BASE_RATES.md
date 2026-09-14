# v1.6 — Market Prior & Existing Market Intelligence

This module governs the question: **what can already be learned before asking the user to collect new primary evidence?**

## Activation

Use for early product/market questions such as:

- "이 앱/웹/게임이 먹힐까?"
- "비슷한 게 잘 됐나?"
- "이 시장은 돈이 되나?"
- "보통 어떤 가격/수익모델을 쓰나?"
- "사람들이 이런 제품을 어디서 발견하나?"
- "더 만들기 전에 시장부터 보고 싶다"

Do not force this module for a narrow research task whose required evidence is already known and not answered by market priors.

If the user asks **which kinds of products tend to work**, compares multiple ideas, or asks for success-pattern analysis, pair this module with `MARKET_FAVORED_PRODUCT_PATTERNS.md`. Builder-supply data (what makers create) must remain separate from customer-demand/outcome evidence.

## Default behavior

For this mode, do an **existing-evidence sufficiency sweep before recommending new interviews, surveys, ad spend, or user tests**, unless:

- the user explicitly asks to execute an already-methodologically-valid primary method; or
- current first-party product telemetry already answers the active proposition more directly; or
- the active proposition is inherently product-specific and cannot be answered by market evidence.

This is not a universal "desk research first" hierarchy. It is a product-mode rule to avoid making non-experts repeat what the market already knows.

## Market Cell

Construct the narrowest decision-useful cell:

```text
problem/job × target user/customer × buyer/payer if distinct × platform × geography
× price band × business model × product form × purchase complexity × alternatives
```

Prefer the user's actual target and product. If a field is unknown and materially changes the research, ask at most two tightly related questions. Otherwise proceed with explicit assumptions.

## Six prior axes

Keep these separate; do not collapse them into a single score.

1. **Demand Prior** — existing spending, search, usage, traffic, downloads, business activity, or explicit problem-seeking behavior.
2. **Supply / Competition Prior** — direct competitors, substitutes, concentration, entry rate, category maturity, technical imitability, and how quickly low-cost substitutes can enter.
3. **Monetization Prior** — observed pricing and business models; transaction/revenue distributions where legitimately available.
4. **Distribution Prior** — where comparable products are discovered/acquired: search, store browse, creators, social, communities, sales, paid, referrals, platform recommendation.
5. **Historical Outcome Prior** — comparable launch cohorts, success/low-performance/closure where observable; right-censoring and missing failures preserved.
6. **Evidence Quality** — direct vs estimated, population/frame, geography, time, denominator, selection/survivorship risk, applicability.

## Claim ceilings

Do not conflate:

```text
MARKET_EXISTS
CATEGORY_ATTRACTIVE
SIMILAR_PRODUCT_SUCCESS_OBSERVED
THIS_PRODUCT_SUCCESS_LIKELIHOOD
THIS_PRODUCT_DEMONSTRATED_DEMAND
```

Market and competitor evidence may often support the first three. It normally cannot establish the last one without this product's own evidence.

## Success terminology and currentness guard

Do not compress heterogeneous signals into the word `success`. Keep at least these separate:

```text
MARKET_EXISTENCE
ADOPTION_OR_USAGE_OBSERVED
REVENUE_OBSERVED
PROFITABILITY_OBSERVED
RETENTION_OR_REPEAT_USE_OBSERVED
GROWTH_OBSERVED
FUNDING_OBSERVED
COMMERCIAL_SUSTAINABILITY_UNKNOWN_OR_OBSERVED
```

Rules:

- funding is a financing event, not demand, PMF, profitability, or commercial success;
- downloads/members/traffic support adoption or reach, not profitability or retention;
- one or a few successful-looking competitors do not justify `the category is validated` or `this type works`; default to precise language such as `market exists` or `similar-product adoption has been observed`;
- if `success` is used, define the outcome metric and period (for example revenue growth, profitability, retained users, or durable paid adoption);
- preserve negative/current signals. A historical growth claim must not be presented as current performance without current corroboration;
- a company's own explanation of why it grew is `company/founder attribution`, useful for mechanism hypotheses but not causal proof;
- when a positive historical case coexists with later weak revenue/profitability/retention or other contrary evidence, surface both rather than narrating a winner story.

For material user-facing market facts or competitor numbers, provide source/date or equivalent provenance when the runtime supports citation. If the source is old, say so explicitly.

## Comparison set

Build a comparison set from:

- direct competitors;
- indirect substitutes;
- manual/workaround alternatives;
- incumbent/general-purpose tools;
- "do nothing" where relevant;
- adjacent analogs only when transfer assumptions are explicit.

Do not select only famous winners. Where feasible, recover low-performing, discontinued, or inactive products. Do not equate delisting with commercial failure unless evidence supports that reason.

## Market statistic contract

Every material statistic or benchmark should preserve:

```text
publisher
source_type
publication_date
retrieval_date
measurement_period
population
sampling_frame
inclusion_criteria
exclusion_criteria
platform
geography
category
metric
numerator
denominator
unit
direct_or_estimated
aggregation
survivorship_risk
selection_risk
censoring
applicability
claim_ceiling
```

Rules:

- No defensible denominator → no invented rate.
- Prefer distributions/percentiles/concentration over a single mean for heavy-tailed digital outcomes.
- Do not mix metrics with different definitions.
- Do not mix geographies/platforms/categories without a transfer rationale.
- Third-party estimates remain `ESTIMATED` and should be sensitivity-tested if decision-critical.

## Current-fact acquisition guard

For named competitors or claims that can change over time (current price, downloads,
funding, revenue, profitability, retention, service status, regulatory status, platform
mechanics), do not rely on model memory when live search/current sources are available.
Verify the material fact and preserve source date/retrieval date. If live verification is
unavailable, label the fact `UNVERIFIED_CURRENT` or `HISTORICAL` as appropriate and keep
the claim ceiling below a current market conclusion. Do not fabricate a present-tense
competitor fact to complete a Market Prior packet.

## Source preference

Prefer question-relative evidence, roughly:

1. first-party user/account telemetry for the user's own product;
2. current primary platform documentation and official benchmark systems;
3. government/public official data and corporate filings;
4. peer-reviewed / high-quality research;
5. transparent large-scale vendor datasets with inclusion criteria;
6. public competitor observations;
7. third-party estimates/proxies;
8. anecdote/community material for hypothesis generation.

Do not mechanically choose government sources when they are not the right evidence for the claim.

## Existing evidence decision

After the sweep, output:

```text
MARKET_PRIOR_PACKET
- market_cell
- comparison_set
- demand_prior
- competition_prior
- monetization_prior
- distribution_prior
- historical_outcome_prior
- failure_coverage
- evidence_quality
- claim_ceiling
- residual_unknowns
- primary_validation_required = YES / NO / PARTIAL
```

Primary validation is recommended only when an unresolved question is:

1. decision-relevant;
2. not adequately resolved by existing evidence;
3. likely to gain materially stronger evidence from new collection.

## Forbidden shortcuts

- TAM/SAM/SOM → product demand.
- category growth → this feature works.
- competitors exist → sufficient demand.
- few competitors → blue ocean.
- winner examples → category success rate.
- third-party estimated visits → users/customers.
- Google Trends 100 → 100 searches.
- store removal → commercial failure.
- benchmark median → this product's expected outcome.
