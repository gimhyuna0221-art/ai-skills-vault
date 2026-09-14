# Method Cards — Market Sizing and Segmentation

Cards implement the Section 10.4 contract. Version `1.5.0`. Market magnitude and demand are separate propositions. Every numeric input and output requires Numeric Provenance.

## `MARKET_SIZING`

- **supported_proposition_types:** `MARKET_MAGNITUDE`; capacity, revenue/volume range, reachable/serviceable constraints, and decision sensitivity under named assumptions.
- **unsupported_proposition_types:** demand, preference, adoption, WTP, product-market fit, causal effect, or a guaranteed forecast.
- **required_evidence_dimensions:** explicit market definition, unit/time/geography, observed inputs versus assumptions, dimensional formula, uncertainty/sensitivity, source conflict/age, reachable constraints, independent cross-check when proportionate.
- **minimum_design_conditions:** define customer/buyer, beneficiary/user, problem/use case, geography, channel, eligibility/exclusions, period, unit, price/revenue basis, currency/base year before calculation.
- **sample_and_unit_requirements:** retain each source/model unit (`people`, `accounts`, `sites`, `transactions`, `volume`, `revenue`) and nested/conversion relationships; do not count users as buyers or seats as independent accounts without justification.
- **instrument_or_stimulus_requirements:** input ledger with `KNOWN_INPUT`, `ASSUMPTION`, `CALCULATION`, `RANGE`, `UNVERIFIED_GAP`; formula/model, scenario and source locator fields.
- **fieldwork_and_quality_controls:** unit/dimensional checks, definition alignment, duplicate-source review, conservative/base/expansive scenarios or justified distribution, material-assumption sensitivity, discrepancy log, currency/inflation handling.
- **analysis_path_and_estimand:** construct top-down, bottom-up, capacity or cohort model appropriate to the decision; compute auditable ranges; cross-check with an independently structured model where feasible; do not average discrepancies away without rationale.
- **assumptions_and_known_biases:** category-definition drift, double counting, stale sources, price/revenue confusion, availability versus reachability, survivorship, arbitrary penetration, false precision.
- **common_failure_modes:** undefined TAM; `SOM = x% of TAM`; precise scalar from weak inputs; mixed currencies/base years; hidden exclusions/conversions; presenting addressable population as validated demand.
- **allowed_claim_templates:** “Under assumptions A and sources S, the modeled [defined unit] range for G/T is L–U”; “Input X is known/assumed/unverified and changes the estimate by Y under sensitivity C.”
- **forbidden_claim_patterns:** “The market is exactly X”; “TAM proves demand”; “We will capture x%”; “TAM/SAM/SOM” without project definitions.
- **numeric_provenance_requirements:** complete value/range, numerator/denominator/base, unit, population, geography, period, currency/base year, source locator, original/derived, formula, assumptions, uncertainty, sensitivity and rounding for every material number.
- **ethics_privacy_and_escalation:** avoid disclosive small-cell outputs and unauthorized data use; escalate technical/statistical or regulated-source interpretation when stakes exceed available expertise.
- **domain_adapter_hooks:** account/user/payer mapping, local catchment/capacity, F&B throughput/perishability, marketplace sides/transactions, ad inventory/yield, physical channel/returns, education institutions, regulation.
- **rule_and_source_ids:** `R-SIZE-01`, `R-SIZE-02`, `R-NUMERIC-01`; `S-GAO`, `S-JCGM`, `S-FORECAST`.

**Escalate/stop:** block material output with unknown buyer/unit/geography/period/source/formula. If uncertainty swamps the decision, expose the sensitivity-driving gap and route research to that input; do not manufacture precision.

## `SEGMENTATION`

- **supported_proposition_types:** `SEGMENT_STRUCTURE` and decision-specific differences in problem, behavior, context, economics, workflow, adoption ability/willingness, or reachability.
- **unsupported_proposition_types:** universal/stereotype personas, natural/permanent customer types, causal mechanisms, prevalence or segment size beyond the eligible sample/model.
- **required_evidence_dimensions:** decision purpose, variables/measurement, sample/coverage, method provenance, within/between variation, stability where data-driven, usefulness/actionability, reachability/economics and fairness.
- **minimum_design_conditions:** state what action differs by segment. Mark `A_PRIORI` or `DISCOVERED`. A-priori labels remain hypotheses; discovered segments require analytic provenance and candidate-solution rationale.
- **sample_and_unit_requirements:** population/unit/frame appropriate to the action; sufficient relevant variation and subgroup coverage; preserve nesting and outliers/missing groups; no universal segment N/count.
- **instrument_or_stimulus_requirements:** construct definitions and measurement provenance; for data-driven work preserve variables, missing-data treatment, transformations/scaling, distance/model, algorithm, candidate solutions and seed.
- **fieldwork_and_quality_controls:** measurement/coverage review, discriminability and within-segment heterogeneity, stability under resampling/specification changes when applicable, held-out/new-data check for material use, fairness/harm review.
- **analysis_path_and_estimand:** a-priori differentiation/reachability/actionability tests or explicit clustering/latent-class/mixture analysis; profile with variables not mechanically defining the groups; compare candidate solutions and decision utility.
- **assumptions_and_known_biases:** researcher-imposed labels, unstable algorithms, correlated/redundant variables, scaling choices, sample-specific structure, post-hoc storytelling, protected-class proxy harms.
- **common_failure_modes:** stereotype persona; one cluster run = stable market; familiar firmographics = validated segments; selecting a pretty solution; ignoring within-group variation; universal cutoff/algorithm/count.
- **allowed_claim_templates:** “In analyzed data D under model/specification M, solution K produced these bounded groups; stability/usefulness diagnostics were X”; “A-priori group G is an operational hypothesis with supported/unsupported differences Y.”
- **forbidden_claim_patterns:** “These are the market’s natural customer types”; “There are exactly K segments”; segment prevalence/generalization without an eligible target link.
- **numeric_provenance_requirements:** sample/frame, variable derivations, size denominators, algorithm/seed, resampling/specification diagnostics and uncertainty; discovered segment sizes remain model/sample scoped unless separately estimated.
- **ethics_privacy_and_escalation:** assess exclusion, discrimination, vulnerability, sensitive/proxy features and harmful targeting; stop or escalate when segmentation creates unlawful/unacceptable harm or unsupported high-stakes action.
- **domain_adapter_hooks:** B2B purchase situation/role, B2C occasion/household, SaaS account behavior, local geography/time, marketplace side, education/accessibility, regulated constraints.
- **rule_and_source_ids:** `R-SEG-01`, `R-SEG-02`, `R-SEG-03`, `R-SEG-04`; `S-DOLNICAR`, `S-SEG-STABILITY`.

**Escalate/stop:** fail closed when no decision action differs, measurement/frame is materially invalid, or a discovered solution lacks reproducible provenance. If stability/usefulness is weak, retain candidate-segment status and route targeted validation instead of hardening personas.
