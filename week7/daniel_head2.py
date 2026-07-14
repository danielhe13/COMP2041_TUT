#!/usr/bin/env python3

import sys

n_lines = 10

if len(sys.argv) >= 2 and sys.argv[1][0] == '-':
    arg = sys.argv[1]
    n_lines = int(arg[1:])

for file in sys.argv[1:]:
    if file[0] == '-':
        continue

    print(f"==> {file} <==")
    with open(file, 'r') as f:
        for line in f.readlines()[0:n_lines]:
            print(line, end="")
