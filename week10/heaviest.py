#!/usr/bin/env python3

import sys, collections

hash_map = collections.Counter()

for i in sys.argv[1:]:
    hash_map[i] += int(i)

print(hash_map.most_common()[0][0])
