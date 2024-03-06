''' Write a program to add first seven terms of the following series using a for loop:
1/1!+2/2!+3/3 !+…+n/n !'''
am = int(input("Enter how many times you want fact value "))
st = 0
fact = 1
for i in range(1,am+1):
    fact *= i
    st = st + (i/fact)
print(st)
