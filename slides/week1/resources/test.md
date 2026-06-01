<!--
Source - https://stackoverflow.com/a/39920717
Posted by TWiStErRob, modified by community. See post 'Timeline' for change history
Retrieved 2026-06-02, License - CC BY-SA 4.0
-->

<details>
  <summary>stuff with *mark* **down** in `summary` doesn't work any more, use HTML <i>italics</i> and <b>bold</b> instead in <code>&lt;summary&gt;</code> (<i>click to expand</i>)</summary>
  <!-- have to be followed by an empty line! -->

## *formatted* **heading** with [a](link)
```java
code block
```

  <details>
    <summary><u>nested</u> <b>stuff</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->

A bit more than normal indentation is necessary to get the nesting correct,
 1. list
 1. with
    1. nested
    1. items
        ```java
        // including code
        ```
    1. blocks
 1. and continued non-nested

  </details>
</details>


<details>
  <summary>⚠️ Major Plot Spoilers Inside</summary>

  Here is a quick breakdown of what happens:
  * Character A makes it out alive.
  * Character B was the traitor all along!

  You can even safely nest a code block:
  ```javascript
  console.log("The secret ending code is 42.");
  ```
</details>
