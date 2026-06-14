# Scene Spec: Sample Product Reveal

## Scene Identity

- Scene ID: 01
- Working title: Sample Product Reveal
- Target duration: 8 seconds
- Output format: 1920x1080, 60fps
- Source composition: `compositions/scene-01.html`
- Render output: `renders/scene-01.mp4`

## User Intent

- Objective: Introduce a product concept with a premium motion style.
- Audience: Enterprise buyers.
- Desired emotional tone: Calm, clear, high-trust.
- What this scene must communicate: A product is moving from concept into measurable workflow.
- What this scene must not feel like: Neon sci-fi, crowded SaaS dashboard, or stock explainer.

## Inputs

- Narration or script: "The system is ready. Now the workflow becomes measurable."
- Reference images: `assets/reference-final-frame.png`
- Logos or brand assets: none
- Product footage: none
- Existing scenes that must remain untouched: none

## Visual Direction

- Final frame description: Off-white canvas with a glass panel, one orange curve, one black comparison line, and direct labels next to each line.
- Background: Warm off-white.
- Primary colors: black ink, orange accent.
- Typography: clean sans-serif.
- Motion language: restrained path drawing and subtle camera drift.
- Component style: glass panel, soft shadows, line-adjacent labels.
- Elements to avoid: legends, bounce, neon, dark background.

## Beat Timeline

| Time | Narration or cue | Visual action | Required proof |
| --- | --- | --- | --- |
| 0.0s | "The system is ready." | Glass panel forms from scale and blur. | first-frame proof |
| 2.0s |  | Starting dot appears. | dot proof |
| 3.0s | "Now the workflow..." | Orange curve draws left to right. | curve proof |
| 5.0s | "...becomes measurable." | Black comparison line draws below. | label proof |
| 6.5s |  | Gap annotation appears. | final-frame proof |

## Continuity

- First frame must match: previous scene final off-white background.
- Last frame must be reusable by: Scene 02 carryover.
- Transition in: camera swipe from left.
- Transition out: camera drift right.
- Carryover frame files to update: `compositions/scene-02.html` if final label changes.

## QA Checklist

- Exact final frame proof timestamp: 7.8s
- Boundary proof timestamps: 0.05s, 7.95s
- Caption proof timestamp: 3.0s
- Audio sync proof timestamp: 5.0s
- Known risk: chart labels may appear too late.
- Acceptance criteria: both line labels visible before final hold.

