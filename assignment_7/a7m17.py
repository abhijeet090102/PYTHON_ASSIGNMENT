'''. Write a Python function that takes a list and returns a new list with
unique elements of the first list.'''
def re(ele):
    l = []
    for i in ele:
        if i not in l:
            l.append(i)
    return l
print(re([1,1,2,2,3,4,5,6,7,8,7]))
