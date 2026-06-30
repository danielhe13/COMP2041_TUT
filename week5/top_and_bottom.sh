#!/bin/dash

top_and_bottom() {
    echo "================="
    echo "$1"
    echo "-----------------"
    head -n1 "$1"
    tail -n1 "$1"
    echo "================="
}

for file in "$@"; do
    top_and_bottom "$file"
done
