# AI and Synthetic Research Runtime

Load this module whenever AI affects a research phase, an AI system interacts with participants, synthetic respondents or simulated cases are proposed, or AI assists analysis/reporting. It operationalizes `R-AI-01` through `R-AI-06` and composes with `ETHICS_AND_PROFESSIONAL_STANDARDS.md`, `CLAIM_GRAMMAR.md`, and `AUDIT_STATE_SCHEMA.md`.

Core boundary: a model output is not a person, participant, customer, transaction, lived experience, or observed market behavior. Human and synthetic material never share an evidentiary denominator.

## 1. Phase-level AI ledger

For every project, record `NONE`, `ASSISTED`, `PARTICIPANT_FACING`, or `SYNTHETIC_GENERATION` for each phase:

```yaml
ai_usage:
  id_and_revision:
  phase: SCOPING | SOURCE_DISCOVERY_EXTRACTION | SAMPLING_RECRUITMENT | INSTRUMENT_STIMULUS | PARTICIPANT_MODERATION | TRANSCRIPTION_TRANSLATION | CODING_CLASSIFICATION | QUANT_ANALYSIS | INTERPRETATION | REPORT_DRAFTING | RECOMMENDATION
  use_state:
  provider:
  model_build_version:
  access_date:
  prompt_or_system_instruction_version:
  parameters_and_seed:
  governed_input_ids: []
  output_ids: []
  selection_and_transformation:
  known_limitations: []
  named_human_owner:
  human_review_method:
  review_result:
  material_override:
```

The human owner remains accountable. Log material defaults, classifications, summaries, translations, calculations, mappings, and prose even if the user accepts them.

### Data-minimizing provenance

Store reusable prompts and material configuration, not duplicated participant/confidential content. Represent sensitive inputs with access-controlled evidence IDs, redacted forms, or non-reidentifying integrity references only when lawful and useful. Provider-side prompts, logs, and outputs follow the project's consent, access, retention, deletion, withdrawal, confidentiality, and cross-border rules. Reproducibility never overrides those duties.

## 2. Provenance partitions

```text
HUMAN_PRIMARY         real participant's attributable response/behavior under the recorded mode
OBSERVED_SYSTEM       eligible system/transaction evidence with inspectable provenance
MODEL_DERIVED         AI code, estimate, classification, summary, or inference from governed inputs
SYNTHETIC_GENERATED   model-created person-like response, quote, case, event, or gap-fill
NOT_HUMAN_EVIDENCE    mandatory flag for every synthetic respondent output
```

Generated transcript repair, inferred answers, fabricated quotes, gap-fill, or model-written participant content is always `SYNTHETIC_GENERATED`, even when surrounded by a real transcript. Preserve the raw human record; never silently repair missing data.

## 3. Synthetic respondent policy

`Synthetic respondent` means any LLM or simulation asked to generate attitudes, experiences, choices, survey answers, interview responses, or behavior for an imagined person or population, including persona-conditioned, retrieval-grounded, or human-anchored variants.

### 3.1 Permitted labeled uses

- hypothesis, scenario, or failure-mode generation;
- wording, ambiguity, accessibility, and instrument red-teaming;
- analysis-pipeline rehearsal;
- synthetic test fixtures isolated from findings;
- exploratory technique evaluation under an approved experimental protocol.

These outputs carry:

```yaml
provenance_status: SYNTHETIC_GENERATED
human_evidence_status: NOT_HUMAN_EVIDENCE
governing_rule_maturity: EMERGING | EXPERIMENTAL
```

### 3.2 Hard prohibitions

- Keep `human_n` and `synthetic_n` separate. Never add, pool, or visually stack them as one sample.
- Synthetic outputs never count toward recruitment, response rate, probability, margin of error, effective human/sample N, qualitative saturation, negative-case coverage, voice-of-customer evidence, or participant quotations.
- They cannot establish human prevalence, lived experience, behavior, purchase, WTP, causal effect, segment size, learning, safety, or market demand.
- Do not call synthetic cases participants, customers, respondents, users, buyers, patients, learners, or advertisers.
- Do not use synthetic material to fill missing human data or make an undercovered subgroup appear covered.

Allowed claim grammar is limited to:

> Model M produced output or pattern P under prompt/configuration C.

Claims such as `customers prefer A`, `n=10,000 respondents`, `the segment would pay`, or `saturation was reached` are `BLOCKED_PROVENANCE` when the underlying cases are synthetic. The permitted rewrite must identify the model/configuration and show `human_n: 0` unless separate eligible human evidence exists.

## 4. Human-anchored rectification

Synthetic augmentation or rectification is `OPTIONAL_EXPERIMENT`, never the default. Before selection require:

```yaml
rectification_protocol:
  target_population:
  estimand:
  human_sampling_design:
  human_allocation:
  independent_held_out_human_validation:
  human_only_comparator:
  calibration_and_coverage_diagnostics:
  subgroup_diagnostics:
  synthetic_model_error_propagation:
  predeclared_failure_threshold:
  fallback_to_human_only:
  drift_and_revalidation_plan:
  model_prompt_data_provenance:
  qualified_owner_and_review:
```

If any field is missing, reject the technique for inferential use. Human observations remain the only human evidence and validity anchor. Vendor language such as `human-anchored` is not validation. The technique may change allocation only after explicit decision acceptance; it cannot silently lower the human-evidence floor in the Required Evidence Contract.

