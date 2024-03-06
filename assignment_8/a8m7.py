'''Write a Python program to get the maximum and minimum values of a dictionary.'''
am = {4: 2, 3: 4, 5: 80, 9: 16,1: 45, 2: 65, 6: 89}
ma = am.values()
ma_x = ma_in = am[4]
for i in am.values():
    if i > ma_x:
        ma_x = i
    elif i < ma_in:
        ma_in = i
print('Maximum value ',ma_x)
print('Minimum value ',ma_in)
