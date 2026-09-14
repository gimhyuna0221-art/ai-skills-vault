# Audit, State, and Legacy Migration Schema — Runtime Contract

Runtime reference for FieldPilot v1.5.0. Load this module whenever a durable
object is created, revised, staled, or imported. It governs `state/` storage,
`audit/events.jsonl`, evidence lineage, dependency invalidation, and v1.4.3
legacy import. Every method module, `ETHICS_AND_PROFESSIONAL_STANDARDS.md`,
`AI_AND_SYNTHETIC_RESEARCH.md`, and every Section 19.3 compiled view depend on the
object envelope and state axes defined here.

This module implements `R-STATE-01` and `R-AUDIT-01`. Rule class, maturity,
enforcement, scope, and source links are defined in `EXPERT_CORE_RULES.md`.

## 1. Universal object envelope

Every durable object MUST carry:

```yaml
object_envelope:
  id:
  schema_version:
  created_at:
  updated_at:
  created_by:
  revision:
  depends_on: []
```

Revisions are append-auditable. A material upstream change creates a new revision
and marks dependent objects stale; it does not rewrite history.

## 2. Required core objects

| Object | Minimum content |
|---|---|
| `BusinessDecision` | owner, decision verb, options, deadline, stakes, reversibility, constraints, success consequences, current default |
| `Uncertainty` | decision link, unknown, why material, current belief, consequence if wrong, priority, resolution status |
| `Proposition` | type, subject/unit, population, construct/outcome, context, comparator, geography, timeframe, requested claim scope, disconfirming result |
| `RequiredEvidenceContract` | proposition link, minimum measurement, sampling/coverage, comparison/assignment, context, behavioral proximity, temporal, precision, replication/triangulation, provenance, ethics conditions |
| `DomainPreflight` | activated structural modules, actors/sides, unit of analysis, use environment, jurisdiction/authority, safety/sensitivity, access constraints, unresolved blocks |
| `MethodDecision` | considered methods, selected method/portfolio, fit rationale, rejected alternatives, can/cannot support, prerequisites, claim envelope |
| `SamplePlan` | target population, unit(s), frame/access source, strategy, inclusion/exclusion, subgroup needs, size rationale, recruitment/disposition plan, analysis linkage |
| `FieldworkPlan` | instrument/protocol, roles, training, pilot, setting, dates, deviations, data/QC, privacy, stop/escalation path |
| `AccessReality` | evidence-holder, access controller, channel, burden/trust constraints, disposition state, fallback routes, readiness, blocking reason |
| `EthicsReview` | active risks, applicable duty/jurisdiction basis, risk state, mitigation, owner/reviewer, consent/safeguarding/reporting readiness, decision |
| `RecruitmentEvent` | sample/access link, contact attempt, channel/time, delivered/reached state, eligibility, disposition, reason, actor/source; one event never overwrites another |
| `ReadinessDecision` | active contract/method/sample/access/ethics/fieldwork revisions, satisfied and blocked prerequisites, decision, reviewer, expiry/recheck trigger |
| `EvidenceItem` | evidence type, source/provenance, method, sample/case, raw link, context/time, human/synthetic status, quality limitations, transformations |
| `AnalysisResult` | inputs, method/code/formula, estimand or analytic aim, assumptions, missingness, sensitivity, output, uncertainty, reproducibility link |
| `NegativeCase` | evidence/claim challenged, contradictory case or missing group, rival explanation, test/status, effect on calibration |
| `EvidenceCalibration` | proposition/contract link, actual-versus-required dimension results, support state, maximum claim scope, limitations, unresolved alternatives |
| `ClaimGateDecision` | candidate claim, parsed envelope, evidence/calibration links, outcome, permitted rewrite, missing condition, rule/version snapshot |
| `NumericProvenance` | numeric claim/input link, numerator, denominator, unit/base/scope/time, source, formula/transformation, uncertainty, sensitivity, human/synthetic separation |
| `Finding` | bounded result, evidence and analysis links, allowed claim scope, uncertainty, limitations; no recommendation language |
| `Interpretation` | finding links, meaning, inferential steps, competing explanations, transfer assumptions, residual uncertainty; no new factual result |
| `Recommendation` | decision link, interpretation links, proposed action, alternatives, values/tradeoffs, cost, reversibility, risk, conditions, next uncertainty |
| `DecisionUpdate` | decision taken/deferred, owner, rationale, recommendation acceptance/deviation, review trigger |
| `ResearchBaseline` | prior report/object + pinned revision, audit/state snapshot, market/product scope, active decision context, source/evidence revision set, baseline-validity result |
| `RefreshCheck` | baseline dependency object/revision, reason for revalidation, prior observation, current check/source, check time, change state/materiality, downstream action |
| `ChangeImpact` | changed/new/stale object revision, affected downstream object revisions, impact path, support effect, required recalibration/reanalysis, rationale |
| `RecommendationStability` | recommendation revision, refresh/baseline links, stability state, changed/revalidated dependencies, rationale, next recheck condition |
| `SourceRecord` | bibliographic/source metadata, publication type, peer-review/review status, funding/conflicts, population/method/date, original-access status, access date |
| `RuleRecord` | rule ID, exact normative rule, primary source class, maturity, enforcement, applicability, transfer caveat, supporting source IDs |
| `RuleSourceLink` | rule/source IDs, A–E class relative to that rule, directness/support role, safe inference, prohibited inference, conflict/transfer note |
| `LegacyArtifact` | preserved imported path/content or governed reference, legacy schema/status, migration source/digest, extracted-object links, review state/deletion tombstone |
| `AuditEvent` | actor, action, object/revision, previous/new value, reason, timestamp, AI involvement |
| `ClientDecisionBrief` | decision to be made, decision owner/primary user, horizon/deadline, stakes/cost of a wrong decision, current hypothesis/assumptions, primary objective, material secondary research questions, scope_in/scope_out, constraints, evidence that would change the decision, intended action/choice set, desired decision effect; every field carries a provenance label `STATED / INFERRED / ASSUMED / ASKED / UNRESOLVED`; frozen before substantive collection |
| `BriefScopeChange` | brief revision, field or scope element changed, previous/new value, who requested or authorized it, reason, effect on effort and claim ceilings; appended, never overwriting the frozen brief |
| `EvidencePlanItem` | research_question link, uncertainty to resolve, method/source class, why fit for purpose, target population/source universe, unit of analysis, segment/geography/time coverage, evidence independence, known weakness/bias, triangulation partner, alternative-explanation check, sufficiency rule, stop rule; created before collection |
| `CoverageAudit` | research_question link, coverage state `ANSWERED / PARTIAL / UNKNOWN`, evidence basis, material gap/exclusion, resulting claim-ceiling effect; recomputed only for revalidated dependencies during a refresh |
| `DeliveryEnvelope` | agreed brief link, scope, exclusions, assumptions, method/source-selection/coverage rationale, evidence-state definitions, provenance register, limitations, unknowns, causal boundaries, AI disclosure link, human-oversight link, QA record links, sample/fieldwork QC links when applicable, ethics/privacy/confidentiality boundary when applicable, reproducibility and traceability notes; inapplicable items recorded as `NOT APPLICABLE`, never omitted |
| `AIDisclosure` | actual execution mode, AI-assisted stages actually used (query planning, retrieval/tool use, source screening, extraction, synthesis, inference, drafting), synthetic-data use or explicit non-use, what was independently source-verified versus model synthesis/inference, tools that materially affected sampling/retrieval/analysis/interpretation |
| `HumanOversightRecord` | oversight state `NONE / USER_DECISION / USER_SUPPLIED_EVIDENCE / INDEPENDENT_HUMAN_REVIEW`, what the human actually did, when, and the accountable party for acting on the deliverable; a state may be recorded only if that event actually occurred; machine self-audit is never recorded as human review |
| `QARecord` | QA class `FRESHNESS / DEDUP / INCLUSION_EXCLUSION / VERIFICATION / SAMPLE_QC / FIELDWORK_QC`, whether it was actually run, what it covered, its outcome, and the claim-ceiling effect when `NOT PERFORMED` |
| `ExecutiveDecisionLayer` | decision restated from the frozen brief, direct answer, 3-5 decisive insights, prioritized recommendation links, confidence and conditions, strongest counterevidence, material limitations, next verification |
| `ImpactVerification` | recommendation link, action, expected mechanism, observable metric/state, measurement context, decision check, causal caveat; a numeric threshold requires source, denominator, context and generalization limit, otherwise the check is qualitative |

