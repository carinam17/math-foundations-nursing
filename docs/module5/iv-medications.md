# IV Medications

## Overview

IV medications require an additional calculation step 
beyond standard fluid rates. You must calculate not only 
the flow rate but also the dose being delivered per unit 
of time — and verify it matches the order.

## Types of IV Medication Orders

| Order Type | Example |
|---|---|
| Fixed dose over time | vancomycin 1000 mg over 60 min |
| Continuous infusion by rate | heparin 1000 units/hr |
| Weight-based continuous | dopamine 5 mcg/kg/min |
| Intermittent piggyback (IVPB) | metronidazole 500 mg over 30 min |

## Concentration

IV medication concentrations are expressed as amount 
of drug per volume of fluid:

\[\text{Concentration} = \frac{\text{Amount of drug (mg, units, mcg)}}{\text{Volume (mL)}}\]

**Example:**
500 mg of drug mixed in 250 mL of fluid:

\[\frac{500 \text{ mg}}{250 \text{ mL}} = 2 \text{ mg/mL}\]

## Fixed Dose Over Time

**Example 1:**
Order: vancomycin 1000 mg in 250 mL over 90 minutes
What is the flow rate in mL/hr?

Convert time to hours:
\[90 \text{ min} \times \frac{1 \text{ hr}}{60 \text{ min}} = 1.5 \text{ hr}\]

Calculate rate:
\[\frac{250 \text{ mL}}{1.5 \text{ hr}} = 166.7 \text{ mL/hr}\]

Round to: **167 mL/hr**

**Example 2:**
Order: metronidazole 500 mg in 100 mL over 30 minutes
What is the flow rate in mL/hr?

\[30 \text{ min} \times \frac{1 \text{ hr}}{60 \text{ min}} = 0.5 \text{ hr}\]

\[\frac{100 \text{ mL}}{0.5 \text{ hr}} = 200 \text{ mL/hr}\]

## Continuous Infusion by Dose Rate

When an order specifies a dose rate (units/hr, mg/hr), 
calculate the flow rate from the concentration.

**Example 3:**
Order: heparin 1200 units/hr
Stock: heparin 25,000 units in 500 mL 0.9% NaCl

Step 1 — find concentration:
\[\frac{25{,}000 \text{ units}}{500 \text{ mL}} = 50 \text{ units/mL}\]

Step 2 — calculate flow rate:
\[\frac{1200 \text{ units/hr}}{50 \text{ units/mL}} = 24 \text{ mL/hr}\]

**Example 4:**
Order: morphine 2 mg/hr IV continuous
Stock: morphine 50 mg in 250 mL 0.9% NaCl

Step 1 — concentration:
\[\frac{50 \text{ mg}}{250 \text{ mL}} = 0.2 \text{ mg/mL}\]

Step 2 — flow rate:
\[\frac{2 \text{ mg/hr}}{0.2 \text{ mg/mL}} = 10 \text{ mL/hr}\]

## Weight-Based Continuous Infusions

Weight-based IV medications are ordered in 
mcg/kg/min or mcg/kg/hr.

**Example 5:**
Order: dopamine 5 mcg/kg/min IV
Patient weight: 70 kg
Stock: dopamine 400 mg in 250 mL D5W

Step 1 — calculate dose per minute:
\[70 \cancel{\text{ kg}} \times \frac{5 \text{ mcg}}{1 \cancel{\text{ kg}} \cdot \text{min}} = 350 \text{ mcg/min}\]

Step 2 — convert mcg/min to mg/hr:
\[350 \cancel{\text{ mcg/min}} \times \frac{1 \cancel{\text{ mg}}}{1000 \cancel{\text{ mcg}}} \times \frac{60 \text{ min}}{1 \text{ hr}} = 21 \text{ mg/hr}\]

Step 3 — find concentration:
\[\frac{400 \text{ mg}}{250 \text{ mL}} = 1.6 \text{ mg/mL}\]

Step 4 — calculate flow rate:
\[\frac{21 \text{ mg/hr}}{1.6 \text{ mg/mL}} = 13.125 \text{ mL/hr}\]

Round to: **13 mL/hr**

## Verifying Dose from Rate

Sometimes you need to verify what dose a patient 
is receiving from a running infusion.

\[\text{Dose rate} = \text{Flow rate (mL/hr)} \times \text{Concentration (drug/mL)}\]

**Example 6:**
An IV is running at 30 mL/hr.
Stock: 500 mg in 250 mL
What dose is the patient receiving per hour?

