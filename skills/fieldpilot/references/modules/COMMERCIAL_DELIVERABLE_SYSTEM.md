# Commercial Deliverable System — v1.9.0

This module compiles the existing FieldPilot research, evidence, case, trend, primary-research, and
refresh controls into a professional client delivery system. It adds no parallel research method and
does not weaken any evidence state, claim ceiling, negative-evidence rule, or direct-research choice.

For v1.9.1, every rendered bundle also passes
`references/modules/CLIENT_VISIBLE_EVIDENCE_PROVENANCE.md`. This is the mandatory final gate for actual
access timestamps, source locators or truthful locator limitations, client-visible source-key resolution,
source role/character, evidence state/claim ceiling, public social/community provenance, and revision safety.

For v1.9.2, applicable pricing, retraceability, validation-plan, and literature-characterization paths also
pass `references/modules/BOUNDED_BEST_OF_AI_DISTILLATION.md`. These are four bounded additions, not permission to
expand a brief, hunt broadly, invent a price/sample size, or weaken an existing evidence control.

## 1. Commercial engagement contract

For a substantial full-market-research engagement, produce a coherent `CLIENT_DELIVERABLE_BUNDLE`,
not one undifferentiated chat or markdown wall. The bundle is proportional to the decision and may be
materialized as separate files or as clearly delimited components in one content package.

```text
CLIENT_DELIVERABLE_BUNDLE
  EXECUTIVE_DECISION_BRIEF
  FINAL_MARKET_RESEARCH_REPORT
  COMPETITOR_AND_CASE_MATRIX
  EVIDENCE_AND_SOURCE_REGISTER
  DATA_TABLE                         when structured research data exists
  PRIMARY_RESEARCH_KIT               when selected and required
  ACTION_AND_VALIDATION_PLAN
  EXECUTIVE_DECK or EXECUTIVE_DECK_OUTLINE when decision-relevant
  DELIVERY_AND_REVISION_NOTE
```

Each component records `bundle_id`, `as_of`, active decision, scope, revision, evidence dependencies,
and its actual materialization state. A missing optional component carries a reason; it is never silently
omitted merely because the runtime cannot render a preferred file format.

The `FINAL_MARKET_RESEARCH_REPORT` must contain visible source keys beside material claims and either embed
the source appendix or name the delivered `EVIDENCE_AND_SOURCE_REGISTER` component exactly. The register is
client-visible; an internal runtime/state pointer is not an acceptable substitute.

## 2. DQ-1 / DQ-2 — executive-first architecture and narrative

The first one to two pages/slides of a substantial package answer, in plain client language:

1. the decision and direct answer;
2. current recommendation and confidence/conditions;
3. strongest opportunity and strongest risk;
4. the decisive evidence and counterevidence;
5. why now or why not now; and
6. the immediate next action or validation.

The default report narrative is:

```text
DECISION / SCOPE / ASSUMPTIONS
→ MARKET / CUSTOMER / DEMAND
→ COMPETITION / PRICING / CHANNEL
→ SUCCESS AND NEGATIVE CASES / DISCRIMINATING FACTORS
→ USER-CASE GAP / OPPORTUNITY / RISK
→ FEASIBILITY / RECOMMENDATION
→ ACTION / VALIDATION / PRIMARY-RESEARCH HANDOFF
→ LIMITATIONS / FALSIFIERS
→ EVIDENCE / SOURCE / DATA APPENDIX
```

The report is finding-led, not template-led. Omit a genuinely inapplicable topic with a stated reason;
do not break this decision narrative with generic methodology education.

## 3. DQ-3 / DQ-4 / DQ-5 — decision representations and visible evidence

Use a table or chart when it reduces decision time. Applicable representation primitives include:

- competitor / substitute and normalized price-package matrix;
- customer segment / job / barrier table;
- success-vs-failure case and factor matrix;
- positioning map only when both axes and placements are evidence-supported;
- risk / opportunity matrix;
- prioritized action and evidence-gap / validation matrix; and
- trend chart only when comparable observations, units, periods, and provenance support it.

Every material table or chart has a finding-led title, one decision message, a short
`SO WHAT / IMPLICATION`, and source keys/date on the same page or an unambiguous pointer. A chart
specification contains:

```yaml
chart_id:
finding_headline:
decision_question:
chart_type_and_why:
data_columns:
axis_unit_denominator_period:
series_and_segment:
source_keys_and_dates: []
transformations_and_assumptions: []
contradictions_or_missingness:
claim_state_and_ceiling:
so_what:
rendering_suppression_rule:
```

