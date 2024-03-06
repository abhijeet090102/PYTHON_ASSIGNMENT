''' Write a Python program to convert more than one list to a nested dictionary.
Original strings:'''
l = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]
d =[{i:{j:k}} for (i,j,k) in (zip(l,l2,l3))]
print(d)

''' this will give me one keys to to many values so this is not the best methode
for i in range(len(l)):
    for j in range(len(l2)):
        for k in range(len(l3)):
            print({l[i]:{l2[j]:l3[k]}})'''
        
