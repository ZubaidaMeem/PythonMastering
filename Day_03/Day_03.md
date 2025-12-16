# Day 3 Loops Iteration
## DEEP DIVE: Theory: The Iterator Protocol

Loops allow us to automate tasks.

- For Loops: Iterate over a known collection (List, String, Range).
- While Loops: Iterate as long as a condition (State) is True.

*Warning:* While loops can run forever (Infinite Loop) if you don't write a line of code that changes the condition to False.

```python
# The Infinite Input Pattern
while True:
    pwd = input("Set Password (min 5 chars): ")
    if(len(pwd) >= 5):
        break # Exits the loop
    print("Too Short. Try again.")
```

Goal:
1. Using while True and handle the exit condition manually.
2. Using for loop and tracker variable to calculate sum from 1 to n.
3. Using the continue keyword.
4. Demonstrating looping characters in a string.