If the data do not support the visual, suppress it and use a bounded evidence table or `UNKNOWN`.
Decorative charts, invented precision, unlabeled normalization, and prose pasted onto slides fail this
contract.

For deck-style delivery apply **One Page/Slide One Message**: a conclusion-led headline, one supporting
visual/table, a short implication, and traceable source/date. The `EXECUTIVE_DECK_OUTLINE` uses exactly
those fields even when a deck file cannot be rendered.

## 4. DQ-6 — reusable data handoff

When research creates a structured dataset, deliver a reusable `DATA_TABLE` in a format the runtime can
actually create, or a complete exportable schema/table when it cannot. Preserve at minimum:

```text
record_id | entity_or_case | metric_or_field | raw_value | raw_unit
normalized_value | normalized_unit | geography_segment_period
source_key | source_locator | source_date | access_date_time
retrieval_route | transformation | assumption | evidence_state
contradiction_state | notes_limitations
```

Raw observations remain distinguishable from normalized or derived values. Every transformation is
reproducible; missing values stay missing. Do not claim that CSV/XLSX/Sheets or another data artifact
exists until it was created and read back or otherwise verified.

## 5. Artifact capability negotiation — render truthfully or fall back professionally

Before promising DOCX, PDF, PPTX, XLSX, Google Docs/Slides/Sheets, or an equivalent artifact, run an
`ARTIFACT_CAPABILITY_AUDIT`:

```yaml
requested_or_decision_useful_formats: []
available_creation_tools: []
available_verification_tools: []
component_format_plan: []
artifact_state: RENDER_AND_VERIFY | STRUCTURED_CONTENT_FALLBACK
unsupported_formats_and_reason: []
```

- `RENDER_AND_VERIFY`: use the host's actual document, presentation, spreadsheet, or PDF capability;
  create only the useful components; then verify the returned file identity, non-emptiness, expected
  sections/sheets/slides, and readable/rendered output in proportion to the format.
- `STRUCTURED_CONTENT_FALLBACK`: provide the complete professionally structured report, matrices,
  exportable data schema/table, exact chart specifications, and executive deck outline. State that the
  preferred binary/native files were not materialized in this runtime.

Tool availability changes the rendering route, never the research content floor. Transport success or
a claimed filename is not verification. Never invent a file, public link, visual inspection, or format
conversion that did not occur. Do not hard-depend on a paid design service or paid external API.

## 6. Primary-research kit and returned-data ingestion

The existing `EVIDENCE GAP → METHOD OPTIONS → USER CHOICE / defensible combination / SKIP → CUSTOM KIT`
contract remains governing. A selected `PRIMARY_RESEARCH_KIT` is executable and includes the applicable
participant/sampling/recruitment criteria, screener, interview/FGI/survey/test instrument, consent and
ethics notes, observation/coding sheet, analysis plan, and decision thresholds or qualitative decision
rules. Planned materials never become evidence.

When the user returns actually collected interview notes, survey exports, test logs, transaction evidence,
or field notes, run `RETURNED_RESEARCH_INGESTION`:

```text
1. create an ingestion manifest: file/source identity, collector, collection window, consent/access basis,
   method/version, population/sample, and REAL vs PLANNED/EXAMPLE_ONLY/QA state;
2. preserve raw input separately and hash or revision-pin it where the host permits;
3. validate schema, missingness, duplicates, exclusions, deviations, measurement health, and sample reach;
4. apply the pre-specified coding/analysis plan; disclose any post-hoc change;
5. separate observation, finding, interpretation, and recommendation;
6. reconcile contradictions with desk/web evidence and search negative/disconfirming observations;
7. update coverage states, claim ceilings, case/gap/action rows, and WHY NOW only where the returned data
   supports the change;
8. issue new affected component revisions plus a delivery/revision note; preserve the prior package.
```

If fieldwork did not occur, use `NOT PERFORMED` or `SKIPPED_BY_USER`, keep the proposition `UNKNOWN`, and
lower dependent recommendations. FieldPilot never claims it recruited, interviewed, moderated an FGI,
or collected field data without verified execution evidence.

## 7. DQ-7 / DQ-8 — editorial professionalism and proportional depth

Use a consistent title hierarchy, terms, labels, units, time basis, geography, source keys, and evidence
states across every component. Prefer concise client language, aligned comparison fields, and short
finding-led sections. Translate runtime states without deleting their meaning.

