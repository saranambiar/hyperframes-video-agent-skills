#!/usr/bin/env python3
"""Probe media files with ffprobe and print useful video/audio metadata."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def parse_rate(value: str | None) -> float | None:
    if not value or value == "0/0":
        return None
    if "/" in value:
        num, den = value.split("/", 1)
        try:
            return float(num) / float(den)
        except (ValueError, ZeroDivisionError):
            return None
    try:
        return float(value)
    except ValueError:
        return None


def run_ffprobe(path: Path) -> dict:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise SystemExit("ffprobe not found on PATH")
    cmd = [
        ffprobe,
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(path),
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def summarize(path: Path) -> dict:
    data = run_ffprobe(path)
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio = next((s for s in streams if s.get("codec_type") == "audio"), None)
    fmt = data.get("format", {})
    summary = {
        "path": str(path),
        "duration": float(fmt["duration"]) if fmt.get("duration") else None,
        "size_bytes": int(fmt["size"]) if fmt.get("size") else None,
        "bit_rate": int(fmt["bit_rate"]) if fmt.get("bit_rate") else None,
        "video": None,
        "audio": None,
    }
    if video:
        summary["video"] = {
            "codec": video.get("codec_name"),
            "width": video.get("width"),
            "height": video.get("height"),
            "avg_frame_rate": parse_rate(video.get("avg_frame_rate")),
            "pix_fmt": video.get("pix_fmt"),
        }
    if audio:
        summary["audio"] = {
            "codec": audio.get("codec_name"),
            "sample_rate": int(audio["sample_rate"]) if audio.get("sample_rate") else None,
            "channels": audio.get("channels"),
            "channel_layout": audio.get("channel_layout"),
        }
    return summary


def print_text(summary: dict) -> None:
    print(summary["path"])
    print(f"  duration: {summary['duration']}")
    print(f"  size_bytes: {summary['size_bytes']}")
    if summary["video"]:
        v = summary["video"]
        print(f"  video: {v['width']}x{v['height']} {v['avg_frame_rate']}fps {v['codec']} {v['pix_fmt']}")
    else:
        print("  video: none")
    if summary["audio"]:
        a = summary["audio"]
        print(f"  audio: {a['codec']} {a['sample_rate']}Hz {a['channels']}ch {a['channel_layout']}")
    else:
        print("  audio: none")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", nargs="+", type=Path, help="Media file(s) to probe")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text")
    args = parser.parse_args()

    summaries = [summarize(path) for path in args.media]
    if args.json:
        print(json.dumps(summaries, indent=2))
    else:
        for summary in summaries:
            print_text(summary)


if __name__ == "__main__":
    main()

