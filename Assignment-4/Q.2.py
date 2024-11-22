def perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Test cases
print(perfect(6))    # True
print(perfect(28))   # True
print(perfect(12))   # False
print(perfect(496))  # True
print(perfect(10))   # False
