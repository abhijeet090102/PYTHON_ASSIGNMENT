'''Program to remove all elements in a range from the List.'''
l = [6,7,8,9,4,5,6]
i = int(input('Enter where to start range '))
g = int(input('Enter where to end range '))
del l[i:g]
print(l)
