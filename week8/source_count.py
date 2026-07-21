#!/usr/bin/env python3

from glob import glob
total = 0

for filename in glob("*.[ch]"):
    with open(filename) as f:
        lines = f.readlines()
        n_lines = len(lines)
        print(f"{n_lines:7} {filename}")
        total += n_lines
print(f"{total:7} total")
