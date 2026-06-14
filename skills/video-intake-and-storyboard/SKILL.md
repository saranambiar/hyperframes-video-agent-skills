---
name: video-intake-and-storyboard
description: Convert rough video prompts, scripts, reference images, and edit notes into decision-complete scene specs and storyboards for agent-led video production. Use when a user describes a scene, gives timestamped narration, asks to preserve previous scenes, references a concept image, or requests a multi-scene video plan.
---

# Video Intake And Storyboard

Use this skill before building scenes. The goal is to transform conversational direction into a spec that another agent can execute without guessing.

## Intake Pass

1. Extract hard facts.
   - Scene number or section.
   - Duration and target frame rate/resolution.
   - Narration text and phrase timestamps.
   - Reference images or final-frame targets.
   - Asset locations.
   - Explicit "do not touch" boundaries.
   - Required transition from previous or next scene.

2. Extract style constraints.
   - Desired aesthetic.
   - Colors, typography, materials, and motion language.
   - Forbidden looks or effects.
   - Brand consistency rules.

3. Extract approval state.
   - Approved scenes.
   - Work-in-progress scenes.
   - Existing renders to preserve.
   - Current known issues.

4. Identify missing decisions.
   - Ask only if the answer changes the implementation.
   - Prefer concrete choices: crop/no crop, caption style, transition direction, final-frame priority, music volume behavior.

## Scene Spec Rules

- Use `templates/scene-spec.md` for each scene.
- Write beats as timestamped visual actions, not vague animation mood.
- Include what must appear by exact timestamps.
- Include what must not appear early.
- Include first-frame and final-frame requirements.
- Include proof timestamps for later QA.

## Storyboard Rules

- Use `templates/storyboard.md` for multi-scene work.
- Mark approved scenes as locked.
- Note carryover dependencies when one scene begins from another scene's final frame.
- Track which audio clip controls each scene duration.
- Track which caption/script file is authoritative.

## Prompt Patterns That Reduce Iteration

Prefer prompts that include:

- Final frame target.
- Exact time when important elements appear.
- What should be visible before and after that timestamp.
- Which existing scenes must remain untouched.
- Whether style can change or must be reused.
- Whether audio is reference-only or must be overlaid.

Avoid treating these as optional:

- First-frame continuity.
- Carryover frame updates.
- Caption timing source.
- Music tail timing.
- Product-demo crop safety.

## Output

Produce a filled scene spec or storyboard, plus a short list of decisions still needed. If all decisions are derivable from assets and prior context, proceed without asking.

## Scene Spec Quality Bar

A scene spec is ready to implement when it answers:

- What happens in the first frame.
- What happens in the final frame.
- What changes over time.
- What narration or audio drives timing.
- What exact timestamp matters most.
- What prior scene must remain untouched.
- What assets are required.
- What style must be reused.
- What visual references control layout.
- What proof frames will demonstrate success.

## Separate Specific Content From Pattern

When converting prompts, split notes into:

- Project-specific content: names, logos, narration, product UI, brand copy, private filenames.
- Reusable pattern: camera swipe, chart draw, caption preview, crop safety, music ducking, final-frame proof.

Only reusable patterns belong in future skills or examples.

## Timestamp Handling

Treat timestamps as production constraints:

- "At 5s" means visible by that global or local time.
- "Start around 3s" means animation may begin slightly earlier if it must be visible by 3s.
- "Land by 10s" means final state should be reached at or before 10s.
- "Hold for 3s" means no major layout change during that hold.
- "Do not appear before" means set initial state and reveal only after the cue.

Always record whether timestamps are local to a scene or global to the full video.

## Reference Image Handling

For a reference image:

- Identify what must match: composition, color, size, text, position, or only concept.
- Identify what may differ: exact copy, real data, logo art, camera crop, or animation path.
- Work backward from final frame.
- Plan a final-frame proof.
- Plan a next-scene carryover proof if the next scene begins from this frame.

## Approval Boundaries

Capture phrases like:

- "Do not modify Scene 01."
- "Treat this as approved."
- "Do not regenerate from scratch."
- "Keep style, typography, colors, and components."
- "Only update this transition."
- "Use the attached image only as reference."

These are constraints, not suggestions.

## Useful Clarifying Questions

Ask only if not discoverable:

- Is the audio final or reference-only?
- Should the final frame match the image exactly or directionally?
- Is the raw screen recording allowed to show its canvas?
- Should captions appear during silent sections?
- Should music rise during pauses or stay low?

## Storyboard Failure Modes

Watch for:

- Scene durations that do not match audio durations.
- A scene that depends on an uncreated prior final frame.
- A reference image that conflicts with written timing.
- A user saying "ignore this reference" after it was already used.
- A final scene change that requires earlier caption or audio updates.

## Handoff Format

For implementation, hand off:

- Filled scene spec.
- Filled storyboard when multi-scene.
- Asset list.
- Locked scene list.
- Open questions.
- Recommended implementation skill order.
