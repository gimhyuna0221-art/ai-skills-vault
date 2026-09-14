# Method Cards — Human Qualitative Research

Cards implement the Section 10.4 contract. Version `1.5.0`. Qualitative cards capture meaning, mechanism, and situated behavior among studied participants or cases in named settings; none of them converts a case pattern into a population percentage without separate quantitative evidence.

## `HUMAN_DEPTH_INTERVIEW`

- **supported_proposition_types:** `MEANING_OR_EXPERIENCE`, `MECHANISM_OR_JOB`; bounded `IMPLEMENTATION_OR_FEASIBILITY` and `BUYING_SYSTEM` questions when situated in participant accounts.
- **unsupported_proposition_types:** `DESCRIPTIVE_DISTRIBUTION`/prevalence, `CAUSAL_EFFECT`, `ACTUAL_TRANSACTION`, `USABILITY_OR_COMPREHENSION` task performance, market-wide `STATED_PREFERENCE_OR_WTP` magnitude.
- **required_evidence_dimensions:** analytic aim and relevant variation, purposive/theoretical/case sampling logic and exclusions, moderator role/positionality/conflicts, setting/mode/language/recording/guide-revision record, coding or analytic approach with disagreement handling and audit trail, negative/deviant cases and missing voices, stopping rationale tied to code breadth, meaning depth, theoretical sufficiency, or information power.
- **minimum_design_conditions:** purposive/theoretical sampling logic stated before recruitment; moderator trained with defined role boundaries; guide piloted with a revision log; reflexivity and negative-case search built into the analysis plan before fieldwork closes.
- **sample_and_unit_requirements:** purposive/theoretical/case sampling; no universal interview count — rationale weighs aim breadth, sample specificity/diversity, theory, dialogue richness, event rarity, analytic strategy, subgroup claims, and evidence collected so far; bounded counts are allowed (“Among these 8 participants, 6 described X”) but never convert purposive cases into a population estimate.
- **instrument_or_stimulus_requirements:** interview guide with pilot and revision log, language/translation protocol, recording/transcription process, moderator training record.
- **fieldwork_and_quality_controls:** reflexivity notes, analyst disagreement handling, evidence-to-transcript links and audit trail, negative-case and missing-voice search, consent/withdrawal handling, deviation log.
- **analysis_path_and_estimand:** coding/thematic or analytic-strategy synthesis bounded to the `STUDIED_SAMPLE`; transfer/generalization rationale stated separately from the finding itself; no estimand beyond the studied cases.
- **assumptions_and_known_biases:** interviewer/social-desirability effects, recall bias, purposive-sample non-representativeness, translation/interpretation loss.
- **common_failure_modes:** applying a universal N or saturation formula; converting quotation counts into prevalence; presenting a convenience sample as purposive; dropping negative/deviant cases from the account.
- **allowed_claim_templates:** “Among these N purposively sampled participants, M described experience/mechanism X, with transfer rationale Y”; “Participant P (case C) reported experience X under context K.”
- **forbidden_claim_patterns:** “X% of customers feel…”; “Most users…” without a population link; a case pattern reported as market prevalence.
- **numeric_provenance_requirements:** any bounded count retains its denominator as the studied sample, the sampling logic, exclusions, and the coding rule that produced it; no extrapolation without separate quantitative evidence.
- **ethics_privacy_and_escalation:** informed consent, withdrawal rights, vulnerable-participant protections, and research/sales separation; escalate disclosed harm, distress, or safeguarding-relevant content beyond the moderator's scope.
- **domain_adapter_hooks:** B2B buying-system role context, SaaS account/user role framing, local site/context specificity, unfamiliar-domain glossary preflight, regulated or vulnerable-population protections.
- **rule_and_source_ids:** `R-QUAL-01`, `R-QUAL-02`, `R-QUAL-03`, `R-ETHICS-01`, `R-ETHICS-02`, `R-NEG-01`; `S-INFO-POWER`, `S-SAT-REVIEW`, `S-SAT-MEANING`, `S-SRQR`, `S-COREQ`, `S-DRISKO`.

**Escalate/stop:** block launch without a stated purposive-sampling rationale, moderator training, or consent materials. If the real question requires a population estimate, route to `PROBABILITY_SURVEY` or `NONPROBABILITY_SURVEY` instead of stretching interview counts; escalate sensitive disclosures beyond researcher scope immediately.

