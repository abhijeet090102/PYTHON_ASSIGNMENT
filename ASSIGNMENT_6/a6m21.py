'''Iterate a list in reverse order'''
l =[45,58,68,23,46,45,79,73,75,57,95,61,64,86,98]
n_l = []
for i in range(len(l)-1,-1,-1):
    print('values:',l[i])
    n_l.append(l[i])
print('reverse list :',n_l)
