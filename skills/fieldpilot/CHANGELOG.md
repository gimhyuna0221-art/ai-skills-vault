# FieldPilot Changelog

## v1.9.9-rc03 — Lifecycle Decision Routing

- Added one lifecycle router for plain-language `/fieldpilot` use across:
  - idea validation;
  - MVP / build decisions;
  - pre-launch / pre-sell;
  - launched with no response;
  - launched with interest but no payment;
  - monetizing products;
  - returning evidence / decision updates.
- Wired existing demand-vs-distribution diagnostics, signal-integrity checks, channel routing, pricing/payment logic, competitor/substitute research, product-state comparison and decision surfaces into the lifecycle route.
- Added post-launch guards so "no response" is not collapsed into a single product or advertising cause.
- Added product-specific promotion/channel output with one first route, one fallback, an exact test and measurement logic.
- Added explicit guardrails for red-ocean, niche, customer and jackpot/no-hope claims.
- Added runtime contract tests for lifecycle routing and updated Korea-local tests to expect rc03.
- Updated public README descriptions and usage examples.

This release does not add a success-probability score, guaranteed advertising channel, PMF/WTP certification, direct code editing, autonomous spend, or proof of a niche from search absence.