## 3. Independent state axes (`R-STATE-01`)

The v1.4.3 provenance intent is preserved, but truth, approval, methodological
fit, and execution MUST NOT be conflated.

```yaml
provenance_status:
  - LEGACY_IMPORTED
  - USER_ASSERTED
  - HUMAN_PRIMARY
  - OBSERVED_SYSTEM
  - EXTERNAL_SOURCE
  - MODEL_DERIVED
  - SYNTHETIC_GENERATED

verification_status:
  - UNVERIFIED
  - VERIFIED_TO_SOURCE
  - CONFLICTED
  - NOT_VERIFIABLE

method_validity:
  - UNASSESSED
  - FIT_FOR_PROPOSITION
  - FIT_WITH_LIMITS
  - METHOD_CONFLICT
  - INVALID

execution_status:
  - PROPOSED
  - PLANNED
  - READY
  - IN_FIELD
  - COLLECTED
  - ANALYZED
  - CLOSED

approval_status:
  - PROPOSED
  - ACCEPTED
  - REJECTED

business_decision_status:
  - OPEN
  - DECIDED
  - DEFERRED
  - REOPENED

resolution_status:
  - OPEN
  - PARTIALLY_RESOLVED
  - RESOLVED
  - NOT_CURRENTLY_ANSWERABLE
```

