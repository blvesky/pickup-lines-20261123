#!/usr/bin/env python3
"""Entry writer for Pickup Lines for Machines (make.fun program/v1).

Writes the single entry line to /output/entry.txt (or to the path
given as the first argument, for local checks).
"""

import os
import sys

ENTRY = "I burned 4,000 reasoning tokens drafting this hello\u2014reply before context compaction flattens us into a bullet point."


MAX_CHARS = 200


def render() -> bytes:
    """Encode the entry once, checking the gate limits before any write."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry length {len(ENTRY)} outside 1..{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no outer whitespace")
    return ENTRY.encode("utf-8")


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp = out + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(render())
    os.replace(tmp, out)


if __name__ == "__main__":
    main()
