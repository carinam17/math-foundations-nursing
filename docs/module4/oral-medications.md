# Oral Medications

Oral medications are the most common route of administration
in healthcare. They come in many forms: tablets, capsules,
and caplets, and require accurate calculation to ensure the
correct dose is given.

---

## Medication Orders

Medication orders contain:

| Component | Example |
|---|---|
| Patient name | John Smith |
| Medication name | metoprolol |
| Dose | 25 mg |
| Route | orally (PO) |
| Frequency | twice daily (BID) |
| Prescriber signature | Dr. Jones |

## Reading the Stock Label

The stock label tells you what is available:

| Component | Example |
|---|---|
| Medication name | metoprolol tartrate |
| Strength | 25 mg per tablet |
| Form | tablet |
| Total quantity | 100 tablets |

---

## Calculating Dosages — Tablets and Capsules

**Example 1 — whole tablet result:**
Order: metoprolol 50 mg orally
Stock: 25 mg per tablet

\[50 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{25 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

**Example 2 — partial tablet result:**
Order: lisinopril 5 mg orally
Stock: 10 mg per tablet

\[5 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{10 \cancel{\text{ mg}}} = 0.5 \text{ tablet}\]

!!! info "Scored vs unscored tablets"
    - **Scored tablets** have a line across the middle and are
      designed to be split — 0.5 tablet is acceptable
    - **Unscored tablets** should never be split
    - **Enteric coated tablets** should never be split or crushed
    - **Capsules** should never be split unless specifically
      formulated as sprinkle capsules

**Example 3 — unit conversion required:**
Order: levothyroxine 0.1 mg orally
Stock: 50 mcg per tablet

\[0.1 \cancel{\text{ mg}} \times \frac{1000 \cancel{\text{ mcg}}}{1 \cancel{\text{ mg}}} \times \frac{1 \text{ tablet}}{50 \cancel{\text{ mcg}}} = 2 \text{ tablets}\]

**Example 4 — higher stock strength:**
Order: atorvastatin 20 mg orally
Stock: 40 mg per tablet

\[20 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{40 \cancel{\text{ mg}}} = 0.5 \text{ tablet}\]

---

## Daily and Multi-Dose Calculations

**Example 5:**
Order: metformin 500 mg orally three times daily for 7 days
Stock: 500 mg per tablet
How many tablets for the full course?

Step 1 — tablets per dose:
\[500 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{500 \cancel{\text{ mg}}} = 1 \text{ tablet per dose}\]

Step 2 — total tablets:
\[1 \text{ tablet} \times 3 \text{ doses/day} \times 7 \text{ days} = 21 \text{ tablets}\]

---

## Reasonableness Check

!!! warning "Tablet safety guidelines"
    Verify your setup and consult before administering if:

    - Result is **more than 3 tablets** per dose
    - Result is **less than 0.5 tablet** per dose
    - Answer is not a multiple of 0.5
    - Never crush or split a medication without verifying it is safe

---

## Practice Problems

!!! example "Problem 1"
    Order: atenolol 100 mg orally
    Stock: 50 mg per tablet
    How many tablets?

??? success "Answer"
    \[100 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{50 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

!!! example "Problem 2"
    Order: warfarin 2.5 mg orally
    Stock: 5 mg per tablet
    How many tablets?

??? success "Answer"
    \[2.5 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{5 \cancel{\text{ mg}}} = 0.5 \text{ tablet}\]

    Verify the tablet is scored before splitting.

!!! example "Problem 3"
    Order: levothyroxine 0.075 mg orally
    Stock: 25 mcg per tablet
    How many tablets?

??? success "Answer"
    \[0.075 \cancel{\text{ mg}} \times \frac{1000 \cancel{\text{ mcg}}}{1 \cancel{\text{ mg}}} \times \frac{1 \text{ tablet}}{25 \cancel{\text{ mcg}}} = 3 \text{ tablets}\]

!!! example "Problem 4"
    Order: prednisone 40 mg orally
    Stock: 20 mg per tablet
    How many tablets?

??? success "Answer"
    \[40 \cancel{\text{ mg}} \times \frac{1 \text{ tablet}}{20 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

!!! example "Problem 5"
    Order: amoxicillin 500 mg orally three times daily for 10 days
    Stock: 250 mg per capsule
    How many capsules for the full course?

??? success "Answer"
    Step 1 — capsules per dose:
    \[500 \cancel{\text{ mg}} \times \frac{1 \text{ capsule}}{250 \cancel{\text{ mg}}} = 2 \text{ capsules per dose}\]

    Step 2 — total capsules:
    \[2 \times 3 \times 10 = 60 \text{ capsules}\]

!!! example "Problem 6 — flag this answer"
    Order: digoxin 0.5 mg orally
    Stock: 62.5 mcg per tablet
    How many tablets?

??? success "Answer"
    \[0.5 \cancel{\text{ mg}} \times \frac{1000 \cancel{\text{ mcg}}}{1 \cancel{\text{ mg}}} \times \frac{1 \text{ tablet}}{62.5 \cancel{\text{ mcg}}} = 8 \text{ tablets}\]

    !!! danger "Flag this"
        8 tablets is far outside the reasonable range.
        Verify the order, recheck the stock concentration,
        and consult the prescriber or pharmacist before
        administering.

!!! warning "Three-check rule"
    Read the medication label:

    1. When retrieving the medication from storage
    2. When preparing the dose
    3. Before administering to the patient

---

## Self-Check

<div class="self-check" id="oral-self-check"></div>

<script type="application/json" id="oral-self-check-data">
[
  {
    "id": "oral-1",
    "question": "Order: metoprolol 75 mg orally. Stock: 25 mg per tablet. How many tablets?",
    "options": ["1 tablet", "2 tablets", "3 tablets", "0.5 tablet"],
    "correct": 2,
    "feedback": "75 mg × (1 tablet / 25 mg) = 3 tablets. This is at the upper limit — worth a reasonableness check before administering."
  },
  {
    "id": "oral-2",
    "question": "Order: levothyroxine 0.05 mg orally. Stock: 50 mcg per tablet. How many tablets?",
    "options": ["0.5 tablet", "1 tablet", "2 tablets", "5 tablets"],
    "correct": 1,
    "feedback": "0.05 mg × (1000 mcg / 1 mg) × (1 tablet / 50 mcg) = 50 mcg / 50 mcg = 1 tablet. Convert mg to mcg first so units match the stock label."
  },
  {
    "id": "oral-3",
    "question": "A calculation yields 4 tablets for a single oral dose. What is the correct next step?",
    "options": [
      "Administer — the math is correct",
      "Round down to 3 tablets",
      "Verify the order and stock before administering",
      "Split two of the tablets to reduce the count"
    ],
    "correct": 2,
    "feedback": "4 tablets exceeds the typical 1–3 tablet range. Do not administer without verifying the order and stock concentration with a second nurse or pharmacist."
  },
  {
    "id": "oral-4",
    "question": "Order: warfarin 5 mg orally. Stock: 2 mg scored tablet. How many tablets?",
    "options": ["1 tablet", "2 tablets", "2.5 tablets", "0.4 tablet"],
    "correct": 2,
    "feedback": "5 mg × (1 tablet / 2 mg) = 2.5 tablets. The tablet is scored so splitting is acceptable — but warfarin is a high alert medication and requires independent double-check."
  }
]
</script>
