from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class ResearchMethodParityContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        cls.qmap=(ROOT/'references/modules/RESEARCH_QUESTION_COVERAGE_MAP.md').read_text(encoding='utf-8')
        cls.bridge=(ROOT/'references/modules/PRIMARY_RESEARCH_PLATFORM_BRIDGE.md').read_text(encoding='utf-8')
        cls.analysis=(ROOT/'references/modules/RESEARCH_ANALYSIS_COMPILER.md').read_text(encoding='utf-8')
        cls.catalog=(ROOT/'references/data/MARKET_RESEARCH_CAPABILITY_CATALOG.md').read_text(encoding='utf-8')
        cls.premium=(ROOT/'references/modules/PREMIUM_FINAL_REPORT_STANDARD.md').read_text(encoding='utf-8')

    def test_revision_and_wiring(self):
        self.assertIn('methodology_extension_revision: "method-parity-01"',self.skill)
        for x in ('RESEARCH_QUESTION_COVERAGE_MAP.md','PRIMARY_RESEARCH_PLATFORM_BRIDGE.md','RESEARCH_ANALYSIS_COMPILER.md'):
            self.assertIn(x,self.skill)

    def test_question_map_is_decision_and_gap_driven(self):
        for x in ('minimum sufficient set','RESEARCH_QUESTION_NODE','Perspective-guided expansion','Branch only on discovered uncertainty','decision coverage stop'):
            self.assertIn(x,self.qmap)
        self.assertIn('not a source-count stop',self.qmap)

    def test_survey_execution_features_are_explicit(self):
        for x in ('skip_or_branch_logic','answer_piping_or_prefill','question_choice_block_randomization','quotas_or_composition_controls','multilingual_and_translation_workflow','accessibility_requirements'):
            self.assertIn(x,self.bridge)

    def test_platform_is_brokered_not_rebuilt(self):
        for x in ('SURVEY_BUILD_AND_LOGIC','RESPONDENT_PANEL / RECRUITMENT','DIGITAL COMPETITIVE INTELLIGENCE','SOCIAL / CONSUMER LISTENING','not a permanent ranking'):
            self.assertTrue(x in self.bridge or x in self.catalog)
        self.assertIn('FieldPilot should **not rebuild**',self.catalog)

    def test_analysis_compiler_has_professional_controls(self):
        for x in ('Data-quality and cleaning pass','Crosstabs / subgroup comparison','statistical from practical','Weighting / representativeness','Open-text / qualitative response analysis','Tracker / wave comparison'):
            self.assertIn(x,self.analysis)

    def test_no_fake_significance_or_representativeness(self):
        self.assertIn('does not become population-representative',self.analysis)
        self.assertIn('does not guarantee representativeness',self.analysis)
        self.assertIn('multiple comparisons',self.analysis)

    def test_scqa_smart_are_bounded_editorial_helpers(self):
        self.assertIn('SCQA as an **editorial heuristic**',self.analysis)
        self.assertIn('SMART-like action',self.analysis)
        self.assertIn('Never invent targets or dates',self.analysis)

    def test_paid_report_portability_and_accessibility(self):
        for x in ('self-contained HTML','Do not rely on color alone','do not claim WCAG conformance','CSV/XLSX','preserve numbers, units, source keys/locators'):
            self.assertIn(x,self.premium)

    def test_existing_methodology_stays_governing(self):
        for x in ('CLAIM_GRAMMAR','SAMPLE_AND_FIELDWORK','EXPERT_CORE_RULES'):
            self.assertIn(x,self.analysis)

if __name__=='__main__': unittest.main()
