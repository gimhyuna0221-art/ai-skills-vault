# v1.6 — Market-Favored Product Patterns

This module governs questions such as:

- "요즘 사람들이 실제로 어떤 앱/서비스를 많이 만들고, 어떤 유형이 잘 되나?"
- "시장에 잘 먹히는 제품 유형이 따로 있어?"
- "비슷한 성공사례를 보고 내가 뭘 만들지 판단하고 싶어"
- "B2B/생산성/AI 앱/게임 중 구조적으로 어느 쪽이 유리해?"

The purpose is to recover a **relative market prior**, not to manufacture a startup-success formula.

## Core invariant — MARKET-FAVORED PATTERN IS A PRIOR, NOT A LAW

`시장 선호 패턴` means that a product structure has repeatedly shown more favorable demand,
monetization, retention, distribution, or ROI conditions in applicable evidence. It does **not** mean:

- every product of that category succeeds;
- a category label is itself causal;
- a favorable prior substitutes for this product's own evidence;
- a pattern can be converted into a fake success probability;
- one famous success story establishes the pattern.

Prefer statements such as:

> "현재 비교 근거에서는 A가 B보다 구조적으로 유리한 출발점입니다. 이유는 기존 지출,
> 반복 워크플로, 접근 가능한 고객, 측정 가능한 ROI가 더 명확하기 때문입니다. 다만 이 제품의
> 실제 수요는 아직 별도 검증이 필요합니다."

## What builders are actually making — descriptive prior only

Recent large-platform evidence can describe builder supply, not market success.
For example, Lovable's 2026 Build Economy report covers platform activity from January 2025–May 2026
and a May 2026 survey of 14,300+ users. Within that platform, projects were concentrated in websites,
business operations, consumer apps, dashboards/analytics, e-commerce, and productivity/utility tools;
AI/chatbots were a smaller share than the broad "everyone is building an AI chatbot" narrative might imply.

Use this only as:

```text
BUILDER_SUPPLY_PATTERN
```

Never infer `customer demand`, `profitability`, or `success rate` from what builders choose to create.
The platform population is selected and not representative of all software builders.

## Favorability vector — keep dimensions separate

For a product idea, assess the following dimensions independently. Use
`STRONG / MODERATE / WEAK / CONTRADICTORY / UNKNOWN` plus evidence/confidence. Do not sum them into a
single "market score" unless a validated predictive model exists for the exact population and outcome.

```text
JOB_PAIN_OR_VALUE
REPEAT_TRIGGER
EXISTING_SPEND_OR_WORKAROUND
MEASURABLE_ECONOMIC_VALUE
TIME_TO_VALUE
TARGET_REACHABILITY
DISTRIBUTION_DENSITY
MONETIZATION_FIT
FOUNDER_DOMAIN_ACCESS
NON_CODE_COMPOUNDING_ASSET
TRUST_OR_REGULATORY_BURDEN
COLD_START_DEPENDENCY
COMMODITIZATION_PRESSURE
RETENTION_NATURALNESS
DELIVERY_COMPLEXITY_AND_READINESS_BURDEN
```

### Interpretation

More favorable starting structures often combine several of these:

1. **Existing recurring workflow or spend.** A real task already consumes time, labor, software spend,
   or operational attention.
2. **Measurable economic or practical pain.** The user can understand what is saved, avoided, accelerated,
   or made possible.
3. **Repeated trigger.** The job naturally recurs often enough to create retention or recurring value.
4. **Fast time-to-value.** A user can experience the core value quickly rather than waiting for a vague future payoff.
5. **Reachable, concentrated target.** The maker knows where the relevant users/buyers can actually be reached.
6. **Domain proximity.** The founder has real workflow knowledge, customer access, trust, or problem context.
7. **Non-code compounding assets.** Data, integrations, workflow embedding, customer relationships, trust,
   operations, community, distribution, or switching costs can accumulate after launch.
8. **Monetization aligned with usage.** Subscription, transaction, usage, lifetime, ads, or enterprise pricing
   matches how often value recurs and who pays.
9. **Low initial cold-start burden.** The product can create value for an early user without first requiring a
   large two-sided network or broad social graph.
10. **Deliverability at the founder's current capability.** The promised value can be delivered reliably enough for the intended test without hidden payment, security, integration, performance, or regulated-data burden dominating the result.

These are **mechanism priors**, not universal rules.

## Recurrently fragile starting structures

Treat these as reasons to demand stronger evidence, not automatic rejection:

- a generic AI wrapper with no narrow job, proprietary context, distribution edge, workflow embedding, or trust advantage;
- a one-off utility forced into a recurring subscription model without recurring value;
- a new social/community/marketplace that needs liquidity or network density before the first user receives value;
- an idea whose acquisition depends almost entirely on virality, celebrity amplification, store featuring, or another
  exogenous event the founder cannot reproduce;
- a builder-first product where the maker has no credible access to the actual target customer;
- a high-trust or regulated product whose delivery capability, privacy/security, or domain credibility is below the buyer's
  requirements;
