''' Write a program to take binary input numbers and convert it to an integer without 
using int() function.'''
st = int(input("Enter any binary no"))
am =0
s = 0
i=0
while st!=0:
    s = st%10
    st = st//10
    am += s*(2**i)
    i = i+1
print(am)