## `AI_MODERATED_INTERVIEW`

- **supported_proposition_types:** the same candidate aims as `HUMAN_DEPTH_INTERVIEW` (`MEANING_OR_EXPERIENCE`, `MECHANISM_OR_JOB`) collected through a named, disclosed AI moderation mode, with mode limitations recorded.
- **unsupported_proposition_types:** any human-moderator-equivalence claim; `DESCRIPTIVE_DISTRIBUTION`/prevalence; `CAUSAL_EFFECT`; safeguarding-dependent topics without an armed human escalation path; any claim requiring synthetic gap-filled content as testimony.
- **required_evidence_dimensions:** AI disclosure/consent, exact-system pilot (model/version, system prompt, guide, language, topic, population, channel, safety setup), `moderator_type: AI` provenance labeling, human oversight/escalation coverage, and an audit of non-leading openness, contextual relevance, follow-up judgment, unsupported assumptions, skips, repetition, tone/empathy, latency, dropout, schema failures, differential disclosure, subgroup accessibility, and adverse events.
- **minimum_design_conditions:** only real participants are enrolled; pre-collection disclosure covers AI moderator status, purpose, recording/processing, providers/retention, limitations, monitoring status, human contact/escalation/withdrawal routes, and a non-AI alternative when required or feasible; a human escalation path with response-time coverage is armed before launch.
- **sample_and_unit_requirements:** same purposive/theoretical sampling logic and no-universal-N rule as `HUMAN_DEPTH_INTERVIEW`; subgroup accessibility explicitly checked for differential AI-mode effects.
- **instrument_or_stimulus_requirements:** pinned model/version and system-prompt pilot record, version-controlled guide, language/localization check, recording/transcription and retention disclosure.
- **fieldwork_and_quality_controls:** live or near-live human-oversight monitoring, dropout/adverse-event log, differential-disclosure audit across subgroups, schema-failure and latency log, deviation log.
- **analysis_path_and_estimand:** bounded to the `STUDIED_SAMPLE` collected under the named AI mode; mode is retained as a recorded covariate in analysis, never stripped out.
- **assumptions_and_known_biases:** AI-interviewer probing may differ materially from human probing (`EXPERIMENTAL` evidence per `S-AI-INTERVIEWER`); disclosure effects on candor; automation bias in interpreting AI-generated follow-ups.
- **common_failure_modes:** presenting a transcript gap as an answered question; claiming human-moderator equivalence from one benchmark; skipping disclosure/consent; letting AI serve as the sole safeguarding layer for distress, abuse, self-harm, minors, or impaired consent.
- **allowed_claim_templates:** “Under AI-moderated mode M (model/version V, piloted P), participants reported X, with mode limitations L noted”; “Human escalation was available/used under condition C.”
- **forbidden_claim_patterns:** “Equivalent to a human interview”; “the AI inferred/filled in that the participant meant X”; synthetic-generated content presented as a participant quotation.
- **numeric_provenance_requirements:** same bounded-count discipline as `HUMAN_DEPTH_INTERVIEW`, plus dropout, adverse-event, and schema-failure counts with denominators and the `moderator_type: AI` label attached.
- **ethics_privacy_and_escalation:** disclosure/consent, exact-system pilot, and oversight/escalation per `R-AI-04`; material AI use and named human responsibility logged per `R-AI-06`; AI must never be the sole safeguarding layer for distress, abuse, self-harm, minors, impaired consent, medical issues, or reportable regulated events.
- **domain_adapter_hooks:** regulated/vulnerable-population extra protections, accessibility/language alternative requirement, unfamiliar-domain glossary preflight, B2B/SaaS role context carried from the human-interview card.
- **rule_and_source_ids:** `R-AI-04`, `R-AI-05`, `R-AI-06`, `R-QUAL-01`, `R-QUAL-02`, `R-QUAL-03`, `R-ETHICS-01`; `S-MRS-AI`, `S-ESOMAR`, `S-AI-INTERVIEWER`.

**Escalate/stop:** block launch without disclosure/consent, an exact-system pilot, or an armed human escalation path. Stop and route to human moderation or defer the topic when a disclosure signals safeguarding-relevant content the AI/escalation setup cannot cover in time. Never issue a moderator-equivalence claim regardless of session quality observed.

