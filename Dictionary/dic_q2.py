'''Write a Python script to check whether a given key already exists in a
dictionary.'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,4:60}
d = {}
for i in dic1:
    d[i] = dic1[i]
for j in dic2:
    d[j] = dic2[j]
for k in dic3:
    if k in d:
        d[k] += dic3[k]
    else:
        d[k] = dic3[k]
print(d)
