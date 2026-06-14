---
name: render-qa-and-surgical-changes
description: Verify final video renders and make tiny safe edits without breaking approved sync, including proof frames, contact sheets, media probing, stale theme scans, exact timestamp checks, carryover-frame refreshes, and re-render-only-affected-scenes workflows. Use when a user asks for final QA, HD/render verification, a small text/audio/color change, or regression checks after approved timing.
---

# Render QA And Surgical Changes

Use this skill when the video is nearly done or already approved and changes must be controlled.

## Surgical Edit Rules

- Patch source artifacts, not the final MP4, when source scenes and assembly scripts exist.
- Re-render only affected scene(s).
- Rebuild the final assembly from the current approved timeline.
- Do not redesign, retime, or re-sync unrelated sections.
- Search for duplicated/carryover frames before declaring done.
- Extract proof frames at exact timestamps requested by the user.

Use `templates/change-request.md` before implementing a final tiny change.

## QA Sequence

1. Probe the final render.
   - Duration.
   - Resolution.
   - Frame rate.
   - Audio stream.
   - Sample rate and channels.

2. Extract proof frames.
   - Scene boundaries.
   - Changed timestamps.
   - Caption style frames.
   - Final CTA or ending frame.

3. Build a contact sheet.
   - Include all risky timestamps.
   - Include before/after frames for surgical changes.

4. Check audio.
   - Narration present.
   - Music bed audible where intended.
   - Final silence or fade timing correct.
   - No clipped words after trims.

5. Check theme and text.
   - Search for stale colors.
   - Search duplicated labels in carryover scenes.
   - Verify logos and product footage were not recolored accidentally.

Read `references/failure-modes.md` for common regressions.

## Scripts

Use repo scripts when available:

- `scripts/probe_media.py`
- `scripts/extract_proof_frames.py`
- `scripts/make_contact_sheet.py`
- `scripts/build_ass_captions.py`
- `scripts/scan_theme_colors.py`
- `scripts/timeline_manifest_to_ffmpeg.py`

## Acceptance

Report:

- Final video path.
- Probe summary.
- Proof frame/contact sheet paths.
- Files changed.
- Exact checks performed.
- Any unverified subjective item.

## Exact Timestamp Checks

When the user names a timestamp:

- Extract a frame at that exact time.
- Extract one frame slightly before if appearance timing matters.
- Extract one frame slightly after if disappearance timing matters.
- Inspect the rendered final, not only the source scene.
- If the same visual appears in the next scene, extract the boundary frame too.

## Source Search Checklist

Before patching:

- Search all source scene files for the text or color.
- Search assembly scripts for audio paths and durations.
- Search caption scripts for old wording.
- Search templates/examples only if public repo docs need updating.
- Ignore generated renders unless doing visual QA.

## Safe Audio Replacement

For replacing one narration clip:

- Probe old clip duration.
- Probe new clip duration.
- If same duration, replace path and rebuild.
- If slightly different, decide whether to tempo-fit or retime visuals.
- Confirm no downstream scene start moves unless requested.
- Regenerate captions if spoken wording changed.

## Safe Text Replacement

For replacing visible text:

- Patch source scene.
- Search next scene for carryover copy.
- Search old captions if spoken wording changed.
- Re-render affected scene.
- Rebuild final.
- Extract proof frames at visible times.

## Safe Theme Replacement

For color cleanup:

- Use a theme scanner.
- Patch editable source only.
- Do not recolor logos.
- Do not recolor product-demo recordings.
- Check SVG values.
- Check next-scene carryovers.

## QA Output Bundle

Produce:

- `probe.txt` or console summary.
- `proof-*.png`.
- `contact-sheet.jpg`.
- `preview-*.mp4` for moving sync checks.
- final render path.

Generated QA files do not need to be committed unless they are public examples.

## Stop Conditions

Stop and ask if:

- The requested change conflicts with locked scene approval.
- The source asset for the visible final frame cannot be found.
- A text/audio change implies a script change the user has not approved.
- A logo recolor is requested but brand ownership is unclear.

Otherwise make the smallest safe change and verify it.
