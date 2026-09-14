#!/usr/bin/env python3
"""FieldPilot v1.9.6 professional report renderer.

Bounded delivery/output-layer tool: turns a finalized FieldPilot
FINAL_MARKET_RESEARCH_REPORT.md (or any report following the same
EXECUTIVE_DECISION_LAYER / evidence-taxonomy markdown convention) into a
self-contained, offline-safe report.html and (when a local Chromium-family
browser is available) a matching report.pdf.

Hard contract (see references/modules/RENDERING_CONTRACT.md and
references/modules/BUYER_FACING_DECISION_REPORT.md):
  - This tool never rewrites, summarizes, reinterprets, renumbers, or drops
    any bold-labeled sentence, backtick evidence/status token, URL, or
    numeric value found in the source markdown. It only restructures markup
    and applies presentation (CSS/layout).
  - Before a report.html is written to its final path, a deterministic
    consistency gate (`renderer_consistency_gate`) compares the extracted
    material-field inventory of the markdown against the rendered HTML.
    If they do not match, rendering FAILS LOUD (non-zero exit, no
    report.html written to the requested path) instead of silently
    shipping a divergent deliverable.
  - When the source markdown opts into the v1.9.6 `## CUSTOMER_DECISION_REPORT`
    / `## AUDIT_METHOD_PROVENANCE_APPENDIX` marker convention, three
    additional bounded gates run before shipping: `buyer_facing_structure_gate`
    (no internal gate name/file path/YAML block/regression-history heading in
    the customer part), `overlap_overclaim_gate` (no unqualified "fully
    equivalent"-class claim while a material competitor capability is still
    unverified), and `practical_feasibility_gate` (no unqualified assertion of
    a builder capability/distribution/budget the user never provided). A
    report without the markers renders exactly as v1.9.5 did.
  - PDF generation uses a local headless Chromium-family browser
    (Edge/Chrome) print-to-pdf route. No paid API, no server dependency.
    If no such browser is found or the print invocation fails, the tool
    reports PDF_RENDER_UNAVAILABLE truthfully and still delivers report.html.

Usage:
    python render_report.py --input REPORT.md --outdir OUTDIR [--basename NAME]
                             [--no-pdf] [--browser PATH]

Stdlib-only. No network access. No third-party import required to produce
report.html or report.pdf; an optional `pypdf` import (if present) is used
only to strengthen the HTML<->PDF text-consistency check and is skipped
gracefully when unavailable.
"""
from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Optional

TOOL_VERSION = "1.9.6"

# v1.9.6 buyer-facing decision report / audit-appendix part markers.
PART_MARKER_CUSTOMER = "CUSTOMER_DECISION_REPORT"
PART_MARKER_APPENDIX = "AUDIT_METHOD_PROVENANCE_APPENDIX"

# ---------------------------------------------------------------------------
# Markdown -> block model
# ---------------------------------------------------------------------------

BLOCK_HEADING = "heading"
BLOCK_PARAGRAPH = "paragraph"
BLOCK_TABLE = "table"
BLOCK_CODE = "code"
BLOCK_LIST = "list"
BLOCK_QUOTE = "quote"
BLOCK_HR = "hr"

TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
HR_RE = re.compile(r"^(-{3,}|\*{3,}|_{3,})\s*$")
ORDERED_ITEM_RE = re.compile(r"^\s*\d+\.\s+(.*)$")
BULLET_ITEM_RE = re.compile(r"^\s*[-*]\s+(.*)$")


@dataclass
class Block:
    kind: str
    text: str = ""
    level: int = 0
    rows: list = field(default_factory=list)
    align: list = field(default_factory=list)
    items: list = field(default_factory=list)
    ordered: bool = False
    lang: str = ""


def parse_markdown(md_text: str) -> list:
    lines = md_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # Code fence
        fence_match = re.match(r"^```(\w*)\s*$", line.strip())
        if fence_match:
            lang = fence_match.group(1)
            body_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                body_lines.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            blocks.append(Block(kind=BLOCK_CODE, text="\n".join(body_lines), lang=lang))
            continue

        # Table (pipe row followed by a separator row)
        if line.lstrip().startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1].strip()):
            header_cells = _split_row(line)
            sep_cells = _split_row(lines[i + 1])
            align = []
            for cell in sep_cells:
                c = cell.strip()
                left = c.startswith(":")
                right = c.endswith(":")
                if left and right:
                    align.append("center")
                elif right:
                    align.append("right")
                elif left:
                    align.append("left")
                else:
                    align.append("")
            i += 2
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(_split_row(lines[i]))
                i += 1
            blocks.append(Block(kind=BLOCK_TABLE, rows=[header_cells] + rows, align=align))
            continue

        # Heading
        h = HEADING_RE.match(line)
        if h:
            blocks.append(Block(kind=BLOCK_HEADING, level=len(h.group(1)), text=h.group(2)))
            i += 1
            continue

        # Horizontal rule (must not collide with a table separator, already handled above)
        if HR_RE.match(line.strip()):
            blocks.append(Block(kind=BLOCK_HR))
            i += 1
            continue

        # Blockquote
        if line.lstrip().startswith(">"):
            quote_lines = []
            while i < n and lines[i].lstrip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(Block(kind=BLOCK_QUOTE, text=" ".join(quote_lines).strip()))
            continue

        # List (bullet or ordered), consecutive lines
        if BULLET_ITEM_RE.match(line) or ORDERED_ITEM_RE.match(line):
            ordered = bool(ORDERED_ITEM_RE.match(line))
            items = []
            while i < n and (BULLET_ITEM_RE.match(lines[i]) or ORDERED_ITEM_RE.match(lines[i])):
                m = ORDERED_ITEM_RE.match(lines[i]) or BULLET_ITEM_RE.match(lines[i])
                items.append(m.group(1).strip())
                i += 1
            blocks.append(Block(kind=BLOCK_LIST, items=items, ordered=ordered))
            continue

        # Paragraph: gather until blank line or a line that starts a different block
        para_lines = [line]
        i += 1
        while i < n and lines[i].strip() and not (
            HEADING_RE.match(lines[i])
            or HR_RE.match(lines[i].strip())
            or lines[i].lstrip().startswith("|")
            or lines[i].lstrip().startswith(">")
            or BULLET_ITEM_RE.match(lines[i])
            or ORDERED_ITEM_RE.match(lines[i])
            or re.match(r"^```", lines[i].strip())
        ):
            para_lines.append(lines[i])
            i += 1
        blocks.append(Block(kind=BLOCK_PARAGRAPH, text=" ".join(l.strip() for l in para_lines)))
    return blocks


