# Example list with 15 numbers, including duplicates
numbers = [2, 4, 6, 8, 2, 10, 12, 14, 16, 18, 4, 6, 20, 22, 24]

# Remove duplicates by converting the list to a set and then back to a list
unique_numbers = list(set(numbers))

# Optional: Sort the list to maintain order (if needed)
unique_numbers.sort()

# Print the list without duplicates
print("Original list with duplicates:", numbers)
print("List after removing duplicates:", unique_numbers)
