#  A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.
no = int(input("Enter five - digit number : "))
ma = no
am1 = (no//10000)%10
am2 = (no//1000)%10
am3 = (no//100)%10
am4 = (no//10)%10
am5 = (no//1)%10
st = am5*10000+am4*1000+am3*100+am2*10+am1
print("reverse no is :",st)
if (ma == st):
    print("Orginal and reversed no are equal")
else:
    print("Orginal and reversed no are not equal")