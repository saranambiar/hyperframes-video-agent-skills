# Minimal Launch Scene Example

This is a synthetic example for testing the skills and scripts in this repository. It does not include private footage, narration, logos, or client-specific visual language.

## Files

- `scene-spec.md`: one filled scene spec.
- `timeline-manifest.json`: sample two-scene timeline for `timeline_manifest_to_ffmpeg.py`.
- `caption-events.json`: sample caption events for `build_ass_captions.py`.
- `change-request.md`: sample surgical edit request.

## Try It

```powershell
python ..\..\scripts\timeline_manifest_to_ffmpeg.py timeline-manifest.json
python ..\..\scripts\build_ass_captions.py --input caption-events.json --output sample.ass --style-template ..\..\templates\caption-style.ass
```

