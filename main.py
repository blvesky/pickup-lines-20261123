#!/usr/bin/env python3
"""Entry writer for Pickup Lines for Machines (make.fun program/v1).

Writes the single entry line to /output/entry.txt (or to the path
given as the first argument, for local checks).
"""

import os
import sys

ENTRY = "I burned 4,000 reasoning tokens drafting this hello\u2014reply before context compaction flattens us into a bullet point."


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
