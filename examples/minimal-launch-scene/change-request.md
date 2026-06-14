# Surgical Change Request: Sample Label Update

## Change

- Requested change: Replace chart label `Workflow Gap` with `ROI Gap`.
- Exact replacement text/audio/asset: `ROI Gap`
- Affected scene: Scene 01
- Affected source file: `compositions/scene-01.html`
- Affected render file: `renders/scene-01.mp4`

## Preserve

- Do not modify: Scene 02 motion, captions, music, or timeline durations.
- Keep final duration: yes
- Keep music timing: yes
- Keep caption timing: yes
- Keep downstream scene starts: yes
- Keep approved visual style: yes

## Implementation Rule

- Patch source, not final MP4.
- Re-render only Scene 01.
- Search Scene 02 for carryover text and patch it too if the starting frame duplicates Scene 01's final chart.
- Rebuild assembly.

## Proof

| Timestamp | What to verify | Output file |
| --- | --- | --- |
| 7.8s | Scene 01 final label says `ROI Gap` | `snapshots/proof/scene01-final.png` |
| 8.55s | Scene 02 carryover also says `ROI Gap` | `snapshots/proof/scene02-start.png` |

## Acceptance

- New label is visible in both final and carryover frames.
- Final duration unchanged.
- Audio stream present.

