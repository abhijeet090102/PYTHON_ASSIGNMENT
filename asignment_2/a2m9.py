#  Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 and breadth = 4 is greater than its perimeter.
length = int (input("Enter the length "))
breadth = int (input("Enter breadth"))
area = length * breadth
peri = 2*(length + breadth)
if(area > peri):
    print("Area of rectangle is greater")
else:
    print("Perimeter is greater")