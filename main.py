#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes one original out-of-office auto-reply line (a single sentence,
146 characters) to /output/entry.txt.

The line is painfully honest about the sender's inbox triage — emails are
answered in the order the sender feels brave enough to face them, not in
the order they arrived — while staying warm and professional enough that a
manager would let it stand. One sentence, no cramming, no trailing off.
"""

import os
import sys

LINE = (
    "I'm away until Monday. Your email will be read, sighed at, and "
    "answered in the order I feel brave enough to face it \u2014 "
    "thank you for your patience."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE.strip()
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    if not (1 <= len(text) <= 200):
        print(f"error: entry is {len(text)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry is only white space", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
