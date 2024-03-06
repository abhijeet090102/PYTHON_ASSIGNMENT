#  Given a point (x, y), write a program to find out if it lies on the x-axis, y-axis or at the origin, viz. (0, 0).
x = int(input("Enter the x-axis value : "))
y = int(input("Enter the y-axis value : "))
if(x == 0 and y !=0):
    print("point",x,y, " lies on y - axis")
elif(x !=0 and y ==0 ):
    print("Point",x,y, "lies on x-axis")
elif(x==0 and y==0):
    print("Point",x,y,"lies on origin")
else:
    print("Point",x,y,"neither lies on x-axis nor y-axis")