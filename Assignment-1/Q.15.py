# Function to check if a number is an Armstrong number
def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number

# Function to print all Armstrong numbers between 1 and 500
def print_armstrong_numbers():
    print("Armstrong numbers between 1 and 500 are:")
    for num in range(1, 501):
        if is_armstrong(num):
            print(num, end=' ')


print_armstrong_numbers()
