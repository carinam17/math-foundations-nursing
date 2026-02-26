# Weight-Based Dosing

## Overview

Many medications are ordered based on the patient's body 
weight. This ensures the dose is proportional to the 
patient's size, minimizing the risk of under or overdosing.

Weight-based orders are expressed as:

\[\text{dose per kg} \rightarrow \text{mg/kg}\]

## The Two-Step Process

Weight-based calculations always require two steps:

1. **Calculate the dose** — multiply weight in kg by the 
   ordered dose per kg
2. **Calculate the volume** — use the dose from step 1 
   to find how much to administer

These can be done separately or as a single unit 
cancellation chain.

## Getting the Weight Right

!!! warning "Always Weigh in kg"
    Clinical doses are calculated using weight in **kg**.
    If the patient's weight is recorded in lb, convert first:
    
    \[\text{kg} = \text{lb} \div 2.2\]
    
    Never estimate weight for drug calculations — 
    always use a measured, documented weight.

!!! danger "Pediatric Weight Verification"
    For pediatric patients, always verify the weight 
    independently before calculating. A weight error 
    in a child can result in a significant overdose.

## Two-Step Method

**Example 1:**
Order: gentamicin 5 mg/kg IV
Patient weight: 70 kg
Stock: 40 mg/mL

Step 1 — calculate dose:
\[70 \cancel{\text{ kg}} \times \frac{5 \text{ mg}}{1 \cancel{\text{ kg}}} = 350 \text{ mg}\]

Step 2 — calculate volume:
\[\frac{350 \cancel{\text{ mg}}}{1} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = 8.75 \text{ mL}\]

Round to nearest tenth: **8.8 mL**

## Single Chain Method

The same problem as one unit cancellation chain:

