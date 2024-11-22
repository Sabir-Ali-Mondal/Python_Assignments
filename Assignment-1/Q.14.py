# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers():
    print("Prime numbers from 1 to 300 are:")
    for num in range(1, 301):
        if is_prime(num):
            print(num, end=' ')

print_prime_numbers()
