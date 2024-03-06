'''Write a program to specific Characters Frequency in String List'''
am = ['ABHIJEET','MANISHA']
ma = 0
print(am)
char = 'A'
for i in am:
    ma += i.count(char)
print(ma,'times ',char, ' Present')
