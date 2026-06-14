# Full Video Production Workflow

Use this workflow when a user wants a complete video, not a single isolated edit.

## 1. Intake

- Read the prompt, assets, script, references, and existing renders.
- Fill `templates/storyboard.md`.
- Fill one `templates/scene-spec.md` per scene.
- Mark approved scenes as locked.
- Identify subjective decisions that require previews: caption style, music volume, crop, final frame, and major motion language.

## 2. Build Scenes

- Build each scene as a separate composition or source artifact.
- Prefer reusable components for repeated UI, charts, cards, labels, logos, and transitions.
- Make the final frame explicit and hold it long enough to inspect.
- If a later scene starts from a previous final frame, create or update the carryover frame in that later scene too.

## 3. Render Scene Drafts

- Render draft scene videos first.
- Extract proof frames for each scene's first frame, key beat, and final frame.
- Compare final frames to references before moving to assembly.

## 4. Sync Audio And Visuals

- Probe all narration audio durations.
- Build a timeline manifest with scene starts, target durations, pauses, and visual cue timestamps.
- Use segment retiming for scenes with important beat timing.
- Prefer hold frames over globally slowing all motion when only a pause is needed.

## 5. Captions And Music

- Build captions from the final narration timeline.
- Preview caption style on a busy frame before burning all captions.
- Mix music under narration with ducking.
- Check music is actually audible where intended and ends exactly where requested.

## 6. Final Assembly

- Assemble from source scene renders, not from a previously patched final MP4.
- Normalize resolution, frame rate, pixel format, and audio sample rate.
- Generate final MP4 plus preview clips around risky sections.

## 7. Validate

- Run `ffprobe` on the final.
- Extract proof frames at scene boundaries and requested exact timestamps.
- Make a contact sheet.
- Watch or preview risky transitions.
- Confirm captions begin on the first spoken word.
- Confirm no old scene or stale carryover frame remains.