def _split_row(line: str) -> list:
    row = line.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    # split on unescaped pipes
    cells = re.split(r"(?<!\\)\|", row)
    return [c.strip().replace("\\|", "|") for c in cells]


# ---------------------------------------------------------------------------
# Inline formatting + evidence-token badges
# ---------------------------------------------------------------------------

_TOKEN_TONE = {
    "FACT": "positive", "PASS": "positive", "LOADED_AND_APPLIED": "positive",
    "NOT_APPLICABLE_TO_THIS_DECISION": "positive", "OBSERVED_PURCHASE": "positive",
    "OBSERVED_REPEAT_PURCHASE_OR_RETENTION": "positive", "PROVEN_WTP": "positive",
    "CURRENT_FIRST_PARTY": "positive", "NEAR_EXACT_FOUND_INCLUDED": "positive",
    "CLOSURE_CONFIRMED_NONE_FOUND": "positive",
    "UNKNOWN": "caution", "UNKNOWN_NEEDS_TEST": "caution", "SECONDARY_UNVERIFIED": "caution",
    "PREORDER_OFFER": "caution", "ACTIVE_OFFER": "caution", "COVERAGE_INCOMPLETE": "caution",
    "NOT_QUERIED": "caution", "HOLD": "caution", "LABELED_HISTORICAL": "caution",
    "LISTED_PRICE": "caution", "SHARED_NON_DISCRIMINATING": "caution",
    "SUPPORTED_INFERENCE": "caution", "NOT_PERFORMED": "negative",
    "SEARCHED_NOT_FOUND": "negative", "STALE_UNLABELED": "negative",
    "DO_NOT_BUILD": "negative", "WEAKNESS": "negative", "FAIL": "negative",
    "SKIPPED_BY_USER": "negative",
}
_POS_HINTS = ("PASS", "FACT", "CONFIRMED", "LOADED_AND_APPLIED", "INCLUDED", "PROVEN", "CURRENT_FIRST_PARTY")
_CAUTION_HINTS = ("UNKNOWN", "NEEDS_TEST", "SECONDARY", "PREORDER", "ACTIVE_OFFER", "INCOMPLETE", "NOT_QUERIED", "HOLD", "HISTORICAL")
_NEG_HINTS = ("NOT_PERFORMED", "NOT_FOUND", "STALE", "DO_NOT_BUILD", "WEAKNESS", "FAIL", "SKIPPED")


def badge_tone(token: str) -> str:
    t = token.strip().upper()
    if t in _TOKEN_TONE:
        return _TOKEN_TONE[t]
    for hint in _NEG_HINTS:
        if hint in t:
            return "negative"
    for hint in _CAUTION_HINTS:
        if hint in t:
            return "caution"
    for hint in _POS_HINTS:
        if hint in t:
            return "positive"
    return "neutral"


_ALLCAPS_TOKEN_RE = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")
_URL_RE = re.compile(r"^https?://\S+$")
_CODE_SPAN_RE = re.compile(r"`([^`]+)`")
_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")


def _render_code_span(inner: str) -> str:
    raw = html_lib.unescape(inner)
    if _URL_RE.match(raw):
        return (
            f'<a class="src-url" href="{html_lib.escape(raw, quote=True)}" '
            f'target="_blank" rel="noopener">{html_lib.escape(raw)}</a>'
        )
    if _ALLCAPS_TOKEN_RE.match(raw):
        tone = badge_tone(raw)
        return f'<code class="tag tag-{tone}">{html_lib.escape(raw)}</code>'
    return f"<code>{html_lib.escape(raw)}</code>"


def render_inline(text: str) -> str:
    escaped = html_lib.escape(text, quote=False)
    escaped = _CODE_SPAN_RE.sub(lambda m: _render_code_span(m.group(1)), escaped)
    escaped = _LINK_RE.sub(
        lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>',
        escaped,
    )
    escaped = _BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", escaped)
    escaped = _ITALIC_RE.sub(lambda m: f"<em>{m.group(1)}</em>", escaped)
    return escaped


_LABEL_COLON_RE = re.compile(r"^\*\*([A-Z][A-Za-z0-9 /()가-힣]{1,40}?):\s*(.*?)\*\*(.*)$", re.S)
_LABEL_ALONE_RE = re.compile(r"^\*\*([A-Z][A-Za-z0-9 /()가-힣]{2,60})\*\*$")

_LABEL_TONE = {
    "DECISION": "decision", "DIRECT ANSWER": "decision",
    "CONFIDENCE": "info",
    "COUNTEREVIDENCE": "caution", "LIMITATIONS": "caution",
    "RECOMMENDATIONS": "action", "RECOMMENDATION": "action",
    "NEXT VERIFICATION": "action", "DECISIVE INSIGHTS": "info",
}


def _label_tone(label: str) -> str:
    key = re.sub(r"\s*\(.*\)\s*$", "", label).strip().upper()
    return _LABEL_TONE.get(key, "neutral")


def render_paragraph(text: str) -> str:
    m = _LABEL_COLON_RE.match(text)
    if m:
        label, bold_rest, trailing = m.group(1), m.group(2), m.group(3)
        tone = _label_tone(label)
        strong_content = label + ":" + (" " + bold_rest if bold_rest else "")
        strong_html = render_inline(strong_content)
        trailing_html = render_inline(trailing) if trailing.strip() else ""
        sep = " " if trailing_html else ""
        return (
            f'<p class="callout callout-{tone}">'
            f'<strong class="callout-label">{strong_html}</strong>{sep}{trailing_html}</p>'
        )
    m2 = _LABEL_ALONE_RE.match(text)
    if m2:
        label = m2.group(1)
        tone = _label_tone(label)
        return (
            f'<p class="callout callout-{tone} callout-heading">'
            f'<strong class="callout-label">{render_inline(label)}</strong></p>'
        )
    return f"<p>{render_inline(text)}</p>"


# ---------------------------------------------------------------------------
# Block -> HTML
# ---------------------------------------------------------------------------

def _slug_stub(index: int) -> str:
    return f"sec-{index}"


