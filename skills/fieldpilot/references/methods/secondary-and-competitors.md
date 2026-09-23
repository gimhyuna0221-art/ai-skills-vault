# Method Cards — Secondary Evidence and Alternatives

Cards implement the Section 10.4 contract. Version `1.5.0`. Route through `../METHOD_ROUTER.md`; pass all numeric outputs through Numeric Provenance and all prose through the Claim-Grammar Gate.

## `SECONDARY_DESK`

- **supported_proposition_types:** `DESCRIPTIVE_DISTRIBUTION` when an eligible existing estimate matches; `MARKET_MAGNITUDE` inputs; `COMPETITIVE_OR_SUBSTITUTION`; `SAFETY_OR_CONSTRAINT`; orientation for any proposition.
- **unsupported_proposition_types:** current target behavior, lived experience, WTP/payment, causal effect, or demand unless the inspected source directly measured the same proposition with an eligible design and transport basis.
- **required_evidence_dimensions:** definition/unit, population/geography/time, method/sample/frame, original provenance, independence/conflict, target similarity, uncertainty.
- **minimum_design_conditions:** define the exact fact sought; search original/authoritative sources proportionate to stakes; inspect the original where possible; distinguish primary, secondary, snippet, vendor-controlled and syndicated material; record contradictory/newer evidence.
- **sample_and_unit_requirements:** preserve the source's unit, population, sampling/design, inclusion/exclusion and denominator. A source corpus is not independent when items trace to the same study.
- **instrument_or_stimulus_requirements:** reproducible query/source-selection criteria, extraction form, access date, exact table/page/variable, translation/definition mapping.
- **fieldwork_and_quality_controls:** publisher/author/identifier, publication/revision date, funding/conflict, original-access status, date/context fit, duplicate lineage, source correction/retraction check.
- **analysis_path_and_estimand:** structured extraction, definition alignment, conflict map, target-transfer assessment; synthesis only after independence and comparability review.
- **assumptions_and_known_biases:** publication/availability bias, outdated context, source incentives, definitional mismatch, missing grey/local evidence, transport uncertainty.
- **common_failure_modes:** search snippet as evidence; duplicated syndication as convergence; press release as neutral truth; current target claim from a distant source; missing denominator/unit/date.
- **allowed_claim_templates:** “Inspected source S reports X for population P, geography G, period T, using method M”; “Source S informs assumption A with transfer caveat C.”
- **forbidden_claim_patterns:** “The target market is X” from an uninspected/indirect source; “several articles prove X” when they share one source; source assertion converted to direct target evidence.
- **numeric_provenance_requirements:** value/range, numerator, denominator/base, unit, population, geography, period, currency/base year, exact source locator, original/derived, transformation, uncertainty and rounding.
- **ethics_privacy_and_escalation:** respect access/licensing/confidentiality; stop high-stakes reliance when the original is unavailable or scope cannot be reconciled; label `SECONDARY_UNVERIFIED` and block it as the sole high-stakes basis.
- **domain_adapter_hooks:** jurisdiction/version check, unfamiliar-domain glossary, regulated authority, local catchment/time, B2B role/source ownership.
- **rule_and_source_ids:** `R-DESK-01`, `R-NUMERIC-01`, `R-SOURCE-01`; `S-ESOMAR`, `S-AAPOR-DISC`.

**Escalate/stop:** seek a qualified source/domain reviewer when applicability, legal force, technical definition, or transfer is decision-critical and unresolved. Stop the proposition as `NOT_CURRENTLY_ANSWERABLE` when no inspected source or valid primary route can meet its contract.

## `COMPETITOR_ALTERNATIVE`

