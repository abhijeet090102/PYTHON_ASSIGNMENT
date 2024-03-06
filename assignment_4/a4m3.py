'''Write a program in C to calculate sum of Fibonacci series.'''
def main(am):
    a = 0
    m = 1
    st = 0
    for i in range(am):
        st += a
        #m = m
        a = a+m
        print(st)
    return st
am = 6
if __name__ == '__main__':
    m = main(am)
print(m)
