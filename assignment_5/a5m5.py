'''WAP to calculate the length of a string, avoid space.'''
am = input('Enter any string')
count = 0
for i in am:
    if i == ' ':
        continue
    count += 1
print('The characters length without spaces : ',count)
