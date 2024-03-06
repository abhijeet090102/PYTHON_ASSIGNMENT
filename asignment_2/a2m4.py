#  According to the Gregorian calendar, it was Monday on the date 01/01/1900. If any year is input through the keyboard write a program to find out what is the day on 1 st January of this year.
base_year = 1900
year = int(input("enter a year"))
entry_year = year
year = (year-1)-base_year
leap = year//4
remaining = year-leap
total_day = (remaining*365)+(leap*366)+1
day = total_day % 7
print(day)
if(day ==0):
    print("It will be monday on 01/01/",entry_year)
elif(day==1):
    print("It will be tuesday on 01/01/", entry_year)
elif(day==2):
    print("It will be wednesday on 01/01/",entry_year)
elif(day==3):
    print("It will be thursday on 01/01/", entry_year)
elif(day==4):
    print("It will be friday on 01/01/",entry_year)
elif(day==5):
    print("It will be saturday on 01/01/",entry_year)
elif(day==6):
    print("It will be sunday on 01/01/",entry_year)
else:
    print("wrong entry")
