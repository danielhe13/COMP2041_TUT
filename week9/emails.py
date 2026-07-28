#! /usr/bin/env python3

import re
import sys
import subprocess

if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} <url>")

url = sys.argv[1]
p = subprocess.run(["curl", "-s", "-L", url], capture_output=True, text=True)
webpage = p.stdout
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", webpage)

for email in sorted(set(emails)):
    print(email)