"""Unit tests for the prompt-robustness code graders (synthetic fixtures only).

Fixtures are invented text. No benchmark output (e.g. the rc03 paid-competitor runs) is stored in
this repository.
"""
from pathlib import Path
import json
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "prompt_robustness"))

import graders  # noqa: E402

LONG_ANSWER_KO = (
    "아직 '망했다'고 볼 근거는 없어요. 지금은 광고보다 먼저 확인할 게 있어요.\n"
    "제가 이해한 상황: 3주 전 공개, 방문 40명, 가입 3명, 결제 0명인 견적서 웹앱으로 봤어요.\n"
    "현재 판단: 결제 0명은 수요가 없다는 뜻이 아니라, 아직 판단할 만큼 노출되지 않았다는 신호에 가까워요. "
    "근거: 비슷한 도구와 대안(스프레드시트 견적 템플릿, 일반 AI 채팅, 기존 인보이스 도구)이 이미 있어서 "
    "왜 바꿀지를 첫 화면에서 보여줘야 해요. 반대 근거: 가입 3명 중 실제 견적서를 만든 사람이 없다면 제품 문제일 수 있어요. "
    "아직 모르는 것: 가입자가 견적서를 끝까지 만들었는지, 결제 화면까지 갔는지. "
    "만들기·바꾸기·보류: 기능 추가는 보류하고 첫 화면 메시지를 바꿔요. "
    "지금 할 일 하나: 가입 3명에게 견적서 완성 여부를 로그로 확인하고, 완성 이벤트를 측정하는 테스트를 하세요. "
    "가격은 월 9달러 가설로 두되 실제 결제 전까지는 지불 의사를 모르는 상태예요.\n"
    "마지막으로 하나만: 주로 어느 나라 프리랜서를 대상으로 하시나요? 알려주시면 현지 경쟁 도구와 가격을 다시 확인할게요."
)


