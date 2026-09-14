# Domain Adapters — B2B, Enterprise, and SaaS/Digital

Runtime reference for FieldPilot v1.5.0. Load this module during Domain Preflight
(Section 9), after the Required Evidence Contract is compiled and before a
`MethodDecision` is finalized. Adapters ADD required fields, units, roles, and claim
restrictions on top of `PROPOSITION_AND_EVIDENCE.md`, `METHOD_ROUTER.md`, and the
method cards in `methods/`. They never weaken core inference or ethics rules, and
they compose: a project may activate more than one adapter in this file at once, and
adapters in this file frequently compose with adapters in the other three domain
files (Section 18).

## `B2B_BUYING_SYSTEM`

- **activation_signals:**
  - the buyer is an organization rather than an individual/household;
  - more than one person plausibly affects the purchase (a user, a budget holder, a
    technical reviewer, a signer);
  - the project references authority, sign-off, escalation, or an internal
    process before money or access changes hands;
  - a single enthusiastic contact ("champion") is the only evidence source offered
    for an account-level claim.
- **mandatory_preflight_fields:**
  - purchase situation and trigger (what created the need or window now);
  - initiator, user, beneficiary, champion, influencer;
  - technical, security, and legal evaluators;
  - gatekeeper, procurement, economic buyer/payer, approver/veto holder;
  - administrator and implementation/renewal owner;
  - for each identified role: authority, influence, evidence held, sequence
    relative to other roles, and points of disagreement.
  - Roles are dynamic and may overlap; the same person can hold several roles, and
    several people can share one role. No fixed role count or role taxonomy is
    treated as ground truth for any account.
- **unit_and_role_model:**
  - units of analysis: the account, the buying group/decision unit for this
    purchase situation, the individual role-holder, and the purchase-situation
    instance itself (a renewal is a different instance than a first purchase).
  - role-scoped evidence limits:
    - a user/champion can report workflow value, internal enthusiasm, and
      informal support, but not approval, procurement status, or budget;
    - a technical/security/legal evaluator can report evaluation criteria and
      blockers, but not user need or purchase intent;
    - an economic buyer/payer can report budget priority and willingness, but
      not technical fit or day-to-day usability;
    - an administrator can report deployment/operational fit, but not
      commercial terms.
  - Nested observations inside one account (several users at one company) do not
    automatically expand the account-level sample; ten users at one account remain
    evidence about that one account (Section 12.1).
- **required_evidence_additions:**
  - a role-and-authority map with sequence and disagreement recorded, not just a
    contact list;
  - explicit purchase-situation classification (first purchase, expansion,
    renewal, or replacement) because involvement and roles vary by situation;
  - disagreement/conflict register across roles, since a positive champion signal
    and a blocked security review can coexist in the same account.
- **method_router_effects:**
  - `HUMAN_DEPTH_INTERVIEW` and `OBSERVATION_CONTEXTUAL` are the primary routes to
    role-specific meaning and workflow evidence; run them across roles, not only
    the most reachable one;
  - `COMPETITOR_ALTERNATIVE` and `SECONDARY_DESK` cover documented procurement
    process, evaluation criteria, and incumbent-switching evidence;
  - a `BUYING_SYSTEM` proposition routes to a portfolio (`COMPLEMENTARITY`) that
    spans roles; a single-role method cannot alone satisfy an account-approval
    contract;
  - `NONPROBABILITY_SURVEY` or `STATED_PRICING_WTP` answered by one role remains
    scoped to that role and is not promoted to account-level or market-level
    fact;
  - `AB_RANDOMIZED_EXPERIMENT` is rarely admissible for account-level buying
    claims; the eligible-unit count is usually too small and the assignment unit
    (account vs. role-holder) must be stated explicitly if attempted.
- **domain_claim_gate:**
  - one person supports only role-specific evidence;
  - a champion cannot establish account approval, procurement status,
    deployability, budget, renewal, or market-wide demand;
  - no universal role count or role taxonomy may be asserted as a hard truth
    about how this account, or B2B buying in general, works.
