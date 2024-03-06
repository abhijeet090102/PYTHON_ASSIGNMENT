'''. Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y'''
am = {'abhi':1,'manisha':2,'megha':3,'ranjay':4}
st = {'abhi':1,'manisha':2}
am_v = am.keys()
st_v = st.keys()
'''for i in am_v:
    for j in st_v:
        if i == j:
            print(i,' is present both am and st dictionary')'''
for (i,j) in set(am.items() and st.items()):
    print(i,j,'is present ')

