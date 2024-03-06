#  Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ) and pow( ) functions)
import math
x = int(input("Enter the first cordinate"))
y = int(input("Enter the second cordinate"))
r = int(input("Enter the radius "))

x1 = int (input("Enter the x1 value"))
y1 = int (input("Enter the y1 value"))
am = math.sqrt(math.pow(x-x1,2) + math.pow(y-y1,2))
print(am)
if(am>r):
    print("Point ",x1,y1, "lies outside the circle")
elif(am<r):
    print("Point ",x1,y1,"lies inside the circle")
elif(am==r):
    print("Point ",x1,y1,"lies on the boundary of circle")
else:
    print("Wrong entry")