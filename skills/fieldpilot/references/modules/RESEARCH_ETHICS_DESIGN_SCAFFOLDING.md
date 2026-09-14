# Research Ethics Design Scaffolding — v1.7.2

`references/core/ETHICS_AND_PROFESSIONAL_STANDARDS.md` governs ethics for research that is **executed**.
This module closes a different gap: a deliverable that *recommends* research involving people must
carry the ethics scaffolding **into the proposed design**, not leave it to the reader.

It also fixes two adjacent disclosure gaps: confidentiality controls over AI processing of
client-provided material, and the ethical basis for secondary use of identifiable public posts.

Nothing here weakens `R-ETHICS-01` or `R-ETHICS-02`. Applicable legal obligations override this
minimum, and this module is not a substitute for qualified review.

Rule anchors: `R-ETHICS-01`, `R-ETHICS-02`, `R-OBS-01`, `R-QUAL-01`, `R-AI-04`, `R-AI-05`,
`R-AI-06`, `R-FIELD-01`, `R-REG-01`.
Source anchors: `S-ESOMAR`, `S-AAPOR-CODE`, `S-AAPOR-DISC`, `S-BELMONT`, `S-MRS-AI`; internet
research ethics anchor `V16-S30`.

## 1. Trigger

Attach `PARTICIPANT_RESEARCH_DESIGN_ETHICS` to **every** proposed, recommended or selected
direct-research method that involves people. This includes, and is not limited to:

- interviews, depth interviews and process-mapping conversations;
- surveys and questionnaires;
- observation of people at work, including front-desk, shop-floor and shift observation;
- usability, concept and prototype tests with real users;
- diary, longitudinal and shadowing designs;
- paid continuation and transaction tests where a real person decides and is recorded;
- any design that captures a person's behaviour, words, images, recordings or contact details.

The scaffolding attaches at **METHOD OPTIONS** time, not only after selection. A client reading the
options must be able to see what each design would require of participants.

It does not attach to desk-only work with no participants. In that case the delivery envelope
records `NOT APPLICABLE` with the reason, as it does today — that behaviour is correct and is
preserved.

## 2. PARTICIPANT_RESEARCH_DESIGN_ETHICS — required design fields

These are **design and disclosure fields to be filled by execution**. They are never pre-filled
with results, and never retro-filled as though fieldwork had occurred.

```text
PARTICIPANT_RESEARCH_DESIGN_ETHICS
  who_participates                    role, relationship to the user, how they are reached
  purpose_disclosed_to_participant    in comprehensible, non-technical language
  researcher_and_sponsor_identity     who is asking, and on whose behalf
  voluntary_participation             how voluntariness is made real, not merely stated
  consent_route                       how consent is obtained and recorded, and by whom
  participant_information             what participation involves, expected duration, what is
                                      recorded, foreseeable risks, incentives, and data use
  recording_and_transcription         whether audio, video, screen or notes are captured
  anonymity_and_confidentiality       what is protected, and the explicit limits of that protection
  data_handling                       minimization, storage location, access, retention period,
                                      deletion, and any third parties
  withdrawal                          right to skip questions and to stop at any time without
                                      penalty, and what happens to data already collected
  research_versus_sales_separation    per R-ETHICS-02; no disguised pitch, no lead transfer
  power_and_setting_considerations    see section 3
  accessibility_and_language
  additional_protections              children, vulnerable participants, sensitive contexts
  safety_and_escalation               stop conditions, distress handling, contact route
  fieldwork_status                    PLANNED / NOT_EXECUTED / EXECUTED
```

Rules:

- An unexecuted design field stays empty or `NOT YET RUN`. It is never filled with a plausible
  value that reads as though it happened.
- `fieldwork_status` is stated truthfully. `NOT_EXECUTED` is the correct and common answer for a
  desk deliverable that recommends research. It must not be softened into language implying the
  research occurred.
- Never fabricate a consent event, a participant, a recruitment, an interview, an observation, an
  ethics approval, or a QC pass. This is a fabrication in the same class as a fabricated source.
- Apply data minimization to safety fields. Do not collect broad health status, diagnosis or
  clinical detail for ordinary product research; use a narrow non-clinical stop-event flag instead.

## 3. Workplace, employer-mediated and power-asymmetric settings

