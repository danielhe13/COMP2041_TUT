#!/bin/sh

# depends on pathnames not containing white-space

for c_file in $(find "/usr/src/linux" -type f -name '*.c')
do
    mutt -s "C for you"  -a "$c_file" -- andrewt@unsw.edu.au
done
