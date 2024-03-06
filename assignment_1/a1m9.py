#  If a four-digit number is input through the keyboard, write a program to obtain the sum of
# the first and last digit of this number.
am = int(input("Enter four digit number:"))
st = am%10
ma = am//1000%10
print(ma)
print(st)
print('Sum of first and last digit number is ',st+ma)