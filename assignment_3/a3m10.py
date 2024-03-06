''' Write a program to find the range of a set of numbers. Range is the difference between the
smallest and biggest number in the list.'''
no = int(input('Enter how many times you want to enter '))
small= 0 #small no
high = 0
num = 0
num = int(input('Enter the number :'))
small= high=num
for i in range(1,no):
    num = int(input('Enter the number :'))
    if  num > high:
        high = num
    elif num<small:
        small = num
range1 = high - small
print('The highest no is ',high)
print('The smallest no is ',small)
print('The range between two numbers are ',range1)
