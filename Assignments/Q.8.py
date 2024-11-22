def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
print("The LCM of", num1, "and", num2, "is:", lcm(num1, num2))
