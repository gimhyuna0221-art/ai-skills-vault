"""v1.9.9-rc04 prompt-skill independence: static contract + policy lint.

These tests protect the runtime text. They are not behavioral evidence by themselves;
behavioral cases, graders and the runner live in tests/prompt_robustness/.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = "references/modules/PROMPT_SKILL_INDEPENDENCE.md"


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(text):
    """Collapse whitespace so wrapped markdown lines match single-line markers."""
    return " ".join(text.split())


def all_markdown():
    return {str(p.relative_to(ROOT)): p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md")}


BANNED_ASK_PATTERNS = [
    (r"either ask (one|a)", "untie-broken ask-or-continue disjunction"),
    (r"ask the minimum one decision-changing geography question when possible; otherwise", "rc03 geography disjunction"),
    (r"ask the minimum one question or lower the claim ceiling", "rc03 competitor-method disjunction"),
    (r"If stage is unresolved and material, ask the minimum one plain-language question", "rc03 blocking stage question"),
    (r"where the user can resolve geography cheaply, ask —", "rc03 pro-ask geography bias"),
    (r"^Ask, in plain language:", "intake that asks the user to formulate the research brief"),
    (r"in order to avoid asking", "rule that frames asking as the only alternative to inventing"),
    (r"who pays, and whether the job recurs\)\.", "asks for findable/inferable monetization facts"),
    (r"ask only the minimum clarifying questions needed or mark", "untimed product-fact question"),
    (r"ask only the minimum clarifying questions or mark the\s*$", "untimed product-fact question"),
]


def lint_offenders(docs):
    """Return 'file:line reason' for every ask rule that re-creates an rc03 variance source."""
    offenders = []
    for rel, text in docs.items():
        for pattern, why in BANNED_ASK_PATTERNS:
            for m in re.finditer(pattern, text, re.I | re.M):
                line = text[: m.start()].count("\n") + 1
                offenders.append(f"{rel}:{line} {why}")
    return offenders


class PromptSkillIndependenceContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = read("SKILL.md")
        cls.module = read(MODULE)
        cls.router = read("references/modules/LIFECYCLE_DECISION_ROUTER.md")
        cls.continuity = read("references/modules/DECISION_CONTINUITY.md")
        cls.docs = all_markdown()

    # ---- kernel -----------------------------------------------------------------
    def test_version_and_kernel_invariants(self):
        self.assertIn('version: "1.9.9-rc04"', self.skill)
        for marker in [
            "**Prompt-skill independence.**",
            "**Minimum necessary question (QUESTION_GATE).**",
            "**Friendly expert delivery.**",
            "## STEP 0 — UNDERSTAND BEFORE ROUTING (every route, every turn)",
            MODULE,
        ]:
            self.assertIn(marker, self.skill)

    def test_kernel_carries_the_gate_in_low_freedom_form(self):
        for marker in ["FINDABLE", "INFERABLE", "USER_OWNED", "ASK_FIRST", "ASK_AFTER", "<=2 questions"]:
            self.assertIn(marker, self.skill)
        self.assertIn("Geography and stage are never blocking questions on their own", self.skill)
        self.assertIn("the first response is that complete answer, not a question", self.skill)

    def test_description_is_valid_and_carries_everyday_triggers(self):
        desc = re.search(r"^description: (.*)$", self.skill, re.M).group(1)
        self.assertLessEqual(len(desc), 1024, "Agent Skills description limit is 1024 characters")
        for phrase in ["이거 팔릴까?", "아무도 안 써", "망한 거야?", "광고해야 돼?", "뭐부터 해?", "nobody uses my app"]:
            self.assertIn(phrase, desc)

    # ---- module structure ---------------------------------------------------------
    def test_module_has_every_stage_of_the_procedure(self):
        for marker in [
            "## 1. CASE_FRAME — restore the case silently",
            "## 2. COVERAGE_FLOOR — set by the case, not by the words",
            "## 3. QUESTION_GATE — the only rule for asking the user",
            "## 4. FRIENDLY_EXPERT delivery — the default for every user",
            "## 5. EXPERT_TWIN — equivalence check before sending",
            "## 6. Precedence and boundaries",
        ]:
            self.assertIn(marker, self.module)

    def test_normalization_covers_typos_multi_questions_worry_and_xy(self):
        for marker in ["홍보문지인지", "결재", "MPC", "Never correct, grade or comment on the",
                       "Several questions in one message", "Never ask which question to answer first",
                       "Worried or emotional questions", "Solution questions (XY)",
                       "Stated limits are choices, not wording"]:
            self.assertIn(marker, self.module)

    def test_owner_novice_mappings_restore_the_right_decision(self):
        expected = {
            "왜 아무도 안 써?": ["POST_LAUNCH", "ALTERNATIVES", "PRODUCT_STATE"],
            "광고해야 돼?": ["POST_LAUNCH", "ALTERNATIVES", "CHANNEL"],
            "뭐 더 만들어?": ["PRODUCT_STATE", "ALTERNATIVES"],
            "사람들이 살까?": ["ALTERNATIVES", "MONEY"],
            "경쟁사 없어?": ["ALTERNATIVES"],
        }
        rows = [line for line in self.module.splitlines() if line.startswith("| \"")]
        for phrase, floors in expected.items():
            row = next((r for r in rows if phrase in r), None)
            self.assertIsNotNone(row, f"no restoration row for {phrase}")
            for floor in floors:
                self.assertIn(floor, row, f"{phrase} must restore to {floor}")
        self.assertIn("Match meaning, not keywords", self.module)

    def test_coverage_floor_matches_owner_quality_floor(self):
        # Owner list: alternatives, product state, counterevidence, key unknowns, commercial ceiling,
        # build/change/hold, one next action, provenance, post-launch cause separation.
        for marker in ["DIRECT_ANSWER", "CURRENT_JUDGMENT", "EVIDENCE", "COUNTEREVIDENCE",
                       "UNKNOWNS_AND_CEILING", "BUILD_CHANGE_OR_HOLD", "ONE_NEXT_ACTION",
                       "| ALTERNATIVES |", "| PRODUCT_STATE |", "| MONEY |", "| POST_LAUNCH |",
                       "| PAYMENT |", "| CHANNEL |", "| LOCAL |", "| DELTA |", "| NARROW |", "| FULL |"]:
            self.assertIn(marker, self.module)
        self.assertIn("Wording may change the order and emphasis of the answer; it never removes a row", flat(self.module))
        self.assertIn("never by vocabulary", self.module)

    def test_question_gate_caps_timing_and_never_ask_list(self):
        gate = flat(self.module.split("## 3. QUESTION_GATE")[1].split("## 4.")[0])
        for marker in ["ASK_FIRST", "ASK_AFTER", "At most 2 questions", "at most 2 follow-up questions at the very end",
                       "the product/case cannot be identified at all", "referenced but did not include",
                       "explicitly asks to be asked first", "ASK_FIRST ≤ 2 questions, ASK_AFTER ≤ 2 questions",
                       "Never drip-feed", "is not asked again"]:
            self.assertIn(marker, gate)
        never = gate.split("**Never ask**")[1].split("**Geography.**")[0]
        for item in ["analysis, mode, framework, depth, research areas or output format",
                     "permission to start research", "anything FINDABLE",
                     "define the decision, decision owner, deadline, success metric or target customer",
                     "re-summarize files", "interviews, surveys or recruitment as a precondition",
                     "direct-research method before the answer"]:
            self.assertIn(item, never)
        self.assertIn("never turns into a question or homework", gate)

    def test_rc03_blocking_geography_antipattern_is_named_and_forbidden(self):
        self.assertIn("Anti-pattern: the blocking market question", self.module)
        # product text carries no benchmark-run references (blind benchmark hygiene)
        self.assertNotIn("clean run", self.module.lower())
        self.assertIn("Geography alone never blocks the first answer", self.module)
        self.assertIn("do not guess and do not stop", self.skill)
        korea = read("references/modules/KOREA_LOCAL_DISTRIBUTION.md")
        self.assertIn("Geography alone never blocks the first answer", korea)
        self.assertIn("Do **not** infer Korea merely from", korea)  # rc02 protection kept

    # ---- policy lint over the whole skill -------------------------------------------
    def test_policy_lint_no_disjunctive_or_pro_ask_rules_remain(self):
        offenders = lint_offenders(self.docs)
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_policy_lint_detects_the_rc03_patterns(self):
        # Self-test: a lint that cannot fail proves nothing.
        samples = {
            "a.md": "either ask one plain-language question or continue with a bounded global conclusion",
            "b.md": "Ask, in plain language:\n1. What decision will this research change?",
            "c.md": "- where the user can resolve geography cheaply, ask — this is a decision-changing question",
            "d.md": "ask only the minimum questions (for example usage frequency, marginal/API cost, who pays, and whether the job recurs).",
        }
        self.assertEqual(len(lint_offenders(samples)), 4)

    def test_known_ask_sites_defer_to_the_gate(self):
        sites = {
            "SKILL.md": "QUESTION_GATE",
            "references/modules/LIFECYCLE_DECISION_ROUTER.md": "ASK_AFTER",
            "references/modules/DECISION_CONTINUITY.md": "QUESTION_GATE",
            "references/modules/KOREA_LOCAL_DISTRIBUTION.md": "ASK_AFTER",
            "references/modules/REGULATORY_CONTEXT_CHECK.md": "ASK_AFTER",
            "references/methods/secondary-and-competitors.md": "ASK_AFTER",
            "references/modules/MONETIZATION_AND_UNIT_ECONOMICS.md": "QUESTION_GATE",
            "references/core/PROPOSITION_AND_EVIDENCE.md": "QUESTION_GATE",
            "references/modules/MARKET_CASE_COMPARISON_AND_GAP.md": "QUESTION_GATE",
            "references/modules/MARKET_RESEARCH_DELIVERABLES.md": "QUESTION_GATE",
            "references/delivery/CLIENT_DECISION_BRIEF.md": "ASK_AFTER",
            "references/modules/MARKET_PRIOR_AND_BASE_RATES.md": "QUESTION_GATE",
            "references/core/ANALYSIS_AND_REPORTING.md": "QUESTION_GATE",
            "references/core/RUNTIME_CORE.md": "QUESTION_GATE",
            "references/modules/FREE_FIRST_AND_CHANNEL_ROUTING.md": "QUESTION_GATE",
        }
        for rel, marker in sites.items():
            self.assertIn(marker, read(rel), f"{rel} must defer to the question gate")

    def test_route_b_intake_does_not_test_the_user(self):
        prop = read("references/core/PROPOSITION_AND_EVIDENCE.md")
        self.assertIn("Do not ask the user to formulate these research objects", prop)
        core = read("references/core/RUNTIME_CORE.md")
        self.assertIn("결정·결정권자·마감·성공기준을", core)
        self.assertIn("숙제가 아니라 다음 행동 하나", core)
        mrd = read("references/modules/MARKET_RESEARCH_DELIVERABLES.md")
        self.assertIn("never asked before it (QUESTION_GATE)", mrd)

    # ---- routing and delivery -------------------------------------------------------
    def test_route_selection_is_not_vocabulary_driven(self):
        self.assertIn('Vocabulary such as "analysis", "assessment" or "viability" does not by itself select this route', self.skill)
        self.assertIn("plain wording never excludes it", self.skill)
        self.assertIn("one-line offer of this full report", self.skill)
        mrd = read("references/modules/MARKET_RESEARCH_DELIVERABLES.md")
        self.assertIn("research vocabulary alone", mrd)
        self.assertIn("offers this full deliverable in one line", mrd)
        self.assertIn("route by the restored case, not by the literal question", self.router)

    def test_solution_questions_get_a_premise_check(self):
        self.assertIn("Whether before where.", self.router)
        self.assertIn("check the premise", self.continuity)
        self.assertIn("answer it directly and check the premise before recommending the solution", self.skill)

    def test_plain_language_is_the_default_register(self):
        self.assertIn("as the default register of every answer", self.skill)
        self.assertIn("This is the default register of every FieldPilot answer", self.continuity)
        self.assertIn("never the main text", flat(self.module))
        self.assertIn("The opening must stand alone", self.module)
        self.assertIn("Length is not thoroughness", self.module)
        self.assertIn("Easy to read never means thinner underneath", self.skill)
        example = read("references/delivery/SELLABILITY_WORKED_EXAMPLE.md")
        self.assertIn("지금 판단 (CURRENT_DECISION)", example)
        self.assertIn("첫 줄 — 직접 답", example)
        # protective distinctions survive the plain rewrite
        for marker in ["UNKNOWN_GAP", "CONFIRMED_GAP", "WTP UNKNOWN", "OBSERVED_PURCHASE", "NOT_CHECKED"]:
            self.assertIn(marker, example)

    # ---- rc04 Stage-A bounded correction: claim discipline + opening action ---------
    def test_claim_discipline_rules_are_in_module_and_kernel(self):
        self.assertIn("**Claim discipline in delivery.**", self.skill)
        self.assertIn("### 4.1 CLAIM_DISCIPLINE — plain words never add certainty", self.module)
        rules = flat(self.module.split("### 4.1 CLAIM_DISCIPLINE")[1].split("## 5.")[0])
        for marker in [
            # A. product-state inference guard
            "No product-state facts from adjacent facts", "payment model", "remote-update capability",
            "support burden", "legal/regulatory status", "not from \"offline\", \"no personal data\"",
            "Regulatory status stays jurisdiction-specific",
            # B. causal-ranking guard
            "No causal dominance from tiny observational samples", "\"dominant\"",
            "\"almost certainly the main cause\"", "cheapest check that tells them apart",
            # C. external outcome/time guard
            "No external outcome or timing guarantees", "response time", "\"하루면 답이 옵니다\"",
            # D. provenance guard
            "Locator or explicit limit for every material researched claim", "NOT_CHECKED",
            "says it is generic",
        ]:
            self.assertIn(marker, rules)
        kernel = flat(self.skill.split("**Claim discipline in delivery.**")[1].split("## STEP 0")[0])
        for marker in ["adjacent facts", "dominant from a tiny observational sample",
                       "never promise external response time", "locator or an explicit NOT_CHECKED limit"]:
            self.assertIn(marker, kernel)

    def test_opening_hard_check_requires_answer_and_action(self):
        delivery = flat(self.module.split("## 4. FRIENDLY_EXPERT")[1].split("### 4.1")[0])
        self.assertIn("Opening hard check (answerable cases): lines 1–3 contain both (a) the direct answer and (b) one immediate action direction", delivery)
        self.assertIn("A conclusion alone, or a meta/setup line", delivery)
        self.assertIn("Lines 1–3 carry both the direct answer and one immediate action", self.skill)
        twin = flat(self.module.split("## 5. EXPERT_TWIN")[1].split("## 6.")[0])
        self.assertIn("one action direction within the first three lines", twin)
        self.assertIn("break §4.1", twin)

    # ---- regression: rc03/core strengths stay in the runtime text -------------------
    def test_rc03_core_strengths_preserved(self):
        anchors = {
            "truth before fluency": ("SKILL.md", "**Truth before fluency.**"),
            "UNKNOWN is valid": ("SKILL.md", "**UNKNOWN is valid.**"),
            "counterevidence": ("SKILL.md", "**Counterevidence stays visible.**"),
            "competitor recall safeguard": ("SKILL.md", "**Competitor recall safeguard.**"),
            "gap safeguard": ("SKILL.md", "`COMPETITOR_FEATURE_NOT_FOUND` never proves `CONFIRMED_GAP`"),
            "commercial/WTP ceiling": ("SKILL.md", "**Commercial claim ceiling.**"),
            "AI-first / no homework": ("SKILL.md", "**AI-first / no homework.**"),
            "product-state honesty": ("SKILL.md", "**Product-state honesty.**"),
            "coverage honesty": ("SKILL.md", "**Coverage honesty.**"),
            "geography no-guessing": ("SKILL.md", "Never infer the target market from the user's language"),
            "full professional route": ("SKILL.md", "## ROUTE B — FULL / PROFESSIONAL MARKET RESEARCH"),
            "returning evidence continuity": ("SKILL.md", "`WHAT_CHANGED / WHAT_STAYED_STABLE / UPDATED_DECISION`"),
            "Korea-local coverage": ("references/modules/KOREA_LOCAL_DISTRIBUTION.md", "LOCAL_DIRECT_SEARCHED_NOT_FOUND"),
            "demand-vs-distribution": ("references/modules/DEMAND_DISTRIBUTION_DIAGNOSTICS.md", "A funnel symptom is not a single-cause diagnosis"),
            "signal integrity": ("references/modules/PRODUCT_READINESS_AND_SIGNAL_INTEGRITY.md", "MARKET SIGNALS REQUIRE DELIVERY INTEGRITY"),
            "first-paid-proof discipline": ("references/modules/DECISION_CONTINUITY.md", "PASS requires actual paid behavior"),
            "role boundary": ("SKILL.md", "FieldPilot이 직접 코드를 수정하지 않는다"),
        }
        for name, (rel, marker) in anchors.items():
            self.assertIn(marker, read(rel), f"rc03 strength weakened or moved: {name}")

    def test_module_never_overrides_protections(self):
        precedence = flat(self.module.split("## 6. Precedence and boundaries")[1])
        for marker in ["truth before fluency", "UNKNOWN", "provenance", "counterevidence",
                       "commercial/WTP claim ceilings", "geography no-guessing rule",
                       "approval gates for external execution", "explicit user limits",
                       "the full professional route", "role boundary"]:
            self.assertIn(marker, precedence)

    def test_every_referenced_runtime_file_exists(self):
        missing = []
        for rel, text in self.docs.items():
            for ref in re.findall(r"`(references/[A-Za-z0-9_./-]+\.md)`", text):
                if not (ROOT / ref).exists():
                    missing.append(f"{rel} -> {ref}")
        self.assertEqual(missing, [], "\n".join(missing))


if __name__ == "__main__":
    unittest.main()
