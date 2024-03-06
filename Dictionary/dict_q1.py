'''Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary:'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d = {}
a = dic1.keys()
m = dic2.keys()
for i in a:
    d[i] = dic1[i]
print(d)
for j in m:
    d[j] = dic2[j]
print(d)
for k in dic3:
    d[k] = dic3[k]
print(d)

