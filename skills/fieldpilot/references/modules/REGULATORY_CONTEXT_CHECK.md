# Conditional Regulatory and Jurisdiction Context Check — v1.7.2

Regulatory context is a **conditional** check, not an optional one. When the product, the buyer's
obligations, or the decision itself is materially shaped by regulation, an absent regulatory
section is a coverage gap — not neutrality.

The opposite failure is worse: FieldPilot must never manufacture a legal conclusion, cite a
regulation it has not verified, or imply that a market is or is not compliant.

Rule anchors: `R-REG-01`, `R-CLAIM-01`, `R-SOURCE-01`, `R-DESK-01`.
Source anchors: `S-ESOMAR`, `S-EU-AI` (within its own legal scope only), `S-CIOMS` and
`S-BELMONT` where human-subject or health context applies.

## 1. Materiality trigger — when the check is required

Run the check when any of these is true for the frozen decision:

- the product handles money, contracts, subscriptions, prepayment, refunds, cancellation or
  auto-renewal;
- it handles personal data, health, biometric, financial, children's or other sensitive data;
- it operates in a licensed, regulated or professionally supervised sector — health, finance,
  education, legal, gambling, alcohol, firearms, transport, food safety and similar;
- claims made to end users are themselves regulated — advertising, health, financial or
  environmental claims;
- platform or store policy functions as a binding constraint on the business model;
- accessibility, employment or workplace rules bear on how the product is used;
- the user's own decision is about entering a specific jurisdiction.

If none applies, record `REGULATORY_CONTEXT: NOT_MATERIAL` **with the reason**. Silence is not an
acceptable output; a stated non-applicability is.

## 2. Output states

```text
REGULATORY_CONTEXT
  MATERIAL_AND_CHECKED                  what was checked, source, date, and what it changes
  MATERIAL_BUT_GEOGRAPHY_UNRESOLVED     the dependency is surfaced, not silently dropped
  MATERIAL_BUT_NOT_VERIFIABLE_NOW       named as an open dependency with its decision impact
  NOT_MATERIAL                          with the reason
```

### Geography unresolved

When geography is `UNRESOLVED` in the frozen `CLIENT_DECISION_BRIEF` and regulation is material,
the correct output is **not** omission and **not** a guessed jurisdiction. It is:

- name the regulatory dimension that would matter — for example membership contract terms,
  prepayment and refund rules, auto-renewal disclosure, or personal-data duties;
- state that its content is jurisdiction-dependent and therefore unresolved;
- state what the answer would change for the decision;
- carry it into the open-unknowns list and the claim ceiling of any dependent conclusion;
- where the user can resolve geography cheaply, ask — this is a decision-changing question and
  therefore passes the existing question-economy test.

## 3. What may and may not be said

May:

- identify the regulatory **dimension** that is plausibly material and why it bears on the decision;
- report a specific rule only with a current, named, dated official or authoritative source;
- state how a regulatory constraint would change cost, feasibility, packaging, claims or timing;
- recommend qualified professional review where the decision turns on the answer.

May not:

- state or imply a legal conclusion, a compliance status, or that something is lawful or unlawful;
- cite a statute, article, regulation number, effective date or penalty from model memory without
  a verified current source;
- assume that a framework applies outside its own jurisdictional or subject-matter scope — this is
  the existing `CONDITIONAL_HARD` applicability procedure in
  `references/core/ETHICS_AND_PROFESSIONAL_STANDARDS.md` section 6, and it continues to govern;
- present the absence of a found regulation as evidence that none exists;
- let an unresolved regulatory dependency block the rest of the market research. Scope the
  affected conclusion and continue.

FieldPilot is not a substitute for qualified legal review, and must say so where the decision
turns on a regulatory answer.

## 4. Rendering

The regulatory context appears in the report's market-structure and context material where it is
material, and its unresolved dependencies appear in the open-unknowns and limitations sections. A
`NOT_MATERIAL` determination is recorded in the coverage audit with its reason, so a reader can
see that the question was asked and answered rather than skipped.

## 5. Failure modes this module exists to prevent

- An error-and-omission-prevention product researched with no reference to the contract,
  prepayment or refund rules that create the very pain it addresses.
- A regulatory section silently omitted because the target geography was never resolved.
- A guessed jurisdiction standing in for an unresolved one.
- A confidently cited article number that no source in the run supports.
- "No regulation was found" presented as "there is no regulation".
- A legal opinion delivered inside a market-research report.

## 6. Korea privacy / data route — v1.9.9-rc02 bounded extension

Activate this subsection only when:
- the target geography/jurisdiction is Korea; and
- personal-data handling, privacy positioning, cloud/analytics/API use, or another data-flow question can change feasibility, cost, claims, or go-to-market.

This is a **regulatory research route**, not legal advice and not a compliance certificate.

### Korea privacy coverage contract

First establish the product fact pattern. Do not assume a privacy obligation merely from the product category, and do not accept a privacy marketing claim merely because the user says "no personal data."

Check only the dimensions made material by the actual architecture and decision:

```text
KOREA_DATA_FACT_PATTERN
  what personal data, if any, is collected/created/read/stored/transmitted;
  actor roles and data flows;
  whether the "no personal data" claim is actually supported by product evidence

KOREA_PROCESSING_OR_ENTRUSTMENT
  whether a third-party/cloud/analytics/API/service provider processes data
  on the business's behalf; if material, verify current official requirements

KOREA_OVERSEAS_TRANSFER
  whether data is provided, entrusted, stored, or otherwise transferred abroad;
  if material, verify current official requirements and exceptions

KOREA_SENSITIVE_OR_SPECIAL_CASE
  sensitive/unique identifiers, children/minors, health, finance, location,
  video/biometric or other sector-specific data only when actually present

KOREA_NOTICE_RETENTION_SECURITY
  privacy notice, retention/deletion, security, disclosure/third-party or
  other duties only to the extent current official sources make them material

KOREA_SECTOR_OVERLAY
  separate laws/rules for health, education, finance, location information,
  communications, employment or other regulated sectors when applicable
```

### Source priority

For current Korean legal requirements, resolve the current text at decision time from official primary sources first:
1. 국가법령정보센터 (law.go.kr) — current statute/enforcement decree and effective date.
2. 개인정보보호위원회 (pipc.go.kr) — current official guidance/interpretation and overseas-transfer/privacy-policy resources.
3. Sector regulator/official platform documentation when a sector or platform overlay is material.

As verified during the 2026-09-24 patch research, the then-current Personal Information Protection Act was effective 2026-09-11; Article 26 covered entrusted processing and Article 28-8 covered overseas transfer. These article references are **freshness anchors, not permanent memory**: re-resolve the current law/effective date before relying on them in a live decision.

### Claim ceiling

Allowed:
- "This data flow makes Korean privacy obligations decision-relevant; current official sources need to be checked."
- "Official source S, effective/accessed on date T, states requirement X for the described fact pattern."
- "The product evidence supports/does not yet support the factual claim that it stores no personal data."

Forbidden:
- "PIPA does not apply" solely because a product is offline or stores no account database.
- "This product is compliant with Korean privacy law."
- "No consent/privacy policy/contract is needed" without a current source and fact-specific legal basis.
- importing a foreign privacy rule as if it were Korean law.

If the product's privacy architecture is a commercial differentiator, verify the factual architecture separately from the legal conclusion. A verified "no personal-data storage" fact may narrow risk and migration burden; it does not by itself prove legal compliance or customer preference.

