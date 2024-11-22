# Example dictionary
example_dict = {
    "apple": 5,
    "banana": 2,
    "cherry": 7,
    "date": 3,
    "elderberry": 9
}

# Function to sort dictionary by value in ascending order
def sort_dict_by_value_ascending(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Function to sort dictionary by value in descending order
def sort_dict_by_value_descending(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

# Sort the dictionary in ascending order by value
sorted_dict_ascending = sort_dict_by_value_ascending(example_dict)
print("Dictionary sorted in ascending order by value:")
print(sorted_dict_ascending)

# Sort the dictionary in descending order by value
sorted_dict_descending = sort_dict_by_value_descending(example_dict)
print("Dictionary sorted in descending order by value:")
print(sorted_dict_descending)
