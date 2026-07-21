#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <file1> <file2>")
    sys.exit(1)

words1 = set()
with open(sys.argv[1]) as f:
    for word in f:
        word = word.strip()
        words1.add(word)

words2 = set()
with open(sys.argv[2]) as f:
    for word in f:
        word = word.strip()
        words2.add(word)

for word in words1 - words2:
    print(word)
