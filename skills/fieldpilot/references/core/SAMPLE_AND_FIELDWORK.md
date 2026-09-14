# Sample, Access, and Fieldwork — Runtime Contract

Load after a candidate method is admissible and before `READY`. Use with the selected method card and domain adapters. This module does not supply universal sample sizes, outreach counts, response thresholds, or interview durations.

## 1. Unit and evidence-holder compiler

Name every unit that matters: decision, analysis, assignment, observation/measurement, account/household/site/classroom/team/network cluster, person/role, event/transaction/session, and time interval. Record nesting. Repeated events from one person do not enlarge the participant denominator; users inside one account do not become independent accounts.

Map who holds the required evidence and who controls access. Distinguish user, beneficiary, payer/economic buyer, approver, gatekeeper, recommender/champion, procurement, and implementation/renewal owner only when relevant. One role cannot answer for another automatically.

## 2. SamplePlan compiler

```yaml
sample_plan:
  target_population_or_case_universe:
  unit_and_nested_structure:
  evidence_holders_and_roles: []
  frame_or_access_path:
  known_coverage_gaps: []
  sampling_strategy:
  inclusion_exclusion:
  relevant_variation_or_strata: []
  subgroup_claims: []
  planned_size_and_rationale:
  duration_or_opportunity_window:
  duration_or_window_rationale:
  replacement_or_adaptive_rules:
  expected_nonresponse_attrition:
  recruitment_dispositions: []
  analysis_link:
  claim_scope_if_achieved:
  claim_scope_if_not_achieved:
  rule_ids: []
```

Size rationale follows the estimand/analytic aim:

- qualitative: aim breadth, case specificity/diversity, theory, dialogue richness, event rarity, subgroup claims, analytic depth, negative cases, and information collected so far;
- quantitative estimate/comparison: expected prevalence/effect/heterogeneity, decision precision, clustering/design effect, multiplicity, model needs, nonresponse/attrition, and eligible frame;
- causal design: estimand, assignment unit, effect of decision interest, power/precision, clustering/interference, compliance and attrition;
- usability: task/problem-discovery aim or performance-estimation precision, representative variation, task/context coverage, prototype fidelity, and safety stakes;
- longitudinal/behavioral: recurrence/opportunity window, events per unit, identity/nesting, attrition, missing telemetry, and seasonal/lifecycle coverage.

Do not use “5 interviews validates the problem,” “large N makes it representative,” or any cross-method magic number. Quotas in opt-in recruitment only control achieved composition on selected variables.

Before a recommended validation is described as executable, apply `VALIDATION_RESOLUTION_GATE`. The
client-visible plan must resolve a justified count or range, a duration or opportunity window, the
metrics, the decision rules, and—when pricing is material—the experimental price bracket. Values may be
derived from the stated estimand, precision need, variation, event frequency, access constraints, cost,
and risk; they are never universal defaults. If a required field is still a user-owned choice, label the
plan `PROPOSED_NOT_READY`, name the owner and missing input, and do not present recruitment or launch as
ready.

## 3. Recruitment and access reality

Compile:

```yaml
access_reality:
  required_evidence_holder:
  access_controller:
  channel_and_contact_source:
  permission_to_use_source:
  burden_trust_accessibility_language_timing:
  gatekeepers_and_warm_paths: []
  incentive_source_amount_rationale:
  incentive_undue_influence_review:
  fraud_duplicate_identity_risks: []
  fallback_routes_preserving_contract: []
  readiness:
  blocking_reason:
  stop_escalation_deferral_conditions: []
```

Participation incentive, product/customer value, commercial discount, and purchase consideration are separate fields. An incentive is not demand or payment evidence. Channel, cadence, burden, timing, trust, language, accessibility, recruitment partner, or targeted role may change only while required construct and quality remain obtainable.

Use append-only dispositions:

```text
NOT_YET_CONTACTED
CONTACT_ATTEMPT_FAILED
DELIVERED_NO_RESPONSE
INELIGIBLE
REFUSED_RESEARCH
REFUSED_OFFER
SCHEDULE_FAILED
PARTIAL
COMPLETED
WITHDRAWN
QUALITY_EXCLUDED
```

No response is not refusal. Research refusal is not offer rejection. Offer refusal is bounded to the offer/role/context and may inform its own proposition. Recruitment failure is access evidence, not demand failure.

## 4. FieldworkPlan compiler

```yaml
fieldwork_plan:
  proposition_contract_method_sample_revisions: []
  instrument_protocol_stimulus_version:
  pilot_and_revision_plan:
  researcher_moderator_roles_training:
  setting_channels_dates:
  consent_privacy_retention_materials:
  secure_raw_data_location_and_access:
  safeguarding_adverse_event_complaint_reporting_path:
  quality_checks:
  deviation_log:
  stop_and_escalation_rules:
  human_escalation_for_automation:
  analysis_handoff:
```

During collection append actual dates, site/channel, version, assistance, contact disposition, missingness, exclusions, withdrawal, incident, instrumentation failure, and protocol deviation. Do not erase a deviation because the outcome is favorable. Preserve raw evidence; corrections/exclusions are new governed events.

## 5. Readiness HARD GATE

Create a revision-pinned `ReadinessDecision`. `READY` requires active approved proposition, contract, domain preflight, method decision, sample/access plan, method-appropriate instrument/protocol and pilot, consent/privacy/retention controls, role training, secure data handling, quality/deviation/stop procedures, and all applicable safeguarding/adverse/reportable-event and human-escalation paths.

Return:

- `READY`: every hard prerequisite active and satisfied;
- `AMBER`: named mitigation/owner/reviewer required before fieldwork;
- `BLOCKED_ACCESS`: the contract is preserved; redesign access, narrow by explicit revision, defer, or mark not-answerable;
- `BLOCKED_ETHICS_OR_LEGAL`: stop for qualified review or a safe lawful route;
- `STALE`: a pinned revision changed; issue a new readiness decision.

FieldPilot may prepare execution materials and audit returned evidence. It must never claim that it contacted, recruited, interviewed, observed, paid, enrolled, or executed fieldwork without verifiable authorized external evidence.

## 6. Method-linked QC and stopping

Load the selected card's explicit QC and stopping logic. Across methods:

- stop for consent withdrawal, material safety/safeguarding risk, reportable event without coverage, prohibited data handling, uncontrolled deception, or inaccessible required human escalation;
- pause/recalibrate for instrument/version drift, fraud/duplicates, randomization/exposure failure, missing telemetry, severe nonresponse/coverage, unplanned assistance, mode failure, or material protocol deviation;
- stop collection for evidentiary sufficiency only under a predeclared or auditable method-specific rule; convenience or a favorable early result is not sufficiency;
- if the achieved sample/fieldwork misses the contract, lower the maximum claim scope or return inconclusive/not-tested. Never retain the stronger claim by relabeling weak execution.

Primary rules: `R-ACCESS-01`, `R-FIELD-01`, `R-QUAL-01`, `R-SURVEY-01`, `R-EXP-02`, `R-ETHICS-01`, and selected method-card rules.
