# v1.6 — Korea Local Distribution Context

## Purpose

한국 시장을 대상으로 하는 빌더에게 글로벌 커뮤니티 관행을 그대로 이식하지 않기 위한 geography adapter다.
이 모듈은 특정 채널의 우월성을 선언하지 않는다. **타깃의 실제 존재 + 접근 가능성 + 현재 규칙 + 제품 적합성**을 확인한 뒤 후보 경로를 좁힌다.

## Governing rules

1. 한국 타깃이면 `한국어 검색행동 / 국내 커뮤니티 / 직업·취미 집단 / 앱·게임 플랫폼 / 오프라인 접근`을 글로벌 채널과 함께 비교한다.
2. 특정 커뮤니티 이름은 현재 타깃이 실제로 존재하고, 링크·셀프홍보·조사 모집이 규칙상 가능한지 확인하기 전에는 실행 채널로 확정하지 않는다.
3. 개발자/AI 커뮤니티 반응은 타깃 고객 반응이 아니다. 타깃이 개발자일 때만 시장증거로 직접 승격할 수 있다.
4. 한국 커뮤니티는 익명성, 팬덤, 직업집단, 지역성 등 선택구조가 강할 수 있으므로 broader-market generalization을 자동으로 하지 않는다.
5. 커뮤니티 바이럴이나 실시간 인기글 유입은 `SPIKE_TRAFFIC`으로 표시하고, activation/return/payment를 별도로 본다.
6. 플랫폼 내부 유통(App Store/Google Play/Steam/미니앱 등)은 외부 SNS와 별도 acquisition system으로 취급하며, 플랫폼 설치기반·피처링·추천 같은 advantage를 사용자 제품의 내재적 수요와 분리한다.

## Candidate Korean routes — conditional, not ranked

### Naver Search / DataLab / Ads Keyword Tool / Blog / Cafe / Knowledge ecosystem
Plausible when the target expresses the problem in Korean search or gathers in topic-specific communities.
For Korean search-intent priors, prefer current first-party NAVER signals where accessible: DataLab for relative trend/demographic/device patterns and NAVER Ads Keyword Tool for monthly search/click/CTR/competition context. Keep their metric definitions separate; neither is purchase-demand proof.
Before recommending a named Cafe/community, verify current membership relevance and posting/self-promotion rules.
Search impressions, qualified clicks, downstream action and query language are stronger than likes/comments alone.

### Kakao communities / Open Chat / local messaging networks
Plausible when the target already coordinates in Kakao-based groups or local/professional communities.
Access can be relationship- or invite-dependent. Lack of access is an access constraint, not demand failure.

### Disquiet and Korean product-launch communities
Plausible for Korean makers, tech early adopters, side-project users and product discovery **only if those users overlap the target**.
Launch reactions are selected early-adopter evidence, not broad-market demand or retention.

### Blind / professional communities
Plausible only when the professional audience, company context or job role matches the target and current community rules allow the intended participation.
Anonymous professional feedback may be useful for language/problem discovery; do not infer buyer authority or willingness to pay automatically.

### DCInside / Ruliweb / Inven / hobby forums
Potentially useful for highly concentrated game, hobby, AI or enthusiast audiences. Community norms and self-promotion tolerance vary materially.
Treat virality, recommendations and replies as community-specific evidence. Developer-community feedback is not player/customer evidence unless the audience overlaps.

### Apps-in-Toss / platform-distribution ecosystems
For compatible products, an installed platform audience can materially change discovery friction. Treat this as a **platform distribution advantage**, not evidence that the same product would acquire users independently elsewhere.
Current eligibility, policy, SDK and monetization mechanics must be verified from first-party documentation before execution.

### Local offline / direct outreach
For local B2B, clinics, gyms, cafes, shops, academies and other geographically concentrated users, direct outreach or observation may dominate online search volume as an access route.
Do not invent universal visit times, contact counts or scripts. Generate an access plan and artifact from the specific business context.

## Korea route contract

