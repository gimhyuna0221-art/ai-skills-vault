# Primary Research Platform Bridge — method-parity-01

Use after an irreducible primary-research EVIDENCE GAP has been identified and a method is being
designed/selected. This module turns professional research requirements into platform capabilities.
It does not make FieldPilot a survey-hosting/panel/SSO product and does not require a specific vendor.

## 1. Research-design chain

Preserve the chain:

```text
BUSINESS QUESTION
-> RESEARCH OBJECTIVE
-> TARGET POPULATION / EVIDENCE HOLDER
-> CONSTRUCT / CLAIM
-> METHOD
-> INSTRUMENT
-> ACCESS / COLLECTOR
-> SAMPLE / FIELDWORK
-> ANALYSIS
-> FINDING
-> INTERPRETATION
-> RECOMMENDATION / ACTION
```

A later step may not silently redefine an earlier one. If the collector/platform cannot preserve
the required design, choose another route or narrow the claim.

## 2. Platform capability audit

Before recommending or using an external platform, verify the currently needed capabilities from
official/current documentation or an authorized live account. Do not infer from brand reputation.

```yaml
PLATFORM_CAPABILITY_AUDIT:
  job:
  current_access_state:
  instrument_builder:
  required_answer_validation:
  screening_and_eligibility:
  skip_or_branch_logic:
  answer_piping_or_prefill:
  question_choice_block_randomization:
  quotas_or_composition_controls:
  multilingual_and_translation_workflow:
  accessibility_requirements:
  collector_modes: []
  email_sms_qr_web_embed_offline_modes:
  respondent_panel_or_recruitment:
  identity_fraud_duplicate_quality_controls:
  response_metadata_and_dispositions:
  export_formats:
  analysis_crosstabs_stats_text:
  API_or_MCP_integrations:
  collaboration_permissions_security:
  data_region_retention_privacy:
  cost_or_credit_state:
  terms_and_use_limits:
  verified_at:
  unsupported_or_unknown: []
```

Only fields required by the active design need to be checked.

## 3. Instrument compilation

For surveys/concept tests where applicable, explicitly resolve:
- eligibility/screener and disqualification;
- consent/privacy language;
- question wording and response scales;
- required vs optional answers;
- validation/range rules;
- display/skip/branch conditions;
- answer or metadata piping/prefill;
- question/answer/block randomization when order effects matter;
- quotas as achieved-composition controls, never proof of probability sampling;
- multilingual versions and the translation/adaptation protocol;
- mobile/accessibility constraints;
- pilot/pretest and version lock;
- expected participant burden;
- attention/fraud/duplicate checks;
- completion/disposition states.

Do not add advanced logic merely because a platform supports it. Every logic rule must serve a
method or respondent-experience purpose and be testable before launch.

## 4. Collector / mode plan

Collector mode can change who responds and how they answer. Record, when relevant:
- channel/source (panel, email, web link, social, QR, SMS, website intercept, in-product, kiosk,
  offline, moderated);
- invitation and reminder cadence;
- identity/recontact rules;
- access restrictions/password/IP or device controls;
- mode-specific accessibility and privacy;
- response/read/click metadata if used;
- mode effect / coverage / nonresponse implications.

Combining modes is allowed only with explicit harmonization and analysis treatment.

## 5. Capability classes — broker instead of rebuild

FieldPilot should route to a task-fit specialist capability rather than reimplementing infrastructure.

Current example classes (provider examples are replaceable and must be re-verified):
- SURVEY_BUILD_AND_LOGIC: SurveyMonkey, Qualtrics, Typeform.
- RESPONDENT_PANEL / RECRUITMENT: SurveyMonkey Audience, Prolific, Pollfish and comparable providers.
- CONSUMER / AUDIENCE DATA: GWI, SparkToro, Statista Consumer Insights and comparable services.
- MARKET / CATEGORY DATA: official statistics, trade groups, Statista-style databases, specialist
  research firms.
- DIGITAL COMPETITIVE INTELLIGENCE: Similarweb, Semrush and comparable sources.
- SOCIAL / CONSUMER LISTENING: Brandwatch and comparable services.
- WEB / MULTI-CHANNEL RETRIEVAL: native tools, Firecrawl, Agent Reach/upstream routes where authorized.
- DEEP-RESEARCH SYNTHESIS: current host or specialized research runtimes where they add value.

These examples are not a permanent ranking and do not imply access, subscription, accuracy or data
ownership. Select by the evidence job, actual output, current scope and total user burden.

Load `references/data/MARKET_RESEARCH_CAPABILITY_CATALOG.md` when platform selection is material.

## 6. Permission / privacy / cost

Connected or discoverable services do not authorize:
- uploading private customer/company data;
- buying panel responses;
- starting paid plans;
- sending invitations/SMS/email;
- publishing results.

Obtain user authorization at the actual external-action boundary. Prefer already-authorized routes
and existing subscriptions where they meet the method.

## 7. Infrastructure is not evidence

A sophisticated survey platform, large panel, dashboard, API, AI analysis feature or beautiful
export does not validate the research by itself. FieldPilot's sample, construct, claim, provenance,
ethics and analysis rules remain governing.
