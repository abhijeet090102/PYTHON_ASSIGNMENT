'''Write a program in C to check whether an inputted number is palindrome.'''
def palin():
    num = int(input('Enter any no :'))
    temp = num
    sum1 = 0
    while num>0:
        re = num%10 # getting reminder
        sum1= (sum1*10)+re
        num = num//10
    if temp == sum1:
        print('Number is palindrome ',sum1)
    else:
        print('Number is not a palindrome ',sum1)
palin()
