# Audio And Caption Resync Workflow

Use this workflow when captions or visual beats are late, early, or out of sync with updated narration.

## 1. Establish Source Of Truth

- Treat the final mixed narration timeline as the caption timing source.
- Use the latest script text as the caption wording source.
- Use scene start times from the current assembly manifest.

## 2. Probe And Map

- Probe every narration clip duration.
- Identify pauses, trimmed sections, and replaced audio.
- Map phrase starts to global timestamps.
- Mark visual cue timestamps that must align with spoken words.

## 3. Caption Rules

- One caption line visible at a time.
- Preserve punctuation and capitalization from the provided script.
- Start each caption when the first word is spoken.
- Avoid captions during silent hooks or silent CTA holds unless explicitly requested.
- Preview the style before burning a full video if style changed.

## 4. Visual Sync Rules

- Use segment retiming when a scene has multiple cue points.
- Use hold frames for silence or deliberate pauses.
- Avoid slowing a whole scene when only one transition needs more time.
- Rebuild from scene segments and narration, not from manual edits to a final MP4.

## 5. Verification

- Extract proof frames at cue timestamps.
- Generate a short preview around each corrected section.
- Confirm final duration and frame rate remain expected.
- Listen for clipped words after audio trimming.

