# . The distance between two cities (in km.) is input through the keyboard. Write a program to
# convert and print this distance in meters, feet, inches and centimeters.
city = int (input('Enter distance between two cities(in km)'))
m = city*1000
centi = city*1000*100
feet =  city*3280.84
inch = city*39370.07
print('distance between two cities in meter :',m)
print('distance between two cities in centimeter :',centi)
print('distance between two cities in feet :',feet)
print('distance between two cities in inch :',inch)