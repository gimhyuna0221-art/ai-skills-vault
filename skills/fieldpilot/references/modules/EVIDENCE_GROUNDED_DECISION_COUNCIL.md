# Evidence-Grounded Decision Council — decision-council-01

FieldPilot's optional decision-lens layer. It applies documented decision principles from
public primary sources to an already-researched business/product decision. It is not role-play,
impersonation, endorsement, a claim about what a real person would decide today, or a substitute
for market evidence.

The required order is:

```text
REAL EVIDENCE
-> BASE FIELDPILOT DECISION
-> 2–3 TASK-FIT DOCUMENTED LENSES (when useful)
-> AGREEMENT / CONFLICT / BLIND SPOTS
-> FIELDPILOT SYNTHESIS
-> REAL-WORLD CHECK / REVERSAL CONDITION
```

No council member gets voting power over evidence. No majority vote.

## 1. Trigger

Load this module only when:
- the user is making a material product/business/strategy choice;
- the base evidence and alternatives are already adequate enough for a bounded decision;
- applying a distinct documented decision lens could expose a trade-off, blind spot, or
  reversal condition that the base answer does not make obvious.

Do NOT load it for:
- narrow fact lookup;
- facts-only/source-only tasks;
- ordinary descriptive category reports unless the user asks for strategic interpretation;
- decisions with insufficient base evidence;
- cosmetic "what would famous person X say?" entertainment unless the user explicitly asks;
- political/electoral persuasion, voter targeting, candidate choice, or election-outcome prediction.

If the user explicitly asks for a named person whose evidence card is not verified, do not invent
one. Either research a card from primary sources or say that the named lens is not yet grounded.

## 2. Evidence card before named lens

A named lens exists only when a `DECISION_LENS_CARD` has adequate provenance:

```text
LENS_ID
DISPLAY_NAME
PERSON_OR_ORG
SOURCE_DATE_RANGE
PRIMARY_SOURCES
DOCUMENTED_PRINCIPLES
CONTEXT_OF_ORIGINAL_DECISIONS
TRANSFERABLE_QUESTIONS
NON_TRANSFERABLE_OR_RISKY_INFERENCES
CURRENTNESS_STATE
```

Source priority:
1. shareholder/founder letters, company investor material, official talks/keynotes, official
   long-form interviews/transcripts;
2. the person's own published essays/books where directly inspectable;
3. verified first-party social posts such as X only when directly accessible and material;
4. reputable secondary reporting only to contextualize, never to fabricate a principle.

Follower count, fame, quote sites, motivational graphics and reposts are not evidence.

For living figures, an old source can support a durable historical principle but not "their current
view" unless refreshed. A direct X post can update a current view, but its short context and
incentives must be recorded. Deleted/inaccessible posts are not treated as verified content.

## 3. No impersonation

Never write:
- "Jeff Bezos would definitely do X";
- "Jensen Huang says you should launch this";
- invented quotes, inner thoughts, private motives, personality traits or personal endorsements.

Prefer:
- "The Bezos/Amazon documented lens puts more weight on ...";
- "Using the YC early-stage lens, this assumption becomes the main objection ...";
- "The NVIDIA system/platform lens highlights ...".

Every named section should make clear: **documented decision lens, not the person's actual advice**.

## 4. Task-fit routing, not celebrity popularity

Select at most 2–3 lenses by decision relevance. Do not summon famous people merely because they are
famous. Suggested routing examples:

- customer value / long-term trade-off / reversible decision speed -> Bezos/Amazon lens;
- early-stage demand / first users / premature scaling / fast iteration -> YC/Paul Graham lens;
- platform/system architecture / ecosystem / end-to-end bottleneck / simulate-before-build ->
  Jensen Huang/NVIDIA lens.

If none adds material value, skip the council.

## 5. Independent lens pass

Each lens receives the same frozen:
- decision question;
- base evidence;
- alternatives;
- material constraints;
- unknowns;
- counterevidence.

It may not search selectively for support after choosing an answer unless it performs the same
reference-first and counterevidence rules as the base research.

Each lens returns:

```text
LENS
SOURCE_BASIS
WHAT_THIS_LENS_PRIORITIZES
WHAT_IT_CHALLENGES_IN_THE_BASE_DECISION
PREFERRED_OPTION_IF_ANY
WHY
TRADEOFF_OR_COST
WHAT_WOULD_CHANGE_THIS_LENS_RESULT
TRANSFER_LIMIT
```

The lens can say NO_ADDED_VALUE.

## 6. Agreement and conflict surface

After the independent passes, synthesize:

```text
AGREEMENT
DISAGREEMENT
UNIQUE_BLIND_SPOTS
SOURCE_OR_CONTEXT_CONFLICTS
BASE_EVIDENCE_THAT_DOMINATES_THE_LENSES
DECISION_RELEVANT_UNKNOWN
```

Agreement among famous lenses is not empirical corroboration. Three lenses using the same underlying
market facts still count as one evidence base plus three interpretations.

## 7. Final FieldPilot synthesis

FieldPilot, not the council, owns the final synthesis.

Priority:
1. verified current evidence;
2. user constraints and observed product/customer facts;
3. counterevidence and claim ceilings;
4. task-fit documented lenses;
5. synthetic scenario stress test, if separately triggered.

A lens can change the recommendation only by surfacing a valid trade-off, mechanism, contradiction,
or verification need. Fame, net worth, company success or rhetorical force never raises the evidence
tier.

Final output:

```text
BASE DECISION
COUNCIL INSIGHTS
WHERE THEY AGREE
WHERE THEY DISAGREE
FIELDPILOT FINAL SYNTHESIS
REVERSAL CONDITION
ONE NEXT CHECK/ACTION
```

Do not duplicate the whole market report under every lens.

## 8. Council -> Scenario Stress Test

Decision Council and Scenario Stress Test are different:
- Council = documented reasoning lenses applied to current evidence.
- Scenario Stress = synthetic downstream actor reactions to feasible actions.

When both trigger:
```text
REAL EVIDENCE
-> BASE DECISION
-> DECISION COUNCIL
-> FEASIBLE OPTIONS FROZEN
-> SCENARIO STRESS TEST
-> REAL-WORLD CHECK
```

Council statements remain INTERPRETATION. Scenario reactions remain `SYNTHETIC_HYPOTHESIS`.
Neither becomes observed customer evidence.

## 9. Report integration

For full/professional research, include a compact buyer-facing section only when it changes or
clarifies the decision:

```text
Decision Council (Documented Lenses)
- Base FieldPilot judgment
- Lens 1: insight + source basis + transfer limit
- Lens 2: insight + source basis + transfer limit
- Agreement / conflict
- Final synthesis
```

Put full source cards in the appendix. Do not use celebrity portraits, signatures, logos, or wording
that implies endorsement without separate rights/permission.

## 10. Product and legal/representation guardrails

This feature may be marketed as "public-source documented decision lenses" or equivalent. Do not
market it as:
- "Get advice from Jeff Bezos/Jensen Huang";
- "AI clone of [person]";
- "what [person] would actually do";
- endorsement, partnership, certification, or affiliation;
- a guarantee that applying a successful founder's historical principles will produce similar results.

If a lens name creates unnecessary representation risk, render the category name first and the
documented-source inspiration second, e.g. "Customer-obsession lens — based on Amazon shareholder
letters."

## 11. Current source library

Load `references/data/DECISION_LENS_LIBRARY.md` for verified starter cards. The library is a
source-backed reference, not a permanent canon. New lenses require the same provenance checks.
