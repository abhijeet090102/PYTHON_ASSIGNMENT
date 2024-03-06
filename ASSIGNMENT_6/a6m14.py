from copy import deepcopy
'''Program to sort the elements of given list in Ascending and Descending Order.'''
am = [4,6,2,8,16,9]
l = am
st = deepcopy(am)
print('Before : ',am)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            t = l[i]
            l[i] = l[j]
            l[j] = t
        elif st[i] < st[j]:
            t = st[i]
            st[i] = st[j]
            st[j] = t
            
print('In ascending order ',l)
print('In descending order ',st)

'''for i in range(0,len(st)):
    for j in range(i+1,len(st)):
        if st[i] < st[j]:
            t = st[i]
            st[i] = st[j]
            st[j] = t'''
 
