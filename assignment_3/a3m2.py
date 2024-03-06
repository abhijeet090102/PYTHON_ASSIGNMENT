#  Write a program to find the factorial value of any number entered through the keyboard.
nuam = int(input("Enter any number "))
factor =1 
i = 1
while i<=nuam:
    factor = factor*i
    i = i+1
print(nuam ,"factorial value is ",factor)
