"""Deterministic, portable helpers for FieldPilot v1.9.7 efficiency controls.

These helpers do not perform web search, crawl, store persistent market state, score market
success, or replace model judgment. They make dedup/saturation/delta/coverage rules testable.
"""
from urllib.parse import urlsplit
import re
import unicodedata

COVERAGE_STATES = {"OK", "LIMITED", "BLOCKED", "NOT_CHECKED", "NOT_APPLICABLE"}


def _norm(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    return re.sub(r"[^0-9a-z가-힣]+", "", value)


def canonical_entity_key(record: dict, alias_map: dict | None = None) -> str:
    name = _norm(str(record.get("name", "")))
    vendor = _norm(str(record.get("vendor", "")))
    aliases = {_norm(str(k)): _norm(str(v)) for k, v in (alias_map or {}).items()}
    if name in aliases:
        name = aliases[name]
    combined = f"{vendor}:{name}" if vendor else name
    if combined and combined != ":":
        return f"name:{combined}"
    url = str(record.get("url", ""))
    if url:
        host = urlsplit(url).netloc.casefold().removeprefix("www.")
        if host:
            return f"host:{host}"
    return f"unknown:{_norm(str(record))}"


def deduplicate_entities(records: list[dict], alias_map: dict | None = None):
    seen = set()
    unique = []
    duplicates = 0
    for record in records:
        key = canonical_entity_key(record, alias_map=alias_map)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        unique.append(record)
    return unique, duplicates


def canonical_query_key(query: str) -> str:
    terms = [t for t in re.split(r"\s+", unicodedata.normalize("NFKC", query).casefold()) if t]
    return " ".join(terms)


def deduplicate_queries(queries: list[str]):
    seen = set()
    result = []
    duplicates = 0
    for query in queries:
        key = canonical_query_key(query)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        result.append(query)
    return result, duplicates


def next_facets(facet_status: dict[str, str], alternate_route_available: dict[str, bool] | None = None):
    alternate_route_available = alternate_route_available or {}
    pending = []
    for facet, status in facet_status.items():
        if status not in COVERAGE_STATES:
            raise ValueError(f"invalid coverage status: {status}")
        if status in {"NOT_CHECKED", "LIMITED"}:
            pending.append(facet)
        elif status == "BLOCKED" and alternate_route_available.get(facet, False):
            pending.append(facet)
    return pending


def saturation_reached(
    facet_status: dict[str, str],
    recent_new_relevant_counts: list[int],
    *,
    stale_rounds_required: int = 2,
    contradiction_requires_followup: bool = False,
    newly_discovered_facet: bool = False,
    alternate_route_available: dict[str, bool] | None = None,
) -> bool:
    if contradiction_requires_followup or newly_discovered_facet:
        return False
    if next_facets(facet_status, alternate_route_available=alternate_route_available):
        return False
    if stale_rounds_required < 1 or len(recent_new_relevant_counts) < stale_rounds_required:
        return False
    return all(count == 0 for count in recent_new_relevant_counts[-stale_rounds_required:])


def full_coverage_claim_allowed(facet_status: dict[str, str]) -> bool:
    for status in facet_status.values():
        if status not in COVERAGE_STATES:
            raise ValueError(f"invalid coverage status: {status}")
        if status not in {"OK", "NOT_APPLICABLE"}:
            return False
    return True


def classify_product_state(
    *,
    code_exists: bool,
    wired_or_referenced: bool,
    acceptance_evidence: bool,
    plan_only: bool,
    contradictory: bool,
) -> str:
    if contradictory:
        return "UNKNOWN"
    if plan_only and not code_exists:
        return "PLANNED"
    if code_exists and wired_or_referenced and acceptance_evidence:
        return "IMPLEMENTED"
    if code_exists:
        return "PARTIALLY_IMPLEMENTED"
    return "UNKNOWN"


def shipping_state(*, release_evidence: bool, deployment_evidence: bool) -> str:
    if deployment_evidence:
        return "DEPLOYED"
    if release_evidence:
        return "RELEASED"
    return "UNKNOWN"


def affected_decision_sections(dependencies: dict[str, set[str]], new_evidence_tags: set[str]) -> set[str]:
    return {section for section, deps in dependencies.items() if set(deps) & set(new_evidence_tags)}


def needs_full_market_rerun(*, valid_baseline: bool, explicit_full_refresh: bool, global_scope_change: bool) -> bool:
    return (not valid_baseline) or explicit_full_refresh or global_scope_change


def compact_output_valid(payload: dict) -> bool:
    required = {
        "CURRENT_DECISION",
        "DECISIVE_EVIDENCE",
        "COUNTEREVIDENCE",
        "UNKNOWNS",
        "BUILD_CHANGE_OR_HOLD",
        "ONE_NEXT_ACTION",
    }
    if not required.issubset(payload):
        return False
    decisive = payload.get("DECISIVE_EVIDENCE")
    return isinstance(decisive, list) and len(decisive) > 0
