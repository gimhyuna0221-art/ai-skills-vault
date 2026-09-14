# v1.6 — Execution Source Registry

This registry complements the frozen v1.5 methodology source registry. It is for volatile platform/data-access facts and v1.6 market-intelligence execution examples. Runtime should re-check volatile platform facts when material.

Retrieval baseline: 2026-08-27. URLs are locators, not frozen truth. Current-platform rows must be re-verified when material.

| ID | Class | Source | Use | Scope / limitation |
|---|---|---|---|---|
| `V16-S01` | CURRENT_PLATFORM | Apple Developer — Peer group benchmarks | App Store benchmark definitions, peer grouping, privacy | User's App Store Connect context; not competitor ground truth |
| `V16-S02` | CURRENT_PLATFORM | Apple Developer — App Store Connect Analytics: Acquisition | acquisition, engagement, monetization, source breakdown | first-party user app data |
| `V16-S03` | CURRENT_PLATFORM | Google Play Console Help — Peer benchmark groups | contextual peer metrics | Google-curated/custom peer groups; private competitor metrics protected |
| `V16-S04` | CURRENT_PLATFORM | Google Play Console Help — Store listing performance | current listing-intent metric definitions | definitions changed in 2026; re-check before numeric comparison |
| `V16-S05` | CURRENT_PLATFORM | Google Ads Help — Duration of learning period | Smart Bidding learning factors and calibration | varies by conversions, cycle, strategy |
| `V16-S06` | CURRENT_PLATFORM | Google Ads Help — Bidding / conversion measurement | Smart Bidding current guidance | not a universal business success threshold |
| `V16-S07` | CURRENT_PLATFORM | TikTok Ads Manager — Learning Phase | current generic learning-phase behavior | context-specific; do not generalize numeric guidance |
| `V16-S08` | CURRENT_PLATFORM | TikTok Ads Manager — Troubleshooting Auction Ad Delivery | 7-day/50-conversion troubleshooting guidance | learning guidance for auction ads, not product-demand rule |
| `V16-S09` | CURRENT_PLATFORM | TikTok Ads Manager — Search Ads Optimization | Search Ads calibration guidance | Search Ads-specific |
| `V16-S10` | CURRENT_PLATFORM | Steamworks — Visibility on Steam | official visibility factors, traffic/conversion/wishlist caveats | Steam-specific and subject to future changes |
| `V16-S11` | CURRENT_PLATFORM | Steamworks — Sales and Marketing / Wishlists | store-native tools and wishlist notifications | wishlist roles are conditional |
| `V16-S12` | CURRENT_PLATFORM | Google Trends Help — FAQ about Trends data | normalized relative search-interest definition; re-verified 2026-08-31 — anonymized/categorized/aggregated **sample** of searches, normalized by total searches for the chosen geography/time range then rescaled 0-100, deliberate statistical noise most visible on low-volume queries, irregular/duplicate activity filtered, time zone differs between ranges of <=7 days and >=30 days | not absolute search volume, not customer counts, not purchase demand; provider states it is not a scientific poll and should not be used for definitive conclusions; a single normalized spike is not a durable trend |
| `V16-S13` | CURRENT_PLATFORM | Meta Ads Library | documented current ad/creative presence | does not establish profitability or causality |
| `V16-S14` | VENDOR_DATA | RevenueCat annual subscription benchmark reports | conditional subscription benchmark distributions | selected customer/app population, not all apps |
| `V16-S15` | VENDOR_DATA | AppsFlyer performance/monetization reports | observed attribution/monetization patterns | AppsFlyer customer/instrumented population |
| `V16-S16` | VENDOR_ESTIMATE | Similarweb methodology / estimates | web traffic/channel estimation | especially weak for small sites; visits != users/customers |
| `V16-S17` | VENDOR_ESTIMATE | Sensor Tower market intelligence | app/game competitive estimates | estimated, plan/access dependent |
| `V16-S18` | VENDOR_ESTIMATE | VG Insights / analogous Steam estimators | Steam sales/revenue ranges | not official unit sales; sensitivity required |
| `V16-S19` | PUBLIC_OFFICIAL | KOSIS / KOCCA / DART | Korean industry, population, game, company context | macro/company context; not product demand by itself |
| `V16-S20` | CURRENT_PLATFORM | NAVER DataLab / DataLab API | Korean search-interest trend by topic/demographic/device | relative trend signal; not absolute customer count or demand proof |
| `V16-S21` | CURRENT_PLATFORM | NAVER Ads Keyword Tool | Korean monthly search count/click/CTR/competition context for search keywords | keyword/ad planning context; not purchase demand or conversion proof |
| `V16-S22` | VENDOR_DATA | Lovable — The Build Economy 2026 | what Lovable builders create; builder role/team/business intent | selected Lovable platform population + self-report; descriptive supply, not market demand/success |
| `V16-S23` | VENDOR_RESEARCH | Menlo Ventures — State of Generative AI in the Enterprise 2025 | U.S. enterprise GenAI spend by horizontal/departmental/vertical use case | ~500 enterprise decision-makers + bottoms-up market model; enterprise context, not startup success probability |
| `V16-S24` | VENDOR_CASE_STUDY | Lovable customer/founder stories | mechanism fixtures for domain expertise, workflow replacement, dense distribution, measurable ROI | vendor-selected winners; figures may be self/vendor reported; high survivorship/selection risk |
| `V16-S25` | SECONDARY_CASE | Indie Hackers / public founder outcome reporting | vibe-coded product outcome and distribution mechanism examples | secondary/self-reported case evidence; not prevalence or causal proof |
| `V16-S26` | COMMUNITY_ANECDOTE | Disquiet / DCInside / Blind maker posts | realistic builder questions, low-outcome examples, local execution context | nonrepresentative anecdote; hypothesis/user-need evidence only |
| `V16-S27` | MIXED_CASE_EVIDENCE | Tiro / ThePlato + App Store + The Bell coverage | Korean AI note-taking/productivity case: product, pricing, adoption proxies, reported growth/ARR context | company claims and press coverage are not audited cohort evidence; mechanism example only, not category success rate |
| `V16-S28` | PUBLIC_AUTHORITATIVE_GUIDANCE | OWASP — Secure Coding with AI Cheat Sheet / Top 10 2025 Next Steps | stage-appropriate security/accountability guard for AI-assisted and vibe-coded software | security guidance, not a prevalence estimate or market-demand source |
| `V16-S29` | METHODOLOGICAL_GUIDANCE | PRISMA-S — PRISMA extension for reporting literature searches (2021, 16 items) | reporting structure for a reproducible source-discovery record: sources searched, strategy as run, limits/restrictions, dates, records found, deduplication | designed for systematic reviews; adapting the reporting structure does **not** make a bounded market scan a systematic review, does not import systematic-review completeness expectations, and does not make a source set representative. Verified 2026-08-31 |
| `V16-S30` | PUBLIC_AUTHORITATIVE_GUIDANCE | AoIR — Internet Research: Ethical Guidelines 3.0 | disciplinary anchor for the duty to reason about secondary use of identifiable public/community posts across the research lifecycle | landing page verified 2026-08-31 for version/lineage/locator; **full PDF text not parsed in this run**, so no specific clause is quoted or attributed. Does not authorize identifiable quoting, does not make "publicly posted" equal to consent for research use, and does not convert posts into prevalence |
| `V16-S31` | ARCHIVAL_INFRASTRUCTURE | Internet Archive — Wayback Machine / Save Page Now | durable capture of an undated or volatile decision-relevant page at access time, returning a citable archived locator | capture is best-effort and can fail on robots-restricted, paywalled or dynamic pages — record `CAPTURED / CAPTURE_FAILED / NOT_ATTEMPTED` truthfully and never assert a snapshot that was not taken. A snapshot preserves what was seen; it does not validate the content. Verified 2026-08-31 |

