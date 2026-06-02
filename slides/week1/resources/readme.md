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

<details>
  <summary>
    Give five reasons why this attempt to search a file for HTML paragraph and break tags may fail <code class="language-shell">grep &lt;p&gt;|&lt;br&gt; index.html</code>
  </summary>
  <br>

  1. `<`, `>` and `|` are apart of the shell’s syntax, 

  2.  are part of the shell’s syntax so the shell will interpret them rather than passing them to `grep` → avoid by wrapping the regex expression with single or double quotes

  3. `grep` by itself doesn’t implement `|` so will need to use `grep -E`
  4. The supplied regex expression won’t match the HTML tags if they’re in upper case (e.g. `<P></P>`) so use `grep -Ei` to make it case-insensitive

  5. The supplied regular expression also won't match HTML tags containing spaces, e.g: `<p >` so account for the whitespaces i.e. `grep -Ei '<\s*(p|br)\s*>' /tmp/index.html`

  6. The HTML tag may contain attributes, e.g: `<p class="lead_para">` so change it to `grep -Ei '<\s*(p|br)[^>]*>' /tmp/index.html`
</details>
<br>

<details>
  <summary>
    Write a <code class="language-shell">grep -E</code> command which will print any lines in a file <code>ips.txt</code> containing an IP addresses in the range <code>129.94.172.1</code> to <code>129.94.172.25</code>
  </summary>
  <br>

  <pre><code>grep -E '129\.94\.172\.([1-9]|1[0-9]|2[0-5])' ips.txt</code></pre>
</details>
<br>

<details>
  <summary>
    Write a <code class="language-shell">grep -E</code> command which prints position real numbers at the start of the line in <code>nums.txt</code>
  </summary>
  <br>

  <pre><code>grep -E '^(([0-9]|[1-9][0-9]+)\.?[0-9]*)' nums.txt</code></pre>
</details>
<br>

### Credits
Mitchell Wang, Angella Pham, Jayden Leung
