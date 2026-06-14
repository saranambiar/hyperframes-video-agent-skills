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

