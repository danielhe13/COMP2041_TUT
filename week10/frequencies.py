#!/usr/bin/env python3

# written by Daniel He

import collections, sys

lines = sys.stdin.readlines()
all_line = " ".join(lines)
freq = collections.Counter([char for char in all_line if char.isalnum()])

for f in sorted(freq):
    print(f"'{f}' occurred {freq[f]} times")
