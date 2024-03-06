'''Write a Python function to find the max of three numbers.'''
def max_no(a,m,st):
    max1 = 0
    if a>m and a>st:
        max1 = a
    elif m>a and m>st:
        max1 = m
    elif st>a and st>m:
        max1= st
    return max1
print('Maximam no is :',max_no(4,6,8))
