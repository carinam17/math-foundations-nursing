# Weight-Based Dosing

Many medications are ordered based on the patient's body weight.
This ensures the dose is proportional to the patient's size,
minimizing the risk of under- or overdosing.

Weight-based orders are expressed as a dose per kilogram:

\[\text{mg/kg} \quad \text{or} \quad \text{mg/kg/day}\]

---

## Getting the Weight Right

!!! warning "Always use weight in kg"
    Clinical doses are calculated using weight in **kg**.
    If the patient's weight is recorded in lb, convert first:

    \[\text{lb} \times \frac{1 \text{ kg}}{2.2 \text{ lb}} = \text{kg}\]

    Never estimate weight for drug calculations —
    always use a measured, documented weight.

!!! danger "Pediatric weight verification"
    For pediatric patients, always verify the weight
    independently before calculating. A weight error
    in a child can result in a significant overdose.

---

## Two-Step Method

Weight-based calculations always have two steps:

1. **Calculate the dose** — multiply weight in kg by the ordered dose per kg
2. **Calculate the volume** — use the dose from step 1 and the stock ratio

**Example 1:**
Order: gentamicin 5 mg/kg IV
Patient weight: 70 kg
Stock: 40 mg/mL

Step 1 — dose:
\[70 \cancel{\text{ kg}} \times \frac{5 \text{ mg}}{1 \cancel{\text{ kg}}} = 350 \text{ mg}\]

