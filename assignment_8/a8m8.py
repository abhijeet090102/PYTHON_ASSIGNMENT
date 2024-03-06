'''Write a Python program to create a dictionary from a string.Note: Track the count of the letters from the string.
Sample string : 'MCA1stsem'
Expected output: {'M':1,'C':2,'A':3,'1':4,'s':5,'t':6,'s':7,'e':8,'m':10}
'''
st = 'Programmer'
am = dict()
a = 1
for i in st:
    am[i] = a
    a += 1
print(am)

'''this will copy whole string and when duplicate string present it will add the value
ma = {st[i]: i for i in range(len(st))}
print(ma)

'''
''' it could't give me same as a question because all no are here keys and all string
are values
ma = {i:st[i] for i in range(len(st))}
print(ma)'''