## Standards-status freshness notes

- ISO 20252: the frozen `S-ISO-20252` row records ISO 20252:2019 (Edition 3) as the current
  published edition, with Edition 4 under publication. Re-checked 2026-08-31: the ISO catalogue
  entry for standard 88881 is titled **ISO/FDIS 20252**, i.e. still a Final Draft International
  Standard and not published, so Edition 3 remains current and the frozen note remains correct.
  VERIFICATION CEILING: a direct fetch of the ISO status page returned HTTP 403 to the checking
  worker, so this status is `UNCONFIRMED_INDIRECT` — derived from the catalogue listing title, not
  from a direct read. Re-check directly before any claim depends on it. Never cite Edition 4 as
  effective while it remains a draft.

## Canonical URLs (baseline)

- V16-S01: https://developer.apple.com/help/app-store-connect-analytics/benchmarks/peer-group-benchmarks/
- V16-S02: https://developer.apple.com/help/app-store-connect-analytics/acquisition/acquisition
- V16-S03: https://support.google.com/googleplay/android-developer/answer/10771707
- V16-S04: https://support.google.com/googleplay/android-developer/answer/9859173
- V16-S05: https://support.google.com/google-ads/answer/13020501
- V16-S06: https://support.google.com/google-ads/faq/10286469
- V16-S07: https://ads.tiktok.com/help/article/learning-phase
- V16-S08: https://ads.tiktok.com/help/article/troubleshooting-auction-ad-delivery-solutions
- V16-S09: https://ads.tiktok.com/help/article/search-ads-optimization
- V16-S10: https://partner.steamgames.com/doc/marketing/visibility
- V16-S11: https://partner.steamgames.com/doc/marketing
- V16-S12: https://support.google.com/trends/answer/4365533
- V16-S13: https://www.facebook.com/ads/library/
- V16-S20: https://developers.naver.com/products/service-api/datalab/datalab.md
- V16-S21: https://ads.naver.com/help/faq/1406
- V16-S22: https://thebuildeconomy.lovable.app/
- V16-S23: https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
- V16-S24: https://lovable.dev/blog
- V16-S25: https://www.indiehackers.com/
- V16-S26: https://disquiet.io/ ; https://gall.dcinside.com/ ; https://www.teamblind.com/kr/
- V16-S27: https://tiro.ooo/ko/ ; https://apps.apple.com/kr/app/id6503079839 ; https://m.thebell.co.kr/m/newsview.asp?newskey=202608061435015560106152&svccode=03
- V16-S28: https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html ; https://owasp.org/Top10/2025/ko/X01_2025-Next_Steps/
- V16-S29: https://www.prisma-statement.org/prisma-search ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/
- V16-S30: https://aoir.org/ethics/ ; https://aoir.org/reports/ethics3.pdf
- V16-S31: https://help.archive.org/help/using-the-wayback-machine/

## Runtime rule

A URL being in this registry does not freeze the content forever. For platform mechanics that materially affect a recommendation, verify the current primary document and retrieval date at execution time where web access is available. If not available, use the stored principle but do not assert volatile numeric facts as current requirements.
