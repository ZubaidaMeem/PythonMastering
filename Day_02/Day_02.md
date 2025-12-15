# Day 2 : Logic Control Flow
## DEEP DIVE : Theory: Boolean Algebra Short-Circuiting
Logic is brain of your code.

Truthiness : In Python, the following are considered False: 0, 0.0, ""(Empty String), [] (Empty List), None. Everything else is True.

Short-Circuit Evaluation: if A and B: if A is False, Python never checks B. This is Critical for preventing crashes(e.g., checking if a variable exists before accessing it).

```python
score = 85
# The Efficient Ladder
if score >= 0:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# Temporary Operator (One-line logic)
status = "Pass" if score >= 70 else "Fail"

```

Goal:
1. Checking access using if else
2. Checking Fraction values in Python
   (Tips : Always use a tolerance threshold(epsilon) or round() when comparing floats in Data Science)
3. Checking Python objects inherent Boolean Values.
4. Using temporary variable to check atomic operation
   (```python
   status = "Pass" if score >= 70 else "Fail"
   ```
   )