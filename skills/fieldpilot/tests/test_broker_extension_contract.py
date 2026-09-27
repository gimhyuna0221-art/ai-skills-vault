"""Synthetic control tests are not model/source quality benchmarks."""
from pathlib import Path
import copy
from datetime import datetime, timezone
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from broker_control import route, source_gate, delivery, method_hash, sha, safe_file, break_even

NOW = datetime(2026, 9, 27, tzinfo=timezone.utc)


class BrokerControlTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        proof = b'SYNTHETIC FIXTURE, not qualification evidence'; (self.root/'proof').write_bytes(proof)
        self.runtime = {'profile_id':'fixture/model-effort-host-tools-v1',
                        'capabilities':['web','files','read'], 'authorized_dispatch':False}
        self.job = {'task_family':'company', 'coverage':['business','risk'], 'capabilities':['web','files'],
                    'scope':{'market':'KR'}, 'risk':'STANDARD', 'delivery':'REPORT_PLUS_APPENDIX'}
        self.method = {'schema_version':1, 'state':'QUALIFIED', 'task_family':'company',
                       'coverage':['business','risk'], 'scope':{'market':['KR']}, 'capabilities':['read'],
                       'review_by':'2026-10-01T00:00:00Z', 'qualifications':[]}
        self.method['qualifications'] = [{'profile_id':self.runtime['profile_id'],
            'method_hash':method_hash(self.method), 'status':'PASS', 'cold_start':True, 'held_out':True,
            'scope_covered':True, 'hard_failures':0, 'reviewer':'fixture-reviewer', 'author':'fixture-writer',
            'valid_until':'2026-10-01T00:00:00Z', 'evidence':{'path':'proof','sha256':sha(proof)}}]
    def run_route(self):
        return route(self.job,self.method,self.runtime,self.root,NOW)
    def test_qualified_execution_does_not_claim_model_switch(self):
        actual=self.run_route(); self.assertEqual(actual['route'],'EXECUTE_QUALIFIED')
        self.assertFalse(actual['actual_model_switch']); self.assertEqual(actual['host_mode'],'SINGLE_HOST')
    def test_available_dispatch_is_not_actual_dispatch(self):
        self.runtime['authorized_dispatch']=True; self.assertFalse(self.run_route()['actual_model_switch'])
    def test_no_method_allows_direct_path(self):
        self.assertEqual(route(self.job,None,self.runtime,self.root,NOW)['route'],'DIRECT_OR_DESIGN')
    def test_new_model_not_qualified(self):
        self.runtime['profile_id']='cheaper-unproven'; self.assertEqual(self.run_route()['route'],'QUALIFY_OR_USE_CAPABLE_CURRENT')
    def test_changed_method_body_invalidates_qualification(self):
        self.method['procedure']=['changed']; self.assertEqual(self.run_route()['route'],'QUALIFY_OR_USE_CAPABLE_CURRENT')
    def test_draft_and_retired(self):
        self.method['state']='DRAFT'; self.assertEqual(self.run_route()['route'],'QUALIFY_OR_USE_CAPABLE_CURRENT')
        self.method['state']='RETIRED'; self.assertEqual(self.run_route()['route'],'REVIEW_METHOD')
    def test_qualification_negative_cases(self):
        original=copy.deepcopy(self.method['qualifications'][0])
        for key,value in [('cold_start',False),('held_out',False),('scope_covered',False),('hard_failures',1),
                          ('hard_failures',False),('reviewer','fixture-writer'),('reviewer',''),
                          ('valid_until','2026-09-26T00:00:00Z'),('method_hash','bad')]:
            with self.subTest(key=key,value=value):
                self.method['qualifications'][0]=dict(original,**{key:value})
                self.assertEqual(self.run_route()['route'],'QUALIFY_OR_USE_CAPABLE_CURRENT')
    def test_evidence_integrity_and_missing_file(self):
        (self.root/'proof').write_text('changed'); self.assertEqual(self.run_route()['route'],'QUALIFY_OR_USE_CAPABLE_CURRENT')
        (self.root/'proof').unlink(); self.assertEqual(self.run_route()['route'],'QUALIFY_OR_USE_CAPABLE_CURRENT')
    def test_scope_and_coverage(self):
        self.job['scope']={}; self.assertEqual(self.run_route()['route'],'REVIEW_SCOPE')
        self.job['scope']={'market':'KR'}; self.job['coverage'].append('new'); self.assertEqual(self.run_route()['route'],'REVIEW_SCOPE')
    def test_job_and_method_capabilities(self):
        self.runtime['capabilities'].remove('web'); self.assertEqual(self.run_route()['route'],'CAPABILITY_GAP')
        self.runtime['capabilities']=['web','files']; self.assertEqual(self.run_route()['route'],'CAPABILITY_GAP')
    def test_private_submission_authority(self):
        self.job['external_submission']=True; self.assertEqual(self.run_route()['route'],'AUTHORITY_GATE')
    def test_method_expiry(self):
        self.method['review_by']='2026-09-26T00:00:00Z'; self.assertEqual(self.run_route()['route'],'REFRESH_METHOD')
    def test_material_exceptions(self):
        for flag in ('scope_changed','material_conflict','method_failure'):
            with self.subTest(flag=flag):
                self.job[flag]=True; self.assertEqual(self.run_route()['route'],'REVIEW_AFFECTED_PART'); self.job[flag]=False
    def test_consequential_review(self):
        self.job['risk']='CONSEQUENTIAL'; self.assertEqual(self.run_route()['route'],'CONSEQUENTIAL_REVIEW')
    def test_fact_refresh_keeps_report_delivery(self):
        self.job['fresh_facts_needed']=True
        self.assertEqual(self.run_route()['route'],'EXECUTE_WITH_FACT_REFRESH')
        self.assertEqual(self.run_route()['delivery'],'REPORT_PLUS_APPENDIX')
    def test_invalid_data_fail_closed(self):
        self.job['coverage']='all'; self.assertRaises(ValueError,self.run_route)
    def test_naive_timestamp_rejected(self):
        self.method['review_by']='2026-10-01'; self.assertRaises(ValueError,self.run_route)
    def test_access_and_popularity_not_quality(self):
        record={'kind':'SOURCE','locator':'https://example.org','content_access':'LOCATED_ONLY'}
        self.assertEqual(source_gate(record)['status'],'NOT_CLAIM_EVIDENCE')
        record.update(kind='SERVICE',popularity=999999,service_evidence='ADVERTISED')
        self.assertEqual(source_gate(record)['status'],'CANDIDATE_ONLY')
        record.update(service_evidence='TESTED_FOR_JOB')
        self.assertEqual(source_gate(record)['status'],'CANDIDATE_ONLY')
    def test_partial_scope_freshness_and_conflict(self):
        r={'kind':'SOURCE','locator':'https://example.org','content_access':'PARTIAL','read_scope':'visible paragraph',
           'claim_fit_checked':True}
        self.assertEqual(source_gate(r)['scope'],'visible paragraph'); self.assertFalse(source_gate(r)['semantic_truth_verified'])
        r['freshness_material']=True; self.assertEqual(source_gate(r)['status'],'NEEDS_REFRESH')
        r['freshness_checked']=True; r['unresolved_conflict']=True; self.assertEqual(source_gate(r)['status'],'CONFLICT_OPEN')
    def test_missing_or_empty_report_not_delivered(self):
        r={'delivery':'REPORT','artifacts':{}}
        self.assertEqual(delivery(r,self.root)['status'],'ARTIFACT_INCOMPLETE')
        (self.root/'r.md').write_text('  '); r['artifacts']={'canonical':'r.md'}
        self.assertEqual(delivery(r,self.root)['status'],'ARTIFACT_INCOMPLETE')
    def test_physical_files_not_semantic_review(self):
        (self.root/'r.md').write_text('# Synthetic')
        r={'delivery':'REPORT','artifacts':{'canonical':'r.md'},'render_limits':{'html':'unavailable','pdf':'unavailable'}}
        actual=delivery(r,self.root); self.assertEqual(actual['status'],'FILES_PRESENT_REVIEW_SEPARATE')
        self.assertFalse(actual['semantic_review_verified'])
        r['delivery']='REPORT_PLUS_APPENDIX'; self.assertEqual(delivery(r,self.root)['status'],'ARTIFACT_INCOMPLETE')
    def test_fake_pdf_rejected(self):
        (self.root/'r.md').write_text('# Fixture'); (self.root/'r.pdf').write_text('fake')
        r={'delivery':'REPORT','artifacts':{'canonical':'r.md','pdf':'r.pdf'},'render_limits':{'html':'unavailable'}}
        self.assertEqual(delivery(r,self.root)['status'],'ARTIFACT_INCOMPLETE')
    def test_narrow_chat_needs_no_file(self):
        self.assertEqual(delivery({'delivery':'CHAT'},self.root)['status'],'NO_FILE_REQUIRED')
    def test_traversal_and_symlink_rejected(self):
        self.assertRaises(ValueError,safe_file,self.root,'../outside')
        (self.root/'link').symlink_to(self.root/'proof'); self.assertRaises(ValueError,safe_file,self.root,'link')
    def test_economic_hierarchy_not_always_better(self):
        self.assertIsNone(break_even(10,2,2,1,0,0)['minimum_reuses'])
        self.assertEqual(break_even(10,5,2,1,0,0)['minimum_reuses'],6)
        self.assertFalse(break_even(0,5,2,1,0,0)['measured_savings'])
        self.assertRaises(ValueError,break_even,10,5,2,1,2,0)


class IntegratedBrokerContract(unittest.TestCase):
    def test_latest_entrypoint_and_modules(self):
        s=(ROOT/'SKILL.md').read_text()
        for token in ('version: "1.9.9-rc04"','extension_revision: "broker-exec-01"','19. **Claim discipline in delivery.**',
                      '"시장조사 해줘"','Geography and stage are never blocking questions on their own',
                      'BROKER_RESEARCH_DELIVERY.md','QUALIFIED_METHOD_EXECUTION.md','no second file request'):
            self.assertIn(token,s)
        for name in ('BROKER_RESEARCH_DELIVERY.md','QUALIFIED_METHOD_EXECUTION.md'):
            self.assertTrue((ROOT/'references/modules'/name).is_file())
    def test_no_false_certification_in_runtime(self):
        s=(ROOT/'references/modules/QUALIFIED_METHOD_EXECUTION.md').read_text()
        self.assertIn('not qualification',s)
        self.assertIn('does not independently authenticate',s)
        self.assertIn('G1-G6',s)


if __name__=='__main__': unittest.main()
