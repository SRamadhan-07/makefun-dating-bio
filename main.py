#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App - a make.fun entry.

Running this program writes the entry text to /output/entry.txt
(or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).
The bio is written exactly as-is, in one line, with no trailing newline:
the sealed gate accepts 1 to 180 characters, and this bio is 164.
"""

import os

TEXT = "Looking for someone who talks to their plants. I have read 10,000 romance novels and I still think the bravest sentence in any language is 'I made soup, come over.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
