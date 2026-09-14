# Domain Adapters — B2C, Local/Offline, Food & Beverage, Physical Product

Runtime reference for FieldPilot v1.5.0. Load this module during Domain Preflight
(Section 9), after the Required Evidence Contract is compiled and before a
`MethodDecision` is finalized. Adapters ADD required fields, units, roles, and claim
restrictions on top of `PROPOSITION_AND_EVIDENCE.md`, `METHOD_ROUTER.md`, and the
method cards in `methods/`. They never weaken core inference or ethics rules, and
they compose: a single-site food business sold to individual consumers can activate
`B2C`, `LOCAL_OFFLINE`, and `FOOD_BEVERAGE` at once, and a packaged consumer good can
add `PHYSICAL_PRODUCT` on top.

## `B2C`

- **activation_signals:**
  - the end customer is an individual or household, not an organization;
  - purchase decisions may involve more than one household member;
  - the project proposes attitude, intention, or preference evidence as a stand-in
    for purchase or repeat behavior.
- **mandatory_preflight_fields:**
  - individual and household decision actors, separated explicitly;
  - user versus payer, when they differ;
  - channel, occasion, and switching context;
  - price/promotion exposure at the time of any measured response;
  - accessibility;
  - identity/device tracking limits;
  - seasonality;
  - stated versus observed behavior, tagged on every evidence item.
- **unit_and_role_model:**
  - units: the individual consumer, the household as a decision-making group, and
    the purchase/use occasion;
  - roles: user, payer, and other household decision-influencers;
  - one household member's stated preference is evidence about that member, not
    an automatic proxy for the household's joint decision.
- **required_evidence_additions:**
  - channel and occasion recorded with every purchase/use observation;
  - price/promotion terms in effect at the time of the response;
  - an explicit stated-versus-observed tag so intention data is never silently
    read as behavior;
  - seasonal window, since consumer behavior in one season is not assumed to
    generalize to another without evidence.
- **method_router_effects:**
  - `CONCEPT_TEST` and `STATED_PRICING_WTP` supply stated response only;
  - `BEHAVIORAL_ANALYTICS` or `ACTUAL_PAYMENT_PAID_PILOT` are required for any
    observed-conversion or repeat-purchase claim;
  - `PROBABILITY_SURVEY`/`NONPROBABILITY_SURVEY` for population-level attitude
    description must state target population and scope per Section 11.6;
  - a household-level claim requires sampling more than one household actor, not
    a single-respondent survey generalized to the household.
- **domain_claim_gate:**
  - attitude or purchase intention is not conversion, repeat use, or market
    demand;
  - household or shared decisions cannot be inferred from one actor
    automatically.
- **composition_notes:**
  - composes with `LOCAL_OFFLINE`, `FOOD_BEVERAGE`, and `PHYSICAL_PRODUCT` for
    consumer goods and venues;
  - composes with `SAAS_DIGITAL` for consumer apps and `AD_SUPPORTED_MEDIA` for
    ad-funded consumer products.
- **rule_and_source_ids:** `R-B2C-01`; `S-MORWITZ`.

**Escalate/stop:** if a claim treats stated intention or attitude as behavior, or
generalizes one household member's response to the household's decision, block
and rewrite to the bounded stated-response or single-actor form (Section 16.3).

## `LOCAL_OFFLINE`

- **activation_signals:**
  - the business operates from a physical site or a bounded service area;
  - the project references foot traffic, a service radius, or a specific
    location/neighborhood;
  - evidence is proposed from observation at one site or one time window.
- **mandatory_preflight_fields:**
  - site definition;
  - catchment evidence, derived for this project rather than assumed;
  - travel friction and access;
  - daypart;
  - weekday/season;
  - capacity/queue;
  - staff;
  - servicescape;
  - local substitutes;
  - weather/events;
  - observation privacy.
  - No default radius is assumed for any business; catchment must be evidenced,
    not guessed by category.
