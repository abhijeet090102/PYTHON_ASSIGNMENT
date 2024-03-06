'''Write a Python function that checks whether a passed string is palindrome
or not.'''
def palin(st):
    for i in range (0,len(st)//2):
        if st[i] == st[len(st)-i-1]:
            return True
        else:
            return False
    '''if palin == palin[::-1]:
        print('Palindrome')'''
print('plindrome',palin('mamaamam'))   
