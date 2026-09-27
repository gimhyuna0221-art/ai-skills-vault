# Research-system comparison — readiness-review-02 (trial)

The owner clarified the rival as `Panniantong/Agent-Reach` on 2026-09-27.
Identity is now CONFIRMED_BY_OWNER. `dimayip/research-agent` remains a secondary
reference only; it is not the named rival. The earlier ambiguity is historical,
not the current state. No package or installer from either was executed.

- dimayip/research-agent @ 5fab4dc258315e9680064b565ba49a5a07ae7895:
  SKILL.md, lead-agent-prompt.md (returned portion), citations-agent-prompt.md,
  LICENSE. Planning/retrieval/synthesis/citation separation motivates the review
  boundary. Retain FieldPilot's claim-first provenance; return unsupported prose
  for repair rather than add citations after an uncorrectable draft. Do not adopt
  mandatory subagents, fixed research budgets, or removal of source appendices.
  https://github.com/dimayip/research-agent/tree/5fab4dc258315e9680064b565ba49a5a07ae7895
- Panniantong/Agent-Reach @ a19a171fa980a0785849596492e0af4db800c82f:
  agent_reach/channels/base.py, agent_reach/doctor.py, LICENSE; repository README
  also inspected as a separate web snapshot, not assumed identical to this pin.
  Ordered access alternatives and actual backend health motivate scoped readiness
  receipts. The base class explicitly says executable presence alone is not health.
  Doctor isolates failed channels and removes stale active-backend state.
  The initial readiness-review-01 adapted task-scoped receipt verification; no broad doctor, cookie import,
  proxy, new dependency, autonomous crawler, provider switch or installation.
  https://github.com/Panniantong/Agent-Reach/tree/a19a171fa980a0785849596492e0af4db800c82f

Both inspected LICENSE files say MIT. No upstream code or prompt passages are
included in this package; the small receipt helper is newly written. References
and version pins are retained for attribution and reproducibility.

Already present: source discovery/fallback, per-claim provenance, report rendering,
method qualification, single-host honesty, no global source cap, all 19 invariants.
The initial patch added a concrete check of readiness/review RECORD BINDINGS;
the confirmed-target follow-up below adds a conditional access playbook.
It cannot discover the best source, verify source truth, authenticate a reviewer,
operate external tools, or prove cost/quality superiority. Live comparative model
runs, upstream end-to-end execution and the inherited rc04 G1-G6 remain NOT_RUN.

## Optional receipt helper input (reuse existing records)

Invoke only for a material route failure/reuse or substantial report review:

```
python tools/research_receipts.py access --input ACCESS.json --root AUTHORIZED_RUN_DIR
python tools/research_receipts.py review --input REVIEW.json --root AUTHORIZED_RUN_DIR
```

ACCESS fields:
- schema_version: 1
- request: resource_key, operation, profile_id (exact, credential-free identities)
- routes: ordered records with backend_id, read_authorized, cost_authorized;
  external_submission requires submission_authorized.
- optional receipt: same three identities; status (OK/AUTH_REQUIRED/RATE_LIMITED/
  FAILED/UNAVAILABLE); probe_level (CONTENT_READ or EXECUTABLE_ONLY); observed_at
  and valid_until (timezone-aware, justified by the task, not a universal TTL);
  evidence: {path: relative path to existing read receipt, sha256: actual hash}.

REVIEW fields:
- schema_version: 1
- report, source_register, review_note: each {path, sha256} for actual local files
- author_id, reviewer_id; review_mode (SAME_SESSION/SEPARATE_SESSION/HUMAN)
- material_coverage_attested and evidence_current_for_task_attested: booleans
  recorded by the actual reviewer, not auto-filled by this helper
- disposition: SUPPORTED_WITH_LIMITS / REPAIR_REQUIRED / UNREVIEWED
- open_findings: actual unresolved findings; any nonempty list blocks a valid binding.

These are attestations, not credentials or a second source database. Exact bytes
must match current artifacts. An unchanged hash cannot establish that a claim is
true; human/AI semantic review and actual host read evidence remain separate.
Missing filesystem capability never authorizes fabricated files. No registration,
external input submission, model call or installer is performed by either command.


## Confirmed-target follow-up — 2026-09-27

At the same Agent-Reach commit, additionally inspected docs/README_en.md (full),
agent_reach/skill/SKILL_en.md (full), references/web.md (full),
references/social.md (lines 1–180) and references/video.md (lines 1–105).
The current public ref was read back at a19a171fa980a0785849596492e0af4db800c82f.
These documents define a FETCH/SEARCH capability layer, not report authoring.
Its strongest reusable idea is per-platform, per-operation upstream selection,
with task-matched reference loading and ordered fallback. Existing source and
quality selection must remain separate from access-path selection.

A new optional AGENT_REACH_ACCESS.md defines that boundary. This revision adds
no connector, crawler, dependency or account. It does not copy upstream code.
Existing receipt functions, the 19 kernel rules and all existing tests stay
unchanged. Successful local tests do not certify this new playbook's real host
behavior or access to TIO/CATCH/Instagram. Native authorized tools remain first.
Do not auto-install, auto-update, read credentials or incur cost from a fetch rule.