## `OBSERVATION_CONTEXTUAL`

- **supported_proposition_types:** `MECHANISM_OR_JOB`, `IMPLEMENTATION_OR_FEASIBILITY`, situated `USABILITY_OR_COMPREHENSION`, and bounded `MEANING_OR_EXPERIENCE` grounded in observed context.
- **unsupported_proposition_types:** unobserved motive/intent, prevalence, voluntary-adoption claims, `CAUSAL_EFFECT`.
- **required_evidence_dimensions:** setting, workflow/tasks/events, sampling of times/cases, observer role, consent/privacy, field-note or recording protocol, assistance level, and observer/reactivity limits.
- **minimum_design_conditions:** consent/access secured before entry; context and tasks defined; an observation protocol with explicit sampling of times/cases; observer-effect and reflexivity plan documented before fieldwork begins.
- **sample_and_unit_requirements:** case/setting/time sampling logic stated; no universal observation count; nested structure preserved — multiple observations at one site do not become independent sites (Section 12.1).
- **instrument_or_stimulus_requirements:** field-note template or recording protocol, event/task-sequence coding scheme, error/workaround map template.
- **fieldwork_and_quality_controls:** observer training and role boundaries, reactivity/observer-effect log, privacy handling in shared or semi-public settings, deviation log.
- **analysis_path_and_estimand:** event/task-sequence analysis, error/workaround maps, case comparison, and bounded pattern coding, scoped to the `STUDIED_SAMPLE` of observed settings/cases.
- **assumptions_and_known_biases:** observer/reactivity effect on behavior, sampled-time non-representativeness, risk of inferring unseen motive.
- **common_failure_modes:** inferring motive without a participant account; treating observed cases as population prevalence; reporting assisted or required access as voluntary adoption.
- **allowed_claim_templates:** “In observed setting S over sampled times T, workflow/behavior X occurred among observed cases C”; “Workaround W was observed under context K; motive is unknown absent participant account.”
- **forbidden_claim_patterns:** “Users want/intend X” from observation alone; “X% of users do Y” from observed cases; “adoption is voluntary” when access was required or assisted.
- **numeric_provenance_requirements:** case/time/setting denominators, sampling logic, coding scheme, no extrapolation beyond the observed sample.
- **ethics_privacy_and_escalation:** consent/privacy in observed settings, safeguarding for vulnerable settings, escalation when observation implicates a regulated or safety condition.
- **domain_adapter_hooks:** local site/servicescape/catchment context, B2B workflow role, physical-product safety context, regulated-setting preflight.
- **rule_and_source_ids:** `R-OBS-01`, `R-QUAL-02`, `R-QUAL-03`, `R-NEG-01`; `S-SRQR`, `S-ISO-USABILITY`.

**Escalate/stop:** fail closed without consent/access or a documented observation protocol. Stop and route to interview or survey design when the real question is motive or prevalence rather than observed process.

## `FOCUS_GROUP`

- **supported_proposition_types:** `MEANING_OR_EXPERIENCE` (shared language, contested meanings), `MECHANISM_OR_JOB` via group discussion, and stated reactions to shared stimuli.
- **unsupported_proposition_types:** independent prevalence, private individual willingness, individual purchase behavior, `CAUSAL_EFFECT`, sensitive topics requiring private disclosure.
- **required_evidence_dimensions:** why group interaction answers the proposition, composition and power relationships, moderator skill, privacy limits, stimulus/order, and number-of-group rationale.
- **minimum_design_conditions:** composition rationale stated before recruitment; skilled/trained moderator assigned; group-dynamics analysis plan set; privacy limits disclosed to participants before sensitive stimuli are shown.
- **sample_and_unit_requirements:** group composition and group-count rationale tied to the analytic aim — no universal group count; participant-level and group-level units both tracked; recruitment screens for professional-participant bias where material.
- **instrument_or_stimulus_requirements:** discussion guide, stimulus materials with order/rotation plan, moderator prompts designed to surface dissent and quiet voices.
- **fieldwork_and_quality_controls:** dominance/silencing log, disclosed privacy limits, recording/transcription, deviation log.
- **analysis_path_and_estimand:** interaction analysis — consensus/dissent, dominant/silenced voices, within- and across-group patterns — bounded to the studied groups.
- **assumptions_and_known_biases:** social conformity/groupthink, dominant-voice distortion, moderator influence, unsuitability for private or sensitive disclosure.
- **common_failure_modes:** treating utterance counts as independent prevalence; treating group consensus as private individual willingness; underpowered capture of dissent.
- **allowed_claim_templates:** “In group G (composition C), participants discussed/reacted to X, with dissent/consensus pattern Y noted”; “Across groups G1…Gk, interaction pattern P recurred/diverged.”
- **forbidden_claim_patterns:** “X% of customers would buy”; group consensus reported as individual private willingness; utterance frequency reported as population prevalence.
- **numeric_provenance_requirements:** group/participant denominators, composition variables, utterance-count scope bound to the group (never population), coding rule.
- **ethics_privacy_and_escalation:** privacy-limit disclosure (participants hear each other), sensitive-topic escalation or routing to a private method, participant care and withdrawal rights.
- **domain_adapter_hooks:** B2B buying-system group composition (mixed vs. single role), consumer household/occasion context, regulated-topic preflight.
- **rule_and_source_ids:** `R-FOCUS-01`, `R-QUAL-02`, `R-QUAL-03`, `R-NEG-01`; `S-COREQ`, `S-SRQR`.

