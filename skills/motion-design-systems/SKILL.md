---
name: motion-design-systems
description: Reusable visual and motion design systems for agent-created videos, including premium motion language, glassmorphism, chart/data storytelling, CTA layouts, logo rows, table frames, color tokens, and brand consistency. Use when a video scene needs polished visual direction, Apple/VisionOS-style motion, enterprise design, theme cleanup, reusable components, or reference-image final-frame matching.
---

# Motion Design Systems

Use this skill when the request depends on visual taste, design consistency, or reusable motion components.

## Start With The Visual System

Define these before animating:

- Background and lighting.
- Primary and neutral colors.
- Typography and type scale.
- Component materials.
- Shadow style.
- Motion language.
- Forbidden looks.

Use `references/premium-motion.md` for motion language and `references/theme-tokens.md` for color discipline.

## Build Reusable Components

Create small components for repeated visual objects:

- Glass cards and panels.
- Logo rows.
- CTA lockups.
- Table frames.
- Chart axes, paths, labels, nodes, and gap fills.
- Orbs, rings, particles, and role labels.

Keep components parameterized with CSS custom properties or JS constants. Avoid hard-coded one-off colors if the user may request theme changes.

## Premium Motion Rules

- Prefer scale, blur, depth, path drawing, camera drift, and material changes over basic fade-only reveals.
- Use restraint. Premium motion should feel deliberate, not busy.
- Avoid bounce, rebound, neon, sci-fi HUDs, and generic SaaS explainer tropes unless explicitly requested.
- Use ease curves that settle naturally: `power2.out`, `power3.out`, `expo.out`, `sine.inOut`.
- Keep final-frame composition readable and still alive with subtle ambient motion.

## Chart And Data Storytelling

Use progressive reveal logic:

- Axes and labels establish the frame.
- Lines draw from left to right.
- Points appear only when the line reaches them.
- Labels sit near the object they describe, not in detached legends, unless the user asks for a legend.
- Gap fills appear after both curves make the gap meaningful.

Read `references/chart-storytelling.md` for more.

## Theme Consistency

When a theme changes:

- Search CSS, SVG, inline styles, gradients, canvas constants, and duplicated carryover frames.
- Do not recolor logos or product-demo footage unless explicitly requested.
- Verify with proof frames from both source scene and next-scene carryover.

## Output

Provide:

- Component or composition changes.
- Token changes.
- Render/proof frame paths.
- Any remaining subjective items that need user approval.

