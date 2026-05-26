# Unit Cancellation

## Why Unit Cancellation Over Cross Multiplication?

Cross multiplication works for simple two-ratio problems but 
breaks down with multi-step calculations. Unit cancellation 
(dimensional analysis) works for **every** problem — simple 
or complex — and produces a visible audit trail of your work.

In this course, **unit cancellation is the preferred method 
for all calculations.**

!!! warning "A Note on Cross Multiplication"
    Cross multiplication is sometimes taught as a shortcut 
    for proportion problems. While it produces correct answers 
    for simple problems, it hides the units and makes errors 
    harder to catch. Unit cancellation is safer, more 
    transparent, and scales to complex problems.

## The Core Principle

When the same unit appears in both a numerator and a 
denominator, it cancels out:

\[\frac{\text{mg}}{\cancel{\text{tablet}}} \times \frac{\cancel{\text{tablet}}}{1} = \text{mg}\]

The unit that **does not cancel** is your answer unit. 
If the wrong unit remains, your setup is incorrect.

## Which Unit Remains?

!!! tip "The Golden Rule"
    Before doing any arithmetic, check which unit will remain 
    after cancellation. If it is not the unit you want, 
    flip a conversion fraction and try again.

    **The unit you want in your answer must not cancel.**
    **Every other unit must cancel.**

## Setting Up the Chain

Write your given value first, then attach conversion 
fractions so unwanted units cancel one by one:

\[\text{Given value} \times \frac{\text{wanted unit}}{\text{unwanted unit}} = \text{answer in wanted unit}\]

## Which Unit Remains — Practice

These problems focus entirely on identifying the surviving 
unit before doing any arithmetic. This builds the habit of 
checking your setup before calculating.

---

!!! example "Problem 1 — Which unit remains?"
    \[\frac{500 \text{ mg}}{1} \times \frac{1 \text{ tablet}}{250 \text{ mg}}\]

??? success "Answer"
    **mg** appears in the numerator of the first fraction 
    and the denominator of the second — it cancels.
    
    **tablet** appears only in the numerator — it remains.
    
    \[\frac{500 \cancel{\text{ mg}}}{1} \times \frac{1 \text{ tablet}}{250 \cancel{\text{ mg}}} = \frac{500}{250} \text{ tablets} = 2 \text{ tablets}\]

---

!!! example "Problem 2 — Which unit remains?"
    \[\frac{2.5 \text{ g}}{1} \times \frac{1000 \text{ mg}}{1 \text{ g}}\]

??? success "Answer"
    **g** cancels. **mg** remains.
    
    \[\frac{2.5 \cancel{\text{ g}}}{1} \times \frac{1000 \text{ mg}}{1 \cancel{\text{ g}}} = 2500 \text{ mg}\]

---

!!! example "Problem 3 — Which unit remains?"
    \[\frac{176 \text{ lb}}{1} \times \frac{1 \text{ kg}}{2.2 \text{ lb}} \times \frac{5 \text{ mg}}{1 \text{ kg}}\]

??? success "Answer"
    **lb** cancels with lb. **kg** cancels with kg. **mg** remains.
    
    \[\frac{176 \cancel{\text{ lb}}}{1} \times \frac{1 \cancel{\text{ kg}}}{2.2 \cancel{\text{ lb}}} \times \frac{5 \text{ mg}}{1 \cancel{\text{ kg}}} = \frac{880}{2.2} \text{ mg} = 400 \text{ mg}\]

---

!!! example "Problem 4 — Which unit remains?"
    \[\frac{3 \text{ tsp}}{1} \times \frac{5 \text{ mL}}{1 \text{ tsp}} \times \frac{1 \text{ L}}{1000 \text{ mL}}\]

??? success "Answer"
    **tsp** cancels. **mL** cancels. **L** remains.
    
    \[\frac{3 \cancel{\text{ tsp}}}{1} \times \frac{5 \cancel{\text{ mL}}}{1 \cancel{\text{ tsp}}} \times \frac{1 \text{ L}}{1000 \cancel{\text{ mL}}} = \frac{15}{1000} \text{ L} = 0.015 \text{ L}\]

---

!!! example "Problem 5 — Spot the Error"
    A student sets up this calculation to find how many 
    tablets to give for a 500 mg order with 250 mg per tablet.
    What is wrong?

    \[\frac{500 \text{ mg}}{1} \times \frac{250 \text{ mg}}{1 \text{ tablet}}\]

??? success "Answer"
    **mg** does not cancel — it appears in the numerator 
    of both fractions. The surviving unit would be 
    **mg²/tablet** which is meaningless.

    The conversion fraction is upside down. Correct setup:

    \[\frac{500 \cancel{\text{ mg}}}{1} \times \frac{1 \text{ tablet}}{250 \cancel{\text{ mg}}} = 2 \text{ tablets}\]

---

## Full Calculation Practice

!!! example "Problem 6"
    Order: 750 mg. Stock: 250 mg/5 mL. How many mL?
    
    Set up the unit cancellation chain first, identify 
    the surviving unit, then calculate.

??? success "Answer"
    Setup:
    \[\frac{750 \cancel{\text{ mg}}}{1} \times \frac{5 \text{ mL}}{250 \cancel{\text{ mg}}}\]
    
    **mg** cancels. **mL** remains. ✅
    
    \[= \frac{750 \times 5}{250} \text{ mL} = \frac{3750}{250} = 15 \text{ mL}\]

!!! example "Problem 7"
    Order: 0.5 g. Stock: 250 mg per tablet. How many tablets?
    
    Note: units don't match — conversion required.

??? success "Answer"
    Setup:
    \[\frac{0.5 \cancel{\text{ g}}}{1} \times \frac{1000 \cancel{\text{ mg}}}{1 \cancel{\text{ g}}} \times \frac{1 \text{ tablet}}{250 \cancel{\text{ mg}}}\]
    
    **g** cancels. **mg** cancels. **tablet** remains. ✅
    
    \[= \frac{0.5 \times 1000}{250} \text{ tablets} = \frac{500}{250} = 2 \text{ tablets}\]

!!! danger "If Your Units Don't Cancel Cleanly"
    Stop. Do not calculate. Recheck your conversion fractions. 
    A setup with non-cancelling units will always produce 
    a wrong answer regardless of the arithmetic.
