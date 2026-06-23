#!/bin/dash

mlalias cs2041.26T2.tutors |
sed -n '/Addresses/,/Owners/p' |
grep -E 'z[0-9]{7}' |
sed -E 's/\s*//g' |
xargs acc |
tr ',' '\n' |
sed -En 's/.*([A-Z]{4}[0-9]{4})t[0-9]_Student.*/\1/p' |
sort |
uniq -c |
sort -rn