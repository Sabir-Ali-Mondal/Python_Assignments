# Function to calculate the sum of a list of integers
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

result = sum_of_list(numbers)
print(f"The sum of the list is: {result}")
