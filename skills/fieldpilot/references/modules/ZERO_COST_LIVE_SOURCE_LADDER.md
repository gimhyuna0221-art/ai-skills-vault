# Zero-Cost Live Source Ladder — v1.9.0

This module governs fresh decision-relevant evidence across market, pricing, competitors, customers,
trends, regulation, platforms, and vertical-specific research. It extends the existing source-discovery,
freshness, provenance, and coverage controls. It is not a command to call every available API.

## 1. Smallest sufficient zero-cost source plan

For each material current-market question, select the smallest source set that improves coverage,
freshness, corroboration, or reproducibility. Prefer, when practical and legally/technically available:

1. an official/open/free API or machine-readable public dataset within a genuinely zero-cost tier;
2. an official current webpage, feed, release, filing, or dashboard;
3. a reputable public statistical/open-data portal or current institutional report;
4. a current platform/store/ranking/review/community/search-interest signal when decision-relevant and
   permitted; then
5. ordinary public-web discovery as fallback.

For fast-moving AI, vibe-coding, developer-tool, startup/product-release, company, stock, or market questions,
the smallest useful set may include public social/community surfaces such as official or maintainer posts,
GitHub releases/issues/discussions, X/Twitter, Threads, Instagram, public Telegram channels, and lawfully
accessible public Discord/community announcements. Use `PUBLIC_SOCIAL_COMMUNITY` only through the provenance
and claim-ceiling rules in `references/modules/CLIENT_VISIBLE_EVIDENCE_PROVENANCE.md`.

This is an evidence-quality ladder, not an API quota. An authoritative official page may be preferable to
an incomplete or stale API. Do not collect irrelevant endpoints or call a free API merely because it exists.

## 2. Authorization, availability, and cost boundary

Before using an API/dataset, verify current terms, allowed use, authentication, quota, and freshness where
those facts affect the run. A source that requires a free key/account may be used only when an already
authorized usable credential exists. In other words, use an **already authorized** credential or no credential.
Never invent credentials, expose secrets, silently create an account, or start a **free trial** that can convert
to paid. New account/credential actions require user authorization.

Paid APIs, paid datasets, paid scraping services, pay-per-call runtimes, and paywalled facts are not silent
dependencies. If a decision-critical fact is unavailable at zero cost, use a defensible free proxy with its
limits or preserve `UNKNOWN / EVIDENCE_GAP`. Never fabricate precision or an API result.

### 2.1 Source-access friction rule — human-test hotfix

Source quality is not the only runtime cost. Repeated permission prompts, failed fetches, paywalls, login walls,
broken URLs, and host-level URL approval dialogs can make otherwise good research unusable. Treat user-interaction
friction as a bounded source-selection cost without weakening evidence quality.

Before opening a candidate source, classify it as far as the current host can reasonably determine:

```text
ACCESS_PREFLIGHT
  PUBLIC_NO_AUTH            public source expected to open without account/login
  HOST_URL_APPROVAL         public source, but the host may require URL/domain approval before fetch
  AUTH_REQUIRED             login/account/credential required
  PAYWALLED                 substantive evidence is behind payment
  BLOCKED_OR_FAILED         robots/network/policy/404/repeated fetch failure
  UNKNOWN                   access state cannot be known before a bounded attempt
```

Rules:

- Prefer the **smallest sufficient set of strong sources** rather than opening many equivalent pages.
- Prefer `PUBLIC_NO_AUTH` sources when they can support the same claim at the required claim ceiling.
- Do **not** deliberately open `AUTH_REQUIRED`, `PAYWALLED`, or already-known `BLOCKED_OR_FAILED` sources when an
  adequate accessible source can answer the same material question.
- A source that fails to open, returns the wrong page, requires unavailable authentication, or is otherwise
  unusable is **excluded from supporting evidence**. Record the access failure internally and move to the declared
  fallback. Do not keep retrying equivalent inaccessible sources.
- Do not ask the user to authorize a source merely because it is potentially useful. Ask only when the missing
  source is **decision-critical**, no adequate accessible fallback exists, and the user can realistically grant
  the required access. Bundle such requests into one concise request where the host allows it; never interrupt
  the user source-by-source for non-critical evidence.
