def convert_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return days, hours, minutes, seconds

total_seconds = int(input("Enter the number of seconds: "))
days, hours, minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} seconds is equivalent to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
