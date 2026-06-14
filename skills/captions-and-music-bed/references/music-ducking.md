# Music Ducking Reference

## Useful FFmpeg Pattern

```text
[0:a]aresample=48000,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,asplit=2[narr][side];
[1:a]aresample=48000,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[bed];
[bed][side]sidechaincompress=threshold=0.028:ratio=4:attack=18:release=260[ducked];
[narr][ducked]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.95[a]
```

## Volume Strategy

- Hook/no voiceover: music can be louder.
- Early narration: lower under voice.
- Dense explanation: lower further and do not pump back up during short pauses.
- Final silent CTA: music may rise if requested, then fade out before the requested silence.

## Tail Strategy

When source music ends before the video:

- Restart from a musically useful later section.
- Choose enough duration so the final beat is not clipped.
- Fade out gently.
- Leave requested final silence.

## Failure Modes

- Music stream exists but is inaudible.
- Music ends several seconds too early.
- Tail restart starts on an awkward transient.
- Narration is masked by music during dense explanation.
- Fade cuts off the final beat.

