'''Write a program uppercase Half String.'''
am = input("Enter any string ")
ma = len(am)//2
res = ''
for i in range(len(am)):
    if i < ma:
        res += am[i].upper()
    else:
        res += am[i]
print(str(res))