def render_blocks_to_sections(blocks: list):
    """Group blocks into a masthead (everything before the first H2) and a
    list of (heading_text, heading_level, html_fragment) H2 sections.

    A v1.9.6 report may mark its own `## CUSTOMER_DECISION_REPORT` /
    `## AUDIT_METHOD_PROVENANCE_APPENDIX` part boundaries; each such marker
    heading is a state transition, not a rendered section, and every
    section dict carries the `part` ("customer" or "appendix") active when
    it was opened. A report without either marker has every section default
    to "customer", rendering exactly as v1.9.5 did."""
    masthead_blocks = []
    sections = []  # list of dicts: {title, anchor, html, part}
    cur = None
    sec_index = 0
    current_part = "customer"
    for b in blocks:
        if b.kind == BLOCK_HEADING and b.level == 1:
            # title handled by caller separately; skip from body flow
            continue
        if b.kind == BLOCK_HEADING and b.level == 2:
            heading_text = b.text.strip()
            if heading_text.startswith(PART_MARKER_CUSTOMER):
                current_part = "customer"
                continue
            if heading_text.startswith(PART_MARKER_APPENDIX):
                current_part = "appendix"
                continue
            sec_index += 1
            cur = {"title": b.text, "anchor": _slug_stub(sec_index), "html": [], "part": current_part}
            sections.append(cur)
            continue
        target = cur["html"] if cur is not None else None
        frag = render_block(b)
        if frag is None:
            continue
        if target is not None:
            target.append(frag)
        else:
            masthead_blocks.append(frag)
    return masthead_blocks, sections


def render_block(b: Block) -> Optional[str]:
    if b.kind == BLOCK_HR:
        return None
    if b.kind == BLOCK_HEADING:
        lvl = min(max(b.level, 3), 4)
        return f"<h{lvl}>{render_inline(b.text)}</h{lvl}>"
    if b.kind == BLOCK_PARAGRAPH:
        return render_paragraph(b.text)
    if b.kind == BLOCK_QUOTE:
        return f"<blockquote>{render_inline(b.text)}</blockquote>"
    if b.kind == BLOCK_LIST:
        tag = "ol" if b.ordered else "ul"
        items = "".join(f"<li>{render_inline(item)}</li>" for item in b.items)
        return f"<{tag}>{items}</{tag}>"
    if b.kind == BLOCK_CODE:
        escaped = html_lib.escape(b.text)
        lang_class = f" language-{b.lang}" if b.lang else ""
        return f'<pre class="evidence-block"><code class="{lang_class.strip()}">{escaped}</code></pre>'
    if b.kind == BLOCK_TABLE:
        header, *rows = b.rows
        align = b.align + [""] * (len(header) - len(b.align))
        style = lambda a: f' style="text-align:{a}"' if a else ""
        thead = "<tr>" + "".join(
            f"<th{style(align[idx] if idx < len(align) else '')}>{render_inline(cell)}</th>"
            for idx, cell in enumerate(header)
        ) + "</tr>"
        tbody_rows = []
        for row in rows:
            cells = "".join(
                f"<td{style(align[idx] if idx < len(align) else '')}>{render_inline(cell)}</td>"
                for idx, cell in enumerate(row)
            )
            tbody_rows.append(f"<tr>{cells}</tr>")
        return (
            '<div class="table-wrap"><table><thead>' + thead + "</thead><tbody>"
            + "".join(tbody_rows) + "</tbody></table></div>"
        )
    return None


# ---------------------------------------------------------------------------
# Full HTML document
# ---------------------------------------------------------------------------

CSS = """
:root{
  --ink:#141a22; --sub:#4b5768; --bg:#f4f6f9; --card:#ffffff; --border:#dde2ea;
  --accent:#0f4c81; --accent-ink:#0a3557; --verdict-bg:#eaf2fb; --verdict-border:#a9c7e8;
  --info-bg:#eef3ff; --info-border:#b9c9f2;
  --caution-bg:#fff6e8; --caution-border:#eecb8c; --caution-ink:#7a4b06;
  --action-bg:#eefaf1; --action-border:#a9d9bb; --action-ink:#1f5c37;
  --neg:#9d3b3b; --pos:#1f7a4d; --neutral:#5b6472;
  --mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Consolas, "Liberation Mono", monospace;
  --sans: -apple-system, "Segoe UI", "Malgun Gothic", "Apple SD Gothic Neo", Roboto, "Noto Sans KR", Helvetica, Arial, sans-serif;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  font-size:15px;line-height:1.62;-webkit-font-smoothing:antialiased}
.page{max-width:920px;margin:0 auto;padding:36px 28px 64px}
.masthead{background:linear-gradient(135deg,var(--accent) 0%,var(--accent-ink) 100%);color:#fff;
  border-radius:14px;padding:30px 32px;margin-bottom:22px}
.masthead .eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;opacity:.85;margin:0 0 8px}
.masthead h1{margin:0 0 12px;font-size:26px;line-height:1.35;font-weight:700}
.masthead .meta{display:flex;flex-wrap:wrap;gap:6px 22px;font-size:13px;opacity:.92}
.masthead .meta strong{font-weight:600}
.masthead-note{margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,.28);
  font-size:13px;line-height:1.6;opacity:.95}
nav.toc{background:var(--card);border:1px solid var(--border);border-radius:12px;
  padding:16px 20px;margin-bottom:22px}
nav.toc h2{margin:0 0 10px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--sub)}
nav.toc ol{margin:0;padding-left:20px;columns:2;column-gap:28px}
nav.toc li{margin-bottom:6px;break-inside:avoid}
nav.toc a{color:var(--accent-ink);text-decoration:none;font-size:13.5px}
nav.toc a:hover{text-decoration:underline}
section.report-section{background:var(--card);border:1px solid var(--border);border-radius:12px;
  padding:22px 26px 26px;margin-bottom:18px}
section.report-section > h2{margin:0 0 14px;font-size:18px;color:var(--accent-ink);
  padding-bottom:10px;border-bottom:2px solid var(--border)}
.audit-appendix{margin-top:8px}
.appendix-banner{text-align:center;font-size:12px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--sub);background:#eceff3;border:1px dashed var(--border);border-radius:10px;
  padding:10px;margin:0 0 16px}
nav.toc.appendix-toc{background:transparent;border-style:dashed}
nav.toc.appendix-toc h2{color:var(--sub)}
nav.toc.appendix-toc a{color:var(--sub)}
section.appendix-section{background:#f7f8fa;border-color:#e4e8ee}
section.appendix-section > h2{color:var(--sub)}
p.appendix-eyebrow{margin:0 0 6px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--sub);font-weight:700}
h3{font-size:15.5px;margin:20px 0 8px;color:var(--ink)}
h4{font-size:14px;margin:16px 0 6px;color:var(--sub);text-transform:uppercase;letter-spacing:.04em}
p{margin:0 0 12px}
ul,ol{margin:0 0 14px;padding-left:22px}
li{margin-bottom:6px}
blockquote{margin:0 0 14px;padding:10px 16px;border-left:4px solid var(--border);
  background:#fafbfd;color:var(--sub)}
a{color:var(--accent);word-break:break-word}
a.src-url{font-family:var(--mono);font-size:12.5px;word-break:break-all}
code{font-family:var(--mono);font-size:.88em;background:#eef1f5;padding:1px 6px;border-radius:5px}
code.tag{font-weight:700;letter-spacing:.02em;padding:2px 9px;border-radius:999px;font-size:.76em;
  white-space:nowrap}
code.tag-positive{background:#e4f5ea;color:var(--pos)}
code.tag-caution{background:#fdf1dc;color:var(--caution-ink)}
code.tag-negative{background:#fbe7e7;color:var(--neg)}
code.tag-neutral{background:#eceff3;color:var(--neutral)}
.callout{border-left:4px solid var(--border);background:#fafbfd;border-radius:8px;
  padding:12px 16px;margin:0 0 12px}
.callout-label{font-weight:700;text-transform:uppercase;font-size:12px;letter-spacing:.05em;
  margin-right:6px}
.callout-decision{background:var(--verdict-bg);border-color:var(--verdict-border)}
.callout-decision .callout-label{color:var(--accent-ink)}
.callout-info{background:var(--info-bg);border-color:var(--info-border)}
.callout-info .callout-label{color:#28418c}
.callout-caution{background:var(--caution-bg);border-color:var(--caution-border)}
.callout-caution .callout-label{color:var(--caution-ink)}
.callout-action{background:var(--action-bg);border-color:var(--action-border)}
.callout-action .callout-label{color:var(--action-ink)}
.callout-heading{font-weight:700;text-transform:uppercase;font-size:12.5px;letter-spacing:.05em;
  background:transparent;border:none;padding:4px 0 0}
.table-wrap{overflow-x:auto;margin:0 0 16px;border:1px solid var(--border);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
thead th{background:#eef2f7;color:var(--accent-ink);text-align:left;font-weight:700;
  padding:9px 12px;border-bottom:2px solid var(--border);white-space:normal}
tbody td{padding:8px 12px;border-bottom:1px solid var(--border);vertical-align:top;
  white-space:normal;word-break:break-word}
tbody tr:nth-child(even){background:#fafbfd}
pre.evidence-block{background:#0f172a;color:#e2e8f0;border-radius:10px;padding:16px 18px;
  overflow-x:auto;font-size:12.5px;line-height:1.55;margin:0 0 16px;white-space:pre-wrap;
  word-break:break-word}
pre.evidence-block code{background:transparent;color:inherit;padding:0;font-size:1em}
footer.report-footer{margin-top:26px;padding-top:16px;border-top:1px solid var(--border);
  color:var(--sub);font-size:12px;text-align:center}
@media print{
  @page{size:A4;margin:16mm 13mm}
  html,body{background:#fff;font-size:12.4px}
  .page{max-width:none;padding:0}
  .masthead{border-radius:0;break-after:avoid}
  nav.toc{display:none}
  section.report-section{border:none;border-radius:0;box-shadow:none;padding:0 0 10px;
    margin-bottom:10px;break-inside:auto}
  section.report-section > h2{break-after:avoid}
  h3,h4{break-after:avoid}
  .callout{break-inside:avoid}
  .appendix-banner{break-before:page;break-after:avoid}
  table{font-size:11px}
  thead{display:table-header-group}
  tr{break-inside:avoid}
  a{color:var(--accent-ink);text-decoration:none}
  a.src-url{word-break:break-all}
}
"""


