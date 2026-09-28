from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class PremiumDeliverableContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        cls.mod=(ROOT/'references/modules/PREMIUM_FINAL_REPORT_STANDARD.md').read_text(encoding='utf-8')
        cls.deliv=(ROOT/'references/modules/MARKET_RESEARCH_DELIVERABLES.md').read_text(encoding='utf-8')
    def test_revision_and_route_b_wiring(self):
        self.assertIn('delivery_extension_revision: "premium-deliverable-01"',self.skill)
        for x in ('MARKET_RESEARCH_DELIVERABLES.md','COMMERCIAL_DELIVERABLE_SYSTEM.md','PREMIUM_FINAL_REPORT_STANDARD.md'):
            self.assertIn(x,self.skill)
    def test_tangible_bundle(self):
        for x in ('FINAL_MARKET_RESEARCH_REPORT.md','report.html','report.pdf','EVIDENCE_AND_SOURCE_REGISTER','DELIVERY_AND_REVISION_NOTE'):
            self.assertIn(x,self.mod)
    def test_paid_sample_shape_without_parity_overclaim(self):
        for x in ('Executive snapshot','Key takeaways','Scope and definitions','Market dynamics','Competitive landscape','Sources and method appendix'):
            self.assertIn(x,self.mod)
        self.assertIn('Do not copy gated report text',self.mod)
        self.assertIn('not any claim that FieldPilot owns',self.mod)
    def test_no_padding_or_fake_precision(self):
        for x in ('Do not pad to hit a page count','Do not fabricate charts','Never average','UNKNOWN'):
            self.assertIn(x,self.mod)
    def test_visual_delivery_verification(self):
        for x in ('visually inspected','tables are readable and not clipped','NOT_VISUALLY_VERIFIED','same revision'):
            self.assertIn(x,self.mod)
    def test_market_deliverables_wires_standard(self):
        self.assertIn('PREMIUM_FINAL_REPORT_STANDARD.md',self.deliv)

if __name__=='__main__': unittest.main()
