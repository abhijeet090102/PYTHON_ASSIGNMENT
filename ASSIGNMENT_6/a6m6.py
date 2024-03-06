''' Program to remove first occurrence of a given element in the list.'''
l = [2,3,4,6,8,6,9]
'''for i in range(len(l)):
    if l[i] == 2:
        l.pop(i)
        break
print(l)'''
am =0
for i in range(0,len(l)):
    for j in range (i+1,len(l)):
        if l[i] == l[j]:
            #l.pop(j)
            am = i
            print(j)
l.pop(am)
print(l)
