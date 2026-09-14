# PROFESSIONAL_REPORT_RENDERING_CONTRACT (v1.9.5)

Bounded delivery/output-layer upgrade. This module adds one thing: a deterministic renderer
that turns the already-finalized `FINAL_MARKET_RESEARCH_REPORT.md` into a professional
`report.html` and, when a local browser is available, a matching `report.pdf`. It is not a
new research engine, benchmark campaign, crawler, multi-agent system, or v2 rewrite, and it
does not change any v1.5-v1.9.4 evidence, provenance, or delivery-quality rule.

## 1. Single-source rendering contract (P0-1)

The finalized report Markdown is canonical. The renderer never rewrites, summarizes,
reinterprets, renumbers, or changes evidence state. It only restructures markup and applies
presentation (CSS/layout). This is enforced mechanically, not by instruction alone:

```text
RENDER_READINESS_GATE
  - final report QA already PASS (v1.7.1 PROFESSIONAL_DELIVERY_ENVELOPE, v1.9.3
    DELIVERY_CONSISTENCY_AND_CURRENCY_GATE, v1.9.4 BOUNDED_BEHAVIORAL_CLOSURE_REPAIR)
  - exactly one current verdict present (EXECUTIVE_DECISION_LAYER rewritten in place, per
    v1.9.3 §2 — never a stale verdict left live beside a newer one)
  - material claims/numbers/entities/status labels are the frozen report content; the
    renderer takes them as-is
```

`RENDERER_CONSISTENCY_GATE` (implemented in `tools/render_report.py`,
`renderer_consistency_gate()`): before `report.html` is written to its requested path, the
tool extracts a material-field inventory from the source Markdown — every bold-labeled
sentence, every backtick-wrapped evidence/status token, every URL, every numeric value — and
the same inventory from the rendered HTML, and compares them. If anything is missing, added,
or altered, the render **FAILS LOUD**: non-zero exit, a `*.RENDER_GATE_FAILED.json` diagnostic
is written, and no `report.html`/`report.pdf` is delivered at the requested path. A rendered
file that differs materially from the canonical report does not ship silently; it HOLDs like
any other v1.9.3/v1.9.4 delivery gate failure.

Two transforms are recognized as structural, not content changes, and are excluded from the
comparison accordingly: an ordered-list item's leading `N. ` marker becomes semantic `<ol>`
numbering (still visible, rendered by the browser/PDF engine, not lost); a horizontal rule
(`---`) carries no claim content and is dropped as pure visual whitespace.

## 2. Professional HTML output (P0-2)

`tools/render_report.py build_full_html()` produces one self-contained `.html` file: inline
`<style>` only, no external fonts/scripts/analytics/tracking, a system font stack that covers
Korean and English (`-apple-system, "Segoe UI", "Malgun Gothic", "Apple SD Gothic Neo",
Roboto, "Noto Sans KR", ...`) so nothing depends on a network font fetch.

Layout, derived mechanically from the report's own existing structure (no new authoring
convention is invented beyond what `references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md`
already requires):

- masthead with title, the report's own metadata line, and any pre-first-section note
  (e.g. a correction-pass disclosure), rendered first since `EXECUTIVE_DECISION_LAYER` is
  already required to be the report's first `##` section (P0-2 "verdict block near top" is
  satisfied by the existing template order, not by renderer-side reinterpretation);
- a contents nav generated from the report's own `##` section headings (hidden in print to
  save paper — the sections are still visible on the printed/PDF page);
- each `##` section as its own bordered card, `###`/`####` preserved as sub-headings inside it;
- a bold-label paragraph whose first bold span matches the EXECUTIVE_DECISION_LAYER/
  IMPACT_VERIFICATION vocabulary (`DECISION`, `DIRECT ANSWER`, `CONFIDENCE`,
  `COUNTEREVIDENCE`, `LIMITATIONS`, `RECOMMENDATIONS`, `NEXT VERIFICATION`, `DECISIVE
  INSIGHTS`) is rendered as a toned callout (decision/info/caution/action) — still the exact
  original sentence, just visually promoted;
