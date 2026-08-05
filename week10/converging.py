#!/usr/bin/env python3

import sys

# parseing input into a int array
list_nums = []
for line in sys.stdin:
    if line[-1] == "\n":
        line = line[:-1]
    for num in line.split(" "):
        list_nums.append(int(num))

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