def _render_content(md_text: str):
    blocks = parse_markdown(md_text)
    title = "FieldPilot Report"
    for b in blocks:
        if b.kind == BLOCK_HEADING and b.level == 1:
            title = b.text
            break
    masthead_frags, sections = render_blocks_to_sections(blocks)
    return title, masthead_frags, sections


def build_material_fragment(md_text: str) -> str:
    """Render only the content that must trace 1:1 back to the source
    markdown (title + masthead note + report sections) with none of the
    renderer's own navigation/footer chrome (TOC, eyebrow, generated-at
    footer). Used exclusively by the consistency gate so boilerplate the
    renderer itself adds can never be mistaken for material content, and
    so it can never mask real drift in material content either."""
    title, masthead_frags, sections = _render_content(md_text)
    sections_html = "".join(
        f'<section>{render_inline(s["title"])}' + "".join(s["html"]) + "</section>"
        for s in sections
    )
    return f"<h1>{render_inline(title)}</h1>" + "".join(masthead_frags) + sections_html


def _section_html(s: dict, appendix: bool = False) -> str:
    cls = "report-section appendix-section" if appendix else "report-section"
    eyebrow = '<p class="appendix-eyebrow">Appendix</p>' if appendix else ""
    return (
        f'<section class="{cls}" id="{s["anchor"]}">{eyebrow}<h2>{render_inline(s["title"])}</h2>'
        + "".join(s["html"]) + "</section>"
    )


def build_full_html(md_text: str, source_filename: str) -> str:
    title, masthead_frags, sections = _render_content(md_text)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    customer_sections = [s for s in sections if s.get("part", "customer") == "customer"]
    appendix_sections = [s for s in sections if s.get("part", "customer") == "appendix"]
    has_appendix = bool(appendix_sections)

    toc_customer = "".join(
        f'<li><a href="#{s["anchor"]}">{render_inline(s["title"])}</a></li>' for s in customer_sections
    )
    customer_html = "".join(_section_html(s) for s in customer_sections)

    # Page 1 must be customer-only: the top-of-page Contents nav lists ONLY
    # customer sections, never a raw appendix/gate-name index. The appendix
    # gets its own, separate index rendered AFTER the appendix divider
    # banner (deeper in the document / on its own printed page), not on the
    # page a buyer opens first.
    toc_html = f'<nav class="toc"><h2>Contents</h2><ol>{toc_customer}</ol></nav>'

    if has_appendix:
        toc_appendix = "".join(
            f'<li><a href="#{s["anchor"]}">{render_inline(s["title"])}</a></li>' for s in appendix_sections
        )
        appendix_toc_html = (
            f'<nav class="toc appendix-toc"><h2>Appendix Contents</h2><ol>{toc_appendix}</ol></nav>'
        )
        appendix_html = "".join(_section_html(s, appendix=True) for s in appendix_sections)
        sections_html = (
            f'<div class="decision-report">{customer_html}</div>'
            f'<div class="audit-appendix">'
            f'<div class="appendix-banner">AUDIT &middot; METHOD &middot; PROVENANCE APPENDIX</div>'
            f'{appendix_toc_html}'
            f'{appendix_html}</div>'
        )
    else:
        sections_html = customer_html
        sections_html = customer_html

    masthead_note = "".join(masthead_frags)

    body = f"""<div class="page">
<div class="masthead">
  <p class="eyebrow">FieldPilot &middot; Professional Market Research Deliverable</p>
  <h1>{render_inline(title)}</h1>
  <div class="masthead-note">{masthead_note}</div>
</div>
{toc_html}
{sections_html}
<footer class="report-footer">Rendered by FieldPilot v{TOOL_VERSION} professional report renderer
from <code>{html_lib.escape(source_filename)}</code> &middot; generated {generated_at} &middot;
content is unmodified from the canonical report source.</footer>
</div>"""

    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html_lib.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Renderer consistency gate (P0-4)
