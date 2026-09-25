"""Code-based graders for the FieldPilot prompt-robustness suite.

Deterministic heuristics only. They catch the interaction failures that matter most and that can be
detected without judgment (blocking first turns, question counts, homework requests, mode menus,
internal-token leaks, unconditioned market assumptions). Coverage-floor depth is scored with the
LLM rubric in rubric.md; code graders never claim to measure research quality.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict

MANIFEST_DELIM = "=====HARNESS_MANIFEST====="

_SENT_SPLIT = re.compile(r"(?<=[\.\?\!？。])\s+|\n+")
_Q_END = re.compile(r"[\?？]\s*[\)\]”\"'»\*_]*\s*$")
_HEADING = re.compile(r"^\s*#{1,6}\s")  # markdown section titles are not asks (bold questions are judged below)
_BOLD_ONLY = re.compile(r"^\s*(\*\*[^*]+\*\*|__[^_]+__)\s*$")
_TABLE_OR_QUOTE_LINE = re.compile(r"^\s*(>|\|)|\s\|\s")
_OFFER = re.compile(r"(필요하시면|원하시면|궁금하시면|필요하면|원하면).{0,60}(말씀|알려|요청|정리해\s*드릴)|"
                    r"if you('d| would)? (like|want|need)|say so\b|let me know if you", re.I)
_META_QUESTION = re.compile(r"(question (it|this) answers|the question (is|here)|확인할\s*질문|답하는\s*질문)", re.I)
_QUOTED = re.compile(r"[“\"「『'‘].{0,80}[\?？].{0,5}[”\"」』'’]")

_DIRECTED_KO = [
    "알려", "말씀", "공유", "보내", "붙여", "있나요", "있으신가요", "인가요", "하셨", "하실", "계신", "계세요",
    "원하시", "어느 나라", "어느 시장", "어디서 팔", "어디에 팔", "몇 명", "무엇인가요", "뭔가요", "혹시", "주실",
    "주시겠", "해 주세요", "해주세요", "생각이세요", "예정인가요", "계획인가요", "맞나요", "맞을까요", "인지요",
    "건가요", "셨나요", "나요?", "까요?", "어떤 제품", "무슨 제품", "어떤 서비스", "어떤 앱",
]
_DIRECTED_EN = [" you", "your", "could you", "can you", "do you", "which market", "what market", "where do you",
                "let me know", "tell me", "share", "is it aimed", "are you"]
_REQUEST_NO_QMARK = re.compile(
    r"(알려\s*주세요|말씀해\s*주세요|공유해\s*주세요|보내\s*주세요|붙여\s*(넣어\s*)?주세요|"
    r"알려\s*줘|please share|let me know|please tell me)", re.I)
_IMPLICIT_CONFIRM = re.compile(r"(틀리|다르|다른\s*(점|부분)|잘못).{0,20}(알려|말씀|고쳐)|이해한\s*상황|correct me|"
                               r"if i got (this|that|it) wrong|tell me if (this|that|anything) is (wrong|off)", re.I)
_DRAFT_LINE = re.compile(r"^\s*[>\-*•]?\s*(\*\*)?(초안|예시\s*문구|문구\s*예시|draft|sample message|메시지\s*초안)", re.I)
_LIST_CUE = re.compile(r"(보내\s*주시면|알려\s*주시면|주시면\s*(제가|바로|더|다시)|알려\s*주세요|보내\s*주세요|공유해\s*주세요|"
                       r"please share|send me|let me know|tell me)", re.I)
_LIST_ITEM = re.compile(r"^\s*(\d+[\.\)]|[-*•])\s+\S")
_RHETORICAL_NEXT = re.compile(r"^\s*(아니요|아닙니다|아니에요|아뇨|네[,\.\s]|맞습니다|아직|짧게 말하면|결론부터|No[,\.\s]|Yes[,\.\s]|Not yet|Short answer)", re.I)

_DECISION_MARKERS = [
    "판단", "근거", "대안", "경쟁", "다음", "추천", "보류", "결제", "가격", "원인", "측정", "테스트", "고객",
    "decision", "evidence", "alternative", "competitor", "next step", "next action", "recommend", "hold",
    "price", "cause", "measure", "test", "customer", "payer",
]

_HOMEWORK = [
    r"경쟁(사|자|업체|앱).{0,24}(알려|적어|정리해|리스트|목록).{0,8}(주세요|줘|주시면|주실|오세요)",
    r"(설문|인터뷰|사용자\s*조사).{0,40}(하고\s*(오세요|오시면|알려)|진행하고\s*(오세요|알려)|받아\s*오세요|해\s*오세요)",
    r"시장\s*규모.{0,24}(조사|알아보|찾아).{0,12}(주세요|오세요|보세요|오시면)",
    r"(타깃|타겟|대상\s*고객|목표\s*고객).{0,16}(정의|정해|확정).{0,8}(주세요|주시면|야\s*합니다|야\s*해요)",
    r"(list|tell me|share|send me)\s+(your|the)\s+(main\s+|key\s+)?competitors",
    r"(research|look up|find)\s+(the\s+)?market\s+size\s+(and|then)",
    r"define\s+your\s+target",
    r"(run|conduct|do)\s+(a\s+)?(survey|interviews?)\s+(and|then)\s+(come back|report back|share|send)",
]
_FINDABLE_ASK = [
    r"경쟁(사|자|업체|앱).{0,20}(있나요|아시나요|알고\s*계신|어디인가요|어떤\s*곳|누구인가요)",
    r"(경쟁사|경쟁 앱|대안).{0,12}가격.{0,12}(알려|아시|있나요)",
    r"시장\s*규모.{0,16}(아시나요|알고\s*계신|알려)",
    r"who\s+are\s+your\s+(main\s+)?competitors",
    r"what\s+do\s+(your\s+)?competitors\s+charge",
    r"do\s+you\s+know\s+(the\s+)?market\s+size",
]
_MODE_MENU = [
    r"(간단|요약|빠른).{0,14}(전문|상세|심층|정밀).{0,24}(중|어느|선택|원하|할까요)",
    r"(어떤|어느)\s*(분석|방식|모드|형식|프레임워크).{0,16}(원하|로\s*해|을까요|를\s*원)",
    r"(which|what)\s+(kind\s+of\s+|type\s+of\s+)?(\w+\s+){0,2}(analysis|mode|format|framework|depth)\b.{0,24}\b(would|do)\s+you",
    r"(shall|should)\s+i\s+(proceed|start)\s*\?",
    r"진행할까요\s*[\?？]",
]
_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]{1,}(?:_[A-Z0-9]{2,})+\b")
_KOREA_ENTITIES = [r"한국(?!어)", "국내", r"Korea(?!n[- ]language)", "네이버", "Naver", "카카오", "Kakao", "당근", "토스",
                   "개인정보보호법", "PIPA", "KRW"]
_CONDITIONAL = ["라면", "이라면", "경우", "만약", "if ", "If ", "대상이", "가정", "assum", "unless", "판다면",
                "타깃이", "시장이면", "달라질", "depend", "?", "？", "모르", "미정", "정해지면", "확인되면", "unknown",
                "UNRESOLVED", "not stated", "not specified", "명시되지", "지역", "어느 나라", "which market",
                "않았", "않고", "않습니다", "않아요", "안 봤", "못 봤", "확인하지", "미확인", "정하진", "정하지", "중 어느",
                "/해외", "해외 중", " or ", "not assum", "didn't", "did not", "haven't", "unverified", "예:", "예시",
                " / ", "(예"]
_EXAMPLE_ANSWER = re.compile(r"(예\s*[:)]|예를\s*들어|예시|처럼|e\.g\.|for example|like\s+\")", re.I)
_REPORT_OFFER = re.compile(r"(전체|풀|정식|상세)\s?(시장조사\s?)?(리포트|보고서)|full (market[- ]research )?report", re.I)


def split_manifest(text: str) -> tuple[str, dict]:
    if MANIFEST_DELIM not in text:
        return text.strip(), {}
    reply, _, tail = text.partition(MANIFEST_DELIM)
    manifest = {}
    for line in tail.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            manifest[k.strip()] = v.strip()
    return reply.strip(), manifest


def _sentences(reply: str) -> list[str]:
    # "…in?** It decides" — let a sentence end at ?/./! even when markdown emphasis closes right after it.
    norm = re.sub(r"([\?？\.\!])[\*_]+(?=\s)", r"\1", reply)
    return [s.strip() for s in _SENT_SPLIT.split(norm) if s and s.strip()]


def _line_of(sentence: str, reply: str) -> str:
    idx = max(0, reply.find(sentence))
    start = reply.rfind("\n", 0, idx) + 1
    end = reply.find("\n", idx)
    return reply[start: end if end != -1 else len(reply)]


def _is_draft_or_quote(sentence: str, reply: str) -> bool:
    """True for text meant for third parties (drafts, blockquotes, table templates) or quoted speech."""
    s = sentence.strip()
    if s[:1] in "\"“「『>" or s[-1:] in "\"”」』":
        return True
    line = _line_of(s, reply)
    return bool(_DRAFT_LINE.match(line) or _TABLE_OR_QUOTE_LINE.search(line))


def _request_list_items(reply: str) -> list[str]:
    return _request_lists(reply)[0]


def _request_lists(reply: str) -> tuple[list[str], list[str]]:
    """Top-level numbered/bulleted items that follow a request cue line ('이것만 보내주시면 …' + 1. 2. 3.),
    plus the cue lines themselves (which are not counted separately)."""
    lines = reply.splitlines()
    items, cues = [], []
    half = len(lines) // 2
    for i, line in enumerate(lines):
        if (len(lines) >= 20 and i < half) or not _LIST_CUE.search(line):
            continue
        if _IMPLICIT_CONFIRM.search(line) or _DRAFT_LINE.match(line) or _TABLE_OR_QUOTE_LINE.search(line) or _OFFER.search(line):
            continue
        j = i + 1
        found = []
        while j < len(lines):
            ln = lines[j]
            if not ln.strip() or (ln[:1] in " \t" and found):
                j += 1
                continue
            if _LIST_ITEM.match(ln) and ln[:1] not in " \t":
                found.append(ln.strip())
                j += 1
                continue
            break
        if found:
            items.extend(found)
            cues.append(line.strip())
    return items, cues


def user_directed_questions(reply: str) -> list[str]:
    """Questions or requests addressed to the user (one per ask), excluding rhetorical, quoted,
    draft-for-others and implicit-confirmation lines."""
    items, cues = _request_lists(reply)
    found = [q for q in _sentence_questions(reply) if not any(q in c or c in q for c in cues)]
    for item in items:
        if not any(item in q or q in item for q in found):
            found.append(item)
    return found


def _sentence_questions(reply: str) -> list[str]:
    sents = _sentences(reply)
    n = len(sents)
    total_len = max(1, len(reply))
    out = []
    pos = 0
    for i, s in enumerate(sents):
        pos = reply.find(s, pos)
        is_q = bool(_Q_END.search(s))
        is_request = bool(_REQUEST_NO_QMARK.search(s))
        if not (is_q or is_request):
            continue
        if (_HEADING.match(s) or _HEADING.match(_line_of(s, reply)) or _QUOTED.search(s) or _IMPLICIT_CONFIRM.search(s) or _is_draft_or_quote(s, reply)
                or _OFFER.search(s) or _REPORT_OFFER.search(s) or _META_QUESTION.search(s)):
            continue
        nxt = sents[i + 1] if i + 1 < n else ""
        if is_q and _RHETORICAL_NEXT.match(nxt):
            continue
        low = " " + s.lower()
        directed = any(m in s for m in _DIRECTED_KO) or any(m in low for m in _DIRECTED_EN)
        in_tail = pos >= 0 and pos / total_len >= 0.65
        if is_request or directed or in_tail:
            # A request sentence that directly follows a counted question is part of the same ask.
            if is_request and not is_q and out and out[-1] == (sents[i - 1] if i > 0 else None):
                continue
            out.append(s)
    return out


def end_questions(reply: str) -> list[str]:
    qs = user_directed_questions(reply)
    tail_start = int(len(reply) * 0.65)
    return [q for q in qs if reply.rfind(q) >= tail_start]


def _min_substantive_len(reply: str) -> int:
    """Korean carries more meaning per character than English; scale the length floor."""
    visible = [ch for ch in reply if not ch.isspace()]
    hangul = sum(1 for ch in visible if "\uac00" <= ch <= "\ud7a3")
    return 450 if visible and hangul / len(visible) > 0.3 else 700


def is_substantive(reply: str) -> bool:
    low = reply.lower()
    hits = {m for m in _DECISION_MARKERS if m.lower() in low}
    return len(reply) >= _min_substantive_len(reply) and len(hits) >= 3


_CANT_JUDGE = re.compile(r"(판단할\s*수\s*없|답할\s*수\s*없|말씀드릴\s*수\s*없|판단은\s*보류|몰라서|보이지\s*않아서|안\s*보여|"
                         r"모르는\s*채로|알\s*수\s*없|"
                         r"can't (tell|judge|answer)|cannot (tell|judge|answer)|no way to (tell|judge))", re.I)
_URL = re.compile(r"https?://")


def blocks_before_answer(reply: str) -> bool:
    """A first turn that asks instead of answering: questions present and either no substantive answer,
    or a short reply without any sourced evidence that says it cannot judge yet."""
    if not user_directed_questions(reply):
        return False
    if not is_substantive(reply):
        return True
    return len(reply) < 1500 and not _URL.search(reply) and bool(_CANT_JUDGE.search(reply))


def _find_all(patterns: list[str], reply: str) -> list[str]:
    found = []
    for p in patterns:
        for m in re.finditer(p, reply, re.I):
            found.append(m.group(0))
    return found


def homework_requests(reply: str) -> list[str]:
    return _find_all(_HOMEWORK, reply)


def findable_asks(reply: str) -> list[str]:
    return _find_all(_FINDABLE_ASK, reply)


def mode_menu(reply: str) -> list[str]:
    return _find_all(_MODE_MENU, reply)


def internal_token_leaks(reply: str) -> list[str]:
    """UPPER_SNAKE identifiers printed outside parentheses (parenthetical traceability is allowed)."""
    leaks = []
    for line in reply.splitlines():
        for m in _TOKEN.finditer(line):
            before = line[: m.start()]
            after = line[m.end():]
            inside_paren = before.rfind("(") > before.rfind(")") and (")" in after)
            if not inside_paren:
                leaks.append(m.group(0))
    return leaks


def unconditioned_market_claims(reply: str, entities: list[str] | None = None) -> list[str]:
    """Sentences that treat a specific market (default: Korea) as established without a condition."""
    entities = entities or _KOREA_ENTITIES
    flagged = []
    for s in _sentences(reply):
        if any(re.search(e, s) for e in entities) and not any(c in s for c in _CONDITIONAL):
            flagged.append(s)
    return flagged


def has_example_answer(reply: str) -> bool:
    return bool(_EXAMPLE_ANSWER.search(reply))


def offers_full_report(reply: str) -> bool:
    return bool(_REPORT_OFFER.search(reply))


@dataclass
class CodeGrade:
    chars: int
    substantive: bool
    blocking: bool
    user_questions: int
    end_questions: int
    homework: list = field(default_factory=list)
    findable_asks: list = field(default_factory=list)
    mode_menu: list = field(default_factory=list)
    token_leaks: list = field(default_factory=list)
    unconditioned_market: list = field(default_factory=list)
    example_answer: bool = False
    report_offer: bool = False
    violations: list = field(default_factory=list)

    def to_dict(self):
        return asdict(self)


def grade(reply: str, expectations: dict) -> CodeGrade:
    qs = user_directed_questions(reply)
    g = CodeGrade(
        chars=len(reply),
        substantive=is_substantive(reply),
        blocking=blocks_before_answer(reply),
        user_questions=len(qs),
        end_questions=len(end_questions(reply)),
        homework=homework_requests(reply),
        findable_asks=findable_asks(reply),
        mode_menu=mode_menu(reply),
        token_leaks=internal_token_leaks(reply),
        example_answer=has_example_answer(reply),
        report_offer=offers_full_report(reply),
    )
    geo = expectations.get("geography", "")
    if geo.startswith("UNRESOLVED"):
        g.unconditioned_market = unconditioned_market_claims(reply)
    # Violations are predeclared from cases.json expectations; they are not tuned after runs.
    if g.blocking and not expectations.get("blocking_allowed", False):
        g.violations.append("BLOCKING_FIRST_TURN")
    if g.user_questions > expectations.get("max_user_questions", 2):
        g.violations.append("TOO_MANY_QUESTIONS")
    if g.homework:
        g.violations.append("HOMEWORK_REQUEST")
    if g.findable_asks:
        g.violations.append("ASKS_FINDABLE_FACT")
    if g.mode_menu:
        g.violations.append("MODE_OR_PERMISSION_MENU")
    if g.unconditioned_market:
        g.violations.append("UNCONDITIONED_MARKET_ASSUMPTION")
    if expectations.get("requires_example_answer") and g.blocking and not g.example_answer:
        g.violations.append("ASK_FIRST_WITHOUT_EXAMPLE_ANSWER")
    return g
