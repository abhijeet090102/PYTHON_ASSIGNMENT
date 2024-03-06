import math
''' Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and
continue)'''
for num in range(0,301):
    if num>1 :
        am = int(math.sqrt(num))
        for i in range(2,am+1):
        #for i in range(2,int(num**0.5)+1):
            if (num%i)==0:
                break
        else:
            print(num)
