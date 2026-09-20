# Repository agent working rules

These rules document the owner's requested prevention measures. They do not grant extra permissions, change licenses, or override the current user's scope.

## Capability and evidence gate

Before saying a connected-service action is possible or impossible, inspect the tools actually available in the current session. For GitHub work, discover the connected GitHub actions and read the exact repository/ref. A local shell without `git push`, credentials, networking, or a working container does not prove the GitHub connector cannot write. Conversely, a past successful write does not prove current permissions: verify again.

Do not retract a previously reported upload merely because it is absent from memory. Read the named commit, target ref, and matching workflow run. Separate earlier completed work from the new requested update. Distinguish observed tool errors from inferred causes; do not invent backend, memory, model-level, or account-permission diagnoses.

## Authorized repository update protocol

1. Read the exact current branch commit and tree; read the files being changed. Use the remote state as the base, not an old local ZIP that predates repository-specific fixes.
2. Change only requested files and directly related tests/docs. Preserve unrelated skills, branches, existing usage terms, and private data. Never upload customer OBJ/texture files, credentials, environment dumps, caches, or private job paths as evidence.
3. Validate code and relevant positive/negative paths. A small example that skips a feature is not a test of that feature. Compilation is not behavioral validation. If the local runtime is unavailable, record that limitation and use available authorized CI; do not label unrun tests as passed.
4. Use a single commit when practical, based on the observed tree and parent. Re-read the target before ref update. Fast-forward only (`force=false`); if changed, reconcile instead of overwriting. Direct `main` writes require explicit user authorization, as in the rect-strip-uv update.
5. After a write, read the target ref and changed-file blobs again. Commit-object creation alone is not branch publication. Compare actual remote contents/hashes with the intended files.
6. Query Actions for the exact new `head_sha`, including push-triggered runs. Check each required job and step. Old green CI is not evidence for new code. A PR-only workflow query can miss a main-branch push.
7. Report separate states: prepared, committed, branch-ref verified, CI pending/failed/passed. Report a specific blocker rather than a generic inability. Do not stop with manual instructions when an authorized connector action can complete the request.

## Long-running file workflows

Use checkpoints, immutable input hashes, fresh work directories for changed code, and active-process checks. Do not restart the same timed-out stage repeatedly without checking process and saved state. Prefer a live process/session with polling when the execution tool supports it. A transport timeout is not evidence of a bad mesh or insufficient user hardware.

## Rect Strip UV acceptance contract

Read `skills/rect-strip-uv/SKILL.md`. Always keep the original UV-only high-poly result. Dense inputs additionally get a strictly smaller, independently reloaded low-poly companion when safe. Never quantize curved caps into a rectangular geometry grid. Error gates and metadata boundaries outrank face targets. If safe reduction is unavailable, disclose partial completion and retain high-poly output; do not relabel an unchanged duplicate as low-poly.

## Reporting and attribution

Claims must have current evidence: actual file, exact commit, matching CI, or explicit error. Numeric checks, generated previews, human/model visual review, DCC round trips, and lower-reasoning-model evaluations are different claims. Do not promise universal future error immunity or automatic cross-session memory. This file helps agents that actually read it.

AI assistance may be credited in an actual work commit when the owner allows it. Do not invent an email or impersonate an OpenAI/GitHub account to obtain a contributor badge. An `Assisted-by: ChatGPT` message is not a guarantee of a Contributors profile.
