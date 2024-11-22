# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_digits += digit  # Add the digit to the sum
        number //= 10  # Remove the last digit
    return sum_digits

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits is: {result}")
