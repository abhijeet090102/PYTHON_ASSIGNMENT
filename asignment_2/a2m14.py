'''A library charges a fine for every book returned late. For first 5 days the
fine is 50 paise, for 6-10 days fine is one rupee and above 10 days fine is 5
rupees. If you return the book after 30 days your membership will be cancelled.
Write a program to accept the number of days the member is late to return the
book and display the fine or the appropriate message.'''

no_of_days = int(input("Enter the no of days"))
fine = 0
if(0<no_of_days <=5):
    fine = 0.50*no_of_days
elif(6<= no_of_days<=10):
    fine = 1*no_of_days
elif(10<no_of_days<=30):
    fine = 5*no_of_days
if(30<no_of_days):
    print("Your membership will cancelled")

print(f'Your fine is {fine} Rs.')
