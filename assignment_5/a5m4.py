''' WAP to print even length words in a string.'''
am = input('Enter any string ')
st = am.split(" ")
for i in st:
    if len(i)%2 ==0:
        print(i)

# print(st)
