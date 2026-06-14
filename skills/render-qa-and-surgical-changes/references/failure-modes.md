# Video QA Failure Modes

## Visual

- Scene starts from an old carryover frame.
- A new chart label exists in one scene but disappears in the next.
- Theme changes miss inline SVG `fill` or `stroke` values.
- Product demo crop cuts off zoomed UI.
- Final frame is blank because a recording had dead time.
- Caption box covers important product controls or chart labels.

## Audio

- Replacement narration shifts downstream sync.
- Audio is technically present but too quiet to hear.
- Music ends before the video ending.
- Music tail restarts but final beat is clipped.
- Ducking pumps too loudly during narration pauses.
- Words are clipped by aggressive trims.

## Captions

- Captions start several words late.
- Caption chunks invent punctuation not in the script.
- Captions wrap to two lines and cover UI.
- Silent hooks or CTA screens get unwanted captions.

## Regression Checks

- Probe final file before and after.
- Extract exact timestamp proof frames.
- Compare boundary frames around changed scenes.
- Search all scene files for changed labels and stale colors.
- Keep generated proof outputs outside version control unless they are public examples.

