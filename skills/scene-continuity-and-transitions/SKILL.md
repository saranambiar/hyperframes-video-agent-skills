---
name: scene-continuity-and-transitions
description: Preserve visual continuity across video scenes with previous-final-frame starts, camera swipes, carryover frames, transition QA, and boundary proofing. Use when a scene must begin from the exact last frame of a previous scene, when adding camera-move transitions, when replacing scene endings, or when debugging stale starting frames.
---

# Scene Continuity And Transitions

Use this skill when scenes must feel like one continuous visual journey instead of separate slides.

## Continuity Contract

Before editing a scene, identify:

- Previous scene final frame.
- Current scene first frame.
- Transition direction.
- Camera movement duration.
- Any duplicated chart/table/card/logo/text in the next scene.
- Any approved scene that must not be modified.

Use `references/carryover-frames.md` for duplicated-frame checks.

## Camera Swipe Pattern

For a rightward camera movement:

- Move the current world left.
- Bring the next world in from the right or land on a clean blank field.
- Keep background color, lighting, and scale continuous.
- Use slight blur or parallax only if it improves realism.
- Avoid fading to a new slide unless the user asks for a cut or fade.

For a downward camera movement:

- Move from the hook/top field into the first current-video frame.
- Keep speed high enough to feel like a transition, not a scene pause.
- Match color and scale at the landing frame.

## First-Frame Matching

When a scene begins from the previous scene:

- Copy or recreate the previous final frame in the new composition.
- Include all latest text, labels, theme colors, plus symbols, highlights, and annotations.
- Re-render both affected scenes if the final frame is source-driven.
- Extract proof frame just before and after the boundary.

## Boundary QA

Always verify:

- No visual pop at the join.
- No stale text from an older render.
- No sudden color shift.
- No missing annotation that was added to the previous scene.
- No unwanted crop or scale change.
- Captions do not cover critical boundary text.

## Surgical Change Rule

If the previous final frame changes, assume the next scene may also need a source patch. Search before declaring done.

## Output

Provide:

- Changed scene files.
- Re-rendered scene list.
- Final assembly path.
- Boundary proof frames.
- Exact timestamps checked.

