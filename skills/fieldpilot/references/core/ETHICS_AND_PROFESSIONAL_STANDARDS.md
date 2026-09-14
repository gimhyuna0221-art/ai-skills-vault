# Ethics and Professional Standards — Runtime Contract

Runtime reference for FieldPilot v1.5.0. Load this module before stage/dependency
routing on every turn, before recruitment, during fieldwork changes, and before
reporting or evidence reuse. It operationalizes the continuous Safety/Ethics
Interrupt and is a prerequisite for `EthicsReview`, `AccessReality`,
`ReadinessDecision`, and every compiled reporting view. `AI_AND_SYNTHETIC_RESEARCH.md`,
`AUDIT_STATE_SCHEMA.md`, `SAMPLE_AND_FIELDWORK.md`, and every method card depend on
the risk-state and protection contracts defined here.

This module implements `R-ETHICS-01`, `R-ETHICS-02`, `R-REG-01`, `R-FNB-01`, and the
professional-duty intersection of `R-AI-04` and `R-AI-06`. Rule class, maturity,
enforcement, scope, and source links are defined in `EXPERT_CORE_RULES.md`.

## 1. Continuous ethics interrupt

The interrupt is a kernel-order invariant: it runs before dependency/stage routing,
before recruitment, during fieldwork changes, and before reporting/reuse — it is
step 1 of every turn, ahead of loading active objects and the rules snapshot. It is
never optional and never deferred to a later stage.

The runtime MUST interrupt for concrete indications of:

- absent or invalid consent, deception without justified review/debriefing,
  coercion, or undisclosed non-research purpose;
- minors, impaired consent, vulnerable/dependent relationships, distress,
  self-harm, abuse, or safeguarding risk without an adequate plan;
- unlawful or unnecessary personal/sensitive data collection, insecure handling,
  prohibited transfer, or re-identification risk;
- physical, food, product, medical, financial, or operational safety risk;
- missing adverse-event, product-complaint, mandatory-reporting, or escalation
  procedure in an applicable regulated context;
- undisclosed AI interaction or material AI use;
- recruitment or research being used as disguised sales, promotion, fundraising,
  or lead transfer;
- fabricated evidence, synthetic material represented as human, selective
  suppression, or unsupported conclusions.

The interrupt MAY: set or change a risk state; name the required mitigation, owner,
and reviewer; block the affected fieldwork action or output only; request the
missing fact; escalate to qualified human review; require a `DecisionUpdate` or
`EthicsReview` revision before proceeding.

The interrupt MUST NOT: make a definitive legal determination when jurisdiction or
applicability is uncertain; silently reclassify a risk state without an audit
event; substitute for qualified legal, regulatory, or ethics review; allow
`approval_status` to resolve or clear a risk state; or let a favorable outcome
retroactively excuse a missed trigger.

## 2. Risk states — state machine

```text
GREEN   proceed with ordinary documented controls
AMBER   proceed only after named mitigation/owner/review is complete
RED     stop fieldwork/output and escalate to qualified human review
UNKNOWN treat as AMBER or RED when the missing fact changes permission or harm
```

| Field | Requirement |
|---|---|
| `reason` | Concrete trigger from Section 1, stated in plain language. |
| `owner` | Named human accountable for mitigation or escalation. |
| `required_mitigation` | The specific action, control, or review that resolves the state. |
| `evidence_of_resolution` | Artifact or confirmation showing the mitigation occurred. |
| `reviewer` | Named human who signed off the resolution, required for `AMBER` and `RED`. |

State transitions:

- `GREEN` is the only state that permits ordinary fieldwork/output to proceed
  without a named mitigation and reviewer.
- `AMBER` blocks the affected action until mitigation, owner, and review are
  recorded; it does not block unrelated independent work.
- `RED` blocks fieldwork/output entirely for the affected scope and requires
  escalation to qualified human review before any downgrade.
- `UNKNOWN` is never treated as `GREEN`. It resolves to `AMBER` or `RED` based on
  whether the missing fact would change permission or harm if answered
  unfavorably; the choice and rationale are recorded.
- Every transition is a new `EthicsReview` revision with an audit event; a prior
  `GREEN`/`AMBER` finding is never silently reused after a material condition
  changes (new population, jurisdiction, data type, participant group, or AI use).

## 3. Minimum participant protections (`R-ETHICS-01`)

