---
name: captions-and-music-bed
description: Generate, style, preview, and burn captions, and build music/percussion beds with ducking, loop/tail selection, fade-outs, and final silence. Use when captions are requested, captions are out of sync, subtitle style needs approval, background music competes with voiceover, or music must start/end at exact moments.
---

# Captions And Music Bed

Use this skill after the narration timeline is stable.

## Captions

Caption source rules:

- Use the user's script as wording source.
- Use the final narration-only master as timing source.
- Preserve punctuation and capitalization.
- Show one caption line at a time.
- Start the caption when the first word is spoken.
- Avoid captions over silent hooks or silent CTA holds unless requested.

Preview style before burning the full video when style changes.

Read `references/caption-rules.md` for timing and style guidance.

## Caption Style Defaults

- Bottom center.
- White text.
- Translucent dark backing.
- Generous bottom margin.
- Font size small enough not to dominate UI.
- One line only; split long sentences into natural phrase chunks.

Use `templates/caption-style.ass` as a starter.

## Music Bed

Music source rules:

- Start from a chosen offset when the intro of the source track is weak.
- Keep hook music audible if there is no voiceover.
- Duck under narration.
- Do not raise music during later narration pauses if the user says it is distracting.
- End music at the requested time, including final silence if requested.
- If the music source ends early, restart from a musically useful tail section.

Read `references/music-ducking.md` for FFmpeg patterns.

## QA

- Listen to start, middle, and final tail.
- Check music is present and audible, not merely technically in the stream.
- Confirm no clipped narration.
- Confirm captions are not late by several words.
- Extract a caption proof frame from a visually busy scene.
- Probe final audio stream.

## Output

Return:

- Caption file path.
- Caption preview frame.
- Music bed strategy.
- Final mixed video path.
- Audio/caption checks performed.

