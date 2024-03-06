'''Write a Python program to print the even numbers from a given list.'''
def even(g_list):
    l = []
    for i in g_list:
        if i%2==0:
            l.append(i)
    return l
li= [2,3,53,57,31,66,68,42,24]
print(even(li))
