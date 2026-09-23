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

## 2.1 Jurisdiction adapter — Korea

When the frozen geography is Korea and regulatory context is material, use current Korean official sources rather than generic/global compliance summaries.

Preferred authority path:
1. exact current statute/decree/regulation at `law.go.kr`;
2. the competent regulator/ministry's current guidance or notice (for privacy, `pipc.go.kr`);
3. first-party platform/store policy when the constraint is contractual/platform-specific rather than statutory.

For a product or research workflow involving personal data, first determine which privacy dimensions are actually decision-material. Candidate dimensions can include collection/use, sensitive or child data, processors/outsourcing, third-party provision, overseas transfer, notices/rights, and security measures. **This is a routing checklist, not a conclusion that every dimension applies.**

Important guards:
- `NO_PERSONAL_DATA_STORED` is a product-state fact, not by itself a legal conclusion that privacy obligations are irrelevant; collection, logs, integrations, communications or future scope can change the analysis.
- Do not claim PIPA applicability, non-applicability, compliance, violation, required consent, or a penalty without a current source and an applicability basis.
- When the product is in a separately regulated Korean sector, identify the competent authority and current sector rule before making the affected market-feasibility claim.
- If the exact Korean rule cannot be verified, use `MATERIAL_BUT_NOT_VERIFIABLE_NOW`, explain the decision impact, and continue the unaffected research.

Record when material:

```text
JURISDICTION: KOREA
REGULATORY_DIMENSION
OFFICIAL_SOURCE
EFFECTIVE_OR_ACCESS_DATE
APPLICABILITY_BASIS
WHAT_IT_CHANGES
WHAT_REMAINS_UNKNOWN
```

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
