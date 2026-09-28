from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class DecisionCouncilContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        cls.mod=(ROOT/'references/modules/EVIDENCE_GROUNDED_DECISION_COUNCIL.md').read_text(encoding='utf-8')
        cls.lib=(ROOT/'references/data/DECISION_LENS_LIBRARY.md').read_text(encoding='utf-8')

    def test_revision_and_wiring(self):
        self.assertIn('council_extension_revision: "decision-council-01"',self.skill)
        self.assertIn('EVIDENCE_GROUNDED_DECISION_COUNCIL.md',self.skill)
        self.assertIn('DECISION_LENS_LIBRARY.md',self.mod)

    def test_base_evidence_dominates(self):
        for x in ('REAL EVIDENCE','BASE FIELDPILOT DECISION','No majority vote','verified current evidence','Fame, net worth'):
            self.assertIn(x,self.mod)

    def test_no_impersonation_or_endorsement(self):
        for x in ('not role-play','Never write','actual advice','endorsement','AI clone'):
            self.assertIn(x,self.mod)

    def test_task_fit_and_small_council(self):
        self.assertIn('at most 2–3 lenses',self.mod)
        self.assertIn('If none adds material value, skip the council',self.mod)

    def test_source_ladder_and_social_limits(self):
        for x in ('shareholder/founder letters','verified first-party social posts','Follower count','direct X/social posts'):
            self.assertTrue(x in self.mod or x in self.lib)

    def test_independent_lens_and_conflict_surface(self):
        for x in ('WHAT_IT_CHALLENGES_IN_THE_BASE_DECISION','TRADEOFF_OR_COST','AGREEMENT','DISAGREEMENT','UNIQUE_BLIND_SPOTS'):
            self.assertIn(x,self.mod)

    def test_starter_cards_present(self):
        for x in ('CUSTOMER_OBSESSION_AND_REVERSIBILITY','EARLY_USER_DEMAND_AND_ITERATION','SYSTEM_PLATFORM_AND_CODESIGN'):
            self.assertIn(x,self.lib)

    def test_primary_source_urls_present(self):
        for x in ('aboutamazon.com/news/company-news/amazons-original-1997-letter-to-shareholders',
                  'aboutamazon.com/news/company-news/2016-letter-to-shareholders',
                  'ycombinator.com/library/4D-yc-s-essential-startup-advice',
                  'blogs.nvidia.com/blog/gtc-2026-news'):
            self.assertIn(x,self.lib)

    def test_council_and_scenario_separated(self):
        self.assertIn('Council = documented reasoning lenses',self.mod)
        self.assertIn('SYNTHETIC_HYPOTHESIS',self.mod)

    def test_political_use_excluded(self):
        self.assertIn('political/electoral persuasion',self.mod)
        self.assertIn('election-outcome prediction',self.mod)

if __name__=='__main__': unittest.main()
