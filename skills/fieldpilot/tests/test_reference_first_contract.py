"""Instruction/preservation tests only; NOT a model or customer-quality evaluation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReferenceFirstContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT/'SKILL.md').read_text(encoding='utf-8')
        cls.module = (ROOT/'references/modules/REFERENCE_FIRST_VALUE.md').read_text(encoding='utf-8')
        cls.broker = (ROOT/'references/modules/BROKER_RESEARCH_DELIVERY.md').read_text(encoding='utf-8')
    def contains_all(self, *snippets):
        for snippet in snippets:
            self.assertIn(snippet, self.module)
    def test_entrypoint_before_routes_and_old_extensions_kept(self):
        self.assertLess(self.skill.index('## REFERENCE-FIRST-01'),self.skill.index('## ROUTE A'))
        for item in ('broker-exec-01','readiness-review-02','report-actionability-01','reference-first-01'):
            self.assertIn(item,self.skill)
    def test_direct_links_are_wired(self):
        self.assertIn('(references/modules/REFERENCE_FIRST_VALUE.md)',self.skill)
        self.assertIn('(REFERENCE_FIRST_VALUE.md)',self.broker)
    def test_reference_order_and_reuse(self):
        self.contains_all('before generating substantive analysis','Do not search again merely','Do not ask the user to find sources')
    def test_narrow_and_source_only_controls(self):
        self.contains_all('Narrow facts go directly','Source-only/no-browse','Returning evidence reopens affected claims only')
    def test_quality_not_popularity(self):
        self.contains_all('EVIDENCE','EXEMPLAR','SERVICE','claim-specific','not automatically the best','observation period','verified universal')
    def test_actual_access_and_permissions(self):
        self.contains_all('Partial samples establish','authorized run','Do not send private inputs','resell another')
    def test_counterevidence_and_no_infinite_discovery(self):
        self.contains_all('preserve counterevidence','not because a numeric quota','Do not search indefinitely','remaining gap')
    def test_actionability_and_customer_value(self):
        self.contains_all('preferred option','trade-offs','reversal conditions','general-purpose AI','total human work','same standard applies to FieldPilot')
    def test_no_arbitrary_kill_rules(self):
        self.contains_all("'80% overlap'", "'4 of 5'", "'two workflow steps'", 'automatic kill rules', 'One-off high-value', 'untested prepayment is not')
    def test_no_advice_and_honest_boundaries(self):
        self.contains_all('Facts-only means no advice','UNKNOWN','bounded answer','not actual model','cold-start loading')

if __name__ == '__main__':
    unittest.main()