- **composition_notes:**
  - composes with `ENTERPRISE` whenever the account is large enough to require
    formal security/procurement review; `ENTERPRISE` adds the process fields,
    `B2B_BUYING_SYSTEM` supplies the role map that process runs on;
  - composes with `SAAS_DIGITAL` whenever the product is delivered digitally;
    account/seat/user unit distinctions from `SAAS_DIGITAL` apply inside the
    buying-group unit defined here;
  - if `REGULATED_SENSITIVE` is also active, its consent/safeguarding/reporting
    gates take precedence over any buying-system convenience (Section 20.6).
- **rule_and_source_ids:** `R-B2B-01`; `S-BUYING-CENTER`, `S-B2B-META`.

**Escalate/stop:** if the role map cannot identify who approves, who can veto, or
who controls budget, and the decision at stake requires an account-level or
procurement-level claim, do not proceed to that claim. Route to
`CONTRACT_PARTIALLY_SATISFIABLE` or `NOT_CURRENTLY_ANSWERABLE` (Section 6.2) and
name the missing role as the next uncertainty rather than substituting the most
reachable contact's account.

## `ENTERPRISE`

- **activation_signals:**
  - the buyer has a formal procurement, security review, legal review, or
    multi-year contracting process;
  - the product requires integration with existing systems, data residency
    commitments, or change management across teams;
  - the sales/adoption path is described as pilot-then-contract, or renewal is a
    separate later event from initial use.
- **mandatory_preflight_fields:**
  - architecture/integration requirements;
  - security, privacy, and legal review requirements;
  - procurement and finance process;
  - deployment and change-management plan;
  - support and governance model;
  - data residency constraints;
  - pilot-to-contract and renewal requirements;
  - a sample plan that spans account levels (end user, administrator, security,
    procurement, executive sponsor) rather than one level only.
- **unit_and_role_model:**
  - units: the enterprise account, nested business units/teams/pilot cohorts
    inside the account, and the pilot-to-contract transition as its own unit of
    observation;
  - roles beyond those in `B2B_BUYING_SYSTEM`: security reviewer, privacy/legal
    reviewer, procurement officer, IT/deployment owner, executive sponsor, and
    the day-to-day end user;
  - end-user evidence speaks to workflow value and usability, not to security
    approval, contract terms, or renewal likelihood; procurement/legal evidence
    speaks to terms and process, not to product value.
- **required_evidence_additions:**
  - security/compliance review status and outcome;
  - data residency and vendor-risk assessment status;
  - procurement process stage and expected timeline;
  - contract and renewal terms, tracked separately from usage evidence;
  - deployment/integration readiness and change-management/support capacity;
  - pilot-to-contract conversion evidence kept as its own tracked outcome, not
    inferred from pilot usage alone.
- **method_router_effects:**
  - `OBSERVATION_CONTEXTUAL` and `HUMAN_DEPTH_INTERVIEW` cover workflow value
    across account levels;
  - `SECONDARY_DESK` covers procurement policy, compliance frameworks, and
    published security requirements;
  - `CONCIERGE_WIZARD_OF_OZ` and `ACTUAL_PAYMENT_PAID_PILOT` evidence from a pilot
    remains bound to the delivered support level and named pilot terms; it does
    not extend to production deployment or standard-terms renewal;
  - a causal claim about pilot success transporting across accounts requires an
    interference and small-sample check (`R-EXP-04`); enterprise accounts are
    typically few and heterogeneous, so `AB_RANDOMIZED_EXPERIMENT` transport
    claims need explicit justification, not assumption.
- **domain_claim_gate:**
  - a successful user pilot does not establish enterprise purchasability,
    production deployment, security approval, contract, or renewal;
  - each of those is its own proposition with its own evidence contract.
