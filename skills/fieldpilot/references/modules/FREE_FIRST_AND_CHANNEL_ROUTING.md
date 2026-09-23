# v1.6 — Free-First Validation & Channel Routing

## Governing rule

**FREE-FIRST is a cost-escalation rule, not an evidence downgrade.**

Among realistic routes strong enough to answer the active decision question, choose the lowest-cost/lowest-burden path. If free evidence cannot distinguish the important alternatives, move upward in cost deliberately.

```text
FREE → NEAR_ZERO_COST → LOW_PAID → SCALED_PAID
```

Escalation requires all of:

- unresolved question can change the decision;
- lower-cost evidence is insufficient;
- paid route can produce stronger information;
- tracking/measurement is interpretable;
- commitment is proportionate and reasonably reversible.

Never escalate merely because "we tried free promotion for N days."

## Channel selection inputs

```text
active_search_intent
latent_discovery_demand
audience_presence_and_concentration
B2B_or_B2C
visual_demoability
trust_requirement
purchase_complexity
price
sales_cycle
platform
geography
founder_content_skill
founder_sales_skill
existing_audience
budget
product_stage
```

There is no universal channel ranking.

### Operational-advice provenance guard

Channel mechanics, algorithm behavior, community norms, timing advice, format claims,
and statements that one channel "works better" for a product class are operational claims.
Classify them as `CURRENT_PLATFORM_FACT`, `RESEARCH_BACKED`, `PROFESSIONAL_GUIDANCE`,
`CONTEXT_DERIVED`, `FIELDPILOT_HEURISTIC`, or `UNSUPPORTED`. Do not present common
marketing lore as a verified expert fact. If the recommendation is only a plausible route,
say why it is plausible for this user and define the cheapest channel-fit test.

### Execution-number guard

Do not invent a universal count of posts, videos, communities, contacts, days, or budget. A phrase such as `post 3–5 videos`, `try three communities`, or `run for seven days` requires a source-backed/platform-scoped reason or an explicit context-derived justification. Otherwise prescribe the artifact and measurement logic without pretending the count is an expert threshold.

### Community/concept evidence guard

- Comments, likes, upvotes, saves, or replies are exposure/attention/qualitative signals; they do not by themselves demonstrate product demand.
- Community members are a selected audience; do not generalize their response to the broader target market without a defensible transfer argument.
- Do not recommend named communities as if access is guaranteed. Verify current audience relevance, participation/self-promotion rules, and feasibility when material.
- Keep problem evidence and concept reaction separate. Avoid leading prompts that presuppose use of a named competitor or tell participants what differentiation they should notice.
- For a concept test, prefer a concrete artifact and a behaviorally meaningful downstream action where feasible; preserve what comments/replies can and cannot establish.

## Geography adapter

Geography can change more than channel choice: it can change the alternative set, local incumbents/manual substitutes, regulation, currency/price anchors, platform rules, and audience access.

When geography materially changes any of those dimensions, load the relevant local context before finalizing the affected recommendation. For Korea:
- load `KOREA_LOCAL_DISTRIBUTION.md`;
- satisfy its local competition/substitute/access slots;
- load `REGULATORY_CONTEXT_CHECK.md` when regulation is material.

Do not treat global maker-channel defaults as geography-neutral.
Do not infer the target geography from the user's language, account/current location, or a previous project. If geography is unresolved and decision-changing, ask only that one necessary question; otherwise keep the local conclusion unresolved.

### Peer-feedback guard

Feedback from developer/maker communities can be strong for bugs, implementation quality, UX friction, store copy or technical concerns. Unless those peers are also the target customers, it is weak evidence for target demand, willingness to pay, retention or broader-market preference.

### Viral-spike guard

Community virality, platform featuring, creator exposure or press spikes are acquisition events. Diagnose their downstream activation, return and payment separately before calling them durable traction or a repeatable growth engine.

## Candidate organic / free routes

### SEO / organic search
Plausible when users already articulate the problem or solution in search.

Can measure: impressions, queries, clicks, qualified downstream actions.

Failure may indicate: no search volume, weak ranking/indexing, wrong query, weak snippet/page, message mismatch.

Failure does not prove: no market demand overall.

### Reddit / niche forums
Plausible when a relevant community demonstrably contains the target audience and discussion norms allow useful participation.

Can measure: actual exposure if available, replies, qualified clicks, conversations, problem language.

Failure may indicate: no exposure, community mismatch, trust/account issue, message/self-promotion issue, weak relevance.

Failure does not prove: product demand failure.

### Discord / community servers
Plausible when the audience is concentrated in known servers and relationship-based participation is feasible.

Evidence is often selective and community-specific; broader-market generalization is limited.

### LinkedIn / direct outreach
Plausible for identifiable professional users/buyers, especially when high trust, complex purchase, or direct demos matter.

No universal message length, contact count, or response-rate threshold.

Distinguish deliverability/access failure from offer/problem rejection.

### TikTok / Reels / Shorts
Plausible when the product or problem can be demonstrated visually and discovery behavior matters.

High views support exposure/attention, not product demand. Trace view → click/profile → landing/store → activation → return/payment.

### YouTube
Plausible when education, comparison, demo depth, or searchable explanation matter. Production burden may be high.

### Creators / newsletters
Plausible when trusted intermediaries already aggregate the target audience. Separate creator access from downstream product value.

### Launch communities
Product Hunt, Hacker News, and similar communities are audience-specific candidate routes, not universal defaults for AI or software products.

