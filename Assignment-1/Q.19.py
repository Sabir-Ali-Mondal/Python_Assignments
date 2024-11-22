# Function to calculate a^b using recursion
def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)


a = float(input("Enter the base number (a): "))
b = int(input("Enter the exponent (b): "))

if b < 0:
    print("This program does not handle negative exponents.")
else:
    result = power(a, b)
    print(f"{a} raised to the power of {b} is: {result}")
