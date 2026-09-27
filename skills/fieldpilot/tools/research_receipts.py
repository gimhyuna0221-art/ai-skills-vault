"""Validate declared access/review receipts; no network, credentials or model calls.

Reuses broker_control's root confinement and content hashing. Results do not
certify the truth of declarations, sources, coverage or reviewer independence.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from broker_control import proof_valid, timestamp


def _object(value: Any) -> dict:
    if not isinstance(value, dict):
        raise ValueError('object required')
    return value


def _key(value: Any) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 300:
        raise ValueError('nonempty bounded identity required')
    return value


def choose_access(record: dict, root: Path, now: datetime | None = None) -> dict:
    """Recommend reuse/read/fallback from exact-scope, unexpired local evidence."""
    _object(record)
    if record.get('schema_version') != 1:
        raise ValueError('unsupported schema')
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError('timezone-aware now required')
    request = _object(record.get('request'))
    identity = {k: _key(request.get(k)) for k in ('resource_key', 'operation', 'profile_id')}
    routes = record.get('routes')
    if not isinstance(routes, list):
        raise ValueError('ordered routes required')
    assessed, ready, read_next, seen = [], [], [], set()
    for route in routes:
        route = _object(route)
        backend = _key(route.get('backend_id'))
        if not re.fullmatch(r'[A-Za-z0-9_.-]+', backend) or backend in seen:
            raise ValueError('unique credential-free backend id required')
        seen.add(backend)
        reason = 'READ_REQUIRED'
        if route.get('read_authorized') is not True or route.get('cost_authorized') is not True:
            reason = 'AUTHORITY_BLOCKED'
        elif route.get('external_submission') is True and route.get('submission_authorized') is not True:
            reason = 'SUBMISSION_BLOCKED'
        else:
            proof = route.get('receipt')
            if proof is not None:
                proof = _object(proof)
                try:
                    start, end = timestamp(proof['observed_at']), timestamp(proof['valid_until'])
                    same = all(proof.get(k) == v for k, v in identity.items())
                    current = start <= now < end
                    valid = proof_valid(proof['evidence'], root)
                    if not same:
                        reason = 'SCOPE_CHANGED'
                    elif not current:
                        reason = 'STALE_OR_FUTURE_RECEIPT'
                    elif not valid:
                        reason = 'PROOF_INVALID'
                    elif proof.get('status') == 'OK' and proof.get('probe_level') == 'CONTENT_READ':
                        reason = 'OBSERVED_READ_REUSABLE'
                    elif proof.get('status') == 'OK':
                        reason = 'CONTENT_READ_REQUIRED'
                    elif proof.get('status') in ('AUTH_REQUIRED', 'RATE_LIMITED', 'FAILED', 'UNAVAILABLE'):
                        reason = 'KNOWN_FAILURE_DO_NOT_REPEAT'
                    else:
                        reason = 'READ_REQUIRED'
                except (ValueError, KeyError, TypeError, OSError):
                    reason = 'PROOF_INVALID'
        assessed.append({'backend_id': backend, 'reason': reason})
        if reason == 'OBSERVED_READ_REUSABLE':
            ready.append(backend)
        elif reason not in ('AUTHORITY_BLOCKED', 'SUBMISSION_BLOCKED', 'KNOWN_FAILURE_DO_NOT_REPEAT'):
            read_next.append(backend)
    return {
        'status': 'OBSERVED_ROUTE_AVAILABLE' if ready else ('READ_REQUIRED' if read_next else 'ACCESS_LIMITED'),
        'selected_backend': (ready or read_next or [None])[0],
        'assessed': assessed,
        'network_executed': False,
        'source_truth_verified': False,
        'record_authenticity_verified': False,
    }


def check_review(record: dict, root: Path) -> dict:
    """Invalidate outdated or unresolved review; validate bindings, not semantics."""
    _object(record)
    if record.get('schema_version') != 1:
        raise ValueError('unsupported schema')
    failures = []
    for field in ('report', 'source_register', 'review_note'):
        if not proof_valid(record.get(field, {}), root):
            failures.append(field.upper() + '_HASH_OR_FILE_INVALID')
    for field in ('author_id', 'reviewer_id'):
        try:
            _key(record.get(field))
        except ValueError:
            failures.append(field.upper() + '_MISSING')
    mode = record.get('review_mode')
    if mode not in ('SAME_SESSION', 'SEPARATE_SESSION', 'HUMAN'):
        failures.append('REVIEW_MODE_INVALID')
    if mode in ('SEPARATE_SESSION', 'HUMAN') and record.get('author_id') == record.get('reviewer_id'):
        failures.append('INDEPENDENCE_CONTRADICTION')
    if record.get('disposition') != 'SUPPORTED_WITH_LIMITS':
        failures.append('REVIEW_NOT_ACCEPTED')
    if record.get('material_coverage_attested') is not True:
        failures.append('MATERIAL_COVERAGE_NOT_ATTESTED')
    if record.get('evidence_current_for_task_attested') is not True:
        failures.append('EVIDENCE_CURRENCY_NOT_ATTESTED')
    findings = record.get('open_findings')
    if not isinstance(findings, list):
        failures.append('OPEN_FINDINGS_MISSING')
    elif findings:
        failures.append('UNRESOLVED_FINDINGS')
    return {
        'status': 'REVIEW_BINDINGS_INVALID' if failures else 'REVIEW_BINDINGS_VALID',
        'failures': failures,
        'declared_review_mode': mode,
        'semantic_truth_verified': False,
        'coverage_independently_verified': False,
        'reviewer_authenticated': False,
        'delivery_verified': False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('access', 'review'))
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.input.stat().st_size > 2_000_000:
            raise ValueError('record too large')
        data = json.loads(args.input.read_text(encoding='utf-8'))
        result = choose_access(data, args.root) if args.command == 'access' else check_review(data, args.root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return int(result['status'] in ('ACCESS_LIMITED', 'REVIEW_BINDINGS_INVALID'))
    except (ValueError, KeyError, TypeError, OSError):
        # Do not print input values, raw tool errors or credential-bearing paths.
        print(json.dumps({'status': 'INVALID_RECORD'}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
