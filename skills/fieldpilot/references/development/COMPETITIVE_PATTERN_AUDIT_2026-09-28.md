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



### shipblueprint/deep-market-research-agent
Useful:
- one capable agent owns context while tools fetch on demand, reducing repeated context reads;
- explicit phased research for brand, desire/pain, competitors, communities, market analysis, final report;
- direct customer-voice quotes with source links;
- batch search / targeted page extraction / saved report.
Already represented or strengthened:
- FieldPilot defaults to one capable worker unless delegation adds value;
- Research Question/Coverage Map replaces fixed phases with decision-driven nodes;
- pain/review/community evidence keeps direct locators and dedup/claim ceilings;
- broker/source receipts and professional report delivery.
Not adopted:
- mandatory competitor/quote counts, since fixed quotas can reward filler and duplicate evidence.

### Hainrixz/maia-skill
Useful:
- deterministic free-source fallback before optional premium data;
- parallel specialists only where sectors are separable;
- explicit JSON/numeric data contract;
- interactive report with HTML fallback;
- bilingual delivery, accessibility, local/private report storage;
- outcome-history comparison with clear caveat that it is not an audited record.
Already represented or strengthened:
- source ladder + access receipts;
- conditional delegation, not mandatory multi-agent;
- reproducible data/transform rules;
- self-contained HTML/PDF fallback;
- premium report portability/accessibility/localization requirements;
- returning-evidence decision continuity.
Not adopted:
- investment-specific risk allocation/scoring or an interactive dashboard dependency.

### ElmatadorZ/MoneyAtlas-ClaudeSkill-Agent
Useful:
- multiple scenarios rather than one brittle prediction;
- explicit invalidation conditions, unknowns and abstention;
- human decision primacy;
- contract tests around decision gates.
Already represented:
- Scenario Stress Test, reversal conditions, UNKNOWN, claim ceilings, human approval and extensive contract tests.
Not adopted:
- financial-market-specific cycle models or numeric confidence without calibration.

## Remaining differentiated thesis

FieldPilot should not try to beat every research system at crawling, every survey platform at
fieldwork infrastructure, or every proprietary data vendor at owned data.

The commercial thesis to test is:
**one portable skill that chooses/reuses the strongest specialist evidence/tools, applies
professional market-research claim/method discipline, turns the evidence into a bounded business
decision, optionally attacks the decision through documented lenses/scenarios, and ships a
professional keepable report.**

This thesis is NOT yet proven WTP.
