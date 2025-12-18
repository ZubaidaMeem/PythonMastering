# Day 5 Dictionaries(Hash Maps)
## DEEP DIVE: Theory: Hash Tables

A Dictionary is a Key-Value store. It is optimized for *O(1)* Lookup.
When you search a List, Python scans left-to-right *(O(N))*. When you search a Dictionary, Python uses a "Hash Function" to calculate exactly where the data is in the memory.
It is instant, even in 1 million items.

```python
user = {"id" : 1, "name" : "Admin"}
# Safe Access (.get)
# Returns none if key missing, prevents crash
email = user.get("email", "No Email Found")

# Iteration
for key, val in user.items():
    print(f"{key}:{val}")
```

Goals:
1. Understanding why Dict/Set search (*O(1)*) is faster than list search(*O(N)*).
2. Accessing Dictionary item safely.
3. Creating a dictionary that counts frequency of each letter of a string.
4. Overriding a dictionary by another dictionary using .update() function.
```python
dict1.update(dict2)
```