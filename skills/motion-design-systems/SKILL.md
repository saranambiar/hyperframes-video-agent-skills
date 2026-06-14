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

## Visual Intake Checklist

Before designing:

- Identify audience and context.
- Identify brand colors and forbidden colors.
- Identify whether the piece is product demo, launch film, UGC, ad, or enterprise explainer.
- Identify whether references are exact final frames or mood references.
- Identify whether the user wants premium restraint or high-energy editing.
- Identify whether typography must match an existing product or brand.

## Design System Defaults

When no brand system is supplied, default to:

- Warm off-white background.
- Black primary text.
- One accent color.
- Soft shadows.
- Conservative border radii.
- Plenty of negative space.
- Direct labels near objects.
- Few decorative elements.

Do not default to blue/purple gradients, neon lines, or dark sci-fi dashboards.

## Motion Palette

Use a small palette of repeated motion:

- Camera push.
- Camera swipe.
- Path draw.
- Material scale-in.
- Soft blur resolving to sharp.
- Highlight sweep.
- Subtle shimmer.
- Particle drift.
- Gentle hold motion.

Repeating a small motion vocabulary makes multi-scene videos feel coherent.

## Component Size Discipline

For fixed-format video:

- Define dimensions explicitly.
- Keep title hierarchy separate from card hierarchy.
- Make cards smaller than instinct suggests.
- Leave room for captions.
- Test final frame with captions on.
- Avoid cards inside cards.
- Avoid chart labels that require a legend to understand.

## Brand Cleanup Checklist

When changing colors:

- Replace CSS variables.
- Replace raw hex values.
- Replace SVG fills and strokes.
- Replace shadows and glows.
- Replace gradients.
- Replace duplicated carryover frame styles.
- Leave real logos alone unless requested.
- Leave product demo footage alone unless requested.

## Reference Matching Checklist

Compare:

- Object count.
- Relative positions.
- Scale.
- Typography weight.
- Line thickness.
- Border radius.
- Background warmth.
- Shadow softness.
- Label placement.
- Final hold readability.

## Questions To Ask

Ask if:

- The reference image conflicts with written brand style.
- A logo color conflicts with requested theme.
- A crop or caption may hide important UI.
- The user asks for a subjective style change without enough preference.

Do not ask if the answer can be proven with a proof frame.

## Failure Recovery

If user says it feels off:

- Check scale first.
- Check spacing second.
- Check color consistency third.
- Check motion timing fourth.
- Check typography last.

Most "not premium" complaints come from oversized elements, too many colors, or uncontrolled motion.
