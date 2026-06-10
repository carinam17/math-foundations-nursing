# Proportions

A proportion states that two ratios are equal:

\[\frac{a}{b} = \frac{c}{d}\]

In nursing, proportions appear any time you apply a stock ratio to
a specific order. The stock ratio and the ordered dose are two equal
expressions of the same relationship — one known, one to be found.


---

## Proportions and Stock Ratios

Every dosage calculation is a proportion. You have a stock ratio
from the label, and you need to find the quantity that matches
the ordered dose.

**Stock:** 250 mg per tablet
**Order:** 500 mg

These form a proportion:

\[\frac{250 \text{ mg}}{1 \text{ tablet}} = \frac{500 \text{ mg}}{x \text{ tablets}}\]

The same ratio holds — you just need to find x.

---

## Solving with Dimensional Analysis

Rather than solving for x algebraically, dimensional analysis
sets up the proportion as a cancellation chain:

\[500 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{250 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

The stock ratio is written as a factor, oriented so mg cancels.
The result is x directly — no algebra needed.

This is why DA is the preferred method. The proportion structure
is still there; the cancellation handles the solving.

!!! info "Alternative methods"
    If you have learned cross-multiplication or ratio-proportion
    algebraic solving, those methods work for the same problems.
    They are covered in [Additional Methods](../reference/additional-methods.md).

---

## Reasonableness Check

Before accepting any answer, ask:

- Would a nurse realistically give this many tablets?
- Is this volume reasonable to administer?
- Does the direction make sense — more drug, more volume?

General guidelines:

- Oral tablets: rarely more than **3 tablets** per dose
- Oral liquid: typically **5–30 mL** per dose

If your answer falls outside these ranges, recheck the setup.

---

## Clinical Application

**Example 1 — oral suspension:**
Stock: 125 mg/5 mL
Order: 250 mg
How many mL?

\[250 \cancel{\text{ mg}} \times \frac{5 \text{ mL}}{125 \cancel{\text{ mg}}} = \frac{1250}{125} = 10 \text{ mL}\]

**Example 2 — injectable:**
Stock: 40 mg/mL
Order: 100 mg
How many mL?

\[100 \cancel{\text{ mg}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = \frac{100}{40} = 2.5 \text{ mL}\]

---

## Practice Problems

!!! example "Problem 1"
    Stock: 500 mg per tablet
    Order: 1000 mg
    How many tablets?

??? success "Answer"
    \[1000 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{500 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

!!! example "Problem 2"
    Stock: 250 mg/5 mL
    Order: 375 mg
    How many mL?

??? success "Answer"
    \[375 \cancel{\text{ mg}} \times \frac{5 \text{ mL}}{250 \cancel{\text{ mg}}} = \frac{1875}{250} = 7.5 \text{ mL}\]

!!! example "Problem 3"
    Stock: 0.25 mg per tablet
    Order: 0.5 mg
    How many tablets?

??? success "Answer"
    \[0.5 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{0.25 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

!!! example "Problem 4"
    Stock: 10 mg/mL
    Order: 25 mg
    How many mL?

??? success "Answer"
    \[25 \cancel{\text{ mg}} \times \frac{1 \text{ mL}}{10 \cancel{\text{ mg}}} = 2.5 \text{ mL}\]

!!! example "Problem 5"
    Stock: 80 mg/2 mL
    Order: 60 mg
    How many mL?

??? success "Answer"
    \[60 \cancel{\text{ mg}} \times \frac{2 \text{ mL}}{80 \cancel{\text{ mg}}} = \frac{120}{80} = 1.5 \text{ mL}\]

---

## Self-Check

<div class="self-check" id="prop-self-check"></div>

<script type="application/json" id="prop-self-check-data">
[
  {
    "id": "prop-1",
    "question": "Stock: 250 mg/5 mL. Order: 500 mg. Which DA setup is correct?",
    "options": [
      "500 mg × (250 mg / 5 mL)",
      "500 mg × (5 mL / 250 mg)",
      "250 mg × (500 mg / 5 mL)",
      "5 mL × (500 mg / 250 mg)"
    ],
    "correct": 1,
    "feedback": "500 mg × (5 mL / 250 mg) = 10 mL. The stock ratio is oriented with mL on top so mg cancels, leaving mL."
  },
  {
    "id": "prop-2",
    "question": "Stock: 10 mg per tablet. Order: 30 mg. How many tablets?",
    "options": ["1 tablet", "2 tablets", "3 tablets", "0.3 tablets"],
    "correct": 2,
    "feedback": "30 mg × (1 tablet / 10 mg) = 3 tablets. This is at the upper limit of a typical oral dose — worth a reasonableness check before administering."
  },
  {
    "id": "prop-3",
    "question": "Your calculation gives 45 mL for a single oral dose. What should you do?",
    "options": [
      "Administer — the math is correct",
      "Round to 40 mL for convenience",
      "Recheck the setup — 45 mL is outside the typical range",
      "Split into two 22.5 mL doses"
    ],
    "correct": 2,
    "feedback": "45 mL exceeds the typical 5–30 mL range for a single oral dose. Recheck the stock ratio and order before proceeding."
  },
  {
    "id": "prop-4",
    "question": "Stock: 40 mg/mL. Order: 80 mg. How many mL?",
    "options": ["0.5 mL", "1 mL", "2 mL", "3.2 mL"],
    "correct": 2,
    "feedback": "80 mg × (1 mL / 40 mg) = 2 mL. The dose doubled, so the volume doubles — that's a proportional relationship."
  }
]
</script>
