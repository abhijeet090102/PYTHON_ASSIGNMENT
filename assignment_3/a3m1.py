''' Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs.
12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for
fractional part of an hour.'''
ot = 0
emp = 1
''' how many times loop will executed or no of employee each how much money recived each person'''
while emp<=10:
    hour = int(input("Enter hour "))
    if(hour>40):
        '''calculating overtime '''
        ot = (hour -40)*12
        print("Employee worked ",emp,"total hours",hour)
        print("Overtime pay is Rs. ",ot)
    else:
        print("No of hour worked ",hour,"which is less than 40 hours so no over time pay for employee",emp)
    emp = emp+1
