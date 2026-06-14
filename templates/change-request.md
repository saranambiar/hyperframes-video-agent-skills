# Surgical Change Request Template

Use this when the user wants a tiny final change after timing, captions, music, or scene design has already been approved.

## Change

- Requested change:
- Exact replacement text/audio/asset:
- Affected scene:
- Affected source file:
- Affected render file:

## Preserve

- Do not modify:
- Keep final duration:
- Keep music timing:
- Keep caption timing:
- Keep downstream scene starts:
- Keep approved visual style:

## Implementation Rule

- Patch source, not final MP4, unless the change is explicitly post-production only.
- Re-render only affected scene(s).
- Rebuild assembly from current approved script.
- Refresh any carryover frame or starting frame that duplicates the changed visual.

## Proof

| Timestamp | What to verify | Output file |
| --- | --- | --- |
|  |  |  |

## Acceptance

- User-visible change is present.
- No unrelated scene visual changed.
- Final duration remains within tolerance.
- Audio stream exists and sync did not drift.

