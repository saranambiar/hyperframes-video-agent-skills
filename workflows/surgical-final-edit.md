# Surgical Final Edit Workflow

Use this workflow when the user says the final video is approved except for one or two small changes.

## Rules

- Do not redesign.
- Do not re-sync unless required by the change.
- Do not regenerate unaffected scenes.
- Do not patch an old final MP4 if source scene renders and assembly scripts exist.
- Always check duplicated/carryover frames.

## Steps

1. Fill `templates/change-request.md`.
2. Identify the smallest source artifact that owns the visible/audio change.
3. Search for duplicates of the changed text, visual, or frame in adjacent scenes.
4. Patch only affected source files.
5. Re-render only affected scene(s).
6. Rebuild the final assembly with existing timing.
7. Extract proof frames at exact requested timestamps and scene joins.
8. Probe final duration, frame rate, resolution, and audio stream.
9. Report the changed files, final output, and proof frames.

## Common Failure Modes

- Updating a chart in one scene but forgetting the next scene's carryover chart.
- Replacing narration with a slightly longer file and shifting all downstream sync.
- Changing a theme token but leaving stale colors inside SVG fills or duplicated HTML.
- Fixing captions without regenerating the burned video.
- Re-rendering too much and accidentally changing approved timing.

