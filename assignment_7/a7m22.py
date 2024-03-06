'''Write a Python function to create and print a list where the values are
square of numbers between 1 and 30 (both included)'''
def square():
    '''l = []
    for i in range(1,31):
        sq = i**2
        l.append(sq)
    print(l)
    '''
    li = [i**2 for i in range(1,31)]
    return li
print(square())
