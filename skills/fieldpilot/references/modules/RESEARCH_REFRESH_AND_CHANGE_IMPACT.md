# Research Refresh & Change Impact Runtime — v1.7

This module governs **user-triggered updates to an existing FieldPilot market-research baseline**. It extends the existing append-auditable revision, dependency, lifecycle, provenance, and claim-ceiling model. It is not an always-on monitor, scheduler, alerting service, or deterministic trend forecaster.

For v1.9.1, every affected client-facing revision passes
`references/modules/CLIENT_VISIBLE_EVIDENCE_PROVENANCE.md`. Preserve the prior source key, locator identity,
access/publication history, source role/character, contradiction state, evidence state, and claim ceiling.
Append a new revision/access observation; do not overwrite history, silently promote evidence, or drop a
locator limitation. Re-run `PROVENANCE_OUTPUT_GATE` and `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`
(`references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md`) against the revised report and register.

## 1. Trigger and scope

Activate this module when a returning user asks to update prior FieldPilot research, asks what changed since a prior report, or asks to recheck only what matters now. Examples include:

- `이전 시장조사 업데이트해줘`
- `지난 보고서 이후 뭐가 바뀌었어?`
- `경쟁사·가격 중 중요한 것만 다시 확인해줘`

Do not activate a delta workflow merely because time has passed. A refresh is an explicit current-run research action.

## 2. Valid baseline gate

A refresh requires a trustworthy `ResearchBaseline` that can identify, at minimum:

- the prior report/logical report object and pinned revision;
- the prior audit/state snapshot or equivalent dependency record;
- the market/product scope and active decision context being refreshed;
- the source/evidence revisions that supported material prior findings or recommendations.

If these cannot be established well enough to compare old and new evidence, do **not** fabricate continuity or call a new report a delta. Explain the missing baseline and route to a safe full-research fallback or a bounded fresh check with an explicit `NO_VALID_BASELINE` limitation.

A baseline is not invalid merely because some inputs are stale. Staleness is a reason to revalidate the affected dependency, not a reason to discard all history.

## 3. ResearchBaseline and selective refresh plan

Use the existing universal object envelope and revision-pinned `depends_on` edges. The refresh planner starts from the active decision, material claims/findings, service-vs-market assessment, and recommendations, then walks **only recorded dependencies that could change the current decision**.

A dependency is a candidate for revalidation when at least one applies:

- its lifecycle is `STALE`, its `revalidation_status` is `REQUIRED`, or its declared freshness/volatility window has expired;
- the user supplies a credible change signal about it;
- a source is corrected, retracted, contradicted, or no longer accessible in a way material to the claim;
- it is a volatile current fact (for example competitor status, price/plan, packaging, positioning, channel availability, or material market/platform condition) whose current value can alter an active conclusion;
- a changed upstream object makes a downstream claim or recommendation potentially invalid.

The v1.7.2 market-intelligence objects are refreshable dependencies on exactly these tests, with no
new refresh behaviour and no new artifact: `SUCCESS_CASE_SET`, `COMPARATOR_SET` and `TREND_STATE`
(see `references/modules/`). They are selected for revalidation only when decision-relevant, and they
are classified through the same change vocabulary in section 4. A stale `TREND_STATE` is worse than
an absent one because it reads as current, so a trend state carried forward without recheck is
reported as `STALE_UNRESOLVED` rather than silently reused.

The v1.9.0 commercial layer also registers `MATERIAL_CLAIM`, `LIVE_SOURCE_OBSERVATION`,
`NORMALIZED_DATA_ROW`, `TABLE_OR_CHART`, `DELIVERABLE_COMPONENT`, and `RECOMMENDATION` dependencies.
On refresh, follow only recorded edges from changed/stale source observations or returned REAL evidence to
affected claims, representations, components, and recommendations. Re-render affected bundle components and
issue a delivery/revision note; do not regenerate an unchanged report/deck/data package merely because another
component changed. See `references/modules/COMMERCIAL_DELIVERABLE_SYSTEM.md` and
`references/modules/ZERO_COST_LIVE_SOURCE_LADDER.md`.

