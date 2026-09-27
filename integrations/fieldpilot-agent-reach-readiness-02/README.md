# FieldPilot readiness-review-02 branch overlay

This branch is an isolated trial layer on top of `worker/fieldpilot-broker-exec-20260927` (`55b1aa7824627b23304be869187dbc25d66e540d`).

It records the exact delta used to build `FieldPilot_readiness_review_02_TRIAL.zip`, including the confirmed Panniantong/Agent-Reach access-playbook adaptation and research-readiness/review receipt checks.

## Build

```bash
python integrations/fieldpilot-agent-reach-readiness-02/build_candidate.py --output /tmp/fieldpilot-readiness-review-02
```

The builder first runs the existing `integrations/fieldpilot-broker-exec-01/build_candidate.py` to reconstruct the rc04 broker candidate, then overlays the exact six changed/added files embedded in the builder payload. It does not modify `main` or any installed skill.

## Boundaries

- Panniantong/Agent-Reach is a retrieval/capability layer, not a market-research truth engine.
- Existing authorized native connectors stay preferred when they already satisfy the retrieval task.
- No automatic login, cookie extraction, proxy setup, paid service, model switch, or system install is authorized by this branch.
- This branch is for isolated evaluation. It is not approved for merge solely because contract tests pass.

## Source package

The exact trial ZIP SHA-256 and pinned upstream Agent-Reach commit are recorded in `manifest.json`.
