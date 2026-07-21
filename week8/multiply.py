#!/usr/bin/env python3

import sys

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <n> <m> <column_width>")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])
width = int(sys.argv[3])

for i in range(1, n + 1):
    print(f"{i:{width}}", end="")
    for j in range(2, m + 1):
        print(f" {i * j:{width}}", end="")
    print()

