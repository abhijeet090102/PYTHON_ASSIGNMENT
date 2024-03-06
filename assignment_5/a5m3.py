'''WAP to remove i^th character of a string.'''
am = input("Enter any string value ")
for i in range(len(am)):
    if i == 6:
        am = am.replace(am[6],"",1)
print(am)
    
