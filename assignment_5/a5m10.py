'''Write a program to count the Number of matching characters in a pair of string .'''
am = 'ABHIJEET'
st = 'MANISHA'
char_count = {}
for i in am:
    if i in char_count:
        char_count[i] += 1
        print(char_count)
    else :
        char_count[i] = 1
counter = 0
for j in st:
    if j in char_count and char_count[j] > 0:
        counter += 1
        char_count[j] -= 1
print('No. of matching char are :',counter)

