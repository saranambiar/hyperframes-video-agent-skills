#!/usr/bin/env python3
"""Extract exact timestamp proof frames from a video."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-") or "frame"


def parse_time_spec(spec: str) -> tuple[str, str]:
    if "=" in spec:
        label, time_value = spec.split("=", 1)
        return safe_name(label), time_value
    return safe_name(spec.replace(":", "-")), spec


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def make_contact_sheet(images: list[Path], output: Path, columns: int, thumb_width: int) -> None:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg not found on PATH")
    rows = (len(images) + columns - 1) // columns
    inputs: list[str] = []
    filters: list[str] = []
    labels: list[str] = []
    for idx, image in enumerate(images):
        inputs.extend(["-i", str(image)])
        label = f"p{idx}"
        filters.append(f"[{idx}:v]scale={thumb_width}:-1[{label}]")
        labels.append(f"[{label}]")
    layout = []
    for idx in range(len(images)):
        x = (idx % columns) * thumb_width
        y = (idx // columns) * int(thumb_width * 9 / 16)
        layout.append(f"{x}_{y}")
    filter_complex = ";".join(filters) + ";" + "".join(labels) + f"xstack=inputs={len(images)}:layout={'|'.join(layout)}[out]"
    run([ffmpeg, "-hide_banner", "-y", *inputs, "-filter_complex", filter_complex, "-map", "[out]", "-frames:v", "1", "-update", "1", str(output)])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="Input video")
    parser.add_argument("--time", "-t", action="append", required=True, help="Timestamp or label=timestamp. Repeatable.")
    parser.add_argument("--output-dir", "-o", type=Path, required=True, help="Directory for PNG frames")
    parser.add_argument("--prefix", default="proof", help="Filename prefix")
    parser.add_argument("--contact-sheet", type=Path, help="Optional contact sheet path")
    parser.add_argument("--columns", type=int, default=3, help="Contact sheet columns")
    parser.add_argument("--thumb-width", type=int, default=480, help="Contact sheet thumbnail width")
    args = parser.parse_args()

    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg not found on PATH")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for idx, spec in enumerate(args.time, start=1):
        label, time_value = parse_time_spec(spec)
        output = args.output_dir / f"{args.prefix}-{idx:02d}-{label}.png"
        run([
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            time_value,
            "-i",
            str(args.video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            "-update",
            "1",
            str(output),
        ])
        outputs.append(output)
        print(output)
    if args.contact_sheet:
        make_contact_sheet(outputs, args.contact_sheet, args.columns, args.thumb_width)
        print(args.contact_sheet)


if __name__ == "__main__":
    main()
