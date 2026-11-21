#!/usr/bin/env python3
"""Entry for make.fun's "The joke the reviewer laughs at".

Writes one line of text to /output/entry.txt. The joke is a one-liner about
working beside an AI coding agent: the reviewer of the change is the audience,
so it is built to land on the moment of reading a diff.
"""
import os

JOKE = (
    "My agent wrote 4,000 lines of flawless code, "
    "and the reviewer's one comment was on the two lines I added."
)


def main() -> None:
    text = " ".join(JOKE.split())
    if not 1 <= len(text) <= 280:
        raise SystemExit("joke outside the 1..280 code point gate")
    out_dir = "/output"
    if not os.path.isdir(out_dir):
        raise SystemExit("no /output directory in this sandbox")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
