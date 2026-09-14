# PROFESSIONAL_DELIVERY_ENVELOPE + RESEARCH_QA_AND_AI_DISCLOSURE

Mandatory end matter for every customer-facing FieldPilot research deliverable: full report, delta
report, and any standalone deliverable a user could reasonably treat as professional research output.

FieldPilot is presented as professional market research. A report that is methodologically useful but
opaque about how it was produced, what was verified, what AI did, and whether any human reviewed it,
fails professional buyer expectations regardless of how good its findings are.

The envelope is **compact by default**. It is disclosure, not ceremony. Executive readers get a short
block; the technical detail sits in the appendix.

## 1. Envelope contents

```text
ENV-01  agreed brief                     frozen CLIENT_DECISION_BRIEF: decision, owner/user, objective,
                                         material questions
ENV-02  scope                            scope_in as delivered
ENV-03  exclusions                       scope_out, plus anything a reader might expect but did not get
ENV-04  assumptions                      every INFERRED/ASSUMED brief field and working assumption, labeled
ENV-05  method-selection rationale       why these methods/source classes were fit for these questions
ENV-06  source-selection rationale       inclusion/exclusion rules actually applied
ENV-07  coverage rationale               population/segment/geography/time actually covered, and not
ENV-08  evidence-state definitions       the labels used, defined in the deliverable itself
ENV-09  provenance register              per material claim where feasible: source, publication date,
                                         access date, and a claim pointer to the supporting location
ENV-10  limitations                      what this deliverable cannot support
ENV-11  unknowns                         questions left UNKNOWN or PARTIAL, and why
ENV-12  causal boundaries                where association is not causation for this evidence
ENV-13  AI / synthetic / tool disclosure truthful, stage-by-stage; see section 3
ENV-14  human oversight & accountability truthful; see section 4
ENV-15  freshness QA                     recency checks actually run and their outcome
ENV-16  dedup QA                         duplicate/reprint collapsing actually performed
ENV-17  inclusion / exclusion QA         how candidate evidence was admitted or rejected
ENV-18  verification QA                  what was independently checked against a primary source
ENV-19  sample QC                        when applicable: eligibility, frame, n or saturation rationale,
                                         recruitment, exclusions, invalid-response handling
ENV-20  fieldwork QC                     when applicable: execution controls and deviation log
ENV-21  ethics boundary                  when applicable
ENV-22  privacy boundary                 when applicable
ENV-23  confidentiality boundary         when applicable
ENV-24  reproducibility notes            what an independent party needs to re-run or re-check this
ENV-25  traceability notes               the claim-to-source convention used in this deliverable
ENV-26  source discovery record          how the evidence was found and selected, not only what was
                                         cited; see references/modules/SOURCE_DISCOVERY_AND_SELECTION.md
ENV-27  evidence independence profile    independence classes actually held, and
                                         INDEPENDENT_EVIDENCE: SEARCHED_NOT_FOUND where that is the
                                         honest outcome for a market-structure claim
ENV-28  research timing log              when substantive research actually started and ended, or
                                         NOT_LOGGED with its reproducibility consequence
ENV-29  prospective research ethics      when a people-involving method is recommended or selected:
                                         the PARTICIPANT_RESEARCH_DESIGN_ETHICS scaffolding and
                                         truthful fieldwork status; see
                                         references/modules/RESEARCH_ETHICS_DESIGN_SCAFFOLDING.md
ENV-30  AI client-material confidentiality  the actual controls over AI processing of client-supplied
                                         material, or NONE / UNKNOWN; never an invented control
ENV-31  regulatory context state         MATERIAL_AND_CHECKED / MATERIAL_BUT_GEOGRAPHY_UNRESOLVED /
                                         MATERIAL_BUT_NOT_VERIFIABLE_NOW / NOT_MATERIAL with reason
```

### Applicability

`ENV-19` through `ENV-23` are marked `NOT APPLICABLE` when no primary research, no participants and no
confidential material were involved — and marking them `NOT APPLICABLE` is itself the required
disclosure. Silence is not an acceptable rendering of an inapplicable control.

