'''Convert a string to integers list.'''
am = []
for j in range(0,6):
    am.append(input('Enter any 5 no '))
l = [int(i) for i in am]
print(am,'string list')
print('List:',l)
