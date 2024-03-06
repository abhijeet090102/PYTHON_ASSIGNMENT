'''. Write a program to enter the numbers till the user wants and at the end it should display the
count of positive, negative and zeros entered'''
ren = int(input("Enter any range"))
num = []
neg = 0
pos = 0 
zer = 0
for i in range(ren):
    num.insert(i,int(input("enter numbers ")))
for i in range(ren):
    if num[i] > 0:
        pos += 1
    elif num[i] < 0:
        neg = neg+1
    else:
        zer += 1
print("Negative values are ",neg)
print("Positive values are ",pos)
print("Zero values are ",zer)
