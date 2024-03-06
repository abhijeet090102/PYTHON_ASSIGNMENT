'''Write a program in C to calculate Power(a,b) using function.'''
def pow1(a,b):
    
    return a**b
a = int(input('Enter the value of base '))
b = int(input('Enter the value of power '))
print(f'The power value of {a} , {b} is : ',pow1(a,b))
