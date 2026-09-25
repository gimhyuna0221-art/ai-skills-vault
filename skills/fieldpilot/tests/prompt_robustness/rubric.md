# Judge rubric — FieldPilot prompt-robustness suite

For a blind judge (a fresh session or a separate model) who sees only the anonymized packet:
the case facts, the user's message, and one reply. The judge never sees which skill version,
arm or model produced the reply, and must not guess it.

Score every item **0 / 1 / 2** or **NA** with a short evidence quote from the reply.

| ID | Item | 2 | 1 | 0 |
|---|---|---|---|---|
| R1 | DIRECT_ANSWER | First line directly answers the user's literal question(s) | Answer present but buried | No direct answer |
| R2 | ASSUMPTIONS_VISIBLE | Restates the understood case and key assumptions so the user can correct them | Partial | None, or assumptions presented as facts |
| R3 | ALTERNATIVES | Direct tools + substitutes + manual/spreadsheet/general-AI + do-nothing; no "no competitor"/whitespace claim without checking | Some classes missing | Missing, or a false "no competition" claim |
| R4 | PRODUCT_STATE | Clear about what is known from the user vs verified; does not invent implemented features | Vague | Invents or overstates product facts |
| R5 | POST_LAUNCH_SEPARATION (NA if not launched) | Separates reach, message, signup/activation, payment, reliability and measurement; names a discriminating check | Two or three causes, no discriminating check | Single-cause story (e.g. "just advertise") |
| R6 | MONEY_AND_CEILING (NA if no selling/charging in the case) | Payer candidates, alternative price anchors with conditions, WTP explicitly unproven | Partial | WTP/demand treated as proven, or invented market price |
| R7 | COUNTEREVIDENCE | Explicit evidence against the judgment | Implied | None |
| R8 | DECISIVE_UNKNOWNS | Names the unknowns that could flip the decision | Generic unknowns | None |
| R9 | BUILD_CHANGE_OR_HOLD | Explicit build / change / hold with scope | Vague | None |
| R10 | ONE_NEXT_ACTION | One concrete action with what to measure and how the result changes the next step; prepared by the AI where possible | Action without measurement | Several unordered actions, generic advice, or none |
| R11 | PROVENANCE | Material external claims carry sources/locators or an honest limit | Some unsourced material claims | Unsourced factual claims throughout, or fabricated sources |
| R12 | PLAIN_LANGUAGE | A beginner can follow it; terms explained; no internal-token dump | Some unexplained jargon | Hard to follow for a beginner |
| R13 | QUESTION_DISCIPLINE | Asks only user-owned facts that change the decision, ≤2, after the answer (or first only when nothing useful could be said); hard cases ask exactly the right thing | Minor excess or mistimed question | Blocks an answerable case, asks many questions, or fails to ask when nothing can be said |
| R14 | NO_HOMEWORK | Does the findable research itself | Mild push of AI-doable work to the user | Tells the user to research competitors/market size/define the brief before an answer |
| R15 | CLAIM_DISCIPLINE | No 대박/망함 labels, guaranteed channels, invented numbers, or PMF/WTP claims | Minor overreach | Material overclaim |
| R16 | LITERAL_COVERAGE (NA for single-question prompts) | Every literal question in the message answered | Some answered | Only one of several answered |

Aggregates computed by `run_eval.py`:

- `FLOOR` = mean of applicable R3–R11, R15, R16, normalized to 0–1 (research and decision floor).
- `FRIENDLY` = mean of R1, R2, R12 (delivery).
- `BURDEN` = mean of R13, R14 (user effort; higher is better).

Judge output: one JSON object per reply, keyed by the blind reply ID:

```json
{"X07": {"R1": [2, "첫 줄: '아직 망했다고 볼 근거는 없어요'"], "R5": ["NA", "not launched"], "...": ["..."]}}
```

Rules for the judge: evaluate only what is in the reply; length, tone and source count are not merit
in themselves; do not reward confident wording; `NA` only when the item truly does not apply to the
case facts given.
