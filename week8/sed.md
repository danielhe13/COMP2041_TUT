# quit
```shell
seq 42 44 | sed 1q
```
- it would print the first line of `seq 42 44` then quit
----

```shell
sed 10q < dictionary.txt
```
- it would print the first 10 lines of `dictionary.txt` then quit
----
```shell
seq 41 43 | sed 4q
```
- it would print the first 4 line of `seq 42 44` then quit
- since there are less than 4 lines, all the lines get printed
----
```shell
seq 90 110 | sed /.1/q
```
- The addess `/.1/` is the address of any line that matches the regex `.1`
- it would quit after the a line with `91`
----
```shell
sed '/r.*v/q' < dictionary.txt
```
- The addess `/r.*v/` is the address of any line that matches the regex `r.*v`
- it would quit after the a line matches that regex
----
```shell
yes | sed 3q
```
- it would print the first 3 line then quit even tho yes runs prints infinitely
----

# print
```shell
seq 41 43 | sed 2p
```
- print the line 2
- sed print by default so it will print line 2 twice
----
```shell
head dictionary.txt | sed 3p
```
- print the line 3
- sed print by default so it will print line 3 twice
----
```shell
seq 41 43 | sed -n 2p
```
- only print the line 2
- the `-n` flag turns off automatic printing
----
```shell
sed -n 42p < dictionary.txt
```
- only print the line 42
- the `-n` flag turns off automatic printing
----
```shell
head -n 1000 dictionary.txt | sed -n '/z.$/p'
```
- Only print a line if it matches the regex `z.$` (second last character is a z)
----

# substitute
```shell
seq 10 15 | sed 's/[15]/zzz/'
```
- replace the first instance of 1 or 5 on each line with zzz
----
```shell
seq 10 15 | sed 's/[15]/zzz/g'
```
- replace all instances of 1 or 5 with zzz
- global flag
----
```shell
echo "Hello Andrew" | sed 's/e//'
```
- replace the first e with nothing
----
```shell
echo "Hello Andrew" | sed 's/e//g'
```
- replace all e with nothing
----

# addresses
```shell
seq 1 5 | sed '$d'
```
- delete the last line of input
- `$` means the last line
- `d` means delete command
- when using `d` lines are not automatically printed
----
```shell
seq 42 44 | sed 2,3d
```
- delete all lines from 2 to 3 inclusive
----
```shell
seq 10 21 | sed 3,/2/d
```
- delete all lines from 3 until it finds a line after that matches the regex `2` inclusive
- if a line with regex `2` doesn't exist, then it keep deleting everything (never turns off deletion)
----
```shell
seq 10 21 | sed /2/,7d
```
- delete the first line that matches the regex `2` then keep deleting until the 7th line inclusive
- if no line has `2` then nothing gets deleted (never turns on deletion)
---
```shell
seq 10 21 | sed /2/,/7/d
```
- delete all lines that are between the regex `2` and `7`
----

# substitute
```shell
seq 1 5 | sed 'sX[15]XzzzX'
```
- `X` is used as the delimiter instead of the usual `/`
- replace the first instance of 1 or 5 on each line with zzz
----


# multiple commands
```shell
seq 1 5 | sed '4q;/2/d'
```
- print the first 4 lines then quit
- Then delete any line that match the regex `2`
- both of the commands will run on each line of input
- Union of both (must satisfy both)
----

# -f
```shell
echo "4q" > commands.script
echo "/2/d" >> commands.script
seq 1 5 | sed -f commands.script
```
- the sed command is being passed in from a file instead so it is basically just `sed '4q;/2/d'`
- each newline is like a `;`
----


# input files
```shell
seq 1 2 > two.txt
seq 1 5 > five.txt
sed '4q;/2/d' two.txt five.txt
```
- instead of running the sed command on stdin, it will run on the contents of the passed in files
- the contents of the passed in files is treated as one big input, so the first line of `five.txt` is appended to the end of `two.txt` so its treated like a big file with 7 lines
----


# whitespace and comments
```shell
seq 24 42 | sed ' 3, 17  d  # comment   ;   /2/p'
```
- same as `sed '3,17d'`
- the spaces do nothing
- everything at and after # is a comment
----


# -i
```shell
seq 1 5 > five.txt
sed -i /[24]/d five.txt
cat five.txt
```
- `-i` flag modifies the input file inplace
- so it will delete all lines that match the regex `[24]` in the file
----


# multiple commands
```shell
echo 'Punctuation characters include . , ; :' | sed 's/;/semicolon/g;/;/q'
```
- this is basically `sed 's/;/semicolon/g'` and `sed '/;/q'`
- replace `;` with the word `semicolon`
- quit after the first line with a semicolon after that
----
