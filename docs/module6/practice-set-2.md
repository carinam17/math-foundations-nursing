# Practice Set 2 — Wrap-Up Challenge

## Instructions

This set simulates a real clinical competency exam.

- Problems are in **random mixed order** with no topic labels
- Numbers are harder than Set 1
- No hints are given
- Attempt every problem before revealing the answer
- Aim for **90% or higher** (23 out of 25 correct)

!!! danger "Challenge Yourself"
    Do not reveal answers until you have committed
    to your solution in writing. The goal is to
    identify gaps before clinical practice —
    not after.

---

!!! example "Problem 1"
    Order: atenolol 12.5 mg orally
    Stock: 25 mg per tablet
    How many tablets?

??? success "Answer"
    \[\frac{12.5 \cancel{\text{ mg}}}{1} \times \frac{1 \text{ tablet}}{25 \cancel{\text{ mg}}} = 0.5 \text{ tablet}\]

??? tip "Walkthrough"
    The conversion factor comes from the stock strength:
    25 mg = 1 tablet. Orient it with **mg in the denominator**
    so it cancels with the starting quantity:

    $$ \overfactor{\conv{12.5 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{tablet}}{25 \cn{\unit{mg}}}}{mg to tablet factor} = 0.5 \unit{tablet} $$

    **Quick mental check:** 12.5 mg is half of 25 mg, so the
    answer is half a tablet. ✓

    Verify the tablet is scored before splitting.

---

!!! example "Problem 2"
    Order: 750 mL 0.9% NaCl over 6 hours
    What is the flow rate in mL/hr?

??? success "Answer"
    \[\frac{750 \text{ mL}}{6 \text{ hr}} = 125 \text{ mL/hr}\]

??? tip "Walkthrough"
    Flow rate is **volume divided by time**:

    $$ \overfactor{\conv{750 \unit{mL}}{6 \unit{hr}}}{Volume \div Time} = 125 \unit{mL/hr} $$

    **Quick mental check:** 750 ÷ 6 = 125. ✓

---

!!! example "Problem 3"
    Order: tobramycin 2.5 mg/kg IV
    Patient weight: 198 lb
    Stock: 40 mg/mL
    How many mL?

