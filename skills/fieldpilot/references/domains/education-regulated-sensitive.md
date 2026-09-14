# Domain Adapters — Education, Regulated/Sensitive, and Unfamiliar Industry

Runtime reference for FieldPilot v1.5.0. Load this module during Domain Preflight
(Section 9), after the Required Evidence Contract is compiled and before a
`MethodDecision` is finalized. Adapters ADD required fields, units, roles, and claim
restrictions on top of `PROPOSITION_AND_EVIDENCE.md`, `METHOD_ROUTER.md`, and the
method cards in `methods/`. They never weaken core inference or ethics rules. They
compose: an education marketplace sold to school districts can activate `EDUCATION`,
`REGULATED_SENSITIVE`, `ENTERPRISE`/`B2B_BUYING_SYSTEM`, and `TWO_SIDED_MARKETPLACE`
at once (Section 18), and `UNFAMILIAR_INDUSTRY` can precede any of these when the
relevant structural module is not yet identifiable.

## `EDUCATION`

- **activation_signals:**
  - the product or service is used in a learning context: learners, teachers,
    courses, curriculum, or schools are involved;
  - the project proposes engagement, completion, or satisfaction as evidence of
    a learning outcome;
  - minors are participants, or a school/institution controls access.
- **mandatory_preflight_fields:**
  - learner, parent/guardian, teacher, administrator, institution, and
    payer/procurement roles;
  - the learning construct definition and its assessment validity;
  - classroom/school clustering;
  - implementation fidelity;
  - accessibility;
  - delayed transfer of learning;
  - minors/privacy/approval requirements.
- **unit_and_role_model:**
  - units: the individual learner, and the classroom/school as a nested cluster
    that affects independence assumptions in analysis;
  - roles: learner, parent/guardian (consent authority for minors), teacher
    (implementer), administrator/procurement (buyer), and the institution
    (deployment context);
  - a teacher's satisfaction speaks to adoption and usability, not to a learning
    outcome; engagement data from one learner does not represent
    classroom-clustered effects, and one classroom does not represent the
    school.
- **required_evidence_additions:**
  - an explicit learning construct and a validated assessment instrument for
    that construct;
  - classroom/school clustering handled in sampling and analysis, consistent
    with the interference logic in `R-EXP-04`;
  - an implementation-fidelity log (was the intervention delivered as
    designed?);
  - accessibility accommodations;
  - delayed/transfer-of-learning measurement when the claim extends beyond
    immediate performance;
  - the minors' consent/privacy basis, resolved before recruitment.
- **method_router_effects:**
  - engagement and completion evidence routes to `BEHAVIORAL_ANALYTICS` only,
    and is reported as engagement/completion, not learning;
  - a learning-effect claim requires `AB_RANDOMIZED_EXPERIMENT` or
    `QUASI_EXPERIMENT` with a valid learning-outcome instrument, correct
    clustering, and bounded generalization, consistent with `S-WWC`; not every
    exploratory education question requires a randomized design;
  - `PROTOTYPE_USABILITY` and `OBSERVATION_CONTEXTUAL` remain sufficient for
    usability/comprehension propositions that do not claim a learning effect;
  - `REGULATED_SENSITIVE` activates automatically whenever minors' data or
    consent is involved.
- **domain_claim_gate:**
  - satisfaction, use, engagement, completion, and educator adoption do not
    establish learning;
  - a learning causal claim needs an eligible outcome measure, an eligible
    design, correct unit-of-analysis handling, and bounded generalization.
- **composition_notes:**
  - composes with `ENTERPRISE`/`B2B_BUYING_SYSTEM` for school/district
    procurement, with `REGULATED_SENSITIVE` for minors and privacy, and with
    `TWO_SIDED_MARKETPLACE` for education marketplaces; the school-marketplace
    example in Section 18 shows all of these active together without any one
    weakening another;
  - the ethics/legal constraint from `REGULATED_SENSITIVE` always wins over an
    adoption or procurement narrative (Section 20.6).
- **rule_and_source_ids:** `R-EDU-01`; `S-WWC`.

**Escalate/stop:** if a learning-outcome claim is proposed from engagement or
completion data alone, block and rewrite to the bounded engagement/completion
finding (Section 16.3, `CG-EDU-01`). If minors' consent/privacy basis is
unresolved, pause fieldwork under `REGULATED_SENSITIVE` before any data
collection from learners.

## `REGULATED_SENSITIVE`

- **activation_signals:**
  - the domain is healthcare/pharmaceutical, financial services, government/public
    sector, or otherwise carries a named regulator, professional code, or
    reporting duty;
  - participants include minors, vulnerable populations, or people in a
    dependent relationship with the researcher/sponsor;
  - the research touches personal, health, financial, or otherwise sensitive
    data.
- **mandatory_preflight_fields:**
  - jurisdiction;
  - classification;
  - regulator/authority;
  - allowed claims;
  - consent basis;
  - vulnerable groups;
  - required ethics/legal review;
  - privacy/retention/transfer constraints;
  - safety escalation path;
  - adverse/reportable events;
  - vendor obligations.
  - All of the above are resolved before recruitment begins, not during
    fieldwork.
- **unit_and_role_model:**
  - units: the individual participant and the case/event (an adverse event or a
    reportable incident) when applicable;
  - roles: participant/patient/subject, guardian (for minors or impaired
    consent), regulator/authority, qualified reviewer, and a named safeguarding
    owner;
  - a market-preference respondent supplies preference evidence only; that
    evidence never becomes a clinical, compliance, or safety fact by itself.
