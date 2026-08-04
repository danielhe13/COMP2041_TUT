#!/usr/bin/env python3

# written by Daniel He

import sys

def chomp(string):
    if string[-1] == '\n':
        return string[:-1]
    else:
        return string

def qw(string):
    return string.split()

def die(message):
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)
