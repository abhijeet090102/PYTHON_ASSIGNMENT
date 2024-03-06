#  The length & breadth of a rectangle and radius of a circle are input through the keyboard.
# Write a program to calculate the area & perimeter of the rectangle, and the area &
# circumference of the circle. 
len = int (input('Enter the lenth :'))
breadth = int(input('Enter the breadth:'))
radius = int(input('Enter the radius of a circle:'))
area = len * breadth
perimeter = 2 * (len*breadth)
area_cir = 3.14 * radius *radius
circum = 2 * 3.14 * radius
print('The area of a rectangle :',area)
print('The perimeter of a rectangle :',perimeter)
print('The area of a circle :',area_cir)
print('The circumference of a circle :',circum)
