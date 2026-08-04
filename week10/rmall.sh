#!/bin/dash


# written by Daniel He

PATH="$PATH:$PWD"

if [ "$#" -lt 1 ]
then
    echo "Usage: $0 dir"
    exit 1
fi

# make sure that it is a directory
if [ ! -d "$1" ]
then
    echo "$1 is not a directory"
    echo "Usage: $0 dir"
    exit 1
fi

# for each file in the directory
cd "$1"
for file in *
do
    # File
    if [ -f "$file" ]
    then
        rm "$file"

    # Directory
    elif [ -d "$file" ]
    then
        echo -n "Delete $file? "
        read answer
        if [ "$answer" = "yes" ]
        then
            rmall "$file"
        fi
    fi
done