- a backtick-wrapped `ALL_CAPS_TOKEN` (the report's own evidence/status-label convention —
  `FACT`, `UNKNOWN`, `SEARCHED_NOT_FOUND`, `ACTIVE_OFFER`, `PREORDER_OFFER`,
  `CURRENT_FIRST_PARTY`, `NOT_APPLICABLE_TO_THIS_DECISION`, ...) is rendered as a small
  color-toned pill (`badge_tone()`); a backtick-wrapped URL is rendered as a clickable,
  word-break-safe link; anything else backtick-wrapped stays inline `<code>`;
- GFM pipe tables keep the source alignment row, get a `<div class="table-wrap">` horizontal
  scroll fallback so nothing is ever clipped, and repeat their header on each printed page
  (`thead{display:table-header-group}` + `tr{break-inside:avoid}`);
- fenced code blocks (the report's `yaml` evidence blocks) render as a dark, wrapped, non-
  clipping `<pre><code>` panel — `white-space:pre-wrap` so long lines never run off the
  printed page edge;
- A4 print CSS (`@page{size:A4;margin:16mm 13mm}`), the nav hidden in print, headings kept
  with their following content where practical (`break-after:avoid`).

## 3. PDF output (P0-3)

`tools/render_report.py render_pdf()` shells out to a local Chromium-family browser
(Microsoft Edge or Google Chrome, whichever `find_browser()` locates on PATH or the platform's
default install location) in `--headless=new --print-to-pdf` mode against the just-written
`report.html`, using a throwaway `--user-data-dir` profile. No paid API, no server dependency,
no network call. If no such browser is found, or the invocation does not produce a
non-trivial PDF file, the tool reports `PDF_RENDER_UNAVAILABLE` with the concrete reason and
still leaves `report.html` in place — it never fabricates a PDF success claim.

`pdf_text_consistency_check()` is a second, best-effort check: when the optional `pypdf`
package is importable, it extracts the PDF's text layer and confirms every printed (non-TOC)
section heading is present, despacing both sides first since CJK PDF text extraction commonly
inserts inter-glyph whitespace that is a text-layer artifact, not dropped content. When
`pypdf` is not installed, this check is skipped and reported as skipped — never silently
treated as passing.

## 4. Renderer consistency gate (P0-4)

Implemented, not just documented: `renderer_consistency_gate()` is the mechanical form of the
P0-4 checklist —

```text
bold-labeled sentence set   md == html   (title/subject/verdict/labels can't drift)
evidence/status token set   md == html   (taxonomy labels can't be dropped or invented)
numeric value multiset      md == html   (currency/unit/period/geography-bearing numbers)
URL set                     md == html   (a material source URL can't be dropped)
```

A mismatch on any of these is exactly a P0-4 failure: title/verdict/numeric/unit/competitor-
status/evidence-label drift, or a dropped source URL. `SINGLE_NEXT_ACTION_CONTRACT`
(v1.9.4 §5) is preserved by construction: the renderer performs no summarization that could
collapse or duplicate the closing instruction; the gate's token-preservation check would also
reject a render that duplicated or dropped it.

## 5. Buyer-facing output UX (P0-5)

For a final substantial market-research delivery, `FINAL_MARKET_RESEARCH_REPORT.md` remains
the canonical file (see `references/modules/MARKET_RESEARCH_DELIVERABLES.md`). After that report
passes final QA, the default closing behavior additionally renders `report.html` and, when a
local browser is available, `report.pdf` from it via `tools/render_report.py`, and tells the
user where all three files are — the buyer is never required to ask separately for a file, or
to know the renderer/module name.

## 6. Preserved behavior

This module does not modify: any v1.5-v1.9.4 evidence, provenance, delivery-consistency,
competitor-recall, commercial-evidence-ladder, or pricing-currency rule; the
`FINAL_MARKET_RESEARCH_REPORT.md` schema; the `EXECUTIVE_DECISION_LAYER` vocabulary; or the
direct-research method-choice/`SKIP` contract. It adds no new research capability, benchmark,
scoring router, evidence architecture, crawler, or always-on monitor. Where this module and
any of the above appear to conflict, the preserved behavior governs.
