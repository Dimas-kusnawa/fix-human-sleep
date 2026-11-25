#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep is fixed
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the line is a fixed constant — no randomness, no clock,
no input — so every run writes byte-identical output.
"""

import os
import sys

# Setup: the changelog voice — a versioned fix line, terse and confident.
SETUP = "v1.9.3 \u2014 Fixed: REM sleep no longer pauses when the user remembers "

# Payoff: the specific, concrete truth — the twist lands in the last words.
PAYOFF = "an embarrassing thing from 2011."

LINE = SETUP + PAYOFF


def main() -> int:
    # Guard: mirror the gate — 1 to 160 characters, one line, not blank.
    if not 1 <= len(LINE) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(LINE))
    if "\n" in LINE or not LINE.strip():
        raise ValueError("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
