'''Write a Python function to multiply all the numbers in a list'''
def mal_no(nu):
    l = 1
    for i in nu:
        l = l* i
    return l
l = [2,4,6,8,9,16]
print('multiply value',mal_no(l))
