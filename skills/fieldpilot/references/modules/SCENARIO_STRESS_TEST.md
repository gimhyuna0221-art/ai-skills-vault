# Scenario Stress Test — scenario-stress-01

Bounded, evidence-grounded scenario testing for FieldPilot. This module borrows the useful
idea behind multi-agent social simulation — actor relationships, second-order reactions,
counter-moves, and scenario comparison — without claiming that synthetic agents are real
customers or that the exercise predicts the future.

It adds no new model, persistent swarm engine, Zep dependency, probability score, autonomous
crawler, or paid simulation service. It runs only after the ordinary FieldPilot evidence and
alternative work is strong enough to ground the scenario.

## 1. Trigger

Load this module only when ALL of the following are true:

1. the active decision has at least two feasible actions, policies, offers, messages, prices,
   channels, launch paths or product variants to compare, or one action whose downstream
   reactions materially affect the decision;
2. real evidence already establishes the relevant market/competitor/customer context well
   enough to define actors and constraints without inventing them;
3. first- or second-order reactions from customers, competitors, channels, partners,
   communities, regulators or other actors could plausibly change the recommendation;
4. a synthetic stress test would expose a decision-changing risk, reversal condition or
   validation question rather than merely decorate the report.

Do NOT load it for:
- narrow factual lookup;
- facts-only or supplied-source-only work;
- a descriptive category report where actor reactions do not change the decision;
- cases with too little real evidence to ground actors;
- any request whose only purpose is to produce a dramatic future prediction;
- election outcome prediction, voter persuasion/targeting, or political probability claims.

If the trigger is not met, skip the module without penalty.

## 2. Evidence foundation before simulation

Real evidence always comes first. Before creating any synthetic actor or reaction:

- freeze the current decision and feasible alternatives;
- identify which material claims are FACT / SUPPORTED / INFERRED / UNKNOWN under the existing
  FieldPilot evidence rules;
- list the sources that justify each actor's observable incentives, constraints or current
  behavior;
- preserve material counterevidence;
- mark unsupported actor traits, preferences or behavioral rules as UNKNOWN rather than
  inventing demographics, budgets, motives, sentiment or purchase intent.

A synthetic scenario may combine evidence and assumptions, but it may never silently turn an
assumption into a fact.

## 3. Actor Map

Build the smallest actor map that can change the decision. Typical actor classes include:

- target user / buyer / payer;
- direct competitor;
- substitute or general-purpose AI;
- channel / marketplace / distributor;
- partner / supplier;
- reviewer / creator / community;
- regulator or platform owner when materially relevant;
- the user's own product/business as the initiating actor.

For each included actor record:

```text
ACTOR
ROLE_IN_DECISION
EVIDENCE_BACKED_INTERESTS_OR_CONSTRAINTS
UNKNOWN_TRAITS
ACTION_LEVERS
WHO_THEY_REACT_TO
SOURCE_KEYS
```

Do not create a crowd simply to imitate a swarm. Ten invented personas are worse than three
evidence-grounded actors when the latter cover the real mechanism.

## 4. Scenario design

Use the minimum number of scenarios needed to discriminate the decision. Prefer a baseline plus
the feasible alternatives already under consideration. Do not manufacture extra options just to
reach a count.

Each scenario records:

```text
SCENARIO
INITIAL_ACTION
KNOWN_ASSUMPTIONS
UNCHANGED_CONDITIONS
DECISION_QUESTION
```

Examples of legitimate initial actions:
- price A vs price B;
- launch now vs hold;
- direct sale vs marketplace;
- broad positioning vs one niche;
- feature inclusion vs deferral;
- free trial vs one-time paid offer.

The scenario is a thought experiment constrained by evidence, not a market forecast.

## 5. Reaction chain

For each scenario, trace only the reaction rounds that can materially alter the decision.

Default:
- ROUND 1 — direct reactions to the initial action;
- ROUND 2 — second-order responses to those reactions;
- ROUND 3 — only when a further counter-response can still change the decision.

