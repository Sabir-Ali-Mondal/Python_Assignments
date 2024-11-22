import math

# Function to check the position of the point
def check_point(x_center, y_center, r, x, y):
    # Calculate the distance from the point to the center of the circle
    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
    
    # Determine the position of the point relative to the circle
    if distance < r:
        return "The point is inside the circle."
    elif distance == r:
        return "The point is on the circle."
    else:
        return "The point is outside the circle."

x_center = float(input("Enter the x-coordinate of the center of the circle: "))
y_center = float(input("Enter the y-coordinate of the center of the circle: "))
r = float(input("Enter the radius of the circle: "))
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

result = check_point(x_center, y_center, r, x, y)
print(result)
