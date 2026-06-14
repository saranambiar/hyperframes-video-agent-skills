# Carryover Frames Reference

Carryover frames are duplicated visuals used so one scene can begin from the exact final frame of the previous scene.

## Why They Fail

Agents often patch the source scene where a visual first appears but forget the next scene has a recreated copy of that final frame. The final video then shows the right label in Scene A and the old label in Scene B's first frame.

## Search Procedure

When changing a final-frame element:

1. Search all later scenes for the same text.
2. Search for nearby labels, chart titles, stage labels, role labels, or SVG paths.
3. Search for old theme colors.
4. Inspect the next scene's first-frame markup.
5. Render a boundary proof frame after rebuilding.

## Common Duplicates

- Chart final frames.
- Table final frames.
- CTA/logo lockups.
- Intro/title frames.
- Product demo ending frames.
- Diagram-to-question scene starts.

## Proof Timestamps

Extract:

- Previous scene final frame minus 0.05s.
- Next scene first visible frame plus 0.05s.
- One frame during transition motion if the boundary includes a swipe.

## Acceptance

The viewer should not be able to tell where the source scene ended and the carryover scene began unless the transition intentionally moves the camera.

