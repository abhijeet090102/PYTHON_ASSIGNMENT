''' Write a program in C to calculate factorial of a natural number.'''
def fact_prima(am):
    if am ==1 or am == 0:
        return 1
    else:
        return am*fact_prima(am-1)
am = int(input('Enter prime num : '))
print('The factorial value is : ',fact_prima(am))
