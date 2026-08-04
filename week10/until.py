#!/usr/bin/env python3

# written by Daniel He

import sys, re

arg1 = sys.argv[1]

try:
    # arg1 is a line number
    number = int(arg1)
    for i, line in enumerate(sys.stdin, start=1):
        print(line, end="")
        if number == i:
            break

except ValueError:
    # arg1 is a regex (remove `/` from start and end)
    regex = rf"{arg1[1:-1]}"
    for i, line in enumerate(sys.stdin, start=1):
        print(line, end="")
        if re.search(regex, line):
            break
