# Ask the user to input the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print both temperatures
print(f"Temperature in Fahrenheit: {fahrenheit}°F")
print(f"Temperature in Celsius: {celsius}°C")
