# Method Cards — Pricing and Transactions

Cards implement the Section 10.4 contract. Version `1.5.0`. Pricing and transaction cards keep stated preference, actual payment, and assisted-delivery evidence in separate claim lanes; none of the three licenses the others' claims.

## `STATED_PRICING_WTP`

- **supported_proposition_types:** `STATED_PREFERENCE_OR_WTP` under a named elicitation method (open-ended, ladder/Gabor-Granger, Van Westendorp, conjoint/discrete-choice, incentive-aligned).
- **unsupported_proposition_types:** `ACTUAL_TRANSACTION`/actual payment, universal price acceptance, market-wide demand.
- **required_evidence_dimensions:** method-specific instrument, price framing, incentive realism, sampling, uncertainty; product/offer, price/currency, taxes/fees/terms, quantity, channel, elicitation method, decision window.
- **minimum_design_conditions:** elicitation method named and matched to the decision — open-ended explores language/ranges; ladder/Gabor-Granger estimates stated acceptance across presented prices; Van Westendorp maps stated price perceptions, not a proven revenue-maximizing price; conjoint/discrete-choice designs estimate tradeoffs under model and task assumptions; incentive-aligned mechanisms are documented when used; hypothetical-bias risk is disclosed without applying a fixed correction.
- **sample_and_unit_requirements:** respondent sample matched to the target buyer/decision population; size follows precision/model-estimation logic for the chosen method, not a universal N.
- **instrument_or_stimulus_requirements:** price-framing stimulus (product/offer, price ladder or choice sets, currency/taxes/fees/terms, quantity, channel), pretested wording, incentive-alignment mechanism if used.
- **fieldwork_and_quality_controls:** framing/order control, attention/quality checks, elicitation-method fidelity check, deviation log.
- **analysis_path_and_estimand:** stated response, acceptance, perception, or tradeoff estimate under the named method and its own assumptions, bounded to the `STUDIED_SAMPLE` with model-based uncertainty when modeled (e.g., conjoint utilities).
- **assumptions_and_known_biases:** hypothetical bias with no fixed correction factor; framing/anchoring effects; method-performance variance by context; intention-behavior gap.
- **common_failure_modes:** applying a fixed hypothetical-bias discount (for example, treating a published corpus average such as “21% hypothetical bias” as a universal correction); treating a Van Westendorp intersection as a proven optimal price; reporting stated WTP as if it were an actual-payment claim.
- **allowed_claim_templates:** “Under elicitation method M (framing F), respondents' stated WTP/acceptance/tradeoff was X, hypothetical-bias-sensitive and not corrected by a universal factor.”
- **forbidden_claim_patterns:** “Customers will pay $X” as fact; “this is the revenue-maximizing price”; any claim that stated WTP equals or predicts actual payment without separate transaction evidence.
- **numeric_provenance_requirements:** price/currency, taxes/fees/terms, quantity, channel, elicitation method, sample/frame, model assumptions (for conjoint/discrete-choice), uncertainty.
- **ethics_privacy_and_escalation:** avoid deceptive price framing beyond disclosed research purpose; escalate regulated pricing-claim contexts (financial, insurance) before release.
- **domain_adapter_hooks:** B2B buying-system pricing-role context, SaaS tiered-pricing structure, regulated-industry price-claim review.
- **rule_and_source_ids:** `R-PRICE-01`, `R-PRICE-02`, `R-NUMERIC-01`; `S-WTP-META`, `S-WTP-METHOD`, `S-MORWITZ`.

**Escalate/stop:** fail closed if the report converts a stated-WTP result into an actual-payment or universal-acceptance claim. Route to `ACTUAL_PAYMENT_PAID_PILOT` when the decision requires transaction evidence instead of stated intent.

## `ACTUAL_PAYMENT_PAID_PILOT`

