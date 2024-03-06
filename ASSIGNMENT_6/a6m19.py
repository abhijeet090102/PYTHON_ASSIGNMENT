''' Create a list from the specified start to end index of another list.'''
l = [56,48,64,42,60,78,98,25,45,65,64,84]
n_l = []
st = int(input('Enter starting index no '))
en = int(input('Enter last index no '))
for i in range(st,en):
    print(l[i])
    n_l.append(l[i])
print(f'New list from {st} to {en} index values :', n_l)
