def check_duplicate(L):
    return len(L) != len(set(L))

print(check_duplicate([1, 2, 3, 4, 5]))
print(check_duplicate([1, 2, 2, 4, 5]))
