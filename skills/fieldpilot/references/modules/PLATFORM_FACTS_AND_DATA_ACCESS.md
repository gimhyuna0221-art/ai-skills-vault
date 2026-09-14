# v1.6 — Platform Facts, Numeric Thresholds & Data Access

## Purpose

Current platform mechanics and third-party market data are volatile. This module prevents old blog advice or decontextualized numbers from becoming FieldPilot hard rules.

## Provenance classes

Every operational claim should be one of:

```text
RESEARCH_BACKED
CURRENT_PLATFORM_FACT
PROFESSIONAL_GUIDANCE
CONTEXT_DERIVED
FIELDPILOT_HEURISTIC
UNSUPPORTED
OUTDATED
```

## Numeric threshold record

For every material numeric threshold:

```text
platform_or_domain
exact_doc_title
publisher
url
last_updated_if_available
retrieval_date
exact_context
metric
numerator
denominator
number_or_range
role = PLATFORM_SETTING / REPORTING_MINIMUM / LEARNING_GUIDANCE /
       ELIGIBILITY_REQUIREMENT / BUSINESS_DECISION_THRESHOLD
required_or_recommended
what_changes_it
what_source_does_not_say
generalization_allowed
```

A current platform recommendation does not become a business success threshold.

## Freshness rule

Market-wide freshness policy, trend validation and timing are governed by
`references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md`, which scopes the freshness requirement to
market velocity, source type **and** the decision horizon already frozen in the
`CLIENT_DECISION_BRIEF`, and which adds durable capture for undated decision-relevant pages. That
module is additive: the provenance classes, numeric-threshold record, data-access classes,
fallback contract and source-conflict rules in this module remain controlling.

For volatile ad/store mechanics that materially affect the user's setup:

1. prefer current primary platform documentation at execution time;
2. record retrieval date and exact scope;
3. if the primary source cannot be verified, do not present a cached number as current fact;
4. downgrade to professional guidance/heuristic or state uncertainty;
5. do not block a broader market-research answer unless the unverified fact is essential to it.

## Current examples preserved only as scoped examples

The following are examples of how to store facts, not permanent universal runtime rules:

- TikTok auction troubleshooting has official guidance to give underperforming auction ads a full 7 days to reach 50 conversions. This is `LEARNING_GUIDANCE`, not a general product-demand threshold.
- TikTok Search Ads has its own calibration guidance, different from generic auction/app guidance.
- Google Smart Bidding learning duration varies with conversion volume, conversion cycle, and bid strategy; published learning windows are guidance, not a universal "do not touch for N days" business rule.
- Apple App Store peer benchmarks define their own conversion and retention metrics and comparison groups; benchmark numbers are contextual, not automatic pass/fail thresholds.
- Google Play peer groups similarly contextualize first-party app metrics and do not reveal competitor private ground truth.
- Steam's official visibility documentation states that store-page traffic and conversion rate are not direct visibility factors and that wishlists have limited/conditional visibility roles; generic e-commerce funnel assumptions must not overwrite platform-specific rules.

## Data access classes

```text
FREE_PUBLIC
FREE_ACCOUNT_REQUIRED
USER_ACCOUNT_DATA
LIMITED_FREE
PAID
ENTERPRISE_ONLY
ESTIMATED
NOT_PUBLIC
```

Store both `access_class` and `direct_or_estimated`.

## Fallback contract

When ideal data is inaccessible:

```text
PRIMARY_SOURCE_NEEDED
ACCESS_STATUS
FALLBACK_SOURCE
WHAT_FALLBACK_CAN_ANSWER
WHAT_IT_CANNOT_ANSWER
ESTIMATION_RISK
EXPECTED_EVIDENCE_LOSS
DECISION_STILL_POSSIBLE = YES / NO / PARTIAL
```

Do not pretend a proxy is equivalent to the missing source.

## Typical source classes

- App Store public pages: public metadata/reviews; competitor exact downloads/revenue not public.
- App Store Connect: user's own acquisition/engagement/monetization/benchmarks.
- Google Play public pages: public listing/reviews; competitor private metrics unavailable.
- Play Console: user's own metrics and peer-group contextual comparisons.
- Steam public/Steamworks: public store/chart information and user's own game data; exact competitor unit sales mostly not public.
- Google Trends: relative normalized search interest; not absolute search counts.
- Keyword Planner: account-dependent keyword planning/forecasting; scope and metric definitions matter.
- Similarweb/Sensor Tower/Appfigures/VG Insights: useful competitor intelligence or estimates depending on product/plan; estimates are not ground truth.
- RevenueCat/ChartMogul/AppsFlyer: strong first-party/customer-dataset evidence for specific included populations; not universal population base rates.
- DART/KOSIS/KOCCA and analogous official sources: strong for public/company/industry context, not automatically product-level demand.
- NAVER DataLab: Korean NAVER integrated-search trend signal; trend values are relative/normalized context rather than a customer-count or purchase-demand measure.
- NAVER Ads Keyword Tool: monthly search volume, click/CTR and competition context for keywords; useful for Korean search-intent priors but not evidence that searchers will use or pay for the user's product.

## Source conflict

When first-party official/user data conflicts with a third-party estimate:

1. reconcile definitions, geography, period, units, gross/net, visit/user distinctions;
2. prefer direct first-party evidence for the user's own product;
3. preserve third-party estimates as estimates;
4. if the discrepancy remains decision-relevant, run sensitivity analysis rather than averaging into a fake precise number.