### App stores / Steam-native routes
Use official store discovery, product-page, demo/playtest, events, wishlist/traffic, or peer benchmark tools where applicable. Do not import generic web-funnel mechanics into platform visibility rules without checking official documentation.

### Partnerships / referrals
Plausible when another actor controls relevant audience access and mutual value exists. Referral requires existing users with a reason to share; absence of referral does not equal absence of product value.

## Mandatory Execution Kit for market-response recommendations

A recommendation to `check market response`, `validate demand`, `see how users react`, or `test the market` is incomplete unless it includes an executable method. Never leave the novice to invent the research operation.

Required fields:

```text
DECISION_QUESTION
TARGET
ACCESS_ROUTE
ARTIFACT
EXACT_STEPS
MEASUREMENT
OBSERVATION_MECHANISM
RECORD_LOCATION_OR_FORMAT
MEASUREMENT_HEALTH_CHECK
SELECTION_BOUNDARY
DECISION_CHECKPOINT_OR_STOP_CONDITION
INTERPRETATION
WHAT_THIS_CAN_PROVE
WHAT_THIS_CANNOT_PROVE
NO_RESPONSE_DIAGNOSTIC
NEXT_ACTION_IF_POSITIVE
NEXT_ACTION_IF_NEGATIVE_OR_AMBIGUOUS
```

Execution behavior:

- If the user has enough context, generate the artifact now rather than asking whether they want one. Examples: copy-ready outreach message, community post, landing-page copy, interview guide, demo script, tracking-event list, store-page experiment brief.
- `MEASUREMENT` is not complete until the user knows how each decision-relevant behavior will be observed and where it will be recorded. Choose one feasible mechanism: a tagged or unique link, named product/analytics events, server or payment logs, or an explicit manual check-in plus a copy-ready record table. If no mechanism exists, instrument the smallest path first and verify a test event before interpreting real-user results.
- Bind the reasoning to this product's job, usage occasion, stage, geography, and current evidence. A generic risk label that could survive a noun swap is not paid differentiation by itself.
- State the selected-sample boundary. Reusing requesters, friends, waitlist members, maker peers, or one community may be efficient, but it does not remove selection bias or establish broader-market prevalence.
- Give a decision checkpoint or stop condition tied to the product's natural usage cycle, runway, or the evidence needed for the next decision. If a number is only a starting heuristic, label and justify it rather than presenting it as a universal rule.
- If access to the target population is the blocker, give an access-finding procedure before a research instrument.
- If a named community/platform is recommended, verify current relevance and participation/self-promotion constraints when material.
- Do not treat comments, likes, or replies as demand by themselves; define a downstream action when a stronger behavioral signal is feasible.
- A failed test must include a diagnostic path so the user can distinguish reach/access/message/channel failure from product-demand failure.
- If an audit discovers that eligible users never received the price, offer, repeat-use opportunity, or other behavior required by the active decision, attach the smallest next step that creates and observes that missing opportunity. Do not report an audit as if it supplied evidence that never had a chance to occur.
- If the product, buyer, job, or prior exposure is absent and changes the route, do not substitute FieldPilot or a familiar example as user fact. Ask only the decision-changing fact, or keep a copy-ready parameterized artifact with explicit placeholders.

### User-visible instrumentation minimum

Do not satisfy the Execution Kit with nouns alone. `Track completion`, `send a
link`, `check analytics`, or `write it in a spreadsheet` still leaves the user to
design the operation. In the answer itself, select and instantiate the smallest
feasible mechanism:

```text
MECHANISM: one unique/tagged link, named analytics events, named server/payment
           log fields, or an explicit manual check-in
RECORD_HEADER: participant_or_source | access_time | core_action_started |
               core_action_completed | return_opportunity | returned |
               friction_or_reason | evidence_link_or_log_id
HEALTH_CHECK: perform one test path and confirm its event/log/row before outreach
CHECKPOINT: decide only after the participant had the product's natural first-use
            occasion and, when repeat value matters, a real opportunity to return
STOP_OR_REPAIR: if access or telemetry failed, repair and rerun; do not label it
                demand failure
```

Adapt field names to the actual product and omit fields that cannot affect the
decision. Prefer literal event names or a copy-ready table header. If the product
has no analytics, a manual record plus timestamp/evidence link is valid; do not
invent nonexistent instrumentation. A checkpoint may be event-based rather than
an arbitrary universal day/count threshold.

User-facing minimum: **what to do today, where/who to do it with, what exact material to use, what to record, and how the result changes the next step.**

## Channel Route contract

For the recommended first route output:

```text
RECOMMENDED_FIRST_CHANNEL
WHY
FREE_VERSION
PAID_VERSION
PREREQUISITES
EXACT_FIRST_TEST
WHAT_TO_MEASURE
WHAT_RESULT_WOULD_SUPPORT
WHAT_RESULT_WOULD_NOT_SUPPORT
SELECTION_BIAS
FAILURE_INTERPRETATIONS
NEXT_ROUTE_IF_IT_FAILS
CONFIDENCE
```

Default to one recommended first route, not a menu, when enough context exists. Give one fallback route.

## Paid acquisition

Paid acquisition may be used for validation when it answers a decision-relevant question and measurement is healthy. It is not automatically superior or required.

Before recommending spend:

1. state what uncertainty paid traffic will distinguish;
2. verify current platform mechanics if they materially determine setup;
3. ensure conversion/analytics tracking is fit for the intended claim;
4. distinguish traffic/attention metrics from activation/retention/payment;
5. set a context-derived commitment boundary, not a universal budget.

Never hard-code an old platform learning threshold as a permanent product rule.