These protections apply to research that is **executed**. When a deliverable *recommends* or
*offers* a method involving people — interviews, surveys, workplace observation, usability or
concept tests, paid continuation tests — the same protections MUST be carried into the proposed
design and shown to the client with the method, not deferred to whoever eventually runs it. The
design-field contract, the workplace/power-asymmetry record, the AI client-material
confidentiality disclosure, and the rules for secondary use of identifiable public posts are in
`references/modules/RESEARCH_ETHICS_DESIGN_SCAFFOLDING.md`. Those are design and disclosure fields
only: an unexecuted design records a truthful `fieldwork_status` and is never retro-filled as
though fieldwork occurred.

All participant research MUST address:

- voluntary participation and a comprehensible purpose;
- sponsor/researcher identity and material conflicts as required;
- what participation involves, recording/transcription, foreseeable risks,
  incentives, and data use;
- right to skip questions and stop or withdraw participation at any time without
  penalty; explain separately any lawful, consented limits on deleting data
  already irreversibly anonymized or incorporated into non-reidentifying
  aggregates, without limiting cessation of participation;
- data minimization, access, retention/deletion, confidentiality/anonymization
  limits, and third parties;
- accessibility, language, cultural fit, and additional protections for
  children/vulnerable participants;
- separate, specific permission for follow-up, marketing, or non-research use;
- debriefing and support/escalation when deception or distress is possible.

Applicable legal obligations override this minimum. The implementation MUST
version applicable standards and jurisdictional rules rather than freezing a
global legal checklist. `S-AAPOR-CODE`, `S-ESOMAR`, and `S-BELMONT` establish the
professional/ethical baseline; local duties vary and are not assumed satisfied by
this baseline alone.

## 4. Research-versus-sales separation (`R-ETHICS-02`)

Keep research separate from sales, promotion, fundraising, and lead transfer
absent separate, specific consent. This applies at recruitment, during fieldwork,
and in reporting/follow-up:

- recruitment materials and screening MUST NOT function as a disguised sales
  pitch or lead-generation funnel;
- participant contact data and responses MUST NOT be transferred to sales,
  marketing, or fundraising functions without a separate, specific permission
  distinct from research consent;
- an interviewer, moderator, or AI system MUST NOT convert a research
  interaction into a promotional or transactional one without stopping to obtain
  that separate consent first;
- detecting disguised sales, promotion, fundraising, or lead transfer during
  research is a Section 1 interrupt trigger and defaults to at least `AMBER`,
  escalating to `RED` if it is already in progress without consent.

Local privacy and marketing law may add duties beyond this separation
(`S-AAPOR-CODE`, `S-ESOMAR`).

## 5. Professional transparency (`R-DESK-01`-adjacent, `13.4`)

Research reports MUST disclose enough for a competent reader to assess fitness for
purpose:

- sponsor/purpose when appropriate;
- population/frame/sample/recruitment;
- method/mode/dates;
- instrument/stimuli;
- weighting/modeling;
- quality controls;
- limitations;
- AI/synthetic use;
- conflicts.

Findings, Interpretations, Recommendations, and unsupported client/model
preferences MUST remain distinguishable objects; a disclosure list does not
replace the `R-FIR-01` separation.

This disclosure duty is grounded in `S-ESOMAR` (professional fitness,
transparency, participant care, AI disclosure, and reporting duties),
`S-AAPOR-CODE` (voluntary participation, transparency, integrity, and the
research/non-research and human/AI-generated-data distinctions), `S-AAPOR-DISC`
(human/AI source, sample, instrument, method, processing, oversight, and
precision disclosure elements), and `S-ISO-20252` (quality/service requirements
within the current edition's scope — check the active edition rather than
assuming a frozen year). None of these sources proves any one method superior, and
a disclosed design is not thereby representative or valid.

Where research intersects a regulated or vulnerable-subject context, `S-BELMONT`
(respect, beneficence, justice) and `S-CIOMS` (health-related research ethics,
vulnerable groups, oversight) inform the professional duty even outside their
originating scope; applicability outside that scope is `INFERRED` and requires the
Section 6 procedure. Pharmaceutical and adjacent regulated market research follows
`S-EPHMRA` adverse-event/product-complaint responsibilities where applicable.

## 6. CONDITIONAL_HARD applicability evaluation procedure

`R-REG-01`, `R-FNB-01`, and `R-AI-04` are `CONDITIONAL_HARD`: enforcement depends
on an applicability finding, not on the underlying research being universally
established. Evaluate applicability with the same procedure as
`EXPERT_CORE_RULES.md`'s enforcement protocol item 2, applied to ethics/regulatory
scope:

1. Identify the candidate `CONDITIONAL_HARD` rule triggered by the current
   decision, proposition, population, domain, or fieldwork action.
