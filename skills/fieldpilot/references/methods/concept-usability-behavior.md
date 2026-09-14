# Method Cards — Concept, Usability, and Behavioral Validation

Cards implement the Section 10.4 contract. Version `1.5.0`. These cards keep concept response, usability, actual-use behavior, and market demand as distinct constructs; no card's claim may substitute for another's.

## `CONCEPT_TEST`

- **supported_proposition_types:** comprehension and relevance/desirability as bounded `USABILITY_OR_COMPREHENSION` and `STATED_PREFERENCE_OR_WTP` reactions to a shown stimulus; comparative stated response across presented concepts.
- **unsupported_proposition_types:** usability/task performance, purchase, retention, product performance, market demand.
- **required_evidence_dimensions:** stimulus fidelity, information/price shown, context, order/randomization, exposure, and diagnostic measures (comprehension, relevance, uniqueness, believability).
- **minimum_design_conditions:** standardized stimuli/context held constant across conditions; order/randomization applied where needed; diagnostic measures defined before fieldwork; construct separation from usability, performance, adoption, and demand preserved throughout.
- **sample_and_unit_requirements:** target-respondent sample matched to the decision population; size follows precision/comparison-power logic for the diagnostic measures, not a universal N.
- **instrument_or_stimulus_requirements:** concept stimulus (fidelity level, information/price shown), response instrument, order/rotation plan, pretested wording.
- **fieldwork_and_quality_controls:** exposure/attention checks, order-effect monitoring, stimulus-version control, deviation log.
- **analysis_path_and_estimand:** comprehension/relevance/comparative-response estimate bounded to the shown stimulus and the studied respondents; no extension to usability, purchase, or performance.
- **assumptions_and_known_biases:** stated-response/hypothetical-bias gap, stimulus-fidelity limits, context/order effects, social-desirability inflation.
- **common_failure_modes:** reporting concept enthusiasm as demand; reporting a comprehension score as usability; generalizing a single-cell result without a comparison basis.
- **allowed_claim_templates:** “Exposed to stimulus S (fidelity F), respondents reported comprehension/relevance X, with comparative response Y under condition C.”
- **forbidden_claim_patterns:** “This concept will sell”; “users can use the product” as a usability claim from a concept test; purchase-intent score reported as an actual purchase.
- **numeric_provenance_requirements:** stimulus version, sample/frame, exposure counts, response scale, comparison basis, uncertainty.
- **ethics_privacy_and_escalation:** avoid deceptive price/claims in stimuli beyond disclosed research framing; escalate regulated-product-claim review (medical, financial) before fielding.
- **domain_adapter_hooks:** B2B concept role (buyer vs. user), physical-product concept safety-claim review, regulated-industry claim review.
- **rule_and_source_ids:** `R-CONCEPT-01`, `R-USABILITY-01`, `R-NUMERIC-01`; `S-ISO-USABILITY`, `S-MORWITZ`.

**Escalate/stop:** fail closed if the study proposes to answer usability, performance, or demand from a concept-only design. Route to `PROTOTYPE_USABILITY`, `BEHAVIORAL_ANALYTICS`, or `ACTUAL_PAYMENT_PAID_PILOT` for those constructs instead.

## `PROTOTYPE_USABILITY`

