'''Program to find the differences of two lists.'''
l = [4,6,8,6,2,5,3,9,16]
am= [6,2,4]
st = []
for i in l:
    if i not in am:
        st.append(i)
print('difference of two list :',st)
