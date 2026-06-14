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

