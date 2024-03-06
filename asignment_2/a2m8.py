#  Find the absolute value of a number entered through the keyboard
am = int (input("Enter a number "))
if(am<0):
    am = am*(-1)
    print("Absolute value is ",am)
else:
    print("Alrady a absolute value ")