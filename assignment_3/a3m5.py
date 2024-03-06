'''Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each
digit of the number is equal to the number itself, then the number is called an Armstrong
number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )'''
am = int(input("Enter any number"))
sum = 0
num = am
while num>0:
   d = num % 10
   sum = sum+(d ** 3)
   num=num//10
if am==sum:
   print(am,"no is armstrong number")
else:
   print(am,"NOt a armstrong no")
