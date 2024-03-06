# If a five-digit number is input through the keyboard, write a program to reverse the number.
am = int(input('Enter five digit number :'))
rev = 0
while (am>0):
    st = am % 10
    rev = rev * 10 + st
    am = am//10
print(rev)
'''st = am%10
a = am//10%10
s = am//100%10
t = am//1000%10
m = am//10000%10
# ma = st*1+a*10+s*100+t*1000+m*10000
ma = m+t*10+s*100+a*1000+st*10000
print(ma)'''
