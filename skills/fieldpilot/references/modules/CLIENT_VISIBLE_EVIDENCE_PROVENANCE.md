# Client-Visible Evidence Provenance Gate — v1.9.1

This module repairs the client-visible provenance path. It does not create a second evidence system.
It validates and renders the existing source discovery record, evidence register, timing log, claim
states, coverage audit, commercial bundle, and refresh dependencies before any client deliverable is
released.

The governing discovery rule is:

> FASTEST SOURCE WINS DISCOVERY. STRONGEST EVIDENCE WINS FINAL CLAIM.

## 1. Execution-time access record

At the first material retrieval, capture `RUN_ACCESS_STARTED_AT` from the host clock as an RFC 3339
date-time with an explicit UTC offset or `Z`. Each actually accessed source receives its own
`access_date_time` from the retrieval event. `RUN_ACCESS_ENDED_AT` is captured from the host clock
when the provenance gate runs.

Never leave a declared access field blank. Never emit whitespace, `TBD`, `TODO`, `N/A`, `UNKNOWN`,
`NOT RECORDED`, a template token, a date copied from an example, or a stale hardcoded date as an
access value. Publication or observation time is not access time. If a source was not accessed in
this run, do not invent an access time; classify it as planned/unavailable and keep it out of the
actually-accessed evidence set.

The gate accepts an access time only when it parses as RFC 3339 and falls between the run's recorded
start and gate time, allowing only the host's documented clock-skew tolerance. A date-only value may
be shown to a client in addition to the timestamp, but the evidence record retains the full timestamp.

## 2. Canonical material source record

Every material source used by a customer-facing claim has one stable `source_key` and this minimum
record. Fields that are not applicable remain explicit; fields that are unavailable carry a truthful
state and reason.

```yaml
source_key: SRC-001
materiality: MATERIAL
source_identity:
source_role_character: OFFICIAL_FIRST_PARTY | INDEPENDENT_AUTHORITATIVE | INDEPENDENT_SECONDARY | COMMUNITY_SENTIMENT | UNVERIFIED_SIGNAL | USER_SUPPLIED
locator:
locator_status: PROVIDED | UNAVAILABLE_WITH_LIMITATION
locator_limitation:
locator_origin: OBSERVED_IN_RETRIEVAL | USER_SUPPLIED | OFFICIAL_METADATA | NOT_AVAILABLE
retrieval_status: RENDERED_AND_VERIFIED | PRIMARY_FAILED_ALTERNATE_VERIFIED | NOT_RETRIEVABLE_WITH_LIMITATION
alternate_locator:
alternate_locator_origin: OBSERVED_IN_RETRIEVAL | OFFICIAL_METADATA | NOT_AVAILABLE
alternate_locator_limitation:
publication_or_observation_date:
publication_date_state: PROVIDED | NOT_STATED | NOT_APPLICABLE
access_date_time:
geography_segment_period:
claim_boundary:
corroborating_source_keys: []
corroboration_status: CORROBORATED | PARTIALLY_CORROBORATED | NOT_CORROBORATED | NOT_REQUIRED_FOR_BOUNDED_CLAIM
evidence_state: FACT | SUPPORTED_INFERENCE | UNKNOWN | RECOMMENDATION | EARLY_SIGNAL
claim_ceiling:
contradiction_state:
retrieval_route:
revision_id:
```

`locator` is a direct URL, exact filing/release/issue/dataset identifier, document plus page/table/line,
or another reproducible stable pointer actually exposed by the source surface. Never synthesize a URL
from a title, account name, guessed slug, search snippet, or remembered route. When no direct locator
can truthfully be produced, use `UNAVAILABLE_WITH_LIMITATION`, leave `locator` empty, explain the
limitation, and preserve the strongest reproducible source identity available. A missing locator and a
missing limitation fail the gate.

For a material source whose primary locator does not render or cannot be retrieved, record the failed
route in `retrieval_status` and use only an alternate locator actually observed during this run. If no
alternate route is available, set `alternate_locator_origin: NOT_AVAILABLE`, state the limitation, and
narrow the affected claim. A guessed alternate route or an unqualified claim fails
`RETRACEABLE_LOCATOR_FALLBACK_GATE`.

## 3. Claim-to-source chain and client rendering

Every material numeric, comparative, or decision-relevant claim receives a `claim_key`, an evidence
state, a claim ceiling, and one or more visible source keys. The complete audit chain is:

```text
claim_key -> source_key -> locator -> access/publication date
          -> source role/character -> evidence state / claim ceiling
```

