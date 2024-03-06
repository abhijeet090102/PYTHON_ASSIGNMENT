'''Write a program in C to calculate l.c.m using while loop.'''
def lcm(am,st):
    if am > st:
        greater = am
    else :
        greater = st
    while True:
        if greater % am ==0 and greater % st ==0:
            lcm1 = greater
            break
        greater +=1
    return lcm1
am = int(input('Enter first no =>'))
st = int(input('Enter second no => '))
print(f'The L.C.M of {am} and {st} is ',lcm(am,st))
