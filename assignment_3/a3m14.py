''' A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The
machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12
percent per annum can be earned on alternate investments what would be the minimum life of
the machine to make it a more attractive investment compared to alternative investment?
'''
year = 0
cost = 6000
am_earn = 1000
salvage = 2000
interast = 0.12
altr = 1
invest = 0
while (altr > invest):
    year +=1
    altr = (1000*0.12)*year
    invest = 1000*year-(6000-2000)
print("The life of the mechine " , year)
