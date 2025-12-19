# Day 6 Functions Modularity
## DEEP DIVE: Theory: The Stack Scope

When a function is called, Python creates a "Stack Frame" in memory. All variables created inside the function live there. When the function returns, the frame is destroyed.

**LEGB Rule:** Python searches for variables in order: Local -> Enclosing -> Global -> Built-in.

```python:
def calculate_area(radius: float) -> float:
    """Returns area of circle. Inputs float."""
    if radius < 0 :
        return 0
    return 3.14 * (radius ** 2)

# Main execution
r = 5
print(calculate_area(r))
```
Goals:
1. Demonstrating Local vs Global Scope.
2. Using return value instead of print(Best practice).
3. Using Default Arguments for flexible API.
4. Using Comparison operators in return for Boolean value.
