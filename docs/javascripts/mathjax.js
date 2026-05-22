// docs/javascripts/mathjax.js
// MathJax 3 configuration for Convergent Math nursing textbook
// Place this file at: docs/javascripts/mathjax.js (relative to your mkdocs project root)

window.MathJax = {
  loader: {
    load: ['[tex]/cancel']
  },
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: { '[+]': ['cancel'] },
    macros: {
      // ===== Unit notation =====
      // General-purpose: \unit{any_unit} produces properly-spaced unit text
      // Usage: \unit{g}, \unit{tab}, \unit{drop}, etc.
      unit: ["\\,\\text{#1}", 1],

      // Common nursing units (shortcuts; chosen to avoid conflicts with built-ins)
      // Note: \g, \L, \min, \hr are NOT defined here because they shadow built-in
      //       LaTeX/MathJax commands. Use \unit{g}, \unit{L}, \unit{min}, \unit{hr}.
      mg:  "\\,\\text{mg}",
      mcg: "\\,\\text{mcg}",
      mL:  "\\,\\text{mL}",
      kg:  "\\,\\text{kg}",

      // ===== Conversion fractions =====
      // Semantic alias for \dfrac — signals "this is a conversion factor"
      // Usage: \conv{1000 \mg}{1 \unit{g}}
      conv: ["\\dfrac{#1}{#2}", 2],

      // ===== Cancellation =====
      // Shorthand for \cancel — saves keystrokes across many problems
      // Usage: \xc{\unit{g}}
      xc: ["\\cancel{#1}", 1],
      cn: ["\\cancel{#1}", 1],
      // ===== Labeled factor (for annotated walkthroughs) =====
      // Renders math with a descriptive label in an underbrace
      // Usage: \factor{\conv{125 \mL}{1 \unit{hr}}}{ordered rate}
      factor: ["\\underbrace{#1}_{\\text{#2}}", 2],

      // Overbrace version (label above). Alternate with \factor for
      // visual variety, or use when underbrace would crowd other elements.
      // Usage: \overfactor{\conv{1 \unit{hr}}{60 \unit{min}}}{hr→min conversion}
      overfactor: ["\\overbrace{#1}^{\\text{#2}}", 2]

    }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Re-typeset math when navigating between pages (only needed if you use
// MkDocs Material's `navigation.instant` feature; safe to keep regardless)
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