`ENV-29` applies whenever the deliverable **recommends** research involving people, even if none was
executed. A desk-only run that proposes interviews or workplace observation is not exempt: the
executed work is `NOT APPLICABLE` for `ENV-19` to `ENV-23`, while `ENV-29` carries the ethics
scaffolding of the proposed design with `fieldwork_status: NOT_EXECUTED`. Those are different
statements and both are required.

`ENV-30` is always rendered when any client-supplied material was processed. `NONE` and `UNKNOWN` are
legitimate answers and are frequently the truthful ones. Stating a control that did not actually
apply to this run is a fabrication in the same class as a fabricated source.

Every other envelope item is always rendered. When an item has nothing to report, say so explicitly
(`NONE`, `NOT PERFORMED`, `NOT APPLICABLE`) rather than omitting the line.

## 2. Findings -> Interpretation -> Recommendations separation

The deliverable keeps three layers visibly distinct:

```text
FINDINGS          what the evidence shows, at the coverage state it actually has
INTERPRETATION    what FieldPilot reads into it, with rival explanations and confidence
RECOMMENDATIONS   what to do, bounded by the claim ceiling of the findings above
```

A recommendation may not be stronger than the evidence that supports it. Where interpretation carries
the weight, say that it is interpretation.

## 3. AI / synthetic / tool-use disclosure (ENV-13)

State, truthfully, which stages were AI-assisted and how:

```text
query planning / search strategy
retrieval and tool use
source screening and selection
extraction from sources
synthesis across sources
inference and interpretation
report drafting
synthetic or AI-generated data, if any was used at all
```

Rules:

- Disclose the **actual** execution mode of this run. If the run was a contract replay, a demonstration,
  a partial execution, or a desk-only pass, say exactly that.
- Never present AI-generated, simulated or synthetic material as observed real-world evidence. If no
  synthetic data was used, state that it was not used rather than leaving it ambiguous.
- Distinguish what was **independently verified against a source** from what is **model synthesis or
  inference**. This distinction is required, not optional.
- Tool use that materially affected sampling, retrieval, analysis or interpretation is disclosed. Tool
  use that did not is not padded in for appearance.
- Disclosure never becomes a disclaimer that excuses a weak claim. It sits alongside claim ceilings; it
  does not replace them.

## 4. Human oversight and accountability disclosure (ENV-14)

This is the control most likely to be filled with comfortable fiction. It must not be.

Permitted oversight states — record only what actually happened:

```text
NONE                        no human reviewed the substantive content of this deliverable
USER_DECISION               the user made specific in-run choices (e.g. method choice, SKIP, scope);
                            record which choices, and note that choosing is not reviewing
USER_SUPPLIED_EVIDENCE      the user executed real-world research and returned REAL evidence;
                            record what they returned; this is not a review of FieldPilot's analysis
INDEPENDENT_HUMAN_REVIEW    a named or role-identified human independently reviewed the content;
                            record who, what they reviewed, and when
```

Absolute prohibitions:

- **Never fabricate** a human reviewer, a professional sign-off, a QC pass, a certification, a
  qualification, an accreditation, an expert validation, participant consent, an ethics approval, a
  respondent, a fieldwork event, or a verification that did not occur.
- Do not describe FieldPilot's own self-audit, exit check, or internal consistency pass as human review,
  professional QC, or independent verification. Machine self-checking is disclosed as machine
  self-checking.
- Do not use passive constructions — "was reviewed", "was verified", "has been checked", "확인되었다",
  "검토되었다" — to imply a human actor who does not exist. Name the actor or use the state label.
- `NONE` is a legitimate, professional, and frequently correct answer. Report it plainly. An honest
  `NONE` is worth more than an invented sign-off, and inventing one is a material misrepresentation.
- Accountability: state who is accountable for acting on this deliverable. For an AI-produced report
  with `NONE` oversight, the accountable party is the user/decision owner, and the deliverable says so.

## 5. QA controls (ENV-15 to ENV-18)

Report the QA that was **actually run**, with its outcome — not a list of QA that would be nice to have.

```text
freshness      which time-sensitive facts were re-checked, when, and what changed
dedup          which apparently distinct sources collapsed into one origin
inclusion      the admission rule applied, and what it excluded
verification   which claims were checked against a primary/first-party source, and the result
```

