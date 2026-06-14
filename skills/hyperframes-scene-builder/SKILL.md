---
name: hyperframes-scene-builder
description: Create and revise HyperFrames HTML video compositions with CSS, GSAP timelines, composition IDs, reusable components, render commands, and proof-frame validation. Use when an agent needs to build a scene, edit a composition, render HyperFrames output, or debug HyperFrames-specific scene behavior.
---

# HyperFrames Scene Builder

Use this skill when implementing or revising a HyperFrames scene. This skill assumes HyperFrames is the render engine and the scene source is HTML/CSS/JS.

## Project Conventions

Prefer this layout for video projects:

```text
compositions/
renders/
assets/
snapshots/
assembly/
captions/
tools/
```

Use one composition per meaningful scene or reusable sub-scene. Keep files small enough to inspect and diff.

## Composition Rules

- Define an explicit composition root with `data-composition-id`, `data-width`, `data-height`, and timing metadata where the project uses it.
- Register GSAP timelines under the matching composition ID.
- Scope selectors to the composition root when scenes are nested.
- Avoid global selectors that can mutate other sub-compositions.
- Prefer reusable HTML/CSS components for repeated cards, labels, charts, rings, logo rows, and panels.
- Keep media paths relative to the composition project.

## GSAP Timeline Rules

- Use paused timelines for deterministic seekable animation.
- Place important moments at named labels or exact seconds.
- Use `set` for initial state.
- Use `fromTo` when CSS transforms already exist.
- Avoid accidental opacity-only transitions when the request asks for physical or material motion.
- Avoid bounce/rebound unless the user explicitly asks for it.
- Keep final frame stable enough for proof extraction.

## Render Loop

Typical commands:

```powershell
npx hyperframes preview
npx hyperframes lint
npx hyperframes render --composition compositions/scene-name.html --output renders/scene-name.mp4 --fps 24 --quality draft --workers 2
```

Use higher FPS or quality only when the scene is approved or when testing frame-rate-specific motion.

## Visual QA

After rendering:

- Extract first-frame, key-beat, and final-frame PNGs.
- Compare reference-image scenes against the final frame, not only the opening frame.
- Check text fit at desktop/video resolution.
- Check that hidden duplicated frames in following scenes are updated.
- Check theme colors in CSS, SVG fills/strokes, and inline styles.

## Common Fixes

- If a scene transition forgets a new label or visual, patch the next scene's carryover frame too.
- If timeline objects appear too early, verify initial `opacity`, path progress, and node visibility.
- If path points appear before the line reaches them, reveal points on line-progress milestones.
- If text gets clipped by a ring or card, reduce the full system scale instead of only shrinking the label.
- If product UI is cropped after a zoom, use no-crop or dynamic crop rather than a fixed aggressive crop.

## Output

Return changed composition files, render command used, render path, and proof frame paths.