- a crowded generic habit/note/productivity clone whose only advantage is implementation speed;
- an AI product with high inference/support cost and weak evidence of repeat usage or payer economics;
- a product whose core value depends on production-grade auth, payments, sensitive data, real-time reliability, or complex integrations that the current founder cannot yet deliver or verify, when those failures would contaminate the market test.

## Category priors — conditional, never categorical winners

### B2B / vertical workflow software

Current evidence often makes this a strong candidate when the product replaces a painful repeated workflow or existing
software/labor spend and the ICP is reachable. RevenueCat's 2026 subscription-app dataset reports Business as a category
with comparatively strong monetization/retention, while Menlo Ventures' 2025 enterprise study reports substantial spending
in role-specific and industry-specific AI applications where productivity gains are immediate and measurable.

Do not convert this into `B2B always wins`. Long sales cycles, procurement, integration, security, buyer/user separation,
and weak founder access can reverse the prior.

### Productivity / utility

Demand is clearly present, but supply is heavy and generic utilities are easy to copy. RevenueCat's 2026 data shows strong
AI concentration in Productivity and also category-specific price/retention pressure. Favor narrow repeated jobs and
workflow integration over generic "AI productivity" positioning.

### AI-native consumer utilities

AI can strengthen initial monetization, but current subscription data shows weaker long-term retention and higher refund
rates for AI-powered apps than non-AI apps in the RevenueCat sample. A novelty spike is therefore not enough; repeated task
value, cost economics, and retention deserve early scrutiny.

### Education / study

Can be favorable when tied to a recurring course/exam workflow and a dense reachable audience. Named cases such as Klar
suggest a plausible mechanism of founder problem proximity + course-specific utility + concentrated campus distribution,
but vendor-published ARR/usage claims remain case evidence, not category success rates.

### Health / fitness / safety

High-value pain and strong annual-plan behavior can be favorable, but trust, medical/safety claims, privacy, and regulation
can dominate. A high-stakes problem increases value **and** evidence burden.

### Creator / marketing tools

Can be attractive when output is directly demonstrable and tied to a repeated production workflow. Generic content generation
is highly substitutable; vertical brand workflows, proprietary inputs, distribution access, or measurable production savings
raise the prior.

### Games / interactive content

Instantly legible, visual, shareable experiences may acquire users efficiently, but outcome variance and hit dependence are
high. Famous viral launches are especially prone to survivorship and non-replicable-audience effects. Evaluate player behavior,
retention, monetization, and the founder's actual distribution assets separately.

### Marketplace / community / social

The value can be large after liquidity/network density exists, but cold-start risk is structurally higher. Prefer designs that
can deliver single-player/single-side value or have a credible wedge into a concentrated existing network.

## Success-case mechanism fixtures

Named cases are **mechanism examples**. They are not proof that copying the category or tactic will work.
Where numbers come from the platform/vendor that enabled the build, preserve the `VENDOR_CASE_STUDY` limitation and seek
independent corroboration when the decision depends on the exact figure.

### eXp Realty / AppDirect / Atonom — replace known spend or workflow friction

Observed vendor case studies describe custom software replacing expensive SaaS, spreadsheets, or workflows with measurable
cost/labor savings. Candidate mechanism:

```text
KNOWN_EXISTING_COST
+ PRECISE_INTERNAL_WORKFLOW
+ IMMEDIATE USER ACCESS
+ MEASURABLE ROI
```

Transfer limit: an internal tool's value inside a company does not prove an external SaaS market exists.

### Lumoo — domain expertise + vertical workflow integration

Vendor case evidence reports fashion/retail founders turning years of domain experience into an integrated content workflow
and reaching paying brands. Candidate mechanism:

```text
DOMAIN_PROXIMITY
+ EXPENSIVE EXISTING PRODUCTION WORKFLOW
+ ENTERPRISE INTEGRATION
+ MULTI-STEP REPEATED VALUE
```

Transfer limit: founder network, enterprise sales ability, vendor-reported ARR, and integration capability may be non-replicable.

### Klar — repeated exam workflow + concentrated campus distribution

Vendor/founder-published evidence reports rapid student adoption and ARR. Candidate mechanism:

```text
FOUNDER_SELF_PROBLEM
+ RECURRING EXAM/STUDY JOB
+ COURSE-SPECIFIC CONTEXT
+ DENSE CAMPUS DISTRIBUTION
```

Transfer limit: short observation period, platform/vendor publication, viral campus effects, and institutional relationships.

### Plinq — high-stakes consumer pain + inaccessible information made accessible

Vendor case evidence reports rapid early usage and revenue for consumer background checks focused on women's safety.
Candidate mechanism:

```text
HIGH_STAKES_PAIN
+ CLEAR VALUE MOMENT
+ PREVIOUSLY BUSINESS-ORIENTED DATA MADE CONSUMER-ACCESSIBLE
+ FOUNDER GROWTH EXPERIENCE
```