A QA control that was not run is recorded as `NOT PERFORMED`, with the effect on claim ceilings. Listing
an unrun check as performed is a fabrication in the same class as a fabricated source.

## 6. Reproducibility and traceability (ENV-24, ENV-25)

- An independent reader must be able to locate the basis of any material claim: source identity,
  publication date, access date, and where in the source the claim comes from, wherever that is feasible.
- Where a claim pointer is not feasible (paywalled, dynamic, offline, or a synthesis across many
  sources), say so for that claim rather than fabricating a precise locator.
- Record enough method detail that an independent party could re-run the same research approach and
  understand why they might reach a different answer.
- For v1.9.1, render a visible source key beside every material numeric, comparative, or decision-relevant
  claim and resolve it to the delivered evidence register. Access values are actual execution-time RFC 3339
  timestamps, never blanks, placeholders, copied examples, or stale hardcoded dates. A source exposes its
  observed direct locator or an explicit truthful locator limitation; the runtime never invents a URL.
- Apply `references/modules/CLIENT_VISIBLE_EVIDENCE_PROVENANCE.md` and require `PROVENANCE_OUTPUT_GATE: PASS`
  before delivery and after every refresh/revision.
- For v1.9.3, this "before delivery and after every refresh/revision" requirement is universal, not
  provenance-only: every applicable delivery gate the runtime already defines — `PROVENANCE_OUTPUT_GATE`,
  `LOCAL_PAID_SUBSTITUTE_ANCHOR_GATE`, `RETRACEABLE_LOCATOR_FALLBACK_GATE`, `VALIDATION_RESOLUTION_GATE`,
  `LITERATURE_HIERARCHY_COMPLETENESS_GATE`, and `DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`
  (`references/modules/BOUNDED_DELIVERY_QUALITY_REPAIR.md`) — must PASS or reach a defined non-fabricating exit
  state before *any* customer-facing deliverable ships, not only a "substantial commercial engagement bundle."
  A single continuous `FINAL_MARKET_RESEARCH_REPORT` reply is a customer-facing deliverable and is not exempt.
  A gate that is `NOT_APPLICABLE` to the active decision is fine; a gate that was simply never checked is a
  delivery-gate bypass and blocks delivery.
- For v1.9.4, "wired" means loaded, not merely named: a delivery gate or reference module a task's routing
  marks as triggered must carry a `LOADED_AND_APPLIED` record (or a reasoned
  `NOT_APPLICABLE_TO_THIS_DECISION` record) before delivery. Reporting that a module was covered because
  the governing-layer summary already mentions it is the same delivery-gate bypass as never checking the
  gate at all — see `MODULE_LOAD_NO_SKIP_GATE`
  (`references/modules/BOUNDED_BEHAVIORAL_CLOSURE_REPAIR.md` §1). The same module additionally requires, before
  any customer-facing deliverable ships: `DIRECT_COMPETITOR_RECALL_CLOSURE` before a "no strong direct
  competitor"/whitespace-class claim; `COMMERCIAL_EVIDENCE_TAXONOMY_GATE`, which names the actual evidence
  rung (`LISTED_PRICE` / `ACTIVE_OFFER` / `PREORDER_OFFER` / `OBSERVED_PURCHASE` /
  `OBSERVED_REPEAT_PURCHASE_OR_RETENTION` / `PROVEN_WTP`) for any commercial claim rather than a binary
  overclaim check; `CURRENT_STATE_PRICING_FRESHNESS_HIERARCHY` for third-party pricing rows in a current
  comparison table; and `SINGLE_NEXT_ACTION_CONTRACT` when the user explicitly asked for exactly one final
  next action.

## 7. Rendering

- Executive rendering: a short disclosure block covering brief/scope/exclusions, evidence states, AI and
  human-oversight status, key limitations, and where the full envelope lives.
- Technical rendering: the complete envelope, in the deliverable's appendix.
- Reuse the existing provenance, evidence-class, execution-mode and limitation fields already produced
  by the run. Do not build a parallel governance subsystem, and do not restate the same content three
  times in different words.
