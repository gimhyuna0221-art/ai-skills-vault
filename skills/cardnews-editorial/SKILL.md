---
name: cardnews-editorial
description: Create and review Korean explanatory cardnews from verified references. Use for difficult-concept explainers, question-led carousels, editorial typography, or requests to reduce generic AI-looking design. Preserve the reader's actual questions, build one idea per card, and verify mobile readability and factual claims.
metadata:
  version: "1.0.0"
  reviewed_on: "2026-10-15"
  upstream_reference: "pbakaus/impeccable 4.5.2"
  installation_type: "original-cardnews-adapter"
---

# Cardnews Editorial

## Scope and boundaries

This is an independently written cardnews adapter informed by the references below, not a full installation or a translation of Impeccable. Upstream binaries, launchers, hooks and web-UI commands are not included or executed. Saving this file does not register a ChatGPT-wide tool or guarantee loading in another session. Only report the actual storage path, branch, commit and checks performed.

Use the user's explicit brief and existing brand assets before stylistic defaults. Read existing project rules before changing a repository. Do not publish to social media, merge a branch, purchase assets, or make unrelated changes without authorization.

## References to read

1. User-specified cardnews design reference: Elancer, "카드 뉴스 디자인: 사람들의 눈길을 사로잡는 완벽한 가이드", dated 2024-07-21.
   https://www.elancer.co.kr/blog/detail/284
   Apply its reading-order and text/image separation guidance, not its unverified marketing-performance statistics. Do not copy example artwork.
2. Reviewed GitHub skill: https://github.com/pbakaus/impeccable
   Entry: .agents/skills/impeccable/SKILL.md, version 4.5.2.
   Reviewed entry blob: b9d82965dd59a45596c5b63a1cf4207168a272a7.
   Quality reference: .agents/skills/impeccable/reference/craft-floor.md.
   Reviewed quality-reference blob: ae213ce801ebb2085033b309b4144e8d7e9996ba.
   Upstream is Apache-2.0. This adapter does not redistribute verbatim upstream files.
3. Alternative considered: https://github.com/Leonxlnx/taste-skill
   Keep as an optional art-direction reference; do not claim it was installed.

The GitHub references target frontend interfaces. Transfer editorial design principles, not website components, software setup instructions, or every numeric web-typography rule. Recheck upstream before a future upgrade; do not silently follow changed instructions.

## 1. Define what the reader should understand

Write one sentence stating what a beginner should be able to explain after the last card. Start with a concrete question or recognizable action. Separate the object, its use, and a research question about that object.

Do not tell a reader who remains confused that they have understood perfectly. Replace the explanation rather than repeating the same abstraction. Keep the user's natural phrasing when it makes the question clearer. Do not caricature or mock a beginner.

## 2. Verify before simplifying

Maintain a claim-to-source record before layout. Prefer original papers, official documentation and primary announcements. Verify current claims on the web rather than reusing a previous assistant's citations or assertions.

Label analogies and invented numbers as illustrations. Distinguish a mathematical model, numerical approximation, formal proof, physical observation, research announcement and external acceptance. Avoid turning a limited or conditional result into a universal claim.

Put short source identifiers on the relevant cards and full citations in the caption or accompanying source document. If a claim cannot be verified, omit it or label the uncertainty explicitly. Brevity is not permission to remove a condition that changes the conclusion.

## 3. Draft the sequence

Default to 6-8 cards unless the brief needs another length. One card answers one question. A useful sequence is: recognizable question -> familiar example -> plain-language rule -> concrete application -> important distinction -> takeaway.

Do not force every topic through all six stages. If the mathematical limit, the application and the research history cannot be understood together, split them into episodes rather than shrinking the text.

A headline should carry one complete thought. Keep the main explanation short; aim for two or three lines when possible. A necessary four-line explanation gets more space, not a smaller font. Do not fill unused space with extra facts.

## 4. Set the visual system

Before rendering, record canvas ratio, safe margins, type roles, palette, illustration style, alignment and page-number location. A suggested starting point, not a platform requirement: portrait 4:5 canvas, 1080 x 1350 pixels, 80-pixel safe margins, headline 72-104 pixels, body 40-48 pixels and source/footer 24-28 pixels. Check the actual Korean line breaks and glyphs.

Use strong size and weight hierarchy. Give the main visual and the main text separate readable areas. For longer text, use upper-left reading order with the illustration below or to the right. Keep the sequence coherent without repeating an identical composition on every card.

Reduce generic AI-design habits: unmotivated gradients, glass panels, decorative glow, unrelated emoji, repeated icon-heading-paragraph boxes and over-polished stock-style visuals. These are defaults to question, not bans on an explicit user style. Avoid both empty decoration and cramped wall-of-text layouts.

Prefer one purposeful visual per card. A hand-drawn direction must use consistent, intentional illustration; a technical diagram must explain a real relation. Do not replace explanation with random swirls, formulas or scientific-looking decoration.

## 5. Build on the appropriate surface

For image-only work, use the available image-generation tool. For editable multi-card work, use supported design or slide tools with text and artwork separated where practical. Do not promise editability, exact pixel dimensions, separate files or exports that were not produced.

Create one coherent sequence rather than independent style variations. No public posting is implied by creating the cards. Do not bundle font files. If the environment supports only a subset of the requested output, label that subset clearly.

## 6. Bounded review

Inspect the actual output, not just the prompt. Batch these checks: factual conditions, one idea per card, reading order, Korean spelling, text clipping, contrast, image/text overlap, consistency, page order and source placement. Review at intended mobile display size as well as full size when the output is available to inspect.

Fix identified defects in one batch and confirm once. Do not spend unlimited generations polishing. Report unperformed visual checks as unperformed. Never claim guaranteed engagement, absence of all AI artifacts, or user comprehension.

## Completion record

Record what was generated, what was saved, exact repository branch/commit when used, the references and date checked, tests actually run, and limitations. Repository storage, local skill availability, tool registration and account-wide installation are different states; do not conflate them.
