from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

class KoreaLocalParityContract(unittest.TestCase):
    def test_kernel_routes_material_geography(self):
        s = read("SKILL.md")
        self.assertIn("Geography changes the evidence set", s)
        self.assertIn("KOREA_LOCAL_DISTRIBUTION.md", s)
        self.assertIn("REGULATORY_CONTEXT_CHECK.md", s)
        self.assertIn("Never infer the target market from the user's language", s)

    def test_korea_module_has_four_local_slots(self):
        s = read("references/modules/KOREA_LOCAL_DISTRIBUTION.md")
        for token in [
            "LOCAL_DIRECT_COMPETITORS",
            "LOCAL_INDIRECT_AND_MANUAL_ALTERNATIVES",
            "LOCAL_REGULATORY_CONSTRAINTS",
            "LOCAL_DISTRIBUTION_ACCESS",
        ]:
            self.assertIn(token, s)
        self.assertIn("SEARCHED_NOT_FOUND / COVERAGE_LIMITED", s)
        self.assertIn("Do **not** assume Korea merely because the user writes Korean", s)

    def test_korea_module_points_to_current_official_sources(self):
        s = read("references/modules/KOREA_LOCAL_DISTRIBUTION.md")
        for host in ["law.go.kr", "pipc.go.kr", "datalab.naver.com", "talksafety.kakao.com"]:
            self.assertIn(host, s)

    def test_competitor_method_requires_local_parity(self):
        s = read("references/methods/secondary-and-competitors.md")
        self.assertIn("Local-market parity guard", s)
        self.assertIn("local-language job/category aliases", s)
        self.assertIn("local direct providers/products", s)
        self.assertIn("local indirect/manual/offline substitutes", s)
        self.assertIn("Do not infer Korea from the user's language or current location alone", s)

    def test_regulatory_module_has_bounded_korea_path(self):
        s = read("references/modules/REGULATORY_CONTEXT_CHECK.md")
        self.assertIn("Jurisdiction adapter — Korea", s)
        self.assertIn("law.go.kr", s)
        self.assertIn("pipc.go.kr", s)
        self.assertIn("NO_PERSONAL_DATA_STORED", s)
        self.assertIn("routing checklist, not a conclusion", s)
        self.assertIn("MATERIAL_BUT_NOT_VERIFIABLE_NOW", s)

    def test_channel_router_treats_geography_as_multi_dimension(self):
        s = read("references/modules/FREE_FIRST_AND_CHANNEL_ROUTING.md")
        self.assertIn("it can change the alternative set", s)
        self.assertIn("load `KOREA_LOCAL_DISTRIBUTION.md`", s)
        self.assertIn("load `REGULATORY_CONTEXT_CHECK.md` when regulation is material", s)
        self.assertIn("Do not infer the target geography from the user's language", s)

    def test_existing_claim_ceiling_is_preserved(self):
        s = read("SKILL.md")
        for token in [
            "UNKNOWN is valid",
            "Counterevidence stays visible",
            "Competitor recall safeguard",
            "Gap safeguard",
            "Commercial claim ceiling",
            "AI-first / no homework",
            "Product-state honesty",
        ]:
            self.assertIn(token, s)

if __name__ == "__main__":
    unittest.main()
