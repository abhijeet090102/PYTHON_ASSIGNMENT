# Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
angle_one = int (input("Enter angle no one "))
angle_two = int (input("Enter angel no two "))
angle_third = int(input("Enter angle no third "))
if(angle_one + angle_two + angle_third ==180):
    print("Triangle is valid")
else:
    print("Triangle is not valid")