Use `[SRC-001]` or an equally unambiguous visible reference next to the claim, table row, chart, or
finding. Every visible source key must resolve to exactly one record in the delivered
`EVIDENCE_AND_SOURCE_REGISTER`. Every source key listed on a material claim must exist. Duplicate keys,
missing keys, or ambiguous aliases fail closed.

The client report must either include a visible source appendix or name the delivered evidence register
by exact component/file identity and use source keys that resolve there. A pointer to an internal runtime
file, private state object, or undisclosed audit log is not client-visible traceability. Principal evidence
anchors expose their source identity, locator or truthful locator limitation, publication/observation
date state, access date-time, source role, and evidence state in the client-visible bundle.

## 4. Public social and community evidence

Use the smallest materially relevant set of publicly accessible, permitted, zero-extra-cost surfaces.
These may include X/Twitter, Threads, Instagram, public Telegram channels, lawfully accessible public
Discord/community announcements, GitHub releases/issues/discussions, maintainer posts, and other public
feeds. This contract does not authorize a crawler, always-on monitor, paid API/firehose/scraper, account
creation, private-group joining, or access-control bypass.

A material social/community record additionally preserves, where exposed:

```yaml
retrieval_route: PUBLIC_SOCIAL_COMMUNITY
platform:
direct_post_thread_message_url_or_stable_locator:
account_channel_name:
account_handle:
account_role: OFFICIAL_FIRST_PARTY | INDEPENDENT_COMMUNITY | UNVERIFIED
publication_timestamp_and_timezone:
access_date_time:
claim_boundary:
corroborating_source_keys: []
corroboration_status:
evidence_state: FACT | SUPPORTED_INFERENCE | UNKNOWN | RECOMMENDATION | EARLY_SIGNAL
```

An official account post is first-party evidence that the account made that statement at that time. It
does not by itself prove every underlying fact. An unofficial expert, user, trader, creator, or community
post is `EARLY_SIGNAL` or `COMMUNITY_SENTIMENT` until its bounded subject is the discussion itself or a
stronger source corroborates the factual claim. Decision-critical release claims should connect to
official docs, releases, repositories, changelogs, or product pages when available. A financial, stock,
or market-moving fact must not become final `FACT` from one social post; prefer filings, company IR,
official releases, regulator/exchange records, or authoritative datasets. Deleted/inaccessible posts and
screenshots without reproducible provenance remain limited/unverified.

## 5. Deterministic `PROVENANCE_OUTPUT_GATE`

Run this gate after rendering and again after any refresh/revision:

1. Parse every declared access field. Reject blank, placeholder, date-only canonical values, invalid
   timezone, values outside the recorded execution window, and example/stale hardcoded values.
2. For each material source, require either a reproducible locator with a non-fabricated observed origin,
   or `UNAVAILABLE_WITH_LIMITATION` plus a non-empty limitation and source identity.
   When the primary route failed, also require an observed retrievable alternate route or an explicit
   no-alternate limitation plus a narrowed claim.
3. Resolve every material claim's source keys to unique register records. Reject missing or duplicate keys.
4. Resolve every source key visible in client output to the delivered register. Reject internal-only
   pointers and a report that neither embeds nor explicitly names the register component.
5. Reject any locator marked or inferred as generated, guessed, reconstructed, or silently filled.
6. Enforce the social/community role, account, publication-time, claim-boundary, corroboration, and
   evidence-state fields when that source class is material and the surface exposes them. Missing values
   remain explicitly `NOT_STATED` or `UNAVAILABLE_WITH_LIMITATION`; they are never invented.
7. On refresh/revision, compare the prior record by `source_key`. Locator identity, access/publication
   history, source role, contradiction state, evidence state, and claim ceiling are append-preserved.
   A change requires new revision metadata and evidence; silence may not promote or erase a state.

Gate output is `PASS` only when all checks pass. Otherwise output `FAIL` with stable reason codes:

```text
ACCESS_VALUE_INVALID
ACCESS_OUTSIDE_EXECUTION_WINDOW
LOCATOR_OR_LIMITATION_MISSING
LOCATOR_ORIGIN_UNTRUSTED
MATERIAL_LOCATOR_NOT_RETRACEABLE
CLAIM_SOURCE_KEY_UNRESOLVED
CLIENT_SOURCE_KEY_UNRESOLVED
CLIENT_REGISTER_NOT_VISIBLE
SOCIAL_PROVENANCE_INCOMPLETE
REVISION_PROVENANCE_REGRESSION
```

Do not deliver a client report while the gate is `FAIL`. Fix the record or narrow the claim and expose
the limitation; never make up metadata to obtain `PASS`.
