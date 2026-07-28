#! /usr/bin/env python3

# fetch specified web page and print heading text with counts and optional level filter

import sys
from collections import Counter
from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup

def main():

    parser = ArgumentParser()
    parser.add_argument('-l', '--level', type=int, choices=range(1, 7), metavar='N',
                        help='only show headings at level N or above (1-6)')
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    response = requests.get(args.url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headings = []
    for tag in soup.find_all():
        if tag.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = tag.name[1]
            text = tag.get_text(strip=True)
            headings.append((level, text))

    # filter by level if specified
    if args.level is not None:
        headings = [(level, text) for level, text in headings if int(level) <= args.level]

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
