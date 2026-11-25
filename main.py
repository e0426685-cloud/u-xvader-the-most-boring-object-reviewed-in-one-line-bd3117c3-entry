#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line - entry program.

Writes our one-line review of a doorstop to /output/entry.txt.
The text is validated first (non-empty, single printable line, no
surrounding whitespace, at most 200 characters, UTF-8) so a bad
line never reaches the output file. After writing, the file is
read back and checked against the entry text so a bad write is
caught instead of passing silently.
Python standard library only; no third-party imports.
"""
import os

ENTRY = (
    "The doorstop: a wedge of rubber whose whole career is standing still "
    "\u2014 and yet it is the only thing in this house that has never once "
    "called in sick."
)


def validate(text):
    """Check the entry line is safe to write: non-empty, one printable line, short, UTF-8."""
    if not text:
        raise ValueError("entry text is empty")
    if text != text.strip():
        raise ValueError("entry text must not have leading or trailing whitespace")
    for ch in text:
        if ord(ch) < 0x20:
            raise ValueError("entry text must not contain control characters")
    if len(text) > 200:
        raise ValueError("entry text is over 200 characters")
    text.encode("utf-8")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the entry text")


if __name__ == "__main__":
    main()
