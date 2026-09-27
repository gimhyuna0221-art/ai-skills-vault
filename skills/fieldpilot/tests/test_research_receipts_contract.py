"""Synthetic receipt-integrity tests, not research-quality or independent evals."""
from __future__ import annotations
import copy
from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from broker_control import sha
from research_receipts import choose_access, check_review

NOW = datetime(2026, 9, 27, 8, tzinfo=timezone.utc)


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.proofs = {}
        for name in ('read.txt', 'report.md', 'sources.md', 'review.md'):
            data = ('SYNTHETIC only: ' + name).encode()
            (self.root / name).write_bytes(data)
            self.proofs[name] = {'path': name, 'sha256': sha(data)}
        self.identity = {'resource_key': 'synthetic-company-source-v1', 'operation': 'read',
                         'profile_id': 'synthetic-runtime-profile'}
        self.receipt = dict(self.identity, status='OK', probe_level='CONTENT_READ',
                            observed_at='2026-09-27T07:00:00Z', valid_until='2026-09-27T09:00:00Z',
                            evidence=self.proofs['read.txt'])
        self.route = {'backend_id': 'native', 'read_authorized': True, 'cost_authorized': True,
                      'receipt': self.receipt}
        self.job = {'schema_version': 1, 'request': self.identity, 'routes': [self.route]}
        self.review = {'schema_version': 1, 'report': self.proofs['report.md'],
                       'source_register': self.proofs['sources.md'], 'review_note': self.proofs['review.md'],
                       'author_id': 'synthetic-writer', 'reviewer_id': 'synthetic-reviewer',
                       'review_mode': 'SEPARATE_SESSION', 'material_coverage_attested': True,
                       'evidence_current_for_task_attested': True, 'open_findings': [],
                       'disposition': 'SUPPORTED_WITH_LIMITS'}
    def access(self): return choose_access(self.job, self.root, NOW)
    def audit(self): return check_review(self.review, self.root)
    def test_valid_read_is_not_fact_verification(self):
        r=self.access(); self.assertEqual(r['status'],'OBSERVED_ROUTE_AVAILABLE')
        for key in ('network_executed','source_truth_verified','record_authenticity_verified'):
            self.assertFalse(r[key])
    def test_working_executable_is_not_read_content(self):
        self.receipt['probe_level']='EXECUTABLE_ONLY'; self.assertEqual(self.access()['status'],'READ_REQUIRED')
    def test_no_probe_can_be_combined_with_actual_task_read(self):
        self.route.pop('receipt'); self.assertEqual(self.access()['status'],'READ_REQUIRED')
    def test_scoped_failure_uses_already_authorized_fallback(self):
        fallback=copy.deepcopy(self.route); fallback['backend_id']='alternate'
        self.receipt['status']='FAILED'; self.job['routes'].append(fallback)
        r=self.access(); self.assertEqual(r['selected_backend'],'alternate')
        self.assertEqual(r['assessed'][0]['reason'],'KNOWN_FAILURE_DO_NOT_REPEAT')
    def test_all_failed_does_not_claim_ready(self):
        self.receipt['status']='UNAVAILABLE'; self.assertEqual(self.access()['status'],'ACCESS_LIMITED')
    def test_active_failure_not_retried_until_conditions_change(self):
        for status in ('FAILED','AUTH_REQUIRED','RATE_LIMITED'):
            with self.subTest(status=status):
                self.receipt['status']=status
                self.assertIsNone(self.access()['selected_backend'])
        self.receipt['valid_until']='2026-09-27T07:30:00Z'
        self.assertEqual(self.access()['status'],'READ_REQUIRED')
    def test_expired_and_future_observations_not_reused(self):
        for field,value in [('valid_until','2026-09-27T08:00:00Z'),('observed_at','2026-09-27T09:01:00Z')]:
            original=self.receipt[field]; self.receipt[field]=value
            self.assertEqual(self.access()['status'],'READ_REQUIRED'); self.receipt[field]=original
    def test_other_resource_operation_or_profile_not_reused(self):
        for field in ('resource_key','operation','profile_id'):
            original=self.receipt[field]; self.receipt[field]='different'
            self.assertEqual(self.access()['status'],'READ_REQUIRED'); self.receipt[field]=original
    def test_corrupt_or_missing_proof_not_reused(self):
        (self.root/'read.txt').write_text('changed'); self.assertEqual(self.access()['status'],'READ_REQUIRED')
        (self.root/'read.txt').unlink(); self.assertEqual(self.access()['status'],'READ_REQUIRED')
    def test_naive_time_is_invalid(self):
        self.receipt['observed_at']='2026-09-27'; self.assertEqual(self.access()['status'],'READ_REQUIRED')
        self.assertRaises(ValueError,choose_access,self.job,self.root,datetime(2026,9,27))
    def test_current_authority_overrides_past_success(self):
        self.route['read_authorized']=False; self.assertEqual(self.access()['status'],'ACCESS_LIMITED')
        self.route['read_authorized']=True; self.route['cost_authorized']=False
        self.assertEqual(self.access()['status'],'ACCESS_LIMITED')
    def test_private_submission_never_implicit(self):
        self.route['external_submission']=True; self.assertEqual(self.access()['status'],'ACCESS_LIMITED')
        self.route['submission_authorized']=True
        self.assertEqual(self.access()['status'],'OBSERVED_ROUTE_AVAILABLE')
    def test_no_routes_is_not_failure_of_source_quality(self):
        self.job['routes']=[]; self.assertEqual(self.access()['status'],'ACCESS_LIMITED')
        self.assertFalse(self.access()['source_truth_verified'])
    def test_duplicate_backend_and_secret_like_id_rejected(self):
        self.job['routes'].append(copy.deepcopy(self.route)); self.assertRaises(ValueError,self.access)
        self.job['routes'].pop(); self.route['backend_id']='user:secret@host'
        self.assertRaises(ValueError,self.access)
    def test_malformed_envelope_rejected(self):
        self.job['schema_version']=2; self.assertRaises(ValueError,self.access)
        self.review['schema_version']=2; self.assertRaises(ValueError,self.audit)
    def test_review_bindings_pass_without_semantic_certification(self):
        r=self.audit(); self.assertEqual(r['status'],'REVIEW_BINDINGS_VALID')
        for key in ('semantic_truth_verified','coverage_independently_verified','reviewer_authenticated','delivery_verified'):
            self.assertFalse(r[key])
    def test_changed_report_requires_new_review(self):
        (self.root/'report.md').write_text('Changed a material conclusion')
        self.assertIn('REPORT_HASH_OR_FILE_INVALID',self.audit()['failures'])
    def test_changed_source_register_requires_new_review(self):
        (self.root/'sources.md').write_text('Changed source')
        self.assertIn('SOURCE_REGISTER_HASH_OR_FILE_INVALID',self.audit()['failures'])
    def test_changed_or_missing_review_note_invalid(self):
        (self.root/'review.md').unlink()
        self.assertIn('REVIEW_NOTE_HASH_OR_FILE_INVALID',self.audit()['failures'])
    def test_open_unsupported_or_contradicted_claim_blocks(self):
        for finding in ('UNSUPPORTED','CONTRADICTED','OVERBROAD','CITATION_MISMATCH'):
            self.review['open_findings']=[finding]
            self.assertIn('UNRESOLVED_FINDINGS',self.audit()['failures'])
    def test_missing_inventory_currency_or_findings_blocks(self):
        for key in ('material_coverage_attested','evidence_current_for_task_attested','open_findings'):
            original=self.review.pop(key); self.assertEqual(self.audit()['status'],'REVIEW_BINDINGS_INVALID')
            self.review[key]=original
    def test_same_writer_cannot_declare_separate_reviewer(self):
        self.review['reviewer_id']=self.review['author_id']
        self.assertIn('INDEPENDENCE_CONTRADICTION',self.audit()['failures'])
    def test_same_session_is_explicit_not_fake_independence(self):
        self.review['reviewer_id']=self.review['author_id']; self.review['review_mode']='SAME_SESSION'
        r=self.audit(); self.assertEqual(r['declared_review_mode'],'SAME_SESSION')
        self.assertEqual(r['status'],'REVIEW_BINDINGS_VALID'); self.assertFalse(r['reviewer_authenticated'])
    def test_unreviewed_or_repair_required_blocks(self):
        for value in ('UNREVIEWED','REPAIR_REQUIRED',None):
            self.review['disposition']=value; self.assertIn('REVIEW_NOT_ACCEPTED',self.audit()['failures'])
    def test_outside_root_and_symlink_proofs_do_not_pass(self):
        self.review['report']['path']='../outside.md'; self.assertEqual(self.audit()['status'],'REVIEW_BINDINGS_INVALID')
        (self.root/'link.md').symlink_to(self.root/'report.md')
        self.review['report']['path']='link.md'; self.assertEqual(self.audit()['status'],'REVIEW_BINDINGS_INVALID')
    def test_existing_module_connects_bounded_tools(self):
        s=(ROOT/'references/modules/BROKER_RESEARCH_DELIVERY.md').read_text()
        for phrase in ('research_receipts.py access','research_receipts.py review',
                       'No mandatory worker','return unsupported','no extra probe','SAME_SESSION'):
            self.assertIn(phrase,s)
        self.assertTrue((ROOT/'references/modules/RESEARCH_REVIEW_NOTES.md').is_file())


if __name__=='__main__': unittest.main()
