# Function to perform union of two sets
def union_sets(set1, set2):
    return set1.union(set2)

# Function to perform intersection of two sets
def intersection_sets(set1, set2):
    return set1.intersection(set2)

# Function to perform set difference (set1 - set2)
def difference_sets(set1, set2):
    return set1.difference(set2)

# Function to perform symmetric difference of two sets
def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform operations
union_result = union_sets(set1, set2)
intersection_result = intersection_sets(set1, set2)
difference_result = difference_sets(set1, set2)
symmetric_difference_result = symmetric_difference_sets(set1, set2)

# Print results
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union of Set 1 and Set 2: {union_result}")
print(f"Intersection of Set 1 and Set 2: {intersection_result}")
print(f"Difference of Set 1 and Set 2 (Set 1 - Set 2): {difference_result}")
print(f"Symmetric Difference of Set 1 and Set 2: {symmetric_difference_result}")