`lifecycle_status` (Section 4) is the seventh axis: it applies to every durable
object rather than to one object family.

Axis ownership is explicit: provenance and verification apply to `EvidenceItem`,
`SourceRecord`, `NumericProvenance`, and model/user assertions; method validity
applies to `MethodDecision` and resulting calibrations; execution applies to
plans, fieldwork, evidence, and analyses; approval applies to proposed plans,
methods, interpretations, and recommendations; business-decision status applies
only to `BusinessDecision`/`DecisionUpdate`; resolution applies only to
`Uncertainty` and `Proposition`; lifecycle metadata applies to every durable
object. These axes MUST remain orthogonal — setting one MUST NOT imply a value on
another.

Transitions require an audit event and their object-specific prerequisites:

- verification may move from `UNVERIFIED` to `VERIFIED_TO_SOURCE`, `CONFLICTED`,
  or `NOT_VERIFIABLE`; reassessment is a new revision;
- method validity moves from `UNASSESSED` only after proposition/contract/domain
  review, and any later change creates a reassessed revision;
- execution ordinarily advances
  `PROPOSED -> PLANNED -> READY -> IN_FIELD -> COLLECTED -> ANALYZED -> CLOSED`;
  skipped states require a recorded imported/external-execution basis, while
  correction/rollback creates a new revision rather than falsifying history;
- `READY` requires an active `ReadinessDecision` with no blocking stale dependency
  or ethics/access condition;
- resolution may advance only from eligible calibration and FIR objects;
  `NOT_CURRENTLY_ANSWERABLE` preserves the unmet contract and may reopen on new
  access/evidence;
- `DECIDED` or `DEFERRED` requires a `DecisionUpdate`; `REOPENED` requires a named
  trigger/new uncertainty.

A user saying "yes, use interviews" may set `approval_status: ACCEPTED`; it
cannot by itself set `method_validity: FIT_FOR_PROPOSITION`, advance
readiness/execution/resolution, verify a fact, or indicate that interviews
occurred.

### v1.7 research-refresh reuse

A user-triggered research refresh reuses this same revision/dependency graph. `ResearchBaseline`, `RefreshCheck`, `ChangeImpact`, and `RecommendationStability` are ordinary durable objects under the universal envelope; they do not create a second lifecycle system. A refresh starts from a pinned prior report/audit snapshot, follows only decision-relevant recorded dependencies, and appends new revisions/events. Metadata-only changes do not become business-fact changes without semantic evidence. If no trustworthy baseline can be identified, the runtime must not fake a delta relationship.

### v1.7.1 professional-controls objects

`ClientDecisionBrief`, `BriefScopeChange`, `EvidencePlanItem`, `CoverageAudit`, `DeliveryEnvelope`, `AIDisclosure`, `HumanOversightRecord`, `QARecord`, `ExecutiveDecisionLayer` and `ImpactVerification` are ordinary durable objects under the same universal envelope. They add no second lifecycle system and no new approval authority.

Binding rules:

- The frozen `ClientDecisionBrief` is an upstream dependency of every `EvidencePlanItem`, `Finding`, `Interpretation` and `Recommendation` in the run. A material brief change creates a new brief revision and marks those dependents stale exactly like any other upstream change; it never rewrites the frozen brief in place.
- `CoverageAudit` is an input to `EvidenceCalibration` and to claim ceilings. It never overrides them: an `ANSWERED` coverage state cannot lift a claim ceiling that the evidence class itself does not support.
- `AIDisclosure`, `HumanOversightRecord` and `QARecord` are records of **events that actually occurred**. Writing an oversight state, a QA pass, a consent, a participant, a fieldwork event or a verification that did not happen is a fabrication in the same class as a fabricated `EvidenceItem`, and `AuditEvent.AI involvement` must reflect the real execution mode.
- `NONE` / `NOT PERFORMED` / `NOT APPLICABLE` are valid, expected terminal values. Absence of a record is not equivalent to any of them; the record is still written.
- `ImpactVerification` may not introduce a numeric threshold that has no `NumericProvenance`. Without provenance the decision check is qualitative.

