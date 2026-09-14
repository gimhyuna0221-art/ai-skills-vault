# Domain Adapters — Marketplaces, Network Effects, and Ad-Supported Media

Runtime reference for FieldPilot v1.5.0. Load this module during Domain Preflight
(Section 9), after the Required Evidence Contract is compiled and before a
`MethodDecision` is finalized. Adapters ADD required fields, units, roles, and claim
restrictions on top of `PROPOSITION_AND_EVIDENCE.md`, `METHOD_ROUTER.md`, and the
method cards in `methods/`. They never weaken core inference or ethics rules, and
they compose: a two-sided platform can activate `TWO_SIDED_MARKETPLACE` and
`NETWORK_EFFECT` together, and an ad-funded platform can add `AD_SUPPORTED_MEDIA`
without weakening either.

## `TWO_SIDED_MARKETPLACE`

- **activation_signals:**
  - the product connects two distinct participant groups that must both act for
    value to exist (supply and demand, sellers and buyers, providers and seekers);
  - the project proposes traction on one side as evidence the platform works;
  - matching, transaction completion, or cross-side price structure is part of
    the value proposition.
- **mandatory_preflight_fields:**
  - separate propositions for each side and for the cross-side interaction;
  - side-specific acquisition, activation, quality, and willingness measures;
  - price structure across sides;
  - matching/transaction success and failure;
  - trust/safety evidence;
  - single- versus multi-homing behavior;
  - disintermediation risk.
- **unit_and_role_model:**
  - units: the side-A participant, the side-B participant, and the match or
    transaction event connecting them;
  - roles: supply-side participant, demand-side participant, and platform
    operator;
  - evidence from one side (interest, sign-ups, a waitlist) speaks only to that
    side; it does not speak to matching success or to the other side's
    participation.
- **required_evidence_additions:**
  - a separate evidence contract per side, each with its own claim scope;
  - cross-side dependency and price-structure evidence, since one side's price
    or supply commonly affects the other side's participation;
  - matching/transaction success and failure rates, not just each side's
    sign-up or listing count;
  - trust/safety incidents and their resolution;
  - single- versus multi-homing and disintermediation signals when relevant to
    the decision.
- **method_router_effects:**
  - build a `COMPLEMENTARITY` portfolio spanning both sides before any
    marketplace-level claim; for example `HUMAN_DEPTH_INTERVIEW` or
    `FAKE_DOOR_LANDING` run independently on each side, not on the more
    reachable side alone;
  - `BEHAVIORAL_ANALYTICS` must report matching/transaction completion, not only
    each side's acquisition or activation numbers;
  - a `PROBABILITY_SURVEY` or `NONPROBABILITY_SURVEY` fielded to one side remains
    scoped to that side and is not promoted to a marketplace-wide finding;
  - `MARKET_SIZING` for a marketplace must model both sides' addressable
    populations, not one side extrapolated to imply the other.
- **domain_claim_gate:**
  - interest or traction on one side never validates the marketplace;
  - aggregate growth cannot hide a failing side or a failing matching mechanism;
  - no universal liquidity threshold determines when a marketplace "works."
- **composition_notes:**
  - frequently composes with `NETWORK_EFFECT`, since cross-side value dependence
    is itself a network-effect mechanism; use `NETWORK_EFFECT`'s mechanism
    fields to operationalize the cross-side dependency claimed here;
  - composes with `B2B_BUYING_SYSTEM` when one side consists of organizational
    buyers, and with `EDUCATION` for education marketplaces (Section 18);
  - the more protective ethics/legal constraint always wins when composed with
    `REGULATED_SENSITIVE` (Section 20.6).
- **rule_and_source_ids:** `R-MARKETPLACE-01`; `S-PLATFORM-RT`,
  `S-PLATFORM-ARMSTRONG`.

**Escalate/stop:** if evidence exists for only one side, block any claim about the
marketplace as a whole and return `CONTRACT_PARTIALLY_SATISFIABLE`, naming the
unaddressed side and the matching-mechanism proposition as the next uncertainty.

## `NETWORK_EFFECT`

