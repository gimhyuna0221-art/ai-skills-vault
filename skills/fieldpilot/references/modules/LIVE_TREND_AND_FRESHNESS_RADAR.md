# Live Trend, Freshness and Timing Runtime — v1.7.2

Trend and freshness are a first-class quality layer, not an appendix. This module governs how
FieldPilot assembles current-market signal, decides how fresh evidence has to be, validates
whether something is actually a trend, and answers WHY NOW.

It is **additive** and subordinate to existing contracts. `references/modules/PLATFORM_FACTS_AND_DATA_ACCESS.md`
remains controlling for provenance classes, numeric-threshold records, data-access classes, the
fallback contract and source conflict. `references/modules/RESEARCH_REFRESH_AND_CHANGE_IMPACT.md`
remains controlling for returning-user delta behaviour. This module adds the first-run radar,
scoped freshness, trend validation and timing judgement.

For source-route selection, authentication/cost boundaries, and reproducible current retrieval, also
apply `references/modules/ZERO_COST_LIVE_SOURCE_LADDER.md`. That ladder governs how evidence is acquired;
this module continues to govern freshness, corroboration, trend meaning, and WHY NOW.

Rule anchors: `R-SOURCE-01`, `R-DESK-01`, `R-TRI-01`, `R-NUMERIC-01`, `R-CLAIM-01`,
`R-CAUSAL-LANG-01`, `R-COMP-02`, `R-NEG-01`.
Source anchors: `V16-S12` (Google Trends first-party caveats), `V16-S31` (durable capture),
`V16-S20`, `V16-S21`, `V16-S16`, `V16-S17`, `V16-S18`, `V16-S19`, `S-ESOMAR`.

## 1. TREND_SOURCE_STACK — adapt to the vertical and the decision

There is no universal source list. Assemble the stack from what actually carries signal for this
product type, buyer and geography. Candidate classes:

```text
official current competitor pages and changelogs
platform charts, rankings and store listings
search-interest and keyword-intent tools
app, game or category intelligence products
current reviews and rating movement
forums, communities and creator signal
release notes, pricing pages and packaging changes
industry and trade coverage
regulatory and policy announcements
the user's own authorized first-party data, where it exists
```

Rules:

- Paid intelligence products are **examples of a class, not dependencies**. When a paid source is
  unavailable, use the accessible alternative and record the evidence loss through the existing
  fallback contract (`PRIMARY_SOURCE_NEEDED`, `ACCESS_STATUS`, `FALLBACK_SOURCE`,
  `WHAT_FALLBACK_CAN_ANSWER`, `WHAT_IT_CANNOT_ANSWER`, `EXPECTED_EVIDENCE_LOSS`). Never present a
  proxy as equivalent to the missing source.
- Search-interest tools report **relative normalized interest for a stated geography and window**,
  not volume, customers or demand. `V16-S12` records the first-party caveats: the data is a
  sample rather than a census, it is normalized and rescaled 0-100, statistical noise is added and
  is most visible on low-volume queries, irregular and duplicate activity is filtered, the time
  zone differs between short and long ranges, and the provider states it is not a scientific poll.
  A normalized index may never be reported as a count, and a rise in it is interest, not purchase.
- Where the current stack cannot see something material, say so. An unobservable dimension is an
  `UNKNOWN`, not a zero.

## 2. CURRENT_CLAIM_RECORD — what every material current-market claim carries

```text
CURRENT_CLAIM
  claim
  as_of                         the state the claim describes
  access_date                   when FieldPilot actually looked
  source_date                   publication or last-updated date, or PUBLICATION_DATE_NOT_STATED
  geography_or_segment
  retrieval_route               FREE_API / OPEN_DATASET / OFFICIAL_WEB / PUBLIC_STATISTICAL /
                                PLATFORM_SIGNAL / PUBLIC_WEB / USER_SUPPLIED
  source_or_endpoint_identity   endpoint/dataset/page/feed/filing and safe reproducible pointer
  terms_auth_quota_state        when relevant; never a secret value
  source_type_and_bias          vendor, platform, third-party estimate, official, community, user
  independence_class            FIRST_PARTY_VENDOR / FIRST_PARTY_PLATFORM /
                                INDEPENDENT_THIRD_PARTY / OFFICIAL_STATISTICAL /
                                COMMUNITY_ANECDOTE / USER_SUPPLIED
  corroboration                 see section 4 origination rule
  confidence                    HIGH / MEDIUM / LOW / UNKNOWN, with the reason
  durable_capture               CAPTURED / CAPTURE_FAILED / NOT_ATTEMPTED, with the locator when captured
```

Never backdate an access date, never convert "current as accessed" into "published on", and never
turn an inaccessible or ambiguous page into a precise fact.

A documented or planned API call is not a current observation. Record it only after actual retrieval;
otherwise use the ladder's fallback state and preserve the unresolved claim. Never invent a key, quota,
response, or live status.

### Durable capture

When a decision-relevant page carries **no publication or update date**, or is known to change
without notice, capture it durably at access time where feasible (`V16-S31`) and record the
archived locator alongside the live URL.

Capture is a reproducibility control, not an evidence upgrade. It does not validate the content.
Capture can legitimately fail on paywalled, robots-restricted or dynamic pages: record
`CAPTURE_FAILED` truthfully. **Never state that a snapshot exists when none was taken.**

## 3. FRESHNESS_POLICY — scoped, never a single global cutoff

Freshness is a function of three inputs, not one:

```text
freshness_requirement = f(MARKET_VELOCITY, SOURCE_TYPE, DECISION_HORIZON)
```

`MARKET_VELOCITY` — assign per claim, with a stated reason:

