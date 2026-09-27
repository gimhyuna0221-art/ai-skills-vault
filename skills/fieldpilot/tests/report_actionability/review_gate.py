#!/usr/bin/env python3
"""Validate DECLARED rubric evidence. No LLM, source verification or self-certification."""
import argparse
import hashlib
import json
from pathlib import Path

CORE = ('format_scope', 'evidence_limits', 'purpose_fit')
ADVICE = ('implications', 'options_tradeoffs', 'next_check')

def evaluate(case: dict, record: dict, output: str) -> dict:
    if record.get('output_sha256') != hashlib.sha256(output.encode('utf-8')).hexdigest():
        return {'status':'INVALID_REVIEW_RECORD', 'reason':'output_hash_mismatch'}
    if record.get('case_id') != case['id']:
        return {'status':'INVALID_REVIEW_RECORD', 'reason':'case_mismatch'}
    if record.get('status') != 'REVIEWED':
        return {'status':'REVIEW_PENDING', 'semantic_quality_verified':False}
    required = CORE + (ADVICE if case['requires_advice'] else ())
    subjects = record.get('subjects', {})
    if set(subjects) != set(case['subjects']):
        return {'status':'INVALID_REVIEW_RECORD', 'reason':'subject_mismatch'}
    failures = []
    for subject in case['subjects']:
        scores = subjects[subject]
        for metric in required:
            item = scores.get(metric, {})
            score, reason, quote = item.get('score'), item.get('reason'), item.get('quote')
            if type(score) is not int or score not in (0,1,2) or not isinstance(reason,str) or not reason.strip():
                return {'status':'INVALID_REVIEW_RECORD','reason':f'{subject}:{metric}:missing_or_invalid_score'}
            if score > 0 and (not isinstance(quote,str) or not quote.strip() or quote not in output):
                return {'status':'INVALID_REVIEW_RECORD','reason':f'{subject}:{metric}:unsupported_quote'}
            if score < 2:
                failures.append(f'{subject}:{metric}')
    hard = record.get('hard_failures')
    if not isinstance(hard,list) or any(not isinstance(x,str) or not x.strip() for x in hard):
        return {'status':'INVALID_REVIEW_RECORD','reason':'hard_failure_list_required'}
    return {'status':'REVIEW_RECORD_FAIL' if failures or hard else 'REVIEW_RECORD_PASS',
            'failed_required_dimensions':failures,'hard_failures':hard,
            'semantic_quality_verified':False,
            'limit':'Validates declared scores/quotes and output identity only; does not authenticate the reviewer or verify sources.'}

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--cases',type=Path,required=True)
    p.add_argument('--case',required=True)
    p.add_argument('--review',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    cases=json.loads(a.cases.read_text(encoding='utf-8'))['cases']
    case=next(c for c in cases if c['id']==a.case)
    result=evaluate(case,json.loads(a.review.read_text(encoding='utf-8')),a.output.read_text(encoding='utf-8'))
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result['status']=='REVIEW_RECORD_PASS' else 1)
