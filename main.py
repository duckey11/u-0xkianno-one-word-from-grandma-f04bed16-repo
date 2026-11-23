#!/usr/bin/env python3
"""One Word From Grandma - make.fun entry.

Writes exactly one word to /output/entry.txt: the word a grandma
would text about AI.

The word is a fixed constant, so every run produces byte-identical
output. No network, no secrets, no files read from outside this repo.
"""

import os

WORD = "Thingamajig"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
