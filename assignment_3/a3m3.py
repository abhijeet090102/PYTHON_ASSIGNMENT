'''Two numbers are entered through the keyboard. Write a program to find the value of one
number raised to the power of another.'''
am = int(input("Enter first/base no:"))
st = int(input("Emter second/power no:"))
i = 1
j = 1
while i<=st:
    j = j*am
    i = i+1
print(j)