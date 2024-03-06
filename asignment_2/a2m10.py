#  Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all the three points fall on one straight line.
x1 = int(input("Enter the x1 point value "))
x2 = int(input("Enter the x2 point value "))
y1 = int(input("Enter the y1 point value "))
y2 = int(input("Enter the y2 point value "))
x3 = int(input("Enter the x3 point value "))
y3 = int(input("Enter the y3 point value "))
m = (y2-y1)/(x2-x1)
a = (y3-y2)/(x3-x2)
if (m == a):
    print("All three points falls on a straight line ")
else:
    print("All points does not fall on a straight line ")
