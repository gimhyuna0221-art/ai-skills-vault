from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class QualityMaxContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        cls.mod=(ROOT/'references/modules/QUALITY_MAXIMUM_PERFORMANCE.md').read_text(encoding='utf-8')
        cls.cont=(ROOT/'references/modules/DECISION_CONTINUITY.md').read_text(encoding='utf-8')

    def test_revision_and_wiring(self):
        self.assertIn('quality_extension_revision: "quality-max-01"',self.skill)
        self.assertIn('QUALITY_MAXIMUM_PERFORMANCE.md',self.skill)

    def test_quality_dominates_efficiency(self):
        for x in ('high-recall competitor / substitute / reference discovery',
                  'Efficiency must never be purchased by dropping',
                  'Do not use token count, output length, elapsed time, or source count as a primary success metric'):
            self.assertIn(x,self.mod)

    def test_overlap_decomposition(self):
        for x in ('High-recall overlap decomposition','MECHANIC_OR_BEHAVIOR','GENRE_OR_CATEGORY',
                  'CROSS_CATEGORY_REFERENCE'):
            self.assertIn(x,self.mod)

    def test_representative_reference_map(self):
        for x in ('Representative reference map','REPRESENTATIVE_REFERENCE','WHY_IT_MATCHES',
                  'IMPORTANT_DIFFERENCE','WHAT_TO_LEARN_OR_AVOID'):
            self.assertIn(x,self.mod)

    def test_search_breadth_and_no_fake_exhaustiveness(self):
        for x in ('alternate category and user vocabulary','component/mechanic analogue',
                  'reviews/community language','Never claim global exhaustiveness'):
            self.assertIn(x,self.mod)

    def test_detail_not_compressed_away(self):
        self.assertIn('do not compress the useful result',self.mod)
        self.assertIn('A long answer/report is acceptable',self.mod)
        self.assertIn('Decision-first output architecture',self.cont)

    def test_generic_ai_differentiation_check(self):
        self.assertIn('general-purpose AI without FieldPilot',self.mod)
        self.assertIn('improve the investigation rather than adding decorative framework prose',self.mod)

    def test_feedback_not_overclaimed(self):
        self.assertIn('qualitative pilot feedback',self.mod)
        self.assertIn('does not prove',self.mod)

if __name__=='__main__': unittest.main()
