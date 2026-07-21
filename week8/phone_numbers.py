#!/usr/bin/env python3

import sys, re, subprocess

res = set()
for url in sys.argv[1:]:
    process = subprocess.run(f"wget -q -O- {url}", capture_output=True, text=True, shell=True)
    webpage = process.stdout

    for number in re.findall(r"[\d \-]+", webpage):
        number = re.sub(r"\D", "", number)
        if len(number) >= 8 and len(number) <= 15:
            res.add(number)

res = [int(i) for i in list(res)]
for num in sorted(res):
    print(num)