\[\frac{70 \cancel{\text{ kg}}}{1} \times \frac{5 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = \frac{350}{40} \text{ mL} = 8.75 \text{ mL}\]

Round to nearest tenth: **8.8 mL**

## Weight Conversion Required

**Example 2:**
Order: vancomycin 15 mg/kg IV
Patient weight: 154 lb
Stock: 500 mg/10 mL

Step 1 — convert weight:
\[154 \cancel{\text{ lb}} \times \frac{1 \text{ kg}}{2.2 \cancel{\text{ lb}}} = 70 \text{ kg}\]

Step 2 — calculate dose:
\[70 \cancel{\text{ kg}} \times \frac{15 \text{ mg}}{1 \cancel{\text{ kg}}} = 1050 \text{ mg}\]

Step 3 — calculate volume:
\[\frac{1050 \cancel{\text{ mg}}}{1} \times \frac{10 \text{ mL}}{500 \cancel{\text{ mg}}} = 21 \text{ mL}\]

Or as one chain:
\[\frac{154 \cancel{\text{ lb}}}{1} \times \frac{1 \cancel{\text{ kg}}}{2.2 \cancel{\text{ lb}}} \times \frac{15 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{10 \text{ mL}}{500 \cancel{\text{ mg}}} = 21 \text{ mL}\]

## Maximum Dose Checks

Some weight-based medications have a **maximum dose** — 
the dose should not exceed this regardless of weight.

!!! info "Maximum Dose"
    When a maximum dose applies:
    
    1. Calculate the weight-based dose normally
    2. Compare to the maximum dose
    3. Administer the **lower** of the two values
    
    **Example:**
    Order: ibuprofen 10 mg/kg orally, max 400 mg
    Patient weight: 55 kg
    
    Calculated dose:
    \[55 \cancel{\text{ kg}} \times \frac{10 \text{ mg}}{1 \cancel{\text{ kg}}} = 550 \text{ mg}\]
    
    550 mg exceeds the maximum of 400 mg.
    **Administer 400 mg.**

## Daily Dose vs Single Dose

!!! warning "Read the Order Carefully"
    Weight-based orders may specify:
    
    - **Per dose** — e.g. 5 mg/kg per dose every 8 hours
    - **Per day** — e.g. 15 mg/kg/day divided every 8 hours
    
    For a daily dose divided into multiple doses:
    \[\text{single dose} = \frac{\text{total daily dose}}{\text{number of doses per day}}\]

**Example:**
Order: amoxicillin 40 mg/kg/day orally divided every 8 hours
Patient weight: 20 kg
Stock: 250 mg/5 mL

Step 1 — total daily dose:
\[20 \cancel{\text{ kg}} \times \frac{40 \text{ mg}}{1 \cancel{\text{ kg}}} = 800 \text{ mg/day}\]

Step 2 — single dose (every 8 hours = 3 doses/day):
\[800 \text{ mg} \div 3 = 266.7 \text{ mg per dose}\]

Step 3 — volume per dose:
\[\frac{266.7 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{250 \cancel{\text{ mg}}} = 5.3 \text{ mL}\]

## Practice Problems

!!! example "Problem 1"
    Order: tobramycin 2 mg/kg IV
    Patient weight: 80 kg
    Stock: 10 mg/mL
    How many mL?

??? success "Answer"
    \[\frac{80 \cancel{\text{ kg}}}{1} \times \frac{2 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{10 \cancel{\text{ mg}}} = 16 \text{ mL}\]

!!! example "Problem 2"
    Order: gentamicin 4 mg/kg IV
    Patient weight: 176 lb
    Stock: 40 mg/mL
    How many mL?

??? success "Answer"
    Step 1 — convert weight:
    \[176 \cancel{\text{ lb}} \times \frac{1 \text{ kg}}{2.2 \cancel{\text{ lb}}} = 80 \text{ kg}\]
    
    Step 2 — full chain:
    \[\frac{80 \cancel{\text{ kg}}}{1} \times \frac{4 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = 8 \text{ mL}\]

!!! example "Problem 3"
    Order: ibuprofen 10 mg/kg orally, max 600 mg
    Patient weight: 75 kg
    Stock: 200 mg/5 mL
    How many mL?

??? success "Answer"
    Step 1 — calculated dose:
    \[75 \cancel{\text{ kg}} \times \frac{10 \text{ mg}}{1 \cancel{\text{ kg}}} = 750 \text{ mg}\]
    
    750 mg exceeds max of 600 mg — **use 600 mg**
    
    Step 2 — volume:
    \[\frac{600 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{200 \cancel{\text{ mg}}} = 15 \text{ mL}\]

!!! example "Problem 4"
    Order: vancomycin 20 mg/kg/day IV
    divided every 12 hours
    Patient weight: 60 kg
    Stock: 500 mg/10 mL
    How many mL per dose?

??? success "Answer"
    Step 1 — total daily dose:
    \[60 \cancel{\text{ kg}} \times \frac{20 \text{ mg}}{1 \cancel{\text{ kg}}} = 1200 \text{ mg/day}\]
    
    Step 2 — single dose (every 12 hours = 2 doses/day):
    \[1200 \div 2 = 600 \text{ mg per dose}\]
    
    Step 3 — volume:
    \[\frac{600 \cancel{\text{ mg}}}{1} \times \frac{10 \text{ mL}}{500 \cancel{\text{ mg}}} = 12 \text{ mL}\]

!!! example "Problem 5"
    Order: morphine 0.1 mg/kg IV PRN
    Patient weight: 132 lb
    Stock: 10 mg/mL
    How many mL?

??? success "Answer"
    Step 1 — convert weight:
    \[132 \cancel{\text{ lb}} \times \frac{1 \text{ kg}}{2.2 \cancel{\text{ lb}}} = 60 \text{ kg}\]
    
    Step 2 — full chain:
    \[\frac{60 \cancel{\text{ kg}}}{1} \times \frac{0.1 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{10 \cancel{\text{ mg}}} = 0.6 \text{ mL}\]

!!! warning "Clinical Tip"
    For weight-based medications, document the patient's 
    weight used for the calculation in your nursing notes. 
    If the weight changes significantly — such as after 
    surgery or with fluid shifts — notify the prescriber 
    as the dose may need to be recalculated.