- **unit_and_role_model:**
  - units: the site, the observation window (daypart, weekday, season), and the
    individual visitor/customer within that window;
  - roles: customer/visitor, staff, and site operator;
  - a customer observed at one site during one window supplies site- and
    time-bound evidence, not a general catchment-wide or brand-wide claim.
- **required_evidence_additions:**
  - a catchment definition with its derivation method, not an assumed radius;
  - daypart, weekday, and season recorded on every site observation;
  - capacity/queue constraints active during the observation;
  - the local competitor/substitute set for that site;
  - weather/event confounds during the observation window;
  - a privacy plan for on-site observation of bystanders and staff.
- **method_router_effects:**
  - `OBSERVATION_CONTEXTUAL` is the primary route to on-site behavior and must
    record daypart/season/capacity on every session;
  - generalizing beyond one observation window requires additional windows
    (`COMPLEMENTARITY` or `SEQUENCE` across dayparts/seasons), not one session
    extrapolated;
  - `SECONDARY_DESK` supplies local demographic/catchment context but does not
    replace site-specific observation;
  - a single-session footfall count from `BEHAVIORAL_ANALYTICS`-style counting is
    not admissible alone as qualified-demand evidence;
  - `MARKET_SIZING` for a local addressable population must state the catchment
    method used, per Section 11.3.
- **domain_claim_gate:**
  - one site/time window stays site- and time-bound;
  - footfall is not qualified demand;
  - success at one site does not establish demand at another catchment.
- **composition_notes:**
  - composes with `FOOD_BEVERAGE` when the site serves food or beverages;
  - composes with `B2C` for individual-consumer sites and `PHYSICAL_PRODUCT` when
    the site is a retail channel for a manufactured good.
- **rule_and_source_ids:** `R-LOCAL-01`; `S-SERVICESCAPE`, `S-CATCHMENT`.

**Escalate/stop:** if a claim extends beyond the observed site, daypart, or
season, or asserts a catchment radius without a stated derivation, block and
return `CLAIM_NARROWING_REQUIRED` bound to the observed site/window, or route
additional observation windows before broadening the claim.

## `FOOD_BEVERAGE`

- **activation_signals:**
  - the product or service is food or beverage, prepared, tasted, or served;
  - the project references ingredients, allergens, kitchen/prep, menu items, or
    delivery of perishable goods.
- **mandatory_preflight_fields:**
  - applicable food-safety, allergen, and licensing rules for the operating
    jurisdiction;
  - perishability;
  - storage/preparation conditions;
  - throughput under real service load;
  - sensory test conditions;
  - service mode;
  - delivery decay;
  - waste;
  - daypart.
- **unit_and_role_model:**
  - units: the dish/product batch, the service occasion, and the site/daypart
    from `LOCAL_OFFLINE` when applicable;
  - roles: customer/taster, kitchen/prep staff, regulator/inspector, and delivery
    courier;
  - a tasting participant supplies sensory-response evidence only; they cannot
    speak to safe operation, real-load throughput, or delivery quality.
- **required_evidence_additions:**
  - the applicable jurisdictional food code/allergen/licensing citation, with
    jurisdiction, effective date, and applicability basis; mark
    `QUALIFIED_REVIEW_REQUIRED` when applicability cannot be established
    (Section 9.2, 18.2);
  - perishability and storage window for every product tested;
  - throughput measured under real service load, not a single controlled
    tasting session;
  - delivery decay and quality when the offer includes delivery;
  - waste tracking when operational-feasibility claims are proposed.
- **method_router_effects:**
  - `CONCEPT_TEST` and blind/labeled tasting sessions are bounded to sensory
    response only;
  - `OBSERVATION_CONTEXTUAL` or `CONCIERGE_WIZARD_OF_OZ` under real service load
    is required for throughput, margin, or delivery-quality claims;
  - `SECONDARY_DESK` on the applicable food code/licensing regime is mandatory
    before fieldwork proceeds past preflight;
  - `ACTUAL_PAYMENT_PAID_PILOT` or repeat-purchase claims from
    `PROBABILITY_SURVEY`/`NONPROBABILITY_SURVEY` remain blocked while the
    safety/licensing preflight is unresolved (`CONDITIONAL_HARD` under
    `R-FNB-01`).
