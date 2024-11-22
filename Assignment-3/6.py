def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:]

print(hex_to_binary("1A3F"))
