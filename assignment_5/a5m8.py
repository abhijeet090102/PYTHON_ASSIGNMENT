'''Python program to check if a string has at least one letter and one number'''
am = 'amst1'
al_digi = False
for i in range(len(am)):
    
    if am.isalnum():
        al_digi= True
print(al_digi)

'''digit_co =False
alpha_co = False
for i in range(len(am)):
    if am.isdigit():
        digit_co = True
    if am.isalpha():
        alpha_co = True'''
#print(digit_co)
#print(alpha_co)
