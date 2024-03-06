''' Write a program to capitalize the first and last character of each word in a string
'''
def word_both_car(str1):
    '''st = am.title().split()
    print(st)
    return ' '.join(map(lambda am:am[:-1] +am[-1].upper(),st))'''
    words = str1.split()
    result = []
    for i in words:
        if len(i) >1:
            n_word = i[0].upper()+i[1:-1] + i[-1].upper()
        else:
            n_word = i.upper()
        result.append(n_word)
    return ' '.join(result)
    #return result this will return as a list 
am = input("Enter any string ")
ma = word_both_car(am)
print(ma)