- **composition_notes:**
  - `ENTERPRISE` is almost always active alongside `B2B_BUYING_SYSTEM`; use the
    role map from that adapter and add the process fields here;
  - composes with `SAAS_DIGITAL` for digitally delivered enterprise products;
  - composes with `REGULATED_SENSITIVE` in regulated verticals (finance,
    healthcare, government); the regulated adapter's consent/reporting gates
    always win over a procurement or sales narrative (Section 20.6).
- **rule_and_source_ids:** `R-ENTERPRISE-01`; `S-BUYING-CENTER`, `S-NIST-SCRM`.

**Escalate/stop:** if security, procurement, or legal review status is unknown and
the recommendation would assert enterprise readiness, block that claim and route
to `CLAIM_NARROWING_REQUIRED` (bound the claim to the pilot's user/workflow
evidence) or `NOT_CURRENTLY_ANSWERABLE` for the deployment/contract proposition.

## `SAAS_DIGITAL`

- **activation_signals:**
  - the product is delivered as software or a digital service with accounts,
    sign-ups, or usage instrumentation;
  - pricing is structured around seats, subscriptions, or usage tiers;
  - adoption evidence is proposed from product-usage data, trials, or an
    assisted/forced pilot rollout.
- **mandatory_preflight_fields:**
  - account/user hierarchy;
  - acquisition source;
  - activation definition, stated explicitly for this project before analysis;
  - required/assisted use versus voluntary use;
  - instrumentation and its known gaps;
  - cohort/window definitions;
  - plan/seat structure;
  - trial/discount terms;
  - churn/renewal definitions;
  - integration and support dependencies.
- **unit_and_role_model:**
  - units: account, individual user, seat, and event/session;
  - roles: account owner/administrator, individual end user, and payer (who may
    differ from the user);
  - one seat's usage does not represent the account; one user's voluntary
    behavior does not represent a required or assisted rollout across the same
    account.
- **required_evidence_additions:**
  - a fixed, project-specific activation definition, set before outcome data is
    examined;
  - an exposure/opportunity denominator for every activation or retention
    statistic;
  - a voluntary-versus-required-use flag and an assisted-versus-independent
    flag on every usage record;
  - trial/discount price distinguished from list price in any pricing or WTP
    result.
- **method_router_effects:**
  - `BEHAVIORAL_ANALYTICS` is required for activation, retention, or churn
    claims, and must carry the opportunity denominator, instrumentation version,
    and voluntary/assisted flags (Section 11.8);
  - `FAKE_DOOR_LANDING` and `CONCEPT_TEST` are limited to interest/comprehension
    evidence and cannot stand in for activation or retention;
  - `ACTUAL_PAYMENT_PAID_PILOT` establishes a payment occurred under the stated
    plan/terms, not that the population accepts standard pricing;
  - `STATED_PRICING_WTP` results are never treated as conversion or payment
    evidence (Section 16.3);
  - `AB_RANDOMIZED_EXPERIMENT` assignment unit must match the claim unit (account
    vs. user vs. seat); when the product has collaborative or shared-account
    features, run the `R-EXP-04` interference check before accepting the
    estimate as independent-unit causal evidence.
- **domain_claim_gate:**
  - sign-up is not activation;
  - activation is not retention;
  - seats are not independent accounts;
  - forced or assisted pilot use is not voluntary adoption.
- **composition_notes:**
  - composes with `B2B_BUYING_SYSTEM`/`ENTERPRISE` for B2B SaaS, where account
    hierarchy here nests inside the buying-group unit there;
  - composes with `B2C` for consumer digital products;
  - composes with `TWO_SIDED_MARKETPLACE` or `NETWORK_EFFECT` for platform SaaS,
    where per-account activation evidence is necessary but not sufficient for a
    marketplace- or network-level claim.
- **rule_and_source_ids:** `R-SAAS-01`.

**Escalate/stop:** if no activation definition is fixed before usage data is
reviewed, block any activation/retention finding and require the definition to be
set first; do not retro-fit a definition that makes existing data look favorable.
If usage evidence comes only from a forced or staff-assisted rollout, cap the
claim to that assisted context and return `CLAIM_NARROWING_REQUIRED` for any
voluntary-adoption proposition.
