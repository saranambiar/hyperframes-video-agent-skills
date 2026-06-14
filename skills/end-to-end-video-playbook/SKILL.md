---
name: end-to-end-video-playbook
description: End-to-end video production workflow for coding agents using HyperFrames, FFmpeg, captions, audio sync, music beds, and render QA. Use when a user asks for a complete video, multi-scene edit, launch video, product/demo video, UGC-style edit, enterprise explainer, or final assembled MP4 from prompt/script/assets.
---

# End-To-End Video Playbook

Use this skill to coordinate a complete video project from rough request to verified final render.

## Workflow

1. Ground in the current project.
   - Inspect available assets, renders, compositions, scripts, audio, captions, and prior approvals.
   - Identify locked scenes and user boundaries such as "do not modify Scene 01."
   - Use `templates/storyboard.md` for multi-scene structure.

2. Convert intent into production artifacts.
   - Create one `templates/scene-spec.md` per scene.
   - Separate user-specific content from reusable production patterns.
   - Record exact durations, final-frame requirements, narration, visual beats, transition dependencies, and proof timestamps.

3. Route to focused skills.
   - Use `video-intake-and-storyboard` for unclear prompts or new scenes.
   - Use `hyperframes-scene-builder` for HTML/GSAP composition work.
   - Use `audio-sync-assembly` for narration timing, segment retiming, and FFmpeg assembly.
   - Use `captions-and-music-bed` for subtitles, music ducking, and final silence.
   - Use `render-qa-and-surgical-changes` for proof frames, exact timestamp checks, and safe final edits.

4. Build in layers.
   - Draft scene renders first.
   - Assemble narration-only master before final music.
   - Add captions after the visual/audio timeline is stable.
   - Add music bed after narration and captions are correct.

5. Verify before reporting completion.
   - Run media probes on final outputs.
   - Extract proof frames at every risky timestamp and scene boundary.
   - Generate preview clips around transitions and sync-critical moments.
   - State what was verified and what remains subjective.

## Production Rules

- Never patch an old final MP4 when source scenes and assembly scripts exist.
- Do not globally slow a scene if only a pause or one cue needs timing.
- Prefer hold frames for silence and deliberate pacing.
- Re-render only affected scenes during final surgical changes.
- Always check duplicated carryover frames when a previous final frame changes.
- Keep client/private assets out of reusable examples.

## Required Outputs

For full projects, produce or update:

- Storyboard or timeline manifest.
- Scene renders.
- Final assembly script or command plan.
- Caption file if captions are requested.
- Final MP4.
- Proof frames/contact sheet.
- Short preview clips for risky sections.

## Decision Checklist

Before building, decide and record:

- Whether this is a new video, scene addition, or final edit.
- Whether the user approved any existing scenes.
- Whether previous renders are source of truth or just previews.
- Whether the final output needs captions.
- Whether music should be added, replaced, lowered, or left alone.
- Whether product-demo footage should be cropped.
- Whether exact phrase timing matters.
- Whether a silent hook, pause, or final hold exists.
- Whether the final render should be 24, 30, 48, 60, or source FPS.
- Whether the user expects proof before full render.

## Agent Routing Table

Use this routing table when several skills could apply:

- User gives rough idea only: start with `video-intake-and-storyboard`.
- User gives a reference final frame: intake first, then `motion-design-systems`, then `hyperframes-scene-builder`.
- User says a scene must start from another scene: use `scene-continuity-and-transitions`.
- User provides raw screen recording: use `product-demo-integration`.
- User says captions are late or too big: use `captions-and-music-bed`.
- User says narration changed: use `audio-sync-assembly`.
- User says "everything is perfect except": use `render-qa-and-surgical-changes`.

## Implementation Order

Use this order for multi-scene work:

1. Lock approved scenes.
2. Prepare scene specs.
3. Build or revise scene sources.
4. Render scene drafts.
5. Extract proof frames.
6. Build narration-only assembly.
7. Align captions.
8. Burn captions.
9. Build music bed.
10. Mix final audio.
11. Export final MP4.
12. Generate proof sheet and preview clips.

## What To Ask The User

Ask only questions that change implementation:

- Which final frame should match the reference if multiple references exist.
- Whether to crop or preserve a product recording when both have tradeoffs.
- Whether caption style is approved before burning a long final.
- Whether music should be audible during narration pauses.
- Whether a requested edit may change approved timing.
- Whether branded logos may be recolored.

Do not ask questions discoverable from files:

- Clip durations.
- Existing scene names.
- Current frame rate.
- Which source files contain a visible label.
- Whether an audio stream exists.

## Quality Gate

Do not call a full video done until:

- Final duration is known.
- Final resolution and FPS are known.
- Audio stream exists.
- Captions are present if requested.
- Scene boundary proofs exist.
- Exact user-requested timestamp proofs exist.
- Music ending behavior is checked.
- Any subjective preview requested by the user was shown or explicitly skipped.

## Handoff Format

When finishing, report:

- Final render path.
- Important scene/render paths.
- Commands or scripts used.
- Proof frame or preview paths.
- Tests performed.
- Anything not verified.
