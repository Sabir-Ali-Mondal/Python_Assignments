def intersect(l1, l2):
    return sorted(set(l1) & set(l2))

# Test cases
print(intersect([2, 2, 4], [1, 2, 2, 3, 4]))  # [2, 4]
print(intersect([1, 2, 3], [4, 5, 6]))        # []
