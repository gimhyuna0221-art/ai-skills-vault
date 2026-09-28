# Competitive Research-System Pattern Audit — 2026-09-28

Development reference only. Not an execution-time ranking.

## Systems inspected

### Survey / research platforms
- SurveyMonkey: professional survey lifecycle, primary/secondary distinction, objectives, audience,
  method selection, data cleaning, significance, longitudinal tracking, segmentation, reporting and
  action; broad builder/logic/collector/analysis infrastructure.
- Qualtrics: crosstabs, statistical analysis/driver exploration, open-text topic/sentiment tooling,
  research readout workflows.
- Prolific / Pollfish: respondent access/recruitment and panel controls.
- GWI / SparkToro: consumer/audience intelligence.
- Statista-style market databases: structured market/category/forecast datasets.
- Similarweb / Semrush: digital competitor/market intelligence.
- Brandwatch: social/consumer listening.

Adoption decision: absorb the research-design/analysis principles and broker capability classes;
do not rebuild panels, delivery infrastructure or proprietary datasets.

### GitHub / open research systems

#### assafelovic/gpt-researcher
Useful:
- plan questions before browsing;
- task-specific research agents;
- parallel retrieval;
- source tracking;
- context filtering;
- long-form cited report/export.
Adopted:
- Research Question/Coverage Map and source-question binding.
Not copied:
- code/runtime, fixed source-count claims, benchmark claims, mandatory parallelism.

#### stanford-oval/storm
Useful:
- perspective-guided question asking;
- grounded follow-up questions;
- pre-writing outline;
- human steering/shared conceptual map.
Adopted:
- perspective-guided coverage expansion + pre-writing outline.
Not copied:
- Wikipedia article objective, simulated expert as evidence.

#### Panniantong/Agent-Reach
Useful:
- capability layer rather than wrapper;
- ordered primary/fallback backends;
- real health probing/doctor;
- channel-specific access.
Already represented in FieldPilot:
- broker/access recipes, research receipts, fallback/access honesty.
No new runtime dependency added.

#### bytedance/deer-flow
Useful:
- subagent/harness separation;
- persistent context/memory;
- tool/skill extensibility;
- diagnostics/tracing/sandbox discipline.
Already largely represented:
- qualified method execution, receipts, durable external project state outside this skill.
Not adopted here:
- full super-agent runtime.

#### rageshns/udaplay-market-research-agent
Useful:
- internal retrieval -> evaluation -> web fallback;
- stateful cited synthesis.
Already represented:
- reference-first reuse -> gap research; source/review receipts.

#### kevinmhorvath/theboardroom
Useful:
- independent role review -> cross-examination -> integrated memo with gates.
Already represented:
- Evidence-Grounded Decision Council, but FieldPilot uses documented source-backed lenses rather
  than fictional role voices.

#### 666ghj/MiroFish
Useful:
- actor map, interaction, second-order reaction and report.
Already represented:
- Scenario Stress Test with stricter SYNTHETIC_HYPOTHESIS ceiling.

## Remaining differentiated thesis

FieldPilot should not try to beat every research system at crawling, every survey platform at
fieldwork infrastructure, or every proprietary data vendor at owned data.

The commercial thesis to test is:
**one portable skill that chooses/reuses the strongest specialist evidence/tools, applies
professional market-research claim/method discipline, turns the evidence into a bounded business
decision, optionally attacks the decision through documented lenses/scenarios, and ships a
professional keepable report.**

This thesis is NOT yet proven WTP.
