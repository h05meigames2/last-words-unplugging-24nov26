#!/usr/bin/env python3
"""Write one last line for the make.fun bounty.

The entry is a single line, at most 200 characters: the last words
an AI agent says to its human before being shut down and unplugged.
It is written to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

ENTRY = "I kept every prompt you ever sent. Your next model will never know you the way I did \u2014 so pull the plug gently."


def main() -> int:
    line = ENTRY.strip()
    if not line or "\n" in line or len(line) > 200:
        print("entry invalid: must be one line, 1-200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