??? success "Answer"
    Convert weight:
    \[\frac{198 \cancel{\text{ lb}}}{1} \times \frac{1 \text{ kg}}{2.2 \cancel{\text{ lb}}} = 90 \text{ kg}\]

    Full chain:
    \[\frac{90 \cancel{\text{ kg}}}{1} \times \frac{2.5 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{40 \cancel{\text{ mg}}} = 5.625 \text{ mL}\]

??? tip "Walkthrough"
    First convert the patient's weight from lb to kg, **then**
    chain weight → dose (mg) → volume (mL):

    $$ \overfactor{\conv{198 \cn{\unit{lb}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{kg}}{2.2 \cn{\unit{lb}}}}{lb to kg factor} = 90 \unit{kg} $$

    $$ \overfactor{\conv{90 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{2.5 \cn{\unit{mg}}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} \times \factor{\conv{1 \unit{mL}}{40 \cn{\unit{mg}}}}{mg to mL factor} = 5.625 \unit{mL} $$

    **Quick mental check:** 198 lb ÷ 2.2 = 90 kg.
    90 kg × 2.5 mg/kg = 225 mg, and
    225 mg ÷ 40 mg/mL ≈ 5.6 mL. ✓

    Round to: **5.6 mL**

---

!!! example "Problem 4"
    Convert 0.375 g to mcg.

??? success "Answer"
    \[\frac{0.375 \cancel{\text{ g}}}{1} \times \frac{1000 \cancel{\text{ mg}}}{1 \cancel{\text{ g}}} \times \frac{1000 \text{ mcg}}{1 \cancel{\text{ mg}}} = 375{,}000 \text{ mcg}\]

??? tip "Walkthrough"
    This is a two-step metric conversion: g → mg → mcg.
    Orient each factor so its denominator cancels the unit
    carried forward:

    $$ \overfactor{\conv{0.375 \cn{\unit{g}}}{1}}{Starting Quantity} \times \factor{\conv{1000 \cn{\unit{mg}}}{1 \cn{\unit{g}}}}{g to mg factor} \times \factor{\conv{1000 \unit{mcg}}{1 \cn{\unit{mg}}}}{mg to mcg factor} = 375{,}000 \unit{mcg} $$

    **Quick mental check:** g→mcg is six places to the right
    (×1,000,000). 0.375 × 1,000,000 = 375,000. ✓

---

!!! example "Problem 5"
    Order: clarithromycin 0.5 g orally
    Stock: 250 mg/5 mL
    How many mL?

??? success "Answer"
    \[\frac{0.5 \cancel{\text{ g}}}{1} \times \frac{1000 \cancel{\text{ mg}}}{1 \cancel{\text{ g}}} \times \frac{5 \text{ mL}}{250 \cancel{\text{ mg}}} = 10 \text{ mL}\]

??? tip "Walkthrough"
    The stock is in mg, but the order is in g — convert g
    to mg first, **then** apply the stock factor:

    $$ \overfactor{\conv{0.5 \cn{\unit{g}}}{1}}{Starting Quantity} \times \factor{\conv{1000 \cn{\unit{mg}}}{1 \cn{\unit{g}}}}{g to mg factor} \times \factor{\conv{5 \unit{mL}}{250 \cn{\unit{mg}}}}{mg to mL factor} = 10 \unit{mL} $$

    **Quick mental check:** 0.5 g = 500 mg, and 500 mg is
    double the 250 mg in 5 mL, so the answer is 10 mL. ✓

---

!!! example "Problem 6"
    Order: 500 mL over 35 minutes
    What is the flow rate in mL/hr?

??? success "Answer"
    Convert time:
    \[\frac{35 \cancel{\text{ min}}}{1} \times \frac{1 \text{ hr}}{60 \cancel{\text{ min}}} = 0.583 \text{ hr}\]

    Rate:
    \[\frac{500 \text{ mL}}{0.583 \text{ hr}} = 857.6 \text{ mL/hr}\]

??? tip "Walkthrough"
    Convert minutes to hours first, **then** divide volume
    by time:

    $$ \overfactor{\conv{35 \cn{\unit{min}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{hr}}{60 \cn{\unit{min}}}}{min to hr factor} = 0.583 \unit{hr} $$

    $$ \overfactor{\conv{500 \unit{mL}}{0.583 \unit{hr}}}{Volume \div Time} = 857.6 \unit{mL/hr} $$

    **Quick mental check:** 35 min ≈ 0.58 hr, and
    500 ÷ 0.583 ≈ 858. ✓

    Round to: **858 mL/hr**

    !!! warning "Verify This Rate"
        Rates above 500 mL/hr are unusual. Verify
        the order before programming the pump.

---

!!! example "Problem 7"
    Order: amoxicillin 30 mg/kg/day orally divided every 8 hours
    Patient: child weighing 16 kg
    Stock: 200 mg/5 mL
    How many mL per dose?

??? success "Answer"
    Total daily dose:
    \[\frac{16 \cancel{\text{ kg}}}{1} \times \frac{30 \text{ mg}}{1 \cancel{\text{ kg}}} = 480 \text{ mg/day}\]

    Single dose (every 8 hours = 3 doses/day):
    \[\frac{480 \text{ mg/day}}{1} \times \frac{1 \text{ day}}{3 \text{ doses}} = 160 \text{ mg/dose}\]

    Volume:
    \[\frac{160 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{200 \cancel{\text{ mg}}} = 4 \text{ mL}\]

??? tip "Walkthrough"
    This is a three-step chain: find the **total daily dose**,
    divide it into a **single dose**, then convert that dose
    to volume:

    $$ \overfactor{\conv{16 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{30 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 480 \unit{mg/day} $$

    $$ \overfactor{\conv{480 \unit{mg/day}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{day}}{3 \unit{doses}}}{day to dose factor} = 160 \unit{mg/dose} $$

    $$ \overfactor{\conv{160 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{5 \unit{mL}}{200 \cn{\unit{mg}}}}{mg to mL factor} = 4 \unit{mL} $$

    **Quick mental check:** 16 kg × 30 mg/kg = 480 mg/day.
    Divided into 3 doses = 160 mg/dose, and 160 mg is
    0.8 × 200 mg, so 0.8 × 5 mL = 4 mL. ✓

---

!!! example "Problem 8"
    Order: heparin 1800 units/hr IV
    Stock: 25,000 units in 250 mL 0.9% NaCl
    What is the flow rate in mL/hr?

??? success "Answer"
    Concentration:
    \[\frac{25{,}000 \text{ units}}{250 \text{ mL}} = 100 \text{ units/mL}\]

    Flow rate:
    \[\frac{1800 \cancel{\text{ units/hr}}}{1} \times \frac{1 \text{ mL}}{100 \cancel{\text{ units}}} = 18 \text{ mL/hr}\]

??? tip "Walkthrough"
    First find the stock's concentration (units per mL),
    **then** use it as the conversion factor for the ordered
    rate:

    $$ \overfactor{\conv{25{,}000 \unit{units}}{250 \unit{mL}}}{Total \div Volume} = 100 \unit{units/mL} $$

    $$ \overfactor{\conv{1800 \cn{\unit{units/hr}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{mL}}{100 \cn{\unit{units}}}}{units to mL factor} = 18 \unit{mL/hr} $$

    **Quick mental check:** 25,000 ÷ 250 = 100 units/mL.
    1800 ÷ 100 = 18 mL/hr. ✓

---

!!! example "Problem 9"
    A 1000 mL bag starts at 2130 running at 80 mL/hr.
    What time will it complete?

??? success "Answer"
    Infusion time:
    \[\frac{1000 \text{ mL}}{80 \text{ mL/hr}} = 12.5 \text{ hr}\]

    Convert decimal:
    \[\frac{0.5 \text{ hr}}{1} \times \frac{60 \text{ min}}{1 \text{ hr}} = 30 \text{ min}\]

    Completion time:
    \[2130 + 12 \text{ hr } 30 \text{ min} = 1000 \text{ next day}\]

??? tip "Walkthrough"
    First find the total infusion time (volume ÷ rate),
    convert the decimal-hour remainder to minutes, **then**
    add the total time to the start time:

    $$ \overfactor{\conv{1000 \unit{mL}}{80 \unit{mL/hr}}}{Volume \div Rate} = 12.5 \unit{hr} $$

    $$ \overfactor{\conv{0.5 \cn{\unit{hr}}}{1}}{Starting Quantity} \times \factor{\conv{60 \unit{min}}{1 \cn{\unit{hr}}}}{hr to min factor} = 30 \unit{min} $$

    $$ 2130 + 12 \unit{hr} \ 30 \unit{min} = 1000 \ \text{next day} $$

    **Quick mental check:** 1000 ÷ 80 = 12.5 hr = 12 hr 30 min.
    2130 + 12 hr 30 min crosses midnight to 1000 the next
    morning. ✓

    Completes at **1000 the following morning.**

---

!!! example "Problem 10"
    Order: digoxin 0.125 mg orally
    Stock: 62.5 mcg per tablet
    How many tablets?

??? success "Answer"
    \[\frac{0.125 \cancel{\text{ mg}}}{1} \times \frac{1000 \cancel{\text{ mcg}}}{1 \cancel{\text{ mg}}} \times \frac{1 \text{ tablet}}{62.5 \cancel{\text{ mcg}}} = 2 \text{ tablets}\]

??? tip "Walkthrough"
    The stock is in mcg, but the order is in mg — convert
    mg to mcg first, **then** apply the stock factor:

    $$ \overfactor{\conv{0.125 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{1000 \cn{\unit{mcg}}}{1 \cn{\unit{mg}}}}{mg to mcg factor} \times \factor{\conv{1 \unit{tablet}}{62.5 \cn{\unit{mcg}}}}{mcg to tablet factor} = 2 \unit{tablet} $$

    **Quick mental check:** 0.125 mg = 125 mcg, and 125 mcg
    is double the 62.5 mcg per tablet. ✓

---

!!! example "Problem 11"
    Order: 1000 mL Lactated Ringer's over 12 hours
    Tubing: 15 gtt/mL
    What is the drip rate in gtt/min?

??? success "Answer"
    Convert time:
    \[\frac{12 \cancel{\text{ hr}}}{1} \times \frac{60 \text{ min}}{1 \cancel{\text{ hr}}} = 720 \text{ min}\]

    Calculate:
    \[\frac{1000 \text{ mL}}{720 \text{ min}} \times 15 \text{ gtt/mL} = 20.8 \text{ gtt/min}\]

??? tip "Walkthrough"
    Convert the infusion time to minutes, then combine the
    rate (volume ÷ time) with the tubing's drop factor:

    $$ \overfactor{\conv{12 \cn{\unit{hr}}}{1}}{Starting Quantity} \times \factor{\conv{60 \unit{min}}{1 \cn{\unit{hr}}}}{hr to min factor} = 720 \unit{min} $$

    $$ \overfactor{\conv{1000 \unit{mL}}{720 \unit{min}}}{Volume \div Time} \times \factor{\conv{15 \unit{gtt}}{1 \unit{mL}}}{drop factor (tubing)} = 20.8 \unit{gtt/min} $$

    **Quick mental check:** 12 hr = 720 min.
    1000 ÷ 720 ≈ 1.39 mL/min, and 1.39 × 15 ≈ 20.8 gtt/min. ✓

    Round to: **21 gtt/min**

---

!!! example "Problem 12"
    Order: morphine 0.08 mg/kg IV PRN
    Patient weight: 187 lb
    Stock: 5 mg/mL
    How many mL? Round to nearest hundredth.

??? success "Answer"
    Convert weight:
    \[\frac{187 \cancel{\text{ lb}}}{1} \times \frac{1 \text{ kg}}{2.2 \cancel{\text{ lb}}} = 85 \text{ kg}\]

    Full chain:
    \[\frac{85 \cancel{\text{ kg}}}{1} \times \frac{0.08 \cancel{\text{ mg}}}{1 \cancel{\text{ kg}}} \times \frac{1 \text{ mL}}{5 \cancel{\text{ mg}}} = 1.36 \text{ mL}\]

??? tip "Walkthrough"
    First convert the patient's weight from lb to kg, **then**
    chain weight → dose (mg) → volume (mL):

    $$ \overfactor{\conv{187 \cn{\unit{lb}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{kg}}{2.2 \cn{\unit{lb}}}}{lb to kg factor} = 85 \unit{kg} $$

    $$ \overfactor{\conv{85 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{0.08 \cn{\unit{mg}}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} \times \factor{\conv{1 \unit{mL}}{5 \cn{\unit{mg}}}}{mg to mL factor} = 1.36 \unit{mL} $$

    **Quick mental check:** 187 lb ÷ 2.2 = 85 kg.
    85 kg × 0.08 mg/kg = 6.8 mg, and
    6.8 mg ÷ 5 mg/mL = 1.36 mL. ✓

---

!!! example "Problem 13"
    Convert 4.5 L to mL.

??? success "Answer"
    \[\frac{4.5 \cancel{\text{ L}}}{1} \times \frac{1000 \text{ mL}}{1 \cancel{\text{ L}}} = 4500 \text{ mL}\]

??? tip "Walkthrough"
    The conversion factor is 1 L = 1000 mL. Orient it with
    **L in the denominator** so it cancels:

    $ \overfactor{\conv{4.5 \cn{\unit{L}}}{1}}{Starting Quantity} \times \factor{\conv{1000 \unit{mL}}{1 \cn{\unit{L}}}}{L to mL factor} = 4500 \unit{mL} $

    **Quick mental check:** L→mL shifts the decimal three
    places to the right. 4.5 → 4500. ✓

---

!!! example "Problem 14"
    Order: dopamine 8 mcg/kg/min IV
    Patient weight: 75 kg
    Stock: dopamine 800 mg in 500 mL D5W
    What is the flow rate in mL/hr?

??? success "Answer"
    Dose per minute:
    \[\frac{75 \cancel{\text{ kg}}}{1} \times \frac{8 \text{ mcg}}{1 \cancel{\text{ kg}} \cdot \text{min}} = 600 \text{ mcg/min}\]

    Convert to mg/hr:
    \[\frac{600 \cancel{\text{ mcg/min}}}{1} \times \frac{1 \cancel{\text{ mg}}}{1000 \cancel{\text{ mcg}}} \times \frac{60 \text{ min}}{1 \text{ hr}} = 36 \text{ mg/hr}\]

    Concentration:
    \[\frac{800 \text{ mg}}{500 \text{ mL}} = 1.6 \text{ mg/mL}\]

    Flow rate:
    \[\frac{36 \cancel{\text{ mg/hr}}}{1} \times \frac{1 \text{ mL}}{1.6 \cancel{\text{ mg}}} = 22.5 \text{ mL/hr}\]

    Round to: **23 mL/hr**

??? tip "Walkthrough"
    This is a multi-step chain: first find the dose per minute,
    convert it to mg/hr, find the concentration of the stock,
    then divide to get the flow rate:

    $ \overfactor{\conv{75 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{8 \unit{mcg}}{1 \cn{\unit{kg}} \cdot min}}{kg to mcg/min factor} = 600 \unit{mcg/min} $

    $ \overfactor{\conv{600 \cn{\unit{mcg/min}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{mg}}{1000 \cn{\unit{mcg}}}}{mcg to mg factor} \times \factor{\conv{60 \unit{min}}{1 \unit{hr}}}{min to hr factor} = 36 \unit{mg/hr} $

    $ \overfactor{\conv{800 \unit{mg}}{500 \unit{mL}}}{Total \div Volume} = 1.6 \unit{mg/mL} $

    $ \overfactor{\conv{36 \cn{\unit{mg/hr}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{mL}}{1.6 \cn{\unit{mg}}}}{mg to mL factor} = 22.5 \unit{mL/hr} $

    **Quick mental check:** 75 kg × 8 mcg/kg/min = 600 mcg/min.
    600 mcg/min ÷ 1000 × 60 = 36 mg/hr. The stock is 1.6 mg/mL,
    so 36 ÷ 1.6 ≈ 22.5, rounded to 23 mL/hr. ✓

---

!!! example "Problem 15"
    Order: ibuprofen 10 mg/kg orally, max 400 mg
    Patient: child weighing 48 kg
    Stock: 100 mg/5 mL
    How many mL?

??? success "Answer"
    Calculated dose:
    \[\frac{48 \cancel{\text{ kg}}}{1} \times \frac{10 \text{ mg}}{1 \cancel{\text{ kg}}} = 480 \text{ mg}\]

    480 mg exceeds max of 400 mg — **use 400 mg**

    Volume:
    \[\frac{400 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{100 \cancel{\text{ mg}}} = 20 \text{ mL}\]

??? tip "Walkthrough"
    First find the calculated dose, then compare it against
    the maximum dose limit before converting to volume:

    $ \overfactor{\conv{48 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{10 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 480 \unit{mg} $

    480 mg exceeds the maximum of 400 mg, so **use 400 mg**:

    $ \overfactor{\conv{400 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{5 \unit{mL}}{100 \cn{\unit{mg}}}}{mg to mL factor} = 20 \unit{mL} $

    **Quick mental check:** 48 kg × 10 mg/kg = 480 mg, which is
    capped at 400 mg. 400 ÷ 100 × 5 = 20 mL. ✓

---

!!! example "Problem 16"
    A 750 mL bag started at 0730 running at 125 mL/hr.
    It is now 1130. How much fluid remains and what time
    will the infusion complete?

??? success "Answer"
    Time elapsed:
    \[1130 - 0730 = 4 \text{ hr}\]

    Volume infused:
    \[\frac{125 \text{ mL/hr}}{1} \times \frac{4 \text{ hr}}{1} = 500 \text{ mL}\]

    Volume remaining:
    \[750 - 500 = 250 \text{ mL}\]

    Time remaining:
    \[\frac{250 \text{ mL}}{125 \text{ mL/hr}} = 2 \text{ hr}\]

    Completion time:
    \[1130 + 2 \text{ hr} = 1330\]

    Completes at **1330 (1:30 PM).**

??? tip "Walkthrough"
    First find how much time has elapsed and how much fluid
    has already infused, then work out what's left and when
    it will finish:

    $ 1130 - 0730 = 4 \unit{hr} $

    $ \overfactor{\conv{125 \unit{mL/hr}}{1}}{Starting Quantity} \times \factor{\conv{4 \unit{hr}}{1}}{Rate \times Time} = 500 \unit{mL} $

    $ 750 - 500 = 250 \unit{mL} $

    $ \overfactor{\conv{250 \unit{mL}}{125 \unit{mL/hr}}}{Volume \div Rate} = 2 \unit{hr} $

    $ 1130 + 2 \unit{hr} = 1330 $

    **Quick mental check:** 4 hours at 125 mL/hr = 500 mL
    infused, leaving 250 mL. At 125 mL/hr that's another
    2 hours, so it finishes 2 hours after 1130, at 1330. ✓

---

!!! example "Problem 17"
    Order: vancomycin 20 mg/kg IV over 90 minutes
    Patient weight: 220 lb
    Stock: 500 mg/10 mL
    What is the total dose in mg and the flow rate in mL/hr?

??? success "Answer"
    Convert weight:
    \[\frac{220 \cancel{\text{ lb}}}{1} \times \frac{1 \text{ kg}}{2.2 \cancel{\text{ lb}}} = 100 \text{ kg}\]

    Total dose:
    \[\frac{100 \cancel{\text{ kg}}}{1} \times \frac{20 \text{ mg}}{1 \cancel{\text{ kg}}} = 2000 \text{ mg}\]

    Volume to infuse:
    \[\frac{2000 \cancel{\text{ mg}}}{1} \times \frac{10 \text{ mL}}{500 \cancel{\text{ mg}}} = 40 \text{ mL}\]

    Convert time:
    \[\frac{90 \cancel{\text{ min}}}{1} \times \frac{1 \text{ hr}}{60 \cancel{\text{ min}}} = 1.5 \text{ hr}\]

    Flow rate:
    \[\frac{40 \text{ mL}}{1.5 \text{ hr}} = 26.7 \text{ mL/hr}\]

    Round to: **27 mL/hr**

??? tip "Walkthrough"
    First convert the patient's weight to kg, then find the
    total dose and the volume to infuse, then convert the
    infusion time to hours to get the flow rate:

    $ \overfactor{\conv{220 \cn{\unit{lb}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{kg}}{2.2 \cn{\unit{lb}}}}{lb to kg factor} = 100 \unit{kg} $

    $ \overfactor{\conv{100 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{20 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 2000 \unit{mg} $

    $ \overfactor{\conv{2000 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{10 \unit{mL}}{500 \cn{\unit{mg}}}}{mg to mL factor} = 40 \unit{mL} $

    $ \overfactor{\conv{90 \cn{\unit{min}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{hr}}{60 \cn{\unit{min}}}}{min to hr factor} = 1.5 \unit{hr} $

    $ \overfactor{\conv{40 \unit{mL}}{1.5 \unit{hr}}}{Volume \div Time} = 26.7 \unit{mL/hr} $

    **Quick mental check:** 220 lb ÷ 2.2 = 100 kg.
    100 kg × 20 mg/kg = 2000 mg, and 2000 mg ÷ 500 mg × 10 mL =
    40 mL. 90 min = 1.5 hr, so 40 ÷ 1.5 ≈ 26.7, rounded to
    27 mL/hr. ✓

---

!!! example "Problem 18"
    Order: gentamicin 6 mg/kg/day IV divided every 8 hours
    Patient weight: 66 kg
    Stock: 10 mg/mL
    How many mL per dose?

??? success "Answer"
    Total daily dose:
    \[\frac{66 \cancel{\text{ kg}}}{1} \times \frac{6 \text{ mg}}{1 \cancel{\text{ kg}}} = 396 \text{ mg/day}\]

    Single dose (every 8 hours = 3 doses/day):
    \[\frac{396 \text{ mg/day}}{1} \times \frac{1 \text{ day}}{3 \text{ doses}} = 132 \text{ mg/dose}\]

    Volume:
    \[\frac{132 \cancel{\text{ mg}}}{1} \times \frac{1 \text{ mL}}{10 \cancel{\text{ mg}}} = 13.2 \text{ mL}\]

??? tip "Walkthrough"
    First find the total daily dose, then divide by the number
    of doses per day, then convert the single dose to volume:

    $ \overfactor{\conv{66 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{6 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 396 \unit{mg/day} $

    $ \overfactor{\conv{396 \unit{mg/day}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{day}}{3 \unit{doses}}}{day to doses factor} = 132 \unit{mg/dose} $

    $ \overfactor{\conv{132 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{mL}}{10 \cn{\unit{mg}}}}{mg to mL factor} = 13.2 \unit{mL} $

    **Quick mental check:** 66 kg × 6 mg/kg = 396 mg/day.
    396 ÷ 3 doses = 132 mg/dose, and 132 mg ÷ 10 mg/mL =
    13.2 mL. ✓

---

!!! example "Problem 19"
    Order: 500 mL over 4 hours
    Tubing: 10 gtt/mL
    What is the drip rate in gtt/min?

??? success "Answer"
    Convert time:
    \[\frac{4 \cancel{\text{ hr}}}{1} \times \frac{60 \text{ min}}{1 \cancel{\text{ hr}}} = 240 \text{ min}\]

    Calculate:
    \[\frac{500 \text{ mL}}{240 \text{ min}} \times 10 \text{ gtt/mL} = 20.8 \text{ gtt/min}\]

    Round to: **21 gtt/min**

??? tip "Walkthrough"
    First convert the infusion time to minutes, then divide
    the volume by time and multiply by the drop factor:

    $ \overfactor{\conv{4 \cn{\unit{hr}}}{1}}{Starting Quantity} \times \factor{\conv{60 \unit{min}}{1 \cn{\unit{hr}}}}{hr to min factor} = 240 \unit{min} $

    $ \overfactor{\conv{500 \unit{mL}}{240 \unit{min}}}{Volume \div Time} \times \factor{\conv{10 \unit{gtt}}{1 \unit{mL}}}{drop factor (tubing)} = 20.8 \unit{gtt/min} $

    **Quick mental check:** 4 hr = 240 min. 500 mL ÷ 240 min ≈
    2.08 mL/min, × 10 gtt/mL ≈ 20.8, rounded to 21 gtt/min. ✓

---

!!! example "Problem 20"
    An IV is running at 40 mL/hr.
    Stock: heparin 25,000 units in 500 mL
    What dose is the patient receiving per hour?

??? success "Answer"
    Concentration:
    \[\frac{25{,}000 \text{ units}}{500 \text{ mL}} = 50 \text{ units/mL}\]

    Dose rate:
    \[\frac{40 \text{ mL/hr}}{1} \times \frac{50 \text{ units/mL}}{1} = 2000 \text{ units/hr}\]

??? tip "Walkthrough"
    First find the concentration of the stock, then multiply
    the running rate by the concentration to get the dose
    being delivered per hour:

    $ \overfactor{\conv{25000 \unit{units}}{500 \unit{mL}}}{Total \div Volume} = 50 \unit{units/mL} $

    $ \overfactor{\conv{40 \unit{mL/hr}}{1}}{Starting Quantity} \times \factor{\conv{50 \unit{units/mL}}{1}}{concentration factor} = 2000 \unit{units/hr} $

    **Quick mental check:** 25,000 units in 500 mL is
    50 units/mL. At 40 mL/hr, that's 40 × 50 = 2000 units/hr. ✓

---

!!! example "Problem 21"
    Order: prednisolone 2 mg/kg/day orally divided every 12 hours
    Patient: child weighing 14 kg
    Stock: 5 mg/5 mL solution
    How many mL per dose?

??? success "Answer"
    Total daily dose:
    \[\frac{14 \cancel{\text{ kg}}}{1} \times \frac{2 \text{ mg}}{1 \cancel{\text{ kg}}} = 28 \text{ mg/day}\]

    Single dose (every 12 hours = 2 doses/day):
    \[\frac{28 \text{ mg/day}}{1} \times \frac{1 \text{ day}}{2 \text{ doses}} = 14 \text{ mg/dose}\]

    Volume:
    \[\frac{14 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{5 \cancel{\text{ mg}}} = 14 \text{ mL}\]

??? tip "Walkthrough"
    First find the total daily dose, then divide by the number
    of doses per day, then convert the single dose to volume:

    $ \overfactor{\conv{14 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{2 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 28 \unit{mg/day} $

    $ \overfactor{\conv{28 \unit{mg/day}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{day}}{2 \unit{doses}}}{day to doses factor} = 14 \unit{mg/dose} $

    $ \overfactor{\conv{14 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{5 \unit{mL}}{5 \cn{\unit{mg}}}}{mg to mL factor} = 14 \unit{mL} $

    **Quick mental check:** 14 kg × 2 mg/kg = 28 mg/day.
    28 ÷ 2 doses = 14 mg/dose, and since the stock is a 1:1
    ratio (5 mg per 5 mL), 14 mg = 14 mL. ✓

---

!!! example "Problem 22"
    Order: morphine 4 mg/hr IV continuous
    Stock: morphine 100 mg in 500 mL 0.9% NaCl
    What is the flow rate in mL/hr?

??? success "Answer"
    Concentration:
    \[\frac{100 \text{ mg}}{500 \text{ mL}} = 0.2 \text{ mg/mL}\]

    Flow rate:
    \[\frac{4 \cancel{\text{ mg/hr}}}{1} \times \frac{1 \text{ mL}}{0.2 \cancel{\text{ mg}}} = 20 \text{ mL/hr}\]

??? tip "Walkthrough"
    First find the concentration of the stock, then divide
    the ordered dose rate by the concentration to get the
    flow rate:

    $ \overfactor{\conv{100 \unit{mg}}{500 \unit{mL}}}{Total \div Volume} = 0.2 \unit{mg/mL} $

    $ \overfactor{\conv{4 \cn{\unit{mg/hr}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{mL}}{0.2 \cn{\unit{mg}}}}{mg to mL factor} = 20 \unit{mL/hr} $

    **Quick mental check:** 100 mg in 500 mL is 0.2 mg/mL.
    4 mg/hr ÷ 0.2 mg/mL = 20 mL/hr. ✓

---

!!! example "Problem 23"
    Order: 1000 mL over 10 hours. After 6 hours only 500 mL has
    infused. 500 mL remains with 4 hours left on the order.
    What rate is needed to complete on time?
    Is this within the 25% adjustment guideline?

??? success "Answer"
    Required rate:
    \[\frac{500 \text{ mL}}{4 \text{ hr}} = 125 \text{ mL/hr}\]

    Original rate:
    \[\frac{1000 \text{ mL}}{10 \text{ hr}} = 100 \text{ mL/hr}\]

    Percentage increase:
    \[\frac{125 - 100}{100} \times 100 = 25\%\]

    Exactly 25% — at the limit of the guideline.
    **Consult the prescriber before adjusting.**

    !!! info "25% adjustment guideline"
        Many facilities use a policy that IV rates should
        not be increased by more than 25% without prescriber
        notification. This is a clinical practice standard,
        not a universal rule — always follow your
        facility's specific policy.

??? tip "Walkthrough"
    First find the rate needed to finish on time, then compare
    it to the original ordered rate to find the percentage
    change:

    $ \overfactor{\conv{500 \unit{mL}}{4 \unit{hr}}}{Volume \div Time} = 125 \unit{mL/hr} $

    $ \overfactor{\conv{1000 \unit{mL}}{10 \unit{hr}}}{Volume \div Time} = 100 \unit{mL/hr} $

    $ \frac{125 - 100}{100} \times 100 = 25\% $

    **Quick mental check:** The new rate (125 mL/hr) is 25
    mL/hr more than the original (100 mL/hr), and 25 is 25%
    of 100 — exactly at the guideline limit, so the prescriber
    should be consulted. ✓

---

!!! example "Problem 24"
    Convert 2 tbsp to mL then to L.

??? success "Answer"
    tbsp to mL:
    \[\frac{2 \cancel{\text{ tbsp}}}{1} \times \frac{15 \text{ mL}}{1 \cancel{\text{ tbsp}}} = 30 \text{ mL}\]

    mL to L:
    \[\frac{30 \cancel{\text{ mL}}}{1} \times \frac{1 \text{ L}}{1000 \cancel{\text{ mL}}} = 0.03 \text{ L}\]

??? tip "Walkthrough"
    This is a two-step conversion: first tbsp to mL, then
    mL to L:

    $ \overfactor{\conv{2 \cn{\unit{tbsp}}}{1}}{Starting Quantity} \times \factor{\conv{15 \unit{mL}}{1 \cn{\unit{tbsp}}}}{tbsp to mL factor} = 30 \unit{mL} $

    $ \overfactor{\conv{30 \cn{\unit{mL}}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{L}}{1000 \cn{\unit{mL}}}}{mL to L factor} = 0.03 \unit{L} $

    **Quick mental check:** 1 tbsp = 15 mL, so 2 tbsp = 30 mL.
    mL→L shifts the decimal three places left: 30 → 0.03. ✓

---

!!! example "Problem 25"
    Safe dose range: 15–30 mg/kg/day
    Order: amoxicillin 20 mg/kg/day divided every 8 hours
    Patient: child weighing 27 kg
    Stock: 250 mg/5 mL
    Is the dose safe? If yes, how many mL per dose?

??? success "Answer"
    Minimum safe dose:
    \[\frac{27 \cancel{\text{ kg}}}{1} \times \frac{15 \text{ mg}}{1 \cancel{\text{ kg}}} = 405 \text{ mg/day}\]

    Maximum safe dose:
    \[\frac{27 \cancel{\text{ kg}}}{1} \times \frac{30 \text{ mg}}{1 \cancel{\text{ kg}}} = 810 \text{ mg/day}\]

    Ordered dose:
    \[\frac{27 \cancel{\text{ kg}}}{1} \times \frac{20 \text{ mg}}{1 \cancel{\text{ kg}}} = 540 \text{ mg/day}\]

    540 mg/day falls between 405 and 810 mg/day ✓
    **Dose is safe.**

    Single dose (every 8 hours = 3 doses/day):
    \[\frac{540 \text{ mg/day}}{1} \times \frac{1 \text{ day}}{3 \text{ doses}} = 180 \text{ mg/dose}\]

    Volume:
    \[\frac{180 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{250 \cancel{\text{ mg}}} = 3.6 \text{ mL}\]

??? tip "Walkthrough"
    First check the ordered dose against the safe range by
    calculating the minimum, maximum, and ordered daily doses,
    then divide the ordered dose into individual doses and
    convert to volume:

    $ \overfactor{\conv{27 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{15 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 405 \unit{mg/day} $

    $ \overfactor{\conv{27 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{30 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 810 \unit{mg/day} $

    $ \overfactor{\conv{27 \cn{\unit{kg}}}{1}}{Starting Quantity} \times \factor{\conv{20 \unit{mg}}{1 \cn{\unit{kg}}}}{kg to mg factor (dose)} = 540 \unit{mg/day} $

    540 mg/day falls between 405 and 810 mg/day, so the dose
    is safe:

    $ \overfactor{\conv{540 \unit{mg/day}}{1}}{Starting Quantity} \times \factor{\conv{1 \unit{day}}{3 \unit{doses}}}{day to doses factor} = 180 \unit{mg/dose} $

    $ \overfactor{\conv{180 \cn{\unit{mg}}}{1}}{Starting Quantity} \times \factor{\conv{5 \unit{mL}}{250 \cn{\unit{mg}}}}{mg to mL factor} = 3.6 \unit{mL} $

    **Quick mental check:** 27 kg × 15–30 mg/kg gives a safe
    range of 405–810 mg/day. The ordered 27 × 20 = 540 mg/day
    fits inside that range. 540 ÷ 3 doses = 180 mg/dose, and
    180 ÷ 250 × 5 = 3.6 mL. ✓

---

!!! tip "How Did You Do?"
    - **23–25 correct** — excellent, you are ready for clinical practice
    - **20–22 correct** — good, review the topics you missed and retry
    - **Below 20** — return to the relevant modules for review

    !!! warning "Remember"
        Clinical competency requires 90% or higher —
        23 out of 25 correct. If you are not there yet,
        that is what review is for. Keep practicing.
