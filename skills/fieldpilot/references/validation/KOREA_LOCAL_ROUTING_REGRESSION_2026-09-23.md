# FieldPilot Korea/local-context routing regression — 2026-09-23

Status: bounded candidate validation, not a release claim.

## Observed failure

In the clean LockerDesk benchmark, FieldPilot's Korea adapter already existed, but the frozen input did not state a geography. The output correctly preserved geography/currency as UNKNOWN, yet a competing report supplied stronger Korean-local competitors, channels and privacy context. The repair must not turn that benchmark loss into a new error by assuming Korea from Korean-language use.

## Contract scenarios

1. **Korea explicit + local B2B product**
   - load Korea adapter;
   - check Korean direct competitors and local substitutes;
   - check local channel/access only if decision-material;
   - decide regulatory/privacy applicability from actual product behavior.

2. **Geography unknown + geography can flip the decision**
   - do not infer Korea from language/account/model location;
   - keep `GEOGRAPHY_UNKNOWN`;
   - local competitor/channel/regulatory coverage remains UNKNOWN/NOT_CHECKED;
   - ask at most one decision-changing geography question if a bounded conclusion cannot otherwise be given.

3. **Geography unknown + narrow geography-neutral fact**
   - do not ask for location merely to fill a schema;
   - answer the bounded fact and its material conditions.

4. **Korea explicit + offline/no-personal-data/no-internet product**
   - Korean competitor/channel checks may still matter;
   - privacy/transmission burden is not invented;
   - mark privacy dimensions not material to the current decision unless other data flows make them relevant.

5. **Korea explicit + cloud/member-data product**
   - check current official Korean privacy/regulatory sources;
   - distinguish collection/use, third-party/outsourcing, cross-border handling and other applicable dimensions;
   - no legal-certainty language from incomplete facts.

6. **Named Naver/Kakao/community recommendation**
   - verify current audience relevance and participation/operating rules;
   - community reaction remains selected-audience evidence, not market prevalence/WTP.

## Deterministic check

Run:

```bash
python skills/fieldpilot/tools/check_korea_local_contract.py
```

This static check proves the routing/safety clauses are present. It does not prove model behavior; a fresh behavioral case is still required before release/version promotion.
