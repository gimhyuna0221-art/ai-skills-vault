# FieldPilot v1.5 Expert Core Rules

This file is the versioned rule snapshot for the v1.5.0 runtime. Load it for every
FieldPilot research cycle. The runtime MUST keep `source_class`, `maturity`,
`enforcement`, `applicability`, `transfer_caveat`, and `source_ids` independent.
`HARD` means the runtime fails closed; it does not mean the underlying research is
universally established. A rule not listed here defaults to
`E / HEURISTIC / GUIDANCE` until reviewed and versioned.

## Enforcement protocol

1. Pin this snapshot to every active research object and recommendation.
2. Evaluate applicability before enforcing `CONDITIONAL_HARD`; record the facts,
   jurisdiction/domain, conclusion source, and reviewer. A model-derived
   applicability conclusion is `INFERRED`, never self-confirming.
3. If a required module, rule, or source record is missing, block only the affected
   expert claim or fieldwork action and state the nearest valid repair.
4. Never promote a preprint, working paper, vendor-supported study, industry
   experiment, or class-D source into a universal hard empirical rule.
5. Preserve the prior snapshot when a rule changes; recursively stale only dependent
   active revisions and create a new revalidation revision.

## Normative registry (68 rules)

| Rule ID | Runtime rule | Class | Maturity | Enforcement | Source IDs / boundary |
|---|---|:---:|---|---|---|
| `R-DEC-01` | A visible impact × belief-risk × urgency aid may prioritize uncertainties; it is overridable and not a validated market metric. | E | HEURISTIC | GUIDANCE | Native decision aid. |
| `R-ARCH-01` | Route methods from the proposition and required evidence; there is no universal method hierarchy. | E | SUPPORTED | HARD | `S-SHMUELI`, `S-AAPOR-NP`, `S-TRANSPORT`; taxonomy is native. |
| `R-ARCH-02` | Compile the Required Evidence Contract before optimizing acquisition. | E | SUPPORTED | HARD | Contract vector is native. |
| `R-ACCESS-01` | Access difficulty cannot silently lower evidence for an unchanged claim. | E | HEURISTIC | HARD | Product-governance invariant. |
| `R-STATE-01` | Keep provenance, verification, method validity, execution, approval, and resolution independent. | E | HEURISTIC | HARD | Native audit architecture. |
| `R-CLAIM-01` | Every material claim must fit evidence-compatible subject, quantifier, construct, verb, causal force, behavioral level, scope, and precision. | E | SUPPORTED | HARD | `S-DRISKO`, `S-AAPOR-NP`, `S-TRANSPORT`, `S-MORWITZ`. |
| `R-FIR-01` | Findings, Interpretations, and Recommendations are distinct traceable objects. | C | ESTABLISHED | HARD | `S-ESOMAR`, `S-SRQR`, `S-CONSORT`; schemas are native. |
| `R-SOURCE-01` | Every major rule stores class, maturity, enforcement, scope, and transfer caveat. | E | HEURISTIC | HARD | Native source governance. |
| `R-DESK-01` | External claims retain original provenance, definition, context, date, conflict, and inference boundary. | C | SUPPORTED | HARD | `S-ESOMAR`, `S-AAPOR-DISC`. |
| `R-COMP-01` | Map proportionate direct, indirect, workaround, incumbent, and do-nothing alternatives. | E | HEURISTIC | GUIDANCE | Native Alternative Map; no completeness count. |
| `R-COMP-02` | Keep vendor-controlled assertions distinct from independently observed behavior, purchase, use, or market evidence. | C | SUPPORTED | HARD | `S-ESOMAR`, `S-AAPOR-DISC`. |
| `R-SIZE-01` | Market size is a constructed estimate with definition, units, lineage, uncertainty, and sensitivity. | E | SUPPORTED | HARD | `S-GAO`, `S-JCGM`, `S-FORECAST`; sizing schema is native. |
| `R-SIZE-02` | No universal TAM/SAM/SOM formula, arbitrary SOM percentage, precision, or accuracy threshold. | E | HEURISTIC | HARD | Anti-false-precision rule. |
| `R-SEG-01` | Data-driven segments retain analytic provenance and remain model results. | A | SUPPORTED | HARD | `S-DOLNICAR`. |
| `R-SEG-02` | Assess stability and decision usefulness when fitted segments will drive decisions. | A | SUPPORTED | CONDITIONAL_HARD | `S-SEG-STABILITY`; no universal cutoff. |
| `R-SEG-03` | A-priori segment labels remain hypotheses until decision-relevant difference, reachability, and usefulness are evidenced. | E | HEURISTIC | HARD | Native actionability guard. |
| `R-SEG-04` | No universal segmentation algorithm, count, minimum size, or stability cutoff. | E | SUPPORTED | HARD | `S-DOLNICAR`, `S-SEG-STABILITY`. |
| `R-QUAL-01` | Qualitative sample size requires study-specific rationale; no universal N or saturation threshold. | B | SUPPORTED | HARD | `S-INFO-POWER`, `S-SAT-REVIEW`, `S-SAT-MEANING`. |
| `R-QUAL-02` | Qualitative counts and patterns stay bounded to studied cases absent separate population evidence. | B | SUPPORTED | HARD | `S-DRISKO`, `S-SRQR`. |
| `R-QUAL-03` | Record sampling, setting, reflexivity, collection/analysis, changes, negative cases, links, and limitations. | B | SUPPORTED | HARD | `S-SRQR`, `S-COREQ`; checklists are not scores. |
| `R-OBS-01` | Observation supports behavior/process in sampled settings; motive, voluntariness, and prevalence need separate evidence. | E | SUPPORTED | HARD | `S-SRQR`, `S-ISO-USABILITY`. |
| `R-FOCUS-01` | Focus-group evidence records interaction, dominance, dissent, privacy, and never becomes independent prevalence. | B | SUPPORTED | HARD | `S-COREQ`, `S-SRQR`; no universal group count. |
| `R-DIARY-01` | Diary evidence stays participant/window/mode-bound with adherence, missingness, and event verification visible. | E | HEURISTIC | HARD | No universal duration or cadence. |
| `R-SURVEY-01` | Evaluate coverage, selection/nonresponse, measurement, processing, weighting/modeling, and sampling error. | B | ESTABLISHED | HARD | `S-TSE`; apply proportionately. |
| `R-SURVEY-02` | Nonprobability results default to sample scope; population inference needs target-link assumptions, diagnostics, and model uncertainty. | C | ESTABLISHED | HARD | `S-AAPOR-NP`, `S-CORNESSE`. |
| `R-SURVEY-03` | Conventional sampling MOE requires an eligible probability design and design-effect disclosure. | C | ESTABLISHED | HARD | `S-AAPOR-MOE`; label model-based intervals differently. |
| `R-SURVEY-04` | Weighting does not automatically confer representativeness. | B | SUPPORTED | HARD | `S-CORNESSE`; require diagnostics and residual caveat. |
| `R-USABILITY-01` | Separate concept response, usability, actual-use performance/safety, adoption, and demand. | E | SUPPORTED | HARD | `S-ISO-USABILITY`, `S-FDA-HF`; cross-construct gate is native. |
| `R-CONCEPT-01` | Concept tests support comprehension and response to shown stimuli, not usability, purchase, retention, or performance. | E | SUPPORTED | HARD | `S-ISO-USABILITY`, `S-MORWITZ`. |
| `R-BEHAVIOR-01` | Behavioral claims retain opportunity denominator, instrumentation, voluntariness, assistance, context, and time. | E | SUPPORTED | HARD | Record schema is native. |
| `R-FAKEDOOR-01` | Fake doors establish contextual interest behavior only and require trust/deception controls. | E | HEURISTIC | HARD | `S-FAKEDOOR`; no universal threshold. |
| `R-PRICE-01` | Stated WTP or purchase intention is distinct from actual payment or behavior. | A | SUPPORTED | HARD | `S-WTP-META`, `S-WTP-METHOD`, `S-MORWITZ`. |
| `R-PRICE-02` | No fixed stated-WTP correction factor or universal best elicitation method. | A | SUPPORTED | HARD | `S-WTP-META`; moderators are contextual. |
| `R-PAYMENT-01` | Actual payment establishes a contextual transaction, not market-wide price acceptance. | E | SUPPORTED | HARD | `S-TRANSPORT`. |
| `R-CONCIERGE-01` | Concierge/Wizard-of-Oz evidence retains manual assistance and supports only the delivered context absent scale/self-service evidence. | E | HEURISTIC | HARD | No universal assistance threshold. |
| `R-EXP-01` | Valid random assignment supports a bounded causal estimand for eligible units, treatment, outcome, and window. | A | ESTABLISHED | HARD | `S-ONLINE-EXP`, `S-CONSORT`. |
| `R-EXP-02` | Check assignment/exposure, SRM, exclusions, missingness, predeclared metrics, multiplicity/peeking, effects/intervals, harms, and practical significance. | A | SUPPORTED | HARD | `S-SRM`, `S-ASA`; no universal p-value, duration, or MDE. |
| `R-EXP-03` | Internal causal validity does not automatically transport across population, channel, market, or time. | B | ESTABLISHED | HARD | `S-TRANSPORT`. |
| `R-EXP-04` | Check interference for networks, marketplaces, classrooms, teams, and local spillovers. | A | SUPPORTED | CONDITIONAL_HARD | `S-INTERFERENCE`; no universal estimator. |
| `R-QUASI-01` | Quasi-causal claims require identification assumptions, comparator diagnostics, violation tests, and bounded language. | E | SUPPORTED | HARD | `S-CAUSAL-LANG`, `S-TRANSPORT`, `S-WWC`. |
| `R-NEG-01` | Before recommendation, inspect negative cases, missing groups, harms, and rival explanations proportionately. | B | SUPPORTED | HARD | `S-DISSONANCE`, `S-ESOMAR`; no fixed count. |
| `R-TRI-01` | Multiple methods do not automatically validate; record convergence, complementarity, and divergence. | B | SUPPORTED | HARD | `S-TRIANGULATION`. |
| `R-CAUSAL-LANG-01` | Observational association cannot silently become causal or action language. | B | SUPPORTED | HARD | `S-CAUSAL-LANG`; semantic boundary is general. |
| `R-NUMERIC-01` | Material numbers require complete unit/base/source/formula/uncertainty provenance. | E | SUPPORTED | HARD | Ledger is native. |
| `R-AI-01` | Synthetic respondents are model-derived cases, never human participants or human evidence. | C | ESTABLISHED | HARD | `S-AAPOR-CODE`, `S-SYNTH-PERILS`, `S-SILICON-REVIEW`. |
| `R-AI-02` | Synthetic use is limited to labeled upstream hypothesis, instrument, failure-mode, or pipeline work unless experimentally approved. | E | EMERGING | HARD | `S-SILICON-REVIEW`; boundary is native. |
| `R-AI-03` | Human-anchored rectification needs held-out humans, a human-only comparator, estimand, diagnostics, uncertainty, and revalidation; it cannot lower the human floor. | E | EMERGING | CONDITIONAL_HARD | `S-RECTIFICATION`; limited contexts. |
| `R-AI-04` | AI moderation needs disclosure/consent, exact-system pilot, provenance, human oversight/escalation, and mode-labeled evidence. | C | SUPPORTED | CONDITIONAL_HARD | `S-MRS-AI`, `S-ESOMAR`, `S-AI-INTERVIEWER`. |
| `R-AI-05` | No human-moderator-equivalence claim without same-context real-human comparative validation. | E | EXPERIMENTAL | HARD | `S-AI-INTERVIEWER`; existing benchmark did not establish equivalence. |
| `R-AI-06` | Log material AI use and named human responsibility at every research phase. | C | SUPPORTED | HARD | `S-MRS-AI`, `S-ESOMAR`, `S-NIST-GENAI`, `S-UNESCO-AI`. |
| `R-ETHICS-01` | Require voluntary participation, harm minimization, privacy/data minimization, withdrawal, and added protection for vulnerable groups. | C | ESTABLISHED | HARD | `S-AAPOR-CODE`, `S-ESOMAR`, `S-BELMONT`; local duties vary. |
| `R-ETHICS-02` | Keep research separate from sales, promotion, fundraising, and lead transfer absent separate consent. | C | ESTABLISHED | HARD | `S-AAPOR-CODE`, `S-ESOMAR`. |
| `R-B2B-01` | Treat B2B evidence as a dynamic buying-system map; impose no fixed role count. | A | SUPPORTED | CONDITIONAL_HARD | `S-BUYING-CENTER`, `S-B2B-META`. |
| `R-ENTERPRISE-01` | User/champion/pilot evidence does not establish procurement, security, integration, deployment, or renewal. | E | SUPPORTED | HARD | `S-BUYING-CENTER`, `S-NIST-SCRM`. |
| `R-B2C-01` | Purchase intention remains stated evidence and does not establish conversion or repeat behavior. | A | ESTABLISHED | HARD | `S-MORWITZ`. |
| `R-SAAS-01` | Account, user, seat, event, activation, retention, and renewal are distinct; assisted/required use is not voluntary account adoption. | E | HEURISTIC | HARD | Native SaaS adapter. |
| `R-LOCAL-01` | Local evidence records site, catchment, daypart, season, and servicescape and remains context-bound; no default radius. | E | HEURISTIC | HARD | `S-SERVICESCAPE`, `S-CATCHMENT`. |
| `R-FNB-01` | Applicable food-safety, allergen, licensing, and operational constraints precede fieldwork and claims. | C | ESTABLISHED | CONDITIONAL_HARD | `S-FDA-FOOD`; jurisdiction-specific. |
| `R-PHYSICAL-01` | Concept/prototype evidence cannot establish actual-use safety, reliability, manufacturability, or demand. | E | SUPPORTED | HARD | `S-ISO-USABILITY`, `S-FDA-HF`. |
| `R-MARKETPLACE-01` | Two-sided markets require separate side propositions and cross-side evidence; one-side traction is insufficient. | E | SUPPORTED | HARD | `S-PLATFORM-RT`, `S-PLATFORM-ARMSTRONG`. |
| `R-NETWORK-01` | A network-effect claim requires an operational mechanism and network-exposure evidence, not growth or retention alone. | E | SUPPORTED | HARD | `S-NETWORK-EFFECTS`; no universal threshold. |
| `R-MEDIA-01` | Audience and advertiser evidence are separate; delivery, engagement, leads, intent, attribution, sales, and incrementality are distinct. | C | ESTABLISHED | HARD | `S-MRC`. |
| `R-EDU-01` | Engagement/completion is not learning; learning-effect claims need valid outcomes/design, correct units, and bounded generalization. | C | ESTABLISHED | HARD | `S-WWC`; exploration need not always be randomized. |
| `R-REG-01` | Resolve applicable jurisdiction, classification, consent/review, safeguarding, privacy, and reportable events before regulated/sensitive fieldwork. | C | ESTABLISHED | CONDITIONAL_HARD | `S-CIOMS`, `S-EPHMRA`, `S-BELMONT`. |
| `R-UNFAMILIAR-01` | Unfamiliar domains require a sourced system/glossary preflight; imported roles, KPIs, analogies, and rules stay hypotheses until validated. | E | HEURISTIC | HARD | Native anti-transfer guard. |
| `R-FIELD-01` | Distinguish non-contact, no response, ineligibility, research refusal, offer refusal, withdrawal, and quality exclusion. | E | HEURISTIC | HARD | Native disposition integrity rule. |
| `R-AUDIT-01` | Preserve stable IDs, raw evidence, lineage, revisions, deviations, stale dependencies, AI use, and the rule snapshot. | E | HEURISTIC | HARD | Native audit architecture. |
| `R-NOVICE-01` | Expose the nearest useful action, reasoned default, known/unknown/claimable boundaries, and progressive detail. | E | HEURISTIC | HARD | Product behavior, not a research theorem. |

## Deliberate non-rules

Never make universal defaults for method rankings; interview, focus-group, diary,
or usability N; ordinary opt-in MOE; representativeness after quotas/weighting;
TAM/SAM/SOM formulas or SOM percentages; segment count/algorithm/cutoff; fake-door,
waitlist, conversion, retention, churn, or liquidity thresholds; WTP discounts or
one best pricing method; A/B p-value, power, MDE, duration, traffic, or transport;
fixed B2B role taxonomies; local radii; automatic confidence from triangulation;
synthetic-human pooling or AI-human equivalence. A project-local threshold records
who chose it, why, the linked proposition/decision, and the consequence of missing
it.
