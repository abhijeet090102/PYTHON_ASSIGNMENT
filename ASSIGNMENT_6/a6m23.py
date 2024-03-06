'''Create two lists with first half and second half elements of a list.'''
l = [98, 86, 64, 61, 95, 57, 75, 73, 79, 45, 46, 23, 68, 58, 45,67]
print(len(l))
first = [l[i] for i in range(0,len(l)//2)]
print('first half:',first)
second =[l[i] for i in range(len(l)//2 ,len(l))]
print('second half:',second)
