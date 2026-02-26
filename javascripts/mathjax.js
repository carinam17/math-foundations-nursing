window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
  }
};
```

---

Then in your markdown you can write:

**Inline fraction:**
```
The dose is \(\frac{1}{2}\) tablet
```

**Display fraction:**
```
\[\frac{500 \text{ mg}}{250 \text{ mg}} \times 1 \text{ tablet} = 2 \text{ tablets}\]
```

**Cancellation:**
```
\[\frac{500 \text{ mg}}{1} \times \frac{1 \text{ g}}{1000 \text{ mg}} = 0.5 \text{ g}\]
