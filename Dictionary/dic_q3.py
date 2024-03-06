'''Write a Python script to concatenate the following dictionaries to create
a new one.
Sample Dictionary :'''
dic1={1:10, 2:20,4:6}
dic2={3:30, 4:40,5:2}
dic3={5:50,6:60}
d = {}
for i in dic1:
    d[i] = dic1[i]
for j in dic2:
    if j in d:
        d[j] += dic2[j]
    else:
        d[j] = dic2[j]
for k in dic3:
    if k in d:
        d[k] += dic3[k]
    else:
        d[k] = dic3[k]
print(d)
