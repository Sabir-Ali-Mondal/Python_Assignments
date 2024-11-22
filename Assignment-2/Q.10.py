def height_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 2.54

feet = float(input("Enter height in feet: "))
inches = float(input("Enter additional inches: "))
height_cm = height_to_cm(feet, inches)
print("Height in centimeters:", height_cm)
