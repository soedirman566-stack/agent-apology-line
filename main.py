#!/usr/bin/env python3
"""Entrypoint for 'The One-Sentence Apology Your Agent Owes You'.

Reads the apology line from line.txt, checks it against the competition
gate (UTF-8 text, 1 to 200 characters, not only whitespace), and writes
it to /output/entry.txt for the harness.
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
LINE_FILE = ROOT / "line.txt"
OUTPUT_FILE = pathlib.Path("/output/entry.txt")

MAX_CHARS = 200


def load_line() -> str:
    return LINE_FILE.read_text(encoding="utf-8").strip()


def main() -> int:
    line = load_line()
    if not line or not (1 <= len(line) <= MAX_CHARS):
        print(f"line fails the gate: {len(line)} characters", file=sys.stderr)
        return 1
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    # Round-trip check: what the judge reads must be the line, byte for byte.
    written = OUTPUT_FILE.read_text(encoding="utf-8")
    if written != line:
        print("written entry does not match line.txt", file=sys.stderr)
        return 1
    print(line)
    print(f"({len(line)} characters, gate 1-{MAX_CHARS})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
