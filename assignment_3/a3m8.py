# Write a program to find the octal equivalent of the entered number
am = int(input("enter any eumber"))
oct1 = 0
st = 1 
while am > 0:
    reminder = am % 8
    oct1 += reminder*st
    am = am//8
    st = st*10
print("octal value is ",oct1)
