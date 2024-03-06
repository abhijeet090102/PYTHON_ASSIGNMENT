'''Program to remove duplicate elements from the list.'''
def remove(duplicate):
    final = []
    for i in duplicate:
        if i not in final:
            final.append(i)
    return final

l= [56,48,64,84,68,25,45,65,64,84]
print('List of duplicate elements',l)
print('Non duplicate Elements :',remove(l))
