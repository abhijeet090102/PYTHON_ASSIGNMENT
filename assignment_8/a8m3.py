'''Write a Python script to concatenate the following dictionaries to create a
new one.
Sample Dictionary :
dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 36, 4: 40, 5: 52, 6: 60}'''
dic = {}
ma = {2:6,6:45,7:89,5:64}
st = {2:4,7:3,4:65,3:56}
for i in ma:
    dic[i] = ma[i]
for j in st:
    if j in dic:
        dic[j] = dic[j]+st[j]
    else:
        dic[j] = st[j]
print('After concatenate ',dic)
