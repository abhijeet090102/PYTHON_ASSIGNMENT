'''Write a program in C to check if a given number is even or odd using the function. '''
def main(am):
    if am %2==0:
        print("Even number")
    else:
        print("odd number")
st = int(input("Enter any number "))
if __name__ == '__main__':
    main(st)
