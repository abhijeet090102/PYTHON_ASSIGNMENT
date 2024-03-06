'''Write a Python program to print a dictionary in table format'''
'''am = {1:['abhijeet', 22],2:['manisha',24],3:['megha',24],4:['ranjay',30]}
print(len(am))
print('{:<10} {:<10}'.format('name ','age'))
for i,j in am.items():
    name,age = j
    print('{:<10} {:<10}'.format(name,age))'''

am = {22:'abhijeet',18:'manisha',23:'megha',30:'ranjay'}
print( 'age ','name ')
for i,j in (am.items()):
        print(i,j)
                
