#! /usr/bin/env python3

import sys, re

MONTH_NAMES = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

MONTHS = {name: i for i, name in enumerate(MONTH_NAMES, 1)}

dates = []
for line in sys.stdin:
    if m := re.search(r"(\d{4})-(\d{2})-(\d{2})", line):
        year, month, day = map(int, m.groups())
    elif m := re.search(r"(\d{2})/(\d{2})/(\d{4})", line):
        day, month, year = map(int, m.groups())
        if month > 12:
            day, month = month, day
    elif m := re.search(r"(\d{1,2})\s+([a-zA-Z]+)\s+(\d{4})", line):
        day = int(m.group(1))
        year = int(m.group(3))
        month_name = m.group(2).lower()
        if month_name not in MONTH_NAMES:
            continue
        month = MONTHS[m.group(2).lower()]
    else:
        continue
    dates.append((year, month, day))

for y, m, d in sorted(dates):
    print(f"{y}-{m:02d}-{d:02d}")