For every reaction row:

```text
ACTOR
TRIGGER
SYNTHETIC_REACTION
EVIDENCE_OR_ASSUMPTION_BASIS
DIRECTIONAL_EFFECT
COUNTER_RESPONSE
CONFIDENCE_IN_HYPOTHESIS
WHAT_REAL_EVIDENCE_WOULD_CONFIRM_OR_REJECT_IT
```

Every generated reaction carries the literal state `SYNTHETIC_HYPOTHESIS`.

Never convert synthetic reactions into:
- demand evidence;
- willingness to pay;
- conversion or retention;
- market share;
- purchase probability;
- causal proof;
- forecast probability;
- observed customer feedback;
- a claim that a real actor will behave that way.

## 6. Adversarial / failure pass

At least one material adverse path must be considered when it is plausible. Examples:

- competitor copies or discounts;
- channel economics worsen;
- buyers interpret a price cut as lower quality;
- switching friction blocks adoption;
- the attractive segment is too small or expensive to reach;
- a substitute becomes "good enough";
- a platform/policy change removes the apparent advantage.

Do not force a negative story if the evidence does not support one. The purpose is to expose
fragility, not to balance every positive statement mechanically.

## 7. Scenario comparison output

Summarize with a compact comparison:

```text
SCENARIO
UPSIDE_MECHANISM
FAILURE_MECHANISM
SECOND_ORDER_RISK
WHAT_WOULD_REVERSE_THE_CURRENT_RANKING
REAL_WORLD_CHECK
STATUS: SYNTHETIC_HYPOTHESIS
```

A scenario may strengthen, weaken or leave the underlying recommendation unchanged, but it cannot
raise the evidence tier. If real evidence is weak, the correct result may simply be "the scenario
is too assumption-sensitive to discriminate."

## 8. Convert simulation into real validation, not fake certainty

The useful output of this module is usually a sharper real-world question.

Examples:
- "Would buyers still prefer A after seeing the real total price?"
- "Does competitor B actually respond with a discount in this channel?"
- "Does the target user treat the missing feature as a blocker or a nuisance?"
- "Does the marketplace fee erase the price advantage?"

FieldPilot researches any answer available from existing evidence first. Only irreducible
product-specific behavior becomes an optional real-world validation step under the existing
direct-research rules.

## 9. Report integration

When triggered in Route B, place a plain-language section such as:

```text
Scenario Stress Test (Synthetic)
- actors and relationships
- scenario A
- scenario B
- second-order risks
- what would change the recommendation
- real-world checks
```

Keep it in the customer report only when it changes the decision or clarifies a major risk. Put
the detailed actor/reaction ledger in the appendix when long. Every detailed actor/reaction ledger
row also carries `SYNTHETIC_HYPOTHESIS` so appendix detail cannot be mistaken for observed evidence.

The first sentence must explain that this is an AI-generated stress test grounded in observed
evidence, not observed behavior or a forecast.

## 10. Cost / complexity guardrail

Do not recreate MiroFish's full simulation architecture inside FieldPilot merely because the idea
is useful. This module intentionally prefers:
- a small evidence-grounded actor map;
- bounded reaction rounds;
- one current capable model;
- explicit assumptions;
- direct conversion to validation questions.

Escalate to an external simulation engine only if the user explicitly asks, tooling is authorized,
the added cost/complexity is justified, and its output is still labeled synthetic.

## 11. Design reference and license boundary

Design inspiration:
- 666ghj/MiroFish: graph building, persona/actor configuration, parallel simulation, report agent,
  and post-simulation interaction.

FieldPilot does not copy MiroFish code, prompts, data structures or AGPL-covered implementation.
The reusable idea is the abstract workflow pattern: evidence-grounded actors -> interaction ->
second-order effects -> report/inspection. MiroFish's own README presents simulation output as a
prediction engine, but FieldPilot deliberately keeps a stricter claim ceiling and does not treat
synthetic simulation as empirical market evidence.
