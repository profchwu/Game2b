# System specification — Godot Web Mist Garden

Status: approved for implementation, version 0.3  
Date: 2026-11-24

## Purpose, users, scope, and non-goals

- Audience: elementary learners, provisionally grades 3–6.
- Purpose: practice a simple savings plan and recognize risk/uncertainty and concentration risk.
- Scope: two short levels, scores, KEY unlocks, gentle retry, progress summary, original 3D rooms/character/animations, web export.
- Non-goals: personal financial advice, securities/prices/accounts, real money, student profiles, telemetry, leaderboards, chat, fear-based pursuit, copied Little Nightmares assets.

## Functional requirements

1. Display an opening screen and clear instructions in Traditional Chinese.
2. Level 1 is one scored savings-plan interaction: choose how to divide 8 fictional dream coins. Keep 2 for today's needed watering can and save 6 toward next week's kite. The correct choice covers today's need and keeps the rest for the stated goal.
3. Level 2 is one scored investment-risk interaction: choose how to spread four fictional dream seeds across two variable garden beds for a distant goal. Feedback explains that spreading can reduce concentration risk but cannot guarantee against loss.
4. The user must solve the level interaction before its KEY is awarded and before the next level unlocks.
5. Each level shows its own score. The final screen shows both scores, a combined score, earned KEYs, and a short progress recap.
6. Incorrect answers provide a gentle explanation and retry; no timer or punitive failure state.
7. Restart resets run-local progress. Score logic is deterministic and local to the session.
8. Every room and character asset follows approved style B. Godot text and interface graphics remain separate from Blender textures.

## Non-functional requirements

- Godot 4.7.2; GDScript; Compatibility renderer; single-threaded Web export by default.
- Browser play via WebAssembly and WebGL 2 on a secure HTTPS site.
- Responsive 16:9-first layout with keyboard, pointer, and touch support; meaningful focus states and minimum touch targets.
- Traditional Chinese text remains legible at 100% and mobile widths; interactions do not rely on color or animation alone.
- Reduced-motion setting; no flashing/strobing; no sound-only information.
- No third-party runtime APIs, user accounts, analytics, or secrets.

## Data and interface contracts

- Per-run state: `level1_score`, `level2_score`, `key1_unlocked`, `key2_unlocked`, `attempt_count`, `selected_language`, `reduced_motion`.
- Score: first-attempt solution = 100; solved after one explanatory retry = 80; no score until solved. These are formative game points, not an educational assessment claim.
- No state is sent to a server or tied to identity.
- Interaction: a single choice per level, then feedback and an explicit continue button.

## Architecture and decisions

- Godot project with a main menu, level state controller, two room scenes, reusable choice/feedback panel, and results screen.
- Blender source: one editable scene file with named collections for character, props, and both rooms; export GLB assets with original materials and animation clips.
- Split presentation: 3D world for rooms/character; Godot Control nodes for text, choices, scores, KEYs, and progress.
- Use deterministic scenario outcomes; no random result determines the score.
- Decision: user selected concept C and style B; this supersedes the AI tournament rank.

## Configuration, privacy, safety, and licensing

- Do not place secrets or user data in the browser build.
- No third-party assets unless their license and source are recorded; prefer original geometry/materials.
- Use only fictional dream coins/seeds; do not name real investment products or imply personal recommendations.
- Keep mystery gentle and avoid threat, gore, pursuit, and jump scares.

## Error handling and recovery

- Invalid or incomplete selection leaves the interaction state unchanged and highlights the missing selection.
- Incorrect answer shows a short reason and permits retry; correct answer unlocks the KEY and continues.
- Asset-loading failure shows an accessible fallback screen with room color, title, and full interaction UI.

## Test strategy and acceptance criteria

- Import/start project headlessly; ensure no parse/import errors.
- Exercise both answer paths, retry and key gate, scores, results, and restart.
- Export and serve Web build; verify an HTTPS WebGL 2 browser, desktop/mobile layout, keyboard/pointer/touch, Traditional Chinese fonts, reduced motion, and browser console.
- Visual check Blender render and Godot integration for scale, light, readability, animation, and style consistency.

## Deployment and operation

- Build output: `build/web/` (not committed as source unless needed for Pages artifact).
- Host: GitHub Pages from the existing repository with a reproducible Actions workflow.
- Use single-threaded web export to avoid cross-origin isolation headers unless tests show a reason to enable threads.
- Record exact engine/export versions and preserve rollback to the last published build.

## Open items

- Exact target grade and class accommodations remain open; use grades 3–6 provisionally.
- Validate language level and learning effect with an educator/learner review before claiming effectiveness.
## 2026-11-25 implementation update
- The repository now contains a Godot 4.7.2 project implementing the selected C gameplay and B stop-motion visual direction.
- Two Blender-exported rooms and an animated character are imported as GLB; per-level scoring, retry, KEY gating, final progress recap, restart, and reduced motion are implemented.
- Added GitHub Pages Actions workflow and a Web export preset. Local Godot startup/import passes. Local export templates are not installed; the workflow obtains them in CI.
- GitHub Pages must be configured to use GitHub Actions on the first deployment if the repository has not enabled Actions-based Pages before.

## Deployment gate — 2026-11-25
GitHub Actions successfully builds the Web export and uploads a Pages artifact. The deployment action cannot create a Pages deployment until Pages is enabled for this repository. Set **Settings → Pages → Build and deployment → Source** to **GitHub Actions**, then rerun the workflow. The current failed deployment did not publish a site.