Observing or interviewing people **at work** is a specific, common case that ordinary consent
language handles badly, and it is exactly the design most often recommended for early product
validation.

Where the design observes staff during their job, or where the person granting access is not the
person being observed:

```text
POWER_AND_ACCESS_RECORD
  who_grants_access                   e.g. owner, manager, site lead
  who_is_observed_or_interviewed      e.g. front-desk staff, shift workers
  consent_of_the_observed             separate from the access-granter's permission
  refusal_route                       how an individual can decline or stop without workplace cost
  what_the_access_granter_will_see    individual-level or aggregate only
  performance_use_boundary            research data must not be repurposed for staff evaluation,
                                      discipline or performance management
  customer_or_third_party_presence    how uninvolved people in the setting are handled
```

Employer permission is **access**, not consent. Record both, or state plainly that individual
consent is unresolved and must be resolved before fieldwork begins.

## 4. AI processing of client-provided material — confidentiality controls

When AI systems read, store, transmit or process client-provided documents, data or product
material, state the **actual** controls over that processing in the delivery envelope.

```text
AI_CLIENT_MATERIAL_CONFIDENTIALITY
  what_client_material_was_processed
  processing_route                    which systems and connectors actually touched it
  controls_in_place                   the real controls, or NONE, or UNKNOWN
  retention_and_training_status       what is known, or UNKNOWN
  third_party_exposure                who else could access it, or UNKNOWN
```

Rules:

- `NONE` and `UNKNOWN` are legitimate, and are frequently the truthful answer.
- **Never fabricate a control that did not occur.** Do not state encryption, isolation, deletion,
  a retention policy, a no-training guarantee, or an access restriction unless it is actually
  known to apply to this run.
- Do not infer a control from the fact that a vendor generally offers one.
- Where the answer is `UNKNOWN`, say so and state what the client would need to check. An honest
  `UNKNOWN` is a disclosure; a comforting invention is a misrepresentation.
- Where confidentiality genuinely was not impacted — for example the material processed was the
  client's own brief at the client's own direction, with no participant or third-party
  confidential data — say that, precisely, rather than claiming a control.

## 5. Secondary use of identifiable public and community posts

Forum, social and community posts are people's words, not anonymous data exhaust. When they are
used as secondary research evidence, record the basis.

```text
PUBLIC_POST_USE_RECORD
  why_admissible                      what this evidence is being used for
  evidence_role                       pain and workaround language, hypothesis generation, or
                                      context — never prevalence
  identifiability_handling            paraphrase by default; quote only where the exact wording
                                      is load-bearing, and keep it minimal
  individual_identification           do not name, profile, contact, or aggregate individuals
                                      across posts to reconstruct a person
  sensitive_content                   heightened care for health, financial, legal, employment or
                                      other sensitive disclosures; prefer exclusion
  platform_terms_and_context          the context the post was written in, and whether research
                                      reuse is consistent with it
```

Rules:

- Public availability is not consent to research use. This is a live ethical question, not a
  settled one (`V16-S30`).
- Community posts remain community signal. They never become prevalence, market size, segment
  share, or a customer count. This restates and does not weaken the existing evidence-class
  separation.
- Do not contact, recruit from, or reply to a post as a research approach without applying the
  full participant scaffolding in section 2.
- Where the post is identifiable and the point can be made without it, make the point without it.

## 6. Rendering in the deliverable

- For any recommended people-involving method, the ethics scaffolding is visible **with the
  method option**, not buried in end matter.
- The delivery envelope's ethics, privacy and confidentiality items are completed with what
  actually applies: `NOT APPLICABLE` with a reason for genuine desk-only work,
  `PLANNED / NOT_EXECUTED` for recommended designs, and real status for executed fieldwork.
- Sample QC and fieldwork QC items are populated only by what actually happened.

## 7. Failure modes this module exists to prevent

- Recommending that a client observe staff at work, or interview named roles, with no consent,
  participant information, confidentiality or data-handling provision anywhere in the design.
- Employer permission silently standing in for the consent of the people observed.
- Research data drifting into staff performance management.
- A comforting but invented confidentiality control over AI processing of client documents.
- Identifiable community posts used as evidence with no stated basis, or quoted when a paraphrase
  would do.
- Ethics fields retro-filled so an unexecuted design reads as completed fieldwork.
