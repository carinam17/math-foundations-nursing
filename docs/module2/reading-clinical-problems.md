# Reading Clinical Problems

A clinical problem gives you the information you need to set up a
calculation — but it doesn't hand you the factors. You have to extract
them from the problem statement before you can write a chain.

This page teaches that extraction step. The arithmetic is the same
dimensional analysis you already know. The new skill is reading a
problem and identifying every factor hidden inside it.

---

## The four steps

Every calculation in this course follows the same process:

1. **Get the information you need** — identify the given value, the
   target unit, and every rate or relationship stated in the problem.
2. **Write each piece as a factor** — express every relationship as a
   fraction with a numerator and a denominator. Use 1 if a value has
   no explicit partner.
3. **Arrange and check for cancellation** — order the factors so
   unwanted units cancel. Confirm the surviving unit is the one you
   want before doing any arithmetic.
4. **Compute** — multiply numerators, multiply denominators, divide.
   Apply rounding and the correct abbreviation.

---

## Extracting factors from problem statements

### Simple stock relationships

> "Stock is labeled 250 mg per tablet."

This gives you two factors depending on which unit you want to cancel:

\[\frac{250\text{ mg}}{1\text{ tablet}} \qquad \text{or} \qquad \frac{1\text{ tablet}}{250\text{ mg}}\]

Keep the numbers as they appear on the label. Do not simplify yet —
let the chain handle the arithmetic.

### Rates (per kg, per hour, per day)

> "The drug is ordered at 5 mg/kg."

This is a factor. The slash means "per," and "per" means the denominator
is 1 of whatever follows:

\[\frac{5\text{ mg}}{1\text{ kg}}\]

### Compound rates

> "Ordered at 40 mg/kg/day in 3 divided doses."

Two factors are embedded here:

\[\frac{40\text{ mg}}{1\text{ kg}} \qquad \text{and} \qquad \frac{1\text{ day}}{3\text{ doses}}\]

Both go into the chain. The chain resolves the full calculation in one pass.

### Liquid stock

> "Stock: 125 mg per 5 mL."

\[\frac{125\text{ mg}}{5\text{ mL}} \qquad \text{or} \qquad \frac{5\text{ mL}}{125\text{ mg}}\]

Do not convert to 25 mg/mL before setting up the chain. Use the
numbers from the label. The chain produces the same result and
preserves the connection to what is written on the vial.

---

## Worked examples

### Example 1 — Dose verification

Order: 0.25 g of amoxicillin. Stock: 250 mg per tablet.
Is the order the same as one tablet?

**Step 1 — Information**

- Given: 0.25 g
- Stock: 250 mg per tablet
- Target: tablets

**Step 2 — Write the factors**

\[\frac{0.25\text{ g}}{1} \qquad \frac{1000\text{ mg}}{1\text{ g}} \qquad \frac{1\text{ tablet}}{250\text{ mg}}\]

**Step 3 — Arrange and check**

\[0.25 \cancel{\text{ g}} \times \frac{1000 \cancel{\text{ mg}}}{1 \cancel{\text{ g}}} \times \frac{1\text{ tablet}}{250 \cancel{\text{ mg}}}\]

Surviving unit: **tablet** ✓

**Step 4 — Compute**

\[\frac{0.25 \times 1000}{250}\text{ tablets} = \frac{250}{250} = 1\text{ tablet}\]

Yes — the order is equivalent to one tablet.

---

### Example 2 — Weight-based dose

Order: gentamicin 5 mg/kg. Patient weight: 176 lb.
What is the dose in mg?

**Step 1 — Information**

- Given: 176 lb
- Rate: 5 mg per kg
- Conversion: 1 kg = 2.2 lb
- Target: mg

**Step 2 — Write the factors**

\[\frac{176\text{ lb}}{1} \qquad \frac{1\text{ kg}}{2.2\text{ lb}} \qquad \frac{5\text{ mg}}{1\text{ kg}}\]

**Step 3 — Arrange and check**

