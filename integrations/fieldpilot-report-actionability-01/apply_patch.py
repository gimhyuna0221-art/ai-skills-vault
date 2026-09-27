#!/usr/bin/env python3
"""Idempotent, bounded text patch; does not rebuild from older compressed overlays."""
from pathlib import Path
import argparse

REV = '  report_extension_revision: "report-actionability-01"'
LINK = """## REPORT-ACTIONABILITY-01 — USER OUTLINE AND IMPLICATIONS

For substantial reports, including user-specified section lists, load
[report actionability](references/modules/REPORT_ACTIONABILITY.md) alongside Route B.
Preserve the requested subjects, headings and order. Connect findings to supported
implications and, when appropriate, options, trade-offs and a bounded next step.
Do not invent a user product or entry plan; facts-only restrictions take precedence.
This is a content-completion check, not permission to expand every narrow question.

"""
TAIL = """
## 7. User-specified outline and purpose — report-actionability-01

For substantial category/industry reports, apply
[report actionability](REPORT_ACTIONABILITY.md).
For a supplied outline, its order governs customer-facing section order rather
than the generic section list above. Preserve the four opening meanings briefly;
if the user requires only their headings, integrate them inside those headings.
This is the bounded presentation exception to sections 1 and 6, not a relaxation
of provenance, practical-fit honesty, audit split or renderer consistency.
General market understanding is not an invented founder/entry decision.
"""

def apply(root: Path) -> None:
    changes = {}
    p = root / 'SKILL.md'
    original = p.read_text(encoding='utf-8')
    s = original
    if REV not in s:
        anchor = '  review_extension_revision: "readiness-review-02"'
        if s.count(anchor) != 1:
            raise ValueError('Wrong candidate baseline; preserve and reconcile before patching')
        s = s.replace(anchor, anchor + '\n' + REV, 1)
    if LINK not in s:
        anchor = '## ROUTE A — ORDINARY BUILDER / MARKET→BUILD'
        if s.count(anchor) != 1:
            raise ValueError('Routing anchor missing or duplicated')
        s = s.replace(anchor, LINK + anchor, 1)
    old_kernel = original.split('## ALWAYS-LOADED INVARIANT KERNEL', 1)[1].split('## STEP 0', 1)[0]
    new_kernel = s.split('## ALWAYS-LOADED INVARIANT KERNEL', 1)[1].split('## STEP 0', 1)[0]
    if old_kernel != new_kernel:
        raise ValueError('Invariant kernel changed')
    changes[p] = s
    q = root / 'references/modules/BUYER_FACING_DECISION_REPORT.md'
    buyer = q.read_text(encoding='utf-8')
    if TAIL not in buyer:
        buyer = buyer.rstrip() + '\n' + TAIL
    changes[q] = buyer
    for path, text in changes.items():
        if path.read_text(encoding='utf-8') != text:
            path.write_text(text, encoding='utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--skill-root', required=True, type=Path)
    apply(parser.parse_args().skill_root)
