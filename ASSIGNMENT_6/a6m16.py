'''Program to Create two lists with EVEN numbers and ODD numbers from a list.'''
l = [4,5,6,7,8,9,7,3]
even = []
odd = []
for i in l:
#range(0,len(l)):  does not work because --odd.append(l(i))TypeError: 'list' object is not callable 
    if i%2 ==0:
        even.append(i)
    elif i % 2 !=0:
        odd.append(i)
print('even list:',even)
print('Odd list:',odd)
