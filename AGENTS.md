# Agent Instructions

This repository is for coding agents that create and edit videos with tools such as HyperFrames, FFmpeg, GSAP, browser rendering, and caption pipelines.

## Operating Rules

- Classify the task before acting: intake, scene build, motion design, continuity, product demo, audio sync, captions/music, QA, or surgical change.
- Load only the relevant skill and reference files.
- Prefer deterministic scripts for FFmpeg, caption, proof-frame, and theme-scan work.
- Ask for confirmation before full expensive renders when the user has not approved style, music, caption appearance, crop, or final-frame composition.
- Never mutate approved scenes unless the user explicitly asks for that scene to change.
- For final video edits, re-render only affected scenes, rebuild the assembly, and extract proof frames at exact timestamps.
- Keep private project assets out of this repository.

## Expected Workflow

1. Convert the request into a concrete spec using `templates/`.
2. Identify which skills apply.
3. Create or edit source artifacts.
4. Render previews or proof frames.
5. Verify with scripts before reporting success.
6. Document assumptions in the final response.

## Safety Checks

- Use `ffprobe` before and after retiming or assembly.
- Extract proof frames around any scene boundary or changed timestamp.
- Make contact sheets for multi-scene visual QA.
- Search source compositions for stale brand colors after theme changes.
- Check carryover frames when a previous scene's final frame changes.
- Confirm captions appear on the first spoken word, not several words late.
- Confirm music is audible where intended and ends at the requested time.

## Repository Boundaries

This is not an official HyperFrames or HeyGen repository. Do not present it as one.

Do not copy HyperFrames internals or official docs into this repo. Link or reference official projects where appropriate, and keep this repository focused on production workflows, reusable skills, and agent-operable utilities.

