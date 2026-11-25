# 小小夢魔 — 遊戲概念競賽決策報告

Date: 2026-11-24
Version: 0.2
Status: AI pre-score; waiting for owner selection

## Brief and hard gates

- Audience: elementary learners, provisionally grades 3–6.
- Purpose: introduce budgeting/saving and investment uncertainty/risk awareness.
- Platform/session: Godot Web, approximately 4–7 minutes, keyboard/pointer/touch.
- Decision owner: project owner; AI scores are advisory.
- Hard gates: exactly two levels; one primary interaction per level; each level shows a score and awards a KEY only when solved; final progress recap; child-safe original content; no real money/product recommendations/guaranteed returns; Godot web-feasible; no identifiable learner data.
- Source date: 2026-11-24. Financial capabilities framework and browser constraints are linked in `project-brief.md`.

## Educational priorities — provisional assumption

- Highest priorities: L Learning and A Appropriate challenge.
- Weights: L=.40, E=.20, M=.15, A=.25 (sum=1.00).
- Maximum penalties: G=.15, C=.10; no hard gate selected.
- Evidence plan: L short concept checks and misconception reduction; E completion and voluntary replay; M brief competence/retry rating; A recoverable errors and confusion notes; G rapid/random answer patterns; C repeated instructions, error clusters, and learner-reported confusion.
- These defaults are AI planning assumptions, not developer-selected values or validated research weights. Revise before final concept approval if desired.

Calculation: `R_edu = clamp(.40L + .20E + .15M + .25A - .15G - .10C, 0, 100)`.

## Hard-gate screen

- A, B, C, D, E pass as proposed, subject to child-safety review and final content review.
- F is eliminated: its multi-step day-management loop requires several scored actions per level and conflicts with the required single interaction unit per level.
- No candidate uses actual securities, live prices, or a promised return.

## Candidate population — generation 1

### A — Pocket Architect (夢幣築巢師)

- Fantasy/core verb: guide a tiny dream-keeper through rooms by planning where dream coins go.
- 30–60 second loop: see a goal and coin count → distribute coins among need, wish, and savings jars → preview what is funded → explain the trade-off → earn the room KEY.
- Two-level use: Level 1 builds a simple budget and savings goal; Level 2 chooses a fictional investment mix for a distant goal and observes that outcomes vary.
- Meaningful choice: spend now, save for a goal, or accept uncertainty for a longer horizon.
- Escalation/recovery: a changed goal demonstrates opportunity cost; a retry is allowed with a hint and no time penalty.
- Success/failure: earn the KEY by meeting the stated goal and explaining why; failed attempts show the consequence and can be revised.
- Session: 4–6 minutes. Minimum prototype: one drag/drop budget scene plus a deterministic second-room outcome table.
- Riskiest assumption: children understand the difference between a near-term savings goal and a longer-term uncertain investment.

### B — Whisper Mailbox (回音郵差)

- Fantasy/core verb: investigate strange letters and receipts before deciding what to do with the dream coins.
- 30–60 second loop: inspect one clue → choose a response → see who bears the consequence → explain the reasoning → earn the KEY.
- Two-level use: Level 1 distinguishes a need, a want, and a savings promise; Level 2 checks a fictional "guaranteed moonseed" claim for risk and pressure clues.
- Meaningful choice: trust a claim immediately, investigate, or ask a trusted adult.
- Escalation/recovery: clues become subtler in room two; feedback points to the missed clue.
- Success/failure: identify a sensible, safe next step rather than predicting investment profit.
- Session: 4–7 minutes. Minimum prototype: two illustrated letters with tappable evidence and a choice panel.
- Riskiest assumption: a story investigation still gives enough practice in positive money planning, rather than only scam avoidance.

### C — Mist Garden (霧中種子園)

- Fantasy/core verb: plant and tend fictional dream seeds while balancing time and uncertainty.
- 30–60 second loop: choose a goal horizon → place seeds in one or more beds → reveal a small deterministic weather outcome → compare result with goal → earn the KEY.
- Two-level use: Level 1 grows a savings goal steadily; Level 2 compares fictional variable seeds and shows that spreading choices can reduce concentration risk without guaranteeing against loss.
- Meaningful choice: concentrate for a chance at a larger outcome or spread across seeds for a steadier result.
- Escalation/recovery: the second season includes a calm, visible change in conditions; retry offers a comparison view.
- Success/failure: meet a goal threshold while identifying that outcomes can vary.
- Session: 5–7 minutes. Minimum prototype: three seed cards, two timeline slots, and a fixed outcome table.
- Riskiest assumption: students will not infer that the higher-variance seed is always the "best" answer after one lucky outcome.

### D — Lantern Bazaar (提燈市集)

- Fantasy/core verb: compare choices and plan purchases along a short lantern-lit route.
- 30–60 second loop: compare two offers or goals → choose a use for limited coins → see remaining resources and goal progress → explain the trade-off → earn the KEY.
- Two-level use: Level 1 compares needs, wants, and prices; Level 2 chooses a plan for a goal that is near or far and compares predictable saving with uncertain growth.
- Meaningful choice: lower immediate cost versus a better fit for the goal; near-term certainty versus long-term uncertainty.
- Escalation/recovery: room two adds one new piece of information; wrong choices reveal total cost and allow correction.
- Success/failure: choose a plan that meets the stated time and safety constraints.
- Session: 4–6 minutes. Minimum prototype: two price cards, a simple route map, and deterministic feedback.
- Riskiest assumption: comparison-shopping and investing can be connected without making investment look like a purchase with a known price.

### E — Weather Jar (天氣罐)

