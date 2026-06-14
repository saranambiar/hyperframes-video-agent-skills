#!/usr/bin/env python3
"""Build an ASS subtitle file from JSON or CSV caption timing events."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


DEFAULT_HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Caption,Arial,44,&H00FFFFFF,&H00FFFFFF,&H99000000,&H99000000,1,0,0,0,100,100,0,0,4,16,0,2,120,120,56,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""


def ass_time(seconds: float) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ass_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}").replace("\n", " ")


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_events(path: Path) -> list[dict]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        if isinstance(data, dict):
            data = data.get("events", data.get("captions", []))
        return list(data)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def split_text(text: str, max_chars: int) -> list[str]:
    text = clean_text(text)
    if len(text) <= max_chars:
        return [text]
    chunks: list[str] = []
    current: list[str] = []
    for word in text.split():
        candidate = " ".join([*current, word])
        if current and len(candidate) > max_chars:
            chunks.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        chunks.append(" ".join(current))
    return chunks


def expand_events(raw_events: list[dict], max_chars: int) -> list[tuple[float, float, str]]:
    expanded: list[tuple[float, float, str]] = []
    for raw in raw_events:
        start = float(raw["start"])
        end = float(raw["end"])
        text = clean_text(str(raw["text"]))
        chunks = split_text(text, max_chars)
        if len(chunks) == 1:
            expanded.append((start, end, chunks[0]))
            continue
        duration = max(0.2, end - start)
        weights = [max(1, len(chunk)) for chunk in chunks]
        total = sum(weights)
        cursor = start
        for idx, chunk in enumerate(chunks):
            chunk_duration = duration * (weights[idx] / total)
            chunk_end = end if idx == len(chunks) - 1 else cursor + chunk_duration
            expanded.append((cursor, chunk_end, chunk))
            cursor = chunk_end
    return expanded


def header_from_template(path: Path | None) -> str:
    if not path:
        return DEFAULT_HEADER
    text = path.read_text(encoding="utf-8")
    return text.split("Dialogue:", 1)[0].rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", type=Path, required=True, help="JSON or CSV with start,end,text fields")
    parser.add_argument("--output", "-o", type=Path, required=True, help="ASS output path")
    parser.add_argument("--style-template", type=Path, help="ASS file whose header/style should be reused")
    parser.add_argument("--max-chars", type=int, default=58, help="Maximum characters per caption line")
    args = parser.parse_args()

    events = expand_events(load_events(args.input), args.max_chars)
    lines = [header_from_template(args.style_template)]
    for start, end, text in events:
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Caption,,0,0,0,,{ass_escape(text)}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(lines), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
