#!/usr/bin/env python3
"""Apply only this pinned additive trial; refuse unexpected source revisions."""
import argparse
import hashlib
from pathlib import Path

PRE = {'SKILL.md': 'de792760b44d90c19cf504f3596e59669de50fea5e4f07194bfafe41ce00e45c', 'references/modules/BROKER_RESEARCH_DELIVERY.md': 'bf60c87d35249a2716c1d3cb864e3e2ce5b935a21cef62e677004f1ac9f8f469'}
ENTRY = "## REFERENCE-FIRST-01 — REQUIRED BEFORE RESEARCH CONCLUSIONS\n\nFor evidence-dependent investigations, inspect task-fit existing references before\nsubstantive conclusions. Reuse adequate current evidence; discover better primary\nsources, specialist analyses or actual service outputs for gaps. Apply\n[reference-first value](references/modules/REFERENCE_FIRST_VALUE.md) before\nsubstantial synthesis, including its customer-value check only for relevant\nproduct/business decisions. Popularity is not '#1' proof. Never add citations to\njustify a preselected conclusion. Narrow facts use their direct source; supplied-\nsource-only and no-browse restrictions remain binding. Preserve actionable options,\nrequested headings, report delivery and the existing efficiency safeguards.\n\n"
BROKER = '### Required reference-first checkpoint\n\nBefore substantive conclusions apply [reference-first value](REFERENCE_FIRST_VALUE.md).\nReuse sufficient inspected evidence first; otherwise discover and inspect better\nclaim-matched sources or authorized service outputs. Record selection rationale and\nremaining gaps in the existing source register. Best available for this task is not\nverified global first place. Finding good material does not replace explaining\nsupported options and why one fits. Explicit source-only limits remain binding.\n\n'
ADDED = {
    "references/modules/REFERENCE_FIRST_VALUE.md": "REFERENCE_FIRST_VALUE.md",
    "tests/test_reference_first_contract.py": "test_reference_first_contract.py",
    "tests/reference_first/README.md": "RETEST.md",
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def apply(root):
    replacements = {}
    for rel, expected in PRE.items():
        p = root / rel
        text = p.read_text(encoding="utf-8")
        if rel == "SKILL.md":
            original = text.replace(ENTRY, "", 1).replace('  reference_extension_revision: "reference-first-01"\n', "", 1)
            new = original.replace('  report_extension_revision: "report-actionability-01"\n', '  report_extension_revision: "report-actionability-01"\n  reference_extension_revision: "reference-first-01"\n', 1).replace('## BROKER-EXEC-01 — PURPOSE, METHOD REUSE, DELIVERY', ENTRY + '## BROKER-EXEC-01 — PURPOSE, METHOD REUSE, DELIVERY', 1)
        else:
            original = text.replace(BROKER, "", 1)
            new = original.replace('## 2. Discover contenders, not permanent winners\n\n', '## 2. Discover contenders, not permanent winners\n\n' + BROKER, 1)
        if sha(original.encode()) != expected:
            raise ValueError("Unexpected baseline: " + rel)
        replacements[rel] = new
    replacements.update({rel: (Path(__file__).resolve().parent / name).read_text(encoding="utf-8") for rel, name in ADDED.items()})
    for rel, text in replacements.items():
        p = root / rel
        if p.is_symlink():
            raise ValueError("Refusing symlink: " + rel)
        if rel in ADDED and p.exists() and p.read_text(encoding="utf-8") != text:
            raise ValueError("Existing added file differs: " + rel)
    for rel, text in replacements.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, required=True)
    args = parser.parse_args()
    apply(args.skill_root.resolve())
