# Given set S
S = {12, -2, 56, 1, 67, 3}

# 1. Number of items in set S
number_of_items = len(S)
print(f"Number of items in set S: {number_of_items}")

# 2. Maximum element in set S
max_element = max(S)
print(f"Maximum element in set S: {max_element}")

# 3. Minimum element in set S
min_element = min(S)
print(f"Minimum element in set S: {min_element}")

# 4. Sum of all elements in set S
sum_of_elements = sum(S)
print(f"Sum of all elements in set S: {sum_of_elements}")

# 5. Obtain a new sorted set from S, with S remaining unchanged
sorted_set = sorted(S)
print(f"Sorted set from S: {sorted_set}")

# 6. Report whether 40 is a member of the set
is_40_in_set = 40 in S
print(f"Is 40 a member of set S? {is_40_in_set}")

# 7. Report whether 1 is an element of set S
is_1_in_set = 1 in S
print(f"Is 1 an element of set S? {is_1_in_set}")
