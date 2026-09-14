# Method Cards — Surveys and Sampling

Cards implement the Section 10.4 contract. Version `1.5.0`. Survey cards estimate defined-population distributions and differences from measured samples; every claim's scope is fixed by its selection-probability basis, never by sample size alone.

## `PROBABILITY_SURVEY`

- **supported_proposition_types:** `DESCRIPTIVE_DISTRIBUTION` and `ASSOCIATION_OR_DIFFERENCE` for a defined target population.
- **unsupported_proposition_types:** `CAUSAL_EFFECT` without an experimental design, `MEANING_OR_EXPERIENCE` depth, timeless/universal truth beyond the sampled frame and period, `ACTUAL_TRANSACTION`.
- **required_evidence_dimensions:** coverage, selection/nonresponse, measurement, processing, weighting/modeling, and sampling error (Total Survey Error); frame/access source; construct definitions and cognitive pretesting.
- **minimum_design_conditions:** known selection probabilities from a defined frame; documented coverage gaps; contact/eligibility/response/partial/refusal/exclusion dispositions logged; cognitive pretesting/pilot completed; design effect and nonresponse/coverage limitations disclosed before any margin of sampling error is reported.
- **sample_and_unit_requirements:** target population and unit defined; frame/access source and coverage gaps recorded; sample size follows the estimand, heterogeneity, prevalence/event rate, clustering/design effect, decision precision, and expected attrition/nonresponse — not a fixed N.
- **instrument_or_stimulus_requirements:** pretested/piloted questionnaire, documented wording/response-option/order choices, mode and interviewer/device-effect notes, language/translation protocol.
- **fieldwork_and_quality_controls:** fraud/duplication/speeding/attention checks, disposition logging, weighting/model-variable and benchmark provenance, planned diagnostics.
- **analysis_path_and_estimand:** population estimate for the defined target under disclosed selection/weighting assumptions; report weighted and unweighted results, design effect, effective sample size, and residual selection risk together.
- **assumptions_and_known_biases:** coverage/frame mismatch, nonresponse bias, measurement/mode effects, model or weighting misspecification.
- **common_failure_modes:** reporting a margin of sampling error without an eligible probability-design basis; treating a large N as curing coverage, measurement, or confounding problems; silent frame drift; treating weighting as automatic representativeness.
- **allowed_claim_templates:** “For target population P (frame F, period T), the estimate is E with margin of sampling error M under disclosed design effect D”; “Weighted and unweighted results were W1/W2 with effective sample size N_eff.”
- **forbidden_claim_patterns:** “This proves causation”; “true for all time”; margin of sampling error reported without an eligible probability-design basis.
- **numeric_provenance_requirements:** numerator/denominator, weights, design effect, frame/coverage, period, MOE method, nonresponse rate, source locator.
- **ethics_privacy_and_escalation:** respondent privacy and data minimization; escalate when frame access is legally contested or design-effect/weighting judgment exceeds available statistical expertise before a high-stakes release.
- **domain_adapter_hooks:** B2B respondent-role sampling, regulated-population frame constraints (education, pharmaceutical), local geography/time frame boundaries.
- **rule_and_source_ids:** `R-SURVEY-01`, `R-SURVEY-03`, `R-SURVEY-04`, `R-NUMERIC-01`; `S-TSE`, `S-AAPOR-MOE`, `S-CORNESSE`.

**Escalate/stop:** fail closed and relabel as `NONPROBABILITY_SURVEY` if selection probabilities are not actually known and documented. Escalate design-effect/weighting judgment beyond available statistical expertise before any high-stakes release.

## `NONPROBABILITY_SURVEY`

- **supported_proposition_types:** sample-scoped `DESCRIPTIVE_DISTRIBUTION` and `ASSOCIATION_OR_DIFFERENCE`; exploratory comparison; conditional modeled population estimates only when explicit target-link assumptions are attached.
- **unsupported_proposition_types:** conventional sampling margin of error, automatic population representativeness, `CAUSAL_EFFECT` without an experimental design.
- **required_evidence_dimensions:** recruitment/source, self-selection mechanism, target-link model and assumptions when estimating beyond the sample, diagnostics/validation benchmarks, and model-based uncertainty.
- **minimum_design_conditions:** recruitment channel/source documented; self-selection risk assessed; if a population estimate is claimed, an explicit target-linking model, its assumptions, validation/benchmark diagnostics, and labeled model-based uncertainty must all be attached before release.
- **sample_and_unit_requirements:** achieved sample composition and any quotas recorded as composition control, not selection probability; target population/unit defined even when the claim stays sample-bound.
- **instrument_or_stimulus_requirements:** same pretesting, wording, and mode discipline as `PROBABILITY_SURVEY`; fraud/duplication/speeding/attention quality procedures.
- **fieldwork_and_quality_controls:** disposition logging, weighting/model-variable provenance when modeled, benchmark-comparison diagnostics, residual selection-risk disclosure.
- **analysis_path_and_estimand:** default estimand is `STUDIED_SAMPLE`-scoped description/comparison; a `TARGET_POPULATION` estimate is permitted only as a labeled model-based estimate with stated assumptions and uncertainty — never as a conventional margin-of-error statement.
- **assumptions_and_known_biases:** self-selection bias, panel/professional-respondent effects, coverage gaps in the recruitment source, model misspecification when target-linking.
- **common_failure_modes:** reporting a conventional margin of error on an opt-in panel; claiming quotas or weighting alone produced a representative sample; silently reframing a sample description as population fact.
- **allowed_claim_templates:** “In this opt-in/nonprobability sample (source S, N), the result is R, sample-scoped”; “Under target-link model M and assumptions A, the modeled population estimate is E with model-based uncertainty U (not a conventional margin of error).”
- **forbidden_claim_patterns:** “Margin of error is ±X%” on an opt-in sample; “the sample represents the population” from quotas/weighting alone; a sample description silently reframed as a population claim.
- **numeric_provenance_requirements:** source/recruitment channel, achieved composition versus quota targets, weighting variables and diagnostics when used, model assumptions and uncertainty for any population estimate.
- **ethics_privacy_and_escalation:** panel-provider data handling and consent; escalate when a population claim will drive a high-stakes decision and target-link validation is weak or unavailable.
- **domain_adapter_hooks:** B2B panel-role verification, consumer online-panel context, regulated-topic screening.
- **rule_and_source_ids:** `R-SURVEY-01`, `R-SURVEY-02`, `R-SURVEY-04`, `R-NUMERIC-01`; `S-AAPOR-NP`, `S-CORNESSE`.

**Escalate/stop:** fail closed on any conventional margin-of-error claim or unqualified representativeness claim from this design. If a decision requires probability-based population inference and only opt-in access exists, expose the gap per Section 8 rather than silently upgrading the claim.
