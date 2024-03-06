''' Write a Python program to filter a dictionary based on values.
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}'''

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165,
     'Pierre Cox': 190}
d_v = {i:j for i,j in d.items() if j>170}
print(d_v)
