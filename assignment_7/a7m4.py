'''Write a Python program to access a function inside a function.'''
def fun1(am,st):
    def pr(st,ma):
        am = st*ma
        return am
    return (pr(am,st))
print('Multiply of two num value are:',fun1(4,6))
