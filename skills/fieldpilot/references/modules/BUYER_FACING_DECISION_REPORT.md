# BUYER_FACING_DECISION_REPORT (v1.9.6)

Bounded pre-launch repair from Issue #24. This module does not add a new research engine,
benchmark campaign, crawler, multi-agent system, pricing engine, app, or v2 rewrite. It
repairs how the already-finalized `FINAL_MARKET_RESEARCH_REPORT.md` is *composed* and
*classified* before it reaches a first-time buyer, and adds one bounded practical-execution
check. It does not change any v1.5-v1.9.5 evidence, provenance, delivery-quality, or
rendering-consistency rule.

## 0. Product positioning guardrail

FieldPilot must not position itself as a proven business-success oracle, and must not imply
the creator has demonstrated business success. The defensible promise is:

> Help a builder inspect competitors/substitutes, evidence, unknowns, practical constraints,
> and the cheapest next validation action before committing more time or money.

No deliverable may claim guaranteed success, proven founder outcomes, proven revenue lift, or
buyer-success evidence that does not exist. This governs every customer-facing sentence, not
only the sections this module adds.

## 1. `CUSTOMER_DECISION_REPORT` / `AUDIT_METHOD_PROVENANCE_APPENDIX` split (P0-1, P0-5)

The canonical `FINAL_MARKET_RESEARCH_REPORT.md` itself — not the renderer — distinguishes two
parts using two literal `##` marker headings, in this order:

```text
## CUSTOMER_DECISION_REPORT
  ... buyer-facing sections ...
## AUDIT_METHOD_PROVENANCE_APPENDIX
  ... technical/audit/provenance sections ...
```

Both markers are required exactly once, in that order, for a report that opts into this
contract. A report predating v1.9.6 (or a test fixture) that carries neither marker renders
exactly as v1.9.5 did — this is additive, not a breaking rewrite of the markdown schema.

`tools/render_report.py` recognizes these markers (`PART_MARKER_CUSTOMER`,
`PART_MARKER_APPENDIX`) and renders the two parts with a different visual hierarchy
(`build_full_html`): the customer part keeps the v1.9.5 masthead/card treatment; the appendix
part renders behind a muted "Audit / Method / Provenance Appendix" divider banner with
subdued styling. This is presentation only — `renderer_consistency_gate` (v1.9.5) still
compares the *complete* material-field inventory (both parts) between Markdown and HTML, so
moving content into the appendix can never be used to silently drop it.

### Required customer-facing opening (P0-1, P0-4)

The `CUSTOMER_DECISION_REPORT` part must open, before any other content, with exactly these
four plain-language ideas in this order:

```text
1. 무엇을 알아봤는가 / What was investigated
2. 현재 판단 / Current decision
3. 왜 그렇게 판단했는가 (3-5개 결정적 이유) / Why (3-5 decisive reasons)
4. 지금 확인해야 할 한 가지 / One immediate next action
```

A reader must be able to answer all four questions after reading only this opening, without
knowing any FieldPilot internal module/gate name.

**The masthead (title + any pre-first-section note) is part of this opening, not a carve-out.**
A CENTRAL visual/buyer-facing verification pass on the first v1.9.6 sample found engine
version, `SKILL.md` frontmatter, GitHub Issue/PR numbers, and candidate-lineage commit hashes
rendered into the customer-visible masthead above the four-part summary — presentation/authoring
mistakes, not evidence errors, but exactly the internal vocabulary this section forbids. The
masthead must stay to the report title and, when useful, a plain access/reference date; engine
version, git commit/branch, Issue/PR lineage, and package/module names belong in the
`AUDIT_METHOD_PROVENANCE_APPENDIX` (or the machine-readable render manifest), never before the
customer decision summary. `buyer_facing_structure_gate()` scans the masthead blocks along with
the rest of the customer part for this.

Then, when applicable, the customer part continues with:

- competitor / substitute comparison
- confirmed overlap vs unverified overlap (§2 below)
- commercial evidence / price evidence
- practical feasibility for this user (§3 below)
- counterevidence / what would change the decision
- limitations / unknowns
- sources

### What must NOT dominate the customer-facing first pages

`MODULE_LOAD_NO_SKIP_GATE`-style internal gate names, package-internal file paths
(`references/...`, `tools/...`, `tests/...`), version-by-version regression history, raw YAML
implementation blocks, and engine/version/commit/Issue/PR build lineage belong only in
`AUDIT_METHOD_PROVENANCE_APPENDIX`. The underlying checks still run in full — hiding their
names from the customer narrative must not weaken QA or provenance, only its *presentation*.
`buyer_facing_structure_gate()` in `tools/render_report.py` enforces this mechanically: it
scans the blocks assigned to the `CUSTOMER_DECISION_REPORT` part (masthead included) and FAILS
the render if it finds a fenced code block, a package-internal file path, a denylisted internal
gate/module name, a version-regression heading, or engine/version/commit/Issue/PR build-lineage
text there.

