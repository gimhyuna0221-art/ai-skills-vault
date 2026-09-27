# FieldPilot rc04 broker-exec-01 integration candidate

This directory is an experimental extension builder, not an installed skill.
It reads the exact rc04 correction snapshot at `cbfe0f10ef849200450cf1c826586aedcbec6450`, verifies its subtree and SKILL blob, changes only the candidate SKILL entrypoint, and adds the overlay files. All 19 original kernel rules and the original runtime corpus/tests remain.

The new source/service broker preserves company, industry and interview purposes; uses suitable existing evidence before extra research; discovers new contenders without ranking popularity as quality; and treats actual report delivery independently from research reuse.

The method-reuse lane does not force a strongest-model/weakest-model hierarchy. It reuses a current method when available, qualifies the executor for the actual method/model/host, and returns uncertain or changed work for review. No API, account, paid model call, fine-tuning or automatic model switch is provided here. Control scripts verify declared records and physical files, not the truth of the research.

## Build and verify

Use an authorized clone containing the pinned commit. The output must be a new directory outside the repository.

```bash
python integrations/fieldpilot-broker-exec-01/build_candidate.py --output /tmp/fieldpilot-candidate
python integrations/fieldpilot-broker-exec-01/build_candidate.py --output /tmp/fieldpilot-candidate --verify
```

The CI artifact contains `fieldpilot/`, the exact manifest, contract test log and a synthetic HTML renderer smoke test. The skill in the artifact is the integrated candidate; the source `skills/fieldpilot/` on this branch deliberately remains the pinned base. Do not install the source branch via a skill installer expecting its root runtime to include this extension.

## Evidence boundaries

Contract tests do not establish research accuracy, economical-model equivalence, token/quota savings, PDF quality or market leadership. Existing rc04 G1-G6 and approval debt remains open. The example method card is an expired draft with no qualifications. Live model tests require separately authorized actual hosts and independent held-out tasks. Prior SK hynix/TIO development cases may be used for regression, not independent proof.

Nothing here merges or installs the candidate. Keep the approved installation until the relevant human/behavioral gates pass. Public/private input submission, spending and publication retain their existing authority boundaries.
