# Regex Questions

<details>
  <summary>
    C preprocessor commands in a C program source file.
  </summary>
  <br>

  ```
  ^#
  ```
</details>
<br>

<details>
  <summary>
    All the lines in a C program except preprocessor commands.
  </summary>
  <br>

  ```
  ^\s*#\s*[_A-Za-z]
  ```
</details>
<br>

<details>
  <summary>
    All lines in a C program with trailing white space (one or more white space at the end of line).
  </summary>
  <br>

  ```
  \s$
  ```
</details>
<br>

<details>
  <summary>
    The names "Barry", "Harry", "Larry" and "Parry".
  </summary>
  <br>

  ```
  [BHLP]arry
  ```
</details>
<br>

<details>
  <summary>
    A string containing the word "hello" followed, some time later, by the word "world".
  </summary>
  <br>

  ```
  hello.*world
  ```
</details>
<br>

<details>
  <summary>
    The word "calendar" and mis-spellings where 'a' is replaced with 'e' or vice-versa.
  </summary>
  <br>

  ```
  c[ae]l[ae]nd[ae]r
  ```
</details>
<br>

<details>
  <summary>
    A list of non-negative integers separated by commas, e.g. 2,4,8,16,32
  </summary>
  <br>

  ```
  ([1-9][0-9]*|0)(,([1-9][0-9]*|0))*
  ```
</details>
<br>

<details>
  <summary>
    A C string whose last character is newline.
  </summary>
  <br>

  ```
  "[^"]*\\n"
  ```
</details>
<br>
