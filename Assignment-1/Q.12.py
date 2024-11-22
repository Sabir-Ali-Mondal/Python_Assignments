# Function to generate the Fibonacci series
def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci_series(n)
    print(f"The Fibonacci series with {n} terms is: {result}")
