''' Program to print all numbers which are divisible by M and N in the List.'''
l = [24,46,25,68,95,64,42,56,47,12,69,15,13,16,9,25]
M = int(input('Enter first divisior no :'))
A = int(input('Enter second divisior no :'))

for i in l:
    if i%M == 0 and i%A ==0:
        print(f'Divisible by {M}&{A} :',i)
    '''else:
        print(f'Does not divisible by {M}& {A} :',i)'''
        
