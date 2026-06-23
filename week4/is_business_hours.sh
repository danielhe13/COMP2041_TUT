#!/bin/dash

current_hour=$(date "+%H")

if [ "$current_hour" -lt 9 ] && [ "$current_hour" -ge 17 ]; then
    exit 0
fi

exit 1