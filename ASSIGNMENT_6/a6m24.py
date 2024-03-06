'''print list after removing ODD numbers.'''
l = [45,65,26,84,98,65,26,42]
n_l = []
for i in l:
    if i%2 ==0:
        n_l.append(i)
print('New list after removing Odd num :',n_l)
