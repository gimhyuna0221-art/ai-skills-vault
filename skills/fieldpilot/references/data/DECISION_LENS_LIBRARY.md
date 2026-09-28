# Decision Lens Library — starter cards for decision-council-01

These are documented decision lenses, not simulations of the named individuals and not endorsements.
The paraphrases below were built from inspected primary/official sources. Re-check currentness when
the task claims a living person's *current* view.

---

## LENS: CUSTOMER_OBSESSION_AND_REVERSIBILITY

**Display:** Customer obsession / reversible-decision lens  
**Documented inspiration:** Jeff Bezos / Amazon  
**Use when:** customer value, long-term vs short-term trade-offs, investment prioritization,
reversible vs irreversible decisions, decision speed.

### Primary sources inspected

1. Amazon, "Amazon's original 1997 letter to shareholders"  
   https://www.aboutamazon.com/news/company-news/amazons-original-1997-letter-to-shareholders  
   Published/reprinted by Amazon. Supports: relentless customer value, long-term orientation,
   market-leadership economics, willingness to invest, and prioritization of investments.

2. Amazon, "2016 Letter to Shareholders"  
   https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders  
   Published by Amazon. Supports: customer obsession, skepticism toward proxies, embracing
   external trends, reversible/two-way-door decisions, fast decisions with incomplete
   information and course correction.

### Documented principles

- Start from customer value rather than competitor imitation.
- Prefer long-term value creation over optimizing a short-term accounting appearance when the
  economics justify it.
- Separate reversible decisions from hard-to-reverse decisions; reversible decisions can use a
  lighter, faster process.
- Do not let process, surveys or internal proxies replace actual customer outcomes.
- Watch major external trends and adapt rather than assuming the current model is permanent.

### Transferable questions

- What customer outcome is materially better?
- Is this decision reversible? What is the cost of reversing it?
- Are we waiting for information that is unlikely to change the decision?
- Are we optimizing a proxy instead of an observed customer/business outcome?
- Does the investment create durable customer value or merely more features?

### Transfer limits

Amazon's scale, capital access, logistics, ecosystem and historical context are not transferable by
default. The approximate "70% information" idea from the 2016 letter is not a universal numeric
threshold for every decision. Regulated, safety-critical and irreversible decisions may require more
evidence.

Currentness state: durable historical lens; do not describe as Bezos's current advice without a
fresh primary-source check.

---

## LENS: EARLY_USER_DEMAND_AND_ITERATION

**Display:** Early-user demand / iteration lens  
**Documented inspiration:** Paul Graham / Y Combinator  
**Use when:** idea viability, MVP scope, first customers, pre-PMF growth, premature scaling,
feature prioritization.

### Primary source inspected

Y Combinator, "YC's essential startup advice"  
https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice

Supports: build something people want; launch, talk to users and iterate; do things that do not
scale; use a 90/10 approach where appropriate; avoid scaling before people want the product; focus on
early customers; treat growth as an outcome of a product users value rather than a substitute for it.

### Documented principles

- Evidence from real early users is more important than a plausible-sounding startup story.
- Launch something usable, learn from users, then iterate.
- Manual/unscalable work can be rational early if it reveals what actually needs to be built.
- Prefer a small amount of high-value work over premature infrastructure.
- Do not scale product/team/process before the core value has evidence.

### Transferable questions

- Who needs this enough to use it now?
- What can we test manually before automating?
- Are we building infrastructure before proving the core value?
- What is the smallest release that can reveal the decisive user behavior?
- Is growth being used to hide a product-value problem?

### Transfer limits

This is strongest for early-stage startups and product discovery. It is not a universal rule for
regulated deployments, mature businesses, capital-intensive infrastructure, or work where manual
testing would be unsafe/unrepresentative. "90/10" is a heuristic, not a mandatory score.

Currentness state: official YC guidance inspected; use as YC/early-stage lens, not a claim that Paul
Graham personally reviewed the user's case.

---

## LENS: SYSTEM_PLATFORM_AND_CODESIGN

**Display:** System / platform / end-to-end bottleneck lens  
**Documented inspiration:** Jensen Huang / NVIDIA  
**Use when:** AI/platform architecture, ecosystem strategy, integration vs point solution,
cost/performance bottlenecks, build-vs-compose decisions, simulation-before-build.

### Primary source inspected

NVIDIA Blog, "NVIDIA GTC 2026: Live Updates on What's Next in AI"  
https://blogs.nvidia.com/blog/gtc-2026-news/

Supports, in the context of NVIDIA's 2026 platform announcements: full-stack system thinking,
software/hardware co-design, ecosystem/platform breadth, cost/performance optimization and using
software simulation before physical deployment in the DSX context.

### Documented principles

- Judge the end-to-end system, not only one model or component.
- Bottlenecks and economics can sit at interfaces between components.
- Co-design can beat local optimization when the layers materially interact.
- Platform/ecosystem leverage can matter more than a single isolated feature.
- Simulation can reduce risk before expensive physical/irreversible deployment when the simulated
  model is appropriate.

### Transferable questions

- Is the bottleneck actually in this feature, or elsewhere in the workflow/system?
- Does an existing ecosystem already solve most of the problem?
- Would integration/orchestration create more value than another standalone component?
- What is the total system cost/performance, not just the local metric?
- Can a bounded simulation or prototype expose a failure before an expensive build?

### Transfer limits

These principles come from NVIDIA's AI infrastructure/platform context. They do not prove that
vertical integration, simulation or ecosystem expansion is optimal for a small SaaS/product. NVIDIA
performance claims are company/product claims, not universal benchmarks.

Currentness state: 2026 official NVIDIA material inspected.

---

## Source refresh and X/social rule

For any living-person lens:
- use an official long-form source as the backbone;
- use direct X/social posts only when the original post is directly accessible and materially updates
  the relevant principle;
- record date and context;
- do not infer a broad philosophy from one short post;
- reposts/screenshots without a verifiable original stay UNVERIFIED;
- if current statements contradict the stored card, preserve the conflict and refresh the card.

## Expansion candidates

Do not add these merely for fame. Add only after primary-source review and a distinct task-fit:
- product focus/simplicity;
- capital allocation;
- distribution/growth loops;
- marketplace/network effects;
- brand/premium positioning;
- operational excellence.

A new card that duplicates an existing lens should be rejected or merged rather than increasing
council size.
