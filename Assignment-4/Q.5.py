def sosq(n):
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int(n**0.5) + 1):
            if i**2 + j**2 == n:
                return True
    return False

# Test cases
print(sosq(10))  # True
print(sosq(25))  # True
print(sosq(11))  # False
print(sosq(3))   # False
print(sosq(50))  # True
