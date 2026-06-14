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