# ---------------------------------------------------------------------------

def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


_NUMBER_RE = re.compile(r"[\$£€₩]?\d[\d,]*(?:\.\d+)?%?")
_FENCE_RE = re.compile(r"^```[^\n]*\n.*?^```\s*$", re.S | re.M)


def _md_inline_to_plaintext(s: str) -> str:
    """Resolve inline markdown syntax to the plain visible text it renders
    as, so md-side and HTML-side material-field extraction compare like
    with like (e.g. a backtick-wrapped URL becomes a link; its *visible*
    text drops the backticks, it does not lose content)."""
    s = _LINK_RE.sub(lambda m: m.group(1), s)
    s = s.replace("`", "")
    return s


def _strip_ordered_list_markers(text: str) -> str:
    """An ordered-list item's leading `N. ` marker becomes semantic <ol>
    numbering in HTML (rendered visually by the browser/PDF engine, not
    present as literal text). Strip it before numeric-content comparison
    so that structural renumbering-by-markup is not mistaken for a
    dropped or altered material number. Heading lines (`## N. Title`)
    are untouched: their numeral is prose content the renderer keeps as
    literal text, not a list marker."""
    return "\n".join(
        ORDERED_ITEM_RE.sub(lambda m: m.group(1), line) if ORDERED_ITEM_RE.match(line) else line
        for line in text.split("\n")
    )


def extract_material_fields_md(md_text: str) -> dict:
    # Bold-label and inline-code-span extraction must skip fenced code
    # blocks: a run of single backticks inside a ```yaml fence is not an
    # inline code span, and scanning it as one would falsely pair the
    # fence's own opening/closing backticks across the whole block.
    non_fenced = _FENCE_RE.sub("", md_text)
    bold = Counter(_md_inline_to_plaintext(_norm(m)) for m in _BOLD_RE.findall(non_fenced))
    code = Counter(_norm(m) for m in _CODE_SPAN_RE.findall(non_fenced))
    urls = set(re.findall(r"https?://[^\s`)\]]+", md_text))
    numbers = Counter(_NUMBER_RE.findall(_strip_ordered_list_markers(md_text)))
    return {"bold": bold, "code": code, "urls": urls, "numbers": numbers}


_BLOCK_TAGS = {"p", "li", "td", "th", "h1", "h2", "h3", "h4", "tr", "div",
               "section", "pre", "blockquote", "nav"}


class _HTMLFieldExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.mode_stack = []
        self.buf_stack = []
        self.bold = []
        self.code = []
        self.urls = []
        self.plain = []
        self._pre_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        mode = None
        if tag == "pre":
            self._pre_depth += 1
        if tag == "strong":
            mode = "strong"
        elif tag == "code" and self._pre_depth == 0:
            # A <code> block inside <pre> is fenced source content
            # (already covered by the numeric/URL comparison), not an
            # inline evidence/status token span.
            mode = "code"
        elif tag == "a":
            href = attrs_d.get("href", "") or ""
            cls = attrs_d.get("class", "") or ""
            if href.startswith("http://") or href.startswith("https://"):
                self.urls.append(href)
            if "src-url" in cls:
                mode = "code"
        self.mode_stack.append(mode)
        self.buf_stack.append("")
        if tag in _BLOCK_TAGS:
            self.plain.append(" ")

    def handle_endtag(self, tag):
        if tag == "pre" and self._pre_depth > 0:
            self._pre_depth -= 1
        if not self.mode_stack:
            return
        mode = self.mode_stack.pop()
        content = self.buf_stack.pop() if self.buf_stack else ""
        if mode == "strong":
            self.bold.append(_norm(content))
        elif mode == "code":
            self.code.append(_norm(content))
        if self.buf_stack:
            self.buf_stack[-1] += content
        if tag in _BLOCK_TAGS:
            self.plain.append(" ")

    def handle_data(self, data):
        self.plain.append(data)
        if self.buf_stack:
            self.buf_stack[-1] += data


def extract_material_fields_html(html_text: str) -> dict:
    m = re.search(r"<body[^>]*>(.*)</body>", html_text, re.S)
    body = m.group(1) if m else html_text
    parser = _HTMLFieldExtractor()
    parser.feed(body)
    plain_text = "".join(parser.plain)
    bold = Counter(b for b in parser.bold if b)
    code = Counter(c for c in parser.code if c)
    urls = set(u for u in parser.urls)
    numbers = Counter(_NUMBER_RE.findall(plain_text))
    return {"bold": bold, "code": code, "urls": urls, "numbers": numbers}


@dataclass
class GateResult:
    ok: bool
    problems: list


def renderer_consistency_gate(md_fields: dict, html_fields: dict) -> GateResult:
    problems = []

    def counter_diff(name, a: Counter, b: Counter):
        missing = a - b
        added = b - a
        if missing:
            problems.append(f"{name} missing in HTML: {dict(missing)}")
        if added:
            problems.append(f"{name} present in HTML but not in source markdown: {dict(added)}")

    counter_diff("bold-labeled sentence", md_fields["bold"], html_fields["bold"])
    counter_diff("evidence/status token", md_fields["code"], html_fields["code"])
    counter_diff("numeric value", md_fields["numbers"], html_fields["numbers"])

    missing_urls = md_fields["urls"] - html_fields["urls"]
    added_urls = html_fields["urls"] - md_fields["urls"]
    if missing_urls:
        problems.append(f"source URL dropped from rendered HTML: {sorted(missing_urls)}")
    if added_urls:
        problems.append(f"URL present in HTML but not sourced from markdown: {sorted(added_urls)}")

    return GateResult(ok=not problems, problems=problems)


# ---------------------------------------------------------------------------
# v1.9.6 buyer-facing structure / overlap-overclaim / practical-feasibility
# gates (references/modules/BUYER_FACING_DECISION_REPORT.md)
# ---------------------------------------------------------------------------