- **supported_proposition_types:** `ACTUAL_TRANSACTION` — occurrence of payment/transaction under a named offer and conditions.
- **unsupported_proposition_types:** market-wide willingness to pay or price acceptance, retention, scalable demand.
- **required_evidence_dimensions:** real price/terms, channel/eligibility, payment verification, refunds/cancellations, support, delivery, assistance, repeat/renewal when relevant.
- **minimum_design_conditions:** real price and terms published; channel and eligibility defined; payment-verification mechanism in place; refund/cancellation policy operative; support/delivery process ready before the pilot opens.
- **sample_and_unit_requirements:** eligible/offered population as the denominator; buyer/account/transaction unit fixed; nested repeat transactions from one buyer do not expand the buyer denominator (Section 12.1).
- **instrument_or_stimulus_requirements:** offer page/terms, payment-processing instrumentation, discount/incentive documentation, delivery/support scripts.
- **fieldwork_and_quality_controls:** payment-verification QC, refund/cancellation tracking, assistance/manual-intervention log, deviation log.
- **analysis_path_and_estimand:** payment occurrence and terms analysis bounded to the eligible/offered population, channel, and conditions under which the offer ran; no extension to untested channels, populations, or prices.
- **assumptions_and_known_biases:** small/early-adopter sample non-representativeness, assisted-sale effects, discount/incentive distortion, novelty effects.
- **common_failure_modes:** reporting one paid pilot as market-wide price acceptance; ignoring refunds/cancellations in the payment count; presenting assisted or discounted sales as proof of unit economics.
- **allowed_claim_templates:** “Under offer O (price P, terms T, channel C, eligibility E), N of M eligible/offered buyers paid, with refund/cancellation rate R.”
- **forbidden_claim_patterns:** “This proves the market will pay $X”; “retention is proven”; an assisted or discounted pilot's sales reported as scalable self-service demand.
- **numeric_provenance_requirements:** price/currency/terms, eligible/offered denominator, payment-verification method, refund/cancellation counts, discount/incentive terms, uncertainty.
- **ethics_privacy_and_escalation:** payment/financial-data handling and consumer-protection compliance; escalate regulated-sales or financial-services contexts before scaling.
- **domain_adapter_hooks:** SaaS trial-to-paid conversion context, local/physical-channel transaction context, marketplace side-specific payment flows.
- **rule_and_source_ids:** `R-PAYMENT-01`, `R-PRICE-01`, `R-NUMERIC-01`; `S-TRANSPORT`.

**Escalate/stop:** fail closed if the report extends one pilot's payment result into a market-wide acceptance, retention, or scalability claim without separate transport evidence. Escalate financial/consumer-protection review before scaling the offer.

## `CONCIERGE_WIZARD_OF_OZ`

- **supported_proposition_types:** `IMPLEMENTATION_OR_FEASIBILITY` (workflow value/use) under assisted/manual delivery; `ACTUAL_TRANSACTION` when payment occurs under the assisted offer.
- **unsupported_proposition_types:** scalable/self-service adoption, unit economics, market-wide demand.
- **required_evidence_dimensions:** assistance log, eligibility, offer/support, repeat window, operational deviations; every human/manual intervention, participant awareness where ethically required, offer/price, channel, operational cost, completion, repeat opportunity, failure, and the counterfactual unassisted path.
- **minimum_design_conditions:** manual-assistance log designed before fieldwork; eligibility and offer/support terms defined; repeat-opportunity window set; operational-deviation logging in place; participant-awareness disclosure resolved through ethics review before launch.
- **sample_and_unit_requirements:** eligible/offered participant/case population as the denominator; case unit tracked with assistance level recorded per case.
- **instrument_or_stimulus_requirements:** assistance-log template, offer/support script, operational-cost tracking sheet, counterfactual-unassisted-path documentation.
- **fieldwork_and_quality_controls:** manual-intervention log completeness check, operational-deviation log, completion/failure tracking, cost tracking.
- **analysis_path_and_estimand:** value/workflow and operational-feasibility analysis under the delivered assisted-support level only; explicitly excludes any unassisted/self-service inference.
- **assumptions_and_known_biases:** assistance masks unresolved self-service friction; small/early case sample; operational cost under manual delivery is not representative of scaled cost.
- **common_failure_modes:** reporting assisted-pilot success as proof of scalable self-service adoption; omitting the assistance log; presenting operational cost under manual delivery as the scaled unit economics.
- **allowed_claim_templates:** “Under assisted delivery (assistance log A, offer O), N of M eligible cases completed/used the workflow, with operational cost C under manual conditions; self-service/scale evidence is separate and not yet collected.”
- **forbidden_claim_patterns:** “This proves the product scales”; “unit economics are proven”; “customers adopted this independently” from an assisted pilot.
- **numeric_provenance_requirements:** eligible/offered denominator, assistance-log entries, completion/failure counts, operational cost, repeat-window results, uncertainty.
- **ethics_privacy_and_escalation:** participant-awareness disclosure where ethically required; escalate when manual assistance masks a safety/quality condition that would not exist in an unassisted deployment.
- **domain_adapter_hooks:** SaaS assisted-onboarding context, local/physical-service delivery context, regulated-service assistance disclosure.
- **rule_and_source_ids:** `R-CONCIERGE-01`, `R-PAYMENT-01`, `R-NUMERIC-01`.

**Escalate/stop:** fail closed if the report extends assisted-pilot results into a scalable/self-service adoption or unit-economics claim without separate scale evidence. Escalate if manual assistance appears to be concealing a condition necessary for safe or quality delivery at scale.
