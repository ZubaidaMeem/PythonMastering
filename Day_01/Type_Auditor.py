val = input("Enter a number: ")
print(type(val))
try:
    float_val = float(val)
    print(type(float_val))
except ValueError:
    print("Invalid number!")
