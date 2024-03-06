'''Write a program to odd Frequency Characters'''
ma = 'ABHIJEET'
am = (ma)
st = {}
print(am,st)
for i in am:
    if i in st:
        st[i] += 1
    else:
        st[i] = 1
for i,freq in st.items():
    if freq%2 !=0:
        print(f'{i} appear {freq} odd times')
    else:
        print(f'{i} appear {freq} times ')
print(st)
