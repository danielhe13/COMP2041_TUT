#!/usr/bin/env python3

import sys

number = False
verbose = False

if sys.argv[1] == '-n':
    number = True
elif sys.argv[1] == '-v':
    verbose = True

for filename in sys.argv[1:]:
    if filename[0] == '-':
        continue

    try:
        with open(filename, 'r') as stream:
            line_number = 1
            for line in stream:
                if number:
                    print(f"{line_number:6}  {line}", end="")

                elif verbose:
                    output = ""
                    for char in line[:-1]:
                        if ord(char) < 32:
                            output += "^" + chr(ord('A') + ord(char) - 1)
                        else:
                            output += char
                    print(f"{output}$")

                else:
                    print(f"{line}", end="")

                line_number += 1

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