```text
VERY_HIGH   daily-to-weekly movement: store charts, live pricing and promotions, ad mechanics,
            platform policy, viral attention, fast-moving app/game categories
HIGH        weekly-to-monthly: competitor packaging, feature launches, category entrants
MODERATE    quarterly-to-annual: category structure, distribution norms, buyer behaviour
LOW         multi-year: official demographic, statistical and structural datasets, durable
            regulatory frameworks, established methodological findings
```

`SOURCE_TYPE` — an official statistical release does not go stale on the same clock as a pricing
page. An older official dataset can be entirely appropriate; a six-week-old scraped price may not be.

`DECISION_HORIZON` — read from `decision_horizon_or_deadline` in the frozen `CLIENT_DECISION_BRIEF`.
Do not ask for it again. The same evidence age can be adequate for a category-entry decision and
inadequate for a pricing decision that executes next week.

Rules:

- State the freshness judgement per material claim, with its reason. Do not apply one age cutoff
  across the report.
- When a claim is materially decision-changing and cannot be re-verified now, downgrade it to
  `UNVERIFIED / HISTORICAL` and lower the dependent conclusion. Do not present a cached figure as
  a current fact, and do not block the rest of the research over it.
- When the horizon is `UNRESOLVED` in the brief, say that the freshness requirement is
  horizon-dependent and unresolved rather than silently choosing one.

## 4. TREND_VALIDATION — a trend is a validated state, not a headline

Before anything is called a trend, evaluate all seven dimensions. Any dimension may be `UNKNOWN`;
`UNKNOWN` is recorded, not skipped.

```text
TREND_VALIDATION
  signal
  VELOCITY                  rate and direction of change, over a stated window
  PERSISTENCE               transient spike versus sustained movement; how long observed
  BREADTH                   one channel or segment versus spread across independent origins
  BEHAVIOR                  attention and sentiment versus observed usage, purchase or retention
  GEOGRAPHY_SEGMENT         where, and for whom
  COMMERCIAL_RELEVANCE      whether it changes this user's decision at all
  CROSS_SOURCE_CONFIRMATION independent corroboration, per the origination rule below
  TREND_STATE               FAD / EMERGING / ACCELERATING / MAINSTREAM / DECLINING / UNCERTAIN
  what_would_falsify_or_reverse_it
```

### Independent origination rule

Corroboration counts **independent origination**, not repeated publication.

- Syndicated, aggregated, republished or derivative coverage of a single origin counts as **one**
  corroboration, no matter how many outlets carry it.
- A vendor announcement plus the coverage of that announcement is one origin.
- `BREADTH` may not be claimed from a single origination.
- Record `ORIGINATION` for each corroborating item so the count is inspectable.

### Hard classification rules

- A single source, or a single time window, is **never** sufficient for `ACCELERATING` or
  `MAINSTREAM`. Without independent corroboration or observed persistence, the ceiling is
  `UNCERTAIN`, or `FAD` where the evidence positively indicates a transient spike.
- Attention is not behaviour. Search interest, mentions, views and sentiment may support
  `EMERGING` at most; `MAINSTREAM` requires observed usage, purchase or retention evidence.
- A viral spike is not a durable trend. This restates and does not weaken the existing
  `VIRAL SPIKE != DURABLE TRACTION` invariant.
- `DECLINING` needs the same evidence standard as a rise. Do not infer decline from silence,
  from a single quarter, or from absence of coverage.
- **No fake precision.** Do not emit a trend score, a strength percentage, a confidence number, or
  any invented threshold such as "3 sources" or "30 days". States are ordinal and justified in
  words. A scoped, preregistered observation window may be stated as a choice for this study; it
  is never a universal market rule.

## 5. WHY_NOW — timing judgement

Answer when timing is material to the decision. Where a sub-answer is unavailable, mark it
`UNKNOWN`; do not fill it with narrative.

```text
WHY_NOW
  what_materially_changed_recently      with evidence and dates
  did_this_opportunity_exist_before     and if so, why it was not taken or not viable
  why_enter_now_rather_than_later       or why later is better
  window_state                          OPENING / STABLE / CROWDED / CLOSING / UNKNOWN
  which_current_signal_could_reverse_the_conclusion
  timing_conclusion
```

`timing_conclusion` is one of:

```text
TIMING_ADVANTAGE_PRESENT
NO_CURRENT_TIMING_ADVANTAGE
TIMING_DISADVANTAGE
TIMING_UNKNOWN
```

**`NO_CURRENT_TIMING_ADVANTAGE` is a legitimate and frequently correct conclusion.** Do not
manufacture urgency. "Everyone is talking about it" is attention, not a window. A crowded window is
a real finding and must not be reported as an opportunity. Timing claims inherit the trend states
they rest on: a `UNCERTAIN` trend cannot support `TIMING_ADVANTAGE_PRESENT`.

## 6. Refresh interaction

`SUCCESS_CASE_SET`, `COMPARATOR_SET` and `TREND_STATE` are refreshable dependencies. On a
returning-user refresh they are selected for revalidation on the same decision-relevance test as
any other dependency, and classified through the existing change vocabulary. A stale trend state
is worse than an absent one, because it looks current. See
`references/modules/RESEARCH_REFRESH_AND_CHANGE_IMPACT.md`.

## 7. Failure modes this module exists to prevent

- One global freshness cutoff applied to structurally different evidence.
- A normalized search index reported as search volume, customers or demand.
- A single viral spike, or one channel's movement, presented as a durable market trend.
- Four articles rewriting one press release counted as four-source corroboration.
- Attention evidence used to claim adoption.
- An undated volatile page cited with no capture and no re-checkability.
- Manufactured urgency when the honest answer is that there is no current timing advantage.
- A trend score or percentage invented from a handful of observations.
