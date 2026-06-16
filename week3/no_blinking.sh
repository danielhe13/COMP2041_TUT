#!/bin/dash

# <blink> </blink>

for file in "$@"; do
    if grep -Eiw "</?blink>" "$file" > /dev/null; then
        echo "Removing $file because it has a <blink> tag"
        mv "$file" "$file.bad"
    fi
done
