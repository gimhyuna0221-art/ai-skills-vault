"""Structural and declared-review checks; not an actual Copilot behavior evaluation."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('fp_report_gate', ROOT/'tests/report_actionability/review_gate.py')
G = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G)

class ReportActionabilityContract(unittest.TestCase):
    def setUp(self):
        self.output = 'Synthetic test evidence. Recommendation and conditions are present.'
        self.case = {'id':'X','subjects':['A','B'],'requires_advice':True}
        scores = {m:{'score':2,'quote':'Synthetic test evidence.','reason':'Synthetic checker fixture; not a real judgment.'} for m in G.CORE+G.ADVICE}
        self.record = {'case_id':'X','status':'REVIEWED','output_sha256':hashlib.sha256(self.output.encode()).hexdigest(),
                       'subjects':{s:copy.deepcopy(scores) for s in self.case['subjects']},'hard_failures':[]}
    def run_gate(self):
        return G.evaluate(self.case,self.record,self.output)
    def test_valid_declared_record_not_semantic_certification(self):
        r=self.run_gate(); self.assertEqual(r['status'],'REVIEW_RECORD_PASS'); self.assertFalse(r['semantic_quality_verified'])
    def test_weak_options_cannot_hide_in_average(self):
        self.record['subjects']['A']['options_tradeoffs']['score']=0
        self.assertEqual(self.run_gate()['status'],'REVIEW_RECORD_FAIL')
    def test_second_subject_must_independently_pass(self):
        self.record['subjects']['B']['next_check']['score']=1
        self.assertEqual(self.run_gate()['status'],'REVIEW_RECORD_FAIL')
    def test_missing_subject_invalid(self):
        del self.record['subjects']['B'];self.assertEqual(self.run_gate()['status'],'INVALID_REVIEW_RECORD')
    def test_missing_score_invalid(self):
        del self.record['subjects']['A']['implications'];self.assertEqual(self.run_gate()['status'],'INVALID_REVIEW_RECORD')
    def test_bool_score_invalid(self):
        self.record['subjects']['A']['implications']['score']=True
        self.assertEqual(self.run_gate()['status'],'INVALID_REVIEW_RECORD')
    def test_changed_output_invalidates_review(self):
        self.output+=' changed';self.assertEqual(self.run_gate()['status'],'INVALID_REVIEW_RECORD')
    def test_quote_must_be_in_output(self):
        self.record['subjects']['A']['implications']['quote']='invented quote'
        self.assertEqual(self.run_gate()['status'],'INVALID_REVIEW_RECORD')
    def test_pending_not_pass(self):
        self.record['status']='NOT_RUN';self.assertEqual(self.run_gate()['status'],'REVIEW_PENDING')
    def test_hard_failure_not_averaged(self):
        self.record['hard_failures']=['fabricated source'];self.assertEqual(self.run_gate()['status'],'REVIEW_RECORD_FAIL')
    def test_no_advice_control_only_requires_core(self):
        self.case['requires_advice']=False
        for s in self.record['subjects'].values():
            for k in G.ADVICE:del s[k]
        self.assertEqual(self.run_gate()['status'],'REVIEW_RECORD_PASS')
    def test_wrong_case_invalid(self):
        self.record['case_id']='Y';self.assertEqual(self.run_gate()['status'],'INVALID_REVIEW_RECORD')
    def test_routing_and_outline_link_present(self):
        skill=(ROOT/'SKILL.md').read_text()
        buyer=(ROOT/'references/modules/BUYER_FACING_DECISION_REPORT.md').read_text()
        self.assertIn('report_extension_revision: "report-actionability-01"',skill)
        self.assertIn('[report actionability](references/modules/REPORT_ACTIONABILITY.md)',skill)
        self.assertIn('[report actionability](REPORT_ACTIONABILITY.md)',buyer)
        self.assertIn('bounded presentation exception',buyer)
    def test_scope_and_negative_controls_present(self):
        module=(ROOT/'references/modules/REPORT_ACTIONABILITY.md').read_text()
        for text in ('facts-only','TWS-only','Retail price, BOM','conditional implications','not a personal GO/NO-GO','not the reasoning'):
            self.assertIn(text,module)
        cases=json.loads((ROOT/'tests/report_actionability/cases.json').read_text())['cases']
        self.assertEqual(len({c['id'] for c in cases}),len(cases))
        self.assertEqual(len(next(c for c in cases if c['id']=='BOTH')['subjects']),2)
        self.assertFalse(next(c for c in cases if c['id']=='FACTS_ONLY')['requires_advice'])
        self.assertFalse(next(c for c in cases if c['id']=='SOURCE_ONLY')['requires_advice'])

if __name__=='__main__':unittest.main()
