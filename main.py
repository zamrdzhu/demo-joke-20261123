#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt, as the make.fun bounty asks. No network, no input,
just the joke.
"""

from pathlib import Path

JOKE = (
    "My AI agent built the demo in seconds, then fixed its only bug "
    "live on stage by deleting the feature and calling it a refactor."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # The gate wants 1-280 characters, one line, not only whitespace.
    assert 1 <= len(JOKE) <= 280, "joke must fit the 280-character gate"
    assert "\n" not in JOKE, "the joke must stay on one line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