\[176 \cancel{\text{ lb}} \times \frac{1 \cancel{\text{ kg}}}{2.2 \cancel{\text{ lb}}} \times \frac{5\text{ mg}}{1 \cancel{\text{ kg}}}\]

Surviving unit: **mg** ✓

**Step 4 — Compute**

\[\frac{176 \times 5}{2.2}\text{ mg} = \frac{880}{2.2} = 400\text{ mg}\]

---

### Example 3 — Volume conversion

An IV bag contains 1.5 L. The tubing set measures in mL.
How many mL is that?

**Step 1 — Information**

- Given: 1.5 L
- Conversion: 1 L = 1000 mL
- Target: mL

**Step 2 — Write the factors**

\[\frac{1.5\text{ L}}{1} \qquad \frac{1000\text{ mL}}{1\text{ L}}\]

**Step 3 — Arrange and check**

\[1.5 \cancel{\text{ L}} \times \frac{1000\text{ mL}}{1 \cancel{\text{ L}}}\]

Surviving unit: **mL** ✓

**Step 4 — Compute**

\[1.5 \times 1000 = 1500\text{ mL}\]

---

### Example 4 — Compound rate

Order: amoxicillin 40 mg/kg/day in 3 divided doses.
Patient weight: 22 kg. Stock: 125 mg per 5 mL.
How many mL per dose?

**Step 1 — Information**

- Given: 22 kg
- Rate: 40 mg per kg per day
- Divided into: 3 doses
- Stock: 125 mg per 5 mL
- Target: mL per dose

**Step 2 — Write the factors**

\[\frac{22\text{ kg}}{1} \qquad \frac{40\text{ mg}}{1\text{ kg}} \qquad \frac{1\text{ day}}{3\text{ doses}} \qquad \frac{5\text{ mL}}{125\text{ mg}}\]

**Step 3 — Arrange and check**

\[22 \cancel{\text{ kg}} \times \frac{40 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1\text{ day}}{3\text{ doses}} \times \frac{5\text{ mL}}{125 \cancel{\text{ mg}}}\]

Surviving units: **mL/dose** ✓

**Step 4 — Compute**

\[\frac{22 \times 40 \times 5}{3 \times 125} \frac{\text{mL}}{\text{dose}} = \frac{4400}{375} \approx 11.7\text{ mL per dose}\]

---

## Self-Check

<div class="self-check" id="rcp-self-check"></div>

<script type="application/json" id="rcp-self-check-data">
[
  {
    "id": "rcp-1",
    "question": "A problem states: 'Stock is 500 mg per 10 mL.' Which factor do you write to convert from mg to mL?",
    "options": [
      "50 mg / 1 mL (simplified)",
      "10 mL / 500 mg (as labeled)",
      "500 mg / 10 mL (as labeled)",
      "1 mL / 50 mg (simplified)"
    ],
    "correct": 1,
    "feedback": "Use the numbers as labeled: 10 mL / 500 mg. Simplifying before setting up the chain is an extra step that introduces error risk and disconnects the setup from the label."
  },
  {
    "id": "rcp-2",
    "question": "An order reads: 'gentamicin 2 mg/kg.' The patient weighs 80 kg. Which factor does the rate give you?",
    "options": [
      "80 kg / 1",
      "1 kg / 2 mg",
      "2 mg / 1 kg",
      "2 kg / 1 mg"
    ],
    "correct": 2,
    "feedback": "The rate 2 mg/kg means 2 mg per 1 kg, written as the factor 2 mg / 1 kg. The patient weight (80 kg) is the given value, not the factor."
  },
  {
    "id": "rcp-3",
    "question": "Before computing, what should you confirm in Step 3?",
    "options": [
      "That all units cancel",
      "That only the target unit survives",
      "That the numerators multiply to a round number",
      "That at least one unit cancels"
    ],
    "correct": 1,
    "feedback": "Every unit except the target unit must cancel. If any unwanted unit survives — or if the target unit cancels — the setup is wrong. Do not compute until Step 3 is clean."
  }
]
</script>