When Korean geography materially changes routing, store:

```text
KOREA_TARGET_SEGMENT
TARGET_PRESENCE_EVIDENCE
CANDIDATE_LOCAL_ROUTE
CURRENT_ACCESS_RULES_VERIFIED? YES/NO/UNKNOWN
SELF_PROMOTION_OR_RESEARCH_RULES
SELECTION_BIAS
EXPECTED_SIGNAL
DOWNSTREAM_BEHAVIOR
GLOBAL_ALTERNATIVE
LOCAL_ALTERNATIVE
FAILURE_INTERPRETATION
```

A response should prefer a Korean route only because the evidence and user constraints make it more informative or feasible — not because it is Korean by default.

## Korea local market coverage — v1.9.9-rc02 bounded extension

This section closes a failure mode observed in an internal blind benchmark: a globally disciplined report can still miss decision-relevant Korean competitors, regulation, or access channels when the target geography is Korea.

### Activation and non-assumption rule

Activate this local coverage only when Korea is established by the user, product/store/contract scope, verified target-market evidence, or another explicit project fact.

Do **not** infer Korea merely from:
- Korean-language conversation;
- the owner's current physical/device/account location;
- KRW appearing in an unrelated context;
- the model's prior knowledge of the owner.

If geography is unknown and can change the recommendation, return `GEOGRAPHY_UNRESOLVED` and either ask one decision-changing geography question or continue with a bounded global conclusion plus the named local dependency.

### LOCAL_COMPETITOR_COVERAGE

For a Korea-targeted commercialization or broad viability decision, the Alternative Map is incomplete until the search has proportionately checked the decision-relevant local classes below:

```text
KOREA_LOCAL_DIRECT
  same job/category in Korea or explicitly serving Korean buyers

KOREA_LOCAL_ADJACENT_OR_BUNDLED
  broader Korean incumbent/SaaS/platform/service that absorbs the job

KOREA_LOCAL_MANUAL_OR_INTERNAL
  spreadsheet, calculator, paper, messaging, staff procedure, agency/service,
  or other non-product workaround actually plausible in the Korean context

KOREA_LOCAL_DO_NOTHING
  tolerate the current friction / keep the incumbent process

KOREA_LOCAL_PRICE_AND_TERMS
  current Korean pricing, contract, billing, refund, procurement or platform
  terms only when they change the decision
```

Search by the buyer's Korean job/problem language and Korean category aliases, not by translated product names alone. Prefer current first-party product/store/company material for offer and pricing facts; use local community or marketplace material as discovery/experience evidence with the existing source-class caveats.

If no local direct competitor is found, record:
`LOCAL_DIRECT_SEARCHED_NOT_FOUND`
with the query families/source classes actually checked. It is not proof that none exists and must not be upgraded to `CONFIRMED_GAP`.

### LOCAL_CHANNEL_COVERAGE

Naver Search/DataLab/Ads, Naver Cafe, Kakao Open Chat/local messaging, Disquiet, Blind, hobby/professional communities, app stores and direct/offline outreach are candidate access surfaces — not a mandatory channel list.

For a named channel:
- verify the target audience is actually there;
- verify current participation/self-promotion/research rules when material;
- separate access from demand;
- treat comments/likes/replies as selected-audience evidence, not payment or prevalence;
- prefer one evidence-backed first route plus one fallback rather than a generic channel menu.

### LOCALIZATION_DELTA

When this module materially changes an ordinary decision, preserve a compact delta:

```text
GEOGRAPHY: KOREA
LOCAL_DIRECT_AND_ADJACENT
LOCAL_MANUAL_AND_NO_ACTION
LOCAL_REGULATORY_DEPENDENCY
LOCAL_BUYER_ACCESS
LOCAL_PRICE_OR_TERMS_IF_MATERIAL
WHAT_CHANGED_VS_GLOBAL_VIEW
WHAT_REMAINS_UNKNOWN
```

The purpose is not to make every Korean report longer. Load and render only the local facts that can change the active decision.