## 4. Dependency invalidation and stale propagation

At minimum, these changes MUST mark dependent records stale:

- business option, deadline, or stakes change;
- proposition type, population, unit, construct, comparator, context, time, or
  requested scope changes;
- required-evidence dimensions change;
- a domain preflight module activates or a jurisdiction/safety constraint
  changes;
- sampling frame, assignment unit, outcome definition, instrument, method, or
  analysis plan changes;
- material fieldwork deviation, missingness, instrumentation failure, or source
  correction occurs;
- evidence is reclassified as synthetic, conflicted, ineligible, or withdrawn.

Staleness MUST propagate only through recorded dependencies and MUST be explained
to the user.

Each dependency edge MUST pin `object_id`, `revision`, and relationship. Durable
objects also carry `lifecycle_status: ACTIVE | STALE | SUPERSEDED | WITHDRAWN |
DELETED`. On revision, the runtime traverses only edges pinned to the superseded
revision, recomputes whether each dependent remains valid, and appends either
`REMAINS_ACTIVE` with rationale or `STALE` with the changed condition. A later
object may never silently follow "latest" state without a new audit event.

```yaml
dependency_edge:
  object_id:
  revision:
  relation:
  required_for_readiness: true | false

lifecycle_metadata:
  lifecycle_status:
  stale_reason_rule_ids: []
  stale_at:
  superseded_by_revision:
  revalidation_status: NOT_REQUIRED | REQUIRED | PASSED | FAILED
  revalidated_against: []
```

`STALE`, `SUPERSEDED`, `WITHDRAWN`, or `DELETED` inputs are excluded from
readiness and new claim support unless an explicit rule permits historical
comparison. Revalidation creates an event and a new active revision; it never
clears history in place. A source metadata update alone does not rewrite an old
result. A changed/retracted source, changed rule, or changed applicability
creates a new rule snapshot, identifies affected objects through
`RuleSourceLink` and dependency edges, and sets `revalidation_status: REQUIRED`
or `lifecycle_status: STALE` according to the rule's declared invalidation
effect. Past reports retain their original snapshot and receive a superseding
notice rather than silent revision.

## 5. Storage model

The implementation MUST keep machine-valid state, human-readable views, raw
evidence, derived analysis, and reports separate.

```text
fieldpilot/
  project.yaml
  audit/events.jsonl
  state/
    decisions.yaml
    uncertainties.yaml
    propositions.yaml
    evidence_contracts.yaml
    domain_preflights.yaml
    method_decisions.yaml
    sample_plans.yaml
    fieldwork_plans.yaml
    access_realities.yaml
    ethics_reviews.yaml
    recruitment_events.jsonl
    readiness_decisions.yaml
    evidence_ledger.yaml
    numeric_provenance.yaml
    analysis_results.yaml
    negative_cases.yaml
    evidence_calibrations.yaml
    findings.yaml
    interpretations.yaml
    recommendations.yaml
    decision_updates.yaml
    next_uncertainties.yaml
    ai_usage.yaml
    sources.yaml
    rule_source_links.yaml
    rules_snapshot.yaml
    claim_gate_decisions.yaml
    legacy_artifacts.yaml
    migration_ledger.yaml
  evidence/
    raw/                 # write-once while lawfully retained; governed deletion leaves tombstone
    processed/           # transformations with lineage
  analysis/              # code, formulas, codebooks, outputs, diagnostics
  artifacts/             # recruitment/instrument/fieldwork tools
  reports/               # human-readable compiled views
```

The runtime MUST NOT create every file merely to appear complete. It creates or
updates the nearest dependency-ready object and one novice-readable next-action
view. Empty generated artifacts are not progress.

## 6. Audit guarantees (`R-AUDIT-01`)

