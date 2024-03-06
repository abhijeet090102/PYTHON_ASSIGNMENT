'''Write a Python function to check whether a number falls in a given range.'''
def In_ren(num,start,end):
    if start<=num<=end:
        return True
    else:
        return False
print(In_ren(4,1,10))
