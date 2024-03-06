'''Write a program to maximum frequency character in String'''
am = 'ABHIJEET'
st = {}
print(max(am))
for i in am:
    if i in st:
        st[i] +=1
    else:
        st[i] = 1
print(st)
max1 = max(st,key=st.get)
print('MAx frequent character is : ',max1)
