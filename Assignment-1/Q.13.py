# Function to display the pattern
def display_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Example usage
n = int(input("Enter the number of rows: "))
display_pattern(n)
