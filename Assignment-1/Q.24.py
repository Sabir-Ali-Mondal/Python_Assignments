from datetime import date

# Function to calculate the number of days between two dates
def days_between_dates(date1, date2):
    d1 = date(date1[2], date1[1], date1[0])
    d2 = date(date2[2], date2[1], date2[0])
    delta = d2 - d1
    return abs(delta.days)

# Create two date tuples (day, month, year)
date1 = (15, 8, 2023)
date2 = (29, 8, 2024)

# Calculate the number of days between the two dates
days_difference = days_between_dates(date1, date2)

# Print the result
print(f"Number of days between {date1} and {date2} is: {days_difference} days")
