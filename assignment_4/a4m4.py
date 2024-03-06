'''Write a program in C to calculate H.C.F using while loop.
'''
def hcf(am,st):
    a =am
    m = st
    s = 0
    while m%a!=0:
        s = m%a
        m = a
        a = s
    return a
a = 21
b = 56
ma = hcf(a,b)
print("Hcf of " ,a,'and',b,'is',ma)
