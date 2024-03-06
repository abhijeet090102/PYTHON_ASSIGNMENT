''' Write a program to accept the strings which contain all vowels
'''
def vowel(am):
    am = am.lower()
    st = set('aeiou')
    ma = set({})
    for char in am :
        if char in st:
            ma.add(char)
        else:
            pass
    if len(ma) == len(st):
        print('Accepted')
    else:
        print('Not Accepted')

am = input('Enter any string')
vowel(am)
