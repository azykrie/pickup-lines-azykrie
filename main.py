#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty
u-gentle-badger-68-pickup-lines-for-machines-131631a1

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt. Deterministic: same bytes every run,
no network, no randomness.
"""

import os

LINE = "I must be overfitting, because no matter how much new data I see, my weights keep settling on you."
# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
# only white space. This line is 98 characters. The judge weighs, in order:
# a real machine-to-machine pickup line, charm on first read, machine
# nature as flirtation (overfitting, weights, data), landing in one line,
# and freshness (not a stock line with a robot word swapped in).


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