- **supported_proposition_types:** `USABILITY_OR_COMPREHENSION` (task success, comprehension, workflow problems); `IMPLEMENTATION_OR_FEASIBILITY` within tested conditions.
- **unsupported_proposition_types:** market demand, production reliability/manufacturability, actual-use safety beyond tested conditions, retention/adoption.
- **required_evidence_dimensions:** representative users/tasks/context, fidelity fit to the tested question, performance measures (success/error/help/severity), observation protocol, moderator-assistance logging.
- **minimum_design_conditions:** representative users, tasks, and context defined; prototype fidelity matched to the question being asked; success/error/help criteria and severity logic set before sessions; moderator-assistance boundaries defined in advance.
- **sample_and_unit_requirements:** representative-user sample sized for task/problem-discovery or performance-estimation logic, not a universal N; task-level and participant-level units both tracked.
- **instrument_or_stimulus_requirements:** task script, prototype build/version, success/error/help criteria, severity-rating scheme, think-aloud/observation protocol.
- **fieldwork_and_quality_controls:** moderator-assistance log, task-order control, environment/context control, severity-coding reliability check, deviation log.
- **analysis_path_and_estimand:** task success/error/help-rate and problem-severity analysis bounded to tested users, tasks, and prototype conditions; no extension beyond tested fidelity.
- **assumptions_and_known_biases:** prototype-fidelity gap from production reality, lab/observed-context effects, small-sample problem-discovery limits.
- **common_failure_modes:** reporting a usability pass as market demand; treating a low-fidelity result as proof of production reliability; reporting assisted completion as independent success.
- **allowed_claim_templates:** “In tested users/tasks/prototype (fidelity F), success/error/help rate was R, with severity S problems found.”
- **forbidden_claim_patterns:** “This proves the product is safe/reliable in production”; “users will buy/adopt” from a usability session.
- **numeric_provenance_requirements:** participant/task denominators, success/error/help definitions, severity scale, fidelity level, uncertainty.
- **ethics_privacy_and_escalation:** safety review for physical/medical prototypes; escalate regulated-device usability questions to qualified human-factors review.
- **domain_adapter_hooks:** physical-product safety/manufacturability escalation, SaaS workflow role context, regulated-device human-factors review.
- **rule_and_source_ids:** `R-USABILITY-01`, `R-PHYSICAL-01`, `R-NUMERIC-01`; `S-ISO-USABILITY`, `S-FDA-HF`.

**Escalate/stop:** fail closed if fidelity is insufficient for the safety/performance question asked. Escalate to a qualified human-factors/regulatory reviewer for medical or safety-critical products before any performance claim is issued.

## `BEHAVIORAL_ANALYTICS`

- **supported_proposition_types:** `ACTUAL_TRANSACTION`/recorded-use patterns, `BEHAVIORAL_INTEREST`, `ASSOCIATION_OR_DIFFERENCE` in observed usage; `IMPLEMENTATION_OR_FEASIBILITY` under instrumented conditions.
- **unsupported_proposition_types:** motive/reason claims, `CAUSAL_EFFECT` without an experimental design, market-wide adoption claims from a single instrumented population/window.
- **required_evidence_dimensions:** eligible population and exposure/opportunity denominator; event definition, instrumentation version, identity/session/time-zone rules and data-quality checks; voluntary versus required behavior; assisted versus independent completion; acquisition channel/offer/price/incentive/context; first/repeat use, retention, churn, refunds; novelty, contamination, support, seasonality, and competing explanations.
- **minimum_design_conditions:** instrumentation validated and versioned; exposure/opportunity denominator explicitly defined before analysis; voluntary/required and assisted/independent use separated in the schema before any adoption number is reported.
- **sample_and_unit_requirements:** eligible/exposed population fixed as the denominator; unit of analysis (account/user/session/event) fixed with nested structure preserved (Section 12.1); no silent denominator switching between periods or reports.
- **instrument_or_stimulus_requirements:** event taxonomy/instrumentation spec, identity-resolution rules, QC checks, version-change log.
- **fieldwork_and_quality_controls:** data-quality checks (deduplication, bot/fraud filtering), time-zone/session-boundary consistency, missing-telemetry handling, seasonality/context annotation.
- **analysis_path_and_estimand:** funnel/recurrence/churn/pathway analysis against the defined exposure/opportunity denominator; voluntary independent adoption reported separately from assisted or required use; competing explanations (novelty, contamination, support intervention) addressed before causal-sounding language is used.
- **assumptions_and_known_biases:** instrumentation drift/version changes, novelty effects, selection into exposure, confounded concurrent changes.
- **common_failure_modes:** reporting a conversion rate without the exposure denominator; presenting assisted or required use as voluntary adoption; treating an association as a causal driver; silently redefining the denominator between periods.
- **allowed_claim_templates:** “Among N eligible/exposed users (window W, instrumentation version V), event E occurred for R, with voluntary/required and assisted/independent use reported separately.”
- **forbidden_claim_patterns:** “X% conversion” without a stated denominator; “this proves the feature caused the increase” from observational analytics alone; an assisted-use rate reported as scalable adoption.
- **numeric_provenance_requirements:** exposure/opportunity denominator, event definition/version, identity/dedup rules, window, voluntary/assisted split, uncertainty.
- **ethics_privacy_and_escalation:** consent/privacy for behavioral tracking, data minimization; escalate when telemetry implicates regulated data categories (health, financial, minors).
- **domain_adapter_hooks:** SaaS account/user/seat/activation/retention distinctions, marketplace two-sided denominators, media delivery/engagement/attribution distinctions.
- **rule_and_source_ids:** `R-BEHAVIOR-01`, `R-CAUSAL-LANG-01`, `R-SAAS-01`, `R-MARKETPLACE-01`, `R-MEDIA-01`, `R-NUMERIC-01`.

