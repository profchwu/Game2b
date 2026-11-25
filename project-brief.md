# 小小夢魔：夢境理財所 — 專案簡述

Status: approved baseline — gameplay C and visual direction B selected
Requirements version: 0.2
Date: 2026-11-24

## Goal

Build a short, original financial-learning adventure for elementary students. Deliver it as a Godot web export. Use Blender for the selected direction's 3D environments, characters, and animations.

## Target users and context

- Primary users: elementary pupils; grades 3–6 are a working assumption, not yet confirmed.
- Context: short classroom or home browser sessions using keyboard, mouse, or touch.
- Language: Traditional Chinese first; avoid text embedded in generated art so localization remains readable.

## Evidence and pain points

- Confirmed from the owner's request: the unit is everyday money management and investment; the build needs two levels, an interaction in each, a score per level, a KEY reward for solving, and a final progress display.
- Domain grounding: CFPB describes middle childhood (ages 6–12) as a period when money habits form and children begin learning basic money management. Its elementary-school materials include a grades 3–5 financial-capability survey. Sources: [CFPB youth financial capability](https://www.consumerfinance.gov/consumer-tools/educator-tools/youth-financial-education/learn/) and [CFPB elementary-school survey guide](https://files.consumerfinance.gov/f/documents/cfpb_building_block_activities_mapping-your-money-journey-elementary_guide.pdf).
- Domain grounding: the EU/OECD framework organizes children's financial competencies around money and transactions, planning and managing finances, and risk and reward. Source: [EU/OECD Financial Competence Framework for Children and Youth](https://www.oecd.org/en/publications/financial-competence-framework-for-children-and-youth-in-the-european-union_bf059471-en.html).
- Financial-safety grounding: investment outcomes are not guaranteed; diversification can reduce concentration risk but cannot guarantee against loss. Sources: [Investor.gov risk and return for teachers](https://www.investor.gov/additional-resources/information/youth/teachers-classroom-resources/risk-and-return) and [Investor.gov diversification](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments).
- Reference mood only: the Steam page describes Little Nightmares as a horror adventure rated Teen. Use broad environmental contrast, oversized architecture, and light/shadow only; do not copy protected characters, rooms, assets, story, or gameplay. Source: [Little Nightmares on Steam](https://store.steampowered.com/app/424840/Little_Nightmares/).
- No learner interviews or playtests have been conducted. All current design scores are AI pre-scores, not evidence of learning or fun.

## Problem statement

Elementary learners need safe, concrete practice making everyday money choices and recognizing that investment involves uncertainty. A short browser game can let them try a decision, see its consequence, and explain what they learned without using real money or recommending actual products.

## Inputs, processing, and outputs

- Inputs: one answer or resource-allocation action per level; pointer/touch and keyboard support are required.
- Processing: deterministic scoring, feedback, KEY unlocks, and progress summary; no AI at runtime.
- Outputs: two level scores, two KEY states, explanations after choices, and a final progress summary.

## AI role and authority

- AI may draft concepts, visual references, code, and test plans.
- The owner selects the gameplay concept and visual direction; AI ranking is advisory and labelled as an AI pre-score.
- Generated images are visual references only. Blender models and game assets must be original and reviewed against the approved style guide.

## MVP and non-goals

### MVP

- Original Godot project in this repository, exported for modern browsers.
- Two short levels in the Mist Garden concept: (1) plan and save dream coins for a goal; (2) compare a concentrated seed plan with a spread plan and learn that diversification can reduce concentration risk but cannot guarantee against loss.
- One clear interaction per level, scored result, explanation, KEY reward, and final progress summary.
- Blender-made 3D room(s), character, and a small set of cause-and-effect animations after art approval.
- GitHub Pages deployment after the Godot web export and browser checks.

### Non-goals

- Real financial accounts, money, trading, or personalized investment advice.
- Student accounts, chat, leaderboards, analytics, or collection of identifiable data.
- Recreating Little Nightmares or using its characters, locations, props, music, or exact visual designs.
- Building all three visual directions as finished assets; only one approved direction will be produced.

## Constraints and risks

- Web compatibility: Godot 4 web builds use WebAssembly and WebGL 2; use GDScript and the Compatibility renderer. Prefer single-threaded web export for simpler hosting unless cross-origin isolation is intentionally configured. Source: [Godot 4.5 web export docs](https://docs.godotengine.org/en/4.5/tutorials/export/exporting_for_web.html).
- Godot 4.7.2 is installed at `C:\Godot`; Blender 5.3 is installed at `C:\blender`.
- Blender Toolkit configuration/add-on was not detected. Use the available Blender executable and a reproducible local Blender script if the add-on is unavailable.
- The dark reference must be softened for children: no gore, frightening pursuit, or punitive failure. Keep text, contrast, reduced-motion options, and touch targets accessible.
- Learning outcomes cannot be claimed until a suitable pre/post assessment or supervised playtest provides evidence.

## Delivery context

Public browser game in the `profchwu/Game2b` GitHub repository, deployed through GitHub Pages. GitHub Pages is not yet configured for the future Godot build.

## Success measures

- Both level interactions and score/KEY transitions complete deterministically.
- A learner can explain one budgeting/saving principle and one risk/uncertainty principle after play; this remains a test criterion, not a demonstrated outcome.
- No real-money choices, investment guarantees, student identity collection, or copied protected assets.
- Godot web export launches on a modern WebGL 2 browser and fits desktop and mobile layouts.
- Blender source files and exported game assets are versioned and reproducible from the project.

## Assumptions to test

- Grades 3–6 can understand fictional coin allocation and simple risk variation when shown with icons and short Traditional Chinese prompts.
- A gentle, mysterious storybook setting adds engagement without making the experience frightening.
- The chosen 3D style can be built efficiently in Blender and rendered well by Godot's web Compatibility renderer.

## Acceptance examples

1. A correct Level 1 choice updates the level score, displays explanatory feedback, and grants KEY 1.
2. Level 2 cannot be skipped; its answer updates its own score and grants KEY 2 only after the interaction is solved.
3. The final screen shows both level scores, combined progress, and a plain-language learning recap.
4. Every investment example states or demonstrates uncertainty; no option is described as guaranteed profit.
5. Restart returns to the opening state and clears run-local score/key state.

## Open questions

- The game will target grades 3–6 provisionally; confirm exact grade band and any classroom accessibility needs.
- Is grades 3–6 acceptable, or should the game target a narrower band?

## User approval

Gameplay C (Mist Garden) and visual direction B (tactile stop-motion 3D) are approved. The Balanced educational reward profile and grades 3–6 remain provisional assumptions.
