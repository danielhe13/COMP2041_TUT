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

  <ol>
    <li><code>&lt;</code>, <code>&gt;</code> and <code>|</code> are apart of the shell’s syntax.</li>
    <li>Characters are part of the shell’s syntax so the shell will interpret them rather than passing them to grep &rarr; avoid by wrapping the regex expression with single or double quotes.</li>
    <li>grep by itself doesn’t implement <code>|</code> so will need to use <code>grep -E</code>.</li>
    <li>The supplied regex expression won’t match the HTML tags if they’re in upper case (e.g. <code>&lt;P&gt;&lt;/P&gt;</code>) so use <code>grep -Ei</code> to make it case-insensitive.</li>
    <li>The supplied regular expression also won't match HTML tags containing spaces, e.g: <code>&lt;p &gt;</code> so account for the whitespaces i.e. <code>grep -Ei '&lt;\s*(p|br)\s*&gt;' /tmp/index.html</code>.</li>
    <li>The HTML tag may contain attributes, e.g: <code>&lt;p class=&quot;lead_para&quot;&gt;</code> so change it to <code>grep -Ei '&lt;\s*(p|br)[^&gt;]*&gt;' /tmp/index.html</code>.</li>
  </ol>

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