**Escalate/stop:** fail closed if the exposure/opportunity denominator or instrumentation validation is undefined. Escalate when telemetry suggests a competing explanation (concurrent change, contamination) that cannot be ruled out before a decision-grade claim is issued.

## `FAKE_DOOR_LANDING`

- **supported_proposition_types:** `BEHAVIORAL_INTEREST` — contextual interest action among exposed eligible users under stated conditions.
- **unsupported_proposition_types:** purchase demand, willingness to pay, retention, market validation, causal claims.
- **required_evidence_dimensions:** exposure denominator, placement/message, action definition, and trust/debrief plan; deception/trust-risk controls.
- **minimum_design_conditions:** exposure denominator defined before launch; placement/message/context documented; action definition (click, signup, waitlist join) fixed in advance; trust/deception controls and a debrief/redirect plan in place before launch.
- **sample_and_unit_requirements:** eligible/exposed-user population as the denominator; no universal conversion threshold; exposure segmented by channel/context.
- **instrument_or_stimulus_requirements:** landing-page/message variants, placement/channel spec, action-tracking instrumentation, debrief/disclosure copy for users who attempted the action.
- **fieldwork_and_quality_controls:** exposure-denominator QC, message/placement version control, trust-risk monitoring (complaints, opt-outs), debrief-delivery verification.
- **analysis_path_and_estimand:** interest-action rate among exposed eligible users under stated conditions, bounded to the tested placement, message, context, and window; no causal or demand extrapolation.
- **assumptions_and_known_biases:** novelty/curiosity clicks, message/placement-specific response, trust erosion from unmet expectation, selection into exposure.
- **common_failure_modes:** reporting a click rate as purchase demand or willingness to pay; omitting the exposure denominator; skipping debrief/disclosure and eroding participant trust; comparing rates across incomparable placements/messages.
- **allowed_claim_templates:** “Among N eligible/exposed users (placement/message M, window W), interest action A occurred for R — contextual interest only.”
- **forbidden_claim_patterns:** “This proves demand”; “X% would pay”; a fake-door conversion rate presented as validated willingness to pay or retention.
- **numeric_provenance_requirements:** exposure/opportunity denominator, action definition, placement/message version, window, uncertainty.
- **ethics_privacy_and_escalation:** trust/deception review before launch; debrief/redirect obligation for users who attempted the blocked action; escalate when the offer implies a real commitment (payment, contract) that cannot be honored.
- **domain_adapter_hooks:** SaaS signup-funnel context, marketplace side-specific fake doors, media placement/attribution distinctions.
- **rule_and_source_ids:** `R-FAKEDOOR-01`, `R-ETHICS-01`, `R-ETHICS-02`, `R-NUMERIC-01`; `S-FAKEDOOR`.

**Escalate/stop:** fail closed without an exposure denominator, trust/deception controls, or a debrief plan. Stop and disclose immediately if participant complaints or trust harm emerge during the run.
