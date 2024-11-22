def int_to_binary_with_leading_zeros(number, width):
    return format(number, f'0{width}b')

number = int(input("Enter an integer: "))
width = int(input("Enter the total width for the binary string: "))
binary_string = int_to_binary_with_leading_zeros(number, width)
print(f"The binary representation with leading zeros is: {binary_string}")