_INTERNAL_GATE_NAME_TOKENS = {
    "MODULE_LOAD_NO_SKIP_GATE", "DIRECT_COMPETITOR_RECALL_CLOSURE",
    "COMMERCIAL_EVIDENCE_TAXONOMY_GATE", "CURRENT_STATE_PRICING_FRESHNESS_HIERARCHY",
    "SINGLE_NEXT_ACTION_CONTRACT", "EXECUTIVE_DECISION_LAYER",
    "SUBJECT_AND_SALE_MODE_LOCK", "USER_CASE_GAP_DIAGNOSIS", "NEGATIVE_CASE_SEARCH",
    "RENDER_READINESS_GATE", "RENDERER_CONSISTENCY_GATE", "CLIENT_DECISION_BRIEF",
    "SUBJECT_FRAME", "PROFESSIONAL_DELIVERY_ENVELOPE", "RESEARCH_QA_AND_AI_DISCLOSURE",
    "BOUNDED_BEHAVIORAL_CLOSURE_REPAIR", "DELIVERY_CONSISTENCY_AND_CURRENCY_GATE",
    "PROVENANCE_OUTPUT_GATE", "PROFESSIONAL_REPORT_RENDERING_CONTRACT",
}
# Generic fallback: an ALLCAPS backtick token ending in a governing-layer-style
# suffix reads as an internal gate/module name even if not in the explicit
# registry above. None of this tool's evidence/status vocabulary (FACT,
# SEARCHED_NOT_FOUND, ACTIVE_OFFER, CONFIRMED_OVERLAP, UNKNOWN_GAP, ...) ends
# in one of these suffixes, so this cannot collide with a legitimate
# customer-facing evidence label.
_INTERNAL_GATE_NAME_SUFFIX_RE = re.compile(
    r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*_(GATE|CLOSURE|CONTRACT|HIERARCHY|LOCK|ENVELOPE|"
    r"DIAGNOSIS|LAYER|FRAME|BRIEF)$"
)
_PACKAGE_PATH_RE = re.compile(r"\b(?:references|tools|tests)/[\w./-]*\.(?:md|py)\b")
_REGRESSION_HEADING_RE = re.compile(
    r"(v1\.\d+(?:\.\d+)?\s*(?:대비|재검증|regression)|regression\s+evidence|회귀\s*\d*\s*개?\s*항목)",
    re.I,
)
# CENTRAL visual/buyer-facing verification (Issue #24 finding 1): engine
# version, git commit/branch, Issue/PR lineage, and SKILL.md/governing-layer
# jargon must never precede the customer decision summary — including in
# the masthead, which is otherwise unrestricted free text.
_BUILD_LINEAGE_RE = re.compile(
    r"(GitHub Issue #\d+|PR #\d+|candidate\s*\(|SKILL\.md|frontmatter|governing layer"
    r"|\bv1\.\d+\.\d+\s*(?:candidate|후보)?\b)",
    re.I,
)

_OVERCLAIM_PHRASES = [
    "사실상 동일", "거의 1:1", "거의 1대1", "fully equivalent", "완전히 동일",
    "identical product", "1:1로 동일", "사실상 같은 제품",
]
_OVERLAP_UNRESOLVED_TOKENS = ("UNVERIFIED_OVERLAP", "UNKNOWN_GAP")

_CAPABILITY_ASSERTION_RE = re.compile(
    r"(기존\s*(?:고객|오디언스|유통망|채널|팔로워)\s*(?:을|를)?\s*(?:활용|기반)"
    r"|당신의\s*(?:예산|팀|영업력|네트워크)"
    r"|existing\s+(?:audience|customer base|distribution|channel|network)"
    r"|your\s+(?:budget|team|sales skill|network)\b)",
    re.I,
)
_QUALIFIER_RE = re.compile(r"UNKNOWN|STATED")


def _is_internal_gate_token(token: str) -> bool:
    t = token.strip()
    if t in _INTERNAL_GATE_NAME_TOKENS:
        return True
    return bool(_INTERNAL_GATE_NAME_SUFFIX_RE.match(t))


def _block_text_for_scan(b: Block) -> str:
    if b.kind == BLOCK_TABLE:
        return " ".join(cell for row in b.rows for cell in row)
    if b.kind == BLOCK_LIST:
        return " ".join(b.items)
    return b.text


def split_parts_blocks(blocks: list):
    """Return (customer_blocks, appendix_blocks, marker_order). marker_order
    lists 'customer'/'appendix' in the order their marker headings appeared
    (empty when the report carries neither marker)."""
    customer, appendix = [], []
    current = "customer"
    marker_order = []
    for b in blocks:
        if b.kind == BLOCK_HEADING and b.level == 2:
            heading_text = b.text.strip()
            if heading_text.startswith(PART_MARKER_CUSTOMER):
                current = "customer"
                marker_order.append("customer")
                continue
            if heading_text.startswith(PART_MARKER_APPENDIX):
                current = "appendix"
                marker_order.append("appendix")
                continue
        (customer if current == "customer" else appendix).append(b)
    return customer, appendix, marker_order


def buyer_facing_structure_gate(blocks: list) -> GateResult:
    """P0-1/P0-5: nothing that reads as internal audit/debug material may
    appear in the CUSTOMER_DECISION_REPORT part -- including the masthead
    (everything before the first marker/section heading), which is
    customer-visible on page 1 and is scanned here too (CENTRAL visual
    verification finding 1: no version/commit/Issue/PR/SKILL.md/candidate
    lineage before the customer decision summary). Only runs when a report
    opts into the v1.9.6 marker convention (marker_order non-empty); a
    report without either marker is unaffected (renders as v1.9.5 did)."""
    problems = []
    customer_blocks, _appendix_blocks, marker_order = split_parts_blocks(blocks)
    if not marker_order:
        return GateResult(ok=True, problems=problems)

    if marker_order != ["customer", "appendix"]:
        problems.append(
            "CUSTOMER_DECISION_REPORT/AUDIT_METHOD_PROVENANCE_APPENDIX markers "
            f"must appear exactly once each, customer before appendix; found order {marker_order}"
        )

    for b in customer_blocks:
        if b.kind == BLOCK_CODE:
            first_line = b.text.strip().splitlines()[0][:80] if b.text.strip() else "(empty)"
            problems.append(
                f"internal fenced code/YAML block found in CUSTOMER_DECISION_REPORT part: {first_line!r}"
            )
            continue
        scan_text = _block_text_for_scan(b)
        for path_match in _PACKAGE_PATH_RE.findall(scan_text):
            problems.append(f"package-internal file path in customer part: {path_match}")
        for code_token in _CODE_SPAN_RE.findall(scan_text):
            if _is_internal_gate_token(code_token):
                problems.append(f"internal gate/module name in customer part: `{code_token}`")
        if b.kind == BLOCK_HEADING and _REGRESSION_HEADING_RE.search(b.text):
            problems.append(f"version-regression-history heading in customer part: {b.text!r}")
        lineage_match = _BUILD_LINEAGE_RE.search(scan_text)
        if lineage_match:
            problems.append(
                "engine/version/commit/Issue/PR build-lineage metadata in customer part "
                f"(including the masthead): {lineage_match.group(0)!r}"
            )

    return GateResult(ok=not problems, problems=problems)


def overlap_overclaim_gate(md_text: str) -> GateResult:
    """P0-2: an unqualified equivalence phrase may not coexist with an
    unresolved (UNVERIFIED_OVERLAP/UNKNOWN_GAP) competitor-capability
    classification in the CUSTOMER_DECISION_REPORT part (the part a buyer
    actually reads). When the report opts into the v1.9.6 marker
    convention, the AUDIT_METHOD_PROVENANCE_APPENDIX may still quote a
    retired overstrong phrase verbatim as part of its own change history
    (e.g. "this replaces v1.9.4's '거의 1:1' wording") without tripping this
    gate — that is a historical record, not a live claim. A report without
    either marker is scanned in full, matching v1.9.5 behavior."""
    problems = []
    blocks = parse_markdown(md_text)
    customer_blocks, _appendix_blocks, marker_order = split_parts_blocks(blocks)
    scan_blocks = customer_blocks if marker_order else blocks
    scan_text = "\n".join(_block_text_for_scan(b) for b in scan_blocks)
    found_phrases = [p for p in _OVERCLAIM_PHRASES if p in scan_text]
    unresolved = [t for t in _OVERLAP_UNRESOLVED_TOKENS if t in scan_text]
    if found_phrases and unresolved:
        problems.append(
            f"overstrong equivalence phrase(s) {found_phrases} present alongside an unresolved "
            f"overlap classification {unresolved} — narrow the wording or verify the remaining "
            "capability before claiming equivalence"
        )
    return GateResult(ok=not problems, problems=problems)


def practical_feasibility_gate(md_text: str) -> GateResult:
    """P0-3: do not invent personal capability, budget, audience, contacts,
    sales skill, or distribution access. An assertion of one of these must
    carry an UNKNOWN (not provided) or STATED (user-provided) marker in the
    same block (paragraph/list item/heading); an unqualified assertion is
    treated as fabricated founder context. Scoped to the
    CUSTOMER_DECISION_REPORT part when the report opts into the v1.9.6
    marker convention (a report without either marker is scanned in full),
    and per-block rather than a whole-document window, so an unrelated
    UNKNOWN elsewhere cannot mask a real violation."""
    problems = []
    blocks = parse_markdown(md_text)
    customer_blocks, _appendix_blocks, marker_order = split_parts_blocks(blocks)
    scan_blocks = customer_blocks if marker_order else blocks
    for b in scan_blocks:
        if b.kind not in (BLOCK_PARAGRAPH, BLOCK_LIST, BLOCK_QUOTE, BLOCK_HEADING):
            continue
        scan_text = _block_text_for_scan(b)
        if _CAPABILITY_ASSERTION_RE.search(scan_text) and not _QUALIFIER_RE.search(scan_text):
            m = _CAPABILITY_ASSERTION_RE.search(scan_text)
            problems.append(
                "builder-capability assertion without an UNKNOWN/STATED qualifier in the same "
                f"block: {m.group(0)!r}"
            )
    return GateResult(ok=not problems, problems=problems)


# ---------------------------------------------------------------------------
# PDF (local headless browser print-to-pdf route)
# ---------------------------------------------------------------------------

_BROWSER_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium-browser", "/usr/bin/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]


