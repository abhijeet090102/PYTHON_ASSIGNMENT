'''Write a Python function to check whether a number is perfect or not.'''
def perfect(nu):
    div= 0
    for i in range(1,nu):
        if nu%i ==0:
            div +=i

    return div == nu
print('No is perfect : ',perfect(6))
