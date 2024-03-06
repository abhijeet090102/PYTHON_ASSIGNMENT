'''Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic = {}
am = {2:32,4:46,6:20,8:24}
st = {4:45,8:46,9:16,16:9}
for i in am:
   dic[i] = am[i]
for i in st:
    '''if i in dic:
        dic[i] = dic[i]+ st[i]
    else:'''
    dic[i] = st[i]
print('New dict ',dic)
