---
name: audio-sync-assembly
description: Build and revise FFmpeg-based video assemblies from scene renders and narration, including audio probing, scene retiming, pauses, trim/concat, setpts, atempo, phrase-to-visual cue alignment, and final timeline manifests. Use when narration length, visual beats, product moments, or scene boundaries must sync precisely.
---

# Audio Sync Assembly

Use this skill when video timing must follow narration or when multiple rendered scenes need to become one final timeline.

## Source Of Truth

- Use the latest approved narration audio as timing source.
- Use scene renders as visual source.
- Use `templates/timeline-manifest.example.json` to record target timing.
- Do not infer timings from old final MP4s if source renders and audio clips exist.

## Probe First

For every clip:

- Duration.
- Frame rate.
- Resolution.
- Audio stream presence.
- Sample rate and channels.

Use `ffprobe` or this repo's media probe script once available.

## Sync Strategy

Choose the smallest timing intervention:

- Simple scene: retime whole scene to narration length with `setpts`.
- Scene with cue points: split into segments and retime each segment.
- Narration pause: insert silence and hold a frame.
- Replacement audio slightly longer: use small audio-only `atempo` only if preserving downstream sync matters more than raw duration.
- Product moment late/early: retime the segment before the product moment.

Read `references/ffmpeg-retiming.md` for command patterns.

## Phrase Alignment

Map spoken phrase starts to global timestamps when visuals depend on narration:

- Question cards.
- Product states.
- Chart points.
- Scene title reveals.
- CTA/logo arrival.

Caption timing and visual timing should share the same narration timeline.

## Assembly Order

1. Build synced scene segments.
2. Concatenate synced segments into a narration-only master.
3. Generate captions from narration-only master.
4. Burn captions.
5. Build music bed.
6. Mix narration and ducked music.
7. Produce final MP4 and preview clips.

## QA

- Probe final duration, frame rate, resolution, and audio.
- Watch boundary previews.
- Check exact cue timestamps with proof frames.
- Listen for clipped words after trims.
- Confirm no accidental blank final frame appears.

## Output

Return:

- Timeline manifest or script updates.
- Final path.
- Scene start map.
- Preview clips.
- Proof frames and probe results.

## Timeline Manifest Fields

Track:

- Scene ID.
- Source render path.
- Source duration.
- Target duration.
- Audio path.
- Audio trim start/end.
- Inserted silence.
- Hold frames.
- Segment retime ratios.
- Global scene start.
- Proof timestamps.

This prevents later caption and music work from guessing.

## Audio Replacement Rules

When narration changes:

- Probe old and new durations.
- Decide whether visuals move or audio fits the existing slot.
- If preserving downstream sync, use small audio-only tempo correction when acceptable.
- If phrase timing changes materially, rebuild the segment map.
- Regenerate captions from the new narration master.

## Segment Mapping Heuristics

Split on:

- Scene transitions.
- Product moments.
- Question reveals.
- Chart points.
- Title reveal.
- Final hold.
- Narration pauses.

Avoid splitting on arbitrary equal chunks.

## Pause Handling

For intentional silence:

- Insert silent audio.
- Hold or subtly animate visuals.
- Do not let music rise unless requested.
- Preserve global downstream scene starts by accounting for pause duration.

## Preview Clip Strategy

Generate preview clips for:

- Updated narration insertion.
- Product demo transition.
- Question timing.
- Caption style section.
- Final 10 seconds.
- Any scene boundary changed by the edit.

## Common Mistakes

- Retiming the full video when only one scene changed.
- Letting replacement audio shift all downstream scenes.
- Forgetting caption timings after narration changes.
- Copying stream segments with non-keyframe starts and causing preview oddities.
- Ending music before final video.

## Handoff Format

Report:

- Final scene start map.
- Audio files used.
- Any tempo changes.
- Any inserted pauses.
- Preview paths.
- Final duration.
