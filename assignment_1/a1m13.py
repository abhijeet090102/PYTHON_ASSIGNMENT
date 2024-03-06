#  If a five-digit number is input through the keyboard, write a program to print a new number by adding one to each of its digits. For example if the number that is input is 12391 then the output should be displayed as 23402.
am = int(input("enter the five -digit number :"))
a1 = (am//10000+1)%10
a2 = (am//1000+1)%10
a3 = (am//100+1)%10
a4 = (am//10+1)%10
a5 = (am//1+1)%10
ma = a1*10000+a2*1000+a3*100+a4*10+a5
print(ma)