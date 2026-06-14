# FFmpeg Retiming Reference

Use these patterns when building timeline assembly scripts.

## Whole Scene Retiming

```text
[0:v]setpts=RATIO*PTS,fps=60,scale=1920:1080:flags=lanczos,setsar=1,format=yuv420p[v]
```

Where:

```text
RATIO = target_duration / source_duration
```

## Segment Retiming

```text
[0:v]trim=start=0:end=4,setpts=1.25*(PTS-STARTPTS)[v0];
[0:v]trim=start=4:end=10,setpts=0.90*(PTS-STARTPTS)[v1];
[v0][v1]concat=n=2:v=1:a=0[v]
```

Use this when specific visual cues need to land on exact narration phrases.

## Hold Frame For Pause

```text
[0:v]trim=start=4:end=4.041667,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1.5,trim=duration=1.5[vhold]
```

Use hold frames for silence or deliberate pause instead of stretching all motion.

## Audio Tempo Fit

```text
[1:a]atempo=1.015,apad,atrim=duration=22.648[a]
```

Use small tempo changes only when preserving an approved timeline is more important than raw audio duration.

## Concatenation

```text
[v0][v1][v2]concat=n=3:v=1:a=0[v]
[a0][s0][a1]concat=n=3:v=0:a=1[a]
```

Keep audio and video timelines explicit. Do not rely on implicit mux behavior for complex edits.