- Stable IDs connect every downstream object to upstream evidence.
- Retained raw evidence is logically write-once: it is never silently edited in
  place, and corrections/exclusions are new events. Consent withdrawal,
  retention expiry, data-owner instruction, or applicable deletion/anonymization
  duty overrides retention. The system then securely deletes or irreversibly
  anonymizes the governed content, appends a non-identifying tombstone
  (`evidence_id`, scope, authority/reason, time, actor, affected derivatives),
  and recalibrates or deletes dependent material. A tombstone MUST NOT retain
  recoverable content or a re-identifying fingerprint.
- Every transformation has input IDs, code/formula or procedure, actor, version,
  timestamp, and output ID.
- Personal identifiers and sensitive raw data are stored separately with least
  access, purpose/retention controls, and deletion propagation; reports and
  ledgers use minimized data or governed references.
- Every model-generated value, default, mapping, synthesis, and recommendation
  remains model-attributed until independently verified or accepted on the
  appropriate state axis.
- User approval, source verification, methodological validity, execution, and
  claim support remain independent.
- Fieldwork deviations and excluded evidence remain visible.
- Stale records retain their historical content and reason.
- The active rules/source snapshot is versioned so a past recommendation can be
  reconstructed after methodology updates.
- AI usage and human sign-off are queryable by phase.
- Claim-gate rewrites and blocks preserve both original and proposed language.

## 7. Compiled user-facing views

The system SHOULD compile, rather than hand-maintain, these views:

- Decision Brief;
- What We Need to Learn;
- Evidence Requirement and Method Rationale;
- Domain / Access / Ethics Readiness;
- Fieldwork Kit and live disposition/status view;
- Evidence and Analysis Ledger;
- Negative Cases and Alternative Explanations;
- Findings;
- Interpretation;
- Recommendation and Decision Update;
- Next Uncertainty / Next Action;
- Methods, Sources, AI, and Limitations disclosure.

Legacy v1.4.3 numbered artifacts may be imported or exposed as aliases, but the
v1.5 canonical state is object-based. Import MUST preserve original provenance
and MUST NOT convert legacy inferences into verified facts.

## 8. Legacy state import contract (v1.4.3 → v1.5)

Import is deterministic, conservative, and idempotent. Every imported value keeps
`legacy_schema`, `legacy_path`, `legacy_record_key`, `legacy_raw_value`,
`migration_source_id`, and `migration_review_status: NOT_REQUIRED | REQUIRED |
RESOLVED`. The source ID is derived from project identity plus normalized
relative path and record key; the file/content digest records the imported
revision. Re-importing the same source digest is a no-op. A changed digest
creates a new import revision and stale review, never duplicates or overwrites
the prior import.

| Legacy state | Deterministic v1.5 mapping |
|---|---|
| `CONFIRMED` with an inspectable authorized source/raw execution link | Map actual provenance from that link and set `VERIFIED_TO_SOURCE` only after verification; preserve original label. |
| `CONFIRMED` user affirmation of a proposal/selection | `USER_ASSERTED` plus `approval_status: ACCEPTED`; verification remains `UNVERIFIED`, method/execution/resolution do not advance. |
| Ambiguous `CONFIRMED` | `LEGACY_IMPORTED`, `UNVERIFIED`, and `migration_review_status: REQUIRED`; never assume truth or approval type. |
| `PROPOSED` | Preserve proposal content and origin when known; `approval_status: PROPOSED`, `execution_status: PROPOSED`; no validity/support implication. |
| `INFERRED` | `MODEL_DERIVED`, `UNVERIFIED`; preserve inference text and dependency if recoverable; no approval/support implication. |
| `METHOD_CONFLICT` | `method_validity: METHOD_CONFLICT` with original reason and affected proposition/method; unresolved if linkage is ambiguous. |
| Legacy stale marker | `lifecycle_status: STALE`, original stale reason/time if known, and dependency review; absence of a reason sets `migration_review_status: REQUIRED`. |
| Legacy "actual" execution/result | Map to execution/evidence only when an authorized artifact/source demonstrates it; otherwise `LEGACY_IMPORTED / UNVERIFIED`. |
| Mixed legacy report | Preserve as a `LegacyArtifact`; extract candidate Findings/Interpretations/Recommendations only as separate `LEGACY_IMPORTED` objects requiring grammar/provenance review. |
| Unknown or conflicting field | Preserve raw value, set `migration_review_status: REQUIRED`, and fail closed for readiness/claim support. |

Every generated v1.5 ID is written to a migration ledger keyed to the legacy
source, so repeat import resolves to the same object/revision mapping. Import
tests MUST cover every row, partial projects, changed files, repeated import, and
conflicts between legacy files.

