#!/usr/bin/env python3

import sys

number = False

if sys.argv[1] == '-n':
    number = True

for filename in sys.argv[1:]:
    if filename[0] == '-':
        continue

    try:
        with open(filename, 'r') as stream:
            line_number = 1
            for line in stream:
                if number:
                    print(f"{line_number:6}  {line}", end="")
                else:
                    print(f"{line}", end="")
                line_number += 1

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
