def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