Step 2 — volume:
\[350 \cancel{\text{ mg}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = 8.75 \text{ mL}\]

Round to nearest tenth: **8.8 mL**

---

## Single Chain Method

The same problem as one cancellation chain:

\[70 \cancel{\text{ kg}} \times \frac{5 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = \frac{350}{40} = 8.75 \text{ mL}\]

Round to nearest tenth: **8.8 mL**

---

## Weight Conversion Required

**Example 2:**
Order: vancomycin 15 mg/kg IV
Patient weight: 154 lb
Stock: 500 mg/10 mL

As a single chain:

\[154 \cancel{\text{ lb}} \times \frac{1 \cancel{\text{ kg}}}{2.2 \cancel{\text{ lb}}} \times \frac{15 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{10 \text{ mL}}{500 \cancel{\text{ mg}}} = 21 \text{ mL}\]

---

## Maximum Dose Checks

Some weight-based medications have a maximum dose — the
calculated dose should not exceed it regardless of weight.

!!! info "When a maximum applies"
    1. Calculate the weight-based dose normally
    2. Compare to the maximum dose
    3. Administer the **lower** of the two values

**Example 3:**
Order: ibuprofen 10 mg/kg orally, max 400 mg
Patient weight: 55 kg

Calculated dose:
\[55 \cancel{\text{ kg}} \times \frac{10 \text{ mg}}{1 \cancel{\text{ kg}}} = 550 \text{ mg}\]

550 mg exceeds the maximum of 400 mg. **Administer 400 mg.**

---

## Daily Dose vs Single Dose

!!! warning "Read the order carefully"
    Weight-based orders may specify:

    - **Per dose** — e.g. 5 mg/kg per dose every 8 hours
    - **Per day** — e.g. 15 mg/kg/day divided every 8 hours

    For a daily dose divided into multiple doses, divide the
    total daily dose by the number of doses per day to get
    the single dose.

**Example 4:**
Order: amoxicillin 40 mg/kg/day orally divided every 8 hours
Patient weight: 20 kg
Stock: 250 mg/5 mL

Step 1 — total daily dose:
\[20 \cancel{\text{ kg}} \times \frac{40 \text{ mg}}{1 \cancel{\text{ kg}}} = 800 \text{ mg/day}\]

Step 2 — single dose (every 8 hours = 3 doses/day):
\[800 \text{ mg/day} \times \frac{1 \text{ day}}{3 \text{ doses}} = 266.7 \text{ mg/dose}\]

Step 3 — volume per dose:
\[266.7 \cancel{\text{ mg}} \times \frac{5 \text{ mL}}{250 \cancel{\text{ mg}}} = 5.3 \text{ mL}\]

---

## Practice Problems

!!! example "Problem 1"
    Order: tobramycin 2 mg/kg IV
    Patient weight: 80 kg
    Stock: 10 mg/mL
    How many mL?

??? success "Answer"
    \[80 \cancel{\text{ kg}} \times \frac{2 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{10 \cancel{\text{ mg}}} = 16 \text{ mL}\]

!!! example "Problem 2"
    Order: gentamicin 4 mg/kg IV
    Patient weight: 176 lb
    Stock: 40 mg/mL
    How many mL?

??? success "Answer"
    \[176 \cancel{\text{ lb}} \times \frac{1 \cancel{\text{ kg}}}{2.2 \cancel{\text{ lb}}} \times \frac{4 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = 8 \text{ mL}\]

!!! example "Problem 3"
    Order: ibuprofen 10 mg/kg orally, max 600 mg
    Patient weight: 75 kg
    Stock: 200 mg/5 mL
    How many mL?

??? success "Answer"
    Calculated dose:
    \[75 \cancel{\text{ kg}} \times \frac{10 \text{ mg}}{1 \cancel{\text{ kg}}} = 750 \text{ mg}\]

    750 mg exceeds max of 600 mg — **use 600 mg**

    Volume:
    \[600 \cancel{\text{ mg}} \times \frac{5 \text{ mL}}{200 \cancel{\text{ mg}}} = 15 \text{ mL}\]

!!! example "Problem 4"
    Order: vancomycin 20 mg/kg/day IV divided every 12 hours
    Patient weight: 60 kg
    Stock: 500 mg/10 mL
    How many mL per dose?

??? success "Answer"
    Total daily dose:
    \[60 \cancel{\text{ kg}} \times \frac{20 \text{ mg}}{1 \cancel{\text{ kg}}} = 1200 \text{ mg/day}\]

    Single dose (every 12 hours = 2 doses/day):
    \[1200 \text{ mg/day} \times \frac{1 \text{ day}}{2 \text{ doses}} = 600 \text{ mg/dose}\]

    Volume:
    \[600 \cancel{\text{ mg}} \times \frac{10 \text{ mL}}{500 \cancel{\text{ mg}}} = 12 \text{ mL}\]

!!! example "Problem 5"
    Order: morphine 0.1 mg/kg IV PRN
    Patient weight: 132 lb
    Stock: 10 mg/mL
    How many mL?

??? success "Answer"
    \[132 \cancel{\text{ lb}} \times \frac{1 \cancel{\text{ kg}}}{2.2 \cancel{\text{ lb}}} \times \frac{0.1 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{10 \cancel{\text{ mg}}} = 0.6 \text{ mL}\]

!!! warning "Document the weight used"
    Record the patient's weight used for the calculation in your
    nursing notes. If the weight changes significantly — such as
    after surgery or with fluid shifts — notify the prescriber
    as the dose may need to be recalculated.

---

## Self-Check

<div class="self-check" id="wbd-self-check"></div>

<script type="application/json" id="wbd-self-check-data">
[
  {
    "id": "wbd-1",
    "question": "Order: gentamicin 3 mg/kg IV. Patient weight: 90 kg. Stock: 10 mg/mL. How many mL?",
    "options": ["2.7 mL", "27 mL", "30 mL", "3 mL"],
    "correct": 1,
    "feedback": "90 kg × (3 mg / 1 kg) × (1 mL / 10 mg) = 270 / 10 = 27 mL."
  },
  {
    "id": "wbd-2",
    "question": "Order: ibuprofen 10 mg/kg orally, max 400 mg. Patient weighs 55 kg. What dose do you administer?",
    "options": ["550 mg", "400 mg", "500 mg", "450 mg"],
    "correct": 1,
    "feedback": "Calculated dose: 55 kg × 10 mg/kg = 550 mg. This exceeds the 400 mg maximum. Administer 400 mg."
  },
  {
    "id": "wbd-3",
    "question": "Order: amoxicillin 30 mg/kg/day divided every 8 hours. Patient weighs 20 kg. What is the single dose?",
    "options": ["100 mg", "150 mg", "200 mg", "600 mg"],
    "correct": 2,
    "feedback": "Total daily dose: 20 kg × 30 mg/kg = 600 mg/day. Every 8 hours = 3 doses/day. Single dose: 600 / 3 = 200 mg."
  },
  {
    "id": "wbd-4",
    "question": "A patient's weight is documented as 165 lb. What is the first step before calculating a weight-based dose?",
    "options": [
      "Estimate the dose based on appearance",
      "Use 165 as the weight in the calculation",
      "Convert lb to kg using (165 lb × 1 kg / 2.2 lb)",
      "Round to the nearest 10 lb first"
    ],
    "correct": 2,
    "feedback": "165 lb × (1 kg / 2.2 lb) = 75 kg. Always convert to kg before calculating. Never use lb directly in a mg/kg calculation."
  }
]
</script>
