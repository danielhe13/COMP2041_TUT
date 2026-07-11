#!/usr/bin/env python3

import sys
import re

number = False
if len(sys.argv) > 1 and sys.argv[1][0] == "-":
    arg = sys.argv.pop(1)
    arg = arg[1:]
    if arg == "n":
        number = True

counter = 1
for filename in sys.argv[1:]:
    try:
        print(f"==> {filename} <==")

        with open(filename) as f:
            for line in f:
                if number and re.search("^hello", line):
                    print(f"{counter:6}  {line}", end="")
                else:
                    print(line, end="")
                counter += 1
            
    except IOError as e:
        print(f"{sys.argv[0]}: cannot open {e.filename}: {e.strerror}")

