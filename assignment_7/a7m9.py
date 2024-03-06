'''Create a function to calculate and return HCF of two numbers.'''
def hcf(a,m):
    if a<m:
        (a,m) = (m,a)
    while m !=0:
        s = a%m
        (a,m) = (m,s)
    return a
print(hcf(int(input('Enter 1st no:')), int(input('Enter 2nd no:'))))
