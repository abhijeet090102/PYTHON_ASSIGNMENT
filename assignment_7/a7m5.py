'''Write a Python program to understand the use of global and nonlocal
variables declared in a function.'''
glob = 4 #global
def fun1():
    n_loc = 6#nonlocal
    global glob
    st = glob+n_loc
    print('Global ',glob)
    def fun2():
        nonlocal n_loc
        print('Non local',n_loc)
        n_loc = glob*n_loc
        return n_loc
    
    print('Multiply',fun2())
    return st
print('addition ',fun1())