Do **not** automatically re-run stable historical evidence, the whole source registry, the historical 14-file research corpus, unrelated market sections, or every competitor. Record what was intentionally not rechecked and why it was not decision-relevant.

## 4. RefreshCheck and change classification

Each revalidated dependency produces a `RefreshCheck` with the prior pinned object/revision, current source/check, check time, materiality assessment, and downstream action.

Use these business-facing change states:

- `NEW` — newly eligible evidence or a newly relevant entity/fact enters the active scope;
- `CHANGED` — the underlying decision-relevant fact or evidentiary meaning materially differs from the baseline;
- `RECONFIRMED` — a current recheck supports the baseline fact/claim within the same material scope;
- `STALE_UNRESOLVED` — a material current claim requires revalidation but cannot now be resolved defensibly;
- `NO_LONGER_APPLICABLE` — the old dependency or claim no longer belongs to the active product/market/decision scope.

Also record `change_materiality: MATERIAL | NON_MATERIAL_METADATA | UNKNOWN`.

A timestamp update, page-layout change, URL redirect, source metadata correction, or formatting change **does not by itself make the underlying business fact `CHANGED`**. Record metadata lineage separately. Unless semantic evidence changes, the business-facing result remains `RECONFIRMED`, `NO_LONGER_APPLICABLE`, or `STALE_UNRESOLVED` as appropriate.

If an inaccessible or conflicting source prevents a responsible current conclusion, use `STALE_UNRESOLVED`; never copy the old value forward as if newly verified.

## 5. Competitor / pricing / material-trend delta lens

For decision-relevant volatile market evidence, compare the prior and current observations without turning every market fact into a trend claim. Where applicable capture:

| Lens | Minimum comparison |
|---|---|
| Competitor | entity/status, offer, target/job, material feature/positioning, evidence dates |
| Pricing | plan/package, billing cadence, original currency, amount/range, eligibility/limits, source/access date |
| Packaging / positioning | material promise, included/excluded value, target/buyer shift |
| Distribution / channel | availability, access constraints, platform/channel rule changes material to the active route |
| Material trend | bounded prior/current observations, relevant period/scope, source quality, alternative explanations |

For each row preserve `prior_observation`, `current_observation`, source/revision pointers, `change_state`, `change_materiality`, and the dependencies potentially affected. Do not infer a durable trend from one new datapoint or deterministic future movement from a delta.

Cross-currency comparisons, current platform facts, source characterization, and comparable-case claims remain governed by the v1.6.1 provenance and claim-ceiling rules.

## 6. Change Impact Map

A detected difference matters only through its dependency path. Build a `ChangeImpact` record that maps:

```text
changed/new/stale dependency
→ affected Proposition / EvidenceCalibration / Finding
→ affected service-vs-market assessment or Interpretation
→ affected Recommendation / DecisionUpdate
```

For every material or unresolved change record:

- changed object/revision and exact reason;
- affected downstream object/revisions;
- whether the old support still stands, narrows, weakens, strengthens, or fails current revalidation;
- whether a new claim gate or analysis is required;
- whether direct primary evidence remains unchanged, newly required, or no longer required.

Staleness propagates only through recorded dependency edges. A price change for competitor A must not stale an unrelated customer-behavior finding merely because both appear in the same report.

## 7. Recommendation Stability

Every material recommendation in a refresh receives one of:

- `UNCHANGED_AFTER_REVALIDATION`
- `CHANGED`
- `WEAKENED`
- `STRENGTHENED`
- `NOT_CURRENTLY_REVALIDATABLE`

The state is not a score. It must name the revalidated or changed dependencies that justify it and explain why the recommendation changed **or why it stayed stable**.

`UNCHANGED_AFTER_REVALIDATION` is a positive research result only when the relevant decision-changing dependencies were actually rechecked or remained valid under the dependency contract. It must not mean “we did nothing and assumed the old advice still holds.”

