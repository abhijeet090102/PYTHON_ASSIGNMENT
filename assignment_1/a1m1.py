#  Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
# salary, and house rent allowance is 20% of basic salary. Write a program to calculate his
# gross salary.
ramesh = int (input('Enter the basic sallary'))
a = ramesh*0.40
rent = ramesh*0.20
gross = ramesh+a+rent
print('gross salary is ',gross)