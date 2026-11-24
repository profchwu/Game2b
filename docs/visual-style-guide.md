# Visual style guide — B: tactile stop-motion 3D

Status: approved by the project owner on 2026-11-24
Canonical reference: [`approved-style-b-stop-motion.png`](../assets/concepts/approved-style-b-stop-motion.png)

## Direction

Create an original, hand-crafted miniature world that looks like a carefully lit stop-motion set. Keep the mystery and oversized scale of a dream house, with warmth and safety appropriate for elementary learners.

## Shape and materials

- Rounded, slightly irregular forms; soft asymmetry is welcome.
- Felt, stitched cloth, knitted trim, clay-like skin, hand-carved wood, aged brass, and softly frosted glass.
- Small seams, patches, dents, and tool marks should support the handmade feel without making surfaces noisy.
- Use bevels and broad silhouettes so models remain readable in a browser viewport.
- Main character: teal patchwork rain cape, rust-red clothing accents, round satchel, brass firefly lantern. Preserve this silhouette and palette in every room and animation.

## Palette and light

- Core colors: deep teal and moss, warm walnut, muted rust, parchment cream, and amber lantern light.
- Use a soft warm key light around points of interaction, with subdued cool ambient fill.
- Maintain enough value contrast for the character, interactable objects, and feedback to read at small screen sizes.
- Avoid strobing lights, pitch-black interaction zones, and color-only status cues.

## Camera and composition

- Compose rooms as tactile miniature sets with strong foreground, play space, and oversized background architecture.
- Keep interaction objects and the character unobstructed; reserve clean space for Godot UI overlays.
- Do not bake words, scores, or labels into textures. Use actual UI text and icons in Godot.

## Motion

- Pose-to-pose, handcrafted timing: gentle idle breathing, lantern sway, short walk, reach/touch, and clear key-unlock response.
- Consequential motion should show cause → room/object response → player result.
- Keep input response immediate; only decorative animation may use a stepped stop-motion feel.
- Provide a reduced-motion option and never make success information depend on animation or sound alone.

## Safety and originality

- Original character, rooms, props, sounds, and story. The supplied Little Nightmares image is only a high-level atmosphere reference; do not recreate its exact composition, props, characters, or protected assets.
- Keep the mood mysterious and cozy; no gore, frightening pursuit, threatening adult figures, or punitive jump scares.

## Asset acceptance

- Blender source scene is editable and organized into named collections.
- Environment and character assets use this palette/material language consistently.
- Character animation includes idle, walk, and interaction/key moments.
- GLB exports preserve scale, materials, and required animations for Godot Web.
