# If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred.
cost_price = input("Enter cost of an item: ")
selling_price = input("Enter selling price of an item: ")
am = float(selling_price)-float(cost_price)
if (am>0):
    print("Seller made profit")
    print("Profit is :",am)
else:
    print("Seller made incurred loss")
    print("loss is :",am)