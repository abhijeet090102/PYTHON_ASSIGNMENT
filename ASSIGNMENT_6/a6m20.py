'''. print list after removing EVEN numbers'''
def evenList(remove):
    n_l = []
    for i in remove:
        if i%2 !=0:
            n_l.append(i)
    return n_l
    
l = [45,58,68,23,46,45,79,73,75,57,95,61,68,86,98]
print('Old list:',l)
print('New list after removing Even Numbers ',evenList(l))
