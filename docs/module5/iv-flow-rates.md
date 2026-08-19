# IV Flow Rates

An IV flow rate tells you how many milliliters of fluid to deliver
per hour (mL/hr). This is the standard unit for programming
electronic infusion pumps in clinical practice.

---

## The Basic Relationship

\[\text{Flow rate (mL/hr)} = \frac{\text{Volume (mL)}}{\text{Time (hr)}}\]

---

## Simple Flow Rate Calculations

**Example 1:**
Order: 1000 mL 0.9% NaCl over 8 hours

\[\frac{1000 \text{ mL}}{8 \text{ hr}} = 125 \text{ mL/hr}\]

**Example 2:**
Order: 500 mL D5W over 4 hours

\[\frac{500 \text{ mL}}{4 \text{ hr}} = 125 \text{ mL/hr}\]

**Example 3:**
Order: 250 mL 0.45% NaCl over 3 hours

\[\frac{250 \text{ mL}}{3 \text{ hr}} = 83.3 \text{ mL/hr}\]

Round to nearest whole number: **83 mL/hr**

!!! info "Rounding IV rates"
    IV pump rates are set in **whole numbers** (mL/hr).
    Always round to the nearest whole number unless your
    facility pump supports decimal rates.

---

## Time Conversion

Orders are sometimes written in minutes rather than hours.

**Example 4:**
Order: 100 mL 0.9% NaCl over 30 minutes

\[30 \cancel{\text{ min}} \times \frac{1 \text{ hr}}{60 \cancel{\text{ min}}} = 0.5 \text{ hr}\]

\[\frac{100 \text{ mL}}{0.5 \text{ hr}} = 200 \text{ mL/hr}\]

**Example 5:**
Order: 250 mL over 90 minutes

\[90 \cancel{\text{ min}} \times \frac{1 \text{ hr}}{60 \cancel{\text{ min}}} = 1.5 \text{ hr}\]

\[\frac{250 \text{ mL}}{1.5 \text{ hr}} = 166.7 \text{ mL/hr}\]

Round to: **167 mL/hr**

---

## Calculating Volume from Rate and Time

\[\text{Volume (mL)} = \text{Rate (mL/hr)} \times \text{Time (hr)}\]

**Example 6:**
An IV is running at 125 mL/hr. How much fluid will the patient
receive in 6 hours?

\[125 \text{ mL/hr} \times 6 \text{ hr} = 750 \text{ mL}\]

---

## Remaining Volume and Time

**Example 7:**
A 1000 mL IV is running at 125 mL/hr. After 3 hours, how much
fluid remains and how much longer will it run?

Volume infused:
\[125 \text{ mL/hr} \times 3 \text{ hr} = 375 \text{ mL}\]

Volume remaining:
\[1000 \text{ mL} - 375 \text{ mL} = 625 \text{ mL}\]

Time remaining:
\[\frac{625 \text{ mL}}{125 \text{ mL/hr}} = 5 \text{ hr}\]

---

## Pump Programming

!!! warning "Verify pump settings"
    When programming an IV pump always verify:

    1. **Rate** — mL/hr matches your calculation
    2. **Volume to be infused (VTBI)** — total volume of the bag
    3. **Drug library** — if pump has one, select the correct drug
    4. **Soft and hard limits** — ensure alerts are active
    5. **Second nurse check** — for high alert medications

!!! warning "Trace the line"
    After programming, trace the tubing from the bag to the
    patient before starting the infusion. This confirms the
    correct fluid is connected to the correct line.

---

## Practice Problems

!!! example "Problem 1"
    Order: 1000 mL Lactated Ringer's over 10 hours
    What is the flow rate in mL/hr?

??? success "Answer"
    \[\frac{1000 \text{ mL}}{10 \text{ hr}} = 100 \text{ mL/hr}\]

!!! example "Problem 2"
    Order: 500 mL 0.9% NaCl over 6 hours
    What is the flow rate in mL/hr?

