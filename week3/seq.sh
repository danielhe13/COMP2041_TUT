#!/bin/dash

# $# - number of arguments parsed
# $@ - all arguments parsed
# $1, $2, $3... - nth argument parsed
# $0 -> name of the program

increment=1

# if number of arguments equals to 1
if [ "$#" -eq 1 ]; then
    first=1
    last=$1
elif [ "$#" -eq 2 ]; then
    first=$1
    last=$2
elif [ "$#" -eq 3 ]; then
    first=$1
    last=$2
    increment=$3
else
    echo "Usage: $0 <FIRST> <LAST> <INCREMENT>"
    exit 1
fi

if ! [ "$first" -eq "$first" ] || ! [ "$last" -eq "$last" ]; then
    echo "Error: arguments must be an integer"
fi

count="$first"
while [ "$count" -le "$last" ]; do
    echo "$count"
    count=$((count + increment))
done