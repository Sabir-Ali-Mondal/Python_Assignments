def is_n_d(lst):
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return is_n_d(lst[1:])

# Test cases
print(is_n_d([]))                     # True
print(is_n_d([7]))                    # True
print(is_n_d([8, 8, 11]))             # True
print(is_n_d([3, 19, 44, 44, 63, 89]))# True
print(is_n_d([3, 18, 4]))             # False
print(is_n_d([23, 14, 3, 14, 3, 23])) # False