??? success "Answer"
    \[\frac{500 \text{ mL}}{6 \text{ hr}} = 83.3 \text{ mL/hr}\]

    Round to: **83 mL/hr**

!!! example "Problem 3"
    Order: 150 mL 0.9% NaCl over 45 minutes
    What is the flow rate in mL/hr?

??? success "Answer"
    \[45 \cancel{\text{ min}} \times \frac{1 \text{ hr}}{60 \cancel{\text{ min}}} = 0.75 \text{ hr}\]

    \[\frac{150 \text{ mL}}{0.75 \text{ hr}} = 200 \text{ mL/hr}\]

!!! example "Problem 4"
    An IV is running at 100 mL/hr.
    How much fluid does the patient receive in 12 hours?

??? success "Answer"
    \[100 \text{ mL/hr} \times 12 \text{ hr} = 1200 \text{ mL}\]

!!! example "Problem 5"
    A 1000 mL bag is running at 150 mL/hr.
    After 4 hours, how much fluid remains and how much longer will it run?

??? success "Answer"
    Volume infused:
    \[150 \text{ mL/hr} \times 4 \text{ hr} = 600 \text{ mL}\]

    Volume remaining:
    \[1000 - 600 = 400 \text{ mL}\]

    Time remaining:
    \[\frac{400 \text{ mL}}{150 \text{ mL/hr}} = 2.67 \text{ hr}\]

    Convert decimal hours to minutes:
    \[0.67 \text{ hr} \times 60 \text{ min/hr} = 40 \text{ min}\]

    **2 hours and 40 minutes remaining.**

!!! example "Problem 6"
    Order: 250 mL over 20 minutes
    What is the flow rate in mL/hr?

??? success "Answer"
    \[20 \cancel{\text{ min}} \times \frac{1 \text{ hr}}{60 \cancel{\text{ min}}} = 0.33 \text{ hr}\]

    \[\frac{250 \text{ mL}}{0.33 \text{ hr}} = 757.6 \text{ mL/hr}\]

    Round to: **758 mL/hr**

    !!! warning "Verify this rate"
        Rates above 500 mL/hr are unusual. Verify the order
        and confirm with the prescriber before programming.

---

## Self-Check

<div class="self-check" id="ivfr-self-check"></div>

<script type="application/json" id="ivfr-self-check-data">
[
  {
    "id": "ivfr-1",
    "question": "Order: 750 mL 0.9% NaCl over 6 hours. What is the flow rate?",
    "options": ["100 mL/hr", "115 mL/hr", "125 mL/hr", "150 mL/hr"],
    "correct": 2,
    "feedback": "750 mL ÷ 6 hr = 125 mL/hr."
  },
  {
    "id": "ivfr-2",
    "question": "Order: 200 mL over 45 minutes. What is the flow rate in mL/hr?",
    "options": ["133 mL/hr", "200 mL/hr", "267 mL/hr", "300 mL/hr"],
    "correct": 2,
    "feedback": "45 min × (1 hr / 60 min) = 0.75 hr. 200 mL ÷ 0.75 hr = 266.7 mL/hr → 267 mL/hr."
  },
  {
    "id": "ivfr-3",
    "question": "An IV is running at 80 mL/hr. How much fluid is delivered in 8 hours?",
    "options": ["480 mL", "560 mL", "640 mL", "720 mL"],
    "correct": 2,
    "feedback": "80 mL/hr × 8 hr = 640 mL."
  },
  {
    "id": "ivfr-4",
    "question": "A 500 mL bag is running at 125 mL/hr. After 2 hours, how much time remains?",
    "options": ["1 hour", "2 hours", "3 hours", "4 hours"],
    "correct": 1,
    "feedback": "Volume infused: 125 × 2 = 250 mL. Remaining: 500 − 250 = 250 mL. Time: 250 ÷ 125 = 2 hours."
  }
]
</script>
