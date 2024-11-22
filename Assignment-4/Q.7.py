def sumof3squares(n):
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int(n**0.5) + 1):
            for k in range(1, int(n**0.5) + 1):
                if i**2 + j**2 + k**2 == n:
                    return True
    return False

# Test cases
print(sumof3squares(29))  # True
print(sumof3squares(6))   # True
print(sumof3squares(16))  # False
print(sumof3squares(20))  # False
