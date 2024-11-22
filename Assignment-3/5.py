def remove_vowels(word):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in word if char not in vowels)

print(remove_vowels("Hello World"))
