'''Write a program to remove all duplicates from a given string in Python, keeping the 
first character only'''
am = "Abhijeet"
st = ""
for i in am:
    if i not in st:
        st = st+i
print(st)
k = list('Abhijeet')
print(k)
