''' Write a program in C to print sum of all +ve numbers and all -ve numbers.'''
def main(ma):
    po = 0
    ne = 0
    for i in range(len(ma)):
        if ma[i]>0:
            po += int(ma[i])
        elif ma[i]<0:
            ne += int(ma[i])
    print('positive number sum',po)
    print('negative number sum ',ne)
#am = int(input('Enter how many times you want to enter numbers: '))
ma = [4,-6,5,6,8,-8]
main(ma)
