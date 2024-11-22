def sublist(l1, l2):
    n, m = len(l1), len(l2)
    for i in range(m - n + 1):
        if l2[i:i+n] == l1:
            return True
    return False

# Test cases
print(sublist([2, 3, 4], [2, 2, 3, 4, 5]))  # True
print(sublist([2, 2, 4], [2, 2, 3, 4, 5]))  # False
print(sublist([2, 4, 5], [2, 2, 3, 4, 5]))  # False
print(sublist([3, 4], [1, 3, 4, 5]))        # True
print(sublist([5], [1, 2, 3, 4, 5]))        # True
