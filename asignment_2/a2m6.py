#  If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three.
age_ram = int ( input("Eneter the age of ram"))
age_shyam = int ( input("Enter the age of shyam"))
age_ajay = int ( input("Enter the age of ajay"))
if (age_ram>age_shyam and age_ram>age_ajay):
    print("Ram is youngest")
elif(age_shyam>age_ram and age_shyam>age_ajay):
    print("Shyam is youngest")
else:
    print("Ajay is youngest")