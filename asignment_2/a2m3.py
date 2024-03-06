# Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not.
year = int(input("Enter a year : "))
if ( (year%4 == 0) & (year%100 !=0) | (year%400 ==0)):
    print("This is a leap year")  
else:
    print("This is not a leap year") 