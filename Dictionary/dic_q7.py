'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'MCA1stsem'
Expected output: {'M':1,'C':2,'A':3,'1':4,'s':5,'t':6,'s':7,'e':8,'m':10}'''
am = 'abhijeet'
for i in range(len(am)):
    print(dict(am))