- **activation_signals:**
  - the project claims a participant's value depends on other participants'
    presence, activity, or growth (a network, viral, or "gets better with more
    users" claim);
  - referral, collaboration, or invitation features are proposed as evidence of
    network value;
  - growth or retention curves alone are offered as proof of a network effect.
- **mandatory_preflight_fields:**
  - operationalized direct/indirect, same-side/cross-side, and local/global
    mechanism;
  - positive or negative direction of the mechanism;
  - definition of whose network exposure changes whose value;
  - an interference/spillover check addressed in the design, not left implicit.
- **unit_and_role_model:**
  - units: the participant, the network-exposure event, and the connected
    cluster or cohort;
  - roles: exposed participant and non-exposed participant (the comparator
    needed to isolate the effect), and the network operator;
  - aggregate growth or retention observed at the platform level does not
    identify which participants were actually exposed to the claimed mechanism.
- **required_evidence_additions:**
  - an explicit mechanism statement: what changes, for whom, when network size
    or density changes;
  - network-exposure measurement at the participant level, not only aggregate
    growth;
  - an interference/spillover check per `R-EXP-04` wherever participants can
    affect each other's outcomes;
  - a comparator condition with differentiated network exposure.
- **method_router_effects:**
  - a causal network-effect claim requires `AB_RANDOMIZED_EXPERIMENT` or
    `QUASI_EXPERIMENT` with the interference check from `R-EXP-04` completed;
  - `BEHAVIORAL_ANALYTICS` growth/retention curves alone are inadmissible as the
    sole evidence for a network-effect claim;
  - `OBSERVATION_CONTEXTUAL` and `HUMAN_DEPTH_INTERVIEW` may supply mechanism
    hypotheses to operationalize before testing, but cannot themselves establish
    the causal claim.
- **domain_claim_gate:**
  - growth, virality, density, or retention alone is not evidence of a network
    effect;
  - a network-effect claim requires an operationalized mechanism plus
    network-exposure evidence, or a credible comparative design that isolates
    the mechanism.
- **composition_notes:**
  - composes with `TWO_SIDED_MARKETPLACE` for cross-side network effects, with
    `SAAS_DIGITAL` for collaboration/invitation features, and with
    `AD_SUPPORTED_MEDIA` for audience-scale claims;
  - the interference check required here also applies wherever classrooms
    (`EDUCATION`), teams, or marketplaces are simultaneously active, per
    `R-EXP-04`.
- **rule_and_source_ids:** `R-NETWORK-01`, `R-EXP-04`; `S-NETWORK-EFFECTS`,
  `S-INTERFERENCE`.

**Escalate/stop:** if only aggregate growth or retention data is available and no
participant-level exposure measurement or comparator exists, block the
network-effect claim and rewrite to a bounded growth/retention finding with the
mechanism stated as an untested hypothesis (Section 16.4).

## `AD_SUPPORTED_MEDIA`

- **activation_signals:**
  - revenue depends on advertisers paying for audience attention or placement
    rather than the audience paying directly;
  - the project proposes audience engagement metrics as evidence of advertiser
    value, or vice versa;
  - attribution or "the ads caused sales" language appears without a causal
    design.
- **mandatory_preflight_fields:**
  - audience and advertiser treated as separate sides;
  - delivery/exposure;
  - qualified audience;
  - viewability;
  - invalid traffic;
  - attention;
  - interaction;
  - leads;
  - intent;
  - visitation;
  - conversion;
  - attribution/incrementality;
  - inventory/fill/yield;
  - advertiser value;
  - brand safety.
- **unit_and_role_model:**
  - units: the audience member/impression, the advertiser/campaign, and the
    exposure event;
  - roles: audience member (media consumer), advertiser (payer/buyer of
    attention), and platform operator;
  - audience-engagement metrics speak to the audience side only; advertiser-value
    claims require separate advertiser-side evidence such as renewal, spend, or
    measured ROI.
- **required_evidence_additions:**
  - delivery/exposure and viewability measurement, distinct from raw impression
    counts;
  - invalid-traffic filtering before any engagement metric is reported;
  - attention/interaction metrics kept separate from leads and intent;
  - an attribution methodology with its incrementality caveat stated explicitly;
  - inventory/fill/yield and brand-safety review when advertiser-value claims are
    proposed.
- **method_router_effects:**
  - `BEHAVIORAL_ANALYTICS` reports delivery/engagement metrics only, unless
    linked to `AB_RANDOMIZED_EXPERIMENT` or `QUASI_EXPERIMENT` for an
    incrementality claim;
  - `SECONDARY_DESK` grounded in `S-MRC`-aligned definitions is required before
    any "attribution" or "qualified audience" claim is finalized;
  - engagement, lead, or intent findings under this adapter MUST NOT be routed
    into `STATED_PRICING_WTP` or `ACTUAL_PAYMENT_PAID_PILOT` (subscription or
    payment validation) unless the actual business decision at stake is a
    subscription or payment decision; media-engagement propositions and
    payment/subscription propositions remain on separate evidence contracts.
- **domain_claim_gate:**
  - impressions, clicks, engagement, leads, intent, attribution, and direct sales
    are different outcomes and MUST NOT substitute for one another;
  - attribution is not automatically causal incrementality.
- **composition_notes:**
  - composes with `TWO_SIDED_MARKETPLACE` (audience and advertiser as the two
    sides) and `NETWORK_EFFECT` (audience-scale claims);
  - composes with `B2C` when the audience is treated as an individual consumer
    for engagement purposes.
- **rule_and_source_ids:** `R-MEDIA-01`; `S-MRC`.

**Escalate/stop:** if an attribution or incrementality claim is proposed without
a causal design, or an engagement/lead finding is being folded into a
subscription/payment proposition the decision does not require, block and
rewrite to the narrowest supported outcome category (delivery, engagement,
leads/intent, or verified transaction) before display.
