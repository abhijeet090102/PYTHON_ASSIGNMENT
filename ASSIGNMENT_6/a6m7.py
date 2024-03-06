'''Remove all occurrences a given element from the list.'''

l = [6,2,4,6,16,9]
am =[]
print(l)
st = int(input('Enter the element you want to remove '))
for i in l:
    if i != st:
       am.append(i) 
#l.pop(am)
print(am)