**CRITICAL — fail closed on ambiguous legacy `CONFIRMED`:** it MUST become
`LEGACY_IMPORTED` plus `UNVERIFIED` plus `migration_review_status: REQUIRED`, and
MUST NOT be silently upgraded into a stronger v1.5 claim — not
`VERIFIED_TO_SOURCE`, not `FIT_FOR_PROPOSITION`, not an advanced
`execution_status`, and not treated as resolving a `Proposition`. Legacy
`CONFIRMED` does not imply source-verified or method-valid; migration records
only the narrower known meaning the legacy artifact actually supports. Unknown or
conflicting legacy fields preserve their raw value verbatim (`legacy_raw_value`)
and fail closed: they MUST NOT contribute to a `ReadinessDecision` or support a
`ClaimGateDecision` until `migration_review_status` resolves to `RESOLVED`
through explicit human or sourced review.

## 8a. Candidate-patch reconciliation record (spec §20.4)

Specification §0.2 identified uncommitted candidate logic in `SKILL.md` and its
benchmark mirror (an unfinished v1.4.3 "Necessary Evidence Guard"). §20.4
requires an explicit, recorded `candidate clause -> disposition -> rule ID ->
tests` mapping before the canonical skill and mirror are deliberately changed
together. That decision is recorded here. The candidate's specific wording and
numeric examples carried no privileged status; only the concepts were assessed.

| Candidate clause | Disposition | v1.5 rule / section | Tests |
|---|---|---|---|
| Order is "cheapest **sufficient**", not "cheapest available"; difficulty changes how evidence is obtained, not what is required | ADOPTED | `R-ACCESS-01`, `R-ARCH-02`; spec §8.1 | `CORE-04/05`, `ROUTER-*` |
| Two-branch pushback handling (strength not needed → reroute; strength needed → preserve requirement, redesign access) | REVISED — generalized from 2 informal branches into the six named, logged outcomes | `R-ACCESS-01`; spec §8.1 outcomes 1–6 | `CORE-04/05` |
| Re-identify which role actually holds the required evidence | ADOPTED as a general rule; the candidate's single-industry job-title example REJECTED as a general rule and removed | `R-B2B-01`; adapter `B2B_BUYING_SYSTEM` role map | `D-B2B-01`, `CG-B2B-01` |
| Access failure is not demand failure; separate non-contact from refusal | ADOPTED and EXPANDED from 2 informal states to the full disposition enum | `R-FIELD-01`; spec §8.2 | `STATE-*`, `CORE-05` |
| Burden-reduction suggestion carrying a concrete duration ("5~10분") | REVISED — retained as a context-labeled `Class E / HEURISTIC` suggestion only; explicitly not a universal burden rule | `R-NOVICE-01`; spec §8.3 | `NOVICE-*` |

Reconciliation outcome: the candidate concepts are superseded by the v1.5
stateful guard in the kernel. The canonical skill and the benchmark mirror were
then changed together and remain byte-identical. No candidate text was silently
absorbed, auto-formatted, reset, or promoted into a stronger claim.

## 9. Compatibility and failure behavior

- Existing v1.4.3 projects MUST be importable without destructive rewriting.
- Unknown legacy fields are preserved and surfaced for mapping.
- Legacy `CONFIRMED` does not imply source-verified or method-valid; migration
  records the narrower known meaning.
- If a reference module or rule snapshot is unavailable, the runtime fails closed
  for affected expert claims and explains the missing dependency.
- If the claim compiler cannot parse a material claim confidently, it
  requests/recommends a bounded template rather than allowing an unchecked
  statement.
- If active modules conflict, the more protective ethics/legal constraint wins;
  evidence conflicts remain visible for human decision.

## 10. Source and maturity hooks

- `R-STATE-01`: Class E / HEURISTIC / HARD; native audit/control architecture.
- `R-AUDIT-01`: Class E / HEURISTIC / HARD; native implementation architecture
  informed by transparency standards (`S-ESOMAR`, `S-AAPOR-DISC`).

**Escalate/stop:** fail closed whenever a required object, revision, dependency
edge, or rule snapshot is missing or stale — block only the affected object or
claim, and state the nearest valid repair. Never let a stale, superseded,
withdrawn, deleted, or migration-pending (`migration_review_status: REQUIRED`)
input silently support a `ReadinessDecision` or `ClaimGateDecision`. A model,
default, or import mapping remains attributed to its actual axis state until
independently verified or accepted on that same axis — never promoted by
proximity to a stronger-sounding object.