**The first-page Contents nav lists only customer sections.** A raw appendix index full of gate
names (`MODULE_LOAD_NO_SKIP_GATE`, `EXECUTIVE_DECISION_LAYER`, ...) sitting on page 1, even
correctly linking into the appendix, still reads as an engineering artifact rather than a
customer report — CENTRAL's second visual-verification finding. `build_full_html()` renders the
top `<nav class="toc">` from customer sections only; the appendix gets its own, separate
`<nav class="toc appendix-toc">` index placed *after* the `AUDIT · METHOD · PROVENANCE APPENDIX`
divider banner (which itself starts a new printed page), so a buyer only encounters the raw
gate-name index if they have already turned past the appendix banner.

## 2. Confirmed overlap vs unknown overlap gate (P0-2)

Four-value taxonomy, replacing free-form "사실상 동일" / "거의 1:1" / "fully equivalent"
language:

```text
CONFIRMED_OVERLAP    a requested capability directly verified as present in a competitor
UNVERIFIED_OVERLAP   an important requested capability that looks similar but is not yet
                     verified against the competitor's actual behavior
CONFIRMED_GAP        a verified missing capability / unmet need
UNKNOWN_GAP          a possible gap requiring direct test
```

A report may not summarize a competitor as "사실상 동일", "거의 1:1", "fully equivalent", or
equivalent phrasing unless every material requested capability is `CONFIRMED_OVERLAP`. If any
material capability is `UNVERIFIED_OVERLAP` or `UNKNOWN_GAP`, the decision layer must reflect
that distinction instead of an unqualified equivalence claim.

`overlap_overclaim_gate()` in `tools/render_report.py` enforces this mechanically: it scans
the `CUSTOMER_DECISION_REPORT` part (the part a buyer actually reads; the full document when
no marker is present) for an overstrong-equivalence phrase (`OVERCLAIM_PHRASES`) and FAILS
the render when one is present alongside any `UNVERIFIED_OVERLAP` or `UNKNOWN_GAP` token. The
`AUDIT_METHOD_PROVENANCE_APPENDIX` may still quote a retired overstrong phrase verbatim as part
of its own version-history record without tripping this gate — a historical quotation of what
changed is not a live claim.

## 3. Practical feasibility / founder-context gate (P0-3)

For build / launch / sell / enter-market decisions, evaluate practical execution constraints
when they are decision-relevant and evidence is available:

- customer access / distribution path: can this specific builder realistically reach the
  target buyer?
- current buyer pain still unresolved despite competitors: verified, inferred, or unknown?
- builder constraints explicitly provided by the user: time, budget, tools, skill, geography,
  sales channel, existing audience/relationships
- cheapest feasible validation step given those constraints

Rules:

- Do not invent personal capability, budget, audience, contacts, sales skill, or distribution
  access. A market opportunity does not automatically mean this user can execute it. A
  competitor's existence does not automatically mean the user's idea is worthless.
- Missing user-specific information stays `UNKNOWN` and may become a reversal condition /
  validation target — it is never silently assumed in either direction.
- Add a concise buyer-facing section such as "내가 실제로 해낼 수 있는가? / Practical fit"
  only when material; when founder-context is materially unknown and does not change the
  immediate next action, say so plainly instead of omitting the topic.

`practical_feasibility_gate()` in `tools/render_report.py` enforces the "do not invent"
half mechanically, scoped to the `CUSTOMER_DECISION_REPORT` part (the full document when no
marker is present): it scans each block for a builder-capability assertion (existing audience,
existing distribution channel, budget, team, sales skill) that is not accompanied by an
`UNKNOWN` or `STATED` qualifier in that same block, and FAILS the render when one is found — an
unqualified assertion of capability the user never provided is exactly the fabrication this
gate exists to catch.

## 4. Plain-language default (P0-4)

- Plain Korean when the user speaks Korean; plain English when the user speaks English.
- Technical evidence labels (`FACT`, `UNKNOWN`, `CONFIRMED_OVERLAP`, ...) may remain in the
  customer part where useful, but are translated/explained in ordinary language the first time
  they appear — never left as an unexplained internal gate name.
- The four-question test in §1 is the acceptance bar: a first-time market-research user must
  be able to answer what/decision/why/next-action from the first screen alone.

## 5. Renderer preserves structure, never re-summarizes (P0-5)

The renderer may not independently summarize or delete evidence; only the canonical Markdown
source may distinguish `CUSTOMER_DECISION_REPORT` from `AUDIT_METHOD_PROVENANCE_APPENDIX`, and
`tools/render_report.py` renders exactly that distinction with different visual hierarchy
(customer: masthead-toned cards; appendix: muted divider + subdued cards). Every v1.9.5
`RENDERER_CONSISTENCY_GATE` and `PDF_RENDER_UNAVAILABLE`-honesty rule is unchanged and
continues to run over the whole document, both parts included.

## 6. Preserved behavior

This module does not modify: any v1.5-v1.9.5 evidence, provenance, delivery-consistency,
competitor-recall, commercial-evidence-ladder, pricing-currency, or rendering-consistency
rule; the `FINAL_MARKET_RESEARCH_REPORT.md` schema for a report that does not opt into the
`CUSTOMER_DECISION_REPORT`/`AUDIT_METHOD_PROVENANCE_APPENDIX` markers; the
`EXECUTIVE_DECISION_LAYER` vocabulary; or the direct-research method-choice/`SKIP` contract.
It adds no new research capability, benchmark, scoring router, evidence architecture, crawler,
pricing engine, or always-on monitor. Where this module and any of the above appear to
conflict, the preserved behavior governs.
