'''Input comma separated elements, convert into list and print.'''

st = input('Enter the numbers using commas: ').split(',')
#st = st.split(',')
print('string list',st)
l = [int(i) for i in st]
print('list: ',l)
