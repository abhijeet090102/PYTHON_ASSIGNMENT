'''Write a program to least Frequent Character in String'''
am = 'ABHIJEET'
st = {}
print(min(am))

for i in am:
    if i in st:
        st[i] +=1
    else:
        st[i] = 1
print(st)
lest = min(st,key=st.get)
print('Least frequent character is : ',lest)
