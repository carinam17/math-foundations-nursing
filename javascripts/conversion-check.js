// =============================================================================
// conversion-check.js
// Lightweight interactive unit-conversion exercises for the Convergent Math
// nursing site. No dependencies, no Python runtime — plain vanilla JS (~3 KB).
//
// Place at: docs/javascripts/conversion-check.js
// Register in mkdocs.yml under extra_javascript.
//
// Usage in any markdown page (raw HTML block, blank line before & after):
//
//   <div class="conversion-exercise"
//        data-prompt="1 kg = {blank} lb"
//        data-answer="2.2"
//        data-tolerance="0.05"></div>
//
// data-prompt    : the exercise text; {blank} marks where the input goes
// data-answer    : the correct numeric answer
// data-tolerance : accepted +/- range (handles rounding, e.g. 2.2 vs 2.20462)
// =============================================================================

(function () {
  // --- Inject styles once -----------------------------------------------------
  function injectStyles() {
    if (document.getElementById("cm-ex-styles")) return;
    var css = `
      .cm-ex { margin: 0.75rem 0; font-size: 1rem; line-height: 1.9; }
      .cm-ex-input {
        width: 5rem; padding: 0.2rem 0.45rem; margin: 0 0.35rem;
        border: 2px solid #3B687E; border-radius: 4px; font-size: 1rem;
        text-align: center;
      }
      .cm-ex-input-correct { border-color: #006600; }
      .cm-ex-btn {
        margin-left: 0.5rem; padding: 0.25rem 0.8rem;
        background: #3B687E; color: #fff; border: none; border-radius: 4px;
        cursor: pointer; font-size: 0.9rem;
      }
      .cm-ex-btn:hover { background: #2e5365; }
      .cm-ex-feedback { margin-left: 0.6rem; font-weight: 600; }
      .cm-ex-correct   { color: #006600; }
      .cm-ex-incorrect { color: #990000; }
      .cm-ex-neutral   { color: #828282; }
      .cm-ex-reveal {
        display: inline-block; margin-left: 0.6rem;
        font-size: 0.8rem; color: #828282;
      }
      .cm-ex-tip {
        display: block; margin-top: 0.25rem;
        font-size: 0.8rem; color: #828282; font-style: italic;
      }
    `;
    var style = document.createElement("style");
    style.id = "cm-ex-styles";
    style.textContent = css;
    document.head.appendChild(style);
  }

  // --- Build a single exercise ------------------------------------------------
  function buildExercise(el) {
    if (el.dataset.cmBuilt) return;       // idempotent guard
    el.dataset.cmBuilt = "1";

    var prompt = el.dataset.prompt || "{blank}";
    var answer = parseFloat(el.dataset.answer);
    var tolerance = parseFloat(el.dataset.tolerance || "0");
    var parts = prompt.split("{blank}");

    el.classList.add("cm-ex");

    var input = document.createElement("input");
    input.type = "text";
    input.className = "cm-ex-input";
    input.setAttribute("inputmode", "decimal");
    input.setAttribute("aria-label", "Your answer");

    var button = document.createElement("button");
    button.type = "button";
    button.className = "cm-ex-btn";
    button.textContent = "Check";

    var feedback = document.createElement("span");
    feedback.className = "cm-ex-feedback";
    feedback.setAttribute("aria-live", "polite");

    var reveal = document.createElement("a");
    reveal.href = "#";
    reveal.className = "cm-ex-reveal";
    reveal.textContent = "Reveal answer";

    var notationTip = document.createElement("span");
    notationTip.className = "cm-ex-tip";

    function check() {
      // Strip thousands-separator commas (US audience): "1,000" -> "1000"
      var raw = input.value.trim().replace(/,/g, "");
      var val = parseFloat(raw);
      notationTip.textContent = "";

      if (isNaN(val)) {
        feedback.textContent = "Enter a number.";
        feedback.className = "cm-ex-feedback cm-ex-neutral";
        return;
      }
      if (Math.abs(val - answer) <= tolerance) {
        feedback.textContent = "✓ Correct";
        feedback.className = "cm-ex-feedback cm-ex-correct";
        input.classList.add("cm-ex-input-correct");

        // Non-blocking clinical-notation coaching. The answer is already
        // marked correct — these tips reinforce ISMP safe-notation habits.
        var tips = [];
        if (/^\.\d/.test(raw)) {
          tips.push("include the leading zero — write 0.5, not .5 " +
                    "(a missed decimal makes \".5\" read as \"5\")");
        }
        if (/\.\d*0$/.test(raw)) {
          tips.push("drop the trailing zero — write 5, not 5.0 " +
                    "(a missed decimal makes \"5.0\" read as \"50\")");
        }
        if (tips.length) {
          notationTip.textContent = "Clinical notation: " + tips.join("; ") + ".";
        }
      } else {
        feedback.textContent = "✗ Not quite — try again";
        feedback.className = "cm-ex-feedback cm-ex-incorrect";
        input.classList.remove("cm-ex-input-correct");
      }
    }

    button.addEventListener("click", check);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") { e.preventDefault(); check(); }
    });
    reveal.addEventListener("click", function (e) {
      e.preventDefault();
      feedback.textContent = "Answer: " + el.dataset.answer;
      feedback.className = "cm-ex-feedback cm-ex-neutral";
      notationTip.textContent = "";
    });

    el.textContent = "";
    el.appendChild(document.createTextNode(parts[0] || ""));
    el.appendChild(input);
    el.appendChild(document.createTextNode(parts[1] || ""));
    el.appendChild(button);
    el.appendChild(feedback);
    el.appendChild(reveal);
    el.appendChild(notationTip);
  }

  // --- Init -------------------------------------------------------------------
  function init() {
    injectStyles();
    document.querySelectorAll(".conversion-exercise").forEach(buildExercise);
  }

  // MkDocs Material instant-loading: re-run on every page change.
  if (window.document$) {
    window.document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
