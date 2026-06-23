#!/bin/dash

limit=$1
p=2

while [ "$p" -lt "$limit" ]; do
    if ./is_prime.sh "$p" > /dev/null; then
        echo "$p"
    fi
    p=$((p + 1))
done