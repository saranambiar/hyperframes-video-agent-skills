#!/usr/bin/env python3
"""Convert a timeline manifest into an FFmpeg-oriented assembly plan."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def ratio(target: float, source: float) -> float:
    if source <= 0:
        raise ValueError("source duration must be positive")
    return target / source


def build_plan(manifest: dict) -> list[str]:
    project = manifest.get("project", {})
    fps = project.get("fps", 60)
    width = project.get("width", 1920)
    height = project.get("height", 1080)
    lines = [
        f"Project: {project.get('name', 'video')}",
        f"Output: {project.get('output', 'renders/final.mp4')}",
        f"Normalize: {width}x{height} @ {fps}fps",
        "",
        "Segments:",
    ]
    cursor = 0.0
    for segment in manifest.get("segments", []):
        sid = segment["id"]
        target = float(segment["target_duration"])
        source = float(segment.get("source_duration", target))
        strategy = segment.get("strategy", "retime-to-audio")
        lines.append(f"- {sid}: {strategy}, start={cursor:.3f}, duration={target:.3f}")
        if strategy == "retime-to-audio":
            lines.append(f"  setpts={ratio(target, source):.6f}*PTS")
        elif strategy == "segment-map":
            for item in segment.get("maps", []):
                if "hold_source_time" in item:
                    lines.append(f"  hold frame at {item['hold_source_time']}s for {item['target_duration']}s")
                else:
                    src_dur = float(item["source_end"]) - float(item["source_start"])
                    lines.append(
                        f"  trim {item['source_start']}..{item['source_end']} -> "
                        f"{item['target_duration']}s setpts={ratio(float(item['target_duration']), src_dur):.6f}*PTS"
                    )
        cursor += target
    lines.append("")
    lines.append(f"Total duration: {cursor:.3f}s")
    if manifest.get("captions"):
        lines.append(f"Captions: {manifest['captions'].get('output')}")
    if manifest.get("music"):
        music = manifest["music"]
        lines.append(f"Music: {music.get('file')} offset={music.get('start_offset', 0)} duck={music.get('duck_under_narration', False)}")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Timeline manifest JSON")
    parser.add_argument("--output-plan", type=Path, help="Write plan text to this file")
    parser.add_argument("--print-ffmpeg-path", action="store_true", help="Print detected ffmpeg path")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    lines = build_plan(manifest)
    text = "\n".join(lines) + "\n"
    if args.print_ffmpeg_path:
        text += f"ffmpeg: {shutil.which('ffmpeg') or 'not found'}\n"
    if args.output_plan:
        args.output_plan.parent.mkdir(parents=True, exist_ok=True)
        args.output_plan.write_text(text, encoding="utf-8")
        print(args.output_plan)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()

