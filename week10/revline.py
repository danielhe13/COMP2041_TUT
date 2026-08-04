#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.split()
    words = reversed(words)
    print(" ".join(words))
