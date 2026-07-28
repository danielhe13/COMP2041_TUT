#! /usr/bin/env python3

# fetch specified web page and print heading text with counts

import sys
from collections import Counter
import requests
from bs4 import BeautifulSoup

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <url>")

    url = sys.argv[1]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headings = []
    for tag in soup.find_all():
        if tag.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = tag.name[1]
            text = tag.get_text(strip=True)
            headings.append((level, text))

    # count headings by level
    level_counts = Counter()
    for level, _ in headings:
        level_counts[level] += 1

    # print summary of counts
    for level in sorted(level_counts.keys()):
        print(f"H{level}: {level_counts[level]}")

    # print headings with indentation
    for level, text in headings:
        indent = "\t" * (int(level) - 1)
        print(f"{indent}{text}")

if __name__ == "__main__":
    main()