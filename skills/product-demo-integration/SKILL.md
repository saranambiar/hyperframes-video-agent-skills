---
name: product-demo-integration
description: Integrate raw product demo recordings into agent-created videos, including crop decisions, zoom preservation, camera swipe transitions, UI readability checks, and timing around narration. Use when a user provides screen recordings, product walkthrough clips, SaaS demos, app footage, browser recordings, or asks to transition into/out of product demo footage.
---

# Product Demo Integration

Use this skill when product footage is part of the final video.

## Intake

Before editing:

- Probe recording duration, resolution, frame rate, and audio.
- Identify whether the recording includes a canvas, browser frame, cursor, zooms, scrolls, or dead time.
- Identify required product moments and their timestamps.
- Identify narration phrases that must align with product states.
- Ask for approval before aggressive crop if important UI may be cut off.

## Crop Decision

Default to preserving UI over removing background canvas.

Use crop only when:

- The important UI remains visible throughout zooms and scrolls.
- The crop does not cut off headings, labels, cursor context, or final state.
- A proof frame confirms the tightest zoom still works.

Use no-crop or light crop when:

- The recording zooms into different areas.
- The product moment moves around the canvas.
- The user already says cropped output cut off key text.

Read `references/crop-and-zoom.md` for a checklist.

## Transition Into Product Footage

- Start from the previous scene final frame.
- Use camera swipe or push motion rather than a hard cut if continuity is requested.
- Land on the current first frame of the product recording.
- If the recording starts with dead time, trim it only if doing so does not break sync.
- If a product moment must align with narration, retime the segment before that moment rather than changing all later sync.

## Transition Out

- Preserve the last meaningful product state long enough for the viewer to register it.
- Create a camera swipe to the next scene if requested.
- Avoid accidental blank frames at the end of screen recordings.
- Extract a proof frame at the transition boundary.

## QA

- Check first product frame.
- Check every zoom peak.
- Check every required product state.
- Check transition in/out.
- Confirm captions do not cover product UI.

## Output

Return:

- Source recording used.
- Crop/no-crop decision.
- Trim/retime segments.
- Render path.
- Proof frames for tightest crop and key product moments.

## Product Moment Map

Create a moment map before editing:

- Recording timestamp.
- What is visible.
- Narration phrase.
- Desired global timestamp.
- Whether cursor matters.
- Whether scroll position matters.
- Whether captions overlap.
- Whether crop is safe.

Use this map to decide trims and retiming.

## Crop Decision Matrix

Choose no crop when:

- The user accepts canvas/background.
- Zooms move across the screen.
- Main text is cut by a tight crop.
- The product state is more important than polish.

Choose light crop when:

- Canvas is distracting but UI stays centered.
- Captions need more room.
- Browser chrome or dead margin can be removed safely.

Choose dynamic crop only when:

- Each crop rectangle is mapped.
- The movement feels intentional.
- All key product states have proof frames.

## Narration Sync

Sync product states to spoken phrases:

- Start transition before the phrase if the product must be visible on the phrase.
- Let final product frame hold after the phrase if comprehension matters.
- Slow pre-moment footage rather than speeding a product scroll unnaturally.
- Do not cut mid-word in narration to reach a product state.

## Screen Recording Cleanup

Check:

- Cursor visibility.
- Browser UI.
- Notification popups.
- Dead time.
- Blank loading screens.
- Accidental desktop edges.
- Scroll speed.
- Zoom focus.

Only remove or hide these if it does not harm product clarity.

## Caption Safety

If captions are burned in:

- Check bottom nav bars.
- Check product tables.
- Check modal buttons.
- Check timeline controls.
- Move caption margin or choose a different proof frame if needed.

## User Approval Points

Ask before:

- Cropping out visible canvas.
- Removing cursor.
- Speeding footage dramatically.
- Blurring or masking product details.
- Replacing real footage with recreated UI.

## Handoff Format

Report:

- Product clip used.
- Crop strategy.
- Trim points.
- Retime ratios.
- Key proof frames.
- Any UI that remains imperfect by design.
