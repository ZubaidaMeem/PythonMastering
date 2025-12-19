# Day 7 Error Handling (Exceptions)
## DEEP DIVE: Theory: Exception Bubbling

When an error occurs, it "bubbles up" the call stack. If nothing catches it, the program crashes.

**Defensive Programming:** We use try/except blocks to catch these bubbles. This is required for Data Science pipelines where one bad row of data shouldn't stop a 10-hour training process.

```python
while True:
    try:
        val = int(input("Enter number: "))
        print(100/val)
        break
    except ValueError:
        print("Text is not allowed")
    except ZeroDivisionError:
        print("Cannot divide by zero")
```
Goals:
1. Using try/except ValueError.
2. Using ZeroDivisionError to avoid undefined division(divided by zero).
3. Using finally block that executes regardless other blocks catches or not.
4. Manually triggering an error using raise.