def subsequence(l1, l2):
    it = iter(l2)
    return all(x in it for x in l1)

# Test cases
print(subsequence([2, 3, 4], [2, 2, 3, 4, 5]))  # True
print(subsequence([2, 2, 5], [2, 2, 3, 4, 5]))  # True
print(subsequence([2, 4, 4], [2, 2, 3, 4, 5]))  # False
print(subsequence([2, 4, 3], [2, 2, 3, 4, 5]))  # False
