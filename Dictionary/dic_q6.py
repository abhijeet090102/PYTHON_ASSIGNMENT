'''Write a Python program to get the maximum and minimum values of a dictionary.'''
d = {1: 10, 2: 20, 3: 36, 4: 40, 5: 52, 6: 60}
am = d.keys()
st = d.values()
max1 = am[0]
min1 = am[0]
for i in am[1: ]:
    if d[i] > d[max1]:
        max1 = i
for j in am[1: ]:
    if d[j] < d[min1]:
        min1 = j
print('Max value of dictionary ',max1)
print('Minimum value of dictionary ',min1)
