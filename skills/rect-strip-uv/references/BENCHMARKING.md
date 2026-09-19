# Publishing benchmark and adoption record

Reviewed for this publication: 2026-09-20 (KST). This is a **repository packaging comparison**, not a measured AI-model performance ranking. The existing UV method is the baseline; external skills were not substituted for it.

| Primary reference | Observed practice | Applied here | Not claimed/adopted |
|---|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | SKILL.md frontmatter, matching folder/name, scripts and references, progressive disclosure | One self-contained skills/rect-strip-uv folder; concise entry instructions and separate detailed references | No certification or automatic discovery guarantee |
| [Anthropic skills](https://github.com/anthropics/skills) | Per-skill instructions and optional executable resources; explicit licensing/testing caveats | Instructions, local executable implementation, examples, tests and limitations together | No third-party skill code or license copied |
| [Vercel agent-skills](https://github.com/vercel-labs/agent-skills) | Discoverable collection and installation-oriented README | Collection index and quick-start before implementation detail | No marketplace listing or endorsement |
| [Vercel Skills CLI](https://github.com/vercel-labs/skills/blob/main/README.md) | owner/repo source, --skill selector, --list, skills subfolder discovery | npx skills add gimhyuna0221-art/ai-skills-vault --skill rect-strip-uv | Installer downloads the skill, not Python; host installation not executed here |
| [OpenAI Codex skills](https://developers.openai.com/codex/skills) | SKILL.md, .agents/skills paths, explicit $skill-name invocation, optional agents/openai.yaml | Existing metadata retained; manual project/user-folder instructions | Not an account-wide ChatGPT installation or approved plugin |
| [GitHub Python CI](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | setup-python, dependency installation, executable tests and artifacts | A path-scoped workflow for tests and a synthetic full-run demonstration | A workflow file is not evidence that a hosted run passed; check the run page |

## Decisions

Use the existing public ai-skills-vault instead of creating another empty repository. Place only this skill in a new subdirectory and add an index entry. Preserve unrelated skills and repository usage terms.

Retain the UV solver and original 14 tests. The only runtime change for 1.0.1 is adaptive evidence-image row height and the corresponding version bump. Add reproducible synthetic examples instead of publishing the user's production geometry.

Distinguish fresh publication tests, historical private-input regression, unexecuted model scenarios and unexecuted host installation. Keep `stable draft`: the repository's `stable` criteria require additional real cases and independent review.

## Rights and provenance

This is structural benchmarking and original explanatory writing, not a copy of another repository's implementation. No MIT/Apache license is applied to this repository. Dependencies are installed separately under their own terms. Production OBJ files, textures, font binaries, personal job paths and credentials are not distributed.
