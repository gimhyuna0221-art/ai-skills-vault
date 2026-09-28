# Research Question and Coverage Map — method-parity-01

A planning layer for substantial market research. It absorbs the useful pattern of
planner/executor research systems and perspective-guided question generation without adding
mandatory multi-agent fan-out, arbitrary source counts, or a second evidence architecture.

## 1. Decision first

Before searching, restore:
- the business/decision question;
- decision owner and intended use;
- subject/product/category;
- geography and time horizon where material;
- requested headings/output;
- what would actually change the decision.

Translate the business question into the **minimum sufficient set of research questions**.
Do not use a fixed count.

Each question is a `RESEARCH_QUESTION_NODE`:

```yaml
question_id:
decision_dependency:
question:
why_it_matters:
required_construct:
required_evidence:
preferred_source_or_method_classes: []
known_evidence: []
counterevidence_needed:
coverage_state: UNSTARTED | PARTIAL | ANSWERED | UNKNOWN
contradictions: []
children: []
stop_condition:
report_destination:
```

## 2. Perspective-guided expansion

To find missing questions, inspect only task-fit perspectives:
- the user's requested outline;
- comparable professional report tables of contents or public samples;
- customer/user/payer;
- direct and substitute alternatives;
- commercial/economic structure;
- channel/distribution;
- operational/technical feasibility;
- regulatory/platform constraints when material;
- negative/failure cases;
- timing/trend/freshness.

A perspective is a question generator, not evidence. Do not create sections merely because a
commercial report template contains them.

When analogous high-quality reports exist, use their public structure as an EXEMPLAR to reveal
coverage gaps, not as evidence for the target market.

## 3. Branch only on discovered uncertainty

A node may create child questions only when new evidence:
- exposes a contradiction;
- reveals a definition/denominator mismatch;
- identifies a material subgroup;
- uncovers a substitute/competitor class;
- leaves a decision-changing causal/commercial unknown;
- shows the original question was framed too broadly.

Do not recursively search because "deep research" sounds better. Close satisfied nodes and reuse
their evidence.

## 4. Retrieval and execution

For each open node:
1. use REFERENCE_FIRST_VALUE / BROKER_RESEARCH_DELIVERY;
2. reuse adequate current inspected evidence;
3. bind each retrieved passage/table/output to the question it can answer;
4. discard or de-prioritize material that is merely topically related but not decision-relevant;
5. use parallel/delegated workers only when the questions are independent enough to avoid duplicate
   work and the host supports it;
6. share original source pointers and scope, not only worker summaries.

The coverage map is the plan. It does not require a particular number of agents, models, searches,
sources, or tokens.

## 5. Pre-writing outline

Before a substantial final report:
- freeze the answered/partial/unknown node states;
- map them to the user's requested headings first;
- add only necessary sections for decision integrity;
- ensure contradictory evidence and unknowns have a visible destination;
- place methodology/audit detail in the appendix unless needed to interpret the finding.

The outline is finding-led. Empty template sections are removed or explicitly marked not applicable.

## 6. Coverage exit

A report may finish with UNKNOWN nodes when additional evidence is unavailable or not worth the
burden. It may not hide them.

Research stops when every decision-material node is:
- ANSWERED to the required claim ceiling;
- PARTIAL/UNKNOWN with the effect on the decision disclosed; or
- explicitly NOT_APPLICABLE.

This is a decision coverage stop, not a source-count stop.

## 7. Design inspirations / boundaries

Abstract patterns reviewed:
- GPT Researcher: planner -> execution/crawling -> source tracking -> publisher/report.
- Stanford STORM / Co-STORM: perspective-guided question asking, pre-writing outline, grounded
  follow-up questions, human steering/shared conceptual structure.
- UdaPlay market research agent: internal retrieval -> quality evaluation -> web fallback.

FieldPilot does not import their code or assume their benchmark claims. The adopted principle is
question coverage and source-question binding under FieldPilot's existing evidence rules.
