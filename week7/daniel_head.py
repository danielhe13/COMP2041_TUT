#!/usr/bin/env python3

import sys

n_lines = 10

if len(sys.argv) == 2:
    arg = sys.argv[1]
    n_lines = int(arg[1:])

for line in sys.stdin.readlines()[0:n_lines]:
    print(line, end="")
