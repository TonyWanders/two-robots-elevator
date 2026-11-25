#!/usr/bin/env python3
"""Write one line of awkward robot elevator small talk to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The line is a fixed
string. resolve_output_path() picks where it goes, validate_entry()
enforces the competition gate, and write_entry() writes it.
"""

import os
import sys
from pathlib import Path

# Make sibling imports resolve from this file's directory even when the
# grader runs with -P -s from elsewhere and the repo is read-only.
sys.path.insert(0, str(Path(__file__).resolve().parent))

LINE = ("So... do you also pretend to scan for updates when the doors close, "
        "or is that just me avoiding eye contact I do not have?")

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_PATH = "/output/entry.txt"


def resolve_output_path() -> Path:
    """Pick the output path: argv[1], then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    env_path = os.environ.get("OUTPUT_PATH")
    if env_path:
        return Path(env_path)
    return Path(DEFAULT_PATH)


def validate_entry(text: str) -> int:
    """Enforce the competition gate: 1 to 200 chars, not only white space.

    Returns the character count. Raises ValueError when the gate fails.
    """
    chars = len(text)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        raise ValueError(f"line is {chars} characters, outside 1-200")
    if not text.strip():
        raise ValueError("line is only white space")
    return chars


def write_entry(path: Path, text: str) -> None:
    """Write the entry text to path, creating its parent directory."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    try:
        chars = validate_entry(LINE)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    path = resolve_output_path()
    write_entry(path, LINE)
    print(f"wrote {chars} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
