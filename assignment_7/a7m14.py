'''Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument.'''
def fact(am):
    if am == 0:
        return 1
    else:
        return am*fact(am-1)
print(fact(6))
