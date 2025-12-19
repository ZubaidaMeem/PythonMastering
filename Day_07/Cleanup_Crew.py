try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x/y)
except ValueError:
    print("Numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution Complete")
