'''Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.'''
def calcu(string):
    low = 0
    up = 0
    for i in string:
        if i.islower():
            low += 1
        elif i.isupper():
            up += 1
        else:
            pass
    print(f'lower case :{low} & upper case :{up}')
    
calcu('hi This Is ABHIjeet')