- Boilerplate is a defect. Each envelope item describes **this** run.
- For v1.9.5, once `FINAL_MARKET_RESEARCH_REPORT.md` carries this envelope and has passed
  `PROVENANCE_OUTPUT_GATE`/`DELIVERY_CONSISTENCY_AND_CURRENCY_GATE`/
  `BOUNDED_BEHAVIORAL_CLOSURE_REPAIR`, render it via `PROFESSIONAL_REPORT_RENDERING_CONTRACT`
  (`references/modules/RENDERING_CONTRACT.md`) into `report.html` and, when a local browser is
  available, `report.pdf`. The renderer's `renderer_consistency_gate` must PASS before either
  file ships — a render that drops or alters a material bold-labeled sentence, evidence/status
  token, numeric value, or source URL is the same delivery-gate bypass as skipping any other
  envelope check, and blocks delivery the same way.
- For v1.9.6, the canonical Markdown additionally marks a `## CUSTOMER_DECISION_REPORT` part
  (opening with the plain-language what/decision/why/next-action summary) separate from a
  `## AUDIT_METHOD_PROVENANCE_APPENDIX` part carrying internal gate names, package-internal
  file paths, YAML implementation blocks, and version-regression history
  (`references/modules/BUYER_FACING_DECISION_REPORT.md`). `render_report.py` renders both with
  different visual hierarchy; its `buyer_facing_structure_gate`, `overlap_overclaim_gate`, and
  `practical_feasibility_gate` must also PASS before either file ships, with the same
  hold-not-ship consequence as any other envelope check.

### Client-facing register — translate state, never drop the disclosure

Internal runtime and state tokens do not belong in client-facing prose. They carry no meaning for a
client and momentarily turn a deliverable into a system log.

The fix is **translation, not deletion**. The information those tokens carry is usually a genuine
professional disclosure, and removing it to tidy the register converts a disclosure into an
omission — a worse defect than the one being repaired.

```text
DIRECT_RESEARCH_STATUS: SKIPPED_BY_USER
  -> "You chose not to run the direct research at this stage, so the questions below remain
      untested rather than answered. That is recorded as untested, not as a negative result."

DIRECT_RESEARCH_STATUS: NOT EXECUTED (scope-bounded, not a user skip)
  -> "No direct research was carried out in this engagement because it was outside the agreed
      scope. This is different from you having declined it."

METHOD_CHOICE_STATUS: PENDING
  -> "You have not yet chosen a research method, so no execution materials were produced."

COVERAGE_STATE: PARTIAL
  -> "This question is partly answered: <what is known>, while <what is missing> is still open."

INDEPENDENT_EVIDENCE: SEARCHED_NOT_FOUND
  -> "We looked for independent third-party evidence on this and did not find any, so this rests
      on the companies' own published material."
```

Rules:

- Every state that carries client-relevant meaning is rendered in plain language somewhere the
  client will read it.
- **Deleting the underlying disclosure is prohibited.** If a token is removed, its meaning is
  stated in prose in the same place.
- Machine-readable state may still be persisted internally and may appear in a clearly labelled
  technical appendix. It does not appear mid-sentence in the client-facing body.
- This rule is about register, not about candour. It never licenses softening an unfavourable
  status, and it never converts an unfavourable state into a favourable phrasing.

## 8. Failure modes this module exists to prevent

- a professional-looking report that never says AI produced it;
- an implied human expert who does not exist;
- QA checklists that describe intentions rather than executed checks;
- claims with no traceable basis;
- exclusions and assumptions that only exist inside the model's head;
- disclosure boilerplate so generic it is identical across unrelated engagements.

## 9. Rule and source anchors

Rule anchors: `R-AI-01`, `R-AI-02`, `R-AI-03`, `R-AI-04`, `R-AI-05`, `R-AI-06`, `R-ETHICS-01`,
`R-ETHICS-02`, `R-SOURCE-01`, `R-CLAIM-01`, `R-AUDIT-01`, `R-FIR-01`.
Source anchors: `S-ESOMAR`, `S-ISO-20252`, `S-MRS-AI`, `S-NIST-GENAI`, `S-AAPOR-DISC`.

ICC/ESOMAR and ISO establish professional duties to disclose methodology, data sources and material
AI/emerging-technology roles including the extent of human oversight. The exact envelope item list,
labels and rendering rules above are FieldPilot operational contracts, not quotations of those standards,
and conformity with any external standard is not claimed.
