# 8. Write a program to calculate grade of the MAKAUT result.

def calculate_grade(percentage):
    if percentage >= 90 and percentage <= 100:
        return "O"
    elif percentage >= 80 and percentage <= 89:
        return "E"
    elif percentage >= 70 and percentage <= 79:
        return "A"
    elif percentage >= 60 and percentage <= 69:
        return "B"
    elif percentage >= 50 and percentage <= 59:
        return "C"
    elif percentage >= 40 and percentage <= 49:
        return "D"
    else:
        return "F"

percentage = float(input("Enter the percentage score: "))
grade = calculate_grade(percentage)
print(f"The grade is: {grade}")
