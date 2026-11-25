#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line - entry program.

Writes our one-line review of a doorstop to /output/entry.txt.
The text is validated first (non-empty, single line, at most 200
characters, UTF-8) so a bad line never reaches the output file.
Python standard library only; no third-party imports.
"""
import os

ENTRY = (
    "The doorstop: a wedge of rubber whose whole career is standing still "
    "\u2014 and yet it is the only thing in this house that has never once "
    "called in sick."
)


def validate(text):
    """Check the entry line is safe to write: non-empty, one line, short, UTF-8."""
    if not text:
        raise ValueError("entry text is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > 200:
        raise ValueError("entry text is over 200 characters")
    text.encode("utf-8")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
