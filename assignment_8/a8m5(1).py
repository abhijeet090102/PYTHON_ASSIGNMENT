''' Write a Python script to merge two Python dictionaries.'''
ma = {}
am = {4:2,3:4,5:80,9:16,1:'abhi',2:'ma'}
st = {0:40,6:20}

for i in am:
    ma[i] = am[i]
for j in st:
    if j in ma:
        ma[j] = ma[j] + st[j]
    else:
        ma[j] = st[j]
print('Dictionary ',ma)
