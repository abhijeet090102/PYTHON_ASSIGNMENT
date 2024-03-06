'''Write a program to take input a string of digits and convert it to an integer without 
using int() function.'''
st = input("Enter any string digit")
n = 0
for i in st:
    n = n* 10 + (ord(i)-48)
    print(i)
print(n)