2. Record the facts: jurisdiction, domain/sector, participant classification,
   data type, and any regulated/sensitive-context indicators from Section 1.
3. Record the conclusion source: `USER_CONFIRMED` (a named authoritative source
   or the user's confirmed instruction) or `INFERRED` (the runtime's own
   determination). A model-derived applicability conclusion is `INFERRED`, never
   self-confirming, regardless of how confident the output reads.
4. Record the reviewer: required whenever the conclusion is `INFERRED` and the
   stakes are material; optional only when the user supplies an authoritative,
   sourced confirmation.
5. Set the risk state per Section 2 using the recorded facts, source, and
   reviewer; `INFERRED` applicability alone does not license `GREEN`.
6. If a required module, rule, or source record is missing, block only the
   affected expert claim or fieldwork action and state the nearest valid repair,
   per `EXPERT_CORE_RULES.md`'s enforcement protocol item 3.
7. If a jurisdiction, regulation, or applicability conclusion later changes,
   re-run this procedure; it creates a new `EthicsReview` revision and MUST NOT
   silently carry forward the prior conclusion.

`R-REG-01` applies this procedure to jurisdiction, classification, consent/review,
safeguarding, privacy, and reportable events before regulated or sensitive
fieldwork (`S-CIOMS`, `S-EPHMRA`, `S-BELMONT`). `R-FNB-01` applies it to
applicable food-safety, allergen, licensing, and operational constraints before
food/beverage fieldwork or claims (`S-FDA-FOOD`; jurisdiction-specific). `R-AI-04`
applies it to AI-moderation disclosure/consent, exact-system pilot, provenance,
and human oversight/escalation as a professional duty (`S-MRS-AI`, `S-ESOMAR`,
`S-AI-INTERVIEWER`); see `AI_AND_SYNTHETIC_RESEARCH.md` for the full moderation
audit rubric. `R-AI-06` is `HARD`, not conditional, and requires logging material
AI use and named human responsibility at every research phase regardless of
jurisdiction (`S-MRS-AI`, `S-ESOMAR`, `S-NIST-GENAI`, `S-UNESCO-AI`).

## 7. Not a substitute for qualified review

FieldPilot does not substitute for qualified legal, regulatory, or ethics review.
Jurisdiction applicability is `INFERRED` unless the user confirms it or it is
sourced to an authoritative, versioned reference. The runtime MUST NOT make a
definitive legal determination when jurisdiction or applicability is uncertain; it
names the required qualified review or safe route instead (mirroring the Method
Router's `ETHICS_OR_LEGAL_BLOCK` outcome). A user's confirmation of applicability
is recorded as `USER_ASSERTED` context for the ethics review; it does not itself
verify the underlying legal fact, and it does not advance `verification_status` on
any linked claim.

## 8. Source and maturity hooks

- `R-ETHICS-01`: Class C / ESTABLISHED / HARD; `S-AAPOR-CODE`, `S-ESOMAR`,
  `S-BELMONT`. Applicability details vary; the professional baseline is direct.
- `R-ETHICS-02`: Class C / ESTABLISHED / HARD; `S-AAPOR-CODE`, `S-ESOMAR`. Local
  privacy/marketing law may add duties.
- `R-REG-01`: Class C / ESTABLISHED / CONDITIONAL_HARD; `S-CIOMS`, `S-EPHMRA`,
  `S-BELMONT`. Domain/jurisdiction rules control.
- `R-FNB-01`: Class C / ESTABLISHED / CONDITIONAL_HARD; `S-FDA-FOOD`.
  Jurisdiction-specific; not global law.
- `R-AI-04` (professional-duty intersection): Class C / SUPPORTED /
  CONDITIONAL_HARD; `S-MRS-AI`, `S-ESOMAR`, `S-AI-INTERVIEWER`.
- `R-AI-06` (professional-duty intersection): Class C / SUPPORTED / HARD;
  `S-MRS-AI`, `S-ESOMAR`, `S-NIST-GENAI`, `S-UNESCO-AI`.

**Escalate/stop:** on `RED`, stop the affected fieldwork/output immediately and
escalate to qualified human review; do not resume until mitigation evidence and a
named reviewer sign-off are recorded as a new `EthicsReview` revision. On
`UNKNOWN` where the missing fact changes permission or harm, treat as `AMBER` or
`RED` — never `GREEN` — and block only the affected action until the fact is
resolved. Never let `approval_status`, a favorable result, or an `INFERRED`
applicability conclusion substitute for the mitigation, reviewer, or qualified
review this module requires.
