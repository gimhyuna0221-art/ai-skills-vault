# Premium Final Report Standard — premium-deliverable-01 (trial)

Use only for a substantial full/professional market-research deliverable. This does not add a
new research engine or promise parity with any paid publisher's proprietary database. It turns
the already-supported FieldPilot evidence into a tangible client report whose structure and
information density are comparable in *presentation class* to public samples from commercial
market-research providers, while keeping FieldPilot's stricter provenance and UNKNOWN rules.

## 1. Buyer must receive a product, not a chat wall

A completed full engagement normally materializes:

```text
FINAL_MARKET_RESEARCH_REPORT.md      canonical content
report.html                          self-contained professional render
report.pdf                           when a verified PDF route is available
EVIDENCE_AND_SOURCE_REGISTER         embedded or separate client-visible table/file
COMPETITOR_AND_CASE_MATRIX           when decision-relevant
DELIVERY_AND_REVISION_NOTE           what was delivered, limits, revision state
```

Optional data/deck components follow COMMERCIAL_DELIVERABLE_SYSTEM. Do not create empty files
for appearance. If a format cannot be produced in the active runtime, deliver the complete
structured fallback and state the limitation; never mark a missing PDF as delivered.

A full report is not complete merely because the chat answer is good. The user should be able to
download, keep, forward and reopen the material without reconstructing the conversation.

## 2. Public paid-report benchmark qualities

Commercial report pages from providers such as Mordor Intelligence, Grand View Research and
Fortune Business Insights publicly expose recurring buyer-facing elements: a market snapshot,
summary/key takeaways, explicit scope/segmentation, trends or market dynamics, competitor/company
coverage, recent developments, methodology/coverage notes and a downloadable sample/report path.
These public structures are design references only. Do not copy gated report text, imply access to
proprietary databases, or claim equal proprietary coverage.

For FieldPilot, a substantial applicable report should therefore make the following easy to find:

1. **Executive snapshot** — subject, as-of date, scope/definition, current bounded conclusion.
2. **Key takeaways** — 3–7 decision-relevant points, including at least one material negative or
   uncertainty when present.
3. **Scope and definitions** — category, geography, time basis, unit/denominator and important
   source-definition differences before market-size numbers are compared.
4. **Requested analysis** — preserve the user's headings/order; for a generic engagement use the
   existing FieldPilot decision narrative instead of inventing decorative sections.
5. **Market dynamics** — drivers and restraints/counterevidence, not trend buzzwords only.
6. **Customer / segment view** — observed evidence separated from inferred candidate segments.
7. **Competitive landscape / alternatives** — direct, substitute, manual and do-nothing where
   relevant; compare common fields and show unknowns rather than forcing symmetry.
8. **Commercial / profitability view** — price/revenue evidence separated from actual margin; name
   missing cost denominators.
9. **Entry barriers / feasibility** — role- and geography-sensitive, with supported response options.
10. **Implications / recommendation** — what the evidence changes, alternatives/trade-offs, reversal
    conditions and next check when advice is part of the job.
11. **Sources and method appendix** — source register, evidence limits, contradictions, AI/tool use,
    human-review state and reproducibility notes.

Do not pad to hit a page count. COMMERCIAL_DELIVERABLE_SYSTEM's 15–30-page *class* means professional
information density when evidence and scope warrant it, not mandatory length. A narrower six-section
category brief may be shorter if it is complete and decision-useful.

## 3. Visual and table standard

Use a table or visual only when it reduces decision time. Every material representation carries:
- a finding-led title or nearby conclusion;
- units, period, geography and denominator when numeric;
- source keys/date or an unambiguous pointer;
- a short implication; and
- an explicit missingness/definition warning when comparisons are not like-for-like.

At least one decision-useful comparison table is expected for a multi-competitor or multi-subject
full report when comparable fields exist. Do not fabricate charts, market shares, TAM/SAM/SOM or
margin merely to make the PDF look expensive. A clean UNKNOWN is more professional than decorative
precision.

## 4. Market-size disagreement is a feature to explain, not hide

Paid sources often use different category definitions and estimation methods. When material numbers
conflict, preserve the distinct values and explain their definitions/method limits. Never average
incompatible estimates into a new unsourced number. If the difference cannot be reconciled from the
public evidence, state that explicitly and show which number is suitable for which decision.

## 5. Customer-facing value test before shipping

Before delivery, the customer-facing report must answer without reading the audit appendix:
- What was researched?
- What matters most?
- What is known versus still unknown?
- What alternatives exist?
- What does this evidence imply for the stated purpose?
- What should be checked or done next, when advice is requested?

The buyer should not need a second prompt to receive the promised file. Internal gate names, version
lineage and debug history stay in the appendix or manifest.

## 6. Delivery verification

Use the existing rendering and professional-envelope gates. Additionally confirm:
- canonical Markdown is nonempty and current;
- HTML, when promised, exists and preserves material content;
- PDF, when promised, exists, is non-trivial and is visually inspected/render-checked when tooling
  permits;
- first pages are buyer-facing rather than audit logs;
- tables are readable and not clipped;
- source links/keys remain traceable;
- the delivered report and the reviewed canonical report are the same revision.

A transport success, filename or valid PDF container is not enough. If visual verification was not
performed, say NOT_VISUALLY_VERIFIED rather than PASS.

## 7. Design-reference anchors (not FieldPilot performance evidence)

- Mordor Intelligence public market-report pages: market snapshot, key takeaways, trends/drivers/
  restraints, geography, competitive landscape, TOC/sample-report path.
- Grand View Research public report pages: report summary, segmentation, methodology, company insights,
  recent developments and sample-report path.
- Fortune Business Insights public report pages: summary/key findings, market dynamics, segmentation,
  regional outlook, competitive landscape, developments and report scope.

These references justify the *shape of the customer deliverable*, not any claim that FieldPilot owns
their proprietary data, analysts, interviews, models or paid report content.