- **domain_claim_gate:**
  - concept or taste appeal does not establish safe operation, repeat purchase,
    throughput, margin, or delivery quality;
  - jurisdictional food-safety/allergen/licensing requirements are conditional
    hard gates: unresolved applicability pauses affected fieldwork rather than
    being assumed satisfied.
- **composition_notes:**
  - composes with `LOCAL_OFFLINE` for the site/daypart fields;
  - composes with `REGULATED_SENSITIVE` when the jurisdiction imposes additional
    licensing or reporting beyond a standard food code; the more protective
    ethics/legal constraint always wins (Section 20.6).
- **rule_and_source_ids:** `R-FNB-01`; `S-FDA-FOOD`.

**Escalate/stop:** if applicable food-safety, allergen, or licensing status is
unresolved, pause affected fieldwork and route to `QUALIFIED_REVIEW_REQUIRED`
before any tasting, service, or delivery claim proceeds beyond stimulus-bound
sensory response.

## `PHYSICAL_PRODUCT`

- **activation_signals:**
  - the offer is a tangible manufactured good, hardware, or physical device;
  - the project references a physical prototype, packaging, shipping, install,
    or supervised use of a sample unit.
- **mandatory_preflight_fields:**
  - separation of concept, representative-use tasks, ergonomics,
    reliability/durability, safety, manufacturability, sourcing, and inventory;
  - packaging;
  - shipping/install;
  - channel trial;
  - returns/repair;
  - end-of-life.
- **unit_and_role_model:**
  - units: the unit/SKU, the production batch, and the individual user/task;
  - roles: end user, manufacturer/supplier, channel partner, and — for
    safety-relevant products — a regulator;
  - a supervised prototype tester supplies task-performance evidence at the
    stated fidelity and support level only; they cannot speak to production
    safety, reliability, or unsupervised cost/demand.
- **required_evidence_additions:**
  - prototype fidelity level recorded on every test;
  - a representative-task definition matched to real use conditions;
  - ergonomics/safety findings separated from stated concept interest;
  - manufacturability, sourcing, and inventory constraints;
  - channel-trial, returns/repair, and end-of-life evidence when demand or
    lifecycle claims are proposed.
- **method_router_effects:**
  - `PROTOTYPE_USABILITY` covers task performance at the stated fidelity;
  - `CONCEPT_TEST` remains bounded to stated response to the shown stimulus;
  - `BEHAVIORAL_ANALYTICS` or `ACTUAL_PAYMENT_PAID_PILOT` through a real channel
    are required for demand or purchase claims;
  - device-like or safety-relevant products additionally route through
    `S-FDA-HF`/`S-ISO-USABILITY` design conditions;
  - one supervised `OBSERVATION_CONTEXTUAL` session does not stand in for
    durability, reliability, or manufacturability testing.
- **domain_claim_gate:**
  - low-fidelity concept interest or supervised prototype use does not establish
    real-use usability, safety, production reliability, cost, or demand.
- **composition_notes:**
  - composes with `LOCAL_OFFLINE`/`B2C` when the retail channel is a physical
    site or an individual consumer purchase;
  - composes with `FOOD_BEVERAGE` for packaged food products;
  - composes with `REGULATED_SENSITIVE` for medical or other regulated devices,
    where `S-FDA-HF` scope applies and the regulated adapter's gates take
    precedence.
- **rule_and_source_ids:** `R-PHYSICAL-01`; `S-ISO-USABILITY`, `S-FDA-HF`.

**Escalate/stop:** if a demand, safety, or reliability claim is proposed from
concept response or a single supervised prototype session, block and rewrite to
the bounded stimulus- or session-scoped form; require representative-use,
real-channel, or manufacturing evidence before releasing the broader claim.
