'''Program to find the position of minimum and maximum elements of a list.'''
l = [4,9,8,7,6,2]
min_ele = l[0]
max_ele = l[0]
for i in range(1,len(l)):
    if l[i] > max_ele:
        max_ele = l[i]
    elif l[i] < min_ele:
        min_ele = l[i]
print('minimum element ',min_ele)
print('maximum element',max_ele)
