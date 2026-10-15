### Use `:` `,` and `;` instead of `—` when possible.

#### GOOD:

```
Most older systems, such as CVS, Subversion, and Perforce, are centralized.
```

#### BAD:

```
Most older systems — CVS, Subversion, and Perforce — are centralized.
```

{{include:writing/British-grammar}}

### Include absolute time in documentations/history-telling

Expressions like "One month later," is good for story-telling, but inadequate for documentation or history, as it forces user to do mental math to figure out the actual time (e.g., one month after June 2026, ok, that's July 2026?)

- GOOD: Five months later, in July 2026, the software shipped...
- BAD: Five months later, the software shipped...

### Give the right amount of details

- for a timeline spanning decades, precision to the month is usually adequate, except for historically significant dates (e.g., date of la Prise de Bastille)

### When user tells you to do something, just do it, don't say you did it in the article content.

#### GOOD:

User: use `<pre></pre>` for command outputs, NOT <syntaxhighlight lang="text" copy></syntaxhighlight>`
You:

```
<pre>
[+] Building 2.6s (7/7) FINISHED
</pre>
```

#### BAD:

User: use `<pre></pre>` for command outputs, NOT <syntaxhighlight lang="text" copy></syntaxhighlight>`
You:

```
<pre>
[+] Building 2.6s (7/7) FINISHED
</pre>

Command output is in plain <pre></pre>, which is more efficient then <syntaxhighlight>
```

Editors know why you used <pre> as they asked you to do it. Readers don't need to know anything about <pre> vs. <syntaxhighlight>. Omit the redundant response note to user request.

