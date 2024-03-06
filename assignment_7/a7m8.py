'''Create a function to calculate and return LCM of two numbers.'''
def gcd(m,a):
    if a ==0:
        return m
    else:
        return gcd(a,m%a)
def lcm(a,m):
    return (a*m)//gcd(a,m)
print(lcm(int(input('Enter 1st no:')), int(input('Enter 2nd no:'))))
