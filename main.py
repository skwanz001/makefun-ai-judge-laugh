#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt (1-200 UTF-8 chars, per the
competition gate). Standard library only: the grading sandbox installs
nothing.
"""

import os

LINE = "I fixed your bug in the first 10,000 tokens, then spent the next 90,000 apologizing for a bug I invented and confidently re-breaking the fix."


def main() -> None:
    # Gate mirror: the entry must be 1-200 UTF-8 characters, not only
    # whitespace. Refuse to write anything that would fail the gate.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
