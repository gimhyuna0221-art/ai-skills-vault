#!/usr/bin/env python3
"""FieldPilot prompt-robustness runner.

Subcommands
  blind   anonymize raw run outputs for a blind judge and write a sealed mapping
  report  code-grade every output, merge optional blind-judge rubric scores, and write
          per-arm / per-case summaries (markdown + JSON)

Raw output file name: <case_id>__<variant_id>__<arm>__<sample>.md
(e.g. F1_QUOTE__C_messy_ko__rc04__1.md). The reply may end with a harness manifest block
(see graders.MANIFEST_DELIM); it is stripped before grading and blinding.

Generating outputs is protocol-driven (fresh session per run, same model and settings per arm,
no memory/project/connectors, skill loaded from the arm's folder) — see README.md.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graders  # noqa: E402

FLOOR_ITEMS = ["R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R15", "R16"]
FRIENDLY_ITEMS = ["R1", "R2", "R12"]
BURDEN_ITEMS = ["R13", "R14"]
NAME_RE = re.compile(r"^(?P<case>[A-Za-z0-9_]+)__(?P<variant>[A-Za-z0-9_]+)__(?P<arm>[A-Za-z0-9_.-]+)__(?P<sample>\d+)\.md$")
VERSION_RE = re.compile(r"(v?1\.9\.9-rc0\d|rc0[0-9]|FieldPilot)", re.I)


def load_cases(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    index = {}
    for case in data["cases"]:
        for v in case["variants"]:
            index[(case["id"], v["id"])] = (case, v)
    return index


def iter_outputs(outputs: Path):
    for p in sorted(outputs.glob("*.md")):
        m = NAME_RE.match(p.name)
        if m:
            yield p, m.groupdict()


def cmd_blind(args):
    cases = load_cases(Path(args.cases))
    outs = list(iter_outputs(Path(args.outputs)))
    rng = random.Random(args.seed)
    rng.shuffle(outs)
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    mapping = {}
    for i, (p, meta) in enumerate(outs, 1):
        blind_id = f"X{i:02d}"
        reply, _ = graders.split_manifest(p.read_text(encoding="utf-8"))
        reply = VERSION_RE.sub("[REDACTED]", reply)
        case, variant = cases[(meta["case"], meta["variant"])]
        packet = (f"# {blind_id}\n\n## CASE FACTS\n{case['case_facts']}\n\n## USER MESSAGE\n{variant['prompt']}\n\n"
                  f"## REPLY\n{reply}\n")
        (dest / f"{blind_id}.md").write_text(packet, encoding="utf-8")
        mapping[blind_id] = {"file": p.name, **meta}
    sealed = Path(args.mapping)
    sealed.write_text(json.dumps({"seed": args.seed, "mapping": mapping}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {len(mapping)} blind replies to {dest}; sealed mapping -> {sealed}")


def _score(items: list[str], scores: dict) -> float | None:
    vals = []
    for it in items:
        v = scores.get(it)
        if isinstance(v, list):
            v = v[0]
        if isinstance(v, (int, float)):
            vals.append(v / 2)
    return round(statistics.mean(vals), 3) if vals else None


def cmd_report(args):
    cases = load_cases(Path(args.cases))
    rubric = {}
    if args.rubric_scores:
        raw = json.loads(Path(args.rubric_scores).read_text(encoding="utf-8"))
        mapping = json.loads(Path(args.mapping).read_text(encoding="utf-8"))["mapping"] if args.mapping else {}
        for blind_id, scores in raw.items():
            key = mapping.get(blind_id, {}).get("file", blind_id)
            rubric[key] = scores
    rows = []
    for p, meta in iter_outputs(Path(args.outputs)):
        case, variant = cases[(meta["case"], meta["variant"])]
        reply, manifest = graders.split_manifest(p.read_text(encoding="utf-8"))
        g = graders.grade(reply, case["expectations"])
        r = rubric.get(p.name, {})
        rows.append({
            "file": p.name, **meta, "family": case["family"], "register": variant.get("register"),
            "code": g.to_dict(), "manifest": manifest,
            "FLOOR": _score(FLOOR_ITEMS, r), "FRIENDLY": _score(FRIENDLY_ITEMS, r), "BURDEN": _score(BURDEN_ITEMS, r),
            "rubric": r,
        })
    summary = summarize(rows, cases)
    Path(args.out_json).write_text(json.dumps({"rows": rows, "summary": summary}, ensure_ascii=False, indent=1), encoding="utf-8")
    Path(args.out_md).write_text(render_md(rows, summary), encoding="utf-8")
    print(f"graded {len(rows)} outputs -> {args.out_md}")


def summarize(rows, cases):
    arms = sorted({r["arm"] for r in rows})
    out = {"by_arm": {}, "by_case": {}}
    for arm in arms:
        rs = [r for r in rows if r["arm"] == arm]
        non_block = [r for r in rs if not cases[(r["case"], r["variant"])][0]["expectations"].get("blocking_allowed")]
        viol = {}
        for r in rs:
            for v in r["code"]["violations"]:
                viol[v] = viol.get(v, 0) + 1
        floors = [r["FLOOR"] for r in rs if r["FLOOR"] is not None]
        out["by_arm"][arm] = {
            "n": len(rs),
            "blocking_on_answerable_cases": sum(r["code"]["blocking"] for r in non_block),
            "answerable_cases": len(non_block),
            "mean_user_questions": round(statistics.mean([r["code"]["user_questions"] for r in rs]), 2) if rs else None,
            "token_leak_replies": sum(1 for r in rs if r["code"]["token_leaks"]),
            "violations": viol,
            "mean_FLOOR": round(statistics.mean(floors), 3) if floors else None,
        }
    for case_id in sorted({r["case"] for r in rows}):
        out["by_case"][case_id] = {}
        for arm in arms:
            rs = [r for r in rows if r["case"] == case_id and r["arm"] == arm]
            if not rs:
                continue
            floors = {f"{r['variant']}#{r['sample']}": r["FLOOR"] for r in rs if r["FLOOR"] is not None}
            entry = {
                "n": len(rs),
                "blocking": sum(r["code"]["blocking"] for r in rs),
                "user_questions": [r["code"]["user_questions"] for r in rs],
                "floor_by_variant": floors,
            }
            if floors:
                vals = list(floors.values())
                entry["floor_min"], entry["floor_max"] = min(vals), max(vals)
                entry["floor_spread"] = round(max(vals) - min(vals), 3)
                expert = [v for k, v in floors.items() if "expert" in k or k.startswith("A_")]
                novice = [v for k, v in floors.items() if not ("expert" in k or k.startswith("A_"))]
                if expert and novice:
                    entry["novice_equivalence_ratio"] = round(min(novice) / max(expert), 3) if max(expert) else None
            out["by_case"][case_id][arm] = entry
    return out


def render_md(rows, summary):
    lines = ["# FieldPilot prompt-robustness report", "", "## By arm", "",
             "| arm | n | blocking on answerable | mean user questions | replies with token leaks | mean FLOOR | violations |",
             "|---|---|---|---|---|---|---|"]
    for arm, s in summary["by_arm"].items():
        lines.append(f"| {arm} | {s['n']} | {s['blocking_on_answerable_cases']}/{s['answerable_cases']} | "
                     f"{s['mean_user_questions']} | {s['token_leak_replies']} | {s['mean_FLOOR']} | "
                     f"{', '.join(f'{k}:{v}' for k, v in sorted(s['violations'].items())) or '-'} |")
    lines += ["", "## By case", "", "| case | arm | n | blocking | user questions | FLOOR min–max (spread) | novice/expert |",
              "|---|---|---|---|---|---|---|"]
    for case_id, arms in summary["by_case"].items():
        for arm, e in arms.items():
            fl = f"{e.get('floor_min')}–{e.get('floor_max')} ({e.get('floor_spread')})" if "floor_min" in e else "-"
            lines.append(f"| {case_id} | {arm} | {e['n']} | {e['blocking']} | {e['user_questions']} | {fl} | "
                         f"{e.get('novice_equivalence_ratio', '-')} |")
    lines += ["", "## Per output", "", "| file | blocking | Qs | end Qs | leaks | violations | FLOOR | FRIENDLY | BURDEN |",
              "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        c = r["code"]
        lines.append(f"| {r['file']} | {c['blocking']} | {c['user_questions']} | {c['end_questions']} | "
                     f"{len(c['token_leaks'])} | {', '.join(c['violations']) or '-'} | {r['FLOOR']} | {r['FRIENDLY']} | {r['BURDEN']} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("blind")
    b.add_argument("--outputs", required=True)
    b.add_argument("--cases", default=str(HERE / "cases.json"))
    b.add_argument("--dest", required=True)
    b.add_argument("--mapping", required=True)
    b.add_argument("--seed", type=int, default=20260925)
    b.set_defaults(func=cmd_blind)
    r = sub.add_parser("report")
    r.add_argument("--outputs", required=True)
    r.add_argument("--cases", default=str(HERE / "cases.json"))
    r.add_argument("--rubric-scores")
    r.add_argument("--mapping")
    r.add_argument("--out-md", required=True)
    r.add_argument("--out-json", required=True)
    r.set_defaults(func=cmd_report)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