`NOT_CURRENTLY_REVALIDATABLE` is required when a recommendation materially depends on unresolved stale evidence and no safe narrower recommendation can be supported.

## 8. Delta report contract

Default bounded refresh output:

`MARKET_RESEARCH_DELTA_REPORT.md`

Recommended structure:

```text
# Market Research Delta Report
## 1. Baseline Identity and Validity
## 2. Refresh Question / Active Decision
## 3. What Was Revalidated — and What Was Intentionally Reused
## 4. Revalidated Sources and Evidence
## 5. Competitor / Pricing / Material-Trend Deltas
## 6. Change Impact Map
## 7. Recommendation Stability
## 8. Stale / Unresolved Dependencies
## 9. Findings Changed, Reconfirmed, or Retired
## 10. Direct-Research / Provenance Status
## 11. Sources and Audit / Revision Pointers
## 12. Limitations and Claim Ceilings
```

The report must distinguish `NEW / CHANGED / RECONFIRMED / STALE_UNRESOLVED / NO_LONGER_APPLICABLE`. It must also state the bounded search/revalidation scope so “not rechecked” is not confused with “unchanged.”

## 9. History-preserving revision behavior

A refresh never silently overwrites a prior report or audit snapshot.

- Keep the baseline report/revision addressable and unchanged.
- Materialize the delta as a new report object/revision with audit events linking it to the baseline.
- New/revalidated evidence creates new evidence/source revisions; historical observations retain their original dates and support state.
- If a prior claim is no longer current, mark the new state and point to the superseding revision; do not edit the historical wording in place.
- This governs the historical record. The live `EXECUTIVE_DECISION_LAYER` itself is a different surface and
  follows the stricter rule in `references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md` §1: it is rewritten
  to the current verdict, not annotated in place while the superseded verdict stays the primary read. Do not
  satisfy this section's history-preservation requirement by leaving the old executive answer live with a
  pointer forward — preserve it in the dated history subsection instead.

If the user explicitly asks for a fully refreshed report, or enough core claims materially changed that a delta alone would mislead a reasonable reader, create a **new `FINAL_MARKET_RESEARCH_REPORT` revision** and a superseding notice that names the prior report revision. Preserve the prior report as historical evidence. Do not replace it silently.

## 10. Direct research and provenance regression boundary

Refresh mode does not relax the v1.6.1 product contract:

- FieldPilot still performs web/desk/official/existing-source/AI-resolvable research itself when tools are available.
- A residual real-world evidence gap still uses `EVIDENCE GAP → METHOD OPTIONS → USER CHOICE / SKIP → CUSTOM KIT` when multiple defensible methods exist.
- `PLANNED`, `TO_COLLECT`, `EXAMPLE_ONLY`, QA rows, simulated/model-derived material, and a prior recommendation never become `REAL` human/observed evidence merely because a refresh occurred.
- `instrument_health` / `measurement_health` remain instrumentation and signal-integrity states, not participant clinical health.
- User-returned REAL evidence keeps raw provenance and receives a new auditable revision before it affects findings/recommendations.

## 11. Full-refresh escalation rule

Escalate from a bounded delta to a new full-report revision only when at least one is true:

1. the user explicitly requests a fully refreshed report; or
2. multiple core decision-bearing claim groups have materially changed such that a delta report would force the reader to reconstruct the current market state from incompatible old/new fragments; or
3. the old market/product scope itself is no longer the active scope.

This is a qualitative, auditable decision based on affected dependencies. Do not invent a universal percentage or numeric threshold for “enough changes.”

## 12. Out-of-scope boundary

v1.7 Research Refresh is **not**:

- background polling or always-on monitoring;
- scheduled alerts or notifications;
- automatic scraping on a timer;
- deterministic prediction of future competitor moves or trends;
- a new monetization, negotiation, recruiting, travel, discount, resume, or viral-content product.

Those capabilities require separate approval and architecture. This module only governs an explicit refresh run initiated in the current interaction.
