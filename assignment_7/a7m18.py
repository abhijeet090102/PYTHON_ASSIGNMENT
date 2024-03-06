'''Write a Python function that takes a number as a parameter and check the
number is prime or not.'''
def check(nu):
    if nu == 1:
        print('Not a prime ',nu)
    elif nu % 1 ==0 and nu % nu == 0:
        print('No is prime ',nu)
    else:
        print('Not prime ',nu)
check(int(input('Enter any no :')))
