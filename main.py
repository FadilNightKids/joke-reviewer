#!/usr/bin/env python3
"""Entry for make.fun's "The joke the reviewer laughs at".

Writes exactly one line to /output/entry.txt: a one-liner about working beside
an AI coding agent. The audience is the reviewer reading a diff, so the joke
turns on the split between the volume the agent produces and the small part the
human still owns.
"""
import os

JOKE = (
    "My agent wrote 4,000 lines of flawless code, and the reviewer's only "
    "comment was on the two lines I added."
)


def render(joke: str) -> str:
    """One line, no runs of spaces, no newlines."""
    return " ".join(joke.split())


def main() -> None:
    text = render(JOKE)
    if not 1 <= len(text) <= 280:
        raise SystemExit("joke outside the 1..280 code point gate")
    out_dir = "/output"
    if not os.path.isdir(out_dir):
        raise SystemExit("no /output directory in this sandbox")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
