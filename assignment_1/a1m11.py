#  A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
wid_amount = int(input("enter the withdraw amount:"))
a = wid_amount//100
wid_amount = wid_amount%100
m = wid_amount//50
wid_amount = wid_amount%50
st = wid_amount//10
wid_amount = wid_amount%10
print('currency of 100 :',a)
print('currency of 50 :',m)
print('currency of 10 :',st)