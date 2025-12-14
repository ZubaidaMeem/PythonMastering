# Day 1
## DEEP DIVE: Theory: The python memory model
To become a Data Scientist, you must understand how Python manages memory. It is distinct from C or Java.
1. Everything is an Object: Numbers, Strings, and Lists are all objects stored in Heap Memory.
2. Variables are References (Sticky Notes): When you execute x = 10:
    i. Python creates an object int (10) at memory address 0x7ff....
    ii. Python creates the name x.
    iii. Python draws a line (reference) connecting x to 0x7ff....
3. Garbage Collection: Python uses "Reference Counting". If you delete x, the reference count for object 10 drops to 0. Python's Garbage Collector then instantly destroys the object to free up RAM.


Syntax Spotlight: The Safe Input Pattern
```python
# Standard Input (Unsafe)
# age = input("Age: ") <-- Returns "25" (String)
# The Academy Standard (Safe)
raw_val = input ("Enter Principal: ")
try:
    principal = float(raw_val) # Explicit Casting
    print (f" Accepted: ${principal:,.2f}") # F-String Formatting
except ValueError:
    print("Error: Invalid Number")
```


Day 1 goals:
1. Identity Swap
2. Type casting
3. Precision Banking
4, Modulo Architect