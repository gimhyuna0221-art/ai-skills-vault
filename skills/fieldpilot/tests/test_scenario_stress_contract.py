from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class ScenarioStressContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        cls.mod=(ROOT/'references/modules/SCENARIO_STRESS_TEST.md').read_text(encoding='utf-8')
    def test_revision_and_wiring(self):
        self.assertIn('scenario_extension_revision: "scenario-stress-01"',self.skill)
        self.assertIn('references/modules/SCENARIO_STRESS_TEST.md',self.skill)
    def test_real_evidence_first(self):
        for x in ('Real evidence always comes first','freeze the current decision','preserve material counterevidence'):
            self.assertIn(x,self.mod)
    def test_actor_and_second_order_structure(self):
        for x in ('Actor Map','ROUND 1','ROUND 2','second-order responses','COUNTER_RESPONSE'):
            self.assertIn(x,self.mod)
    def test_synthetic_never_promoted(self):
        self.assertGreaterEqual(self.mod.count('SYNTHETIC_HYPOTHESIS'),3)
        for x in ('demand evidence','willingness to pay','market share','forecast probability','observed customer feedback'):
            self.assertIn(x,self.mod)
    def test_bounded_not_swarm(self):
        for x in ('Do not create a crowd simply to imitate a swarm','one current capable model','bounded reaction rounds'):
            self.assertIn(x,self.mod)
    def test_reversal_and_real_validation(self):
        for x in ('WHAT_WOULD_REVERSE_THE_CURRENT_RANKING','REAL_WORLD_CHECK','Convert simulation into real validation'):
            self.assertIn(x,self.mod)
    def test_no_political_prediction(self):
        self.assertIn('election outcome prediction',self.mod)
        self.assertIn('voter persuasion/targeting',self.mod)
    def test_license_boundary(self):
        self.assertIn('does not copy MiroFish code',self.mod)
        self.assertIn('AGPL',self.mod)

if __name__=='__main__': unittest.main()