A bounded question remains concise. A substantial commercial brief receives the information density of a
professional 15–30-page report class where the evidence and decision warrant it, without page-count padding.
Completeness is assessed by the decision path, representations, evidence visibility, and unresolved gaps—not
by word or page count.

## 8. DQ-9 / DQ-10 — delivery manifest and bounded revision

`DELIVERY_AND_REVISION_NOTE` records:

```yaml
delivered_components: []
component_revisions_and_formats: []
as_of_and_scope:
material_limitations_and_unknowns: []
artifact_capability_limitations: []
fieldwork_status:
one_bounded_revision_pass:
revision_inputs_required: []
evidence_state_change_rule:
superseded_components: []
```

One bounded correction/revision pass may fix factual inputs, calculation, wording, layout, or scope agreed
with the client. It may change a conclusion only when new/corrected evidence justifies the change. It may
not promote evidence, erase contradictions, or raise a claim ceiling to please the client. Prior revisions
remain addressable.

## 9. FieldPilot +alpha and reproducible refresh

The bundle exposes, rather than hides:

- `FACT / SUPPORTED INFERENCE / UNKNOWN / RECOMMENDATION` for material claims;
- success-vs-failure factor discrimination and alternative explanations;
- evidence gap → executable experiment/fieldwork design;
- freshness, market velocity, decision horizon, and WHY NOW;
- source/date/role/contradiction and coverage state; and
- dependency records that identify what must be refreshed later.

Register material claim, source observation, normalized data row, table/chart, deliverable component, and
recommendation dependencies. A later refresh follows those edges and re-renders only affected components.
This is reproducible refreshability, not an always-on monitor.

## 10. Bundle exit check

Before delivery, verify structurally:

1. the executive answer is visible before the appendix;
2. the narrative reaches action and limitations rather than stopping at collected facts;
3. applicable matrices/specifications exist and every material visual is source/date traceable;
4. the bundle is not a single unbroken response for a substantial brief;
5. data handoff is reusable when structured data exists;
6. artifact generation and verification claims match actual host capabilities;
7. returned REAL data can be ingested through a documented path;
8. the delivery note exposes limitations and revision boundaries; and
9. no evidence state, negative evidence, claim ceiling, or human/fieldwork status was fabricated; and
10. `PROVENANCE_OUTPUT_GATE` passed against the rendered report and delivered evidence register, including
    execution-window access timestamps, unique source-key resolution, locator truth, social/community claim
    ceilings when applicable, and append-preserved provenance across revisions; and every gate triggered
    under §11 below also resolved (`PASS`/applicable exit state, not skipped).

## 11. v1.9.2 bounded decision-utility gates

Apply only the gates triggered by the active decision:

1. A pricing/WTP question passes `LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE`: the client sees verified local paid
   direct/indirect substitute packages, the proposed price is positioned against them, and any suggested bracket
   is explicitly an unmeasured experiment. If anchors are unavailable, the bounded search and evidence loss are
   visible and no price is invented.
2. A material failed primary locator passes `RETRACEABLE_LOCATOR_FALLBACK_GATE`: it has an observed retrievable
   alternate route, or a no-alternate limitation plus a narrowed client claim. Do not call a source retraceable
   merely because a URL string exists.
3. A recommended validation passes `VALIDATION_RESOLUTION_GATE` before it is called executable: count/range,
   duration/opportunity window, metrics, and decision rules are resolved with method/context rationale, or the
   plan remains `PROPOSED_NOT_READY` with a named resolution rule or owner.
4. A literature-wide characterization passes `LITERATURE_HIERARCHY_COMPLETENESS_GATE`: an eligible synthesis
   is represented with the relevant individual evidence, or a bounded `SYNTHESIS_SEARCHED_NOT_FOUND` record
   keeps the claim study-specific.
5. (v1.9.3) The bundle passes `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`
   (`references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md`): no unresolved cross-report numeric/entity/unit/
   scope conflict, no stale self-referential product-state claim, no undisclosed sale-mode mismatch or WTP
   overclaim, and the executive layer carries exactly one current verdict with any superseded conclusion
   moved to history rather than left live.

The existing competitor/case matrix, plain-client-language, negative-evidence, regulatory, ethics,
STOP/MODIFY/CONTINUE, claim-state, and source-key rules remain mandatory regression constraints.