- **supported_proposition_types:** `COMPETITIVE_OR_SUBSTITUTION`, `MECHANISM_OR_JOB`, `BUYING_SYSTEM`, and selected `IMPLEMENTATION_OR_FEASIBILITY` questions about available choices, switching, and workflow.
- **unsupported_proposition_types:** preference, willingness to switch/pay, current target demand, prevalence, retention, or causality from feature/offer presence alone.
- **required_evidence_dimensions:** decision-relevant alternative universe, comparable dimensions, source type/control, observed versus claimed behavior, switching/no-action context, evidence gaps.
- **minimum_design_conditions:** define the decision and selection criteria; include proportionately direct competitors, indirect substitutes, manual/internal workarounds, adjacent/bundled services, paid incumbents/switching costs, delay/tolerance/do nothing.
- **sample_and_unit_requirements:** sample alternatives and evidence sources by target use case/channel/geography, not search rank alone; preserve customer/account/site/time units behind use or commercial evidence.
- **instrument_or_stimulus_requirements:** Alternative Map with documented offer/availability/pricing/target, vendor claims, observed purchase/use/renewal/switching/complaint/workaround, selection context, and gaps.
- **fieldwork_and_quality_controls:** dated source capture, comparable definitions/terms, vendor-control label, direct observation/interview provenance, search limits and missing-category review.
- **analysis_path_and_estimand:** compare alternatives on decision-relevant jobs, tradeoffs, switching friction, reachability and evidence strength; keep offer facts, source assertions, and independently observed behavior separate.
- **assumptions_and_known_biases:** search visibility, survivor/popularity bias, regional/version differences, unknown internal workarounds, founder framing, nonindependent reviews.
- **common_failure_modes:** feature list = preference; competitor existence = demand validation; absence from search = absence from market; popularity = target fit; user anecdote transported beyond observed case.
- **allowed_claim_templates:** “Alternative A documents offer/term X as of T”; “In observed/interviewed cases C, workaround W was used under context K”; “Doing nothing remains an unmeasured/observed alternative.”
- **forbidden_claim_patterns:** “Customers prefer us”; “The market is validated”; “There are no competitors”; “Users will switch” without eligible direct evidence.
- **numeric_provenance_requirements:** price/usage/share/review counts retain source, unit, denominator/base, geography, date, terms and uncertainty; vendor numbers stay vendor-controlled.
- **ethics_privacy_and_escalation:** use lawful, nondeceptive collection; do not impersonate buyers or access protected systems; escalate confidential/proprietary or regulated comparisons.
- **domain_adapter_hooks:** B2B incumbent/procurement/renewal roles, physical/local channel and switching, marketplace side alternatives, unfamiliar-industry workarounds.
- **rule_and_source_ids:** `R-COMP-01`, `R-COMP-02`, `R-DESK-01`, `R-NUMERIC-01`.

**Escalate/stop:** if the active decision depends on why targets choose/switch, route complementary direct human/behavior/transaction evidence. If the map omits a decision-relevant alternative class, mark it incomplete for this proposition rather than universally invalid.

**v1.9.4:** before asserting the forbidden-pattern-adjacent claim "there are no competitors," "no strong
direct competitor," or "white space," run `DIRECT_COMPETITOR_RECALL_CLOSURE`
(`references/modules/BOUNDED_BEHAVIORAL_CLOSURE_REPAIR.md` §2). A near-exact candidate surfaced by that
closure search must enter the Alternative Map before the claim ships; an incomplete closure search
downgrades the claim to `SEARCHED_NOT_FOUND` / `COVERAGE_INCOMPLETE` rather than a bare absence claim.

### v1.9.9-rc02 — LOCAL_GEOGRAPHY_CLOSURE

When geography is established and materially changes the buyer's alternatives, the `COMPETITOR_ALTERNATIVE` map must not be satisfied by a global-only search.

For the active geography, proportionately close the relevant classes:
- local direct competitors;
- local adjacent/bundled incumbents or services;
- local manual/internal workarounds;
- do-nothing/tolerance;
- local pricing/terms/switching conditions when decision-material.

For Korea, route the local source/channel details through `../modules/KOREA_LOCAL_DISTRIBUTION.md`.

If geography is unresolved:
- do not infer it from conversation language or owner location;
- mark the affected competitor coverage `LOCAL_GEOGRAPHY_NOT_CHECKED` or `GEOGRAPHY_UNRESOLVED`;
- if the missing geography can change the recommendation, ask the minimum one question or lower the claim ceiling.

A local search miss is `LOCAL_DIRECT_SEARCHED_NOT_FOUND`, not "no local competitor" and not `CONFIRMED_GAP`.