- **required_evidence_additions:**
  - the applicable law/code/standard, with jurisdiction, effective/version date,
    and applicability basis; mark `QUALIFIED_REVIEW_REQUIRED` when applicability
    cannot be established (Section 9.2, 18.2);
  - a consent basis appropriate to the vulnerable or sensitive population
    involved;
  - a safeguarding and reportable-event pathway with a named owner;
  - privacy, retention, and cross-border transfer constraints;
  - vendor/third-party obligations relevant to sensitive data handling.
- **method_router_effects:**
  - every candidate method card's `ethics_privacy_and_escalation` field is
    treated as `CONDITIONAL_HARD` and blocking under this adapter, not merely
    advisory;
  - `HUMAN_DEPTH_INTERVIEW`, `PROBABILITY_SURVEY`, `NONPROBABILITY_SURVEY`, and
    every other candidate method may proceed only after the preflight fields
    above are resolved;
  - `SECONDARY_DESK` on the applicable regulatory text is mandatory before any
    other fieldwork step;
  - `AI_MODERATED_INTERVIEW` additionally requires the `R-AI-04` disclosure and
    escalation path plus this adapter's named safeguarding owner; AI is never
    the sole safeguarding layer for distress, abuse, self-harm, minors, impaired
    consent, or reportable events (Section 13.1, 14.4).
- **domain_claim_gate:**
  - if applicability, reporting, safeguarding, or safe-collection status is
    unresolved, fieldwork pauses (`CONDITIONAL_HARD` under `R-REG-01`);
  - preference evidence does not establish clinical efficacy, safety,
    compliance, or regulatory approval.
- **composition_notes:**
  - when this adapter is active alongside any other adapter in this file set —
    `EDUCATION` plus minors, `FOOD_BEVERAGE` plus licensing, `ENTERPRISE` plus
    data residency — its ethics/legal constraint always wins over the other
    adapter's evidence-design convenience, per Section 20.6; it is never
    weakened by a business-side adapter.
- **rule_and_source_ids:** `R-REG-01`, `R-ETHICS-01`; `S-CIOMS`, `S-EPHMRA`,
  `S-BELMONT`.

**Escalate/stop:** if jurisdiction, classification, consent basis, safeguarding,
or reportable-event path is unresolved, pause affected fieldwork
(`CONDITIONAL_HARD`) and route to `QUALIFIED_REVIEW_REQUIRED` or
`ETHICS_OR_LEGAL_BLOCK`. Do not let a decision-owner's urgency or a favorable
preference signal substitute for the missing review.

## `UNFAMILIAR_INDUSTRY`

- **activation_signals:**
  - FieldPilot or the user cannot confidently name the relevant actors, roles,
    regulators, KPIs, or terminology for this market;
  - domain-specific jargon appears without a working definition;
  - no other domain adapter in this specification clearly and confidently
    applies yet.
- **mandatory_preflight_fields:**
  - a sourced glossary and system map;
  - actors, transactions, incentives, and workflow;
  - value/risk transfer;
  - authority;
  - economics;
  - standards/regulators;
  - seasonality;
  - data generation;
  - alternatives;
  - disputed assumptions;
  - built using multiple independent sources and domain informants, not one
    convenient source.
- **unit_and_role_model:**
  - the unit and role model is undetermined by default; it is discovered
    per-project through the glossary/system-map work rather than imported from a
    superficially similar familiar domain;
  - a domain informant's account is evidence about that domain, not automatic
    validation of an imported framework or role list.
- **required_evidence_additions:**
  - a sourced glossary of the market's own terms;
  - a system/workflow map showing how value and information move;
  - an actor/incentive map;
  - an inventory of applicable regulators/standards;
  - an explicit, visible list of imported assumptions and analogies with their
    validation status.
- **method_router_effects:**
  - `SECONDARY_DESK` and `HUMAN_DEPTH_INTERVIEW` with domain informants are
    required before the method router makes any admissibility decision;
  - other domain adapters may activate only once their own triggering
    conditions are independently confirmed in this market; they are never
    activated by analogy to a familiar domain alone;
  - `MARKET_SIZING` and `SEGMENTATION` must not reuse a familiar domain's unit,
    formula, or category structure without re-deriving it for this market.
- **domain_claim_gate:**
  - familiar analogies remain hypotheses;
  - do not import another domain's role taxonomy, sample rule, KPI, conversion
    rate, regulatory status, or evidence threshold without validation in this
    market.
- **composition_notes:**
  - this adapter is provisional: once the glossary/system-map work identifies
    which other adapters actually apply (for example, discovering the market is
    B2B and regulated), those adapters take over their specific fields;
  - `UNFAMILIAR_INDUSTRY`'s hypotheses-only gate remains in force for any
    imported assumption that has not yet been independently validated, even
    after another adapter activates.
- **rule_and_source_ids:** `R-UNFAMILIAR-01`.

**Escalate/stop:** if a claim relies on an imported role, KPI, conversion rate,
or regulatory assumption from a superficially similar familiar domain without
this market's own validating evidence, block the claim and label the import a
hypothesis pending validation (Section 25). If the glossary/system map cannot be
built from available sources and informants, return `NOT_CURRENTLY_ANSWERABLE`
for propositions that depend on it.
