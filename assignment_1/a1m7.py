#  If a five-digit number is input through the keyboard, write a program to calculate the sum of
# its digits.(Hint: Use the modulus operator ‘%’)
am = int(input('Enter the five digit number'))
st = am%10
a = am//10%10
s = am//100%10
t = am//1000%10
m = am//10000%10
print('Sum of all digits are:',st+a+m+t+s ,end='')