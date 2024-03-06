#  Any year is entered through the keyboard, write a program to determine whether the year is leap or not. Use the logical operators && and ||.
year = int(input("Enter a year: "))
if (year//4) & (year//100) | (year//400):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
