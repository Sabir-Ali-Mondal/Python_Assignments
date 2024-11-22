def int_to_binary(n):
    if n == 0:
        return ''
    return int_to_binary(n // 2) + str(n % 2)

print(int_to_binary(10))
