'''If the three sides of a triangle are entered through the keyboard,
write a program to check whether the triangle is isosceles, equilateral,
scalene or right angled triangle. isosceles = two sides are equal
equilateral = all sides are equal  , scalene = all three sides are dif length ,
right angle = any one angle is 90'''

am = int(input("Enter the first side "))
st = int(input("Enter the second side "))
ma = int(input("Enter the third side "))
if(am==st==ma):
    print("Triangle is equilateral")
elif(am==st or st == ma or am == ma ):
    print("Triangle is isolated ")
elif(am != st != ma):
    if((am**2+st**2==ma**2) or (am**2+ma**2==st**2) or (st**2+ma**2==am**2) ):
        print("Right angle triangle and as well as scalene triangle")
