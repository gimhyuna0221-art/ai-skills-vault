# Method Cards — Experimentation and A/B Testing

Cards implement the Section 10.4 contract. Version `1.5.0`. Experiment cards bound every causal claim to the tested units, treatment, outcome, and window; internal validity never substitutes for transport evidence.

## `AB_RANDOMIZED_EXPERIMENT`

- **supported_proposition_types:** `CAUSAL_EFFECT` for eligible units, metric, and window under the tested experiment conditions.
- **unsupported_proposition_types:** automatic transport to other populations, channels, or times; non-experimental correlational claims presented as this method's output.
- **required_evidence_dimensions:** causal estimand and eligible population; treatment/control/assignment unit/allocation/exclusion rules; primary outcome, guardrails/harms, effect size of decision interest, and analysis window; exposure/compliance definition and instrumentation validation; power/precision rationale; clustering/spillover/interference/novelty/carryover/network risk; stopping/sequential plan and multiplicity handling; sample-ratio and randomization-integrity checks; attrition/missingness/implementation-failure/practical-significance; transport limits.
- **minimum_design_conditions:** valid randomization/assignment mechanism defined before launch; estimand, primary outcome, guardrails, and analysis window predeclared; power/precision rationale specific to the estimand and design; sample-ratio-mismatch and randomization-integrity checks built into the analysis plan before launch.
- **sample_and_unit_requirements:** eligible-unit population and assignment unit defined (individual, session, or cluster); clustering/interference risk assessed; nested units preserved per Section 12.1.
- **instrument_or_stimulus_requirements:** treatment/control implementation spec, instrumentation validation for exposure/compliance, guardrail-metric definitions.
- **fieldwork_and_quality_controls:** sample-ratio-mismatch check, randomization-integrity check, exclusion/attrition/missingness log, implementation-failure log, peeking/multiplicity-control adherence.
- **analysis_path_and_estimand:** predeclared primary-outcome analysis for the causal estimand among eligible units, treatment, outcome, and window; report the effect estimate with interval and practical significance; address interference/spillover when applicable; no transport beyond the tested population, channel, or time without separate evidence.
- **assumptions_and_known_biases:** interference/spillover violations, novelty/carryover effects, implementation-fidelity gaps, multiplicity/peeking inflation.
- **common_failure_modes:** reporting a result as universally generalizable across markets, segments, channels, or time; ignoring a sample-ratio mismatch; peeking without multiplicity control; treating a guardrail miss as a success because the primary metric moved.
- **allowed_claim_templates:** “For eligible units U, treatment T versus control C produced effect E (interval I) on outcome O over window W, under experiment conditions D.”
- **forbidden_claim_patterns:** “This effect holds everywhere/always”; “proven for all users” beyond the eligible/tested population; a causal claim from a design lacking valid randomization.
- **numeric_provenance_requirements:** unit counts by arm, sample-ratio-mismatch statistic, effect estimate/interval, primary/guardrail metric definitions, window, exclusions/attrition, multiplicity-adjustment method.
- **ethics_privacy_and_escalation:** harm/guardrail-triggered stop rules; escalate when the experiment affects safety, pricing, or regulated outcomes.
- **domain_adapter_hooks:** marketplace two-sided interference, network-effect exposure context, SaaS account-level assignment, education classroom/team clustering.
- **rule_and_source_ids:** `R-EXP-01`, `R-EXP-02`, `R-EXP-03`, `R-EXP-04`, `R-NUMERIC-01`; `S-ONLINE-EXP`, `S-CONSORT`, `S-SRM`, `S-ASA`, `S-INTERFERENCE`, `S-TRANSPORT`, `S-CAUSAL-LANG`.

**Escalate/stop:** fail closed on sample-ratio-mismatch failure, invalid randomization, or predeclaration gaps before reporting any causal claim. Escalate transport claims beyond the tested population, channel, or time to a separate validation study rather than asserting them.

## `QUASI_EXPERIMENT`

- **supported_proposition_types:** `CAUSAL_EFFECT`, conditionally, when randomization is unavailable, under explicit identification assumptions.
- **unsupported_proposition_types:** randomized-design certainty or language, unrestricted transport.
- **required_evidence_dimensions:** explicit identification assumptions, comparator construction, pre-trend/design diagnostics, plausible-violation checks, sensitivity analyses.
- **minimum_design_conditions:** identification strategy (for example, difference-in-differences, regression discontinuity, matching, instrumental variable) named with its required assumptions stated before analysis; comparator group/construction documented; pre-trend or design-validity diagnostics run before results are treated as causal.
- **sample_and_unit_requirements:** treated and comparator units defined with the same unit-of-analysis discipline as `AB_RANDOMIZED_EXPERIMENT`; nested/clustered structure preserved per Section 12.1.
- **instrument_or_stimulus_requirements:** comparator-construction method, covariate/matching specification, pre-period data and diagnostic plots/tests.
- **fieldwork_and_quality_controls:** pre-trend/parallel-trends or design-validity check, placebo/falsification tests where applicable, sensitivity-analysis log, deviation log.
- **analysis_path_and_estimand:** conditional causal estimate under the named identification assumptions, with sensitivity analysis reported alongside the point estimate; causal language bounded per `R-CAUSAL-LANG-01`.
- **assumptions_and_known_biases:** unobserved confounding, violated parallel-trends/exclusion-restriction assumptions, comparator non-comparability, selection into treatment.
- **common_failure_modes:** presenting a quasi-experimental estimate with randomized-trial confidence language; skipping pre-trend/placebo diagnostics; omitting sensitivity analysis; unrestricted transport of the estimate.
- **allowed_claim_templates:** “Under identification assumption A (comparator M, diagnostics D), the conditional causal estimate for outcome O is E, sensitivity range S; this is not a randomized result.”
- **forbidden_claim_patterns:** “This is as good as an A/B test”; “proven causal” without stated identification assumptions; unrestricted transport beyond the study context.
- **numeric_provenance_requirements:** comparator construction, pre-trend/diagnostic statistics, effect estimate with sensitivity range, sample/unit counts, assumptions log.
- **ethics_privacy_and_escalation:** escalate when the identification strategy or its assumptions require specialized statistical/causal-inference review before a high-stakes claim.
- **domain_adapter_hooks:** education outcome-design context, B2B/enterprise deployment comparator context, regulated-market comparator constraints.
- **rule_and_source_ids:** `R-QUASI-01`, `R-EXP-03`, `R-CAUSAL-LANG-01`, `R-NUMERIC-01`; `S-CAUSAL-LANG`, `S-TRANSPORT`, `S-WWC`.

**Escalate/stop:** fail closed if identification assumptions, comparator diagnostics, or sensitivity analysis are missing before any causal claim is issued. Escalate to a qualified causal-inference reviewer when assumption plausibility is contested or stakes are high.
