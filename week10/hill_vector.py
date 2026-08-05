#!/usr/bin/env python3

import sys

# parseing input into a int array
list_nums = []
for line in sys.stdin:
    if line[-1] == "\n":
        line = line[:-1]
    for num in line.split(" "):
        list_nums.append(int(num))

# start from left and move i to the right if it is increasing
i=0
while i < len(list_nums)-1 and list_nums[i] < list_nums[i+1]:
    i += 1

# start from right and move j to the left if it is increasing
j=len(list_nums)-1
while j >= 0+1 and list_nums[j] < list_nums[j-1]:
    j -= 1

# if they both have moved and they are on the same index
# then that is a hill
if i == j and j != len(list_nums)-1 and i != 0:
    print("hill")
else:
    print("not hill")
