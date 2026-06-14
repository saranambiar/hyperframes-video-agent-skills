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

## Caption Chunking Rules

Split captions by:

- Natural phrase boundaries.
- Breath points.
- Punctuation.
- Maximum line length.
- Visual complexity behind the caption.

Do not split in a way that changes meaning. Do not add punctuation that the script does not contain.

## Timing Sources

Preferred order:

1. Word-level alignment from final narration master.
2. Phrase timestamps from user or transcript.
3. Scene-level known timings plus manual phrase estimates.

Never time captions from an obsolete pre-edit audio file.

## Caption Preview Procedure

Before full burn-in:

- Pick a visually busy frame.
- Render one still with caption style.
- Show or inspect it.
- Adjust font size, backing opacity, margin, and width.
- Only then burn the full video.

## Music Bed Build Procedure

1. Probe source music duration.
2. Pick source start offset.
3. Decide hook volume.
4. Decide narration-bed volume.
5. Decide dense-explanation volume.
6. Decide whether pauses stay ducked.
7. Decide final CTA volume.
8. Decide music end timestamp.
9. Add fade out.
10. Mix with limiter.

## Music QA

Listen/check:

- First 5 seconds.
- First narration entry.
- Dense explanation section.
- Long pause.
- Tail restart.
- Final 5 seconds.

If music is "technically there" but inaudible, raise bed or reduce ducking threshold.

## Caption Failure Recovery

If captions are late:

- Check alignment source.
- Check whether silence/hook shifted global times.
- Start chunks at first word, not middle of phrase.
- Regenerate from final narration master.

If captions are too big:

- Reduce font size.
- Increase max characters slightly only if still one line.
- Lower backing opacity only if readable.

## Handoff Format

Report:

- Caption source script.
- Caption timing source.
- ASS file path.
- Music source and offset.
- Ducking strategy.
- Final silence duration.
