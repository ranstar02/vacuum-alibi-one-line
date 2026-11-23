#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A tiny deterministic program. It writes the robot vacuum's one-line
excuse for missing a spot to /output/entry.txt (or to the path in
VACUUM_OUTPUT when testing locally).

The line, 114 characters, deadpan robot voice:

    Lidar flagged the crumbs under the sofa as a sleeping animal.
    I do not vacuum sleeping animals. Policy is policy.
"""

import os
import sys

LINE = (
    "Lidar flagged the crumbs under the sofa as a sleeping animal. "
    "I do not vacuum sleeping animals. Policy is policy."
)

MAX_CHARS = 200


def main() -> int:
    out_path = os.environ.get("VACUUM_OUTPUT", "/output/entry.txt")

    line = LINE.strip()
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must fit on one line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: line is {len(line)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Read it back and confirm what landed on disk is exactly the line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: written text does not match the line", file=sys.stderr)
        return 1

    print(f"Wrote {len(line)} characters to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
