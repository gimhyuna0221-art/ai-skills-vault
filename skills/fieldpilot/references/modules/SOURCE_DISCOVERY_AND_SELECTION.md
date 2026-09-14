# Source Discovery, Selection and Reproducibility — v1.7.2

A per-claim citation list makes evidence **re-checkable**. It does not make it **reproducible**.
An independent reviewer can verify the sources that were supplied, but cannot re-derive why those
sources and not others — which matters, because the source set is itself a sampling decision.

This module records the search, the selection, the independence profile of the evidence, and the
timing of substantive research.

It is **additive**. `references/delivery/EVIDENCE_PLAN_AND_COVERAGE_AUDIT.md` remains controlling for
coverage states and sufficiency. **No minimum source count is introduced here, and source counts
remain description, never evidence of sufficiency.**

Rule anchors: `R-SOURCE-01`, `R-DESK-01`, `R-TRI-01`, `R-COMP-02`, `R-AUDIT-01`, `R-CLAIM-01`.
Source anchors: search-reporting structure adapted from `V16-S29`; `S-ESOMAR`, `S-AAPOR-DISC`.

## 1. SOURCE_DISCOVERY_RECORD

Record how the evidence was found, at a level a competent reader could repeat.

```text
SOURCE_DISCOVERY_RECORD
  questions_this_search_served        which material questions from the EVIDENCE_PLAN
  where_searched                      engines, platforms, official registries, app or game stores,
                                      review sites, community platforms, trade press, official
                                      statistical sources, the user's own authorized data
  how_searched                        the actual queries or query patterns as run, and the
                                      language(s) used
  limits_and_restrictions             geography, language, period, paywall or access barriers,
                                      robots or rate limits, and why each limit was applied
  search_dates
  what_was_found_and_admitted
  what_was_found_and_excluded         with the exclusion reason
  inclusion_and_exclusion_criteria    fixed before scanning results where practical
  deduplication                       how mirrored, syndicated or republished items were collapsed
  stop_rule                           why the search stopped where it did
  known_blind_spots                   what this strategy would systematically miss
```

Adapt the depth to the engagement. A bounded question needs a short record; a full engagement
needs a complete one. The record is never omitted on the grounds that the search was informal —
an informal search is recorded as an informal search.

This structure is adapted from literature-search reporting practice (`V16-S29`). Adapting the
structure does **not** make a market scan a systematic review, does not import systematic-review
completeness expectations, and does not make the resulting source set representative. Do not claim
or imply systematic-review status.

### 1.1 Access-aware admission gate

Discovery and evidence admission are separate. A result may be discoverable but still unusable as
support because the current host cannot retrieve it safely or without unavailable authorization.
Apply the access-friction rules in `references/modules/ZERO_COST_LIVE_SOURCE_LADDER.md` before
turning a discovered locator into admitted evidence.

For each material source candidate:

1. discover the candidate;
2. perform a bounded access preflight where the host permits;
3. prefer a smaller set of accessible authoritative sources over a larger set of equivalent domains;
4. if retrieval fails, the page is wrong, login/paywall is unavailable, or host/network policy blocks it,
   put it in `what_was_found_and_excluded` with the reason and move to a fallback;
5. do not ask the user for source-specific access unless that source is decision-critical and no adequate
   accessible fallback exists;
6. never present excluded/inaccessible content as if it had been read.

Host-level URL approval dialogs are not themselves evidence that a source is private or invalid. They are
security controls. FieldPilot must not attempt to bypass them; it should reduce unnecessary prompts by fetching
only the smallest sufficient evidence set.

## 2. INDEPENDENCE and source diversity

Independence is part of sufficiency, and it is separate from source count.

```text
INDEPENDENCE_CLASS
  FIRST_PARTY_VENDOR          the vendor's own page about its own offer
  FIRST_PARTY_PLATFORM        the platform's own documentation about its own mechanics
  INDEPENDENT_THIRD_PARTY     not controlled by, and not derived from, the subject
  OFFICIAL_STATISTICAL        official statistical, regulatory or registry source
  COMMUNITY_ANECDOTE          forum, social or community post
  USER_SUPPLIED               evidence the user provided
```

Rules:

- For a claim about **market structure** — category shape, competitive landscape, adoption,
  prevalence, who the players are — actively seek at least one `INDEPENDENT_THIRD_PARTY` or
  `OFFICIAL_STATISTICAL` source.
- For a claim about **a vendor's own offer** — its published price, its stated features, its stated
  plans — a `FIRST_PARTY_VENDOR` source is the correct and preferred source. Do not weaken it by
  demanding third-party corroboration of a vendor's own price.
- When no independent evidence is materially available after a bounded search, record
  `INDEPENDENT_EVIDENCE: SEARCHED_NOT_FOUND` with the search boundary, and **lower the claim
  ceiling** on the affected market-structure statements. This is a legitimate, reportable outcome.
- **Never force it.** Do not promote an SEO comparison article, a content-marketing listicle, a
  vendor-sponsored report presented as neutral, or an aggregator restating a vendor page into
  `INDEPENDENT_THIRD_PARTY` in order to satisfy this rule. A derivative of the subject is not
  independent of the subject.
- Corroboration counts independent **origination**, per the origination rule in
  `references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md` section 4.
- No minimum count is imposed, and a larger source set is not thereby a better one.

## 3. RESEARCH_TIMING_LOG

Record when substantive research actually happened, so execution ordering can be reconstructed by
someone who was not present.

```text
RESEARCH_TIMING_LOG
  substantive_research_start          first substantive evidence-gathering action, with timestamp
  substantive_research_end            last substantive evidence-gathering action, with timestamp
  timezone
  material_interruptions              continuations, tool failures, session breaks
  ordering_note                       what preceded what, where ordering is claimed
```

Rules:

- If the timing was not logged, record `NOT_LOGGED` and state the reproducibility consequence:
  the asserted ordering cannot be independently reconstructed. Do not reconstruct a plausible
  timestamp after the fact — an invented timestamp is a fabricated record.
- Access dates on individual sources are **not** a substitute for the run timing log. They record
  when a page was seen, not when the research began or in what order.
- This log is a QA and reproducibility artifact. It is summarized in the delivery envelope's
  reproducibility notes in plain language, not pasted as raw internal state.

## 4. Rendering in the deliverable

- The discovery record and independence profile appear in the report's evidence-base section, so
  the reader sees them next to the source register rather than in end matter.
- The delivery envelope's method and source-selection rationale points to that section instead of
  duplicating it.
- Where the search was bounded by access or capability, say what the boundary was. A stated
  boundary is a professional disclosure; an unstated one reads as coverage that was never achieved.

## 5. Failure modes this module exists to prevent

- A final source list presented as if it were a search method.
- A competitor set that is a sampling decision, presented as a neutral fact.
- Every market-structure claim resting on the subjects' own pages, with the absence of independent
  evidence never stated.
- A content-marketing article promoted to independent evidence to fill the independence slot.
- A discovered-but-unread URL presented as supporting evidence.
- Repeated user interruption for non-critical source access when an adequate accessible fallback exists.
- Four republications of one origin counted as four sources.
- Source count offered as evidence of sufficiency.
- An unlogged research start reconstructed after the fact as a plausible timestamp.
