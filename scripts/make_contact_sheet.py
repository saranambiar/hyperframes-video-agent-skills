#!/usr/bin/env python3
"""Create a contact sheet from proof-frame images using ffmpeg."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def collect_images(args: argparse.Namespace) -> list[Path]:
    images = [Path(p) for p in args.images]
    if args.dir:
        images.extend(sorted(args.dir.glob(args.glob)))
    images = [p for p in images if p.exists()]
    if not images:
        raise SystemExit("No input images found")
    return images


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="*", type=Path, help="Image files")
    parser.add_argument("--dir", type=Path, help="Directory to scan for images")
    parser.add_argument("--glob", default="*.png", help="Glob used with --dir")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Output image")
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--thumb-width", type=int, default=480)
    args = parser.parse_args()

    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg not found on PATH")
    images = collect_images(args)
    inputs: list[str] = []
    filters: list[str] = []
    labels: list[str] = []
    row_height = int(args.thumb_width * 9 / 16)
    layout = []
    for idx, image in enumerate(images):
        inputs.extend(["-i", str(image)])
        label = f"p{idx}"
        filters.append(f"[{idx}:v]scale={args.thumb_width}:-1[{label}]")
        labels.append(f"[{label}]")
        layout.append(f"{(idx % args.columns) * args.thumb_width}_{(idx // args.columns) * row_height}")
    filter_complex = ";".join(filters) + ";" + "".join(labels) + f"xstack=inputs={len(images)}:layout={'|'.join(layout)}[out]"
    subprocess.run(
        [ffmpeg, "-hide_banner", "-y", *inputs, "-filter_complex", filter_complex, "-map", "[out]", "-frames:v", "1", "-update", "1", str(args.output)],
        check=True,
    )
    print(args.output)


if __name__ == "__main__":
    main()
