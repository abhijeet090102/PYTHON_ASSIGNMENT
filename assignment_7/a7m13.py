'''Write a Python program to reverse a string.'''
def re(st):
    if not st:
        return''
    else:
        return re(st[1:]) + st[0]
print(re('abhijeet'))
        
