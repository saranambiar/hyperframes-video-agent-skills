#!/usr/bin/env python3
"""Scan text source files for color values outside an allowed token list."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


COLOR_RE = re.compile(
    r"(?P<hex>#[0-9A-Fa-f]{3,8}\b)|"
    r"(?P<func>\b(?:rgb|rgba|hsl|hsla)\([^)]*\))"
)

DEFAULT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".svg",
    ".json",
    ".md",
}

SKIP_DIRS = {"node_modules", ".git", "renders", "snapshots", "assembly", "dist", "build"}


def iter_files(root: Path, extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in extensions:
            files.append(path)
    return files


def normalize(value: str) -> str:
    return re.sub(r"\s+", "", value).lower()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Directory to scan")
    parser.add_argument("--allow", action="append", default=[], help="Allowed color value. Repeatable.")
    parser.add_argument("--extensions", default=",".join(sorted(DEFAULT_EXTENSIONS)), help="Comma-separated extensions")
    parser.add_argument("--show-allowed", action="store_true", help="Print allowed colors too")
    args = parser.parse_args()

    extensions = {ext if ext.startswith(".") else f".{ext}" for ext in args.extensions.split(",") if ext}
    allowed = {normalize(value) for value in args.allow}
    findings: list[str] = []
    for path in iter_files(args.root, extensions):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            for match in COLOR_RE.finditer(line):
                color = match.group(0)
                is_allowed = normalize(color) in allowed
                if is_allowed and not args.show_allowed:
                    continue
                status = "allowed" if is_allowed else "review"
                findings.append(f"{path}:{lineno}: {status}: {color}")
    for finding in findings:
        print(finding)
    if any(": review:" in finding for finding in findings):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

