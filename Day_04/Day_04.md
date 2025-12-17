# Day 4 Lists (Data Structures I)
## DEEP DIVE: Theory: Mutability Memory

Lists are **Mutable**. This means they can be changed in place.

**The Aliasing Trap:** A = [1,2] B = A. This does not copy the list. It creates a second name for the list. Modifying B will distroy A.
**Solution:** Always use B = A.copy().

```python
data = [10, 20, 30, 40, 50]
# Slicing (Start : Stop : Step)
subset = data[1 : 4] #[20, 30, 40]
reverse = data[::-1] # [50, 40, 30, 20, 10]

# List Comprehension
# [Action for Item in List if condition]
squares = [x ** 2 for x in data]
print(squares)
```
Goals:
1. Checking Aliasing Trap and copying Reference (Memory Address) instead of List.
2. Using slicing syntax [start : stop : step]
3. Using stack functions (.append() and pop()) instead of insert() or remove().
4. Using List Comprehension for new list from old list.
```python
squares = [x ** 2 for x in nums if x % 2 == 0 ]
```

