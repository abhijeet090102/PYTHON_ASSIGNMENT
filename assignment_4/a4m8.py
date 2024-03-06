''' Write a program in C to calculate combinatoric C(n,r) using function.'''
def fact(am):
    f = 1
    for i in range(1,am+1):
        f = f*i
    return f
#am = int(input("Enter any number "))
#st = fact(am)
#print("factorial of ",am ,"is ",st)
def main():
    n = int(input('Enter the value of n: '))
    r = int(input('Enter the value of r: '))
    nCr = fact(n)//(fact(r)*fact(n-r))
    #print(fact(r))
    #print(fact(n))
    #print(fact(n-r))
    print(f'The value of {n} , {r} , is :',nCr)
main()