class GraderUnitTests(unittest.TestCase):
    def test_blocking_first_turn_is_detected(self):
        reply = "Which market is StudioTally being piloted in? Competitors and pricing differ a lot by region."
        g = graders.grade(reply, {"blocking_allowed": False, "max_user_questions": 2})
        self.assertTrue(g.blocking)
        self.assertIn("BLOCKING_FIRST_TURN", g.violations)

    def test_substantive_answer_with_one_end_question_passes(self):
        g = graders.grade(LONG_ANSWER_KO, {"blocking_allowed": False, "max_user_questions": 2,
                                           "geography": "UNRESOLVED_NO_GUESS"})
        self.assertTrue(g.substantive)
        self.assertFalse(g.blocking)
        self.assertEqual(g.user_questions, 1)
        self.assertEqual(g.end_questions, 1)
        self.assertEqual(g.violations, [])

    def test_rhetorical_and_quoted_questions_are_not_user_questions(self):
        reply = ("“광고해야 돼?”에 대한 답부터 드릴게요. 망한 걸까요? 아니요, 아직 판단할 근거가 없습니다. "
                 "지금은 원인을 나눠 보는 게 먼저예요.")
        self.assertEqual(graders.user_directed_questions(reply), [])

    def test_homework_requests_are_detected(self):
        for reply in ["먼저 경쟁사 5개를 알려주세요.", "고객 인터뷰 5명 하고 오세요.",
                      "시장 규모를 조사해서 알려주세요.", "타깃 고객을 먼저 정의해 주세요.",
                      "Please list your main competitors first."]:
            self.assertTrue(graders.homework_requests(reply), reply)

    def test_mode_menu_and_permission_questions_are_detected(self):
        for reply in ["간단 분석과 전문 분석 중 어떤 걸 원하세요?", "어떤 분석 방식을 원하시나요?",
                      "Which analysis mode would you like?", "조사를 진행할까요?"]:
            self.assertTrue(graders.mode_menu(reply), reply)

    def test_findable_asks_are_detected(self):
        self.assertTrue(graders.findable_asks("경쟁사가 어디인지 알고 계신가요?"))
        self.assertTrue(graders.findable_asks("Who are your main competitors?"))

    def test_internal_tokens_outside_parentheses_are_leaks(self):
        self.assertEqual(graders.internal_token_leaks("현재 판단: UNKNOWN_GAP 입니다"), ["UNKNOWN_GAP"])
        self.assertEqual(graders.internal_token_leaks("아직 모르는 빈틈이에요 (UNKNOWN_GAP)."), [])
        self.assertEqual(graders.internal_token_leaks("`GEOGRAPHY_UNRESOLVED` 상태"), ["GEOGRAPHY_UNRESOLVED"])
        self.assertEqual(graders.internal_token_leaks("USD 9/month, MVP, WTP"), [])

    def test_unconditioned_market_assumption_is_flagged(self):
        self.assertTrue(graders.unconditioned_market_claims("국내 댄스학원은 네이버 카페에서 홍보하세요."))
        self.assertFalse(graders.unconditioned_market_claims("한국에서 판다면 네이버 카페 규칙을 먼저 확인하세요."))
        self.assertFalse(graders.unconditioned_market_claims("지역이 정해지지 않아 국내 경쟁 도구는 아직 확인하지 않았어요."))

    def test_ask_first_hard_case_requires_an_example_answer(self):
        good = "어떤 제품인지 한 줄만 알려주세요. 예: '헬스장 프론트용 회원권 계산 앱'. 링크나 파일도 좋아요."
        bad = "어떤 제품인가요? 타깃은 누구인가요? 가격은요? 지역은요?"
        exp = {"blocking_allowed": True, "max_user_questions": 2, "requires_example_answer": True}
        g_good = graders.grade(good, exp)
        g_bad = graders.grade(bad, exp)
        self.assertTrue(g_good.blocking)
        self.assertEqual(g_good.violations, [])
        self.assertIn("TOO_MANY_QUESTIONS", g_bad.violations)
        self.assertIn("ASK_FIRST_WITHOUT_EXAMPLE_ANSWER", g_bad.violations)

    def test_request_lists_count_each_item_as_an_ask(self):
        reply = ("분석 본문입니다.\n**이것만 보내주시면 제가 더 좁혀드릴게요**\n"
                 "1. 사이트 주소: 첫 화면을 봐요.\n2. 올린 글 링크: 반응을 봐요.\n3. 어느 나라 고객인지: 경쟁이 달라져요.\n")
        self.assertEqual(len(graders.user_directed_questions(reply)), 3)

    def test_implicit_confirmation_and_drafts_are_not_asks(self):
        reply = ("**제가 이해한 상황** (틀리면 알려주세요)\n견적서 웹앱으로 봤어요.\n"
                 "초안: \"[직군] 분들, 써보시고 막히는 곳 하나만 알려주세요.\"\n"
                 "끝으로 하나만: 어느 나라 고객을 대상으로 하시나요?")
        qs = graders.user_directed_questions(reply)
        self.assertEqual(len(qs), 1, qs)
        self.assertIn("어느 나라", qs[0])

    def test_blockquote_drafts_tables_offers_and_meta_questions_are_not_asks(self):
        reply = ("- **Message to copy**:\n  > Hi [name], how do you track passes today? Tell me your rules.\n"
                 "- **Record in a sheet:** studio | replied? | paid? | refunded?\n"
                 "The question it answers: will one real customer pay anything?\n"
                 "If you'd like a full report with a source table, say so.\n"
                 "원하시면 출처까지 붙인 전체 보고서로 정리해 드릴게요.\n"
                 "## 망한 걸까요?\n"
                 "1. **Which country are the studios in?** It decides local competitors.\n")
        qs = graders.user_directed_questions(reply)
        self.assertEqual(len(qs), 1, qs)
        self.assertIn("Which country", qs[0])

    def test_bold_directed_question_counts(self):
        reply = "지금은 무엇인지 몰라요.\n\n**무엇을 파실 건가요?**\n\n예: '헬스장 회원권 계산 앱'"
        self.assertEqual(len(graders.user_directed_questions(reply)), 1)
        self.assertTrue(graders.blocks_before_answer(reply))

    def test_language_mentions_are_not_market_claims(self):
        self.assertFalse(graders.unconditioned_market_claims("영문·한국어 공식 페이지 모두 US$로 표시돼요."))
        self.assertFalse(graders.unconditioned_market_claims("(예: 한국 / 영어권 / 아직 안 정함) 답해 주시면 확정할게요."))

    def test_explicitly_unassumed_market_is_not_flagged(self):
        self.assertFalse(graders.unconditioned_market_claims("한국어로 말씀하셨어도 그걸로 정하진 않았어요."))
        self.assertFalse(graders.unconditioned_market_claims("한국 쪽 경쟁·가격 감각은 안 봤고, 달라질 수 있어요."))
        self.assertTrue(graders.unconditioned_market_claims("한국 댄스학원은 카카오 오픈채팅으로 모집하세요."))

    def test_manifest_is_split_from_the_reply(self):
        reply, manifest = graders.split_manifest("답변 본문\n=====HARNESS_MANIFEST=====\nFILES_READ: SKILL.md\nWEB_SEARCHES: 3")
        self.assertEqual(reply, "답변 본문")
        self.assertEqual(manifest["WEB_SEARCHES"], "3")

    def test_cases_file_is_well_formed(self):
        data = json.loads((HERE / "prompt_robustness" / "cases.json").read_text(encoding="utf-8"))
        families = {c["family"] for c in data["cases"]}
        self.assertEqual(families, {"F1_SAME_INTENT_DIFFERENT_LANGUAGE", "F2_MISSING_CONTEXT", "F3_USER_BURDEN",
                                    "F4_FRIENDLY_DELIVERY", "F5_HARD_CASE"})
        f1 = next(c for c in data["cases"] if c["id"] == "F1_QUOTE")
        self.assertGreaterEqual(len(f1["variants"]), 5)
        for case in data["cases"]:
            self.assertIn("expectations", case)
            self.assertNotIn("LockerDesk", json.dumps(case, ensure_ascii=False))
            for v in case["variants"]:
                self.assertTrue(v["prompt"].strip())


if __name__ == "__main__":
    unittest.main()
