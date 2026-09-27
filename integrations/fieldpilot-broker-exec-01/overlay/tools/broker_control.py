"""Declared-state and physical-delivery gates. No network or model invocation.

Records are supplied by the existing trusted controller. Hashes establish
integrity, not the truth of a qualification, source or completed research.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError('timezone-aware ISO timestamp required')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('timezone required')
    return result.astimezone(timezone.utc)


def names(value):
    if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
        raise ValueError('list of nonempty strings required')
    return set(value)


def safe_file(root, value):
    if not isinstance(value, str) or not value:
        raise ValueError('relative file path required')
    rel = Path(value)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('path outside authorized root')
    base = Path(root).resolve(strict=True)
    item = base
    for part in rel.parts:
        item = item / part
        if item.is_symlink():
            raise ValueError('symlinks rejected')
    item = item.resolve(strict=True)
    if not item.is_relative_to(base) or not item.is_file():
        raise ValueError('regular file within root required')
    return item


def sha(data):
    return hashlib.sha256(data).hexdigest()


def method_hash(method):
    content = {k: v for k, v in method.items() if k not in ('qualifications', 'state')}
    return sha(json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode())


def proof_valid(proof, root):
    try:
        data = safe_file(root, proof['path']).read_bytes()
        return bool(data) and sha(data) == proof['sha256']
    except (ValueError, OSError, KeyError, TypeError):
        return False


def route(job, method, runtime, root, now=None):
    """Recommendation only. Task/risk normalization and source judgment are external."""
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError('now needs timezone')
    if job.get('delivery') not in ('CHAT', 'REPORT', 'REPORT_PLUS_APPENDIX'):
        raise ValueError('invalid delivery')
    if job.get('risk') not in ('STANDARD', 'CONSEQUENTIAL'):
        raise ValueError('explicit risk classification required')
    family = job.get('task_family')
    profile = runtime.get('profile_id')
    if not isinstance(family, str) or not family or not isinstance(profile, str) or not profile:
        raise ValueError('task family and exact runtime profile required')
    needed = names(job.get('capabilities', []))
    available = names(runtime.get('capabilities', []))
    coverage = names(job.get('coverage', []))
    base = {'delivery': job['delivery'], 'actual_model_switch': False,
            'host_mode': 'DISPATCH_AVAILABLE' if runtime.get('authorized_dispatch') is True else 'SINGLE_HOST'}
    def result(code, reason):
        return dict(base, route=code, reason=reason)
    if needed - available:
        return result('CAPABILITY_GAP', sorted(needed - available))
    if job.get('external_submission') is True and job.get('submission_authorized') is not True:
        return result('AUTHORITY_GATE', 'No private-input submission without authorization')
    if method is None:
        return result('DIRECT_OR_DESIGN', 'No reusable method; direct completion may be cheaper')
    if method.get('schema_version') != 1 or method.get('state') not in ('DRAFT', 'QUALIFIED', 'RETIRED'):
        raise ValueError('invalid method schema/state')
    if method['state'] == 'RETIRED':
        return result('REVIEW_METHOD', 'retired')
    if method.get('task_family') != family or not coverage.issubset(names(method.get('coverage', []))):
        return result('REVIEW_SCOPE', 'outside task/coverage qualification')
    scope = method.get('scope', {})
    job_scope = job.get('scope', {})
    if not isinstance(scope, dict) or not isinstance(job_scope, dict):
        raise ValueError('scope must be object')
    for key, allowed in scope.items():
        permitted = names(allowed)
        if '*' not in permitted and job_scope.get(key) not in permitted:
            return result('REVIEW_SCOPE', key)
    missing = names(method.get('capabilities', [])) - available
    if missing:
        return result('CAPABILITY_GAP', sorted(missing))
    if timestamp(method['review_by']) <= now:
        return result('REFRESH_METHOD', 'declared review boundary reached')
    for flag in ('material_conflict', 'scope_changed', 'method_failure'):
        if job.get(flag) is True:
            return result('REVIEW_AFFECTED_PART', flag)
    if job['risk'] == 'CONSEQUENTIAL':
        return result('CONSEQUENTIAL_REVIEW', 'independent/domain/human review as appropriate')
    qualified = False
    entries = method.get('qualifications', [])
    if not isinstance(entries, list):
        raise ValueError('qualifications must be list')
    for q in entries:
        try:
            valid = (q['profile_id'] == profile and q['method_hash'] == method_hash(method)
                     and q['status'] == 'PASS' and q['cold_start'] is True and q['held_out'] is True
                     and q['scope_covered'] is True and type(q['hard_failures']) is int
                     and q['hard_failures'] == 0 and bool(q['reviewer']) and bool(q['author'])
                     and q['reviewer'] != q['author'] and timestamp(q['valid_until']) > now
                     and proof_valid(q['evidence'], root))
        except (ValueError, KeyError, TypeError):
            valid = False
        qualified = qualified or valid
    if method['state'] != 'QUALIFIED' or not qualified:
        return result('QUALIFY_OR_USE_CAPABLE_CURRENT', 'no valid recorded method/runtime qualification')
    return result('EXECUTE_WITH_FACT_REFRESH' if job.get('fresh_facts_needed') is True else 'EXECUTE_QUALIFIED',
                  'controller attestation, not independently authenticated by this script')


def source_gate(record):
    if record.get('kind') not in ('SOURCE', 'SERVICE'):
        raise ValueError('source or service required')
    if not record.get('locator'):
        raise ValueError('locator required')
    if record.get('kind') == 'SERVICE':
        if record.get('service_evidence') != 'TESTED_FOR_JOB' or not record.get('evaluation_pointer'):
            return {'status': 'CANDIDATE_ONLY', 'semantic_truth_verified': False}
    access = record.get('content_access')
    if access not in ('READ', 'PARTIAL', 'LOCATED_ONLY', 'UNAVAILABLE'):
        raise ValueError('invalid access state')
    if access in ('LOCATED_ONLY', 'UNAVAILABLE'):
        return {'status': 'NOT_CLAIM_EVIDENCE', 'semantic_truth_verified': False}
    status = 'ELIGIBLE_FOR_REVIEW'
    if not record.get('read_scope') or record.get('claim_fit_checked') is not True:
        status = 'NEEDS_REVIEW'
    elif record.get('freshness_material') is True and record.get('freshness_checked') is not True:
        status = 'NEEDS_REFRESH'
    elif record.get('unresolved_conflict') is True:
        status = 'CONFLICT_OPEN'
    return {'status': status, 'scope': record.get('read_scope'), 'semantic_truth_verified': False}


def delivery(receipt, root):
    kind = receipt.get('delivery')
    if kind not in ('CHAT', 'REPORT', 'REPORT_PLUS_APPENDIX'):
        raise ValueError('invalid delivery')
    if kind == 'CHAT':
        return {'status': 'NO_FILE_REQUIRED', 'semantic_review_verified': False}
    artifacts = receipt.get('artifacts', {})
    limits = receipt.get('render_limits', {})
    if not isinstance(artifacts, dict) or not isinstance(limits, dict):
        raise ValueError('artifact/limit objects required')
    expected = {'canonical'} | ({'appendix'} if kind == 'REPORT_PLUS_APPENDIX' else set())
    failures = [f'{x}: missing artifact' for x in sorted(expected - artifacts.keys())]
    checked = {}
    for key, value in artifacts.items():
        try:
            path = safe_file(root, value)
            data = path.read_bytes()
            if not data.strip():
                raise ValueError('empty file')
            if key == 'canonical' and path.suffix.lower() != '.md':
                raise ValueError('canonical must be Markdown')
            if key == 'html' and b'<html' not in data.lower():
                raise ValueError('invalid HTML')
            if key == 'pdf' and not data.startswith(b'%PDF-'):
                raise ValueError('invalid PDF header')
            checked[key] = {'path': value, 'bytes': len(data), 'sha256': sha(data)}
        except (ValueError, OSError) as exc:
            failures.append(f'{key}: {exc}')
    for key in ('html', 'pdf'):
        if key not in artifacts and not limits.get(key):
            failures.append(f'{key}: no artifact and no explicit rendering limit')
    return {'status': 'ARTIFACT_INCOMPLETE' if failures else 'FILES_PRESENT_REVIEW_SEPARATE',
            'failures': failures, 'checked': checked, 'semantic_review_verified': False}


def break_even(design, direct, execution, review, probability, retry_cost):
    values = (design, direct, execution, review, probability, retry_cost)
    if any(not math.isfinite(x) or x < 0 for x in values) or probability > 1:
        raise ValueError('nonnegative same-unit costs; probability 0..1')
    recurring = execution + review + probability * retry_cost
    margin = direct - recurring
    return {'minimum_reuses': None if margin <= 0 else math.floor(design / margin) + 1,
            'recurring': recurring, 'measured_savings': False, 'same_quality_required': True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=('route', 'source', 'delivery'))
    p.add_argument('--input', required=True)
    p.add_argument('--root', required=True)
    a = p.parse_args()
    try:
        path = Path(a.input)
        if path.stat().st_size > 2_000_000:
            raise ValueError('control record too large')
        record = json.loads(path.read_text(encoding='utf-8'))
        if a.command == 'route':
            out = route(record['job'], record.get('method'), record['runtime'], Path(a.root))
        elif a.command == 'source':
            out = source_gate(record)
        else:
            out = delivery(record, Path(a.root))
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 1 if out.get('status') == 'ARTIFACT_INCOMPLETE' else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'INVALID_RECORD', 'error': str(exc)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
