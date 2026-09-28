# Research Analysis and Insight Compiler — method-parity-01

Use for returned primary research, survey/panel exports, tracker studies, concept tests and other
structured customer research where analysis is required. It complements existing method cards,
CLAIM_GRAMMAR, SAMPLE_AND_FIELDWORK and EXPERT_CORE_RULES.

## 1. Freeze the analysis question before reading outcomes

Record:
- research objective / proposition;
- target population and achieved sample;
- unit and nesting;
- primary metrics / constructs;
- predefined subgroups/segments;
- weighting/modeling plan;
- comparisons and multiplicity plan where inferential;
- wave/time comparison plan where longitudinal;
- exclusions/QC rules.

Any post-hoc change stays labeled exploratory.

## 2. Data-quality and cleaning pass

Before interpreting results:
- preserve raw data;
- validate schema/types/ranges;
- identify duplicates and identity conflicts where observable;
- apply predeclared speeding/attention/straight-line or fraud rules only when supported by the
  instrument/method;
- inspect missingness, partials, dropouts and display/branch exposure;
- record exclusions and reasons append-only;
- compare included vs excluded cases when exclusion could change the result;
- do not remove inconvenient responses because they weaken the conclusion.

Low-quality flags are review states, not automatic deletion unless the predeclared rule says so.

## 3. Descriptive tables and denominators

Every material result exposes the correct base:
- raw n / eligible n / answering n as appropriate;
- count and percentage denominator;
- unweighted and weighted results when weighting is used;
- missing/not-shown/not-applicable;
- geography/segment/wave/time window;
- measure/scale definition.

Small subgroup bases remain visible. Do not hide an unstable subgroup behind a percentage.

## 4. Crosstabs / subgroup comparison

When subgroup differences can change the decision:
1. define rows/columns and the decision question;
2. show counts/bases with percentages or means;
3. check whether the sampling/design supports population inference;
4. select the appropriate inferential procedure only under its assumptions;
5. report effect size/difference and an appropriate uncertainty interval where meaningful;
6. address multiple comparisons/peeking when many cells are tested;
7. distinguish statistical from practical/business significance;
8. keep exploratory cuts labeled exploratory.

A p-value or non-overlapping interval never repairs selection, measurement, coverage or construct
bias. An opt-in sample does not become population-representative because software prints a
significance marker.

## 5. Weighting / representativeness

When weights are used:
- record benchmark/source variables;
- transformation/raking/calibration method;
- weighted and unweighted distributions;
- weight variability/effective sample size/design effect when applicable;
- residual selection/coverage limitations.

Weighting may improve alignment on observed variables; it does not guarantee representativeness.

## 6. Open-text / qualitative response analysis

For material verbatim/open-ended analysis:
- preserve original text and source row/participant;
- define or iteratively document the code/topic scheme;
- keep emergent topics distinguishable from pre-set categories;
- allow AI-assisted tagging/sentiment as a transparent processing aid, not human ground truth;
- inspect ambiguous/high-impact cases and material minority/negative themes;
- report topic frequency with the actual sample/base and avoid population prevalence language unless
  independently justified;
- keep sentiment/model uncertainty and language/translation effects visible;
- use quotations only within applicable consent/reuse rules.

Topic count + sentiment can enrich explanation; neither by itself establishes causal drivers.

## 7. Quant + qual triangulation

Compare:
- CONVERGENCE: different methods support the same bounded proposition;
- COMPLEMENTARITY: one explains/contextualizes another;
- DIVERGENCE: findings conflict or apply to different scopes.

Multiple methods do not automatically validate one another. Explain the difference in sample,
construct, mode, time or context.

## 8. Tracker / wave comparison

For repeated surveys or longitudinal tracking, freeze or document changes in:
- target population / sampling frame / recruitment channel;
- questionnaire wording/scales/order;
- collector mode;
- field dates/seasonality;
- weighting/benchmark;
- data-quality rules;
- platform/instrument version;
- definitions/calculation.

Only compare like-for-like observations. A material method break creates a new series, bridge study,
calibration, or explicit comparability limitation rather than a seamless trend claim.

## 9. Benchmarks

Before comparing to industry/global/peer benchmarks, match:
- construct;
- numerator/denominator;
- population;
- geography;
- period;
- collection mode;
- weighting/modeling;
- source independence.

A vendor benchmark is contextual evidence, not an automatic pass/fail threshold.

## 10. Reporting story and action

For substantial client delivery, lead with the decision-relevant finding, not a methodology wall.
When useful, use SCQA as an **editorial heuristic**:
- Situation — established context;
- Complication — evidence-backed problem/tension;
- Question — active business/research question;
- Answer — finding/implication/recommendation.

SCQA cannot erase counterevidence or turn UNKNOWN into an answer.

When an accepted recommendation needs an execution handoff, translate it into a SMART-like action
only to the extent supported:
- Specific;
- Measurable;
- Attainable under known resources;
- Relevant to the business question;
- Time-bound only when a defensible/user-owned timeline exists.

Never invent targets or dates merely to complete the acronym. Use UNKNOWN / owner-to-set when needed.

## 11. Output set

Applicable analysis output may include:
- cleaned-analysis manifest;
- descriptive table;
- crosstab/subgroup table;
- weighted/unweighted comparison;
- open-text topic/sentiment table;
- tracker/wave comparison;
- contradictions/limitations;
- FINDINGS -> INTERPRETATIONS -> RECOMMENDATIONS;
- source/method appendix;
- exportable CSV/XLSX/PDF/PPT only when actually materialized and verified.

This module performs or specifies analysis; it does not claim a platform executed a statistical
procedure unless the result was actually produced and inspected.
