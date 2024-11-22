# Function to reverse a number
def reverse_number(number):
    reverse = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        reverse = reverse * 10 + digit  # Shift current reverse and add the digit
        number //= 10  # Remove the last digit
    return reverse

number = int(input("Enter a number: "))
result = reverse_number(number)
print(f"The reverse of the number is: {result}")
