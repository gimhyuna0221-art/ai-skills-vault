# Market Research Capability Catalog — dynamic broker examples

Purpose: help FieldPilot decide **which capability to seek**, not hardcode a permanent winner.
Examples below are discovered current-market candidates and must be re-verified for active
features, coverage, price, access and terms at execution time.

| Capability class | Current examples to inspect | Typical use | Important limit |
|---|---|---|---|
| Survey build / logic / collectors | SurveyMonkey, Qualtrics, Typeform | questionnaire logic, branching, piping, randomization, collectors, exports | tool capability != valid research design |
| Panel / participant recruitment | SurveyMonkey Audience, Prolific, Pollfish | access to defined respondents/participants | panel composition/selection and target-population fit must be disclosed |
| Consumer / audience intelligence | GWI, SparkToro, Statista Consumer Insights | demographics, behaviors, media/attention, audience hypotheses | provider methodology, geography and denominator differ |
| Market/category databases | official statistics, trade bodies, Statista-style market databases, specialist research firms | market magnitude, forecasts, industry structure | estimates can conflict; preserve definitions/method |
| Digital competitive intelligence | Similarweb, Semrush | traffic/share-of-traffic, acquisition channels, keywords, digital competitors | modeled digital activity != total company revenue/demand |
| Social/consumer listening | Brandwatch and comparable services | public conversation, themes, trend/social signal | social participants != target population; sentiment model limits |
| Web/multi-channel retrieval | native search/connectors, Firecrawl, Agent Reach/upstream routes | fetch/search/extract multi-source evidence | access != truth; platform terms/login/privacy matter |
| Deep research/report synthesis | current capable host, GPT Researcher-style runtimes, STORM-style systems | question planning, broad retrieval, cited synthesis | breadth != market-research validity; keep evidence claim ceilings |
| Decision challenge/council | FieldPilot Decision Council, role-based board tools | expose trade-offs/blind spots | interpretation != independent market evidence |
| Synthetic scenario stress | FieldPilot Scenario Stress, simulation systems | second-order reaction hypotheses | synthetic != observed demand/forecast |

## Selection contract

For the active job:
1. name the evidence/analysis capability actually needed;
2. discover current candidates;
3. inspect official scope and, where possible, actual output;
4. compare category/geography/period/method/access/cost/user effort;
5. reuse the strongest adequate authorized route;
6. preserve alternatives and gaps;
7. never call one platform globally best without comparable evidence.

## Build-vs-broker rule

FieldPilot should **not rebuild**:
- respondent panels;
- enterprise survey hosting/SSO;
- email/SMS delivery infrastructure;
- proprietary clickstream/consumer databases;
- large social-firehose archives;
- CRM/BI integrations already better provided elsewhere.

FieldPilot's product layer is research design + source/service brokerage + evidence QA + synthesis +
decision support + professional deliverable. Integrate or hand off to specialist infrastructure
when that is the stronger route.
