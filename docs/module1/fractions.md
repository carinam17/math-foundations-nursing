# Fractions

## What Is a Fraction?

A fraction represents a relationship between two quantities. It has
two parts:

- **Numerator** — the top number
- **Denominator** — the bottom number

\[\frac{\text{numerator}}{\text{denominator}}\]

In dimensional analysis, every conversion factor is a fraction. The
numerator and denominator are not arbitrary — they represent the same
quantity expressed in two different units, or a rate between two
quantities. Which unit you place on top determines which unit will
survive after cancellation.

\[\frac{1\text{ g}}{1000\text{ mg}} \qquad \frac{1000\text{ mg}}{1\text{ g}}\]

These are the same relationship written two ways. You choose the
orientation based on which unit you need to cancel.

## Multiplying Fractions

Multiply numerators together and denominators together.

\[\frac{1}{2} \times \frac{3}{4} = \frac{1 \times 3}{2 \times 4} = \frac{3}{8}\]

This is the only operation you need for every calculation in this
course. Dimensional analysis chains are a series of fractions
multiplied together — nothing more.

## Simplifying

Dividing both numerator and denominator by the same number does not
change the value of a fraction.

\[\frac{6}{8} = \frac{6 \div 2}{8 \div 2} = \frac{3}{4}\]

In a calculation chain, simplifying before multiplying reduces the
size of the numbers you work with and makes errors easier to spot.
It is not required — the answer is the same either way.

!!! tip "In this course"
    You will only multiply fractions. Dimensional analysis handles
    every conversion and every dosage calculation through
    multiplication alone. The orientation of each factor — which
    unit is on top — determines the result. You will not need to
    divide, add, or subtract fractions anywhere in this course.

## Self-Check

<div class="self-check" id="frac-self-check"></div>

<script type="application/json" id="frac-self-check-data">
[
  {
    "id": "frac-1",
    "question": "You need to cancel mg and end up with g. Which factor orientation is correct?",
    "options": [
      "mg / g (mg on top)",
      "g / mg (g on top)",
      "Either — orientation doesn't matter",
      "Neither — use division instead"
    ],
    "correct": 1,
    "feedback": "To cancel mg, it must appear in the denominator of your factor. That means g goes on top: g / mg. The unit that needs to cancel always goes in the denominator."
  },
  {
    "id": "frac-2",
    "question": "What is (3/5) × (10/6)?",
    "options": ["1/2", "1", "30/30", "2/1"],
    "correct": 1,
    "feedback": "(3 × 10) / (5 × 6) = 30 / 30 = 1. Multiplying numerators together and denominators together is the only fraction operation you need."
  },
  {
    "id": "frac-3",
    "question": "A student is unsure whether to multiply or divide to convert 500 mg to g. What resolves this?",
    "options": [
      "Memorizing the rule: always divide when going from smaller to larger units",
      "Writing the conversion as a factor and checking which unit cancels",
      "Using a calculator to try both and pick the reasonable answer",
      "Cross multiplying"
    ],
    "correct": 1,
    "feedback": "Factor orientation resolves it. Write 500 mg × (1 g / 1000 mg) — mg cancels, g remains. No rule to memorize, no decision between multiply and divide."
  }
]
</script>
