'''. Write a Python program to get the top three items in terms of cost in a shop.
d1={'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}
output:
bungle 55
pant 45
dress 23'''
dl={'dress':54,'pant':40,'shoe':19,'bungle':12,'book':68}
value = sorted( dl.values(),reverse = True)
value = value[:3]
print('Item ' , 'Value/Price')
for j in value:
    for i in dl.keys():
        if dl[i] == j:
            print(i,' ',j)
