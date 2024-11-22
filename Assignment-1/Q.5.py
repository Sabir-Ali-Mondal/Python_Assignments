def collinear(x1, y1, x2, y2, x3, y3):  
    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))  
    return area == 0  

x1, y1 = map(float, input("Enter coordinates of point 1 (x1 y1): ").split())  
x2, y2 = map(float, input("Enter coordinates of point 2 (x2 y2): ").split())  
x3, y3 = map(float, input("Enter coordinates of point 3 (x3 y3): ").split())  

if collinear(x1, y1, x2, y2, x3, y3):  
    print("The points are collinear.")  
else:  
    print("The points are not collinear.")