#  If the three sides of a triangle are entered through the keyboard, write a program to check whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than the largest of the three sides.
am = int(input("Enter 1st side"))
st = int(input("Enter 2nd side"))
ma = int(input("Enter 3rd side"))
if (am+st > ma and am+ma >st and ma+st >am):
    print("Triangle is valid")
else:
    print("Triangle is not valid")
