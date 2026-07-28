#! /usr/bin/env python3

# fetch specified web page and print heading text

import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} <url>")

url = sys.argv[1]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# print headings with indentation
for tag in soup.find_all():
    if tag.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = int(tag.name[1])
        text = tag.text.strip()
        indent = "\t" * (level - 1)
        print(f"{indent}{text}")