Transfer limit: geography, legal data access, privacy, regulatory and trust burden are central; do not generalize to
"safety apps win".

### Tiro — repeated note-taking workflow + multi-segment expansion (Korea)

Mixed current evidence shows a live Korean AI note-taking product with consumer and team pricing, substantial App Store review activity, company-reported ARR/funding, and 2026 Korean business coverage reporting roughly 10x annual-revenue growth over a year. Candidate mechanism:

```text
REPEATED MEETING / LECTURE JOB
+ FAST CAPTURE / SUMMARY VALUE
+ INDIVIDUAL → TEAM / ENTERPRISE EXPANSION
+ CAMPUS / PROFESSIONAL DISTRIBUTION SURFACES
```

Transfer limit: exact ARR/funding figures are company/promotional claims unless independently audited; revenue growth does not establish causality; founder network, capital, enterprise sales, model quality, and timing may matter. Treat Tiro as a Korean mechanism fixture, not proof that `AI note takers win`.

### Fly — immediate demoability + external viral amplification

Secondary reporting described rapid revenue for a browser flight simulator after a high-profile social share.
Candidate mechanism:

```text
INSTANT VISUAL VALUE
+ LOW START FRICTION
+ SHAREABILITY
+ MICROTRANSACTION FIT
```

But founder reputation and celebrity amplification are major alternative explanations. Treat this as a high-replicability-risk
success story, not a default game GTM playbook.

## Counterevidence / low-outcome fixtures

Public maker anecdotes in Korean communities include AI-built content pipelines, website-template services, and games that
were technically functional yet produced zero or minimal revenue/users. These anecdotes cannot estimate a failure rate.
They are useful only to preserve this mechanism:

```text
BUILD_COMPLETION != DISTRIBUTION
BUILD_COMPLETION != CUSTOMER_VALUE
BUILD_COMPLETION != REVENUE
```

Aggregate evidence is more important: RevenueCat's 2026 sample shows a large increase in subscription-app launches alongside
extreme outcome dispersion, with top performers growing strongly and bottom performers contracting. This supports a
`SUPPLY_SHOCK + DISTRIBUTION/RETENTION BOTTLENECK` prior, not a universal failure probability.

## Pattern triangulation contract

Do not call something a `market-favored pattern` merely because one case succeeded.

Prefer at least two **different evidence classes** where feasible, for example:

```text
aggregate benchmark / market-spend data
+ named product case
+ low-outcome/counterexample or failure-risk evidence
```

Record:

```text
PATTERN_NAME
OBSERVED_ACROSS
EVIDENCE_CLASSES
MECHANISM_HYPOTHESIS
COUNTEREVIDENCE
TRANSFER_ASSUMPTIONS
FOUNDER_SPECIFIC_ADVANTAGES
APPLICABILITY_TO_CURRENT_PRODUCT
CONFIDENCE
WHAT_WOULD_CHANGE_THE_PRIOR
```

If evidence is limited to vendor success stories, label the result `CASE-DERIVED HYPOTHESIS`, not `market-favored`.

## Relative comparison contract

When the user gives two or more product ideas, FieldPilot should make a recommendation when the evidence permits it.
Do not hide behind "both could work" if one has a materially stronger prior.

Example:

> "현재는 범용 AI SNS 비서보다 특정 판매자의 반복 상품등록 업무를 줄이는 도구를 먼저 검증하겠습니다.
> 후자는 타깃, 반복 트리거, 기존 작업비용, 가치 측정이 더 명확합니다. 다만 실제 판매자 사용/결제는 아직
> 검증되지 않았으므로 이 판단은 우선순위 추천이지 성공 보장이 아닙니다."

Then give the exact cheapest informative test.

## Source baseline (2026-08-27)

- `V16-S14` RevenueCat — State of Subscription Apps 2026: 115,000+ apps / $16B+ subscription revenue sample;
  strong for conditional app monetization/retention distributions, not all apps or startup success rates.
- `V16-S22` Lovable — The Build Economy 2026: platform usage Jan 2025–May 2026 + 14,300+ user survey;
  descriptive of Lovable builders, not market demand.
- `V16-S23` Menlo Ventures — State of Generative AI in the Enterprise 2025: ~500 U.S. enterprise decision-makers +
  bottoms-up market model; enterprise spend/adoption prior, not startup survival probability.
- `V16-S24` Lovable customer/founder case studies: named mechanism examples; vendor-selected success stories with
  strong selection/survivorship risk.
- `V16-S25` Indie Hackers/public founder reporting on vibe-coded apps: secondary/self-reported outcome examples;
  use for mechanism hypotheses and replicability analysis, not prevalence.
- `V16-S26` Korean maker/community posts (Disquiet/DCInside/Blind): user-need and low-outcome anecdotes;
  not representative market statistics.
- `V16-S27` Tiro mixed case evidence: company/product/App Store/press sources for a Korean productivity mechanism fixture;
  not a category success-rate estimate or causal proof.

Re-verify volatile figures and case status when material to a recommendation.