Step 1 — concentration:
\[\frac{500 \text{ mg}}{250 \text{ mL}} = 2 \text{ mg/mL}\]

Step 2 — dose rate:
\[30 \text{ mL/hr} \times 2 \text{ mg/mL} = 60 \text{ mg/hr}\]

## High Alert IV Medications

!!! danger "High Alert IV Medications"
    The following IV medications require independent 
    double checking of all calculations and pump settings:
    
    - **Heparin** — risk of serious bleeding
    - **Insulin** — risk of severe hypoglycemia
    - **Morphine and opioids** — risk of respiratory depression
    - **Dopamine and vasopressors** — risk of cardiovascular collapse
    - **Chemotherapy** — risk of severe toxicity
    - **Concentrated electrolytes** — risk of cardiac arrest
    
    Never administer these medications without a verified 
    independent double check.

## Practice Problems

!!! example "Problem 1"
    Order: ampicillin 500 mg in 100 mL over 30 minutes
    What is the flow rate in mL/hr?

??? success "Answer"
    \[30 \text{ min} = 0.5 \text{ hr}\]
    
    \[\frac{100 \text{ mL}}{0.5 \text{ hr}} = 200 \text{ mL/hr}\]

!!! example "Problem 2"
    Order: heparin 1500 units/hr IV
    Stock: 25,000 units in 500 mL 0.9% NaCl
    What is the flow rate in mL/hr?

??? success "Answer"
    Concentration:
    \[\frac{25{,}000 \text{ units}}{500 \text{ mL}} = 50 \text{ units/mL}\]
    
    Flow rate:
    \[\frac{1500 \text{ units/hr}}{50 \text{ units/mL}} = 30 \text{ mL/hr}\]

!!! example "Problem 3"
    Order: morphine 3 mg/hr IV continuous
    Stock: morphine 50 mg in 500 mL 0.9% NaCl
    What is the flow rate in mL/hr?

??? success "Answer"
    Concentration:
    \[\frac{50 \text{ mg}}{500 \text{ mL}} = 0.1 \text{ mg/mL}\]
    
    Flow rate:
    \[\frac{3 \text{ mg/hr}}{0.1 \text{ mg/mL}} = 30 \text{ mL/hr}\]

!!! example "Problem 4"
    Order: vancomycin 1500 mg in 500 mL over 3 hours
    What is the flow rate in mL/hr?

??? success "Answer"
    \[\frac{500 \text{ mL}}{3 \text{ hr}} = 166.7 \text{ mL/hr}\]
    
    Round to: **167 mL/hr**

!!! example "Problem 5"
    Order: dopamine 3 mcg/kg/min IV
    Patient weight: 80 kg
    Stock: dopamine 400 mg in 250 mL D5W
    What is the flow rate in mL/hr?

??? success "Answer"
    Step 1 — dose per minute:
    \[80 \cancel{\text{ kg}} \times \frac{3 \text{ mcg}}{1 \cancel{\text{ kg}} \cdot \text{min}} = 240 \text{ mcg/min}\]
    
    Step 2 — convert to mg/hr:
    \[240 \cancel{\text{ mcg/min}} \times \frac{1 \cancel{\text{ mg}}}{1000 \cancel{\text{ mcg}}} \times \frac{60 \text{ min}}{1 \text{ hr}} = 14.4 \text{ mg/hr}\]
    
    Step 3 — concentration:
    \[\frac{400 \text{ mg}}{250 \text{ mL}} = 1.6 \text{ mg/mL}\]
    
    Step 4 — flow rate:
    \[\frac{14.4 \text{ mg/hr}}{1.6 \text{ mg/mL}} = 9 \text{ mL/hr}\]

!!! example "Problem 6"
    An IV is running at 20 mL/hr.
    Stock: heparin 25,000 units in 500 mL
    What dose of heparin is the patient receiving per hour?

??? success "Answer"
    Concentration:
    \[\frac{25{,}000 \text{ units}}{500 \text{ mL}} = 50 \text{ units/mL}\]
    
    Dose rate:
    \[20 \text{ mL/hr} \times 50 \text{ units/mL} = 1000 \text{ units/hr}\]

!!! warning "Clinical Tip"
    When hanging a new IV medication always perform 
    a three-way check:
    
    1. Verify the **drug name and concentration** 
       on the bag matches the order
    2. Verify the **pump rate** matches your calculation
    3. Verify the **patient** using two identifiers 
       before connecting the line
    
    These three checks take less than 60 seconds 
    and prevent the most common IV medication errors.
