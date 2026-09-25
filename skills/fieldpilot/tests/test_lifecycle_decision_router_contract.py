from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LifecycleDecisionRouterContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.router = (ROOT / "references/modules/LIFECYCLE_DECISION_ROUTER.md").read_text(encoding="utf-8")
        cls.demand = (ROOT / "references/modules/DEMAND_DISTRIBUTION_DIAGNOSTICS.md").read_text(encoding="utf-8")
        cls.channels = (ROOT / "references/modules/FREE_FIRST_AND_CHANNEL_ROUTING.md").read_text(encoding="utf-8")

    def test_runtime_routes_through_lifecycle_router(self):
        self.assertIn('version: "1.9.9-rc04"', self.skill)
        self.assertIn("LIFECYCLE_DECISION_ROUTER.md", self.skill)
        for marker in [
            "IDEA",
            "BUILDING_OR_MVP",
            "PRE_LAUNCH_OR_PRE_SELL",
            "LAUNCHED_NO_RESPONSE",
            "LAUNCHED_WITH_INTEREST_NO_PAYMENT",
            "MONETIZING",
            "RETURNING_EVIDENCE",
        ]:
            self.assertIn(marker, self.router)

    def test_post_launch_does_not_collapse_to_one_cause(self):
        for marker in [
            "PRODUCT_READINESS_AND_SIGNAL_INTEGRITY.md",
            "DEMAND_DISTRIBUTION_DIAGNOSTICS.md",
            "NO_IMPRESSIONS",
            "CLICKS_NO_SIGNUPS",
            "SIGNUPS_NO_ACTIVATION",
            "ACTIVATION_NO_RETENTION",
            "PAID_AD_POOR_RESPONSE",
        ]:
            self.assertIn(marker, self.router)
        self.assertIn("A funnel symptom is not a single-cause diagnosis", self.demand)

    def test_interest_without_payment_has_payment_diagnostic(self):
        for marker in [
            "PAYMENT_PATH_HEALTH",
            "RETENTION_NO_PAYMENT",
            "PAYMENT_OR_BILLING_FAILURE",
            "USER_VS_PAYER",
            "MONEY_SHAPE",
            "FIRST_PAID_PROOF",
        ]:
            self.assertIn(marker, self.router)

    def test_channel_advice_is_product_specific_and_measured(self):
        for marker in [
            "RECOMMENDED_FIRST_CHANNEL",
            "WHY_THIS_CHANNEL_FITS_THIS_PRODUCT_AND_CUSTOMER",
            "EXACT_FIRST_TEST",
            "WHAT_TO_MEASURE",
            "ONE_FALLBACK_CHANNEL",
        ]:
            self.assertIn(marker, self.router)
        self.assertIn("There is no universal channel ranking", self.channels)
        self.assertIn("Do not invent a universal count of posts", self.channels)

    def test_niche_and_customer_claims_are_bounded(self):
        self.assertIn("candidate customer", self.router.lower())
        self.assertIn("COMPETITOR_FEATURE_NOT_FOUND", self.router)
        self.assertIn("CONFIRMED_GAP", self.router)
        self.assertIn("UNKNOWN_GAP", self.router)
        self.assertIn("대박 / 망함 / 가망 없음", self.router)

    def test_router_keeps_one_next_action(self):
        self.assertIn("ONE_NEXT_ACTION", self.router)
        self.assertIn("one concrete next action", self.router)


if __name__ == "__main__":
    unittest.main()
