# Regex Questions

<details>
  <summary>
    C preprocessor commands in a C program source file.
  </summary>
  <br>

  <pre><code>^#</code></pre>
</details>
<br>

<details>
  <summary>
    All the lines in a C program except preprocessor commands.
  </summary>
  <br>

  Assuming only preprocessor starts with #
  <pre><code>^[^#]|^$</code></pre>
</details>
<br>

<details>
  <summary>
    All lines in a C program with trailing white space (one or more white space at the end of line).
  </summary>
  <br>

  <pre><code>\s$</code></pre>
</details>
<br>

<details>
  <summary>
    The names "Barry", "Harry", "Larry" and "Parry".
  </summary>
  <br>

  <pre><code>[BHLP]arry</code></pre>
</details>
<br>

<details>
  <summary>
    A string containing the word "hello" followed, some time later, by the word "world".
  </summary>
  <br>

  <pre><code>hello.*world</code></pre>
</details>
<br>

<details>
  <summary>
    The word "calendar" and mis-spellings where 'a' is replaced with 'e' or vice-versa.
  </summary>
  <br>

  <pre><code>c[ae]l[ae]nd[ae]r</code></pre>
</details>
<br>

<details>
  <summary>
    A list of non-negative integers separated by commas, e.g. 2,4,8,16,32
  </summary>
  <br>

  <pre><code>([1-9][0-9]*|0)(,([1-9][0-9]*|0))*</code></pre>
</details>
<br>

<details>
  <summary>
    A C string whose last character is newline.
  </summary>
  <br>

  <pre><code>"[^"]*\\n"</code></pre>
</details>
<br>

---

# Grep Questions

<details>
  <summary>
    Why does this <code class="language-shell">grep -E hello</code> seem to be taking a long time to run?
  </summary>
  <br>

  Because it is waiting for input from stdin.
</details>
<br>

<details>
  <summary>
    Why won’t <code class="language-shell">grep -E int main program.c</code> work?
  </summary>
  <br>

  <code class="language-shell">grep -E</code> will attempt to search files main and program.c for lines containing the string int, will need quotations around the rege
</details>
<br>