- If the host itself requires confirmation before any external URL can be fetched, that security dialog is a
  **host-level control**, not proof that the source is private or invalid. FieldPilot cannot bypass it. Reduce the
  number of prompts by consolidating evidence to fewer authoritative domains/sources; never disable or evade the
  host's security controls on the user's behalf.
- If a valid public source still requires host approval, continue only to the extent needed for the smallest
  sufficient evidence set. Do not fan out to extra citations merely to increase source count.
- Never cite an inaccessible source as if its substantive content was verified. A discovered locator may be
  recorded only as an access limitation / evidence gap, not as support for the claim.

The target behavior is: **search broadly, fetch selectively, fail over silently when safe, interrupt only when
access is truly decision-critical.**

## 3. LIVE_SOURCE_PLAN and provenance

```yaml
LIVE_SOURCE_PLAN:
  material_question:
  freshness_need_and_decision_horizon:
  preferred_route: FREE_API | OPEN_DATASET | OFFICIAL_WEB | PUBLIC_STATISTICAL | PLATFORM_SIGNAL | PUBLIC_WEB
  source_or_endpoint_identity:
  why_fit_for_purpose:
  terms_auth_quota_state:
  credential_state: ALREADY_AUTHORIZED | NOT_REQUIRED | UNAVAILABLE | USER_AUTHORIZATION_REQUIRED
  access_preflight: PUBLIC_NO_AUTH | HOST_URL_APPROVAL | AUTH_REQUIRED | PAYWALLED | BLOCKED_OR_FAILED | UNKNOWN
  fallback_route:
  stop_rule:
```

Every material observation records where possible:

```text
AS_OF / ACCESS_DATE_TIME
source publication/update/observation date
geography / segment / period
endpoint, dataset, page, feed, filing, or reproducible retrieval pointer
retrieval_route: FREE_API / OPEN_DATASET / OFFICIAL_WEB / PUBLIC_STATISTICAL /
                 PLATFORM_SIGNAL / PUBLIC_WEB / USER_SUPPLIED
source role, first-party/independent class, and known bias
for public social/community sources: platform, direct post/thread/message locator, account/channel and handle,
official/independent/unverified role, publication timestamp/timezone, claim boundary, and corroboration status
terms/auth/quota state when relevant
raw unit / denominator and any normalization
freshness fit to market velocity and decision horizon
corroboration / contradiction state
durable capture or retrieval revision when available
```

An API response is evidence only if it was actually retrieved. A planned call, documentation page, or
unavailable credential is not a result. Preserve the access failure and use the declared fallback.

Fastest source wins discovery; strongest evidence wins the final claim. An official account post can prove
that the account announced something at that time. An unofficial post remains `EARLY_SIGNAL` or bounded
`COMMUNITY_SENTIMENT` unless stronger evidence supports the factual claim. A financial, stock, or other
market-moving fact never becomes final `FACT` from one social post.

## 4. Freshness and trend boundary

Use current API/open-data retrieval for fast-moving numeric/time-series/ranking/state data only when it is
materially stronger than a stale page. Use the authoritative official page/report when it is semantically
stronger or more current. Apply `references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md` before calling a change
a durable trend: one datapoint, viral post, rank move, or interest spike does not establish persistence,
breadth, behavior, or commercial relevance.

## 5. Reproducible fallback and refreshability

Persist enough non-secret retrieval state for a later rerun: material question, route, endpoint/dataset/page,
safe parameters or query, access time, source revision/date, transformation, dependency, fallback, and stop
rule. Never persist secrets. Register every material live observation as a refreshable dependency of the
claims, tables/charts, and recommendations that use it.

## 6. Failure modes

- fixed universal API list regardless of market;
- invented API response, credential, quota, or live status;
- free-trial or paid-source dependency without authorization;
- copying an old datapoint while describing it as a current retrieval;
- turning inaccessible paywalled evidence into an exact claim;
- repeatedly interrupting the user for non-critical source/domain approvals instead of using an accessible fallback;
- citing a failed, wrong, blocked, login-only, or unverified page as if its contents were retrieved;
- opening many equivalent domains when a smaller authoritative source set is sufficient;
- counting syndicated observations as independent corroboration;
- recording only final citations without a reproducible discovery/retrieval route; or
- hiding an irreducible gap instead of preserving `UNKNOWN`.
