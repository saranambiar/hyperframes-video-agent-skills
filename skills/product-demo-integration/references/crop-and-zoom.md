# Crop And Zoom Reference

Use this before cropping product demo footage.

## Crop Safety Procedure

1. Extract frames at:
   - Start of recording.
   - Every zoom-in moment.
   - Every scroll landing.
   - Required product state.
   - Final frame.
2. Test the proposed crop on all frames.
3. Reject the crop if any critical text, cursor context, or UI control is cut off.
4. Prefer a slightly wider crop over a clean but unusable crop.

## Common Mistakes

- Cropping to the initial UI state while later zooms reveal a different area.
- Removing the canvas background but losing the main heading.
- Cutting off scroll-based product moments.
- Hiding a key UI state under captions.
- Trimming the first second and shifting all narration sync.

## Better Alternatives

- Keep full canvas and use a camera swipe transition.
- Add a subtle frame or soft background match instead of cropping.
- Use dynamic crop only when every crop rectangle is explicitly mapped.
- Slow the pre-product segment if a later product state must land on a narration phrase.