- Fantasy/core verb: prepare a dream-coin reserve before a gentle storybook weather change.
- 30–60 second loop: set aside coins → reveal a fictional expense or change → choose what to protect → see whether the goal survives → earn the KEY.
- Two-level use: Level 1 builds a small reserve for an unexpected need; Level 2 separates near-term money from long-term uncertain growth.
- Meaningful choice: protect a near-term need or expose too much to a variable outcome.
- Escalation/recovery: one mild forecast changes; the game explains why a reserve helps but cannot predict everything.
- Success/failure: keep a near-term goal available and identify uncertainty in the long-term option.
- Session: 4–6 minutes. Minimum prototype: a coin reserve bar and two scripted weather cards.
- Riskiest assumption: the weather metaphor communicates uncertainty rather than implying investment returns are literally predictable from forecasts.

### F — Clockwork Orchard (時鐘果園) — eliminated

- Fantasy/core verb: manage a multi-day orchard economy through repeated earning, spending, saving, and investment actions.
- Loop: many repeated actions across simulated days; long-run outcomes are visible.
- Elimination: hard-gate failure. Its multi-action management loop conflicts with one primary scored interaction per level and is likely too much for a short elementary web game.
- Reusable mechanism: a small, non-scored end-of-level consequence animation may be used by a selected concept.

## Tournament process

- Five separated review lenses were applied: game design, first-time player/accessibility, financial-domain accuracy, research/assessment validity, and production feasibility.
- Generation 2: simplified candidate actions to one explicit decision in each room; removed avoidable timers and extra controls; retired F at the hard gate.
- Generation 3: finalists converged on a short two-room structure with one deliberate choice, visible consequence, recovery feedback, score, and KEY per room. Further mutation would change only theme details, so the tournament stops here.
- Scores are model-generated pre-scores, not observations or expert/player evidence. Confidence: medium at most.

## Final tournament scorecard

R means Purpose Fit because this is an instructional product, not a research game. G/R/D axes remain separate. `R_edu` is not averaged into those axes.

| Rank | ID | G | Purpose Fit | D | L/E/M/A/G/C pre-score | R_edu | Evidence | Confidence | Main advantage | Main risk | Cheapest falsification test |
|---:|---|---:|---:|---:|---|---:|---|---|---|---|---|
| 1 | A | 84 | 91 | 88 | 83/72/76/86/18/24 | 75.4 | AI pre-score | medium | Directly connects a visible budget choice to a goal, with a clear second-level risk decision | Could oversimplify investment as a menu choice | Paper prototype: ask learners to explain why the near-term goal stays out of the variable option |
| 2 | D | 81 | 87 | 91 | 78/83/79/85/18/26 | 75.6 | AI pre-score | medium | Very feasible in Godot Web; card comparison is easy to localize and test | Near/far goal and investment risk may blur together | Two-card playthrough; ask what is known and what remains uncertain |
| 3 | B | 80 | 94 | 84 | 82/76/72/84/14/27 | 75.0 | AI pre-score | medium | Strongest alignment with recognizing pressure and guaranteed-return claims | Could under-teach ordinary budgeting and saving | Test whether players can name one positive saving action after the story |
| 4 | C | 86 | 88 | 77 | 84/82/76/78/25/35 | 73.7 | AI pre-score | medium | Memorable metaphor and strong visible cause/effect | Outcome randomness may reward guessing or teach lucky results | Give two different deterministic seasons and ask learners to compare risk, not just outcome |
| 5 | E | 78 | 90 | 86 | 81/73/76/83/16/24 | 74.4 | AI pre-score | medium | Naturally teaches reserve before long-term risk | Weather metaphor can imply false predictability | Ask learners to explain what a reserve can and cannot protect against |

Ranking rule: Pareto front first; within a shared front, lowest G/Purpose/D dimension, then mean score, then lower prototype cost. A, B, C, and D are on the first front; A leads by its minimum dimension (84), then D (81), B (80), and C (77). E is dominated by A and placed in the second front. All survivors meet default G≥75, Purpose Fit≥75, and D≥75 thresholds. `R_edu` below 75 triggers revision/testing for C and E. G<60 and C<70 review flags are absent in these pre-scores; this is not player evidence.

## Blind review lens summary

| Lens | Main finding | Evidence status |
|---|---|---|
| Game designer | A and C create the clearest action-consequence loop; D has the lowest bespoke mechanic cost | AI pre-score |
| First-time player/accessibility | One action, visible icons, no timers, and recoverable choices fit the age and browser context | Hypothesis; requires playtest |
| Financial-domain reviewer | Teach saving goals, uncertain returns, and warning signs; avoid a single "best investment" answer or guarantees | Primary-source grounded design review |
| Research/assessment reviewer | Keep game score formative; use separate short pre/post items if learning is evaluated; collect no names | AI pre-score; no formal study design |
| Production director | A or D has the lowest Godot/Blender scope; C needs careful outcome tuning and more animation | AI pre-score; local Godot/Blender installations confirmed |

## Recommendation and human decision

- Recommendation: A — Pocket Architect. It best balances concrete budgeting, the requested investment unit, browser feasibility, and a clear two-level score/KEY structure.
- Alternative: D — Lantern Bazaar, if short browser production and comparison-shopping are the main priorities.
- Style concepts already generated in this conversation: A hand-painted storybook; B tactile stop-motion 3D; C geometric paper diorama. They use the same room, character, and decision moment. Generated images are previsualizations, not production geometry.
- Owner selected C — Mist Garden. This human decision overrides the AI pre-score ranking; the recommendation A is not treated as approval. Visual direction B — tactile stop-motion 3D is also approved; see `visual-style-guide.md` and `../assets/concepts/approved-style-b-stop-motion.png`.
