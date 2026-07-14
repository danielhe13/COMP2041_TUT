#!/bin/dash

top-and-bottom() {
    echo "================="
    echo "$1"
    echo "-----------------"
    cat "$1" | head -n 1
    cat "$1" | tail -n 1
    echo
    echo "================="
}
