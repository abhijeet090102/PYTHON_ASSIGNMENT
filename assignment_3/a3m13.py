'''Write a program to generate all combinations of 1, 2 and 3 using for loop.'''
am = [1,2,3]
st = len(am)
for i in range(st):
    for j in range(st):
        for k in range(st):
            if(i!=j and i!=k and j!=k):
                print(am[i],am[j],am[k])
    