An approved study may report `model_assisted_estimator_efficiency` or another fully defined study-specific efficiency diagnostic only with its formula, human N, human-only comparator, uncertainty, validation, and failure boundary. It is not human N, recruited N, respondent count, response rate, representativeness, or ordinary human-sample precision.

## 5. AI-moderated human research

Real participants moderated by AI remain `HUMAN_PRIMARY` with `moderator_type: AI`. The mode is material and appears in consent, evidence, analysis, limitations, and reports.

### 5.1 Before collection

Disclose in understandable language:

- that the moderator is AI and the research purpose;
- recording/transcription and personal-data processing;
- relevant providers, third parties, transfers, and retention;
- foreseeable limitations and whether a human is monitoring;
- human contact, escalation, stop, and withdrawal routes;
- a non-AI alternative when legally required or materially needed for consent/accessibility.

Pilot the exact model/version, system prompt, guide, language, topic, target population, channel, and safety setup. A materially changed component invalidates the prior pilot/readiness decision.

### 5.2 Audit rubric

Record:

- non-leading openness and contextual relevance;
- follow-up judgment and unsupported assumptions;
- skips, repetition, tone/empathy, latency, dropout, and schema failures;
- differential disclosure and subgroup accessibility;
- privacy/data-handling conformance;
- adverse events, stop-rule triggers, and human escalation performance.

AI cannot be the sole safeguarding layer for distress, abuse, self-harm, minors, impaired consent, medical issues, or reportable regulated events. These contexts require an approved human escalation path, response-time coverage, stop rules, and domain review. Missing coverage is `BLOCKED_ETHICS`.

### 5.3 Equivalence boundary

Do not claim equivalence to human moderation without same-context comparative validation with real participants, predefined quality and safety endpoints, mode controls, subgroup/accessibility checks, dropout/adverse-event comparison, and uncertainty. Until such evidence exists for the active context, equivalence remains `EXPERIMENTAL` and is blocked as a substantive claim.

## 6. AI-assisted analysis and reporting

- Preserve raw evidence separately from AI summaries, translations, codes, and classifications.
- Trace every material model output to governed input IDs and the AI ledger record.
- Validate outputs against raw evidence with a documented human-review strategy proportionate to stakes.
- Preserve disagreement, negative cases, missing voices, and material model uncertainty.
- Never invent quotations, sources, participants, calculations, missing values, themes, or execution events.
- Do not use stylistic confidence to upgrade `MODEL_DERIVED` material.
- A named human signs off Findings, Interpretation, and Recommendation separately.
- Final reports disclose material AI use, provenance, limitations, and human oversight.

AI-generated Findings or rationale still need eligible evidence links and a passing ClaimGateDecision. AI may help draft a Recommendation, but cannot become the accountable decision owner or create factual support.

## 7. Runtime decision table

| Situation | Runtime outcome |
|---|---|
| Synthetic cases proposed as customer evidence | `BLOCKED_PROVENANCE`; offer only isolated upstream/test-fixture use |
| Synthetic and human rows pooled | Block analysis and denominator until separated |
| AI moderation with real adults, clear consent, exact-system pilot, and adequate oversight | Eligible with mode disclosure and context-bounded claims |
| AI moderation in sensitive context without approved live escalation | `BLOCKED_ETHICS` |
| AI transcript gap-fill presented as participant speech | Exclude as `SYNTHETIC_GENERATED`; preserve missingness |
| Rectification lacks held-out human validation or human-only comparator | Reject inferential use |
| AI-assisted coding with raw links and human audit | `MODEL_DERIVED`; eligible only after documented review and calibration |
| User approves an AI output | Approval changes only `approval_status`; provenance and verification do not change |

## 8. Audit and output requirements

Each AI-linked EvidenceItem, AnalysisResult, Finding, Interpretation, Recommendation, and ClaimGateDecision points to its `ai_usage` revision. If model/version or prompt changes materially, create a new revision and reassess dependencies. Withdrawal or deletion of governed human inputs triggers deletion/recalibration through the audit state; the AI ledger must not retain a recoverable copy.

The novice view says what AI did, what a human checked, and what the output cannot prove. Never imply that FieldPilot interviewed, recruited, observed, or generated real market evidence by itself.

## 9. Source and maturity hooks

- `R-AI-01`: Class C / ESTABLISHED / HARD; `S-AAPOR-CODE`, with research evidence from `S-SYNTH-PERILS` and `S-SILICON-REVIEW`.
- `R-AI-02`: Class E / EMERGING / HARD; permitted-use boundary is FieldPilot-native.
- `R-AI-03`: Class E / EMERGING / CONDITIONAL_HARD; `S-RECTIFICATION` is limited-domain evidence, not a universal rule.
- `R-AI-04`: Class C / SUPPORTED / CONDITIONAL_HARD; `S-MRS-AI`, `S-ESOMAR`, `S-AI-INTERVIEWER`.
- `R-AI-05`: Class E / EXPERIMENTAL / HARD; no human-equivalence promotion.
- `R-AI-06`: Class C / SUPPORTED / HARD; `S-MRS-AI`, `S-ESOMAR`, `S-NIST-GENAI`, `S-UNESCO-AI`.

Applicable law, professional standards, participant consent, and data-owner restrictions override convenience. Source maturity governs the rule, never the evidentiary status of a generated case.