def find_browser(explicit: Optional[str] = None) -> Optional[Path]:
    if explicit:
        p = Path(explicit)
        return p if p.exists() else None
    for name in ("msedge", "chrome", "google-chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return Path(found)
    for c in _BROWSER_CANDIDATES:
        if Path(c).exists():
            return Path(c)
    return None


def render_pdf(browser: Path, html_path: Path, pdf_path: Path, timeout: int = 90):
    # Some Chromium-family builds on Windows fail to load a file:// URI
    # whose path contains non-ASCII (e.g. Korean) segments even when
    # correctly percent-encoded, exiting 0 with no PDF written and no
    # stderr. Stage a copy of the HTML under a plain-ASCII temp path so
    # PDF generation is robust regardless of where the user's project
    # directory lives, then deliver the PDF to the real requested path.
    stage_dir = Path(tempfile.mkdtemp(prefix="fieldpilot-render-"))
    staged_html = stage_dir / "report.html"
    staged_pdf = stage_dir / "report.pdf"
    shutil.copyfile(html_path, staged_html)
    html_uri = staged_html.resolve().as_uri()

    profile_dir = tempfile.mkdtemp(prefix="fieldpilot-print-")
    cmd = [
        str(browser), "--headless=new", "--disable-gpu", "--no-sandbox",
        f"--user-data-dir={profile_dir}",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={staged_pdf}",
        "--virtual-time-budget=20000",
        html_uri,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=timeout)
    except Exception as exc:  # noqa: BLE001 - surface any invocation failure honestly
        shutil.rmtree(profile_dir, ignore_errors=True)
        shutil.rmtree(stage_dir, ignore_errors=True)
        return "PDF_RENDER_UNAVAILABLE", f"browser invocation failed: {exc}"
    shutil.rmtree(profile_dir, ignore_errors=True)

    # Some Chromium-family builds return from --headless=new print-to-pdf
    # slightly before the PDF write is flushed to disk. Poll briefly for a
    # stable, non-trivial file size instead of failing on that race.
    deadline = time.time() + 5
    last_size = -1
    staged_ok = False
    while time.time() < deadline:
        if staged_pdf.exists():
            size = staged_pdf.stat().st_size
            if size > 1000 and size == last_size:
                staged_ok = True
                break
            last_size = size
        time.sleep(0.25)
    if not staged_ok and staged_pdf.exists() and staged_pdf.stat().st_size > 1000:
        staged_ok = True

    if staged_ok:
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(staged_pdf, pdf_path)
        shutil.rmtree(stage_dir, ignore_errors=True)
        return "OK", f"generated via {browser.name} headless print-to-pdf"

    stderr_tail = (result.stderr or b"").decode(errors="replace")[-500:]
    shutil.rmtree(stage_dir, ignore_errors=True)
    return "PDF_RENDER_UNAVAILABLE", f"exit={result.returncode} stderr={stderr_tail}"


def printed_section_headings(body_html: str) -> list:
    """Extract `<h2>` section headings that actually appear on a printed
    page, i.e. every one EXCEPT those inside a `nav.toc` element -- the
    main Contents nav and, for a v1.9.6 two-part report, the separate
    appendix Contents nav (both `<nav class="toc">`/`<nav class="toc
    appendix-toc">`) are hidden in print (`nav.toc{display:none}`) to save
    paper, so their `<h2>` labels ("Contents", "Appendix Contents") must
    never be treated as printed section headings."""
    body_without_navs = re.sub(r"<nav\b.*?</nav>", "", body_html, flags=re.S)
    return re.findall(r"<h2>(.*?)</h2>", body_without_navs, re.S)


def pdf_text_consistency_check(html_text: str, pdf_path: Path):
    try:
        import pypdf  # type: ignore
    except ImportError:
        return None, ["pypdf not installed; HTML<->PDF text-consistency check skipped"]
    try:
        reader = pypdf.PdfReader(str(pdf_path))
        pdf_text = "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception as exc:  # noqa: BLE001
        return False, [f"failed to read PDF for consistency check: {exc}"]
    # CJK PDF text extraction commonly inserts extra inter-glyph whitespace
    # that is not present in the source HTML/markdown (a pypdf/Chromium
    # text-layer artifact, not dropped content). Compare with all
    # whitespace stripped so that spacing artifacts cannot register as a
    # false consistency failure.
    despaced_pdf = re.sub(r"\s+", "", pdf_text)
    problems = []
    m = re.search(r"<body[^>]*>(.*)</body>", html_text, re.S)
    body = m.group(1) if m else html_text
    headings = printed_section_headings(body)
    for h in headings:
        clean = _norm(re.sub(r"<[^>]+>", "", h))
        despaced_clean = re.sub(r"\s+", "", clean)
        if despaced_clean and despaced_clean not in despaced_pdf:
            problems.append(f"section heading not found in extracted PDF text: {clean!r}")
    if len(reader.pages) < 1:
        problems.append("PDF has zero pages")
    return (not problems), problems


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def render_report(input_path: Path, outdir: Path, basename: str,
                   make_pdf: bool = True, browser_path: Optional[str] = None):
    md_text = input_path.read_text(encoding="utf-8")
    outdir.mkdir(parents=True, exist_ok=True)

    blocks = parse_markdown(md_text)
    structure_gate = buyer_facing_structure_gate(blocks)
    overlap_gate = overlap_overclaim_gate(md_text)
    feasibility_gate = practical_feasibility_gate(md_text)

    html_text = build_full_html(md_text, input_path.name)
    material_fragment = build_material_fragment(md_text)

    md_fields = extract_material_fields_md(md_text)
    html_fields = extract_material_fields_html(material_fragment)
    consistency_gate = renderer_consistency_gate(md_fields, html_fields)

    gate = GateResult(
        ok=structure_gate.ok and overlap_gate.ok and feasibility_gate.ok and consistency_gate.ok,
        problems=(
            structure_gate.problems + overlap_gate.problems
            + feasibility_gate.problems + consistency_gate.problems
        ),
    )

    manifest = {
        "tool_version": TOOL_VERSION,
        "source_markdown": str(input_path),
        "buyer_facing_structure_gate": {"ok": structure_gate.ok, "problems": structure_gate.problems},
        "overlap_overclaim_gate": {"ok": overlap_gate.ok, "problems": overlap_gate.problems},
        "practical_feasibility_gate": {"ok": feasibility_gate.ok, "problems": feasibility_gate.problems},
        "consistency_gate": {"ok": consistency_gate.ok, "problems": consistency_gate.problems},
    }

    if not gate.ok:
        failure_path = outdir / f"{basename}.RENDER_GATE_FAILED.json"
        failure_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        manifest_path = outdir / f"{basename}.render_manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        return manifest, gate

    md_out = outdir / f"{basename}.md"
    html_out = outdir / f"{basename}.html"
    md_out.write_text(md_text, encoding="utf-8")
    html_out.write_text(html_text, encoding="utf-8")
    manifest["report_md"] = str(md_out)
    manifest["report_html"] = str(html_out)

    pdf_status, pdf_detail = "SKIPPED", "PDF generation not requested"
    if make_pdf:
        browser = find_browser(browser_path)
        if browser is None:
            pdf_status, pdf_detail = "PDF_RENDER_UNAVAILABLE", "no local Chromium-family browser found"
        else:
            pdf_out = outdir / f"{basename}.pdf"
            pdf_status, pdf_detail = render_pdf(browser, html_out, pdf_out)
            if pdf_status == "OK":
                manifest["report_pdf"] = str(pdf_out)
                pdf_ok, pdf_problems = pdf_text_consistency_check(html_text, pdf_out)
                manifest["pdf_text_consistency"] = {"ok": pdf_ok, "problems": pdf_problems}
    manifest["pdf_status"] = pdf_status
    manifest["pdf_detail"] = pdf_detail

    manifest_path = outdir / f"{basename}.render_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest, gate


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001 - best-effort console encoding fix
            pass
    parser = argparse.ArgumentParser(description="FieldPilot professional report renderer")
    parser.add_argument("--input", required=True, help="path to canonical report .md")
    parser.add_argument("--outdir", required=True, help="output directory")
    parser.add_argument("--basename", default=None, help="output file base name (default: input stem)")
    parser.add_argument("--no-pdf", action="store_true", help="skip PDF generation")
    parser.add_argument("--browser", default=None, help="explicit path to a Chromium-family browser")
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    basename = args.basename or input_path.stem

    if not input_path.exists():
        print(f"FAIL: input not found: {input_path}", file=sys.stderr)
        return 2

    manifest, gate = render_report(input_path, outdir, basename,
                                    make_pdf=not args.no_pdf, browser_path=args.browser)

    if not gate.ok:
        print("FAIL: render gate rejected this render (HOLD, nothing shipped)")
        for p in gate.problems:
            print(f"  - {p}")
        return 1

    print("PASS: buyer_facing_structure_gate + overlap_overclaim_gate + "
          "practical_feasibility_gate + renderer_consistency_gate")
    print(f"report_md={manifest.get('report_md')}")
    print(f"report_html={manifest.get('report_html')}")
    print(f"pdf_status={manifest.get('pdf_status')} ({manifest.get('pdf_detail')})")
    if manifest.get("report_pdf"):
        print(f"report_pdf={manifest.get('report_pdf')}")
    if "pdf_text_consistency" in manifest:
        print(f"pdf_text_consistency={manifest['pdf_text_consistency']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
