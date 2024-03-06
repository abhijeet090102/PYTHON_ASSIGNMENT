'''Program to Print the index of first matched element of a list.'''
l = [2,8,4,6,8,16,9]
am = 0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            am = i
print(am)
