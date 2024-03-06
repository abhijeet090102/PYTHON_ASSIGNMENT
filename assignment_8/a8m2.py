'''Write a Python script to check whether a given key already exists in a dictionary. '''
dic = {}
am = {2:32,4:46,6:20,8:24}
st = {2:45,4:46,9:16,16:9}
for i in am:
   dic[i] = am[i]
for i in st:
    if i in dic:
        print('given key is already exists ',i)
    else:
        dic[i] = st[i]
print('New dict ',dic)