**Escalate/stop:** stop and route to individual interviews when the topic requires private disclosure or the planned composition creates an undue power imbalance. Fail closed without a moderator-training record and a stated composition rationale.

## `DIARY_LONGITUDINAL`

- **supported_proposition_types:** `MECHANISM_OR_JOB` (journey, recurrence), `MEANING_OR_EXPERIENCE` over time, `IMPLEMENTATION_OR_FEASIBILITY` for delayed use, and bounded `BEHAVIORAL_INTEREST` when externally verified.
- **unsupported_proposition_types:** population frequency claims, unverified behavior asserted as fact, `CAUSAL_EFFECT`.
- **required_evidence_dimensions:** event- or interval-contingent prompts, duration tied to the decision-relevant recurrence/lag, participant burden, reminders, verification method, missing-entry and dropout rules.
- **minimum_design_conditions:** time window and prompt cadence justified by the decision-relevant recurrence/lag — no universal duration or cadence; compliance/adherence tracking plan and a verification plan (external trace versus self-report only) set before fieldwork.
- **sample_and_unit_requirements:** participant/window/mode-bound units; nested entries per participant do not expand the participant denominator (Section 12.1); adherence and missingness tracked per participant.
- **instrument_or_stimulus_requirements:** prompt template (event- or interval-contingent), reminder schedule, entry format, verification/trace linkage where available.
- **fieldwork_and_quality_controls:** adherence/missingness log, dropout log, entry-authenticity spot checks, deviation log.
- **analysis_path_and_estimand:** within-case time-path analysis and cross-case pattern analysis with adherence visible, bounded to participating cases and the study window.
- **assumptions_and_known_biases:** self-report recall/reactivity bias, attrition/dropout selection, unverifiable entries absent an external trace.
- **common_failure_modes:** applying a universal diary duration/cadence; treating self-report entries as verified behavior; excluding dropout cases silently from pattern claims.
- **allowed_claim_templates:** “Among participating cases (N, window W), pattern X recurred with adherence rate A”; “Entry E is self-reported; behavior is externally verified/unverified.”
- **forbidden_claim_patterns:** “This happens to X% of users” from diary cases; unverified self-report presented as confirmed behavior; silent exclusion of dropout cases from pattern claims.
- **numeric_provenance_requirements:** participant/window denominators, adherence/missingness rates, verification status per entry, no extrapolation beyond participating cases.
- **ethics_privacy_and_escalation:** participant burden and withdrawal rights, privacy of diary content, escalation for safeguarding-relevant disclosures found during the window.
- **domain_adapter_hooks:** SaaS usage-journey context, B2B renewal/procurement timeline, consumer household routine, regulated-event reporting where applicable.
- **rule_and_source_ids:** `R-DIARY-01`, `R-QUAL-02`, `R-QUAL-03`, `R-NEG-01`; `S-SRQR`.

**Escalate/stop:** fail closed without a duration/cadence rationale tied to the decision-relevant recurrence, or without a missingness/verification plan. Escalate safeguarding-relevant disclosures found in entries immediately.
