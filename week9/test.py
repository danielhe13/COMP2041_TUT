#!/usr/bin/env python3

import sys, re, subprocess

url = sys.argv[1]

process = subprocess.run(["wget", "-q", "-O-", url], capture_output=True, text=True)
webpage = process.stdout.lower()

# response = requests.get(url)
# webpage = response.text.lower()
# soup = BeautifulSoup(webpage, 'html5lib')

# remove comments
webpage = re.sub(r"<!--.*?-->", "", webpage, flags=re.DOTALL)

# get all tags
tags = re.findall(r"< *([a-z]+)", webpage)

# using collections.counter, alternatively can use a dict to count
tags_counter = {}
for tag in tags:
    if (tag not in tags_counter):
        tags_counter[tag] = 0
    tags_counter[tag] += 1

for tag, counter in sorted(tags_counter.items()):
    print(f"{tag} {counter}")