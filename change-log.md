# Change log

## 0.2 — 2026-11-24

- Reframed the deliverable from the previously pushed standalone HTML prototype to a Godot web game, as requested.
- Added an initial Design Thinking brief, explicit assumptions, domain-source notes, deployment requirements, and educational safety boundaries.
- Added a game-design tournament report and three generated visual concepts; no style or gameplay winner has been silently selected.
- Owner selected visual direction B; the approved concept image and reusable prompt pack are now included in the repository.
- Owner selected gameplay concept C — Mist Garden. The selected concept and visual style now form the approved production baseline.
- No Godot implementation or Blender asset changes have been made yet; they depend on the user's gameplay and style choices.
# Change log

## 2026-11-25 — Godot Web implementation
- Added Godot 4.7.2 project with two 3D learning rooms and a puppet-style dream keeper exported from Blender 5.3.
- Implemented the selected Mist Garden concept: savings planning, investment uncertainty, retry feedback, per-level scores, gated KEY rewards, and a final progress recap.
- Added single-threaded Web export preset and GitHub Pages Actions deployment workflow.
- Added Traditional Chinese font and its SIL Open Font License.
- Verified Godot headless project import and runtime startup. Local Web export needs the matching Godot Web export templates; GitHub Actions downloads templates during CI.

## GitHub CI result — 2026-11-25
- GitHub Actions run `45574000146` successfully imported assets, exported the Godot Web build, and uploaded the Pages artifact.
- Deployment stopped because GitHub Pages is not enabled for this repository (`Ensure GitHub Pages has been enabled`, HTTP 404).
- After setting **Settings → Pages → Build and deployment → Source: GitHub Actions**, push any new commit or run the workflow manually to publish.
