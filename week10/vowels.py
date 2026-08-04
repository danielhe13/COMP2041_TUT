#!/usr/bin/env python3

# written by Daniel He

import sys

lower_vowels = "aeiou"
upper_vowels = "AEIOU"

for line in sys.stdin:
    new_line = ""

    for c in line:
        if c in lower_vowels:
            new_line += c.upper()
        elif c in upper_vowels:
            new_line += c.lower()
        else:
            new_line += c

    print(new_line, end="")
