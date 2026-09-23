#!/usr/bin/env python3
"""Static regression guard for FieldPilot Korea/local-context routing.

This does not prove model behavior. It prevents the specific 2026-09-23 regression
where a Korea adapter existed but the ordinary routing contract could still close a
local-market decision without explicit geography/local competitor/regulatory gates.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = (ROOT / "skills/fieldpilot/SKILL.md").read_text(encoding="utf-8")
DECISION = (ROOT / "skills/fieldpilot/references/modules/DECISION_CONTINUITY.md").read_text(encoding="utf-8")
KOREA = (ROOT / "skills/fieldpilot/references/modules/KOREA_LOCAL_DISTRIBUTION.md").read_text(encoding="utf-8")
CHANNEL = (ROOT / "skills/fieldpilot/references/modules/FREE_FIRST_AND_CHANNEL_ROUTING.md").read_text(encoding="utf-8")

required = {
    "skill_geography_invariant": (SKILL, "Geography can change the answer."),
    "skill_unknown_state": (SKILL, "GEOGRAPHY_UNKNOWN"),
    "decision_local_gate": (DECISION, "GEOGRAPHY_AND_LOCAL_CONTEXT_GATE"),
    "decision_local_direct": (DECISION, "LOCAL_DIRECT_CATEGORY"),
    "decision_local_regulatory": (DECISION, "LOCAL_REGULATORY_CONSTRAINT"),
    "decision_no_language_inference": (DECISION, "Do **not** infer Korea solely from Korean language"),
    "korea_local_competitor_contract": (KOREA, "KOREA_LOCAL_DIRECT_COMPETITORS"),
    "korea_regulatory_applicability": (KOREA, "KOREA_REGULATORY_APPLICABILITY"),
    "korea_privacy_authority": (KOREA, "개인정보보호위원회"),
    "korea_law_authority": (KOREA, "law.go.kr"),
    "korea_naver_official": (KOREA, "https://datalab.naver.com/"),
    "korea_kakao_official": (KOREA, "https://business.kakao.com/guide.html"),
    "korea_offline_no_data_boundary": (KOREA, "stores no personal data and has no internet permission"),
    "channel_geography_gate": (CHANNEL, "DECISION_CONTINUITY.md"),
    "channel_no_language_inference": (CHANNEL, "do not infer Korea from Korean-language input alone"),
}

missing = [name for name, (text, needle) in required.items() if needle not in text]
if missing:
    raise SystemExit("FAIL missing Korea/local-routing contract markers: " + ", ".join(missing))

# Negative-path guards: localization must remain conditional, not a Korean default.
negative_requirements = [
    "Korean-language input alone is **not** evidence that Korea is the target market.",
    "Do not create compliance burden merely because the product is Korean",
    "A foreign competitor's listed USD price is an alternative-price clue, not Korean WTP.",
]
for needle in negative_requirements:
    if needle not in KOREA:
        raise SystemExit("FAIL missing anti-overlocalization guard: " + needle)

print("PASS fieldpilot Korea/local-context routing static contract")
