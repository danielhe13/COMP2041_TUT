#!/usr/bin/env python3

import sys

# parseing input into a int array
list_nums = []
for line in sys.stdin:
    if line[-1] == "\n":
        line = line[:-1]
    for num in line.split(" "):
        list_nums.append(int(num))

# alternate parseing input in one line
# list_nums = [int(item) for line in [line.split(" ") for line in [line[:-1] if line[-1] == '\n' else line for line in sys.stdin.readlines()]] for item in line]

# Keep track of the difference of each pair
prev = -1
for i in range(len(list_nums)-1):
    curr = list_nums[i] - list_nums[i+1]

    # if the difference is not decreasing then fail
    if prev != -1 and curr > prev:
        print("not converging")
        exit(0)

    prev = curr

print("converging")
